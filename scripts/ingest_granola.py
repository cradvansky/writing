#!/usr/bin/env python3
"""
Ingest Granola meeting transcripts → samples/granola/

Pulls every meeting with a transcript, writes one markdown file per meeting.
Splits each utterance into Chris's lines (speaker.source = 'microphone') vs.
the other party (speaker.source = 'speaker'). Downstream voice-distill should
focus on the 'microphone' lines.

Run:
  python3 scripts/ingest_granola.py

Source: rad_dashboard.granola.meetings on n8n-postgres-1.
"""
from __future__ import annotations

import json
import os
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "samples" / "granola"
OUT.mkdir(parents=True, exist_ok=True)

CONTAINER = "n8n-postgres-1"
USER = "n8n"
DB = "rad_dashboard"
PASSWORD = os.environ.get("GRANOLA_PG_PASSWORD")
if not PASSWORD:
    # Fall back to the DSN line in the granola builder env file, since that is
    # the local source of truth for this DB on this host.
    import re
    try:
        with open("/var/www/rad-dashboard/granola/builder/.env") as f:
            m = re.search(r"password=(\S+)", f.read())
            if m:
                PASSWORD = m.group(1)
    except FileNotFoundError:
        pass
if not PASSWORD:
    raise SystemExit(
        "Set GRANOLA_PG_PASSWORD env var, or place the password in "
        "/var/www/rad-dashboard/granola/builder/.env (password=...). "
        "This script does not ship credentials."
    )


def psql_json_rows(sql: str) -> list[dict]:
    """Run a SELECT and get one JSON object per row via COPY to stdout.

    Robust to embedded newlines / separators in TEXT and JSONB columns —
    each row is a single JSON object on its own line, with PG newlines
    escaped as \\n inside the JSON strings.
    """
    copy_sql = f"COPY (SELECT row_to_json(t) FROM ({sql}) t) TO STDOUT"
    cmd = [
        "docker", "exec", "-e", f"PGPASSWORD={PASSWORD}", CONTAINER,
        "psql", "-U", USER, "-d", DB, "-c", copy_sql,
    ]
    r = subprocess.run(cmd, capture_output=True, text=True, check=True)
    out = []
    for line in r.stdout.splitlines():
        line = line.strip()
        if not line:
            continue
        out.append(json.loads(line))
    return out


def slugify(s: str, max_len: int = 60) -> str:
    s = re.sub(r"[^a-zA-Z0-9]+", "-", s).strip("-").lower()
    return (s or "untitled")[:max_len]


def main() -> int:
    rows = psql_json_rows(
        "SELECT id, meeting_date, title, owner_email, is_external, "
        "summary_md, transcript "
        "FROM granola.meetings "
        "WHERE transcript IS NOT NULL "
        "AND jsonb_array_length(transcript) > 0 "
        "ORDER BY meeting_date DESC"
    )

    written = 0
    skipped = 0
    for row in rows:
        mid = row["id"]
        mdate = row["meeting_date"]
        title = row.get("title") or ""
        owner = row.get("owner_email") or ""
        is_ext = row.get("is_external")
        summary = row.get("summary_md") or ""
        utterances = row.get("transcript") or []

        if not utterances:
            skipped += 1
            continue

        try:
            ts = datetime.fromisoformat(mdate.replace(" ", "T").rstrip("Z"))
            date_part = ts.strftime("%Y-%m-%d")
        except Exception:
            date_part = mdate[:10] if mdate else "unknown"

        chris_lines, other_lines, full_lines = [], [], []
        for u in utterances:
            text = (u.get("text") or "").strip()
            if not text:
                continue
            src = (u.get("speaker") or {}).get("source") or ""
            if src == "microphone":
                chris_lines.append(text)
                full_lines.append(f"**Chris:** {text}")
            elif src == "speaker":
                other_lines.append(text)
                full_lines.append(f"**Other:** {text}")
            else:
                full_lines.append(f"**?:** {text}")

        if not chris_lines:
            skipped += 1
            continue

        slug = slugify(title or "untitled")
        out_path = OUT / f"{date_part}_{slug}_{mid[-8:]}.md"
        body = [
            f"# {title or '(untitled meeting)'}",
            "",
            f"- meeting_id: `{mid}`",
            f"- meeting_date: {mdate}",
            f"- owner: {owner or '(none)'}",
            f"- external: {is_ext}",
            f"- chris_utterance_count: {len(chris_lines)}",
            f"- other_utterance_count: {len(other_lines)}",
            "",
            "## Granola summary",
            "",
            summary.strip() or "(no summary)",
            "",
            "## Chris's lines only",
            "",
            "\n\n".join(chris_lines),
            "",
            "## Full transcript",
            "",
            "\n\n".join(full_lines),
            "",
        ]
        out_path.write_text("\n".join(body), encoding="utf-8")
        written += 1

    print(f"granola ingest: wrote={written} skipped={skipped} -> {OUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
