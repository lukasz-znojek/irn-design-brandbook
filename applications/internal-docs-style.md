# Internal docs style

## Purpose
- Set a consistent style for IRIN internal documents such as proposals, statements of work, and internal wikis.
- Make internal materials feel disciplined and readable without over-branding routine work.
- Keep internal writing aligned with external identity while allowing more operational directness.
- Support reuse across docs, decks, and project workstreams by referencing `../docs/03_quality-bar.md` and related templates.
- Ensure internal artifacts are easy to scan, maintain, and hand off.

## When to use
- Use for proposals, scopes of work, workshop notes, decision logs, and internal wiki pages.
- Use when creating reusable operating docs for design, engineering, or delivery teams.
- Use when transforming rough notes into durable internal knowledge.
- Use when briefing collaborators who need to write in the IRIN house style.
- Use alongside `../applications/presentation-template.md` when a deck is derived from a document.
- Use alongside `../templates/creative-brief-template.md` and `../templates/campaign-brief-template.md` when those files are filled out.
- Do not use as a reason to over-polish disposable notes that do not need archival value.

## Inputs
- Document purpose and audience.
- Source material such as meeting notes, project plans, or prior briefs.
- Required headings and any contractual clauses if relevant.
- Naming and storage conventions for the project or workspace.
- Links to related artifacts that the document should reference.
- Reviewers and approval expectations.
- Sensitivity level or confidentiality context.

## Outputs
- A clearly structured document with predictable heading hierarchy.
- Readable tables, callouts, and links that support action rather than clutter.
- File names that sort cleanly and indicate status or date where needed.
- Tone calibrated for internal clarity while staying recognizably IRIN.
- A reusable document that can become a system asset rather than a dead file.

## Owner
- Primary owner: Document author closest to the work.
- Structural owner: Team lead or operations lead maintaining consistency.
- Final approver: Project owner, founder, or designated reviewer depending on sensitivity.
- Archive owner: Operations or knowledge-management owner.

## Quality criteria
### Heading hierarchy
- Use a single H1 for the document title.
- Use H2 for major sections that reflect the decision or work structure.
- Use H3 for subtopics or repeated subsections.
- Avoid descending beyond H4 unless the document is genuinely complex.
- Keep headings descriptive; a heading should preview what follows.
- Prefer sentence case over title case unless the format requires otherwise.

### Paragraph and list style
- Lead paragraphs with the point, then support it.
- Keep paragraphs short enough to scan in a shared workspace.
- Use bullets for options, decisions, assumptions, and actions.
- Use numbered lists for sequences, workflows, or approval steps.
- Avoid nested bullets deeper than two levels when possible.
- Use bold sparingly to highlight labels, not to simulate emphasis everywhere.

### Table style
| Use case | Guidance | Notes |
| --- | --- | --- |
| Comparison table | Keep dimensions explicit | Good for vendor or option reviews |
| Timeline table | Include owner and date columns | Avoid ambiguous status labels |
| Scope table | Use in SOWs for in/out boundaries | Pair with assumptions |
| Risk table | Likelihood, impact, mitigation | Update as the work changes |

### Callout and admonition style
- Use blockquotes or labeled callouts for decision, risk, note, or action.
- Keep callout labels literal: Decision, Risk, Constraint, Action, Open question.
- Do not create decorative admonitions with multiple emoji or visual noise.
- Reserve high-emphasis callouts for genuinely important items.
- Pair each action callout with an owner and timing note where possible.

### File naming
- Use lowercase kebab-case for file names.
- Front-load meaning before dates when the document will live in a shared folder.
- Add date in ISO format when chronology matters: `2026-09-scope-review.md`.
- Add version suffixes only when needed for explicit external circulation.
- Avoid names such as `final-final-v2` or `notes-new`.
- Keep related documents grouped by folder rather than by cryptic abbreviations.

### Tone differences vs external communications
- Internal documents can be more operational and less polished than public copy.
- External-facing flourish should give way to clarity, ownership, and decision traceability.
- It is acceptable to be direct about risks, ambiguity, or tradeoffs.
- Avoid marketing language in internal docs unless the document is a marketing artifact.
- Keep confidence calm; do not write internal memos like a pitch deck.

### Structural recommendations by document type
- Proposal: context, objective, scope, approach, timeline, investment, assumptions, next steps.
- SOW: project summary, deliverables, included work, excluded work, timeline, dependencies, approvals, commercial terms.
- Wiki page: purpose, current state, decisions, workflows, references, open questions.
- Decision log: decision, date, owner, rationale, alternatives considered, downstream impact.
- Workshop notes: agenda, participants, notes, decisions, actions, follow-ups.

### Readability and maintenance checks
- Every document should show who owns it and when it was last materially updated.
- Broken links should be fixed immediately during maintenance passes.
- Avoid screenshots of text when selectable text will do.
- Highlight what changed when circulating a revision-heavy document.
- Archive stale documents rather than letting them silently rot.

### Recommended metadata block
- Include owner, date, and status near the top for live working docs.
- Mark confidential documents clearly but quietly.
- Add a short summary line when the document is longer than three screens.
- Show linked source artifacts so a reader can verify context quickly.
- If a doc replaces an earlier one, link the prior version or archive location.

## Example (IRIN)
- Scenario: IRIN drafts a statement of work for a product redesign and engineering support engagement.
- H1: `Product redesign and implementation SOW`.
- H2 sections: objective, scope, deliverables, working model, dependencies, timeline, approvals.
- Scope table lists included and excluded activities side by side.
- A risk callout identifies dependency on client-side analytics access.
- Tone remains direct, practical, and specific about responsibilities.
- File name example: `irin-client-a-product-redesign-sow-2026-09.md`.
- Why it fits: the document is clean, clear, and operational without sounding generic or bureaucratic.
- Internal wiki variant: a design-system note might open with purpose, decision, implementation rules, and change log.
- Proposal variant: the opening section can frame opportunity, desired outcome, and recommended path in under one page.
- Review behavior: action items are easy to scan because labels, owners, and dates are explicit.

## Template (blank reusable block)
```md
Document title:
Document type:
Audience:
Owner:
Last updated:
Purpose:
Decision or outcome sought:
Required sections:
Related links:
Risks or constraints:
Reviewers:
Approval path:
File name:
Notes:
```
- Add the block at the planning stage before writing the document body.
- Expand required sections into H2 headings before drafting prose.
- Add status and confidentiality lines above the main body if the document needs them.
- Add a change log under notes when the file is expected to evolve over multiple reviews.

## Common failure modes
- Writing internal docs like polished brochures.
- Hiding decisions inside long paragraphs.
- Using inconsistent heading patterns across similar documents.
- Creating tables with no clear purpose or update owner.
- Naming files so vaguely that retrieval becomes guesswork.
- Letting wiki pages accumulate stale process information.
- Avoiding direct language about constraints because it feels impolite.
- Treating metadata like owner and date as optional.
- Copying a past document structure without checking whether it fits the current decision.

## How to avoid generic output
- Start from the operating need of the document.
- State ownership, decisions, and dependencies explicitly.
- Use formatting to support action, not aesthetics alone.
- Make the tone warmer than bureaucracy but firmer than casual chat.
- Reuse structures that have earned trust inside the studio.
- Compare major documents against `../docs/03_quality-bar.md` before circulation.
- If the document could belong to any consultancy, sharpen the project specifics and ownership cues.
- Use the opening lines to signal the exact decision, recommendation, or operating need.
- Favor active verbs and named owners over soft collective phrasing.
