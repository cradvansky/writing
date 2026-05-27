# Writing — Status

**Phase:** Discovery
**Priority:** Medium
**Last Session:** 2026-05-27
**Next Focus:** Run sample ingest (Granola + Outlook + LinkedIn), then distill into `me/*.md`

## Current state

Fork of jonocatliff/writing cloned to `/var/www/writing`. Template ships with:

- `me/` — 8 unfilled voice files (identity, tone, vocabulary, beliefs, stories, analogies, humour, data, stats)
- `.claude/skills/linkedin/SKILL.md` — LinkedIn writer skill (uses `me/`)

Rad scaffolding added: CLAUDE.md, this STATUS.md, .gitignore.

## Inventory

- Granola: 27 meetings with transcripts available in `rad_dashboard.granola.meetings`
- Outlook: Microsoft Graph route confirmed — needs one-time device-code auth
- LinkedIn: Apify actor `apimaestro/linkedin-profile-posts` is the path; token TBD

## Next session

1. Run `scripts/ingest_granola.py` → populates `samples/granola/`
2. Wire up Graph device-code flow → run `scripts/ingest_outlook.py`
3. Run `scripts/ingest_linkedin.py` against cradvansky profile
4. Invoke `/capture-voice` skill — distill samples into `me/*.md`
5. Test with `/linkedin "..."` — verify the draft sounds like Chris

## Blockers

- Apify token not in `/root/radcrm-agents/.env` (var is empty); not in any plaintext file under `/root/`. n8n has 4 Apify credentials encrypted in DB. Need to either: (a) Chris pastes his Apify token, or (b) we proxy LinkedIn scrape through an n8n workflow that uses an existing stored credential.
- Microsoft Graph app registration: needs Chris to approve the device-code in a browser.
