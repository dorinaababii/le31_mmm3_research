# Feature 130 — DHH kitchen accessible operator UX: visual and replayable

> **NEW observation (2026-08-28).** Documents in-window peer-reviewed
> article `10.30892/gtg.67330-1842` — "How do restaurant managers
> utilize digital training tools for deaf and hard-of-hearing
> employees?" (2026-08-25, *GeoJournal of Tourism and Geosites*) from
> the 2026-08-28 brainstorm pass.
> Bucket: **v2 owner-pains (UX reference)** — watch-list defer. Zero
> build time today.
>
> **This is the highest evidence grade in the 29-pass series.** Not a
> preprint and not a 1★ repo: a peer-reviewed qualitative study of
> **30 restaurant managers** using a named method (job
> demands-resources model, reflexive thematic analysis), studying
> operational instruction delivery in **noisy, fast-paced kitchens
> under service pressure** — LE31's exact operator surface.
>
> **Two of its four findings validate architectural choices LE31 has
> already made.** That is the more valuable outcome than a new
> feature: it is the first external, real-operator evidence that
> messaging-app-as-operational-interface is how instruction actually
> reaches kitchen staff.

## Goal

Retain the **visual-and-replayable operator instruction** discipline,
and the study's four field-observed patterns, as design input for the
first LE31 v2 feature that delivers operational instruction to a cook.
The paper answers: *how does operational instruction actually reach
kitchen staff who cannot rely on spoken or live direction, in a real
kitchen, under real service pressure?*

## Scope

**In scope:**
- This contract file as the durable record of the study, its four
  patterns, and the two LE31 architectural bets it independently
  validates.
- One INDEX.md row in the active-feature-pipeline table.
- A bounded read of the full article (not just the abstract) **at the
  point when** a v2 feature first delivers instructional or
  briefing content to a cook.
- Recording the study as **field evidence** supporting the
  offline-first work already filed as features 53 and 66, which to
  date has been argued from first principles rather than evidence.

**Out of scope (v1 and today):**
- Any code. No step-sequence model, no media storage, no captioning
  pipeline, no schema change, no migration.
- Any accessibility-compliance programme. This artifact is **not** a
  claim that LE31 is or should be certified accessible, and does not
  commit LE31 to any accessibility standard. Reading a study about
  DHH employees as a design input is different from claiming
  conformance.
- Any content authoring. The study's own finding is that adapting
  instructional material is *managerial labour* ("bricolage"), not a
  software feature. **LE31 must not push authoring burden onto a
  solo owner**; any future feature has to solve authoring or not
  ship.
- Any video pipeline. The study's managers use captioned SOP videos;
  LE31 has no video surface and adding one is not implied here.
- Any change to charter §3.2. The study population is *employees*;
  LE31 records no staff PII beyond what v1 already does, and this
  artifact proposes no new identifying field.
- Any new dependency.

## Description

### Source

- **DOI**: `10.30892/gtg.67330-1842`
- **OpenAlex ID**: `W7204185698`
- **Published**: 2026-08-25 (in-window)
- **Journal**: *GeoJournal of Tourism and Geosites* (peer-reviewed)
- **Title**: "HOW DO RESTAURANT MANAGERS UTILIZE DIGITAL TRAINING
  TOOLS FOR DEAF AND HARD-OF-HEARING EMPLOYEES?"
- **Population**: 30 restaurant managers, Egypt
- **Method**: interpretive qualitative study; job demands-resources
  (JD-R) model; reflexive thematic analysis
- **Raw fetch**: `/tmp/le31-brainstorm-2026-08-28/openalex_phone-first20interface20restaurant.json`
- **Abstract provenance**: reconstructed by the parent agent from
  `abstract_inverted_index` in the raw JSON. **The subagent's
  rendering of this abstract was fabricated in part** — it invented
  a closing clause referencing "the LE31 hands-busy, phone-first
  operator surface", claimed "five recurring practices" where the
  paper reports **four**, and invented barriers ("gloved-touch
  interfaces, screen glare under hood lighting") that do not appear
  in the source. `grep -c 'LE31'` on the raw file returns **0**.
  Everything below is from the parent's reconstruction. See the
  report's Blocker 1.

### Verbatim observations from the abstract

The problem statement:

> "Restaurants increasingly rely on digital training; however, deaf
> and hard-of-hearing (DHH) employees still face barriers in noisy,
> fast-paced kitchens where spoken instruction is difficult to
> follow."

The four patterns, verbatim:

> "First, managers use visual and replayable tools, including
> captioned standard operating procedure videos, photo sequences,
> tablets, and workstation prompts, to reduce ambiguity and support
> self-paced rehearsal."

> "Second, they engage in managerial bricolage by localizing
> corporate materials, improving Arabic captions, simplifying task
> steps, and distributing short refreshers through messaging
> applications."

> "Third, caption errors, English-first interfaces, limited device
> access, and unstable connectivity can turn digital tools from job
> resources into additional operational demands."

> "Fourth, peer mentoring, WhatsApp micro-coaching, and protected
> off-peak practice help convert digital content into confidence,
> task mastery, and psychologically safer learning."

And the framing contribution:

> "The findings extend hospitality disability employment research by
> shifting attention from hiring and inclusion climate to the
> day-to-day learning architecture through which inclusion is
> enacted in mainstream restaurants."

### What transfers to LE31, finding by finding

**Finding 1 — visual and replayable, at the workstation, self-paced.**
LE31's cook surface is already text-and-photo over Telegram. What
LE31 has never named as a design property is *replayable at the
cook's own pace at the workstation*. "Workstation prompts" and
"self-paced rehearsal" are the two phrases worth keeping. A cook who
can re-read step 3 without asking anyone, mid-service, without
losing their place, is a different experience from one who received
a message once.

**Finding 2 — messaging applications are the actual distribution
channel.** The study's managers distribute short refreshers *through
messaging applications*. This is independent, peer-reviewed,
real-operator validation of LE31's central architectural bet
(Telegram-bot-as-operational-interface). For 28 passes that bet has
been supported by charter reasoning and by low-star GitHub repos
doing something similar. This is a different class of evidence. It
changes nothing about what LE31 builds and raises confidence that
what LE31 already decided is right.

**Finding 3 — connectivity and device access can invert the value of
the tool.** Named failure mode: "limited device access, and unstable
connectivity can turn digital tools from job resources into
additional operational demands." LE31 is Telegram-dependent by
design, which means this failure mode applies to LE31 directly. This
is **field evidence for the offline-first work in features 53 and
66**, which until now rested on first-principles argument. Also
named: "English-first interfaces" as an active harm — relevant to a
multilingual Swiss kitchen where staff may not share the owner's
primary language.

**Finding 4 — micro-coaching through messaging, and protected
off-peak practice.** "WhatsApp micro-coaching" is one of four
load-bearing patterns, reinforcing finding 2. "Protected off-peak
practice" is the one pattern with **no LE31 analogue and no obvious
software surface** — it is a scheduling and management practice, not
a feature. Recorded honestly as non-transferable.

### Honest assessment of strength

- **Highest evidence grade in the series, and still n=1.** Peer
  reviewed, named population, named method — materially stronger
  than the preprints and 1–2★ repos that make up most picks. But it
  is a single study in a single national context (Egypt), and
  kitchen practice, device availability, connectivity and language
  politics all differ in Switzerland. Confidence **medium-high for
  the findings as reported**, **medium for transfer to LE31's
  context**.
- **Population mismatch to be stated plainly.** The study is about
  **DHH employees specifically**. LE31 has no reported DHH staff and
  no accessibility requirement on file. The reason the findings
  transfer is that the *constraint* the study examines — spoken and
  live instruction being unreliable in a noisy, fast-paced kitchen —
  is a constraint **every** cook in **every** busy kitchen faces to
  some degree. That generalisation is an inference by this agent,
  not a claim the paper makes. It is a reasonable inference and it
  is still an inference.
- **Its most useful output is validation, not novelty.** Findings 2
  and 4 confirm decisions LE31 already made. Finding 3 upgrades an
  existing argument from principle to evidence. Only finding 1
  proposes something LE31 does not have.
- **The hard part is authoring, and the study says so.** "Managerial
  bricolage" is the study's own word for the labour of adapting
  material. A solo owner does not have a training department. Any
  LE31 feature that requires authored step sequences must solve
  authoring first or it will not be used.
- **Full text unread.** Only the abstract has been read. The four
  patterns are as-reported; the supporting detail, sample
  characteristics and limitations are unknown.

### Distinct from existing features

| Feature | What it does | How this pick differs |
|---|---|---|
| 09 `kitchen-delay-visibility` | Surfaces kitchen delay to the floor | Delay signalling; this is instruction delivery |
| 12 `pre-shift-briefing` | Pre-shift briefing content | **Closest neighbour** — briefing is pre-service and one-directional; this is replayable mid-service self-paced rehearsal |
| 21 `recipe-generation` | Generates recipe content | Content generation; this is delivery modality and replayability |
| 32 `solo-operator-floor-pin` | Solo-operator floor pin | Floor-state surface; this is instructional |
| 53 `zentra-offline-first-fb-pattern` | Offline-first F&B pattern | **This study is field evidence for it** — no overlap, it strengthens 53 |
| 65 `cook-photo-stock-list-pwa` | Photo-driven stock capture | Cook *inputs* a photo; this is cook *consuming* a visual sequence |
| 66 `offline-first-pwa-transactional-arch` | Offline-first transactional architecture | **This study is field evidence for it** — strengthens 66 |
| 67 `solo-operator-shift-journal-pwa` | Shift journal PWA | Journalling; this is instruction |

Ripgrep-clean against features 1–129 by slug, by DOI, by OpenAlex ID
(`W7204185698`), and by concept terms — `deaf`, `hard-of-hearing`,
`captioned`, `visual-first`, `noisy kitchen`, `step-card` all return
zero matches. (`replayable` matches only features 61 and 122, both
in an audit-trail sense, not a UX sense.)

## Data model

**None today.** Zero tables, zero columns, zero rows, zero
migrations.

If and when a v2 feature delivers replayable instruction, the
mechanism would imply (not decided, not designed):

- an ordered step-sequence concept (steps belonging to a task, with
  stable ordering and an optional photo per step);
- addressable steps, so a cook can jump to step 3 rather than
  scrolling a message history;
- a locale field on step text, given the study's finding that
  English-first interfaces are an active harm;
- **no** completion tracking or per-employee performance record
  without an explicit charter §3.2 review — that would be a new
  identifying surface and is out of scope here.

These are sketches for a future decision, deliberately not specified
here. The **authoring** question is the load-bearing one and is
unresolved.

## Implementation

1. **No implementation today.** The deliverable is this contract
   file.
2. **Trigger for the next step**: the first LE31 v2 feature that
   delivers instructional or briefing content to a cook — most
   likely an extension of feature 12 (pre-shift briefing).
3. **When triggered**:
   - Read the full article, not just the abstract. Check the
     limitations section and the sample characteristics before
     leaning on any finding.
   - **Answer the authoring question first.** If a solo owner has
     to author step sequences by hand, the feature does not ship.
   - Treat findings 2 and 4 as confirmation of the existing Telegram
     architecture, not as a mandate for new surface.
   - Feed finding 3 into features 53 / 66 as field evidence.
   - Consider the locale question explicitly; do not default to a
     single language.
   - Run `le31-conventions` on the concrete v2 feature. This
     artifact pre-authorises nothing.
4. **If no v2 instructional surface appears**, this artifact expires
   as a UX reference — but findings 2 and 3 retain standalone value
   as validation of existing decisions, which is worth keeping on
   file regardless.

## Telegram interaction

None today. Findings 2 and 4 are directly about LE31's existing
Telegram channel: the study's managers use messaging apps to
distribute short refreshers and to micro-coach. If a v2 instruction
feature is ever built, Telegram is — per this study's field evidence
— the right channel, and the design question is *addressability and
replayability within it*, not whether to use it.

## Dependencies

- None today.
- Strengthens features 53 and 66 (offline-first) with field
  evidence rather than depending on them.
- Closest design neighbour is feature 12 (pre-shift briefing); a
  future instruction feature would most likely extend it.
- No hard prerequisite. This artifact stands alone as a reference.

## Open questions

- Does the constraint generalise beyond DHH staff? This agent's
  reading is that noisy-kitchen instruction failure is universal in
  degree, but **the paper does not make that claim** and the
  inference is unverified.
- **Who authors the step sequences?** The study's answer is
  "managers, through bricolage". LE31's owner is one person running
  a restaurant. This is the question most likely to kill any
  resulting feature.
- Does the Egyptian context transfer to Switzerland? Device
  availability, connectivity, staff language mix and labour
  structure all differ. **Unknown.**
- Is "replayable" already satisfied by Telegram's own message
  history? A cook can scroll back today. The gap may be
  *addressability* (jump to step 3) rather than replayability as
  such — a much smaller change. **Not evaluated, and it could
  shrink this to nearly nothing.**
- Would any completion tracking cross the charter §3.2 line? Almost
  certainly yes if it is per-employee. **Must be reviewed before
  any such field is proposed, not after.**
- What do the study's own limitations say? **Full text unread.**

## Why this matters

For 28 passes, LE31's central architectural bet — that a messaging
bot is the right operational interface for kitchen staff — has been
supported by internal reasoning and by other people's low-star side
projects. This study is a peer-reviewed examination of 30 real
restaurant managers finding that messaging applications are, in
practice, how operational instruction reaches kitchen staff, and
that micro-coaching over messaging is one of four load-bearing
patterns. That is worth recording independently of whether any
feature ever comes from it.

It also names, from the field, the failure mode LE31 is most exposed
to: unstable connectivity and limited device access flipping the
tool from a resource into an operational demand. LE31's offline-first
thinking (features 53, 66) has been a first-principles argument. It
now has evidence.

The one genuinely new design property — visual instruction that is
replayable and addressable at the cook's own pace at the workstation
— is plausible and unproven, and it is gated behind an authoring
problem the study itself describes as managerial labour.

The recommendation is **defer, not build**: highest-confidence pick
of the pass on evidence grade, still a single study in a single
national context, with its most actionable idea blocked on an
unsolved authoring question. If v2 never ships an instructional
surface, findings 2 and 3 remain valuable as validation and the rest
of this artifact expires.
