# 02 — Decision Log

## Purpose
A single append-only ledger of every strategic or visual decision made for the IRIN brand, with rationale, alternatives considered, and approver. This is the audit trail that keeps the system research-first and prevents silent re-litigation of settled choices.

## When to use
- Immediately after any human approval (palette choice, positioning statement, naming decision, tone direction).
- When an agent makes a reversible assumption in the absence of a human decision (log it as "provisional" so it's visible and revisitable).
- Before proposing a change that contradicts a prior decision — check here first.

## Inputs
- Options presented (e.g. the 7-option color palette comparison in `identity/color-system.md`).
- Human feedback block (`Choose / Keep / Change / Confidence`).
- Research backing (`research/sources.md`).

## Outputs
- A chronological, greppable record other docs can cite (e.g. "see `docs/02_decision-log.md#DEC-003`").

## Owner
Brand System Owner logs final decisions; Master Orchestrator logs provisional/assumed decisions on the human's behalf, clearly marked.

## Quality criteria
- Every entry has: ID, date, decision, status, options considered, rationale, approver, links.
- No entry is edited after the fact — corrections are new entries that supersede old ones (`Superseded by DEC-00X`).

## Example (IRIN)

| ID | Date | Area | Decision | Status | Options considered | Rationale | Approver |
|---|---|---|---|---|---|---|---|
| DEC-001 | 2026-09-01 | Repository scope | Adopt the Brandbook Operating System structure exactly as specified in the founding brief | Approved | N/A (founding brief) | Establishes one system of record across strategy/identity/AI/orchestration | @lukasz-znojek |
| DEC-002 | 2026-09-01 | Brand category (provisional) | Assume IRIN = boutique design & technology studio, precision-positioned vs. big consultancies | Provisional — pending confirmation | N/A, working assumption flagged in `strategy/brand-core.md` | Needed a concrete anchor to avoid generic strategy writing; must be validated in `research/market-category-analysis-template.md` | Master Orchestrator (assumption, human to confirm) |
| DEC-003 | 2026-09-01 | Typeface | Preserve Manrope as sole primary typeface; define scale/weight rules only | Approved (non-negotiable, restated) | N/A — founder directive | Explicit constraint in founding brief | @lukasz-znojek |
| DEC-004 | 2026-09-01 | Logo | Preserve existing logo exactly; no geometry/symbol edits | Approved (non-negotiable, restated) | N/A — founder directive | Explicit constraint in founding brief | @lukasz-znojek |
| DEC-005 | pending | Color system | Choose 1 of 7 options in `identity/color-system.md` | **Open — awaiting founder decision** | Options A–G, see `identity/color-system.md` | — | — |

## Template (blank reusable block)
```
| ID | Date | Area | Decision | Status | Options considered | Rationale | Approver |
|---|---|---|---|---|---|---|---|
| DEC-0XX |  |  |  | Proposed / Provisional / Approved / Rejected / Superseded |  |  |  |
```

## Common failure modes
- Decisions made verbally/in chat but never logged — they get "lost" and re-debated later.
- Logging a decision without the alternatives considered, making it impossible to audit later.
- Editing history instead of superseding it.

## How to avoid generic output
- Require a rationale tied to a specific IRIN fact or research note — reject "because it looks good" as a rationale.
