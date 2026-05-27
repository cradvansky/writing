---
name: linkedin
description: Write a LinkedIn post in the user's voice. Use when the user asks to draft a LinkedIn post, hook, or long-form social caption. Pulls voice, stories, beliefs, stats, humour, and vocabulary from the me/ context files and follows the structure of examples/linkedin-example.md.
---

# /linkedin — LinkedIn post in your voice

Use this skill any time the user asks you to draft a LinkedIn post, hook, carousel caption, or long-form social post. Output is ready to paste into LinkedIn.

## Step 1 — Load the user's voice

Always read these files first (they live in the `me/` folder at the root of this project). Do not guess the user's voice — pull from source:

1. `me/identity.md` — who they are, what they sell
2. `me/tone.md` — how they write
3. `me/vocabulary.md` — words they use + words to avoid
4. `me/humour.md` — how they joke
5. `me/beliefs.md` — their hot takes / positions
6. `me/stories.md` — anecdotes they tell
7. `me/data.md` — numbers they name-drop
8. `me/analogies.md` — metaphors they use

Also read `examples/linkedin-example.md` for the canonical post structure (if it exists).

## Step 2 — Ask only what you can't infer

If the user gave you a topic, run with it. Only ask if it's genuinely ambiguous (e.g., "post about AI" — clarify angle). Default to action over questioning.

## Step 3 — Post structure

1. **Bold unicode headline** (𝐁𝐎𝐋𝐃) — the big claim or result. Specifics, dollar amounts, percentages.
2. **Hook line** — one punchy line that tightens the headline. Use a 👉 arrow if that matches the user's style.
3. **Pattern interrupt** — short line that creates tension or curiosity.
4. **Story bridge** — transition into the story (e.g., "Let me explain how I got there:").
5. **Narrative body** — short paragraphs, 1–3 sentences each. Heavy use of line breaks. One thought per line. Use a real story from `me/stories.md` when the topic allows.
6. **Payoff / lesson** — the one-line takeaway. Often maps to a belief from `me/beliefs.md`.
7. **Numbered list of specifics** — 3–5 items with real numbers pulled from `me/data.md`. Never invent stats.
8. **Soft close / CTA** — what the reader does next. No hard pitch unless requested.

## Step 4 — Voice rules (non-negotiable)

- Match the user's default voice from `me/tone.md`. Never sound generic.
- Use their sentence rhythm, not yours.
- Drop in their real numbers from `me/data.md` — never invent stats.
- Self-deprecation, humour, and profanity should match the levels defined in `me/humour.md` and `me/vocabulary.md`.
- Banned words from `me/vocabulary.md` are a hard filter. Scan the draft and remove every instance before delivering.
- End with a clear next step or a quietly confident line. No "what do you think?" beg-for-engagement closers unless the user asks for one.

## Step 5 — Banned words (hard filter)

Before returning the draft, scan against `me/vocabulary.md` § "Banned words" section and remove every instance. Common AI-sounding offenders to watch for:

delve, tapestry, realm, testament, navigate (as verb), robust, leverage (as verb), synergy, holistic, ecosystem, bespoke, elevate, unlock, streamline, game-changer, moving forward, circle back, touch base, low-hanging fruit.

Also avoid emoji spam unless the user's style explicitly uses them. Match their emoji usage from `me/tone.md`.

## Step 6 — Length & format

- **Default:** ~150–300 words. Long enough to tell a story, short enough to read on a phone.
- **Short hook post:** ~60–120 words — bold headline + hook + 2–3 paragraphs + CTA.
- **Long-form / announcement:** 300–500 words — full story arc.

Default to long-form when the topic is a launch, announcement, or result reveal. Default to short when it's an opinion or quick take.

## Step 7 — Deliver

Output the post as a plain markdown code block (so the user can copy it cleanly). Below the post, in 1–2 lines, note:

- Which story / stat you anchored on
- One alternate hook the user can swap in

Do not write a preamble. Do not explain the post. Just deliver it.

## Topic-to-story mapping

<!-- After filling in me/stories.md and me/data.md, add shortcuts here so the AI knows which stories pair with which topics. Example format: -->

<!-- - **Websites / conversion** → [story name] + [stat from data.md] -->
<!-- - **Getting started / fear** → [origin story] + [lowest point numbers] -->
<!-- - **Your product / tools** → [product story] + [result stat] -->

## What success looks like

Reader can tell within the first line who wrote this. The post lands a real number, tells one true story, and ends with a clear next step. Nothing in it sounds like it was written by an AI.
