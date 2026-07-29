---
name: le31-handoff-protocol
description: Use at the boundary between the coding agent (Hermes + Kimi K3) and the research agent (Hermes + MiniMax-M3). Defines diff disclosure, blast radius, evidence obligations, and human-approval gates for every PR touching money, stock, schema, or auth.
version: 1.0.0
author: Hermes Agent (research side)
license: MIT
metadata:
  hermes:
    tags: [le31, handoff, ai-safety, review, pr, blast-radius]
    related_skills: [le31-conventions-coder, le31-quality-gates, requesting-code-review]
---

# LE31 Handoff Protocol

## Overview

Every AI-generated change flows through this protocol. The coding agent proposes; the human owner (or designated reviewer) disposes. AI never owns a merge to main without explicit approval.

## Standards anchor

- **HiLDe (arXiv 2501.04880)** — within-subjects study (N=18) showed LLM coding assistants *increase* vulnerabilities in security-critical tasks when humans disengage. The human-in-the-loop is therefore non-negotiable.
- **Inference-Time Safety For Code LLMs (arXiv 2502.06302)** — bounded LLM in the loop with explicit safety checks at inference time.
- **NIST SP 800-218 SSDF PW.7** — code review as a practice.
- **OWASP A01 / A08 / A09** — access control, integrity, logging.

## Mandatory human-approval triggers

A human must approve before any of the following reach `main`:

- change to `stock_entry`, `money_event`, `tip`, `tax`, `closed_*` tables
- change to a SQL migration file
- change to authentication, allowlist, or role-based access logic
- change to `requirements.txt` or the lockfile
- change to the i18n, currency, or timezone configuration
- change to a webhook, callback, or external API integration

A solo repo still requires a recorded self-review with the same checklist, dated.

## PR disclosure (mandatory sections)

1. Slice ID and goal.
2. Files touched, with paths.
3. Schema or migration impact (forward + rollback).
4. Test plan and commands run, with observed output.
5. Rollback or feature-removal path.
6. Blast radius: who is affected, which surfaces, what could go wrong.
7. Open follow-ups (if any).

If a section is empty, the PR is incomplete and cannot be merged.

## AI self-disclosure

- Every AI-authored line is acknowledged in the commit body: "AI-assisted: yes" plus the tool/version.
- A PR led by an AI carries "[ai-assisted]" in the title prefix.
- A solo run still records the AI tool/version in the disclosure.

## Evidence obligations before merge

The PR must include:

- `static-gates.txt` — output of `ruff`, `mypy`, `bandit`, `pip-audit`, `gitleaks`.
- `e2e.log` — happy + failure paths executed in the target environment.
- `db-dump.sql` — anonymised if it contains customer data.
- `screenshots/*.png` — at least one per UI surface change.
- `rollback.log` — `migrate-rollback` rehearsal output.

## Blast radius policy

| Change scope | Required reviewers | Required evidence |
|---|---|---|
| Ledger/money/auth schema | 1 human reviewer with the LE31 conventions read | full evidence kit + pre-merge rehearsal |
| New runtime dependency | 1 human reviewer | `pip-audit`, `bandit`, integration smoke test |
| New endpoint or callback | 1 human reviewer | full evidence kit |
| Bug fix in domain logic | 1 human reviewer | regression test that fails before and passes after |
| Cosmetic / UI text | self-review allowed | screenshot of the change |
| Docs only | none | `git log --diff` |

## Recovery

- A merge to `main` that does not satisfy the protocol is rolled back by default.
- The reviewer writes a short incident note.
- The coding agent logs what was missed and the team updates the gates.

## Channel conventions

- The PR description is the canonical record; the chat is not.
- Use stable paths; avoid paste-as-link patterns.
- Cite the active handoff contract by name and commit SHA.

## Common pitfalls

1. Pressing merge because tests passed and a diff "looks right" (HiLDe 2025: this is exactly when humans disengage).
2. Skipping the privacy column gate because "we'll never store it".
3. Omitting the migration rollback from the PR.
4. Calling a half-built feature "done".

## Verification checklist

- [ ] PR has all 7 disclosure sections.
- [ ] Required evidence files attached.
- [ ] Required reviewer count and roles satisfied.
- [ ] Schema/auth PRs rehearsed before merge.
- [ ] AI-assisted commit prefix and tool/version present.
- [ ] Recovery plan in place if the merge goes wrong.
