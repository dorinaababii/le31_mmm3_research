# ledger-commitment-field-tier-minimization — HANDOFF

> **Slice for the coding agent.** Read this *and*
> `features/121-ledger-commitment-field-tier-minimization.md` before
> touching anything. **This is a WATCH-LIST / ARCHITECTURE-REFERENCE
> slice, NOT a build slice.** There is no code deliverable. Do not
> paste chat excerpts back into the build.

## Frozen identifiers (do not rename)

- Feature ID: `121`
- Slug: `ledger-commitment-field-tier-minimization`
- Contract file: `features/121-ledger-commitment-field-tier-minimization.md`
- Bucket: **v2 owner-pains (architecture reference)** — defer
- Linear parent: **HMM-159** (Research 2026-08-27 — daily)
- Linear sub-issue: **HMM-160** (Feature)
- Source: arXiv `2608.25474v1` (2026-08-26, cs.CR)
- Raw fetch: `/tmp/le31-daily-2026-08-27/arxiv/arxiv_append-only_ledger.xml`

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md`.

**Evidence precondition: inferred.** The paper is a real, dated,
in-window primary source and its mechanism is well-specified. What is
inferred is LE31's *need* for it — no owner has reported a
privacy-minimisation problem, because v1 stores only counts per charter
§3.2.

**Confidence: medium** for mechanism quality; **low** for present LE31
urgency.

**Decision: defer (watch-list architecture reference).** No check
fails. The only blocker is absence of present need. The mechanism
strengthens rather than strains the charter §3.1 append-only invariant.

**Known rabbit hole:** canonicalisation of parameters across schema
evolution. The abstract does not resolve it; this is where such schemes
usually fail in practice and it must be settled before any
implementation.

**Circuit breaker:** if LE31 v2 scope settles without recording any
identifying field, this artifact expires unused. That is an acceptable
outcome and should not be treated as a failure.

## Mandatory LE31 skill list (load these first)

1. `le31-conventions` — project invariants + the seven-check gate.
2. `le31-research` — research observation discipline; no fabrication.
3. `le31-daily-research` — this pick came from the 2026-08-27 pass.
4. `le31-feature-pipeline` — how this slice is sequenced.

If the destination repo does not ship these skills, request them from
the project owner before starting. **Do not invent LE31 conventions.**

## Files to touch

| File | Action | Notes |
|---|---|---|
| `features/121-ledger-commitment-field-tier-minimization.md` | (already written) | the contract; no further edit needed today |
| `/opt/data/INDEX.md` | append | one pipeline row (done in this pass) |

**No source file is touched. No test is added. No migration is
written.**

## What the coding agent must NOT do

- **Do not implement a canonical digest, a tier table, or any
  minimisation logic.** No code was authorised by this slice.
- **Do not modify the `StockEntry` model or any existing ledger row.**
  v1 entries carry no identifying fields and need no minimisation.
- **Do not change the v1 privacy boundary.** Charter §3.2 keeps v1
  guest demographics as counts, not identity or contact data. That
  decision stands and this slice does not reopen it.
- **Do not add a dependency.**
- **Do not treat this artifact as pre-authorising a v2 feature.** Any
  concrete v2 surface must run the gate on its own merits.

## Trigger for the next step

The first LE31 v2 feature proposal that records an **identifying
field** (supplier contact, staff identifier, delivery detail, or
similar).

When that happens:

1. Read the **full paper**, not just the abstract, with specific
   attention to canonicalisation across schema change.
2. **First ask whether the field needs recording at all.** Per charter
   §3.2, "record less" is the cheaper and usually better answer, and
   should be the default.
3. Only if a commitment is genuinely warranted, design it — and run
   `le31-conventions` on that concrete feature independently.

## Verification protocol

Reference: `coding-agent/skills/le31-verification-protocol/SKILL.md`.

For this slice, verification is documentary rather than behavioural,
because there is no behaviour:

- [ ] `features/121-ledger-commitment-field-tier-minimization.md` exists
      and was read back.
- [ ] The arXiv ID, publication date, and category in the contract match
      the raw XML at
      `/tmp/le31-daily-2026-08-27/arxiv/arxiv_append-only_ledger.xml`.
- [ ] Quoted passages are verbatim from that raw file — **not
      paraphrased and not reconstructed from memory.**
- [ ] `/opt/data/INDEX.md` has the pipeline row.
- [ ] Linear HMM-160 exists with label `Feature` and parent HMM-159.
- [ ] No source file, schema, or test was modified.

## Rollback path

Delete `features/121-ledger-commitment-field-tier-minimization.md`,
delete `specs/ledger-commitment-field-tier-minimization-HANDOFF.md`,
remove the `/opt/data/INDEX.md` row, and cancel HMM-160.

**Rollback cost: zero.** Nothing depends on this artifact, no schema
was touched, no data was migrated, and no behaviour changed.

## Open questions carried into the slice

- Will LE31 v2 ever record an identifying field? If no, expire this.
- Does the paper's canonicalisation approach survive schema evolution
  under SQLModel/Postgres? **Unknown — full text unread.**
- Is a hash-committed ledger with an offline verifier proportionate for
  a single small restaurant?
- **Who would run the offline verifier?** The owner is the only
  stakeholder; there is no adversarial auditor. This materially weakens
  the case for the full construction and should be answered before any
  implementation is contemplated.
