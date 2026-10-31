# Feature 402 — `rockcut/restaurant-reservation-system`: **the guard that lives below the UI** (Supabase RLS), and a **real deployed restaurant's** account of what paper costs (defer)

> **NEW observation (2026-10-29, parent-verified).** Documents in-window GitHub repo `rockcut/restaurant-reservation-system` (**MIT ✓ §3.2 STRICTLY-COMPATIBLE**, **★0/⑂0**, **238 KB**, **TypeScript ✗ off-stack** — Next.js + Tailwind + Supabase, `archived=false`, `fork=false`, created **2026-07-16**, pushed **2026-10-26** = **in-window by `pushed_at` ONLY** — a 3.5-month-old repo with an in-window push). All fields parent-verified via a **direct `GET /repos/`** on 2026-10-29 (`/tmp/le31-daily-2026-10-29/parent/rockcut__restaurant-reservation-system__repo.json`), **never from search-result numbers**. README read in full by the parent (`/tmp/le31-daily-2026-10-29/parent/rockcut__restaurant-reservation-system__README.md`, 9,133 bytes, Japanese; repo tree 37 files including `docs/requirements.md`, `docs/database.md`, `docs/api.md`, `frontend/app/`, `frontend/components/Seat.tsx`, `frontend/components/SeatLayout.tsx`).
>
> **Why this artifact and not another.** It is the **only in-window artifact describing a system actually running in a real restaurant** — not a demo, not a prototype, not a hackathon entry. Its README says so, and names the store. Verbatim:
>
> > *"個人経営の飲食店 **AuVingtQuatre** で実際に使用することを目的として開発している、予約管理Webアプリケーションです。"* ("a reservation-management web application, developed with the aim of **actually being used** at the individually-run restaurant **AuVingtQuatre**.")
> > *"現在は店舗のiPadに導入し、実際の運用を想定した試験・改善を進めています。"* ("it has now been **introduced on the restaurant's iPad**, and we are proceeding with trials and improvements assuming actual operation.")
> > *"**データベース側でも権限制御** — Editor / Viewerの権限制御はフロントエンドだけに依存せず、**Supabase RLSでも制御**しています。そのため、Viewerが直接データベースへの更新処理を実行しようとしても、予約データを変更できない構成になっています。"* ("**permission control on the database side too** — the Editor/Viewer permission control does not rely on the front end alone, but is **also enforced with Supabase RLS**. Therefore, even if a Viewer attempts an update directly against the database, they **cannot change the reservation data**.")
> > *"**閲覧と予約追加の操作を分離** — 予約済みの席をクリックした場合は「予約詳細の確認」を優先し、空席をクリックした場合は「新規予約の席選択」として扱います。同じ席UIを利用しながらも、ユーザーの操作目的によって処理を分けることで、店舗での誤操作を減らすようにしています。"* ("**separate the 'view' and 'create reservation' operations** — clicking an occupied seat prioritises 'view reservation details'; clicking a free seat is treated as 'choose a seat for a new reservation'. Using the same seat UI but branching the handling by the user's intent, **to reduce mis-operation in the store**.")
> > *"**複数席を使用する予約への対応**"* ("support for reservations that use **multiple seats**")
> > *"**席交換** — 予約時に設定した席と、当日実際にお客様を案内した席が異なる場合に対応するため、席交換機能を実装しています。通常の予約編集とは分離した専用の席交換モードを用意しています。"* ("**seat swap** — because the seat configured at booking time may differ from the seat the party is actually given on the day, we implemented a seat-swap function, with a **dedicated seat-swap mode separated from ordinary reservation editing**.")
>
> **⭐ The first-party gap this names, parent-verified against LE31's own code.** `backend/app/security.py` exists and is a **JWT + PBKDF2-SHA256 authentication layer** — it proves *who you are*. It does **not** prove *what you may change*. `grep -rn "CHECK\|check_constraint\|Constraint" backend/` → **no output**; there is **no row-level-security equivalent, no storage-layer guard, and no state-dependent action rule anywhere in `backend/`**. LE31's charter requires *"operational transitions are explicit user actions"*, and **an action enforced only in the UI is not explicit** — it is a convention.
>
> Bucket: **v1 (vocabulary only, parking-lot defer)** — Pick C of Daily Research 2026-10-29. Build verdict: **`defer`** (vocabulary-only; **no code is adopted** — and **deliberately scoped so that the reservation domain is NOT pulled into v1**: LE31 has no reservation model, and §3.2 fixes the surface count to a waiter web UI and a cook Telegram bot).

## Goal

Retain, as a **written, quotable reference**, the **two rules** this artifact states that LE31's charter implies but never makes operational:

1. **The guard must live below the UI.** An action that the charter calls *explicit* must be enforced by something that is **not the interface**. The artifact's rule is stated in one sentence: *"Editor / Viewerの権限制御はフロントエンドだけに依存せず、Supabase RLSでも制御しています"* — and the consequence is stated too: a Viewer *cannot* change the data even by going straight at the database. LE31 has **no such layer**, and LE31's `security.py` proves identity without constraining action.
2. **The same control may resolve to different intents depending on the state it is clicked in.** *"予約済みの席をクリックした場合は「予約詳細の確認」を優先し、空席をクリックした場合は「新規予約の席選択」として扱います"* — one seat widget, two intents, decided by the state behind it. This is a **UI-rule** pattern with a hard dependency on rule 1: if the guard is only in the UI, the state-dependent branch is a *suggestion*, not a rule.

And record the **third, more interesting observation** this artifact supplies — not as a feature, but as evidence:

3. **A reservation occupying more than one table has no analogue in LE31's model at all.** The artifact's operator pain list includes *"複数席を使用する予約"* — a booking that joins tables 1+2+3. LE31's `Table` model is **one table per row** (`backend/app/models.py` line 64: `__tablename__ = "table_"`), and LE31 has **no reservation concept whatsoever**. **This is recorded as a scope observation, explicitly NOT proposed for v1.**

**No code today.** This feature is a **written record** plus **two named decisions**. It changes **zero lines** of `backend/app/models.py` and **zero lines** of the backend.

## Scope

**In scope (defer artifact):**

- A written record of the **storage-layer guard rule** (RLS as the enforcement point), with the verbatim quotes above, and the LE31-specific statement of what it would mean for a `StockEntry` or `OrderItem.status` write.
- A written record of the **state-dependent action rule** (one control, two intents, decided by state), and the requirement that it be backed by rule 1.
- A written record of the **Editor/Viewer two-role split** as the minimum permission granularity a one-restaurant system actually needs, and the mapping question for LE31's waiter/cook split.
- A written record of the **operator pain list from a real restaurant** (paper bookings, joined tables, assumed-vs-actual seat, differing staff permissions) as **evidence about what a single restaurant actually needs**, and the explicit statement that **joined tables and seat-swap are out of v1 scope**.

**Out of scope (defer artifact):**

- **Any code, table, column, row-level policy, endpoint, or bot command.** This feature changes **zero lines** of `backend/app/models.py` and **zero lines** of the backend.
- **Any reservation model.** **LE31 has no reservations and §3.2 fixes the surface count** (waiter web UI + cook Telegram bot). **This is the single most important thing this feature does *not* adopt** — the domain is excellent and it is still out of scope.
- **Any adoption of the `rockcut` codebase**, its Next.js/Tailwind stack, its Supabase schema, its RLS policies, its Japanese UI, its iPad deployment, its reservation editor, its seat-layout component, or its normalised-kana search (which is a nice idea — *"たなか"* / *"タナカ"* search normalisation — and is **also** out of scope).
- **Any change to the waiter/cook role split** in the charter. **The mapping is recorded as a question, not a change.**
- **A new Linear sub-issue in `le31 v2 owner-pains` or `le31 v2-AI`** — those projects **do not exist**; per `le31-feature-pipeline/SKILL.md` line 33 the sub-issue attaches to **`le31 Research`** (P-HMM-1).
- **Any change to `PROJECT_CHARTER.md`** — the charter is the owner's document.

## Description

### What the artifact is

A **reservation-management web application for one restaurant**, built and being trialled on that restaurant's own iPad. The README is unusually complete for a small project: it lists the **operator pain** that motivated it, the **feature set**, the **permission model**, the **design decisions**, and a *docs/` folder* with `requirements.md`, `database.md`, `api.md`, `ui.md`, `meeting.md`.

The pain list, verbatim in substance, is the most valuable part of the whole window:

> *"店舗では、電話で受けた予約を紙を中心に管理していました。"* — "the store managed phone bookings on paper."
>
> *"予約状況を確認するために紙を確認する必要がある"* — "to check the booking status you have to fetch the paper."
>
> *"どの席にどの予約が入っているか把握しにくい"* — "it is hard to tell which booking is at which seat."
>
> *"複数テーブルを連結して使用する予約がある"* — "some bookings join multiple tables."
>
> *"予約時に想定した席と実際に案内した席が異なる場合がある"* — "the seat assumed at booking time sometimes differs from the seat actually given."
>
> *"スタッフによって必要な操作権限が異なる"* — "**different staff need different operational permissions**."

That last one is the sentence that makes this artifact worth filing.

### The two rules, and why they are LE31 rules

**Rule 1 — enforce below the interface.** The artifact's stated reasoning is not security-theatre; it is *mis-operation*:

> *"**閲覧と予約追加の操作を分離** … ユーザーの操作目的によって処理を分けることで、**店舗での誤操作を減らす**ようにしています。"* ("…by branching the handling according to the user's intent, **to reduce mis-operation in the store**.")

and the mechanism:

> *"Editor / Viewerの権限制御はフロントエンドだけに依存せず、**Supabase RLSでも制御**しています。"*

For LE31 this is a **§3.2 read**: the charter says operational transitions are **explicit user actions**. It does not say *where* the explicitness is enforced. This artifact answers: **not only in the UI.** Today LE31 has a JWT layer that answers "who are you" and **nothing** that answers "what may you change" — so every permission rule LE31 has today is a **UI convention**.

**Rule 2 — one control, state-dependent intent.** The seat widget is the same control; the *intent* is derived from the state behind it. For LE31 this maps onto surfaces it already has: clicking a table that is free vs. a table that is seated vs. an item that is `ready` vs. `served` should not be the same action. LE31's `ItemStatus` (`backend/app/models.py` lines 35–40) and `Table` model already have the states that would drive such a branch; **the artifact supplies the rule that a branch must be backed by a storage-layer guard, or it is merely a convention.**

### The domain mismatch, stated plainly

Everything about this artifact's *domain* is out of LE31's v1 scope:

| Artifact | LE31 v1 |
|---|---|
| Reservations (phone bookings, seat allocation, waitlist) | **no reservation concept at all** |
| Joined tables (1+2, 2+3, 1+2+3) | one `table_` row per table |
| Seat swap at service time | **no seat-swap concept** |
| Next.js + Tailwind + Supabase (RLS) | FastAPI + SQLModel + Postgres (aiogram v3 for the cook) |
| iPad front-of-house | waiter web UI + cook Telegram bot |

**The permission pattern is the transferable half; the domain is not.** This feature is scoped to make that boundary explicit, because a reader who sees *"real restaurant, real deployment, real staff permissions"* could otherwise be tempted to open a reservation feature — and that would be a §3.2 scope violation.

### The third observation, recorded and explicitly not proposed

The **joined table** is the only concept here with **no analogue in LE31's model**. `Table` is one row per table. A booking that joins three tables has no representation. That is recorded because it is a genuine gap in the *domain model* — and it is **not proposed**, because reservations are out of v1 scope and adding a join table to `Table` **now** would be building a reservation model's foundation without the reservation model.

## Data model

**No schema change today.** This feature records two rules and one out-of-scope observation; it adds no columns and no policies.

If the two rules are ever promoted, the shapes are:

1. **Storage-layer guard.** For Postgres this is **row-level security** (`CREATE POLICY`), which is available on LE31's production database but **not present anywhere today**. The design question is **which tables carry policies and what the policy predicate reads** — for LE31 the natural subject is *"which staff may change this `Batch`/`OrderItem`/`StockEntry`"*, which requires the acting user's identity to be reachable **inside the database session**, not only in the request. **That is a real architectural question (session variable vs. a claims table) and it is the reason this is a `defer` and not a `build`.**
2. **State-dependent action rule.** No schema change — but it **requires** rule 1 to be meaningful, and it does impose a constraint on the *interface* layer: a control whose action depends on state must be rendered from **server-read state**, not from a client-side guess.

## Implementation steps

**None.** This is a `defer` artifact — rules and one decision only. If the owner promotes rule 1, the implementation belongs to a **new, separately-gated** feature (it is an architecture change, not a vocabulary change) and would need:

- A decision on how the acting user reaches the database session.
- A policy per guarded table.
- A test that attempts the forbidden write **directly against the database**, bypassing the API — because an API-level test proves nothing about rule 1.

If the owner promotes rule 2 only, it is a UI-layer change with a server-read-state requirement.

## Telegram interaction if any

**None today.** The artifact's controls are all **front-of-house** (the host stand on an iPad). LE31's second surface is the **cook Telegram bot**, and the bot's authority questions — *may this cook mark an item `ready`? may this cook reverse a `StockEntry`?* — are exactly where rules 1 and 2 would bite first. **Recorded as the most likely first consumer of the pattern, not proposed.**

## Dependencies

- **Feature 400** — the same window's parallel artifact (records the idempotency key and the void/reversal event — **both are permission-bearing writes**).
- **Feature 382** — stock-deduction idempotency + shortfall (the write path a storage-layer guard would protect).
- **Feature 388** — table state machine (owns `Table` and `OrderItem.status`; **the state that would drive a state-dependent action rule**).
- **Feature 397** — menu availability / sold-out state (a state-dependent control on the waiter UI).
- **Charter §3.2** (two surfaces, fixed stack) and **§3.4** (AI may assist staff with observable evidence and a non-AI fallback — a permission question is *never* an AI question) — `/opt/data/le31_mmm3_research_work/PROJECT_CHARTER.md`.
- **`backend/app/security.py`** — the existing JWT/PBKDF2 layer, which this feature identifies as **identity-only**.

## Open questions

1. **How does the acting user reach the database session?** Postgres RLS predicates read session state (`SET LOCAL app.current_user_id`, or a `request.jwt.claim` style setting). LE31 currently authenticates in FastAPI. **The bridging mechanism is undecided, and it is the blocker on rule 1.**
2. **Which tables get policies?** `stock_entry` and `order_item` are the obvious candidates; `menu_item` and `table_` may need none. **Undecided.**
3. **Does the waiter/cook split map onto Editor/Viewer, or is it orthogonal?** The artifact's Editor can create, edit and delete; a LE31 cook probably cannot *create* an order but must be able to *advance* one. **The mapping is a real question, and the answer may be "neither" — LE31's roles are not permission levels.** **Undecided.**
4. **Does a state-dependent control require server-read state to be rendered, or only to be enforced?** The artifact enforces in both places. **Undecided.**
5. **Is RLS even the right mechanism for a one-restaurant system with two roles?** A simpler answer — an explicit authorisation check in the service layer — is possible and much cheaper. **The artifact does not prove RLS is required; it proves that *some* layer below the UI must enforce it.** **This is the most important open question in this feature.**

## Why this matters

LE31's charter says *"operational transitions are explicit user actions"*. It says **nothing** about where that explicitness is enforced, and today's answer is effectively **nowhere below the UI**: `backend/app/security.py` is a JWT + PBKDF2 authentication layer, and `grep -rn "Constraint" backend/` returns **nothing** — there is no row-level guard, no check constraint, and no state-dependent action rule anywhere in the codebase.

This artifact supplies, from a **system actually running in a real restaurant on that restaurant's own iPad**, three things LE31 does not have:

1. a **named place** to put the guard (below the UI), with the consequence stated (*"even a direct database write cannot change the data"*);
2. a **rule** for the common case (one control, state-dependent intent, so a mis-click cannot do the wrong thing);
3. a **concrete operator pain list** from a single restaurant — paper bookings, joined tables, assumed-vs-actual seat, differing staff permissions — which is the best available evidence in this window about what one restaurant actually needs, and which is **mostly out of LE31's v1 scope**, and is recorded as such rather than smuggled in.

The cost of deciding rules 1 and 2 is now is one paragraph each. The cost of deciding them after the first production write site is a **retrofit that touches every write path in the system**.
