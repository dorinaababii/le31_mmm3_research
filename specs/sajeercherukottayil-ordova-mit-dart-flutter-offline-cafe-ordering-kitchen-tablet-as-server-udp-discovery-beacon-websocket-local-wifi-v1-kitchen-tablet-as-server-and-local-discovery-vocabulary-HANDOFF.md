# HANDOFF — Feature 381: `sajeercherukottayil/Ordova` kitchen-tablet-as-server + UDP discovery beacon (vocabulary reference)

**This is a `defer` pick — a vocabulary reference, NOT a build.** No code changes. No schema change. **And no licence to copy from: the upstream repo's licence field is `null`, which is §3.2 strictly-incompatible.** The deliverable is **one paragraph in LE31's own documentation**.

If a coding agent finds itself writing application code for this feature, it has misread the contract — stop. If it finds itself copying a port number, a file layout or a discovery mechanism out of the upstream repo, it has misread the licence — stop.

**Discovery chain:** Daily Brainstorm 2026-10-25 → GitHub Search `topic:restaurant` cluster → parent read the upstream README → parent ran the audit instrument (`grep -rni 'mdns|zeroconf|avahi|bonjour|ssdp|udp|broadcast|discover' --include=*.py backend/` → **no output**) and confirmed LE31's backend contains **no** device discovery and **no** WebSocket code at all.

**Full evidence record: `features/381-sajeercherukottayil-ordova-mit-dart-flutter-offline-cafe-ordering-kitchen-tablet-as-server-udp-discovery-beacon-websocket-local-wifi-v1-kitchen-tablet-as-server-and-local-discovery-vocabulary.md`**

## Active feature path

`features/381-sajeercherukottayil-ordova-mit-dart-flutter-offline-cafe-ordering-kitchen-tablet-as-server-udp-discovery-beacon-websocket-local-wifi-v1-kitchen-tablet-as-server-and-local-discovery-vocabulary.md` — **defer** (Pick C of Daily Brainstorm 2026-10-25).

## Seven-check gate verdict

| # | Check | Pass? | Note |
|---|-------|-------|------|
| 1 | Raison d'être / JTBD | ✗ **FAIL — by design** | The pain is **not observed**. No LE31 restaurant is currently failing to pair a device, because LE31 has no device-pairing problem — the waiter surface talks to a hosted URL and the cook surface is a Telegram bot that already has its own network identity. Evidence class: **inferred** (from one external README), confidence **low**. **This is the weakest of the three picks today, and the contract says so.** What *is* observed is a **question LE31 has never written down** ("in a one-restaurant deployment, which physical device is the server?"), which is a documentation gap, not a user pain. |
| 2 | Viability | ✓ | Trivial — one paragraph of documentation. Nothing for an operator to run, train or maintain. |
| 3 | Practicability and confidence | ✓ | On-stack requirement: **none** — no code is written, and **no code may be copied** (licence `null`). The transferable items are the *shapes*: discovery-vs-transport as separate concerns, and a four-rung degradation ladder (auto-discovery → tap-to-connect → manual IP → DHCP reservation). Both are stack-neutral. **Named rabbit hole:** whether discovery is needed at all — see Open questions 2, where the recommendation is "no, ever, if LE31 stays server-hosted". |
| 4 | Conflict | ✓ | No invariant is violated. **One conflict to respect explicitly:** `PROJECT_CHARTER.md` §3.2 **defers WebSockets in favour of polling** (and Feature 375 builds the waiter surface's status visibility on that polling model). **This feature must not reopen that decision.** The upstream project uses WebSockets throughout; **LE31 does not adopt that, and the paragraph must not imply that it should.** |
| 5 | Outcome + appetite + scope | ✓ | Serves a v1 documentation outcome (a named deployment-topology question). Maximum time worth spending: **20 minutes**. Scope is one paragraph. **Explicitly NOT in scope:** any UDP/multicast/mDNS/Zeroconf/Bonjour/Avahi/SSDP implementation, any WebSocket, any LAN relay, any Flutter/Dart, any device-as-server decision. |
| 6 | Cost to operational value | ✓ | Very low cost, low immediate operational value. The value is **option-preserving**: if LE31 ever needs zero-configuration pairing, the pattern and a working reference are already named, and the degradation ladder is known rather than reinvented. **The honest reason this file exists:** it is the **third** arrival in three consecutive passes describing the same venue boundary from the operator side (feature 376's `drsamonline/canteen-lan`, feature 380's KitchenLink LAN relay, this one) — three independent implementations of the same real-world shape is evidence about a deployment, not about a preference. |
| 7 | Circuit breaker + reversibility | ✓ | **Trivially reversible: delete one paragraph.** No data, no code, no migration. **Stop evidence:** if LE31's deployment decision is made and recorded (VPS, always-on box, or otherwise), this paragraph becomes redundant and should be **deleted**, not reworded. **Review point:** whenever the deployment topology is revisited, check whether this paragraph is still needed. |

**Gate verdict: `defer`** (parking-lot). Check 1 fails on observed evidence — deliberately. The file is honest about being the weakest of the three.

## Bucket

**v1 (device-topology vocabulary)** — Pick C of Daily Brainstorm 2026-10-25. This is a **v1-bucket** pick, so per `le31-feature-pipeline/SKILL.md` step 4 the matching project would be `le31 v1 — Core MVP` (P-HMM-3). **However**, per `le31-feature-pipeline/SKILL.md` line 33, confirm the workspace with `list_projects` before assuming — the parent confirmed on 2026-10-25 that the workspace contains exactly three projects (`le31 v1 — Core MVP` P-HMM-3, `le31 Workflow` P-HMM-2, `le31 Research` P-HMM-1); `le31 v2 owner-pains` / `le31 v2-AI` do **not** exist. Because the **parent research issue for this pass also failed to create** (Linear MCP write endpoint blocked — 38th consecutive day), the sub-issue has no parent to hang under — it is routed to `le31 Research` (P-HMM-1) in the fallback payload, and that is the only project that exists for the write.

## Files to touch

**The change (documentation only — this is the complete list):**

- `PROJECT_CHARTER.md` — **add ONE paragraph** recording (a) the **device-topology question** ("in a one-restaurant deployment, which physical device hosts the server?"), (b) the **three candidate answers** (a small always-on host in the back office; the kitchen tablet itself; the VPS), and (c) that **no answer is chosen** and this is a deployment decision, not a v1 blocker. Add a pointer to feature 376 (LAN-only ordering surface) and feature 380 (zero-cloud relay state).
- **ONE sentence** in the same paragraph recording that **LAN device discovery is a solved-enough problem to have named references** (this feature; feature 380), so it is a known unknown rather than an unexplored one.

**Do NOT touch (out of scope, explicitly):**

- `backend/app/` — **no change whatsoever.** In particular **do not add** `zeroconf`, `pyzeroconf`, `netifaces`, `multicast`, or any DNS-SD/mDNS library. **None is in the project today; do not add one for this feature.**
- `backend/app/bot/cook_bot.py` — **no change.** A Telegram bot cannot host a server; the cook's phone is not a reliable host. **Do not re-open this.**
- `backend/requirements.txt` — **no new dependency.**
- The waiter UI — no change.
- `PROJECT_CHARTER.md` §3.2's WebSocket deferral — **do not reopen it.**
- **Features 11 (`customer-qr-menu`), 375 (waiter-surface status visibility), 376 (`drsamonline/canteen-lan`), 380 (KitchenLink LAN relay)** — all already filed; **do not re-implement or re-file them.**

## Verification protocol reference

Per `le31-conventions`: *"Declaring done from a diff or passing tests alone"* is a pitfall. For a documentation-only feature the observable behaviour is **the paragraph existing in the file a future agent actually reads**, and nothing else changing.

```bash
cd /opt/data/le31_mmm3_research_work
# 1. The paragraph is present.
grep -n -i 'device topology\|which device\|topology question\|discovery' PROJECT_CHARTER.md

# 2. No code crept in — the backend must still have no discovery mechanism.
grep -rni 'mdns\|zeroconf\|avahi\|bonjour\|ssdp\|udp\|broadcast\|discover' --include=*.py backend/
# expect: NO output

# 3. Still no WebSocket in the backend (the §3.2 polling decision stands).
grep -rn 'websocket\|WebSocket\|ws://' --include=*.py backend/
# expect: NO output

# 4. No new dependency crept in.
grep -n -i 'zeroconf\|netifaces\|multicast' backend/requirements.txt
# expect: no output
```

**Verification is a negative check here.** The success condition of a `defer` vocabulary feature is that **nothing changed except one paragraph.** If any of commands 2–4 shows a change, the feature was implemented wrongly — revert it.

## Rollback path

`git revert` the commit, or delete the paragraph. **No data loss, no migration, no operator impact.** Cheapest possible rollback.

## Mandatory LE31 skill list for the coding agent

- `le31-conventions` — hard invariants and the seven-check gate (read the *State* rule — "operational transitions are explicit user actions" — and the *Privacy* rule)
- `le31-handoff-spec` — this document's format
- `PROJECT_CHARTER.md` — source of truth; **the file being edited** (§3.2 for the WebSocket deferral, §4.4 for the folder layout)
- `le31-feature-pipeline` — for the "what a `defer` pick means" contract
- **Do NOT load** `le31-backend` unless you are writing code — **this feature writes no code.** (Load it only if the owner later promotes the feature to a build, in which case a fresh contract must be written first.)

## Open questions carried into any future build

1. **Where does LE31's server physically live in a one-restaurant deployment?** Today the charter assumes a VPS, and the `le31 Workflow` project treats the VPS as part of LE31's setup — so the assumption exists, but **it has never been written down as a *decision* with a named alternative.** This is a **deployment** question, not a feature, and it should be asked **once**. It is the real payload of this feature.
2. **Does the waiter surface ever need zero-configuration pairing?** If LE31 stays server-hosted and the waiter's phone talks to a public URL, **discovery is never needed** and this feature remains a vocabulary note forever. **Recommendation: leave it exactly there — record it, do not build it.**
3. **If discovery is ever needed, is UDP broadcast acceptable in the venue's Wi-Fi?** Some enterprise APs and some phone hotspots block broadcast traffic. The upstream ladder (auto-discovery → tap-to-connect → manual IP → DHCP reservation) is the mitigation, and **if it is ever needed it must be copied as a ladder, not as a single mechanism.**
4. **Could the cook's Telegram bot ever be the server?** **No** — aiogram v3 connects *out* to Telegram's servers; the bot cannot accept inbound connections, and a phone that a staff member unplugs to charge is a single point of failure for the whole system. **Record the question; the answer is not this.**
5. **Does the deployment-topology paragraph belong in `PROJECT_CHARTER.md` or in the `le31 Workflow` project?** The VPS setup is `le31 Workflow`'s subject; the charter's §4.4 is the architecture's. **Recommendation: the charter, because the topology question constrains the architecture (a tablet-as-server would change §4.1's stack assumption).** The parent has not decided.
