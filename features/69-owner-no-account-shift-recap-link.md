# Feature 69 — Owner No-Account Shift Recap Link

> **Priority**: P2 · **Effort**: S (≤3 days) · **Source**: brainstorm 2026-08-15
> (cross-section pick C) · **Bucket**: v2 owner-pains
> **One-line**: A new `/recap` command on the existing cook bot that returns a
> signed expiring link — same primitive as feature 29's `/ownerlink` — but the
> link opens a printable, PDF-able **end-of-shift recap page**: today's covers
> (count + total EUR), voids with reasons (feature 37), top 3 movers, tomorrow's
> prep alerts (feature 26), and the day's shift journal (feature 67). The owner
> can print the page or hit "Save as PDF" (browser-native); the page is also
> Telegram-shareable as a single PDF attachment. No new account, no install, no
> Telegram required (the link works in any browser, like
> `Sreenivas-Sadhu-Prabhakara/slipbook`'s "no sign-up, make a clean invoice in
> under a minute" pattern).

## Goal

Close the LE31 owner's end-of-week friction: *the owner wants to file today's
recap with the accountant or store it in a physical folder at the end of the
week, but feature 39's Telegram recap is a push that disappears in chat and
feature 29's live link is too noisy for a printed artifact.* The owner wants
a printable single-page recap with covers / voids-with-reasons / top 3 movers /
tomorrow's prep alerts — exactly the `Sreenivas-Sadhu-Prabhakara/slipbook`
shape ("make a clean invoice in under a minute, then print or save as PDF").

Inspired by today's brainstorm: GitHub `topic:small-business` repo
`Sreenivas-Sadhu-Prabhakara/slipbook` (pushed **2026-08-15T03:05:35Z**, 0★,
"Free invoice & receipt maker, no sign-up. Make a clean invoice in under a
minute, then print or save as PDF. Private, offline, nothing leaves your
device."). Same author as feature 29's inspiration; the **printable-PDF
dimension** is fresh today because the repo was just pushed and it
specifically targets the "no sign-up invoice / receipt" shape that the
owner's end-of-shift recap is the small-restaurant equivalent of. The HN
solo-founder SaaS cluster (objectID 49181766, 13 pts — up from 7 pts at the
2026-08-06 brainstorm) reinforces the indie-SaaS "what needs me right now"
pattern.

This feature **depends on features 29, 37, 39** — reuses the `OwnerLink`
token from 29, the `rationale` column from 37, the `OwnerRecap` body from
39. The contract will list all three as prerequisites and will refuse to
ship without them.

## Evidence / JTBD

When the owner wants to file today's recap with the accountant or store it
in a physical folder at the end of the week, the owner wants a printable
single-page recap with covers / voids-with-reasons / top 3 movers /
tomorrow's prep alerts, but struggles because feature 39's Telegram recap
is a push that disappears in chat and feature 29's live link is too noisy
for a printed artifact, so that a `/recap` command on the cook bot returns
a signed expiring link to a printable end-of-shift recap page that the
owner can print or save as PDF.

## Scope

**In scope (v2 owner-pains):**
- A new cook-bot command `/recap [<date>]` (no args = today; with date =
  that day's recap; date must be within the last 30 days) that returns a
  single signed URL of the form
  `https://<host>/owner/<token>/recap/<date>`. The token is a `secrets`
  `token_urlsafe(32)` string, signed with the existing `SECRET_KEY`
  (charter §3.2). The token is hashed (SHA-256) and stored in the same
  `OwnerLink` row (feature 29) with `expires_at = now() + 12h`. The raw
  token is only in the URL; the database only stores the hash.
- A new FastAPI route `GET /owner/<token>/recap/<date>` that renders a
  single-page printable Jinja2 template (`owner_recap.html`) with the
  end-of-shift recap:
  1. **Header**: restaurant name, date, EUR totals header.
  2. **Covers**: number of paid orders + total EUR (from `Order.total_eur`).
  3. **Voids with reasons**: list of today's negative `StockEntry` rows
     with `rationale` populated (from feature 37), grouped by
     `menu_item_id`.
  4. **Top 3 movers**: top 3 `menu_item`s by revenue (from `OrderItem`).
  5. **Tomorrow's prep alerts**: items at-or-below `reorder_point` (from
     feature 26).
  6. **Shift journal** (feature 67): the day's chronological
     `ShiftJournalNote` rows, abbreviated (one line per note).
  7. **Footer**: `Reply /ack to dismiss, or /explain <N> to drill in` —
     same primitive as feature 39.
- The page is browser-printable with `@media print` styles; no
  server-side PDF generation. Matches `slipbook`'s "browser-native Save as
  PDF" pattern.
- The page is Telegram-shareable as a single PDF attachment (the owner
  uses the browser's "Save as PDF" → "Share to Telegram" flow on a phone;
  no new Telegram send-message code needed).
- The owner-only chat-id allowlist is reused from feature 39
  (`OWNER_TELEGRAM_CHAT_IDS`); `/recap` is refused for non-owner chat-ids.

**Out of scope (v2 owner-pains):**
- Server-side PDF generation — browser-native print is sufficient and
  matches `slipbook`'s pattern.
- Weekly or monthly rollups — daily only in v1.
- Email delivery of the recap — out of scope; the link is shareable by
  any means the owner prefers.
- Edit / sign-off from the printable page — out of scope; the recap is
  read-only.
- Per-item revenue breakdown beyond top 3 — full report is one click away
  in the manager dashboard.

## User flow

**Owner — requests the recap at end-of-shift:**

1. From the cook bot, owner replies `/recap`. Bot replies with the recap
   URL: `https://<host>/owner/<token>/recap/2026-08-15`.
2. Owner opens the URL on any phone. Page renders with the seven sections
   (header / covers / voids-with-reasons / top 3 movers / tomorrow's prep
   alerts / shift journal / footer).
3. Owner taps "Print" or "Save as PDF". The browser prints or saves the
   page as a single PDF.
4. Owner shares the PDF with the accountant via email or stores it in a
   physical folder.

**Owner — requests a recap for a specific date:**

1. Owner replies `/recap 2026-08-10`. Bot replies with the recap URL for
   that date (provided the date is within the last 30 days; older dates
   return 410 Gone with a friendly "recaps older than 30 days are not
   available; ask the cook bot for a fresh daily recap" message).

**Owner — opens the link the next morning:**

1. The link has expired. Page returns 410 Gone with a friendly "this link
   expired; ask the cook bot for a new one" message. The owner can request
   a fresh `/recap` from the cook bot.

**Non-owner requests `/recap`:**

1. Cook replies `/recap`. Bot replies "owner-only command" (same primitive
   as feature 39's `/ack` and `/explain <N>`).

## Data model

No new tables. Reuses:

- `OwnerLink` (feature 29) — the signed expiring token.
- `Order.total_eur` (existing) — the covers count + EUR total.
- `StockEntry.rationale` (feature 37) — the voids-with-reasons list.
- `OrderItem` (existing) — the top 3 movers.
- `MenuItem.reorder_point` (feature 26) — the tomorrow's prep alerts.
- `ShiftJournalNote` (feature 67) — the shift journal section.
- `OWNER_TELEGRAM_CHAT_IDS` (feature 39) — the owner-only chat-id
  allowlist.

## API / bot / UI contract

**Bot (aiogram v3, existing webhook from feature 04):**
- New command: `/recap [<date>]` — owner-only (chat-id in
  `OWNER_TELEGRAM_CHAT_IDS`).
- The `/recap` command creates a new `OwnerLink` row (same primitive as
  feature 29's `/ownerlink`) and returns the recap URL.
- The bot replies with the recap URL, not the recap body (the URL is the
  shareable surface; the recap body is rendered in the browser, not in
  Telegram).

**API (FastAPI):**
- New route: `GET /owner/<token>/recap/<date>` — renders `owner_recap.html`.
- The route validates the `OwnerLink` token (hash + 12h expiry); 410 Gone
  on miss/expired.
- No new HTTP routes on the authenticated waiter/cook/manager surface.

**Templates:**
- `backend/app/templates/owner_recap.html` — single-page printable recap;
  `@media print` styles; htmx loaded from CDN; no nav, no auth UI.

## Dependencies

- **No new pip dependencies.** Jinja2 is already imported for feature 29's
  `owner.html`.
- **Required upstream features**:
  - feature 29 (`owner-no-account-live-floor-link`) — supplies the
    `OwnerLink` token primitive. Without 29, there is no signed expiring
    URL surface to build the recap on. This contract **lists 29 as a
    prerequisite and will refuse to ship without it**.
  - feature 37 (`void-rationale-ledger-field`) — supplies the `rationale`
    column on `StockEntry` for the voids-with-reasons section.
  - feature 39 (`owner-daily-recap-telegram`) — supplies the
    `OwnerRecap` body, the `OWNER_TELEGRAM_CHAT_IDS` config field, and
    the owner-only chat-id allowlist primitive.
  - feature 67 (`solo-operator-shift-journal-pwa`) — supplies the
    `ShiftJournalNote` rows for the shift journal section. **Soft
    dependency** — if 67 is not yet built, the recap renders without the
    shift journal section (the recap still works).
  - feature 26 (`reorder-point-on-stockentry`) — supplies the
    `reorder_point` query for the tomorrow's prep alerts section.

## Failure / recovery

- **`OwnerLink` token expired or unknown** — route returns 410 Gone with a
  friendly message. The owner can re-request a link from the cook bot.
- **Date is older than 30 days** — route returns 410 Gone with a friendly
  message.
- **Cook bot is down / webhook broken** — the recap route is independent
  of the bot webhook for *reading*; reading always works as long as
  FastAPI is up. Requesting a fresh `/recap` link requires the bot.
- **Time zone misconfiguration** — `<date>` is computed in `Europe/Paris`
  at insert time and at query time; no manual offset math. DST transitions
  handled by the same `ZoneInfo("Europe/Paris")` as feature 39.
- **No data for the date (closed day)** — recap renders with a friendly
  "Closed today — see you tomorrow" header and zero entries for every
  section. No noise.

## Definition of done

- [ ] Cook bot `/recap [<date>]` command shipped; owner-only chat-id
      allowlist enforced.
- [ ] FastAPI route `GET /owner/<token>/recap/<date>` shipped.
- [ ] `owner_recap.html` template shipped with the seven sections (header /
      covers / voids-with-reasons / top 3 movers / tomorrow's prep alerts /
      shift journal / footer); `@media print` styles verified.
- [ ] End-to-end observed: owner types `/recap` → opens the recap URL →
      page renders with the seven sections → owner taps "Save as PDF" →
      PDF saves cleanly → owner shares the PDF with the accountant.
- [ ] Existing tests still green.
- [ ] Manual acceptance: in a 7-day pilot, the owner requests the recap
      every evening, prints or PDFs each day's recap, and zero unintended
      noise happens (no recap with missing rationale, no recap on a
      closed day with stale data).

## Open questions

- Should the recap include a revenue breakdown by payment method (cash vs
  card vs other)? Decision: not for v1; out of scope. Could be a one-line
  addition later (uses the existing `Bill.payment_method` column from
  feature 05).
- Should the recap show the day's *reservation list*? Decision: not for
  v1; out of scope. Could be a one-line addition later.
- Should the recap include a "what was 86ed today" summary line? Decision:
  yes — covered by the voids-with-reasons section if rationale is
  populated; if not, the recap shows "(legacy — no rationale recorded)"
  (same primitive as feature 39).

## Why this matters

LE31's solo operator is also the same person who runs the floor and manages
the books. The end-of-week paperwork is the friction the operator cites
most often in any pilot — handing the accountant a stack of printed recaps
is the weekly ritual. Today feature 39's Telegram recap is a *push* that
disappears in chat; feature 29's live link is a *pull* that is too noisy
for a printed artifact. Neither is the printable single-page recap the
owner wants to file.

`Sreenivas-Sadhu-Prabhakara/slipbook` (pushed today 2026-08-15) is the same
author's "no sign-up invoice / receipt maker" pattern that inspired feature
29 two weeks ago; the **printable PDF dimension** is fresh today because
the repo was just pushed and it specifically targets the "no sign-up,
printable, browser-native" shape. The HN solo-founder SaaS cluster
(objectID 49181766, 13 pts) is the indie-founder monthly-recap
transparency thread applied to a *single-day printable* surface — the
owner wants the same recurring filing ritual for the day's recap as the
founder wants for the month's MRR.

Translated to LE31, this is the missing printable end-of-shift recap that
sits *beside* (not replaces) feature 29's live link and feature 39's
Telegram push recap. Tiny cost (one new bot command + one new route + one
Jinja2 template), high value (the solo-operator's most-cited end-of-week
friction: "I want to file today's recap, not just see it on Telegram").
Depends on features 29, 37, 39 (hard) and 67 (soft).
