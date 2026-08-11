# Feature 55 — Evidence Review Surface

> **Priority**: P2 · **Effort**: M (≤3 days) · **Source**: brainstorm 2026-08-11
> (cross-section pick A) · **Bucket**: v2 owner-pains
> **One-line**: an owner-facing evidence-review surface over the existing
> append-only ledger — "show me the receipts" — that composes the
> already-shipped audit features (30 + 47 + 49 + 50) and the existing
> StockEntry + AuditLog + DecisionRationale tables into one Telegram
> surface that answers "what claim is *this* LE31 push backed by, and
> where is the evidence row?".

## Goal

LE31 already ships four append-only-strength features:

- **30** `append-only-audit-redirect` (HTTP 308 preserve-method safety net)
- **47** `decision-rationale-mixin` (per-row rationale column)
- **49** `postledger-tamper-evident-hash` (per-row hash chain)
- **50** `lifecycle-citation-mixin` (state-machine citation)

and the underlying tables:

- `AuditLog`
- `StockEntry` (append-only stock ledger)
- `VoidRationale` (per-void WhyReason)
- `DecisionRationale` (mixin column)

These pieces collectively form a **defensible, audit-grade evidence
chain** — but the owner cannot get to them today without database
inspection. The owner needs a one-Telegram-tap surface that answers:
when the recap or any other push claims "we ran out of lamb at 21:30",
"here is the row, the rationale, the hash, the cook who entered it, and
when it was entered".

The cross-section anchor is `paulmurphynet/chronicle` (pushed
**2026-08-11**, Python, ★0, "Local, append-only evidence review for
consequential answers") — an identical-shape service from a different
domain. The owner-side review surface is novel because LE31 already has
the data; chronicle validates the *shape*, and LE31 contributes the
*content*.

## Scope

**In scope (v2 owner-pains):**

- One new SQLModel table: `EvidenceLink(id, claim_kind, claim_ref_id,
  evidence_table, evidence_ref_id, added_at)`. Append-only. Each row
  says: "for claim of kind X (e.g. recap-summary) referencing row Y
  (e.g. the recap row at 21:30), the evidence is at table T row R (e.g.
  StockEntry at 21:30)". One-many: a claim can reference multiple
  evidence rows; an evidence row can be cited by multiple claims.
- One new Alembic migration creating `evidence_link`.
- A nightly builder job `evidence_link_build()` that, for every
  `OwnerRecap` row from the last 7 days (feature 39), walks the recap's
  supporting claims (covers, voids-with-reasons, top movers, prep
  shortfalls) and inserts one `EvidenceLink` row per claim-evidence
  pair. APScheduler-triggered at 00:30 Europe/Paris (1 hour after
  feature 39's 23:30 push). Idempotent (key on
  `(claim_kind, claim_ref_id, evidence_table, evidence_ref_id)`).
- A backfill helper `scripts/backfill_evidence_links.py` that, given a
  date range, rebuilds `EvidenceLink` rows for historical `OwnerRecap`
  rows. Used once after deploy.
- A new bot command `/explain <recap_row_id>` — owner-only. Bot replies
  with a structured card:
  ```
  📑 OwnerRecap #R-2026-08-10-001 — folded 23:30 (H:abcd)
  Claim "lamb was 86ed at 21:30"
    ├─ StockEntry #4128 — qty_delta=-3 — by_user_id=cook-2
    │   at: 2026-08-10T21:31:04+02:00 — hash: a3f9…
    ├─ VoidRationale #V-219 — "ran out" — by_user_id=cook-2
    │   at: 2026-08-10T21:31:05+02:00 — hash: 12ee…
    └─ CookChannel SSE event #C-2026-08-10-21:30
        payload: "lamb 86ed" — at: 2026-08-10T21:31:00+02:00
  ```
- A new bot command `/verify last-week` — owner-only. Bot replies with a
  short summary: `7 owner recaps · 127 evidence links · 1 missing
  link (R-2026-08-08-001 · "tiramisu sold out" has no StockEntry row)`.
  Missing links are surfaced so the owner can spot gaps.
- A new CLI `scripts/verify_evidence_chain.py` that prints the same
  data structure to stdout for owner-offline review.

**Out of scope (v2 owner-pains):**

- Per-row on-chain-style verification (e.g. publish the hash chain to
  Ethereum) — feature 49 is sufficient at v2.
- Cross-restaurant evidence chains — single restaurant per instance.
- Auto-redaction of named staff in the `/explain` reply — names are
  intentional for the owner; redaction is a v3 follow-up if the owner
  surfaces the card to others.
- AI summary of evidence — this is a lookup surface; the v3
  second-opinion-council-recap (parking-lot) will sit on top.

## Description

The owner receives an `OwnerRecap` (feature 39) at 23:30 every evening.
The recap is a set of claims (covers, voids, top movers, prep
adherence). Each claim is *backed by* rows in LE31's existing tables —
but until today, the owner has no way to see the chain.

This feature adds the missing *evidence link* table and a builder that
populates it. The owner then gets two new commands:

1. `/explain <recap_row_id>` — per-claim evidence card.
2. `/verify last-week` — gap-check for the last 7 days.

Both commands are read-only; they never modify the chain. The
underlying append-only guarantee is preserved (47 + 49 + 50).

## Data model

```
EvidenceLink    (id, claim_kind, claim_ref_id,
                 evidence_table, evidence_ref_id,
                 added_at)
                -- claim_kind in ('owner_recap_summary',
                --                 'void_with_reason',
                --                 'cook_channel_event',
                --                 'prep_checkoff_skip')
```

`claim_kind` is an enum-style string; new kinds can be added without
schema migration. `evidence_table` is also an enum-style string; adding
a new evidence source requires one new value and one new builder code
path.

Append-only: rows are never updated or deleted. The
`(claim_kind, claim_ref_id, evidence_table, evidence_ref_id)` tuple is
unique — runs of the builder are idempotent at the SQL level.

## Implementation steps

1. Add `EvidenceLink` SQLModel table to `backend/app/models.py`.
2. Add Alembic migration to
   `backend/alembic/versions/<new>_evidence_link.py`.
3. Add `evidence_link_build()` background task to
   `backend/app/services/evidence.py` (NEW module). Runs nightly at
   00:30 Europe/Paris.
4. Add idempotent `unique(claim_kind, claim_ref_id, evidence_table,
   evidence_ref_id)` constraint at the SQLModel level (Alembic
   migration creates the index).
5. Add `/explain` and `/verify` bot command handlers in
   `backend/app/bot/cook_bot_explain.py` (NEW module).
6. Register the two new bot command handlers in
   `backend/app/bot/cook_bot.py` router (mirror feature 39's
   registration pattern).
7. Add the APScheduler job registration to `backend/app/main.py`
   lifespan (1 line).
8. Add `scripts/verify_evidence_chain.py` (read-only CLI).
9. Add `scripts/backfill_evidence_links.py` (idempotent backfill).
10. Add `backend/tests/test_evidence_link.py` (unit tests for the
    builder and the bot commands).
11. Update `backend/README.md` with the two bot commands.

## Telegram interaction if any

Two new owner-only commands:

- `/explain <recap_row_id>` — returns a structured per-claim evidence
  card (see Description). Markdown formatted. Falls back to "No recap
  row <R>" if not found. Falls back to "No evidence links yet for this
  recap (builder hasn't run)" if the builder has not yet run on this
  row.
- `/verify last-week` — returns a 2-3 line gap-check summary. Falls
  back to "All clear — no missing evidence links." for a perfect 7-day
  run.

Both commands reject any non-owner chat_id with the same 1-line
"unauthorized" message used by feature 39's `/ack`.

## Dependencies

- **Feature 30** `append-only-audit-redirect` — pre-existing.
- **Feature 47** `decision-rationale-mixin` — pre-existing.
- **Feature 49** `postledger-tamper-evident-hash` — pre-existing.
- **Feature 50** `lifecycle-citation-mixin` — pre-existing.
- **Feature 39** `owner-daily-recap-telegram` — pre-existing; the
  `OwnerRecap` table is the primary `claim_kind` source.

No new pip dependencies. APScheduler is already imported.

## Open questions

- Should `evidence_table` allow free-form strings or be an enum-style
  fixed set at the v1 cut? Decision: fixed set, add new values via PR.
- Should `/verify` accept explicit date ranges, or just `last-week` /
  `last-month` shorthand? Decision: shorthand only at v1, range parser
  added in v2 if the owner asks.
- Should missing links trigger an automatic Telegram alert to the
  owner (e.g. "3 missing links in the last 7 days — run /verify"), or
  stay pull-only? Decision: pull-only at v1; auto-alert is a v2
  follow-up.

## Why this matters

LE31's moat is its append-only ledger. Today the moat is
defence-grade (the rows are honest) but invisible (the owner cannot see
the chain). This feature turns the moat into a **daily-grade UX** — the
owner can answer any "why did the recap say X?" in two Telegram commands.
That converts a technical guarantee (hash chain) into a sales-grade
promise ("the owner can verify it themselves").

`paulmurphynet/chronicle` is a same-week, same-shape, different-domain
data point that we did not invent this; we merely recognise that LE31
already has both the data and the need, and that today the link is
unmade.
