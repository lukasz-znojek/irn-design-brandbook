# Roadmap — IRIN Brandbook Operating System

> Companion to `docs/agent-live-dashboard.md`. That file is the at-a-glance status; this file is the phase-by-phase execution plan. Update both together.

## Purpose
Give a linear, phased plan from "empty repo" to "brand system fully in production use," with explicit entry/exit criteria per phase so anyone can tell what phase we're in and what unblocks the next one.

## When to use
- Planning the next unit of work.
- Explaining to a new stakeholder what's done vs. pending.
- Deciding whether a task belongs to GitHub/Copilot (system layer) or Claude Code (execution layer) — see `docs/01_operating-model.md`.

## Inputs
- `docs/00_project-charter.md`, `docs/agent-live-dashboard.md`.

## Outputs
- Phase gates with clear entry/exit criteria; a standing "Claude Code Handoff" section.

## Owner
Master Orchestrator, ratified by Brand System Owner.

## Quality criteria
- Each phase has explicit exit criteria (not vibes).
- Status always matches `docs/agent-live-dashboard.md`.

---

## Phase 0 — Repository scaffolding *(current)*
**Goal**: every directory/file in the founding brief exists with real, opinionated starter content.
**Exit criteria**: PR "Initialize IRIN Brandbook Operating System v1" merged; dashboard + roadmap live.
**Status**: 🟢 in progress → near complete.

## Phase 1 — Discovery / research import
**Goal**: replace working assumptions with confirmed facts; import the founder's draft brandbook and logo asset as primary source material.
**Entry criteria**: Phase 0 merged.
**Work**:
- Add real logo file(s) under `/identity/assets/logo/` (binary assets — tracked via Git LFS if large, see `.gitignore`).
- Paste/attach founder's Claude-Design draft brandbook content; log it in `research/sources.md` as the primary source.
- Run `research/market-category-analysis-template.md` and `research/competitor-analysis-template.md` for real (not illustrative) findings.
**Exit criteria**: `docs/02_decision-log.md#DEC-002` flips from Provisional to Approved (or is corrected); `research/sources.md` has ≥5 real sources.
**Status**: 🟡 blocked — awaiting founder input (see dashboard "Pending approvals").

## Phase 2 — Strategy confirmation
**Goal**: `strategy/*` moves from "well-reasoned draft" to "confirmed brand strategy."
**Entry criteria**: Phase 1 exit criteria met.
**Work**: Founder reviews `strategy/brand-core.md` and `strategy/positioning.md`; Brand Strategy subagent (`orchestration/subagent-brand-strategy.md`) revises based on feedback.
**Exit criteria**: Positioning statement and brand core approved and logged in decision log.
**Status**: 🟡 blocked — depends on Phase 1.

## Phase 3 — Identity system (color decision + full system lock)
**Goal**: Founder selects one of the 7 color options in `identity/color-system.md`; typography/spacing/imagery/icon/motion systems finalized around it.
**Entry criteria**: Phase 2 exit criteria met (strategy informs which option best fits positioning).
**Work**: Founder fills the feedback block in `identity/color-system.md`; Visual Identity subagent (`orchestration/subagent-visual-identity.md`) propagates the chosen tokens into `applications/*`.
**Exit criteria**: `docs/02_decision-log.md#DEC-005` = Approved; all `applications/*` files reference the confirmed palette (no more "pending option" language).
**Status**: 🟡 blocked — options drafted, awaiting founder choice (can happen in parallel with Phase 1/2 if founder wants to move fast — it only requires this PR to be merged).

## Phase 4 — Production (Claude Code execution)
**Goal**: turn the approved system into real production assets — website components, deck templates, exported logo files, social templates.
**Entry criteria**: Phases 2–3 complete.
**Work**: See "Claude Code Handoff" below.
**Exit criteria**: First production surface (recommend: website hero + core components) implemented and passes `templates/design-qa-checklist.md`.
**Status**: ⚪ not started.

## Phase 5 — QA & approval / ongoing operations
**Goal**: steady-state brand operations — every new asset flows through `workflows/05_qa-and-approval.yaml`.
**Status**: ⚪ not started.

---

## Claude Code Handoff

### When and why to move to Claude Code
Move to Claude Code once Phase 2 (strategy) and Phase 3 (color decision) are both **Approved** in `docs/02_decision-log.md`. Claude Code is for **execution** — writing/generating real components, exported assets, and larger-scale content batches against approved specs — not for re-deciding strategy or identity direction (that stays here, in this repo, per `docs/01_operating-model.md`).

### What to run in Claude Code next (step-by-step)
1. Clone this repository locally (or open the existing local clone).
2. Point Claude Code at `orchestration/master-orchestrator.md` as its operating instructions and `orchestration/handoff-contracts.md` for I/O format.
3. Give Claude Code a single master brief, e.g.: *"Using the approved strategy in `/strategy` and the approved palette (Option __ ) in `/identity/color-system.md`, implement the website hero + core components described in `applications/website-guidelines.md`."*
4. Claude Code (via the Master Orchestrator prompt) splits this into subagent tasks: Visual Identity subagent implements tokens/components; Content/Tone subagent drafts copy against `strategy/tone-of-voice.md`; QA subagent validates against `templates/design-qa-checklist.md` before opening a PR.
5. Claude Code opens a feature branch + PR for the *implementation* repo/surface (this brandbook repo remains the system-of-record; implementation may live in a downstream product/marketing repo).
6. Founder reviews the PR, approves or requests changes; approved state is mirrored back into `docs/02_decision-log.md` here.

### Recommended Claude Code settings
**Model**
- **Recommended default**: a high-capability reasoning model (e.g. the current top-tier "Sonnet"/"Opus"-class model available to you) for anything touching strategy interpretation, copywriting, or first-pass component architecture — this work is judgment-heavy and benefits from stronger reasoning.
- **Alternative — faster/cheaper model**: for high-volume, low-ambiguity tasks (e.g. batch-generating 20 social template variants from an already-approved template, or re-running the QA checklist across many files), use a faster/lighter model to save time and cost.
- **When to switch**: switch to the high-capability model whenever a task requires interpreting `strategy/*` or making a judgment call that isn't fully specified by an approved template.

**Effort level**
- **Low**: mechanical tasks with a fully-specified template (e.g. filling in `templates/design-qa-checklist.md` for a single asset, generating one social post from an approved template).
- **Medium**: most production tasks — implementing an approved component from `identity/*` + `applications/*` specs, writing on-brand copy for a defined channel.
- **High**: first-pass architecture decisions, ambiguous or cross-cutting tasks (e.g. "design the full website information architecture"), or anything where a mistake is expensive to unwind (public-facing launch assets).

### Tracking guidance (minimal manual effort)
- Keep watching **`docs/agent-live-dashboard.md`** in this repo — Claude Code sessions should be instructed (via `orchestration/master-orchestrator.md`) to update it at the end of every work session, mirroring status back here even though execution happens elsewhere.
- In Claude Desktop/Code, request that every session end with a short structured status update matching the dashboard's fields (current plan / next actions / blockers) — paste that back into `docs/agent-live-dashboard.md` here, or let an orchestrator agent do it automatically if wired up.
- You only need to actively *decide* at the "Pending approvals" checkpoints listed in the dashboard — everything else is designed to proceed on reasonable, logged, reversible assumptions.

## First 7 tasks recommended for immediate execution
1. Confirm or correct the brand-category working assumption (`docs/02_decision-log.md#DEC-002`).
2. Choose a color palette option A–G in `identity/color-system.md`.
3. Add the real logo asset + founder-drafted brandbook content to the repo (`identity/assets/logo/`, `research/sources.md`).
4. Approve or revise the draft positioning statement (`strategy/positioning.md`).
5. Run `research/competitor-analysis-template.md` against 3–5 real named competitors.
6. Approve the tone-of-voice word bank (`strategy/tone-of-voice.md`) or flag adjustments.
7. Kick off Phase 4 in Claude Code with the website hero as the first production surface (`applications/website-guidelines.md`).

## Common failure modes
- Letting this roadmap drift out of sync with `docs/agent-live-dashboard.md` (they must always agree on phase status).
- Starting Phase 4 (Claude Code production) before Phase 2/3 decisions are actually logged as Approved, not just "discussed."

## How to avoid generic output
- Every phase gate here is tied to a specific file/decision-log entry, not a vague milestone name — keep it that way when this roadmap is updated.
