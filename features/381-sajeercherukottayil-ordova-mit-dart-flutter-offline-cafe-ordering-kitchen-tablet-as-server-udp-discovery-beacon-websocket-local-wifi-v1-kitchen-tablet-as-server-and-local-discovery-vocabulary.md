# Feature 381 — `sajeercherukottayil/Ordova`: the kitchen tablet as the server, and UDP discovery as the answer to "how does the waiter's phone find the kitchen?" (defer)

> **NEW observation (2026-10-25).** Documents in-window GitHub repo `sajeercherukottayil/Ordova` (**licence: `null` ✗ §3.2 STRICTLY-INCOMPATIBLE — the *vocabulary-shape* is the transferable item; the *code-shape* is NOT adopted**), **★0/⑂0**, **6,041 KB**, `default_branch=main`, `archived=false`, created **2026-10-19T00:00:00Z AND pushed 2026-10-22T00:00:00Z = IN-WINDOW BY BOTH FIELDS**, 6 days old at the time of the pass. All field values read from a **direct `/repos/` GET** by the parent on 2026-10-25, not from search-result numbers. Description (verbatim from GitHub API): *"Offline café ordering & kitchen display app in Flutter. Waiter phones and a kitchen tablet sync over local Wi-Fi with WebSockets. No internet needed."*
>
> Bucket: **v1 (device-topology vocabulary)** — Pick C of Daily Brainstorm 2026-10-25. Build verdict: **`defer`** (parking-lot; **vocabulary reference only** — no code changes, no schema change, and **no licence to copy from**).

## Goal

Retain `sajeercherukottayil/Ordova` as the external arrival that answers a question LE31 has never asked in writing:

> **In a small restaurant, which device is the server?**

Ordova's answer is concrete and testable: **the kitchen tablet is the server.** It holds all data, serves the WebSocket on port 4567, shows the ticket board, and announces itself on a **UDP discovery beacon on port 4568** so that waiter phones find it without typing an IP address.

**The deliverable is one paragraph in LE31's own documentation** recording the *question*, the *candidate answers*, and why LE31 has not chosen one.

## Scope

**In scope (v1 — documentation only):**
- One paragraph naming the device-topology question and recording the three candidate answers (kitchen tablet as server / a small always-on host / the VPS).
- One sentence recording that **UDP multicast/broadcast discovery on a shop LAN is a real, working pattern** — so that if LE31 ever needs zero-configuration device pairing, the pattern is known to exist and has a known reference.

## Out of scope (v1)

- **Any code or port from this repo.** The licence is `null` — §3.2 strictly-incompatible. **Nothing is copied. The vocabulary is the deliverable.**
- Any UDP, multicast, mDNS, Zeroconf, Bonjour, Avahi, or SSDP implementation in LE31. **LE31's backend contains none of these today** (parent-verified 2026-10-25: `grep -rni 'mdns|zeroconf|avahi|bonjour|ssdp|udp|broadcast|discover' --include=*.py backend/` returns **no output**).
- Any WebSocket transport. LE31's backend contains **no WebSocket code today** (parent-verified 2026-10-25: `grep -rn 'websocket|WebSocket|ws://' --include=*.py backend/` returns **no output**), and `PROJECT_CHARTER.md` §3.2 explicitly defers WebSockets in favour of **polling** (see Feature 375).
- The LAN-only ordering surface — **already filed as Feature 376**; not re-picked.
- The zero-cloud relay concept — **already filed as Feature 380**; not re-picked.
- Flutter/Dart. LE31's waiter surface is FastAPI + HTML/HTMX; the cook surface is aiogram v3.
- Any allergen or dish-metadata work — **Feature 380** owns that vocabulary.

## Description

The upstream README (quoted facts about *that* project):

> *"Kitchen device (ground floor): holds all data, shows the live ticket board, beeps on new orders."*
> *"Waiter phones (first floor): pick a table, add items, send to kitchen, get a sound when an order is ready."*
> *"lib/server/kitchen_server.dart: HTTP/WebSocket server on port 4567, JSON file storage, UDP discovery beacon on port 4568."*
> *"On the kitchen tablet: open Ordova and choose Kitchen. Its IP is shown at the top. On each waiter phone: open Ordova and choose Waiter. The kitchen should appear automatically; tap it. If it doesn't, type the IP."*
> *"Tip: give the kitchen tablet a fixed IP (DHCP reservation) in the router so waiters never need to reconnect."*

Three things worth taking, none of them code:

1. **The topology question itself.** LE31's architecture (§4.1, §4.4) assumes a deployed FastAPI server and a Postgres database. It has never written down **where that server physically lives in a one-restaurant deployment** — the VPS (today's assumption), a cheap always-on box in the back office, or the kitchen tablet itself. This is a **deployment-topology** question that is not a v1 blocker but has never been asked out loud.

2. **Discovery as a distinct concern from transport.** Ordova separates them: the WebSocket carries orders; the UDP beacon on a *different port* answers *"who is the server?"*. That separation is the transferable shape: **device discovery and data transport are different problems with different failure modes.** LE31 currently has neither, but when it needs either, it should know they are separate.

3. **The fallback ladder is explicit.** *"The kitchen should appear automatically; tap it. If it doesn't, type the IP."* — discovery, then a tap-to-connect UI, then manual IP entry, then **DHCP reservation** as the operational fix. That is a **four-rung degradation ladder** for one problem. LE31's waiter surface has no such ladder because it has no such problem yet; recording the shape costs one sentence and prevents reinventing a worse version later.

**Note the contrast with LE31's own surfaces.** LE31's cook surface is a **Telegram bot** — the cook's phone already has an app and a network identity, so LE31 never faces "how does this device reach the server". Its *waiter* surface is the one that would face it. Ordova's answer — one device holds the data and everything else connects to it — maps onto LE31's cook-Telegram-bot topology **only partially**: a Telegram bot cannot be the server; the phone it runs on is not a reliable host.

## Data model

**No change.** No table, no column, no migration.

## Implementation steps

1. **A short paragraph in the charter's §4.4 (Folder layout) or a separate note** recording the device-topology question and the three candidate answers, with a pointer that no answer is chosen.
2. **One sentence** recording that LAN device discovery is a solved-enough problem to have named references (this feature; Feature 380's LAN relay), so it is not an unknown.
3. **Do not touch** `backend/app/`. **Do not add a dependency** (`zeroconf`, `pyzeroconf`, `netifaces` — none are in the project today; do not add one for this feature).

## Telegram interaction if any

None. The cook Telegram bot is unaffected. The *only* LE31 surface this touches, if it ever does, is the **waiter web UI** — and this feature changes nothing about it.

## Dependencies

- `PROJECT_CHARTER.md` (edit, one paragraph) or a sibling note file.
- **No code dependency. No new package.**

## Open questions

1. **Where does LE31's server physically live in a one-restaurant deployment?** Today the charter assumes a VPS. **Is a VPS acceptable to the owner?** This is a **deployment** question, not a feature, and it should be asked once. (Note: the 2026-10-25 daily-research cron reported the VPS as part of the `le31 Workflow` project's scope, so the assumption exists — but it has never been written down as a *decision* with an alternative.)
2. **Does the waiter surface ever need zero-configuration pairing?** If LE31 stays server-hosted with the waiter's phone talking to a public URL, **discovery is never needed** and this whole feature stays a vocabulary note forever. **Recommendation: leave it at that.** Record it; do not build it.
3. **If discovery is ever needed, is UDP broadcast acceptable in the venue's Wi-Fi?** Some enterprise APs and some phone hotspots block broadcast traffic. The ladder in the upstream README (discovery → tap → manual IP → DHCP reservation) is the mitigation, and **it should be copied as a ladder, not as a single mechanism**, if it is ever needed.

## Why this matters

Feature 376 (2026-10-25) named the *venue whose only network is its own Wi-Fi*. Feature 380 named the *zero-cloud fallback state*. This feature names the **device topology that makes those two possible** — and it does so with the one artifact in the window that actually *works* that way.

The honest framing: **this is the weakest of the three picks, deliberately placed third.** The licence is `null`, the stars are zero, and the codebase is Flutter — none of which can be adopted. What it contributes is a **question LE31 has never written down** (which device is the server in a one-restaurant deployment?) together with a **worked reference** for the answer.

Two things keep it from being filler:

- **It is the third arrival in three passes describing the same boundary from the operator side.** Feature 376's `drsamonline/canteen-lan` (39 KB, single-file, LAN-only), Feature 380's KitchenLink (SwiftUI, LAN relay, zero-cloud fallback), and this one (Flutter, kitchen tablet as server, UDP discovery) are three independent implementations of the same venue shape. **Three independent implementations is evidence about a real deployment, not about a preference.**
- **The "UDP discovery beacon" is one specific, nameable technique** — not a vague "they had some kind of local network thing". A future LE31 pass that needs zero-config pairing can start from a known pattern instead of rediscovering it. That is what a vocabulary reference is for.

**What this feature deliberately does not do:** it does not propose that LE31 run its server on a kitchen tablet. The cook's Telegram bot cannot host a server, and a tablet that a staff member unplugs to charge is a single point of failure for the whole system. **The question is worth writing down. The answer is not this one.**
