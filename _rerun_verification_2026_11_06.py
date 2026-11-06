#!/usr/bin/env python3
"""LE31 brainstorm pass verifier — 2026-11-06.

Launcher pattern: the BODY lives as a string, is written to a
tempfile.mkstemp(prefix="hermes-verify-") in /tmp, executed, and unlinked
in a finally block. The inner body ends with a real sys.exit(1 if fails else 0).

Run:      python3 _rerun_verification_2026_11_06.py
Negctl:   python3 _rerun_verification_2026_11_06.py --negctl
"""
import os, sys, subprocess, tempfile, shutil

BODY = r'''
import os, sys, json, glob, subprocess, re

REPO = "/opt/data/le31_mmm3_research_work"
BASE = "/tmp/le31-brainstorm-2026-11-06"
REPORT = "/opt/data/le31-brainstorm-2026-11-06.md"
FALLBACK = "/opt/data/le31-brainstorm-2026-11-06.linear-fallback.json"
DATE = "2026-11-06"

fails = []
def chk(cond, label):
    if cond:
        print("  PASS  " + label)
    else:
        print("  FAIL  " + label)
        fails.append(label)

def sh(cmd):
    return subprocess.run(cmd, shell=True, capture_output=True, text=True).stdout

def walk(root):
    src, side = [], []
    for r, d, fs in os.walk(root):
        for f in fs:
            p = os.path.join(r, f)
            rel = os.path.relpath(p, root)
            if rel == "_manifest.json":
                continue
            (side if f.startswith("_") else src).append(p)
    return sorted(src), sorted(side)

print("== A. report file ==")
chk(os.path.exists(REPORT), "report exists")
rt = open(REPORT, encoding="utf-8").read() if os.path.exists(REPORT) else ""
SECTIONS = ["## Sources fetched", "## Cross-app signals (other industries)",
            "## Restaurant-adjacent signals", "## Operator UX and HCI signals",
            "## Three cross-section ideas", "## LE31 gate verdict per idea",
            "## Why this could take LE31 further", "## Adjacent evidence",
            "## Blockers"]
for s in SECTIONS:
    chk(s in rt, "report section: " + s)

print("\n== B. raw tree + canary ==")
chk(os.path.isdir(BASE), "raw tree exists")
src, side = walk(BASE)
chk(len(src) == 30, "source file count == 30 (got %d)" % len(src))
chk(len(side) == 4, "sidecar file count == 4 (got %d)" % len(side))
tot = sum(os.path.getsize(p) for p in src + side)
chk(tot == 7607154, "total bytes == 7607154 (got %d)" % tot)
bad = [p for p in src + side if open(p, "rb").read().count(b"LE31")]
chk(not bad, "canary: 0 files contain 'LE31' (%d offenders)" % len(bad))
# helper scripts must NOT be inside the raw tree
chk(not glob.glob(os.path.join(BASE, "**", "*.py"), recursive=True),
    "no .py inside the raw tree (helpers live in a sibling dir)")

print("\n== C. manifest agreement with disk ==")
mp = os.path.join(BASE, "_manifest.json")
chk(os.path.exists(mp), "manifest exists")
man = json.load(open(mp))
mism = []
for f in man.get("files", []):
    p = os.path.join(BASE, f["path"])
    if not os.path.exists(p):
        mism.append(f["path"]); continue
    if os.path.getsize(p) != f.get("bytes"):
        mism.append(f["path"])
chk(not mism, "manifest files[] agree with disk (%d mismatches)" % len(mism))
chk(len(man.get("files", [])) == 34, "manifest files[] == 34")

print("\n== D. stub scan ==")
gh = sorted(glob.glob(os.path.join(BASE, "gh", "*.json")))
chk(len(gh) == 17, "gh file count == 17")
szs = [os.path.getsize(p) for p in gh]
chk(6 not in szs, "no 6-byte gh file")
chk(73 not in szs, "no 73-byte gh file")
legit = 0; authfail = 0
for p in gh:
    if os.path.getsize(p) < 200:
        d = json.load(open(p))
        if "total_count" in d: legit += 1
        elif "message" in d: authfail += 1
chk(authfail == 0, "0 auth-failure envelopes")
chk(legit == 3, "3 legitimate empty envelopes (got %d)" % legit)

print("\n== E. feature contracts: template + paths ==")
TEMPLATE = ["## Goal", "## Scope", "## Out of scope", "## Description", "## Data model",
            "## Implementation steps", "## Telegram interaction if any", "## Dependencies",
            "## Open questions", "## Why this matters"]
PAIRS = [
    ("447", "le31-an-expired-batch-can-still-be-sold-from"),
    ("448", "le31-a-bill-has-no-human-facing-identity"),
    ("449", "le31-an-order-line-may-carry-any-price-it-likes"),
]
for num, slug in PAIRS:
    fs = glob.glob(os.path.join(REPO, "features", num + "-*.md"))
    chk(len(fs) == 1, "exactly 1 feature file for %s (got %d)" % (num, len(fs)))
    if not fs: continue
    ft = open(fs[0], encoding="utf-8").read()
    for sec in TEMPLATE:
        chk(sec in ft, "feature %s section: %s" % (num, sec))
    chk("**Out of scope" not in ft or "## Out of scope" in ft,
        "feature %s: 'Out of scope' is a real heading" % num)
    # HANDOFF located by SLUG body derived from the feature filename
    ss = glob.glob(os.path.join(REPO, "specs", slug + "-HANDOFF.md"))
    chk(len(ss) == 1, "exactly 1 HANDOFF for %s (got %d)" % (num, len(ss)))
    if ss:
        ht = open(ss[0], encoding="utf-8").read()
        chk("features/%s-" % num in ht, "HANDOFF %s references its feature path" % num)
        chk("Frozen contract" in ht, "HANDOFF %s has a Frozen contract section" % num)
        chk("Rollback path" in ht, "HANDOFF %s has a Rollback path section" % num)
        chk("Mandatory LE31 skill list" in ht, "HANDOFF %s has the skill list" % num)
        chk("Verification protocol reference" in ht, "HANDOFF %s has the verification protocol" % num)
    # every path mentioned in the contract/HANDOFF must resolve
    for doc in ([ft] + ([ht] if ss else [])):
        for m in re.finditer(r"features/(\d{3}-[A-Za-z0-9._-]+\.md)", doc):
            p = os.path.join(REPO, m.group(0))
            chk(os.path.exists(p), "referenced path resolves: %s" % m.group(0))

print("\n== F. INDEX rows in BOTH files ==")
for ip in ("/opt/data/INDEX.md", os.path.join(REPO, "INDEX.md")):
    chk(os.path.exists(ip), "INDEX exists: %s" % ip)
    if os.path.exists(ip):
        t = open(ip, encoding="utf-8").read()
        for num, slug in PAIRS:
            chk(("features/%s-%s.md" % (num, slug)) in t,
                "INDEX %s has the row for %s" % (os.path.basename(ip), num))

print("\n== G. git: membership in origin/main (NOT tip) ==")
log = sh("cd %s && git log --oneline origin/main" % REPO)
chk("Daily brainstorm 2026-11-06" in log, "the brainstorm commit IS in origin/main history")
for num, slug in PAIRS:
    # the HANDOFF filename carries the SLUG body, not the number prefix
    for p in ("features/%s-%s.md" % (num, slug), "specs/%s-HANDOFF.md" % slug):
        chk(sh("cd %s && git cat-file -e origin/main:%s" % (REPO, p)).strip() == "",
            "origin/main contains %s" % p)
chk(sh("cd %s && git diff --name-only origin/main -- INDEX.md features/447-* features/448-* features/449-* specs/le31-an-expired* specs/le31-a-bill* specs/le31-an-order*" % REPO).strip() == "",
    "worktree matches origin/main for this pass's paths")
chk(sh("cd %s && git status --porcelain -- INDEX.md features/447-* features/448-* features/449-* specs/le31-an-expired* specs/le31-a-bill* specs/le31-an-order*" % REPO).strip() == "",
    "nothing uncommitted for this pass's paths")

print("\n== H. Linear fallback ==")
chk(os.path.exists(FALLBACK), "fallback JSON exists")
if os.path.exists(FALLBACK):
    fb = json.load(open(FALLBACK))
    chk(fb.get("linear_write_status") == "blocked", "fallback records blocked")
    chk(fb["linear_error"].get("status") == 400, "fallback records HTTP 400")
    chk(bool(fb["linear_error"].get("parent_requestId")), "fallback records the parent requestId")
    chk(len(fb.get("intended_sub_issues", [])) == 3, "fallback has 3 sub-issues")
    for si in fb.get("intended_sub_issues", []):
        chk(si.get("project") == "le31 Research", "sub-issue %s routed to le31 Research" % si.get("feature_number"))
        chk(si.get("created") is False, "sub-issue %s marked NOT created" % si.get("feature_number"))
    chk(len(fb.get("le31_bucket_projects_checked", [])) == 3,
        "fallback records the 3 projects checked")
    lp = fb["read_endpoints_reverified_this_pass"]["list_projects"]
    chk(lp.get("le31_v2_owner_pains_exists") is False,
        "fallback records that 'le31 v2 owner-pains' does NOT exist")
    chk(lp.get("le31_v2_AI_exists") is False,
        "fallback records that 'le31 v2-AI' does NOT exist")

print("\n== I. report content integrity ==")
for slug, _ in PAIRS:
    chk(slug in rt, "report mentions %s" % slug)
# the report must NOT be a 'no new signal' report: the headline is the H1 line
h1 = next((l for l in rt.splitlines() if l.startswith("# ")), "")
chk(h1.strip() == "# LE31 Daily Brainstorm — 2026-11-06",
    "report H1 is the dated brainstorm headline (got %r)" % h1[:60])
chk("No new signal — sources quiet" not in rt,
    "report is not a 'no new signal' report")
chk("34 files" in rt and "7,607,154" in rt, "report states the re-derived file/byte totals")
chk("2,957" in rt and "591" in rt and "DEAD" in rt, "report records the dead-qualifier probe result")
chk("pushed:>=" in rt, "report names the correct qualifier")
chk("canary" in rt.lower(), "report records the canary")

print("\n== J. no stale scratch paths claimed as live ==")
scripts = "/opt/data/le31-brainstorm-2026-11-06-scripts"
chk(os.path.isdir(scripts), "helper scripts live in the sibling dir")
chk(not any(p.startswith(scripts) for p in glob.glob(os.path.join(REPO, "*"))),
    "helper scripts are NOT inside the repo")

print("\n" + "=" * 60)
if fails:
    print("FAILURES: %d" % len(fails))
    for f in fails:
        print("   - " + f)
    sys.exit(1)
print("ALL CHECKS PASS")
sys.exit(0)
'''


def run(mutate=False):
    fd, path = tempfile.mkstemp(prefix="hermes-verify-", dir="/tmp")
    os.close(fd)
    code = 1
    try:
        body = BODY
        if mutate:
            body = body.replace(
                'chk("Daily brainstorm 2026-11-06" in log,',
                'chk("Daily brainstorm 2026-11-06-MUTATED" in log,')
        with open(path, "w", encoding="utf-8") as f:
            f.write(body)
        p = subprocess.run([sys.executable, path], capture_output=True, text=True)
        print(p.stdout)
        if p.stderr.strip():
            print("STDERR:", p.stderr[-2000:])
        code = p.returncode
    finally:
        try:
            os.unlink(path)
        except Exception:
            pass
    return code


if __name__ == "__main__":
    if "--negctl" in sys.argv:
        print("=== NEGATIVE CONTROL (mutate the commit-membership assertion) ===")
        c = run(mutate=True)
        print("negctl exit code:", c)
        if c == 1:
            print("NEGCTL OK: the mutated assertion flipped the exit code 0 -> 1")
            sys.exit(0)
        print("NEGCTL FAILED: the mutated assertion did not flip the exit code")
        sys.exit(1)
    code = run()
    print("verifier exit code:", code)
    sys.exit(code)
