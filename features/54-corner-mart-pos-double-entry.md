# Feature 54 — Corner-Mart-POS Single-Store Reference Watch (parking-lot)

> **Priority**: P3 · **Effort**: S (≤0.5 day, only if promoted from parking-lot) · **Source**: brainstorm 2026-08-10 (cross-section pick C, parking-lot) · **Bucket**: parking-lot (no build)
> **One-line**: A **parking-lot watch entry** for the canonical `htmx + SQLite + double-entry + single binary + no build` pattern for a single-store POS, exemplified by `channyeintun/corner-mart-pos` (pushed 2026-08-08T16:27:44Z, 0★). The reference exists so when the operator reports features 39 (`owner-daily-recap-telegram`) or 45 (`print-fallback-floor-sheet`) as inadequate, the path is documented and the reference fork is on file.

## Goal

LE31 already implements the *htmx + SQLite + double-entry + single binary + no build* pattern for the waiter UI (`index.html` mock-up, FastAPI server, SQLModel ORM, Postgres in production) and for the owner-facing reports (`index.html` mock-up, FastAPI server). Today's `channyeintun/corner-mart-pos` (pushed 2026-08-08T16:27:44Z, 0★, "Point-of-sale software for a single convenience store. Go and htmx, SQLite, double-entry accounting, Material Design 3 — one binary, two dependencies, no build step.") is a *clean Go reference* for this pattern. It does not add a new feature to LE31 — it documents an existing pattern so future maintainers (or a future v2 fork) have a canonical reference.

The pattern matters because:
- The single-binary + no-build approach is the simplest way to keep an LE31-style operator-facing surface installable on the operator's laptop without Docker, without a build step, and without a CI pipeline.
- The htmx + SQLite approach is the simplest way to keep an LE31-style reports surface *offline-capable* — the operator can open the reports on a plane.
- The double-entry approach is the simplest way to keep the owner's books *self-consistent* — every credit has a matching debit, and the books balance by construction.

`channyeintun/corner-mart-pos` is a parking-lot reference for LE31, not a buildable feature today. The pattern is *already implemented* in LE31 by the existing v1 surface; the only thing this feature adds is a *canonical external reference* so future maintainers can compare LE31's implementation against a known-good third-party implementation.

## Why parking-lot (not build)

**The reference is Go, not Python.** LE31's stack is Python 3.13 + FastAPI + SQLModel + Postgres (charter §3.2). A stack change requires an explicit charter decision; forking a Go reference into Python is a 3-day effort with marginal new value (LE31 already has a Python implementation of the pattern in `index.html` + FastAPI + SQLModel). The reference is therefore *watch-only*, not a *fork-target*.

**The pattern is already covered for LE31** by features 39 (`owner-daily-recap-telegram`) and 45 (`print-fallback-floor-sheet`). The htmx+SQLite+no-build pattern is what those features are built on; the `corner-mart-pos` reference would be a clean third-party example, but the *implementation* already exists in LE31's codebase.

**The JTBD is hypothetical.** "If LE31 ever wants a reference for owner-facing reports" is a v3-AI concern, not a v2 concern. The operator reports features 39 and 45 as adequate for v1; the next operator feedback cycle will tell us if the reports surface needs a clean rewrite (in which case `corner-mart-pos` becomes the reference). Until that feedback arrives, the reference sits in parking-lot.

## Evidence / JTBD

When a future maintainer (or a v2 fork) wants to understand the *canonical* `htmx + SQLite + double-entry + single binary + no build` pattern for a single-store POS, they want a clean third-party reference, but currently the only references in the LE31 codebase are the operator's own implementation (`index.html`, `backend/`), so that the `channyeintun/corner-mart-pos` reference (and its 0★ README) is parked as a watch entry, with a note that the pattern is *already implemented in LE31* and the reference is for *comparison*, not *adoption*.

## Scope

**In scope (parking-lot):**
- This file (`features/54-corner-mart-pos-double-entry.md`) — a parking-lot artifact documenting the reference, the pattern, and the conditions under which the reference would be promoted to a build.
- One Linear sub-issue (parking-lot label, status Backlog) — `HMM-?` — with the same content as this file's body.
- One HANDOFF slice (`specs/corner-mart-pos-double-entry-HANDOFF.md`) — frozen identifiers + the parking-lot conditions + the rollback path (which is "no code was written").
- One row in `/opt/data/le31_mmm3_research_work/INDEX.md` active pipeline table — picks 52/53/54.

**Out of scope (parking-lot):**
- No new code. No new Alembic migration. No new FastAPI endpoint. No new HTML mock-up.
- No fork of `corner-mart-pos` into the LE31 codebase. The reference is *external* (read-only).
- No rewrite of features 39 or 45. Both are accepted as adequate for v1.
- No promotion criteria for moving from parking-lot to a real feature. The criteria are documented in the HANDOFF ("when the operator reports feature 39 or 45 as inadequate"); no fixed date.

## Description (what the reference documents)

The `channyeintun/corner-mart-pos` reference documents:

1. **Single binary + no build**: the Go binary embeds the HTML templates, CSS, and JavaScript at compile time; the operator runs `./corner-mart-pos` and gets a web UI on `localhost:8080`. No Docker, no `npm install`, no `go build` for the operator. Translated to LE31, this is the *pyinstaller* path (a single `.exe` / single binary on the operator's laptop) — not currently in scope, but the pattern is on file.

2. **htmx + SQLite**: the server renders HTML fragments on every request; the database is a single-file SQLite. The operator can `cp corner-mart.db corner-mart.db.backup` and have a full backup. Translated to LE31, this is the *Postgres → SQLite fallback* path for v1 development (LE31 already supports SQLite in dev per `backend/README.md`); the pattern is on file.

3. **Double-entry accounting**: every transaction (sale, refund, void) is recorded as a balanced pair of debits and credits in a `journal_entries` table with `debit_account`, `credit_account`, `amount_cents`, `tx_id`. The books balance by construction (sum of debits = sum of credits for each transaction). Translated to LE31, this is the *tip-reconciliation* path (feature 05) — the tip is derived from `paid − consumed`, and the books balance because every payment has a matching consumption. The pattern is on file.

4. **Material Design 3**: the UI uses Material Design 3 components for a clean, modern look. Translated to LE31, this is the *waiter UI polish* path (the existing `index.html` mock-up uses a different design language); the pattern is on file as a reference if the operator ever wants to switch.

## Data model

No new data model. The parking-lot entry is a documentation artifact, not a code artifact.

## Implementation steps

1. **No implementation steps.** This is a parking-lot entry. The "implementation" is the artifact (this file, the HANDOFF, the Linear sub-issue, the INDEX row) and the *act of parking it*.

## Telegram interaction

No new Telegram interaction. No new cook-bot commands. No new waiter-side changes. The parking-lot entry is documentation-only.

## Dependencies

- No new dependencies. The parking-lot entry is a documentation artifact.
- If/when the reference is promoted to a real feature (see HANDOFF), the dependencies would be:
  - Existing `sqlmodel` (already a dep).
  - Existing `sqlalchemy` (already a dep).
  - Existing `pyinstaller` (already a dep via `pip` if needed).
  - Existing `htmx` (already a dep via the existing `index.html` mock-up).
  - No new packages for the documentation artifact itself.

## Failure / recovery

**No code = no failure modes.** The parking-lot entry is a documentation artifact; the only "failure" is that the reference becomes obsolete (e.g. `channyeintun/corner-mart-pos` is archived, or the pattern is superseded by a new approach). Recovery: re-evaluate the parking-lot entry on the next brainstorm; either remove the entry (if the pattern is no longer relevant) or update it (if a new reference has emerged).

## Definition of done

- This file is in the repo (`features/54-corner-mart-pos-double-entry.md`).
- The HANDOFF is in the repo (`specs/corner-mart-pos-double-entry-HANDOFF.md`).
- The Linear sub-issue is created (parking-lot label, status Backlog).
- The INDEX row is added (picks 52/53/54, parking-lot flag).
- The change is committed and pushed to `main`.

## Open questions

1. **Should the parking-lot entry be removed after 90 days if no operator feedback references it?** Lean: yes — the cron can clean up unused parking-lot entries to keep the feature backlog lean. The 90-day clock starts on the brainstorm date (2026-08-10); if no feedback arrives by 2026-11-08, the next brainstorm can either remove the entry or extend it for another 90 days.

2. **Should the parking-lot entry also reference `lbliii/chirp` (6★, 2026-08-09T19:04:31Z, "HTML-first web framework for Python 3.14+ with streaming, SSE, and fragment rendering") and `captain-shane/trcc` (2★, 2026-08-08T21:37:00Z, "TR Command Center — local-first Technical Request tracking with local-model AI. Server-rendered, SQLite-backed, no build step.")?** Lean: yes — both are stack-matches to LE31 (Python + htmx + SSE for Chirp; SQLite + server-rendered for trcc) and reinforce the same pattern. Add them to the "adjacent evidence" section of the HANDOFF (already done in the brainstorm report).

3. **Should the parking-lot entry promote itself to a real feature if features 39 or 45 are reported as inadequate?** Lean: yes — but only after the operator feedback arrives, not before. The HANDOFF lists the promotion criteria explicitly ("operator reports feature 39 or 45 as inadequate; operator asks for a clean third-party reference").

4. **Should the parking-lot entry also include a "what would a Python fork look like?" sketch?** Lean: as a follow-up, not in this entry. The sketch would be a 1-page code outline showing how to port the Go binary's pattern to Python (pyinstaller + FastAPI + SQLite). Defer until the parking-lot entry is promoted.

## Why this matters

LE31's existing moat is the **per-batch append-only `StockEntry` ledger paired with a Telegram cook surface** (feature 03 + 04). Features 39 and 45 implement the owner-facing surface (daily Telegram recap + printable floor sheet). The `channyeintun/corner-mart-pos` reference is the *canonical third-party example* of the pattern those features are built on.

The parking-lot entry exists so that when the operator does report feature 39 or 45 as inadequate — a hypothetical but plausible scenario — the path forward is documented and the reference fork is on file. The cost of parking it is zero (one Markdown file + one HANDOFF + one Linear sub-issue + one INDEX row). The benefit is that a future maintainer doesn't have to rediscover the canonical reference; they can read this file and the HANDOFF and immediately know what to do.

This complements features 39 (`owner-daily-recap-telegram`) and 45 (`print-fallback-floor-sheet`) by providing a *reference implementation* that those features can be compared against. If/when the operator reports either as inadequate, the parking-lot entry becomes the starting point for the rewrite — not a from-scratch invention.

## Promotion criteria (for moving from parking-lot to a real feature)

The parking-lot entry is promoted to a real feature when **all** of the following are true:

1. The operator reports feature 39 (`owner-daily-recap-telegram`) or feature 45 (`print-fallback-floor-sheet`) as inadequate (e.g. "the recap is too verbose", "the floor sheet doesn't include the prep board", "I want a printable PDF, not an HTML page").
2. The operator explicitly asks for a clean third-party reference (or the developer judges that a clean rewrite is the right path).
3. The team has the bandwidth for a 3-day Python re-implementation of the Go reference (the stack-mismatch is real; a port is required).
4. The team has reviewed the LE31 charter and confirmed that the change does not violate any invariants (no stack change without an explicit charter decision).

Until all four conditions are met, the parking-lot entry stays on file as a *reference*, not a *plan*.
