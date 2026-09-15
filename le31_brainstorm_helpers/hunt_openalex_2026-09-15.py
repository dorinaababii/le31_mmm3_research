#!/usr/bin/env python3
"""LE31 brainstorm 2026-09-15 — last-pass hunt for any LE31-shape academic
paper that maps onto the charter §3.1 / §3.4 / §3.2 gates and isn't already
filed.

Constraints:
- NOT in features 121..181 (already filed as architecture-reference)
- In window 2026-08-16..2026-09-15
- Not by a generative-spam author (verify self-citations vs external)
- Maps onto LE31 primitive (operator UX / append-only / explicit-state)
- §3.4-clean (no customer-facing AI; owner/staff AI allowed)
"""
import json, os, time
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from datetime import datetime, timezone

HEADERS = {"User-Agent": "le31-brainstorm-2026-09-15 (mailto=openalex-team@ourresearch.org)"}

WINDOW_START = datetime(2026, 8, 16, tzinfo=timezone.utc)
WINDOW_END = datetime(2026, 9, 15, 23, 59, 59, tzinfo=timezone.utc)
OUTDIR = "/tmp/le31-brainstorm-2026-09-15/_parent_recheck"
os.makedirs(OUTDIR, exist_ok=True)


def fetch(q, per_page=20, page=1, sort="cited_by_count:desc"):
    base = "https://api.openalex.org/works"
    params = {
        "search": q,
        "filter": "from_publication_date:2026-08-16,to_publication_date:2026-09-15",
        "per_page": per_page, "page": page, "sort": sort,
    }
    url = base + "?" + urlencode(params)
    req = Request(url, headers=HEADERS)
    with urlopen(req, timeout=30) as r:
        return json.loads(r.read())


# Targeted hunts:
# - operator UX for AI-assisted tools (charter §3.4 allows owner/staff AI)
# - human-in-the-loop / explicitness design principles
# - low-effort operator surfaces
# - auditability of operator decisions (not customer-facing)
QUERIES = [
    ("hunt_operator_ux_ai",     "operator ux ai-assisted"),
    ("hunt_human_in_the_loop",  "human in the loop accountability"),
    ("hunt_workflow_audit",     "workflow audit ledger"),
    ("hunt_small_team_dashboard","small team dashboard"),
    ("hunt_one_owner_saas",    "one owner saas"),
    ("hunt_offline_first_pos",  "offline first pos"),
    ("hunt_audit_log_sme",      "audit log small business"),
    ("hunt_solo_restaurant",    "solo restaurant software"),
    ("hunt_kitchen_safety_log", "kitchen safety log"),
    ("hunt_append_only_audit_log", "append-only audit log"),
    ("hunt_explicit_transition", "explicit transition operator"),
    ("hunt_ergonomics_kitchen", "ergonomics small restaurant"),
]


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
    for r in in_window[:6]:
        doi = (r.get("doi") or "").replace("https://doi.org/", "")[:48]
        title = (r.get("title") or "")[:90]
        cited = r.get("cited_by_count", 0)
        pub = (r.get("publication_date") or "")[:10]
        rtype = r.get("type", "?")
        authors = ", ".join(
            (a.get("author", {}).get("display_name") or "?")
            for a in (r.get("authorships") or [])[:2]
        )
        print(f"  - {pub} | cit={cited:>3} | {rtype:18s} | {doi:48s} | {authors[:30]:30s} | {title}")
    time.sleep(1.0)