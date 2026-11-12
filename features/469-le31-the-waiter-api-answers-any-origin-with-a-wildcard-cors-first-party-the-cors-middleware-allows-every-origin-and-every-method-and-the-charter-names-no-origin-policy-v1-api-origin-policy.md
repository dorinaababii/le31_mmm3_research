# Feature 469 — The waiter API answers any origin with a wildcard CORS, and the charter names no origin policy: `allow_origins=["*"]` is the shipped default

> **Pick A of Daily Research 2026-11-12 (89th pass).** **FIRST-PARTY.** The defect is in LE31's own shipped `backend/app/main.py` and its own default configuration. **Evidence class OBSERVED** — reproduced by execution against the real `app.main:app` object with `TestClient`; the transcript is re-runnable.
>
> **Executed against LE31's real app object (2026-11-12):**
>
> ```
> OPTIONS /api/tables   Origin: https://attacker.example   Access-Control-Request-Method: DELETE
>   -> HTTP 200
>      access-control-allow-origin      : *
>      access-control-allow-methods     : DELETE, GET, HEAD, OPTIONS, PATCH, POST, PUT, QUERY
>      access-control-allow-headers     : None
>      access-control-allow-credentials : None
>
> GET /api/tables   Origin: https://attacker.example
>   -> HTTP 200   access-control-allow-origin: *
> ```
>
> **The code that does it** — `backend/app/main.py:32-37`:
>
> ```python
> app.add_middleware(
>     CORSMiddleware,
>     allow_origins=["*"] if settings.debug else ["https://your-domain.example"],
>     allow_methods=["*"],
>     allow_headers=["*"],
> )
> ```
>
> **The load-bearing nuance, and why this is not "the developer wrote a star":** the wildcard is **already conditional on `settings.debug`**, and `settings.debug` **defaults to `True`** (`backend/app/config.py:15`) with no environment override in the shipped configuration. **The defect is not the existence of the permissive branch — it is that the application's default state is the permissive one, and nothing in the charter, the config, or the README says the app must be started with `DEBUG=false` to be safe.**
>
> **What is NOT claimed, checked as carefully as what is:** `access-control-allow-credentials` is **`None`** — this is **not** the dangerous `*`-with-credentials configuration, so a browser will not attach cookies cross-origin. **This is not a credential-theft finding.** It is an **origin-policy** finding: any web page the waiter visits can read the restaurant's floor API and the full `/openapi.json` schema.
>
> **The corpus gate:** `cors|allow_origins|allow_credentials` → **0 hits across all 966 corpus files** (502 feature contracts + 464 HANDOFFs). `api key|bearer token|authorization header` → **0 hits in any LE31 feature contract**. `session cookie|cookie|jwt|oauth` → **0 hits in any LE31 feature contract** (the `cookie` hit is feature 29's owner-link prose; the `jwt` hits are third-party vocabulary references).
>
> **The charter was checked, and the boundary is explicit.** `PROJECT_CHARTER.md` contains **no** occurrence of `cors`, `origin`, `same-origin` or `cross-origin` (all verified **False**). The charter's §3.2 *does* exclude *"Per-user PIN auth in v1"* — so this feature **does not add authentication** and **does not touch the `server_id = 1` TODO**. It constrains **which origins may read the response**, and nothing else.

## Goal

Make the **safe origin policy the default state** of LE31's waiter API, so that an operator who runs `uvicorn app.main:app` with no environment variables does not silently serve a wildcard-CORS API.

The concrete outcome:

1. **The application's default configuration is the restrictive one**, not the permissive one.
2. **The permissive branch is still reachable**, but only when an operator **explicitly** opts into it — by naming the setting, not by omitting it.
3. **The origin list is a configuration value**, not a constant buried in a middleware call.
4. **A regression test proves the shipped default does not answer a foreign origin with `*`.**

**The single sentence this feature exists to make true:** *LE31's waiter API does not answer every origin, unless an operator deliberately says so.*

## Scope

**In scope (v1):**

- **Move the origin list out of the middleware call and into `config.py`**, as a named setting (e.g. `cors_allow_origins: list[str] = []`) — no magic value in `main.py`.
- **Change the default from permissive to restrictive.** An empty list means **same-origin only** — the browser sends same-origin requests without a preflight, so a same-origin deployment is unaffected.
- **Keep the permissive option, explicitly.** A named setting (e.g. `cors_allow_origins=["*"]`) still produces the wildcard, for the developer who genuinely wants it.
- **One README note** in `backend/README.md` recording the deployment requirement: a **cross-origin** deployment must set the origin list explicitly; the default is same-origin.
- **A regression test** that fails on today's code and passes on the fixed code: with the shipped default settings, a request carrying a foreign `Origin` must **not** receive `access-control-allow-origin: *`.
- **A decision note** recording the owner's origin list for the real deployment — **recorded, not guessed** (see *Open questions*).

**Explicitly NOT in scope (v1):**

- **Authentication, authorization, sessions, tokens, logins.** `PROJECT_CHARTER.md` §3.2 excludes *"Per-user PIN auth in v1"* and says the tables router will *"use a hardcoded `server_id = 1` … wire proper auth later"*. **This feature does not add any of it.** Features **451**, **388**, **403** and **463** own those questions; each explicitly defers authentication in its own *Out of scope* section.
- **The `server_id: int = 1,  # TODO: from auth token` line** (`backend/app/routers/tables.py:39`). **Untouched.** Feature **451** owns the actor-resolution seam; feature **388** calls the TODO *"a separate, untouched TODO"*.
- **The static-file mount.** Feature **469's sibling** — the repo-root static mount — is **not** this feature's business; see *Dependencies*.
- **Any change to the API's routes, payloads, or behaviour.** The CORS policy is a **response-header** concern; the routes are untouched.
- **A reverse proxy, a TLS terminator, or a deployment story.** §3.2's single-VPS posture is unchanged.
- **The `/api/health` probe.** It carries no data and is intentionally unauthenticated and uncross-origin-restricted.
- **Any change to `PROJECT_CHARTER.md`** — the charter is the owner's document.
- **Changing `settings.debug`'s default.** `debug` has other meanings (FastAPI's error pages, tracebacks). **Do not overload it** to carry the origin policy; use a separate, named setting.

## Description

LE31's waiter API is a FastAPI app served on a single VPS behind a systemd unit (charter §3.2: *"single VPS + systemd unit is fine for v1"*). The waiter opens it from a tablet or phone on the restaurant's network.

The CORS middleware is configured as:

```python
allow_origins=["*"] if settings.debug else ["https://your-domain.example"],
```

This **looks** like it has a production posture — the `else` branch names a domain. But:

1. **`settings.debug` defaults to `True`.** `backend/app/config.py:15` reads `debug: bool = True`. There is no `.env` in the repository (the real one lives outside the repo) and no `DEBUG=false` anywhere in the shipped configuration or README.
2. **The `else` branch's origin is a placeholder** — `https://your-domain.example` — so even the restrictive branch would **not** serve a real same-origin deployment correctly: a deployment at `https://pos.example.com` would be refused by its own UI. **The restrictive branch is therefore not a working posture today; it is an unused string.**
3. **The consequence is that the only *reachable* behaviour is the wildcard.** `settings.debug` is true by default, so the app answers every origin.

The executed evidence above shows the concrete shape: a preflight for a **DELETE** from `https://attacker.example` is answered **HTTP 200** with `access-control-allow-origin: *` and `access-control-allow-methods: DELETE, GET, HEAD, OPTIONS, PATCH, POST, PUT, QUERY`.

**What an attacker can read:** `GET /api/tables` returns the floor — every table's label, section, seat count and floor-map coordinates. `GET /openapi.json` returns the complete API schema: every route, every parameter, every response shape. `GET /docs` and `GET /redoc` render the interactive documentation.

**What an attacker cannot do, and this feature does not pretend otherwise:**

- **No credentials are exposed.** `access-control-allow-credentials` is `None`. A browser will not attach cookies to a wildcard cross-origin request.
- **There is no session to steal** — LE31 has no authentication in v1 (charter §3.2).
- **`POST /api/tables/{id}/seat` writes.** This is the important limitation: a cross-origin page **can** issue the write, because `allow_methods=["*"]`. But it cannot **read** the response usefully if the origin is restricted... **except that with a wildcard it can read it too.** The finding is therefore about **read exposure of the floor and the API surface**, and the write is a **secondary consequence that the same policy change addresses**. The feature contract states this plainly rather than overstating a credential breach.

**Why the default is the defect, and not the constant.** The permissive branch is a legitimate developer convenience and the restrictive branch is a legitimate production posture. The bug is that **the state an operator gets by doing nothing is the unsafe one**, and that the "safe" branch is a placeholder that would not work anyway. A feature that made the permissive branch the default and required the operator to opt *out* would have made things worse; a feature that required an explicit origin list makes the safe state the default **and** makes the placeholder problem visible, because an empty list means same-origin and therefore *works*.

### The cost of leaving it

The floor plan and the API schema are **not** secret in the sense of credentials — but they are the restaurant's operational layout, and the API schema is a precise map of what the system accepts. On the restaurant's own network, a laptop with a browser is a normal thing to be present. The finding is a **hygiene and default-safety** defect, not a breach, and this contract says so in those words.

## Data model

**No schema change. No column. No table.**

The only new state is a **configuration value**:

| Setting | Type | Default | Meaning |
|---|---|---|---|
| `cors_allow_origins` | `list[str]` | `[]` | Origins permitted to read the API cross-origin. **`[]` = same-origin only.** `"*"` = the permissive wildcard, opt-in only. |

The middleware call becomes:

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_allow_origins,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

**Why the empty list is the right default and not `None`:** `pydantic-settings` parses a comma-separated env var into a `list[str]`, so `CORS_ALLOW_ORIGINS=""` and an unset variable both yield `[]`. The permissive case is `CORS_ALLOW_ORIGINS="*"` — **one deliberate keystroke**, and the README says so.

**Why `allow_methods=["*"]` and `allow_headers=["*"]` stay:** once the origin list is restricted, the methods and headers that a *permitted* origin may use are not the exposure. Narrowing them is a separate hardening decision and is **not bundled** here (see *Open questions*).

## Implementation steps

Each step is independently verifiable. **Do not begin step 2 before step 1's test fails.**

1. **Write the failing regression test first.**
   - A test that builds the app with **the shipped default settings** (no environment override for `cors_allow_origins`).
   - It sends `OPTIONS /api/tables` with `Origin: https://attacker.example`.
   - It asserts the response does **not** carry `access-control-allow-origin: *`.
   - **On today's code this test FAILS** (the header is `*`). Record the failure output.
2. **Add the setting** to `backend/app/config.py`:
   ```python
   # ───── HTTP surface ─────
   cors_allow_origins: list[str] = []   # same-origin only; "*" to opt in explicitly
   ```
3. **Rewrite the middleware call** in `backend/app/main.py` to read `settings.cors_allow_origins`, and **remove the `settings.debug` conditional** — the origin policy must not be coupled to the debug flag. Keep `allow_methods`/`allow_headers` as they are.
4. **Add the test's positive case:** with `cors_allow_origins=["*"]` the header **is** `*` — the permissive path still works and is still reachable.
5. **Add the same-origin case:** a request with **no** `Origin` header is served normally (the waiter UI is same-origin and must not break).
6. **Write the README note** in `backend/README.md`: the default is same-origin; a cross-origin deployment must set `CORS_ALLOW_ORIGINS`; `*` is available but deliberate.
7. **Record the decision note** (see *Open questions*) — the owner's origin list for the real deployment, or an explicit "same-origin only, no cross-origin deployment planned".
8. **Run the whole test suite.** Nothing else may break — in particular, the waiter UI (`index.html`) must still load its data, which it does because it is same-origin.

## Telegram interaction if any

**None.** This feature touches no bot handler, no Telegram command and no `StockEntry`. The cook bot is a separate surface on a separate transport (the Telegram Bot API), and the CORS policy governs the browser-facing HTTP surface only.

**Note for the implementer:** do **not** add the Telegram bot token to `allow_origins` or treat Telegram as an origin. Telegram's webhook delivery is not a browser origin and is not governed by this middleware.

## Dependencies

- **No hard dependency.** This feature can land on its own, in any order relative to the rest of the corpus.
- **Feature 451 (a visit may name a cook as its server) — adjacent, NOT a dependency.** 451 owns the *role* predicate and the *actor-resolution seam*. Its *Out of scope* says verbatim: *"Authentication. The seat route's `server_id: int = 1,  # TODO: from auth token` implies auth is a separate feature. This contract does not build authentication and does not build a session, a token, or a login."* **This feature does not build any of those either — and must not, because §3.2 forbids it for v1.**
- **Feature 388 (table state machine / seat idempotency) — adjacent.** 388 rewrites the same router; its *Out of scope* says the `server_id` TODO is *"a separate, untouched TODO"*. **This feature does not touch that line.**
- **Feature 403 (role-based Telegram allowlist) — different surface.** 403 owns *who may act* on the **Telegram chat-id** allowlist. **This feature owns which browser origins may read the HTTP response.** Different subjects; **do not merge.**
- **Feature 463 (the PIN hash is not verified) — adjacent.** 463 is about credential *verification*, not origin policy.
- **The repo-root static mount — a sibling finding, NOT this feature.** The 2026-11-11 pass filed the static mount as a separate defect. **If that feature lands, it shrinks what is served; this feature shrinks who may read it. They are complementary and must not be merged into one PR.**
- **Feature 446 (schema evolution) — not applicable.** No schema change.

## Open questions

1. **What is the owner's origin list for the real deployment?** This feature makes the setting exist and defaults it to same-origin. **If the waiter UI and the API are served from the same origin (the normal single-VPS case), `[]` is correct and complete.** If the owner plans a separate API host, the list must name it. **Recorded default: `[]` (same-origin), on the basis that the charter describes a single VPS serving one UI.** The implementer **must not invent a hostname.**
2. **Should `allow_methods` / `allow_headers` be narrowed too?** They are currently `["*"]`. With a restricted origin list they are not an exposure, so they are **out of scope here**. **Recorded default: leave them.** If the owner later wants defence in depth, that is a separate slice.
3. **What about the `https://your-domain.example` placeholder that this change removes?** It was never reachable (the `debug` default made it dead code) and it would not have worked anyway. **Recorded default: delete it.** The new setting supersedes it entirely.
4. **Does the owner intend any deployment where the API is on a different origin from the UI — a hosted API, a CDN, a separate admin host?** If yes, the same-origin default must be overridden at deploy time and the README note is the operator's contract. **No decision is made here.**

## Why this matters

LE31's waiter API is the surface the **waiter** uses while standing in a dining room, usually on a tablet, usually on the restaurant's own Wi-Fi. The API is the only way the UI learns what the floor looks like.

**The safe state should be the state you get by doing nothing.** Today it is not: an operator who follows the README (`uvicorn app.main:app --host 0.0.0.0 --port 8000`) gets a wildcard-CORS API, and the code contains a "production" branch that was never reachable and would not have worked if it had been. That is the defect this feature removes — **not** a missing security feature, but a **default that fails open**.

The cost is **one setting and one test**. The rollback is **one line**. And the slice is careful to stay inside the charter: it does **not** add authentication, because §3.2 explicitly defers that, and it records that decision instead of quietly widening the scope.

## Adjacent evidence

- **`/openapi.json`, `/docs` and `/redoc` are all reachable** and return **200** with no credentials (executed 2026-11-12: 2,543 B / 1,013 B / 895 B). The same origin policy governs them.
- **`GET /api/health`** returns `{"status": "ok", "app": "restaurant", "version": "0.0.1"}` — no data, deliberately unauthenticated, and **not** a finding.
- **The wildcard `allow_methods` includes `DELETE` and `PATCH`** — so a foreign origin may *attempt* writes as well as reads. The write surface today is `POST /api/tables/{id}/seat`, whose behaviour is owned by feature **388**. **This feature does not change what that route does; it changes who may reach it.** The two are complementary.
- **The 2026-11-11 pass filed the repo-root static mount** (`app.mount("/", StaticFiles(directory=str(_STATIC_DIR.parent), html=True))`), which serves the charter, the backend source and the git index over HTTP. **If that mount is still present, the origin policy is the *second* control, not the only one** — the two features are independent and both are worth landing.
- **No feature in 966 corpus files mentions CORS at all.** That is the gap this feature fills.

## Verification protocol

The implementer must run these and record the actual output. **"Tests pass" is not the acceptance criterion — the header value is.**

```bash
# 1. The contract file exists and is parseable.
python3 - <<'PY'
import re, pathlib
p = pathlib.Path("features/469-le31-the-waiter-api-answers-any-origin-with-a-wildcard-cors-first-party-the-cors-middleware-allows-every-origin-and-every-method-and-the-charter-names-no-origin-policy-v1-api-origin-policy.md")
assert p.exists(), "contract file missing"
txt = p.read_text()
for h in ("## Goal", "## Scope", "## Description", "## Data model",
          "## Implementation steps", "## Telegram interaction if any",
          "## Dependencies", "## Open questions", "## Why this matters"):
    assert h in txt, f"missing section {h}"
print("PASS contract sections")
PY

# 2. THE load-bearing check: with the SHIPPED DEFAULT settings, a foreign
#    origin must NOT receive the wildcard.
#    -> asserts: response.headers.get("access-control-allow-origin") != "*"
python3 - <<'PY'
from fastapi.testclient import TestClient
from app.main import app
c = TestClient(app)
r = c.options("/api/tables", headers={
    "Origin": "https://attacker.example",
    "Access-Control-Request-Method": "GET"})
allow = r.headers.get("access-control-allow-origin")
print("allow-origin:", allow)
assert allow != "*", "FAIL: shipped default still answers every origin with *"
print("PASS default is not the wildcard")
PY

# 3. The permissive path is still reachable, but only when asked for.
python3 - <<'PY'
from app.config import Settings
s = Settings(cors_allow_origins=["*"])
assert s.cors_allow_origins == ["*"]
print("PASS explicit '*' is accepted")
PY

# 4. A same-origin request (no Origin header) is still served.
python3 - <<'PY'
from fastapi.testclient import TestClient
from app.main import app
c = TestClient(app)
r = c.get("/api/health")
assert r.status_code == 200, r.text
print("PASS same-origin request served")
PY

# 5. The middleware no longer consults settings.debug for the origin list.
grep -n "allow_origins" backend/app/main.py
#    -> asserts: the line reads settings.cors_allow_origins
#    -> asserts: it does NOT read settings.debug

# 6. No authentication was added. The charter forbids it for v1.
grep -rn "Authorization\|api_key\|oauth2\|OAuth2Password\|SessionMiddleware" backend/ || true
#    -> asserts: no new auth mechanism appears in backend/

# 7. The corpus agrees: the origin policy is now owned.
grep -rl "cors_allow_origins" features/ specs/
#    -> asserts: exactly one feature contract names it

# 8. Nothing but the named files changed.
git status --short
#    -> asserts: only backend/app/config.py, backend/app/main.py,
#                backend/README.md, this feature file and the HANDOFF changed
```

## Rollback path

**One line.** Restore `allow_origins=["*"] if settings.debug else [...]` in `backend/app/main.py`, or set `CORS_ALLOW_ORIGINS="*"` in the environment.

- **No data is at risk.** No schema change, no column, no table, no migration.
- **No ledger is touched.** No `StockEntry` is written, updated or deleted by this feature.
- **The test suite's other checks are unaffected.** The permissive path remains reachable via the environment variable even after the code is reverted.
- **If the owner later wants the permissive default back** (e.g. during local development with a separate UI host), the environment variable is sufficient — **no code change is needed**.
