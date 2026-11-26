# Google Play KB Snapshot Inventory / Google Play 知识库快照清单

## Source package

GooglePlay-KnowledgeBase-2026-10-24-review.zip

## Snapshot contents

The supplied snapshot contains paired Chinese and English Google Play policy topics, Policy Center and Help link graphs, URL audit CSVs, source ledgers, policy announcements, Play Console workflows, publishing readiness, permissions, Data Safety, payments, child safety, content, device and network abuse, Android implementation references, and an offline HTML reader.

The package's own start page records 176 Markdown knowledge files, 87 explicit Chinese/English pairs, two combined-language references, source-link inventories, and manual access states for current targets.

## Imported in Phase 1

- Google Play platform navigation
- Google Play Data Safety baseline in Chinese and English
- Shared privacy baseline
- Submission quick check
- Source registry and editorial policy
- Regional and deadline navigation

## Imported in Google batch 1

Six paired topics from the 2026-10-24 snapshot. `kb_checked_at` on those pages is the review date recorded in the snapshot source file. This import did not re-open the live official pages.

The Developer Distribution Agreement, the consolidated Developer Program Policy, Play Console release operations, and Data Safety declarations stay separate. The Phase 1 Data Safety baseline remains in place and links to the detailed form topic.

| Topic | Hub path | Snapshot id | Review date in source | Authority | Status |
| --- | --- | --- | --- | --- | --- |
| Developer Distribution Agreement | `docs/google-play/developer-distribution-agreement/` | `play.developer-distribution-agreement` | 2026-10-24; agreement body viewed 2026-10-22 | normative | current |
| Consolidated Developer Program Policy | `docs/google-play/developer-program-policy/` | `play.developer-program-policy` | 2026-10-24 | normative | current |
| User Data | `docs/google-play/user-data/` | `play.user-data` | 2026-10-24 | normative | current |
| Data safety form | `docs/google-play/data-safety/data-safety.*.md` | `play.data-safety` | 2026-10-24 | operational | partial |
| Payments, billing, and subscriptions | `docs/google-play/payments/` | `play.payments-subscriptions` | 2026-10-24 | normative | current |
| Testing, review, and release workflow | `docs/google-play/publishing/` | `play.release-workflow` | 2026-10-22 | operational | current |

Chinese hub text is an editorial paraphrase from the snapshot, not Google's published Chinese page text. English official pages are the source of truth. Relative snapshot links that target these six topics point at the hub files. Relative links to topics, link graphs, ledgers, and CSVs that are not in this repository are text mentions. Phrases such as “this knowledge base” inside the imported pages describe the snapshot library, not the pages present in this repository.

### Official-page language gaps recorded in the snapshot

1. **Developer Program Policy.** Effective 2026-09-30 unless the official page says otherwise. Older wording is not treated as current. On 2026-10-24 the English body and the readable `hl=zh-Hans` Simplified Chinese body were opened. The `hl=zh-CN` route returned a fetch error.
2. **Developer Distribution Agreement.** The English page says effective 2025-09-15. Section 16.1 says English controls and translations are for reference. The Simplified Chinese page is the locale path `https://play.google/intl/ALL_cn/developer-distribution-agreement.html`, and the snapshot records its date line as the malformed “2025 年92 月 15 日”. During the 2022→2023 comparison, Google's change-summary page rendered in German; the clause text used for that comparison came from the English agreement bodies. The snapshot pair is not section-identical: the Chinese file has a clause index and a short project checklist, and the English file keeps a one-line section note and places the External Content Links cross-reference under “Related program terms.”
3. **Data safety form.** `hl=zh-CN` redirects to `hl=zh-Hans`. Google warns that the Chinese Help page may contain AI-translated content. Both locales still leave an unexplained form-field boundary between the general ephemeral-processing rule and a narrower FAQ. Some Android metadata schema descriptions on the Chinese route remain in English. Technical, course, media, and signed-in Console descendants are partial.
4. **User Data.** The readable Simplified Chinese route recorded in the snapshot is `hl=zh-Hans`. A retry on 2026-10-24 returned HTTP 429 for English and HTTP 500 for the Chinese route. The snapshot did not treat that failure as a content change, because an earlier full read the same day had succeeded. The prominent-disclosure best-practices page was read in English and still cites the historical Data safety date 2022-07-20.
5. **Payments and subscriptions.** The English and Simplified Chinese Payments Help bodies were both opened. The Subscriptions policy `hl=zh-CN` URL was inaccessible, so that check used the English page. The Simplified Chinese variant of the supported-locations Help article was inaccessible. Merchant guidelines returned Cache miss on the English and Simplified Chinese routes tried in the snapshot. The EEA External Offers terms recorded there say the English text controls and translations are for reference. Android Billing and API material on the page is implementation guidance.
6. **Release workflow.** The primary source recorded in the snapshot is the English *Prepare and roll out a release* Help article, reviewed 2026-10-22. The snapshot does not record a separate Chinese-versus-English lag for that primary guide. The Chinese file is an editorial paraphrase. Two snapshot metadata URLs, white-label best practices and publishing tips, use `hl=zh-CN` in the Chinese source file and `hl=en` in the English source file, and those exact URLs are not repeated in the article body.

## Planned next import

- Sensitive permissions and declaration workflows
- Account deletion, background location, SMS/call log, and photo/video permissions
- Target API level requirements
- UGC, children, content ratings, deceptive behavior, and enforcement
- Announcement archive, link graph, URL audit, and source-target ledger

## Handling notes

The snapshot is a point-in-time working source. Android implementation guidance is kept separate from Play eligibility. Access failures, sign-in gates, partial pages, redirects, and historical targets must remain visible in the source ledger.

Google batch 1 does not import the offline wiki HTML, link graphs, URL-audit CSVs, announcement archives, or the remaining snapshot topics. The consolidated Developer Program Policy effective date recorded in the snapshot remains September 30, 2026.
