---
name: le31-daily-brainstorm
description: Use when the daily 08:00 Europe/Zurich brainstorm cron runs, or whenever a fresh LE31 cross-section idea scan is requested. Produces a dated Markdown report under /opt/data/, updates INDEX.md, and creates a Linear research index issue with the top three cross-app picks.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [le31, brainstorm, cross-section, daily, cron]
    related_skills: [le31-daily-research, le31-conventions, le31-feature-pipeline]
---

# LE31 Daily Brainstorm

## Overview

Daily 08:00 Europe/Zurich pass that scans adjacent apps, operator UX patterns, and creator/HCI literature for cross-section ideas that could bring LE31 further. Focus is on out-of-the-box thinking, not on incremental polish.

## When to Use

- Triggered by the cron job `le31-daily-brainstorm`.
- Manual invocation when a fresh cross-section idea scan is needed.

## Procedure

1. Confirm the date and the working directory.
2. **Schedule caveat (timezone)**: the cron job is stored in UTC. To fire at **08:00 Europe/Zurich** the cron expression is `30 6 * * *` UTC (DST-aware).
3. Delegate a curl-based brainstorm pass (no browser) to a subagent. Source families allowed:
   - HN Algolia `search_by_date`, 30-day window, queries like `crossover restaurant app`, `micro SaaS small business`, `solo founder SaaS`, `low-effort UX`, `phone-first POS`, `kitchen workflow`
   - GitHub Search with creative queries: `topic:small-business`, `topic:hci`, `topic:mobile-ux`, `topic:real-time`, `topic:append-only`, `topic:telegram-bot`, plus any restaurant-adjacent repos that surfaced in the last daily research and look interesting
   - OpenAlex: `creativity AND product`, `restaurant OR hospitality AND hci`, `single page application OR no-build OR htmx`
   - ProductHunt public RSS: `https://www.producthunt.com/feed` if reachable; treat as soft source, not blocking
   - ScienceDirect is blocked; treat as not retrievable
4. Save raw responses under `/tmp/le31-brainstorm-YYYY-MM-DD/`.
5. Produce `/opt/data/le31-brainstorm-YYYY-MM-DD.md` with this exact shape:
   ```
   # LE31 Daily Brainstorm — YYYY-MM-DD
   ## Sources fetched
   ## Cross-app signals (other industries)
   ## Restaurant-adjacent signals
   ## Operator UX and HCI signals
   ## Three cross-section ideas
   ## LE31 gate verdict per idea
   ## Why this could take LE31 further
   ## Adjacent evidence
   ## Blockers
   ```
6. Append a row to `/opt/data/INDEX.md` with date, headline, and file path.
7. Create a Linear issue in project `le31 Research` titled `Brainstorm YYYY-MM-DD — daily` with status `Done`. Body has the short summary plus the file path.
8. Hand the three picks to `le31-feature-pipeline`. Each pick gets:
   - a feature contract at `features/NN-<slug>.md` using the existing template
   - a slice hand-off at `specs/<slug>-HANDOFF.md`
   - a draft Linear sub-issue in the matching project with label `Feature`
9. Commit and push to `main` on the `le31_mmm3_research` repo. Commit message: `Daily brainstorm YYYY-MM-DD`.

## Hard rules

- Out-of-the-box is encouraged, but the gate still runs. `build / experiment / defer / reject / parking-lot`. Parking-lot is the new bucket: rejected by the gate today, but worth keeping on file.
- Do not duplicate picks already in `features/`. If the brainstorm surfaces a known idea, say so and skip.
- Treat the report file as the source of truth. The Linear issue is the index.
- **Never quote a subagent's prose as source text.** On 2026-08-28 the curl subagent presented OpenAlex abstracts labelled "verbatim" that contained fabricated sentences — it appended `"...that approximate the LE31 hands-busy, phone-first operator surface"` to a third-party paper's abstract, reported "five recurring practices" where the paper says **four**, and invented specific findings. Its own final message claimed "96/96 assertions pass, zero fabrication". **Subagent self-verification is not evidence.** Instruct the subagent to emit abstracts **only as raw `abstract_inverted_index` dumps or raw file paths, never as prose**, and reconstruct every abstract in the parent from the raw JSON. Re-verify every star count, fork count, licence, `created_at` and `pushed_at` in the parent too — the same pass had `pronto` reported as 42★/15f when the raw JSON said 43★/17f, omitted an AGPL-3.0 licence that is a charter §3.2 blocker, and reported two off-window repos as in-window.
- **Cheap fabrication canary:** `grep -c 'LE31' <raw_source_file>` must return `0` for any third-party paper or repo. No external source mentions LE31; if a summary's "verbatim" text does, it is invented.
- **In-window means `created_at` OR `pushed_at` in window — say which.** A repo created years ago that merely received a push is *in-window by push only* and must be labelled that way, not presented as a fresh discovery.
- **HN Algolia hits with `title: null` are comments, not stories.** Check `story_title` / `comment_text` before promoting one as a signal; a comment on a Show HN is not the same as the product.
- **The GitHub `language:` qualifier does not guarantee the language of returned repos.** Check the `language` field on each result (a TypeScript repo surfaced under `language:python` on 2026-08-28).

## No-signal handling

If no source family returns anything in-window, the report still ships, with headline `No new signal — sources quiet on YYYY-MM-DD`, per-source counts, and the `## Three cross-section ideas` section saying `No new ideas today; previously queued picks remain active`. The Telegram delivery is the same short shape with `signal: none` instead of slugs. Quiet days are valid output, not a failure.

## Verification checklist

- [ ] Report file exists and was read back.
- [ ] /opt/data/INDEX.md updated.
- [ ] Linear issue in `le31 Research` with status `Done`.
- [ ] Three picks (or `signal: none`) handed off to `le31-feature-pipeline`.
- [ ] Push to `main` confirmed.
