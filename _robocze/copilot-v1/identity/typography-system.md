# IRIN Typography System

## Purpose
- Define how Manrope is used as IRIN’s sole primary typeface across web, product, print, presentations, and internal brand outputs.
- Turn a fixed font choice into a disciplined hierarchy that feels engineered, editorial, and warm-minimal.
- Reduce arbitrary type decisions so the brand reads consistently across design and code.

## When to use
- Use this document when setting any headline, body copy, UI label, caption, table heading, proposal section, or campaign asset.
- Use it while building interfaces, landing pages, decks, long-form case studies, and motion title cards.
- Use it alongside `./spacing-grid-layout.md` for rhythm and `./color-system.md` for contrast decisions.
- Use it before approving typography tokens in code or component libraries.

## Inputs
- Manrope font files with weights 200, 300, 400, 500, 600, 700, and 800.
- Context of use: product UI, marketing site, social graphic, document, pitch deck, or print layout.
- Content characteristics: density, desired emphasis, line length, viewport size, and accessibility constraints.
- Brand tone requirements: precise, quietly confident, warm-minimal, editorial.

## Outputs
- A clear type hierarchy with predictable sizing, line-height, and spacing.
- Legible text that survives responsive changes without becoming cramped or generic.
- A limited-weight composition that feels intentional rather than over-styled.
- Shared implementation guidance for design files and coded systems.

## Owner
- Primary owner: Design lead.
- Approval partner: Founder / Creative Director.
- Technical implementation owners: Design systems engineer and front-end developers.
- Exception approval: only for language support or accessibility reasons.

## Quality criteria
- Manrope remains the primary typeface in all brand and product contexts.
- Hierarchy is established through scale, weight, spacing, and layout—not through font swapping.
- Body text stays readable at target sizes and line lengths.
- No screen uses more than two main text weights unless there is a strong editorial reason.
- Typographic rhythm aligns with the spacing system in `./spacing-grid-layout.md`.
- The result feels confident and premium, not overly expressive or startup-loud.

## Typeface role
- **Primary typeface**: Manrope.
- **Status**: non-negotiable.
- **Use Manrope for**: headings, body text, UI labels, navigation, metadata, pull quotes, data labels, and buttons.
- **Allowed fallback for code or technical strings**: system mono stack only when content is actually code or tabular debug data.
- Mono fallback stack:
  - `ui-monospace`
  - `SFMono-Regular`
  - `SF Mono`
  - `Menlo`
  - `Consolas`
  - `Liberation Mono`
  - `monospace`
- Do not introduce secondary serif or display pairings to create “personality.” Precision should come from composition.

## Weight scale and intended use
| Weight | Label | Primary use | Notes |
| --- | --- | --- | --- |
| 200 | Extra Light | Rare large-format editorial headlines | Use sparingly; can feel too fragile below 48 px |
| 300 | Light | Long-form pull quotes or spacious marketing headlines | Best when layout has generous white space |
| 400 | Regular | Body copy, paragraphs, captions in calm layouts | Default reading weight |
| 500 | Medium | UI labels, navigation, secondary emphasis | Best utility weight for interfaces |
| 600 | SemiBold | Section headings, buttons, dense metadata emphasis | Use for structural hierarchy |
| 700 | Bold | H2-H3 emphasis, calls to action, key numeric highlights | Avoid overusing in editorial pages |
| 800 | ExtraBold | Display moments only | Use as a controlled accent, not a default brand voice |

## Weight usage rules
- Default body copy should use 400.
- Default UI label weight should use 500.
- Section headings typically use 600 or 700.
- Display typography should usually stay between 300 and 700; reserve 800 for short, deliberate emphasis.
- On a single screen, prefer no more than two primary weights plus italic-free hierarchy through size and spacing.
- Avoid using 200 and 800 together on the same screen; the jump can feel theatrical instead of refined.

## Type scale
| Token | Use case | px | rem | Line-height | Letter-spacing | Recommended weight |
| --- | --- | --- | --- | --- | --- | --- |
| Display-XL | Hero statement on wide desktop | 72 px | 4.5 rem | 1.02 | -0.04em | 600 |
| Display-L | Hero statement on standard desktop | 64 px | 4 rem | 1.04 | -0.035em | 600 |
| Display-M | Compact hero / opener | 56 px | 3.5 rem | 1.06 | -0.03em | 600 |
| H1 | Primary page title | 48 px | 3 rem | 1.10 | -0.025em | 600 |
| H2 | Major section heading | 36 px | 2.25 rem | 1.15 | -0.02em | 600 |
| H3 | Section heading | 28 px | 1.75 rem | 1.20 | -0.015em | 600 |
| H4 | Card / subsection heading | 22 px | 1.375 rem | 1.25 | -0.01em | 600 |
| Body-L | Lead paragraph | 20 px | 1.25 rem | 1.50 | -0.005em | 400 |
| Body | Default paragraph | 16 px | 1 rem | 1.55 | 0em | 400 |
| Body-S | Dense support copy | 14 px | 0.875 rem | 1.50 | 0em | 400 |
| Label-L | Button / nav / field label | 16 px | 1 rem | 1.35 | 0.01em | 500 |
| Label | UI micro-hierarchy | 14 px | 0.875 rem | 1.35 | 0.01em | 500 |
| Caption | Meta / timestamps / figure notes | 12 px | 0.75 rem | 1.40 | 0.015em | 500 |
| Overline | Small section kicker | 12 px | 0.75 rem | 1.25 | 0.08em | 600 |

## Hierarchy rules
- Use fewer sizes than most teams expect; restraint reads as confidence.
- If two text blocks are adjacent and serve different hierarchy levels, change one variable decisively—size, weight, or spacing—not all three slightly.
- Reserve Display tokens for short lines of five to ten words where shape and rhythm matter.
- Keep H1 unique within a page template.
- Use H2 for major page segmentation, H3 for nested sections, and H4 for cards or dense modules.
- For body copy, let spacing between paragraphs signal rhythm rather than stacking many text styles.

## Responsive scaling guidance
| Breakpoint | Display behavior | Heading behavior | Body behavior | Notes |
| --- | --- | --- | --- | --- |
| 1440 px and above | Use full scale | H1-H4 at default | Body stays 16-20 px | Protect whitespace; do not upscale body just because space exists |
| 1024-1439 px | Step Display down one token when needed | H1 may drop from 48 to 42 px | Body unchanged | Preserve line length before preserving size |
| 768-1023 px | Display usually caps at 48-56 px | H2/H3 may step down slightly | Body stays 16 px | Avoid three-line hero breaks if possible |
| 480-767 px | Display 40-48 px | H1 around 36-40 px | Body 16 px, Body-S 14 px | Prioritize clean wrapping and generous leading |
| Below 480 px | Display only when necessary | H1 around 32-36 px | Body minimum 14 px, preferably 16 px | Never shrink body below 14 px |

## Line-length and readability guidance
- Target body text line length between 45 and 75 characters.
- In product settings or tables, 60-72 characters often balances density and readability well.
- Use line-height between 1.4 and 1.6 for paragraphs.
- Short headlines can tighten to 1.02-1.2 depending on scale.
- Dense UI labels can drop to 1.25-1.35 if spacing around components is sufficient.
- Avoid full-width desktop text columns without a measure constraint.

## Alignment principles
- Left align almost all running text.
- Center alignment is acceptable for brief hero statements, pull quotes, or ceremonial title slides only.
- Avoid justified text; it creates inconsistent spacing and weakens the engineered feel.
- Use consistent baseline relationships across neighboring components.
- Numbers in tables should align intentionally by decimal or right edge where scanning matters.

## Pairing rules
- Manrope is the only primary font family for the brand.
- Use weight contrast before size contrast when you need subtle differentiation inside dense UI.
- Use size contrast before color contrast when hierarchy must remain accessible in grayscale or print.
- Use uppercase sparingly and mainly for short overlines, metadata, or compact labels.
- When code snippets appear in documentation or product contexts, use the mono fallback stack and keep it visually secondary to the core Manrope system.

## Accessibility guidance
- Minimum body size: 14 px absolute, 16 px preferred for routine reading.
- Use 4.5:1 contrast for body text and 3:1 for large text; see `./color-system.md`.
- Avoid long passages in light weights below 20 px.
- Do not communicate hierarchy through color alone.
- Preserve visible focus states and sufficient label clarity in forms.
- Review typography on real devices, especially mid-range laptops and small phones, not only in design tools.

## Do
- Use generous margins to let type feel expensive.
- Use 500 or 600 for utility emphasis instead of jumping to heavy bold everywhere.
- Tighten tracking slightly on large display type where the forms allow it.
- Keep interface copy concise so the typography can breathe.
- Let contrast between scale and whitespace create the editorial tone.

## Don’t
- Don’t use more than two primary weights on a single screen unless a long-form editorial layout truly requires it.
- Don’t condense, stretch, or artificially slant Manrope.
- Don’t set body text below 14 px.
- Don’t set large passages in all caps.
- Don’t rely on low-contrast grey text for sophistication.
- Don’t use random negative tracking on body copy.
- Don’t create hierarchy by mixing several near-identical sizes.

## Implementation notes
- Tokenise the scale in code so spacing and component patterns can reuse it.
- Keep rem values tied to a 16 px root unless an accessibility-led platform decision changes this globally.
- If variable font support is available, still align usage to the approved weight steps above.
- Audit button labels and navigation first; these are where weight drift often begins.
- Cross-check hero text wrapping with `../applications/website-guidelines.md` before finalizing responsive breakpoints.

## Example (IRIN)
- Scenario: an IRIN service page hero for a growth-stage platform team.
- Eyebrow: Overline, 12 px / 0.75 rem, 600, letter-spacing 0.08em, all caps used for a two-word kicker only.
- Headline: Display-M, 56 px / 3.5 rem, line-height 1.06, weight 600.
- Supporting copy: Body-L, 20 px / 1.25 rem, line-height 1.5, weight 400, max width 34ch.
- CTA label: Label-L, 16 px / 1 rem, line-height 1.35, weight 500.
- Result: the page feels exacting and premium because hierarchy is carried by scale, measure, and calm spacing—not by font variety.

## Template (blank reusable block)
```md
### Typography decision
- Context:
- Content type:
- Token used:
- Size:
- Line-height:
- Letter-spacing:
- Weight:
- Measure / max width:
- Contrast check:
- Notes:
- Reviewer:
```

## Common failure modes
- Treating Manrope like a default UI font instead of giving it an editorial system.
- Overusing bold weights so every headline competes with every button.
- Letting developers approximate sizes without a token set.
- Setting body copy in narrow line-height to fit more text above the fold.
- Using too many tiny distinctions that no reader can perceive consistently.
- Copyfitting long marketing sentences into display styles designed for brevity.

## How to avoid generic output
- Favor fewer styles with clearer intent.
- Write shorter copy so type can stay large and confident.
- Keep measures narrow enough to feel considered.
- Reuse the same hierarchy patterns across channels so the brand reads as a system rather than a series of one-off layouts.
- If a page starts to resemble a SaaS template, remove a style, increase whitespace, and simplify the hierarchy.
