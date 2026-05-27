#!/usr/bin/env python3
"""
Ingest Outlook sent items -> samples/outlook/

Calls the n8n proxy workflow `writing-outlook-sent` (id `sNyoG9vGTUtDKAJH`)
which uses the stored `Rad.com Outlook` Microsoft Graph OAuth2 credential to
list /me/mailFolders/sentitems/messages.

Run:
  python3 scripts/ingest_outlook.py [limit]

Default: limit=200
"""
from __future__ import annotations

import hashlib
import html
import json
import re
import sys
import time
import urllib.request
from pathlib import Path

NOISE_SUBJECT_PATTERNS = [
    r"^prospect opened page",
    r"^prospect page view",
    r"^web visit:",
    r"^canceled:",
    r"^accepted:",
    r"^declined:",
    r"^tentative:",
    r"^auto[- ]?reply",
    r"^out of office",
    r"^undeliverable:",
    r"^delivery (status notification|failure)",
    r"^read:",
    r"^message read:",
]
NOISE_RE = re.compile("|".join(NOISE_SUBJECT_PATTERNS), re.IGNORECASE)

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "samples" / "outlook"
OUT.mkdir(parents=True, exist_ok=True)

WEBHOOK = "https://n8n.radconsultants.org/webhook/writing-outlook-sent"


def slugify(s: str, max_len: int = 50) -> str:
    s = re.sub(r"[^a-zA-Z0-9]+", "-", s).strip("-").lower()
    return (s or "msg")[:max_len]


def strip_html(s: str) -> str:
    s = re.sub(r"<style[^>]*>.*?</style>", "", s, flags=re.S | re.I)
    s = re.sub(r"<script[^>]*>.*?</script>", "", s, flags=re.S | re.I)
    s = re.sub(r"<br\s*/?>", "\n", s, flags=re.I)
    s = re.sub(r"</p>", "\n\n", s, flags=re.I)
    s = re.sub(r"<[^>]+>", "", s)
    s = html.unescape(s)
    s = re.sub(r"\r\n?", "\n", s)
    s = re.sub(r"\n{3,}", "\n\n", s)
    return s.strip()


def is_chris_authored(msg: dict, my_addrs: set[str]) -> bool:
    frm = ((msg.get("from") or {}).get("emailAddress") or {}).get("address", "").lower()
    return frm in my_addrs


def fetch(limit: int) -> list[dict]:
    body = json.dumps({"limit": limit}).encode()
    req = urllib.request.Request(
        WEBHOOK,
        data=body,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=300) as r:
        payload = json.loads(r.read())
    items = payload.get("items") or []
    if not isinstance(items, list):
        items = [items]
    return items


def main() -> int:
    limit = int(sys.argv[1]) if len(sys.argv) > 1 else 200
    my_addrs = {
        "chris@radconsultants.com",
        "chris@radconsultants.org",
        "cradvansky@gmail.com",
    }

    print(f"outlook ingest: limit={limit}")
    t0 = time.time()
    msgs = fetch(limit)
    print(f"  fetched {len(msgs)} messages in {time.time() - t0:.1f}s")

    written = 0
    not_chris = 0
    empty = 0
    noise = 0
    for m in msgs:
        if not isinstance(m, dict):
            continue
        if not is_chris_authored(m, my_addrs):
            not_chris += 1
            continue

        subject = m.get("subject") or "(no subject)"
        if NOISE_RE.match(subject.strip()):
            noise += 1
            continue

        sent = m.get("sentDateTime") or "?"
        date_part = sent.split("T")[0] if sent else "undated"

        body_obj = m.get("body") or {}
        ctype = (body_obj.get("contentType") or "").lower()
        raw = body_obj.get("content") or m.get("bodyPreview") or ""
        text = strip_html(raw) if ctype == "html" else raw.strip()
        if not text or len(text) < 30:
            empty += 1
            continue

        to_list = [
            ((t.get("emailAddress") or {}).get("address") or "")
            for t in (m.get("toRecipients") or [])
        ]
        cc_list = [
            ((t.get("emailAddress") or {}).get("address") or "")
            for t in (m.get("ccRecipients") or [])
        ]
        slug = slugify(subject[:60])
        msg_id = (m.get("internetMessageId") or m.get("id") or sent).strip("<>")
        digest = hashlib.sha1(msg_id.encode()).hexdigest()[:10]
        out_path = OUT / f"{date_part}_{slug}_{digest}.md"

        doc = [
            f"# {subject}",
            "",
            f"- sent: {sent}",
            f"- from: {((m.get('from') or {}).get('emailAddress') or {}).get('address','?')}",
            f"- to: {', '.join(to_list) or '(none)'}",
            f"- cc: {', '.join(cc_list) or '(none)'}",
            f"- conversation_id: {m.get('conversationId','')}",
            "",
            "## Body",
            "",
            text,
            "",
        ]
        out_path.write_text("\n".join(doc), encoding="utf-8")
        written += 1

    print(
        f"outlook ingest: wrote={written} noise={noise} empty/short={empty} not_chris={not_chris} -> {OUT}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
