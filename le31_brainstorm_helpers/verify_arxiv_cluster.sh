#!/usr/bin/env bash
# Verify arXiv IDs from parent's daily-research cluster (non-HANSARD, non-ECHO)
set +e
OUTDIR="/tmp/le31-brainstorm-2026-08-29"
cd "${OUTDIR}"
UA="Mozilla/5.0"
mkdir -p arxiv_verify

# Look up by arXiv ID via OpenAlex's IDs filter (https://api.openalex.org/works/doi:... or works.search)
# Use the doi: prefix; arxiv preprints get DOI 10.48550/arxiv.XXXX.YYYYY
IDS=(
  "2608.27086|Contract-Centered-Architecture"
  "2608.23863|DreamLedger"
  "2608.21867|MemGuard"
  "2608.26237|Trace-Level-Provenance"
  "2608.23282|NL-to-Executable-Obligations"
)

for ENTRY in "${IDS[@]}"; do
  AXID="${ENTRY%%|*}"
  SLUG="${ENTRY##*|}"
  TMP="arxiv_verify/_tmp_${SLUG}.json"
  # Use OpenAlex with filter: ids.openalex:none matches anything; use filter=doi -> works/doi:10.48550/arxiv.XXXX.YYYYY
  URL="https://api.openalex.org/works/doi:10.48550/arxiv.${AXID}"
  HTTP=$(curl -sS -w "%{http_code}" -o "${TMP}" -A "${UA}" "${URL}" 2>/dev/null || echo "000")
  if [ "${HTTP}" = "200" ]; then
    # Some endpoints return a single work, others return error JSON
    ISWORK=$(python3 -c "import json; d=json.load(open('${TMP}')); print('YES' if d.get('id') and 'openalex.org/W' in str(d.get('id','')) else 'NO')" 2>/dev/null || echo "ERR")
    if [ "${ISWORK}" = "YES" ]; then
      SHA=$(sha256sum "${TMP}" | cut -c1-6)
      FINAL="arxiv_verify/${SLUG}_${AXID}_${SHA}.json"
      mv "${TMP}" "${FINAL}"
      TITLE=$(python3 -c "import json; d=json.load(open('${FINAL}')); print(d.get('title','n/a'))" 2>/dev/null)
      PUB=$(python3 -c "import json; d=json.load(open('${FINAL}')); print(d.get('publication_date','n/a'))" 2>/dev/null)
      ABS=$(python3 -c "import json; d=json.load(open('${FINAL}')); a=d.get('abstract_inverted_index'); print('YES' if a else ('NULL' if a is None else 'no'))" 2>/dev/null)
      echo "OK ${AXID} (${SLUG}) HTTP=${HTTP} ISWORK=${ISWORK} pub=${PUB} abs=${ABS} title=$(echo $TITLE | cut -c1-90)"
    else
      echo "FAIL ${AXID} not a work -> kept as _FAIL_${SLUG}.json"
      mv "${TMP}" "arxiv_verify/_FAIL_${SLUG}.json"
    fi
  else
    echo "FAIL ${AXID} HTTP=${HTTP}"
    if [ -s "${TMP}" ]; then
      mv "${TMP}" "arxiv_verify/_FAIL_${SLUG}.json"
    else
      rm -f "${TMP}"
    fi
  fi
done
