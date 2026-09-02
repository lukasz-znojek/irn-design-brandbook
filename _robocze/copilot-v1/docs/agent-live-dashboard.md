# Agent Live Dashboard — Single Source of Truth

> **Update this file at every major progress step.** It is the one place to look for current status. Last updated: 2026-09-01 (repository initialization).

## How to read this file
- **Current plan**: what's being worked on right now.
- **Roadmap status**: high-level phase tracker (detail in `docs/roadmap.md`).
- **Active decisions**: things awaiting or recently given a human decision.
- **Pending approvals**: blocked on @lukasz-znojek specifically.
- **Next actions**: the immediate next 1–3 things an agent or human should do.
- **Risks/blockers**: anything that could stall progress.
- **Dependencies**: what's waiting on what.

---

## Current plan
Initializing the IRIN Brandbook Operating System repository structure (v1): strategy, identity, applications, templates, AI prompts, orchestration protocol, workflows, and governance docs, per the founding brief. This is a **system scaffolding pass** — content is real and opinionated, not placeholder, but the underlying brand facts (category, real logo asset, real founder-drafted brandbook) still need confirmation/import.

## Roadmap status (see `docs/roadmap.md` for full detail)
| Phase | Status |
|---|---|
| 0. Repository scaffolding (this PR) | 🟢 In progress → near complete |
| 1. Discovery / research import | 🟡 Blocked — awaiting founder-provided draft brandbook + logo asset |
| 2. Strategy confirmation | 🟡 Blocked — depends on Phase 1 |
| 3. Identity system (color decision) | 🟡 Blocked — 7 options drafted, awaiting founder choice |
| 4. Production (Claude Code) | ⚪ Not started |
| 5. QA & approval | ⚪ Not started |

Legend: 🟢 in progress/on track · 🟡 blocked/needs input · 🔴 at risk · ⚪ not started · ✅ complete

## Active decisions
- **Color system**: 7 options presented in `identity/color-system.md` (Options A–G). Awaiting founder choice via the feedback block. See `docs/02_decision-log.md#DEC-005`.
- **Brand category assumption**: working assumption logged as provisional in `docs/02_decision-log.md#DEC-002` — IRIN modeled as a boutique design & technology studio. Needs explicit confirmation or correction.

## Pending approvals (blocked on @lukasz-znojek)
1. Confirm or correct the working brand-category assumption (`docs/02_decision-log.md#DEC-002`).
2. Choose a color option A–G from `identity/color-system.md` (fill in the feedback block).
3. Add the real logo asset (any format) and the founder-drafted brandbook (file or pasted text) to the repo — see `identity/logo-guidelines.md` placeholder path `/identity/assets/logo/` and `research/sources.md` for where to log it as a source.
4. Approve/adjust the draft positioning statement in `strategy/positioning.md`.
5. Final go/no-go on this PR merging as "v1 of the system" (structure + drafts), independent of the above open decisions, which continue in follow-up PRs.

## Next actions
1. Merge this PR to establish the system baseline (structure, templates, drafts).
2. Founder reviews and responds to the 5 pending approvals above (can be async, one at a time).
3. Once logo + draft brandbook are added, run a dedicated "Phase 1: Discovery" pass to populate `research/sources.md` with real citations and update `strategy/*` from assumption to confirmed.
4. Once color option is chosen, update `docs/02_decision-log.md#DEC-005` to Approved and propagate the token into `applications/*` and `templates/design-qa-checklist.md`.
5. Move to Claude Code for first production implementation task — see `docs/roadmap.md` → "Claude Code Handoff."

## Risks / blockers
- **No real logo/brandbook asset in repo yet** — all identity content is written against a working assumption and clearly flagged as such; risk of rework once real assets arrive is low (system is designed to absorb this: only the *facts*, not the *structure*, change).
- **Attachment access**: files pasted into a local Claude/Copilot session on the founder's machine are not automatically visible to this cloud agent — they must be explicitly added to the git repository (commit, or paste text/hex values directly into an issue/PR comment) for the system to ingest them.
- **Trademark/legal clearance** for any naming decisions is explicitly out of scope here (see `strategy/naming-principles.md`) and must be tracked separately.

## Dependencies
- `identity/color-system.md` decision → blocks `applications/*` final palette application and `templates/design-qa-checklist.md` accessibility checks going from "generic AA guidance" to "verified against chosen palette."
- Real logo asset → blocks `identity/logo-guidelines.md` from referencing actual file exports and `applications/print-guidelines.md` proofing checklist.
- Founder-drafted brandbook import → blocks `research/sources.md` from citing it and `strategy/*` moving from "assumption" to "confirmed."

---
*Maintained by: Master Orchestrator, on behalf of Brand System Owner @lukasz-znojek. Update this file in the same PR/commit as any change that shifts phase status, adds a decision, or resolves/creates a blocker.*
