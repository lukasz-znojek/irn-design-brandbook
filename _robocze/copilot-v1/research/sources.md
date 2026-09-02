# Sources — Running Citation Ledger

## Purpose
An append-only ledger of every source used anywhere in this repository to back a strategic or visual claim. If a claim in `/strategy` or `/identity` doesn't have a corresponding entry here (or an explicit "working assumption, unconfirmed" flag), treat it as unverified.

## When to use
- Every time a research pass produces a citable source.
- Before approving any decision in `docs/02_decision-log.md` that claims to be "research-backed."

## Inputs
- URLs, documents, interview notes, analytics exports, prior brandbook drafts.

## Outputs
- A numbered, dated, greppable list other docs can link to (e.g. `research/sources.md#SRC-004`).

## Owner
Whoever runs the research pass (subagent or human) logs it; Master Orchestrator audits for staleness quarterly.

## Quality criteria
- Every entry: ID, date added, source type, source reference, one-line relevance note, which file(s) cite it.
- No dead links left uncorrected for more than one review cycle.

## Example (IRIN)
| ID | Date | Type | Source | Relevance | Cited by |
|---|---|---|---|---|---|
| SRC-001 | 2026-09-01 | Founding brief | This repository's founding problem statement (founder direction) | Establishes non-negotiables: preserve logo, preserve Manrope, research-first workflow, option-based collaboration | `docs/00_project-charter.md`, all `/strategy` and `/identity` files |
| SRC-002 | pending | Primary — prior draft brandbook | Founder's Claude-Design draft brandbook (to be added to repo) | Primary input for refinement; not yet available in this repo — see `docs/agent-live-dashboard.md` pending approvals | *(pending import)* |
| SRC-003 | pending | Primary — logo asset | Founder-provided logo file (to be added under `/identity/assets/logo/`) | Ground truth for `identity/logo-guidelines.md`; not yet available | *(pending import)* |
| SRC-004 | 2026-09-01 | Standard | WCAG 2.1 Success Criterion 1.4.3 (Contrast Minimum) and 1.4.11 (Non-text Contrast) | Basis for accessibility guidance in `identity/color-system.md` | `identity/color-system.md`, `templates/design-qa-checklist.md` |

## Template (blank reusable block)
```
| ID | Date | Type | Source | Relevance | Cited by |
|---|---|---|---|---|---|
| SRC-0XX |  |  |  |  |  |
```

## Common failure modes
- Adding a source without noting *which specific claim* it supports — makes future audits impossible.
- Letting SRC-002/SRC-003 (pending imports) sit unresolved indefinitely instead of escalating them as blockers in `docs/agent-live-dashboard.md`.

## How to avoid generic output
- Prefer primary sources (actual IRIN interviews, actual competitor sites) over generic secondary "industry trend" articles wherever possible.
