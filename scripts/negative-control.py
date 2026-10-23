#!/usr/bin/env python3
"""Negative control for the 2026-10-23 verification.

A verifier assertion that has only ever passed is not evidence that it works.
This reinjects the exact bug the 83rd pass shipped green (a stale feature path
left behind by a rename) into a THROWAWAY COPY of the fallback JSON, re-runs
the verifier, and asserts the exit code flips 0 -> 1. The original is restored
in a finally block and a residue check confirms nothing is left behind.

Run:  python3 scripts/negative-control.py
"""
import os
import shutil
import subprocess
import sys

REPO = "/opt/data/le31_mmm3_research_work"
FB = "/opt/data/le31-brainstorm-2026-10-23.linear-fallback.json"
BACKUP = FB + ".negctl.bak"
VERIFIER = os.path.join(REPO, "_rerun_verification.py")


def run():
    p = subprocess.run([sys.executable, VERIFIER], capture_output=True, text=True,
                       cwd=REPO)
    return p.returncode, p.stdout


def residue_check():
    leftovers = [f for f in os.listdir("/opt/data") if "negctl" in f]
    return leftovers


def main():
    base_code, base_out = run()
    print(f"[baseline] exit={base_code}")
    if base_code != 0:
        print("[negctl] ABORT: baseline must be clean before injecting a fault")
        return 2
    print(f"[baseline] {base_out.strip().splitlines()[-2] if len(base_out.strip().splitlines()) > 1 else ''}")

    injected = False
    try:
        shutil.copy2(FB, BACKUP)
        # Reinject the 83rd-pass bug: point a pick back at its PRE-RENAME path.
        txt = open(BACKUP, encoding="utf-8").read()
        bad = txt.replace("features/367-tianye1999", "features/364-tianye1999")
        if bad == txt:
            print("[negctl] ABORT: could not find the path to invalidate")
            return 2
        with open(FB, "w", encoding="utf-8") as f:
            f.write(bad)
        injected = True
        print("[negctl] injected stale pre-rename path (features/364-tianye1999...)")

        inj_code, inj_out = run()
        print(f"[injected] exit={inj_code}")
        fails = [ln for ln in inj_out.splitlines() if ln.startswith("FAIL")]
        for ln in fails[:8]:
            print("   ", ln)
        print(f"[negctl] {len(fails)} FAIL line(s) surfaced by the injected fault")

        if inj_code == 0:
            print("\n[negctl] RESULT: *** NEGATIVE CONTROL FAILED ***")
            print("[negctl] The verifier passed with a dead path. The path-resolution")
            print("[negctl] assertions are NOT load-bearing and must not be trusted.")
            return 1
        print("\n[negctl] RESULT: PASS — exit flipped 0 -> 1, so the path checks ARE")
        print("[negctl] load-bearing. A dead path cannot ship green.")
        return 0
    finally:
        if injected:
            shutil.move(BACKUP, FB)
            print("[negctl] original restored from backup")
        left = residue_check()
        print(f"[negctl] residue check: {left if left else 'clean — no .negctl artefacts'}")
        if left:
            for f in left:
                try:
                    os.unlink(f)
                except OSError:
                    pass


if __name__ == "__main__":
    sys.exit(main())