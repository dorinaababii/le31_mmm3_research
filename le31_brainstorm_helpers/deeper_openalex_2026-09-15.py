#!/usr/bin/env python3
"""LE31 brainstorm 2026-09-15 — deeper pages of productive queries."""
import json, os, time
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from datetime import datetime, timezone

HEADERS = {"User-Agent": "le31-brainstorm-2026-09-15 (mailto=openalex-team@ourresearch.org)"}

WINDOW_START = datetime(2026, 8, 16, tzinfo=timezone.utc)
WINDOW_END = datetime(2026, 9, 15, 23, 59, 59, tzinfo=timezone.utc)
OUTDIR = "/tmp/le31-brainstorm-2026-09-15/_parent_recheck"


def fetch(q, per_page=20, page=1, sort="cited_by_count:desc"):
    base = "https://api.openalex.org/works"
    params = {
        "search": q,
        "filter": "from_publication_date:2026-08-16,to_publication_date:2026-09-15",
        "per_page": per_page,
        "page": page,
        "sort": sort,
    }
    url = base + "?" + urlencode(params)
    req = Request(url, headers=HEADERS)
    with urlopen(req, timeout=30) as r:
        return json.loads(r.read())


# Sort by cited_by_count:desc is default; first page shows top-cited.
# Page 2 may have lower-cited but still relevant papers.
QUERIES = [
    ("deep_append_only_audit_p2",  "append-only audit", 20, 2),
    ("deep_append_only_audit_p3",  "append-only audit", 20, 3),
    ("deep_event_sourcing_p2",     "event sourcing",   20, 2),
    ("deep_oa_append_only_p2",     "append-only ledger", 20, 2),
    ("deep_oa_append_only_p3",     "append-only ledger", 20, 3),
    # Sort by date to get freshest hits regardless of citation count
    ("fresh_append_only_audit",    "append-only audit", 20, 1),
    ("fresh_event_sourcing",       "event sourcing",   20, 1),
    ("fresh_append_only_ledger",   "append-only ledger", 20, 1),
]

for slug, q, pp, page in QUERIES:
    sort = "publication_date:desc" if slug.startswith("fresh_") else "cited_by_count:desc"
    try:
        d = fetch(q, per_page=pp, page=page, sort=sort)
    except Exception as e:
        print(f"ERROR  {q} p{page}  -> {e}")
        continue
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
    raw_path = os.path.join(OUTDIR, slug + ".json")
    with open(raw_path, "w") as f:
        json.dump(d, f, indent=2)
    print(f"\n=== {slug} (q='{q}', p={page}, sort={sort})  meta.count={meta.get('count')}  in_page={len(in_window)} ===")
    for r in in_window[:10]:
        doi = (r.get("doi") or "").replace("https://doi.org/", "")[:48]
        title = (r.get("title") or "")[:90]
        cited = r.get("cited_by_count", 0)
        pub = (r.get("publication_date") or "")[:10]
        oa = (r.get("open_access") or {}).get("oa_status", "?")
        rtype = r.get("type", "?")
        authors = ", ".join(
            (a.get("author", {}).get("display_name") or "?")
            for a in (r.get("authorships") or [])[:2]
        )
        print(f"  - {pub} | cit={cited:>3} | oa={oa:6s} | {rtype:18s} | {doi:48s} | {authors[:30]:30s} | {title}")
    time.sleep(1.0)