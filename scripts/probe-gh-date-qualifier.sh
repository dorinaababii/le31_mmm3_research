#!/usr/bin/env bash
# Probe: distinguish "topic genuinely quiet in window" from "you used the dead pushed_at:>= qualifier".
# Found on the 2026-10-22 pass: pushed_at:>= returns total_count=0 for every topic while pushed:>= works.
# Run this BEFORE escalating to the gh_nodate/ fallback. Exits 0 = fallback not needed, 1 = justified.
set -u
TOPIC="${1:?usage: probe-gh-date-qualifier.sh <topic> <since YYYY-MM-DD>}"
SINCE="${2:?usage: probe-gh-date-qualifier.sh <topic> <since YYYY-MM-DD>}"
set -a; . /opt/data/.env; set +a

tc() {
  curl -s -H "Authorization: token ${HERMES_GITHUB_TOKEN}" \
    -H "Accept: application/vnd.github+json" \
    "https://api.github.com/search/repositories?q=$1&per_page=1" \
  | python3 -c 'import sys,json
try:
    d=json.load(sys.stdin)
except Exception:
    print("PARSE_ERROR"); sys.exit(0)
print(d.get("total_count","?") if "total_count" in d else "AUTH_ERR:"+str(d.get("message"))[:40])'
}

echo "qualifier probe for topic=${TOPIC} since=${SINCE}"
A=$(tc "$(python3 -c "import urllib.parse,sys;print(urllib.parse.quote('topic:${TOPIC}'))")")
B=$(tc "$(python3 -c "import urllib.parse,sys;print(urllib.parse.quote('topic:${TOPIC} pushed_at:>=${SINCE}'))")")
C=$(tc "$(python3 -c "import urllib.parse,sys;print(urllib.parse.quote('topic:${TOPIC} pushed:>=${SINCE}'))")")
D=$(tc "$(python3 -c "import urllib.parse,sys;print(urllib.parse.quote('topic:${TOPIC} created:>=${SINCE}'))")")
printf '  topic:%-22s                 -> %s\n' "$TOPIC" "$A"
printf '  topic:%-22s pushed_at:>=   -> %s   <-- dead qualifier\n' "$TOPIC" "$B"
printf '  topic:%-22s pushed:>=      -> %s   <-- CORRECT spelling\n' "$TOPIC" "$C"
printf '  topic:%-22s created:>=     -> %s\n' "$TOPIC" "$D"

# Fallback justified only if the CORRECT spelling also returns zero.
if [ "$C" = "0" ]; then
  echo "RESULT: pushed:>= also zero -> fallback to gh_nodate/ is justified"
  exit 1
fi
echo "RESULT: pushed:>= returns data -> topic is NOT quiet; do NOT run the no-date fallback"
exit 0