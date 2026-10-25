#!/usr/bin/env python3
"""Ad-hoc verification for the 2026-10-25 LE31 daily-research pass.

NOT SUITE GREEN. This repo has no canonical test/lint/build command (it is a
research-scratch repo of fetch scripts: no pyproject.toml, Makefile, or CI), so
this is focused ad-hoc verification of the changed paths.

Every figure asserted below is re-derived from the raw fetch files on disk
rather than read from the report, so a wrong number in the report FAILS here.

Authored under scripts/ because HERMES_WRITE_SAFE_ROOT=/opt/data blocks
write_file to /tmp/. The daily-research cron deletes its per-pass scratch
helpers after use; this file is the durable survivor.
"""
import collections
import datetime
import glob
import json
import os
import re
import subprocess
import sys

REPO = "/opt/data/le31_mmm3_research_work"
BASE = "/tmp/le31-daily-2026-10-25"
IDX = "/opt/data/INDEX.md"
REPORT = "/opt/data/le31-daily-research-2026-10-25.md"
FALLBACK = "/opt/data/le31-daily-research-2026-10-25.linear-fallback.json"

START, END = 1792281600, 1792886399
SD, ED = "2026-10-18T00:00:00Z", "2026-10-25T00:00:00Z"
PERM = {"mit", "apache-2.0", "bsd-2-clause", "bsd-3-clause", "isc", "unlicense",
        "0bsd", "mit-0", "cc0-1.0", "zlib", "mpl-2.0", "epl-2.0", "osl-3.0", "python-2.0"}

# this pass's three picks: repo, direct-GET filename, feature number, slug
PICKS = [
    ("drsamonline/canteen-lan", "drsamonline__canteen-lan.json", "376",
     "drsamonline-canteen-lan-mit-javascript-lan-offline-first-restaurant-single-file-"
     "order-from-the-table-over-the-room-own-wifi-v1-local-network-ordering-surface-vocabulary"),
    ("Anatolii198/mesa-lite", "Anatolii198__mesa-lite.json", "377",
     "Anatolii198-mesa-lite-mit-javascript-vanilla-js-no-dependencies-no-build-step-"
     "restaurant-analytics-dashboard-eight-svg-charts-v1-zero-dependency-analytics-surface-vocabulary"),
    ("Leonardo-Dalan/material-request-system", "Leonardo-Dalan__material-request-system.json", "378",
     "Leonardo-Dalan-material-request-system-mit-javascript-firebase-vanilla-js-offline-first-"
     "factory-material-request-logistics-queue-stock-tracking-v1-operator-request-queue-vocabulary"),
]

results = []


def chk(ok, label, detail=""):
    results.append((bool(ok), label, detail))


def inwin(ts):
    return bool(ts) and SD <= ts < ED


def git(*a):
    return subprocess.run(["git", "-C", REPO, *a], capture_output=True, text=True).stdout.strip()


# 0. the pass's scratch helpers are gone; the durable verifier is committed
for f in ("_append_index_2026-10-25.py", "_parent_verify_2026-10-25.py",
          "_parent_verify_2026-10-25.txt"):
    chk(not os.path.exists(os.path.join(REPO, f)), f"scratch removed: {f}")
chk(git("ls-files", "--error-unmatch", "scripts/ad-hoc-verify-daily-2026-10-25.py")
    or os.path.exists(os.path.join(REPO, "scripts/ad-hoc-verify-daily-2026-10-25.py")),
    "durable verifier present")

# 1. raw fetch integrity
files = [f for f in glob.glob(f"{BASE}/**/*", recursive=True) if os.path.isfile(f)]
chk(len(files) == 260, "raw fetches: 260 files", f"got {len(files)}")
canary = subprocess.run(["grep", "-rcF", "LE31", BASE], capture_output=True, text=True).stdout
chk(not [l for l in canary.splitlines() if l.strip() and not l.endswith(":0")],
    "anti-fabrication canary: no raw source mentions LE31")

rep = open(REPORT, encoding="utf-8").read()

# 2. epochs
for e in (START, END):
    chk(datetime.datetime.fromtimestamp(e, datetime.timezone.utc).strftime("%Y-%m-%d")
        in ("2026-10-18", "2026-10-24"), f"epoch {e} decodes to window date")

# 3. HN: nbHits total and the null-title hazard
hn = {}
for f in glob.glob(f"{BASE}/hn/*.json"):
    if os.path.basename(f).startswith("_"):
        continue
    d = json.load(open(f))
    hn[os.path.basename(f)[:-5]] = (d.get("nbHits", 0),
        sum(1 for h in d.get("hits", []) if not h.get("title")))
chk(sum(v[0] for v in hn.values()) == 48, "HN nbHits total = 48")
chk(sum(v[1] for v in hn.values()) == 0, "HN null_title = 0 on every query")
for q, (nb, _) in hn.items():
    chk(str(nb) in rep, f"HN {q} nbHits={nb} in report")

# 4. arXiv: a genuine zero, not a filter bug
entries = 0
inwin_entries = 0
for f in glob.glob(f"{BASE}/arxiv/*.xml"):
    ents = re.findall(r"<entry>.*?</entry>", open(f, encoding="utf-8", errors="replace").read(), re.S)
    entries += len(ents)
    for e in ents:
        pm = re.search(r"<published>(\d{4}-\d{2}-\d{2})", e)
        if pm and datetime.date(2026, 10, 18) <= datetime.date.fromisoformat(pm.group(1)) \
                <= datetime.date(2026, 10, 24):
            inwin_entries += 1
chk(entries == 104, "arXiv raw entries = 104", f"got {entries}")
chk(inwin_entries == 0, "arXiv in-window entries = 0")
chk("104 raw `<entry>`" in rep and "**0 in-window**" in rep, "report states the arXiv null")

# 5. OpenAlex
oa = [json.load(open(f))["meta"]["count"] for f in sorted(glob.glob(f"{BASE}/openalex/oa*.json"))]
chk(oa == [226, 317, 77], "OpenAlex meta.count = 226/317/77", str(oa))
chk("226 / 317 / 77" in rep, "report states OpenAlex counts")

# 6. GitHub union + licence histogram
union = {}
for f in glob.glob(f"{BASE}/gh/dated_*.json") + glob.glob(f"{BASE}/gh/undated_*.json"):
    try:
        d = json.load(open(f))
    except Exception:
        continue
    if isinstance(d, dict) and "items" in d:
        for it in d["items"]:
            if it.get("full_name"):
                union.setdefault(it["full_name"], it)
lic = collections.Counter(
    ((it.get("license") or {}).get("spdx_id") or "(none)").lower() for it in union.values())
chk(len(union) == 998, "GH union = 998 unique repos", f"got {len(union)}")
chk(sum(1 for it in union.values() if inwin(it.get("pushed_at"))) == 528, "GH in-window pushed = 528")
chk(sum(1 for it in union.values() if inwin(it.get("created_at"))) == 295, "GH in-window created = 295")
chk(sum(1 for it in union.values() if inwin(it.get("pushed_at")) and inwin(it.get("created_at"))) == 270,
    "GH in-window both = 270")
chk(sum(v for k, v in lic.items() if k in PERM) == 369, "GH permissive = 369")
chk(all(f"`{k}` {v}" in rep for k, v in lic.most_common() if v >= 4),
    "report licence histogram matches raw")
chk(len(glob.glob(f"{BASE}/gh/dated_*.json") + glob.glob(f"{BASE}/gh/undated_*.json")) == 48,
    "GH query files = 48")

# 7. PyPI
pypi = {}
for f in glob.glob(f"{BASE}/pypi/*.json"):
    b = os.path.basename(f)
    if b.startswith("_") or "inwindow" in b:
        continue
    try:
        d = json.load(open(f))
    except Exception:
        continue
    if isinstance(d, dict) and "info" in d:
        n = sum(1 for rel, fl in (d.get("releases") or {}).items() for x in fl
                if (x.get("upload_time_iso_8601") or x.get("upload_time")) and
                SD <= (x.get("upload_time_iso_8601") or x.get("upload_time")) < ED)
        pypi[d["info"]["name"].lower()] = n
chk(pypi.get("fastapi") == 66, "PyPI fastapi = 66 in-window uploads")
chk(pypi.get("sqlalchemy") == 72, "PyPI sqlalchemy = 72")
chk(pypi.get("alembic") == 2, "PyPI alembic = 2")
chk(all(pypi.get(k) == 0 for k in ("sqlmodel", "aiogram", "pydantic", "uvicorn")),
    "PyPI sqlmodel/aiogram/pydantic/uvicorn = 0")

# 8. releases.atom
atom = {}
for f in glob.glob(f"{BASE}/releases/*.atom"):
    n = 0
    for e in re.findall(r"<entry>.*?</entry>", open(f, encoding="utf-8", errors="replace").read(), re.S):
        tm = re.search(r"<updated>([^<]+)</updated>", e)
        if tm:
            try:
                d = datetime.datetime.fromisoformat(tm.group(1).replace("Z", "+00:00"))
                n += START <= int(d.timestamp()) <= END
            except ValueError:
                pass
    atom[os.path.basename(f)[:-5]] = n
chk(atom.get("fastapi__fastapi") == 10, "atom fastapi = 10 in-window")
chk(atom.get("sqlalchemy__sqlalchemy") == 1, "atom sqlalchemy = 1")
chk(atom.get("fastapi__sqlmodel") == 0, "atom sqlmodel = 0 (valid empty feed)")

# 9. regulators
fx = json.load(open(f"{BASE}/regulators/_parsed_ecb_fx.json"))
chk(len([c for c in fx if c.get("in_window")]) == 5, "ECB in-window USD cubes = 5")
chk("1.1193" in rep and "5 in-window cubes" in rep, "report states ECB cubes")
cnil = open(f"{BASE}/regulators/cnil_en.xml", encoding="utf-8", errors="replace").read()
items = re.findall(r"<item>.*?</item>", cnil, re.S)
dates = [m.group(1) for m in (re.search(r"<pubDate>([^<]+)</pubDate>", i) for i in items) if m]
chk(len(items) == 10, "CNIL has 10 <item> blocks", f"got {len(items)}")
chk(len([d for d in dates if "Oct 2026" in d and
         any(f"{n:02d} Oct 2026" in d for n in (19, 20, 21, 22, 23, 24))]) == 3,
    "CNIL 3 in-window items")
e144 = open(f"{BASE}/regulators/eurlex_144.html", encoding="utf-8", errors="replace").read()
e143 = open(f"{BASE}/regulators/eurlex_143.html", encoding="utf-8", errors="replace").read()
chk(len(e144) == 249 and "no longer valid" in e144, "EUR-Lex 144 = 249-byte dead body")
chk(len(e143) > 40000, "EUR-Lex 143 = valid large body", f"got {len(e143)}")
chk(not glob.glob(f"{BASE}/**/*sciencedirect*", recursive=True), "ScienceDirect never fetched")
chk("NOT RETRIEVABLE" in rep, "report states ScienceDirect NOT RETRIEVABLE")

# 10. report shape: exactly the nine sections from le31-daily-research/SKILL.md
heads = re.findall(r"^## .+$", rep, re.M)
for h in ("## Sources fetched", "## Restaurant-tech findings (last 7 days)",
          "## Stack-relevant findings (last 7 days)", "## Competitor and operator UX signals",
          "## Three feature picks", "## LE31 gate verdict per pick", "## Recommendations",
          "## Adjacent evidence", "## Blockers"):
    chk(h in heads, f"report section: {h}")
chk(len(heads) == 9, "report has exactly 9 '##' sections", str(len(heads)))
chk(rep.startswith("# LE31 Daily Research — 2026-10-25"), "report H1 exact")
chk("**Headline**:" in rep, "report has headline")

# 11. picks: raw-file backing, template shape, dedup
own = set()
for _, _, num, slug in PICKS:
    own |= {f"{num}-{slug}.md", f"{slug}-HANDOFF.md"}
for repo, pvfile, num, slug in PICKS:
    p = f"{BASE}/pv/{pvfile}"
    chk(os.path.exists(p), f"{repo}: direct-GET file exists")
    if not os.path.exists(p):
        continue
    d = json.load(open(p))
    tok = f"★{d['stargazers_count']}/⑂{d['forks_count']}"
    chk(((d.get("license") or {}).get("spdx_id") or "").upper() == "MIT", f"{repo}: MIT")
    chk(inwin(d.get("pushed_at")) and inwin(d.get("created_at")),
        f"{repo}: in-window by both dates")
    chk(tok in rep, f"{repo}: star count in report matches raw API", tok)
    chk((d.get("description") or "")[:60] in rep, f"{repo}: description quoted verbatim")
    chk(str(d.get("size")) in rep, f"{repo}: size_kb in report")
    fpath = f"{REPO}/features/{num}-{slug}.md"
    hpath = f"{REPO}/specs/{slug}-HANDOFF.md"
    chk(os.path.exists(fpath), f"features/{num} exists")
    chk(os.path.exists(hpath), f"specs handoff {num} exists")
    if os.path.exists(fpath):
        ft = open(fpath, encoding="utf-8").read()
        for sec in ("## Goal", "## Scope", "## Out of scope", "## Description", "## Data model",
                    "## Implementation steps", "## Telegram interaction if any", "## Dependencies",
                    "## Open questions", "## Why this matters"):
            chk(sec in ft, f"features/{num} section {sec}")
        chk(tok in ft, f"features/{num} star count matches raw API", tok)
        chk(ft.index("## Goal") < ft.index("## Scope") < ft.index("## Out of scope")
            < ft.index("## Description"), f"features/{num} template order")
    if os.path.exists(hpath):
        ht = open(hpath, encoding="utf-8").read()
        for sec in ("## Frozen identifiers", "## LE31 feature-gate verdict",
                    "## Mandatory LE31 skill list", "## Files to touch",
                    "## Verification protocol", "## Rollback path"):
            chk(sec in ht, f"handoff {num} section {sec}")
        chk("pv/" in ht, f"handoff {num} cites raw fetch path")
        chk("le31-verification-protocol" in ht, f"handoff {num} cites verification protocol")
    # dedup against PRE-EXISTING files only: this pass's siblings legitimately cite each other
    others = [q for q in glob.glob(f"{REPO}/features/*.md") + glob.glob(f"{REPO}/specs/*.md")
              if os.path.basename(q) not in own]
    hits = [o for o in others
            if repo.split("/")[-1] in open(o, encoding="utf-8", errors="replace").read()]
    chk(not hits, f"{repo}: unique vs all pre-existing feature/spec files",
        f"{len(hits)}: {[os.path.basename(h) for h in hits[:3]]}")

# 12. INDEX rows
idx = open(IDX, encoding="utf-8").read()
rows = [l for l in idx.splitlines() if l.startswith("| 2026-10-25")]
chk(len(rows) == 7, "INDEX: 7 rows dated 2026-10-25 (1 summary + 3 picks + 3 pipeline)", f"got {len(rows)}")
chk(REPORT in idx, "INDEX cites the report path")
chk(all(s[3] in idx for s in PICKS), "INDEX names all three pick slugs")
chk(idx.count("[linear: blocked]") >= 4, "INDEX marks Linear blocked")
chk("38th consecutive day" in idx, "INDEX states the 38th consecutive blocked day")

# 13. Linear fallback: honest failure claim, no false success
fb = json.load(open(FALLBACK))
chk(fb["date"] == "2026-10-25", "fallback: date")
chk(fb["linear_status"] == "blocked", "fallback: linear_status blocked")
chk(fb["linear_error"]["status"] == 400, "fallback: records HTTP 400")
chk(fb["linear_error"]["parent_requestId"] == "a4ff44223faad34e", "fallback: parent requestId")
chk(fb["linear_error"]["sub_issue_probe"]["requestId"] == "a4ff4b20fc068c52",
    "fallback: sub-issue probe requestId")
chk(len(fb["workspace_projects_confirmed"]) == 3, "fallback: 3 projects that exist")
chk(set(fb["projects_that_do_not_exist"]) == {"le31 v2 owner-pains", "le31 v2-AI"},
    "fallback: 2 projects that do NOT exist")
chk(len(fb["intended_sub_issues"]) == 3, "fallback: 3 intended sub-issues")
chk(all("le31 Research" in s["project"] for s in fb["intended_sub_issues"]),
    "fallback: sub-issues routed to le31 Research")
chk([p[3] for p in PICKS] == fb["picks"], "fallback: picks match the report")

# 14. git: committed, pushed, and the working tree matches origin/main
chk(git("log", "-1", "--pretty=%s") == "Daily research 2026-10-25", "HEAD message")
chk(git("branch", "--show-current") == "main", "HEAD is on main")
chk(git("rev-parse", "origin/main") == git("rev-parse", "HEAD"), "origin/main == HEAD")
msgs = [m for m in git("log", "--pretty=%s", "-3").split("\n") if m]
chk(all(m == "Daily research 2026-10-25" for m in msgs),
    "all commits from this pass use the required message", str(msgs))
committed = set(git("log", "--name-only", "--pretty=format:", "-3").split("\n"))
for _, _, num, slug in PICKS:
    chk(f"features/{num}-{slug}.md" in committed, f"features/{num} committed")
    chk(f"specs/{slug}-HANDOFF.md" in committed, f"handoff {num} committed")
dirty = [l for l in git("status", "--porcelain").splitlines()
         if any(k in l for k in ("376", "377", "378", "canteen-lan", "mesa-lite", "material-request"))]
chk(not dirty, "no uncommitted drift in this pass's artefacts", str(dirty[:3]))

fails = [r for r in results if not r[0]]
for ok, label, detail in results:
    if not ok:
        print(f"FAIL  {label}" + (f"  [{detail}]" if detail else ""))
print(f"\n{len(results) - len(fails)}/{len(results)} ad-hoc checks passed")
sys.exit(1 if fails else 0)
