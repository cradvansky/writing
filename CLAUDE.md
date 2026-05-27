# Writing — Chris's voice clone for Claude Code

Fork of [jonocatliff/writing](https://github.com/jonocatliff/writing) from his video
*"Make Claude Code Write EXACTLY Like You"*. Local Claude Code repo — no webserver,
no nginx, no subdomain. Purpose: let Claude draft LinkedIn posts, emails, and
proposal copy in Chris's actual voice, anchored on real samples.

## How it works

1. `me/` — 8 markdown files describing Chris's voice (identity, tone, vocabulary,
   stories, analogies, humour, beliefs, data). The skills read these before
   drafting anything.
2. `samples/` — raw harvested writing samples (gitignored, never committed).
   Three subdirs: `granola/` (spoken voice), `outlook/` (email voice),
   `linkedin/` (social voice).
3. `scripts/` — one ingest script per source. Read-only against each source.
4. `.claude/skills/` — channel-specific skills. Each reads `me/` and produces
   ready-to-paste output. Ships with `linkedin`; we add `email`,
   `proposal-blurb`, `capture-voice`.

## Sources of truth

| Source | Where | Notes |
|---|---|---|
| Granola transcripts | `granola.meetings.transcript` (jsonb array of `{text, speaker.source}`) on `n8n-postgres-1` / db `rad_dashboard` | Chris = `speaker.source = 'microphone'`. 27 meetings as of 2026-05-27. |
| Outlook sent items | Microsoft Graph `/me/mailFolders/SentItems/messages` | OAuth device-code flow, one-time auth. Mail.Read scope. |
| LinkedIn posts | Apify actor `apimaestro/linkedin-profile-posts` (or `harvestapi/linkedin-profile-posts`) | Profile: linkedin.com/in/cradvansky. |

## Hard rules (inherited from /var/www/CLAUDE.md and /root/.claude/CLAUDE.md)

- **No em-dashes / en-dashes anywhere.** Banned project-wide.
- **No banned AI words** (delve, tapestry, robust, leverage, synergy, etc.) — full
  list in `me/vocabulary.md` § Banned words. Every skill must scrub the draft
  before delivering.
- **No "what do you think?" engagement-bait closes.**
- **Brand = "Rad Consultants"** (title case), never "RAD Consultants".
- **Never commit `samples/`** — real meeting transcripts and client emails are
  private. Enforced by `.gitignore`.
- **Pre-push secret scan**: the universal Rad Postgres password, any Apify or
  Microsoft Graph tokens, and JWT secrets. See the `feedback_github_secret_audit`
  memory for the canonical block-list before pushing.

## Gotchas

- Granola transcript is JSONB array, not markdown. Use jq/python to filter for
  `speaker.source = 'microphone'` (Chris's utterances) vs `'speaker'` (other
  party).
- The `linkedin` skill from Jono uses bold-unicode headlines (𝐁𝐎𝐋𝐃) and 👉
  arrows. Match Chris's actual LinkedIn style after ingest — may need to override.
- Skill structure follows Jono's pattern: `name`, `description` (as trigger
  condition, not summary), then numbered steps. See Skill Authoring guide in
  /var/www/CLAUDE.md.
