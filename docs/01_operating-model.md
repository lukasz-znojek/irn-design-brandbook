# 01 — Operating Model

## Purpose
Explain *how work actually gets done* in the IRIN Brandbook Operating System: the division of labor between humans, GitHub/Copilot, and Claude Code, and the rhythm (cadence) of planning vs. execution.

## When to use
- Before starting any new phase of work (discovery, strategy, identity, production, QA).
- When unsure whether a task belongs in "planning" (this repo, GitHub/Copilot) or "execution" (Claude Code + feature branches).
- When onboarding a new subagent or human collaborator.

## Inputs
- `docs/00_project-charter.md` (mission and non-negotiables).
- `orchestration/master-orchestrator.md` (task-splitting protocol).

## Outputs
- A shared mental model: two execution environments, one source of truth.

## Owner
Brand System Owner + Master Orchestrator (shared).

## Quality criteria
- Any contributor can answer "where does X happen?" within 30 seconds of reading this file.
- No task is ambiguous between "planning" and "execution."

---

## The two environments

### 1. GitHub / Copilot Coding Agent (this repository, planning + system layer)
This is where the **system itself** lives: strategy documents, identity rules, templates, AI prompts, orchestration contracts, and governance. Copilot Coding Agent (this session and similar future ones) is responsible for:
- Scaffolding and maintaining the repository structure.
- Drafting and refining strategy/identity/template content.
- Keeping `docs/agent-live-dashboard.md` and `docs/roadmap.md` current.
- Opening PRs for review when structural or strategic changes are proposed.
- Recording decisions in `docs/02_decision-log.md`.

**Not responsible for:** producing final pixel-perfect production assets (hi-fi mockups, exported logo files, final font files) — that is Claude Code's job, executed locally with direct access to design tools/exports.

### 2. Claude Code (local execution layer)
This is where **production work** happens once the system layer approves direction: implementing chosen palette/typography into real components, building website/app UI, exporting production assets, running larger batch content generation against the AI prompts defined in `/ai/`.
- Operates on feature branches, opens PRs back against this repo (or a downstream implementation repo).
- Executes atomic tasks defined by the Master Orchestrator (`orchestration/master-orchestrator.md`) using the subagent contracts in `orchestration/handoff-contracts.md`.
- Subject to the same QA gates (`templates/design-qa-checklist.md`, `ai/evaluation-rubric.md`) before merge.

See `docs/roadmap.md` "Claude Code Handoff" section for the concrete step-by-step transition plan.

## Operating rhythm
1. **Brief in** — human states an intent (a phase, a deliverable, or a fix).
2. **Plan** — Master Orchestrator splits the brief into atomic subagent tasks (strict I/O contracts).
3. **Research** — any strategic claim gets a source note (`research/sources.md`) before it is used.
4. **Draft** — subagents produce structured outputs with confidence + open questions.
5. **Option presentation** — for major visual/strategic forks, 7 options (A–G) are presented per `identity/color-system.md`'s pattern.
6. **Human decision** — founder chooses/adjusts via the feedback block; decision logged in `docs/02_decision-log.md`.
7. **QA** — QA subagent validates against `ai/evaluation-rubric.md` and `templates/design-qa-checklist.md`.
8. **Merge** — PR merged; `docs/agent-live-dashboard.md` and `docs/roadmap.md` updated same-day.

## High-autonomy principle
Agents should **not** ask the human for anything that can be resolved by (a) reading this repo, (b) applying `docs/03_quality-bar.md`, or (c) making a reasonable, reversible, logged assumption. Human involvement is reserved for:
- Style/taste calls (which of 7 options wins).
- Final go/no-go before external publication.
- Anything that would violate a non-negotiable in `docs/00_project-charter.md` if decided wrong.

## Single-window orchestration
One master brief (a single message/issue) can be decomposed into parallel subagent tasks (research, visual, tone, QA) that execute concurrently and report back into a single dashboard — see `orchestration/master-orchestrator.md`.

## Common failure modes
- Confusing "committed to the repo" with "approved" — draft ≠ final.
- Claude Code producing final assets before the system layer (palette, positioning) has founder approval.
- Multiple agents editing `docs/agent-live-dashboard.md` simultaneously without reconciling — always treat it as the single source of truth and update it last in any batch of changes.

## How to avoid generic output
- Keep this operating model specific to the two real environments in use (GitHub/Copilot + Claude Code), not a generic "agile process" description.
