#!/usr/bin/env python3
"""Check citations of the Burned Page paper (W7207792450) and Co-Performance paper (the new one)."""
import json, time
from urllib.request import Request, urlopen

HEADERS = {"User-Agent": "le31-brainstorm-2026-09-15 (mailto=openalex-team@ourresearch.org)"}

WORKS = [
    ("burned-page",       "W7207792450"),
    ("co-performance",    "W4405748457"),  # placeholder; will resolve below
]


def fetch(url):
    req = Request(url, headers=HEADERS)
    with urlopen(req, timeout=30) as r:
        return json.loads(r.read())


# Resolve the OpenAlex ID for the Co-Performance paper
d = json.load(open("/tmp/le31-brainstorm-2026-09-15/openalex-restaurant-hci.json"))
for r in d["results"]:
    if "Disentangling Innovation Practices" in (r.get("title") or ""):
        print(f"Co-Performance paper OpenAlex ID: {r.get('id')}")
        print(f"  cited_by_count: {r.get('cited_by_count')}")
        works_list = list(WORKS)
        for i, (n, _) in enumerate(works_list):
            if n == "co-performance":
                works_list[i] = (n, r.get("id").split("/")[-1])
        WORKS = works_list

# Resolve the Burned Page paper
d2 = json.load(open("/tmp/le31-brainstorm-2026-09-15/_parent_recheck/oa_append_only_ledger.json"))
for r in d2["results"]:
    if "Burned Page" in (r.get("title") or ""):
        print(f"Burned Page OpenAlex ID: {r.get('id')}, cited_by_count: {r.get('cited_by_count')}")

print()

# Check citations
for name, wid in WORKS:
    url = f"https://api.openalex.org/works?filter=cites:{wid}&per_page=20"
    d = fetch(url)
    print(f"\n=== Citing {name} ({wid})  count={d.get('meta',{}).get('count')} ===")
    for r in d.get("results", [])[:10]:
        a = r.get("authorships", [{}])[0].get("author", {}).get("display_name", "?")
        print(f"  - {a:30s} | {r.get('publication_date')} | cit={r.get('cited_by_count',0):>3} | {r.get('title')[:70]}")
    time.sleep(1)