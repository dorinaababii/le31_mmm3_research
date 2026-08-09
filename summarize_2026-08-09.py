#!/usr/bin/env python3
"""Parse the manifest + raw fetches and emit SUMMARY.md per the spec."""
import json, os, datetime, glob, re
from pathlib import Path

RAW = Path("/tmp/le31-daily-2026-08-09")
manifest = json.load(open(RAW / "index.json"))
entries = [e for e in manifest if e.get("filename") != "sciencedirect_blocked.json"]

# 1. Manifest-level counts
total_files = len(manifest)
total_bytes = sum(e.get("byte_size", 0) for e in manifest)
http_200 = sum(1 for e in manifest if e.get("http_status") == "200")
non_200 = sum(1 for e in manifest if e.get("http_status") not in ("200", "BLOCKED"))
blocked = sum(1 for e in manifest if e.get("http_status") == "BLOCKED")

# 2. Per-source family counts
def by_source(name):
    return [e for e in entries if e.get("source") == name]

# HN: nbHits
hn_counts = {}
for e in by_source("hn_algolia"):
    fn = e["filename"]
    nb = (e.get("meta") or {}).get("nbHits")
    hn_counts[fn] = nb

# GitHub: total_count
gh_counts = {}
for e in by_source("github_search"):
    fn = e["filename"]
    tc = (e.get("meta") or {}).get("total_count")
    gh_counts[fn] = tc

# OpenAlex: meta.count
oa_counts = {}
for e in by_source("openalex"):
    fn = e["filename"]
    raw = json.load(open(RAW / fn))
    oa_counts[fn] = raw.get("meta", {}).get("count", "?")

# PyPI: info.version + upload_time
pypi_top = {}
for e in by_source("pypi"):
    fn = e["filename"]
    raw = json.load(open(RAW / fn))
    v = raw["info"]["version"]
    ut = raw["releases"][v][0]["upload_time"]
    pypi_top[fn.replace("pypi_", "").replace(".json", "")] = (v, ut[:10])

# release.atom: latest <updated>
atom_latest = {}
for e in by_source("github_releases"):
    fn = e["filename"]
    raw = open(RAW / fn).read()
    m = re.search(r"<updated>([^<]+)</updated>", raw)
    atom_latest[fn] = m.group(1) if m else "?"

# ECB: latest time=
ecb_raw = open(RAW / "ecb.xml").read()
ecb_latest = re.findall(r"time='([^']+)'", ecb_raw)
ecb_latest = ecb_latest[-1] if ecb_latest else "?"

# CNIL: latest pubDate
def cnil_latest(fn):
    raw = open(RAW / fn).read()
    m = re.findall(r"<pubDate>([^<]+)</pubDate>", raw)
    return m[0] if m else "?"

# 3. Most interesting raw hits
# - HN: pick top-2 by points among aiogram + telegram_bot
hn_interesting = []
for fn in ["hn_aiogram.json", "hn_telegram_bot.json", "hn_fastapi_sse.json"]:
    raw = json.load(open(RAW / fn))
    hits = raw.get("hits", [])
    hits_sorted = sorted(hits, key=lambda h: (h.get("points") or 0), reverse=True)
    for h in hits_sorted[:2]:
        hn_interesting.append({
            "title": h.get("title", ""),
            "url": h.get("url") or h.get("story_url", ""),
            "hn": f"https://news.ycombinator.com/item?id={h.get('objectID','')}",
            "points": h.get("points", 0),
            "created_at": h.get("created_at", ""),
        })
hn_interesting.sort(key=lambda x: x["points"], reverse=True)

# - GitHub: top repos by stars from the noisy queries
gh_interesting = []
for e in by_source("github_search"):
    raw = json.load(open(RAW / e["filename"]))
    for it in raw.get("items", [])[:3]:
        gh_interesting.append({
            "full_name": it.get("full_name"),
            "url": it.get("html_url"),
            "stars": it.get("stargazers_count", 0),
            "desc": (it.get("description") or "")[:120],
            "query": e["filename"].replace("github_", "").replace(".json", ""),
        })
gh_interesting.sort(key=lambda x: x["stars"], reverse=True)
# Dedup by full_name
seen = set()
gh_top = []
for it in gh_interesting:
    if it["full_name"] in seen:
        continue
    seen.add(it["full_name"])
    gh_top.append(it)

# - OpenAlex: top work by cited_by_count
oa_interesting = []
for e in by_source("openalex"):
    raw = json.load(open(RAW / e["filename"]))
    for w in raw.get("results", [])[:3]:
        oa_interesting.append({
            "title": w.get("title", "") or w.get("display_name", ""),
            "doi": w.get("doi"),
            "cited": w.get("cited_by_count", 0),
            "pub": w.get("publication_date"),
            "query": e["filename"].replace("openalex_", "").replace(".json", ""),
        })
oa_interesting.sort(key=lambda x: x["cited"], reverse=True)
oa_top = []
seen = set()
for w in oa_interesting:
    k = w["title"]
    if k in seen:
        continue
    seen.add(k)
    oa_top.append(w)

# 4. Write SUMMARY.md
out = []
out.append("# LE31 Daily Research — 2026-08-09 — SUMMARY")
out.append("")
out.append("## Manifest summary")
out.append(f"- Total files written: **{total_files}**")
out.append(f"- Total bytes: **{total_bytes:,}**")
out.append(f"- HTTP 200: **{http_200}**")
out.append(f"- HTTP non-200 (404, etc): **{non_200}** (all EUR-Lex)")
out.append(f"- Blocked (no fetch): **{blocked}** (ScienceDirect)")
out.append("")
out.append("## Per-source family counts")
out.append("")
out.append("### HN Algolia `search_by_date` (nbHits)")
out.append("| query | nbHits |")
out.append("|---|---|")
for fn, nb in hn_counts.items():
    out.append(f"| {fn.replace('hn_','').replace('.json','')} | {nb} |")
out.append("")
out.append("### arXiv (XML returned; entry count varies, all HTTP 200)")
for e in by_source("arxiv"):
    raw = open(RAW / e["filename"]).read()
    n = raw.count("<entry>")
    out.append(f"- {e['filename']}: {n} entries")
out.append("")
out.append("### OpenAlex (meta.count)")
out.append("| query | count |")
out.append("|---|---|")
for fn, c in oa_counts.items():
    out.append(f"| {fn.replace('openalex_','').replace('.json','')} | {c} |")
out.append("")
out.append("### GitHub Search Repositories (total_count)")
out.append("| query | total_count |")
out.append("|---|---|")
for fn, tc in gh_counts.items():
    out.append(f"| {fn.replace('github_','').replace('.json','')} | {tc} |")
out.append("")
out.append("### PyPI (top version, upload date)")
out.append("| package | version | uploaded |")
out.append("|---|---|---|")
for pkg, (v, ut) in sorted(pypi_top.items()):
    out.append(f"| {pkg} | {v} | {ut} |")
out.append("")
out.append("### GitHub release.atom (latest <updated>)")
for fn, t in atom_latest.items():
    out.append(f"- {fn}: {t}")
out.append("")
out.append(f"### ECB eurofxref (latest `time=`): {ecb_latest}")
out.append(f"### CNIL EN latest pubDate: {cnil_latest('cnil_en.xml')}")
out.append(f"### CNIL FR latest pubDate: {cnil_latest('cnil_fr.xml')}")
out.append("")
out.append("## Three to seven most interesting raw hits")
out.append("")
# pick top 7 across families
out.append("### HN (top by points)")
for h in hn_interesting[:3]:
    out.append(f"- **{h['title']}** ({h['points']} pts, {h['created_at'][:10]}) — {h['url']}  ←  [hn_algolia]")
out.append("")
out.append("### GitHub (top by stars)")
for it in gh_top[:3]:
    out.append(f"- **{it['full_name']}** ({it['stars']} ★) — {it['url']} — {it['desc']}  ←  [github_search/{it['query']}]")
out.append("")
out.append("### OpenAlex (top by cited_by_count)")
for w in oa_top[:3]:
    out.append(f"- **{w['title']}** (cited {w['cited']}, {w['pub']}) — {w['doi'] or 'no doi'}  ←  [openalex/{w['query']}]")
out.append("")
out.append("## Blockers")
out.append("- **EUR-Lex** `https://eur-lex.europa.eu/collection/eu-law/feed.html?rssId={1,2,3,4,5,18}` — all 6 return HTTP 404 (~55 KB EUR-Lex 404 HTML). This matches the 2026-08-04/07 pattern; EUR-Lex RSS is end-to-end blocked from this VPS.")
out.append("- **ScienceDirect** — recorded as BLOCKED, not fetched (Cloudflare blocks curl).")
out.append("- **Window audit pitfall:** spec-given epoch pair `1754265600..1754784000` resolves to `2025-08-04..2025-08-10` (not `2026-08-03..2026-08-09` as the prose says). The spec's date strings `from_publication_date:2026-08-03,to_publication_date:2026-08-09` and `pushed:>2026-08-02` are also 2026 dates. Per the hard-rule \"use only the queries and date filters above\" we fired the literal binding contract. **The HN `numericFilters` therefore queried 2025-08-04..2025-08-10** (older window); HN returned near-zero hits as a result. The OpenAlex and GitHub queries used the 2026 strings and returned real 2026 results. This is a (c) prose-vs-epoch year-disagree case, surfaced for the parent to reconcile.")
out.append("- **OpenAlex** `telegram bot restaurant` query returned HTTP 200 with the 679-byte empty/null response (0 results).")
out.append("")
out.append("## Sources I could not interpret (count-only, no useful items)")
out.append("- `openalex_telegram_bot_restaurant.json`: HTTP 200, 679 bytes, `meta.count` present but `results: []` — empty-result signature.")
out.append("- arXiv `arxiv_telegram_bot_aiogram.xml` and `arxiv_fastapi_sse.xml` returned the standard 20-entry descending-by-submittedDate list. Most entries are not in-window for 2026-08-03..2026-08-09 and are not directly restaurant-tech relevant; counts only.")
out.append("")
out.append("## On-disk confirmation")
out.append("- Manifest: `/tmp/le31-daily-2026-08-09/index.json` (well-formed JSON, validated via `json.load`).")
out.append("- Summary: this file, `/tmp/le31-daily-2026-08-09/SUMMARY.md`.")
out.append("- Script: `/opt/data/le31_mmm3_research_work/fetch_le31_2026-08-09.sh` (mirrors prior `fetch_le31.sh` shape).")
open(RAW / "SUMMARY.md", "w").write("\n".join(out) + "\n")
print(f"Wrote SUMMARY.md ({os.path.getsize(RAW / 'SUMMARY.md')} bytes)")
