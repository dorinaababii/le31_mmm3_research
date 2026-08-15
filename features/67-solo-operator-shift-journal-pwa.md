# Feature 67 — Solo Operator Shift Journal PWA

> **Priority**: P2 · **Effort**: M (≤1 week) · **Source**: brainstorm 2026-08-15
> (cross-section pick A) · **Bucket**: v2 owner-pains
> **One-line**: A private, offline, no-account **shift journal** view that the
> owner opens from the same `/ownerlink` surface as feature 29 — chronological
> log of every explicit operational decision (from feature 46), every negative
> `StockEntry` with the rationale (from feature 37), every owner `/explain` reply
> (from feature 39), every reservation update, and every free-text note the owner
> types during the day. Owner can append a `ShiftJournalNote` from the same page;
> each note gets its own signed share-link so the owner can email/text a single
> note to a supplier or accountant. End-of-shift, the owner prints or saves the
> day's journal as a single PDF.

## Goal

Close the LE31 owner's middle-tier observation: *the owner often makes a policy
decision mid-service ("we 86 the lamb on slow days", "Tuesdays we open at 18:00
not 18:30", "if the chef is alone, table 6 cannot be seated") and the cook
records the event in `StockEntry` with the rationale — but the **chronological
context** that makes the decision interpretable three weeks later ("did we 86
the lamb *because* it rained that day or was it just slow?") lives in nobody's
head, in chat logs that scroll past, or on a paper notebook nobody reads.* Today
the owner has feature 39's Telegram recap (a *summary*, push-shaped) and feature
29's live link (the *current state*, pull-shaped); neither is the
*chronological journal* the owner wants for follow-up questions three weeks
later.

Inspired by today's brainstorm: GitHub `topic:small-business` repo
`Sreenivas-Sadhu-Prabhakara/slotone` (pushed **2026-08-15T03:05:39Z**, 0★, "A
private, offline appointment day-book for a one-person business. No accounts,
no network."). Same author as feature 29's inspiration; the **day-book
dimension** is fresh today because the repo was just pushed and it specifically
targets a single-person business's daily log. The HN solo-founder-saas cluster
(objectID 49181766, 13 pts — up from 7 pts at the 2026-08-06 brainstorm)
reinforces the indie-SaaS "what needs me right now" pattern that the owner's
chronological journal is the small-restaurant equivalent of.

This feature **depends on feature 29 (`owner-no-account-live-floor-link`)** —
reuses the `OwnerLink` token primitive. The contract will list 29 as a
prerequisite and will refuse to ship without it.

## Evidence / JTBD

When the owner wants to remember why a decision was made three weeks from now
(a supplier dispute, a tax query, an owner-couple argument about "did we 86 the
lamb that day"), the owner wants a chronological journal of today's decisions
and notes, but struggles because the live link (feature 29) only shows the
*current* state and the daily Telegram recap (feature 39) is a *summary*, not
a journal, so that a printable per-day journal view from the same no-account
link makes "what did we decide on 2026-08-15?" answerable in one grep + one
print.

## Scope

**In scope (v2 owner-pains):**
- A new append-only `ShiftJournalNote` SQLModel table
  `(id, ownerlink_id, day_date, kind, body, created_at, created_by_chat_id)`
  where `kind` is one of `decision`, `void`, `explain`, `reservation`, `note`,
  and `body` is a short markdown string.
- A new FastAPI route `GET /owner/<token>/journal/<date>` that renders a
  chronological Jinja2 template (`owner_journal.html`) showing every
  `ShiftJournalNote` for that date, in `created_at` order, grouped by `kind`.
  Each note renders with the time, the kind tag, and the body. Same htmx +
  CSS as feature 29's `owner.html`.
- A new FastAPI route `POST /owner/<token>/journal/<date>` that appends a new
  `ShiftJournalNote` of `kind=note` with `body=<free-text>` from a single
  textarea at the bottom of the journal page. The form is signed by the same
  `OwnerLink` token; no CSRF token needed (the signed URL is the auth).
- A new FastAPI route `GET /owner/<token>/journal/<date>/note/<note_id>` that
  returns a printable single-note page (a printable share-link for one note).
  Same `OwnerLink` token check; same 12h expiry.
- One new module `backend/app/services/shift_journal.py` that composes the
  journal from existing append-only tables (`DecisionNote` from feature 46,
  `StockEntry.rationale` from feature 37, `OwnerRecap` rows from feature 39,
  `Reservation` rows) plus the new `ShiftJournalNote` table. **No duplication**
  — the journal view is composed from existing rows; the new table only
  stores owner-typed notes.
- The cook bot's existing `/ownerlink` command gains a second URL: the link
  returned now points to `/owner/<token>/journal/<today>` (the journal view)
  instead of `/owner/<token>` (the live floor view). The original live-floor
  URL is reachable as `/owner/<token>` (unchanged) and the journal is the new
  default landing.
- One new `printable.journal.html` Jinja2 template that renders the journal
  page in a print-friendly layout (single column, no nav, monospace time,
  `@media print` styles). The page is browser-printable; no server-side PDF
  generation (the browser's "Save as PDF" is sufficient and matches
  `Sreenivas-Sadhu-Prabhakara/slipbook`'s "make a clean invoice in under a
  minute" pattern).

**Out of scope (v2 owner-pains):**
- Weekly or monthly rollups — daily only in v1.
- Per-note attachments (out of scope for the first slice; defer to v3).
- Multi-owner journals (one journal per `OwnerLink`; the owner allowlist stays
  the same as feature 39).
- Editing or deleting notes — the journal is append-only.
- Server-side PDF generation — browser-native print is sufficient.

## User flow

**Owner — opens the journal at end-of-shift:**

1. From the cook bot, owner replies `/ownerlink` (existing command from
   feature 29).
2. Bot replies with the journal URL: `https://<host>/owner/<token>/journal/2026-08-15`.
3. Owner opens the URL on any phone. Page renders with the day's chronological
   journal: decisions (from feature 46), voids with reasons (from feature 37),
   `OwnerRecap` body (from feature 39), reservation updates, and any
   owner-typed notes.
4. Owner types a free-text note in the textarea at the bottom, hits "Add
   note". A new `ShiftJournalNote` row is appended (kind=`note`).
5. Owner taps "Print" or "Save as PDF". The browser prints the page.

**Owner — shares one note with the supplier:**

1. Owner taps "Share" on any note in the journal page.
2. Browser navigates to `/owner/<token>/journal/<date>/note/<note_id>` — a
   single-note printable view.
3. Owner emails or texts the URL to the supplier. The supplier sees a clean
   single-note page with the time, the kind, and the body.
4. The URL expires after 12h (same `OwnerLink` token expiry as feature 29).

**Owner — opens the link the next morning:**

1. The link has expired. Page returns 410 Gone with a friendly "this link
   expired; ask the cook bot for a new one" message.

## Data model

One new table:

```python
# backend/app/models.py (additive)

class ShiftJournalNote(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    ownerlink_id: int = Field(foreign_key="ownerlink.id", index=True)
    day_date: date = Field(index=True)
    kind: str = Field(max_length=20)  # 'decision' | 'void' | 'explain' | 'reservation' | 'note'
    body: str = Field(max_length=2000)
    created_at: datetime = Field(default_factory=lambda: datetime.now(ZoneInfo("Europe/Paris")))
    created_by_chat_id: int | None = Field(default=None)
```

`ShiftJournalNote` is append-only (same SQLAlchemy listener as `StockEntry`,
`OwnerAuditEvent`, `OwnerRecap`). No `UPDATE` or `DELETE` paths exist.

No changes to existing models. Reuses `OwnerLink` (feature 29), `DecisionNote`
(feature 46), `StockEntry.rationale` (feature 37), `OwnerRecap` (feature 39).

## API / bot / UI contract

**Bot (aiogram v3, existing webhook from feature 04):**
- No new bot commands. The existing `/ownerlink` command (feature 29) is
  patched to return the *journal* URL instead of the *live floor* URL. The
  live floor URL is still reachable as `/owner/<token>` (unchanged).

**API (FastAPI):**
- New routes:
  - `GET /owner/<token>/journal/<date>` — renders `owner_journal.html`
  - `POST /owner/<token>/journal/<date>` — appends a `ShiftJournalNote`
  - `GET /owner/<token>/journal/<date>/note/<note_id>` — renders a single
    note (printable share-link)
- All three routes validate the `OwnerLink` token (hash + 12h expiry); 410 Gone
  on miss/expired.
- No new HTTP routes on the authenticated waiter/cook/manager surface.

**Templates:**
- `backend/app/templates/owner_journal.html` — chronological view, htmx
  loaded from CDN, `@media print` styles for the printable surface.
- `backend/app/templates/owner_journal_note.html` — single-note printable
  view, no nav, monospace time.

## Dependencies

- **No new pip dependencies.** Jinja2 is already imported for feature 29's
  `owner.html`.
- **Required upstream features**:
  - feature 29 (`owner-no-account-live-floor-link`) — supplies the
    `OwnerLink` token primitive. Without 29, there is no signed expiring URL
    surface to build the journal on. This contract **lists 29 as a
    prerequisite and will refuse to ship without it**.
  - feature 46 (`havemind-decision-notes`) — supplies the `DecisionNote`
    rows that compose into the journal.
  - feature 37 (`void-rationale-ledger-field`) — supplies the `rationale`
    column on `StockEntry`.
  - feature 39 (`owner-daily-recap-telegram`) — supplies the `OwnerRecap`
    rows.
- **Required downstream features**:
  - feature 68 (`owner-no-account-shift-recap-link`) — uses the journal as
    the body of the printable end-of-shift recap.

## Failure / recovery

- **`OwnerLink` token expired or unknown** — route returns 410 Gone with a
  friendly message. The owner can re-request a link from the cook bot.
- **`ShiftJournalNote` insert fails (DB error)** — route returns 500 with a
  "try again" message; the journal view re-renders with the existing notes
  unchanged (the failed insert is not partially committed).
- **Cook bot is down / webhook broken** — the journal route is independent
  of the bot webhook for *reading*; reading always works as long as FastAPI
  is up. Writing a note requires the bot (only to get a fresh link).
- **Time zone misconfiguration** — `day_date` is computed in `Europe/Paris`
  at insert time and at query time; no manual offset math. DST transitions
  handled by the same `ZoneInfo("Europe/Paris")` as feature 39.
- **Owner opens a date with no notes** — page renders with a friendly "no
  notes for this day" message and the textarea still works.

## Definition of done

- [ ] `ShiftJournalNote` table added; append-only listener extended.
- [ ] FastAPI routes `GET /owner/<token>/journal/<date>`, `POST
      /owner/<token>/journal/<date>`, `GET
      /owner/<token>/journal/<date>/note/<note_id>` shipped.
- [ ] `shift_journal.py` module shipped; composes the journal from existing
      `DecisionNote`, `StockEntry.rationale`, `OwnerRecap`, and `Reservation`
      rows plus the new `ShiftJournalNote` table.
- [ ] `owner_journal.html` and `owner_journal_note.html` templates shipped;
      `@media print` styles verified.
- [ ] Cook bot `/ownerlink` command patched to return the journal URL by
      default; live floor URL still reachable.
- [ ] End-to-end observed: owner types `/ownerlink` → opens the journal URL
      → sees the day's chronological entries → types a note → note appears →
      owner taps "Print" → browser prints a clean single-column page →
      owner shares a single-note URL → supplier opens it → page renders.
- [ ] Existing tests still green.
- [ ] Manual acceptance: in a 7-day pilot, the owner opens the journal every
      evening, prints or PDFs each day's recap, and zero unintended writes
      happen (no duplicate notes, no edits).

## Open questions

- Should the journal page show *all* entries for the day, or only the
  owner's own typed notes + the system-composed entries? Decision: show all
  (decision + void + explain + reservation + note), grouped by kind — that's
  the "chronological journal" shape; otherwise it's just a notes app.
- Should the printable view strip the "Add note" textarea? Decision: yes —
  the printable page is read-only; the owner prints after typing the note,
  not before.
- Should the `ShiftJournalNote.body` be Markdown or plain text? Decision:
  plain text — matches the bot's plain-text style (feature 39's
  `OwnerRecap.body_markdown` uses Markdown; this is plain text to keep the
  print surface minimal).

## Why this matters

LE31's solo operator is also the same person who runs the floor and manages
the books. Three weeks after the fact, the supplier dispute / tax query /
owner-couple argument all need the *same* answer: "what did we decide on
2026-08-15, and why?" Today the answer lives in Telegram chat logs that
scrolled past, in the owner's head, or on a paper notebook nobody reads.
Feature 39's Telegram recap is a *summary* (covers / voids / movers), not a
chronological journal; feature 29's live link is the *current state*, not a
historical record.

`Sreenivas-Sadhu-Prabhakara/slotone` (pushed today 2026-08-15) is the same
author's solo-operator private offline day-book pattern that inspired feature
29 two weeks ago; the **day-book dimension** is fresh today because the repo
was just pushed and it specifically targets the "single-person business's
daily log" shape. The HN solo-founder SaaS cluster (objectID 49181766, 13 pts)
is the indie-founder monthly-recap transparency thread applied to a
*single-day* surface — the owner wants the same recurring push/pull ritual
for the day's decisions as the founder wants for the month's MRR.

Translated to LE31, this is the missing chronological owner-view journal that
sits *beside* (not replaces) feature 29's live link and feature 39's daily
recap. Tiny cost (one new table + three routes + one Jinja2 template + a
`shift_journal.py` composer module), high value (the solo-operator's
follow-up-question friction: "what did we decide on 2026-08-15?"). Depends
on feature 29's `OwnerLink` token primitive.
