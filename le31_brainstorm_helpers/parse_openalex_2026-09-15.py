#!/usr/bin/env python3
"""LE31 brainstorm 2026-09-15 — OpenAlex per-query inspection.
For each of the 5 queries, print top-10 papers by cited_by_count with the
verifiable fields (id, doi, title, pub_date, cited_by_count, type, open_access).
"""
import json, os
from datetime import datetime, timezone

OUTDIR = "/tmp/le31-brainstorm-2026-09-15"

WINDOW_START = datetime(2026, 8, 16, tzinfo=timezone.utc)
WINDOW_END = datetime(2026, 9, 15, 23, 59, 59, tzinfo=timezone.utc)

QUERIES = [
    "openalex-creativity-product.json",
    "openalex-restaurant-hci.json",
    "openalex-htmx-no-build-spa.json",
    "openalex-small-business-operator.json",
    "openalex-kitchen-kds-usability.json",
]

for fname in QUERIES:
    path = os.path.join(OUTDIR, fname)
    if not os.path.exists(path):
        print(f"MISSING {path}")
        continue
    with open(path) as f:
        d = json.load(f)
    meta = d.get("meta", {})
    results = d.get("results", [])
    in_window = []
    for r in results:
        pub = r.get("publication_date") or ""
        try:
            pub_dt = datetime.fromisoformat(pub).replace(tzinfo=timezone.utc)
        except Exception:
            continue
        if WINDOW_START <= pub_dt <= WINDOW_END:
            in_window.append(r)
    print(f"\n=== {fname} ===")
    print(f"  meta.count={meta.get('count')}  in returned-page-of-20: {len(in_window)}")
    for r in in_window[:15]:
        doi = (r.get("doi") or "").replace("https://doi.org/", "")[:50]
        title = (r.get("title") or "")[:90]
        cited = r.get("cited_by_count", 0)
        pub = (r.get("publication_date") or "")[:10]
        authors = ", ".join(
            (a.get("author", {}).get("display_name") or "?")
            for a in (r.get("authorships") or [])[:2]
        )
        oa = (r.get("open_access") or {}).get("oa_status", "?")
        rtype = r.get("type", "?")
        print(f"  - {pub} | cit={cited:>4} | oa={oa:6s} | {rtype:18s} | {doi:50s} | {authors[:30]:30s} | {title}")