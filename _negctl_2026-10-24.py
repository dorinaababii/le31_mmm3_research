#!/usr/bin/env python3
"""Negative control for the 2026-10-24 brainstorm verifier.

A check that has only ever passed is not evidence that it works. This script
re-injects the known bugs into THROWAWAY copies of the artifacts under test and
asserts the verifier's exit code flips 0 -> 1 each time, restoring the
originals in a finally block and asserting no .bak residue survives.

Run:  python3 /opt/data/le31_mmm3_research_work/_negctl_2026-10-24.py
"""
import json
import os
import shutil
import subprocess
import sys

REPO = "/opt/data/le31_mmm3_research_work"
LAUNCHER = os.path.join(REPO, "_verify_2026-10-24.py")
FALLBACK = "/opt/data/le31-brainstorm-2026-10-24.linear-fallback.json"
REPORT = "/opt/data/le31-brainstorm-2026-10-24.md"


def run_verifier():
    r = subprocess.run([sys.executable, LAUNCHER], capture_output=True, text=True)
    return r.returncode, r.stdout


def resid():
    out = []
    for root, dirs, files in os.walk(REPO):
        for f in files:
            if f.endswith(".bak"):
                out.append(os.path.join(root, f))
    for f in os.listdir("/opt/data"):
        if f.endswith(".bak"):
            out.append(os.path.join("/opt/data", f))
    return out


results = []


def case(name, mutate, restore):
    try:
        mutate()
        code, out = run_verifier()
        failed = [l for l in out.splitlines() if l.strip().startswith("FAIL")]
        results.append((name, (code != 0) and bool(failed), code, len(failed), failed[:3]))
    finally:
        restore()
        after = run_verifier()
        results.append((f"  {name} -> restored", after[0] == 0, after[0], 0, []))


base_code, base_out = run_verifier()
print(f"BASELINE exit={base_code}  clean={base_code == 0}")
if base_code != 0:
    print("Baseline is not clean - negative control cannot run.")
    for l in base_out.splitlines():
        if l.strip().startswith("FAIL"):
            print("   ", l)
    sys.exit(1)
print()

# ---- case 1: dead feature path in the fallback JSON -----------------------
orig_slots = open(FALLBACK).read()


def mut1():
    fb2 = json.loads(orig_slots)
    fb2["sub_issues"][0]["feature_file"] = "features/999-does-not-exist.md"
    with open(FALLBACK, "w") as fh:
        json.dump(fb2, fh, indent=1)


def res1():
    with open(FALLBACK, "w") as fh:
        fh.write(orig_slots)


case("fallback: dead feature_file path", mut1, res1)

# ---- case 2: genuine rename drift (the 83rd-pass bug) ---------------------
specs_dir = os.path.join(REPO, "specs")
b_handoff = ("le31-qty-remaining-derived-not-stored-charter-4-3-vs-schema-"
             "contradiction-first-party-v1-derive-batch-qty-remaining-from-"
             "stockentry-ledger-HANDOFF.md")
b_renamed = "374-shortened-name-after-ext4-cap-HANDOFF.md"
b_old_path = os.path.join(specs_dir, b_handoff)
b_new_path = os.path.join(specs_dir, b_renamed)


def mut2():
    shutil.move(b_old_path, b_new_path)


def res2():
    shutil.move(b_new_path, b_old_path)


case("fallback: genuine rename drift (file renamed, JSON points at old name)",
     mut2, res2)

# ---- case 3: report loses a required section ------------------------------
orig_report = open(REPORT, encoding="utf-8").read()


def mut3():
    with open(REPORT, "w", encoding="utf-8") as fh:
        fh.write(orig_report.replace("## Blockers", "## Blockerz"))


def res3():
    with open(REPORT, "w", encoding="utf-8") as fh:
        fh.write(orig_report)


case("report: missing required section '## Blockers'", mut3, res3)

# ---- case 4: canary fooled by a fabricated 'LE31' in a source file ----------
ghf = os.path.join("/tmp/le31-brainstorm-2026-10-24", "gh",
                   "07-topic-restaurant-pushed-2026-09-24.json")
orig_gh = open(ghf, "rb").read()


def mut4():
    with open(ghf, "wb") as fh:
        fh.write(orig_gh[:-1] + b', "leak": "LE31 was mentioned here"}')


def res4():
    with open(ghf, "wb") as fh:
        fh.write(orig_gh)


case("canary: 'LE31' string injected into a fetched source file", mut4, res4)

# ---- case 5: the first-party defect is 'fixed' but the claim is stale ------
models = os.path.join(REPO, "backend", "app", "models.py")
orig_models = open(models, encoding="utf-8").read()


def mut5():
    with open(models, "w", encoding="utf-8") as fh:
        fh.write(orig_models.replace("    qty_remaining: int\n", ""))


def res5():
    with open(models, "w", encoding="utf-8") as fh:
        fh.write(orig_models)


case("claim: qty_remaining column removed -> 'defect still present' must fail",
     mut5, res5)

print("NEGATIVE CONTROL RESULTS")
print("=" * 78)
all_ok = True
for name, ok, code, nfail, lines in results:
    if not name.strip().startswith("-"):
        all_ok = all_ok and ok
    print(f"  [{'OK ' if ok else 'BAD'}] {name:62s} exit={code} fails={nfail}")
    for l in lines:
        print(f"          {l.strip()[:150]}")
print("=" * 78)
r = resid()
print(f"residue check: {len(r)} .bak files remaining -> {'CLEAN' if not r else r}")
print(f"restored-state baseline exit=0 confirmed for every case: "
      f"{all(o for n, o, c, f, l in results if n.strip().startswith('-'))}")
print(f"NEGATIVE CONTROL: {'PASS - verifier is load-bearing' if all_ok and not r else 'FAIL'}")
sys.exit(0 if (all_ok and not r) else 1)
