---
name: capture-voice
description: Distill raw samples in samples/{granola,linkedin,outlook}/ into the 8-file me/ personality dossier. Use when the user wants to (re)populate me/identity.md, me/tone.md, me/vocabulary.md, me/beliefs.md, me/stories.md, me/analogies.md, me/humour.md, me/data.md from real harvested writing samples. Reads samples, writes me/*.md with verbatim quotes and `> source:` provenance lines.
---

# /capture-voice — Distill samples into me/*.md

Use this skill when the user wants to fill (or refresh) the `me/` dossier from raw samples already collected by the ingest scripts.

## Inputs

- `samples/granola/*.md` — meeting transcripts. Each file has a "Chris's lines only" section that is pure spoken Chris.
- `samples/linkedin/*.md` — public LinkedIn posts (text in the "## Text" section).
- `samples/outlook/*.md` — sent emails (full bodies in "## Body").

If `samples/` is empty, stop and tell the user to run the ingest scripts first:
```
python3 scripts/ingest_granola.py
python3 scripts/ingest_linkedin.py
python3 scripts/ingest_outlook.py
```

## Outputs

Eight files in `me/` (overwriting placeholder content):

| File | What to extract | Best source |
|---|---|---|
| identity.md | Name, business, offers, audience, prior roles, operating beliefs, standard links | Outlook signatures + LinkedIn bio posts + Granola intros |
| tone.md | Default voice, email opener/closer patterns, social hooks, sentence rhythm | All three sources (cross-channel comparison is the point) |
| vocabulary.md | Words Chris actually uses, banned words, brand names, profanity level | Outlook (most repeatable) + LinkedIn |
| beliefs.md | Hot takes, positions, hills to die on | LinkedIn (opinions) + Granola (unfiltered) |
| stories.md | Anecdotes repeated across calls/posts | LinkedIn (curated) + Granola (unrehearsed) |
| analogies.md | Metaphors and frameworks | Granola (in-the-moment explanations) |
| humour.md | What lands, what's off-limits | LinkedIn + Granola |
| data.md | Real stats, dollar amounts, percentages | Outlook (deal sizes) + LinkedIn (proof) |

## Method

1. **Sample for breadth, not exhaustion.** Pick 8-12 files from each source — a mix of recent and older, short and long. The goal is high-signal patterns, not coverage.
2. **For each `me/*.md` file in order:**
   - Read the existing template to understand the section structure
   - Scan the sampled files for content that fits each section
   - **Quote verbatim, don't paraphrase.** Jono's README is explicit: "The AI learns more from 5 real examples than from 50 adjectives."
   - Add a `> source: samples/<path>` line under every block quote so future updates can trace provenance
3. **Hard rules (override anything in the template):**
   - **No em-dashes or en-dashes** anywhere in the output. Use commas, periods, or rephrase. Rad-wide ban.
   - **No banned AI words:** delve, tapestry, robust, leverage, synergy, holistic, ecosystem, bespoke, elevate, unlock, streamline, game-changer. Scrub before saving.
   - **Brand = "Rad Consultants"** (title case), never "RAD Consultants".
4. **Vocabulary banned-words section is special.** Beyond the standard AI offenders, populate it with words Chris specifically avoids based on absence in his samples. If "leverage" never appears in 350 files, that's signal.
5. **Cross-channel calibration in tone.md** must be a real differential, not generic. Show how the same idea sounds different across LinkedIn vs. cold email vs. spoken.

## Output format for each me/*.md section

```markdown
## Default voice

Chris talks like he's pacing the room. Short bursts. Lots of "OK" and "right, so" to chain thoughts. Concrete-first, abstract-second.

> "OK, so the way I'm thinking about this is...you're going to plug in your company name and the address...and then a Claude agent goes and pulls every recent news article."
> source: samples/granola/2026-05-19_rad-aspire-weekly-meeting_KGf3TOCM.md
```

Three to six quoted examples per section, each with provenance. Plus a one-paragraph synthesis at the top of each section.

## Deliver

After writing all 8 files, output a single summary:

- Count of files updated
- Sample-file count by source
- Two or three patterns you noticed that the user might not have seen themselves
- One question for the user about anything ambiguous (e.g., "Saw 'Annie' and 'Brian' mentioned often — co-founder? family? confirm before I cite them as recurring characters.")

Do not preface this with "I'll now..." or "Here's..." — just deliver.
