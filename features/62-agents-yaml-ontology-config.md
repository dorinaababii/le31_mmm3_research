# Feature 62 — Agents YAML Ontology Config

> **Priority**: P2 · **Effort**: S (≤2 days) · **Source**: brainstorm
> 2026-08-13 (cross-section pick B) · **Bucket**: **v2-AI control-plane**
> (companion to features 58 + 61).
> **One-line**: move the AI permission table from a Python dict
> inside `backend/app/config.py` to a version-controlled
> `agents.yaml` at the repo root, so the file (not the code) is
> the single source of truth for *"what is the AI allowed to do
> today?"*.

## Goal

Feature 58 (`operator-ai-action-surface`) ships the control plane
with a default-deny permission dict in `backend/app/config.py`:
```python
AI_PERMISSIONS = {"…": False, ...}
```
This is correct for v2-AI control-plane v1, but **the dict is
code**, which means:

- A reviewer (`owner-daily-recap` / coding-agent / auditor) cannot
  read "what is the AI allowed to do" with `git log agents.yaml`.
- A future v3 owner-edited change requires a deploy.
- A second restaurant (charter §3.2 says single-tenant v1, but
  v3+ wouldn't be) cannot override the policy per-location.

`cruxible-ai/cruxible` (pushed 2026-08-12, 16★, Python,
Apache-2.0) ships a *production* version of the **declarative
ontology** pattern: *"Governed state engine for AI agents: typed,
executable knowledge artifacts with a code-like lifecycle"*. The
pattern is *not* a research idea; it is a 16-star Python package
shipping in 2026.

`agents-yaml-ontology-config` is the **experiment**: ship the
artifact, ship the loader, do not yet ship the runtime dispatcher.
The dispatcher stays in code (feature 58). The artifact, when
present, **overrides** the dict; when absent, the dict is the
fallback (so existing tests keep passing).

## Scope

**In scope (v2-AI control-plane experiment, S effort, ≤2 days):**

- New repo-root file `agents.yaml` — a strict, minimal schema:
  ```yaml
  version: 1                       # required; integer; loader rejects unknown versions
  default_policy: deny             # required; "deny" | "allow"; loader rejects other values
  permissions:
    feature_19.menu_engineering_suggest: false
    feature_20.waste_prediction_suggest:  false
    feature_21.recipe_generation_suggest: false
    # everything else: not in the dict => follow default_policy (deny)
  fallback_aliases:
    feature_19.menu_engineering_suggest: "/menu_engineering_suggest manual"
    # mapping from canonical action name to the existing /<action> manual Telegram command
  ```
- `backend/app/services/ai_control_plane.py` (extension of
  feature 58): add `load_agents_yaml(path)` and a module-level
  cache `_loaded_yaml_permissions`. New helper
  `permission_table_get()` first reads the YAML cache, then
  falls back to the dict in `backend/app/config.py`. Defaults
  remain deny.
- `backend/app/config.py`: keep `AI_PERMISSIONS` as the fallback;
  do not delete. README documents the precedence.
- `backend/tests/test_agents_yaml_loader.py`: 6 fixtures (valid
  file, missing file → fallback, version mismatch, unknown value
  rejection, default-deny propagation, fallback-alias resolve).
- `agents.yaml.example`: an example checked in for reference;
  `agents.yaml` itself is in `.gitignore` to keep the local
  install out of version control.
- `backend/README.md`: short note on `agents.yaml`, the loader,
  and `git log agents.yaml` as the audit trail.

**Out of scope (v2-AI control-plane experiment v1):**

- The runtime dispatcher. The control plane reads the YAML at
  startup; the runtime path is unchanged. (The dispatcher change
  is feature 58 already.)
- An owner-facing Telegram command to edit the YAML. That is a
  later pick, gated on a charter revision to "owner can edit
  policy without redeploy" (currently §3.2 silent).
- Multi-tenant override. Charter §3.2 explicitly excludes
  multi-restaurant. The YAML is single-tenant at the file path
  `agents.yaml`; a future v3 multi-tenant feature would read
  per-tenant.
- Schema migrations. `version: 1` is the only supported
  version today; a `version: 2` requires a new feature, not a
  silent in-place migration.

## Description

Three corroborating sources for the same pattern.

**1. `cruxible-ai/cruxible`** (16★, pushed 2026-08-12, Python,
Apache-2.0) — *"Governed state engine for AI agents: typed,
executable knowledge artifacts with a code-like lifecycle"*. The
shape: declarative artefacts (typed, code-like lifecycle) drive
the runtime; the artefact is the truth. Cruxible authors pushed
it actively throughout 2026-Q3 (`pushed_at` 2026-08-12T22:02:50Z;
created 2026-03-04).

**2. HN Show HN `Cruxible – Terraform-like ontology config to
governed state for agents`** (2026-07-14,
`https://github.com/cruxible-ai/cruxible`). The "Terraform-like"
framing is the key: just as Terraform files are version-controlled
infra declarations, the agent policy is a version-controlled
*operating policy*.

**3. `Org-EthereaLogic/adws-pipeline-skill`** (pushed 2026-08-13,
JavaScript) — *"A gated, evidence-producing seven-phase coding
pipeline for Claude Code (plan→build→test→review→document→ship→committed)"*.
The pipeline *itself* is the declarative artefact. A LE31
analogue is `agents.yaml` itself.

**Literature anchor**: OpenAlex `Designing Agentic AI
Experiences` (DOI 10.1201/9781003738374, 2026-07-28) — the
"designing agentic AI experiences" framing requires a
reviewable policy artefact, separate from the AI logic.

LE31's contribution: take the *shape* of cruxible, *not* its
implementation (cruxible is a runtime engine; LE31 ships a
small declarative file + a tiny loader). What makes it novel
for LE31 is *that the artefact lives at the repo root and is
version-controlled alongside the code that runs the AI*. The
charter invariant *"AI may assist owner/staff, with observable
evidence and a non-AI fallback"* is centralised in **one
file that the auditor can read in 30 seconds**.

## Data model

No new SQLModel table. The artefact is a YAML file.

The runtime cache is a module-level variable:

```python
# backend/app/services/ai_control_plane.py
_loaded_yaml_permissions: dict[str, bool] | None = None  # None = YAML not loaded

def load_agents_yaml(path: str = "agents.yaml") -> dict[str, bool]:
    """If the file is present, parse + validate; cache result; return.
    If absent or invalid, log a warning and return {} (fall back to dict)."""
```

`permission_table_get(action_name)` first consults
`_loaded_yaml_permissions`, then falls back to
`backend/app.config.AI_PERMISSIONS`, then to the default-deny
rule.

## Implementation steps

1. Create `agents.yaml.example` (committed). Document the schema
   in a 2-paragraph comment block at the top.
2. Add `agents.yaml` to `.gitignore` (already gitignored via
   `*.yaml`/`*.yml` patterns — verify; if not, add an explicit
   entry).
3. Add `backend/app/services/ai_control_plane.py` extensions:
   `load_agents_yaml()`, `permission_table_get()` override.
4. Add `backend/tests/test_agents_yaml_loader.py` (6 fixtures).
5. Add `backend/README.md` section: 1 paragraph on `agents.yaml`,
   loader precedence, and the example file.
6. Validate by running the existing `test_ai_control_plane.py`
   suite with `agents.yaml` absent (must pass; behavior unchanged)
   and present (the `feature_19.menu_engineering_suggest: true`
   test fixture must pass only when the YAML permits it).

## Telegram interaction if any

None in this slice. The runtime dispatcher is feature 58's
existing `/ai-actions` / `/approve <id>` / `/reject <id>` path.
A future pick could add a `/ai-policy` owner-only Telegram
command that re-reads `agents.yaml` and shows the currently
effective policy; that pick is not in scope here.

## Dependencies

- **Feature 58** (`operator-ai-action-surface`) — the
  `permission_table_get()` function lives in feature 58's
  service module; this slice extends it.
- **PyYAML** — not yet a hard dependency. The loader uses
  `tomllib` from stdlib first if the file is in TOML, falling
  back to a minimal hand-rolled YAML reader for the strict
  schema. If a future pick needs full YAML features, PyYAML
  becomes a dependency. The shipped schema is small enough
  that a hand-rolled parser keeps the dependency footprint at
  zero.

No SQLModel changes. No Alembic migration. No new pip
dependency at v1 of this experiment.

## Open questions

- TOML or YAML? Recommendation: YAML (matches `cruxible`'s
  framing; LE31's existing `index.html` mock-ups and `README.md`
  are Markdown-adjacent; YAML keeps the policy human-readable).
  Revisit if PyYAML ever becomes a heavy dep.
- Schema versioning: are we committing to `version: 1` only?
  Recommendation: yes for now; `version: 2` requires a new pick.
- Should the YAML be git-ignored or committed-by-default?
  Recommendation: `.gitignore` (single-tenant v1; a v3 with
  multi-tenant would commit a per-tenant override).

## Why this matters

The charter invariant says *AI may assist owner/staff, with
observable evidence and a non-AI fallback*. The first half
(*observable evidence*) is enforced by features 30, 47, 49, 50,
55, 58, 61. The first half *of that first half* — what the
AI is allowed to attempt — is today buried in a Python dict.
Externalizing that dict to a reviewable artefact makes the
control plane auditable end-to-end.

`cruxible`'s existence (16★, Python, Apache-2.0, just-pushed)
is the strongest 2026 signal that this pattern is production
mature, not a research idea. LE31 ships the LE31-flavoured
version of it: small file, strict schema, audit-friendly,
code-replaceable fallback.

This is an **experiment**, not a build. The slice boundary
is hard: a tiny file + a tiny loader + 6 unit tests. If the
experiment validates, a follow-up pick wires the runtime
dispatcher through it.

## Evidence (recorded)

- **Cross-section anchor 1**: `cruxible-ai/cruxible` (16★,
  pushed 2026-08-12, Python, Apache-2.0) — *"Governed state
  engine for AI agents: typed, executable knowledge artifacts
  with a code-like lifecycle"*. Read at
  `/tmp/le31-brainstorm-2026-08-13/gh_evidence_review.json` (also
  pushed to top results in the `evidence_review` GitHub query).
- **Cross-section anchor 2**: HN Show HN `Cruxible –
  Terraform-like ontology config to governed state for agents`
  (2026-07-14, `https://github.com/cruxible-ai/cruxible`).
  Listed in `/tmp/le31-brainstorm-2026-08-13/hn_evidence-review-agent.json`.
- **Cross-section anchor 3**: `Org-EthereaLogic/adws-pipeline-skill`
  (pushed 2026-08-13, JavaScript) — *"gated, evidence-producing
  seven-phase coding pipeline"*. Same shape, different domain.
- **Literature anchor**: OpenAlex `Designing Agentic AI
  Experiences` (DOI 10.1201/9781003738374, 2026-07-28).
- **In-repo dependency**: feature 58's `permission_table_get()`,
  which this slice extends without changing its signature.
