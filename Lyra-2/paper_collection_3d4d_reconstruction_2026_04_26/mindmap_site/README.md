# 3D/4D Reconstruction Mindmap Website

Static local website for browsing the 839-paper 3D/4D reconstruction taxonomy.

## Run

From the collection root:

```bash
cd /Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2/paper_collection_3d4d_reconstruction_2026_04_26
python3 -m http.server 8765
```

Open:

```text
http://localhost:8765/mindmap_site/
```

## What It Shows

- Motivation -> angle -> subproblem -> solution family -> paper hierarchy
- Search and dropdown filters
- Pan/zoom SVG mindmap
- Paper cards with method diagram, one-line summary, PDF link, and code candidate link

## Rebuild Data

If `boardmix_cards.csv` changes:

```bash
cd /Volumes/UBag/Documents/l40server_mirror/lyra/Lyra-2
python3 tools/build_mindmap_website.py
```

The rebuild step creates `mindmap-data.json` and compressed JPEG figure assets
under `assets/figures/`. PDF links point to arXiv so the site does not need to
ship the local 12 GB PDF folder.
