#!/usr/bin/env bash
# LE31 daily research fetch — 2026-08-20
# 7-day window 2026-08-13..2026-08-20 UTC
set -u

RAW_DIR=/tmp/le31-daily-2026-08-20
LOG=$RAW_DIR/_fetch.log
INDEX=$RAW_DIR/index.json

# Per 2026-08-19 finding: HN Algolia rejects 'Hermes-LE31-Daily/1.0' UA with HTTP 400; use Mozilla/5.0 default.
UA="Mozilla/5.0"
START=1786579200   # 2026-08-13 00:00 UTC
END=1787184000     # 2026-08-20 00:00 UTC (exclusive)

: > "$LOG"
: > "$INDEX"

fetch() {
  local url="$1"
  local file="$2"
  local extra_header="${3:-}"
  local code size ts
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
  size=${code#* }
  code=${code%% *}
  echo "$ts $url $code $size" >> "$LOG"
  printf '{"url":"%s","file":"%s","status":%s,"bytes":%s}\n' \
    "$(printf '%s' "$url" | sed 's/"/\\"/g')" \
    "$file" "$code" "$size" >> "$INDEX"
}

# Source GH token from /opt/data/.env
set +u
GH_TOKEN="$(grep -oP '(?<=^HERMES_GITHUB_TOKEN=).*' /opt/data/.env || true)"
set -u
GH_AUTH="Authorization: Bearer ${GH_TOKEN:-}"

# (a) HN Algolia (8 queries) — numericFilters URL-encoded for HN grammar
for q in "restaurant+POS" "kitchen+display" "aiogram" "restaurant+inventory" "telegram+bot" "fastapi+SSE" "aiogram+restaurant" "fastapi+restaurant"; do
  url="https://hn.algolia.com/api/v1/search_by_date?query=${q}&tags=story&hitsPerPage=50&numericFilters=created_at_i%3E${START},created_at_i%3C${END}"
  fetch "$url" "hn-${q}.json"
done

# (b) arXiv (5 queries)
for q in "restaurant+kitchen+inventory" "kitchen+display+system" "telegram+bot+restaurant" "postgres+append+only+ledger" "Point+of+Sale+restaurant"; do
  enc=$(printf '%s' "$q" | sed 's/+/%20/g')
  url="http://export.arxiv.org/api/query?search_query=${enc}&max_results=20&sortBy=submittedDate&sortOrder=descending"
  fetch "$url" "arxiv-${q}.atom.xml"
done

# (c) OpenAlex (3 queries)
for q in "restaurant+kitchen+inventory" "kitchen+display+system" "telegram+bot+restaurant"; do
  enc=$(printf '%s' "$q" | sed 's/+/%20/g')
  url="https://api.openalex.org/works?search=${enc}&filter=from_publication_date:2026-08-13,to_publication_date:2026-08-20&per_page=20"
  fetch "$url" "openalex-${q}.json"
done

# (d) GitHub Search Repos (7 queries)
for q in "restaurant+language:python" "kitchen+display+language:python" "telegram+kitchen+language:python" "pos+language:python" "restaurant+language:typescript" "aiogram+restaurant" "pos+language:go"; do
  enc=$(printf '%s' "$q" | sed 's/+/%2B/g; s/:/%3A/g')
  url="https://api.github.com/search/repositories?q=${enc}+created:2026-08-13..2026-08-20+archived:false&per_page=30"
  fetch "$url" "github-${q}.json" "$GH_AUTH"
done

# (e) GitHub single-repo (3 carry-over watch-list peers)
fetch "https://api.github.com/repos/longnick/small-pos-open-source" "gh-longnick.json" "$GH_AUTH"
fetch "https://api.github.com/repos/satisfecho/pos" "gh-satisfecho.json" "$GH_AUTH"
fetch "https://api.github.com/repos/helloman3/foodieshub" "gh-foodieshub.json" "$GH_AUTH"

# (f) PyPI (10 packages)
for pkg in uvicorn fastapi sqlmodel aiogram pydantic pydantic-core sqlalchemy alembic httpx tiktoken; do
  fetch "https://pypi.org/pypi/${pkg}/json" "pypi-${pkg}.json"
done

# (g) GitHub releases.atom (7 repos)
for repo in "Kludex/uvicorn" "fastapi/fastapi" "sqlalchemy/sqlalchemy" "pydantic/pydantic" "pydantic/pydantic-core" "sqlmodel/sqlmodel" "aiogram/aiogram"; do
  slug=$(printf '%s' "$repo" | tr '/' '-')
  fetch "https://github.com/${repo}/releases.atom" "releases-${slug}.atom"
done
fetch "https://api.github.com/repos/sqlalchemy/alembic/releases" "releases-alembic.json" "$GH_AUTH"

# (h) ECB
fetch "https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml" "ecb.xml"

# (i) CNIL
fetch "https://www.cnil.fr/en/rss.xml" "cnil-en.rss.xml"
fetch "https://www.cnil.fr/fr/rss.xml" "cnil-fr.rss.xml"

# (j) EUR-Lex (6 feeds)
for id in 1 2 3 4 5 18; do
  fetch "https://eur-lex.europa.eu/RSS/feed.rss?rssId=${id}" "eurlex-${id}.rss.xml"
done

# (k) ScienceDirect BLOCKED
ts=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
echo "$ts https://www.sciencedirect.com/ BLOCKED 0" >> "$LOG"
printf '{"url":"https://www.sciencedirect.com/","file":"BLOCKED","status":0,"bytes":0}\n' >> "$INDEX"

echo "Fetch pass complete."
wc -l "$LOG" "$INDEX"
