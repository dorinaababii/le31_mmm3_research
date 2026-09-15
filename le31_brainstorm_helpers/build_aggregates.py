#!/usr/bin/env python3
"""Build _AGGREGATES.json from all raw third-party fetches in /tmp/le31-brainstorm-2026-08-29/."""
import json
from pathlib import Path
from datetime import datetime

OUTDIR = Path("/tmp/le31-brainstorm-2026-08-29")

aggregates = {
    "window": {
        "from": "2026-07-30T00:00:00Z",
        "to": "2026-08-29T06:51:00Z",
        "epoch_from": 1785369600,
        "epoch_to": 1788399060,
    },
    "hn": {},
    "github_search": {},
    "github_direct": {},
    "openalex": {},
    "arxiv_verify": {},
    "producthunt": {},
    "sciencedirect": {"status": "BLOCKED per spec, not attempted", "marker_path": "sd_BLOCKED.txt"},
}

# HN
hn_dir = OUTDIR / "hn"
if hn_dir.exists():
    for f in sorted(hn_dir.glob("*.json")):
        try:
            d = json.loads(f.read_text())
        except Exception:
            continue
        name = f.name
        # Extract query slug (everything before _<shortsha>.json)
        slug = name.rsplit("_", 1)[0]
        aggregates["hn"][slug] = {
            "path": str(f.relative_to(OUTDIR)),
            "http": 200,
            "nbHits": d.get("nbHits", 0),
            "hits_returned": len(d.get("hits", [])),
        }

# GitHub search
gh_dir = OUTDIR / "gh"
if gh_dir.exists():
    for f in sorted(gh_dir.glob("*.json")):
        if f.name.startswith("_FAIL") or "_FAIL_" in f.name:
            continue
        try:
            d = json.loads(f.read_text())
        except Exception:
            continue
        if "items" in d:
            name = f.name
            slug = name.rsplit("_", 1)[0]
            aggregates["github_search"][slug] = {
                "path": str(f.relative_to(OUTDIR)),
                "http": 200,
                "total_count": d.get("total_count", 0),
                "items_returned": len(d.get("items", [])),
            }

# GitHub direct
if gh_dir.exists():
    for f in sorted(gh_dir.glob("direct_*.json")):
        try:
            d = json.loads(f.read_text())
        except Exception:
            continue
        name = f.name
        if not (d.get("full_name") and "stargazers_count" in d):
            continue
        try:
            ca = datetime.fromisoformat(d["created_at"].replace("Z", "+00:00"))
            pa = datetime.fromisoformat(d["pushed_at"].replace("Z", "+00:00"))
        except Exception:
            ca = pa = None
        win_from = datetime.fromisoformat("2026-07-30T00:00:00+00:00")
        win_to = datetime.fromisoformat("2026-08-29T06:51:00+00:00")
        in_window = "in_window:" + (
            "CREATE" if ca and win_from <= ca <= win_to else "no_create"
        ) + "/" + (
            "PUSH" if pa and win_from <= pa <= win_to else "no_push"
        )
        lic = (d.get("license") or {}).get("spdx_id") if d.get("license") else None
        aggregates["github_direct"][d["full_name"]] = {
            "path": str(f.relative_to(OUTDIR)),
            "http": 200,
            "stargazers_count": d.get("stargazers_count"),
            "forks_count": d.get("forks_count"),
            "language": d.get("language"),
            "license_spdx_id": lic,
            "created_at": d.get("created_at"),
            "pushed_at": d.get("pushed_at"),
            "description": d.get("description"),
            "topics": d.get("topics"),
            "html_url": d.get("html_url"),
            "in_window": in_window,
        }

# OpenAlex
oa_dir = OUTDIR / "openalex"
if oa_dir.exists():
    for f in sorted(oa_dir.glob("*.json")):
        try:
            d = json.loads(f.read_text())
        except Exception:
            continue
        name = f.name
        slug = name.rsplit("_", 1)[0]
        aggregates["openalex"][slug] = {
            "path": str(f.relative_to(OUTDIR)),
            "http": 200,
            "meta_count": d.get("meta", {}).get("count", 0),
            "results_returned": len(d.get("results", [])),
        }

# arxiv_verify
av_dir = OUTDIR / "arxiv_verify"
if av_dir.exists():
    for f in sorted(av_dir.glob("*.json")):
        try:
            d = json.loads(f.read_text())
        except Exception:
            continue
        name = f.name
        if "FAIL" in name:
            aggregates["arxiv_verify"][name] = {"path": str(f.relative_to(OUTDIR)), "resolved": False}
            continue
        if "openalex.org/W" in str(d.get("id", "")):
            wid = d["id"].split("/")[-1]
            aggregates["arxiv_verify"][wid] = {
                "path": str(f.relative_to(OUTDIR)),
                "resolved": True,
                "title": d.get("title"),
                "publication_date": d.get("publication_date"),
                "doi": (d.get("ids") or {}).get("doi") or d.get("doi"),
                "abstract_inverted_index_dump": f"openalex_abstract_{wid}.json",
            }

# ProductHunt
ph_dir = OUTDIR / "producthunt"
if ph_dir.exists():
    for f in sorted(ph_dir.glob("ph_*")):
        if f.name.startswith("_failures"):
            continue
        text = f.read_text(errors="ignore")
        if "cf403" in f.name:
            aggregates["producthunt"][f.name] = {
                "path": str(f.relative_to(OUTDIR)),
                "http": 403,
                "body_kind": "cloudflare_challenge_html",
            }
        else:
            entries = text.count("<entry>")
            aggregates["producthunt"][f.name] = {
                "path": str(f.relative_to(OUTDIR)),
                "http": 200,
                "entry_count": entries,
            }

agg_path = OUTDIR / "_AGGREGATES.json"
agg_path.write_text(json.dumps(aggregates, indent=2, default=str))
print(f"Wrote {agg_path} ({agg_path.stat().st_size} bytes)")
print(json.dumps({k: list(v.keys())[:5] for k, v in aggregates.items()}, indent=2))
