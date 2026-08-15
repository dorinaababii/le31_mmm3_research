# owner-no-account-shift-recap-link — HANDOFF

> **Slice for the coding agent.** Read this *and*
> `features/69-owner-no-account-shift-recap-link.md` before touching any code.
> Do not paste chat excerpts back into the build.

## Frozen identifiers (do not rename)

- Feature ID: `69`
- Slug: `owner-no-account-shift-recap-link`
- Contract file: `features/69-owner-no-account-shift-recap-link.md`
- Bucket: v2 owner-pains (printable end-of-shift recap; no new client)
- Linear parent: see Brainstorm 2026-08-15 — daily issue
- Linear sub-issue: see `le31 v2 owner-pains` project, label `Feature`

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md` — all seven checks answered in the
contract file under "Why this matters" and the body of the report.
**Decision: build** (with features 29, 37, 39 as hard prerequisites and 67 as
a soft prerequisite). No failed checks.

Evidence precondition: **observed** (1 in-window GitHub repo pushed today —
`Sreenivas-Sadhu-Prabhakara/slipbook` pushed 2026-08-15T03:05:35Z — shares
the no-account printable-PDF micro-tool primitive; HN solo-founder SaaS
cluster at objectID 49181766 (13 pts) reinforces). Confidence: **high**.

## Mandatory LE31 skill list (load these first)

External coding agent MUST load before starting:

1. `le31-conventions` (project invariants + the seven-check gate).
2. `le31-v1-feature-pattern` (canonical contract shape + slicing rules).
3. `le31-handoff-spec` (frozen-contract discipline; mirror contract back).
4. `le31-daily-brainstorm` (this pick came from the daily brainstorm job).
5. `le31-feature-pipeline` (so the agent understands how this slice will
   be sequenced after it ships).

If the destination repo does not yet ship these skills, request them from
the research-side Hermes instance before writing code.

## Files the slice touches

```
backend/app/main.py                                            # NEW: FastAPI route registration (1 route)
backend/app/bot/cook_bot_recap.py                              # NEW: /recap [<date>] command handler (owner-only chat-id allowlist)
backend/app/templates/owner_recap.html                         # NEW: printable end-of-shift recap Jinja2 template
backend/README.md                                              # note the new route + /recap command
```

No new pip dependencies. Jinja2 is already imported for feature 29's
`owner.html`.

## Endpoints and contracts added

One new FastAPI route:

- `GET /owner/<token>/recap/<date>` — renders `owner_recap.html` with the
  seven sections (header / covers / voids-with-reasons / top 3 movers /
  tomorrow's prep alerts / shift journal / footer); `@media print` styles
  for the printable surface.

The route validates the `OwnerLink` token (hash + 12h expiry); 410 Gone on
miss/expired. The route validates `<date>` is within the last 30 days;
410 Gone on older dates.

One new bot command (owner-only):

- `/recap [<date>]` — chat-id in `OWNER_TELEGRAM_CHAT_IDS`; no args =
  today; with date = that day's recap. Creates a new `OwnerLink` row (same
  primitive as feature 29's `/ownerlink`) and returns the recap URL.

One new Jinja2 template:

```html
<!-- backend/app/templates/owner_recap.html -->
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>LE31 Recap — {{ date }}</title>
  <style>
    body { font-family: -apple-system, BlinkMacSystemFont, sans-serif; max-width: 720px; margin: 24px auto; padding: 0 16px; color: #111; }
    h1 { font-size: 20px; margin: 0 0 4px; }
    h2 { font-size: 14px; margin: 24px 0 8px; color: #555; text-transform: uppercase; letter-spacing: 0.05em; }
    .section { border-top: 1px solid #ddd; padding-top: 8px; }
    .footer { margin-top: 32px; padding-top: 8px; border-top: 1px solid #ddd; color: #777; font-size: 12px; }
    @media print {
      body { max-width: none; margin: 0; padding: 0; }
      .no-print { display: none; }
    }
  </style>
</head>
<body>
  <h1>{{ restaurant_name }} — Recap {{ date }}</h1>
  <div class="section">
    <h2>Covers</h2>
    <p>{{ covers_count }} orders · €{{ "%.2f"|format(covers_total_eur) }}</p>
  </div>
  <div class="section">
    <h2>Voids with reasons ({{ voids_count }})</h2>
    {% for v in voids %}
      <p>• {{ v.menu_item_name }} — {{ v.qty_delta }} — "{{ v.rationale }}"</p>
    {% endfor %}
  </div>
  <div class="section">
    <h2>Top 3 movers</h2>
    {% for m in top_movers %}
      <p>{{ loop.index }}. {{ m.menu_item_name }} — {{ m.qty }} orders · €{{ "%.2f"|format(m.revenue_eur) }}</p>
    {% endfor %}
  </div>
  <div class="section">
    <h2>Tomorrow's prep alerts ({{ prep_alerts_count }})</h2>
    {% for p in prep_alerts %}
      <p>• {{ p.menu_item_name }} — {{ p.remaining_qty }} {{ p.unit }} remaining</p>
    {% endfor %}
  </div>
  {% if shift_journal %}
  <div class="section">
    <h2>Shift journal</h2>
    {% for sj in shift_journal %}
      <p>{{ sj.created_at | datetime_format }} — [{{ sj.kind }}] {{ sj.body }}</p>
    {% endfor %}
  </div>
  {% endif %}
  <div class="footer">
    Reply /ack to dismiss, or /explain &lt;N&gt; to drill in.
  </div>
</body>
</html>
```

## Verification

1. `/recap` unit test — verify the bot replies with a signed URL whose
   hashed token matches the new `OwnerLink` row, with `expires_at` set to
   12h ahead.
2. `GET /owner/<token>/recap/2026-08-15` end-to-end — verify the page
   renders with the seven sections; `@media print` styles hide nav and
   other UI; the page is single-column when printed.
3. Owner-only allowlist test — `/recap` from a non-owner chat-id returns
   "owner-only command".
4. Expired-token test — `OwnerLink.expires_at` in the past → route returns
   410 Gone.
5. Old-date test — `GET /owner/<token>/recap/2025-01-01` → 410 Gone with a
   friendly message.
6. Closed-day test — `GET /owner/<token>/recap/<closed-day>` → page
   renders with a friendly "Closed today — see you tomorrow" header and
   zero entries for every section.
7. DST transition test — at the spring-forward boundary (last Sunday of
   March), `day_date` is computed in `Europe/Paris` correctly.
8. Existing tests still green.

## Rollback path

Set `OWNER_TELEGRAM_CHAT_IDS=` (empty) and remove the `/recap` command
registration in `.env` — the recap route is unreachable from the cook bot
but the existing `/ownerlink` live-floor URL still works. To fully
rollback: remove the new files, remove the new route. No upstream feature
is broken by removing this.

## Dependencies

- No new pip dependencies.
- **Required upstream features**:
  - feature 29 (`owner-no-account-live-floor-link`) — supplies the
    `OwnerLink` token primitive. This contract **lists 29 as a hard
    prerequisite and will refuse to ship without it**.
  - feature 37 (`void-rationale-ledger-field`) — supplies the `rationale`
    column on `StockEntry` for the voids-with-reasons section.
  - feature 39 (`owner-daily-recap-telegram`) — supplies the `OwnerRecap`
    body, the `OWNER_TELEGRAM_CHAT_IDS` config field, and the owner-only
    chat-id allowlist primitive.
  - feature 26 (`reorder-point-on-stockentry`) — supplies the
    `reorder_point` query for the tomorrow's prep alerts section.
  - feature 67 (`solo-operator-shift-journal-pwa`) — **soft dependency**
    — supplies the `ShiftJournalNote` rows for the shift journal section.
    If 67 is not yet built, the recap renders without the shift journal
    section (the recap still works).
- **Required downstream features**: none.
