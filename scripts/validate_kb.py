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
KNOWN_AUTHORITIES = {"normative", "operational", "implementation", "editorial"}
KNOWN_STATUSES = {"current", "future-dated", "historical", "partial", "superseded"}
KNOWN_PLATFORMS = {"apple", "google-play", "shared", "regional", "operations"}
LANGUAGE_SUFFIXES = {
    ".zh-CN.md": "zh-CN",
    ".en-US.md": "en-US",
}


def front_matter(text: str) -> str:
    if not text.startswith("---\n"):
        return ""
    end = text.find("\n---", 4)
    return text[4:end] if end != -1 else ""


def scalar(fm: str, field: str) -> str:
    for line in fm.splitlines():
        if line.startswith(f"{field}:"):
            return line.split(":", 1)[1].strip().strip(""'")
    return ""


def main() -> int:
    errors = []
    zh = {}
    en = {}
    for path in DOCS.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        language = next(
            (value for suffix, value in LANGUAGE_SUFFIXES.items() if path.name.endswith(suffix)),
            None,
        )
        if path.name.endswith(".zh-CN.md"):
            zh[path.name[:-9]] = path
        if path.name.endswith(".en-US.md"):
            en[path.name[:-9]] = path
        if language:
            fm = front_matter(text)
            missing = [field for field in REQUIRED if field not in fm]
            if missing:
                errors.append(f"{path}: missing metadata {', '.join(missing)}")
                continue

            declared_language = scalar(fm, "language")
            authority = scalar(fm, "authority")
            status = scalar(fm, "status")
            platform = scalar(fm, "platform")

            if declared_language != language:
                errors.append(
                    f"{path}: language metadata {declared_language!r} "
                    f"does not match filename language {language!r}"
                )
            if authority not in KNOWN_AUTHORITIES:
                errors.append(
                    f"{path}: unknown authority {authority!r}; "
                    f"expected one of {sorted(KNOWN_AUTHORITIES)}"
                )
            if status not in KNOWN_STATUSES:
                errors.append(
                    f"{path}: unknown status {status!r}; "
                    f"expected one of {sorted(KNOWN_STATUSES)}"
                )
            if platform not in KNOWN_PLATFORMS:
                errors.append(
                    f"{path}: unknown platform {platform!r}; "
                    f"expected one of {sorted(KNOWN_PLATFORMS)}"
                )
            if not re.search(r"\[[^\]]+\]\(https?://", text):
                errors.append(f"{path}: no Markdown source link found")

    for stem in sorted(set(zh) ^ set(en)):
        errors.append(f"bilingual pair missing: {stem}")

    if errors:
        print("\n".join(errors))
        return 1

    print(
        f"KB validation passed: {len(en)} English pages, "
        f"{len(zh)} Chinese pages, {len(set(en) & set(zh))} pairs."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
