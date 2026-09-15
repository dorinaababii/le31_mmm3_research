#!/usr/bin/env python3
"""Diagnose why broader queries return total_count=0 today (2026-09-15)."""
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

# Mirror known-working 09-14 queries exactly
QUERIES = [
    ("control_fastapi_restaurant_no_push",      "fastapi+restaurant+language:python"),
    ("control_fastapi_restaurant_pushed_30d",   "fastapi+restaurant+language:python+pushed:>2026-08-15"),
    ("control_aiogram_no_push",                 "aiogram+language:python"),
    ("control_aiogram_pushed_30d",              "aiogram+language:python+pushed:>2026-08-15"),
    ("control_htmx_no_push",                    "htmx+language:python"),
    ("control_htmx_pushed_30d",                 "htmx+language:python+pushed:>2026-08-15"),
    ("control_append_only_no_push",             "append-only+language:python"),
    ("control_append_only_pushed_30d",          "append-only+language:python+pushed:>2026-08-15"),
    ("control_topic_small_business_pushed_30d", "topic:small-business+language:python+pushed:>2026-08-15"),
    ("control_topic_small_business_no_push",    "topic:small-business+language:python"),
    ("control_restaurant_no_push",             "restaurant+language:python"),
    ("control_restaurant_pushed_30d",          "restaurant+language:python+pushed:>2026-08-15"),
    # Search via sort=stars for index health check
    ("control_python_recent_sort_updated",      "language:python+sort:updated-desc"),
    ("control_topic_python_topic_py",           "topic:python"),
    ("control_topic_python_topic_py_pushed",    "topic:python+pushed:>2026-08-15"),
]

OUTDIR = "/tmp/le31-brainstorm-2026-09-15/_parent_recheck"
os.makedirs(OUTDIR, exist_ok=True)


def fetch(q, per_page=10, sort=None, order="desc"):
    params = {"q": q, "per_page": per_page, "order": order}
    if sort:
        params["sort"] = sort
    url = "https://api.github.com/search/repositories?" + urlencode(params)
    req = Request(url, headers=HEADERS)
    with urlopen(req, timeout=20) as r:
        return json.loads(r.read())


for slug, q in QUERIES:
    sort = None
    if "sort:updated" in q:
        sort = "updated"
        q = q.replace("sort:updated-desc", "").strip()
    try:
        d = fetch(q, sort=sort)
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
        lang = i.get("language") or ""
        desc = (i.get("description") or "")[:80]
        print(f"     - {i['full_name']:40s} | {i['stargazers_count']:>3}★ | {lic:12s} | {pushed} | {lang:8s} | {desc}")
    time.sleep(0.7)