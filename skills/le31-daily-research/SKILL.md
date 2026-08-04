---
name: le31-daily-research
description: Use when the daily 08:00 Europe/Zurich cron job runs, or whenever a fresh LE31 research pass is requested. Produces a dated Markdown report under /opt/data/, updates INDEX.md, and creates a Linear research index issue.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [le31, daily, research, cron]
    related_skills: [le31-conventions, le31-research, le31-feature-pipeline]
---

# LE31 Daily Research

## Overview

Daily 08:00 Europe/Zurich pass that scans restaurant-tech and the LE31 tech stack, produces a dated report, and feeds the feature pipeline.

## When to Use

- Triggered by the cron job `le31-daily-research`.
- Manual invocation when a fresh LE31 research pass is needed.

## Procedure

1. Confirm the date and the working directory.
2. **Schedule caveat (timezone)**: the cron job is stored in UTC. To fire at **08:00 Europe/Zurich** the cron expression is `30 6 * * *` UTC (DST-aware). If the operator's timezone changes, update the cron schedule first; do not rely on Hermes to translate.
2. Delegate the fetch+research to a subagent using raw curl (no browser). Sources allowed:
   - HN Algolia `search_by_date`, 7-day window
   - arXiv API
   - OpenAlex API
   - GitHub Search Repositories API and release.atom
   - PyPI JSON
   - CNIL, EU EUR, ECB for any data-protection/EUR news
   - ScienceDirect is blocked on this VPS; treat as not retrievable
3. Save raw responses under `/tmp/le31-daily-<date>/`.
4. Produce `/opt/data/le31-daily-research-YYYY-MM-DD.md` with this exact shape:
   ```
   # LE31 Daily Research — YYYY-MM-DD
   ## Sources fetched
   ## Restaurant-tech findings (last 7 days)
   ## Stack-relevant findings (last 7 days)
   ## Competitor and operator UX signals
   ## Three feature picks
   ## LE31 gate verdict per pick
   ## Recommendations
   ## Adjacent evidence
   ## Blockers
   ```
5. Append a row to `/opt/data/INDEX.md` with date, headline, and file path.
6. Create or update a Linear issue in project `le31 Research` titled `Research YYYY-MM-DD — daily` with status `Done`. Body has the short summary and the file path.
7. Hand the three picks to `le31-feature-pipeline`.

## Hard rules

- Do not fabricate. Nulls and blockers are reported plainly.
- The report must reference real source URLs and dates.
- Do not start Linear issues for "v2-AI" picks unless explicitly scoped as v2-AI in the original prompt.
- Treat the report file as the source of truth. The Linear issue is the index.

## Verification checklist

- [ ] Report file exists and was read back.
- [ ] /opt/data/INDEX.md updated.
- [ ] Linear issue in `le31 Research` with status `Done`.
- [ ] Three picks handed off to `le31-feature-pipeline`.
