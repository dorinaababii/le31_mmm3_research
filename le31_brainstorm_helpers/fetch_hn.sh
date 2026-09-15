#!/usr/bin/env bash
# HN Algolia fetch loop
set +e
OUTDIR="/tmp/le31-brainstorm-2026-08-29"
cd "${OUTDIR}"
UA="Mozilla/5.0"
WIN_FROM=1785369600
WIN_TO=1788399060
mkdir -p hn

QUERIES=(
  "crossover+restaurant+app"
  "micro+SaaS+small+business"
  "solo+founder+SaaS"
  "low-effort+UX"
  "phone-first+POS"
  "kitchen+workflow"
  "append-only+event+log"
  "telegram+bot+business"
  "restaurant+software"
  "local-first+reconciliation"
)

for Q in "${QUERIES[@]}"; do
  URL="https://hn.algolia.com/api/v1/search_by_date?query=${Q}&tags=story&numericFilters=created_at_i%3E${WIN_FROM},created_at_i%3C${WIN_TO}&hitsPerPage=50"
  TMP="hn/_tmp_${Q}.json"
  HTTP=$(curl -sS -w "%{http_code}" -o "${TMP}" -A "${UA}" "${URL}" 2>/dev/null || echo "000")
  if [ "${HTTP}" = "200" ] && [ -s "${TMP}" ]; then
    SHA=$(sha256sum "${TMP}" | cut -c1-6)
    NBHITS=$(python3 -c "import json; d=json.load(open('${TMP}')); print(d.get('nbHits',0))" 2>/dev/null || echo "ERR")
    FINAL="hn/${Q}_${SHA}.json"
    mv "${TMP}" "${FINAL}"
    echo "OK ${Q} HTTP=${HTTP} nbHits=${NBHITS} -> ${FINAL}"
  else
    echo "FAIL ${Q} HTTP=${HTTP}"
    rm -f "${TMP}"
  fi
done
