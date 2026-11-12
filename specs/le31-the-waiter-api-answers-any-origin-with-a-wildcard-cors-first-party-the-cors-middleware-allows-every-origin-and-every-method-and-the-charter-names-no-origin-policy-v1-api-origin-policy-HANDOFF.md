# HANDOFF — Feature 469: the waiter API answers any origin with a wildcard CORS

> **Slice contract for an external coding agent.** Read this file and the feature contract it names; you should need nothing else. **Do not paste chat excerpts.** If anything here is ambiguous, stop and say so — do not invent product behaviour.
>
> **Pick A of Daily Research 2026-11-12 (89th pass). FIRST-PARTY, execution-proven.** Bucket: **v1**. Gate verdict: **`build`**.

## 1. The active feature path

```
features/469-le31-the-waiter-api-answers-any-origin-with-a-wildcard-cors-first-party-the-cors-middleware-allows-every-origin-and-every-method-and-the-charter-names-no-origin-policy-v1-api-origin-policy.md
```

**The one-sentence claim:** LE31's waiter API answers a request from any origin with `Access-Control-Allow-Origin: *` and every HTTP method, because `settings.debug` defaults to `True` and the restrictive branch is both unreachable and a placeholder hostname.

**The one sentence this feature exists to make true:** *LE31's waiter API does not answer every origin, unless an operator deliberately says so.*

**The executed evidence (re-run it; do not trust this paragraph):**

```
OPTIONS /api/tables   Origin: https://attacker.example   Access-Control-Request-Method: DELETE
  -> HTTP 200
     access-control-allow-origin      : *
     access-control-allow-methods     : DELETE, GET, HEAD, OPTIONS, PATCH, POST, PUT, QUERY
     access-control-allow-headers     : None
     access-control-allow-credentials : None
```

**The offending lines — `backend/app/main.py:32-37`:**

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"] if settings.debug else ["https://your-domain.example"],
    allow_methods=["*"],
    allow_headers=["*"],
)
```

**And `backend/app/config.py:15`:** `debug: bool = True`.

## 2. The seven-check gate verdict

| # | Check | Verdict |
|---|---|---|
| 1 | Raison d'être / JTBD | When the owner runs the app with no environment variables, the API answers every origin, but nothing says which origins are allowed — so the owner cannot tell whether the app is safe on the restaurant's network. |
| 2 | Viability | **Yes** — one setting, one test, one README note. |
| 3 | Practicability & confidence | **Yes** — the restrictive branch already exists in the code; the slice makes the safe state the default. **Rabbit hole: the correct origin list is the owner's deployment decision. Do NOT invent a hostname.** |
| 4 | Conflict | **No invariant violated.** The charter contains **no** `cors`, `origin`, `same-origin` or `cross-origin` (all verified False). **⚠️ Adding authentication WOULD violate §3.2 — this slice must not add any.** |
| 5 | Outcome / appetite / scope | **v1** — 1–2 hours. Scope fixed: the **origin-policy default**, nothing else. |
| 6 | Cost to operational value | **High** — the exposure is silent and the default is the permissive one. |
| 7 | Circuit breaker & reversibility | **Stop evidence:** a test asserting a foreign origin does **not** receive `access-control-allow-origin: *`. **Rollback:** one config value. |
| — | **Decision** | **`build`** |

**Evidence class:** **observed**. Confidence: **high**.

## 3. Files to touch

**Exactly these, and no others:**

| File | Change |
|---|---|
| `backend/app/config.py` | **Add** `cors_allow_origins: list[str] = []` with a comment saying `[]` = same-origin and `"*"` = the permissive opt-in. **Do not change `debug`'s default.** |
| `backend/app/main.py` | **Rewrite the middleware call** to read `settings.cors_allow_origins`. **Remove the `settings.debug` conditional.** Delete the `https://your-domain.example` placeholder. |
| `backend/README.md` | **Add** a note: default is same-origin; a cross-origin deployment must set `CORS_ALLOW_ORIGINS`; `*` is available but deliberate; **authentication is a v1 non-goal (§3.2)**. |
| `backend/tests/test_cors_policy.py` (or the repo's existing test location) | **Add** the regression tests. |
| `features/469-…md` | The contract. Read-only for you except for fixing a typo. |
| `specs/le31-the-waiter-api-answers-any-origin-with-a-wildcard-cors-first-party-the-cors-middleware-allows-every-origin-and-every-method-and-the-charter-names-no-origin-policy-v1-api-origin-policy-HANDOFF.md` | This file. |

**Files you must NOT touch:** `backend/app/models.py`, `backend/app/db.py`, `backend/app/routers/tables.py`, `backend/app/bot/cook_bot.py`, `backend/app/routers/__init__.py`, anything under `features/` other than 469, anything under `specs/` other than this one, `PROJECT_CHARTER.md`, `INDEX.md` (the parent owns the INDEX rows).

## 4. The implementation, in order

1. **Write the failing test first.** With the **shipped default settings**, `OPTIONS /api/tables` carrying `Origin: https://attacker.example` must **not** receive `access-control-allow-origin: *`. **On today's code it DOES — record the failure output before you change anything.**
2. **Add the setting** to `backend/app/config.py`:
   ```python
   # ───── HTTP surface ─────
   cors_allow_origins: list[str] = []   # same-origin only; "*" to opt in explicitly
   ```
3. **Rewrite the middleware** in `backend/app/main.py`:
   ```python
   app.add_middleware(
       CORSMiddleware,
       allow_origins=settings.cors_allow_origins,
       allow_methods=["*"],
       allow_headers=["*"],
   )
   ```
   **The origin policy must not be coupled to `settings.debug`.**
4. **Add the positive case:** with `cors_allow_origins=["*"]` the header **is** `*`. The permissive path must remain reachable.
5. **Add the same-origin case:** a request with **no** `Origin` header is served normally (the waiter UI is same-origin and must not break).
6. **Write the README note.**
7. **Record the decision note** for Open question 1 (the owner's origin list) — as a short paragraph in the feature file's *Open questions*, marked as **recorded default: `[]` (same-origin)**.

## 5. The four things that will go wrong if nobody tells you

1. **⚠️ You will be tempted to add authentication.** Do not. `PROJECT_CHARTER.md` §3.2 says verbatim: *"Per-user PIN auth in v1 (we'll use a hardcoded `server_id = 1` in the tables router — wire proper auth later)."* **Adding auth violates the charter.** Features 451, 388, 403 and 463 own that question.
2. **⚠️ You will be tempted to fix `server_id: int = 1,  # TODO: from auth token`.** Do not. Feature **451** owns the actor-resolution seam; feature **388** calls that TODO *"a separate, untouched TODO"*. **Leave the line exactly as it is.**
3. **⚠️ You will be tempted to narrow `allow_methods`/`allow_headers` too.** Do not. They are not an exposure once the origin list is restricted, and narrowing them is a separate decision the owner has not made. **Recorded default: leave them.**
4. **⚠️ You will be tempted to keep `settings.debug` in the condition** because "that's how it was". **That is the bug.** The defect is precisely that the safe state requires remembering to set an environment variable.

## 6. Verification protocol

Run each of these and record the **actual output**. **"Tests pass" is not the acceptance criterion — the header value is.**

```bash
# 1. The contract file exists and is parseable.
python3 - <<'PY'
import pathlib
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
#                backend/README.md, the test file, this feature file and this HANDOFF
```

## 7. Rollback path

**One line, or one environment variable.**

- Restore `allow_origins=["*"] if settings.debug else [...]` in `backend/app/main.py`, **or** set `CORS_ALLOW_ORIGINS="*"` in the environment.
- **No data is at risk.** No schema change, no column, no table, no migration.
- **No ledger is touched.** No `StockEntry` is written, updated or deleted by this feature.
- **Even after the code is reverted, the permissive path remains reachable** via the environment variable.

## 8. The mandatory LE31 skill list

**Load these before you write code. In this order:**

1. `le31-conventions` — the seven-check gate, the hard invariants, and the charter's §3.2 non-goals. **This is why you are not adding authentication.**
2. `le31-v1-feature-pattern` — the contract shape, the slicing rules, and the definition of done.
3. `le31-handoff-spec` — the frozen-contract discipline: **do not silently change the slice, the scope or the verification path.** If you find something that must change, **surface it and stop.**
4. `development` — the generic pipeline: specify → plan → tasks → implement → **independent review**.
5. `speckit-specify`, `speckit-plan`, `speckit-tasks` — as `development` directs.
6. `pre-merge-review` — **product code does not merge on your own say-so.** It merges on green checks **and** a review from an agent or person who did not author the change.
7. `verify-before-fixing` — when a check fails, **fix what it is flagging. Never weaken a check to make it pass.**

**The project skills live in the repository** at `skills/<name>/SKILL.md`. If the Hermes loader cannot find one by name, **read the file directly** — do not proceed without it.

## 9. The one thing that matters

**The safe state must be the state you get by doing nothing.** Today it is not: an operator who follows the README gets a wildcard-CORS API, because the "production" branch is unreachable *and* would not have worked anyway (it names a placeholder host).

The fix is **one setting and one test**. The temptation you must resist is the one that makes this feature a *security project* instead of a *default-hygiene fix*: **do not add authentication.** The charter forbids it for v1, three filed features already defer it, and this slice's entire value is that it is **small enough that you will actually finish it**.
