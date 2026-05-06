#!/usr/bin/env python3
"""Audit open-source code links for the 3D/4D reconstruction paper corpus.

The script is intentionally conservative: it does not call a paper "fake" just
because code is missing. It records observable evidence about code availability,
repository relevance, and implementation substance so that the final label is
auditable.
"""

from __future__ import annotations

import argparse
import csv
import html
import json
import os
import re
import shutil
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Iterable


ROOT = Path("/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2")
CORPUS = ROOT / "paper_collection_3d4d_reconstruction_2026_04_26"
MANIFEST = CORPUS / "metadata" / "papers_manifest.json"
AUDIT_DIR = CORPUS / "code_audit"
CACHE_DIR = AUDIT_DIR / "cache"
HTML_CACHE = CACHE_DIR / "html"
GITHUB_CACHE = CACHE_DIR / "github"
REPO_CACHE = AUDIT_DIR / "repos"

USER_AGENT = "Codex 3D/4D reconstruction code audit (local research workflow)"

URL_RE = re.compile(r"https?://[^\s<>{}\"']+", re.IGNORECASE)
URI_RE = re.compile(r"/URI\s*\((.*?)\)", re.IGNORECASE | re.DOTALL)
HREF_RE = re.compile(r"""href=["']([^"']+)["']""", re.IGNORECASE)
GITHUB_RE = re.compile(r"^https?://(?:www\.)?github\.com/([^/\s?#]+)/([^/\s?#]+)", re.IGNORECASE)

CODE_EXTS = {
    ".py", ".ipynb", ".cpp", ".cc", ".cxx", ".c", ".cu", ".h", ".hpp",
    ".m", ".mm", ".swift", ".rs", ".go", ".java", ".kt", ".js", ".jsx",
    ".ts", ".tsx", ".sh", ".bash", ".zsh", ".ps1", ".cmake", ".glsl",
    ".yaml", ".yml", ".toml", ".json",
}
ENTRY_HINTS = (
    "train", "eval", "test", "infer", "demo", "render", "reconstruct",
    "reconstruction", "optimize", "pipeline", "run", "launch", "scripts/",
)
DEP_REPOS = {
    "pytorch", "tensorflow", "jax", "opencv", "colmap", "gtsam", "ceres-solver",
    "diffusers", "transformers", "nerfstudio", "gaussian-splatting",
    "gsplat", "open3d", "mmdetection3d", "instant-ngp",
}
NON_CODE_HOSTS = (
    "arxiv.org", "doi.org", "youtube.com", "youtu.be", "twitter.com",
    "x.com", "linkedin.com", "creativecommons.org", "openaccess.thecvf.com",
    "ieeexplore.ieee.org", "dl.acm.org", "springer.com", "wiley.com",
    "scite.ai", "txyz.ai", "catalyzex.com", "code.jquery.com",
    "static.arxiv.org",
)


@dataclass
class Candidate:
    kind: str
    url: str
    repo: str | None = None
    source: str = ""
    score: int = 0
    reason: str = ""
    context: str = ""


@dataclass
class RepoAudit:
    repo: str
    url: str
    exists: bool = False
    cloned: bool = False
    default_branch: str | None = None
    total_files: int = 0
    code_files: int = 0
    has_readme: bool = False
    has_license: bool = False
    has_env_file: bool = False
    has_entrypoint: bool = False
    root_files_sample: list[str] = field(default_factory=list)
    code_files_sample: list[str] = field(default_factory=list)
    error: str | None = None
    verdict: str = "not_checked"


@dataclass
class PaperAudit:
    arxiv_id: str
    title: str
    source_group: str
    tags: list[str]
    pdf_path: str
    candidates: list[Candidate] = field(default_factory=list)
    best_repo: RepoAudit | None = None
    verdict: str = "not_checked"
    evidence: str = ""


def slug(text: str, max_len: int = 160) -> str:
    text = re.sub(r"[^A-Za-z0-9._-]+", "_", text).strip("_")
    return text[:max_len] or "item"


def request(url: str, timeout: int = 30) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read()


def normalize_url(url: str) -> str:
    url = html.unescape(url).replace(r"\)", ")").replace(r"\(", "(").replace("\\/", "/")
    url = url.strip().strip(" \t\r\n\"'<>")
    while url and url[-1] in ".,;:])}":
        # Keep the common .git suffix intact.
        if url.lower().endswith(".git"):
            break
        url = url[:-1]
    return url


def extract_urls_from_pdf(path: str) -> list[tuple[str, str]]:
    if not path or not Path(path).exists():
        return []
    data = Path(path).read_bytes()
    text = data.decode("latin-1", "ignore")
    urls: list[tuple[str, str]] = []
    for match in URL_RE.finditer(text):
        url = normalize_url(match.group(0))
        start = max(0, match.start() - 160)
        end = min(len(text), match.end() + 160)
        urls.append((url, text[start:end].replace("\n", " ")))
    for match in URI_RE.finditer(text):
        url = normalize_url(match.group(1))
        if url.startswith("http"):
            start = max(0, match.start() - 160)
            end = min(len(text), match.end() + 160)
            urls.append((url, text[start:end].replace("\n", " ")))
    seen = set()
    unique = []
    for url, ctx in urls:
        if url not in seen:
            seen.add(url)
            unique.append((url, ctx[:320]))
    return unique


def cached_html(url: str, cache_name: str, sleep: float) -> str:
    HTML_CACHE.mkdir(parents=True, exist_ok=True)
    path = HTML_CACHE / f"{slug(cache_name)}.html"
    if path.exists():
        return path.read_text(encoding="utf-8", errors="ignore")
    try:
        data = request(url, timeout=30)
        text = data.decode("utf-8", "ignore")
    except Exception as exc:
        text = f"<!-- fetch failed: {exc} -->"
    path.write_text(text, encoding="utf-8")
    time.sleep(sleep)
    return text


def extract_links_from_abs(arxiv_id: str, sleep: float) -> list[tuple[str, str]]:
    url = f"https://arxiv.org/abs/{arxiv_id}"
    text = cached_html(url, f"arxiv_abs_{arxiv_id}", sleep)
    links = []
    for href in HREF_RE.findall(text):
        full = urllib.parse.urljoin(url, html.unescape(href))
        if full.startswith("http"):
            links.append((normalize_url(full), "arxiv_abs_html"))
    return links


def should_probe_project_page(url: str) -> bool:
    host = urllib.parse.urlparse(url).netloc.lower().removeprefix("www.")
    if not host or any(host.endswith(h) for h in NON_CODE_HOSTS):
        return False
    return (
        "github.io" in host
        or host.endswith(".io")
        or host.endswith(".ai")
        or "project" in url.lower()
        or "code" in url.lower()
    )


def extract_github_from_project_page(url: str, paper_id: str, idx: int, sleep: float) -> list[tuple[str, str]]:
    text = cached_html(url, f"project_{paper_id}_{idx}_{slug(url, 80)}", sleep)
    out = []
    for href in HREF_RE.findall(text):
        full = normalize_url(urllib.parse.urljoin(url, html.unescape(href)))
        if "github.com" in full.lower():
            out.append((full, f"project_page:{url}"))
    for match in URL_RE.finditer(text):
        full = normalize_url(match.group(0))
        if "github.com" in full.lower():
            out.append((full, f"project_page_text:{url}"))
    return out


def github_repo(url: str) -> str | None:
    parsed = urllib.parse.urlparse(url)
    if parsed.netloc.lower() not in {"github.com", "www.github.com"}:
        return None
    parts = [p for p in parsed.path.split("/") if p]
    if len(parts) < 2:
        return None
    owner, repo = parts[0], parts[1]
    if owner.lower() in {"topics", "collections", "marketplace", "features", "about"}:
        return None
    repo = repo[:-4] if repo.lower().endswith(".git") else repo
    if not owner or not repo:
        return None
    return f"{owner}/{repo}"


def title_tokens(title: str) -> set[str]:
    stop = {
        "the", "and", "for", "with", "from", "using", "via", "towards", "toward",
        "real", "time", "neural", "learning", "scene", "scenes", "field", "fields",
        "representation", "representing", "rendering", "synthesis", "view", "views",
        "image", "images", "video", "dynamic", "dynamics", "reconstruction",
        "reconstructing", "model", "models", "modeling",
    }
    return {t.lower() for t in re.findall(r"[A-Za-z0-9]+", title) if len(t) >= 3 and t.lower() not in stop}


def acronym(title: str) -> str:
    words = re.findall(r"[A-Za-z0-9]+", title)
    caps = "".join(w[0] for w in words if w and w[0].isupper())
    return caps.lower()


def title_code_names(title: str) -> list[str]:
    names: list[str] = []
    first = title.split(":", 1)[0].strip()
    if first and len(first) <= 48:
        names.append(first)
    for match in re.findall(r"\b[A-Za-z]*[A-Z][A-Za-z]*[-_]?[A-Z0-9][A-Za-z0-9-]*\b", title):
        if len(match) >= 3:
            names.append(match)
    seen = set()
    out = []
    for name in names:
        key = re.sub(r"[^a-z0-9]+", "", name.lower())
        if key and key not in seen:
            seen.add(key)
            out.append(name)
    return out


def score_candidate(url: str, source: str, context: str, title: str) -> Candidate | None:
    repo = github_repo(url)
    kind = "github_repo" if repo else "project_or_code_page"
    lower = f"{url} {source} {context}".lower()
    score = 0
    reasons = []
    if repo:
        owner, name = repo.split("/", 1)
        repo_bits = set(re.findall(r"[a-z0-9]+", name.lower()))
        overlap = repo_bits & title_tokens(title)
        substring_overlap = {
            tok for tok in title_tokens(title)
            if len(tok) >= 4 and tok in name.lower().replace("-", "").replace("_", "")
        }
        acro = acronym(title)
        if overlap:
            score += 3
            reasons.append(f"title-token-overlap:{','.join(sorted(overlap)[:5])}")
        if substring_overlap:
            score += 3
            reasons.append(f"title-substring-overlap:{','.join(sorted(substring_overlap)[:5])}")
        if acro and len(acro) >= 3 and acro in name.lower().replace("-", "").replace("_", ""):
            score += 4
            reasons.append(f"title-acronym:{acro}")
        if name.lower() in DEP_REPOS or owner.lower() in DEP_REPOS:
            score -= 4
            reasons.append("known-dependency-repo")
        score += 2
        reasons.append("github")
    if any(k in lower for k in ["code", "source", "implementation", "project page", "available at", "our project", "our repo"]):
        score += 2
        reasons.append("code-context")
    if source.startswith("github_search"):
        score += 1
        reasons.append("github-search")
    if source.startswith("project_page"):
        score += 1
        reasons.append("from-project-page")
    if "arxiv_abs_html" in source:
        score += 1
        reasons.append("from-arxiv-page")
    if not repo and should_probe_project_page(url):
        score += 1
        reasons.append("probable-project-page")
    if repo or score > 1:
        return Candidate(kind=kind, url=url, repo=repo, source=source, score=score, reason=";".join(reasons), context=context[:240])
    return None


def paper_candidates(paper: dict, sleep: float, probe_pages: bool) -> list[Candidate]:
    raw: list[tuple[str, str, str]] = []
    for url, ctx in extract_urls_from_pdf(paper.get("pdf_path") or ""):
        raw.append((url, "pdf_uri", ctx))
    for url, ctx in extract_links_from_abs(paper["arxiv_id"], sleep):
        # arXiv's abs pages include third-party discovery widgets (scite, TXYZ,
        # CatalyzeX). Treat only direct GitHub links as paper-owned evidence;
        # project pages should come from the PDF itself.
        if github_repo(url):
            raw.append((url, ctx, ""))
    if probe_pages:
        project_urls = []
        for url, source, _ctx in raw:
            if source == "pdf_uri" and should_probe_project_page(url) and "github.com" not in url.lower():
                project_urls.append((url, source))
        for idx, (url, _source) in enumerate(project_urls[:8]):
            for gh, source in extract_github_from_project_page(url, paper["arxiv_id"], idx, sleep):
                raw.append((gh, source, ""))
    candidates: list[Candidate] = []
    seen = set()
    for url, source, ctx in raw:
        cand = score_candidate(url, source, ctx, paper["title"])
        if not cand:
            continue
        key = cand.repo or cand.url
        if key in seen:
            continue
        seen.add(key)
        candidates.append(cand)
    candidates.sort(key=lambda c: (c.score, bool(c.repo)), reverse=True)
    return candidates


def cached_github_json(url: str, cache_name: str, sleep: float) -> dict:
    GITHUB_CACHE.mkdir(parents=True, exist_ok=True)
    path = GITHUB_CACHE / f"{slug(cache_name)}.json"
    if path.exists():
        return json.loads(path.read_text(encoding="utf-8"))
    try:
        data = request(url, timeout=30)
        obj = json.loads(data.decode("utf-8", "ignore"))
    except Exception as exc:
        obj = {"error": str(exc), "items": []}
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding="utf-8")
    time.sleep(sleep)
    return obj


def github_search_candidates(paper: dict, sleep: float) -> list[Candidate]:
    # Search is a fallback. It can find official repos that are not linked from
    # old PDFs, but it is weaker evidence than a paper/project-page link.
    tokens = sorted(title_tokens(paper["title"]))
    acro = acronym(paper["title"])
    queries = title_code_names(paper["title"])
    if acro and len(acro) >= 3:
        queries.append(acro)
    if tokens:
        queries.append(" ".join(tokens[:5]))
    queries.append(paper["title"][:120])
    candidates: list[Candidate] = []
    seen = set()
    for q in queries[:5]:
        url = "https://api.github.com/search/repositories?" + urllib.parse.urlencode({"q": q, "per_page": "10"})
        obj = cached_github_json(url, f"search_{paper['arxiv_id']}_{q}", sleep)
        for item in obj.get("items", [])[:10]:
            repo = item.get("full_name")
            html_url = item.get("html_url")
            if not repo or not html_url or repo in seen:
                continue
            seen.add(repo)
            desc = item.get("description") or ""
            cand = score_candidate(html_url, f"github_search:{q}", desc, paper["title"])
            if not cand:
                continue
            stars = int(item.get("stargazers_count") or 0)
            repo_name_norm = re.sub(r"[^a-z0-9]+", "", repo.split("/", 1)[1].lower())
            q_norm = re.sub(r"[^a-z0-9]+", "", q.lower())
            if q_norm and (repo_name_norm == q_norm or q_norm in repo_name_norm):
                cand.score += 4
                cand.reason += ";query-name-match"
            if stars >= 500:
                cand.score += 2
                cand.reason += ";stars>=500"
            elif stars >= 50:
                cand.score += 1
                cand.reason += ";stars>=50"
            if re.search(r"\bofficial\b", desc, re.I):
                cand.score += 4
                cand.reason += ";official-description"
            cand.context = f"stars={stars}; description={desc}"[:240]
            # Penalize obvious third-party reimplementations when the repo name
            # itself is not an exact/acronym match.
            if re.search(r"\b(unofficial|re-?implementation|implementation of|copy of)\b", desc, re.I):
                cand.score -= 2
                cand.reason += ";possible-third-party"
            candidates.append(cand)
    candidates.sort(key=lambda c: (c.score, bool(c.repo)), reverse=True)
    return candidates


def run(cmd: list[str], cwd: Path | None = None, timeout: int = 120) -> tuple[int, str]:
    try:
        proc = subprocess.run(
            cmd,
            cwd=str(cwd) if cwd else None,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            timeout=timeout,
        )
        return proc.returncode, proc.stdout
    except subprocess.TimeoutExpired as exc:
        return 124, (exc.stdout or "") + f"\nTIMEOUT: {' '.join(cmd)}"


def clone_or_update(repo: str, sleep: float) -> tuple[Path | None, str | None]:
    REPO_CACHE.mkdir(parents=True, exist_ok=True)
    dest = REPO_CACHE / repo.replace("/", "__")
    url = f"https://github.com/{repo}.git"
    if (dest / ".git").exists():
        code, out = run(["git", "fetch", "--depth", "1", "origin"], cwd=dest, timeout=120)
        if code != 0:
            return dest, out[-1000:]
        return dest, None
    code, out = run(["git", "clone", "--depth", "1", "--filter=blob:none", "--no-checkout", url, str(dest)], timeout=180)
    time.sleep(sleep)
    if code != 0:
        shutil.rmtree(dest, ignore_errors=True)
        return None, out[-1000:]
    return dest, None


def audit_repo(repo: str, sleep: float) -> RepoAudit:
    audit = RepoAudit(repo=repo, url=f"https://github.com/{repo}")
    repo_path, err = clone_or_update(repo, sleep)
    if err or not repo_path:
        audit.error = err or "clone failed"
        audit.verdict = "repo_unavailable_or_clone_failed"
        return audit
    audit.exists = True
    audit.cloned = True
    code, branch_out = run(["git", "branch", "--show-current"], cwd=repo_path, timeout=30)
    audit.default_branch = branch_out.strip() if code == 0 else None
    code, tree_out = run(["git", "ls-tree", "-r", "--name-only", "HEAD"], cwd=repo_path, timeout=60)
    if code != 0:
        audit.error = tree_out[-1000:]
        audit.verdict = "repo_tree_unavailable"
        return audit
    files = [line.strip() for line in tree_out.splitlines() if line.strip()]
    audit.total_files = len(files)
    root_files = [f for f in files if "/" not in f]
    code_files = [f for f in files if Path(f).suffix.lower() in CODE_EXTS]
    audit.code_files = len(code_files)
    lower_files = [f.lower() for f in files]
    audit.has_readme = any(Path(f).name.lower().startswith("readme") for f in files)
    audit.has_license = any(Path(f).name.lower().startswith(("license", "licence")) for f in files)
    audit.has_env_file = any(Path(f).name.lower() in {"requirements.txt", "environment.yml", "environment.yaml", "pyproject.toml", "setup.py", "package.json"} for f in files)
    audit.has_entrypoint = any(any(h in f.lower() for h in ENTRY_HINTS) for f in files)
    audit.root_files_sample = root_files[:20]
    audit.code_files_sample = code_files[:30]
    if audit.total_files < 8 or audit.code_files < 3:
        audit.verdict = "weak_or_placeholder_repo"
    elif audit.code_files >= 10 and audit.has_readme and (audit.has_env_file or audit.has_entrypoint):
        audit.verdict = "verified_substantial_code"
    elif audit.code_files >= 5:
        audit.verdict = "likely_code_repo"
    else:
        audit.verdict = "weak_or_placeholder_repo"
    return audit


def paper_verdict(candidates: list[Candidate], repo_audit: RepoAudit | None) -> tuple[str, str]:
    if not candidates:
        return "no_code_link_found", "No GitHub/project code link found in arXiv page or PDF URI annotations."
    if not repo_audit:
        best = candidates[0]
        return "code_link_found_not_audited", f"Best candidate {best.url} score={best.score} reason={best.reason}"
    best = next((c for c in candidates if c.repo == repo_audit.repo), candidates[0])
    search_only = best.source.startswith("github_search")
    if repo_audit.verdict == "verified_substantial_code":
        if search_only:
            return "open_source_verified_search_only", f"{repo_audit.repo}: found via GitHub search, {repo_audit.code_files} code-like files; not directly linked in paper/PDF."
        return "open_source_verified", f"{repo_audit.repo}: {repo_audit.code_files} code-like files, README={repo_audit.has_readme}, env={repo_audit.has_env_file}, entry={repo_audit.has_entrypoint}"
    if repo_audit.verdict == "likely_code_repo":
        if search_only:
            return "open_source_likely_search_only", f"{repo_audit.repo}: found via GitHub search, {repo_audit.code_files} code-like files; not directly linked in paper/PDF."
        return "open_source_likely", f"{repo_audit.repo}: {repo_audit.code_files} code-like files, partial reproducibility signals."
    if repo_audit.verdict == "weak_or_placeholder_repo":
        return "suspicious_weak_code_repo", f"{repo_audit.repo}: only {repo_audit.total_files} files / {repo_audit.code_files} code-like files."
    return "suspicious_broken_code_link", f"{repo_audit.repo}: {repo_audit.error or repo_audit.verdict}"


def write_outputs(audits: list[PaperAudit]) -> None:
    AUDIT_DIR.mkdir(parents=True, exist_ok=True)
    (AUDIT_DIR / "paper_code_audit.json").write_text(
        json.dumps([asdict(a) for a in audits], ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    with (AUDIT_DIR / "paper_code_audit.tsv").open("w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f, delimiter="\t", lineterminator="\n")
        writer.writerow([
            "arxiv_id", "source_group", "verdict", "title", "best_repo",
            "repo_verdict", "candidate_count", "best_candidate_url", "evidence",
        ])
        for a in audits:
            best = a.candidates[0] if a.candidates else None
            writer.writerow([
                a.arxiv_id,
                a.source_group,
                a.verdict,
                a.title,
                a.best_repo.repo if a.best_repo else "",
                a.best_repo.verdict if a.best_repo else "",
                len(a.candidates),
                best.url if best else "",
                a.evidence,
            ])
    repo_rows = []
    for a in audits:
        if a.best_repo:
            repo_rows.append(asdict(a.best_repo) | {"arxiv_id": a.arxiv_id, "title": a.title})
    (AUDIT_DIR / "repo_audit.json").write_text(json.dumps(repo_rows, ensure_ascii=False, indent=2), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=0, help="Limit papers processed, 0 means all.")
    parser.add_argument("--offset", type=int, default=0)
    parser.add_argument("--source-group", choices=["2026-arxiv", "curated-pre2026"], default=None)
    parser.add_argument("--sleep", type=float, default=0.1)
    parser.add_argument("--probe-project-pages", action="store_true")
    parser.add_argument("--github-search", action="store_true", help="Fallback to GitHub repository search when paper links are weak/missing.")
    parser.add_argument("--audit-repos", action="store_true")
    parser.add_argument("--repo-score-threshold", type=int, default=3)
    parser.add_argument("--repo-limit", type=int, default=0, help="Max repo clones/audits, 0 means no cap.")
    args = parser.parse_args()

    papers = json.loads(MANIFEST.read_text(encoding="utf-8"))
    if args.source_group:
        papers = [p for p in papers if p.get("source_group") == args.source_group]
    papers = papers[args.offset:]
    if args.limit:
        papers = papers[:args.limit]

    audits: list[PaperAudit] = []
    repo_cache: dict[str, RepoAudit] = {}
    repo_audited = 0
    for idx, paper in enumerate(papers, start=1 + args.offset):
        sys.stderr.write(f"[{idx}/{args.offset + len(papers)}] {paper['arxiv_id']} {paper['title'][:80]}\n")
        sys.stderr.flush()
        candidates = paper_candidates(paper, args.sleep, args.probe_project_pages)
        if args.github_search and (not candidates or (candidates[0].score < args.repo_score_threshold)):
            by_key = {c.repo or c.url: c for c in candidates}
            for cand in github_search_candidates(paper, args.sleep):
                key = cand.repo or cand.url
                if key not in by_key or cand.score > by_key[key].score:
                    by_key[key] = cand
            candidates = sorted(by_key.values(), key=lambda c: (c.score, bool(c.repo)), reverse=True)
        pa = PaperAudit(
            arxiv_id=paper["arxiv_id"],
            title=paper["title"],
            source_group=paper.get("source_group", ""),
            tags=paper.get("tags", []),
            pdf_path=paper.get("pdf_path", ""),
            candidates=candidates,
        )
        best_repo = next((c.repo for c in candidates if c.repo and c.score >= args.repo_score_threshold), None)
        if args.audit_repos and best_repo:
            if args.repo_limit and repo_audited >= args.repo_limit and best_repo not in repo_cache:
                pa.verdict, pa.evidence = paper_verdict(candidates, None)
            else:
                if best_repo not in repo_cache:
                    repo_cache[best_repo] = audit_repo(best_repo, args.sleep)
                    repo_audited += 1
                pa.best_repo = repo_cache[best_repo]
                pa.verdict, pa.evidence = paper_verdict(candidates, pa.best_repo)
        else:
            pa.verdict, pa.evidence = paper_verdict(candidates, None)
        audits.append(pa)
        if idx % 25 == 0:
            write_outputs(audits)
    write_outputs(audits)
    print(f"papers_audited={len(audits)}")
    print(f"repo_audited={repo_audited}")
    print(f"out={AUDIT_DIR / 'paper_code_audit.tsv'}")


if __name__ == "__main__":
    main()
