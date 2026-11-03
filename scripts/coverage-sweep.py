#!/usr/bin/env python3
"""Coverage sweep — 2026-11-03 brainstorm pass.
Greps the WHOLE features/ corpus once per concept. A zero-hit result is a
CANDIDATE, not a licence — the script names the three extra checks.
Exit 1 when something is uncovered, 2 when the repo cannot be read.
"""
import os, re, sys

REPO = "/opt/data/le31_mmm3_research_work"
FE = os.path.join(REPO, "features")
SP = os.path.join(REPO, "specs")

feats = sorted(f for f in os.listdir(FE) if f.endswith(".md"))
specs = sorted(f for f in os.listdir(SP) if f.endswith(".md"))
if len(feats) < 50:
    print("cannot read features corpus (only %d files)" % len(feats)); sys.exit(2)

blob = {}
for f in feats:
    blob[f] = open(os.path.join(FE, f), encoding="utf-8", errors="replace").read().lower()
sblob = {}
for f in specs:
    sblob[f] = open(os.path.join(SP, f), encoding="utf-8", errors="replace").read().lower()

def sweep(corpus, name):
    for label, pat in OBS:
        rx = re.compile(pat, re.I)
        hits = [f for f in corpus if rx.search(corpus[f])]
        if hits:
            print("  %-52s COVERED (%d)  %s" % (label, len(hits), sorted(hits)[:2]))
        else:
            print("  %-52s *** NOT COVERED ***" % label)

# ---- concept sweep -------------------------------------------------------
OBS = [
    # --- order / kitchen state machine ---
    ("kitchen ticket fire -> ready -> served transition",
     r"fired_at|fire_time|kitchen ticket.*(ready|served)"),
    ("order item state machine (new/preparing/ready/served)",
     r"itemstatus|item_status|preparing.*ready.*served|status.*new.*preparing"),
    ("who is cooking / kitchen display of items to make",
     r"kitchen display|kds|items to (make|cook)|cook queue"),
    ("course sequencing (appetizer before main)",
     r"\bcourse\b.*(appetizer|starter)|course sequenc|sequential.*course"),
    ("dishes course to course (fire per course)",
     r"per course|course by course|dish.*course"),
    # --- money / payments ---
    ("split bill across guests / payment allocation",
     r"split bill|split payment|payment.*allocat|allocat.*payment"),
    ("multiple tenders on one bill",
     r"multiple (payment|tender)|partial (payment|cash)|multi-tender"),
    ("cash drawer / float / over and short",
     r"cash drawer|over and short|shortage|float.*variance"),
    ("card payment terminal / reader integration",
     r"payment terminal|card reader|stripe|adyen|sumup|zettle|sumup.*terminal"),
    ("receipt / receipt printing",
     r"receipt"),
    ("discount / promo code",
     r"discount|promo code"),
    ("service charge",
     r"service charge"),
    # --- table / seating ---
    ("table reservation / booking",
     r"reservation|book(ing)? a table|reserve a table"),
    ("table turn / turnover time",
     r"turnover|turn time|table turn"),
    ("waitlist",
     r"wait ?list"),
    ("table merge / split (combining tables)",
     r"merge.*table|table.*merge|combine.*table|split.*table.*party"),
    ("floor plan / table positions",
     r"floor ?plan|floor map|\bfloor\b"),
    # --- staff ---
    ("staff rota / shift scheduling",
     r"rota|shift schedul|schedule.*staff|staff schedul"),
    ("tip pooling / tip share between staff",
     r"tip pool|tip shar|pool.*tip|tip split"),
    ("telegram command catalogue / permission per command",
     r"command.*(allowlist|permission)|allowed_user_ids"),
    # --- menu ---
    ("allergen / dietary",
     r"allergen|dietary|gluten|nut allergy"),
    ("menu item modifier / variant / option group",
     r"modifier|variant|option group"),
    ("menu availability per day / seasonal menu",
     r"seasonal|menu.*per day|daily menu"),
    # --- reporting ---
    ("covers today KPI",
     r"covers today|cover count"),
    ("avg dwell time",
     r"dwell"),
    ("top items report",
     r"top.?item"),
    ("forecast / prep quantity suggestion",
     r"forecast|avg_14d|prep quantit"),
    # --- ordering channels ---
    ("customer-facing ordering (QR / kiosk)",
     r"qr code|qr menu|kiosk|customer.?facing|self.?order"),
    ("delivery / takeaway channel",
     r"delivery|takeaway|take.?away|pickup"),
    ("online ordering integration",
     r"online order|web order|ordering channel"),
    # --- inventory ---
    ("supplier / purchase order",
     r"supplier|purchase order|\bpo\b"),
    ("waste / spoilage",
     r"waste|spoilage"),
    ("stock count / stocktake",
     r"stocktak|stock count|cycle count|inventory count"),
    ("recipe / bill of materials (BOM)",
     r"bill of material|\bbom\b|recipe.*ingredient|ingredient"),
    ("unit of measure (kg vs piece)",
     r"unit of measure|\bunit\b.*(kg|piece|litre)|different units|unit.*dimension"),
    # --- audit / reliability ---
    ("idempotency key on writes",
     r"idempotenc"),
    ("offline mode / sync conflict",
     r"offline.?first|conflict resolution|sync conflict"),
    ("audit log / who changed what",
     r"audit log|audit trail|who changed"),
    ("soft delete vs void",
     r"soft delete|voided|void the|void\b"),
    ("timezone / business day boundary",
     r"business date|service day|timezone|business day"),
    ("privacy / data retention",
     r"retention|gdpr|privacy|pii"),
]
print("=== CONCEPT SWEEP over %d feature contracts ===" % len(feats))
sweep(blob, "features")

print()
print("=== CONCEPT SWEEP over %d spec HANDOFFs ===" % len(specs))
sweep(sblob, "specs")

print()
print("Three extra checks required for every NOT COVERED result:")
print("  (a) out of scope per charter s3.2 non-goals?")
print("  (b) already registered as an open owner question? (e.g. service charge = D-005 in feature 409)")
print("  (c) covered under different words by another feature?")
sys.exit(1)
