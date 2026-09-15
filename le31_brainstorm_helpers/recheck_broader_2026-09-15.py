#!/usr/bin/env python3
"""LE31 brainstorm 2026-09-15 — broader parent re-walk.

After the spec queries all return total_count=0, broaden:
- No `topic:` qualifier on language:python (broader small-business)
- No `pushed:` filter (entire index)
- Drop `language:python` to see whether the index has anything
- Try `created:>2026-08-16` instead of `pushed:` (catches fresh repos that
  have never been pushed but were created in window)
"""
import json, os, time
from urllib.parse import urlencode
from urllib.request import Request, urlopen

TOKEN = (
    os.environ.get("HERMES_GITHUB_TOKEN")
    or open("/opt/data/.env").read().split("HERMES_GITHUB_TOKEN=")[1].split("\n")[0]
)
HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28",
    "User-Agent": "le31-brainstorm-2026-09-15",
}

QUERIES = [
    # Broader: just language:python + push, no topic
    ("broader_small-business",     "small-business+language:python+pushed:>2026-08-15"),
    ("broader_hci",                "hci+language:python+pushed:>2026-08-15"),
    ("broader_htmx",               "htmx+language:python+pushed:>2026-08-15"),
    ("broader_telegram-bot",       "telegram-bot+language:python+pushed:>2026-08-15"),
    ("broader_append-only",        "append-only+language:python+pushed:>2026-08-15"),
    ("broader_real-time",          "real-time+language:python+pushed:>2026-08-15"),
    ("broader_restaurant",         "restaurant+language:python+pushed:>2026-08-15"),
    ("broader_kitchen",            "kitchen+language:python+pushed:>2026-08-15"),
    ("broader_pos",                "pos+language:python+pushed:>2026-08-15"),
    # created: filter
    ("broader_small-business_created",  "small-business+language:python+created:>2026-08-15"),
    ("broader_hci_created",             "hci+language:python+created:>2026-08-15"),
    ("broader_append-only_created",     "append-only+language:python+created:>2026-08-15"),
    # No language filter
    ("any-lang_small-business_pushed",  "small-business+pushed:>2026-08-15"),
    ("any-lang_htmx_pushed",            "htmx+pushed:>2026-08-15"),
]

OUTDIR = "/tmp/le31-brainstorm-2026-09-15/_parent_recheck"
os.makedirs(OUTDIR, exist_ok=True)


def fetch(q, per_page=10):
    url = "https://api.github.com/search/repositories?" + urlencode({
        "q": q, "sort": "updated", "order": "desc", "per_page": per_page
    })
    req = Request(url, headers=HEADERS)
    with urlopen(req, timeout=20) as r:
        return json.loads(r.read())


for slug, q in QUERIES:
    try:
        d = fetch(q)
    except Exception as e:
        print(f"ERROR  {q}  -> {e}")
        continue
    tc = d.get("total_count")
    inc = d.get("incomplete_results")
    msg = d.get("message", "")
    raw_path = os.path.join(OUTDIR, slug + ".json")
    with open(raw_path, "w") as f:
        json.dump(d, f, indent=2)
    items = d.get("items", [])
    print(f"\n{tc!s:>6} | inc={inc} | {slug} (q='{q}'){'  msg='+msg if msg else ''}")
    for i in items[:5]:
        lic = (i.get("license") or {}).get("spdx_id", "NONE")
        pushed = (i.get("pushed_at") or "")[:10]
        created = (i.get("created_at") or "")[:10]
        lang = i.get("language") or ""
        desc = (i.get("description") or "")[:90]
        print(f"     - {i['full_name']:38s} | {i['stargazers_count']:>3}★ {i['forks_count']:>2}⑂ | {lic:12s} | pushed={pushed} created={created} | {lang:8s} | {desc}")
    time.sleep(0.7)