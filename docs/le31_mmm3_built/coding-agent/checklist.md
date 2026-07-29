# LE31 Coding-Agent One-Page Checklist

This is the field checklist. Each line is enforced by a SKILL.md in this folder.

## Before coding

- [ ] Read `docs/PROJECT_CHARTER.md` and the active `docs/features/<id>-*.md`.
- [ ] Load LE31 skills: `conventions-coder`, `arch-patterns`, `data-correctness`. Add others only when the slice names them.
- [ ] Confirm the feature gate answers for all 7 checks.
- [ ] Confirm rollout and rollback are documented.

## During coding

- [ ] One service operation per action; never business logic in router/handler.
- [ ] Money columns are integer cents or `Decimal` only. Never `float`.
- [ ] Every timestamp is `TIMESTAMPTZ`. Render in `Europe/Paris`.
- [ ] Ledger rows: INSERT only. UPDATE/DELETE revoked in prod.
- [ ] VAT stored as `rate_bps`, `base_cents`, `tax_cents` per line.
- [ ] No customer PII column without an approved feature.
- [ ] Idempotency key on every state-changing endpoint.

## Bot surface (cook)

- [ ] Every state change uses `InlineKeyboardButton`. No free-text mutation.
- [ ] Plain French. EU number format. Visible state in plain text.
- [ ] Duplicate taps are idempotent.
- [ ] Allowlist `TELEGRAM_ALLOWED_USERS` checked first.

## Pre-merge

- [ ] `ruff check .` clean.
- [ ] `mypy --strict app/` clean.
- [ ] `bandit -r app/ -ll` clean.
- [ ] `pip-audit --strict` clean (no high/critical).
- [ ] `gitleaks detect` clean.
- [ ] Migrations replay forward/back/forward with the app booting.
- [ ] Append-only UPDATE/DELETE blocked at DB role.
- [ ] Privacy column gate green.
- [ ] Reconciliation: ledger total = derivation view total (zero delta).
- [ ] End-to-end happy + failure paths captured.
- [ ] PR disclosure: 7 sections, all populated.

## Handoff to research side

- [ ] AI-assisted commit prefix and tool/version present.
- [ ] Handoff contract file referenced by name and SHA.
- [ ] Evidence artefacts archived under `docs/coding-agent/evidence/<slice-id>/`.
