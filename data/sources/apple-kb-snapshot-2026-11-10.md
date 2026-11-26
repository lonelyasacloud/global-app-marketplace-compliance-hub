# Apple KB Snapshot Inventory / Apple 知识库快照清单

## Source package

AppleStore_Compliance_KB_v1.1_2026-11-10.zip

## Snapshot contents

The supplied snapshot contains a bilingual App Store compliance summary, pre-submission checklist, rule-decomposition model, review workflow, age-rating guide, license-agreement summary, embedded-link index, Apple News index, community evidence, maintenance notes, and an offline HTML reader.

## Imported in Phase 1

- Apple platform navigation
- Apple review-readiness guide in Chinese and English
- Shared privacy baseline
- Submission quick check
- Rejection and appeals workflow
- Source and editorial policy

## Imported core topics

Imported from this snapshot as paired `zh-CN` / `en-US` pages. `kb_checked_at` is 2026-11-09 (snapshot check). The package date is 2026-11-10. This import did not re-open the live official pages. Summaries are operational and are not Apple source text. Review-readiness and the cross-platform quick check were left in place; the new checklist links to both.

| Topic | Pages | Baseline recorded in the snapshot |
| --- | --- | --- |
| Pre-submission checklist | `docs/apple-app-store/pre-submission/submission-checklist` | Operational checklist. Official Help links are in the page. Items that restate English guideline changes after 2026-06-08 are labeled as editorial translation in Chinese. |
| App Review Guidelines summary | `docs/apple-app-store/app-review-guidelines/guidelines-summary` | English guidelines updated 2026-10-16. Simplified Chinese official page shows 2026-06-08. In-snapshot guideline comparison dated 2026-10-21. Chinese wording for later English rules is an editorial translation, not Apple’s published Chinese text. |
| Review workflow, submission objects, statuses, and timing | `docs/apple-app-store/review-workflow/review-workflow` | Operational summary of App Store Connect Help, submission statuses, and the snapshot’s recorded deadlines (age-rating declarations by 2027-01-12, Taiwan storefront rate from 2026-10-31, SDK 27 from April 2027). |
| Age-rating values and definitions | `docs/apple-app-store/age-ratings/age-ratings` | English and Simplified Chinese Help URLs are both cited. The snapshot does not record a date lag between those two Help pages. Shared Location and Dating and Relationships dates come from the English notice of 2026-11-02. Chinese wording of that notice is an editorial summary. |
| Developer Program license agreement summary | `docs/apple-app-store/developer-program/license-agreement` | The supplied `/cn/` agreement URL rendered English on 2026-11-09. The October 13, 2026 amendment notice said a translation would follow within one month. The Chinese page is an editorial summary, not Apple’s published translation or legal advice. August 18, 2026 agreement notice is historical only. |

### Official-page gap kept with this import

English [App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/) show **October 16, 2026**. The Simplified Chinese page shows **June 8, 2026**. Apple’s [October 16, 2026 update notice](https://developer.apple.com/news/?id=92th7e5i) says translations will be published within one month. Until the localized guidelines page is updated, English is the policy baseline. Hub Chinese for those newer rules is an editorial translation.

The license page has a separate language fact: the supplied [Chinese-path agreement URL](https://developer.apple.com/cn/support/terms/apple-developer-program-license-agreement/) rendered English, and the [October 13, 2026 amendment notice](https://developer.apple.com/news/?id=17mwd36z) said a translation would follow within one month.

Not imported as topics from the orientation files: `index.html`, `README.md`, and `START-HERE.md`. `maintenance.md` was not imported as its own topic. Its source list, the October 16, 2026 change paraphrase, and the changelog dates already inform the guidelines summary and this inventory. The embedded-link catalog keeps its own crawl date of 2026-10-21. Version-gap notes that the core topics rely on stay in the guidelines summary, the license summary, and this inventory.

## Imported reference indexes and the rule model

Imported from the same 2026-11-10 package as paired `zh-CN` / `en-US` pages. `kb_checked_at` remains 2026-11-09. This import did not re-open the live official pages and did not re-parse the RSS XML. None of these pages is Apple source text.

| Topic | Pages | What it is |
| --- | --- | --- |
| Rule-decomposition model | `docs/apple-app-store/app-review-guidelines/rule-decomposition` | Editorial and analytical model for rule units, domains, and an example breakdown of guideline 2.5.19. Authority is an implementation note. It does not add Apple policy. |
| Embedded official-link catalog | `docs/apple-app-store/app-review-guidelines/embedded-links` | Operational index of direct links in the English and Simplified Chinese guideline bodies, crawled in the snapshot on 2026-10-21. Unresolved form URLs were not guessed. Some design links returned a crawler 404. Not a policy rule. |
| Apple news / changelog index | `docs/apple-app-store/news/news-rss-index` | Operational and historical index of selected 2026 announcements. The RSS XML item count, feed boundary, and raw `pubDate` values remain unverified. P3 is background. The August 18, 2026 agreement notice is historical only. |
| News source-link targets | `docs/apple-app-store/news/news-link-targets` | Operational map from those announcements to target pages, including read, partial, and unread status. Unread link labels are not confirmed policy. |
| Community evidence | `docs/apple-app-store/community-evidence/community-evidence` | Community evidence only. Tier C reports may become test cases. Tier D material is excluded from any execution plan. Quora was blocked by robots.txt and is not included. |

## Planned next import

These items are still not imported. They were **not full source texts in the 2026-11-10 snapshot package** attached for this import. Do not treat a mention inside the news index, the embedded-link catalog, or community evidence as a substitute topic.

- Full App Review Guidelines topic map. The guidelines summary and the rule-decomposition model are imported. A page per guideline is not.
- Children-specific topic beyond the age-rating page. Age ratings were imported with the core topics. A separate children topic is not in this package.
- Privacy Manifest and Required Reason API detail. Not in this snapshot package. Community evidence only points at the official documentation URLs as troubleshooting back-references.
- App Privacy Details and ATT as their own topic. Not in this snapshot package. The EU ATT notice is only a news-index row.
- IAP, subscriptions, external purchase, and regional terms. Not in this snapshot package as topic source. Related rows exist only inside the news index, the news target map, the license summary, and the embedded-link catalog.

## Handling notes

The snapshot is a point-in-time working source. Its summaries are not Apple source text. Each imported topic must retain the official URL, source update date, knowledge-base review date, and any English/Chinese version gap.
