# dhh-kitchen-accessible-operator-ux-visual-replayable — HANDOFF

> **Slice for the coding agent.** Read this *and*
> `features/130-dhh-kitchen-accessible-operator-ux-visual-replayable.md`
> before touching anything. **This is a WATCH-LIST / UX-REFERENCE
> slice, NOT a build slice.** There is no code deliverable.
>
> **This slice does NOT authorise any instructional feature, and it is
> NOT an accessibility-compliance commitment.** Reading a study about
> deaf and hard-of-hearing employees as design input is a different
> thing from claiming conformance to any accessibility standard. LE31
> makes no such claim here.

## Frozen identifiers (do not rename)

- Feature ID: `130`
- Slug: `dhh-kitchen-accessible-operator-ux-visual-replayable`
- Contract file: `features/130-dhh-kitchen-accessible-operator-ux-visual-replayable.md`
- Bucket: **v2 owner-pains (UX reference)** — defer
- Linear parent: **HMM-169** (Brainstorm 2026-08-28 — daily)
- Linear sub-issue: **HMM-171** (Feature)
- Source: DOI `10.30892/gtg.67330-1842` / OpenAlex `W7204185698` (2026-08-25)
- Journal: *GeoJournal of Tourism and Geosites* (**peer-reviewed**)
- Raw fetch: `/tmp/le31-brainstorm-2026-08-28/openalex_phone-first20interface20restaurant.json`

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md`.

**Evidence precondition: observed — highest evidence grade in the
29-pass series.** Peer-reviewed journal article (not a preprint, not a
low-star repo), named population (**30 restaurant managers**, Egypt),
named method (job demands-resources model, reflexive thematic
analysis), studying instruction delivery in noisy fast-paced kitchens
under service pressure.

**⚠️ CRITICAL PROVENANCE WARNING.** The delegated subagent's rendering
of this specific abstract was **partly fabricated**. It appended a
closing clause referencing *"the LE31 hands-busy, phone-first operator
surface"*, claimed **"five recurring practices"** where the paper
reports **four**, and invented barriers (*"gloved-touch interfaces,
screen glare under hood lighting"*) that **do not appear in the
source**. `grep -c 'LE31'` on the raw OpenAlex file returns **0**.
Everything in the contract was re-extracted by the parent agent from
`abstract_inverted_index`. **Any future quotation must come from the
raw file or from the DOI directly — never from the subagent summary.**

**Confidence: medium-high** for the findings as reported; **medium**
for transfer to LE31's Swiss context; **low** for present urgency.

**Decision: defer (watch-list UX-reference).** No check fails.

**Known rabbit hole — and it is the likely killer:** **authoring.**
The study's own term for adapting instructional material is
"managerial **bricolage**" — it is labour, not software. A solo owner
has no training department. **Any feature requiring authored step
sequences must solve authoring first or it will not ship.**

**Second known rabbit hole:** building a video or captioning pipeline
because the study's managers use captioned SOP videos. **Explicitly
out of scope.** LE31 has no video surface and adding one is not
implied.

**Circuit breaker:** if no v2 instructional surface appears, this
expires as a UX reference — but findings 2 and 3 retain standalone
value as validation of decisions already made.

## Mandatory LE31 skill list (load these first)

1. `le31-conventions` — project invariants + the seven-check gate.
2. `le31-research` — research observation discipline; no fabrication.
3. `le31-daily-brainstorm` — this pick came from the 2026-08-28 pass.
4. `le31-feature-pipeline` — how this slice is sequenced.
5. `le31-frontend` — if any operator-surface question is ever opened.

If the destination repo does not ship these skills, request them from
the project owner before starting. **Do not invent LE31 conventions.**

## Files to touch

| File | Action | Notes |
|---|---|---|
| `features/130-dhh-kitchen-accessible-operator-ux-visual-replayable.md` | (already written) | the contract; no further edit needed today |
| `/opt/data/INDEX.md` | append | one pipeline row (done in this pass) |

**No source file is touched. No test is added. No migration is
written. No media is stored.**

## What the coding agent must NOT do

- **Do not build a step-sequence model, media store, or captioning
  pipeline.** No schema change of any kind.
- **Do not build a video surface.** The study's managers use captioned
  videos; that does not make video an LE31 requirement.
- **Do not add completion tracking or per-employee performance
  records.** That would create a new identifying surface and requires
  an explicit charter §3.2 review **before** it is proposed, not
  after.
- **Do not claim or imply accessibility conformance.** This artifact
  is design input, not a compliance statement.
- **Do not push authoring burden onto the owner.** If a design
  requires the owner to author step sequences by hand, the design is
  wrong for a solo operator.
- **Do not read findings 2 and 4 as a mandate for new surface.** They
  *confirm* the existing Telegram channel; they do not ask for more.

## The four findings (the actual deliverable content)

Verbatim from the abstract, parent-reconstructed from raw JSON:

1. *"managers use visual and replayable tools, including captioned
   standard operating procedure videos, photo sequences, tablets, and
   workstation prompts, to reduce ambiguity and support self-paced
   rehearsal"* — **the one genuinely new design property.** The
   keepers are *workstation prompts* and *self-paced rehearsal*.
2. *"distributing short refreshers through messaging applications"* —
   **independent peer-reviewed validation of LE31's central
   architectural bet.** For 28 passes, Telegram-as-operational-
   interface rested on charter reasoning and low-star repos. This is a
   different class of evidence.
3. *"caption errors, English-first interfaces, limited device access,
   and unstable connectivity can turn digital tools from job resources
   into additional operational demands"* — **field evidence for
   features 53 and 66** (offline-first), which until now rested on
   first-principles argument. Also flags English-first interfaces as
   an active harm.
4. *"peer mentoring, WhatsApp micro-coaching, and protected off-peak
   practice"* — micro-coaching over messaging reinforces finding 2.
   **"Protected off-peak practice" has no LE31 analogue and no
   software surface** — recorded honestly as non-transferable.

**The most valuable output is validation, not novelty.** Findings 2
and 4 confirm decisions already made. Finding 3 upgrades an existing
argument from principle to evidence. Only finding 1 proposes something
LE31 does not have.

## Trigger for the next step

The first LE31 v2 feature delivering instructional or briefing content
to a cook — most likely an extension of feature 12 (pre-shift
briefing).

When that happens:

1. Read the full article, not just the abstract. **Check the
   limitations section and sample characteristics before leaning on
   any finding.**
2. **Answer the authoring question first.** If the owner has to author
   step sequences by hand, the feature does not ship.
3. **Check whether Telegram's own scrollback already satisfies
   "replayable".** The real gap may be *addressability* (jump to step
   3) rather than replayability — a much smaller change that could
   shrink this to nearly nothing.
4. Treat findings 2 and 4 as confirmation of existing architecture,
   not as a mandate for new surface.
5. Feed finding 3 into features 53 / 66 as field evidence.
6. Consider the locale question explicitly. Do not default to a single
   language.
7. Run `le31-conventions` on that feature independently. This artifact
   pre-authorises nothing.

## Verification protocol

Reference: `coding-agent/skills/le31-verification-protocol/SKILL.md`.

Documentary verification only, because there is no behaviour:

- [ ] `features/130-dhh-kitchen-accessible-operator-ux-visual-replayable.md`
      exists and was read back.
- [ ] DOI (`10.30892/gtg.67330-1842`), OpenAlex ID (`W7204185698`),
      journal name, and publication date (2026-08-25) match the raw
      JSON at
      `/tmp/le31-brainstorm-2026-08-28/openalex_phone-first20interface20restaurant.json`.
- [ ] **The count is FOUR patterns, not five.** This is the specific
      number the subagent got wrong; it must not be reintroduced.
- [ ] Quoted passages are verbatim from the **raw file**, reconstructed
      from `abstract_inverted_index`.
- [ ] `grep -c 'LE31'` on the raw OpenAlex file returns `0` —
      confirming the source contains no LE31-specific language, so any
      such phrasing in a summary is fabricated.
- [ ] The phrases "gloved-touch", "screen glare", and "hood lighting"
      appear **nowhere** in the contract — they were subagent
      inventions and must not propagate.
- [ ] `/opt/data/INDEX.md` has the pipeline row.
- [ ] Linear HMM-171 exists with label `Feature` and parent HMM-169.
- [ ] No source file, schema, or test was modified. No media stored.

## Rollback path

Delete
`features/130-dhh-kitchen-accessible-operator-ux-visual-replayable.md`,
delete
`specs/dhh-kitchen-accessible-operator-ux-visual-replayable-HANDOFF.md`,
remove the `/opt/data/INDEX.md` row, and cancel HMM-171.

**Rollback cost: zero.** Nothing depends on it, no schema was touched,
no behaviour changed.

## Open questions carried into the slice

- Does the constraint generalise beyond DHH staff? This agent's
  reading is that noisy-kitchen instruction failure is universal in
  degree, but **the paper does not make that claim** and the inference
  is unverified.
- **Who authors the step sequences?** The question most likely to kill
  any resulting feature.
- Does the Egyptian context transfer to Switzerland? Device
  availability, connectivity, staff language mix and labour structure
  all differ. **Unknown.**
- Is "replayable" already satisfied by Telegram scrollback? **Not
  evaluated.**
- Would completion tracking cross the charter §3.2 line? **Almost
  certainly yes if per-employee. Must be reviewed before proposal.**
- What do the study's own limitations say? **Full text unread.**
