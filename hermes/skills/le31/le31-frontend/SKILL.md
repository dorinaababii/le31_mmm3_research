---
name: le31-frontend
description: Use when designing, prototyping, implementing, or reviewing LE31 waiter and owner web interfaces. Requires an index.html interaction mock-up first, mobile-first explicit actions, accessible state feedback, and no unnecessary SPA/build tooling.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [le31, frontend, waiter-ui, html, mobile]
    related_skills: [le31-conventions, le31-v1-feature-pattern, le31-backend]
---

# LE31 Frontend

## Overview

The waiter UI is operational software used under time pressure. Optimize for obvious state, large targets, few steps, and reliable recovery. The owner view must explain numbers plainly.

## When to Use

Use for `index.html`, templates, CSS, browser JavaScript, waiter/owner flows, responsive behavior, accessibility, formatting, polling, and UI validation.

## Mock-up First

For a new or materially changed interaction: update the repository `index.html` with realistic data and states; exercise it at phone/tablet dimensions; record user acceptance or unresolved UX questions; then freeze the API contract. Completion: the user can explain and complete the flow from the mock-up.

## Interface Rules

- Mobile/tablet first; primary controls are thumb-sized and not hover-only.
- Show operational states in text, not color alone.
- Financial, stock, send, serve, close, and adjustment actions are explicit.
- Prevent duplicate submission while pending; backend idempotency remains mandatory.
- Errors say what happened, what remained unchanged, and what to do next.
- Format exact backend EUR values; never calculate authoritative totals in browser float arithmetic.
- Render restaurant business time in `Europe/Paris`.
- Avoid customer-facing AI surfaces.

## Technology Discipline

Use the simplest current surface: vanilla HTML/CSS/JS or server-rendered partials. Do not introduce a SPA, bundler, or design system without an approved demonstrated need. Keep domain decisions in the backend.

## Required States

For each view cover loading, empty, normal, stale/polling, validation error, conflict/invalid transition, network failure, and completed state. Stock/order screens also cover sold out and concurrent change.

## Verification

Observe the UI at phone/tablet sizes, with keyboard focus, slow/failing requests, duplicate taps, server refresh, EUR values, and Paris-time rendering. A screenshot proves appearance; interaction proves behavior.

## Common Pitfalls

1. Starting endpoints before the interaction is agreed.
2. Using color as the only state indicator.
3. Showing a financial/stock mutation as final before server confirmation.
4. Adding a SPA because the mock-up has several views.
5. Hiding recovery instructions in generic errors.

## Verification Checklist

- [ ] Mock-up was accepted or UX questions are explicit.
- [ ] Required states and explicit transitions are represented.
- [ ] Phone/tablet, keyboard, failures, and duplicate taps were exercised.
- [ ] Exact EUR and Paris-time values match after refresh.
- [ ] No unnecessary framework or duplicated domain logic was added.
