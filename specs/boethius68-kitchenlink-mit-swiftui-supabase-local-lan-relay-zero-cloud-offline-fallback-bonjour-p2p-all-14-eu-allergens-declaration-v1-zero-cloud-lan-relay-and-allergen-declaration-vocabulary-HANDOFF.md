# HANDOFF — Feature 380: `boethius68/KitchenLink` zero-cloud LAN relay + EU-14 allergen declaration (vocabulary reference)

**This is a `defer` pick — a vocabulary reference, NOT a build.** No code changes. No schema change. The deliverable is **two sentences in LE31's own documentation**. If a coding agent finds itself writing application code for this feature, it has misread the contract — stop.

**Discovery chain:** Daily Brainstorm 2026-10-25 → GitHub Search `topic:restaurant` / `topic:pos` / `topic:hospitality` cluster (17/17 queries HTTP 200, aggregate `total_count` re-derived from disk) → parent read the upstream README → parent read LE31's own `backend/app/models.py` and found **`MenuItem` has no allergen field at all**.

**Full evidence record: `features/380-boethius68-kitchenlink-mit-swiftui-supabase-local-lan-relay-zero-cloud-offline-fallback-bonjour-p2p-all-14-eu-allergens-declaration-v1-zero-cloud-lan-relay-and-allergen-declaration-vocabulary.md`**

## Active feature path

`features/380-boethius68-kitchenlink-mit-swiftui-supabase-local-lan-relay-zero-cloud-offline-fallback-bonjour-p2p-all-14-eu-allergens-declaration-v1-zero-cloud-lan-relay-and-allergen-declaration-vocabulary.md` — **defer** (Pick B of Daily Brainstorm 2026-10-25).

## Seven-check gate verdict

| # | Check | Pass? | Note |
|---|-------|-------|------|
| 1 | Raison d'être / JTBD | ✗ **FAIL — by design** | The pain is **not observed in LE31**. There is no restaurant currently asking for allergen data from LE31, and no evidence of a missed allergen declaration causing a problem. Evidence class: **inferred** (from one external README), confidence **low**. **This is why the verdict is `defer` and not `build`.** The one part that *is* observed is the shape gap: `MenuItem` has no field capable of holding an allergen set (parent-read `backend/app/models.py`, 2026-10-25). **A shape gap is not a pain.** |
| 2 | Viability | ✓ | Trivial — one or two sentences of documentation. No operator-facing surface, so nothing to train, nothing to maintain, nothing for a non-technical owner to operate. |
| 3 | Practicability and confidence | ✓ | On-stack requirement: **none** — no code is written. The vocabulary (a *set* of allergen codes, EU-14-shaped, owned by the dish not the guest) fits LE31's `MenuItem` model without conflict with the *Privacy* invariant (allergens are a **dish** attribute; v1 guest data stays counts). **Named rabbit hole:** whether EU-14 is even the right regulatory set for LE31's owner — see Open questions 1. |
| 4 | Conflict | ✓ | No invariant is violated by documentation. **One near-miss to respect:** LE31's *Privacy* invariant ("store only data needed for restaurant operations"). Recording that *allergens will eventually live on the menu item, not the guest record* is the point of the sentence — it forecloses a future design that would collect guest medical data. That is the sentence's real job. |
| 5 | Outcome + appetite + scope | ✓ | Serves a v1 documentation outcome (named boundaries). Maximum time worth spending: **30 minutes**. Scope is two sentences. **Explicitly NOT in scope:** any `allergens` column, any LAN relay, any multicast/mDNS/Bonjour, any WebSocket, any Flutter/Dart, any Supabase. |
| 6 | Cost to operational value | ✓ | Very low cost, **currently low value** — the value is *option-preserving* (the shape is known before it is needed) rather than operational today. **The honest reason this file exists:** it is the first in 88 passes to name a *menu-dish attribute LE31's model cannot express at all*, and the third arrival in three passes describing the same venue boundary. Neither justifies a schema change; both justify two sentences. |
| 7 | Circuit breaker + reversibility | ✓ | **Trivially reversible: delete two sentences.** No data, no code, no migration, no operator-visible change. **Stop evidence:** if the owner states EU-14 is irrelevant to their venue, the allergen sentence should be deleted rather than reworded. **Review point:** when the waiter/cook UX feature is scheduled (see Feature 375), decide whether the named zero-cloud state needs more than a sentence. |

**Gate verdict: `defer`** (parking-lot). Check 1 fails on observed evidence — deliberately, and the file says so.

## Bucket

**v1 (connectivity-boundary + allergen-declaration vocabulary)** — Pick B of Daily Brainstorm 2026-10-25. This is a **v1-bucket** pick, so per `le31-feature-pipeline/SKILL.md` step 4 the matching project would be `le31 v1 — Core MVP` (P-HMM-3). **However**, per `le31-feature-pipeline/SKILL.md` line 33, confirm the workspace with `list_projects` before assuming — the parent confirmed on 2026-10-25 that the workspace contains exactly three projects (`le31 v1 — Core MVP` P-HMM-3, `le31 Workflow` P-HMM-2, `le31 Research` P-HMM-1); `le31 v2 owner-pains` / `le31 v2-AI` do **not** exist. Because the **parent research issue for this pass also failed to create** (Linear MCP write endpoint blocked — 38th consecutive day), the sub-issue has no parent to hang under — it is routed to `le31 Research` (P-HMM-1) in the fallback payload, and that is the only project that exists for the write.

## Files to touch

**The change (documentation only — this is the complete list):**

- `PROJECT_CHARTER.md` — **add ONE sentence** somewhere in §3.2 (Out of scope / explicit non-goals) or §4.4 (Folder layout) recording that the **zero-cloud fallback is a named state** distinct from a failed request, with a pointer to feature 376 (the LAN-only ordering surface, filed 2026-10-25 by the daily-research cron) and to this feature.
- `PROJECT_CHARTER.md` — **add ONE sentence** (or a comment beside `class MenuItem` in `backend/app/models.py`) recording that `MenuItem` will eventually carry a **structured, EU-14-shaped allergen set** — a set of codes, not free text, owned by the dish and never by the guest — and that this is **deferred to v2 pending an owner decision**.

**Do NOT touch (out of scope, explicitly):**

- `backend/app/models.py` — **no column.** The only permitted change is an optional **comment**; **no schema change of any kind.**
- `backend/app/` — **no new module, no new dependency.** In particular, **do not add** `zeroconf`, `pyzeroconf`, `netifaces`, `zeroconf` or any multicast/DNS-SD library. None is in the project today; **do not add one for this feature.**
- `backend/app/bot/cook_bot.py` — no change.
- The waiter UI (`index.html` and the FastAPI static surface) — no change.
- **Features 11 (`customer-qr-menu`), 375 (waiter-surface status visibility), 376 (`drsamonline/canteen-lan` LAN ordering surface)** — all already filed; **do not re-implement or re-file them.**

## Verification protocol reference

Per `le31-conventions`: *"Declaring done from a diff or passing tests alone"* is a pitfall. For a documentation-only feature the observable behaviour is **the sentence existing in the file a future agent actually reads**, and the charter staying internally consistent.

```bash
cd /opt/data/le31_mmm3_research_work
# 1. The two sentences are present.
grep -n -i 'allergen' PROJECT_CHARTER.md
grep -n -i 'zero-cloud\|zero cloud\|local relay\|LAN relay' PROJECT_CHARTER.md

# 2. No schema change crept in — MenuItem must still have exactly its original fields.
sed -n '/^class MenuItem/,/^class Batch/p' backend/app/models.py
# expect: id, name, category, unit_price, unit, is_prepared, photo_url — and NO allergens field

# 3. No new dependency crept in.
grep -n -i 'zeroconf\|netifaces\|multicast' backend/requirements.txt
# expect: no output
```

**Verification is a negative check here.** The success condition of a `defer` vocabulary feature is that **nothing changed except two sentences.** If any of the three commands shows a schema or dependency change, the feature was implemented wrongly — revert it.

## Rollback path

`git revert` the commit, or delete the two sentences. **No data loss, no migration, no operator impact.** This is the cheapest possible rollback in the whole series.

## Mandatory LE31 skill list for the coding agent

- `le31-conventions` — hard invariants and the seven-check gate (read the *Privacy* rule first; the allergen sentence's job is to keep allergen data on the dish and off the guest)
- `le31-handoff-spec` — this document's format
- `PROJECT_CHARTER.md` — source of truth; **the file being edited**
- `le31-feature-pipeline` — for the "what a `defer` pick means" contract
- **Do NOT load** `le31-backend` unless you are writing code — **this feature writes no code.** (Load it only if the owner later promotes the feature to a build, in which case a fresh contract must be written first.)

## Open questions carried into any future build

1. **Is EU-14 the right regulatory set for LE31's owner?** The charter sets business time to `Europe/Paris`, which implies France — and France's declarable-allergen list is the EU-14. **But the owner's actual venue may need a different set, and a wrong allergen list is worse than no allergen list.** **Owner decision required. Until then, do not collect allergen data and do not add the column.**
2. **`MenuItem.allergens` as a set column, or a separate `MenuItemAllergen` table?** LE31's §4.3 append-only discipline applies to *stock*, not to *mutable menu metadata*, so a simple set column is defensible. **But it should be decided once, deliberately, when the feature is actually scheduled** — not now.
3. **Does the "named zero-cloud state" belong in the charter, or in the waiter/cook UX feature?** Feature 375 (85th pass, "visibility of system status") is where the *behaviour* belongs. **Recommendation: one cross-reference sentence in the charter now, full treatment deferred to Feature 375.** **Do not open a new charter section for this.**
4. **Does LE31 need a *guest* allergen filter at all** (a guest with an allergy asking "does this dish contain nuts?")? That is a **guest-facing** feature and **LE31 has no customer-facing surface** — the charter's *AI* and *Privacy* invariants both constrain it. **If the answer is "no", the dish-side allergen set is still worth having (for the waiter to read aloud); if the answer is "yes", it is a scope decision for the owner, not for this feature.**
