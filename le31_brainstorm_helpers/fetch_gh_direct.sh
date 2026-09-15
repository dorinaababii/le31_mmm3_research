#!/usr/bin/env bash
# GitHub direct GET for watch list repos
set +e
OUTDIR="/tmp/le31-brainstorm-2026-08-29"
cd "${OUTDIR}"
GH_TOKEN=$(grep HERMES_GITHUB_TOKEN /opt/data/.env | cut -d= -f2)
UA="Mozilla/5.0"
mkdir -p gh

REPOS=(
  "longnick/small-pos-open-source"
  "satisfecho/pos"
  "SGrappelli/pronto"
  "devnest-hq/restaurant-management-system"
  "Ritchalison/BalanceDesk"
  "nematjon555/telegram-restaurant-delivery-bot"
)

for R in "${REPOS[@]}"; do
  SLUG=$(echo "${R}" | tr '/' '-')
  TMP="gh/_tmp_${SLUG}.json"
  HTTP=$(curl -sS -w "%{http_code}" -o "${TMP}" -H "Authorization: Bearer ${GH_TOKEN}" -H "Accept: application/vnd.github+json" -H "User-Agent: ${UA}" -H "X-GitHub-Api-Version: 2022-11-28" "https://api.github.com/repos/${R}" 2>/dev/null || echo "000")
  if [ "${HTTP}" = "200" ] && [ -s "${TMP}" ]; then
    SHA=$(sha256sum "${TMP}" | cut -c1-6)
    FINAL="gh/direct_${SLUG}_${SHA}.json"
    mv "${TMP}" "${FINAL}"
    STAR=$(python3 -c "import json; d=json.load(open('${FINAL}')); print(d.get('stargazers_count',0))" 2>/dev/null || echo "ERR")
    LIC=$(python3 -c "import json; d=json.load(open('${FINAL}')); print((d.get('license') or {}).get('spdx_id') or 'null')" 2>/dev/null || echo "ERR")
    CREATED=$(python3 -c "import json; d=json.load(open('${FINAL}')); print(d.get('created_at','n/a'))" 2>/dev/null || echo "ERR")
    PUSHED=$(python3 -c "import json; d=json.load(open('${FINAL}')); print(d.get('pushed_at','n/a'))" 2>/dev/null || echo "ERR")
    echo "OK ${R} HTTP=${HTTP} stars=${STAR} license=${LIC} created=${CREATED} pushed=${PUSHED} -> ${FINAL}"
  else
    echo "FAIL ${R} HTTP=${HTTP}"
    if [ -s "${TMP}" ]; then
      mv "${TMP}" "gh/_FAIL_direct_${SLUG}.json"
    else
      rm -f "${TMP}"
    fi
  fi
done
