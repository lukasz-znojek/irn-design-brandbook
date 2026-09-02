# IRIN Logo Guidelines

## Purpose
- Define how the fixed IRIN logo system is used across digital, print, product, and partnership contexts.
- Protect recognition, consistency, and perceived quality while the repository holds only written rules and not the production logo binaries.
- Give designers, developers, and external partners a practical standard before the real files are added under `/identity/assets/logo/`.

## When to use
- Use this document whenever the IRIN wordmark, symbol, favicon, app icon, social avatar, or a partner lockup is being placed.
- Use it before exporting marketing assets, presentation slides, web headers, proposals, pitch decks, social images, motion titles, or print collateral.
- Use it with `./typography-system.md`, `./spacing-grid-layout.md`, and `../docs/03_quality-bar.md` when judging whether a composition feels precise enough for the brand.
- Use it as the baseline for handing off logo files to product teams once binary assets are available.

## Inputs
- Approved IRIN logo files supplied by the founder and stored, when available, in `/identity/assets/logo/`.
- Context of use: screen, print, signage, social, app icon, browser favicon, motion title, or partner lockup.
- Placement surface details: dimensions, background color, contrast level, export format, and language locale.
- Associated brand elements: typography rules from `./typography-system.md`, color rules from `./color-system.md`, and spacing rules from `./spacing-grid-layout.md`.

## Outputs
- A correctly placed and exported IRIN logo instance with sufficient contrast, spacing, and size.
- A selected variant: full color, black, white, or mono, based on background and production constraints.
- A handoff-ready asset package whose filenames make variant, size, and format unambiguous.
- A layout that preserves the logo exactly as provided and avoids improvised redraws or effects.

## Owner
- Primary owner: Founder / Creative Director.
- Day-to-day stewards: Design lead and brand-facing product designers.
- Implementation partners: Marketing, web, product design, and any external production vendor.
- Approval for exceptions: Founder only.

## Quality criteria
- The logo matches the supplied master artwork exactly with no visual modification.
- Clearspace is preserved on all sides, including inside dense UI headers or sponsor walls.
- The variant chosen is legible at first glance on the intended background and medium.
- Minimum size rules are respected so counters, spacing, and stroke relationships do not collapse.
- Export naming is systematic enough that another team can identify the correct file without opening it.
- The result feels quiet, precise, and premium rather than loud, decorative, or startup-generic.

## Logo system overview
- The IRIN logo system consists of an existing wordmark and, where supplied, an optional supporting mark or symbol.
- In this repository, the mark is described only in usage terms because the binary source file is not yet present.
- Treat the wordmark as the primary identifier in most applications.
- Treat the optional mark as a secondary identifier for compact use cases such as avatars, favicons, app icons, embossed details, loading screens, and subtle footer signatures.
- The logo geometry itself is out of scope for this repository — it must be preserved exactly as provided.
- No one working from this file should attempt to redraw curves, adjust spacing, reinterpret terminals, or rebuild the symbol from memory.
- Once assets arrive, store source and exports under `/identity/assets/logo/` using the naming convention in this document.

## Protected elements
- Preserve the exact relationship between letterforms, spacing, symbol geometry, and alignment defined in the master asset.
- Do not detach the optional mark from its approved lockup unless a separate standalone asset has been provided.
- Do not recreate the wordmark by typing “IRIN” in Manrope or any other font; the logo is not a live-typed substitute.
- Preserve optical balance at small sizes by using official exports instead of self-scaled screenshots.
- Use vector source files for print and high-density digital contexts whenever possible.

## Clearspace rule
- Base clearspace unit: the cap-height of the “I” in the approved wordmark.
- Minimum clearspace on all four sides equals `1x`, where `x = cap-height of the “I”`, measured from the outermost visible edge of the logo artwork.
- In dense layouts, treat `1.5x` as the preferred clearspace target even if `1x` is the hard minimum.
- When pairing the wordmark with the optional mark in a supplied lockup, use the embedded spacing in the official file rather than re-measuring.
- When the logo sits near rules, cards, photos, browser edges, or partner marks, the clearspace still applies; background changes do not reduce it.
- If a container is too tight to honor the clearspace, reduce surrounding content density or increase the container size rather than shrinking the clearspace.

## Minimum size
| Context | Wordmark minimum | Optional mark minimum | Notes |
| --- | --- | --- | --- |
| Digital standard screens | 96 px width | 24 px square | Safe minimum for routine interface and web use |
| Digital compact UI | 72 px width | 20 px square | Use only when the logo is present but not the main focal element |
| Social avatar source art | 160 px export | 160 px export | Export large; platform crops unpredictably |
| Browser favicon source art | 32 px and 16 px outputs | 32 px and 16 px outputs | Use the approved standalone mark, not the full wordmark |
| Print stationery | 22 mm width | 6 mm square | Maintains legibility on quality paper stocks |
| Print small collateral | 18 mm width | 5 mm square | Absolute minimum; prefer larger |
| Signage / environmental | Scale proportionally | Scale proportionally | Judge from intended viewing distance, but never below print proportions |

## Color variants
- **Full color**: default hero variant for owned channels when the approved palette from `./color-system.md` supports strong contrast.
- **Black**: use on very light backgrounds, uncoated paper, embossing specs, or simple one-color production.
- **White**: use on dark solid fields, dark photography, or dark-mode application surfaces with tested contrast.
- **Mono**: use only when production or interface constraints require a single non-black, non-white brand color; this should still follow approved token values from `./color-system.md`.
- The logo should never be recolored ad hoc to “match” campaign art.
- If contrast is uncertain, fall back to black or white before inventing a tinted version.

## Background and contrast guidance
- Place the logo on calm, high-contrast surfaces first: solid neutrals, quiet gradients, or low-noise photographic areas.
- On photography, use a placement zone with stable luminance and low detail behind the logo.
- If the background is busy but unavoidable, introduce a disciplined container, crop change, or image darkening treatment rather than adding effects to the logo itself.
- As a rule of thumb, the logo should be instantly readable at one arm’s length on screen and at normal tabletop distance in print.
- Avoid situations where the logo and background are close in luminance even if the hues are technically different.

## Incorrect usage
- Do not rotate the logo.
- Do not stretch, condense, or distort its aspect ratio.
- Do not add a drop shadow, outer glow, bevel, blur, or texture.
- Do not recolor the logo outside approved variants.
- Do not outline the logo.
- Do not place it on low-contrast backgrounds.
- Do not place it on visually noisy or highly patterned areas without a controlled container.
- Do not crop the logo in normal identification use.
- Do not re-typeset the wordmark in Manrope or any other font.
- Do not redraw, simplify, sharpen, or “clean up” the symbol geometry.
- Do not add badges, slogans, frames, or decorative shapes that appear fused to the logo.
- Do not animate the logo with playful elastic motion or gimmick effects; see `./motion-principles.md`.

## Export file naming convention
- Use predictable filenames so internal and external teams can request the correct asset without ambiguity.
- Naming format:
  - `irin-logo-[lockup]-[variant]-[bg]-[size]-[format].[ext]`
  - `irin-mark-[variant]-[bg]-[size]-[format].[ext]`
- Recommended field meanings:
  - `lockup`: `wordmark`, `wordmark-mark`, `mark`
  - `variant`: `fullcolor`, `black`, `white`, `mono`
  - `bg`: `light`, `dark`, `transparent`
  - `size`: `16`, `32`, `96w`, `22mm`, `social-1024`
  - `format`: `svg`, `pdf`, `png`, `ico`
- Example filenames:
  - `irin-logo-wordmark-black-light-96w-svg.svg`
  - `irin-logo-wordmark-fullcolor-transparent-22mm-pdf.pdf`
  - `irin-mark-white-dark-32-png.png`
  - `irin-mark-black-transparent-social-1024-png.png`
- Keep master source files separate from exports:
  - `/identity/assets/logo/source/`
  - `/identity/assets/logo/export/`

## Lockup rules with partner logos
- Default relationship: IRIN and partner marks should align by visual center or cap-height, not by box edge alone.
- Use a thin divider rule only when a shared composition genuinely needs separation.
- Minimum spacing between IRIN and a partner logo should equal at least `2x` the IRIN clearspace unit.
- When logos differ greatly in visual density, size to optical balance rather than identical bounding-box height.
- IRIN should not be reduced to accommodate an oversized partner mark if that creates a weak, illegible presentation.
- If the partner logo is extremely complex, give both identities more white space rather than tightening the lockup.
- In sponsor walls, use monochrome treatments where contractually allowed to reduce visual noise.
- Do not place IRIN inside another brand’s holding shape.
- Do not merge the IRIN symbol into a co-branded chimera mark.

## Favicon and app-icon guidance
- Use the approved standalone mark if one exists; do not use the full wordmark as a favicon.
- Favicon outputs should be tested at 16 px, 32 px, and 48 px against light and dark browser chrome.
- App icons require a background container designed from the approved palette, not a squeezed wordmark.
- Prefer a simple field plus the approved mark, centered with generous internal padding.
- Avoid miniature typography, taglines, or fine keylines in app icon contexts.
- Export app icon source at large sizes first, then downsample with pixel-grid review.
- If the standalone mark does not survive at 16 px, commission a founder-approved small-size variant rather than improvising one.

## Production notes
- For SVG exports, keep shapes clean and avoid stray clipping masks.
- For print PDFs, outline fonts only if the source logo file depends on live type; otherwise preserve vector curves from the official artwork.
- For raster exports, use transparent backgrounds only when the placement context is controlled.
- Check anti-aliasing on dark-mode surfaces; a thin light fringe can cheapen the mark.
- Keep version control in filenames or folder metadata, not by renaming the logo itself in inconsistent ways.

## Example (IRIN)
- Scenario: IRIN homepage header on a light editorial layout.
- Asset used: `irin-logo-wordmark-black-light-96w-svg.svg`.
- Placement: top-left of a 12-column grid with the left edge aligned to the main content margin.
- Size: 112 px wide on desktop, 96 px on tablet, 88 px on mobile only if the navigation remains uncluttered.
- Clearspace: at least `1.5x` around the wordmark because it is a primary brand moment.
- Background: solid `Neutral-100` from the chosen palette in `./color-system.md`.
- Nearby elements: navigation in Manrope 14 px medium, separated by whitespace rather than a visible box.
- Result: precise, calm, recognisable, and consistent with a premium studio rather than a tech template.

## Template (blank reusable block)
```md
### Logo use case
- Context:
- Surface:
- Asset file:
- Variant:
- Width or size:
- Background condition:
- Clearspace used:
- Adjacent elements:
- Accessibility / contrast check:
- Reviewer:
- Approval status:
```

## Common failure modes
- Treating the wordmark as if it were just a text string.
- Shrinking the logo to solve layout crowding instead of fixing the layout.
- Choosing a full-color variant on an uncontrolled image background.
- Exporting a raster screenshot because the vector source was not easy to find.
- Allowing multiple nearly identical filenames to circulate with no clear “official” asset.
- Letting partner lockups become visually negotiated case by case with no optical rules.
- Using the logo as decoration rather than identification.

## How to avoid generic output
- Use restraint: one precise placement usually feels more premium than repeated branding.
- Let clearspace do the work; avoid surrounding the logo with noisy treatments to force attention.
- Prefer controlled backgrounds and disciplined sizing over “brand moments” built from effects.
- Cross-check every application against `./typography-system.md` and `./spacing-grid-layout.md` so the logo sits inside a complete system, not as a floating sticker.
- If a result feels interchangeable with a startup landing page template, simplify it until the composition feels more editorial and more deliberate.
