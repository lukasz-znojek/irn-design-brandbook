# 03 — Quality Bar

## Purpose
Define the measurable criteria that separate "shipped" from "actually good" for every artifact produced inside this repository. This is the rubric the QA subagent (`orchestration/subagent-qa-review.md`) and `ai/evaluation-rubric.md` are built against.

## When to use
- Before merging any PR that touches `/strategy`, `/identity`, `/applications`, or `/templates`.
- When a subagent self-assesses confidence before returning output (per `orchestration/handoff-contracts.md`).
- During brand audits (`templates/brand-audit-template.md`).

## Inputs
- Draft artifact (doc, template, copy, visual spec).
- This rubric.

## Outputs
- A score (1–5) per dimension + an overall gate decision (Pass / Pass with fixes / Fail).

## Owner
QA Subagent (`orchestration/subagent-qa-review.md`), ratified by Brand System Owner for anything customer-facing.

## Quality criteria
- Every dimension has a concrete, checkable definition — not just an adjective.
- Score of 3 ("meets bar") is the minimum to pass; anything below requires revision, not just a note.

---

## The six dimensions

### 1. Strategic coherence (1–5)
Does this artifact trace cleanly back to `strategy/brand-core.md` and `strategy/positioning.md` without contradiction?
- **5**: Directly reinforces brand promise and positioning; a reviewer can point to the exact line it derives from.
- **3**: Consistent, but doesn't clearly reinforce the strategy (neutral).
- **1**: Contradicts stated positioning or values.

### 2. Visual consistency (1–5)
Does it correctly apply `identity/color-system.md`, `identity/typography-system.md`, `identity/spacing-grid-layout.md`?
- **5**: Uses approved palette option/tokens, correct Manrope weights/scale, correct spacing scale, no ad hoc hex codes or fonts.
- **3**: Mostly correct, minor scale/spacing deviation.
- **1**: Off-palette colors, wrong/extra typeface, arbitrary spacing.

### 3. Linguistic consistency (1–5)
Does copy match `strategy/tone-of-voice.md`?
- **5**: Passes the word-bank check (no banned generic words), correct sentence rhythm, correct persona-adapted register.
- **3**: Broadly on-voice, 1–2 minor lapses.
- **1**: Reads like generic SaaS/agency copy — see `docs/04_risks-and-anti-generic-checklist.md`.

### 4. Production readiness (1–5)
Can this be handed to Claude Code / a designer / a developer and implemented without further clarification?
- **5**: All specs (sizes, hex, spacing, states) are explicit; no "TBD" in a shipped artifact.
- **3**: Mostly complete, 1–2 gaps flagged as open questions.
- **1**: Vague, requires a follow-up meeting to implement.

### 5. Template reusability (1–5)
Could this file be reused for a *different* IRIN project/campaign by only filling in the blank template block?
- **5**: Clean separation between the IRIN example and the blank template; template has no IRIN-specific residue.
- **3**: Reusable with minor edits.
- **1**: Template is really just the IRIN example with names swapped — not generalizable.

### 6. Anti-generic score (1–5)
Score against `docs/04_risks-and-anti-generic-checklist.md`.
- **5**: Passes all anti-generic checks; a competitor could not plausibly ship the identical artifact.
- **3**: Passes most checks, 1 minor generic pattern flagged.
- **1**: Could be relabeled with any competitor's name with zero changes.

## Gate logic
- **Pass**: all dimensions ≥ 4.
- **Pass with fixes**: all dimensions ≥ 3, at least one at 3 with a logged fix-it note.
- **Fail**: any dimension ≤ 2 — return to originating subagent with the specific failing dimension(s).

## Example (IRIN)
A LinkedIn quote-card template (`applications/social-templates.md`) is submitted. QA scores: Strategic coherence 4, Visual consistency 3 (uses correct palette but wrong caption line-height), Linguistic consistency 5, Production readiness 4, Template reusability 5, Anti-generic 4. → **Pass with fixes**: line-height corrected to spec in `identity/typography-system.md`, then merged.

## Template (blank reusable block)
```
Artifact: 
Reviewer: 
Date: 
| Dimension | Score (1-5) | Note |
|---|---|---|
| Strategic coherence |  |  |
| Visual consistency |  |  |
| Linguistic consistency |  |  |
| Production readiness |  |  |
| Template reusability |  |  |
| Anti-generic score |  |  |
Gate decision: Pass / Pass with fixes / Fail
```

## Common failure modes
- Scoring everything a 4 by default ("grade inflation") — require a specific note justifying any score ≥ 4.
- Treating "Pass with fixes" as "Pass" and forgetting to apply the fix before merge.

## How to avoid generic output
- Dimension 6 exists specifically to catch generic output structurally, not just editorially — always run it last as a final gate.
