# Print guidelines

## Purpose
- Define how the IRIN identity translates from screen to print without losing precision.
- Establish print production standards for stationery, leave-behinds, and premium collateral.
- Connect printed output back to `../identity/color-system.md`, `../identity/typography-system.md`, and `../docs/03_quality-bar.md`.
- Reduce risk in color conversion, trimming, and proofing.
- Keep printed materials minimal, tactile, and editorial rather than promotional.

## When to use
- Use when producing business cards, letterheads, envelopes, proposal covers, or event leave-behinds.
- Use when briefing a printer or preparing press-ready files.
- Use when adapting a digital composition into a printed format.
- Use when selecting paper stock or finish for an IRIN physical touchpoint.
- Use when approving press proofs or hard-copy mockups.
- Use alongside `../templates/design-qa-checklist.md` before releasing print-ready art.
- Do not use for environmental signage or packaging without an additional specification layer.

## Inputs
- Approved digital brand files, including the fixed wordmark asset.
- Exact document format and finished size.
- Printing process: digital, offset, or specialty spot-color production.
- Printer ICC profile or house recommendations when available.
- Paper stock options and finish constraints.
- Mailing or handling requirements for stationery pieces.
- Quantity, deadline, and shipping context.
- Reference to digital palette values in `../identity/color-system.md`.
- Accessibility or legibility requirements for small text.

## Outputs
- Press-ready PDF or equivalent production package.
- Documented CMYK and spot-color decisions derived from the digital palette.
- Clear bleed, trim, and safe-margin setup.
- Material specification for stock, finish, and special processes.
- A proofing record showing sign-off on color, text, and production details.
- Naming and version control aligned with the wider brand operating system.

## Owner
- Primary owner: Brand designer preparing production artwork.
- Production owner: Print vendor or studio operations lead.
- Final approver: Founder or brand steward for external-facing pieces.
- Color approval owner: Designer reviewing calibrated proofs.

## Quality criteria
### Print color management
- Start from the approved digital palette; never eyeball-print a new color family.
- Convert RGB brand colors to CMYK with printer profile awareness, then visually review proofs.
- For signature high-value pieces, define Pantone or spot equivalents where consistency matters more than cost.
- Record the chosen CMYK and spot mappings on the job ticket.
- Expect some deep digital colors to dull in CMYK; compensate through stock choice and contrast planning, not brand drift.
- Avoid large rich-black fields unless the printer confirms reliable output.
- Use overprint settings intentionally, never by accident.

### Paper and finish recommendations
| Use case | Recommended stock direction | Finish guidance |
| --- | --- | --- |
| Business card | Uncoated premium stock, 300-400 gsm | Soft-touch only if it improves handling |
| Letterhead | Uncoated text stock, 100-140 gsm | Keep finish subtle for writing and scanning |
| Envelope | Matching uncoated stock | Ensure address windows or print zones are tested |
| Proposal cover | Heavier uncoated or silk stock | Consider duplex or subtle texture if justified |
| Event leave-behind | Sturdy text or cover stock | Matte over gloss for editorial feel |

### Bleed, trim, and margins
- Default bleed: 3 mm on all sides unless the printer specifies otherwise.
- Minimum safe margin for text: 5 mm from trim, more for small formats.
- Align the wordmark with a structural margin, never optically floating near the edge.
- Avoid hairlines thinner than reliable print reproduction.
- If the format folds, account for panel creep and inside margins before final layout.
- Use print marks only when the printer requests them.

### Stationery specs
| Item | Finished size | Core layout notes |
| --- | --- | --- |
| Business card | 85 x 55 mm | Front: wordmark and role hierarchy; back optional minimal detail |
| Letterhead | A4 or US Letter by region | Generous top margin, light footer metadata |
| Envelope | DL or #10 by region | Return address placement must survive mailing automation |

### Business card rules
- Keep one side calmer than instinct suggests; restraint reads as confidence.
- Use Manrope only, with small text tested on proof at actual size.
- Do not crowd contact lines; better fewer fields than cramped hierarchy.
- If using a dark card, ensure edge wear and scuffing have been considered.
- QR codes are optional and should appear only when they serve a direct, current destination.

### Letterhead rules
- Keep the wordmark placement consistent across all templates.
- Contact metadata should be present but secondary.
- Test printed letterheads through a standard office printer if they will be overprinted later.
- Ensure digital PDF versions of the same letterhead remain readable on screen.

### Envelope rules
- Respect postal clear zones and addressing requirements.
- Avoid decorative back-flap elements that complicate production.
- Keep any lining or interior print extremely subtle.
- Test seal performance if heavier stocks are used.

### Proofing checklist
- Confirm document size, bleed, and trim are correct.
- Verify all fonts are embedded or outlined only when appropriate.
- Check black builds, tint percentages, and overprint settings.
- Read every line of text at 100 percent and on a physical proof.
- Compare proof color against approved references under neutral light.
- Inspect edges, spacing, and back/front alignment on duplex pieces.
- Confirm paper stock, finish, quantity, and delivery date in writing.

## Example (IRIN)
- Scenario: IRIN prints a founder business card and matching letterhead.
- Business card front: small approved wordmark upper-left, founder name and title lower-left, ample negative space.
- Business card back: optional URL only, centered or aligned to the front system.
- Stock: thick uncoated bright white with a smooth but not glossy finish.
- Palette behavior: dark graphite ink on warm white stock with one muted accent line if needed.
- Letterhead: wordmark at top with broad margin, body area largely open, metadata in a restrained footer.
- Why it fits: the materials feel designed, engineered, and warm without resorting to luxury clichés.

## Template (blank reusable block)
```md
Print item:
Finished size:
Quantity:
Print method:
Stock:
Finish:
Bleed:
Safe margin:
Front layout notes:
Back layout notes:
Color mapping notes:
Spot colors:
Special production notes:
Proof reviewer:
Approval date:
Vendor:
Delivery date:
File name:
```
- Add one block per print item and attach proof observations beneath color mapping notes.
- Keep vendor-specific instructions explicit rather than implied.

## Common failure modes
- Assuming screen colors will print accurately without conversion and proofing.
- Using coated stocks that make the brand feel colder than intended.
- Letting margins collapse on small formats.
- Choosing finishes because they sound premium rather than because they serve the piece.
- Forgetting postal or office-printer realities for stationery.
- Delivering files without clear production notes or color intent.
- Using the wordmark too large in an attempt to make the piece feel branded.

## How to avoid generic output
- Start from tactile intent: calm, precise, premium, useful.
- Let stock and spacing carry the sophistication.
- Keep copy sparse and exact.
- Choose printing methods that support restraint rather than spectacle.
- Validate with real proofs, not assumptions.
- Cross-check each item against `../docs/03_quality-bar.md` so material quality matches visual quality.
- If the piece feels like luxury-for-luxury's-sake, simplify it until it feels like IRIN again.
