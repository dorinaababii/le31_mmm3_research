#!/usr/bin/env python3
"""Dump abstract_inverted_index for each OpenAlex candidate pick."""
import json
from pathlib import Path

OUTDIR = Path("/tmp/le31-brainstorm-2026-08-29")
arxiv_files = list((OUTDIR / "arxiv_verify").glob("*.json"))

want_ids = ["W7204450379"]  # Separating Disclosure from Authorization
for f in arxiv_files:
    try:
        d = json.loads(f.read_text())
    except Exception:
        continue
    wid = (d.get("id") or "")
    if wid.startswith("https://openalex.org/W"):
        want_ids.append(wid.replace("https://openalex.org/", ""))

def find_id(want_id):
    for d in (OUTDIR / "openalex", OUTDIR / "arxiv_verify"):
        if not d.exists():
            continue
        for f in d.glob("*.json"):
            try:
                data = json.loads(f.read_text())
            except Exception:
                continue
            rid = data.get("id") or ""
            if rid.endswith(want_id):
                return f, data
    return None, None

for w in want_ids:
    found, data = find_id(w)
    if not found:
        print(f"NOT_FOUND: {w}")
        continue
    inv = data.get("abstract_inverted_index")
    if inv is None:
        print(f"{w}: abstract_inverted_index=null (skipping)")
        continue
    out_path = OUTDIR / f"openalex_abstract_{w}.json"
    out_path.write_text(json.dumps(inv, indent=2, sort_keys=True))
    print(f"{w} -> {out_path}  ({len(inv)} word entries)  title={(data.get('title') or 'n/a')[:90]}")
