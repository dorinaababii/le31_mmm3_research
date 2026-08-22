# Feature 91 — ezdmb-python-display-menu-board-watch

> **NEW observation (2026-08-21).** Documents the in-window
> `justinmichaelvieira/ezdmb` Python digital menu board peer
> observed during the 2026-08-21 daily brainstorm (see
> `/opt/data/le31-brainstorm-2026-08-21.md`, Pick B).
> Bucket: **v2 owner-pains (parking-lot, future-display-surface)** —
> hard defer pending charter §3.1 surface-expansion review.

## Goal

Record the **in-window Python front-of-house display peer** — `ezdmb`
("easy digital menu board") is a dead-simple Python application for
displaying a digital menu board. The pattern is **a single-purpose
Python display surface that runs without operational overhead**. The
cross-section question: should LE31 v2 grow a third surface for
displaying the menu to customers? Currently LE31 ships two surfaces
(waiter web UI + cook Telegram bot); neither is a front-of-house
display.

## Scope

**In scope:**
- Daily direct-repo `GET https://api.github.com/repos/justinmichaelvieira/ezdmb`
  (via `$HERMES_GITHUB_TOKEN`).
- Reading the `ezdmb` README in the next daily-research pass to
  confirm the single-purpose Python display pattern.
- Tracking star velocity + push activity on `ezdmb`.

**Out of scope (v1 / v2):**
- Importing any code from `ezdmb` (the pattern is single-purpose, not
  a library).
- Building a third surface (front-of-house display) for LE31 v2
  (charter §3.1 says two primary surfaces; this is a charter-level
  surface-expansion question).
- Building any feature based on the ezdmb code surface.

## Description

### `justinmichaelvieira/ezdmb`

|| Date | Stars | Pushed | License | Language |
||---|---|---|---|---|---|
|| 2026-08-21 (baseline) | 25★ | 2026-08-18 | (not checked) | Python |

**Direct repo URL**: https://github.com/justinmichaelvieira/ezdmb

**Verbatim description** (from GitHub API):
> A dead-simple digital menu board display and configuration, written
> in Python.

**Why this is the cross-section peer of the pass:**

1. **Single-purpose Python display surface.** The ezdmb pattern is
   "one Python file, one config, one HTML render" — fits the LE31
   "minimal ops" posture.
2. **★25 is mid-adoption.** Lower than ★39 (Pronto, Pick A) but high
   enough to be confirmed-not-accidental.
3. **Pushed 2026-08-18 (3 days before the fetch).** Active
   development.

**Why this is a parking-lot (not a build)**: the cross-section
question is "should LE31 v2 grow a third surface?" — the answer
depends on charter §3.1 surface-expansion review, not on the
existence of the peer. The peer proves the pattern is buildable; it
does not prove the pattern is needed for LE31.

### Cross-section peers in this 30-day window

- `justinmichaelvieira/ezdmb` (★25, pushed 2026-08-18, Python) —
  **this pick**.
- `radcliffkey/restabot` (★6, pushed 2026-07-23, Python) — restaurant
  menu bot (Telegram-bot-shaped, not display-shaped).
- `satisfecho/pos` (★30, pushed 2026-08-20, Python) — full-stack
  multi-tenant POS (AGPL-3.0, blocks v1 import per charter §3.2;
  already covered by features 40/42/89).
- `ablott976/splitbill-oss` (★6, pushed 2026-07-23, Python) —
  real-time bill splitting with OCR.

ezdmb is the **only** in-window Python peer with a single-purpose
**display** shape (not a POS, not a bot, not a scraper). The shape
uniqueness is the cross-section signal.

### Distinct from existing features

| Feature | What it does | How this pick differs |
|---|---|---|
| 11 `customer-qr-menu` | QR-code menu (web UI) | QR code on waiter-side; ezdmb is wall-mounted |
| 02 `order-taking` | Waiter-side order entry | Waiter-driven; ezdmb is display-only |
| 24 `visual-table-layout-v2` | Waiter-side table layout | Waiter-driven; ezdmb is display-only |

This pick is **NOT** a duplicate of any existing feature. It is a
**cross-section peer observation** that surfaces a charter-level
question ("should LE31 v2 add a front-of-house display surface?") that
the existing feature pipeline has not yet reached.

## Data model

None. Zero DB tables, zero columns, zero rows. This is a research
observation, not a feature build.

## Implementation

1. Read the `ezdmb` README in the next daily-research pass via
   `curl -sS` to
   `https://raw.githubusercontent.com/justinmichaelvieira/ezdmb/main/README.md`
   (or whatever branch the active push targets). Confirm the
   single-purpose Python display pattern.
2. Continue daily direct-repo GET on ezdmb to track star velocity.
3. **No build implied.** The pick is a parking-lot observation. The
   "should LE31 add a third surface?" question is parked pending
   charter §3.1 surface-expansion review.

## Telegram interaction

None. This is a passive observation; no cook or manager action.

## Dependencies

- `$HERMES_GITHUB_TOKEN` for the daily direct-repo GET (already in
  `/opt/data/.env`).

## Open questions

- Does the `ezdmb` README confirm the single-purpose Python display
  pattern with a documented configuration surface?
- Does the `ezdmb` data model include a `MenuItem` table that LE31
  could compare against feature 02 (`MenuItem`) + feature 11
  (customer-qr-menu)?
- Is the "add a front-of-house display surface" question on the LE31
  charter roadmap? If yes, this pick becomes a build candidate. If
  no, the pick stays parked.

## Why this matters

The `ezdmb` peer proves a single-purpose Python display surface is
**buildable in ★25 by a solo developer**. The pattern is method-
adjacent (Python display, minimal config) but not domain-adjacent
(ezdmb is menu-board, not restaurant-POS). The cross-section question
("should LE31 v2 grow a third surface?") is a charter-level
surface-expansion question that the artifact explicitly defers. The
pick is filed as a parking-lot entry with a clear re-evaluation
trigger so the next research pass knows what to look for.
