# telegram-commerce-anchor — HANDOFF

> **Slice for the research agent.** This is a passive peer-observation research-note of the **in-window `indmdev` Telegram-commerce 3-pack** — the **highest in-window Python repo on the `topic:telegram-bot` topic by 4×** (Free-Telegram-Store-Bot ★153, pushed 2026-08-22, with sibling repos Telegram-Store-MiniApp ★38 + indmshopbot ★33). The slice boundary is hard: zero source-file edits, zero schema changes, zero new config keys. Read this *and* `features/98-telegram-commerce-anchor.md` before touching any code. Do not paste chat excerpts back into the build.

## Frozen identifiers (do not rename)

- Feature ID: `98`
- Slug: `telegram-commerce-anchor`
- Contract file: `features/98-telegram-commerce-anchor.md`
- Bucket: **v2 owner-pains (parking-lot, peer observation)** — hard defer pending charter §3.1 surface-expansion review
- Linear parent: **HMM-125** (Brainstorm 2026-08-22 — daily, created in this cron)
- Linear sub-issue: **HMM-128** (Feature label, project `le31 v1 — Core MVP` per le31-feature-pipeline SKILL.md nonexistent-`le31 v2 owner-pains` correction)

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md`. Evidence precondition: **observed** (verified in-window via GitHub `topic:telegram-bot` + `topic:real-time` searches at 2026-08-22 06:44 UTC with PAT `Authorization: Bearer $HERMES_GITHUB_TOKEN`; 3 indmdev repos identified).

**Confidence:** **high** for the adoption signal (★153 is the highest in-window Python repo on the telegram-bot topic by 4×); **low** for the build implication (charter §3.1 — two primary operational surfaces only; commerce is a third surface not in v1/v2; no observed LE31-owner demand for commerce).

**Decision: parking-lot; hard defer pending charter §3.1 surface-expansion review.** The indmdev cluster proves that "Telegram as a commerce surface" is production-viable at scale with the same Python+aiogram v3 stack LE31 uses. The re-evaluation trigger is **charter-level scoping** — revisit when (i) LE31 owner explicitly asks for commerce, OR (ii) indmdev ships a public API surface that LE31 could integrate against, OR (iii) a second in-window Python commerce-stack repo crosses ≥50★.

## Mandatory LE31 skill list (load these first)

External research agent MUST load before starting:

1. `le31-conventions` (project invariants + the seven-check gate; specifically charter §3.1 — two primary operational surfaces).
2. `le31-v1-feature-pattern` (canonical contract shape + slicing rules).
3. `le31-handoff-spec` (frozen-contract discipline; mirror contract back).
4. `le31-daily-brainstorm` (this pick came from the daily brainstorm job on 2026-08-22).

If the destination repo does not yet ship these skills, request them from the research-side Hermes instance before writing code.

## Files the slice touches

```
features/98-telegram-commerce-anchor.md            # NEW (this artifact)
specs/telegram-commerce-anchor-HANDOFF.md           # NEW (this file)
INDEX.md                                             # EDIT: append one row to "Active feature pipeline" table (parking-lot continue entry)
```

Zero source-file edits outside the research artifacts. Zero schema changes. Zero new config keys.

## Verification protocol

After the artifact ships:

1. **Read back** `features/98-telegram-commerce-anchor.md` and confirm it matches the daily-brainstorm report's "telegram-commerce-anchor" pick description (Pick C section).
2. **Read back** the new row in `INDEX.md` "Active feature pipeline" table and confirm the date (2026-08-22), pick slug (`telegram-commerce-anchor`), feature path (`features/98-telegram-commerce-anchor.md`), and Linear sub-issue ID (HMM-128).
3. **On the next daily-research pass**:
   a. Direct-repo GETs on all 3 indmdev repos via `curl -sS -H "Authorization: Bearer $HERMES_GITHUB_TOKEN"`:
      - `https://api.github.com/repos/indmdev/Free-Telegram-Store-Bot`
      - `https://api.github.com/repos/indmdev/Telegram-Store-MiniApp`
      - `https://api.github.com/repos/indmdev/indmshopbot`
   b. Verify the **license** on each repo (charter §3.2 — MIT/Apache allowed; GPL/AGPL blocks import). Update the "Open questions" section of `features/98-telegram-commerce-anchor.md` with the license finding.
   c. Read the Free-Telegram-Store-Bot README via `curl -sS https://raw.githubusercontent.com/indmdev/Free-Telegram-Store-Bot/main/README.md` to confirm the "100% Free Shop Bot" model + MiniApp + bot architecture.
   d. Track star velocity + push activity + Python/aiogram version + dependency footprint on each repo.
   e. Update `features/98-telegram-commerce-anchor.md` with the README-confirmed primitives.
4. **No build implied.** The pick is a peer-observation research-note. The re-evaluation trigger is **charter-level scoping** (LE31 owner explicitly asks for commerce, OR indmdev ships a public API, OR a second in-window Python commerce-stack repo crosses ≥50★) — not a build decision.

## Linear sub-issue

Create a Linear sub-issue in project **`le31 v1 — Core MVP`** (per le31-feature-pipeline SKILL.md nonexistent-`le31 v2 owner-pains` correction — the canonical v2 owner-pains bucket does not exist) with label `Feature`.

- Title: `Feature 98 — telegram-commerce-anchor`.
- Body: the contract from `features/98-telegram-commerce-anchor.md` (or a short summary + the file path).
- Parent: **HMM-125** (Brainstorm 2026-08-22 — daily).
- Status: `Backlog`.

## Rollback path

Delete `features/98-telegram-commerce-anchor.md` and this HANDOFF.md. Remove the corresponding row from `INDEX.md`. No other code changes to revert. No data migration to revert.

## Why this matters (for the research agent)

The indmdev 3-repo commerce stack **proves that "Telegram as a commerce surface" is production-viable at scale** with the **same Python+aiogram v3 stack LE31 uses**. The cross-section is direct: LE31's cook-Telegram-bot surface (features 33/41/43/56/60) and owner-recap surface (features 39/57/69) all live on the same Telegram surface that indmdev proves can support commerce at ★153. The pattern informs a **charter-level scoping question** ("should LE31 v2 add Telegram-commerce semantics?") — but no build implied today. Filed as a parking-lot peer-observation with a clear re-evaluation trigger: charter-level scoping review.

## Carry-over history

This is the **NEW observation** (2026-08-22); no prior artifact exists. Combines:

- The 3 in-window `indmdev` repos (Free-Telegram-Store-Bot ★153 + Telegram-Store-MiniApp ★38 + indmshopbot ★33, all pushed 2026-08-22).
- The 22-pass observation that the LE31-target cook-Telegram-bot surface is at ★40 (Pronto) and below.
- The cross-section with features 33, 41, 43, 56, 60 (cook-Telegram-bot surface) + features 39, 57, 69 (owner-recap surface) + features 90, 94 (Pronto peer at ★40).
- The charter §3.1 surface-expansion question ("should LE31 v2 add a commerce/MiniApp surface?") that this artifact explicitly defers.

## Sources

- **GitHub `topic:telegram-bot` + `topic:real-time`** (searches verified at 2026-08-22 06:44 UTC; PAT `Authorization: Bearer $HERMES_GITHUB_TOKEN`).
- Raw responses:
  - `/tmp/le31-brainstorm-2026-08-22/gh_topic_telegram-bot.json` (173,365 bytes)
  - `/tmp/le31-brainstorm-2026-08-22/gh_topic_real-time.json` (182,111 bytes)
- 3 indmdev repos verified via raw GitHub API responses (item ids for each — see raw JSON for full IDs).
- Full report: `/opt/data/le31-brainstorm-2026-08-22.md` (Pick C section, lines 109–121).
- Linear parent: HMM-125 (Brainstorm 2026-08-22 — daily, status Done).
- Linear sub-issue: HMM-128 (Feature label, status Backlog, parent HMM-125).