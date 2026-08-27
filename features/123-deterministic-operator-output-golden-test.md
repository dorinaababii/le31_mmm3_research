# Feature 123 — Deterministic operator-output golden testing

> **NEW observation (2026-08-27).** Documents in-window GitHub repo
> `nicholasrossi0530/escpos-render` (1★, 0 forks, MIT, Go, pushed
> 2026-08-24) from the 2026-08-27 daily research pass. The repo renders
> raw receipt-printer byte streams to deterministic JSON/text/PNG "so
> POS printing can be golden-tested in CI without hardware". Bucket:
> **v2 utility (technique reference)** — parking-lot defer.
>
> **The evidence here is the technique, not the repo's traction.** At
> 1★ / 0 forks the repo has no demand signal whatsoever, and per the
> standing pitfall (stars are not restaurant need) the star count is
> explicitly not offered as justification. This is the weakest of the
> three picks from 2026-08-27 and is recorded as such.

## Goal

Retain the **render-deterministically-then-golden-test** technique for
verifying operator-facing output, so that changes to what a cook or
waiter actually sees can be asserted mechanically instead of by a human
reading a device during service.

The artifact is the persistent technique reference. No code today.

## Scope

**In scope:**
- This contract file as the durable record of the technique and its
  source.
- One INDEX.md row in the active-feature-pipeline table.
- Applying the technique **when** LE31 next materially changes
  cook-bot ticket or recap rendering.

**Out of scope (v1 and today):**
- Any code, test, or CI change.
- **Any ESC/POS or thermal-printer support.** LE31's cook surface is a
  Telegram bot (charter §3.1). Physical receipt printing is not in v1
  and is not proposed here. Only the *technique* transfers.
- Any Go dependency. The referenced repo is Go; LE31 is Python 3.13.
  **The repo is a reference, never a dependency.**
- Any new library.
- Snapshot-testing whitespace or cosmetic formatting — see "Open
  questions" for why that is the failure mode to avoid.

## Description

### Source

- **Repo**: `nicholasrossi0530/escpos-render`
- **URL**: https://github.com/nicholasrossi0530/escpos-render
- **Stars / forks**: **1★ / 0 forks** (verified 2026-08-27 06:35 UTC)
- **Language**: Go
- **License**: MIT
- **Pushed**: 2026-08-24T18:39:38Z (in-window)
- **Description (verbatim)**: "A virtual ESC/POS printer: render raw
  receipt-printer byte streams to deterministic JSON, text, and PNG so
  POS printing can be golden-tested in CI without hardware"
- **Raw fetch**: `/tmp/le31-daily-2026-08-27/gh_search/gh_pos_go.json`

Surfaced in the `pos+language:go` query (31 in-window results, 3 with
≥1★, of which the other two were `Post`-substring false positives).

### The technique, stated generally

The repo's specific job is ESC/POS, which LE31 does not need. The
generalisable shape is:

1. Take the **exact byte stream / payload** that would go to the
   operator-facing output device.
2. Render it through a **deterministic** function into a comparable
   artifact (structured JSON, plain text, or an image).
3. **Commit that artifact as a golden file.**
4. In CI, re-render and diff. A rendering regression fails the build
   rather than surfacing to a human mid-service.

The load-bearing word is **deterministic**: the same input must produce
byte-identical output, or the golden file is useless and the test
becomes flaky — which historically leads to the test being disabled,
the worst possible outcome.

### The LE31 analogue

LE31's operator-facing outputs are:

- **Cook Telegram bot messages** — ticket text, inline keyboard markup,
  message entities. The Telegram send payload *is* the byte stream. The
  analogue of a virtual printer is snapshotting the exact payload
  (text + entities + `reply_markup`) that `aiogram` would send, without
  contacting Telegram.
- **Waiter web UI views** — server-rendered content.
- Any future owner recap or reconciliation summary.

So the technique maps cleanly onto the cook bot: build the message
payload, snapshot it, golden-test it. No Telegram API call, no device,
no Go, no ESC/POS.

### Why this is worth writing down (and why it is weak today)

**The case for:** LE31's cook bot is the surface where a formatting
regression is most costly and least likely to be caught by ordinary
tests. A unit test asserting an order contains three items passes
happily while the rendered ticket shows quantities in the wrong column
or drops a modifier. The cook discovers it during service. Golden
tests on the rendered payload close exactly that gap, and cost little
once the payload construction is already a pure function.

**The case against (honest):**

- **LE31's cook-bot messages are currently simple.** The value of
  golden testing scales with rendering complexity, and today there may
  not be enough complexity to justify it.
- **1★ / 0 forks is no demand signal at all.** The repo is one
  person's tool. It is cited for its idea, not its adoption, and it
  would be dishonest to present it otherwise.
- **Different domain and language.** ESC/POS thermal printing in Go
  versus Telegram messages in Python — only the shape transfers.
- **Snapshot tests have a well-known failure mode**: they become
  brittle, fail on every cosmetic change, and get deleted or
  `--update`-ed reflexively until they assert nothing. A brittle
  golden test is worse than no golden test, because it trains people
  to bypass a failing check.

Confidence: **low-medium**. Genuinely the weakest of the three picks
from 2026-08-27.

### Distinct from existing features

| Feature | What it does | How this pick differs |
|---|---|---|
| 67 `solo-operator-shift-journal-pwa` | operator shift journal | Product surface; not a testing technique |
| 91 `ezdmb-python-display-menu-board-watch` | menu-board display peer | Display product; no golden-test technique |
| 120 `geminka-agent-aiogram-3-telegram-premium-markup-pattern` | aiogram-3 rich-markup capability | *What* to render; this is *how to verify* what was rendered |
| 122 `trace-integrity-cait-acceptance-criterion` | acceptance criterion for assisted computation | Validates a computed number; this validates rendered output |
| 63 `visual-table-layout-v2` | table layout UI | Product surface |

No existing feature covers verification of rendered operator output.
Ripgrep-clean against features 1–120 by slug and by repo name.

## Data model

**None.** Zero tables, zero columns, zero rows, zero migrations. This
is test infrastructure; it touches no persisted state, and specifically
does not touch `StockEntry`, order state, or money.

## Implementation

1. **No implementation today.** The deliverable is this contract file.
2. **Trigger**: the next material change to cook-bot ticket rendering
   or introduction of an owner recap/summary output.
3. **When triggered (sketch, not a committed plan):**
   - Ensure payload construction is a pure function: order state in,
     message payload out, no I/O.
   - Snapshot the payload (text, entities, `reply_markup`) for a small
     set of representative orders.
   - Commit the snapshots; diff in CI.
   - **Scope the assertions to semantically load-bearing content** —
     item names, quantities, modifiers, totals, button actions — and
     **not** whitespace, emoji choice, or decorative separators.
4. **Explicitly do not:**
   - Add ESC/POS or printer support.
   - Add a Go dependency or vendor the referenced repo.
   - Snapshot entire message bodies verbatim if that makes the test
     fail on cosmetic edits.
   - **Weaken or delete a golden test to make CI green.** If a golden
     test fails, either the rendering regressed (fix it) or the change
     was intended (review the diff and update deliberately, with the
     diff read by a human). Reflexive `--update` is the failure mode
     that makes this technique worthless.

## Telegram interaction

None directly — this is test infrastructure. Indirectly it protects the
cook-bot surface: the intended effect is that a cook never sees a
malformed ticket because a golden test caught the regression in CI
first.

## Dependencies

- None. The technique is self-contained.
- Best sequenced *alongside* a rendering change rather than as
  standalone work, so the golden files are written against a
  deliberately-reviewed rendering rather than retrofitted onto one
  nobody re-examined.
- Complementary to feature 120 (aiogram-3 rich markup): if LE31 ever
  adopts richer markup, golden testing becomes more valuable, because
  richer rendering has more to regress.

## Open questions

- Is LE31's cook-bot rendering complex enough today to justify golden
  tests? **Probably not yet.** This is the main reason for the
  parking-lot verdict rather than a build verdict.
- Is cook-bot message payload construction currently a pure function,
  or is it interleaved with sending? If interleaved, the technique
  needs a small refactor first — which changes the cost calculus and
  should be assessed before committing.
- What granularity avoids brittleness? Asserting the full message body
  is brittle; asserting only item count is too weak to catch the
  regressions that matter. The right level is probably a structured
  projection of the payload, but this is undecided.
- Should the waiter web UI get the same treatment, or is that better
  served by ordinary integration tests against the DOM?
- Does LE31's CI currently run any test that would catch a cook-bot
  rendering regression? **Unknown — not verified in this pass.** If one
  already exists, this artifact adds little and should expire.

## Why this matters

LE31's charter is explicit that done means the operator flow was
actually exercised, not that tests passed. That principle has a gap:
the cook-bot ticket is the artifact the cook depends on, and "the
rendered output is exactly what we intended" is precisely the assertion
ordinary unit tests skip. Today that gap is closed by a human noticing
a broken ticket — during service, which is the worst time.

This repo's technique closes that gap mechanically and without hardware.
The idea is small, well-scoped, has no runtime cost, and adds no
dependency.

It is filed as **parking-lot defer**, not build, for three honest
reasons: LE31's rendering may not yet be complex enough to warrant it;
the source repo has no traction and is cited only for its idea; and a
badly-scoped golden test is actively harmful. It should be picked up
opportunistically when cook-bot rendering next changes materially, and
allowed to expire if that never happens.
