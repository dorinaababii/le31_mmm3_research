# Feature 498 — `v2-signed-versioned-rule-pack-with-local-manual-override`

> **Pick A of Daily Research 2026-11-19.** **Bucket: v2 (new bucket — justified below).** **Verdict: `defer` — parking-lot vocabulary reference.**
>
> **Source artifact:** `FreeOpenSourcePOS/FloCafe` — MIT, ★195 / ⑂92, TypeScript/Electron, created 2026-05-07, pushed 2026-11-19T03:15:51Z. Parent-verified direct repository GET: `/tmp/le31-daily-2026-11-19/gh/repo_01_FreeOpenSourcePOS_FloCafe.json`; README: `/tmp/le31-daily-2026-11-19/gh/readme_01_FreeOpenSourcePOS_FloCafe.md`; source URL: https://github.com/FreeOpenSourcePOS/FloCafe.
>
> **Why this pick:** one README states a **distribution channel for business rules** as a first-class product surface — *"signed, versioned country tax packs for regional rules, tax categories, and rounding policies"* — with a deliberate **local escape hatch**: *"Operators can also configure manual tax rules and rates locally"*, and a **generic calculation engine** underneath. LE31 has business rules baked into code and has no channel by which a rule arrives, nor a documented precedence between a distributed rule and a local one.
>
> **Why it is net-new:** the parent ran a targeted dedup sweep across all **1,022 feature and spec files** in the repository before selecting this pick: `(signed|versioned).{0,30}(pack|bundle|catalog)` → **0 files**; `tax.{0,20}pack` → **0**; `(rule|calculation).{0,20}pack` → 3 (two `shiftwright` HANDOFFs about *rule-explaining* rota logic, one `agent-audit-kit` feature about a static rules catalogue — neither is a signed distributable channel); `rounding polic` → 2 (feature 411's money-precision guard, which owns *precision enforcement*, not *rule distribution*); `distributab` → 1 (feature 64's retail-localization pattern). The **signed + versioned + distributable** triple has never been written down in the corpus.
>
> **Boundary with feature 411 (money-precision-guard):** 411 owns whether a decimal survives the database. This pick owns **how a rule arrives and how it is overridden**. A pack may carry a rounding policy; 411 then enforces it. They are different concerns and neither is a subset of the other.
>
> **Bucket justification (new bucket):** no existing bucket covers "a distributable rules channel". It is not v1 (the charter fixes a flat tax and forbids the scope), not v2 owner-pains (the owner-pains bucket is workflow/ops surface for the owner), and not v2-AI (there is no model in this mechanism). It is recorded as **v2** because it is a capability that arrives only after a multi-country or per-category tax decision exists — the class of work LE31 defers past v1.
>
> **Project constraint:** the workspace contains only `le31 v1 — Core MVP` (P-HMM-3), `le31 Workflow` (P-HMM-2), and `le31 Research` (P-HMM-1). The matching Linear sub-issue is attached to `le31 Research`; no v2 project was invented.

## Goal

Record the source artifact's **rule-pack distribution channel** as the reference design for any future LE31 rule that arrives from outside the codebase:

1. a rule arrives as a **pack** — a named, self-contained bundle of rules, not a code change;
2. a pack is **signed** — its provenance is verifiable without trusting the operator;
3. a pack is **versioned** — an operator can pin, and can tell which version is in force;
4. a pack declares its **own scope** (here: country, tax categories, rounding policies) so that two packs in force at once have a defined relationship;
5. a pack is evaluated by a **generic calculation engine**, so adding a rule category does not mean adding an engine;
6. a **local manual override always wins over the pack** — the operator can deviate per site without editing the pack;
7. the vendor's own **disclaimer** is part of the design: a pack is software, not compliance certification, and the operator remains responsible for the rules that apply to their business.

No pack format, no signature scheme, no engine and no override-resolution code is built by this feature.

## Scope

**In scope (defer artifact):**

- Verbatim source evidence and the seven-point mechanism summary above.
- The explicit conflict with charter §3.3 open question 3 and §3.1's flat-tax rule, recorded rather than resolved.
- The dedup result that establishes the mechanism is net-new to the corpus.
- The explicit boundary with feature 411 (precision enforcement) and with feature 408/411 (tax rate home and rounding).
- The precedence rule that the contract states as the design's load-bearing sentence: **local manual override wins over the pack.**
- A future-project attachment decision: `le31 Research`, because no v2 project exists and this pick is not v1 work today.

## Out of scope

- No pack format, no schema, no signing key handling, no signature verification.
- No pack catalogue, no registry, no distribution endpoint, no update channel.
- No tax calculation engine and no change to how any bill total is computed today.
- No change to the waiter web UI, the cook Telegram bot, the `StockEntry` ledger, or the bill lifecycle.
- No adoption of the TypeScript/Electron stack.
- No country coverage plan, no pack authoring tooling, no localisation of the shipped UI (§3.2 already excludes UI internationalisation).
- **No resolution of charter §3.3 open question 3.** This feature explicitly does not decide whether tax is flat, per-category or per-item.

## Description

The source artifact's README describes three separable pieces that together form the mechanism:

**1. The pack.** *"FloCafe includes a generic calculation engine and supports signed, versioned country tax packs for regional rules, tax categories, and rounding policies. Country coverage is expanding through the catalog, and availability varies."* Three attributes are load-bearing: **signed** (provenance is checkable), **versioned** (an operator can pin), and **scoped** (a pack declares what it governs, so packs do not collide silently).

**2. The local override.** *"Operators can also configure manual tax rules and rates locally."* This is the part that makes the whole design survivable in practice: a distributed rule that the operator cannot override is not a distributed rule, it is a hostage situation. The source gives local rules **precedence** over the pack, and the pack is still the default. The contract records the same precedence: **local manual override wins.**

**3. The disclaimer.** *"FloCafe is software, not legal or tax advice. Tax packs and configuration tools do not by themselves certify compliance with local regulations. Operators remain responsible for verifying the requirements that apply to their business."* A rules-distribution channel without an explicit statement of who is responsible for the outcome is a liability transfer the operator did not agree to. The contract records the disclaimer as part of the mechanism, not as marketing copy.

**What LE31 does not have.** LE31 computes tax in code, in one place, with a flat rate by charter default. Feature 408 records that *"tax rate has no home"* — the tax rate is a free-floating money number. Feature 411 records that precision is *declared but not enforced*. Both are **inside** the codebase. This pick is about a rule arriving from **outside** the codebase, with a verifiable provenance and an overridable default. It is a strictly different concern: 408/411 are "is our own tax number right?", this is "who decides what the tax rule is, and can the operator say no?".

**Why the source's own limits are recorded rather than hidden.** The README does not specify the pack format, the signature scheme, the trust root, or the override-resolution order beyond "local wins". So this contract records a **shape**, not a copyable design. A future implementation would have to specify all four, and this contract is honest that they are unspecified.

**Adjacent but not owned.** The source also ships *"Granular roles & permissions: Owner, Manager, Cashier, Server, and Chef roles with context-aware access policies"* (27 corpus files match the RBAC family; feature 403 owns the permission matrix) and *"Cash drawer management: Cash pulse on checkout and end-of-shift cash drawer reconciliations"* (feature 426 owns shift close and cash variance; feature 391 owns the shift-variance derivation). Neither is bundled into this feature.

## Data model

**None is created by this feature.** The following is a *reference shape* recorded for a future implementation, and it is deliberately not a schema:

```
RulePack
  pack_id          opaque identifier
  pack_version     monotonic version string, pinnable by the operator
  scope            what the pack governs (e.g. country, tax categories)
  signature        signature over the pack content
  publisher        who published it
  published_at     when it was published

LocalRuleOverride
  scope            the same scope key as the pack it overrides
  rule_key         the specific rule within the scope
  local_value      the operator's value
  effective_at     when the operator's value takes effect
```

**The precedence rule, stated once, as the contract's load-bearing sentence:** *a `LocalRuleOverride` matching a pack rule takes effect in preference to that pack rule; the pack remains the default for every rule not overridden.*

**The reference shape is deliberately incomplete**, and the gaps are named rather than guessed: the pack's **content format** is unspecified, the **signature algorithm and trust root** are unspecified, and the **conflict order between two packs of different scopes in force simultaneously** is unspecified. An implementer must decide all three and record the decision. A contract that guessed them would be worse than one that names them.

## Implementation

**No implementation is authorised by this feature.** It is a `defer` reference.

If a future feature is separately approved, the plausible touch points would be:

- `backend/app/models.py` — future `RulePack` and `LocalRuleOverride` models;
- `backend/app/services/rules.py` — future rule resolution: pack lookup, signature verification, override precedence;
- `backend/app/services/tax.py` — future call site replacing the current inline tax computation;
- `backend/app/routers/rules.py` — future pack listing and local-override CRUD routes;
- tests — override-wins-over-pack, pinned-version resolution, two-scopes-in-force, unsigned-pack rejection.

**Ordering constraint.** A future implementation must land **after** the charter's §3.3 question 3 is answered and after the tax rate has a home (feature 408). A pack channel that writes into a free-floating tax number would make the existing defect unfixable rather than fixable.

## Telegram interaction

**None.** The cook Telegram bot is not a consumer of rule packs in this disposition, and no bot command is added. A future owner-facing surface for "which pack is in force and what have I overridden" would be a separate feature; the chat-id allowlist model (feature 403) means a new bot command would need its own owner decision.

## Dependencies

**Existing LE31 features this pick depends on or is adjacent to:**

- **Feature 408** (`tax-rate-and-rounding`) — the tax rate needs a home before any rule channel can write into it. **Prerequisite.**
- **Feature 411** (`money-precision-guard`) — the precision guard becomes the thing that enforces a pack's rounding policy. **Adjacent, not owned.**
- **Feature 403** (`role-carrying-bot-chat-table`) — the local-override surface needs an actor. **Adjacent.**
- **Feature 496** (`audit-ready-daily-export-with-financial-reconciliation-identities`) — a pack in force is a fact an export may need to state. **Adjacent, and deliberately not bundled.**
- **Charter §3.3 question 3** — *Tax — flat 10%? Per-category? Per-item?* **Blocking.**

**External dependency:** none. The source artifact is a MIT-licensed reference, not a code dependency; nothing is imported.

## Open questions

1. **Does the charter's §3.3 tax question get answered as per-category?** If the answer is "flat forever", this pick has no consumer and should be deleted rather than deferred.
2. **What is the trust root?** If packs are signed, who signs them and how does an operator obtain the public key without trusting the same channel that delivered the pack?
3. **Two scopes in force at once** — a country pack and a city pack, say. Which wins? This is unspecified in the source and must be decided before any implementation.
4. **What is the pack format** — and is it a data format (JSON/YAML) or a plugin? A plugin format turns a signed pack into executable code, which changes the security model completely.
5. **Does the override apply per-site or per-rule?** The source says "local tax rules and rates", which suggests per-rule, but a per-site blanket override is also plausible.
6. **Does LE31 ever ship a pack itself**, or only consume third-party ones? If LE31 ships them, the trust root question becomes internal rather than external.

## Why this matters

LE31's rules currently live in code, and the codebase already shows what that costs: feature 408 found a tax rate with no home, feature 411 found precision that is declared but not enforced. Those are *internal* correctness problems. This pick is about a different and larger one — **rules that must change without a deployment**, which is what a restaurant owner in a new tax jurisdiction actually needs.

The value of recording it now, while it is still a `defer`, is that the **precedence sentence** is cheap to get right on paper and expensive to get wrong in code. A rules channel with an ambiguous override order is worse than no rules channel: the operator believes their local rule is in force and it is not, and the discrepancy surfaces on a tax line, in front of a customer, at closing time.

Two things this contract deliberately refuses to do. It does not resolve the charter's tax question — that is the owner's call and the charter's §3.3 already tracks it. And it does not pretend the source's design is more specified than it is: the pack format, the signature scheme and the conflict order are all named as open questions rather than invented.

The honest summary is that LE31 does not need rule packs today, may never need them if the answer to §3.3 question 3 is "flat 10% forever", and will need them badly the moment a second country or a per-category rate is on the table. The vocabulary is cheap to hold and expensive to rediscover.
