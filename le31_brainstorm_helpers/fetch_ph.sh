#!/usr/bin/env bash
# ProductHunt feed fetches
set +e
OUTDIR="/tmp/le31-brainstorm-2026-08-29"
cd "${OUTDIR}"
UA="Mozilla/5.0"
mkdir -p producthunt

FEEDS=(
  "https://www.producthunt.com/feed|ph_main"
  "https://www.producthunt.com/feed/topics/restaurant|ph_restaurant"
  "https://www.producthunt.com/feed/topics/pos|ph_pos"
  "https://www.producthunt.com/feed/topics/saas|ph_saas"
)

for ENTRY in "${FEEDS[@]}"; do
  URL="${ENTRY%%|*}"
  SLUG="${ENTRY##*|}"
  TMP="producthunt/_tmp_${SLUG}.xml"
  HTTP=$(curl -sS -w "%{http_code}" -o "${TMP}" -A "${UA}" "${URL}" 2>/dev/null || echo "000")
  if [ -s "${TMP}" ]; then
    SHA=$(sha256sum "${TMP}" | cut -c1-6)
    FINAL="producthunt/${SLUG}_${SHA}.xml"
    mv "${TMP}" "${FINAL}"
    N=$(grep -oc '<entry>' "${FINAL}" || echo 0)
    echo "${SLUG} HTTP=${HTTP} entries=${N} -> ${FINAL}"
  else
    echo "${SLUG} HTTP=${HTTP} (empty body)"
    rm -f "${TMP}"
    echo "${SLUG} HTTP=${HTTP}" >> producthunt/_failures.log
  fi
done
