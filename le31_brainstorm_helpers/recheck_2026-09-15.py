#!/usr/bin/env python3
"""LE31 brainstorm 2026-09-15 — parent re-walk of GitHub Search totals.

Re-runs each of the 8 spec queries + 2 control queries that mirror the
2026-09-14 daily-research baseline, prints total_count + the top in-window
items per query. Saves raw JSON to /tmp/le31-brainstorm-2026-09-15/_parent_recheck/.
"""
import json, os, time, sys
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
    # spec queries
    ("gh_topic_small-business_lang_py_pushed",  "topic:small-business+language:python+pushed:>2026-08-15"),
    ("gh_topic_hci_lang_py_pushed",            "topic:hci+language:python+pushed:>2026-08-15"),
    ("gh_topic_mobile-ux_pushed",              "topic:mobile-ux+pushed:>2026-08-15"),
    ("gh_topic_real-time_lang_py_pushed",      "topic:real-time+language:python+pushed:>2026-08-15"),
    ("gh_topic_append-only_lang_py_pushed",    "topic:append-only+language:python+pushed:>2026-08-15"),
    ("gh_topic_telegram-bot_lang_py_pushed",   "topic:telegram-bot+language:python+pushed:>2026-08-15"),
    ("gh_restaurant_kitchen_lang_py_pushed",   "restaurant+kitchen+language:python+pushed:>2026-08-15"),
    ("gh_htmx_no-build_lang_py_pushed",        "htmx+no-build+language:python+pushed:>2026-08-15"),
    # controls / mirrors of 09-14 daily-research baseline (no pushed: filter)
    ("gh_topic_small-business_no_push",        "topic:small-business+language:python"),
    ("gh_topic_append-only_no_push",           "topic:append-only+language:python"),
    ("gh_restaurant_kitchen_lang_py_no_push",  "restaurant+kitchen+language:python"),
    ("gh_append_only_ledger_lang_py",          "append-only+ledger+language:python"),
    ("gh_topic_telegram-bot_no_push",          "topic:telegram-bot+language:python"),
    ("gh_topic_real-time_no_push",             "topic:real-time+language:python"),
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
    pp = 50 if "per50" in slug else 10
    try:
        d = fetch(q, per_page=pp)
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
    print(f"\n{tc!s:>6} | inc={inc} | {slug} (q='{q}', pp={pp}){'  msg='+msg if msg else ''}")
    for i in items[:5]:
        lic = (i.get("license") or {}).get("spdx_id", "NONE")
        pushed = (i.get("pushed_at") or "")[:10]
        lang = i.get("language") or ""
        desc = (i.get("description") or "")[:90]
        print(f"     - {i['full_name']:38s} | {i['stargazers_count']:>3}★ {i['forks_count']:>2}⑂ | {lic:12s} | {pushed} | {lang:8s} | {desc}")
    time.sleep(0.6)