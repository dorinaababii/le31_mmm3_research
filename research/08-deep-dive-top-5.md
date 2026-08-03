# Deep-Dive: Top 5 Open-Source Projects to Fork or Extend

After the broad sweep, these are the projects worth serious consideration.
Each gets a verdict: **fork**, **extract-pattern**, **library-only**, or **skip**.

---

## 1. TastyIgniter (https://github.com/tastyigniter/TastyIgniter) — verdict: **skip**

**Why it's interesting**
- Most popular dedicated open-source restaurant platform (3.6k⭐, MIT).
- Full Laravel app: menu, orders, reservations, customers, locations.
- Multi-language (EN/ES/etc.), multi-currency.

**Why we should not fork it**
- It's a full Laravel app — we'd inherit Twig templating, MySQL, npm build
  chain, and a deeply opinionated admin panel.
- It has **no Telegram integration** and **no first-class prepared-item stock**.
- Adding those features means fighting the framework at every layer.

**What we should copy**
- Their `Menu → Category → MenuItem` data model.
- Their modifier / option group design pattern.

---

## 2. URY (https://github.com/ury-erp/ury) + URY Mosaic (https://github.com/ury-erp/mosaic) — verdict: **extract-pattern**

**Why it's interesting**
- Built on ERPNext/Frappe — gets real inventory, batches, BOM, accounting for free.
- Mosaic is a dedicated Python KDS for URY.
- Active development, 318⭐ on the main repo, 45⭐ on Mosaic.

**Why we should not fork it**
- Requires a Frappe/ERPNext install (Python + MariaDB + Redis + Node + bench CLI).
  The smallest Frappe install is ~2 GB of disk and nontrivial ops.
- AGPL-3.0 license — fine for self-hosted single-tenant, but heavy.

**What we should copy**
- **Mosaic's order ticket lifecycle** (new → preparing → ready → served → bumped).
- **ERPNext's Batch + StockEntry ledger** pattern (already documented in
  [03-inventory-stock.md](./03-inventory-stock.md)).
- URY's "menu of the day" concept with `available_from/until` timestamps.

---

## 3. evan361425/flutter-pos-system (https://github.com/evan361425/flutter-pos-system) — verdict: **extract-pattern**

**Why it's interesting**
- Mobile-first POS built in Flutter/Dart (488⭐, Apache-2.0).
- Already tracks **customer demographics including gender** — matches our spec.
- Single-tenant, small enough to read end-to-end.

**Why we should not fork it**
- Flutter is great for mobile but our kitchen-side is Telegram (already a
  chat app) — no need for a custom mobile UI.
- Database is SQLite; we'd want Postgres.

**What we should copy**
- Customer entity shape: `name`, `gender`, `phone`, `email`.
- Table-side UI flow: tap table → tap item → confirm → send to kitchen.
- The "bump bar" UX for marking items ready.

---

## 4. RestoPOS (https://github.com/faizaldevs/RestoPOS) — verdict: **skip**

**Why it's interesting**
- Laravel + Vue + multi-tenant SaaS pattern (Stancl Tenancy).
- 100⭐, MIT, active in 2025.

**Why we should not fork it**
- Multi-tenant complexity is irrelevant for one restaurant.
- No Telegram integration, no prepared-item stock, no analytics.

**What we should copy**
- Their AdminLTE-inspired admin panel layout (looks clean).
- Print-template approach for receipts (HTML → thermal printer).

---

## 5. Nishiki (https://github.com/nishiki-tech/nishiki-frontend) — verdict: **extract-pattern**

**Why it's interesting**
- Specifically about food inventory tracking (24⭐, MIT, TS).
- React Native + TypeScript frontend; backend is likely separate (not fetched).
- Closest in spirit to our "batch / prepared items" model.

**Why we should not fork it**
- Small community, modest star count.
- React Native frontend doesn't fit Telegram-driven kitchen.

**What we should copy**
- "Food group / container" entity concept (similar to a Batch).
- "Sharing" model — multiple kitchens/users seeing the same inventory.
- The way they model expiry dates on prepped items.

---

## Honorable mentions (worth knowing exist)

- **CampusBites** — full-stack canteen system; TypeScript + Next.js-style. Read for the data model.
- **harismuneer/Restaurant-Management-System** — Java/Android, has analytics dashboard, useful for UI inspiration.
- **OpenKDS** — minimal Node/EJS KDS, useful as a starting point if we ever build a screen-based KDS.

---

## The single best path forward

**Build a fresh, thin Python app** with:
- **FastAPI** for the HTTP/JSON API (dining-service side).
- **aiogram** for the Telegram bot (kitchen side).
- **PostgreSQL** for persistence (with the Batch + StockEntry ledger pattern from URY/ERPNext).
- **index.html** as the first UI mock-up, served by the same FastAPI app.
- **RapidOCR + LLM post-processing** for menu-photo digitization.

This is far less code (~5k lines) than forking any existing project, fits
the user's two-role split cleanly, and avoids inheriting opinionated frameworks.

See [09-recommended-stack.md](./09-recommended-stack.md) for the architecture sketch.