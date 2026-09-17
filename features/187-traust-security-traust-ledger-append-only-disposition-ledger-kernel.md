# Feature 187 — `traust-security-traust-ledger-append-only-disposition-ledger-kernel` (defer)

> **NEW observation on 2026-09-17.** Documents in-window GitHub repo `traust-security/traust-ledger` (**Apache-2.0 ✓**, **1★/4⑂** — the 4 forks on 1★ is an unusual fork/derivative activity signal, Python, **pushed 2026-09-16T20:32:20Z**, in-window by push only, **747 KB** substantial kernel, owned by `traust-security` GitHub org). Description (verbatim from GitHub API): *"Append-only disposition ledger kernel for security auditing workflows."* The **closest reusable v2-hardening primitive** of any 2026-09-17 in-window repo: the security-audit domain is OFF-LE31 but the **append-only-ledger-kernel pattern** is the reusable bit — same architectural dual as feature 167 provtrail + feature 181 Merkle Audit. Bucket: **v2 architecture-reference (defer, parking-lot)**. Zero build time today.

## Goal

Document `traust-ledger` as a v2 architecture-reference observation: an Apache-2.0 append-only ledger kernel that a future LE31 v2 operator could fork and adapt to LE31's `StockEntry` + `audit_logs` schema. The artifact is vocabulary + a future-forkable-kernel note; NO code adoption today.

## Scope

**In scope (defer artifact):**

- A written record of the **append-only disposition ledger kernel** pattern (carry-over from feature 167 provtrail + feature 181 Merkle Audit).
- A written record of the **Apache-2.0 permissive license** (charter-compatible per §3.2).
- A written record of the **1★/4⑂ fork/derivative activity signal** (4 forks on 1★ is unusual and indicates active fork-based adoption by others).
- A written record of the **two next-step questions** for the coding agent (AGPL/SSPL dependency ripgrep + kernel interface inspection).
- A decision record: today's verdict is `defer` because both next-step questions need resolution before any v2 reference usage.
- A cross-section reference with the v2-hardening cluster: features 121, 122, 133, 134, 135, 141, 148, 167, 168, 169, 181, 182.

**Out of scope (defer artifact):**

- Any change to LE31 v1's `audit_logs` or `StockEntry` schema.
- Adoption of the `traust-ledger` codebase today (next-step questions unresolved).
- Any v1 build implication.

## Evidence / JTBD

When a future LE31 v2 surface introduces an external-audit-trail primitive (e.g., for tax filing), the owner wants *a kernel pattern that exposes a tamper-evident append-only ledger interface without depending on the writer's runtime*, but struggles because *LE31 v1's audit_logs is a single-table PostgreSQL design with no tamper-evident primitive*, so that *the v2 surface can answer provenance questions with a defensible answer*.

- **Evidence class**: observed (the `traust-ledger` description directly names the append-only disposition ledger kernel pattern).
- **Confidence**: high for the primitive match (the description is direct; the pattern is well-established in security-audit research).
- **Real observed LE31 JTBD**: zero-pain today; LE31 v1 doesn't need an external-audit-trail primitive; the v2 surface that would *use* the kernel doesn't exist.
- **The value is naming, not direct demand**: when the first v2 surface introduces an external-audit-trail primitive, the `traust-ledger` pattern is a documented kernel that can be forked.

## Description

GitHub `traust-security/traust-ledger` (Apache-2.0, 1★/4⑂, Python, pushed 2026-09-16T20:32:20Z, created date TBD, 747 KB substantial kernel, owned by `traust-security` GitHub org).

Description (verbatim): *"Append-only disposition ledger kernel for security auditing workflows."*

The architectural primitive has three clauses:

1. **"Append-only disposition ledger"** — the core pattern: events are committed to the ledger but never updated or deleted (charter §3.1 LE31 invariant).
2. **"Kernel"** — the implementation is a *library* (not a standalone service), so a LE31 v2 surface could compose it into `StockEntry` + `audit_logs` operations via Python import (rather than IPC).
3. **"For security auditing workflows"** — the domain is OFF-LE31 (security auditing vs restaurant operations) but the *kernel pattern* is the reusable bit.

**The 1:1 mapping onto LE31 v1 architecture (today):**

| traust-ledger primitive | LE31 v1 today | Charter section | Status |
|---|---|---|---|
| Append-only ledger | `audit_logs` is append-only | §3.1 ✓ | **Implemented (v1)** |
| Kernel (library, not service) | SQLModel models + FastAPI route handlers | §3.1 ✓ | **Implemented (v1, via SQLModel)** |
| Security auditing domain | (LE31 is restaurant operations, not security auditing) | (scope mismatch) | **OFF-DOMAIN for LE31 v1** |
| Apache-2.0 license | (LE31 may use Apache-2.0 dependencies) | §3.2 ✓ | **Charter-compatible** |

**The 1★/4⑂ fork/derivative activity signal** is worth noting: 4 forks on 1 star is an unusual fork-to-star ratio (typically you see fork count ≤ star count, or close to it; here fork count is 4× star count). This indicates that other developers are *forking* the kernel for their own use rather than *starring* it for bookmarking — exactly the adoption pattern you'd want for a reusable kernel primitive.

## Data model

**No schema change today.** The defer artifact is documentation only.

If the future v2 trigger condition fires (first v2 surface that needs an external-audit-trail primitive), the v2 schema migration would need:

- An optional `tamper_evidence` field on `audit_logs` (a hash chain that ties each row to the previous row, per the `traust-ledger` pattern).
- A kernel-composition layer that wraps `audit_logs` operations in `traust-ledger`-style kernel calls.

**No existing schema change today.**

## Implementation steps

**None today.** The defer artifact is documentation only.

Future v2 implementation would include (pending the two next-step questions being answered):

1. **AGPL/SSPL dependency ripgrep**: ripgrep the `traust-ledger` codebase for any AGPL-3.0 or SSPL dependency that would contaminate the permissive Apache-2.0 license (unlikely given 747 KB kernel size but verify).
2. **Kernel interface inspection**: determine whether the kernel exposes a Python class that LE31 could compose into `StockEntry` + `audit_logs` operations, or whether it's a standalone service (which would require IPC).

The answer to these two questions is the gate to any future v2 reference usage of `traust-ledger`.

**No existing code change today.**

## Telegram interaction

**None today.** The defer artifact is documentation only.

Future v2: the cook Telegram bot would not change; the v2 surface that would *use* the `traust-ledger` reference is hypothetical and not LE31-specific.

## Dependencies

1. Read access to the `traust-ledger` GitHub repository (`traust-security/traust-ledger`).
2. AGPL/SSPL dependency ripgrep of the `traust-ledger` codebase.
3. Kernel-interface inspection (Python class vs standalone service).
4. Owner decision on whether the future v2 trigger (introduction of external-audit-trail primitive) should preempt the v2 surface scope.

## Open questions

1. **AGPL/SSPL dependency contamination**: are there any AGPL-3.0 or SSPL dependencies in `traust-ledger`? Ripgrep the codebase to verify. **Required for any future v2 reference usage.**
2. **Kernel interface shape**: does `traust-ledger` expose a Python class that LE31 could compose into `StockEntry` + `audit_logs` operations (preferred — in-process integration), or is it a standalone service that would require IPC (more complex — network/Unix-socket integration)? Inspect the kernel interface to determine. **Required for any future v2 reference usage.**
3. **What does "disposition" mean in the kernel description?** The word "disposition" suggests event-outcome tracking (e.g., "this event was disposition: approved / denied / pending"). LE31's `audit_logs` doesn't have a notion of disposition today. Should the v2 schema add an optional `disposition` field? **Vocabulary-only question; defer until v2 trigger.**

## Why this matters

`traust-ledger` is the **closest reusable v2-hardening primitive** of any 2026-09-17 in-window repo: Apache-2.0 permissive license + append-only ledger kernel + 1★/4⑂ fork/derivative activity signal + 747 KB substantial implementation + Python (LE31's chosen language). The security-audit domain is OFF-LE31 but the kernel pattern is the reusable bit — same architectural dual as feature 167 provtrail + feature 181 Merkle Audit (both already filed as v2 architecture-reference observations). Documenting `traust-ledger` as a third append-only-ledger-kernel option gives future LE31 v2 surfaces a richer choice when the first external-audit-trail primitive is needed.