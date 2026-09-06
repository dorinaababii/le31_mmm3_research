#!/usr/bin/env python3
"""Parse the manifest + raw fetches for the 2026-09-06 LE31 daily research pass.

Outputs a per-source numeric summary that can be diffed against the next
pass. Mirrors summarize_2026-08-09.py but consumes the modern folder layout
(/opt/data/le31-daily-<date>/<source>/<query>.json|.xml|.atom — no manifest).

Anti-fabrication: every number in this script's output came from the raw
file on disk; the parent agent runs a sibling `grep -rlF 'le31' *` canary
to confirm no third-party raw file mentions LE31.
"""
import json, os, datetime, glob, re, sys
from pathlib import Path
import xml.etree.ElementTree as ET

RAW = Path("/opt/data/le31-daily-2026-09-06")

WIN_START = datetime.datetime(2026, 8, 30, 0, 0, 0, tzinfo=datetime.timezone.utc)
WIN_END = datetime.datetime(2026, 9, 6, 6, 30, 0, tzinfo=datetime.timezone.utc)

# 1. HN Algolia
print("=== HN Algolia (8 queries, in-window 7d) ===")
hn_counts = {}
for f in sorted(RAW.glob("hn_algolia/*.json")):
    d = json.loads(f.read_text())
    nb = d.get("nbHits", 0)
    in_window = 0
    for h in d.get("hits", []):
        ca = h.get("created_at", "")
        if ca:
            dt = datetime.datetime.fromisoformat(ca.replace("Z", "+00:00"))
            if WIN_START <= dt < WIN_END:
                in_window += 1
    hn_counts[f.name] = (nb, in_window)
    print(f"  {f.name}: nbHits={nb} in_window={in_window}")

# 2. arXiv
print("\n=== arXiv (8 queries, in-window 7d) ===")
arxiv_counts = {}
NS = {"atom": "http://www.w3.org/2005/Atom"}
for f in sorted(RAW.glob("arxiv/*.xml")):
    tree = ET.parse(f)
    root = tree.getroot()
    entries = root.findall("atom:entry", NS)
    in_window = 0
    for e in entries:
        pub = e.find("atom:published", NS)
        if pub is not None and pub.text:
            dt = datetime.datetime.fromisoformat(pub.text.replace("Z", "+00:00"))
            if WIN_START <= dt < WIN_END:
                in_window += 1
    arxiv_counts[f.name] = (len(entries), in_window)
    print(f"  {f.name}: total_entries={len(entries)} in_window={in_window}")

# 3. OpenAlex
print("\n=== OpenAlex (6 queries, in-window 7d) ===")
oa_counts = {}
KEYWORDS = ("fastapi", "aiogram", "sqlmodel", "sqlalchemy", "postgres",
            "telegram", "asyncio", "asyncpg")
for f in sorted(RAW.glob("openalex/*.json")):
    d = json.loads(f.read_text())
    m = d.get("meta", {})
    c = m.get("count", 0)
    oa_counts[f.name] = (c, len(d.get("results", [])))
    print(f"  {f.name}: meta.count={c} returned={len(d.get('results', []))}")

# Stack-keyword scan across OpenAlex results
sk_hits = 0
for f in sorted(RAW.glob("openalex/*.json")):
    d = json.loads(f.read_text())
    for r in d.get("results", []):
        title = (r.get("title") or "").lower()
        rec = r.get("abstract_inverted_index") or {}
        if isinstance(rec, dict):
            parts = []
            for val in rec.values():
                if isinstance(val, list):
                    parts.extend(str(x) for x in val)
                else:
                    parts.append(str(val))
            abstract = " ".join(parts).lower()
        else:
            abstract = ""
        blob = title + " " + abstract
        if any(k in blob for k in KEYWORDS):
            sk_hits += 1
print(f"  Stack-keyword hits across all top-results: {sk_hits}")

# 4. GitHub Search
print("\n=== GitHub Search Repositories (7 queries) ===")
gh_counts = {}
all_cands = []
for f in sorted(RAW.glob("github_search/*.json")):
    d = json.loads(f.read_text())
    items = d.get("items", [])
    in_window_py = [it for it in items if it.get("language") == "Python" and it.get("pushed_at", "") >= "2026-08-30"]
    gh_counts[f.name] = (d.get("total_count", 0), len(in_window_py))
    for it in in_window_py:
        it["_query"] = f.name
        all_cands.append(it)
    print(f"  {f.name}: total_count={d.get('total_count', 0)} in_window_python={len(in_window_py)}")

seen = set()
unique = []
for c in all_cands:
    fn = c.get("full_name")
    if fn not in seen:
        seen.add(fn)
        unique.append(c)

fail_axes = {"zero_star": 0, "null_license": 0, "NOASSERTION": 0,
             "AGPL-3.0": 0, "customer_ai": 0}
for c in unique:
    lic = c.get("license") or {}
    spdx = (lic.get("spdx_id") or "null").upper()
    stars = c.get("stargazers_count", 0)
    desc = (c.get("description") or "").lower()
    if stars == 0:
        fail_axes["zero_star"] += 1
    if spdx in ("NULL", "NONE", ""):
        fail_axes["null_license"] += 1
    elif spdx == "NOASSERTION":
        fail_axes["NOASSERTION"] += 1
    if spdx == "AGPL-3.0":
        fail_axes["AGPL-3.0"] += 1
    if any(w in desc for w in ("chatbot", "voice agent", "voice-assistant",
                                "mini app", "twilio", "deepgram",
                                "speech-to-text", "ai agent")):
        fail_axes["customer_ai"] += 1

print(f"  Total unique in-window Python candidates: {len(unique)}")
print(f"  Fail axes: {fail_axes}")

# 5. GitHub Watchlist
print("\n=== GitHub Watchlist (12 repos direct GET) ===")
# 2026-09-05 baseline (from /opt/data/le31-daily-research-2026-09-05.md)
baseline = {
    "longnick__small-pos-open-source": (92, 87, "MIT", "TypeScript", "2026-08-18T12:02:14Z"),
    "satisfecho__pos": (34, 10, "AGPL-3.0", "Python", "2026-08-26T12:34:33Z"),
    "SGrappelli__pronto": (49, 20, "MIT", "TypeScript", "2026-08-25T15:50:14Z"),
    "devnest-hq__restaurant-management-system": (2, 1, "MIT", "JavaScript", "2026-09-04T11:25:01Z"),
    "helloman3__foodieshub": (5, 0, None, "TypeScript", "2026-08-17T07:03:23Z"),
    "SkrudjReal__geminka-agent": (8, 0, "MIT", "Python", "2026-08-25T18:35:50Z"),
    "captainsaify__textile-erp": (1, 0, "MIT", "Python", "2026-08-25T01:27:20Z"),
    "jonalemndi2__ALdia": (1, 0, "Apache-2.0", "Python", "2026-09-02T13:59:45Z"),
    "RafaelEmery__rafood-api": (3, 0, None, "Python", "2026-08-30T20:33:14Z"),
    "Ritchalison__BalanceDesk": (1, 0, "NOASSERTION", "CSS", "2026-09-03T18:57:39Z"),
    "nematjon555__telegram-restaurant-delivery-bot": (0, 0, None, "Python", "2026-08-23T10:38:41Z"),
    "nicholasrossi0530__escpos-render": (1, 0, "MIT", "Go", "2026-08-24T18:39:38Z"),
}
for f in sorted(RAW.glob("github_watchlist/*.json")):
    d = json.loads(f.read_text())
    fn = d.get("full_name")
    stars = d.get("stargazers_count", 0)
    forks = d.get("forks_count", 0)
    pushed = d.get("pushed_at", "")
    lic = (d.get("license") or {}).get("spdx_id")
    name = f.stem  # filename without .json
    if name in baseline:
        bs, bf, bspdx, blang, bpushed = baseline[name]
        dstar = stars - bs
        dfork = forks - bf
        print(f"  {fn}: {stars}* {forks}f pushed={pushed} lic={lic} Δ*={dstar:+} Δf={dfork:+}")
    else:
        print(f"  {fn}: {stars}* {forks}f pushed={pushed} lic={lic} NO_BASELINE")

# 6. PyPI
print("\n=== PyPI in-window uploads per package ===")
for f in sorted(RAW.glob("pypi/*.json")):
    pkg = f.stem
    d = json.loads(f.read_text())
    info_v = d.get("info", {}).get("version", "?")
    releases = d.get("releases", {})
    in_win = []
    for ver, files in releases.items():
        for file_meta in files:
            ut = file_meta.get("upload_time", "")
            if ut >= "2026-08-30":
                in_win.append((ver, ut, file_meta.get("filename", "")))
    print(f"  {pkg} info.version={info_v} in_window_uploads={len(in_win)}")

# 7. releases.atom
print("\n=== GitHub releases.atom in-window entries per repo ===")
for f in sorted(RAW.glob("releases_atom/*.atom")):
    raw = f.read_text()
    updates = re.findall(r"<updated>(.*?)</updated>", raw)
    entries_in_window = [u for u in updates if u >= "2026-08-30" and u < "2026-09-06T07:00"]
    print(f"  {f.name}: atom updates={len(updates)} in_window={len(entries_in_window)}")

# 8. ECB
print("\n=== ECB USD/EUR ===")
ecb = (RAW / "ecb" / "eurofxref-daily.xml").read_text()
m_date = re.search(r"<Cube\s+time='(\d{4}-\d{2}-\d{2})'", ecb)
m_usd = re.search(r"currency='USD'\s+rate='([\d.]+)'", ecb)
print(f"  cube_date={m_date.group(1) if m_date else '?'} USD/EUR={m_usd.group(1) if m_usd else '?'}")

# 9. CNIL RSS
print("\n=== CNIL RSS (both feeds) ===")
for f in sorted(RAW.glob("cnil/*.xml")):
    raw = f.read_text()
    pubdates = re.findall(r"<pubDate>([^<]*)</pubDate>", raw)
    in_window = [p for p in pubdates if re.search(r"(?:30|31)\s+Aug\s+2026|0[1-3]\s+Sep\s+2026", p)]
    print(f"  {f.name}: {len(pubdates)} items, in_window={len(in_window)}")

# 10. EUR-Lex
print("\n=== EUR-Lex failure mode ===")
for f in sorted(RAW.glob("eurlex/*")):
    raw = f.read_text(errors="ignore")
    sz = len(raw)
    first = raw[:120].replace("\n", "\\n")
    print(f"  {f.name}: {sz} bytes | first 120 = {first!r}")

print("\n=== Anti-fabrication canary (LE31 in raw third-party files) ===")
canary_count = 0
for f in RAW.rglob("*"):
    if f.is_file() and f.suffix in (".json", ".xml", ".atom", ".html"):
        try:
            if "le31" in f.read_text(errors="ignore").lower():
                canary_count += 1
        except Exception:
            pass
print(f"  Files containing 'le31' (case-insensitive): {canary_count} / target 0")
