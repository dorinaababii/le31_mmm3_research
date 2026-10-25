# drsamonline-canteen-lan-mit-javascript-lan-offline-first-restaurant-single-file-order-from-the-table-over-the-room-own-wifi-v1-local-network-ordering-surface-vocabulary — HANDOFF

> **Slice for the coding agent.** Read this *and*
> `features/376-drsamonline-canteen-lan-mit-javascript-lan-offline-first-restaurant-single-file-order-from-the-table-over-the-room-own-wifi-v1-local-network-ordering-surface-vocabulary.md`
> before touching anything. **This is a WATCH-LIST / ARCHITECTURE-
> REFERENCE slice, NOT a build slice.** There is no code deliverable.
>
> **This slice does NOT authorise offline mode, LAN mode, a client-side
> cache, an outbox, or a third surface.** It proposes **one sentence**
> of documentation (the connectivity boundary) and nothing else.

## Frozen identifiers (do not rename)

- Feature ID: `376`
- Slug: `drsamonline-canteen-lan-mit-javascript-lan-offline-first-restaurant-single-file-order-from-the-table-over-the-room-own-wifi-v1-local-network-ordering-surface-vocabulary`
- Contract file: `features/376-drsamonline-canteen-lan-mit-javascript-lan-offline-first-restaurant-single-file-order-from-the-table-over-the-room-own-wifi-v1-local-network-ordering-surface-vocabulary.md`
- Bucket: **v1 (connectivity-boundary vocabulary)** — defer
- Linear parent: **not created — Linear MCP write endpoint blocked (38th consecutive day), requestId `a4ff44223faad34e`**
- Linear sub-issue: **not created — same blocker**. Intended payload at `/opt/data/le31-daily-research-2026-10-25.linear-fallback.json`
- Source repo: GitHub `drsamonline/canteen-lan` (MIT), ★1/⑂0, 39 KB, JavaScript, created 2026-10-23T01:29:25Z, pushed 2026-10-24T15:09:22Z
- Raw fetch: `/tmp/le31-daily-2026-10-25/pv/drsamonline__canteen-lan.json`
- Report: `/opt/data/le31-daily-research-2026-10-25.md`

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md`.

**Evidence precondition: inferred.** The artifact exists and is real
(direct `/repos/` GET, HTTP 200, in-window by both `created_at` and
`pushed_at`). **But no LE31 owner, waiter, or cook has reported
connectivity, offline, or LAN pain.** The existence of an
independently-built LAN-only ordering board is evidence that the
*venue profile* exists in the world — **not** evidence that LE31's
owner has that pain.

**Confidence: high** for the artifact's existence and shape (direct
API read, MIT licence verified, 39 KB, four topics including `lan`
and `offline-first`). **Low** for how common the venue profile is
among LE31's addressable venues — **no evidence is claimed either
way, and the naming is justified by cost (one sentence), not by
frequency (unknown).**

**Decision: defer (vocabulary reference).** Check 1 (JTBD) **fails**:
LE31's owner has never asked for offline or LAN-connectivity
support, and there is no reported pain to attach the proposal to.
Checks **2** and **4** also fail: a second ordering surface is a §3.1
surface-count question, and a LAN-only ordering surface directly
contradicts §3.2's online-only, server-authoritative VPS posture.

**Known rabbit hole:** treating "the LAN-only venue exists as a
software category" as "the LAN-only venue is a market LE31 should
chase". **No market claim is made.** The artifact's job is to *name
an exclusion*, not to argue for an inclusion.

**Circuit breaker:** if the boundary sentence is never added and the
owner is never asked about internetless venues, this remains an
unused reference. **Acceptable outcome.** The cost of the artifact
is one file.

## Mandatory LE31 skill list (load these first)

1. `le31-conventions` — project invariants + the seven-check gate.
2. `le31-research` — research observation discipline; no fabrication.
3. `le31-daily-research` — this pick came from the 2026-10-25 pass.
4. `le31-feature-pipeline` — how this slice is sequenced.
5. `le31-handoff-spec` — the frozen-contract discipline this slice follows.

If the destination repo does not ship these skills, request them
from the project owner before starting. **Do not invent LE31
conventions.**

## Files to touch

| File | Action | Notes |
|---|---|---|
| `features/376-…-v1-local-network-ordering-surface-vocabulary.md` | (already written) | the contract; no further edit needed today |
| `/opt/data/INDEX.md` | append | one pipeline row (done in this pass) |

**No source file is touched. No test is added. No migration is
written. No UI is built. No LAN server is written.**

## What the coding agent must NOT do

- **Do not build offline mode, LAN mode, a client-side cache, an
  outbox, idempotent sync, service-worker logic, mDNS/Bonjour, or any
  local-network discovery.** LE31 v1 is a single server-authoritative
  VPS reached over the internet (§3.2). This slice does not change that.
- **Do not port `canteen-lan`'s code.** It is MIT and small, so the code
  is legally adoptable — but adopting it would be a JavaScript LAN
  server inside a Python/FastAPI/Postgres product, which is a §3.2
  stack change requiring an explicit charter decision. **The artifact
  is cited, not ported.**
- **Do not add a guest-facing ordering surface, a table board, or a QR
  menu.** §3.1 says two surfaces; feature 11 already covers the QR menu.
- **Do not edit the charter, `le31-conventions`, or `PROJECT_CHARTER.md`.**
  This artifact *proposes* a one-sentence boundary; it does not *make*
  it. Charter edits are infrequent and deliberate, and per the
  2026-10-24 pick precedent a charter edit is an **owner decision**.
- **Do not re-litigate offline mode.** Feature 373
  (`ramaraihan12/warung-pos`) already holds the offline-first POS
  vocabulary. This slice must not duplicate it.

## The proposed boundary (the actual deliverable content)

If and when the charter or `le31-conventions` is next materially
re-edited, the relevant section should add one sentence:

> *LE31 v1 requires a server reachable over the internet. A venue
> whose only network is its own LAN is out of scope for v1.*

**Why one sentence and not a feature.** A boundary that is written
down is a decision a future contributor can cite, test against, and
stop re-deriving. A boundary that is merely absent is an accident
that gets re-litigated in every planning session — and eventually
discovered by the *owner*, the first time a prospective venue says
"we don't have internet".

**The reason the boundary is total, not partial, is worth stating in
the sentence's vicinity:** the cook surface is a **Telegram bot**,
whose inbound webhook is served by Telegram's servers. **A LAN-only
venue cannot run LE31's cook bot at all.** So this is not a degraded
mode — it is a genuine scope statement, and it should not be phrased
as if LE31 might half-work.

**The citation for why the sentence is worth writing** (from the
contract's *Description*): a **39 KB, single-file, LAN-only** ordering
board (`drsamonline/canteen-lan`) built *only* because this venue
profile exists; a second artifact with the same offline posture and a
heavier dependency tree (`CrausalX/fork`, Dexie/PWA/indexeddb); a
third-party backend in the same cluster (Supabase); and the
operator-side story *"Keeping restaurant iPads in sync without a
router"* (`tablelink.app`, HN 2026-10-19) which **recurred in two
consecutive windows**. Two independent arrivals from two different
sides, one week apart.

## Trigger for the next step

The next time **any one** of these is true:

1. A venue, owner, or prospective customer asks whether LE31 works
   without internet.
2. A PR touches deployment, networking, or the VPS topology.
3. The owner explicitly asks for offline or LAN-only support.

When triggered:

1. Read the contract in full, plus feature 373 (offline-first POS
   vocabulary) and feature 348 (offline-first Kafka vocabulary) — the
   offline question is **not** new and must not be answered twice.
2. Confirm the proposed sentence is still the right shape.
3. **If the owner has asked for offline support (trigger 3), this is
   no longer a vocabulary reference.** It becomes a **v2-scale
   architectural decision** and **the feature gate must be re-run from
   scratch**, with the owner's own words as the evidence class
   (`reported`, not `inferred`). Do not treat this artifact as
   pre-approval.

## Verification protocol

Reference: `coding-agent/skills/le31-verification-protocol/SKILL.md`.

Documentary verification only, because there is no behaviour:

- [ ] `features/376-…-v1-local-network-ordering-surface-vocabulary.md`
      exists and was read back.
- [ ] The repo's licence, star/fork counts, size, language, topics,
      `created_at`, `pushed_at`, `archived`, `fork` and `default_branch`
      match the raw JSON at
      `/tmp/le31-daily-2026-10-25/pv/drsamonline__canteen-lan.json`.
- [ ] The description quoted in the contract
      (*"Order from your table over the room's own Wi-Fi - a LAN canteen board for Forge"*)
      is **verbatim** from the raw file.
- [ ] The `tablelink.app` HN story's date and URL match
      `/tmp/le31-daily-2026-10-25/hn/*.json`.
- [ ] `/opt/data/INDEX.md` has the pipeline row.
- [ ] **No source file, schema, template, or test was modified. No LAN
      server, offline mode, cache, or third surface exists.** No
      charter edit was made.

## Rollback path

Delete
`features/376-drsamonline-canteen-lan-mit-javascript-lan-offline-first-restaurant-single-file-order-from-the-table-over-the-room-own-wifi-v1-local-network-ordering-surface-vocabulary.md`,
delete
`specs/drsamonline-canteen-lan-mit-javascript-lan-offline-first-restaurant-single-file-order-from-the-table-over-the-room-own-wifi-v1-local-network-ordering-surface-vocabulary-HANDOFF.md`,
remove the `/opt/data/INDEX.md` row, and delete the (uncreated) Linear
sub-issue if it ever exists.

**Rollback cost: zero.** Nothing depends on it, no schema was touched,
no behaviour changed.

## Open questions carried into the slice

- **Where should the boundary sentence live** — `PROJECT_CHARTER.md` §3.2,
  the `le31-conventions` skill, or both? **Owner decision, not an agent
  guess.**
- **Should the boundary mention v2?** E.g. *"v2 may support LAN-only
  venues"* — that would be a **promise about v2**, which LE31's own
  discipline does not make casually. **Unmade, and deliberately unmade.**
- **Is the LAN-only venue common enough to name?** No evidence either
  way is claimed. The naming is justified by **cost** (one sentence),
  not **frequency** (unknown). **Recorded as such, not dressed up as a
  market finding.**
- **Does `canteen-lan`'s implementation contain a transferable
  primitive** (LAN discovery, single-file deployment trick)? **Unknown —
  the repo was not read beyond its API metadata.** If the owner ever
  scopes LAN support, the code must be read properly (MIT, 39 KB)
  before any primitive is claimed.
