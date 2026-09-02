# IRIN Spacing, Grid, and Layout

## Purpose
- Establish a shared spacing rhythm and layout structure for IRIN brand, marketing, product, and print work.
- Translate the studio’s precision-driven positioning into measurable rules that designers and developers can apply consistently.
- Prevent crowded interfaces, arbitrary padding, and template-like compositions.

## When to use
- Use this document when designing pages, sections, cards, modals, forms, decks, PDFs, proposals, and print collateral.
- Use it while building responsive layouts, component spacing tokens, and editorial spreads.
- Use it with `./typography-system.md` to align vertical rhythm and with `./logo-guidelines.md` to protect brand clearspace.
- Use it during QA for web implementation and before approving production-ready component specs.

## Inputs
- Content hierarchy: what is primary, secondary, or tertiary.
- Target medium: responsive web, native product screen, static social asset, slide, or print format.
- Chosen typography tokens from `./typography-system.md`.
- Chosen palette and contrast requirements from `./color-system.md`.

## Outputs
- A layout with consistent internal spacing and predictable section rhythm.
- A grid structure that can scale from editorial marketing pages to dense product views.
- Component padding and gap values tied to a reusable base scale.
- Cleaner implementation handoff between design and code.

## Owner
- Primary owner: Design systems lead.
- Supporting owners: Product design and front-end engineering.
- Print adaptation owner: Brand or editorial designer.
- Exception approval: Founder / Creative Director for flagship communications.

## Quality criteria
- Spacing decisions resolve to the approved scale rather than arbitrary values.
- Layouts feel calm, aligned, and intentional across breakpoints.
- Grids support both editorial openness and product clarity.
- Components breathe without becoming wasteful.
- Alignment decisions can be explained in terms of content hierarchy, not taste alone.
- The overall composition feels premium and engineered rather than padded by default.

## Base spacing scale
| Token | px | Typical use |
| --- | --- | --- |
| 0.5 | 4 px | Hairline offsets, icon nudges, small chip padding |
| 1 | 8 px | Tight internal spacing, small control gaps |
| 1.5 | 12 px | Compact lists, label-to-field spacing |
| 2 | 16 px | Default small component padding, text block gaps |
| 3 | 24 px | Standard card padding, stacked content groups |
| 4 | 32 px | Section internals, modal padding |
| 6 | 48 px | Major component separation, hero padding |
| 8 | 64 px | Section spacing on desktop |
| 12 | 96 px | Large-page rhythm, major chapter breaks |

## Scale rules
- Prefer values from the scale above before considering custom spacing.
- Use 4 px only as a supporting micro-adjustment, not as a general layout unit.
- When between two values, choose the larger one if the content is brand-facing and the smaller one if the content is operational UI.
- Repeat spacing values within a component family so users learn the rhythm visually.
- If a section requires many one-off exceptions, the structure likely needs redesign rather than more spacing tokens.

## 12-column web grid
- Default web grid: 12 columns.
- Use a consistent max-width container; do not stretch brand-facing pages edge to edge without reason.
- Suggested desktop content max width: 1280 px.
- Standard desktop gutter: 24 px.
- Standard tablet gutter: 20 px.
- Standard mobile gutter: 16 px.
- Main content should align to the same left and right margins as the logo and primary heading unless the composition has a deliberate editorial break.

## Breakpoint guidance
| Breakpoint | Columns | Outer margins | Gutters | Notes |
| --- | --- | --- | --- | --- |
| 1440 px and above | 12 | 80-96 px | 24 px | Preserve generous white space; avoid filling every column |
| 1024-1439 px | 12 | 56-72 px | 24 px | Default desktop working range |
| 768-1023 px | 8 or 12 | 32-40 px | 20 px | Choose structure based on component density |
| 480-767 px | 4 | 20-24 px | 16 px | Reduce side-by-side content aggressively |
| Below 480 px | 4 | 16-20 px | 16 px | Stack decisively; prioritize readability |

## Section layout guidance
- Major page sections should typically use vertical spacing of 64 px or 96 px on desktop.
- On tablet, major sections often compress to 48 px or 64 px.
- On mobile, use 32 px or 48 px unless the section is a hero moment.
- Do not alternate spacing randomly between sections; use a consistent page rhythm.
- If two consecutive sections share similar visual weight, increase contrast through spacing or background change—not both unless needed.

## Component spacing rules
| Component | Internal padding | Gap guidance | Notes |
| --- | --- | --- | --- |
| Button | 12 px vertical / 16-20 px horizontal | Icon gap 8 px | Compact but not cramped |
| Text input | 12-16 px internal padding | Label gap 8 px | Allow readable cursor breathing room |
| Card | 24-32 px padding | Internal stack gap 12-16 px | Premium default treatment |
| Modal | 32 px padding desktop / 24 px mobile | Section gap 16-24 px | Avoid edge crowding |
| Navbar | 16-24 px vertical zone | Item gap 16-24 px | Let the logo breathe |
| Data row | 12-16 px cell padding | Row gap by border or 8 px | Maintain scanability |
| Hero block | 48-64 px internal padding | Text-to-CTA gap 24 px | Keep statement crisp |

## Alignment principles
- Align to columns, not to arbitrary object edges.
- Maintain consistent left edges across title, copy, and CTA groups.
- Use one dominant alignment system per section.
- Center alignment is reserved for deliberate editorial hero compositions, not default cards or feature grids.
- If an element intentionally breaks the grid, make the break meaningful and singular.
- Use optical alignment when icons or rounded containers appear visually off even if mathematically centered.

## Vertical rhythm
- Tie most vertical gaps to typography size and content density.
- Paragraph-to-paragraph spacing should usually be 16 px or 24 px depending on text scale.
- Heading-to-body spacing usually ranges from 12 px to 24 px.
- Section kicker to headline can use 8 px or 12 px for crispness.
- Related metadata clusters should feel tighter than content clusters.
- Keep card internals denser than page sections so the page still breathes.

## Responsive adaptation rules
- Collapse multi-column layouts earlier than a generic template would if content quality improves.
- Preserve margin integrity on mobile; do not chase screen width so aggressively that text touches the edges.
- Let stacked spacing increase slightly when content becomes vertical to maintain clarity.
- Reduce decorative layout complexity before reducing legibility.
- Review awkward orphan CTAs and two-word lines at every breakpoint.

## Print grid guidance
- Start print layouts from the same spacing logic, then adapt to physical trim size.
- Use a baseline grid when document density is high or when multi-page editorial consistency matters.
- For A4 or US Letter proposals, a 6- or 12-column grid usually translates well from digital compositions.
- Maintain generous outer margins; IRIN should feel considered, not maximized to the page edge.
- Use 3 mm bleed where required by production, but do not confuse bleed with live-content margin.
- Respect logo clearspace independently from trim, fold, or bind constraints.

## Layout patterns for IRIN
- **Editorial hero**: 5-7 columns for copy, empty space retained as a strategic signal of confidence.
- **Case study section**: 7/5 or 8/4 split with copy leading and supporting artifact block secondary.
- **Service comparison**: 3 equal columns on desktop, single stacked list on mobile.
- **Proposal page**: strong left alignment, clear chapter spacing, and restrained side notes.
- **Product UI dashboard**: denser 12-column structure with cards sharing padding tokens and consistent row spacing.

## Density guidance
- Brand-facing marketing should default to low-to-medium density.
- Product surfaces can move to medium density, but high density still needs token discipline.
- If a screen needs very high density, enforce stronger alignment and typography rules to keep it feeling premium.
- Resist the temptation to reduce every gap once content grows; first edit the content or restructure the hierarchy.

## Do
- Use repeated spacing patterns to build recognition.
- Increase white space around high-value messages.
- Let sections end cleanly on rhythm values instead of manual nudges.
- Align imagery, text, and controls to a common grid edge.
- Test layouts with real content lengths before approving them.

## Don’t
- Don’t invent arbitrary gaps like 18 px or 22 px without a strong system reason.
- Don’t rely on auto-layout defaults without checking the resulting rhythm.
- Don’t cram the logo into the same horizontal band as too many controls.
- Don’t use equal spacing everywhere; hierarchy requires contrast.
- Don’t sacrifice margin quality just to keep a layout symmetrical.

## Example (IRIN)
- Scenario: IRIN landing page with logo, hero, proof strip, and services overview.
- Container: 12 columns, 1280 px max width, 72 px outer margins on standard desktop.
- Header: 24 px vertical zone with wordmark aligned to column 1 and navigation starting later rather than crowding it.
- Hero: copy spans 6 columns, CTA cluster sits below with a 24 px gap, surrounding section padding 96 px top and 64 px bottom.
- Proof strip: 48 px top padding, 24 px between logos, divider avoided in favor of whitespace.
- Services cards: 3-up grid, each card 24 px internal padding, 16 px content gaps.
- Result: the page feels deliberate and boutique because empty space is treated as structure, not as leftover area.

## Template (blank reusable block)
```md
### Layout decision
- Surface / page:
- Breakpoint:
- Grid:
- Outer margins:
- Gutters:
- Key column spans:
- Section spacing:
- Component padding:
- Alignment notes:
- Reviewer:
```

## Common failure modes
- Building a page from component defaults with no page-level rhythm.
- Using the grid only for broad columns while ignoring internal alignment.
- Compressing spacing whenever content volume increases.
- Keeping too many columns active on tablet and small laptop sizes.
- Treating whitespace as decorative instead of functional.
- In print, forgetting that binding and trim alter perceived balance.

## How to avoid generic output
- Keep at least one meaningful area of open space in major layouts.
- Let the grid guide composition, but allow editorial asymmetry where it sharpens hierarchy.
- Choose fewer layout patterns and repeat them consistently.
- Use spacing contrast to signal confidence: not everything deserves equal visual urgency.
- If a layout resembles a no-code landing page template, simplify the number of simultaneous modules and strengthen the margins.
