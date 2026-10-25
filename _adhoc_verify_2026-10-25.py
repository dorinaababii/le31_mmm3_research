#!/usr/bin/env python3
"""Ad-hoc verification launcher for the LE31 brainstorm 2026-10-25 pass.

Pattern (per the skill's launcher rules):
  * the verifier BODY lives in a string constant;
  * it is written to tempfile.mkstemp(prefix="hermes-verify-", dir="/tmp") at RUNTIME;
  * it is executed, and unlinked in a finally block;
  * the inner body ends with a REAL sys.exit(1 if fails else 0) -- never a print;
  * the launcher initialises code = 1 BEFORE the try, so an exception cannot
    mask the real error via UnboundLocalError;
  * a --negctl mode reinjects a known-bad state and requires the exit code to
    flip 0 -> 1, proving the checks are load-bearing.

This is AD-HOC verification of a research pass's artefacts -- NOT a project test
suite. The repo has no canonical test/lint/build command for this artefact class.
"""
import os, sys, json, subprocess, tempfile, shutil

REPO = "/opt/data/le31_mmm3_research_work"
BASE = "/tmp/le31-brainstorm-2026-10-25"
REPORT = "/opt/data/le31-brainstorm-2026-10-25.md"
FALLBACK = "/opt/data/le31-brainstorm-2026-10-25.linear-fallback.json"
STANDALONE_INDEX = "/opt/data/INDEX.md"

# Feature number -> slug body (derived from what is ON DISK, not from any JSON string).
SLUGS = {
    "379": "le31-order-item-transition-actor-attribution-first-party-charter-explicit-user-action-vs-schema-no-actor-field-v1-order-item-transition-attribution",
    "380": "boethius68-kitchenlink-mit-swiftui-supabase-local-lan-relay-zero-cloud-offline-fallback-bonjour-p2p-all-14-eu-allergens-declaration-v1-zero-cloud-lan-relay-and-allergen-declaration-vocabulary",
    "381": "sajeercherukottayil-ordova-mit-dart-flutter-offline-cafe-ordering-kitchen-tablet-as-server-udp-discovery-beacon-websocket-local-wifi-v1-kitchen-tablet-as-server-and-local-discovery-vocabulary",
}

BODY = r'''
import json, os, glob, sys, subprocess, collections

REPO = "/opt/data/le31_mmm3_research_work"
BASE = "/tmp/le31-brainstorm-2026-10-25"
REPORT = "/opt/data/le31-brainstorm-2026-10-25.md"
FALLBACK = "/opt/data/le31-brainstorm-2026-10-25.linear-fallback.json"
STANDALONE_INDEX = "/opt/data/INDEX.md"
WIN_S, WIN_E = "2026-09-25", "2026-10-25"
SLUGS = json.loads(os.environ["VERIFY_SLUGS"])

fails = []
def chk(cond, label, detail=""):
    if cond:
        print("PASS " + label)
    else:
        print("FAIL " + label + ((" :: " + str(detail)) if detail else ""))
        fails.append(label)

def resolve(rel, d):
    """One helper; never re-derive the bare-vs-prefixed conditional at a call site."""
    return os.path.join(REPO, rel if rel.startswith(d + "/") else d + "/" + rel)

# ---- 1. report file + exact section shape ----
chk(os.path.isfile(REPORT), "report file exists")
txt = open(REPORT, encoding="utf-8").read()
for sec in ["## Sources fetched", "## Cross-app signals (other industries)",
            "## Restaurant-adjacent signals", "## Operator UX and HCI signals",
            "## Three cross-section ideas", "## LE31 gate verdict per idea",
            "## Why this could take LE31 further", "## Adjacent evidence", "## Blockers"]:
    chk(sec in txt, "report section: " + sec)
chk(txt.startswith("# LE31 Daily Brainstorm — 2026-10-25"), "report title line")

# ---- 2. source files vs sidecars, re-derived from disk ----
allf = sorted(f for f in glob.glob(BASE + "/**/*", recursive=True) if os.path.isfile(f))
side = [f for f in allf if os.path.basename(f).startswith("_")]
src  = [f for f in allf if not os.path.basename(f).startswith("_")]
byfam = collections.Counter(f.replace(BASE + "/", "").split("/")[0] for f in src)
chk(byfam.get("gh") == 17 and byfam.get("hn") == 8 and byfam.get("openalex") == 3
    and byfam.get("ph") == 1 and byfam.get("readmes") == 9,
    "source split 17gh/8hn/3oa/1ph/9readmes", dict(byfam))
chk((len(src), len(side), len(allf)) == (38, 11, 49),
    "38 source + 11 sidecars = 49 on disk", (len(src), len(side), len(allf)))
chk(("38 fetched source files" in txt) and ("11 metadata sidecars" in txt)
    and ("49 files on disk in total" in txt),
    "report states the same file counts as disk")

# ---- 3. no GH stubs; real data present ----
ghf = [f for f in src if "/gh/" in f]
chk(not [f for f in ghf if os.path.getsize(f) < 200], "no GH stub files (<200 B)")
chk(max(os.path.getsize(f) for f in ghf) > 100000, "largest GH file > 100 KB")

# ---- 4. anti-fabrication canary over SOURCE files only ----
leak = [f for f in src if b"LE31" in open(f, "rb").read()]
chk(not leak, "canary: 'LE31' absent from every source file", leak)

# ---- 5. manifest agrees with the raw files it describes ----
m = json.load(open(BASE + "/_fetch_results_all.json"))
bad = []
for q in m["github"]:
    f = q.get("file")
    if not f or not os.path.isfile(f):
        bad.append(("missing", q.get("query"))); continue
    d = json.load(open(f))
    if d.get("total_count") != q.get("total_count"): bad.append(("total_count", q.get("query")))
    if len(d.get("items", [])) != q.get("items_returned"): bad.append(("items", q.get("query")))
    if os.path.getsize(f) != q.get("bytes"): bad.append(("bytes", q.get("query")))
chk(not bad, "manifest agrees with raw GH files", bad)
chk(all(q.get("http_status") == 200 for q in m["github"]), "all 17 GH queries HTTP 200")
chk(m["producthunt"]["http_status"] == 200, "ProductHunt HTTP 200")

# ---- 6. in-window is created_at OR pushed_at ----
items = {}
for f in ghf:
    for it in json.load(open(f)).get("items", []):
        items[it["full_name"]] = it
chk(all(WIN_S <= (it.get("created_at") or "")[:10] <= WIN_E
        or WIN_S <= (it.get("pushed_at") or "")[:10] <= WIN_E
        for it in items.values()),
    "every repo is in-window by created_at OR pushed_at (%d repos)" % len(items))

# ---- 7. each pick: exactly one feature file + one HANDOFF, located by SLUG body ----
TEMPLATE = ["## Goal", "## Scope", "## Out of scope", "## Description", "## Data model",
            "## Implementation steps", "## Telegram interaction if any", "## Dependencies",
            "## Open questions", "## Why this matters"]
for num, body in SLUGS.items():
    ff = sorted(f for f in os.listdir(REPO + "/features") if f.startswith(num + "-"))
    chk(len(ff) == 1, "exactly one feature file for " + num, ff)
    if len(ff) != 1:
        continue
    chk(ff[0] == num + "-" + body + ".md", "feature " + num + " filename == expected slug")
    sf = sorted(f for f in os.listdir(REPO + "/specs") if f.endswith("-HANDOFF.md") and body in f)
    chk(len(sf) == 1, "exactly one HANDOFF for " + num + " (found by slug body)", sf)
    ft = open(os.path.join(REPO, "features", ff[0]), encoding="utf-8").read()
    for sec in TEMPLATE:
        chk(sec in ft, "feature " + num + " section: " + sec)
    ht = open(os.path.join(REPO, "specs", sf[0]), encoding="utf-8").read()
    for sec in ["## Active feature path", "## Seven-check gate verdict", "## Files to touch",
                "## Verification protocol reference", "## Rollback path",
                "## Mandatory LE31 skill list"]:
        chk(sec in ht, "HANDOFF " + num + " section: " + sec)

# ---- 8. fallback JSON: every path it names resolves ----
chk(os.path.isfile(FALLBACK), "linear fallback JSON exists")
fb = json.load(open(FALLBACK))
chk(fb["linear_status"] == "blocked", "fallback records linear_status=blocked")
chk(len(fb["intended_sub_issues"]) == 3, "fallback names 3 intended sub-issues")
chk(fb["anti_fabrication_canary"]["nonzero_matches"] == 0, "fallback records canary = 0")
chk(fb["gh_nodate_fallback_triggered"] is False, "fallback records fallback not triggered")
dead = [si[key] for si in fb["intended_sub_issues"] for key in ("feature_file", "handoff_file")
        if not os.path.isfile(resolve(si[key], si[key].split("/")[0]))]
chk(not dead, "TERMINAL: no path named by the fallback is dead", dead)
chk(all(si["project_id"] == "P-HMM-1" for si in fb["intended_sub_issues"]),
    "all 3 sub-issues routed to le31 Research (P-HMM-1)")
chk(all(si["labels"] == ["Feature"] for si in fb["intended_sub_issues"]),
    "all 3 sub-issues carry label Feature")
chk(all(si.get("verdict") in ("build", "experiment", "defer", "reject")
        for si in fb["intended_sub_issues"]), "every sub-issue carries a gate verdict")

# ---- 9. INDEX rows in BOTH files ----
for p in (STANDALONE_INDEX, os.path.join(REPO, "INDEX.md")):
    t = open(p, encoding="utf-8").read()
    chk(t.count("| 2026-10-25 | **Brainstorm**") == 1, "1 brainstorm log row in " + os.path.basename(p))
    chk(t.count("| 2026-10-25 (brainstorm) |") == 3, "3 pipeline rows in " + os.path.basename(p))
    for body in SLUGS.values():
        chk(body in t, "INDEX names slug in " + os.path.basename(p) + ": " + body[:40])

# ---- 10. the two INDEX files agree on this pass's content ----
a = open(STANDALONE_INDEX, encoding="utf-8").read()
b = open(os.path.join(REPO, "INDEX.md"), encoding="utf-8").read()
ra = [l for l in a.split("\n") if l.startswith("| 2026-10-25 | **Brainstorm**")]
rb = [l for l in b.split("\n") if l.startswith("| 2026-10-25 | **Brainstorm**")]
chk(ra and rb and ra[0] == rb[0], "the brainstorm log row is byte-identical in both INDEX files")

# ---- 11. the committed verifier is itself a real, exit-code-bearing checker ----
ver = os.path.join(REPO, "_verify_2026-10-25.py")
chk(os.path.isfile(ver), "committed verifier launcher exists")
if os.path.isfile(ver):
    v = open(ver, encoding="utf-8").read()
    chk("sys.exit(1 if fails else 0)" in v, "inner body ends with a real sys.exit, not a print")
    chk("code = 1" in v, "launcher initialises code = 1 before the try")
    chk("tempfile.mkstemp" in v and 'prefix="hermes-verify-"' in v,
        "launcher uses tempfile.mkstemp with the hermes-verify- prefix")
    chk("finally" in v and "os.unlink(path)" in v, "launcher unlinks the temp body in a finally")

# ---- 12. committed and pushed: assert against origin/main, not HEAD ----
def sh(c):
    return subprocess.run(c, shell=True, capture_output=True, text=True, cwd=REPO).stdout
for num, body in SLUGS.items():
    for rel in ("features/%s-%s.md" % (num, body), "specs/%s-HANDOFF.md" % body):
        chk(sh("git cat-file -e origin/main:%s" % rel).strip() == "" and
            subprocess.run("git cat-file -e origin/main:%s" % rel, shell=True,
                           cwd=REPO).returncode == 0,
            "on origin/main: " + rel.split("/")[-1][:55])
chk(sh("git diff --name-only origin/main -- INDEX.md features/379-* features/380-* "
       "features/381-* specs/*le31-order-item* specs/*boethius68* specs/*sajeercherukottayil*").strip() == "",
    "worktree matches origin/main for this pass's paths")
chk("Daily brainstorm 2026-10-25" in sh("git log --oneline -1 origin/main"),
    "origin/main tip is the 2026-10-25 brainstorm commit")

print("")
print("TOTAL FAILS:", len(fails))
for f in fails:
    print("  -", f)
sys.exit(1 if fails else 0)
'''


def run(body_text):
    code = 1
    try:
        fd, path = tempfile.mkstemp(prefix="hermes-verify-", dir="/tmp", suffix=".py")
        try:
            with os.fdopen(fd, "w") as fh:
                fh.write(body_text)
            r = subprocess.run([sys.executable, path], capture_output=True, text=True, timeout=300,
                               env={**os.environ, "VERIFY_SLUGS": json.dumps(SLUGS)})
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
        # Reinject the known-bad state (a dead path in the fallback) and require
        # the exit code to flip 0 -> 1. Restore in a finally; assert no residue.
        bak = FALLBACK + ".negctl.bak"
        orig = open(FALLBACK, encoding="utf-8").read()
        ok = False
        try:
            d = json.loads(orig)
            d["intended_sub_issues"][0]["feature_file"] = "features/379-DOES-NOT-EXIST.md"
            open(FALLBACK, "w", encoding="utf-8").write(json.dumps(d, indent=2))
            print("=== NEGATIVE CONTROL: dead path reinjected; expect exit 1 ===")
            rc = run(BODY)
            ok = (rc == 1)
            print("NEGCTL_EXIT=%d (must be 1)" % rc)
            print("NEGCTL_RESULT:", "PASS (exit flipped 0->1)" if ok else "FAIL (no flip)")
        finally:
            if os.path.exists(bak):
                shutil.move(bak, FALLBACK)
            else:
                open(FALLBACK, "w", encoding="utf-8").write(orig)
            residue = [f for f in os.listdir(os.path.dirname(FALLBACK))
                       if f.startswith(os.path.basename(FALLBACK) + ".negctl")]
            print("negctl residue after restore:", residue if residue else "NONE")
            print("fallback restored byte-identical:", open(FALLBACK, encoding="utf-8").read() == orig)
        sys.exit(0 if ok else 1)
    rc = run(BODY)
    print("VERIFY_EXIT=%d" % rc)
    sys.exit(rc)
