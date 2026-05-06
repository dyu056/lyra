#!/usr/bin/env python3
"""Build Boardmix-ready mind-map artifacts for the 3D/4D paper corpus.

Outputs:
- Markdown mind maps using heading hierarchy, suitable for Boardmix text-to-mind-map/import workflows.
- CSV card table with the same hierarchy and local method-figure paths.
- Extracted method/overview figure thumbnails from each PDF when possible.
"""

from __future__ import annotations

import argparse
import csv
import html
import json
import sys
import re
import textwrap
from collections import Counter, defaultdict
from concurrent.futures import ProcessPoolExecutor, as_completed
from dataclasses import dataclass, asdict
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
from pypdf import PdfReader


ROOT = Path("/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2")
CORPUS = ROOT / "paper_collection_3d4d_reconstruction_2026_04_26"
MANIFEST = CORPUS / "metadata" / "papers_manifest.json"
CODE_AUDIT = CORPUS / "code_audit" / "paper_code_audit.json"
OUT_DIR = CORPUS / "boardmix_mindmap"
FIG_DIR = OUT_DIR / "method_figures"


ANGLE_KEYWORDS = [
    ("计算角度", ["fast", "real-time", "real time", "efficient", "accelerat", "speed", "one-step", "feed-forward", "feedforward", "streaming", "online", "lightweight", "runtime"]),
    ("内存/存储角度", ["memory", "compact", "compression", "compress", "pruning", "prune", "quant", "sparse", "progressive", "low-rank", "hash", "storage", "coding"]),
    ("训练/监督角度", ["training", "train", "self-supervised", "unsupervised", "supervised", "distillation", "distill", "test-time", "few-shot", "zero-shot", "prior", "diffusion", "foundation", "synthetic", "data generation"]),
    ("表示/几何角度", ["gaussian", "splat", "nerf", "radiance field", "sdf", "implicit", "mesh", "point", "voxel", "surface", "geometry", "depth", "normal", "scene coordinate", "convex"]),
    ("时空/动态角度", ["4d", "dynamic", "motion", "temporal", "time", "deform", "tracking", "spatiotemporal", "scene flow", "video", "evolution"]),
    ("数据/传感角度", ["sparse-view", "sparse view", "single image", "monocular", "multi-view", "rgb-d", "stereo", "satellite", "sonar", "tactile", "underwater", "medical", "event", "hyperspectral", "lidar"]),
    ("系统/在线部署角度", ["slam", "mapping", "robot", "autonomous", "driving", "navigation", "embodied", "digital twin", "viewer", "sim-to-real", "closed-loop"]),
    ("生成/世界模型角度", ["world model", "video generation", "simulator", "simulation", "generative", "diffusion", "policy", "planning", "action", "controllable"]),
]

MOTIVATION_KEYWORDS = [
    ("稀疏/单目/少视角 3D 重建", ["sparse view", "sparse-view", "single image", "single-view", "monocular", "few view", "one image", "one-shot", "feed-forward", "novel view synthesis"]),
    ("多视角几何/表面/场景重建", ["multi-view", "multiview", "surface reconstruction", "3d reconstruction", "depth", "normal", "point cloud", "mesh", "sdf", "implicit surface"]),
    ("动态场景与 4D 重建", ["4d", "dynamic", "motion", "temporal", "deformable", "tracking", "scene flow", "spatiotemporal"]),
    ("实时/大规模/高效 3D 表示", ["real-time", "real time", "efficient", "fast", "accelerat", "compact", "compression", "scalable", "streaming", "large-scale"]),
    ("SLAM/机器人/自动驾驶世界模型", ["slam", "robot", "autonomous", "driving", "navigation", "embodied", "parking", "manipulation", "world model", "planning"]),
    ("人体/头像/可动画资产", ["human", "avatar", "head", "face", "body", "hand", "garment", "cloth", "animation", "animatable"]),
    ("生成式 3D/4D 内容与仿真", ["text-to-3d", "generation", "generative", "diffusion", "video generation", "world simulator", "simulation", "content creation"]),
    ("领域/传感器特化重建", ["medical", "satellite", "underwater", "sonar", "tactile", "crop", "cattle", "colon", "brain", "hyperspectral", "membrane", "civil"]),
]

SUBPROBLEM_KEYWORDS = [
    ("减少优化/采样/渲染步骤", ["one-step", "few-step", "accelerat", "fast", "efficient", "adaptive ray", "sampling", "runtime", "real-time"]),
    ("降低显存/存储/模型体积", ["memory", "compact", "compression", "pruning", "quant", "sparse", "progressive", "coding", "low-rank"]),
    ("解决稀疏视角几何不稳定", ["sparse", "few view", "sparse-view", "single image", "monocular", "one image", "initialization", "pose"]),
    ("提升几何一致性/表面质量", ["geometry", "surface", "normal", "depth", "sdf", "mesh", "floater", "consistency", "regularization"]),
    ("建模运动/形变/时间一致性", ["motion", "deform", "dynamic", "temporal", "tracking", "scene flow", "4d", "spatiotemporal"]),
    ("提升泛化/跨场景/开放世界能力", ["generalizable", "foundation", "zero-shot", "few-shot", "in-the-wild", "open-vocabulary", "scaling"]),
    ("接入 SLAM/机器人闭环系统", ["slam", "mapping", "robot", "navigation", "planning", "closed-loop", "digital twin", "sim-to-real"]),
    ("提升可控生成/世界演化预测", ["world model", "video generation", "simulator", "policy", "action", "planning", "controllable", "evolution"]),
    ("适配特殊传感器/行业场景", ["satellite", "medical", "underwater", "sonar", "tactile", "hyperspectral", "crop", "cattle", "colon", "brain"]),
]

SOLUTION_KEYWORDS = [
    ("Gaussian Splatting 表示与正则化", ["gaussian", "splat"]),
    ("NeRF/辐射场/体渲染", ["nerf", "radiance field", "volume rendering", "neural field"]),
    ("SDF/隐式表面/网格/点云", ["sdf", "implicit surface", "mesh", "point cloud", "surface reconstruction", "normal"]),
    ("Feed-forward / Transformer / Foundation Model", ["feed-forward", "feedforward", "transformer", "foundation", "vggt", "dust3r", "mast3r"]),
    ("Diffusion/生成先验/视频模型", ["diffusion", "generative", "video generation", "world model"]),
    ("Motion decomposition / canonical space / deformation", ["deform", "canonical", "motion", "tracking", "scene flow", "temporal"]),
    ("Pruning / compression / progressive coding", ["pruning", "compress", "compact", "quant", "progressive", "coding", "low-rank"]),
    ("SLAM / pose graph / online mapping pipeline", ["slam", "pose", "mapping", "online", "loop", "bundle adjustment"]),
    ("Sensor/domain-specific pipeline", ["satellite", "medical", "sonar", "tactile", "underwater", "hyperspectral", "crop", "cattle"]),
]


@dataclass
class Card:
    arxiv_id: str
    title: str
    source_group: str
    motivation: str
    angle: str
    subproblem: str
    solution_family: str
    method_name: str
    one_liner: str
    method_figure: str
    pdf_path: str
    code_url: str
    code_status: str
    tags: str


def norm_text(paper: dict) -> str:
    return f"{paper.get('title', '')}\n{paper.get('abstract', '')}\n{' '.join(paper.get('tags') or [])}".lower()


def choose_bucket(text: str, rules: list[tuple[str, list[str]]], default: str) -> str:
    scores = []
    for label, keys in rules:
        score = sum(1 for k in keys if k in text)
        scores.append((score, label))
    scores.sort(reverse=True)
    return scores[0][1] if scores and scores[0][0] > 0 else default


def method_name(title: str) -> str:
    title = re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", " ", title)
    first = title.split(":", 1)[0].strip()
    if first and len(first) <= 50:
        return first
    match = re.search(r"\b[A-Za-z][A-Za-z0-9]*[-_]?[A-Z0-9][A-Za-z0-9-]*\b", title)
    return match.group(0) if match else "本文方法"


def one_liner(paper: dict, motivation: str, angle: str, subproblem: str, solution_family: str) -> str:
    name = method_name(paper["title"])
    return md_escape(f"{name} 针对「{subproblem}」，从「{angle}」切入，主要采用「{solution_family}」来服务「{motivation}」。")


def safe_name(text: str, max_len: int = 90) -> str:
    text = re.sub(r"[^A-Za-z0-9._-]+", "_", text).strip("_")
    return (text[:max_len] or "paper").strip("_")


def placeholder_image(path: Path, title: str, arxiv_id: str, message: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    img = Image.new("RGB", (900, 520), (248, 250, 252))
    draw = ImageDraw.Draw(img)
    try:
        font_title = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 30)
        font_body = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 22)
    except Exception:
        font_title = font_body = None
    y = 52
    draw.text((48, y), arxiv_id, fill=(37, 99, 235), font=font_title)
    y += 56
    for line in textwrap.wrap(title, width=46)[:4]:
        draw.text((48, y), line, fill=(15, 23, 42), font=font_title)
        y += 42
    y += 20
    for line in textwrap.wrap(message, width=62):
        draw.text((48, y), line, fill=(71, 85, 105), font=font_body)
        y += 32
    img.save(path)


def extract_method_figure(paper: dict, max_pages: int = 4, max_width: int = 900) -> str:
    pdf_path = Path(paper.get("pdf_path") or "")
    fig_path = FIG_DIR / f"{paper['arxiv_id'].replace('/', '_')}_{safe_name(method_name(paper['title']), 50)}.png"
    if fig_path.exists() and fig_path.stat().st_size > 1000:
        return str(fig_path)
    if not pdf_path.exists():
        placeholder_image(fig_path, paper["title"], paper["arxiv_id"], "PDF not found; no method figure extracted.")
        return str(fig_path)
    try:
        reader = PdfReader(str(pdf_path))
        best = None
        best_score = -1
        for page_idx, page in enumerate(reader.pages[:max_pages]):
            for img_idx, image_file in enumerate(page.images):
                pil = image_file.image.convert("RGB")
                w, h = pil.size
                if w < 220 or h < 120:
                    continue
                score = w * h
                # Slightly prefer earlier overview pages but avoid tiny logos.
                score = score / (1 + page_idx * 0.25)
                if score > best_score:
                    best_score = score
                    best = pil
        if best is None:
            placeholder_image(fig_path, paper["title"], paper["arxiv_id"], "No embedded figure was extractable from the first pages; use PDF link for full method diagram.")
        else:
            w, h = best.size
            if w > max_width:
                h = int(h * max_width / w)
                w = max_width
                best = best.resize((w, h), Image.Resampling.LANCZOS)
            fig_path.parent.mkdir(parents=True, exist_ok=True)
            best.save(fig_path, optimize=True)
    except Exception as exc:
        placeholder_image(fig_path, paper["title"], paper["arxiv_id"], f"Figure extraction failed: {exc}")
    return str(fig_path)


def load_code_audit() -> dict[str, dict]:
    if not CODE_AUDIT.exists():
        return {}
    audits = json.loads(CODE_AUDIT.read_text(encoding="utf-8"))
    return {a["arxiv_id"]: a for a in audits}


def best_code_url(audit: dict | None) -> str:
    if not audit:
        return ""
    for cand in audit.get("candidates") or []:
        url = cand.get("url", "")
        if cand.get("repo") or "github.com" in url.lower():
            return url
    return ""


def extract_figure_task(paper: dict) -> tuple[str, str]:
    return paper["arxiv_id"], extract_method_figure(paper)


def make_cards(limit_figures: int = 0, workers: int = 1) -> list[Card]:
    papers = json.loads(MANIFEST.read_text(encoding="utf-8"))
    code = load_code_audit()
    figure_paths: dict[str, str] = {}
    figure_papers = papers[:limit_figures] if limit_figures else papers
    if workers > 1 and figure_papers:
        with ProcessPoolExecutor(max_workers=workers) as ex:
            futures = {ex.submit(extract_figure_task, paper): paper for paper in figure_papers}
            for done, fut in enumerate(as_completed(futures), start=1):
                paper = futures[fut]
                try:
                    arxiv_id, figure = fut.result()
                    figure_paths[arxiv_id] = figure
                except Exception as exc:
                    fig_path = FIG_DIR / f"{paper['arxiv_id'].replace('/', '_')}_{safe_name(method_name(paper['title']), 50)}.png"
                    placeholder_image(fig_path, paper["title"], paper["arxiv_id"], f"Figure extraction failed: {exc}")
                    figure_paths[paper["arxiv_id"]] = str(fig_path)
                if done == 1 or done % 25 == 0 or done == len(figure_papers):
                    sys.stderr.write(f"[figures {done}/{len(figure_papers)}]\n")
                    sys.stderr.flush()
    cards: list[Card] = []
    for i, paper in enumerate(papers, start=1):
        if i == 1 or i % 25 == 0 or i == len(papers):
            sys.stderr.write(f"[{i}/{len(papers)}] {paper['arxiv_id']} {paper['title'][:70]}\n")
            sys.stderr.flush()
        text = norm_text(paper)
        motivation = choose_bucket(text, MOTIVATION_KEYWORDS, "其他/待人工归并")
        angle = choose_bucket(text, ANGLE_KEYWORDS, "综合方法角度")
        subproblem = choose_bucket(text, SUBPROBLEM_KEYWORDS, "其他开放子问题")
        solution = choose_bucket(text, SOLUTION_KEYWORDS, "组合式/混合 pipeline")
        figure = ""
        if not limit_figures or i <= limit_figures:
            figure = figure_paths.get(paper["arxiv_id"])
            if figure is None:
                figure = extract_method_figure(paper)
        audit = code.get(paper["arxiv_id"])
        cards.append(Card(
            arxiv_id=paper["arxiv_id"],
            title=paper["title"],
            source_group=paper.get("source_group", ""),
            motivation=motivation,
            angle=angle,
            subproblem=subproblem,
            solution_family=solution,
            method_name=method_name(paper["title"]),
            one_liner=one_liner(paper, motivation, angle, subproblem, solution),
            method_figure=figure,
            pdf_path=paper.get("pdf_path", ""),
            code_url=best_code_url(audit),
            code_status=(audit or {}).get("verdict", ""),
            tags=", ".join(paper.get("tags") or []),
        ))
    return cards


def write_csv(cards: list[Card]) -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    def clean(value):
        if isinstance(value, str):
            return re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", " ", value)
        return value
    with (OUT_DIR / "boardmix_cards.csv").open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(asdict(cards[0]).keys()))
        writer.writeheader()
        for card in cards:
            writer.writerow({k: clean(v) for k, v in asdict(card).items()})


def md_escape(text: str) -> str:
    return re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", " ", text.replace("\n", " ")).strip()


def group_cards(cards: list[Card]):
    groups = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: defaultdict(list))))
    for card in cards:
        groups[card.motivation][card.angle][card.subproblem][card.solution_family].append(card)
    return groups


def write_mindmap(cards: list[Card], path: Path, max_leaf_per_solution: int | None = None) -> None:
    groups = group_cards(cards)
    lines: list[str] = []
    lines.append("# 3D/4D 重建与世界模型论文问题-切入点脑图")
    lines.append("")
    lines.append("> Boardmix 导入建议：用 Boardmix 的文本/Markdown 生成思维导图，或先导入 XMind/Markdown。每个 paper 叶子节点附一句话方案、代码状态、PDF 和 method figure 路径。")
    lines.append("")
    for motivation in sorted(groups):
        count_m = sum(len(cards4) for angles in groups[motivation].values() for subs in angles.values() for cards4 in subs.values())
        lines.append(f"## Motivation：{motivation}（{count_m}）")
        for angle in sorted(groups[motivation]):
            count_a = sum(len(cards4) for subs in groups[motivation][angle].values() for cards4 in subs.values())
            lines.append(f"### 切入点：{angle}（{count_a}）")
            for subproblem in sorted(groups[motivation][angle]):
                count_s = sum(len(cards4) for cards4 in groups[motivation][angle][subproblem].values())
                lines.append(f"#### 子问题：{subproblem}（{count_s}）")
                for solution in sorted(groups[motivation][angle][subproblem]):
                    bucket = sorted(groups[motivation][angle][subproblem][solution], key=lambda c: (c.source_group != "curated-pre2026", c.title))
                    shown = bucket if max_leaf_per_solution is None else bucket[:max_leaf_per_solution]
                    suffix = "" if len(shown) == len(bucket) else f"；另有 {len(bucket)-len(shown)} 篇见 full/csv"
                    lines.append(f"##### 解法族：{solution}（{len(bucket)}{suffix}）")
                    for card in shown:
                        lines.append(f"###### {md_escape(card.method_name)} ｜ {card.arxiv_id}")
                        lines.append(f"- Paper：{md_escape(card.title)}")
                        lines.append(f"- 一句话：{md_escape(card.one_liner)}")
                        if card.method_figure:
                            rel = Path(card.method_figure)
                            try:
                                rel = rel.relative_to(path.parent)
                            except ValueError:
                                pass
                            lines.append(f"- Method diagram：![{card.arxiv_id}]({rel})")
                        lines.append(f"- PDF：{card.pdf_path}")
                        if card.code_url:
                            lines.append(f"- Code：{md_escape(card.code_url)}（{md_escape(card.code_status or 'candidate')}）")
                    lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def write_summary(cards: list[Card]) -> None:
    lines = ["# Boardmix 脑图构建摘要", ""]
    for name, values in [
        ("Motivation", [c.motivation for c in cards]),
        ("切入点", [c.angle for c in cards]),
        ("子问题", [c.subproblem for c in cards]),
        ("解法族", [c.solution_family for c in cards]),
        ("代码状态", [c.code_status or "not_checked" for c in cards]),
    ]:
        lines.append(f"## {name}")
        for label, count in Counter(values).most_common():
            lines.append(f"- {label}: {count}")
        lines.append("")
    (OUT_DIR / "taxonomy_summary.md").write_text("\n".join(lines), encoding="utf-8")


def write_html(cards: list[Card]) -> None:
    rows = []
    for card in cards:
        fig = ""
        if card.method_figure:
            rel = Path(card.method_figure)
            try:
                rel = rel.relative_to(OUT_DIR)
            except ValueError:
                pass
            fig = f'<img src="{html.escape(str(rel))}" loading="lazy" />'
        rows.append(f"""
<article class="card">
  <div class="meta">{html.escape(card.arxiv_id)} · {html.escape(card.source_group)} · {html.escape(card.angle)}</div>
  <h2>{html.escape(card.title)}</h2>
  {fig}
  <p>{html.escape(card.one_liner)}</p>
  <p class="small"><b>Motivation</b>: {html.escape(card.motivation)}<br><b>Subproblem</b>: {html.escape(card.subproblem)}<br><b>Solution</b>: {html.escape(card.solution_family)}</p>
  <p class="small"><a href="{html.escape(card.pdf_path)}">PDF</a>{' · <a href="'+html.escape(card.code_url)+'">Code</a>' if card.code_url else ''}</p>
</article>
""")
    doc = f"""<!doctype html>
<html><head><meta charset="utf-8"><title>3D/4D Boardmix Paper Cards</title>
<style>
body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; background:#f8fafc; color:#0f172a; margin:0; }}
header {{ padding:32px 40px; background:#0f172a; color:white; }}
main {{ display:grid; grid-template-columns: repeat(auto-fill, minmax(360px, 1fr)); gap:18px; padding:24px; }}
.card {{ background:white; border:1px solid #e2e8f0; border-radius:8px; padding:16px; box-shadow:0 1px 2px #0001; }}
.card img {{ width:100%; max-height:280px; object-fit:contain; background:#f1f5f9; border-radius:6px; border:1px solid #e2e8f0; }}
.meta,.small {{ color:#475569; font-size:13px; line-height:1.45; }}
h2 {{ font-size:17px; line-height:1.25; margin:8px 0 12px; }}
a {{ color:#2563eb; }}
</style></head><body>
<header><h1>3D/4D Reconstruction & World Models: Boardmix Cards</h1><p>{len(cards)} papers grouped by motivation, problem angle, subproblem, and solution family.</p></header>
<main>{''.join(rows)}</main></body></html>"""
    (OUT_DIR / "boardmix_cards_preview.html").write_text(doc, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit-figures", type=int, default=0, help="Extract figures only for the first N papers; 0 means all.")
    parser.add_argument("--focus-leaves", type=int, default=3, help="Max papers per solution family in focus map.")
    parser.add_argument("--workers", type=int, default=1, help="Parallel workers for PDF figure extraction.")
    args = parser.parse_args()
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    cards = make_cards(limit_figures=args.limit_figures, workers=args.workers)
    write_csv(cards)
    write_mindmap(cards, OUT_DIR / "boardmix_full_mindmap.md", max_leaf_per_solution=None)
    write_mindmap(cards, OUT_DIR / "boardmix_focus_mindmap.md", max_leaf_per_solution=args.focus_leaves)
    write_summary(cards)
    write_html(cards)
    print(f"cards={len(cards)}")
    print(f"out={OUT_DIR}")
    print(f"figures={len(list(FIG_DIR.glob('*.png')))}")


if __name__ == "__main__":
    main()
