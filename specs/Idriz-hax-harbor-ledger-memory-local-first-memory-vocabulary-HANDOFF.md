# Idriz-hax-harbor-ledger-memory-local-first-memory-vocabulary — HANDOFF

> **Slice for the coding agent — NOT YET ACTIVE.** This artifact is a
> `defer` (parking-lot) vocabulary reference. **Do not implement anything from
> this file today.** Read this *and* `features/352-Idriz-hax-harbor-ledger-memory-...md`
> before any work begins. Do not paste chat excerpts back into the build.

## Frozen identifiers (do not rename)

- Feature ID: `352`
- Slug: `Idriz-hax-harbor-ledger-memory-local-first-memory-vocabulary`
- Contract file: `features/352-Idriz-hax-harbor-ledger-memory-mit-local-first-neural-memory-for-ai-agents-private-markdown-obsidian-vaults-auditable-retrieval-mcp-access-fastapi-python-v2-ai-local-first-memory-vocabulary.md`
- Bucket: **v2-AI** — `defer` (parking-lot, vocabulary reference only)
- Source repo: `Idriz-hax/harbor-ledger-memory` (MIT, ★0/⑂0, Python ON-STACK, pushed 2026-10-14T10:00:20Z, created 2026-04-21T23:25:42Z)
- Linear parent: `le31 Research` (P-HMM-1)
- Linear sub-issue: **NOT CREATED** — Linear MCP write endpoint blocked (32nd consecutive day). Fallback JSON: `/opt/data/le31-daily-research-2026-10-21.linear-fallback.json`

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md`. Evidence precondition: **observed**
(in-window GitHub repo; verbatim description names `Local-first`, `private
Markdown/Obsidian vaults`, `auditable retrieval`, `MCP access`; 6/6 topics
LE31-relevant).

**Confidence:** **medium-high** for the vocabulary match (full LE31
backend-stack match, all four primitives named explicitly); **low** for present
urgency (LE31 has no AI surface; ★0 provides no traction evidence in either
direction).

**Decision: defer (parking-lot).** No build commitment.

**Checks that would block a `build` today:**
- **Viability (§2)**: ★0/⑂0 with no in-window corroboration. Single-source
  evidence; the pattern is plausible but the peer signal is thin.
- **Practicability (§3)**: the upstream repo's own framing is **"neural memory"**,
  which implies an embedding dependency. **This directly conflicts with the §3.7
  guarantee** if the embedding computation is a third-party API call. The LE31
  version would need to be **keyword/file-based retrieval with the document set
  always surfaced** — accepting worse recall for better auditability. That is a
  design decision, not an implementation detail.
- **Outcome and scope (§5)**: zero v1 demand; v2-AI bucket. LE31 has no AI
  surface and therefore no memory surface.

**Checks that pass:** Conflict — this is the **only in-window agent-memory
vocabulary of the 82-pass series that satisfies the §3.7 privacy invariant *by
construction*** rather than by review; private Markdown vaults on the owner's own
disk mean restaurant documents have no egress path. Reversibility: fully
reversible, vocabulary-only.

## Mandatory LE31 skill list (load these first)

External coding agent MUST load before starting (when this slice is ever
re-elevated from `defer` to `experiment` or `build`):

1. `le31-conventions` (project invariants + the seven-check gate; **especially
   §3.7 privacy — counts not identity, minimal data**).
2. `le31-v1-feature-pattern` (canonical contract shape + slicing rules).
3. `le31-handoff-spec` (frozen-contract discipline; mirror the contract back).
4. `le31-daily-research` (this pick came from the daily research job on 2026-10-21).
5. `le31-feature-pipeline` (how this slice will be sequenced once re-elevated).
6. `le31-research` (for the cross-section evidence base).

If the destination repo does not yet ship these skills, request them from the
research-side Hermes instance before writing code.

## Files the slice would touch (NOT NOW — reference only)

```
features/352-Idriz-hax-harbor-ledger-memory-...md      # NEW (this contract)
specs/Idriz-hax-harbor-ledger-memory-local-first-memory-vocabulary-HANDOFF.md   # NEW (this file)
INDEX.md                                              # EDIT: one row in "Active feature pipeline" (added 2026-10-21)
# --- the following exist only as a design sketch; DO NOT CREATE until re-elevated ---
agent/models/memory.py                                # MemoryDocument + MemoryRetrievalEvent + MemoryWriteEvent
agent/services/vault_reader.py                        # reads Markdown from a configured dir; NO embedding service
agent/api/memory.py                                   # GET /api/memory/documents + GET /api/memory/retrievals
agent/services/memory_mcp.py                          # MCP tool surface: memory_search + memory_write
cook_bot/handlers/memory.py                           # aiogram v3 /memory + /memory show + /memory forget
agent/tests/test_memory_vault.py                      # no-egress test + retrieved set always non-empty + append-only
```

One Alembic migration when re-elevated: `CREATE TABLE memory_document` +
`CREATE TABLE memory_retrieval_event` +
`CREATE TABLE memory_write_event`.
**Zero schema impact on `MenuItem`, `StockEntry`, `Order`, `OrderItem`, `Bill`,
`Payment`, `Visit`, `Shift`.** `memory_retrieval_event` and `memory_write_event`
are **append-only with no update/delete code path** (charter §3.1). Zero new pip
dependencies (`pathlib` is stdlib).

**Hard constraints for any future implementation:**

1. **No outbound network call on the retrieval path.** This is the §3.7
   guarantee. If a future design adds embeddings, the embedding computation MUST
   be local or the guarantee is broken. Test 3 below enforces this.
2. **`surfaced_to_operator` MUST default to `TRUE` and MUST NOT be settable to
   `FALSE` by any caller.** Per §3.4, a retrieval that is not shown to the
   operator is not permitted. If a future need arises for a silent retrieval,
   that is a charter amendment, not a flag.
3. **`memory_write_event` is append-only.** Deleting a vault file is an ordinary
   filesystem operation; the *record* of the deletion is an append.

## Verification protocol

**Today: none.** This is a `defer` artifact; there is nothing to verify. The
protocol below activates only if and when this slice is re-elevated.

1. **Re-run the seven-check gate** before any implementation. Confirm nothing in
   the owner's stated priorities has changed the demand picture.
2. **Read back** `features/352-Idriz-hax-harbor-ledger-memory-...md` and confirm
   it matches the daily-research report's Pick C description.
3. **Run the no-egress test (the critical one):** perform a retrieval with the
   network disabled at the OS level; assert it still succeeds. This proves the
   §3.7 guarantee structurally rather than by inspection.
4. **Run the surfaced-set test:** every `MemoryRetrievalEvent` MUST carry a
   non-empty `retrieved_document_ids` array; assert the cook-bot reply includes
   the source paths.
5. **Run the append-only test:** attempt `UPDATE` and `DELETE` on
   `memory_write_event` and `memory_retrieval_event`; both MUST raise.
6. **Run the operator-bypass test:** open a vault file directly in a text editor
   with the agent stopped, and confirm the content is readable and the agent
   picks it up on next retrieval. The non-AI fallback is opening the file — it
   must work with the agent entirely offline.
7. **Run the §3.7 boundary test:** confirm guest identity data CANNOT be written
   into the vault (no name, no contact, no table-of-origin identifiers tied to a
   person). Counts and aggregate operational facts only.
8. **Run the LE31 test suite** and confirm it still passes.
9. **Hand-test on the cook bot**: trigger `/memory <query>`, `/memory show
   <path>`, `/memory forget <path>` in a test chat; verify each reply renders
   within the 4096-char Telegram limit.

## Rollback path

The artifact is a Markdown file in a git repository.

- **Rollback**: `git revert <commit>` on the commit that added
  `features/352-…md` and `specs/Idriz-hax-harbor-ledger-memory-…-HANDOFF.md`.
  No runtime impact to roll back, because nothing was deployed.
- **Feature-removal path** (if re-elevated and later reverted): drop the three
  tables; remove `vault_reader` and `memory_mcp` from the agent's tool surface;
  remove the `/memory` handlers. **The vault files themselves are NOT deleted by
  the rollback** — they are operator-owned content in a directory the operator
  chose. Removing the feature must not destroy the operator's data.
- **Data retained on removal**: the three tables (retrieval history + write
  provenance). The vault Markdown files are operator-owned and must be left
  intact.

## Linear sub-issue

**NOT CREATED.** The Linear MCP write endpoint has been blocked for 32
consecutive days (HTTP 400: *"You've exceeded the free issue limit for this
workspace"*). Read endpoints work; write endpoints do not.

When the block lifts, create the sub-issue as:
- **Project**: `le31 Research` (P-HMM-1) — per `le31-feature-pipeline/SKILL.md`
  line 33, because `le31 v2-AI` **does not exist** in this workspace (only
  `le31 v1 — Core MVP` P-HMM-3, `le31 Workflow` P-HMM-2, `le31 Research` P-HMM-1
  exist). Do **not** invent a project.
- **Label**: `Feature`
- **Title**: `Feature 352 — harbor-ledger-memory local-first memory vocabulary (defer)`
- **Body**: the feature-contract summary + the file path + the §3.7 no-egress
  constraint.

Full pending-issue specification: `/opt/data/le31-daily-research-2026-10-21.linear-fallback.json`.

## Sign-off gap

This package is **incomplete by design**: it records a `defer` decision, not an
agreed build. The external agent must NOT mirror this contract back as an
accepted slice. When this slice is re-elevated, the package must be regenerated
with (a) a fresh feature-gate verdict, (b) the §3.7 vault-boundary decision
recorded, and (c) a real Linear sub-issue ID.