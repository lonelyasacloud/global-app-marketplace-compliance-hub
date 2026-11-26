---
id: apple.app-review.rule-decomposition
platform: apple
language: en-US
authority: implementation-note
status: current
kb_checked_at: 2026-11-09
review_due: 2027-02-09
snapshot_package: 2026-11-10
regions: [global]
topics: [review, evidence, safety, performance, business, design, legal]
editorial_note: "Editorial and analytical model from the snapshot checked 2026-11-09 (package 2026-11-10). It is not Apple source text and does not add Apple policy. This import did not re-check live pages. English App Review Guidelines in the snapshot are dated 2026-10-16; the Simplified Chinese official page shows 2026-06-08."
---

# App Review Rule Decomposition Model

## What this page is

This page defines the knowledge base’s rule-unit model. Its evidence level is an **implementation note**. It is not an additional Apple policy, and it does not replace the [guidelines summary](guidelines-summary.en-US.md) or the live official page. It decomposes Apple rules, App Store Connect requirements, deadlines, review evidence, and internal actions into fields a team can execute.

The knowledge-base check date is 2026-11-09 (package dated 2026-11-10). This import did not reopen the live official pages.

## Rule unit

Keep at least these fields on every rule:

| Field | Meaning |
| --- | --- |
| `rule_id` | Apple clause number, App Store Connect page identifier, or stable internal id. |
| `domain` | Safety, Performance, Business, Design, Legal, or an agreement, age-rating, or platform-specific domain. |
| `title_zh` / `title_en` | Bilingual title. Mark `title_zh` as an editorial translation when it is not Apple’s published Chinese text. |
| `authority` | Apple rule, Apple operational guidance, community experience, or internal recommendation. Community experience and internal recommendations are not Apple rules. |
| `source_url` | Current source text. An older page does not override the current page. |
| `source_updated_at` | Source-page update date or announcement date. |
| `effective_at` | When the rule, feature, or rate starts to apply. |
| `deadline_at` | Date by which the work must be finished. Leave empty when there is no single deadline. |
| `scope` | Affected platforms, storefronts, regions, app types, user types, or business models. |
| `triggers` | App functionality, data, configuration, or submission behavior that brings the rule into scope. |
| `must` | What must be done. |
| `must_not` | What is prohibited. |
| `exceptions` | Exceptions by eligibility, region, platform, or business model. |
| `review_evidence` | Accounts, documents, video, qualifications, paths, or screenshots a reviewer needs to see. |
| `test_cases` | Checks product, engineering, QA, and release should run. |
| `failure_signals` | Signs that may lead to rejection, removal, agreement risk, or delay. |
| `remediation` | Pause, fix, disclose, resubmit, or appeal after a problem is found. |
| `owner` | Product, engineering, QA, release, legal, finance, or App Owner. |
| `status` | Current, Upcoming, Effective, Conditional, Historical, or Background. |

## Five review domains

The lists below are the model’s clause map. Use them to choose `domain` and `rule_id`. They are not guideline text. Current wording is the English guidelines. In this snapshot the Simplified Chinese official page still shows June 8, 2026. See the [guidelines summary](guidelines-summary.en-US.md).

### 1. Safety

- 1.1 Harmful, objectionable, pornographic, violent, or misleading content
- 1.2 UGC, AI-generated content, creator content, filtering, reporting, blocking, and remediation after notice
- 1.3 Kids Category, children’s privacy, and parental controls
- 1.4 Medical and health features, dangerous activities, and physical harm
- 1.5–1.7 Developer information, security, and crime reporting

### 2. Performance

- 2.1 App completeness, crashes, URLs, sign-in, backend, and whether IAP can be reviewed
- 2.2 Beta, trial, and demo builds use TestFlight
- 2.3 Metadata, screenshots, previews, creative assets, age rating, and What’s New
- 2.4 Hardware compatibility, power use, and device impact
- 2.5 Public APIs, background services, permissions, WebKit, extensions, ads, and 2.5.19 hidden functionality

### 3. Business

- 3.1 IAP, subscriptions, refunds, randomized virtual items, external purchase links, and regional entitlements
- 3.2 Other business models, finance, medical, VPN, gambling, fundraising, crypto assets, and enterprise services

Dedicated pages for payments, subscriptions, external purchase, and regional terms are not imported. Start with the guidelines summary and the [license summary](../developer-program/license-agreement.en-US.md).

### 4. Design

- 4.1–4.3 Copycats, impersonation, duplicate apps, templated apps, and spam submissions
- 4.4–4.6 Extensions, Apple services, notifications, marketing, and user experience
- 4.7 Mini apps, mini games, chatbots, plug-ins, and emulators
- 4.8 Sign-in, Apple Pay, system capabilities, and commercialization limits on Apple services

### 5. Legal

- 5.1 Privacy, permissions, account deletion, ATT, third-party SDKs, and data lifecycle
- 5.2 Intellectual property and content rights
- 5.3 Games, gambling, lotteries, and contests
- 5.4 VPN, MDM, regulated businesses, and licensing
- 5.5 Other legal obligations
- 5.6 Developer Code of Conduct and developer behavior

## Example: 2.5.19 hidden, dormant, or undocumented functionality

This example decomposes the direction recorded for English guideline 2.5.19: hidden, dormant, or undocumented functionality is prohibited. The triggers, obligations, prohibitions, and closure checks below are an **editorial execution breakdown**. They are not Apple’s clause text, and they do not replace checking the current English guidelines when writing review notes.

### Triggers

- Remote configuration, feature flags, A/B tests, or server-driven behavior
- Different functionality by region, language, user identity, ad entry point, or account permission
- A WebView, third-party domain, dynamic page, or remote asset that changes the user experience
- A configuration during review that differs from the configuration after release

### Must

- Keep the submitted version consistent with the experience that actually ships
- Explain material differences and reproduction steps in App Review Information
- Provide a working review account, test data, a configuration snapshot, and a rollback path
- Freeze critical remote configuration during review

### Must not

- Hide behavior during review and enable it afterward
- Place the review account in a cohort that cannot see the issue
- Hide functionality with obfuscation, a different entry point, or a dynamic web page
- Treat a previous approval as a substitute for disclosure and verification of the current version

### Evidence and closure

- Inventory of feature flags and backend configuration
- Test matrix for account, region, language, device, and user state
- Review notes, demo account, and reproduction video
- Record of the configuration freeze and rollback
- Release decision from legal and the App Owner

Official help for submission materials is the [review workflow](../review-workflow/review-workflow.en-US.md).

## Source and experience layers

When filling a rule unit, take evidence in this order. A lower layer does not override a higher one.

1. **Normative.** The current English guidelines, current App Store Connect Help, and the current agreement plus applicable attachments. English guidelines: [App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/) (page date in the snapshot: October 16, 2026). Simplified Chinese official page: [App Review Guidelines](https://developer.apple.com/cn/app-store/review/guidelines/) (still shows June 8, 2026 in the snapshot; historical translation only). The agreement entry point is the page recorded on the license topic. The supplied [`/cn/` agreement URL](https://developer.apple.com/cn/support/terms/apple-developer-program-license-agreement/) rendered English on 2026-11-09.
2. **Operational.** Apple’s review materials, submission statuses, help pages, and API documentation. Entry point: [App Store Connect Help](https://developer.apple.com/help/app-store-connect/).
3. **Change.** Apple Developer News, RSS, announcement body links, and target pages. See the [news index](../news/news-rss-index.en-US.md). News is not policy text.
4. **Experience.** Apple Developer Forums, Reddit, CSDN, and similar community material are used only to discover test scenarios. They do not change rule priority. See [community evidence](../community-evidence/community-evidence.en-US.md).
5. **Historical.** Older Chinese guidelines, older agreement notices, older news, and expired requirements. Change history only. Do not use them as current terms.
