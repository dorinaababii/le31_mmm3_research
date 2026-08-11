#!/bin/bash
# LE31 daily research fetcher for 2026-08-11, 7d window 2026-08-04..2026-08-11
# START=1785801600  END=1786492799
set -u

UA='LE31Research/1.0 (research; contact: hermes-agent@nousresearch.local)'
RAW=/tmp/le31-daily-2026-08-11
START=1785801600
END=1786492799
INDEX=/tmp/le31-daily-2026-08-11/index.json.tmp
> "$INDEX"
echo '[' >> "$INDEX"

fetch() {
  local family="$1"
  local url="$2"
  local out="$3"
  shift 3
  local extra_args=("$@")

  local write_out='%{http_code} %{size_download} %{url_effective}'
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
      local x
      x=$(grep -c '<entry>' "$RAW/$out" 2>/dev/null || echo 0)
      extra=$(jq -c -n --argjson e "$x" '{entry_count:$e}')
      ;;
  esac

  local entry
  entry=$(jq -c -n --arg fn "$out" --arg src "$family" --arg url "$url" --arg st "$status" --arg sz "$size" --arg eu "$effective" --arg ex "$extra" '{filename:$fn, source:$src, url:$url, http_status:$st, byte_size:($sz|tonumber), url_effective:$eu, meta: ($ex | fromjson? // $ex)}')
  echo "$entry," >> "$INDEX"
  printf "  %-40s %s %8s bytes  %s\n" "$out" "$status" "$size" "$effective"
}

echo "[1] HN Algolia (6 queries)"
for pair in \
  "restaurant_pos|restaurant POS" \
  "kitchen_display|kitchen display" \
  "aiogram|aiogram" \
  "restaurant_inventory|restaurant inventory" \
  "telegram_bot|telegram bot" \
  "fastapi_sse|fastapi SSE"; do
  slug=${pair%%|*}; q=${pair##*|}
  url="https://hn.algolia.com/api/v1/search_by_date?query=$(printf '%s' "$q" | jq -sRr @uri)&tags=story&numericFilters=created_at_i%3E=${START},created_at_i%3C=${END}&hitsPerPage=50"
  fetch "hn_algolia" "$url" "hn_${slug}.json"
done

echo "[2] arXiv (5 queries)"
for pair in \
  "restaurant_kitchen_inventory|restaurant kitchen inventory" \
  "kitchen_display_system|kitchen display system" \
  "telegram_bot_aiogram|telegram bot aiogram" \
  "fastapi_sse|fastapi server-sent events" \
  "restaurant_operations|restaurant operations"; do
  slug=${pair%%|*}; q=${pair##*|}
  url="http://export.arxiv.org/api/query?search_query=all:$(printf '%s' "$q" | jq -sRr @uri)&sortBy=submittedDate&sortOrder=descending&max_results=20"
  fetch "arxiv" "$url" "arxiv_${slug}.xml"
done

echo "[3] OpenAlex (3 queries)"
for pair in \
  "restaurant_kitchen_inventory|restaurant kitchen inventory" \
  "kitchen_display_system|kitchen display system" \
  "telegram_bot_restaurant|telegram bot restaurant"; do
  slug=${pair%%|*}; q=${pair##*|}
  url="https://api.openalex.org/works?search=$(printf '%s' "$q" | jq -sRr @uri)&per-page=20"
  fetch "openalex" "$url" "openalex_${slug}.json"
done

echo "[4] GitHub Search Repositories (7 queries)"
for pair in \
  "restaurant_python|restaurant language:python" \
  "kds_python|kitchen display language:python" \
  "telegram_kitchen|telegram bot kitchen" \
  "pos_python|POS language:python" \
  "restaurant_typescript|restaurant language:typescript" \
  "aiogram_restaurant|aiogram restaurant" \
  "pos_go|POS language:go"; do
  slug=${pair%%|*}; q=${pair##*|}
  url="https://api.github.com/search/repositories?q=$(printf '%s' "$q" | jq -sRr @uri)+created:2026-08-04..2026-08-11&sort=updated&order=desc&per_page=30"
  fetch "github_search" "$url" "gh_${slug}.json" "-H" "Accept:application/vnd.github+json"
done

echo "[5] PyPI (6 packages)"
for pkg in aiogram fastapi sqlmodel pydantic sqlalchemy uvicorn; do
  url="https://pypi.org/pypi/${pkg}/json"
  fetch "pypi" "$url" "pypi_${pkg}.json"
done

echo "[6] GitHub releases.atom (6 repos)"
for repo in "aiogram/aiogram" "fastapi/fastapi" "tiangolo/sqlmodel" "pydantic/pydantic" "encode/uvicorn" "sqlalchemy/sqlalchemy"; do
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

sed -i '$ s/,$//' "$INDEX"
echo ']' >> "$INDEX"
mv "$INDEX" /tmp/le31-daily-2026-08-11/index.json

echo
echo "=== Summary ==="
ENTRIES=$(jq 'length' /tmp/le31-daily-2026-08-11/index.json)
BYTES=$(jq '[.[].byte_size] | add' /tmp/le31-daily-2026-08-11/index.json)
ERRORS=$(jq '[.[] | select(.http_status != "200" and .http_status != "304")] | length' /tmp/le31-daily-2026-08-11/index.json)
echo "[index] entries: $ENTRIES, total_bytes: $BYTES, non-200: $ERRORS"
