#!/usr/bin/env python3
"""Collect 3D/4D reconstruction papers from arXiv and import them into Zotero.

The script intentionally keeps an auditable paper manifest next to the PDFs.
It uses arXiv OAI-PMH for broad 2026 coverage because the regular search API
rate-limits aggressively for large query batches.
"""

from __future__ import annotations

import argparse
import datetime as dt
import html
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Iterable


TODAY = dt.date(2026, 4, 26)
BASE_URL = "https://export.arxiv.org/oai2"
ZOTERO = "http://127.0.0.1:23119"

OAI_NS = {
    "oai": "http://www.openarchives.org/OAI/2.0/",
    "arxiv": "http://arxiv.org/OAI/arXiv/",
}

RELEVANT_CATEGORIES = {
    "cs.CV",
    "cs.GR",
    "cs.RO",
    "cs.LG",
    "cs.AI",
    "eess.IV",
}

NEGATIVE_TERMS = [
    "protein",
    "molecular",
    "molecule",
    "medical image",
    "ct reconstruction",
    "mri",
    "tomography",
    "semiconductor",
    "wafer",
    "in-memory",
    "hardware",
    "time series",
    "religious",
    "homelessness",
    "recommender system",
    "large language model agents",
]

TAG_RULES = [
    (
        "Codex:4D-Reconstruction",
        [
            "4d reconstruction",
            "4-d reconstruction",
            "dynamic 3d reconstruction",
            "dynamic scene reconstruction",
            "dynamic reconstruction",
            "dynamic novel view",
            "dynamic view synthesis",
            "4d gaussian",
            "dynamic gaussian",
            "deformable gaussian",
            "spacetime gaussian",
            "space-time gaussian",
            "scene flow",
            "video-to-4d",
            "spatiotemporal reconstruction",
            "spatio-temporal reconstruction",
        ],
    ),
    (
        "Codex:3D-Reconstruction",
        [
            "3d reconstruction",
            "3-d reconstruction",
            "3d scene reconstruction",
            "scene reconstruction",
            "surface reconstruction",
            "mesh reconstruction",
            "shape reconstruction",
            "point cloud reconstruction",
            "multi-view reconstruction",
            "multiview reconstruction",
            "single-view 3d",
            "single image 3d",
            "monocular 3d",
            "image-to-3d",
            "video-to-3d",
            "multi-view stereo",
            "multiview stereo",
            "structure from motion",
            "structure-from-motion",
            "sfm",
            "slam",
            "novel view synthesis",
            "radiance field",
            "neural radiance",
            "nerf",
            "gaussian splatting",
            "3dgs",
            "dust3r",
            "mast3r",
        ],
    ),
    (
        "Codex:3D+4D-Evolution",
        [
            "4d generation",
            "dynamic scene generation",
            "world model",
            "world modeling",
            "world generation",
            "interactive world",
            "geometry-aware",
            "geometric-aware",
            "spatial reasoning",
            "video prediction",
        ],
    ),
]

INCLUDE_TERMS = sorted({term for _, terms in TAG_RULES for term in terms}, key=len, reverse=True)

CORE_3D_PATTERNS = [
    r"\b3d reconstruction\b",
    r"\b3-d reconstruction\b",
    r"\b3d scene reconstruction\b",
    r"\bscene reconstruction\b",
    r"\bsurface reconstruction\b",
    r"\bmesh reconstruction\b",
    r"\bshape reconstruction\b",
    r"\bpoint cloud reconstruction\b",
    r"\bobject reconstruction\b",
    r"\bhuman reconstruction\b",
    r"\bavatar reconstruction\b",
    r"\bfeed[- ]forward 3d\b",
    r"\bsingle[- ]view 3d\b",
    r"\bsingle image to 3d\b",
    r"\bimage[- ]to[- ]3d\b",
    r"\bvideo[- ]to[- ]3d\b",
    r"\bmulti[- ]view stereo\b",
    r"\bmultiview stereo\b",
    r"\bstructure[- ]from[- ]motion\b",
    r"\bvisual slam\b",
    r"\bdense slam\b",
    r"\brgb[- ]d slam\b",
    r"\bnovel view synthesis\b",
    r"\bdynamic view synthesis\b",
    r"\bradiance fields?\b",
    r"\bneural radiance\b",
    r"\bnerf\b",
    r"\b3d gaussian\b",
    r"\bgaussian splatting\b",
    r"\b3dgs\b",
    r"\bdust3r\b",
    r"\bmast3r\b",
    r"\bvggt\b",
    r"\bpointmap\b",
]

CORE_4D_PATTERNS = [
    r"\b4d reconstruction\b",
    r"\b4-d reconstruction\b",
    r"\bdynamic 3d reconstruction\b",
    r"\bdynamic scene reconstruction\b",
    r"\bdynamic reconstruction\b",
    r"\bdynamic novel view\b",
    r"\bdynamic view synthesis\b",
    r"\b4d gaussian\b",
    r"\bdynamic 3d gaussians?\b",
    r"\bdynamic gaussian\b",
    r"\bdeformable 3d gaussians?\b",
    r"\bdeformable gaussian\b",
    r"\bspacetime gaussian\b",
    r"\bspace[- ]time gaussian\b",
    r"\bscene flow\b",
    r"\bvideo[- ]to[- ]4d\b",
    r"\b3d[- ]to[- ]4d\b",
    r"\bspatiotemporal reconstruction\b",
    r"\bspatio[- ]temporal reconstruction\b",
]

WORLD_PATTERNS = [
    r"\b4d generation\b",
    r"\bdynamic scene generation\b",
    r"\bgeometry[- ]aware 4d video generation\b",
    r"\bworld models?\b",
    r"\bworld generation\b",
    r"\binteractive world\b",
]

WORLD_ANCHOR_PATTERNS = [
    r"\b3d\b",
    r"\b4d\b",
    r"\bgeometry\b",
    r"\bgeometric\b",
    r"\bspatial\b",
    r"\bscene\b",
    r"\bvideo\b",
    r"\bdriving\b",
    r"\brobot",
    r"\bnavigation\b",
    r"\bmanipulation\b",
    r"\bsimulat",
]

# High-impact/top-venue seed list for <=2025. Kept intentionally curated rather
# than exhaustive; 2026 papers are discovered from arXiv metadata.
CURATED_OLD_ARXIV_IDS = {
    # Classical/multi-view/neural 3D reconstruction
    "1804.02505": "MVSNet",
    "2003.08934": "NeRF",
    "2003.09852": "IDR",
    "2012.02190": "pixelNeRF",
    "2102.13090": "IBRNet",
    "2104.00681": "NeuralRecon",
    "2106.10689": "NeuS",
    "2106.12052": "VolSDF",
    "2108.10869": "DROID-SLAM",
    "2111.12077": "Mip-NeRF 360",
    "2112.00724": "RegNeRF",
    "2112.12130": "NICE-SLAM",
    "2201.05989": "Instant-NGP",
    "2206.00665": "MonoSDF",
    "2308.04079": "3D Gaussian Splatting",
    "2312.14132": "DUSt3R",
    "2406.09756": "MASt3R",
    "2410.03825": "MonST3R",
    "2503.11651": "VGGT",
    # Dynamic / 4D reconstruction and view synthesis
    "1906.07751": "Neural Volumes",
    "2011.12948": "Nerfies",
    "2011.13084": "NSFF",
    "2011.13961": "D-NeRF",
    "2103.02597": "Neural 3D Video Synthesis",
    "2106.13228": "HyperNeRF",
    "2205.15285": "TiNeuVox",
    "2301.09632": "HexPlane",
    "2301.10241": "K-Planes",
    "2308.09713": "Dynamic 3D Gaussians",
    "2309.13101": "Deformable 3D Gaussians",
    "2310.08528": "4D Gaussian Splatting",
    "2310.11448": "4K4D",
    "2312.16812": "Spacetime Gaussian Feature Splatting",
    # 3D generation / geometry-aware world modeling bridge
    "2209.14988": "DreamFusion",
    "2303.11328": "Zero-1-to-3",
    "2309.03453": "SyncDreamer",
    "2402.05054": "LGM",
    "2405.10314": "CAT3D",
    "2503.18945": "Aether",
}


@dataclass
class Paper:
    arxiv_id: str
    title: str
    authors: list[str]
    created: str
    updated: str | None
    categories: list[str]
    abstract: str
    doi: str | None = None
    journal_ref: str | None = None
    source_group: str = ""
    reason: str = ""
    tags: list[str] = field(default_factory=list)
    pdf_path: str | None = None
    zotero_status: str | None = None
    zotero_citekey: str | None = None

    @property
    def year(self) -> int:
        return int(self.created[:4])

    @property
    def abs_url(self) -> str:
        return f"https://arxiv.org/abs/{self.arxiv_id}"

    @property
    def pdf_url(self) -> str:
        return f"https://arxiv.org/pdf/{self.arxiv_id}"


def request_bytes(url: str, *, data: bytes | None = None, headers: dict[str, str] | None = None,
                  method: str | None = None, timeout: int = 60, retries: int = 4) -> bytes:
    headers = {
        "User-Agent": "Codex literature collection for local Zotero import",
        **(headers or {}),
    }
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, data=data, headers=headers, method=method)
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return resp.read()
        except urllib.error.HTTPError as exc:
            if exc.code in {429, 500, 502, 503, 504} and attempt + 1 < retries:
                time.sleep(6 * (attempt + 1))
                continue
            raise
        except (TimeoutError, urllib.error.URLError):
            if attempt + 1 < retries:
                time.sleep(6 * (attempt + 1))
                continue
            raise
    raise RuntimeError(f"unreachable request failure for {url}")


def oai_url(params: dict[str, str]) -> str:
    return BASE_URL + "?" + urllib.parse.urlencode(params)


def clean_text(text: str | None) -> str:
    return re.sub(r"\s+", " ", html.unescape(text or "")).strip()


def parse_record(record: ET.Element) -> Paper | None:
    meta = record.find("oai:metadata/arxiv:arXiv", OAI_NS)
    if meta is None:
        return None
    arxiv_id = clean_text(meta.findtext("arxiv:id", namespaces=OAI_NS))
    title = clean_text(meta.findtext("arxiv:title", namespaces=OAI_NS))
    abstract = clean_text(meta.findtext("arxiv:abstract", namespaces=OAI_NS))
    created = clean_text(meta.findtext("arxiv:created", namespaces=OAI_NS))
    updated = clean_text(meta.findtext("arxiv:updated", namespaces=OAI_NS)) or None
    categories = clean_text(meta.findtext("arxiv:categories", namespaces=OAI_NS)).split()
    doi = clean_text(meta.findtext("arxiv:doi", namespaces=OAI_NS)) or None
    journal_ref = clean_text(meta.findtext("arxiv:journal-ref", namespaces=OAI_NS)) or None
    authors = []
    for author in meta.findall("arxiv:authors/arxiv:author", OAI_NS):
        key = clean_text(author.findtext("arxiv:keyname", namespaces=OAI_NS))
        fore = clean_text(author.findtext("arxiv:forenames", namespaces=OAI_NS))
        suffix = clean_text(author.findtext("arxiv:suffix", namespaces=OAI_NS))
        name = " ".join(part for part in [fore, key, suffix] if part)
        if name:
            authors.append(name)
    if not arxiv_id or not title or not created:
        return None
    return Paper(
        arxiv_id=arxiv_id,
        title=title,
        authors=authors,
        created=created,
        updated=updated,
        categories=categories,
        abstract=abstract,
        doi=doi,
        journal_ref=journal_ref,
    )


def fetch_oai_range(out_dir: Path, set_name: str, start: dt.date, end: dt.date, sleep: float) -> list[Paper]:
    cache = out_dir / "metadata" / f"oai_{set_name}_{start.isoformat()}_{end.isoformat()}.xml"
    cache.parent.mkdir(parents=True, exist_ok=True)
    xml_chunks: list[bytes] = []

    if cache.exists():
        raw = cache.read_bytes()
        chunks = raw.split(b"\n<!-- CODEx-OAI-CHUNK -->\n")
    else:
        params = {
            "verb": "ListRecords",
            "metadataPrefix": "arXiv",
            "set": set_name,
            "from": start.isoformat(),
            "until": end.isoformat(),
        }
        token: str | None = None
        while True:
            if token:
                url = oai_url({"verb": "ListRecords", "resumptionToken": token})
            else:
                url = oai_url(params)
            sys.stderr.write(f"Fetching OAI {set_name}: {url}\n")
            sys.stderr.flush()
            chunk = request_bytes(url, timeout=90)
            xml_chunks.append(chunk)
            root = ET.fromstring(chunk)
            err = root.find("oai:error", OAI_NS)
            if err is not None:
                code = err.attrib.get("code")
                if code == "noRecordsMatch":
                    break
                raise RuntimeError(f"OAI error {code}: {clean_text(err.text)}")
            token_el = root.find(".//oai:resumptionToken", OAI_NS)
            token = clean_text(token_el.text if token_el is not None else "")
            if not token:
                break
            time.sleep(sleep)
        cache.write_bytes(b"\n<!-- CODEx-OAI-CHUNK -->\n".join(xml_chunks))
        chunks = xml_chunks

    papers: list[Paper] = []
    for chunk in chunks:
        if not chunk.strip():
            continue
        root = ET.fromstring(chunk)
        for record in root.findall(".//oai:record", OAI_NS):
            paper = parse_record(record)
            if paper:
                papers.append(paper)
    return papers


def fetch_oai_id(arxiv_id: str) -> Paper | None:
    url = oai_url({
        "verb": "GetRecord",
        "metadataPrefix": "arXiv",
        "identifier": f"oai:arXiv.org:{arxiv_id}",
    })
    try:
        root = ET.fromstring(request_bytes(url, timeout=60))
    except Exception as exc:
        sys.stderr.write(f"Could not fetch seed {arxiv_id}: {exc}\n")
        return None
    err = root.find("oai:error", OAI_NS)
    if err is not None:
        sys.stderr.write(f"OAI seed error {arxiv_id}: {clean_text(err.text)}\n")
        return None
    record = root.find(".//oai:record", OAI_NS)
    return parse_record(record) if record is not None else None


def classify(paper: Paper) -> tuple[bool, list[str], str]:
    title = paper.title.lower()
    text = f"{paper.title}\n{paper.abstract}".lower()
    if any(term in text for term in NEGATIVE_TERMS):
        return False, [], "negative-domain-filter"

    tags = ["Codex:3D4D-Reconstruction"]
    matched: list[str] = []

    def hits(patterns: list[str], haystack: str = text) -> list[str]:
        return [pattern for pattern in patterns if re.search(pattern, haystack)]

    title_3d = hits(CORE_3D_PATTERNS, title)
    title_4d = hits(CORE_4D_PATTERNS, title)

    exact_abstract_3d = hits([
        r"\b3d reconstruction\b",
        r"\b3d scene reconstruction\b",
        r"\bscene reconstruction\b",
        r"\bsurface reconstruction\b",
        r"\bmesh reconstruction\b",
        r"\bpoint cloud reconstruction\b",
        r"\bnovel view synthesis\b",
        r"\bradiance fields?\b",
        r"\bneural radiance\b",
    ])
    exact_abstract_4d = hits([
        r"\b4d reconstruction\b",
        r"\bdynamic 3d reconstruction\b",
        r"\bdynamic scene reconstruction\b",
        r"\bdynamic view synthesis\b",
        r"\bvideo[- ]to[- ]4d\b",
        r"\bscene flow\b",
    ])

    title_recon_anchor = re.search(
        r"\b(reconstruction|reconstruct|view synthesis|rendering|radiance|slam|mapping|surface|dynamic|4d|sparse[- ]view|monocular|feed[- ]forward|scene)\b",
        title,
    )
    gaussian_title = re.search(r"\b(gaussian splatting|3d gaussian|3dgs)\b", title)
    nerf_title = re.search(r"\b(nerf|radiance field|neural radiance)\b", title)
    method_title = []
    if gaussian_title and title_recon_anchor:
        method_title.append("title: gaussian/radiance reconstruction anchor")
    if nerf_title and title_recon_anchor:
        method_title.append("title: nerf/radiance reconstruction anchor")

    core_3d = sorted(set(title_3d + method_title))
    # Allow abstract-only inclusion only when the title already looks like a 3D
    # geometry/reconstruction paper; this keeps generic papers whose abstracts
    # mention "3D Gaussian" from flooding the collection.
    if exact_abstract_3d and re.search(r"\b(3d|4d|nerf|gaussian|splat|recon|view|slam|sfm|mesh|surface|point cloud|radiance)\b", title):
        core_3d = sorted(set(core_3d + exact_abstract_3d))

    core_4d = sorted(set(title_4d))
    if exact_abstract_4d and re.search(r"\b(4d|dynamic|video|temporal|spatio|scene flow|gaussian|recon)\b", title):
        core_4d = sorted(set(core_4d + exact_abstract_4d))

    world_terms = hits(WORLD_PATTERNS, title)
    world_anchors = hits(WORLD_ANCHOR_PATTERNS, title)
    if not world_terms:
        # Keep a small bridge category for papers where the title is explicitly
        # 3D/4D/video/robotic and the abstract says world model.
        if re.search(r"\b(3d|4d|video|robot|driving|spatial|scene|simulation)\b", title):
            world_terms = hits([r"\bworld models?\b", r"\bworld generation\b"], text)
            world_anchors = hits(WORLD_ANCHOR_PATTERNS, title)

    if core_3d:
        tags.append("Codex:3D-Reconstruction")
        matched.extend(core_3d)
    if core_4d:
        tags.append("Codex:4D-Reconstruction")
        matched.extend(core_4d)
    if world_terms and world_anchors:
        tags.append("Codex:3D+4D-Evolution")
        matched.extend(world_terms + world_anchors[:3])

    include = bool(core_3d or core_4d or (world_terms and world_anchors))

    # Do not let generic detection/segmentation/classification papers through
    # unless they also contain an explicit reconstruction/rendering/NVS signal.
    generic_task = re.search(
        r"\b(detection|segmentation|classification|forecasting|retrieval|compression|benchmark|survey|editing|face swapping)\b",
        title,
    )
    explicit_geometry_product = re.search(
        r"\b(reconstruction|view synthesis|radiance field|nerf|4d gaussian|scene flow)\b",
        title,
    )
    if generic_task and not explicit_geometry_product:
        return False, [], "generic-task-filter"

    return include, sorted(set(tags)), ", ".join(sorted(set(matched))) or "precise 3D/4D/world-model match"


def dedupe(papers: Iterable[Paper]) -> list[Paper]:
    by_id: dict[str, Paper] = {}
    for paper in papers:
        by_id[paper.arxiv_id] = paper
    return sorted(by_id.values(), key=lambda p: (p.created, p.title.lower()))


def slugify(value: str, max_len: int = 90) -> str:
    value = re.sub(r"[^A-Za-z0-9]+", "_", value).strip("_")
    return value[:max_len].strip("_") or "paper"


def pdf_destination(paper: Paper, pdf_dir: Path) -> Path:
    fname = f"{paper.year}_{slugify(paper.title)}_{paper.arxiv_id.replace('/', '_')}.pdf"
    return pdf_dir / fname


def download_pdf(paper: Paper, pdf_dir: Path, sleep: float) -> None:
    pdf_dir.mkdir(parents=True, exist_ok=True)
    dest = pdf_destination(paper, pdf_dir)
    paper.pdf_path = str(dest)
    if dest.exists() and dest.stat().st_size > 20_000:
        return
    data = request_bytes(paper.pdf_url, timeout=120, retries=5)
    if not data.startswith(b"%PDF"):
        sys.stderr.write(f"Warning: {paper.arxiv_id} PDF response did not start with %PDF\n")
    dest.write_bytes(data)
    time.sleep(sleep)


def zotero_rpc(method: str, params: list) -> dict:
    payload = json.dumps({"jsonrpc": "2.0", "method": method, "params": params, "id": method}).encode()
    data = request_bytes(
        f"{ZOTERO}/better-bibtex/json-rpc",
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST",
        timeout=60,
    )
    return json.loads(data.decode())


def zotero_search_existing(paper: Paper) -> tuple[bool, str | None]:
    for query in [paper.arxiv_id, paper.doi or "", paper.title[:80]]:
        if not query:
            continue
        try:
            result = zotero_rpc("item.search", [query]).get("result", [])
        except Exception:
            continue
        for item in result:
            hay = "\n".join(str(item.get(k, "")) for k in ["DOI", "number", "title", "URL", "note"])
            if paper.arxiv_id in hay or (paper.doi and paper.doi in hay):
                return True, item.get("citekey") or item.get("citation-key")
    return False, None


def split_author(name: str) -> dict[str, str]:
    parts = name.split()
    if len(parts) == 1:
        return {"creatorType": "author", "lastName": parts[0]}
    return {"creatorType": "author", "firstName": " ".join(parts[:-1]), "lastName": parts[-1]}


def zotero_item_json(paper: Paper, connector_id: str) -> dict:
    tags = [{"tag": tag} for tag in paper.tags]
    if paper.source_group == "2026-arxiv":
        tags.append({"tag": "Codex:2026-arXiv"})
    else:
        tags.append({"tag": "Codex:Classic-Pre2026"})
    tags.extend({"tag": cat} for cat in paper.categories if cat in RELEVANT_CATEGORIES)
    extra_lines = [
        f"arXiv: {paper.arxiv_id}",
        "Codex collection: 3D/4D reconstruction survey",
        f"Codex source group: {paper.source_group}",
        f"Codex match reason: {paper.reason}",
    ]
    if paper.journal_ref:
        extra_lines.append(f"Journal/venue: {paper.journal_ref}")
    if paper.pdf_path:
        extra_lines.append(f"Local PDF: {paper.pdf_path}")
    return {
        "id": connector_id,
        "itemType": "preprint",
        "title": paper.title,
        "creators": [split_author(author) for author in paper.authors],
        "abstractNote": paper.abstract,
        "date": paper.created,
        "url": paper.abs_url,
        "DOI": paper.doi or f"10.48550/arXiv.{paper.arxiv_id}",
        "archiveID": f"arXiv:{paper.arxiv_id}",
        "repository": "arXiv",
        "extra": "\n".join(extra_lines),
        "tags": tags,
        "attachments": [],
    }


def zotero_import(paper: Paper, sleep: float, force: bool = False, attach_pdf: bool = False) -> None:
    exists, citekey = zotero_search_existing(paper)
    if exists and not force:
        paper.zotero_status = "existing"
        paper.zotero_citekey = citekey
        return

    safe_id = re.sub(r"[^A-Za-z0-9]", "", paper.arxiv_id)
    connector_id = f"codex{safe_id}"
    attachment_id = f"pdf{safe_id}"
    session_id = f"codex3d4d{safe_id}{int(time.time() * 1000) % 100000}"
    item = zotero_item_json(paper, connector_id)
    payload = json.dumps({
        "sessionID": session_id,
        "uri": paper.abs_url,
        "items": [item],
    }).encode()
    request_bytes(
        f"{ZOTERO}/connector/saveItems",
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST",
        timeout=60,
    )
    if attach_pdf and paper.pdf_path and Path(paper.pdf_path).exists():
        pdf = Path(paper.pdf_path).read_bytes()
        metadata = {
            "id": attachment_id,
            "url": paper.pdf_url,
            "contentType": "application/pdf",
            "parentItemID": connector_id,
            "title": "Full Text PDF",
        }
        request_bytes(
            f"{ZOTERO}/connector/saveAttachment?sessionID={urllib.parse.quote(session_id)}",
            data=pdf,
            headers={"Content-Type": "application/pdf", "X-Metadata": json.dumps(metadata)},
            method="POST",
            timeout=120,
        )
    paper.zotero_status = "imported"
    time.sleep(sleep)


def write_bibtex(papers: list[Paper], path: Path) -> None:
    lines: list[str] = []
    for paper in papers:
        key = f"{slugify((paper.authors[0].split()[-1] if paper.authors else 'anon') + str(paper.year), 30)}_{paper.arxiv_id.replace('.', '')}"
        fields = {
            "title": paper.title,
            "author": " and ".join(paper.authors),
            "year": str(paper.year),
            "eprint": paper.arxiv_id,
            "archivePrefix": "arXiv",
            "primaryClass": paper.categories[0] if paper.categories else "",
            "doi": paper.doi or f"10.48550/arXiv.{paper.arxiv_id}",
            "url": paper.abs_url,
            "abstract": paper.abstract,
            "keywords": ", ".join(paper.tags + paper.categories),
        }
        lines.append(f"@misc{{{key},")
        for name, value in fields.items():
            if value:
                escaped = value.replace("{", "\\{").replace("}", "\\}")
                lines.append(f"  {name} = {{{escaped}}},")
        lines.append("}\n")
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out-dir", default="paper_collection_3d4d_reconstruction_2026_04_26")
    parser.add_argument("--skip-fetch", action="store_true")
    parser.add_argument("--skip-pdf", action="store_true")
    parser.add_argument("--skip-zotero", action="store_true")
    parser.add_argument("--force-zotero-duplicates", action="store_true")
    parser.add_argument("--zotero-attach-pdf", action="store_true",
                        help="Copy PDFs into Zotero storage as attachments. Off by default to avoid duplicating many GB.")
    parser.add_argument("--sleep", type=float, default=3.0)
    args = parser.parse_args()

    out_dir = Path(args.out_dir).resolve()
    metadata_dir = out_dir / "metadata"
    pdf_dir = out_dir / "pdfs"
    metadata_dir.mkdir(parents=True, exist_ok=True)

    all_papers: list[Paper] = []
    if not args.skip_fetch:
        for set_name in ["cs", "eess"]:
            all_papers.extend(fetch_oai_range(metadata_dir.parent, set_name, dt.date(2026, 1, 1), TODAY, args.sleep))
    else:
        for cache in (metadata_dir).glob("oai_*.xml"):
            chunks = cache.read_bytes().split(b"\n<!-- CODEx-OAI-CHUNK -->\n")
            for chunk in chunks:
                if not chunk.strip():
                    continue
                root = ET.fromstring(chunk)
                for record in root.findall(".//oai:record", OAI_NS):
                    paper = parse_record(record)
                    if paper:
                        all_papers.append(paper)

    selected: list[Paper] = []
    for paper in dedupe(all_papers):
        # "2026 work on arXiv" is interpreted as 2026 arXiv IDs (2601-2604
        # as of 2026-04-26), not older IDs that merely received 2026 revisions.
        if not re.match(r"^260[1-4]\.", paper.arxiv_id):
            continue
        if not (set(paper.categories) & RELEVANT_CATEGORIES):
            continue
        include, tags, reason = classify(paper)
        if include:
            paper.source_group = "2026-arxiv"
            paper.tags = tags
            paper.reason = reason
            selected.append(paper)

    for arxiv_id, note in CURATED_OLD_ARXIV_IDS.items():
        paper = fetch_oai_id(arxiv_id)
        time.sleep(args.sleep)
        if not paper:
            continue
        include, tags, reason = classify(paper)
        # Curated seeds are intentionally included even if the automatic filter is conservative.
        paper.source_group = "curated-pre2026"
        paper.reason = note if not include else f"{note}; {reason}"
        paper.tags = sorted(set(tags + ["Codex:3D4D-Reconstruction"]))
        selected.append(paper)

    selected = dedupe(selected)
    for paper in selected:
        paper.pdf_path = str(pdf_destination(paper, pdf_dir))
    manifest = metadata_dir / "papers_manifest.json"
    manifest.write_text(json.dumps([asdict(p) for p in selected], ensure_ascii=False, indent=2), encoding="utf-8")
    tsv = metadata_dir / "papers_manifest.tsv"
    with tsv.open("w", encoding="utf-8") as f:
        f.write("arxiv_id\tyear\tsource_group\ttags\ttitle\tauthors\tcategories\tpdf_path\tzotero_status\n")
        for p in selected:
            f.write("\t".join([
                p.arxiv_id,
                str(p.year),
                p.source_group,
                ",".join(p.tags),
                p.title,
                "; ".join(p.authors),
                " ".join(p.categories),
                p.pdf_path or "",
                p.zotero_status or "",
            ]) + "\n")
    write_bibtex(selected, metadata_dir / "papers.bib")

    if not args.skip_pdf:
        for i, paper in enumerate(selected, start=1):
            sys.stderr.write(f"[{i}/{len(selected)}] PDF {paper.arxiv_id} {paper.title[:80]}\n")
            sys.stderr.flush()
            try:
                download_pdf(paper, pdf_dir, args.sleep)
            except Exception as exc:
                sys.stderr.write(f"PDF failed {paper.arxiv_id}: {exc}\n")
        manifest.write_text(json.dumps([asdict(p) for p in selected], ensure_ascii=False, indent=2), encoding="utf-8")

    if not args.skip_zotero:
        for i, paper in enumerate(selected, start=1):
            sys.stderr.write(f"[{i}/{len(selected)}] Zotero {paper.arxiv_id} {paper.title[:80]}\n")
            sys.stderr.flush()
            try:
                zotero_import(paper, args.sleep, args.force_zotero_duplicates, args.zotero_attach_pdf)
            except Exception as exc:
                paper.zotero_status = f"failed: {exc}"
                sys.stderr.write(f"Zotero failed {paper.arxiv_id}: {exc}\n")
        manifest.write_text(json.dumps([asdict(p) for p in selected], ensure_ascii=False, indent=2), encoding="utf-8")
        with tsv.open("w", encoding="utf-8") as f:
            f.write("arxiv_id\tyear\tsource_group\ttags\ttitle\tauthors\tcategories\tpdf_path\tzotero_status\n")
            for p in selected:
                f.write("\t".join([
                    p.arxiv_id,
                    str(p.year),
                    p.source_group,
                    ",".join(p.tags),
                    p.title,
                    "; ".join(p.authors),
                    " ".join(p.categories),
                    p.pdf_path or "",
                    p.zotero_status or "",
                ]) + "\n")

    print(f"Selected papers: {len(selected)}")
    print(f"Manifest: {manifest}")
    print(f"PDF dir: {pdf_dir}")


if __name__ == "__main__":
    main()
