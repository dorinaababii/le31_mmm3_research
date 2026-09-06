#!/usr/bin/env bash
# LE31 daily research fetcher — 2026-09-06
# Window: 2026-08-30 00:00 UTC .. 2026-09-06 06:30 UTC (7-day; epoch 1788048000..1788676200).
# Mirrors prior fetch_le31_*.sh patterns (see git log for fetch_le31_2026-08-09.sh).
#
# Raw response convention: this cron's write-safe root is /opt/data, so all raw
# fetches land under /opt/data/le31-daily-2026-09-06/ (not /tmp/... as the
# le31-daily-research skill nominally mandates — flagged for skill patch).
#
# Sources: HN Algolia (UA=Mozilla/5.0), arXiv (no date param — silently dropped
# in 2026), OpenAlex (colon-syntax date filter), GitHub Search (Bearer token,
# language:python, pushed:>2026-08-30), GitHub direct-repo GET (watchlist of
# 12), PyPI JSON (9 packages), GitHub releases.atom (6 repos), ECB
# eurofxref-daily.xml, CNIL RSS EN+FR, EUR-Lex (legacy + WS). ScienceDirect
# BLOCKED — not attempted.
#
# Token: HERMES_GITHUB_TOKEN from /opt/data/.env.
set -u

DATE="2026-09-06"
OUT="/opt/data/le31-daily-${DATE}"
mkdir -p "${OUT}"/{hn_algolia,arxiv,openalex,github_search,github_watchlist,pypi,releases_atom,ecb,cnil,eurlex,scripts}

UA="Mozilla/5.0"
START=1788048000   # 2026-08-30T00:00:00Z
END=1788676200     # 2026-09-06T06:30:00Z

# Source HERMES_GITHUB_TOKEN
GH_TOKEN="$(grep '^HERMES_GITHUB_TOKEN=' /opt/data/.env | head -1 | cut -d= -f2-)"

# Rate-limit config
ARXIV_PAUSE=3.5
GITHUB_PAUSE=0.4

###############################
# 1. HN Algolia — 8 queries
###############################
for Q in "restaurant POS" "aiogram" "aiogram restaurant" "telegram bot" \
         "fastapi SSE" "fastapi restaurant" "kitchen display" "restaurant inventory"; do
  ENC=$(python3 -c "import urllib.parse,sys;print(urllib.parse.quote(sys.argv[1]))" "$Q")
  OUT_F="${OUT}/hn_algolia/${Q// /_}.json"
  URL="https://hn.algolia.com/api/v1/search_by_date?query=${ENC}&tags=story&numericFilters=created_at_i%3E${START}%20AND%20created_at_i%3C${END}&hitsPerPage=20"
  echo "[fetch HN] $Q -> $OUT_F"
  curl -sS -A "$UA" "$URL" -o "$OUT_F" -w "  http=%{http_code} bytes=%{size_download}\n"
done

###############################
# 2. arXiv — 8 queries (no submittedDate — silently dropped)
###############################
for Q in "aiogram" "aiogram+restaurant" "fastapi+SSE" "fastapi+restaurant" \
         "kitchen+display" "restaurant+POS" "restaurant+inventory" "telegram+bot"; do
  OUT_F="${OUT}/arxiv/${Q//+/_}.xml"
  URL="http://export.arxiv.org/api/query?search_query=${Q}&max_results=20"
  echo "[fetch arXiv] $Q -> $OUT_F"
  curl -sSL "$URL" -o "$OUT_F" -w "  http=%{http_code} bytes=%{size_download}\n"
  sleep $ARXIV_PAUSE
done

###############################
# 3. OpenAlex — 6 queries (colon-syntax date filter)
###############################
OA_FROM="2026-08-30"
OA_TO="2026-09-05"
for Q in "restaurant" "kitchen display" "restaurant POS" "restaurant inventory" \
         "aiogram" "telegram bot restaurant"; do
  ENC=$(python3 -c "import urllib.parse,sys;print(urllib.parse.quote(sys.argv[1]))" "$Q")
  OUT_F="${OUT}/openalex/${Q// /_}.json"
  URL="https://api.openalex.org/works?search=${ENC}&filter=from_publication_date:${OA_FROM},to_publication_date:${OA_TO}&per_page=10"
  echo "[fetch OpenAlex] $Q -> $OUT_F"
  curl -sS "$URL" -o "$OUT_F" -w "  http=%{http_code} bytes=%{size_download}\n"
  sleep $GITHUB_PAUSE
done

###############################
# 4. GitHub Search Repositories — 7 queries
###############################
declare -a QUERIES=(
  "fastapi+restaurant"
  "telegram+bot+restaurant"
  "kitchen+display"
  "kitchen+inventory"
  "aiogram+restaurant"
  "sqlmodel+restaurant"
  "pos+system+restaurant"
)
for Q in "${QUERIES[@]}"; do
  OUT_F="${OUT}/github_search/${Q//+/_}.json"
  ENC=$(python3 -c "import urllib.parse,sys;print(urllib.parse.quote(sys.argv[1]))" "$Q")
  URL="https://api.github.com/search/repositories?q=${ENC}+language:python+pushed:>2026-08-30&sort=updated&order=desc&per_page=30"
  echo "[fetch GitHub Search] $Q -> $OUT_F"
  curl -sS -H "Authorization: Bearer $GH_TOKEN" "$URL" -o "$OUT_F" -w "  http=%{http_code} bytes=%{size_download}\n"
  sleep $GITHUB_PAUSE
done

###############################
# 5. GitHub Watchlist — 12 repos direct repo GET
###############################
REPOS=(
  "longnick/small-pos-open-source"
  "satisfecho/pos"
  "SGrappelli/pronto"
  "devnest-hq/restaurant-management-system"
  "helloman3/foodieshub"
  "SkrudjReal/geminka-agent"
  "captainsaify/textile-erp"
  "jonalemndi2/ALdia"
  "RafaelEmery/rafood-api"
  "Ritchalison/BalanceDesk"
  "nematjon555/telegram-restaurant-delivery-bot"
  "nicholasrossi0530/escpos-render"
)
for R in "${REPOS[@]}"; do
  SAFE="${R//\//__}"
  OUT_F="${OUT}/github_watchlist/${SAFE}.json"
  URL="https://api.github.com/repos/${R}"
  echo "[fetch Watchlist] $R -> $OUT_F"
  curl -sS -H "Authorization: Bearer $GH_TOKEN" "$URL" -o "$OUT_F" -w "  http=%{http_code} bytes=%{size_download}\n"
  sleep $GITHUB_PAUSE
done

###############################
# 6. PyPI JSON — 9 packages
###############################
PKGS=(sqlalchemy pydantic pydantic-core sqlmodel alembic aiogram fastapi uvicorn httpx)
for P in "${PKGS[@]}"; do
  OUT_F="${OUT}/pypi/${P}.json"
  URL="https://pypi.org/pypi/${P}/json"
  echo "[fetch PyPI] $P -> $OUT_F"
  curl -sS "$URL" -o "$OUT_F" -w "  http=%{http_code} bytes=%{size_download}\n"
  sleep 0.2
done

###############################
# 7. GitHub releases.atom — 6 repos
###############################
ATOM_REPOS=(
  "sqlalchemy/sqlalchemy"
  "pydantic/pydantic"
  "sqlmodel/sqlmodel"
  "aiogram/aiogram"
  "fastapi/fastapi"
  "encode/uvicorn"
)
for R in "${ATOM_REPOS[@]}"; do
  SAFE="${R//\//_}"
  OUT_F="${OUT}/releases_atom/${SAFE}.atom"
  URL="https://github.com/${R}/releases.atom"
  echo "[fetch atom] $R -> $OUT_F"
  curl -sSL "$URL" -o "$OUT_F" -w "  http=%{http_code} bytes=%{size_download}\n"
  sleep $GITHUB_PAUSE
done

###############################
# 8. ECB eurofxref-daily.xml
###############################
curl -sSL "https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml" \
  -o "${OUT}/ecb/eurofxref-daily.xml" \
  -w "[fetch ECB] http=%{http_code} bytes=%{size_download}\n"

###############################
# 9. CNIL RSS EN + FR
###############################
curl -sS -A "$UA" "https://www.cnil.fr/en/rss.xml" \
  -o "${OUT}/cnil/en_rss.xml" \
  -w "[fetch CNIL EN] http=%{http_code} bytes=%{size_download}\n"
curl -sS -A "$UA" "https://www.cnil.fr/fr/rss.xml" \
  -o "${OUT}/cnil/fr_rss.xml" \
  -w "[fetch CNIL FR] http=%{http_code} bytes=%{size_download}\n"

###############################
# 10. EUR-Lex (both endpoints; documented failure mode today)
###############################
curl -sS "https://eur-lex.europa.eu/RSS/feed.rss" \
  -o "${OUT}/eurlex/feed.rss" \
  -w "[fetch EUR-Lex RSS] http=%{http_code} bytes=%{size_download}\n"
curl -sS "https://eur-lex.europa.eu/eurlex-ws" \
  -o "${OUT}/eurlex/eurlws.html" \
  -w "[fetch EUR-Lex WS] http=%{http_code} bytes=%{size_download}\n"

echo "[done] 2026-09-06 fetches"
