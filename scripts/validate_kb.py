#!/usr/bin/env python3
"""Validate bilingual topic pairs and basic KB metadata.

This validator is intentionally conservative. It checks document hygiene,
not legal correctness.
"""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
REQUIRED = ("id:", "platform:", "language:", "authority:", "status:")


def front_matter(text: str) -> str:
    if not text.startswith("---\n"):
        return ""
    end = text.find("\n---", 4)
    return text[4:end] if end != -1 else ""


def main() -> int:
    errors = []
    zh = {}
    en = {}
    for path in DOCS.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        if path.name.endswith(".zh-CN.md"):
            zh[path.name[:-9]] = path
        if path.name.endswith(".en-US.md"):
            en[path.name[:-9]] = path
        if path.name.endswith((".zh-CN.md", ".en-US.md")):
            fm = front_matter(text)
            missing = [field for field in REQUIRED if field not in fm]
            if missing:
                errors.append(f"{path}: missing metadata {', '.join(missing)}")
            if not re.search(r"\[[^\]]+\]\(https?://", text):
                errors.append(f"{path}: no Markdown source link found")
    for stem in sorted(set(zh) ^ set(en)):
        errors.append(f"bilingual pair missing: {stem}")
    if errors:
        print("\n".join(errors))
        return 1
    print("KB validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
