#!/usr/bin/env python3
"""
Ingest LinkedIn posts -> samples/linkedin/

Calls the n8n proxy workflow `writing-linkedin-scrape` (id `1rbUrIjLy4bFliW2`)
which wraps the Apify `apimaestro/linkedin-profile-posts` actor. The proxy
holds the Apify token in n8n; this script never sees it.

Run:
  python3 scripts/ingest_linkedin.py [username] [limit]

Defaults: username=radaiworkflows  limit=100 (actor caps at 100 per call)
"""
from __future__ import annotations

import json
import re
import sys
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "samples" / "linkedin"
OUT.mkdir(parents=True, exist_ok=True)

WEBHOOK = "https://n8n.radconsultants.org/webhook/writing-linkedin-scrape"


def slugify(s: str, max_len: int = 50) -> str:
    s = re.sub(r"[^a-zA-Z0-9]+", "-", s).strip("-").lower()
    return (s or "post")[:max_len]


def fetch_posts(username: str, limit: int) -> list[dict]:
    body = json.dumps({"username": username, "limit": limit}).encode()
    req = urllib.request.Request(
        WEBHOOK,
        data=body,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=600) as r:
        payload = json.loads(r.read())
    items = payload.get("items") or []
    if not isinstance(items, list):
        items = [items]
    return items


def main() -> int:
    username = sys.argv[1] if len(sys.argv) > 1 else "radaiworkflows"
    limit = int(sys.argv[2]) if len(sys.argv) > 2 else 100

    print(f"linkedin ingest: username={username} limit={limit}")
    t0 = time.time()
    posts = fetch_posts(username, limit)
    print(f"  fetched {len(posts)} posts in {time.time() - t0:.1f}s")

    written = 0
    skipped = 0
    for p in posts:
        urn = (
            (p.get("urn") or {}).get("activity_urn")
            or (p.get("urn") or {}).get("share_urn")
            or p.get("full_urn", "").split(":")[-1]
            or str(p.get("posted_at", {}).get("timestamp", "no-id"))
        )
        text = (p.get("text") or "").strip()
        if not text:
            skipped += 1
            continue

        posted = p.get("posted_at") or {}
        date_part = (posted.get("date") or "").split(" ")[0] or "undated"

        slug = slugify(text[:60])
        out_path = OUT / f"{date_part}_{slug}_{urn[-10:]}.md"

        author = p.get("author") or {}
        stats = p.get("stats") or {}
        body = [
            f"# LinkedIn post {urn}",
            "",
            f"- posted_at: {posted.get('date') or '?'} ({posted.get('relative') or '?'})",
            f"- author: {author.get('first_name','')} {author.get('last_name','')}".strip(),
            f"- url: {p.get('url','')}",
            f"- post_type: {p.get('post_type','')}",
            f"- reactions: {stats.get('total_reactions') or stats.get('reactions') or '?'}",
            f"- comments: {stats.get('comments') or '?'}",
            f"- reposts: {stats.get('reposts') or stats.get('shares') or '?'}",
            "",
            "## Text",
            "",
            text,
            "",
        ]
        out_path.write_text("\n".join(body), encoding="utf-8")
        written += 1

    print(f"linkedin ingest: wrote={written} skipped={skipped} -> {OUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
