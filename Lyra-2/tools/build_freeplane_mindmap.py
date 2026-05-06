#!/usr/bin/env python3
"""Create Freeplane/FreeMind .mm maps from the paper taxonomy cards."""

from __future__ import annotations

import argparse
import csv
import html
import time
import xml.etree.ElementTree as ET
from collections import defaultdict
from pathlib import Path


ROOT = Path("/Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2")
BOARDMIX_DIR = ROOT / "paper_collection_3d4d_reconstruction_2026_04_26" / "boardmix_mindmap"
CARDS = BOARDMIX_DIR / "boardmix_cards.csv"
OUT_DIR = BOARDMIX_DIR / "freeplane"


def now_ms() -> str:
    return str(int(time.time() * 1000))


def file_link(path: str) -> str:
    if not path:
        return ""
    try:
        return Path(path).resolve().as_uri()
    except Exception:
        return path


def add_node(parent: ET.Element, text: str, *, folded: bool = False, link: str = "") -> ET.Element:
    attrs = {
        "TEXT": text,
        "CREATED": now_ms(),
        "MODIFIED": now_ms(),
    }
    if folded:
        attrs["FOLDED"] = "true"
    if link:
        attrs["LINK"] = link
    return ET.SubElement(parent, "node", attrs)


def add_note(node: ET.Element, paragraphs: list[str], image_path: str = "") -> None:
    rich = ET.SubElement(node, "richcontent", {"TYPE": "NOTE"})
    html_el = ET.SubElement(rich, "html")
    ET.SubElement(html_el, "head")
    body = ET.SubElement(html_el, "body")
    for paragraph in paragraphs:
        p = ET.SubElement(body, "p")
        p.text = paragraph
    if image_path:
        p = ET.SubElement(body, "p")
        img = ET.SubElement(p, "img", {"src": file_link(image_path)})
        img.tail = ""


def load_cards() -> list[dict]:
    with CARDS.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def grouped(cards: list[dict]):
    tree = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: defaultdict(list))))
    for card in cards:
        tree[card["motivation"]][card["angle"]][card["subproblem"]][card["solution_family"]].append(card)
    return tree


def add_paper(parent: ET.Element, card: dict) -> None:
    label = f"{card['method_name']} | {card['arxiv_id']}"
    paper = add_node(parent, label, folded=True, link=file_link(card["pdf_path"]))
    add_note(
        paper,
        [
            f"Paper: {card['title']}",
            f"一句话: {card['one_liner']}",
            f"Motivation: {card['motivation']}",
            f"切入点: {card['angle']}",
            f"子问题: {card['subproblem']}",
            f"解法族: {card['solution_family']}",
            f"Code status: {card.get('code_status') or 'not checked'}",
        ],
        card.get("method_figure", ""),
    )
    add_node(paper, f"一句话：{card['one_liner']}")
    if card.get("method_figure"):
        add_node(paper, "Method diagram", link=file_link(card["method_figure"]))
    if card.get("pdf_path"):
        add_node(paper, "PDF", link=file_link(card["pdf_path"]))
    if card.get("code_url"):
        add_node(paper, f"Code：{card.get('code_status') or 'candidate'}", link=card["code_url"])


def build_map(cards: list[dict], path: Path, *, focus_leaves: int | None = None) -> None:
    root = ET.Element("map", {"version": "freeplane 1.11.14"})
    root_node = add_node(root, "3D/4D 重建与世界模型：问题-切入点-方法脑图")
    add_note(root_node, [
        "结构：Motivation → 切入点 → 子问题 → 解法族 → Paper/Method",
        "每个 paper 节点带有一句话方案、PDF 链接、候选代码链接，以及 method diagram 图片链接/注释图。",
        "这是从本地 839 篇 paper manifest 自动生成的 Freeplane/FreeMind .mm 文件。",
    ])

    for motivation, angles in sorted(grouped(cards).items()):
        motivation_count = sum(len(v) for sub in angles.values() for sol in sub.values() for v in sol.values())
        m_node = add_node(root_node, f"Motivation：{motivation} ({motivation_count})", folded=True)
        for angle, subproblems in sorted(angles.items()):
            angle_count = sum(len(v) for sol in subproblems.values() for v in sol.values())
            a_node = add_node(m_node, f"切入点：{angle} ({angle_count})", folded=True)
            for subproblem, solutions in sorted(subproblems.items()):
                sub_count = sum(len(v) for v in solutions.values())
                s_node = add_node(a_node, f"子问题：{subproblem} ({sub_count})", folded=True)
                for solution, bucket in sorted(solutions.items()):
                    bucket = sorted(bucket, key=lambda c: (c["source_group"] != "curated-pre2026", c["title"]))
                    sol_node = add_node(s_node, f"解法族：{solution} ({len(bucket)})", folded=True)
                    shown = bucket if focus_leaves is None else bucket[:focus_leaves]
                    for card in shown:
                        add_paper(sol_node, card)
                    if focus_leaves is not None and len(bucket) > len(shown):
                        add_node(sol_node, f"... 另有 {len(bucket) - len(shown)} 篇，见 full map 或 CSV", folded=True)

    ET.indent(root, space="  ")
    path.parent.mkdir(parents=True, exist_ok=True)
    ET.ElementTree(root).write(path, encoding="utf-8", xml_declaration=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--focus-leaves", type=int, default=3)
    args = parser.parse_args()
    cards = load_cards()
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    build_map(cards, OUT_DIR / "3d4d_reconstruction_focus.freeplane.mm", focus_leaves=args.focus_leaves)
    build_map(cards, OUT_DIR / "3d4d_reconstruction_full.freeplane.mm", focus_leaves=None)
    print(f"cards={len(cards)}")
    print(f"focus={OUT_DIR / '3d4d_reconstruction_focus.freeplane.mm'}")
    print(f"full={OUT_DIR / '3d4d_reconstruction_full.freeplane.mm'}")


if __name__ == "__main__":
    main()
