---
name: le31-research
description: Use when researching LE31 product ideas, restaurant operations, competitors, regulations, libraries, releases, architecture, or AI feasibility. Produces traceable source-backed reports, explicit nulls and blockers, and a durable repository or local artifact.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [le31, research, evidence, restaurant-tech]
    related_skills: [le31-conventions, raw-api-web-research, arxiv]
---

# LE31 Research Workflow

## Overview

Research answers a decision; it does not collect links for their own sake. Frame the question, gather direct evidence, distinguish observed facts from interpretation, persist the report, then run the LE31 feature gate if the result may change the product.

## When to Use

Use for market, restaurant-operations, competitor, academic, regulatory, library/release, architecture, data, or AI research. Do not use when the answer is already an explicit charter decision or can be proven directly from the current repository.

## Procedure

### 1. Specify the decision

Write the question and decision, strict time window/geography/user role, inclusion/exclusion rules, evidence types, and expected output path. Completion: another researcher could run the same search without guessing.

### 2. Inspect existing evidence first

Read the relevant charter, feature file, prior report, latest Linear research index, and live source identifiers provided by the user. Session history is secondary context, never proof of current external state. Completion: prior work is cited or explicitly found irrelevant.

### 3. Build a source plan

Prefer official documentation, legislation, release notes, repositories, academic papers, and standards bodies. Use reputable reporting and practitioner material for context; use forums/social signals only as leads or demand anecdotes. Use multiple independent query families.

### 4. Fetch and preserve

Use raw HTTP/curl when browser search is blocked or unnecessary. Save raw responses under `/tmp/le31-<topic>/`. Record URL, fetch time, HTTP status, publication date, and source type. Do not claim a blocked page was read. Completion: every material claim is traceable or labeled inference.

### 5. Evaluate evidence

For each finding record the claim, source/date, direct quote or data point, LE31 relevance, confidence, limitations, and confirming/contradicting sources. Treat zero-result searches as nulls only after several relevant query families.

### 6. Synthesize for the decision

Separate findings, implications, recommendations, adjacent/older evidence, blockers, and unknowns. Run `le31-conventions` before recommending a product feature. A release can make a feature practicable without making it viable or valuable.

### 7. Persist and index

Save a dated Markdown report in the repository when it is durable project research; otherwise use `/opt/data/le31-<topic>-YYYY-MM-DD.md`. Include source URLs and HTTP statuses. Create/update a Linear research index only when it adds durable navigation value. Commit and push repository artifacts immediately. Completion: report exists, is read back, and index links point to the actual artifact.

## Report Shape

```markdown
# <Question>
## Decision informed
## Scope and method
## Sources fetched
## Findings
## Contrary or null evidence
## LE31 implications
## Feature-gate result
## Recommendation
## Adjacent evidence
## Blockers and limitations
```

## Common Pitfalls

1. Using snippets as sources; fetch the underlying page or label the snippet a lead.
2. Equating GitHub stars, HN votes, or vendor claims with restaurant need.
3. Mixing dates outside a strict window into recent findings.
4. Hiding blocked sources or empty results.
5. Leaving the only copy in a subagent summary.
6. Fabricating source counts or claiming a file was written without verifying it.

## Verification Checklist

- [ ] Decision, scope, window, and inclusion rules are explicit.
- [ ] Existing project evidence was checked first.
- [ ] Material claims have direct sources, dates, and statuses.
- [ ] Findings, inference, recommendation, nulls, and blockers are separated.
- [ ] Feature gate was run for product recommendations.
- [ ] Report exists and was read back; repository artifacts were pushed.
