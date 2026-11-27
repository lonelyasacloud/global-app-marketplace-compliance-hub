# Knowledge Base Release Readiness

Use this checklist before merging a policy import, translation update, navigation change, or site configuration change.

## Content and evidence

- [ ] The official source URL is reachable or the failure is documented.
- [ ] The page states its knowledge-base review date.
- [ ] Effective dates and future-dated previews are separated.
- [ ] The authority and status describe the page accurately.
- [ ] The coverage boundary records important omissions, failed fetches, or language gaps.
- [ ] No third-party text has been copied; summaries are original and attributed.

## Bilingual parity

- [ ] Every .en-US.md page has a matching .zh-CN.md page.
- [ ] Both pages use the same stable id.
- [ ] Dates, scope, obligations, and evidence levels agree or explain the difference.
- [ ] Language-only links point to the corresponding page.

## Navigation and site

- [ ] The page is linked from the relevant platform, shared, regional, or operations map.
- [ ] Internal links resolve in GitHub Markdown.
- [ ] python scripts/validate_kb.py passes.
- [ ] mkdocs build --strict passes.
- [ ] The site build does not introduce a second authored copy of the content.

## Release decision

- [ ] Product, engineering, legal/privacy, and release owners know which pages changed.
- [ ] High-risk topics have a follow-up review date.
- [ ] The final release decision rechecks the current Apple App Review Guidelines (https://developer.apple.com/app-store/review/guidelines/) or Google Play Developer Policy Center (https://play.google.com/about/developer-content-policy/).
- [ ] This knowledge base is treated as operational guidance, not as a guarantee of approval.
