# auditable-continual-learning-measured-transaction-driver-role — HANDOFF

> **Slice for the coding agent.** Read this *and*
> `features/125-auditable-continual-learning-measured-transaction-driver-role.md`
> before touching anything. **This is a WATCH-LIST / ARCHITECTURE-
> REFERENCE slice, NOT a build slice.** There is no code deliverable.
> Do not paste chat excerpts back into the build.

## Frozen identifiers (do not rename)

- Feature ID: `125`
- Slug: `auditable-continual-learning-measured-transaction-driver-role`
- Contract file: `features/125-auditable-continual-learning-measured-transaction-driver-role.md`
- Bucket: **v2 owner-pains (architecture reference)** — defer
- Linear parent: **HMM-163** (Brainstorm 2026-08-27 — daily)
- Linear sub-issue: **HMM-164** (Feature)
- Sources: OpenAlex `W7202188416` (2026-08-11, primary) +
  `W7202172049` (verification bundle) + `W7202186994` (v2 update,
  2026-08-12)
- Raw fetch: `/tmp/le31-brainstorm-2026-08-27/oa_append-only-ledger-audit.json`

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md`.

**Evidence precondition: inferred.** The papers are real, dated,
in-window primary sources and the primitives are well-specified. What
is inferred is LE31's *need* for them — no owner has reported a
missing-driver-role or cumulative-halt problem, because v1 has no
effectful downstream cascades from `StockEntry`.

**Confidence: medium** for primitive quality; **low** for present LE31
urgency.

**Decision: defer (watch-list architecture reference).** No check
fails. The primitives complement charter §3.1 (explicit-state-
transitions, attributable to a named actor) rather than straining it.

**Known rabbit hole:** the meaning of "trusted base" in LE31's
single-restaurant setting. The paper's base is a model checkpoint
(multi-row, multi-dimensional); LE31's natural base would be the
prior `StockEntry` for the same `menu_item_id` (single-row, less rich
than the paper's base). The semantic transfers but adds less than the
ML setting, and the cumulative halt's value scales with the richness
of the base.

**Circuit breaker:** if LE31 v2 scope settles without any effectful
downstream cascades from `StockEntry`, this artifact expires unused.
That is an acceptable outcome and should not be treated as a failure.

## Mandatory LE31 skill list (load these first)

1. `le31-conventions` — project invariants + the seven-check gate.
2. `le31-research` — research observation discipline; no fabrication.
3. `le31-daily-brainstorm` — this pick came from the 2026-08-27 pass.
4. `le31-feature-pipeline` — how this slice is sequenced.

If the destination repo does not ship these skills, request them from
the project owner before starting. **Do not invent LE31 conventions.**

## Files to touch

| File | Action | Notes |
|---|---|---|
| `features/125-auditable-continual-learning-measured-transaction-driver-role.md` | (already written) | the contract; no further edit needed today |
| `/opt/data/INDEX.md` | append | one pipeline row (done in this pass) |

**No source file is touched. No test is added. No migration is
written.**

## What the coding agent must NOT do

- **Do not implement a `driver` column, a `measured_against` column,
  a `cumulative_halt` table, or any related schema change.** No code
  was authorised by this slice.
- **Do not modify the `StockEntry` model or any existing ledger row.**
  v1 commits carry explicit `via` enum entries and `actor_user_id`;
  that posture stands and this slice does not reopen it.
- **Do not change the v1 privacy boundary.** Charter §3.2 keeps v1
  guest demographics as counts, not identity or contact data. That
  decision stands and this slice does not reopen it.
- **Do not start any v2-AI work.** The paper is set in ML continual
  learning; LE31 v1 ships no AI surface. The primitives transfer
  because both settings have an append-only ledger, but the evidence
  base is AI-adjacent and the slice does not pre-authorise v2-AI
  work.
- **Do not add a dependency.**
- **Do not treat this artifact as pre-authorising a v2 feature.** Any
  concrete v2 cascade surface must run the gate on its own merits.

## Trigger for the next step

The first LE31 v2 feature proposal that introduces an **effectful
downstream cascade** from a `StockEntry` commit. Candidates:

- auto-reorder trigger (when current stock falls below threshold,
  emit a supplier-order `StockEntry`)
- supplier email cascade (when a `StockEntry` of `via=receive`
  commits, send the supplier an acknowledgement)
- payment reconciliation cascade (when a `StockEntry` of
  `via=void` commits, mark the matching payment as adjusted)
- end-of-shift auto-recap (when the day's last `StockEntry` commits,
  generate the owner's daily Telegram recap)

When any of these (or equivalent) is proposed:

1. Read the **full pre-registration bundle** (FP-471..FP-516), not
   just the abstract, with specific attention to the gate-policy
   ladder and the seal / driver / report triplet.
2. **First ask whether the cascade is needed at all.** Per charter
   §3.1, explicit-state-transitions are a deliberate safety
   principle; an "automatic cascade" is exactly the kind of silent
   transition the charter forbids. The cascade should be *opt-in per
   context*, never default.
3. Only if a cascade is genuinely warranted, design it with the
   three primitives (measured transaction + driver + cumulative halt)
   in mind — and run `le31-conventions` on that concrete feature
   independently.

## Verification protocol

Reference: `coding-agent/skills/le31-verification-protocol/SKILL.md`.

For this slice, verification is documentary rather than behavioural,
because there is no behaviour:

- [ ] `features/125-auditable-continual-learning-measured-transaction-driver-role.md`
      exists and was read back.
- [ ] The OpenAlex IDs, publication dates, and quoted passages in the
      contract match the raw JSON at
      `/tmp/le31-brainstorm-2026-08-27/oa_append-only-ledger-audit.json`.
- [ ] Quoted passages are verbatim from that raw file — **not
      paraphrased and not reconstructed from memory.**
- [ ] `/opt/data/INDEX.md` has the pipeline row.
- [ ] Linear HMM-164 exists with label `Feature` and parent HMM-163.
- [ ] No source file, schema, or test was modified.

## Rollback path

Delete `features/125-auditable-continual-learning-measured-transaction-driver-role.md`,
delete `specs/auditable-continual-learning-measured-transaction-driver-role-HANDOFF.md`,
remove the `/opt/data/INDEX.md` row, and cancel HMM-164.

**Rollback cost: zero.** Nothing depends on this artifact, no schema
was touched, no data was migrated, and no behaviour changed.

## Open questions carried into the slice

- Will LE31 v2 ever introduce effectful downstream cascades from
  `StockEntry`? If no, expire this artifact.
- Is the *driver* role worth modeling as a separate primitive, or is
  expanding `actor_user_id`'s semantics sufficient?
- What "trusted base" means in LE31's single-restaurant setting.
  Single-row reference (prior `StockEntry` for the same
  `menu_item_id`) is the obvious choice but adds little beyond
  `prev_hash`. The paper's value comes from a multi-row base which
  LE31 doesn't have.
- Is a *cumulative halt* proportionate for any plausible v2 cascade?
  Per-supplier aggregate, per-day aggregate, per-restaurant aggregate
  each have different halt semantics.
- Does LE31 need the "seal / driver / report" triplet, or only the
  driver? The seals (cryptographic commitments) are paper-specific;
  the driver (attribution) and report (audit trail) are the
  generalisable pair.
