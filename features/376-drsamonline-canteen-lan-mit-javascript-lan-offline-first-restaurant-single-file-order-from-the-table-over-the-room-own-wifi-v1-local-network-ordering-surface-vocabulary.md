# Feature 376 — LAN-only ordering surface vocabulary: `drsamonline/canteen-lan` (defer)

> **NEW observation (2026-10-25).** A **39 KB, single-file, LAN-only** ordering board for small venues. GitHub repo `drsamonline/canteen-lan` (**MIT ✓ §3.2 STRICTLY-COMPATIBLE — code-shape IS adoptable**), **★0/⑂0**, **39 KB — the smallest pick of the 87-pass daily-research series** (prior record: `johnohhh1/gfs-invoice-breakdown` at 18 KB on 2026-10-20; 36 KB `kinv` on 2026-10-24), **JavaScript ✗ OFF-STACK**, created **2026-10-23T01:29:25Z AND pushed 2026-10-24T15:09:22Z = IN-WINDOW BY BOTH FIELDS** (window 2026-10-18..2026-10-24), 4 topics `['lan','offline-first','restaurant','single-file']`, `default_branch=main`, `archived=false`, `fork=false`, 0 open issues. All field values read from a **direct `/repos/` GET** by the parent on 2026-10-25 (`/tmp/le31-daily-2026-10-25/pv/drsamonline__canteen-lan.json`), not from search-result numbers. Description (verbatim from GitHub API): *"Order from your table over the room's own Wi-Fi - a LAN canteen board for Forge"*.
>
> **The convergence this pick documents.** Two independent arrivals in **two consecutive windows**, from **two different sides of the same question**:
> (1) **The operator side** — HN story *"Keeping restaurant iPads in sync without a router"* (2026-10-19T14:26:33Z, https://tablelink.app/blog/ipads-in-sync-router-unplugged) — appeared in the 2026-10-24 pass and reappeared in this window.
> (2) **The software side** — this 39 KB artifact, which describes exactly that venue: ordering over the room's own Wi-Fi, with no router and no internet.
>
> Bucket: **v1 (connectivity-boundary vocabulary)** — Pick A of Daily Research 2026-10-25. Build verdict: `defer` (parking-lot; **vocabulary reference only** — no code changes, no schema change).

## Goal

Turn **"a venue whose only network is its own Wi-Fi"** from an *unconsidered* case into a **named, written-down boundary** of LE31 v1 — with a real, in-window, 39 KB artifact as the citation that proves the case is common enough to be worth naming.

**The deliverable is one sentence in LE31's own documentation.** Not a feature. Not a build.

## Scope

**In scope (defer artifact):**

- A written record of `drsamonline/canteen-lan`'s shape: single-file, LAN-only, offline-first ordering board, **39 KB total**, topics `lan` + `offline-first` + `restaurant` + `single-file`.
- A written record of the convergence: the operator-side story (`tablelink.app`, HN 2026-10-19) and the software-side artifact (this repo) arriving at the same venue profile **in two consecutive windows**.
- **One proposed boundary sentence** for LE31's charter or `le31-conventions`, stated in a form an owner can accept or reject:
  > *LE31 v1 requires a server reachable over the internet. A venue whose only network is its own LAN is out of scope for v1.*
- A **trigger condition** naming the moment the boundary should be revisited.

**Out of scope (defer artifact):**

- **Any LAN server, any offline mode, any client-side cache, any local-network discovery, any mDNS/Bonjour, any self-hosted appliance.** LE31 v1 is a single server-authoritative VPS reached over the internet (§3.2). This pick does not propose changing that.
- **Any offline-sync, outbox, or idempotency design.** Feature 373 (`ramaraihan12/warung-pos`) already filed the offline-first POS vocabulary; this pick must not re-litigate it.
- **A second ordering surface.** §3.1 says two surfaces (waiter web UI, cook Telegram bot). A guest-facing table board would be a third, and this pick does not propose one.
- **Any guest-facing QR menu.** Already covered by feature 11 (`customer-qr-menu`) and the filed QR-menu cluster.
- **A port of `canteen-lan`'s code.** It is MIT and small, so the code is legally adoptable — but adopting it would be adopting a **JavaScript LAN server** into a Python/FastAPI/Postgres product, which is exactly the stack change §3.2 requires an explicit charter decision to authorise. **The artifact is cited, not ported.**

## Description

LE31's charter §3.2 commits the product to a specific deployment: a **single server-authoritative VPS**, reached over the internet, with the waiter web UI and the cook Telegram bot as its two surfaces. §3.2 also explicitly *defers* real-time WebSocket push (*"waiter UI polls; v2 can add WebSockets"*), which is a different but related decision — LE31 is online-first by construction.

That posture is correct and should not change. **What is missing is not a capability — it is a name for the case LE31 declines to serve.**

There is a class of small venue whose network topology is: *one router, in the room, serving the venue's own devices, and that router may be offline or firewalled from the internet.* A market stall in a covered market. A café in a building whose landlord blocks inbound traffic. A venue on a restaurant-provided LTE hotspot. A venue whose POS host deliberately keeps the venue off the public internet for PCI reasons. **For these venues, LE31 v1 does not work, and no amount of frontend polish will make it work** — the server is simply unreachable.

`drsamonline/canteen-lan` is what a practitioner builds when the venue is that venue: **39 KB, one file, ordering over the room's own Wi-Fi.** The name says it — `canteen-lan`. The topic set says it — `lan` + `offline-first` + `single-file`. And it is **not an unusual artifact**: it appeared in a window where 998 GitHub repos surfaced, three of which (`canteen-lan`, `mesa-lite`, `material-request-system`) share the *no-dependency-tree, ship-it-whole* instinct, and a fourth (`CrausalX/fork`) is an offline-first cashier PWA with `Dexie` + `PWA` + `indexeddb` — the same offline posture, built with a heavier dependency tree and a third-party backend (Supabase).

**Two independent arrivals in two consecutive windows.** The 2026-10-24 pass recorded the operator-side question — the `tablelink.app` post on keeping restaurant iPads in sync *without a router*. This pass records the software-side answer, from a different author, in a different medium, in a different window, for a different (smaller) venue type. **The convergence is the finding.** A single story could be a curiosity; a story plus an independent implementation plus a near-neighbour (offline-first cashier PWA) plus a third-party backend is a **shape**.

**The shape's relevance to LE31 is entirely negative, and that is the point.** LE31 cannot serve the LAN-only venue, and the LAN-only venue is a real, recurring, independently-built case. **Naming that exclusion turns a silent gap into a decision.** A boundary that is written down is a decision a future contributor can cite, test against, and stop re-litigating. A boundary that is merely absent is an accident that gets re-litigated in every planning session — and, worse, gets discovered by the *owner* the first time a prospective venue says "we don't have internet".

**What this pick is NOT.** It is not an argument that LE31 should build offline mode. It is not an argument that LAN-only venues are a large market (no evidence of that is claimed, and none is available). It is not a feature request. It is a **one-sentence documentation change**, deferred, with a citation.

## Data model

None. No table, no column, no endpoint, no template, no migration.

## Implementation steps

None. `defer` — parking-lot vocabulary reference.

**Trigger condition (any one):**

1. **Any venue, owner, or prospective customer asks whether LE31 works without internet** — the boundary sentence must be quoted in the answer, and this pick is the citation for why the answer is "no".
2. **A PR touches deployment, networking, or the VPS topology** — the boundary sentence must appear in the PR description, so a future contributor does not "helpfully" add a LAN fallback without an explicit charter decision.
3. **The owner explicitly asks for offline or LAN-only support** — at that point this is no longer a vocabulary reference. It becomes a **v2-scale architectural decision** (client-side outbox, UUIDv7 ids, idempotent sync — the shape feature 373 already documents) and **the feature gate must be re-run from scratch** with the owner's own words as the evidence class. It would then be `reported`, not `inferred`.

## Telegram interaction if any

None today, and this is deliberate. **The cook Telegram bot is already an internet-facing surface**: a Telegram bot receives updates over Telegram's servers, so a LAN-only venue **cannot run LE31's cook bot at all** — the bot's inbound webhook is unreachable from the venue's LAN. This is worth stating plainly because it means the LAN-only case is **not a partial degradation of LE31 but a total incompatibility**, and the boundary sentence is therefore not a "degraded mode" note but a genuine scope statement.

## Dependencies

None. No new packages, no schema change, no infrastructure.

## Open questions

1. **Where should the boundary sentence live** — `PROJECT_CHARTER.md` §3.2, the `le31-conventions` skill, or both? The charter is the source of truth for product scope; the skill is what the coding agent loads. **Owner decision, not an agent guess.** The prior art for the *form* of this sentence is `le31-conventions`' own non-goal discipline.
2. **Should the boundary mention v2?** E.g. *"v1 requires internet; v2 may support LAN-only venues"* — **that would be a promise**, and a promise about v2 is exactly the kind of thing §3.1/§3.2 discipline forbids making casually. **Unmade, and deliberately unmade.**
3. **Is the LAN-only venue common enough to name, or is it a niche?** **No evidence either way, and none is claimed.** The naming is justified by *cost* (one sentence) rather than by *frequency* (unknown), which is a legitimate basis for a scope statement but should be recorded as such rather than dressed up as a market finding.
4. **Does `canteen-lan`'s implementation contain a transferable primitive** — e.g. the LAN discovery mechanism, or a single-file deployment trick? **Unknown: the repo was not read beyond its API metadata.** If the owner ever scopes LAN support, the code should be read properly (it is MIT and 39 KB) before any primitive is claimed.

## Why this matters

**Because a boundary that is written down is a decision, and a boundary that is merely absent is an accident.**

LE31's §3.2 already excludes the LAN-only venue — by consequence, not by statement. Every future contributor who asks "could we support this?" will have to re-derive that exclusion from first principles, or will quietly assume it is possible and discover otherwise at implementation time. The cost of the exclusion is zero; the cost of *not naming it* is a repeated, unfunded re-litigation, and one eventual awkward conversation with an owner whose venue has no internet.

The evidence for naming it is unusually strong for a `defer`: **a 39 KB artifact that exists only because this venue profile exists** (the smallest pick of an 87-pass series), **a second artifact with the same offline posture and a heavier dependency tree** (`CrausalX/fork`, Dexie/PWA/indexeddb), **a third-party backend dependency in that same cluster** (Supabase), and **an operator-side story from outside the software ecosystem** — all in a 7-day window, with the operator-side half recurring in two consecutive windows.

**The vocabulary transfers and the code does not.** `MIT` means the code is adoptable; adopting it would be a stack change requiring an explicit charter decision, and would also add a third surface. What transfers is the *sentence* — and sentences are exactly what the previous pass found in `kitchen-erp` (*"Decimal money, append-only facts, no required outbound calls"*) and in `kinv` (*"without stock-valuation busywork"*). **Three passes, three one-sentence prior arts, each naming an exclusion LE31 already holds implicitly.** The accumulating pattern is itself the argument: LE31's boundaries are correct, and they are worth writing down.

**Fully reversible (vocabulary-only artifact).** Trigger condition: an owner question about internetless venues, a PR touching deployment or networking, or an explicit owner request for offline support — at which point this is re-gated from scratch with `reported` evidence.
