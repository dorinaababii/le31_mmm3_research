#!/usr/bin/env python3
"""LE31 brainstorm 2026-09-15 — deeper pages on the productive non-topic queries.
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


def fetch(q, sort="updated", per_page=100, page=1):
    url = "https://api.github.com/search/repositories?" + urlencode({
        "q": q, "sort": sort, "order": "desc", "per_page": per_page, "page": page
    })
    req = Request(url, headers=HEADERS)
    with urlopen(req, timeout=30) as r:
        return json.loads(r.read())


# Deeper pages on the productive queries, sorted by updated (most recently
# active repos first).
QUERIES = [
    ("deep_real-time_py_p1",   "real-time+language:python", 100, 1),
    ("deep_real-time_py_p2",   "real-time+language:python", 100, 2),
    ("deep_telegram-bot_py_p1", "telegram-bot+language:python", 100, 1),
    ("deep_telegram-bot_py_p2", "telegram-bot+language:python", 100, 2),
    ("deep_pos_py_p1",         "pos+language:python", 100, 1),
    ("deep_restaurant_py_p1",  "restaurant+language:python", 100, 1),
    ("deep_restaurant_py_p2",  "restaurant+language:python", 100, 2),
    ("deep_append-only_py_p1", "append-only+language:python", 100, 1),
    # Star-sorted: any popular in-domain Python repos updated recently
    ("star_pos_py",            "pos+language:python", 50, 1),
]

OUTDIR = "/tmp/le31-brainstorm-2026-09-15/_parent_recheck"
os.makedirs(OUTDIR, exist_ok=True)


def analyze(items):
    in_window = []
    for i in items:
        pushed = i.get("pushed_at") or ""
        try:
            pushed_dt = datetime.fromisoformat(pushed.replace("Z", "+00:00"))
        except Exception:
            continue
        if pushed_dt >= WINDOW:
            in_window.append(i)
    return in_window


for slug, q, pp, page in QUERIES:
    try:
        d = fetch(q, per_page=pp, page=page)
    except Exception as e:
        print(f"ERROR  {q} p{page}  -> {e}")
        continue
    tc = d.get("total_count")
    items = d.get("items", [])
    in_window = analyze(items)
    raw_path = os.path.join(OUTDIR, slug + ".json")
    with open(raw_path, "w") as f:
        json.dump(d, f, indent=2)
    print(f"\n{tc!s:>6} total | {len(in_window):>3} in-window-by-push (returned {len(items)}) | {slug} (q='{q}', p={page})")
    for i in in_window[:10]:
        lic = (i.get("license") or {}).get("spdx_id", "NONE")
        pushed = (i.get("pushed_at") or "")[:10]
        created = (i.get("created_at") or "")[:10]
        lang = i.get("language") or ""
        topics = ",".join(i.get("topics", []) or [])[:40]
        desc = (i.get("description") or "")[:90]
        print(f"     - {i['full_name']:38s} | {i['stargazers_count']:>3}★ {i['forks_count']:>2}⑂ | {lic:12s} | p={pushed} c={created} | {lang:8s} | {topics:42s}| {desc}")
    time.sleep(1.5)