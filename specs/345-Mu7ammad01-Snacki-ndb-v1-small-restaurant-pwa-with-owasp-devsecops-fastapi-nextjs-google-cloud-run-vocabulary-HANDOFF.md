# Slice Handoff — Feature 345 (Mu7ammad01/Snacki.ndb)

> **Feature ID**: 345
> **Feature path**: `/opt/data/le31_mmm3_research_work/features/345-Mu7ammad01-Snacki-ndb-mit-small-restaurant-pwa-devsecops-fastapi-nextjs-google-cloud-run-owasp-pwa-python-v1-vocabulary.md`
> **Decision**: defer (parking-lot, vocabulary reference)
> **Bucket**: v1

## LE31 feature gate verdict (carried from feature contract)

- **Evidence precondition**: inferred (vocabulary observation, not observed LE31 user pain). Confidence: medium.
- **Seven checks**:
  1. **JTBD**: When a v1 PR proposes a small-restaurant PWA (Pick B), the operator wants the deployment to follow the PWA + devsecops + OWASP + Google-Cloud-Run quartet.
  2. **Viability**: high — the *PWA + devsecops + OWASP + Google-Cloud-Run* discipline is operator-readable + operator-deployable; the v1 PR candidate is straightforward.
  3. **Practicability and confidence**: Python ✓ ON-STACK + FastAPI ✓ ON-STACK + Next.js (portable to HTMX) + PWA (portable to v1 waiter web UI) + OWASP (charter §3.7 GDPR-compatible) + Google-Cloud-Run (deployment choice); confidence: high for the v1 PR candidate.
  4. **Conflict**: no hard conflict with any charter invariant. v1 bucket pick; the `le31 v1 — Core MVP` project DOES exist, but the v1 PR candidate requires a charter §3.7 + §3.2 review (PWA + Google-Cloud-Run is a deployment choice; the underlying FastAPI+Python+OWASP code is on-stack).
  5. **Outcome / appetite / scope**: v1 outcome; 0 build time today; max 2 weeks if a v1 PR is proposed (3 days to specify, 3 days to plan, 1 week to build + verify).
  6. **Cost to operational value**: low RICE; not a v1 PR candidate today.
  7. **Circuit breaker / reversibility**: fully reversible (vocabulary-only artifact; no code adoption).
- **Decision**: **defer (parking-lot, vocabulary reference)**.

## Files this slice will touch (when implemented)

> Not implemented today. When a v1 PR is proposed, the implementation will touch:

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

## Verification protocol (when implemented)

1. Run `pytest app/v1/pwa/tests/` and verify all tests pass.
2. Manually install the PWA on a phone (Android or iOS); verify the install prompt appears and the app installs successfully.
3. Manually open the PWA in airplane mode; verify the offline cache works (the static assets load from the service worker).
4. Manually trigger a push notification (e.g. cook → waiter "table 5 is ready"); verify the push notification appears on the waiter's phone.
5. Manually run `bandit` + `safety` + `trivy` + `gitleaks`; verify all security scans pass.
6. Manually run `gcloud builds submit` + `gcloud run deploy`; verify the PWA deploys to Google Cloud Run successfully.
7. Manually run the OWASP top-10 threat-model review; verify all 10 threats are explicitly addressed in the design and code.

## Rollback path

- `git revert <commit-hash>` to remove the v1 PWA waiter-UI surface.
- `gcloud run services delete <service-name>` to remove the Google Cloud Run deployment.
- No v1 data is affected (greenfield; no migration of existing v1 data).
- The v1 vanilla web UI is unchanged (the v1 PWA is a new surface, not a migration).

## Mandatory LE31 skill list for the external coding agent

Before starting, the external coding agent MUST load these skills:

1. **`le31-conventions`** — the global LE31 decision layer + feature gate + hard invariants.
2. **`le31-v1-feature-pattern`** — the canonical contract shape + slicing rules + definition of done.
3. **`le31-handoff-spec`** — the handoff discipline + frozen contract + verification protocol.
4. **`le31-coding-agent-brief`** — the paste-in prompt template that produces the slice prompt from this HANDOFF.
5. **`le31-research`** — the research workflow + evidence-before-recommendation discipline.
6. **`development`** — the generic code-development pipeline (specify → plan → tasks → implement).

## Trigger policy for the external coding agent

- **DO NOT start** until a v1 PR is proposed that explicitly migrates the waiter web UI to a PWA on Google Cloud Run.
- **DO NOT start** until the charter §3.7 + §3.2 review has been completed (PWA + Google-Cloud-Run is a deployment choice).
- **DO NOT start** until the owner has approved the Google-Cloud-Run deployment (or the self-hosted alternative is chosen instead).
- When triggered, mirror back the frozen contract fields (feature ID, decision, bucket, files to touch, verification protocol) before implementing; stop if the mirror-back does not match.

## External-context Linear reference

- Parent research issue: Research 2026-10-19 — daily (Linear MCP BLOCKED 30th consecutive day; parent fallback JSON at `/opt/data/le31-daily-research-2026-10-19.linear-fallback.json` documents the intended parent + 3 sub-issues).
- This feature: Feature 345 — Mu7ammad01/Snacki.ndb (intended sub-issue in `le31 v1 — Core MVP` P-HMM-3 IF a v1 PR is proposed; otherwise in `le31 Research` P-HMM-1 as parent of the sub-issue per `le31-feature-pipeline/SKILL.md` line 33).

## Sign-off gap

- External agent has NOT yet been dispatched.
- Charter §3.7 + §3.2 review has NOT yet been completed.
- v1 PR has NOT yet been proposed.
- Owner decision on Google-Cloud-Run deployment has NOT yet been made.
- No v1 build today.
