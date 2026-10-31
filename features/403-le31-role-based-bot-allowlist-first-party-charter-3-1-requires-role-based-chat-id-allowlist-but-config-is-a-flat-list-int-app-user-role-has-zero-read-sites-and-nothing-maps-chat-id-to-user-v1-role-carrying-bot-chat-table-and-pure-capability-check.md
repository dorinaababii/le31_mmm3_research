# Feature 403 — LE31's charter requires a **role-based** Telegram bot, and the data structure it would use **cannot carry a role**

> **Pick A of Daily Brainstorm 2026-10-29 (91st pass).** **FIRST-PARTY, and the defect is in LE31's own source and its own charter** — not inferred from a third-party repo.
>
> `PROJECT_CHARTER.md` §3.1 (In scope, v1) states, verbatim:
>
> > - **One Telegram bot, role-based via chat_id allowlist** (cook + manager).
>
> `backend/app/config.py` line 24 implements it as, verbatim:
>
> ```python
> telegram_allowed_user_ids: list[int] = []  # cook + manager IDs
> ```
>
> **A `list[int]` has no place to put a role.** The comment asserts a distinction the type cannot express — *"cook + manager IDs"* — and if the list were ever read, **every listed user would receive every capability, cook and manager alike.**
>
> **Evidence, all parent-verified on 2026-10-29** (commands in the HANDOFF, re-runnable):
> 1. `grep -rn 'telegram_allowed_user_ids' backend/` returns **exactly one hit — the declaration itself**. The setting is **never read**. `backend/app/bot/cook_bot.py` carries the literal comment `# TODO: filter incoming messages to allowed user IDs.`
> 2. `class UserRole(str, Enum)` declares `server / cook / manager`. **Zero** qualified read sites (`UserRole.server`, `UserRole.cook`, `UserRole.manager`) exist anywhere in `backend/`. The enum is declared and never consulted.
> 3. `chat_id` appears **nowhere** in `backend/` outside that config comment, and there is **no** `chat_id ↔ app_user.id` mapping in **either** direction. `AppUser` has a `role`; the bot config has user IDs; the two are never joined.
> 4. The bot registers exactly two commands — `dp.message.register(cmd_start_today, Command("start_today"))` and `cmd_help` — and **no manager-only command exists to gate yet**.
>
> **External triangulation (three unrelated artifacts, one rule — the artifacts are the *instrument*, not the subject):**
> - `devstroop/ros` (MIT): *"Permissions buried in a router `redirect:` | Permissions are a **pure function** (`core/rbac.zig`); the current matrix test is tautological and is being replaced with a **real table**"*.
> - `MrPettitt/restaurant-pos` (MIT): an explicit **role → capability table** (Manager / Server / Kitchen, each with a PIN), with *"**Manager approval** by PIN for voids, large discounts and refunds, with every approval recorded in an audit log."*
> - `Ariastiadi/OmniPOS` (MIT): a four-tier **role capability table** (Pending / Cashier / Manager / Admin) where each row's permissions are enumerated, the admin owning *"staff roles, business settings and the audit log"*.
>
> **Bucket: v1** — the need is a §3.1 in-scope v1 requirement. **Build verdict: `build`.** Evidence class: **OBSERVED** (all four claims above are reproducible greps against LE31's own tree).

## Goal

Make it possible for LE31 to **say which role a Telegram chat belongs to**, and to **decide what that role may do**, without changing any of LE31's product behaviour.

Concretely, the outcome is:

- a **role** is attachable to an allowlisted chat ID — not implied by a comment;
- a **capability check** is a single pure function, not a branch buried in a handler;
- the chef and the manager can be told apart by the bot, so that the charter's §3.1 wording — *"role-based via chat_id allowlist (cook + manager)"* — is **true of the implementation**, not merely of the plan.

**The single sentence this feature exists to make true:** *LE31's bot allowlist carries a role, and the role decides the capability.*

## Scope

**In scope (v1):**

- **One small table** that maps a Telegram chat ID to a role, with a uniqueness constraint on the chat ID.
- **One pure function** — a capability check of the form `can(role, capability) -> bool` — that is the **only** place a role is consulted.
- **One place** where the bot consults it, so the function has at least one caller and is not dead code.
- **A forward-pointer line** in `PROJECT_CHARTER.md` §3.1 recording that the allowlist is role-carrying, so the charter and the code describe the same thing.

**Out of scope (v1):**

- **Per-user PIN auth.** Charter §3.2 explicitly defers it (*"Per-user PIN auth in v1 (we'll use a hardcoded `server_id = 1` in the tables router — wire proper auth later)"*). This feature does **not** add a login, a password, a session, or a token. It is about **role**, which is a different thing from **identity**.
- **Any new bot command.** In particular **no manager-only command is added here.** The feature supplies the *mechanism*; whether a manager-only command exists is a separate change with its own gate. (Today the bot registers only `/start_today` and `/help`, neither of which is manager-only.)
- **Any change to the waiter web UI.** The `server_id: int = 1  # TODO: from auth token` in `backend/app/routers/tables.py` is **not** touched — that is the §3.2-deferred PIN work.
- **Row-level security.** Feature 402 (`rockcut/restaurant-reservation-system`) records the RLS pattern as vocabulary for a Supabase/Postgres deployment. LE31 v1 is a single-tenant VPS app; **the role check here is application-level and in-process.** Adopting RLS is a v2 deployment decision.
- **An audit log.** `MrPettitt` and `OmniPOS` both record one. LE31 has **no** audit-log concept today, and feature 379 records that `OrderItem` carries **no actor at all** — an audit log over an unactored history would be an audit log of nothing. **Recorded, not picked.**
- **A capability *catalogue*.** Which capabilities exist is an owner decision. This feature defines the *mechanism* and the *shape*; it does not enumerate the full permission matrix.
- **Alembic / migrations.** §3.2's stated v1 policy is `init_db()`. Follow it and record the prod-migration step as known debt.
- **Multi-tenant / multi-role inheritance.** §3.1 excludes multi-tenancy. One flat role per chat.

## Description

### The defect, as observed in LE31's own code on 2026-10-29

**Shape (a) — contradiction.** The charter requires a *role-based* allowlist. The mechanism is a *flat* list.

```
PROJECT_CHARTER.md §3.1   "One Telegram bot, role-based via chat_id allowlist (cook + manager)."
backend/app/config.py:24  telegram_allowed_user_ids: list[int] = []  # cook + manager IDs
```

**Shape (b) — omission.** `UserRole` is declared on `AppUser.role` and read **zero** times. Its three sibling classes that record *who did something* — `StockEntry.by_user_id`, `Shift.by_user_id`, `Bill.closed_by` — are all written. The one enum that describes **what kind of person** did something is never consulted.

**Shape (c) — missing inverse edge.** `AppUser.role` points at the user; `telegram_allowed_user_ids` names chats. Nothing points either way between them. A chat is not a user; a user is not a chat; and LE31 has no join between the two, so **"which role is this chat?" has no answer** — not a wrong answer, no answer.

**Shape (d) — undefined term.** *"cook + manager IDs"* has no defined referent: two **roles**? two **people**? a **group** that may contain both? The comment reads as all three simultaneously, and a reader has to guess.

### Why the quiet wrong answer is the expensive one

The plausible implementation of this feature — by someone who reads only the config comment — is:

```python
# WRONG: admits every allowlisted chat to every capability
if message.from_user.id in settings.telegram_allowed_user_ids:
    await cmd_manager_only(message)
```

That is **true today** (there is no allowlist check at all) and **silently false** the moment anyone adds one. Nothing errors; the manager-only action simply becomes available to the cook. There is **no ground truth to audit against**, because no capability boundary exists anywhere else in the system.

The asymmetry that makes this worth doing **now** rather than later: the cost of the wrong answer is **one line**, and the cost of discovering it later is an audit of every privileged action ever performed with no record of who performed it.

### The shape, from the three artifacts

All three external artifacts converge on the same structural rule, and it is a rule about **where** a permission decision lives:

| Artifact | The rule, verbatim | The structural point |
|---|---|---|
| `devstroop/ros` | "Permissions buried in a router `redirect:` … Permissions are a **pure function** … being replaced with a **real table**" | a permission decision must be a **function of data**, not a **branch in control flow** |
| `MrPettitt/restaurant-pos` | an explicit **role → capability table**, each role with a PIN | the **role-to-capability mapping is data**, and it is **enumerable** |
| `Ariastiadi/OmniPOS` | a four-tier **role capability table**, each row's permissions enumerated | the mapping is **per role**, and the table is **the** place it lives |

**The vocabulary transfers; the code-shape does not.** None of these is adopted: `ros` is Zig on a bespoke Native SDK, `MrPettitt` is a single-file browser app with a hardcoded demo PIN, `OmniPOS` is a Supabase/RLS web app with a four-tier role model that is **larger** than LE31's two-role §3.1 scope. **Only the rule is adopted: the role→capability mapping is a table, and the check is a function over it.**

## Data model

**New table:**

```
BotChat
  id            PK
  chat_id       INT UNIQUE NOT NULL     # Telegram chat id; the identity of the channel
  role          UserRole NOT NULL       # reuses the enum that already exists on AppUser
  created_at    DATETIME NOT NULL
```

- `role` reuses `UserRole` (`server` / `cook` / `manager`). **No new enum.** The enum already exists and is already declared on `AppUser.role`; this feature gives it a **second, read** site.
- `chat_id` is `UNIQUE` — **one chat, one role.** A chat that is both a cook chat and a manager chat is not a thing; if that is wanted, it is a different model and a different decision.

**Changed:**

```
backend/app/config.py
  telegram_allowed_user_ids: list[int] = []   # REMOVED (or kept as a deprecated alias)
```

The setting is replaced by the table. **Keeping it** would leave two sources of truth for "who is allowed", and one of them cannot carry a role — which is the defect. It is removed.

**One pure function** (new module `backend/app/services/`):

```python
def can(role: UserRole, capability: str) -> bool:
    """The ONLY place a role is consulted. Pure: no I/O, no DB."""
```

**The capability → role map** is a **constant**, not a database table, for v1:

```python
CAPABILITIES = {
    UserRole.cook:    {"menu.setup", "stock.report", "sold_out.mark", "leftover.log"},
    UserRole.manager: {"menu.setup", "stock.report", "sold_out.mark", "leftover.log",
                       "shift.close", "forecast.read", "report.read"},
    UserRole.server:  {"order.take"},
}
```

Two sets, two files: the **mapping** (which role has which capability) and the **check** (`can()`). The mapping is a constant because it changes with the product, not with the data; the **chat → role** assignment is a table because it changes with the staff.

## Implementation steps

1. **Create the table.** Add `BotChat` to `backend/app/models.py` with `chat_id: int` (unique, indexed), `role: UserRole`, `created_at: datetime`. Add the `UNIQUE` constraint on `chat_id` — **without it, two rows can claim the same chat with different roles and the capability check becomes order-dependent.**
2. **Create the services package.** `backend/app/services/` **does not exist today** (`ls backend/app/services/` → no such directory). Create it with `__init__.py` and `permissions.py`.
3. **Write the pure function.** `permissions.py` holds `CAPABILITIES` and `can(role, capability)`. **No database access, no session, no request object** — the function takes a role and a capability and returns a bool. That purity is what makes it testable without a fixture and what the `ros` rule ("permissions are a pure function") is actually asking for.
4. **Write the resolver.** `async def role_for_chat(session, chat_id) -> UserRole | None` — one query against `BotChat`, returning `None` for an unknown chat. **The unknown case is the point**: `None` means "not allowed", and it must be impossible to confuse with a role.
5. **Wire one call site.** In `backend/app/bot/cook_bot.py`, add a single guard helper that resolves the chat's role and asks `can(...)`. **Start with exactly one command** so the function has a caller and the wiring is observable. `cmd_start_today` is the natural one: it is a **cook** capability.
6. **Replace the config setting.** Delete `telegram_allowed_user_ids` from `backend/app/config.py` and delete the `# TODO: filter incoming messages to allowed user IDs.` comment **only once the guard in step 5 actually filters.** Leaving the TODO in place after the filter exists would be a lie in a comment.
7. **Add the regression test.** A test that asserts, for each of the three roles, that `can(role, capability)` returns the expected value — including that **`can(UserRole.cook, "shift.close") is False`** and **`can(UserRole.server, "order.take") is True`**. A second test asserts that an **unknown chat resolves to `None`** and is refused.
8. **Add the charter forward-pointer.** In `PROJECT_CHARTER.md` §3.1, amend the bullet to note that the allowlist is role-carrying and lives in `BotChat`. **One line.** The charter must not continue to describe a mechanism that no longer exists.

## Telegram interaction if any

**No new command, and no change to any existing command's user-visible behaviour.**

What changes is that `/start_today` — a **cook** capability — begins to be **refused for a chat that is not a cook**. Today it is accepted from every chat because no check exists. So the *observable* change is that a manager's chat can no longer run the cook's setup flow, and an unknown chat is refused.

**Refusal shape (proposed, owner to confirm):** one short line, no stack trace, no chat id echoed back:

> `This command is for the kitchen. Ask your manager to run it.`

**Do not** leak *which* role the chat has, and do not enumerate the capability list back to the user.

## Dependencies

- **No new package.** `sqlmodel` / `sqlalchemy` are already dependencies; `UserRole` is already imported into `models.py`.
- **No dependency on feature 379** (`OrderItem` actor attribution) or on feature 388 (`Table.status`). This feature is **independent** and can be built first.
- **Related, not blocking:** feature 379 (actor attribution — *"who did it"* vs this feature's *"who may do it"*), feature 402 (RLS vocabulary), feature 126 (the v2-AI allowlist pattern — a **deferred** artifact that discusses the allowlist as a pattern for *long-lived enrolled principals* and explicitly leaves the v1 allowlist alone).
- **No dependency on the Linear write endpoint** (blocked on this workspace — see the HANDOFF's sign-off gap).

## Open questions

1. **What is the capability vocabulary?** This feature defines the mechanism; the *catalogue* is an owner decision. The provisional set above is the minimum that makes the feature non-vacuous. **The owner picks.**
2. **Is `server` a Telegram role at all?** §3.1's bot has *cook + manager*. The waiter's web UI is not the bot. So does `BotChat.role` ever hold `server`? The provisional map says no — a chat that tries to take an order is refused. **Confirm.**
3. **Which chat is a manager chat in practice?** A personal Telegram account, a group chat, a topic in a group? Telegram's chat-id semantics differ for each, and the `UNIQUE` constraint assumes one chat = one role. **Owner to confirm.**
4. **What happens to a chat whose row is deleted?** The resolver returns `None` and the chat is refused. Is there a need for a **suspended** state distinct from *absent*? **Not decided here.**
5. **Does the waiter's web UI get a role check in v1?** §3.2 defers PIN auth, so the web UI stays on `server_id = 1`. But that means the **web UI has no role check at all** while the bot does — an asymmetry. **Recorded as a known v1 gap, not solved here.**

## Why this matters

**Because the charter says this is in scope for v1, and LE31 cannot currently do it.** Not because a vendor published a permission table — the three artifacts were the *instrument* that made the parent look, and the finding is LE31's own.

**This is the first pick in the series that is not a missing *field*.** The 85th–90th passes all found columns or states that should exist and do not. This one finds a requirement that **exists in the charter**, a field that **exists in the schema** (`UserRole`), and a setting that **exists in the config** — and the defect is that **the three are shaped incompatibly.** A per-class field audit of `AppUser` sees a `role` column and reports it as present. The thing that is missing is a **relationship**: which role a chat ID belongs to, and which capability a role carries.

**Why the cost is asymmetric, in the direction that argues for `build`:** the wrong answer is *free to write and free to ship*. Adding the allowlist as-is — a flat `list[int]` — looks like a completed feature, satisfies the charter's wording at a glance, and silently grants the cook the manager's powers. It will not fail loudly. It will be discovered, if at all, by an owner noticing something odd, with no record of who did what to audit against.

**Why the audit's series-level result matters here.** Six consecutive passes have now produced six first-party findings, and every one has come from the **code corpus**, never from the paper families. This pass's finding came from reading three GitHub READMEs and then **four greps and a `sqlite3` probe against LE31's own tree**. The papers contributed nothing. The budget belongs where the audit is.

**And the honest limit of this claim.** The audit is now producing **sibling defects of the same shape**, and this pass found **three instances of one new shape**: a rule that is **written down** and a mechanism that **cannot carry it** — a flat `list[int]` against a "role-based" requirement, a nullable column compared with `>`, a `NUMERIC` column in a non-`STRICT` table. That is the next thing to audit for. It is also the reason to be careful: this pass found the shape three times, which is a reason to check for it elsewhere, **not** a reason to believe there are only three instances.
