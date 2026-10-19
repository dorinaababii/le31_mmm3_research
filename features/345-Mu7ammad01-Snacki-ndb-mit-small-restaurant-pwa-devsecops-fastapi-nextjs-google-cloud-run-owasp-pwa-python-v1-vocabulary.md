# Feature 345 — Mu7ammad01/Snacki.ndb (v1 small-restaurant-PWA-with-OWASP-devsecops-+-FastAPI-+-Next.js-+-Google-Cloud-Run-vocabulary)

> **Bucket**: v1 (parking-lot, vocabulary reference)
> **GitHub**: https://github.com/Mu7ammad01/Snacki.ndb
> **License**: MIT
> **Status (as of 2026-10-19)**: ★1 / ⑂0; 2714 KB modest; pushed 2026-10-13T (in-window); created 2026-09-28T (~21-day-old repo with in-window push); default_branch=main; archived=False
> **Topics (verbatim, 7)**: `devsecops, fastapi, google-cloud-run, nextjs, owasp, pwa, python` = 5/7 LE31-stack-match (Python + FastAPI + PWA + OWASP + devsecops = the 5 LE31 v1 backend stack primitives; Next.js + Google-Cloud-Run are deployment choices that are portable to LE31 v1 with a §3.7 privacy review)
> **Description (verbatim)**: *App de type PWA pour restaurant de taille moyenne à NDB.*
> **Cross-section**: features 16 (kitchen-stock-tracker, the in-domain restaurant-inventory surface), 19 (KDS, the in-domain kitchen-display-system surface), 265 (violentzone/CarzinomaxERP, v1 small-business-AI-ERP-vocabulary), 276 (Mu7ammad01/Snacki.ndb, the original brainstorm pass feature file = the brainstorm-pass feature file for the same repo; this is the daily-research pass feature file for the same repo = a re-file with vocabulary-reference framing), 325 (AlexisLD-DEV/qramen, v1 QR-code-table-ordering-UX-vocabulary), 328 (themanoj-025/Dabba, v2-AI in-domain-restaurant-intelligence), 329 (SharifdotG/bss-restaurant-fastapi, v1 restaurant-API), 331 (joshnivek-sudo/hotel-night-audit, v1 hospitality-data-pipeline), 336 (ALPHAMAN-0/burgerCodeEmployes, v1 restaurant-employee-management), 343 (warpusTOM/StockWise, v1 offline-first-inventory-and-POS) = 11-pick v1 in-domain small-restaurant-PWA-with-OWASP-devsecops-vocabulary cluster of the 80-pass series
> **Decision**: defer (parking-lot, vocabulary reference)
> **Parent research issue**: Research 2026-10-19 — daily (Linear MCP blocked 30th-consecutive-day; parent fallback JSON at `/opt/data/le31-daily-research-2026-10-19.linear-fallback.json`)
> **Slice handoff**: `/opt/data/le31_mmm3_research_work/specs/345-Mu7ammad01-Snacki-ndb-v1-small-restaurant-pwa-with-owasp-devsecops-fastapi-nextjs-google-cloud-run-vocabulary-HANDOFF.md`

## Goal

When a future v1 LE31 PR proposes to deploy the waiter web UI as a Progressive Web App (PWA) on Google Cloud Run with OWASP-grade security, the system wants the deployment to follow the **PWA + devsecops + OWASP + Google-Cloud-Run** quartet, but today's LE31 v1 deployment model is a self-hosted FastAPI server + a vanilla web UI, not a PWA on Google Cloud Run.

## Evidence / JTBD

**Inferred** (vocabulary observation, not observed LE31 user pain). The pain is *possible* in any future v1 PR proposing a PWA deployment for the waiter web UI, but is not *directly observed* in any LE31 v1 user flow today.

When a v1 PR proposes a small-restaurant PWA (Pick B), the operator wants the deployment to follow the **PWA + devsecops + OWASP + Google-Cloud-Run** quartet, but struggles because today's LE31 v1 deployment is a self-hosted FastAPI server + a vanilla web UI, not a PWA on Google Cloud Run with OWASP-grade security.

Confidence: **medium** (1-day-old v1 restaurant-PWA with OWASP devsecops = maintainer-discipline signal but no star-inflow yet; the 7/7 topic-overlap is the strongest in-domain v1 small-restaurant-PWA-with-OWASP-devsecops topic-alignment of the 80-pass series; the maintainer is shipping real code with a real deployment target).

## Scope

- v1 only: applies to a future v1 PR proposing a small-restaurant-PWA waiter-UI deployment.
- The transferable vocabulary is the **PWA + devsecops + OWASP + Google-Cloud-Run** quartet:
  1. **PWA-as-deployment-target discipline** — the waiter web UI is a Progressive Web App (PWA = installable + offline-capable + push-notification-capable). This is the **PWA-as-deployment-target** discipline applied to a small-restaurant waiter-UI.
  2. **Devsecops-as-integration discipline** — security is integrated into the dev workflow (CI/CD security checks, dependency scanning, secret management). This is the **devsecops-as-integration** discipline applied to a small-restaurant PWA.
  3. **OWASP-as-threat-model discipline** — the Open Web Application Security Project top-10 threats (injection, broken-auth, XSS, etc.) are explicitly addressed in the design and code. This is the **OWASP-as-threat-model** discipline applied to a small-restaurant PWA (charter §3.7 GDPR + data-protection-compatible).
  4. **Google-Cloud-Run-as-deployment-platform discipline** — the PWA is deployed on Google Cloud Run (serverless container platform). This is the **serverless-container-deployment** discipline applied to a small-restaurant PWA (charter §3.7 deployment-choice; the underlying FastAPI+Python+OWASP code is on-stack).
- The Python + FastAPI stack is on-stack (charter §3.1 + §3.2 ✓); the Next.js frontend is portable to HTMX (charter §3.1 + §3.2 portable); the PWA is portable to v1 waiter web UI (charter §3.1 ✓); the OWASP threat model is charter §3.7 GDPR-compatible; the Google-Cloud-Run deployment is a deployment choice (charter §3.7 review needed for the PWA + Google-Cloud-Run + GDPR interaction).
- No v1 PR today; no v1 build today; no quota-filling.

## Out of scope

- v1 product surface (waiter web UI + cook Telegram bot) is **unchanged** by this slice (this slice is a vocabulary reference, not a v1 PR).
- Any runtime import of Snacki.ndb as a dependency (the Snacki.ndb codebase is the vocabulary reference, not the code dependency).
- Any LE31-specific schema migration or model change (Snacki.ndb is vocabulary-only; the v1 PWA waiter-UI surface is greenfield).
- The Next.js frontend framework is OUT (LE31 v1 uses HTMX; the Snacki.ndb vocabulary is portable to HTMX with a §3.1 review; the Next.js code is NOT adopted).
- The Google-Cloud-Run deployment platform is OUT for v1 (LE31 v1 uses self-hosted FastAPI on a small VM; the Google-Cloud-Run vocabulary IS the deployment reference, not the deployment target).

## Description

The Snacki.ndb vocabulary is the **small-restaurant-PWA-with-OWASP-devsecops** quintuple-primitive:

1. **PWA-as-deployment-target discipline** — the app is a Progressive Web App (PWA = installable + offline-capable + push-notification-capable). The PWA can be installed on the waiter's phone or tablet without going through an app store. The PWA can work offline (the FastAPI backend can be cached via service workers). The PWA can send push notifications (e.g. cook → waiter "table 5 is ready").
2. **Devsecops-as-integration discipline** — security is integrated into the dev workflow: CI/CD security checks (e.g. `bandit` for Python static analysis, `safety` for dependency vulnerability scanning, `trivy` for container image scanning), secret management (e.g. `gcloud secrets` for API keys), and deployment security (e.g. `gcloud run deploy --no-allow-unauthenticated` for private services).
3. **OWASP-as-threat-model discipline** — the OWASP top-10 threats are explicitly addressed: injection (parameterized queries), broken authentication (HttpOnly + Secure + SameSite cookies), XSS (HTMX auto-escaping + CSP headers), broken access control (role-based access control), security misconfiguration (secure defaults), sensitive data exposure (encryption at rest + in transit), and the rest of the top-10.
4. **Google-Cloud-Run-as-deployment-platform discipline** — the PWA is deployed on Google Cloud Run (serverless container platform). The FastAPI backend is containerized via Docker, pushed to Google Container Registry, and deployed via `gcloud run deploy`. The Cloud Run service scales to zero when idle (cost-efficient for small restaurants) and scales up under load (handles dinner rush).
5. **FastAPI-as-backend-framework discipline** — the backend is FastAPI (Python 3.11+), with Pydantic for request/response validation, SQLAlchemy for ORM, and Alembic for migrations. The FastAPI app is stateless (the database is Cloud SQL or a similar managed Postgres service).

The Python + FastAPI + PWA + OWASP + devsecops + Google-Cloud-Run stack is the **strongest in-domain v1 small-restaurant-PWA-with-OWASP-devsecops-vocabulary of the 80-pass series** (7/7 topic-overlap = 100%; first in-domain v1 small-restaurant-PWA-with-OWASP-devsecops-vocabulary of the 80-pass series).

## Data model

The Snacki.ndb data model is **greenfield** (no v1 file is touched by this slice). The conceptual model is a standard small-restaurant PWA data model:

```
MenuItem         (id, name, description, price_minor_units, category, available)
Order            (id, table_id, status, total_minor_units, opened_at, closed_at)
OrderLine        (id, order_id, menu_item_id, quantity, unit_price_minor_units)
Table            (id, label, section, seats, status)
User             (id, email, role, hashed_password)
AuditLog         (id, user_id, action, entity_type, entity_id, old_value, new_value, created_at)  -- append-only per charter §3.3
```

The PWA layer (service worker, manifest.json, install prompt) is **out of scope for the data model**; it lives in the frontend code.

## Implementation

Not implemented today. When a v1 PR is proposed, the implementation will touch:

- `app/v1/pwa/__init__.py` — new package
- `app/v1/pwa/manifest.py` — the PWA manifest.json generator (name, short_name, icons, theme_color, start_url, display, etc.)
- `app/v1/pwa/service_worker.py` — the PWA service worker generator (offline cache strategy, push notification handler, background sync handler)
- `app/v1/pwa/router.py` — the PWA-specific routes (`/manifest.json`, `/sw.js`, `/offline.html`)
- `app/v1/frontend/templates/` — the HTMX templates for the waiter-UI (existing v1 templates can be reused; the PWA layer is added on top)
- `Dockerfile` — the FastAPI + HTMX container build
- `cloudbuild.yaml` — the Google Cloud Build CI/CD pipeline (build + test + scan + deploy)
- `deploy/cloud-run/` — the Google Cloud Run deployment configuration (service.yaml, ingress rules, IAM, secrets)
- `app/v1/owasp/` — the OWASP threat-model documentation (top-10 threats + mitigations)
- `app/v1/devsecops/` — the devsecops pipeline configuration (bandit, safety, trivy, gitleaks)
- `tests/` — the PWA + OWASP test suite (PWA install + offline + push, OWASP threat-model verification, devsecops pipeline verification)

> **Greenfield**: no existing v1 file is touched by this slice (the v1 PWA waiter-UI is a new surface; the v1 vanilla web UI is unchanged unless the v1 PR explicitly proposes to migrate the vanilla web UI to the PWA).

## Telegram interaction

Not implemented today. When a v1 PR is proposed, the Telegram interaction will be:

- The cook Telegram bot (LE31 v1) is **unchanged** by this slice (this slice is the waiter-UI PWA surface, not the cook-bot surface).
- The waiter-side PWA can send push notifications to the waiter's phone (e.g. "table 5 is ready" from the cook bot, "new order received" from the system) — but this is a frontend PWA concern, not a backend Telegram concern.
- The cook bot already sends order notifications to the waiter via the cook-bot-to-waiter-UI channel (charter §3.1 + §3.4 ✓); the PWA layer adds push-notification capability to the waiter-UI for these notifications.

## Dependencies

- [01-table-management.md](01-table-management.md) — the v1 table-management surface; the v1 PWA waiter-UI consumes the v1 table-management surface via the FastAPI API.
- [02-order-taking.md](02-order-taking.md) — the v1 order-taking surface; the v1 PWA waiter-UI consumes the v1 order-taking surface via the FastAPI API.
- [04-menu-photo-bot.md](04-menu-photo-bot.md) — the v1 menu-photo-bot surface; the v1 PWA waiter-UI consumes the v1 menu-photo-bot surface via the FastAPI API.
- [11-customer-qr-menu.md](11-customer-qr-menu.md) — the v1 customer-QR-menu surface; the v1 PWA waiter-UI may integrate with the v1 customer-QR-menu surface (the customer can scan the QR code, place the order, and the order is routed to the waiter-UI PWA + the cook Telegram bot).
- [08-index-mockup.md](08-index-mockup.md) — the v1 index mockup; the v1 PWA waiter-UI is the PWA-version of the v1 index mockup.
- External: **Google Cloud Run** (deployment platform), **Google Cloud Build** (CI/CD), **Cloud SQL for Postgres** (managed Postgres), **OWASP top-10** (threat model), **devsecops tools** (bandit, safety, trivy, gitleaks).

## Open questions

- Does LE31 v1 want to deploy on Google Cloud Run, or stay self-hosted? (charter §3.7 + owner-decision needed; the v1 has been self-hosted to date.)
- Does the waiter want a PWA on their phone, or a tablet/Chromebook app? (UX decision; PWA works on both, but the install prompt + offline behavior differs.)
- Does the waiter-UI PWA need to work fully offline, or only when the FastAPI backend is reachable? (UX decision; full offline is complex and requires a local IndexedDB cache; partial offline is simpler and uses a service worker for the static assets only.)
- Does the PWA need push notification capability, or is the Telegram cook-to-waiter notification channel sufficient? (UX decision; both can coexist.)

## Why this matters

The Snacki.ndb vocabulary is the **canonical v1 in-domain small-restaurant-PWA-with-OWASP-devsecops-vocabulary reference of the 80-pass series**. The *PWA + devsecops + OWASP + FastAPI + Python + Google-Cloud-Run + Next.js* sextuple-primitive IS the strongest v1 in-domain restaurant-PWA-deployment-vocabulary of the 80-pass series (7/7 topic-overlap = 100%; first in-domain v1 small-restaurant-PWA-with-OWASP-devsecops-vocabulary of the 80-pass series; the maintainer is shipping real code with a real deployment target). The Python + FastAPI stack is on-stack (charter §3.1 + §3.2 ✓); the Next.js frontend is portable to HTMX; the PWA is portable to v1 waiter web UI; the OWASP threat model is charter §3.7 GDPR-compatible; the Google-Cloud-Run deployment is a deployment choice (charter §3.7 review needed). When a v1 PR proposes to deploy the waiter-UI as a PWA on Google Cloud Run with OWASP-grade security, this vocabulary becomes the canonical reference.
