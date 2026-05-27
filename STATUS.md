# Writing - Status

**Phase:** Build (V1 shipped 2026-05-27)
**Priority:** Medium
**Last Session:** 2026-05-27
**GitHub:** https://github.com/cradvansky/writing (forked from jonocatliff/writing)
**Next Focus:** Real-world test - draft a LinkedIn post + cold email via the skills and iterate `me/*.md` based on what feels off

## V1 shipped

Forked jonocatliff/writing, populated `me/` from real harvested samples, added 3 custom skills, pushed to https://github.com/cradvansky/writing.

### Harvested samples (gitignored, ~3 MB on disk)

| Source | Files | Size | Pulled via |
|---|---|---|---|
| Granola transcripts | 27 | 1.3 MB | Direct read from `rad_dashboard.granola.meetings` |
| LinkedIn posts | 100 | 416 KB | n8n proxy `writing-linkedin-scrape` (id `1rbUrIjLy4bFliW2`) wrapping Apify `apimaestro/linkedin-profile-posts` |
| Outlook sent items | 223 | 1.2 MB | n8n proxy `writing-outlook-sent` (id `sNyoG9vGTUtDKAJH`) using Microsoft Graph `/me/mailFolders/sentitems/messages` with the `Rad.com Outlook` credential (`ggymNDDHY1yNe4ae`) |

### `me/` populated

All 8 dossier files filled with verbatim quotes plus `> source:` provenance. Em-dashes scrubbed per Rad voice rules.

### `.claude/skills/`

- `linkedin/` - from Jono's template (unchanged)
- `email/` - cold intro, warm reply, scope/pricing, scheduling, internal - one of 7 patterns per draft
- `proposal-blurb/` - one-liner through deep-dive scope copy
- `capture-voice/` - re-runnable distillation skill (read `samples/` to update `me/*.md`)

### `scripts/`

- `ingest_granola.py` - reads from `rad_dashboard.granola.meetings`, requires `GRANOLA_PG_PASSWORD` env (or falls back to `/var/www/rad-dashboard/granola/builder/.env`)
- `ingest_linkedin.py` - calls n8n proxy
- `ingest_outlook.py` - calls n8n proxy

## n8n workflows owned by this project

- `1rbUrIjLy4bFliW2` writing-linkedin-scrape (ACTIVE)
- `sNyoG9vGTUtDKAJH` writing-outlook-sent (ACTIVE)

Both use stored credentials only - no tokens in the repo.

## Next session

1. **Real test:** From Claude Code in this repo, run `/linkedin "..."` and `/email "..."` against a real prompt. Validate the voice.
2. **Iterate `me/*.md`** when a draft is off. The fix is in the dossier, not the skills.
3. **Refresh samples** if 27 Granola transcripts feels light - re-run `scripts/ingest_granola.py` periodically as new meetings come in.
4. **Optional:** add `cold-outreach/`, `speaking-pitch/`, or `youtube-script/` skills as new channels emerge.

## No active blockers
