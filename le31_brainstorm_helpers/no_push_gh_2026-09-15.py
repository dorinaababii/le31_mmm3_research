#!/usr/bin/env python3
"""LE31 brainstorm 2026-09-15 — broader no-push GitHub Search walks.

After the parent confirmed the `pushed:` qualifier is structurally returning
0 today (2026-09-15), fall back to: full search index (no pushed: filter),
then parent-side filters by `pushed_at` >= 2026-08-16.
"""
import json, os, time
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from datetime import datetime, timezone

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

# No-push version of each spec query — parent filters pushed_at >= 2026-08-16
QUERIES = [
    ("np_topic_small-business",    "topic:small-business+language:python"),
    ("np_topic_hci",               "topic:hci+language:python"),
    ("np_topic_real-time",         "topic:real-time+language:python"),
    ("np_topic_append-only",       "topic:append-only+language:python"),
    ("np_topic_telegram-bot",      "topic:telegram-bot+language:python"),
    ("np_restaurant_kitchen",      "restaurant+kitchen+language:python"),
    ("np_htmx_no-build",           "htmx+no-build+language:python"),
    # broader still
    ("np_small-business_py",       "small-business+language:python"),
    ("np_append-only_py",       "append-only+language:python"),
    ("np_hci_py",                  "hci+language:python"),
    ("np_real-time_py",            "real-time+language:python"),
    ("np_htmx_py",                 "htmx+language:python"),
    ("np_telegram-bot_py",         "telegram-bot+language:python"),
    ("np_restaurant_py",           "restaurant+language:python"),
    ("np_pos_py",                  "pos+language:python"),
    ("np_kitchen_py",              "kitchen+language:python"),
    ("np_food_py",                 "food+language:python"),
    ("np_telegram-restaurant_py",  "telegram+restaurant+language:python"),
]

OUTDIR = "/tmp/le31-brainstorm-2026-09-15/_parent_recheck"
os.makedirs(OUTDIR, exist_ok=True)
WINDOW = datetime(2026, 8, 16, tzinfo=timezone.utc)

PER_PAGE = 30  # fetch first 30 per query for in-window inspection


def fetch(q, per_page=PER_PAGE):
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
    items = d.get("items", [])
    in_window = []
    for i in items:
        pushed = i.get("pushed_at") or ""
        try:
            pushed_dt = datetime.fromisoformat(pushed.replace("Z", "+00:00"))
        except Exception:
            continue
        if pushed_dt >= WINDOW:
            in_window.append(i)
    raw_path = os.path.join(OUTDIR, slug + ".json")
    with open(raw_path, "w") as f:
        json.dump(d, f, indent=2)
    msg = d.get("message", "")
    print(f"\n{tc!s:>6} total | {len(in_window):>3} in-window-by-push (returned {len(items)}) | {slug} (q='{q}'){'  msg='+msg if msg else ''}")
    for i in in_window[:6]:
        lic = (i.get("license") or {}).get("spdx_id", "NONE")
        pushed = (i.get("pushed_at") or "")[:10]
        created = (i.get("created_at") or "")[:10]
        lang = i.get("language") or ""
        desc = (i.get("description") or "")[:90]
        print(f"     - {i['full_name']:38s} | {i['stargazers_count']:>3}★ {i['forks_count']:>2}⑂ | {lic:12s} | pushed={pushed} created={created} | {lang:8s} | {desc}")
    time.sleep(1.2)