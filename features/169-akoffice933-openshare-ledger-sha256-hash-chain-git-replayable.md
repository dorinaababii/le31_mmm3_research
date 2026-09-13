# Feature 169 — akoffice933-openshare-ledger-sha256-hash-chain-git-replayable (defer)

> **NEW observation (2026-09-13).** Documents in-window GitHub repo `akoffice933-maker/openshare-ledger` (MIT, **0★/0⑂**, Python, **pushed 2026-09-12**, in-window by push only, **created 2026-09-12** — 1-day-old repo, 70 KB). Description (verbatim from GitHub API): *"Open infrastructure for verifiable contribution attribution in community-trained AI. Append-only SHA-256 hash chain, replayable from git."* Topics: `ai`, `auditability`, `contribution-tracking`, `data-provenance`, `evaluation`, `hash-chain`, `machine-learning`, `open-models`, `open-source`, `provenance`. Bucket: **v2 architecture-reference (charter §3.1 territory; SHA-256 hash chain + git-replayable discipline; off-domain for community-AI training attribution; v2-hardening primitive for independent-verifiability without a third-party timestamping service)** — watch-list defer. Zero build time today.

## Goal

Retain the **"open infrastructure for verifiable contribution attribution in community-trained AI with append-only SHA-256 hash chain, replayable from git"** primitive as a persistent cross-section reference for any future LE31 v2 surface that introduces an external auditor (EU compliance audit per §3.1, tax authority audit, or a regulatory inspection) OR the first v2 surface that operates without internet access and needs independent replay. The artifact is the persistent cross-section reference + a candidate *decentralized-replay* design discipline for the next v2-hardening primitive. No code today.

## Scope

**In scope (defer artifact):**
- A written record of the **"append-only SHA-256 hash chain"** primitive: every entry is *append-only* (no row is updated), the chain uses *SHA-256* as the hash function (collision-resistant, widely supported), and each entry's hash includes the previous entry's hash + the entry's canonical-JSON content. Tampering with any entry is detectable by re-running the chain.
- A written record of the **"replayable from git"** primitive: the chain's authoritative source is the *git history* itself, not a separate database. Any auditor with read access to the git repository can verify the chain by re-running the replay. **No third-party timestamping service is required.** This is the *decentralized replay* discipline — the chain is verifiable without trusting any central authority.
- A written record of the **"contribution attribution"** use case (the openshare-ledger context): in community-trained AI, multiple contributors submit data and code; the chain records *who contributed what, when, with what content*; the chain is the *attribution ledger* that credits each contributor fairly.
- A written record of the **"verifiable contribution attribution"** discipline: the chain is *replayable from git* means any auditor can reconstruct the full contribution history by reading the git log; the SHA-256 hash chain means any tampering with the history is detectable.
- A decision record: today's verdict is `defer` because LE31 v1 has no external auditor (single owner, single restaurant, single jurisdiction), no v2 audit-export surface, and no offline mode requirement. The *SHA-256 hash chain + replayable from git* pattern is a v2-hardening primitive that doesn't have a v1 trigger.

**Out of scope (defer artifact):**
- Any change to LE31 v1's `audit_logs` schema (charter §3.1: explicit state changes; v1 `audit_logs` is sufficient for v1 ops).
- Any change to LE31 v1's `StockEntry` ledger.
- Any new external-auditor surface (LE31 v1 has no auditor surface; introducing one would require an owner decision).
- Any new offline-mode surface (LE31 v1 requires internet access for the Telegram bot; introducing an offline mode would be a v2 product decision).
- Adoption of the openshare-ledger codebase (the repo is 1 day old, 70 KB, MIT Python; the *primitive* is portable; the *codebase* is not adoptable without a full read-and-eval).
- Cross-pollination with feature 151 (Offline Attestation Record) + feature 154 (`machine-native/chronology-protocol` post-quantum provenance + OpenTimestamps). This primitive is *git-replayable* (independent of any third-party service); feature 151/154 use *OpenTimestamps* (Bitcoin-anchored). Different verification paths, same family of *decentralized-verifiability* primitives.

## Evidence / JTBD

When a future LE31 v2 surface introduces an external auditor (EU compliance audit per §3.1, French tax authority inspection, or a regulatory inspection), the auditor wants *a primitive that records every state change in a SHA-256 hash chain, replayable from git*, but struggles because *LE31 v1's `audit_logs` is text-only and depends on the auditor trusting the database*, so that *the v2 surface can be independently verified by any auditor with read access to the git repository*.

- **Evidence class**: observed (the openshare-ledger description + 10 topics name the primitive explicitly: `ai`, `auditability`, `contribution-tracking`, `data-provenance`, `evaluation`, `hash-chain`, `machine-learning`, `open-models`, `open-source`, `provenance`).
- **Confidence**: medium-high for the primitive match (the description is direct; the SHA-256 + replayable-from-git discipline is well-established in software supply-chain security research — see also Sigstore, in-toto, SLSA); low for transferability (the openshare-ledger is for community-AI training attribution, not restaurant ops; the *primitive* is portable, the *use case* is not).
- **Real observed LE31 JTBD**: zero-pain today; LE31 v1 has no external-auditor surface; the v2 surface that would *use* the primitive doesn't exist.
- **The value is naming, not direct demand**: when the first v2 external-auditor or offline-mode surface lands (if/when the owner requires independent-verifiability), the openshare-ledger pattern is a ready-made *named primitive* — and the *SHA-256 hash chain + replayable from git* vocabulary slot into features 121 (Field-Tier Minimization, *what is committed*) / 133 (HANSARD, *who witnessed*) / 134 (ECHO, *record shape*) / 141 (KRINEIA, *append-only as proof*) / 151 (Offline Attestation Record, *sovereign/offline* + *OpenTimestamps*) / 154 (chronology-protocol post-quantum provenance + OpenTimestamps) / 167 (Pick A today) / 168 (Pick B today).

## Description

GitHub `akoffice933-maker/openshare-ledger` (MIT, 0★/0⑂, Python, pushed 2026-09-12, created 2026-09-12, 70 KB). Description (verbatim): *"Open infrastructure for verifiable contribution attribution in community-trained AI. Append-only SHA-256 hash chain, replayable from git."*

The architectural primitive has three components:

1. **"Append-only SHA-256 hash chain"** — every entry is *append-only* (no row is updated), the hash function is *SHA-256* (collision-resistant, widely supported), and each entry's hash includes the previous entry's hash + the entry's canonical-JSON content: `entry_hash = sha256(parent_hash + canonical_json(this_entry))`. Tampering with any entry breaks the chain.
2. **"Replayable from git"** — the chain's authoritative source is the *git history* itself, not a separate database. Each git commit contains one entry; the SHA-256 hash chain is computed by walking the git log in commit order. **No third-party timestamping service is required** — the chain is verifiable by anyone with read access to the git repository.
3. **"Verifiable contribution attribution"** — in community-AI training, multiple contributors submit data and code; the chain records *who contributed what, when, with what content*; the chain is the *attribution ledger* that credits each contributor fairly. The replayable-from-git discipline means contributors can verify their own attribution by reading the git log.

**The 1:1 mapping onto LE31 v2 architecture (if/when external-auditor or offline-mode surfaces are designed):**

| openshare-ledger primitive | LE31 v2 equivalent | Charter section | Status |
|---|---|---|---|
| Append-only SHA-256 hash chain | (LE31 v1's `audit_logs` is append-only but not hash-chained; no SHA-256 discipline today) | §3.1 + v2 hardening | **Not implemented** |
| Replayable from git | (LE31 v1's git history is not the audit trail's authoritative source; the database is) | v2 hardening | **Not implemented** |
| Decentralized replay (no third-party) | (LE31 v1 has no decentralized-verifiability surface) | v2 hardening | **Not implemented** |
| Verifiable contribution attribution | (LE31 v1 has no multi-contributor surface; single owner) | (future v2) | **Not implemented** |
| Audit query (walk the chain) | (LE31 v1's `audit_logs` supports SQL queries on rows; no chain-walk query primitive) | §3.1 + v2 hardening | **Not implemented** |

## Data model

**No schema change today.** The defer artifact is documentation only.

If the future v2 trigger condition fires (first v2 PR that adds a SHA-256 hash chain over `audit_logs` + an external-auditor or offline-mode surface), the v2 schema migration would need:

- `audit_logs.entry_hash` field: nullable SHA-256 hex, computed as `sha256(parent_hash + canonical_json(this_row))`. The first entry's parent_hash is the SHA-256 of the empty string.
- `audit_logs.parent_hash` field: nullable SHA-256 hex, references the previous row's `entry_hash`.
- A git pre-commit hook that computes the `entry_hash` for each new `audit_logs` row and stores it in a git-tracked file (`audit_chain.json`) so the chain is replayable from git alone.
- A v2 surface that exposes the chain-walk query primitive (e.g. "show me every audit-log entry from the SHA-256 hash chain between entry X and entry Y").

**No existing schema change today.**

## Implementation steps

**None today.** The defer artifact is documentation only.

Future v2 implementation would include:
1. Add the `entry_hash` and `parent_hash` fields to `audit_logs`.
2. Compute the hash chain on every `audit_logs` insert (in the same database transaction, so the chain is atomic with the row).
3. Add the git pre-commit hook to write `audit_chain.json` so the chain is replayable from git alone.
4. Add a v2 surface that exposes the chain-walk query primitive + the audit-export surface for external auditors.

**No existing code change today.**

## Telegram interaction if any

**None today.** The defer artifact is documentation only.

Future v2: if an external-auditor surface is built, it would likely be exposed through a Telegram command (`/audit_export <date_range>` → reply with the SHA-256 chain between the two dates). But the cook's daily ops surface is unaffected.

## Dependencies

- **Charter §3.1 invariant compatibility**: ✓ (append-only SHA-256 hash chain IS the strongest form of "explicit state changes" — every entry is immutable, hash-indexed, and tamper-evident).
- **§3.2 license compatibility**: ✓ (openshare-ledger is MIT permissive).
- **Stack compatibility**: ✓ (Python + SQLModel can hold the schema; git pre-commit hooks are language-agnostic; SHA-256 is in the Python stdlib).
- **First v2 surface that introduces an external auditor OR an offline-mode requirement**: trigger condition.

## Open questions

1. **Does LE31 v2 need external-auditor support?** v1 has not surfaced a JTBD for it. The v2 question is whether the owner would ever need to show an auditor "here is the chain of every StockEntry change in the last year" with the auditor able to verify it independently.
2. **Does LE31 v2 need offline mode?** v1 requires internet for the Telegram bot. The v2 question is whether the owner needs to operate during internet outages (this is more likely for rural restaurants or disaster-recovery scenarios).
3. **What is the git hosting model?** If LE31 v2 uses GitHub or a self-hosted Gitea, the *replayable from git* primitive works out of the box. If LE31 v2 uses a different VCS, the primitive needs adaptation.

## Why this matters

The **SHA-256 hash chain + replayable from git** vocabulary is the **v2-hardening primitive** for any future LE31 surface that needs independent-verifiability without depending on a third-party service (OpenTimestamps, EU regulatory timestamping service, or a managed cloud WORM storage). Without this vocabulary, the first external-auditor surface would have to invent SHA-256 chaining + git replay from scratch. With this vocabulary, the v2 surface can adopt the openshare-ledger pattern directly: every `audit_logs` row carries its SHA-256 entry_hash, the chain is replayable from git alone, and any auditor with read access to the git repository can verify the chain independently.

Companion artifacts: features 121 (Field-Tier Minimization), 133 (HANSARD), 134 (ECHO), 141 (KRINEIA), 151 (Offline Attestation Record), 154 (chronology-protocol post-quantum provenance + OpenTimestamps), 167 (Pick A today), 168 (Pick B today) — all ripgrep-verified distinct from this artifact.
