---
name: le31-quality-gates
description: Use at every commit boundary in the LE31 coding-agent repository. Lists the security, code-quality, and disclosure gates that must pass before a feature claim of "done" can be made.
version: 1.0.0
author: Hermes Agent (research side)
license: MIT
metadata:
  hermes:
    tags: [le31, quality, gates, security, owasp, sast, sbom]
    related_skills: [le31-conventions-coder, le31-verification-protocol, requesting-code-review]
---

# LE31 Quality Gates

## Overview

What must pass before a commit, a PR, or a feature claim of "done". These gates are designed to be run as part of the standard pipeline (pre-commit / CI / human review). Skipping a gate requires an explicit, written reason.

## Standards anchor

- **OWASP Top 10:2025** as the minimum security baseline — most relevant items for this stack: A01 Broken Access Control, A03 Software Supply Chain Failures, A05 Injection, A08 Software or Data Integrity Failures, A09 Security Logging and Alerting Failures.
- **NIST SP 800-218 SSDF v1.1** for secure software development practices (PO.1–PO.5, PS.1–PS.3, PW.1–PW.9, RV.1). PW.7 (code review) and PW.8 (test executable code) are non-negotiable.
- **NIST SP 800-92** for log management practice.

## Static security gates

Run before each push:

| Gate | Command | Pass criteria |
|---|---|---|
| Dependency vulnerabilities | `pip-audit --strict` | No high/critical. |
| SAST | `bandit -r app/ -ll` | No high/critical. |
| Hardcoded secrets | `gitleaks detect --no-banner` or `trufflehog filesystem ./` | Zero findings. |
| Lint | `ruff check .` | Zero errors. |
| Type check | `mypy --strict app/` | Zero errors. |

Secrets found by `gitleaks` always block the commit, regardless of branch.

## Behavioural gates

| Gate | Pass criteria |
|---|---|
| All migrations apply forward and reverse | migrations replay against a clean Postgres in CI; rollback documented |
| Append-only ledger enforcement in production mode | ALTER on posted rows fails for the application role |
| Idempotency | every callback-driven mutation is idempotent (duplicate POST returns same result) |
| Money totals reconciliation | sum of emitted events equals sum of derived views within ±0 cents |

## Logging and audit gates

Reference OWASP A09 and NIST SP 800-92. Every domain operation emits one event with:

- `event_type`, `correlation_id`, `actor`, `occurred_at`
- the affected entity IDs and the value delta
- the originating surface (`bot`, `ui`, `import`)

The test suite asserts that each operation emits an event.

## Dependency and supply-chain gates (OWASP A03)

- Pin every dependency in `requirements.txt` with a `==`.
- Lockfile (`uv.lock` or `pip-tools`) is committed.
- Renovate or Dependabot runs weekly; PRs reviewed within 7 days.
- New runtime dependency = checkpoint commit + named use + trade-off note.

## Code review gate (NIST SSDF PW.7)

Every PR requires:

- one reviewer who did not write the code
- pass on the static and behavioural gates
- a written summary of the diff, tests, and rollback plan

A solo repo still requires a recorded self-review with the same sections, dated.

## Pre-merge disclosure

Every PR body or commit summary names:

1. Slice ID and goal
2. Files touched
3. Schema or migration impact
4. Verification commands run, with results
5. Rollback or feature-removal path
6. Open follow-ups (if any)

## Common pitfalls

1. Marking "ready" without running `mypy --strict` and `pip-audit`.
2. Suppressing a lint or type error with a `# noqa` or `type: ignore` to make CI green.
3. Bypassing append-only enforcement "for dev".
4. Suppressing an O09 logging gap with a generic 200 response.

## Verification checklist

- [ ] `pip-audit`, `bandit`, `ruff`, `mypy --strict`, secret-scan all clean.
- [ ] Migrations replay both forward and back.
- [ ] Append-only enforced in the configured DB role.
- [ ] Idempotency + reconciliation tests added with the change.
- [ ] PR disclosure complete.
- [ ] Independent review recorded.
