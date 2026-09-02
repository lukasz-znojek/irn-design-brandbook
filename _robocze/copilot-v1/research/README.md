# Research — README

## Purpose
This directory is the evidentiary backbone of the whole system. Every strategic or visual recommendation in `/strategy` and `/identity` should be traceable to a note here. Research-first is a non-negotiable operating principle (`docs/00_project-charter.md`).

## When to use
- Before writing or revising anything in `/strategy`.
- Before presenting the 7-option format for a major visual decision (`identity/color-system.md`).
- Whenever a claim about the market, competitors, or audience is made anywhere in the repo.

## Inputs
- Primary sources: founder-provided draft brandbook (Claude Design), interviews, analytics, win/loss notes.
- Secondary sources: competitor sites/decks, category reports, style scans (Pinterest/Dribbble/industry sites — cited, not copied).

## Outputs
- `sources.md` — the running citation ledger.
- Filled-in copies of the four templates below, one per research pass.

## Owner
Research function within the Master Orchestrator's task split — typically executed by the Brand Strategy subagent (`../orchestration/subagent-brand-strategy.md`) for market/competitor work, and the Visual Identity subagent (`../orchestration/subagent-visual-identity.md`) for the visual territory scan.

## Quality criteria
- Every finding has a source (URL, document, date, or "primary interview with [role], [date]").
- Findings are separated from interpretation (`insights-synthesis-template.md` exists specifically to do this separation explicitly).

## Files in this directory
| File | Use for |
|---|---|
| `sources.md` | Running ledger of every source cited anywhere in the repo |
| `market-category-analysis-template.md` | Defining/validating what category IRIN competes in and how that category is evolving |
| `competitor-analysis-template.md` | Structured teardown of 3-5 named competitors/archetypes |
| `visual-territory-scan-template.md` | Surveying visual conventions in-category to identify what to avoid (generic) and where whitespace exists |
| `insights-synthesis-template.md` | Converting raw findings from the above into a short list of decision-ready insights |

## Example (IRIN)
Before drafting `strategy/positioning.md`, the Brand Strategy subagent ran a competitor analysis on 3 archetypes (Big-4-style consultancy, boutique branding agency, in-house DIY) and logged 6 sources in `sources.md`, which the positioning statement's "unlike" clause directly cites.

## Template (blank reusable block)
```
Research pass: 
Date: 
Owner (subagent/human): 
Template(s) used: 
Sources added to sources.md: [list IDs]
Key insight(s) produced: 
Where the insight was applied: [file/section]
```

## Common failure modes
- Skipping straight to opinions in `/strategy` without a research pass, then retrofitting sources later (or never).
- Citing a source once and never revisiting it when the market changes.

## How to avoid generic output
- A finding that could apply to any company in any category is not a finding — push until it's specific to IRIN's actual category and competitors (named, not hypothetical, once real data is available).
