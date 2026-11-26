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

## Imported in Google batch 2

Seven paired topics from the same 2026-10-24 snapshot. `kb_checked_at` on those pages is the review date recorded in each snapshot source file. This import did not re-open the live official pages. Package date remains 2026-10-24.

These topics stay separate from User Data and Data Safety. The User Data page keeps its short account-deletion summary and links to the standalone topic.

| Topic | Hub path | Snapshot id | Review date in source | Authority | Status |
| --- | --- | --- | --- | --- | --- |
| Sensitive permissions and APIs | `docs/google-play/sensitive-permissions/` | `play.sensitive-permissions` | 2026-10-24 | normative | current |
| Permissions declaration and review | `docs/google-play/permissions-declaration/` | `play.permissions-declaration` | 2026-10-22 | operational | current |
| Background location | `docs/google-play/background-location/` | `play.background-location` | 2026-10-23 | normative | current |
| SMS and Call Log | `docs/google-play/sms-call-log/` | `play.sms-call-log` | 2026-10-24 | normative | current |
| Photo and video permissions | `docs/google-play/photo-video-permissions/` | `play.photo-video-permissions` | 2026-10-23 | normative | current |
| Account deletion | `docs/google-play/account-deletion/` | `play.account-deletion` | 2026-10-24 | normative | current |
| Target API level requirements | `docs/google-play/target-api/` | `play.target-api-level` | 2026-10-24 | normative | current |

Chinese hub text is an editorial paraphrase from the snapshot, not Google's published Chinese page text, except where a source file records that a Chinese official page was actually opened. English official pages are the source of truth. Relative snapshot links that target these seven topics or the batch 1 topics point at the hub files. Relative links to topics, link graphs, ledgers, and CSVs that are not in this repository are text mentions. Phrases such as “this knowledge base” inside the imported pages describe the snapshot library, not the pages present in this repository.

Android API and migration material on these pages is an implementation note. It does not by itself establish Play eligibility.

### Official-page language gaps and dated previews recorded in the snapshot

1. **Sensitive permissions.** Reviewed 2026-10-24. The English consolidated article and its linked policy preview were reopened. The current `hl=zh-CN` page could not be fetched. The Chinese hub page is a structured translation from the English article and that preview, not an independent line-by-line review of a Chinese official page. The article shows both rules already in effect and changes effective 2027-01-27, including the contacts and location preview. Those dates stay separate. The failed fetch is not a policy change.
2. **Permissions declaration.** Reviewed 2026-10-22. The English Help body and the Simplified Chinese page were both opened, and the snapshot says the substantive body links match. It does not record a failed fetch of this primary article. The linked Sensitive Permissions page announces location and contacts changes effective 2027-01-27; those future changes are not current declaration-form rules. The Play Academy course link returned Cache miss, and no course content is inferred from the title.
3. **Background location.** Reviewed 2026-10-23. The snapshot records that the current English article was opened. It does not record a failed `hl=zh-CN` fetch, or a Chinese-versus-English lag, for this primary Help article. The Chinese hub text is the snapshot's structured paraphrase. Descendant fetch errors, including a legacy User Data URL, stay access limits and are not policy changes. Play's removal of geofencing as an approved foreground-service use case is dated 2027-01-27 in the source and is not folded into the current background-location rules.
4. **SMS and Call Log.** Reviewed 2026-10-24. The snapshot says the Chinese article could not be reliably retrieved, so the Chinese hub page is an organized translation of the official English text. Separately, the `hl=zh-Hans` article still showed the old exception table and did not show the English update notice or the newer Digital Credentials and Incoming Call Retriever alternatives. That omission is not evidence that the announced date changed. Current policy still lists general account verification by phone call. The preview removes that `READ_CALL_LOG` exception on 2027-01-27. The July 15, 2026 announcement's general minimum 30-day window does not replace that date. Banking and brokerage call-based authentication remains a separate use case in the source. A failed or incomplete Chinese fetch is not a policy change.
5. **Photo and video permissions.** Reviewed 2026-10-23 in the snapshot YAML. The body also says the shared parent Help page was opened in full on 2026-10-22, and the closing line dates the paraphrase to official pages available on 2026-10-23. Those two snapshot dates are not treated as a policy change. The snapshot calls the page a bilingual paraphrase and does not record a failed `hl=zh-CN` fetch for this primary article. The same parent page states Contacts rules effective 2027-01-27. The photo and video full-compliance date in the source is 2025-05-28, which the snapshot says has passed. Those dates stay separate.
6. **Account deletion.** Reviewed 2026-10-24. The English Help article and the Simplified Chinese `hl=zh-Hans` body were reopened and agree on the core requirements. The exact `hl=zh-CN` route was inaccessible; the Chinese content check used the opened `zh-Hans` page. That failure is not a content change. December 7, 2023 and May 31, 2024 remain expired migration dates. The Chinese hub text is the snapshot paraphrase, not Google's published Chinese page text.
7. **Target API.** Reviewed 2026-10-24. The `?hl=zh-CN` Play Help view remained inaccessible, so the Chinese summary of the Play rules is based on the readable English body. That failure is not a policy change. The English and Simplified Chinese Android migration-guide views were both read and remained aligned. Their footers show October 16 and “Last updated (UTC): October 17,” with no corresponding policy-content difference recorded in the snapshot.

## Planned next import

- UGC, children, content ratings, deceptive behavior, and enforcement
- Announcement archive, link graph, URL audit, and source-target ledger

## Handling notes

The snapshot is a point-in-time working source. Android implementation guidance is kept separate from Play eligibility. Access failures, sign-in gates, partial pages, redirects, and historical targets must remain visible in the source ledger.

Google batch 1 and Google batch 2 do not import the offline wiki HTML, link graphs, URL-audit CSVs, announcement archives, or the remaining snapshot topics. The consolidated Developer Program Policy effective date recorded in the snapshot remains September 30, 2026.
