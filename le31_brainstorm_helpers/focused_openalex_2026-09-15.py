#!/usr/bin/env python3
"""LE31 brainstorm 2026-09-15 — focused OpenAlex queries to find cross-section
papers that map onto LE31's append-only / ledger / operator / solo / SME axis.
"""
import json, os, time
from urllib.parse import urlencode, quote
from urllib.request import Request, urlopen
from datetime import datetime, timezone

TOKEN = os.environ.get("HERMES_GITHUB_TOKEN")  # not needed for OpenAlex
HEADERS = {
    "User-Agent": "le31-brainstorm-2026-09-15 (mailto=openalex-team@ourresearch.org)",
}

QUERIES = [
    # LE31-adjacent queries (all in window 2026-08-16..2026-09-15)
    ("oa_append_only_ledger",        "append-only ledger"),
    ("oa_append_only_audit_log",     "append-only audit"),
    ("oa_event_sourcing",            "event sourcing"),
    ("oa_solo_operator_software",    "solo operator software"),
    ("oa_solo_owner_saas",           "solo owner saas"),
    ("oa_phone_first_pos",           "phone first point of sale"),
    ("oa_small_kitchen_workflow",    "small kitchen workflow"),
    ("oa_solo_founder_ux",           "solo founder ux"),
    ("oa_low_effort_ux_operator",    "low effort ux operator"),
    ("oa_restaurant_append_only",    "restaurant append only"),
]

OUTDIR = "/tmp/le31-brainstorm-2026-09-15/_parent_recheck"
os.makedirs(OUTDIR, exist_ok=True)
WINDOW_START = datetime(2026, 8, 16, tzinfo=timezone.utc)
WINDOW_END = datetime(2026, 9, 15, 23, 59, 59, tzinfo=timezone.utc)


def fetch(q, per_page=20):
    base = "https://api.openalex.org/works"
    params = {
        "search": q,
        "filter": "from_publication_date:2026-08-16,to_publication_date:2026-09-15",
        "per_page": per_page,
        "sort": "cited_by_count:desc",
    }
    url = base + "?" + urlencode(params)
    req = Request(url, headers=HEADERS)
    with urlopen(req, timeout=30) as r:
        return json.loads(r.read())


for slug, q in QUERIES:
    try:
        d = fetch(q)
    except Exception as e:
        print(f"ERROR  {q}  -> {e}")
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
    print(f"\n=== {slug} (q='{q}')  meta.count={meta.get('count')}  in_page={len(in_window)} ===")
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