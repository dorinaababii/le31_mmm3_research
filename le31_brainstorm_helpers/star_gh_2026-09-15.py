#!/usr/bin/env python3
"""LE31 brainstorm 2026-09-15 — star-sorted GitHub Search to find any popular
in-domain Python repo that was updated recently enough.
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

WINDOW = datetime(2026, 8, 16, tzinfo=timezone.utc)
OUTDIR = "/tmp/le31-brainstorm-2026-09-15/_parent_recheck"

# Star-sorted, no push filter — see if any popular in-domain Python repo exists
QUERIES = [
    ("star_telegram-bot_py",      "telegram-bot+language:python"),
    ("star_restaurant_py",       "restaurant+language:python"),
    ("star_pos_py",              "pos+language:python"),
    ("star_kitchen_py",          "kitchen+language:python"),
    ("star_append-only_py",      "append-only+language:python"),
    ("star_small-business_py",   "small-business+language:python"),
    ("star_food_py",             "food+language:python"),
    ("star_hci_py",              "hci+language:python"),
    ("star_low_effort_py",       "low-effort+language:python"),
    ("star_solo_py",             "solo+language:python"),
    ("star_micro_saas_py",       "micro-saas+language:python"),
    ("star_aiogram_py",          "aiogram+language:python"),
]


def fetch(q, per_page=30, sort="stars"):
    url = "https://api.github.com/search/repositories?" + urlencode({
        "q": q, "sort": sort, "order": "desc", "per_page": per_page
    })
    req = Request(url, headers=HEADERS)
    with urlopen(req, timeout=20) as r:
        return json.loads(r.read())


for slug, q in QUERIES:
    try:
        d = fetch(q, sort="stars")
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
    print(f"\n=== {slug} (q='{q}')  total={tc}  in-window-by-push (of {len(items)} shown)={len(in_window)} ===")
    for i in in_window[:5]:
        lic = (i.get("license") or {}).get("spdx_id", "NONE")
        pushed = (i.get("pushed_at") or "")[:10]
        lang = i.get("language") or ""
        desc = (i.get("description") or "")[:80]
        print(f"  - {i['full_name']:40s} | {i['stargazers_count']:>4}★ {i['forks_count']:>3}⑂ | {lic:12s} | pushed={pushed} | {lang:8s} | {desc}")
    time.sleep(1.5)