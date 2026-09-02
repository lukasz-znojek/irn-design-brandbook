# 00 — Project Charter: IRIN Brandbook Operating System

## Purpose
Define why this repository exists, what it is accountable for, and the boundaries of its authority. This charter is the constitutional document — every other file in this repo operates inside the boundaries set here.

## When to use
- Onboarding a new contributor, agent, or subagent.
- Resolving a scope dispute ("is this in scope for the brandbook repo?").
- Kicking off a new phase of work (re-read charter before `docs/roadmap.md` planning).

## Inputs
- Founder/stakeholder intent (this problem statement and any follow-up direction from **@lukasz-znojek**).
- Prior draft brandbook material produced in Claude Design (external, to be added under `/identity/assets/` and referenced from `research/sources.md` once available).

## Outputs
- A shared understanding of mission, non-negotiables, and success criteria that all subsequent docs, templates, and agents inherit.

## Owner
Brand System Owner (human) — currently **@lukasz-znojek**. Delegates execution to Master Orchestrator (`orchestration/master-orchestrator.md`) but retains final approval authority per `governance/approval-flow.md`.

## Quality criteria
- No ambiguity about what "done" means for the brandbook.
- Non-negotiables are stated explicitly and cannot be silently violated by any agent.
- Charter is short enough to be read in under 5 minutes.

---

## Mission
Build IRIN's **Brandbook Operating System**: a production system, reusable template library, and AI-ready foundation that lets IRIN create, apply, and evolve a premium, non-generic brand identity with minimal manual overhead and maximum creative rigor.

This repository is not a one-off design deliverable. It is infrastructure — the same way a build system is infrastructure for code, this is the build system for brand.

## What "world-class, non-generic" means here (operational definition)
A brand artifact produced by this system is **non-generic** only if it passes all four:
1. **Specific to IRIN** — it could not be relabeled with a competitor's name without becoming false or awkward.
2. **Evidence-backed** — a strategic claim traces to a note in `research/sources.md` or a decision in `docs/02_decision-log.md`.
3. **Opinionated** — it picks a side (a palette, a voice, a layout) rather than hedging with "flexible" options presented as if all were equally valid.
4. **Testable** — it can be scored against `docs/03_quality-bar.md` and `docs/04_risks-and-anti-generic-checklist.md`.

## Non-negotiables (hard constraints — no agent may override these without explicit human approval logged in `docs/02_decision-log.md`)
1. **Logo preservation** — the existing IRIN logo (wordmark/symbol) must be preserved exactly as provided. No redesign, no geometry changes, no symbol edits, no re-typesetting. See `identity/logo-guidelines.md`.
2. **Typeface preservation** — Manrope remains the primary brand typeface. Scale, weight usage, and hierarchy may be optimized; the typeface itself may not be replaced. See `identity/typography-system.md`.
3. **Human approval on major visual/strategic decisions** — color system, positioning statement, and any customer-facing asset requires founder sign-off per `governance/approval-flow.md` before it is considered final (not just "committed").
4. **Research-first** — no strategic recommendation ships without a linked source note in `research/sources.md` and a rationale.
5. **Option-based collaboration for major visual decisions** — present 7 labeled options (A–G) in the standard comparison format before converging (see `identity/color-system.md` for the reference implementation of this pattern).

## In scope
- Brand strategy documents, visual identity system documents, application guidelines, reusable templates, AI prompts/system prompts, orchestration protocols, workflow definitions, governance process.
- Refinement and elevation of the founder-provided draft brandbook (once added to the repo) to production-grade quality.

## Out of scope (for this repository, in its current phase)
- Producing final production-ready binary design assets (logo files, font files, high-fidelity mockups) — this repo defines the *system and rules*; final asset production happens in a design tool or Claude Code execution pass (see `docs/01_operating-model.md`).
- Legal trademark clearance (flagged as an open question wherever naming is discussed, not resolved here).
- Redesigning the logo mark itself, under any circumstance.

## Success criteria for v1 of this repository
- [ ] Full directory structure from the brief exists and every file has real, non-placeholder content.
- [ ] `docs/agent-live-dashboard.md` and `docs/roadmap.md` reflect true current status.
- [ ] `identity/color-system.md` presents 7 fully-specified, distinct palette options in the required format.
- [ ] Every template file includes Purpose/When to use/Inputs/Outputs/Owner/Quality criteria/Example/Template/Failure modes/Anti-generic guidance.
- [ ] A PR is opened titled "Initialize IRIN Brandbook Operating System v1" with architecture summary and first 7 recommended tasks.

## Common failure modes
- Treating this charter as decorative rather than binding — agents cite "flexibility" to justify violating a non-negotiable.
- Scope creep into producing final pixel-perfect assets before the strategic layer is approved.
- Silent divergence: a later doc contradicts this charter without a logged decision explaining why.

## How to avoid generic output
- Every claim in this charter is falsifiable (you can point to the repo and check it). Keep it that way when editing.
- Prefer "must/may not" language over "should/could" for non-negotiables.
