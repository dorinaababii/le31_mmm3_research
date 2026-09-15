#!/usr/bin/env bash
# GitHub search repositories fetch loop
set +e
OUTDIR="/tmp/le31-brainstorm-2026-08-29"
cd "${OUTDIR}"
GH_TOKEN=$(grep HERMES_GITHUB_TOKEN /opt/data/.env | cut -d= -f2)
UA="Mozilla/5.0"
CREATED="2026-07-30..2026-08-29"
mkdir -p gh

run_search() {
  local Q="$1"
  local SLUG="$2"
  local TMP="gh/_tmp_${SLUG}.json"
  URL="https://api.github.com/search/repositories?q=${Q}&sort=stars&order=desc&per_page=30&created=${CREATED}"
  HTTP=$(curl -sS -w "%{http_code}" -o "${TMP}" -H "Authorization: Bearer ${GH_TOKEN}" -H "Accept: application/vnd.github+json" -H "User-Agent: ${UA}" -H "X-GitHub-Api-Version: 2022-11-28" "${URL}" 2>/dev/null || echo "000")
  if [ "${HTTP}" = "200" ] && [ -s "${TMP}" ]; then
    SHA=$(sha256sum "${TMP}" | cut -c1-6)
    TC=$(python3 -c "import json; d=json.load(open('${TMP}')); print(d.get('total_count',0))" 2>/dev/null || echo "ERR")
    FINAL="gh/${SLUG}_${SHA}.json"
    mv "${TMP}" "${FINAL}"
    echo "OK ${SLUG} HTTP=${HTTP} total_count=${TC} -> ${FINAL}"
  else
    echo "FAIL ${SLUG} HTTP=${HTTP}"
    # Keep the failure response for visibility
    if [ -s "${TMP}" ]; then
      mv "${TMP}" "gh/_FAIL_${SLUG}.json"
    else
      rm -f "${TMP}"
    fi
  fi
}

# Topic queries (6)
run_search "topic:small-business+archived:false" "topic_small-business_archived-false"
run_search "topic:hci+archived:false" "topic_hci_archived-false"
run_search "topic:mobile-ux+archived:false" "topic_mobile-ux_archived-false"
run_search "topic:real-time+archived:false" "topic_real-time_archived-false"
run_search "topic:append-only+archived:false" "topic_append-only_archived-false"
run_search "topic:telegram-bot+archived:false" "topic_telegram-bot_archived-false"

# Creative + qualified queries (6) — percent-encoded > as %3E
run_search "restaurant+language:python+stars:%3E1+archived:false" "creative_restaurant_py_stars_gt1"
run_search "kitchen+display+language:python+stars:%3E1+archived:false" "creative_kitchen-display_py_stars_gt1"
run_search "telegram+kitchen+language:python+stars:%3E1+archived:false" "creative_telegram-kitchen_py_stars_gt1"
run_search "htmx+language:python+stars:%3E1+archived:false" "creative_htmx_py_stars_gt1"
run_search "local-first+language:python+stars:%3E1+archived:false" "creative_local-first_py_stars_gt1"
run_search "aiogram+restaurant+stars:%3E1+archived:false" "creative_aiogram_restaurant_stars_gt1"
