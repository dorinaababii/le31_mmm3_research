# HANDOFF — Feature 498: v2 signed/versioned rule pack with local manual override

## Active feature path

`features/498-v2-signed-versioned-rule-pack-with-local-manual-override.md`

**Disposition:** `defer` — v2 parking-lot vocabulary reference. **A coding agent must not implement this feature from this handoff.** The handoff records the mechanism, the boundary with feature 411, and the trigger for a future, separately-gated rule-distribution scope.

## Seven-check gate verdict

| Check | Verdict |
|---|---|
| 1. Raison d'être / JTBD | INFERRED — no LE31 operator has asked for a distributable rule channel; the JTBD is inferred from the source's own operator-facing language |
| 2. Viability | PASS in principle — the mechanism is stated in the source README and the source is MIT |
| 3. Practicability / confidence | MEDIUM — FloCafe is TypeScript/Electron (off-stack); the README does not specify the pack format, the signature scheme, the trust root or the override-resolution order, so this records a **shape**, not a copyable design |
| 4. Conflict | CONFLICT with charter §3.3 open question 3 (tax) and §3.1's flat-tax rule — a per-category rule pack presumes an unanswered question. **This pick resolves nothing.** |
| 5. Outcome, appetite, scope | DEFER — LE31 v1 has a flat tax by design and an open question about it; there is no v1 caller for a rule channel |
| 6. Cost to operational value | LOW today (one document), HIGH if adopted (pack format + signer + trust root + engine + override precedence) |
| 7. Circuit breaker / reversibility | PASS — documentation only, fully reversible, no code authorised |

## Files to touch

**None in this disposition.** The only repository files for this slice are the feature contract above and this HANDOFF.

If a future rule-distribution feature is separately approved, likely touch points are:

- `backend/app/models.py` — future `RulePack` and `LocalRuleOverride` models;
- `backend/app/services/rules.py` — future rule resolution: pack lookup, signature verification, **override precedence**;
- `backend/app/services/tax.py` — future call site replacing the current inline tax computation (requires feature 408 to have landed first);
- `backend/app/routers/rules.py` — future pack listing and local-override CRUD routes;
- tests — override-wins-over-pack, pinned-version resolution, two-scopes-in-force, unsigned-pack rejection.

**Ordering constraints (not optional):**
1. Charter §3.3 question 3 must be answered. A rule pack that writes into a free-floating tax number makes feature 408's defect unfixable rather than fixable.
2. Feature 408 (`tax-rate-and-rounding`) must land first.
3. Feature 411 (`money-precision-guard`) is the component that would *enforce* a pack's rounding policy — it is a peer, not a prerequisite of the vocabulary.

## Verification protocol reference

For this defer disposition, verification is documentary:

1. Read `features/498-v2-signed-versioned-rule-pack-with-local-manual-override.md`.
2. Re-read the source evidence at `/tmp/le31-daily-2026-11-19/gh/readme_01_FreeOpenSourcePOS_FloCafe.md` and the repository metadata at `/tmp/le31-daily-2026-11-19/gh/repo_01_FreeOpenSourcePOS_FloCafe.json` (MIT, ★195, pushed 2026-11-19T03:15:51Z).
3. Confirm the parent report at `/opt/data/le31-daily-research-2026-11-19.md` records the pick as `DEFER` and the project attachment as `le31 Research`.
4. Confirm the dedup result by re-running the corpus sweep: `grep -rilE '(signed|versioned).{0,30}(pack|bundle|catalog)|tax.{0,20}pack' features/ specs/` → **0 files**.

For a future implementation, required verification includes a test proving **a local manual override wins over the pack rule it shadows**, a test proving a **pinned pack version** resolves to that version rather than the latest, a test proving **two packs of different scopes in force simultaneously** resolve per a recorded rule, and a test proving an **unsigned or wrongly-signed pack is rejected**. The repository currently has **no test harness, no `pyproject.toml`, no `pytest`/`conftest.py` and no test directory** — the implementer must establish the harness as part of the slice, and must not assume one exists.

## Rollback path

- Delete `features/498-v2-signed-versioned-rule-pack-with-local-manual-override.md`.
- Delete `specs/498-v2-signed-versioned-rule-pack-with-local-manual-override-HANDOFF.md`.
- Remove the feature-498 row from `/opt/data/INDEX.md`.
- No application rollback is needed because this slice changes no runtime code.

## Mandatory LE31 skill list

Before any future implementation, load and follow:

- `le31-conventions` — charter §3.1/§3.2/§3.3 scope rules, the truth invariant, and the **seven-check feature gate**;
- `le31-research-workflow` — signed-delta and source-evidence discipline;
- `le31-v1-feature-pattern` — contract conventions, slicing rules, and the *Definition of Done*;
- `le31-handoff-spec` — frozen-contract and HANDOFF discipline;
- `le31-coding-agent-brief` — paste-in prompt generation from this slice contract;
- `pre-merge-review` — independent review before merge.

## Trigger to promote

Promote only when **all** of the following hold:

1. the owner has answered charter §3.3 question 3 with a tax model that is **not** a single flat rate — if the answer is "flat 10% forever", **delete this feature rather than promoting it**;
2. feature 408 (`tax-rate-and-rounding`) has landed, so a rule has somewhere to live;
3. a new feature is separately scoped and gated under a project that exists at that time — the workspace currently has only `le31 v1 — Core MVP`, `le31 Workflow` and `le31 Research`, and **no v2 project**;
4. the trust-root and pack-format questions in the contract's open-questions list have an owner answer, because a signed channel without a trust root is not a signed channel.
