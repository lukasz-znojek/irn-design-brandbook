# IRIN Motion Principles

## Purpose
- Define how motion should support clarity, polish, and perceived precision across IRIN’s digital brand and product experiences.
- Prevent animation from drifting into novelty or unnecessary spectacle.
- Provide a motion system that feels engineered, quiet, and editorial.

## When to use
- Use this document when designing or implementing transitions, hover states, loading behavior, page reveals, navigation shifts, or micro-interactions.
- Use it for website motion, product interface states, presentation transitions, and lightweight social motion assets.
- Use it with `./iconography.md` for icon behavior and `./spacing-grid-layout.md` when motion affects layout.
- Use it before approving new easing curves or adding animation libraries to core brand surfaces.

## Inputs
- Interaction context: hover, tap, load, expand, sort, reveal, transition, or dismiss.
- User intent and task criticality.
- Device context, performance constraints, and accessibility requirements.
- Related visual tokens from typography, color, spacing, and iconography systems.

## Outputs
- Motion decisions that make state changes easier to understand.
- A shared duration and easing scale for designers and developers.
- Reduced inconsistency across interactive surfaces.
- Animations that feel premium without demanding attention.

## Owner
- Primary owner: Product design lead.
- Supporting owners: Front-end engineering and brand design.
- Accessibility review partner: whoever owns QA for the surface.
- Exception approval: Founder / Creative Director for flagship brand pieces.

## Quality criteria
- Motion clarifies cause and effect.
- Durations and easing choices are consistent with the system.
- Motion never blocks task completion or overwhelms content.
- Reduced-motion users receive an equivalent, respectful experience.
- Performance remains smooth on ordinary devices.
- The result feels controlled and precise rather than playful or overproduced.

## Core principles
- Animate with purpose.
- Prefer subtle transition over theatrical entrance.
- Reflect interface structure; do not animate unrelated properties just because it looks “richer.”
- Motion should help the user anticipate what changed and where to look next.
- If an animation calls attention to itself before it clarifies the interface, it is too much.

## Duration scale
| Token | Duration | Use |
| --- | --- | --- |
| Instant | 0-80 ms | State toggles that should feel immediate |
| Fast | 120 ms | Hover, icon tint, button state, focus refinement |
| Standard | 200 ms | Dropdowns, small reveals, filter chips, card elevation |
| Calm | 320 ms | Panel transitions, section fades, content swaps |
| Deliberate | 480 ms | Large page transitions, hero media, editorial reveals |

## Easing curves
| Name | Cubic-bezier | Use | Notes |
| --- | --- | --- | --- |
| Standard out | `cubic-bezier(0.22, 1, 0.36, 1)` | Entrances and reveals | Fast start, calm settle |
| Standard in-out | `cubic-bezier(0.4, 0, 0.2, 1)` | Position or size shifts | Familiar, neutral system curve |
| Soft in | `cubic-bezier(0.32, 0, 0.67, 0)` | Exits and dismissals | Controlled acceleration |
| Linear | `linear` | Progress indicators only | Avoid for expressive UI transitions |

## Property priorities
- Prefer opacity, transform, and subtle color changes.
- Use scale sparingly and within a narrow range such as 0.98 to 1 or 1 to 1.02.
- Avoid animating large shadow jumps unless the component already uses elevation meaningfully.
- Avoid animating width or height directly when transform or opacity can communicate the change more cleanly.
- If layout must reflow, keep the motion stable and short.

## When to animate
- Animate when the user benefits from understanding a state change.
- Animate when revealing additional content, confirming an action, or indicating spatial relationship.
- Animate when hover or focus needs a tactile but restrained response.
- Animate hero or editorial surfaces only when motion strengthens the premium feel without delaying comprehension.

## When not to animate
- Do not animate purely to decorate a static marketing section.
- Do not animate repetitive interface events every time they occur if they slow expert users down.
- Do not animate critical alerts in a way that competes with the message.
- Do not animate long page-load sequences to hide performance issues.
- Do not add oscillation, bounce, rubber-band, or springy novelty by default.

## Micro-interaction guidance
- Hover states should usually resolve in 120 ms.
- Button hover can combine slight background shift, subtle border change, and perhaps a 1-2 px optical lift.
- Focus states should appear quickly and clearly, with motion never reducing visibility.
- Expand/collapse patterns should preserve the user’s sense of origin.
- Drag, sort, or rearrangement states should privilege clarity and positional continuity.

## Page and section transitions
- Default to no full-page transition unless the experience genuinely benefits.
- For marketing pages, use restrained fade/translate reveals tied to scroll only if they do not feel performative.
- Large reveals should still complete quickly enough that copy remains the main event.
- Staggering is acceptable for short sets of related elements, but keep intervals tight and stop before it feels choreographed.

## Loading and feedback states
- Prefer truthful progress indicators over decorative endless loops.
- Skeleton screens should be calm and low-contrast.
- Shimmer, if used, should be subtle and disabled for reduced-motion users.
- Success feedback may include a brief fade or icon transition, but the information hierarchy matters more than the flourish.
- Error states should be immediate and readable, not dramatically animated.

## Icon motion
- Icons may rotate or transform only when the motion communicates a real state change, such as disclosure or refresh.
- Keep icon rotation anchored and short.
- Avoid elastic path morphing or playful bounces.
- Pair icon state changes with label or container changes where clarity matters.

## Accessibility guidance
- Respect `prefers-reduced-motion: reduce`.
- In reduced-motion mode, remove non-essential transform and parallax effects.
- Replace animated transitions with instant or near-instant state changes plus clear visual differentiation.
- Do not use flashing, pulsing, or repeated motion to convey critical meaning.
- Ensure motion does not interfere with keyboard navigation, focus order, or readable timing.

## Performance guidance
- Keep animated surfaces composited efficiently where possible.
- Avoid stacking multiple simultaneous large-area blurs, masks, or parallax layers.
- Test on mid-range hardware, not only current flagship devices.
- If performance and polish conflict, choose simpler motion.
- Brand quality is hurt more by jank than by restraint.

## Do
- Use one motion idea per interaction.
- Keep state changes quick and calm.
- Make transitions feel authored by aligning timing across related components.
- Use motion to support spatial understanding.
- Review motion with sound off and with reduced-motion enabled.

## Don’t
- Don’t bounce the interface.
- Don’t use long chained staggers for ordinary content blocks.
- Don’t rely on motion to create excitement when the composition itself is weak.
- Don’t hide slow loading behind decorative animation.
- Don’t animate every hoverable item differently.

## Implementation notes
- Document durations and easing as tokens in code.
- Reuse shared motion utilities instead of hardcoding component-by-component values.
- Pair motion QA with accessibility QA on every major release surface.
- Review hero and navigation animations against `../applications/website-guidelines.md` before launch.
- Keep transition names literal so engineers can apply them consistently.

## Example (IRIN)
- Scenario: CTA button and supporting disclosure panel on the IRIN website.
- Button hover: 120 ms background and border transition using `Standard out`, with no bounce or overshoot.
- Disclosure icon: 200 ms rotation to 180 degrees only when the panel changes state.
- Panel reveal: 200-320 ms opacity and translateY from 6 px to 0 using `Standard out`.
- Reduced-motion mode: hover remains color-only; panel appears instantly with no transform.
- Result: the interaction feels precise and polished, like a considered product system rather than a template animation pack.

## Template (blank reusable block)
```md
### Motion decision
- Interaction:
- Trigger:
- Duration token:
- Easing token:
- Animated properties:
- Reduced-motion behavior:
- Performance concerns:
- QA notes:
- Reviewer:
```

## Common failure modes
- Adding motion late as decoration.
- Using many different easings across one product surface.
- Letting hover states linger too long.
- Animating layout dimensions in ways that feel unstable.
- Forgetting reduced-motion behavior until after implementation.
- Keeping flashy hero motion that competes with the message.

## How to avoid generic output
- Start from the question “what should become clearer?”
- Keep motion almost invisible when it works well.
- Use the same timing vocabulary everywhere so the product feels intentional.
- Remove any effect that exists only to seem modern.
- If the motion feels like it belongs to a no-code startup template, simplify it until it feels quieter and more exact.
