# Design QA checklist

## Purpose
- Provide a literal pass/fail checklist for reviewing IRIN design outputs before release.
- Make visual QA consistent across web, social, decks, print, and internal materials.
- Protect critical brand constants such as the fixed wordmark, Manrope-only typography, and color accuracy.
- Ensure accessibility and export details are checked before work leaves the studio.
- Support sign-off with clear reviewer, date, and status fields.

## When to use
- Use before publishing any client-facing or public-facing IRIN asset.
- Use before sharing design work with a printer, developer, or external collaborator.
- Use when reviewing deck slides, social graphics, page mocks, or print-ready files.
- Use after revisions, not only before first release.
- Use alongside `../applications/social-templates.md`, `../applications/website-guidelines.md`, `../applications/presentation-template.md`, and `../applications/print-guidelines.md` as needed.
- Use as a standalone working checklist during live reviews.

## Inputs
- The final or near-final design file.
- Approved brand references for color, typography, and logo usage.
- Intended output context: web, social, deck, print, or internal doc.
- Accessibility expectations, including contrast baseline.
- Export specs and naming convention for the asset type.
- Reviewer name and release date.

## Outputs
- A marked pass/fail checklist with notes.
- A clear release status for the asset.
- A sign-off record including reviewer and date.
- A list of corrective actions if the asset does not pass.
- Higher confidence that the asset matches IRIN standards before handoff or publication.

## Owner
- Primary owner: Designer or reviewer running the QA pass.
- Final approver: Brand lead, founder, or project owner depending on visibility.
- Remediation owner: Asset creator unless otherwise assigned.

## Quality criteria
### Checklist metadata
- Asset name:
- Asset type:
- Channel or destination:
- File name:
- Reviewer:
- Review date:
- Release date:
- Status: Pass / Pass with changes / Fail

### Logo usage
- [ ] Fixed IRIN wordmark used only from approved source file.
- [ ] Wordmark has not been redrawn, stretched, compressed, or retyped.
- [ ] Clear space around the wordmark is respected.
- [ ] Wordmark scale is appropriate for the format.
- [ ] No unapproved lockups, outlines, shadows, or effects are applied.
- [ ] Logo placement supports hierarchy instead of dominating it.

### Color accuracy
- [ ] Hex values match the approved palette from `../identity/color-system.md`.
- [ ] Accent colors are used sparingly and intentionally.
- [ ] Contrast for text and essential UI meets WCAG AA where applicable.
- [ ] Gradient or texture use does not introduce visible banding or muddy color.
- [ ] Dark and light surfaces preserve legibility.
- [ ] Print jobs include documented CMYK or spot conversions where required.

### Typography
- [ ] Manrope is the only typeface used unless a justified exception is documented.
- [ ] Type weights are consistent with the approved hierarchy.
- [ ] Type sizes fit the medium and remain legible at real viewing size.
- [ ] Line length and line spacing support comfortable reading.
- [ ] No orphaned lines, awkward breaks, or accidental widows remain in key copy.
- [ ] Typographic emphasis is created through hierarchy, not random styling.

### Spacing and grid adherence
- [ ] Layout aligns to the intended grid or structural spacing system.
- [ ] Margins are consistent and visually calm.
- [ ] Negative space is preserved; the layout does not feel crowded.
- [ ] Alignment between text, media, and dividers is precise.
- [ ] Repeated modules use consistent spacing rules.
- [ ] Safe zones are respected for platform-specific or print-specific formats.

### Accessibility
- [ ] Text contrast passes the required baseline.
- [ ] Important meaning is not carried by color alone.
- [ ] Interactive states are visible for web or prototype outputs.
- [ ] Alt text or accessibility notes are prepared where needed.
- [ ] Text embedded in graphics remains readable on likely devices.
- [ ] Motion, if present, does not compromise comprehension or control.

### Content and accuracy
- [ ] Names, dates, URLs, and metrics are correct.
- [ ] Tone sounds specific to IRIN and avoids generic agency language.
- [ ] CTA, if present, is appropriate to the asset and channel.
- [ ] Required legal, confidentiality, or source notes are included.
- [ ] Copy has been proofread at final size.
- [ ] Supporting facts or claims have a source owner.

### File naming and export specs
- [ ] File name follows project and channel naming conventions.
- [ ] Export dimensions or document size match the destination requirements.
- [ ] File format is appropriate: PNG, JPG, PDF, SVG, or source file as needed.
- [ ] Compression is balanced with visible quality.
- [ ] Fonts, links, and images are embedded or packaged correctly when required.
- [ ] Version shared externally matches the approved internal version.

### Sign-off block
- Reviewer:
- Role:
- Review date:
- Final status:
- Changes required:
- Approval comment:
- Release owner:

## Example (IRIN)
- Asset name: LinkedIn launch card for new service page.
- Asset type: Social graphic.
- Reviewer: Brand design lead.
- Status: Pass with changes.
- Findings: hex values are correct, Manrope is used correctly, and spacing is strong.
- Required changes: shorten caption line on artwork and strengthen alt text specificity.
- Why it fits: the checklist catches practical refinements without reopening the whole concept.

## Template (blank reusable block)
```md
Asset name:
Asset type:
Channel or destination:
File name:
Reviewer:
Review date:
Release date:
Status:

Logo usage
- [ ]
- [ ]
- [ ]

Color accuracy
- [ ]
- [ ]
- [ ]

Typography
- [ ]
- [ ]
- [ ]

Spacing and grid adherence
- [ ]
- [ ]
- [ ]

Accessibility
- [ ]
- [ ]
- [ ]

Content and accuracy
- [ ]
- [ ]
- [ ]

File naming and export specs
- [ ]
- [ ]
- [ ]

Sign-off
- Reviewer:
- Date:
- Status:
- Notes:
```
- Keep the blank block with the asset until sign-off is complete.
- Add extra checklist items only when the medium truly requires them.

## Common failure modes
- Treating QA as a quick visual glance.
- Checking styling but not accuracy.
- Using the checklist once and then skipping it after revisions.
- Failing assets for personal taste instead of explicit standards.
- Ignoring file naming or export settings because the design looks correct.
- Marking accessibility as passed without an actual contrast or interaction review.

## How to avoid generic output
- Use the checklist as a decision tool, not a ritual.
- Tie every pass/fail note to a real IRIN standard.
- Document why an item failed so the fix is obvious.
- Keep the review calm, precise, and evidence-based.
- Re-run the checklist after material changes.
- Use `../docs/03_quality-bar.md` as the standard of finish behind every checkbox.
- If the review comments could apply to any brand file without specifics, the QA pass is too shallow.
