# IRIN Color System

## Purpose
- Define a strategic, option-based color framework for IRIN before a final founder-approved palette is locked.
- Give brand, product, and engineering teams a shared way to evaluate color direction in terms of tone, usability, accessibility, and production reality.
- Make color feel like a precision tool, not a decorative afterthought.

## When to use
- Use this document when selecting a core palette direction for the brand.
- Use it when creating UI themes, website pages, decks, proposals, diagrams, motion frames, and print collateral.
- Use it when testing accessibility or converting a brand palette into semantic design tokens.
- Use it with `./typography-system.md`, `./imagery-art-direction.md`, and `../docs/03_quality-bar.md` when evaluating whether a color choice still feels premium and editorial.

## Inputs
- Brand strategy: independent design-and-technology studio, premium, precise, warm-minimal, editorial.
- Functional needs: readable text, accessible UI states, light and dark mode, digital-to-print translation.
- Existing fixed brand constraints: Manrope as typeface and the founder-created logo geometry, described in `./logo-guidelines.md`.
- Founder preference signals and future decision logging in `../docs/02_decision-log.md`.

## Outputs
- Seven differentiated palette directions that can be discussed, compared, and tested.
- A clear recommendation for the strongest starting point.
- Practical rules for accessibility, neutral-scale extension, semantic states, dark mode, and print behavior.
- A reusable format for documenting future palette explorations without drifting into generic language.

## Owner
- Primary owner: Founder / Creative Director.
- Supporting owners: Brand design lead, product design lead, and front-end/design systems engineering.
- Accessibility review support: QA or design systems owner.
- Final approval: Founder.

## Quality criteria
- Each option is strategically distinct rather than a minor tint shift of the same idea.
- Core text and UI combinations can realistically meet WCAG 2.1 AA in routine use.
- The palette supports both editorial restraint and premium digital product execution.
- Neutral values remain strong enough for typography and interface structure.
- Accent use is disciplined; the palette should not depend on visual noise to feel premium.
- The recommendation is decisive, defensible, and explicitly pending founder approval.

## Accessibility approach
- IRIN should treat accessibility as a design quality requirement, not a compliance add-on.
- Practical WCAG 2.1 AA targets:
  - Body text: minimum 4.5:1 contrast ratio.
  - Large text: minimum 3:1 contrast ratio.
  - UI components and meaningful graphical objects: minimum 3:1 against adjacent colors.
- In day-to-day design, assume paragraph text, labels, and button text need the stricter 4.5:1 threshold unless they are clearly large-display text.
- Use contrast-ratio tools during palette evaluation and again during component implementation.
- Recommended workflow:
  - Check text on background for all default and hover states.
  - Check disabled or muted states separately; they fail more often than primary ones.
  - Check icons, dividers, and focus rings against their immediate surfaces, not against the page at large.
  - Re-test in dark mode and on production-calibrated displays.
- Rule of thumb for text-on-color combinations:
  - Near-black text on very light backgrounds is the safest default.
  - White text should sit on genuinely dark colors, not merely saturated ones.
  - Accent colors are usually better for fills, highlights, or borders than for long body text.
  - If a colored surface needs white text, darken the surface enough that readability is obvious without squinting.
  - If a palette only works when text is oversized, it is too fragile for a system role.

## Option-based decision: 7 palette directions

### Option A
#### 1. Concept name
**Precision Ink**

#### 2. Strategic intent
A deep navy-graphite system with one restrained warm metal accent. This direction feels engineered, editorial, and premium without becoming cold or generic enterprise blue.

#### 3. Palette values
| Role | HEX | Usage | Contrast note |
| --- | --- | --- | --- |
| Primary | #17324D | Main brand field, primary buttons, strong headings on light surfaces | White text is comfortably above 4.5:1 |
| Primary-Dark | #0C1A2B | Dark-mode base, hero bands, deep structural surfaces | White text is very high contrast |
| Secondary/Accent | #C98A2E | Highlights, key lines, restrained CTA accents, data emphasis | Use mostly with dark text; white text is not reliable for body copy |
| Neutral-900 | #11161C | Default near-black text and key UI labels | Strong on Neutral-100 |
| Neutral-700 | #38424D | Secondary text, dividers on light layouts | Safe for larger text and support copy on light backgrounds |
| Neutral-100 | #F5F2EC | Main light background with a soft editorial warmth | Use near-black text for best readability |
| Success | #1D6B52 | Positive status, confirmations, good-state charts | White text works on filled badges/buttons |
| Warning | #A66A12 | Caution states, restrained alerts | Use near-black text on pale tints; white text only on the dark base |
| Error | #A33A36 | Critical alerts and error emphasis | White text works on the base tone |
| Info | #2A668C | Informational surfaces and links where blue meaning helps | White text works on the base tone |

#### 4. Strengths
- Feels closest to IRIN’s “precision made visible” positioning.
- Supports editorial layouts, product UI, and premium proposals without palette drift.
- Warm accent adds humanity without softening the system too much.
- Works well with black-and-white photography and restrained motion.

#### 5. Risks/tradeoffs
- Could feel slightly conservative if the accent is underused.
- Requires discipline so the amber accent does not become ornamental “luxury” styling.
- Teams may default too heavily to navy unless usage ratios are defined.

#### 6. Best-use scenarios
- Core website and product marketing foundation.
- Case studies and proposal documents requiring authority and clarity.
- Product UI where trust, precision, and premium restraint matter.

### Option B
#### 1. Concept name
**Signal Foundry**

#### 2. Strategic intent
A dark neutral system energized by amber-rust signals. This direction leans warmer and more differentiated than default consultancy palettes while still reading as serious and crafted.

#### 3. Palette values
| Role | HEX | Usage | Contrast note |
| --- | --- | --- | --- |
| Primary | #3B2A21 | Main dark brand anchor, headers, deep text accents | White text is safely readable |
| Primary-Dark | #1F130F | Deep backdrop, dark-mode surfaces, footer fields | White text is very high contrast |
| Secondary/Accent | #D47A1F | Calls to attention, controlled highlight lines, active tags | Use near-black text on light tints; base accent is better as fill with dark text |
| Neutral-900 | #181311 | Default text on light surfaces | Strong on Neutral-100 |
| Neutral-700 | #4E433D | Secondary text, quieter metadata | Works for larger text on light backgrounds |
| Neutral-100 | #F7F0E8 | Warm paper-like background | Near-black text strongly recommended |
| Success | #2E7A58 | Positive states | White text works on the base tone |
| Warning | #B95C15 | Warnings and pending states | Use near-black text on light tints |
| Error | #B1412E | Errors, destructive emphasis | White text works on the base tone |
| Info | #4A6F8F | Informational notes, links, charts | White text works on the base tone |

#### 4. Strengths
- Strong editorial warmth without slipping into lifestyle branding.
- Distinctive against the sea of blue-heavy B2B palettes.
- Excellent for materials, print, and proposal environments.
- Can make interface highlights feel more intentional and crafted.

#### 5. Risks/tradeoffs
- Warmth can drift toward rustic if the neutral system is not kept sharp.
- Requires careful image grading to avoid muddy combinations.
- Less obviously “digital product” than cooler options.

#### 6. Best-use scenarios
- Brand-led website pages and founder-led thought leadership pieces.
- Proposal documents and case-study narratives.
- Print applications where paper warmth can work in the palette’s favor.

### Option C
#### 1. Concept name
**Verdant Systems**

#### 2. Strategic intent
A deep forest-tech direction that blends rigor with a subtle sense of growth and stewardship. It feels modern and premium without using default fintech blue.

#### 3. Palette values
| Role | HEX | Usage | Contrast note |
| --- | --- | --- | --- |
| Primary | #174C43 | Primary brand color, buttons, navigation emphasis | White text is comfortably readable |
| Primary-Dark | #0B2723 | Dark surfaces, dark mode, deep headers | White text is very high contrast |
| Secondary/Accent | #8EA63A | Accent, data highlights, subtle environmental warmth | Use near-black text; white text is not dependable for small copy |
| Neutral-900 | #121816 | Main near-black text | Strong on Neutral-100 |
| Neutral-700 | #3D4B47 | Secondary text, rules, subdued labels | Works for larger text on light surfaces |
| Neutral-100 | #EFF3EE | Light base with a cool natural cast | Near-black text recommended |
| Success | #1F7F5A | Success and health indicators | White text works |
| Warning | #9A7414 | Warning states | Use near-black text on lighter tints |
| Error | #9F3D48 | Error states | White text works |
| Info | #2B6D73 | Informational emphasis | White text works |

#### 4. Strengths
- Distinctive, credible, and less overused than blue.
- Suggests growth and systems thinking without obvious “green company” clichés.
- Works well with material and documentary imagery.
- Feels premium in both product and editorial contexts.

#### 5. Risks/tradeoffs
- Some audiences may read green as sustainability-first unless messaging stays clear.
- Accent greens can turn soft if too many light tints are used.
- Requires careful semantic separation between brand green and success green.

#### 6. Best-use scenarios
- Product positioning that emphasizes long-term systems and thoughtful build quality.
- Case studies with strong operational transformation narratives.
- Editorial content paired with architectural or material photography.

### Option D
#### 1. Concept name
**Ultraviolet Edge**

#### 2. Strategic intent
A high-clarity indigo-violet system for a more digitally assertive expression. This is the boldest route while still retaining seriousness through dark neutrals and disciplined use.

#### 3. Palette values
| Role | HEX | Usage | Contrast note |
| --- | --- | --- | --- |
| Primary | #3C2FA8 | Primary buttons, standout brand moments, digital product emphasis | White text is readable on the base tone |
| Primary-Dark | #1A1447 | Dark hero surfaces, footers, dark mode | White text is very high contrast |
| Secondary/Accent | #8A52E3 | Accent lines, active states, controlled motion highlights | White text is weaker here; use near-black or the dark base |
| Neutral-900 | #13131B | Main text color | Strong on Neutral-100 |
| Neutral-700 | #464859 | Secondary text and structure | Works for support text on light backgrounds |
| Neutral-100 | #F2F1F8 | Cool pale base | Near-black text recommended |
| Success | #1B7B67 | Success states | White text works |
| Warning | #B57A18 | Warning states | Near-black text on tints; white on deep variants |
| Error | #B03957 | Error states | White text works |
| Info | #355FC9 | Info states, links, chart lines | White text works |

#### 4. Strengths
- More unmistakably digital than the warmer options.
- Strong for product launches, demos, and motion-led web moments.
- Indigo base remains serious enough to avoid playful startup energy if used sparingly.
- Distinctive in competitive markets crowded with plain navy brands.

#### 5. Risks/tradeoffs
- Can feel trend-led if gradients or secondary violets are overused.
- Easier to push into “AI startup” cliché than other directions.
- Demands more discipline in imagery and motion to stay premium.

#### 6. Best-use scenarios
- Product-first web experiences and launch campaigns.
- Dark-mode interfaces with high visual precision.
- Interactive demos where a stronger digital tone is helpful.

### Option E
#### 1. Concept name
**Warm Graphite**

#### 2. Strategic intent
A near-monochrome base with one vivid coral accent. This route is the most editorial and understated, letting composition and typography carry most of the brand expression.

#### 3. Palette values
| Role | HEX | Usage | Contrast note |
| --- | --- | --- | --- |
| Primary | #2C2927 | Primary dark, headings, key surfaces | White text is safely readable |
| Primary-Dark | #151311 | Deepest structural surface | White text is very high contrast |
| Secondary/Accent | #D95C4A | Accent buttons, links, callouts, micro-highlights | White text is marginal for small text; prefer near-black or dark base |
| Neutral-900 | #161412 | Default text | Strong on Neutral-100 |
| Neutral-700 | #56504C | Secondary text, dividers, supporting structure | Good for larger text and utility elements |
| Neutral-100 | #F4F0EB | Soft paper-like background | Near-black text recommended |
| Success | #2B7C63 | Success states | White text works |
| Warning | #AD6E21 | Warning states | Near-black text on tints recommended |
| Error | #A33E48 | Error states | White text works |
| Info | #4D6E86 | Informational states | White text works |

#### 4. Strengths
- Feels highly editorial, calm, and premium.
- Gives typography and layout maximum room to lead.
- Excellent for print and understated website systems.
- Distinct without depending on saturated color.

#### 5. Risks/tradeoffs
- Could feel too quiet for product marketing if the accent is not used with intent.
- Teams may mistake restraint for lack of system and begin improvising colors.
- Coral accent needs tight control to avoid consumer-lifestyle associations.

#### 6. Best-use scenarios
- Founder notes, essays, and proposal decks.
- Portfolio or case-study presentations emphasizing craft.
- Minimal website surfaces where imagery and typography carry most of the weight.

### Option F
#### 1. Concept name
**Cold Precision**

#### 2. Strategic intent
A steel-blue grey palette designed for product trust, interface rigor, and almost clinical clarity. This is the coolest, most operationally precise direction in the set.

#### 3. Palette values
| Role | HEX | Usage | Contrast note |
| --- | --- | --- | --- |
| Primary | #24475D | Primary buttons, system headers, control emphasis | White text is readable on the base tone |
| Primary-Dark | #102331 | Dark surfaces and high-contrast anchors | White text is very high contrast |
| Secondary/Accent | #5FA3C7 | Highlight strokes, charts, data accents, active filters | Use near-black text; white text is not strong enough for small copy |
| Neutral-900 | #0F151A | Default text | Strong on Neutral-100 |
| Neutral-700 | #465761 | Secondary text and structural UI lines | Works for support copy on light backgrounds |
| Neutral-100 | #EFF4F6 | Cool light background | Near-black text recommended |
| Success | #1E7A70 | Success states | White text works |
| Warning | #A87119 | Warning states | Near-black text on pale tints recommended |
| Error | #B04343 | Error states | White text works |
| Info | #2E6FA3 | Informational states and links | White text works |

#### 4. Strengths
- Excellent for product UIs, dashboards, and technical service positioning.
- Very clear hierarchy in light and dark surfaces.
- Feels modern and exact without relying on trend-heavy saturation.
- Easy to extend into data visualization and component systems.

#### 5. Risks/tradeoffs
- Can feel emotionally distant if paired with overly sterile imagery.
- Less distinctive than warmer options in print collateral.
- Accent blue-cyan may read slightly conventional in some tech contexts.

#### 6. Best-use scenarios
- Product interface foundation and systems-heavy marketing.
- Technical documentation and platform screenshots.
- Dark-mode product environments needing disciplined contrast.

### Option G
#### 1. Concept name
**Terracotta Studio**

#### 2. Strategic intent
A clay-led editorial palette with grounded warmth and crafted authority. This is the most boutique and tactile option, well suited to a studio identity that wants a stronger human-artifact feel.

#### 3. Palette values
| Role | HEX | Usage | Contrast note |
| --- | --- | --- | --- |
| Primary | #7A3F2B | Main brand anchor, buttons, section bands | White text is readable on the base tone |
| Primary-Dark | #3A1D16 | Deep surfaces, footer, dark mode accents | White text is very high contrast |
| Secondary/Accent | #C48D5B | Accent highlights, supporting details, diagrams | Use near-black text; white text is not dependable for small text |
| Neutral-900 | #1A1411 | Main text color | Strong on Neutral-100 |
| Neutral-700 | #5E4D43 | Secondary text and lines | Works for larger text and quiet support copy |
| Neutral-100 | #F6EFE8 | Light background with warm paper character | Near-black text recommended |
| Success | #2F7859 | Success states | White text works |
| Warning | #B56A22 | Warning states | Near-black text on tints recommended |
| Error | #AB4238 | Error states | White text works |
| Info | #506D7E | Informational states | White text works |

#### 4. Strengths
- Memorable and tactile compared with standard digital-studio palettes.
- Strong fit for editorial storytelling, printed matter, and founder-led brand expression.
- Warmth can make the studio feel approachable without becoming casual.
- Works beautifully with paper textures, architecture, and material-detail imagery.

#### 5. Risks/tradeoffs
- The least “default digital” of the set, which may divide opinions internally.
- Requires very careful product UI translation to avoid feeling too artisanal.
- Could overpower subtle logo use if applied too broadly.

#### 6. Best-use scenarios
- Brand storytelling, publications, and case studies.
- Printed collateral, proposal decks, and selective campaign moments.
- Studio environments where IRIN wants more human warmth and craft presence.

## Feedback block template
```
Choose: [A/B/C/D/E/F/G]
Keep from this option: …
Change: …
Confidence: low/medium/high
```

## Recommendation
- Recommended starting point: **Option A — Precision Ink**.
- Why this option wins now:
  - It best balances IRIN’s three core tensions: premium but not flashy, technical but not sterile, and editorial but still digital-product credible.
  - The dark ink base supports excellent typography, disciplined UI, and consistent logo application.
  - The warm accent introduces distinction without turning the identity into a trend-based luxury palette.
  - It is the easiest option to extend into a full digital system while still feeling boutique in proposals and case studies.
- What this recommendation is not:
  - It is not final brand law.
  - It is not a claim that other options are weaker in all contexts.
- Decision status:
  - Treat Option A as the default working palette until founder approval is recorded in `../docs/02_decision-log.md`.

## Recommended usage ratios for Option A
- Neutral and near-black values should carry most of the system.
- Suggested starting ratio:
  - 65-75% light neutrals and surfaces.
  - 15-20% dark structural colors.
  - 5-10% accent and semantic colors combined.
- This ratio preserves restraint and prevents the palette from feeling over-designed.
- Accent should behave like punctuation, not wallpaper.

## Semantic and neutral color scale guidance
### Extending a chosen option into a 10-step neutral scale
- Start from the option’s `Neutral-900` and `Neutral-100` anchors.
- Build a 10-step scale for implementation tokens such as `Neutral-0` through `Neutral-900` or `Neutral-50` through `Neutral-950`.
- Suggested behavior of the scale:
  - Lightest steps: page backgrounds, cards, subtle chips, table fills.
  - Middle steps: borders, dividers, disabled states, quiet labels.
  - Dark steps: headings, body text, inverse surfaces.
- Do not interpolate mechanically without visual review; warm and cool neutrals can drift muddy if generated blindly.
- Review the scale in both pure text contexts and component states.
- A practical 10-step pattern:
  - Step 1: pure or almost pure background.
  - Step 2: alternate surface.
  - Step 3: raised card surface.
  - Step 4: subtle border fill / hover tint.
  - Step 5: divider and disabled field line.
  - Step 6: muted text.
  - Step 7: secondary text.
  - Step 8: tertiary heading or icon on light backgrounds.
  - Step 9: primary text.
  - Step 10: deepest inverse surface.

### Extending semantic colors
- Keep semantic colors function-first, brand-second.
- Success, warning, error, and info should each have at least:
  - a dark base tone for filled components,
  - a mid tone for strokes and icons,
  - a pale tint for backgrounds or banners.
- Do not overload the brand accent as a substitute for warning or success semantics.
- Where the brand primary is close to info blue or success green, preserve clear naming and role separation in tokens.
- Example token structure:
  - `success-100`, `success-500`, `success-700`
  - `warning-100`, `warning-500`, `warning-700`
  - `error-100`, `error-500`, `error-700`
  - `info-100`, `info-500`, `info-700`

### Accent discipline
- A premium system usually uses less accent than teams expect.
- Reserve accent for:
  - CTA emphasis,
  - key active states,
  - chart highlight,
  - selected navigation state,
  - small editorial signal moments.
- Avoid full-page accent backgrounds unless the tone is dark enough and the content importance warrants it.
- If everything is accented, nothing is prioritized.

## Digital vs print behavior
### Digital guidance
- Use HEX or RGB tokens as the source of truth for interface and web implementation.
- Test color on calibrated displays and at common brightness levels.
- Remember that pale neutrals can appear cooler or flatter on low-quality panels.
- Always validate hover, focus, pressed, and disabled states, not only default states.

### Print guidance
- Do not assume screen colors will reproduce faithfully in CMYK.
- Dark navies and deep greens can flatten or shift in print if converted casually.
- Warm accent tones may dull significantly on uncoated stocks.
- For high-value print pieces, create print-adjusted values after proof review rather than using untested automatic conversions.
- If a single signature ink is strategically important, consider a spot color for the primary or accent tone in premium collateral.
- Keep rich black recipes and overprint behavior under production review; do not fake brand depth with unsafe print settings.

### Material and finish considerations
- Uncoated paper will mute saturation and increase tactile warmth.
- Coated stocks preserve contrast but can feel less editorial.
- Foil, emboss, or deboss accents should remain minimal; the palette already communicates premium quality without layered gimmicks.
- If print finishing is introduced, test it against the logo constraints in `./logo-guidelines.md`.

## Dark-mode guidance
- Dark mode should feel like a designed extension of the system, not a simple inversion.
- Use `Primary-Dark` or a related deep structural tone as the base, then layer neutral steps upward for text and surfaces.
- Avoid using pure black unless a product context truly benefits; deep near-black tones usually feel more premium.
- Preserve a hierarchy of surfaces even in dark mode so cards and panels remain distinguishable.
- Reduce accent spread in dark mode; small bright accents become much louder against dark fields.
- Re-test semantic colors in dark mode because apparent contrast shifts dramatically.
- Do not let white text become the only dark-mode option; use off-white neutrals to reduce glare where appropriate.

## Applying the recommendation to real UI behavior
### Button guidance with Option A
- Primary button fill: `#17324D`.
- Primary button text: white.
- Hover state: darken toward `#0C1A2B` or increase surface depth slightly without dramatic saturation change.
- Secondary button: light neutral background with `#11161C` text and `#38424D` border.
- Accent-only button use should be rare; the amber accent is better as a highlight within a primary-dark system than as the main surface on every CTA.

### Link and emphasis guidance with Option A
- Default body links can use `#17324D` on `#F5F2EC` if underlines or weight support is present.
- Micro-emphasis within text can use the amber accent only for short callouts, labels, or indicators.
- Avoid setting long paragraphs in accent color.

### Editorial layout guidance with Option A
- Use the warm light neutral for most reading surfaces.
- Introduce dark bands sparingly for section transitions or proof moments.
- Keep accent concentrated in lines, tags, bullets, or key UI interaction states.

## Example (IRIN)
- Scenario: IRIN website primary CTA on a light editorial hero using the recommended Option A.
- Background: `Neutral-100` = `#F5F2EC`.
- Heading and body text: `Neutral-900` = `#11161C`.
- Primary CTA fill: `Primary` = `#17324D`.
- Primary CTA label: `#FFFFFF`.
- Supporting micro-accent: `Secondary/Accent` = `#C98A2E` used only as a 2 px underline under a small overline label.
- Contrast reasoning:
  - `#11161C` on `#F5F2EC` is a very dark-on-light pairing and comfortably exceeds 4.5:1 for body text.
  - White on `#17324D` is a clearly dark-fill pairing and comfortably exceeds 4.5:1 for button text.
  - The amber accent is not used for long text, avoiding a likely contrast failure.
- Result: the UI feels premium, controlled, and legible, with warmth appearing as a precise signal rather than as broad decoration.

## Template (blank reusable block)
```md
### Option [letter]
#### 1. Concept name
[Name]

#### 2. Strategic intent
[One to two lines]

#### 3. Palette values
| Role | HEX | Usage | Contrast note |
| --- | --- | --- | --- |
| Primary |  |  |  |
| Primary-Dark |  |  |  |
| Secondary/Accent |  |  |  |
| Neutral-900 |  |  |  |
| Neutral-700 |  |  |  |
| Neutral-100 |  |  |  |
| Success |  |  |  |
| Warning |  |  |  |
| Error |  |  |  |
| Info |  |  |  |

#### 4. Strengths
- 
- 
- 

#### 5. Risks/tradeoffs
- 
- 
- 

#### 6. Best-use scenarios
- 
- 
- 
```

## Common failure modes
- Treating palette exploration as a search for a “favorite color” instead of a system choice.
- Choosing a palette that looks striking in a hero shot but collapses in product UI.
- Ignoring contrast until after marketing art is approved.
- Overusing accent colors because the neutral system feels too subtle.
- Confusing brand color roles with semantic UI states.
- Assuming digital values will translate directly into print without proofing.
- Letting dark mode become a crude inversion.
- Failing to record the approved choice and forcing teams to guess.

## How to avoid generic output
- Start from brand behavior—precision, warmth, editorial restraint—not from trend colors.
- Judge each option across typography, UI, imagery, and print, not as isolated swatches.
- Favor palettes that become more interesting in use, not only in presentation tables.
- Keep accent rare enough that it means something.
- If a palette would fit equally well for any generic startup landing page, it is not specific enough for IRIN.
