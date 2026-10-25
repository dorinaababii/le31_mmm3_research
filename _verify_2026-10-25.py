#!/usr/bin/env python3
"""Post-pass verification for LE31 brainstorm 2026-10-25.
Launcher pattern: the verifier BODY lives in a string, is written to
tempfile.mkstemp(dir='/tmp') at runtime, executed, and unlinked in a finally.
The inner body ends with a REAL sys.exit(1 if fails else 0) -- never a print.
Exit code is the verifier's output; the launcher initialises code = 1 BEFORE the try.
"""
import os, sys, json, subprocess, tempfile, shutil

BODY = r'''
import json, os, glob, sys, subprocess, collections

REPO = "/opt/data/le31_mmm3_research_work"
BASE = "/tmp/le31-brainstorm-2026-10-25"
REPORT = "/opt/data/le31-brainstorm-2026-10-25.md"
FALLBACK = "/opt/data/le31-brainstorm-2026-10-25.linear-fallback.json"
WIN_S, WIN_E = "2026-09-25", "2026-10-25"

fails = []
def chk(cond, label, detail=""):
    if cond:
        print("PASS " + label)
    else:
        print("FAIL " + label + ((" :: " + str(detail)) if detail else ""))
        fails.append(label)

def resolve(rel, d):
    """One helper, never re-derive the bare-vs-prefixed conditional (83rd-pass bug)."""
    if rel.startswith(d + "/"):
        return os.path.join(REPO, rel)
    return os.path.join(REPO, d, rel)

# ---------- 1. report file ----------
chk(os.path.isfile(REPORT), "report file exists", REPORT)
if os.path.isfile(REPORT):
    txt = open(REPORT, encoding="utf-8").read()
    for sec in ["## Sources fetched", "## Cross-app signals (other industries)",
                "## Restaurant-adjacent signals", "## Operator UX and HCI signals",
                "## Three cross-section ideas", "## LE31 gate verdict per idea",
                "## Why this could take LE31 further", "## Adjacent evidence", "## Blockers"]:
        chk(sec in txt, "report has section: " + sec)

# ---------- 2. fetch files on disk ----------
allf = sorted(f for f in glob.glob(BASE + "/**/*", recursive=True) if os.path.isfile(f))
side = [f for f in allf if os.path.basename(f).startswith("_")]
src  = [f for f in allf if not os.path.basename(f).startswith("_")]
byfam = collections.Counter(f.replace(BASE + "/", "").split("/")[0] for f in src)
# 38 source files = 17 gh + 8 hn + 3 openalex + 1 ph + 9 readmes
# (the readmes/ family is the parent's own raw README fetches, added AFTER the
#  subagent's manifest was written -- counted as source, not sidecar, because
#  they are third-party content.)
chk(byfam.get("gh") == 17 and byfam.get("hn") == 8 and byfam.get("openalex") == 3
    and byfam.get("ph") == 1 and byfam.get("readmes") == 9,
    "source file split 17gh/8hn/3oa/1ph/9readmes", dict(byfam))
chk(len(src) == 38, "38 fetched source files (excluding sidecars)", len(src))
chk(len(side) == 11, "11 metadata sidecars", len(side))
chk(len(allf) == 49, "49 files on disk in total", len(allf))

# ---------- 3. stub check ----------
ghf = [f for f in src if "/gh/" in f]
stubs = [f for f in ghf if os.path.getsize(f) < 200]
chk(not stubs, "no GH stub files (<200 bytes)", stubs)
chk(max(os.path.getsize(f) for f in ghf) > 100000,
    "largest GH file > 100KB", max(os.path.getsize(f) for f in ghf))

# ---------- 4. anti-fabrication canary over SOURCE files only ----------
hits = []
for f in src:
    try:
        if b"LE31" in open(f, "rb").read():
            hits.append(f)
    except Exception as e:
        hits.append("%s (%s)" % (f, e))
chk(not hits, "anti-fabrication canary: 'LE31' absent from all source files", hits)

# ---------- 5. manifest agreement with disk ----------
mp = BASE + "/_fetch_results_all.json"
chk(os.path.isfile(mp), "fetch manifest exists")
m = json.load(open(mp))
bad = []
for q in m["github"]:
    f = q.get("file")
    if not f or not os.path.isfile(f):
        bad.append(("missing", q.get("query"))); continue
    d = json.load(open(f))
    if d.get("total_count") != q.get("total_count"): bad.append(("tc", q.get("query")))
    if len(d.get("items", [])) != q.get("items_returned"): bad.append(("items", q.get("query")))
    if os.path.getsize(f) != q.get("bytes"): bad.append(("bytes", q.get("query")))
chk(not bad, "manifest agrees with raw GH files", bad)
chk(all(q.get("http_status") == 200 for q in m["github"]), "all 17 GH queries HTTP 200")
chk(m.get("producthunt", {}).get("http_status") == 200, "ProductHunt HTTP 200")

# ---------- 6. in-window filter is OR, not AND ----------
items = {}
for f in ghf:
    for it in json.load(open(f)).get("items", []):
        items[it["full_name"]] = it
ok_or = True
for fn, it in items.items():
    c_in = WIN_S <= (it.get("created_at") or "")[:10] <= WIN_E
    p_in = WIN_S <= (it.get("pushed_at") or "")[:10] <= WIN_E
    if not (c_in or p_in):
        ok_or = False
chk(ok_or, "every returned repo is in-window by created_at OR pushed_at")

# ---------- 7. the three picks: feature + HANDOFF exist, and paths resolve ----------
PICKS = {
    "379": "le31-order-item-transition-actor-attribution-first-party-charter-explicit-user-action-vs-schema-no-actor-field-v1-order-item-transition-attribution",
    "380": "boethius68-kitchenlink-mit-swiftui-supabase-local-lan-relay-zero-cloud-offline-fallback-bonjour-p2p-all-14-eu-allergens-declaration-v1-zero-cloud-lan-relay-and-allergen-declaration-vocabulary",
    "381": "sajeercherukottayil-ordova-mit-dart-flutter-offline-cafe-ordering-kitchen-tablet-as-server-udp-discovery-beacon-websocket-local-wifi-v1-kitchen-tablet-as-server-and-local-discovery-vocabulary",
}
for num, body in PICKS.items():
    ff = sorted(f for f in os.listdir(REPO + "/features") if f.startswith(num + "-"))
    chk(len(ff) == 1, "exactly one feature file for " + num, ff)
    if len(ff) == 1:
        chk(ff[0] == num + "-" + body + ".md", "feature " + num + " filename matches expected slug", ff[0])
        sf = sorted(f for f in os.listdir(REPO + "/specs") if f.endswith("-HANDOFF.md") and body in f)
        chk(len(sf) == 1, "exactly one HANDOFF for " + num + " (located by SLUG body, not number)", sf)
    # feature file must carry all template sections
    p = os.path.join(REPO, "features", ff[0]) if len(ff) == 1 else None
    if p and os.path.isfile(p):
        t = open(p, encoding="utf-8").read()
        for sec in ["## Goal", "## Scope", "## Out of scope", "## Description",
                    "## Data model", "## Implementation steps", "## Telegram interaction if any",
                    "## Dependencies", "## Open questions", "## Why this matters"]:
            chk(sec in t, "feature " + num + " has section: " + sec)

# ---------- 8. fallback JSON: every referenced path resolves ----------
chk(os.path.isfile(FALLBACK), "linear fallback JSON exists", FALLBACK)
if os.path.isfile(FALLBACK):
    fb = json.load(open(FALLBACK))
    chk(fb.get("linear_status") == "blocked", "fallback records linear_status=blocked")
    chk(fb.get("report_file") == REPORT, "fallback report_file matches")
    for si in fb.get("intended_sub_issues", []):
        for key in ("feature_file", "handoff_file"):
            rel = si.get(key)
            chk(bool(rel) and os.path.isfile(resolve(rel, rel.split("/")[0])),
                "fallback " + si.get("slot") + " " + key + " resolves: " + str(rel))
    chk(len(fb.get("intended_sub_issues", [])) == 3, "fallback has 3 intended sub-issues")
    chk(fb.get("anti_fabrication_canary", {}).get("nonzero_matches") == 0,
        "fallback records canary nonzero_matches=0")
    chk(fb.get("gh_nodate_fallback_triggered") is False,
        "fallback records gh_nodate_fallback_triggered=false")

# ---------- 9. INDEX rows in BOTH files ----------
for p in ("/opt/data/INDEX.md", os.path.join(REPO, "INDEX.md")):
    t = open(p, encoding="utf-8").read()
    chk(t.count("| 2026-10-25 | **Brainstorm**") == 1, "INDEX has 1 brainstorm log row: " + p)
    chk(t.count("| 2026-10-25 (brainstorm) |") == 3, "INDEX has 3 pipeline rows: " + p)
    for body in PICKS.values():
        chk(body in t, "INDEX mentions pick slug in " + os.path.basename(p) + ": " + body[:45])

# ---------- 10. no dead path in the fallback (terminal assertion) ----------
if os.path.isfile(FALLBACK):
    fb = json.load(open(FALLBACK))
    dead = []
    for si in fb.get("intended_sub_issues", []):
        for key in ("feature_file", "handoff_file"):
            rel = si.get(key)
            if not rel or not os.path.isfile(resolve(rel, rel.split("/")[0])):
                dead.append(rel)
    chk(not dead, "TERMINAL: no referenced path in the fallback is dead", dead)

# ---------- 11. feature numbers are unique for this pass ----------
for num in PICKS:
    n = len([f for f in os.listdir(REPO + "/features") if f.startswith(num + "-")])
    chk(n == 1, "feature number " + num + " used exactly once on disk", n)

# ---------- 12. no self-reported third-party metrics restated as fact ----------
UNVERIFIED_MARKERS = ["self-reported", "NOT independently verified"]
for num in PICKS:
    p = os.path.join(REPO, "features", num + "-" + PICKS[num] + ".md")
    if os.path.isfile(p):
        t = open(p, encoding="utf-8").read()
        for bad_phrase in ["automated tests", "documented design decisions", "documented decisions"]:
            if bad_phrase in t.lower():
                chk(any(mk.lower() in t.lower() for mk in UNVERIFIED_MARKERS),
                    "feature " + num + " labels self-reported metrics unverified (" + bad_phrase + ")")

print("")
print("TOTAL FAILS:", len(fails))
if fails:
    for f in fails:
        print("  -", f)
sys.exit(1 if fails else 0)
'''

MUTATE_TARGET = None  # no mutation in the default run

def run(body_text, mutate=False):
    code = 1
    try:
        fd, path = tempfile.mkstemp(prefix="hermes-verify-", dir="/tmp", suffix=".py")
        try:
            with os.fdopen(fd, "w") as fh:
                fh.write(body_text)
            r = subprocess.run([sys.executable, path], capture_output=True, text=True, timeout=300)
            sys.stdout.write(r.stdout)
            if r.stderr:
                sys.stderr.write(r.stderr)
            code = r.returncode
        finally:
            try:
                os.unlink(path)
            except OSError:
                pass
    except Exception as e:
        print("LAUNCHER ERROR:", e)
        code = 1
    return code


if __name__ == "__main__":
    if "--negctl" in sys.argv:
        # Negative control: reinject the known-bad state (dead path in the fallback)
        # and require the exit code to flip 0 -> 1.
        fb = "/opt/data/le31-brainstorm-2026-10-25.linear-fallback.json"
        bak = fb + ".negctl.bak"
        orig = open(fb, encoding="utf-8").read()
        try:
            d = json.loads(orig)
            d["intended_sub_issues"][0]["feature_file"] = \
                "features/379-DOES-NOT-EXIST-dead-path-vocabulary.md"
            open(fb, "w", encoding="utf-8").write(json.dumps(d, indent=2))
            print("=== NEGATIVE CONTROL: dead path reinjected, expecting exit 1 ===")
            rc = run(BODY)
            print("NEGCTL_EXIT=%d (must be 1)" % rc)
            ok = (rc == 1)
            print("NEGCTL_RESULT:", "PASS (exit flipped 0->1)" if ok else "FAIL (exit did not flip)")
        finally:
            shutil.move(bak, fb) if os.path.exists(bak) else open(fb, "w", encoding="utf-8").write(orig)
            residue = [f for f in os.listdir(os.path.dirname(fb)) if f.startswith(os.path.basename(fb) + ".negctl")]
            print("negctl residue after restore:", residue if residue else "NONE")
            # verify the fallback was restored byte-identically
            print("fallback restored identical:", open(fb, encoding="utf-8").read() == orig)
        sys.exit(0 if ok else 1)
    else:
        rc = run(BODY)
        print("VERIFY_EXIT=%d" % rc)
        sys.exit(rc)
