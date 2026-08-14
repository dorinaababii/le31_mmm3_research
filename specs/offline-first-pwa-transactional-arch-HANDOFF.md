# offline-first-pwa-transactional-arch — HANDOFF

> **Slice for the coding agent.** Read this *and*
> `features/66-offline-first-pwa-transactional-arch.md` before
> touching any code. Do not paste chat excerpts back into the build.

## Frozen identifiers (do not rename)

- Feature ID: `66`
- Slug: `offline-first-pwa-transactional-arch`
- Contract file: `features/66-offline-first-pwa-transactional-arch.md`
- Bucket: **v2 owner-pains (resilience experiment)** (same
  bucket as features 49 + 53)
- Linear parent: `HMM-77` (Brainstorm 2026-08-14 — daily)
- Linear sub-issue: `HMM-81` (see `le31 v1 — Core MVP` project,
  label `Feature`; matches the v2 owner-pains sub-issue convention
  used by features 58/61/62/63)

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md`. Evidence precondition:
**observed** (Nugraha et al. 2026-08-10, *bit-Tech* 9(1):4044,
doi:10.32877/bt.v9i1.4044, diamond-OA — the single strongest
academic anchor for the offline-first transactional pattern in
this pass; corroborating `gaganjainse/ClinicLedger` Kotlin 1★
2026-07-15; corroborating `Sreenivas-Sadhu-Prabhakara/shelftrack`
HTML PWA MIT 2026-07-15 + 2026-08-14). Confidence: **high**.

**Decision: experiment (v2 owner-pains resilience experiment,
S effort, ≤2 days).** The slice boundary is hard: one Markdown
file + zero source code changes. The slice ships a design doc,
not an implementation. Circuit breaker: delete the
`docs/offline-first-architecture.md` file; no other code changes
to revert.

## Mandatory LE31 skill list (load these first)

External coding agent MUST load before starting:

1. `le31-conventions` (project invariants + the seven-check gate).
2. `le31-v1-feature-pattern` (canonical contract shape + slicing
   rules; even though this is v2 owner-pains, the slicing
   discipline inherits).
3. `le31-handoff-spec` (frozen-contract discipline; mirror
   contract back).
4. `le31-daily-brainstorm` (this pick came from the daily
   brainstorm job on 2026-08-14).
5. `le31-feature-pipeline` (so the agent understands how this
  slice will be sequenced after it ships).

If the destination repo does not yet ship these skills, request
them from the research-side Hermes instance before writing code.

## Files the slice touches

```
docs/offline-first-architecture.md                       # NEW (≤500 words)
INDEX.md                                                 # EDIT: append one row to "Active feature pipeline" table
```

Zero source files touched. Zero migrations. Zero new config
keys. Zero new pip dependencies.

## Design doc shape (spec for the coding agent)

`docs/offline-first-architecture.md` is a single Markdown file
with three sections, in order:

### Section 1 — Nugraha et al. pattern summary (≤100 words)

Cite the paper: Nugraha, Somantri, Rofiqi (2026-08-10).
*Implementation of an Offline-First Progressive Web App
Architecture for Transactional System Resilience.* bit-Tech
9(1):4044. doi:10.32877/bt.v9i1.4044.

Summarize the four-component pattern:
1. **Local cache** — every operational surface has a local
   write-ahead log that survives network drops.
2. **Sync queue** — the local cache flushes to the server when
   the network returns; the queue is durable across restarts.
3. **Idempotency keys** — every write carries a client-generated
   unique id; the server uses the id to deduplicate retries.
4. **Reconciliation** — when the server's view diverges from
   the local cache, the server emits a reconciliation event
   that the local cache surfaces to the operator.

### Section 2 — Mapping table

| Nugraha component | LE31 surface today | Gap |
|---|---|---|
| Local cache | feature 53's IndexedDB replay queue (waiter side); absent on cook side | cook side |
| Sync queue | feature 53's flush-on-reconnect (waiter side); Telegram bot's request/response on cook side | cook-side sync queue |
| Idempotency keys | absent | **smallest next experiment** |
| Reconciliation | absent; manual via feature 39 daily-recap | reconciliation event surface |

### Section 3 — Smallest next experiment paragraph

Identify the **transactional idempotency key** as the next
concrete slice, scoped to the **cook bot photo upload flow
from feature 65** (the natural place where "same photo
uploaded twice during a network retry" becomes a real-world
problem).

The paragraph names:
- The specific surface (cook bot `/stock-snap` photo upload).
- The specific shape (idempotency key: client-generated UUID
  attached to each `create_stock_entry_from_photo` call;
  server-side dedup table; one row per key).
- The expected size (S effort, ≤3 days, build candidate).
- The expected outcome (network-retry of a photo upload does
  not create a duplicate `StockEntry` row).

## Verification protocol reference

Per `le31-conventions` "Verification" pattern. The coding agent
MUST:

1. Create `docs/offline-first-architecture.md` with the three
   sections above.
2. Confirm the doc is ≤500 words (`wc -w docs/offline-first-architecture.md`).
3. Add one row to `INDEX.md` "Active feature pipeline" table
   for pick 66 (date, pick, bucket, feature path, Linear ID,
   handoff).
4. Confirm zero source files touched:
   `git diff --stat HEAD~1..HEAD -- backend/ bot/ specs/`
   should be empty.
5. No tests; no migrations; no config changes.

## Rollback / feature-removal path

1. Delete `docs/offline-first-architecture.md`.
2. Remove the pick 66 row from `INDEX.md` "Active feature
   pipeline" table.
3. (No source code to revert.)

Estimated rollback cost: ≤5 minutes.

## Files for the coding agent to verify against

```
features/66-offline-first-pwa-transactional-arch.md
specs/offline-first-pwa-transactional-arch-HANDOFF.md       (this file)
features/03-kitchen-stock-tracker.md                       (mapped surface)
features/04-menu-photo-bot.md                             (mapped surface)
features/49-postledger-tamper-evident-hash.md              (mapped surface)
features/53-zentra-offline-first-fb-pattern.md             (composed surface)
features/65-cook-photo-stock-list-pwa.md                   (smallest-next-experiment target)
skills/le31-conventions/SKILL.md
skills/le31-v1-feature-pattern/SKILL.md
skills/le31-handoff-spec/SKILL.md
PROJECT_CHARTER.md
```
