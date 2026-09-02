# IRIN Iconography

## Purpose
- Define a clear icon style for interfaces, diagrams, service explanations, and lightweight brand-support moments.
- Ensure icons feel engineered and consistent with IRIN’s typography, spacing, and motion systems.
- Prevent the brand from drifting into mixed icon packs or decorative inconsistency.

## When to use
- Use this document when creating or selecting icons for product UI, website content, presentations, diagrams, or wayfinding-like supporting graphics.
- Use it when exporting SVG assets, designing icon buttons, or briefing an illustrator on pictographic support elements.
- Use it alongside `./typography-system.md` for label pairing and `./motion-principles.md` for interactive icon behavior.
- Use it before importing any third-party icon set into a product or website.

## Inputs
- Functional need: navigation, status, feature explanation, system state, social link, file type, or diagrammatic support.
- Context of use: product interface, website section, deck, PDF, or motion sequence.
- Active color rules from `./color-system.md`.
- Component spacing and sizing requirements from `./spacing-grid-layout.md`.

## Outputs
- A consistent icon family with predictable stroke, scale, and optical balance.
- SVG or component-ready icon assets aligned to the IRIN design language.
- Clear acceptance criteria for selecting external icons or drawing new ones.
- Reduced visual noise in interface and brand-support graphics.

## Owner
- Primary owner: Design systems lead.
- Supporting owners: Product design and brand design.
- Implementation owners: Front-end developers and design ops.
- Exception approval: Founder / Creative Director for campaign or editorial uses.

## Quality criteria
- Icons are legible at their target size without feeling chunky or ornamental.
- Stroke weight, radius, and visual density remain consistent across the set.
- Icons support comprehension rather than stealing attention from content.
- Construction rules align with IRIN’s precise, warm-minimal tone.
- Interaction states remain crisp in motion and high-contrast contexts.
- New icons can be added without changing the overall style logic.

## Core style specification
- Base grid: 24 px.
- Default stroke: 2 px.
- Stroke alignment: center-aligned in vector tooling where possible, then exported cleanly.
- Corner radius: subtle, typically 2 px optical rounding or equivalent curve softness.
- End caps: round or slightly softened square, but consistent across the family.
- Fill style: primarily outline icons; use fills only for small status dots, contained shapes, or semantically necessary solids.
- Visual tone: technical, calm, and exact—not cute, loud, or toy-like.

## Size system
| Size token | Use | Notes |
| --- | --- | --- |
| 16 px | Dense product UI only | Use simplified forms; test carefully |
| 20 px | Compact nav and utility actions | Good for top bars and lists |
| 24 px | Default icon size | Standard system baseline |
| 32 px | Feature cards or marketing support | Use when icon shares space with a heading |
| 48 px | Section illustration support | Keep stroke relationships consistent |

## Construction rules
- Start every icon on a 24 px grid, then derive smaller and larger sizes from the same geometry.
- Preserve even padding inside the artboard; icons should not visually touch the edges.
- Use a limited number of primitives so forms stay calm.
- Maintain comparable visual weight across open and closed shapes.
- Simplify internal detail before reducing size.
- Align diagonal and curved forms optically, not just mathematically.

## Stroke and detail guidance
- Default stroke is 2 px at 24 px size.
- At 16 px, consider 1.75 px visually if export technology allows; otherwise simplify geometry while keeping a 2 px stroke.
- Avoid nested micro-details that blur at interface scale.
- If an icon requires more than one interior motif to be understood, it is probably too complex.
- Negative space should remain open and deliberate.

## Filled vs outlined use
- Outline icons are the default for navigation, system actions, and product tools.
- Filled icons may be used for active state emphasis, semantic markers, or highly compact contexts.
- Do not mix filled and outline styles randomly inside the same component row.
- If active states use fill, inactive states should remain visually related—not from a different icon family.

## Color usage
- Use neutral or text colors for standard icons.
- Use accent color only when the icon is part of a defined emphasis or semantic state.
- Do not rainbow-code icons for decorative variety.
- Semantic icons should follow success, warning, error, and info mappings defined in `./color-system.md`.
- Ensure interactive icon states preserve sufficient contrast in light and dark mode.

## Icon families IRIN should maintain
- Navigation and UI controls.
- Status and feedback indicators.
- Product feature explanation icons.
- File / export / system object icons.
- Social and contact icons.
- Diagram support shapes for decks and case studies.
- Optional favicon-adjacent utility symbols only if explicitly approved and distinct from the logo.

## Label pairing rules
- Most icons should pair with text on first use in marketing contexts.
- In product UI, icon-only actions are acceptable when the symbol is conventional and tooltip support exists.
- Keep icon-to-label gap at 8 px in compact contexts and 12 px in roomier ones.
- Align icon optical center to the first text line or control center, depending on component type.

## Do
- Use simple geometric construction.
- Use one consistent stroke logic across the full set.
- Keep silhouette recognition strong at small sizes.
- Test icons on real screens and against real text labels.
- Remove details until the icon reads faster.

## Don’t
- Don’t mix rounded playful icons with sharp technical ones.
- Don’t use illustrations as icons.
- Don’t switch stroke widths arbitrarily to solve one icon’s edge case.
- Don’t overfill shapes just to increase contrast; use better color or layout support.
- Don’t mirror or stretch icons to force-fit a context.
- Don’t decorate icons with shadows, gradients, or glossy effects.

## Accessibility guidance
- Icons should not be the sole carrier of meaning for critical actions or statuses.
- Maintain clear labels or supporting text for non-obvious icons.
- Preserve contrast for icon strokes against their background, especially at 16 px and 20 px sizes.
- Ensure tap targets and button containers are sized through component padding, not by enlarging icons alone.
- Respect `prefers-reduced-motion` when icons animate; see `./motion-principles.md`.

## Implementation notes
- Export SVGs with clean paths and sensible viewBox values.
- Snap obvious vertical and horizontal edges to the pixel grid where possible.
- Use shared naming patterns for icons in code and design assets.
- If importing a third-party library, redraw or normalize any icons that do not fit the system.
- Create approval examples for edge-case icons such as analytics, AI, integration, or workflow concepts.

## Example (IRIN)
- Scenario: service-overview cards on the IRIN website.
- Size: 32 px icons on a 24 px-derived geometry scaled proportionally.
- Stroke: 2 px, rounded ends, minimal internal detail.
- Color: neutral text color by default, accent used only on hover indicator or key highlighted card.
- Pairing: icon above H4 heading with 12 px gap, aligned to the same left edge as the text block.
- Result: the icons support the message of precision and systems thinking without becoming decorative mascots.

## Template (blank reusable block)
```md
### Icon decision
- Name:
- Function:
- Context:
- Grid size:
- Stroke width:
- Fill or outline:
- Color token:
- Label pairing:
- Accessibility note:
- Reviewer:
```

## Common failure modes
- Pulling icons from multiple libraries with different corner logic and density.
- Designing one icon in detail and forcing the rest of the set to match it awkwardly.
- Using accent color everywhere, which weakens hierarchy.
- Relying on icon-only meaning for uncommon actions.
- Letting dense feature pages become symbol-heavy and label-light.
- Treating icons as a brand personality shortcut.

## How to avoid generic output
- Keep icons secondary to content and typography.
- Favor system clarity over novelty.
- Use a limited formal vocabulary so repeated use builds recognition.
- If an icon looks trendy but not timeless, simplify it.
- If a set feels like it could belong to any off-the-shelf dashboard, refine stroke, spacing, and pairing until it feels more authored and exact.
