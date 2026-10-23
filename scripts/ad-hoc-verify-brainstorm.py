#!/usr/bin/env python3
"""Ad-hoc verification for the 2026-10-23 LE31 brainstorm pass.

NOT SUITE GREEN. This repo has no canonical test/lint/build command (it is a
research-scratch repo of fetch scripts: no pyproject.toml, Makefile, or CI), so
this is focused ad-hoc verification of the changed paths.

Authored here because HERMES_WRITE_SAFE_ROOT=/opt/data blocks write_file to
/tmp/. Run via a tempfile launcher, or directly — it performs its own
tempfile lifecycle internally where needed.

Four of the eight flagged changed paths no longer exist (post-use scratch
scripts). This verifier asserts their ABSENCE explicitly rather than silently
omitting them, so a stale report cannot hide a deleted file.
"""
import glob
import json
import os
import re
import subprocess
import sys

REPO = "/opt/data/le31_mmm3_research_work"
FB = "/opt/data/le31-brainstorm-2026-10-23.linear-fallback.json"
REPORT = "/opt/data/le31-brainstorm-2026-10-23.md"

DELETED = (".ad_hoc_verify_final.py", ".bs_append_index.py",
           ".bs_fix_fallback_numbers.py", ".bs_verify_picks_2026_10_23.py")
LIVE = ("_rerun_verification.py", "scripts/negative-control.py",
        "scripts/probe-gh-date-qualifier.sh")

results = []
def chk(ok, label, detail=""):
    results.append((bool(ok), label, detail))

def resolve(rel, d):
    """Bare-vs-prefixed normalisation in one place (83rd-pass rename pitfall)."""
    rel = rel.lstrip("/")
    return os.path.join(REPO, rel if rel.startswith(d + "/") else f"{d}/{rel}")


# 0. deleted scratch paths are genuinely gone (not silently unverified)
for f in DELETED:
    chk(not os.path.exists(os.path.join(REPO, f)), f"scratch removed: {f}")

# 1. surviving tools exist, compile, and are committed
for f in LIVE:
    p = os.path.join(REPO, f)
    chk(os.path.isfile(p), f"exists: {f}")
    chk(subprocess.run(["git", "-C", REPO, "ls-files", "--error-unmatch", f],
                       capture_output=True).returncode == 0, f"tracked in git: {f}")

for f in ("_rerun_verification.py", "scripts/negative-control.py"):
    r = subprocess.run([sys.executable, "-m", "py_compile", os.path.join(REPO, f)],
                       capture_output=True, text=True)
    chk(r.returncode == 0, f"compiles clean: {f}", r.stderr.strip()[:160])

r = subprocess.run(["bash", "-n", os.path.join(REPO, "scripts/probe-gh-date-qualifier.sh")],
                   capture_output=True, text=True)
chk(r.returncode == 0, "bash -n clean: probe script", r.stderr.strip()[:160])

# 2. the probe's central claim, live — it goes stale silently if GitHub changes
r = subprocess.run(["bash", os.path.join(REPO, "scripts/probe-gh-date-qualifier.sh"),
                    "restaurant", "2026-09-24"], capture_output=True, text=True, timeout=180)
dead = re.search(r"pushed_at:>=\s*-> (\d+)", r.stdout)
works = re.search(r"pushed:>=\s*-> (\d+)", r.stdout)
chk(r.returncode == 0, "probe exits 0 (no-date fallback not needed)", f"exit={r.returncode}")
chk(dead and dead.group(1) == "0", "live: pushed_at:>= still returns 0 (dead qualifier)",
    dead.group(1) if dead else "not observed")
chk(works and works.group(1) not in ("0", "AUTH_ERR"),
    "live: pushed:>= still returns data (correct qualifier)",
    works.group(1) if works else "not observed")
chk("RESULT: pushed:>= returns data" in r.stdout, "probe reaches correct branch")

# 3. launcher tempfile lifecycle: created, used, unlinked, no leak on re-run
before = set(glob.glob("/tmp/hermes-verify-*"))
r = subprocess.run([sys.executable, os.path.join(REPO, "_rerun_verification.py")],
                   capture_output=True, text=True, timeout=300, cwd=REPO)
chk(r.returncode == 0, "verifier exits 0 on committed state", r.stdout[-300:])
m = re.search(r"\[launcher\] cleaned up (/tmp/hermes-verify-\S+\.py)", r.stdout)
chk(bool(m), "launcher reports tempfile cleanup")
chk(bool(m) and not os.path.exists(m.group(1)), "launcher tempfile actually gone from disk")
r2 = subprocess.run([sys.executable, os.path.join(REPO, "_rerun_verification.py")],
                    capture_output=True, text=True, timeout=300, cwd=REPO)
leaked = set(glob.glob("/tmp/hermes-verify-*")) - before
chk(not leaked, "repeat run leaks no /tmp artefacts", ",".join(sorted(leaked)))
chk(r2.returncode == 0, "verifier idempotent across runs")

# 4. fallback JSON: schema, honest failure claim, every path resolves
fb = json.load(open(FB))
chk(fb["linear_status"] == "blocked", "fallback: linear_status blocked")
chk(fb["linear_error"]["consecutive_days_blocked"] == 35, "fallback: 35 days recorded")
chk(fb["linear_error"]["requestId"] == "a4eed7f5dc4bccf7", "fallback: real requestId")
chk(len(fb["issues"]) == 4, "fallback: 4 issues (1 parent + 3 picks)")
chk(all(i["created"] is False for i in fb["issues"]),
    "fallback: every issue marked NOT created (no false success)")
chk(all(i["project_id"] == "P-HMM-1" for i in fb["issues"]),
    "fallback: all routed to le31 Research P-HMM-1")

dead_paths = [resolve(f"{mm.group(1)}/{mm.group(2)}", mm.group(1))
              for i in fb["issues"]
              for mm in re.finditer(r"(features|specs)/([0-9A-Za-z_.-]+?\.md)", i["body"])
              if not os.path.isfile(resolve(f"{mm.group(1)}/{mm.group(2)}", mm.group(1)))]
chk(not dead_paths, "TERMINAL: no referenced path is dead", "; ".join(dead_paths))

for slug in fb["picks"]:
    chk(len(glob.glob(os.path.join(REPO, "features", f"*-{slug}.md"))) == 1,
        f"slug -> exactly one feature file: {slug}")

# 5. this pass's numbers unambiguous and clear of the contested range
for n in ("367", "368", "369"):
    chk(len(glob.glob(os.path.join(REPO, "features", n + "-*.md"))) == 1, f"features/{n} unique")
    chk(len(glob.glob(os.path.join(REPO, "specs", n + "-*.md"))) == 1, f"specs/{n} unique")
for claimed in ("362", "363", "364", "365", "366"):
    hits = glob.glob(os.path.join(REPO, "features", claimed + "-*.md"))
    chk(not any(any(k in h for k in ("tianye1999", "ytzhiyun", "sepehr071")) for h in hits),
        f"contested {claimed} carries no file of this pass")

# 6. report completeness
rep = open(REPORT, encoding="utf-8").read()
for sec in ["## Sources fetched", "## Cross-app signals (other industries)",
            "## Restaurant-adjacent signals", "## Operator UX and HCI signals",
            "## Three cross-section ideas", "## LE31 gate verdict per idea",
            "## Why this could take LE31 further", "## Adjacent evidence",
            "## Blockers"]:
    chk(sec in rep, f"report section: {sec}")
for slug in fb["picks"]:
    chk(slug in rep, f"report names pick: {slug}")
chk("ChainWarden" in rep and "X.509" in rep, "report records demotion + reason")
chk("BLOCKED" in rep or "linear: blocked" in rep, "report states Linear block plainly")

# 7. committed AND reachable from origin/main (not merely in the tip commit —
#    a rebase can leave the tip commit holding a peer's files instead)
head = subprocess.run(["git", "-C", REPO, "show", "--name-only", "--format=", "HEAD"],
                      capture_output=True, text=True)
committed = {l.strip() for l in head.stdout.splitlines() if l.strip()}
for f in ("INDEX.md",) + LIVE:
    r = subprocess.run(["git", "-C", REPO, "cat-file", "-e", f"origin/main:{f}"],
                       capture_output=True)
    chk(r.returncode == 0, f"present on origin/main: {f}")
# and the working tree matches origin/main for exactly these paths
drift = subprocess.run(["git", "-C", REPO, "diff", "--name-only", "origin/main", "--"] +
                       ["INDEX.md", "_rerun_verification.py", "scripts/",
                        "features/367-*", "features/368-*", "features/369-*",
                        "specs/367-*", "specs/368-*", "specs/369-*"],
                       capture_output=True, text=True)
chk(not drift.stdout.strip(), "worktree matches origin/main for this pass's artifacts",
    drift.stdout.strip()[:200])
dirty = subprocess.run(["git", "-C", REPO, "status", "--porcelain"] +
                       ["_rerun_verification.py", "scripts/", "INDEX.md",
                        "features/367-*", "features/368-*", "features/369-*",
                        "specs/367-*", "specs/368-*", "specs/369-*"],
                       capture_output=True, text=True)
chk(not dirty.stdout.strip(), "no uncommitted drift in this pass's artifacts",
    dirty.stdout.strip()[:200])

fails = [r for r in results if not r[0]]
for ok, label, detail in results:
    if not ok:
        print(f"FAIL  {label}" + (f"  [{detail}]" if detail else ""))
print(f"\n{len(results) - len(fails)}/{len(results)} ad-hoc checks passed")
sys.exit(1 if fails else 0)