# Feature 08 — index.html Mock-up (Visualization Prototype)

## Goal

A static HTML page that visualizes what the app *will* look like, before
writing any backend. Lets the user iterate on UX quickly and serves as a
visual contract for the implementation phase.

## Scope

**In scope (v1):**
- Single `index.html` file with inline CSS + JS (no build step).
- Mock data hard-coded in JS — fake tables, fake menu, fake orders.
- Three views selectable via tabs or hash-routing:
  1. **Floor view** — table grid, color-coded by status.
  2. **Order view** — current visit's items + menu picker.
  3. **Reports view** — manager dashboard cards + a couple of charts.
- Optional: a 4th view that simulates the Telegram bot conversation (chat
  bubbles in a fake phone frame) so the user can see the cook-side UX too.

**Out of scope (v1):**
- Real backend wiring.
- User authentication.
- Persistence (refresh = back to mock data).

## Description

A pure-static HTML file that anyone can open in a browser. Three or four
"pages" (divs toggled by JS). Tasteful typography, generous spacing, mobile-
responsive so it previews well on a phone. The point is to make the data
model and workflow *concrete* before committing to a stack.

## File location

```
index.html          ← entry point (project root)
```

Or:
```
docs/mockups/v1/index.html
```

(Open question — see below.)

## Sections (tabs)

1. **Floor** — grid of tables with status colors, click a table to "seat" a party.
2. **Order** — split-pane: menu left, current order right, bill button at bottom.
3. **Reports** — covers today, top items, dwell time histogram.
4. **Bot** — fake Telegram conversation for the cook's morning setup.

## Mock data (hard-coded JS)

```js
const MOCK_MENU = [
  { id: 1, name: 'Schnitzel', price: 14, category: 'Mains', prepared: true, stock: 18 },
  { id: 2, name: 'Burger',    price: 12, category: 'Mains', prepared: true, stock: 15 },
  { id: 3, name: 'Tiramisu',  price:  6, category: 'Desserts', prepared: true, stock: 6 },
  // ...
];

const MOCK_TABLES = [
  { id: 1, label: 'T1', section: 'main', status: 'free',   seats: 4 },
  { id: 2, label: 'T2', section: 'main', status: 'seated', seats: 4, party: 4 },
  // ...
];
```

## Style guide (for consistency)

- **Color tokens** (CSS variables):
  - `--status-free: #10b981` (green)
  - `--status-seated: #f59e0b` (amber)
  - `--status-ordered: #f97316` (orange)
  - `--status-billed: #ef4444` (red)
  - `--status-dirty: #6b7280` (gray)
- **Typography**: system-ui sans, generous line-height (1.5), readable on phone.
- **Density**: tap-friendly (44px min touch targets).

## Dependencies

- This is a **pure visualization**. No backend dependencies. The features
  it previews are described in 01–07.

## Open questions

- Single file vs. multi-file (separated CSS/JS)? Single is easier to share.
- Include the bot view in v1 or punt? (Punted — keep it simple.)
- Dark mode? (Probably not — adds complexity for little value in a mock-up.)

## How to view

Just open `index.html` in a browser. No server needed. When the real backend
exists, the same HTML can be served by FastAPI (static files at `/`).