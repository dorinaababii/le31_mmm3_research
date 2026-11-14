# Feature 479 — The shipped `.env.example` documents comma-separated Telegram IDs, but pydantic-settings requires JSON and the app cannot start

> **Pick C of Daily Research 2026-11-14.** **First-party, execution-proven.**
>
> **Executed against LE31's own `Settings` and pydantic-settings (2026-11-14):**
>
> ```text
> TELEGRAM_ALLOWED_USER_IDS=123456,789012
> -> SettingsError: error parsing value for field "telegram_allowed_user_ids"
>
> TELEGRAM_ALLOWED_USER_IDS=[123456,789012]
> -> [123456, 789012]
> ```
>
> Additional executed results: **unset → `[]`**, **`"[]"` → `[]`**, but the **exact shipped value `TELEGRAM_ALLOWED_USER_IDS=` (empty after `=`) raises `SettingsError`**. The shipped example therefore fails to load even before an operator supplies a comma-separated list.
>
> The same execution disproves three claims in feature 469: `pydantic-settings` does **not** parse comma-separated values into a `list[str]`; `CORS_ALLOW_ORIGINS=""` does **not** yield `[]`; and bare `CORS_ALLOW_ORIGINS="*"` does **not** parse — only the JSON array `["*"]` does.

## Goal

Make the shipped configuration example describe a value that LE31 can actually parse, so an operator who follows the instructions can start the app.

**The single sentence this feature exists to make true:** *every value format shown in `backend/.env.example` is accepted by LE31's `Settings` class.*

## Scope

**In scope (v1):**

- Correct the `TELEGRAM_ALLOWED_USER_IDS` example and its comment to use a parseable JSON array format.
- Define and document the empty-value behavior for complex list settings.
- Add a settings-loading test that parses the shipped example format and asserts the expected typed value.
- Correct the three false pydantic-settings statements in feature 469's `## Data model` (comma-separated parsing, empty-string parsing, and bare `"*"` parsing).

**Out of scope (v1):**

- The Telegram allowlist and role model (feature 403).
- CORS origin-policy behavior (feature 469 owns that behavior; this feature only corrects its false parsing claim).
- Adding `NoDecode` or any new pydantic-settings behavior.
- Adding a new settings field, a new dependency, or a dotenv-management library.
- Redesigning the configuration system.

## Out of scope

The exclusions listed under **Scope** are binding: the Telegram allowlist (feature 403), feature 469's CORS behavior, `NoDecode` or new pydantic-settings behavior, a new settings field or dependency, and a broader configuration redesign.

## Description

`backend/app/config.py` declares:

```python
telegram_allowed_user_ids: list[int] = []
```

`backend/.env.example` says:

```text
# Comma-separated list of Telegram user IDs allowed to use the bot (cook + manager)
TELEGRAM_ALLOWED_USER_IDS=
```

For complex fields, pydantic-settings parses the raw dotenv value as JSON. The documented comma-separated format therefore raises `SettingsError`. The empty value has separate behavior and must be documented explicitly rather than assumed.

The example file is the first thing an operator copies. A format that fails during settings construction makes the failure look like an application bug rather than a documentation error.

## Data model

No schema or model change. `telegram_allowed_user_ids` remains `list[int]`.

The contract changes only the documented serialization and pins the intended behavior:

- unset → `[]`
- `"[]"` → `[]`
- JSON array of integers → the parsed list
- **an empty value after `=` → parse error** (this is the shipped value today)
- comma-separated values → not accepted; must fail visibly if supplied

## Implementation steps

1. Change the `.env.example` comment and example value to the JSON-array format. **The shipped value must become `TELEGRAM_ALLOWED_USER_IDS=[]` (or a JSON array of IDs), not an empty value and not a comma-separated list.**
2. Document the empty/unset behavior next to the example.
3. Write a failing settings test using a temporary dotenv file: comma-separated must raise; JSON must parse; unset and `"[]"` must yield `[]`; the empty value must raise. **The implementer must establish the test harness if the repository does not already contain one.**
4. Apply the fix and rerun the test.
5. Patch feature 469's parsing claims so the corpus no longer asserts disproved mechanisms. **Three sentences in feature 469's `## Data model` are false:** comma-separated → `list[str]`; `CORS_ALLOW_ORIGINS=""` → `[]`; and bare `CORS_ALLOW_ORIGINS="*"` parses. Correct all three operator instructions; do not otherwise change feature 469's scope.
6. Run the settings and application startup tests.

## Telegram interaction if any

None. This feature changes configuration parsing and documentation only; it does not change which Telegram IDs are accepted by a running bot.

## Dependencies

- `backend/.env.example`.
- `backend/app/config.py` — `Settings`, `telegram_allowed_user_ids`.
- pydantic-settings complex-field decoding.
- Feature 469 — its parsing claim is corrected here; its CORS behavior is untouched.
- Feature 403 — owns the authorization data model; this feature must not implement the allowlist.

## Open questions

1. Should the empty value stay empty, or become `[]` explicitly in the example? Both must resolve to `[]`; the contract requires the behavior to be tested rather than left implicit.
2. Should a malformed non-empty value produce a clearer error message? The default is no extra parsing layer; pydantic-settings' error is explicit enough once the example is correct.
3. Are any other shipped examples invalid? A repository-wide example-value audit is adjacent and not bundled here.

## Why this matters

Configuration is the first contract between LE31 and the person deploying it. An example that cannot be loaded converts a two-minute setup into a boot-time failure with an error that points at the field rather than at the documentation.

The correction also matters for the corpus: feature 469 currently proposes an empty-list default based on a parsing behavior that does not exist. Leaving the claim in place would send a later implementer down the wrong path.

## Adjacent evidence

- Feature 469's `## Data model` contains three false pydantic-settings statements. Executed behavior contradicts all three.
- The shipped file also documents blank optional values for scalar string settings; those are outside this slice.

## Verification protocol

1. Parse a temporary dotenv file containing the exact format from the shipped example and assert the application settings construct successfully.
2. Assert comma-separated input raises `SettingsError` rather than being silently accepted.
3. Assert unset and `"[]"` yield `[]`, while the empty value after `=` raises `SettingsError`.
4. Assert the corrected `.env.example` text matches the format the passing test uses.
5. Assert feature 469 no longer contains any of the three false parsing claims.

## Rollback path

Revert the example and test. The existing application behavior is unchanged; no data, migration, or runtime state is affected.
