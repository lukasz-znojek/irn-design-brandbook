# 04 — Risks & Anti-Generic Checklist

## Purpose
A concrete, checkable list of the ways brand work quietly becomes generic — and the specific countermeasure for each. Used as the final gate (dimension 6) in `docs/03_quality-bar.md`.

## When to use
- As a final pass on any customer-facing artifact before it is marked "Approved" in `docs/02_decision-log.md`.
- When an artifact "feels off" but you can't articulate why — walk this checklist.
- During onboarding, to calibrate new contributors/agents to IRIN's specific anti-generic standards.

## Inputs
- Draft artifact.
- `strategy/tone-of-voice.md` word bank.
- `identity/color-system.md` chosen palette.

## Outputs
- A pass/fail per risk item, with fixes applied inline.

## Owner
QA Subagent + any human reviewer before external publication.

## Quality criteria
- Every risk item names the *specific generic pattern* and the *specific IRIN countermeasure* — not a vague "be more original."

---

## The checklist

### Language risks
- [ ] **Startup-generic verbs banned**: "empower," "unlock," "elevate," "seamless," "leverage," "revolutionize," "game-changing," "innovative solutions," "best-in-class," "cutting-edge." If found, rewrite using the `strategy/tone-of-voice.md` word bank.
- [ ] **Hedge-everything copy**: sentences that say nothing specific ("we help you achieve your goals"). Replace with a concrete claim tied to a proof point in `strategy/messaging-house.md`.
- [ ] **Interchangeable-brand test**: read the copy aloud replacing "IRIN" with a competitor name. If it still reads true, it's generic — add IRIN-specific specificity (a named process, a real number, a distinct POV).

### Visual risks
- [ ] **Palette drift**: any hex code used that isn't in the approved option from `identity/color-system.md`. Countermeasure: lint against the approved token list before merge (see `.github/workflows/docs-lint.yml`).
- [ ] **Stock-photo sameness**: imagery that could appear in any SaaS homepage (laptop-on-desk, generic handshake, isolated smiling professional against a gradient). Countermeasure: apply `identity/imagery-art-direction.md` treatment rules (grading tied to palette, specific subject framing).
- [ ] **Font substitution creep**: any non-Manrope typeface introduced "just this once." Countermeasure: `identity/typography-system.md` is the single allowed source; flag and revert.
- [ ] **Trend-chasing motion/UI**: adopting a design trend (e.g. a currently-fashionable gradient mesh or glassmorphism) without a rationale tied to `identity/motion-principles.md` or `strategy/positioning.md`.

### Structural risks
- [ ] **Unsourced strategic claims**: any positioning or competitive claim without an entry in `research/sources.md`.
- [ ] **False-choice options**: when presenting the required 7 options (A–G) for a major decision, options are not genuinely distinct (e.g. 7 shades of the same blue). Countermeasure: options must differ in *strategic intent*, not just hue — see the required structure in `identity/color-system.md`.
- [ ] **Approval theater**: marking something "Approved" in the decision log without an actual human confirmation captured (Choose/Keep/Change/Confidence block filled in).

## Example (IRIN)
Draft headline: *"IRIN empowers teams to unlock seamless brand experiences."* — fails the interchangeable-brand test and the banned-verbs check (empowers, unlock, seamless). Rewrite per `strategy/tone-of-voice.md`: *"We build the brand system your team can run without us in the room."* — specific claim, distinct POV, passes.

## Template (blank reusable block)
```
Artifact: 
| Risk | Present? (Y/N) | Fix applied |
|---|---|---|
| Startup-generic verbs |  |  |
| Hedge-everything copy |  |  |
| Interchangeable-brand test |  |  |
| Palette drift |  |  |
| Stock-photo sameness |  |  |
| Font substitution creep |  |  |
| Trend-chasing motion/UI |  |  |
| Unsourced strategic claims |  |  |
| False-choice options |  |  |
| Approval theater |  |  |
```

## Common failure modes
- Running this checklist only on final copy, missing generic patterns baked into an early creative brief that then propagate downstream.
- Treating "not technically banned word list" as equivalent to "not generic" — the interchangeable-brand test catches what the word list misses.

## How to avoid generic output
- Make this checklist a required step in `templates/design-qa-checklist.md` and `orchestration/subagent-qa-review.md`, not an optional nice-to-have.
