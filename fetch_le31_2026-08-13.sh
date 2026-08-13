#!/bin/bash
# LE31 daily research fetcher for 2026-08-13, 7d window 2026-08-06..2026-08-13
# START=1786838400  END=1787443199
# Adapted from /opt/data/le31_mmm3_research_work/fetch_le31_2026-08-12.sh
set -u

UA='LE31Research/1.0 (research; contact: hermes-agent@nousresearch.local)'
RAW=/tmp/le31-daily-2026-08-13
START=1786838400
END=1787443199
INDEX=/tmp/le31-daily-2026-08-13/index.json.tmp
LOG=/tmp/le31-daily-2026-08-13/_fetch.log
STARTED=$(date -u +%Y-%m-%dT%H:%M:%S+00:00)
: > "$INDEX"
: > "$LOG"
echo '[' >> "$INDEX"

log_line() { printf '%s\n' "$*" >> "$LOG"; }

fetch() {
  local family="$1"
  local url="$2"
  local out="$3"
  shift 3
  local extra_args=("$@")

  local write_out='%{http_code} %{size_download} %{url_effective}'
  local now
  now=$(date -u +%Y-%m-%dT%H:%M:%S+00:00)
  local result
  result=$(curl -sS -L -A "$UA" --max-time 30 -D /dev/null \
    -w "$write_out" \
    -o "$RAW/$out" \
    "${extra_args[@]}" \
    "$url" 2>/dev/null)
  local status size effective
  read -r status size effective <<<"$result"
  if [ -z "$status" ]; then status="ERR"; fi
  if [ -z "$size" ]; then size=0; fi

  if [ ! -f "$RAW/$out" ]; then
    status="NOFILE"
  fi

  local extra="null"
  case "$out" in
    *.json)
      local j
      j=$(jq -c '{nbHits: .nbHits, total_count: .total_count, count: .count, meta: .meta}' "$RAW/$out" 2>/dev/null)
      if [ -n "$j" ] && [ "$j" != "null" ]; then extra="$j"; fi
      ;;
    *.xml)
      local x rc
      x=$(grep -c '<entry>' "$RAW/$out" 2>/dev/null); rc=$?
      if [ $rc -ne 0 ] || [ -z "$x" ]; then x=0; fi
      extra=$(jq -c -n --argjson e "$x" '{entry_count:$e}' 2>/dev/null)
      if [ -z "$extra" ]; then extra='null'; fi
      ;;
  esac

  local slug
  slug=$(echo "$out" | sed -E 's/\.(json|xml|atom)$//')
  local entry
  entry=$(jq -c -n \
    --arg fn "$out" --arg slug "$slug" \
    --arg src "$family" --arg url "$url" \
    --arg st "$status" --arg sz "$size" \
    --arg eu "$effective" --arg ex "$extra" \
    --arg ts "$now" \
    '{filename:$fn, slug:$slug, source:$src, url:$url, url_effective:$eu, http_status:$st, byte_size:($sz|tonumber), fetched_at_utc:$ts, meta: ($ex | fromjson? // $ex)}' 2>/dev/null)
  if [ -z "$entry" ]; then
    # Fallback minimal entry so we never lose a fetch
    entry=$(jq -c -n --arg fn "$out" --arg src "$family" --arg st "$status" --arg sz "$size" --arg ts "$now" '{filename:$fn, source:$src, http_status:$st, byte_size:($sz|tonumber), fetched_at_utc:$ts, meta:null}')
  fi
  echo "$entry," >> "$INDEX"
  printf "  %-40s %s %8s bytes  %s\n" "$out" "$status" "$size" "$effective" >> "$LOG"
  printf "  %-40s %s %8s bytes  %s\n" "$out" "$status" "$size" "$effective"
}

log_line "==== LE31 daily fetch - window 2026-08-06..2026-08-13 (epoch $START..$END) ===="
log_line "Started: $STARTED"

echo "[1] HN Algolia (8 queries: 6 baseline + 2 paired-keyword)"
for pair in \
  "restaurant_pos|restaurant POS" \
  "kitchen_display|kitchen display" \
  "aiogram|aiogram" \
  "restaurant_inventory|restaurant inventory" \
  "telegram_bot|telegram bot" \
  "fastapi_sse|fastapi SSE" \
  "aiogram_restaurant|aiogram restaurant" \
  "fastapi_restaurant|fastapi restaurant"; do
  slug=${pair%%|*}; q=${pair##*|}
  url="https://hn.algolia.com/api/v1/search_by_date?query=$(printf '%s' "$q" | jq -sRr @uri)&tags=story&numericFilters=created_at_i%3E${START},created_at_i%3C${END}&hitsPerPage=50"
  fetch "hn_algolia" "$url" "hn_${slug}.json"
done

echo "[2] arXiv (5 queries)"
for pair in \
  "restaurant_pos|restaurant POS" \
  "kitchen_display_system|kitchen display system" \
  "telegram_bot_restaurant|telegram bot restaurant" \
  "restaurant_inventory_management|restaurant inventory management" \
  "postgres_append_only_ledger|postgres append-only ledger"; do
  slug=${pair%%|*}; q=${pair##*|}
  url="http://export.arxiv.org/api/query?search_query=all:$(printf '%s' "$q" | jq -sRr @uri)&sortBy=submittedDate&sortOrder=descending&max_results=20"
  fetch "arxiv" "$url" "arxiv_${slug}.xml"
done

echo "[3] OpenAlex (3 queries, date-filtered 2026-08-06..2026-08-13)"
for pair in \
  "restaurant_kitchen_inventory|restaurant kitchen inventory" \
  "kitchen_display_system|kitchen display system" \
  "telegram_bot_restaurant|telegram bot restaurant"; do
  slug=${pair%%|*}; q=${pair##*|}
  url="https://api.openalex.org/works?search=$(printf '%s' "$q" | jq -sRr @uri)&per-page=20&filter=from_publication_date:2026-08-06,to_publication_date:2026-08-13"
  fetch "openalex" "$url" "openalex_${slug}.json"
done

echo "[4] GitHub Search Repositories (7 queries, created:2026-08-06..2026-08-13)"
for pair in \
  "restaurant_python|restaurant language:python" \
  "kds_python|kitchen display language:python" \
  "telegram_kitchen|telegram bot kitchen" \
  "pos_python|POS language:python" \
  "restaurant_typescript|restaurant language:typescript" \
  "aiogram_restaurant|aiogram restaurant" \
  "pos_go|POS language:go"; do
  slug=${pair%%|*}; q=${pair##*|}
  url="https://api.github.com/search/repositories?q=$(printf '%s' "$q" | jq -sRr @uri)+created:2026-08-06..2026-08-13&sort=updated&order=desc&per_page=30"
  fetch "github_search" "$url" "gh_${slug}.json" "-H" "Accept:application/vnd.github+json"
done

echo "[5] PyPI (10 packages)"
for pkg in aiogram fastapi sqlmodel pydantic pydantic-core sqlalchemy uvicorn alembic httpx tiktoken; do
  url="https://pypi.org/pypi/${pkg}/json"
  fetch "pypi" "$url" "pypi_${pkg}.json"
done

echo "[6] GitHub releases.atom (8 repos)"
for repo in "aiogram/aiogram" "fastapi/fastapi" "tiangolo/sqlmodel" "pydantic/pydantic" "pydantic/pydantic-core" "encode/uvicorn" "sqlalchemy/sqlalchemy" "alembic/alembic"; do
  safe=$(echo "$repo" | tr '/' '_')
  url="https://github.com/${repo}/releases.atom"
  fetch "github_releases" "$url" "release_${safe}.atom"
done

echo "[7] ECB eurofxref"
fetch "ecb" "https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml" "ecb.xml"

echo "[8] CNIL EN + FR"
fetch "cnil" "https://www.cnil.fr/en/rss.xml" "cnil_en.xml"
fetch "cnil" "https://www.cnil.fr/fr/rss.xml" "cnil_fr.xml"

echo "[9] EUR-Lex RSS (6 ids)"
for rid in 1 2 3 4 5 18; do
  url="https://eur-lex.europa.eu/RSS/feed.rss?rssId=${rid}"
  fetch "eurlex" "$url" "eurlex_${rid}.xml"
done

SD_TS=$(date -u +%Y-%m-%dT%H:%M:%S+00:00)
sd=$(jq -c -n \
  --arg ts "$SD_TS" \
  '{filename:"sciencedirect_blocked", slug:"sciencedirect_blocked", source:"sciencedirect", url:"https://www.sciencedirect.com/", url_effective:"https://www.sciencedirect.com/", http_status:"BLOCKED", byte_size:0, fetched_at_utc:$ts, note:"Per task instructions: record as BLOCKED, do not retry."}')
echo "$sd," >> "$INDEX"
printf "  %-40s %s %8s bytes  %s\n" "sciencedirect_blocked" "BLOCKED" "0" "https://www.sciencedirect.com/" >> "$LOG"

sed -i '$ s/,$//' "$INDEX"
echo ']' >> "$INDEX"

FINISHED=$(date -u +%Y-%m-%dT%H:%M:%S+00:00)

ENVELOPE=/tmp/le31-daily-2026-08-13/index.json
jq -s --arg started "$STARTED" --arg finished "$FINISHED" \
  --argjson ws "$START" --argjson we "$END" --arg ua "$UA" \
  '{
    started_utc: $started,
    finished_utc: $finished,
    window_start_epoch: $ws,
    window_end_epoch: $we,
    ua: $ua,
    total_fetches: (. | length),
    entries: .
  }' "$INDEX" > "$ENVELOPE.tmp"
mv "$ENVELOPE.tmp" "$ENVELOPE"

echo
echo "=== Summary ==="
ENTRIES=$(jq '.total_fetches' "$ENVELOPE")
BYTES=$(jq '[.entries[].byte_size] | add' "$ENVELOPE")
ERRORS=$(jq '[.entries[] | select(.http_status != "200" and .http_status != "304")] | length' "$ENVELOPE")
echo "[index] entries: $ENTRIES, total_bytes: $BYTES, non-200: $ERRORS"
echo "  finished: $FINISHED"
log_line "==== finished: $FINISHED  entries: $ENTRIES  total_bytes: $BYTES  non-200: $ERRORS ===="
