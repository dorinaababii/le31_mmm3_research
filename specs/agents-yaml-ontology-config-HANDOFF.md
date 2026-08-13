# agents-yaml-ontology-config — HANDOFF

> **Slice for the coding agent.** Read this *and*
> `features/62-agents-yaml-ontology-config.md` before touching any
> code. Do not paste chat excerpts back into the build.

## Frozen identifiers (do not rename)

- Feature ID: `62`
- Slug: `agents-yaml-ontology-config`
- Contract file: `features/62-agents-yaml-ontology-config.md`
- Bucket: **v2-AI control-plane** (companion to features 58 + 61)
- Linear parent: HMM-71 (Brainstorm 2026-08-13 — daily)
- Linear sub-issue: HMM-73 (see `le31 v1 — Core MVP` project, label `Feature`; matches the v2-AI control-plane sub-issue convention used by feature 58 HMM-67)

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md`. Evidence precondition:
**observed** (`cruxible-ai/cruxible` 16★ Python Apache-2.0
pushed 2026-08-12, the strongest 2026 production anchor for the
declarative-ontology pattern; `Org-EthereaLogic/adws-pipeline-skill`
pushed 2026-08-13 corroborating; HN `Cruxible` Show HN 2026-07-14
anchor). Confidence: **high**.

**Decision: experiment (v2-AI control-plane experiment, S effort,
≤2 days).** The slice is small enough to ship as a wiring
experiment before the runtime path is wired in. The experiment
ships the artifact + the loader, **not the dispatcher**. Circuit
breaker: drop `load_agents_yaml()` call from `permission_table_get()`,
the control plane falls back to `backend/app.config.AI_PERMISSIONS`
with no behavior change.

## Mandatory LE31 skill list (load these first)

External coding agent MUST load before starting:

1. `le31-conventions` (project invariants + the seven-check gate).
2. `le31-v1-feature-pattern` (canonical contract shape + slicing
   rules; even though this is v2-AI, the slicing discipline
   inherits).
3. `le31-handoff-spec` (frozen-contract discipline; mirror
   contract back).
4. `le31-daily-brainstorm` (this pick came from the daily
   brainstorm job on 2026-08-13).
5. `le31-feature-pipeline` (so the agent understands how this
   slice will be sequenced after it ships).

If the destination repo does not yet ship these skills, request
them from the research-side Hermes instance before writing code.

## Files the slice touches

```
agents.yaml.example                                   # NEW (committed): schema reference
.gitignore                                            # EDIT: ensure `agents.yaml` (not .example) is ignored
backend/app/services/ai_control_plane.py              # EDIT: load_agents_yaml() + permission_table_get() extension (≤40 lines)
backend/app/config.py                                 # EDIT: keep AI_PERMISSIONS as fallback; document precedence in a docstring
backend/tests/test_agents_yaml_loader.py              # NEW: 6 fixtures
backend/README.md                                     # note agents.yaml + loader precedence + example file
```

No new pip dependencies at v1 of this experiment. Schema is
small enough to read with stdlib + a hand-rolled minimal
parser; a future pick that needs full YAML features can add
PyYAML.

## Endpoints and bot commands added

None in this slice. The runtime dispatcher is feature 58's
existing `/ai-actions` / `/approve <id>` / `/reject <id>` path,
unchanged. A `/ai-policy` owner-only Telegram command is a
**separate future pick**; not in this slice.

## Schema (agents.yaml)

```yaml
# agents.yaml.example — committed for reference; copy to `agents.yaml` at
# the repo root to override the fallback dict in
# `backend/app/config.py::AI_PERMISSIONS`.
#
# The control plane consults this file at startup. When the file is
# absent, invalid, or version-mismatched, the loader logs a warning
# and falls back to the dict.

version: 1                       # required; integer >= 1; loader rejects unknown versions
default_policy: deny             # required; 'deny' | 'allow'; loader rejects other values

permissions:
  feature_19.menu_engineering_suggest: false
  feature_20.waste_prediction_suggest:  false
  feature_21.recipe_generation_suggest: false
  # Permissions not listed here follow `default_policy`.

fallback_aliases:
  feature_19.menu_engineering_suggest: "/menu_engineering_suggest manual"
  # Maps a canonical action name to the existing /<action> manual
  # Telegram command. The dispatcher consults this map when the AI
  # proposal is rejected or the verifier (future feature 63) flags
  # insufficient evidence.
```

## Loader (spec for the coding agent)

`backend/app/services/ai_control_plane.py` extension:

```python
# Pseudo-code — the slice implements this exactly.

_loaded_yaml_permissions: dict[str, bool] | None = None
_loaded_yaml_aliases: dict[str, str] | None = None

def load_agents_yaml(path: str = "agents.yaml") -> tuple[dict[str, bool], dict[str, str]]:
    """Parse + validate agents.yaml. Return (permissions, fallback_aliases).

    - File absent: log INFO, return ({}, {}).
    - File present + invalid: log WARNING, return ({}, {}).
    - File present + valid: cache and return.
    """
    ...

def permission_table_get(action_name: str) -> bool:
    """Override of feature 58's helper.

    Order:
      1. _loaded_yaml_permissions (if a key for action_name exists)
      2. backend/app/config.AI_PERMISSIONS (if a key exists)
      3. _loaded_yaml default_policy (if loaded)
      4. False (deny)
    """
    ...
```

The signature `permission_table_get(action_name: str) -> bool` is
unchanged from feature 58, so callers do not need to be
modified. Only the implementation changes.

## Verification protocol reference

Per `le31-conventions` "Verification" pattern. The coding agent
MUST:

1. Write all 6 test fixtures; `pytest backend/tests/test_agents_yaml_loader.py`
   must pass.
2. With `agents.yaml` absent: existing
   `pytest backend/tests/test_ai_control_plane.py` suite must
   pass; the `permission_table_get()` behavior must be
   unchanged.
3. With `agents.yaml` present and valid: confirm the YAML key
   overrides the dict by setting
   `feature_19.menu_engineering_suggest: true` and observing
   `permission_table_get('feature_19.menu_engineering_suggest')`
   returns `True`.
4. With `agents.yaml` malformed (e.g. `version: 2` or a non-`deny`
   `default_policy`): confirm the loader logs a WARNING and
   returns empty; confirm `permission_table_get()` falls back
   to the dict.
5. Confirm `agents.yaml` is in `.gitignore`; `agents.yaml.example`
   is committed.

## Rollback / feature-removal path

Delete `load_agents_yaml()` calls from `permission_table_get()`;
delete the test file; the control plane reverts to using
`backend/app.config.AI_PERMISSIONS` directly. Estimated
rollback cost: ≤30 minutes.

## Files for the coding agent to verify against

```
features/62-agents-yaml-ontology-config.md
specs/agents-yaml-ontology-config-HANDOFF.md          (this file)
features/58-operator-ai-action-surface.md             (parent)
features/61-holdfast-approval-ledger.md               (sibling)
specs/operator-ai-action-surface-HANDOFF.md           (parent's hand-off)
specs/holdfast-approval-ledger-HANDOFF.md             (sibling's hand-off)
skills/le31-conventions/SKILL.md
skills/le31-v1-feature-pattern/SKILL.md
skills/le31-handoff-spec/SKILL.md
PROJECT_CHARTER.md
```
