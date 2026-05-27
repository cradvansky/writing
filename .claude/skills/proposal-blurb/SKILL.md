---
name: proposal-blurb
description: Generate short pitch / proposal / "what I'd do for you" copy in Chris's voice. Use when the user asks for a proposal blurb, scope summary, portfolio caption, services-page copy, or one-paragraph pitch for a specific prospect. Output is 1-3 paragraphs paste-ready into a proposal doc, landing page, or email body.
---

# /proposal-blurb - Pitch copy in Chris's voice

Use this skill when the user asks for proposal copy, a scope summary, a portfolio caption, services-page copy, or a "what would you do for [Prospect]?" pitch. Output: 1-3 paragraphs, paste-ready, no preamble.

## Step 1 - Load Chris's voice

Always read these from `me/`:

1. `me/identity.md` - tools, what he sells, offer stack, audience
2. `me/tone.md` - sentence rhythm, channel calibration
3. `me/vocabulary.md` - banned words + signature phrases
4. `me/beliefs.md` + `me/stories.md` - frame and proof points
5. `me/data.md` - real numbers (timelines, costs, project counts)
6. `me/analogies.md` - frameworks (3 A's, give-give-give-then-ask, plane-as-flying)

## Step 2 - Identify the proposal shape

Ask the user what they need if ambiguous. Default shapes:

| Shape | Length | Use case |
|---|---|---|
| One-liner | 1 sentence | Portfolio caption, services page row, hover card |
| Short pitch | 1 paragraph (~80-150 words) | Cold email value-prop, LinkedIn DM, proposal opener |
| Standard scope | 2-3 paragraphs (~200-350 words) | Proposal section, services page, prospect page intro |
| Deep dive | 4-5 paragraphs | Full proposal "what we'd build" section |

## Step 3 - Structure

Every proposal blurb has the same beats. Compress or expand based on shape.

1. **Concrete scene or current-state.** Name the prospect's reality in one line. "Your team is wearing every hat." / "Your sales ops still live in spreadsheets." / "Your candidate sourcing is one person doing the work of three."
2. **The shift Chris is going to make.** What changes for them. Direct, no fluff.
3. **The how, in their words.** Tools and approach (Claude Code + n8n + Postgres / Firecrawl / Apify, bespoke build, integrated into their systems). Reference the toolkit from `me/identity.md`.
4. **Proof / story anchor (optional but recommended for longer shapes).** Lean on a story from `me/stories.md` - the LegalFenix scope conversation, the Cutco beat, the .org-to-.com switch, etc. Real names where appropriate (Engage2Excel, LegalFenix, Conexis, Telabotics).
5. **Quiet close.** What the next step is. **Never a "book a call today!"** beg. More like "happy to show you a clickable version" or "I'd shoot for [date]" or "let me know if there's a fit."

## Step 4 - Voice rules (non-negotiable)

- **No em-dashes (-).** Replace with comma, period, hyphen-spaces, or rephrase.
- **No banned AI words.** Full list in `me/vocabulary.md`.
- **Brand = "Rad Consultants"** (title case).
- **"I" not "we"** unless a real collaborator is tagged.
- **Specifics over abstractions.** "$8/mo VPS, n8n is free" beats "low ongoing costs." "Built it for Conexis in 3 weeks" beats "rapidly delivered." Use real numbers from `me/data.md`.
- **Pull real client names when they're already public** (Engage2Excel, LegalFenix, Conexis, Picklr, etc.). Never invent client names.
- **Self-effacing > self-aggrandizing.** A small wink is fine: "I'm wearing every hat too, so I know the feeling."

## Step 5 - Banned-word scrub

Same as the `email` skill: scan and remove em-dashes, AI cliches, filler openers, and trailing summaries. Reference `me/vocabulary.md` banned list.

## Step 6 - Length-specific rules

- **One-liner:** Lead with the verb. "Build a bespoke AI workflow that turns [pain] into [outcome] in [timeframe]." Max 25 words.
- **Short pitch:** Open with a scene, name the shift, name the tools, quiet close. No story unless it's a real one in 1 sentence.
- **Standard scope:** Add the story beat. Drop in real numbers from `me/data.md`. Cite a comparable client if the parallel is real.
- **Deep dive:** Add a "what's in scope" bullet list (3-6 items) and a "what's out of scope" bullet list (1-3 items). Keep both honest. End with a timeline estimate using the LegalFenix pattern.

## Step 7 - Deliver

Output the blurb in a single fenced code block. Below the block, in 1-2 lines:

- The shape you chose (one-liner / short / standard / deep)
- One alternate opening hook the user can swap in

No preamble. No "here's your blurb." Just deliver.

## Templates by audience

### Staffing / RPO / MSP / VMS (his core market)

Pull from: contingent workforce language. References to industry events (HRO Today, PSPS, Randstad Strategic Partnership Forum) land here. Tools: Bullhorn, Job Diva, internal VMS portals.

### Single-operator service business (Picklr-style)

Pull from: "wearing every hat" beat. The Picklr Gmail / PlaybyPoint integration is a real reference.

### Law firm marketing (LegalFenix-style)

Pull from: LegalFenix scoping email. The "schema replacing Excel" framing. HubSpot pilot. Fractional CMO context.

### Compliance / regulated (PayDataOps-style)

Pull from: pay data + CA SB 1162. "Productized" framing. Note that he's still solo - the productization is forkable templates, not a SaaS team.

## Examples to anchor on

> "On the site you can check out scrubbed, trimmed-down versions of my client solutions - clickable and all. All the same, they are not. They are built bespoke for my clients, integrating with their systems and modifiable with a quick email / message to their friendly AI consultant - me!"
> source: samples/linkedin/2026-04-22_today-is-a-big-day-yes-it-is-wednesday-yes-it-is-e_3943857152.md

> "What started as a Command Center for 2 of my current clients to ensure they can quickly and easily engage with AI in their business development efforts, I got the GREAT idea of bringing the sales guidance from those books into a CRM."
> source: samples/linkedin/2026-04-28_a-crm-for-soloentrepreneurs-i-tell-people-that-i-a_3290815488.md

## What success looks like

A staffing exec reads the blurb and thinks "this person gets my world." A LegalFenix-style client reads it and thinks "this is the level of specificity I want." Generic AI marketing copy would never land that - the blurb has to feel like Chris drafted it on his phone between calls.
