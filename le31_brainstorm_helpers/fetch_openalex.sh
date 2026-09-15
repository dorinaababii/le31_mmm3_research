#!/usr/bin/env bash
# OpenAlex /works fetch + candidate abstract dumps
set +e
OUTDIR="/tmp/le31-brainstorm-2026-08-29"
cd "${OUTDIR}"
UA="Mozilla/5.0"
mkdir -p openalex

QUERIES=(
  "creativity AND product|creativity-and-product"
  "restaurant OR hospitality AND hci|restaurant-or-hospitality-and-hci"
  "single page application OR no-build OR htmx|spa-or-htmx-or-nobuild"
  "phone-first interface restaurant|phone-first-interface-restaurant"
  "append-only ledger audit|append-only-ledger-audit"
)

run_search() {
  local Q="$1"
  local SLUG="$2"
  local TMP="openalex/_tmp_${SLUG}.json"
  URL="https://api.openalex.org/works?search=${Q}&per_page=10&filter=from_publication_date:2026-07-30,to_publication_date:2026-08-29&sort=publication_date:desc"
  HTTP=$(curl -sS -w "%{http_code}" -o "${TMP}" -A "${UA}" "${URL}" 2>/dev/null || echo "000")
  if [ "${HTTP}" = "200" ] && [ -s "${TMP}" ]; then
    SHA=$(sha256sum "${TMP}" | cut -c1-6)
    FINAL="openalex/${SLUG}_${SHA}.json"
    mv "${TMP}" "${FINAL}"
    CNT=$(python3 -c "import json; d=json.load(open('${FINAL}')); print(d.get('meta',{}).get('count',0))" 2>/dev/null || echo "ERR")
    echo "OK ${SLUG} HTTP=${HTTP} meta.count=${CNT} -> ${FINAL}"
  else
    echo "FAIL ${SLUG} HTTP=${HTTP}"
    if [ -s "${TMP}" ]; then
      mv "${TMP}" "openalex/_FAIL_${SLUG}.json"
    else
      rm -f "${TMP}"
    fi
  fi
}

run_search "creativity%20AND%20product" "creativity-and-product"
run_search "restaurant%20OR%20hospitality%20AND%20hci" "restaurant-or-hospitality-and-hci"
run_search "single%20page%20application%20OR%20no-build%20OR%20htmx" "spa-nobuild-htmx"
run_search "phone-first%20interface%20restaurant" "phone-first-interface-restaurant"
run_search "append-only%20ledger%20audit" "append-only-ledger-audit"
