#!/usr/bin/env python3
"""Build a static website for browsing the 3D/4D paper mind map."""

from __future__ import annotations

import csv
import json
import re
from collections import defaultdict
from pathlib import Path

from PIL import Image


ROOT = Path("/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2")
COLLECTION = ROOT / "paper_collection_3d4d_reconstruction_2026_04_26"
CARDS = COLLECTION / "boardmix_mindmap" / "boardmix_cards.csv"
SITE = COLLECTION / "mindmap_site"
FIGURES = SITE / "assets" / "figures"


def rel_from_site(path: str) -> str:
    if not path:
        return ""
    p = Path(path)
    if p.exists():
        return "../" + str(p.relative_to(COLLECTION))
    return path


def figure_asset(path: str, arxiv_id: str, method_name: str) -> str:
    if not path:
        return ""
    src = Path(path)
    if not src.exists():
        return rel_from_site(path)
    FIGURES.mkdir(parents=True, exist_ok=True)
    name = f"{arxiv_id}_{slug(method_name)[:56]}.jpg"
    dest = FIGURES / name
    if not dest.exists() or dest.stat().st_size < 1000:
        image = Image.open(src).convert("RGB")
        max_width = 720
        if image.width > max_width:
            new_height = int(image.height * max_width / image.width)
            image = image.resize((max_width, new_height), Image.Resampling.LANCZOS)
        image.save(dest, "JPEG", quality=72, optimize=True, progressive=True)
    return "./assets/figures/" + name


def arxiv_pdf_url(arxiv_id: str) -> str:
    return f"https://arxiv.org/pdf/{arxiv_id}"


def slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-") or "node"


def load_cards() -> list[dict]:
    with CARDS.open(encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    for row in rows:
        row["method_figure"] = figure_asset(row["method_figure"], row["arxiv_id"], row.get("method_name") or "paper")
        row["pdf_path"] = arxiv_pdf_url(row["arxiv_id"])
        row["search_text"] = " ".join([
            row.get("arxiv_id", ""),
            row.get("title", ""),
            row.get("method_name", ""),
            row.get("motivation", ""),
            row.get("angle", ""),
            row.get("subproblem", ""),
            row.get("solution_family", ""),
            row.get("one_liner", ""),
            row.get("tags", ""),
        ]).lower()
    return rows


def tree_node(name: str, kind: str, children: list[dict] | None = None, paper_ids: list[str] | None = None) -> dict:
    node = {
        "id": f"{kind}:{slug(name)}",
        "name": name,
        "kind": kind,
        "children": children or [],
        "paper_ids": paper_ids or [],
    }
    node["count"] = len(node["paper_ids"])
    return node


def build_tree(cards: list[dict]) -> dict:
    grouped = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: defaultdict(list))))
    for card in cards:
        grouped[card["motivation"]][card["angle"]][card["subproblem"]][card["solution_family"]].append(card["arxiv_id"])

    root_papers = [c["arxiv_id"] for c in cards]
    root = tree_node("3D/4D Reconstruction & World Models", "root", paper_ids=root_papers)
    for motivation in sorted(grouped):
        motivation_papers = []
        motivation_node = tree_node(motivation, "motivation")
        for angle in sorted(grouped[motivation]):
            angle_papers = []
            angle_node = tree_node(angle, "angle")
            for subproblem in sorted(grouped[motivation][angle]):
                sub_papers = []
                sub_node = tree_node(subproblem, "subproblem")
                for solution in sorted(grouped[motivation][angle][subproblem]):
                    paper_ids = sorted(grouped[motivation][angle][subproblem][solution])
                    sub_papers.extend(paper_ids)
                    sol_node = tree_node(solution, "solution", paper_ids=paper_ids)
                    sol_node["children"] = [
                        {
                            "id": f"paper:{pid}",
                            "name": next(card["method_name"] for card in cards if card["arxiv_id"] == pid),
                            "kind": "paper",
                            "paper_ids": [pid],
                            "count": 1,
                            "children": [],
                        }
                        for pid in paper_ids
                    ]
                    sub_node["children"].append(sol_node)
                sub_node["paper_ids"] = sorted(sub_papers)
                sub_node["count"] = len(sub_papers)
                angle_papers.extend(sub_papers)
                angle_node["children"].append(sub_node)
            angle_node["paper_ids"] = sorted(angle_papers)
            angle_node["count"] = len(angle_papers)
            motivation_papers.extend(angle_papers)
            motivation_node["children"].append(angle_node)
        motivation_node["paper_ids"] = sorted(motivation_papers)
        motivation_node["count"] = len(motivation_papers)
        root["children"].append(motivation_node)
    return root


def stats(cards: list[dict]) -> dict:
    def counts(field: str) -> list[dict]:
        counter = defaultdict(int)
        for card in cards:
            counter[card[field]] += 1
        return [{"name": k, "count": v} for k, v in sorted(counter.items(), key=lambda kv: (-kv[1], kv[0]))]

    return {
        "total": len(cards),
        "motivation": counts("motivation"),
        "angle": counts("angle"),
        "solution_family": counts("solution_family"),
        "source_group": counts("source_group"),
        "code_status": counts("code_status"),
    }


def main() -> None:
    cards = load_cards()
    SITE.mkdir(parents=True, exist_ok=True)
    payload = {
        "cards": cards,
        "tree": build_tree(cards),
        "stats": stats(cards),
    }
    (SITE / "mindmap-data.json").write_text(json.dumps(payload, ensure_ascii=False), encoding="utf-8")
    print(f"cards={len(cards)}")
    print(f"site={SITE}")


if __name__ == "__main__":
    main()
