#!/usr/bin/env bash
# LE31 daily research fetch — 2026-08-28
# 7-day window 2026-08-21..2026-08-28 UTC
# 29th consecutive daily-research pass.
#
# Per 2026-08-19 finding: HN Algolia rejects 'Hermes-LE31-Daily/1.0' UA
# with HTTP 400; use Mozilla/5.0 default. HN Algolia numericFilters
# MUST use URL-encoded `%3E` / `%3C` (raw `<` is rejected).
#
# Per 2026-08-27 finding: arXiv parallel burst returns HTTP 429. Serialize
# with `sleep 4` between arXiv requests.
#
# Per 2026-08-27 finding: GitHub search `+`-separated with `language:`
# qualifiers is the working form (underscore-joined multi-word returns
# "Validation Failed" 73-byte body).
#
# Subagent of record: MiniMax-M3, dispatched from parent on
# 2026-08-28 06:31 UTC.
set -u

RAW_DIR=/tmp/le31-daily-2026-08-28
LOG=$RAW_DIR/_fetch.log

UA="Mozilla/5.0"
# window: 2026-08-21 00:00 UTC .. 2026-08-28 06:30 UTC (exclusive upper bound)
START=1787875200   # 2026-08-21 00:00 UTC
END=1788071400     # 2026-08-28 06:30 UTC

GH_TOKEN="$(grep -E '^HERMES_GITHUB_TOKEN=' /opt/data/.env | cut -d= -f2-)"

mkdir -p "$RAW_DIR"

fetch() {
  local url="$1"
  local file="$2"
  local extra_header="${3:-}"
  local code ts
  ts=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
  if [ -n "$extra_header" ]; then
    code=$(curl -sS -L -A "$UA" --max-time 30 \
      -H "$extra_header" \
      -o "$RAW_DIR/$file" \
      -w '%{http_code} %{size_download}' "$url" 2>/dev/null)
  else
    code=$(curl -sS -L -A "$UA" --max-time 30 \
      -o "$RAW_DIR/$file" \
      -w '%{http_code} %{size_download}' "$url" 2>/dev/null)
  fi
  echo "$ts $1 -> $file: $code" | tee -a "$LOG" >/dev/null
}

# --- HN Algolia (8 queries, %3E / %3C URL-encoded) ---
for q in "restaurant%20POS" "kitchen%20display" "aiogram" "restaurant%20inventory" \
         "telegram%20bot" "fastapi%20SSE" "aiogram%20restaurant" "fastapi%20restaurant"; do
  url="https://hn.algolia.com/api/v1/search_by_date?query=${q}&tags=story&hitsPerPage=50&numericFilters=created_at_i%3E${START},created_at_i%3C${END}"
  fetch "$url" "hn_$(echo $q | tr '%' '_' | head -c 30).json"
done

# --- arXiv API (5 queries; serialized with sleep 4) ---
for q in "restaurant%20AND%20POS" "kitchen%20display%20system" "telegram%20bot%20restaurant" \
         "fastapi%20SSE" "append-only%20ledger"; do
  url="http://export.arxiv.org/api/query?search_query=all:${q}&start=0&max_results=20&sortBy=submittedDate&sortOrder=descending"
  fetch "$url" "arxiv_$(echo $q | head -c 20).xml"
  sleep 4
done

# --- OpenAlex (3 queries) ---
for q in "restaurant%20kitchen%20inventory" "kitchen%20display%20system" "telegram%20bot%20restaurant"; do
  url="https://api.openalex.org/works?search=${q}&per_page=20&filter=from_publication_date:2026-08-21,to_publication_date:2026-08-28"
  fetch "$url" "openalex_$(echo $q | head -c 25).json"
done

# --- GitHub Search Repositories (7 queries, +language qualifier form) ---
for q in "restaurant+language:python" "kitchen+display+language:python" \
         "telegram+kitchen+language:python" "pos+language:python" \
         "restaurant+language:typescript" "aiogram+restaurant" "pos+language:go"; do
  url="https://api.github.com/search/repositories?q=${q}+archived:false+created:2026-08-21..2026-08-28&per_page=30"
  fetch "$url" "ghsearch_$(echo $q | tr '+' '_' | tr ':' '_').json" "Authorization: token $GH_TOKEN"
done

# --- Direct repo star-velocity checks (watch list — 11 active repos) ---
for repo in "longnick/small-pos-open-source" "satisfecho/pos" "helloman3/foodieshub" \
            "devnest-hq/restaurant-management-system" "SGrappelli/pronto" \
            "SkrudjReal/geminka-agent" "captainsaify/textile-erp" \
            "jonalemndi2/ALdia" "RafaelEmery/rafood-api" \
            "Ritchalison/BalanceDesk" "nicholasrossi0530/escpos-render"; do
  url="https://api.github.com/repos/${repo}"
  fetch "$url" "repo_$(echo $repo | tr '/' '_').json" "Authorization: token $GH_TOKEN"
done

# --- PyPI JSON (10 packages) ---
for pkg in "aiogram" "fastapi" "sqlmodel" "pydantic" "pydantic-core" "uvicorn" \
           "sqlalchemy" "alembic" "httpx" "tiktoken"; do
  url="https://pypi.org/pypi/${pkg}/json"
  fetch "$url" "pypi_${pkg//-/_}.json"
done

# --- GitHub releases.atom (6 repos) ---
for repo in "Kludex/uvicorn" "fastapi/fastapi" "sqlmodel/sqlmodel" "pydantic/pydantic" \
             "aiogram/aiogram" "encode/httpx"; do
  url="https://github.com/${repo}/releases.atom"
  fetch "$url" "releases_$(echo $repo | cut -d/ -f2 | tr '/' '_').xml"
done

# --- ECB eurofxref daily ---
fetch "https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml" "ecb_eurofxref.xml"

# --- CNIL EN + FR RSS ---
fetch "https://www.cnil.fr/fr/rss/actualite_en" "cnil_en.xml"
fetch "https://www.cnil.fr/fr/rss/actualite" "cnil_fr.xml"

# --- EUR-Lex legacy RSS (3 endpoints) ---
for rid in 1 2 3; do
  fetch "https://eur-lex.europa.eu/EUR-Lex-2-EN/rss/feed.rss?rssId=${rid}" "eurlex_rss_${rid}.xml"
done

# --- EUR-Lex REST API ---
fetch "https://eur-lex.europa.eu/api/v1/notice/search?q=restaurant&pageSize=10" "eurlex_rest.json"

# --- ScienceDirect: BLOCKED, not attempted ---

echo "Fetch pass complete. Total lines in $LOG:"
wc -l "$LOG"