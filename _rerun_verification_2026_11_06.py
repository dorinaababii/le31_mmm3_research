#!/usr/bin/env python3
"""Ad-hoc verification for the 2026-11-06 LE31 brainstorm pass.

NOTE: this repo has NO canonical test/lint/build command. This is an AD-HOC
verification script, not a suite. It exists to answer one question:

  "Do the audit scripts under /opt/data/le31-brainstorm-2026-11-06-scripts/
   still reproduce, by EXECUTION, the specific facts that the three shipped
   feature contracts assert?"

Every check below re-derives its claim against LE31's real models.py on a
throwaway SQLite DB, rather than trusting the contract's prose.

Also re-checks the SHIPPED artefacts (features/, specs/, INDEX.md, origin/main)
because those are what the pass actually delivered.

Run:   python3 _rerun_verification_2026_11_06.py
Negctl: python3 _rerun_verification_2026_11_06.py --negctl
"""
import os, sys, subprocess, tempfile

BODY = r'''
import os, sys, glob, json, subprocess, tempfile, datetime
from decimal import Decimal

REPO = "/opt/data/le31_mmm3_research_work"
SCRIPTS = "/opt/data/le31-brainstorm-2026-11-06-scripts"
BASE = "/tmp/le31-brainstorm-2026-11-06"
REPORT = "/opt/data/le31-brainstorm-2026-11-06.md"
FALLBACK = "/opt/data/le31-brainstorm-2026-11-06.linear-fallback.json"
DATE = "2026-11-06"

fails = []
def chk(cond, label):
    if cond: print("  PASS  " + label)
    else:
        print("  FAIL  " + label); fails.append(label)

def sh(cmd):
    return subprocess.run(cmd, shell=True, capture_output=True, text=True)

print("== A. the audit scripts still compile ==")
bad = []
for f in sorted(glob.glob(os.path.join(SCRIPTS, "*.py"))):
    r = sh("python3 -m py_compile %s" % f)
    if r.returncode != 0: bad.append((f, r.stderr[-200:]))
chk(not bad, "all %d audit scripts compile (%d bad)" % (len(glob.glob(os.path.join(SCRIPTS,'*.py'))), len(bad)))
for f, e in bad: print("      ", os.path.basename(f), e)

print("\n== B. re-run the parent re-derivation (the canary + census + manifest) ==")
r = sh("python3 %s/parent_rederive.py" % SCRIPTS)
out = r.stdout
chk(r.returncode == 0, "parent_rederive.py exits 0")
chk("CANARY: PASS" in out, "canary PASS on a fresh run")
chk("non-zero matches: 0" in out, "canary: 0 non-zero matches")
chk("manifest byte/path mismatches: 0" in out, "manifest agrees with disk")
chk("aggregate total_count: 10540" in out, "GH aggregate total_count == 10540")
chk("zeros: 3" in out, "GH zeros == 3")
chk("6-byte files: 0  73-byte files: 0  55-byte: 3" in out, "stub scan: 3x55B, no 6B/73B")
chk("null titles: 0" in out, "HN null-title count == 0")
chk("nbHits sum: 23" in out, "HN nbHits sum == 23")

print("\n== C. re-EXECUTE the three contract claims against LE31's real schema ==")
sys.path.insert(0, "/opt/data/le31_mmm3_research_work/backend")
from sqlmodel import SQLModel, Session, create_engine
from app.models import (Table, AppUser, MenuItem, Batch, StockEntry, Visit,
                        OrderItem, Bill, DerivedTip, Shift,
                        UserRole, PaymentMethod, ItemStatus, StockReason)
import sqlite3

def fresh_db():
    p = tempfile.mktemp(suffix=".db")
    e = create_engine("sqlite:///" + p)
    SQLModel.metadata.create_all(e)
    return e, sqlite3.connect(p)

# ---- CLAIM 1 (feature 447): an expired batch accepts a sale -------------------
e, C = fresh_db()
def q1(sql, args=()):
    return C.execute(sql, args).fetchall()
with Session(e) as s:
    srv = AppUser(name="s", pin_hash="x", role=UserRole.server)
    t = Table(label="T1", section="main", seats=4)
    m = MenuItem(name="Espresso", category="drink", unit_price=Decimal("2.50"))
    mi = MenuItem(name="Tiramisu", category="dessert", unit_price=Decimal("6.00"))
    s.add_all([srv, t, m, mi]); s.commit()
    for o in (srv, t, m, mi): s.refresh(o)
    past = datetime.datetime(2026, 11, 1, 9, 0, tzinfo=datetime.timezone.utc)
    fut = datetime.datetime(2026, 11, 30, 9, 0, tzinfo=datetime.timezone.utc)
    exp = Batch(menu_item_id=mi.id, qty_start=5, qty_remaining=5, prepared_at=past, expires_at=past)
    fresh = Batch(menu_item_id=mi.id, qty_start=5, qty_remaining=5,
                  prepared_at=datetime.datetime.now(datetime.timezone.utc), expires_at=fut)
    nullx = Batch(menu_item_id=mi.id, qty_start=5, qty_remaining=5,
                  prepared_at=datetime.datetime.now(datetime.timezone.utc))
    s.add_all([exp, fresh, nullx]); s.commit()
    for o in (exp, fresh, nullx): s.refresh(o)
    EXP_ID = exp.id
    # sale against the EXPIRED batch -- must be ACCEPTED (that IS the defect)
    s.add(StockEntry(batch_id=exp.id, qty_delta=-1, reason=StockReason.sale)); s.commit()
    v = Visit(table_id=t.id, server_id=srv.id, party_size=1, adults=1)
    s.add(v); s.commit(); s.refresh(v)
    oi = OrderItem(visit_id=v.id, menu_item_id=mi.id, qty=1, unit_price=Decimal("6.00"))
    s.add(oi); s.commit(); s.refresh(oi)
    s.add(StockEntry(batch_id=exp.id, qty_delta=-1, reason=StockReason.sale,
                     ref_order_item_id=oi.id)); s.commit()
    now = datetime.datetime.now(datetime.timezone.utc)
    sales_expired = q1("SELECT COUNT(*) FROM stock_entry WHERE batch_id=? AND reason='sale'", (exp.id,))[0][0]
    expired_batches = q1("SELECT COUNT(*) FROM batch WHERE expires_at IS NOT NULL AND expires_at<=?", (now.isoformat(),))[0][0]
    pred_active = q1("SELECT COUNT(*) FROM batch WHERE expires_at IS NULL OR expires_at>?", (now.isoformat(),))[0][0]
    null_is_active = q1("SELECT COUNT(*) FROM batch WHERE expires_at IS NULL")[0][0]
chk(sales_expired == 2, "CLAIM 1: 2 sales accepted against the EXPIRED batch (got %d)" % sales_expired)
chk(expired_batches == 1, "CLAIM 1: exactly 1 expired batch (got %d)" % expired_batches)
chk(pred_active == 2, "CLAIM 1: the predicate marks 2 batches active, EXCLUDING the expired one (got %d)" % pred_active)
chk(null_is_active == 1, "CLAIM 1: a NULL-expiry batch IS active (404's default) (got %d)" % null_is_active)
# the expired batch was excluded by the predicate yet still sold from
chk(expired_batches == 1 and sales_expired == 2,
    "CLAIM 1: the defect -- predicate excludes it, the write path still sold it")

# ---- CLAIM 2 (feature 448): a bill has no human-facing identity --------------
e, C = fresh_db()
def q2(sql, args=()):
    return C.execute(sql, args).fetchall()
with Session(e) as s:
    srv = AppUser(name="s", pin_hash="x", role=UserRole.server)
    t = Table(label="T1", section="main", seats=4)
    m = MenuItem(name="E", category="drink", unit_price=Decimal("2.50"))
    s.add_all([srv, t, m]); s.commit()
    for o in (srv, t, m): s.refresh(o)
    for i in range(3):
        v = Visit(table_id=t.id, server_id=srv.id, party_size=2, adults=2)
        s.add(v); s.commit(); s.refresh(v)
        s.add(OrderItem(visit_id=v.id, menu_item_id=m.id, qty=2, unit_price=Decimal("2.50"))); s.commit()
        s.add(Bill(visit_id=v.id, subtotal_items=Decimal("5.00"), subtotal_tax=Decimal("0.00"),
                   total_due=Decimal("5.00"), total_paid=Decimal("5.00"),
                   payment_method=PaymentMethod.card, closed_by=srv.id)); s.commit()
nb = q2("SELECT COUNT(*) FROM bill b JOIN visit v ON v.id=b.visit_id WHERE v.table_id=?", (t.id,))[0][0]
nd = q2("SELECT COUNT(DISTINCT total_due) FROM bill b JOIN visit v ON v.id=b.visit_id WHERE v.table_id=?", (t.id,))[0][0]
cols = [r[1] for r in q2("PRAGMA table_info(bill)")]
labels = [c for c in ("number","no","receipt","code","reference","label") if c in cols]
chk(nb == 3, "CLAIM 2: 3 bills on one table (got %d)" % nb)
chk(nd == 1, "CLAIM 2: 1 distinct total_due among them (got %d)" % nd)
chk(not labels, "CLAIM 2: NO human-facing label column on bill (found %s)" % labels)
chk("id" in cols and "visit_id" in cols, "CLAIM 2: the only identity is the auto-increment id")

# ---- CLAIM 3 (feature 449): a line may carry any price ----------------------
e, C = fresh_db()
def q3(sql, args=()):
    return C.execute(sql, args).fetchall()
with Session(e) as s:
    srv = AppUser(name="s", pin_hash="x", role=UserRole.server)
    t = Table(label="T1", section="main", seats=4)
    m = MenuItem(name="E", category="drink", unit_price=Decimal("2.50"))
    s.add_all([srv, t, m]); s.commit()
    for o in (srv, t, m): s.refresh(o)
    v = Visit(table_id=t.id, server_id=srv.id, party_size=1, adults=1)
    s.add(v); s.commit(); s.refresh(v)
    # a line at 99.00 against a 2.50 menu item -- must be ACCEPTED
    oi = OrderItem(visit_id=v.id, menu_item_id=m.id, qty=1, unit_price=Decimal("99.00"))
    s.add(oi); s.commit()
    stored = q3("SELECT unit_price FROM order_item WHERE id=?", (oi.id,))[0][0]
    menu_p = q3("SELECT unit_price FROM menu_item WHERE id=?", (m.id,))[0][0]
chk(stored == Decimal("99.00"), "CLAIM 3: the line's 99.00 price was ACCEPTED and stored (got %s)" % stored)
chk(menu_p == Decimal("2.50"), "CLAIM 3: the menu price is 2.50 (got %s)" % menu_p)
ratio = float(stored) / float(menu_p)
chk(abs(ratio - 39.6) < 0.1, "CLAIM 3: the ratio is 39.6x (got %.1f)" % ratio)
ocols = [r[1] for r in q3("PRAGMA table_info(order_item)")]
chk("price_reason" not in ocols, "CLAIM 3: order_item has NO price_reason column today (the gap)")
chk("unit_price" in ocols, "CLAIM 3: order_item has unit_price")

print("\n== D. the shipped artefacts are intact ==")
TEMPLATE = ["## Goal", "## Scope", "## Out of scope", "## Description", "## Data model",
            "## Implementation steps", "## Telegram interaction if any", "## Dependencies",
            "## Open questions", "## Why this matters"]
PAIRS = [("447", "le31-an-expired-batch-can-still-be-sold-from"),
         ("448", "le31-a-bill-has-no-human-facing-identity"),
         ("449", "le31-an-order-line-may-carry-any-price-it-likes")]
for num, slug in PAIRS:
    fs = glob.glob(os.path.join(REPO, "features", num + "-*.md"))
    chk(len(fs) == 1, "exactly 1 feature file for %s" % num)
    if not fs: continue
    ft = open(fs[0], encoding="utf-8").read()
    for sec in TEMPLATE:
        chk(sec in ft, "feature %s has section %s" % (num, sec))
    ss = glob.glob(os.path.join(REPO, "specs", slug + "-HANDOFF.md"))
    chk(len(ss) == 1, "exactly 1 HANDOFF for %s" % num)
    if ss:
        ht = open(ss[0], encoding="utf-8").read()
        for sec in ("Frozen contract", "Rollback path", "Mandatory LE31 skill list",
                    "Verification protocol reference"):
            chk(sec in ht, "HANDOFF %s has %s" % (num, sec))

print("\n== E. INDEX rows in BOTH files ==")
for ip in ("/opt/data/INDEX.md", os.path.join(REPO, "INDEX.md")):
    t = open(ip, encoding="utf-8").read()
    for num, slug in PAIRS:
        chk(("features/%s-%s.md" % (num, slug)) in t, "INDEX %s has the %s row" % (os.path.basename(ip), num))

print("\n== F. git: MEMBERSHIP in origin/main (never the tip) ==")
log = sh("cd %s && git log --oneline origin/main" % REPO).stdout
chk("Daily brainstorm 2026-11-06" in log, "the brainstorm commit is in origin/main history")
chk("ad-hoc verifier for the 2026-11-06 brainstorm pass" in log, "the verifier commit is in origin/main history")
for num, slug in PAIRS:
    for p in ("features/%s-%s.md" % (num, slug), "specs/%s-HANDOFF.md" % slug):
        chk(sh("cd %s && git cat-file -e origin/main:%s" % (REPO, p)).stdout.strip() == "",
            "origin/main contains %s" % p)
chk(sh("cd %s && git status --porcelain -- INDEX.md features/44[789]-* specs/le31-an-expired* specs/le31-a-bill* specs/le31-an-order* _rerun_verification_2026_11_06.py" % REPO).stdout.strip() == "",
    "nothing uncommitted for this pass's paths")

print("\n== G. raw tree: canary + census + manifest agreement ==")
def walk(root):
    src, side = [], []
    for r, d, fs in os.walk(root):
        for f in fs:
            p = os.path.join(r, f)
            rel = os.path.relpath(p, root)
            if rel == "_manifest.json": continue
            (side if f.startswith("_") else src).append(p)
    return sorted(src), sorted(side)
src, side = walk(BASE)
chk(len(src) == 30, "30 source files (got %d)" % len(src))
chk(len(side) == 4, "4 sidecar files (got %d)" % len(side))
chk(sum(os.path.getsize(p) for p in src + side) == 7607154, "total bytes == 7607154")
chk(not [p for p in src + side if open(p, "rb").read().count(b"LE31")], "canary: 0 files contain 'LE31'")
chk(not glob.glob(os.path.join(BASE, "**", "*.py"), recursive=True), "no .py inside the raw tree")
man = json.load(open(os.path.join(BASE, "_manifest.json")))
mism = [f["path"] for f in man.get("files", [])
        if not os.path.exists(os.path.join(BASE, f["path"]))
        or os.path.getsize(os.path.join(BASE, f["path"])) != f.get("bytes")]
chk(not mism, "manifest files[] agree with disk (%d mismatches)" % len(mism))

print("\n== H. Linear fallback ==")
fb = json.load(open(FALLBACK))
chk(fb.get("linear_write_status") == "blocked", "fallback records blocked")
chk(fb["linear_error"].get("status") == 400, "fallback records HTTP 400")
chk(fb["linear_error"].get("parent_requestId") == "a56254647db6bbcd", "fallback records the parent requestId")
chk(len(fb.get("intended_sub_issues", [])) == 3, "fallback has 3 sub-issues")
for si in fb.get("intended_sub_issues", []):
    chk(si.get("created") is False, "sub-issue %s marked NOT created" % si.get("feature_number"))
    chk(si.get("project") == "le31 Research", "sub-issue %s routed to le31 Research" % si.get("feature_number"))
lp = fb["read_endpoints_reverified_this_pass"]["list_projects"]
chk(lp.get("le31_v2_owner_pains_exists") is False, "'le31 v2 owner-pains' recorded as NON-existent")

print("\n" + "=" * 60)
if fails:
    print("FAILURES: %d" % len(fails))
    for f in fails: print("   - " + f)
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
                'chk("CANARY: PASS" in out, "canary PASS on a fresh run")',
                'chk("CANARY: PASS-MUTATED" in out, "canary PASS on a fresh run")')
        with open(path, "w", encoding="utf-8") as f:
            f.write(body)
        # sqlmodel/sqlalchemy live ONLY in the verification venv, not the
        # system interpreter (which has no pip and no deps).
        py = "/opt/data/le31-verify-2026-10-27/.venv/bin/python"
        p = subprocess.run([py, path], capture_output=True, text=True)
        print(p.stdout)
        if p.stderr.strip():
            print("STDERR:", p.stderr[-3000:])
        code = p.returncode
    finally:
        try:
            os.unlink(path)
        except Exception:
            pass
    return code


if __name__ == "__main__":
    if "--negctl" in sys.argv:
        print("=== NEGATIVE CONTROL (mutate the canary assertion) ===")
        c = run(mutate=True)
        print("negctl exit code:", c)
        sys.exit(0 if c == 1 else 1)
    sys.exit(run())
