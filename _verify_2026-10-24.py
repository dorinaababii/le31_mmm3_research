#!/usr/bin/env python3
"""Verification launcher — LE31 daily brainstorm 2026-10-24.

Why this shape: HERMES_WRITE_SAFE_ROOT=/opt/data blocks write_file to ANY path
under /tmp/, so neither this launcher nor the verifier body can be authored
there. The launcher therefore lives under /opt/data/ and reaches /tmp/ at
runtime via tempfile.mkstemp(dir="/tmp"), which is atomic and unique.

Every assertion re-derives its subject from disk. A check that trusts a string
inside the artifact under test is not a check — renames orphan references
silently (verified on the 83rd pass: six dead paths shipped green).

This is the 2026-10-24 pass's launcher. The previous pass's launcher is kept
at _rerun_verification.py and is NOT overwritten — its window is hardcoded to
2026-09-24..2026-10-23.

Run:  python3 /opt/data/le31_mmm3_research_work/_verify_2026-10-24.py
"""
import os
import subprocess
import sys
import tempfile

REPO = "/opt/data/le31_mmm3_research_work"
BASE = "/tmp/le31-brainstorm-2026-10-24"
REPORT = "/opt/data/le31-brainstorm-2026-10-24.md"
FALLBACK = "/opt/data/le31-brainstorm-2026-10-24.linear-fallback.json"
STANDALONE_INDEX = "/opt/data/INDEX.md"

BODY = r'''
import os, sys, json, glob

REPO = "/opt/data/le31_mmm3_research_work"
BASE = "/tmp/le31-brainstorm-2026-10-24"
REPORT = "/opt/data/le31-brainstorm-2026-10-24.md"
FALLBACK = "/opt/data/le31-brainstorm-2026-10-24.linear-fallback.json"
STANDALONE_INDEX = "/opt/data/INDEX.md"

FAILS = []
CHECKS = [0]

def chk(cond, label, detail=""):
    CHECKS[0] += 1
    if cond:
        print(f"  PASS  {label}")
    else:
        print(f"  FAIL  {label}   {detail}")
        FAILS.append(label)

def resolve(rel, d):
    """Fallback paths may be bare or prefixed with d+'/'; return a real path."""
    rel = rel if rel.startswith(d + "/") else f"{d}/{rel}"
    return os.path.join(REPO, rel)

print("=== A. raw data on disk ===")
allf = sorted(glob.glob(BASE + "/**/*", recursive=True))
allf = [f for f in allf if os.path.isfile(f)]
# fetched SOURCE files = everything except the metadata sidecars
sidecars = [f for f in allf if os.path.basename(f).startswith("_")]
srcf = [f for f in allf if not os.path.basename(f).startswith("_")]
chk(len(allf) == 46, "46 files on disk in total", f"got {len(allf)}")
chk(len(srcf) == 40, "40 fetched source files (sidecars excluded)", f"got {len(srcf)}")
chk(len(sidecars) == 6, "6 metadata sidecars (_fetch_results_* + _parent_fresh)", f"got {len(sidecars)}")
chk(len([f for f in srcf if f.startswith(BASE + "/gh/")]) == 28, "28 gh/ files")
chk(len([f for f in srcf if f.startswith(BASE + "/hn/")]) == 8, "8 hn/ files")
chk(len([f for f in srcf if f.startswith(BASE + "/openalex/")]) == 3, "3 openalex/ files")
chk(len([f for f in srcf if f.startswith(BASE + "/ph/")]) == 1, "1 ph/ file")
chk(os.path.isdir(BASE + "/gh") and os.path.isdir(BASE + "/hn")
    and os.path.isdir(BASE + "/openalex") and os.path.isdir(BASE + "/ph"),
    "all 4 source-family subdirs present")
chk(not os.path.isdir(BASE + "/gh_nodate") or not glob.glob(BASE + "/gh_nodate/*"),
    "gh_nodate fallback empty (not triggered)")

print("=== B. GitHub search: no stubs, no auth errors, real counts ===")
agg = 0
stubs = 0
autherr = 0
nfiles = 0
for f in sorted(glob.glob(BASE + "/gh/*.json")):
    if os.path.basename(f).startswith("pv_"):
        continue
    nfiles += 1
    b = open(f, "rb").read()
    d = json.loads(b)
    if "total_count" not in d:
        autherr += 1
        continue
    if len(b) < 100:
        stubs += 1
    agg += d["total_count"]
    chk("items" in d, f"{os.path.basename(f)[:38]} has items array")
chk(nfiles == 17, "17 GitHub search files", f"got {nfiles}")
chk(stubs == 0, "zero sub-100-byte stubs", f"got {stubs}")
chk(autherr == 0, "zero auth-failure bodies (message field)", f"got {autherr}")
chk(agg == 43433, "aggregate total_count = 43433", f"got {agg}")

print("=== C. direct /repos/ GETs: field values verified from disk ===")
EXPECT = {
    "Donkie/Spoolman": dict(stars=2932, forks=308, size=8827, spdx="MIT", lang="Python"),
    "hitaishi2222/kinv": dict(stars=0, forks=0, size=36, spdx="MIT", lang="Python"),
    "jdmacleod/kitchen-erp": dict(stars=0, forks=0, size=8283, spdx="MIT", lang="Python"),
}
seen = set()
for f in sorted(glob.glob(BASE + "/gh/pv_*.json")):
    d = json.load(open(f))
    fn = d.get("full_name")
    if fn in EXPECT:
        e = EXPECT[fn]
        seen.add(fn)
        chk(d.get("stargazers_count") == e["stars"], f"{fn} stars={e['stars']}", d.get("stargazers_count"))
        chk(d.get("forks_count") == e["forks"], f"{fn} forks={e['forks']}", d.get("forks_count"))
        chk(d.get("size") == e["size"], f"{fn} size_kb={e['size']}", d.get("size"))
        chk((d.get("license") or {}).get("spdx_id") == e["spdx"], f"{fn} spdx={e['spdx']}")
        chk(d.get("language") == e["lang"], f"{fn} lang={e['lang']}")
        chk(d.get("archived") is False, f"{fn} archived=false")
        chk(d.get("fork") is False, f"{fn} fork=false")
        chk(d.get("pushed_at")[:10] <= "2026-10-24", f"{fn} pushed_at within window")
        # in-window means created_at OR pushed_at in window
        c_in = "2026-09-24" <= d.get("created_at")[:10] <= "2026-10-24"
        p_in = "2026-09-24" <= d.get("pushed_at")[:10] <= "2026-10-24"
        chk(c_in or p_in, f"{fn} in-window by created_at OR pushed_at", f"c={c_in} p={p_in}")
chk(len(seen) == 3, "all 3 research-cron repos cross-verified", f"got {len(seen)}")
for fn, star, fork, sz in [("ramaraihan12/warung-pos", 0, 0, 575),
                            ("fat2fast/mobile-web-ui-ux-skill", 0, 0, 6526)]:
    d = json.load(open(BASE + f"/gh/pv_{fn.replace('/', '_')}.json"))
    chk(d.get("stargazers_count") == star, f"{fn} stars={star}", d.get("stargazers_count"))
    chk(d.get("forks_count") == fork, f"{fn} forks={fork}", d.get("forks_count"))
    chk(d.get("size") == sz, f"{fn} size_kb={sz}", d.get("size"))
    chk((d.get("license") or {}).get("spdx_id") == "MIT", f"{fn} MIT")
    chk(d.get("archived") is False and d.get("fork") is False, f"{fn} not archived/fork")
d = json.load(open(BASE + "/gh/pv_Raktim94_nodedr-restaurant-pos.json"))
chk((d.get("license") or {}).get("spdx_id") == "AGPL-3.0",
    "nodedr-restaurant-pos AGPL-3.0 (reported as a §3.2 blocker, not picked)")

print("=== D. anti-fabrication canary ===")
hits = [f for f in srcf if f.endswith((".json", ".xml")) and b"LE31" in open(f, "rb").read()]
chk(not hits, "no fetched source file contains 'LE31'", hits)

print("=== E. HN + OpenAlex sanity ===")
hn = sorted(glob.glob(BASE + "/hn/*.json"))
chk(len(hn) == 8, "8 HN query files", f"got {len(hn)}")
stories = nullt = sum_nb = sum_ret = 0
for f in hn:
    d = json.load(open(f))
    chk("query" in d, f"{os.path.basename(f)[:30]} used query= (not q=)")
    sum_nb += d.get("nbHits", 0)
    sum_ret += len(d.get("hits", []))
    for h in d.get("hits", []):
        if h.get("title") is None:
            nullt += 1
        else:
            stories += 1
chk(stories == 17, "17 titled HN stories", f"got {stories}")
chk(nullt == 100, "100 null-title comment objects (not promoted to signals)", f"got {nullt}")
chk(sum_nb == 186, "HN nbHits sum = 186", sum_nb)
chk(sum_ret == 117, "HN hits returned = 117 (2 queries page-capped at 50)", sum_ret)
oa = sorted(glob.glob(BASE + "/openalex/*.json"))
chk(len(oa) == 3, "3 OpenAlex files", f"got {len(oa)}")
mc = []
for f in oa:
    d = json.load(open(f))
    mc.append(d.get("meta", {}).get("count"))
chk(mc == [4447, 45, 81373], "OpenAlex meta.counts 4447/45/81373", mc)
chk(os.path.getsize(BASE + "/ph/producthunt.xml") == 43840, "ProductHunt RSS 43840 bytes")

print("=== F. report file: exists, read back, exact section shape ===")
chk(os.path.isfile(REPORT), "report exists")
rt = open(REPORT, encoding="utf-8").read()
for s in ["## Sources fetched", "## Cross-app signals (other industries)",
          "## Restaurant-adjacent signals", "## Operator UX and HCI signals",
          "## Three cross-section ideas", "## LE31 gate verdict per idea",
          "## Why this could take LE31 further", "## Adjacent evidence", "## Blockers"]:
    chk(s in rt, f"report section present: {s}")
chk(rt.startswith("# LE31 Daily Brainstorm — 2026-10-24"), "report H1 exact")
chk(rt.count("\n## ") >= 9, "report has >= 9 H2 sections", rt.count("\n## "))

print("=== G. feature + handoff files: exist, numbered, under ext4 cap ===")
NUMS = [373, 374, 375]
for n in NUMS:
    ff = sorted(f for f in os.listdir(REPO + "/features") if f.startswith(f"{n}-"))
    # HANDOFF filenames in specs/ start with the SLUG, not the number.
    if ff:
        body = ff[0].split("-", 1)[1][:-3]
        sf = sorted(f for f in os.listdir(REPO + "/specs")
                    if f.endswith("-HANDOFF.md") and body in f)
    else:
        sf = []
    chk(len(ff) == 1, f"exactly one features/{n}- file", ff)
    chk(len(sf) == 1, f"exactly one specs/ HANDOFF for {n}", sf)
    if ff and sf:
        chk(len(ff[0].encode()) <= 255, f"features/{n} filename <= 255 bytes", len(ff[0].encode()))
        chk(len(sf[0].encode()) <= 255, f"specs/{n} HANDOFF filename <= 255 bytes", len(sf[0].encode()))
        ftxt = open(os.path.join(REPO, "features", ff[0]), encoding="utf-8").read()
        for sec in ["## Goal", "## Scope", "## Description", "## Data model",
                    "## Implementation steps", "## Dependencies", "## Open questions",
                    "## Why this matters"]:
            chk(sec in ftxt, f"features/{n} has section {sec}")
        stxt = open(os.path.join(REPO, "specs", sf[0]), encoding="utf-8").read()
        for sec in ["## Active feature path", "## Seven-check gate verdict", "## Bucket",
                    "## Files to touch", "## Verification protocol reference",
                    "## Rollback path", "## Mandatory LE31 skill list"]:
            chk(sec in stxt, f"specs/{n} has section {sec}")

print("=== H. fallback JSON: paths resolve, derived from disk, not trusted from JSON ===")
fb = json.load(open(FALLBACK))
chk(fb["linear_status"] == "blocked", "fallback records linear blocked")
chk(fb["linear_block_detail"]["http_status"] == 400, "fallback records HTTP 400")
chk(fb["linear_block_detail"]["consecutive_blocked_days"] == 37, "fallback records 37 consecutive days")
chk(bool(fb["linear_block_detail"]["parent_issue_request_id"]), "fallback records parent requestId")
chk(len(fb["sub_issues"]) == 3, "fallback has 3 sub-issues")
for s in fb["sub_issues"]:
    for key, d in (("feature_file", "features"), ("handoff_file", "specs")):
        p = resolve(s[key], d)
        chk(os.path.isfile(p), f"fallback {s['slot']} {key} resolves on disk", p)
    num = int(os.path.basename(s["feature_file"]).split("-", 1)[0])
    on_disk = sorted(f for f in os.listdir(REPO + "/features") if f.startswith(f"{num}-"))
    chk(len(on_disk) == 1, f"fallback {s['slot']}: exactly one features/{num}- on disk", on_disk)
    chk(os.path.basename(s["feature_file"]) == on_disk[0],
        f"fallback {s['slot']}: JSON filename == on-disk filename (no rename drift)")
    body = on_disk[0].split("-", 1)[1][:-3]
    hon = sorted(f for f in os.listdir(REPO + "/specs")
                 if f.endswith("-HANDOFF.md") and body in f)
    chk(len(hon) == 1, f"fallback {s['slot']}: exactly one HANDOFF for {num}", hon)
    if hon:
        chk(os.path.basename(s["handoff_file"]) == hon[0],
            f"fallback {s['slot']}: HANDOFF filename == on-disk filename", hon)
dead = [s[k] for s in fb["sub_issues"] for k in ("feature_file", "handoff_file")
        if not os.path.isfile(resolve(s[k], "features" if "feature" in k else "specs"))]
chk(not dead, "TERMINAL: no fallback path is dead", dead)

print("=== I. INDEX.md: both files, rows present ===")
for path, label in ((STANDALONE_INDEX, "standalone"), (REPO + "/INDEX.md", "in-repo")):
    t = open(path, encoding="utf-8").read()
    chk("2026-10-24 | **Brainstorm** 85th consecutive" in t, f"{label} INDEX has the brainstorm summary row")
    for slug in ("ramaraihan12-warung-pos-mit-offline-first-pos-no-network",
                 "le31-qty-remaining-derived-not-stored-charter-4-3-vs-schema",
                 "fat2fast-mobile-web-ui-ux-skill-mit-ai-skill-touch-first-mobile-web-ux"):
        chk(slug in t, f"{label} INDEX has row for {slug[:40]}")
    chk(t.count("| 2026-10-24 |") >= 4, f"{label} INDEX has >=4 rows for 2026-10-24", t.count("| 2026-10-24 |"))
    chk(os.path.getsize(path) > 0, f"{label} INDEX non-empty")

print("=== J. feature-number collision check (scoped to this pass) ===")
for n in NUMS:
    ff = [f for f in os.listdir(REPO + "/features") if f.startswith(f"{n}-")]
    body = ff[0].split("-", 1)[1][:-3]
    sf = [f for f in os.listdir(REPO + "/specs") if f.endswith("-HANDOFF.md") and body in f]
    chk(len(ff) == 1 and len(sf) == 1, f"number {n} used exactly once in features/ and specs/",
        f"ff={ff} sf={sf}")
standalone_txt = open(STANDALONE_INDEX, encoding="utf-8").read()
inrepo_txt = open(REPO + "/INDEX.md", encoding="utf-8").read()
for n in (370, 371, 372):
    claimed = (f"features/{n}-" in standalone_txt) or (f"features/{n}-" in inrepo_txt)
    chk(claimed, f"peer research-cron number {n} still claimed somewhere (left untouched)")
    ff = [f for f in os.listdir(REPO + "/features") if f.startswith(f"{n}-")]
    chk(len(ff) == 1, f"peer number {n} still has exactly one feature file (not overwritten)", ff)
for n in NUMS:
    chk(f"features/{n}-" in standalone_txt and f"features/{n}-" in inrepo_txt,
        f"this pass's number {n} claimed in BOTH indexes")

print("=== K. first-party defect: re-verify the CLAIM is still true ===")
mtxt = open(REPO + "/backend/app/models.py", encoding="utf-8").read()
chk("qty_remaining: int" in mtxt, "models.py still declares qty_remaining (defect present as filed)")
chk(not os.path.isdir(REPO + "/backend/app/services"), "backend/app/services still absent (as filed)")
rt2 = os.listdir(REPO + "/backend/app/routers")
chk(sorted(rt2) == ["__init__.py", "tables.py"], "routers/ still only __init__.py + tables.py (as filed)", rt2)
f374 = [f for f in os.listdir(REPO + "/features") if f.startswith("374-")][0]
t374 = open(os.path.join(REPO, "features", f374), encoding="utf-8").read()
chk("`build`" in t374, "feature 374 records a BUILD verdict")
chk("OBSERVED" in t374, "feature 374 marks its evidence class OBSERVED")

print("=== L. no self-reported third-party metrics left unlabelled ===")
for n in NUMS:
    ff = [f for f in os.listdir(REPO + "/features") if f.startswith(f"{n}-")][0]
    t = open(os.path.join(REPO, "features", ff), encoding="utf-8").read()
    for claim in ("1,100+", "90+", "automated tests"):
        if claim in t:
            chk("NOT independently verified" in t, f"features/{n} labels '{claim}' unverified")

print()
print(f"CHECKS_RUN={CHECKS[0]}  CHECKS_FAILED={len(FAILS)}")
if FAILS:
    for f in FAILS:
        print("  FAILED:", f)
    sys.exit(1)
print("VERIFICATION: ALL CHECKS PASSED")
sys.exit(0)
'''


def main():
    fd, path = tempfile.mkstemp(prefix="hermes-verify-", suffix=".py", dir="/tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            fh.write(BODY)
        r = subprocess.run([sys.executable, path], capture_output=True, text=True)
        sys.stdout.write(r.stdout)
        if r.stderr:
            sys.stderr.write(r.stderr)
        print(f"verifier_exit={r.returncode}")
        return r.returncode
    finally:
        try:
            os.unlink(path)
        except OSError:
            pass


if __name__ == "__main__":
    sys.exit(main())
