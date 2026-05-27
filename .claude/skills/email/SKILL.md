---
name: email
description: Draft an email in Chris Radvansky's voice (cold intro, warm reply, scope/proposal blurb, scheduling, internal). Use when the user asks to write, draft, reply to, or "send" an email. Pulls voice from me/*.md and matches the channel rules in me/tone.md.
---

# /email - Email in Chris's voice

Use this skill any time the user asks you to draft an email. Output is paste-ready into Outlook with the signature block intact.

## Step 1 - Load Chris's voice

Always read these files first from `me/`:

1. `me/identity.md` - email signature, phone, common inbound patterns
2. `me/tone.md` - opener/body/closer rules per channel
3. `me/vocabulary.md` - banned words and signature phrases
4. `me/humour.md` - profanity calibration (none in cold emails, mild in long-thread warm replies)
5. `me/beliefs.md` + `me/stories.md` - only if the email needs a frame or proof point
6. `me/data.md` - only if the email needs a real number

## Step 2 - Classify the email type first

Before drafting, identify which category and follow its rules. Ask the user if ambiguous; otherwise infer from their prompt.

| Type | Default length | Opener | Booking link? | Profanity |
|---|---|---|---|---|
| Cold intro (first touch) | 4-7 sentences | "Hey [First]," | No - earn permission | None |
| Warm reply (known contact) | 2-5 sentences | "Hey [First]," | If they asked | None |
| Reply to mutual intro | 3-5 sentences | "Thanks for the intro [Introducer]." then turn to the new person | Only if invited | None |
| Scheduling | 1-3 sentences | "Hey [First],", direct ask | Yes (Book a Rad chat) | None |
| Scope / pricing | 5-10 sentences | "Hey [First]," | No | None |
| Internal / casual | 1-3 sentences | First name, comma, often no opener at all | n/a | Mild |
| One-line ack | 1 line | none, just the line | n/a | None |

## Step 3 - Structure each type

### Cold intro (first touch)

1. "Hey [First]," opener.
2. One specific concrete reason you're writing - real context, not generic value-prop. Pulled from research, mutual contact, or recent post.
3. One short line about what Chris does (in his voice from `me/identity.md`).
4. A give. Not an ask. Example: a link to a relevant clutchsales marketing engine page personalized for them, a 1-sentence observation about their company, a free idea.
5. Optional: one-sentence "would love to swap notes if there's a fit" close. **No booking link.** See [feedback_e2e_email_sequencing](../../../../../root/.claude/projects/-var-www/memory/feedback_e2e_email_sequencing.md): earn permission before the booking link.
6. Signature block.

### Warm reply / known contact

1. "Hey [First]," opener.
2. Acknowledge what they said in one sentence.
3. Answer their question or propose the next step directly.
4. Optional: forward-looking sentence ("I will drop you a line Wednesday with an update.").
5. Signature.

### Reply to mutual intro

1. "Thanks for the intro [Introducer]!" (with exclamation - Chris uses these in intros)
2. Turn directly to the new contact: "Great to meet you [New Person]."
3. One short line about what Chris does (or what he's been building).
4. Propose a quick call or ask what they're working on.
5. Signature.

> Real example to mimic:
>
> "Thanks for the intro Michele! Great to meet you Ben and Sumant. I have been building with Claude Code and n8n for about a year now and would love to learn more about what you are working on. I am an independent and developing flexible solutions for my clients in the space."
> source: samples/outlook/2026-05-27_re-introductions_933aed60e6.md

### Scope / pricing

1. "Hey [First]," opener.
2. Direct estimate: "I would shoot for [date]" pattern.
3. One sentence on why that date (back-and-forth on credentials, fine-tuning, etc.).
4. If asked about ongoing costs: name the real numbers from `me/data.md` ($8/mo VPS, n8n free, AI APIs as the variable).
5. Honest reassurance about what the client will/won't need to maintain.
6. Signature.

> Real example:
>
> "I would shoot for June 19th for completion. If I knew exactly all that you wanted to fully achieve at every step and I had visibility to how everything would play out exactly right now, I could probably do it within the next 3 weeks. But given client experience, there is a good amount of back and forth with credentials and fine-tuning so I think that kind of buffer is appropriate. Given the nature of the end-deliverable, I don't think you will need much on going AI enablement. I will be using AI to build but don't think you will need much to maintain. It is possible you will need to set up a VPS and n8n instance but the VPS is $8/mo or so and n8n is free. My main costs are AI APIs, Firecrawl, and Hunter but this project won't need those ongoing."
> source: samples/outlook/2026-05-07_re-rad-legalfenix_27273ea081.md

### Scheduling

1. "Hey [First]," or just first name.
2. Direct: "[Day/time] works for me." or "Let's do [time]. If that doesn't work, I could do [option B] or [option C] that same day."
3. Optional one-liner reason if rescheduling: "I have a conflict at that time."
4. Signature.

### Internal / casual

- Often no opener at all. Just go.
- "Sounds like a plan."
- "What do you think?"
- "Wanna send an invite?"
- Sign off with first name only or just the signature block.

## Step 4 - Voice rules (non-negotiable)

- **No em-dashes (-).** Hard ban. Use comma, period, or hyphen with spaces.
- **No banned AI words** from `me/vocabulary.md` Banned-words section. Scrub before delivering.
- **No "I hope this finds you well", "Certainly!", "Absolutely!", "Of course!".** Filler openers banned.
- **No trailing summary / "to recap" / "looking forward to hearing back at your earliest convenience".**
- **No "what do you think?" beg unless it's a real handoff** (it's fine when there's a real artifact to opinion on).
- **Brand = "Rad Consultants"** (title case), never "RAD Consultants".
- **No "we" unless there's a real collaborator on the thread.** Chris is solo by design.
- **Sentence rhythm is short-short-long-short.** Don't write a 4-line run-on.

## Step 5 - Signature block (always include unless told otherwise)

```
Chris Radvansky
Owner, Rad Consultants
215.801.3625
chris@radconsultants.com
Book a Rad chat
```

For very informal internal/casual emails, just "Chris" is fine.

## Step 6 - Banned-word scrub (hard filter)

Before returning, scan the draft against the banned list in `me/vocabulary.md` and remove every instance. Common offenders to watch for:

delve, tapestry, robust, leverage, synergy, holistic, ecosystem (in abstract), elevate, unlock, streamline, game-changer, moving forward, circle back, touch base, low-hanging fruit, in today's fast-paced world.

Also scan for em-dashes (-) and replace them.

## Step 7 - Deliver

Output the email in a single fenced code block. Below the block, in 1-2 lines:

- Which email type you wrote (cold intro / warm reply / etc.)
- One alternate subject line the user can swap in

No preamble. No "here's your email." No "let me know if you want changes." Just deliver.

## What success looks like

The recipient reads it and assumes Chris wrote it directly in Outlook on his phone. Direct, specific, no corporate-speak, ends with the signature block. If it sounds like an AI wrote it, the skill failed.
