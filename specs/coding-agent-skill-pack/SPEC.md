---
name: coding-agent-skill-pack
description: Pack of 7 SKILL.md files shipped to a separate coding-agent repository so Hermes-on-Kimi-K3 implements LE31 features to research-side standards.
---

# Coding-Agent Skill Pack Specification

## What

Produce 7 self-contained `SKILL.md` files for the coding-agent repository (Hermes running Kimi K3). The pack enforces LE31 standards that the research-side Hermes already follows, without sharing conversation context.

## Why

- Same engineer, two model surfaces (MiniMax-M3 and Kimi K3) — both must produce code that meets LE31 standards.
- Sharing the chat is not portable; the coding agent must act from the skill pack alone.
- A separate `coding-agent/` folder in this repo makes the pack shippable and `.gitignore`-able in the destination repo.

## Acceptance

- 7 SKILL.md files at `coding-agent/skills/<name>/SKILL.md`.
- Each skill cites its primary source in the body and includes verification commands.
- Plus one `README.md` and one `checklist.md` in `coding-agent/`.
- SPEC/PLAN/TASKS files at `specs/coding-agent-skill-pack/`.
- Branch is `feature/le31-coding-agent-skill-pack`, not `main`.
- Validation passes (frontmatter + names + description length + body present).

## Standards sources

See `/opt/data/le31-coding-agent-research-2026-07-27.md` for the full citation set. Standards map:

- Money → Fowler Money + Husobee 2016 + IEEE 754
- Timestamps → RFC 3339 + IANA tzdb
- Audit/append-only → double-entry + Whittaker + NIST SP 800-92
- GDPR/CNIL → Art. 5, Art. 25
- Code security → NIST SSDF v1.1 + OWASP Top 10:2025
- Bot UX → Nielsen 10 + Telegram Bot API
- AI safety → HiLDe arXiv 2501.04880 + Inference-Time Safety arXiv 2502.06302
