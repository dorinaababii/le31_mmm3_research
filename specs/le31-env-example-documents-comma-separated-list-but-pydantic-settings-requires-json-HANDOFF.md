# Slice contract — `le31-env-example-documents-comma-separated-list-but-pydantic-settings-requires-json`

## Active feature path

`features/479-le31-env-example-documents-comma-separated-list-but-pydantic-settings-requires-json-first-party-the-shipped-example-makes-settings-parsing-fail-v1-settings-list-format.md`

## Seven-check gate verdict

**BUILD.** Evidence class: **observed**, execution-proven against LE31's `Settings`; confidence high.

1. **JTBD:** When an operator configures Telegram IDs from the shipped example, they want the app to start, but the documented comma-separated format raises `SettingsError`.
2. **Viability:** pass; one example-format decision, one settings test, one corpus correction.
3. **Practicability:** pass; no dependency or stack change.
4. **Conflict:** none; feature 403's allowlist model and feature 469's CORS behavior remain untouched.
5. **Outcome/scope:** v1 operability; limited to the documented format, empty-value behavior, and feature 469's false claim.
6. **Cost/value:** tiny cost; prevents a boot-time failure caused by following shipped instructions.
7. **Circuit breaker:** stop if the settings layer changes; revert the documentation/test change; no data risk.

## Files to touch

- `backend/.env.example` — Telegram ID list example and comment.
- `backend/app/config.py` only if a comment is needed; do not add a new decoder.
- A focused settings-loading test.
- `features/469-...md` — correct only the false pydantic-settings parsing claim; do not alter feature 469's scope.

Do not implement the allowlist, add `NoDecode`, add a dependency, or redesign configuration.

## Verification protocol reference

Follow the feature contract's `## Verification protocol`:

1. Parse a temporary dotenv file containing the exact shipped example format and assert settings construct. **The implementer must establish the test harness if the repository does not already contain one.**
2. Assert comma-separated input raises `SettingsError`.
3. Assert unset and `"[]"` yield `[]`, while the empty value after `=` raises `SettingsError`.
4. Assert the corrected example matches the passing test's input.
5. Assert feature 469 no longer contains any of its three false parsing claims (comma-separated, empty-string, and bare `"*"`).

The test must fail before the example correction and pass afterward.

## Rollback path

Revert the example and test changes. Runtime behavior is unchanged; no data, migration, or state is affected.

## Mandatory LE31 skill list

- `le31-conventions`
- `le31-v1-feature-pattern`
- `development`
- `speckit-specify`
- `speckit-plan`
- `speckit-tasks`
- `speckit-implement`
- `verify-before-fixing`
- `pre-merge-review`

## Linear reference

Created as a draft Feature sub-issue under the 2026-11-14 research issue. If Linear writes remain blocked, use `/opt/data/le31-daily-research-2026-11-14.linear-fallback.json` and record `linear: blocked`.
