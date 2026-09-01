# Website guidelines

## Purpose
- Define how IRIN's identity behaves on the web across marketing pages, case studies, and contact flows.
- Align website decisions with `../identity/typography-system.md`, `../identity/color-system.md`, and `../docs/03_quality-bar.md`.
- Balance editorial clarity with engineering discipline so the site feels premium and fast.
- Prevent visual drift between launch pages, product pages, and long-form content.
- Ensure the brand's precision shows up in responsiveness, accessibility, and performance, not only aesthetics.

## When to use
- Use when designing or building any page on irin.studio or its subdomains.
- Use when updating page templates, navigation, or shared components.
- Use when creating landing pages tied to campaigns or launches.
- Use when adapting case-study assets from decks or social posts into the web system.
- Use when preparing content and layout briefs for product marketing pages.
- Use when auditing accessibility or performance regressions.
- Use alongside `../applications/social-templates.md` for launch campaigns spanning site and social.
- Use alongside `../templates/design-qa-checklist.md` before shipping visual changes.

## Inputs
- Approved page objective and audience definition.
- Current design tokens for color, spacing, and type.
- Copy that follows the IRIN verbal standard.
- Approved screenshots, diagrams, or case-study media.
- Component inventory or design system references.
- Target devices and content priorities per breakpoint.
- Accessibility acceptance criteria with WCAG AA as baseline.
- Performance budgets for page weight, images, and fonts.
- Measurement needs such as analytics events or form submissions.

## Outputs
- A page or component design that follows the web-specific rules below.
- Clear responsive behavior across breakpoints.
- Accessible color, type, and interaction states.
- Performance-conscious assets and implementation notes.
- A template mapping for home, product, case study, or contact pages.
- Exported or coded assets named consistently for handoff and maintenance.
- A QA record showing contrast, responsiveness, and content checks passed.

## Owner
- Primary owner: Product designer or brand designer working on web surfaces.
- Engineering owner: Front-end engineer responsible for implementation fidelity and performance.
- Content owner: Marketing or strategy lead.
- Accessibility owner: Design and engineering shared responsibility.
- Final approver: Founder or brand steward for high-visibility pages.

## Quality criteria
### Web typography application
- Use Manrope exclusively for UI and marketing type unless a code sample requires a monospace fallback.
- Set type using rem-based scales so accessibility zoom and system settings behave predictably.
- Keep heading line lengths compact; wide desktop screens still require editorial restraint.
- Body copy should sit in a comfortable measure, typically 60 to 75 characters.
- Avoid over-light weights that disappear on commodity displays.
- Use optical hierarchy through size, weight, and spacing before introducing color shifts.

### Web color application
- Start from the approved digital palette in `../identity/color-system.md`.
- Reserve the highest-contrast pairing for primary headings and key actions.
- Use accent colors sparingly to signal action, emphasis, or data categories.
- Keep neutrals doing most of the structural work.
- Avoid large gradient fields unless they are tested for banding and legibility.
- Check hover, focus, disabled, and visited states explicitly.

### Component patterns
| Component | Guidance | Notes |
| --- | --- | --- |
| Primary button | Solid fill, concise label, strong contrast | One primary action per section |
| Secondary button | Outline or low-emphasis fill | Use for alternatives, not indecision |
| Text link | Underline on hover or persistent underline in long-form contexts | Links should read as links |
| Navigation | Simple label set, no jargon, visible current state | Prioritize clarity over cleverness |
| Footer | Contact, links, legal, light brand presence | Treat as calm utility zone |
| Card | One idea per card, consistent padding | Avoid ornamental shadows |
| Form field | Large enough hit area, explicit labels, clear errors | No placeholder-only labels |
| Section divider | Spacing and contrast, not decoration | Editorial rhythm tool |

### Responsive breakpoints
| Breakpoint | Width | Behavior |
| --- | --- | --- |
| Small mobile | 0-479 px | Single column, stacked actions, short headings |
| Large mobile | 480-767 px | Single column with improved media ratios |
| Tablet | 768-1023 px | Two-column opportunities, simplified nav |
| Desktop | 1024-1439 px | Standard 12-column grid, fuller spacing |
| Large desktop | 1440 px and up | Increase margins before increasing line length |

### Accessibility baseline
- Meet WCAG AA color contrast for text, controls, and meaningful graphics.
- Provide visible focus states that do not rely on browser defaults alone.
- Ensure interactive targets are large enough for touch and motor accessibility.
- Preserve heading order and semantic HTML structure.
- Avoid autoplay motion that cannot be paused.
- Provide alt text for informative images and empty alt for decorative ones.
- Ensure forms expose labels, instructions, and errors programmatically.
- Test keyboard navigation for primary flows.
- Verify zoom to 200 percent without loss of function.

### Performance-conscious asset guidance
- Prefer SVG for simple marks and icons when it improves sharpness and weight.
- Use responsive images with appropriate source sets.
- Compress images without visibly harming premium presentation.
- Avoid shipping multiple similar hero images when one will do.
- Self-host or subset Manrope if implementation strategy requires it.
- Minimize layout shift by reserving media dimensions.
- Keep motion and video purposeful; weight must justify value.
- Audit third-party scripts before adding them to marketing pages.

### Page template list
- Home page: positioning, capabilities, proof, selected work, contact CTA.
- Product page: specific offering, outcomes, process, evidence, CTA.
- Case study: challenge, intervention, system, artifacts, outcomes, reflection.
- Contact page: concise invitation, contact routes, timing expectations, light qualification.
- Journal or insights page: article index, tags, compact excerpt system.
- Team or studio page: point of view, leadership, working model, optional values.

### Page behavior rules
- Home page hero must communicate who IRIN is and who it is for within one screen.
- Product pages should define the operating problem before describing the offer.
- Case studies should show evidence and method, not only polished screens.
- Contact pages should feel welcoming but selective.
- Navigation labels should be literal enough to scan instantly.
- CTAs should be few, plainspoken, and context-appropriate.
- Reuse modules, but tune sequencing to page intent.

### Production checks
- Test on real mobile and desktop widths, not only artboards.
- Review dark mode only if supported intentionally; otherwise avoid accidental inverted states.
- Validate page speed, CLS, and contrast before release.
- Cross-check implemented spacing against the design system.
- Confirm analytics events do not compromise privacy or performance.

## Example (IRIN)
- Scenario: IRIN launches a productized studio offer page.
- Hero heading: "Product design and engineering, with precision built in." 
- Supporting line: "A focused studio for growth-stage teams that need senior craft without consultancy sprawl." 
- Primary CTA: "Start a conversation".
- Secondary CTA: "See recent work".
- Page structure: hero, operating problem, offer modules, proof, process, FAQ, contact.
- Visual behavior: restrained light background, dark text, one muted accent used for highlights only.
- Component note: navigation stays simple with Work, Services, Journal, Contact.
- Accessibility note: CTA contrast exceeds AA and focus rings are visible on all controls.
- Performance note: hero media is optimized and loads progressively without layout shift.

## Template (blank reusable block)
```md
Page name:
Template type:
Primary audience:
Primary objective:
Secondary objective:
Key message:
CTA 1:
CTA 2:
Sections in order:
Required components:
Breakpoint notes:
Accessibility checks:
Performance budget:
Media assets:
Analytics events:
Reviewer:
Approval date:
Release notes:
```
- Duplicate the block for each page or shared component.
- Add a component-by-component audit beneath breakpoint notes when revising an existing page.

## Common failure modes
- Designing the site like a deck, with too much text locked inside graphics.
- Using homepage copy that sounds like every digital studio.
- Letting hero sections become oversized mood boards without a clear proposition.
- Shipping interactive states without testing keyboard or focus behavior.
- Adding unnecessary libraries or scripts that slow the site down.
- Using tiny captions or labels that read well only on a designer's monitor.
- Reusing templates without adjusting message hierarchy to the page goal.

## How to avoid generic output
- Name the real operating tension the page is solving.
- Show method and proof, not only aesthetic polish.
- Keep copy plainspoken, exact, and editorial.
- Let structure do the persuasion; avoid inflated claims.
- Use system consistency as a marker of quality.
- Review every page against `../docs/03_quality-bar.md` and the identity docs before shipping.
- If a section could appear on any agency website unchanged, rewrite it with a sharper audience and point of view.
