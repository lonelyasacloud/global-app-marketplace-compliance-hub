---
id: google-play.app-policy-scope-intake
platform: google-play
language: en-US
authority: operational
status: current
kb_checked_at: 2026-10-23
review_due: 2027-01-23
regions: [global]
topics: [scope-intake, release-checklist, navigation]
snapshot_id: play.app-policy-scope-intake
snapshot_package: "GooglePlay-KnowledgeBase-2026-10-24-review.zip"
coverage_status: "operational-router"
source_url: "https://play.google.com/about/developer-content-policy/"
source_url_zh: "https://support.google.com/googleplay/android-developer/answer/9859455?hl=zh-CN"
effective_date: "router only; 2027-01-27 kept separate from other deadlines"
---

> **Import note (Google batch 9).** The body is the paraphrased release router from the already separated 2026-10-24 Google Play knowledge-base snapshot (`play.app-policy-scope-intake`, reviewed 2026-10-23). It is not a verbatim copy of an official page and it is not a compliance finding for any app. The English official source is the source of truth. `kb_checked_at` is the review date recorded in the snapshot source file; this import did not re-open the live official pages. Phrases such as “this knowledge base,” “this library,” and “local topic” describe coverage inside that snapshot, not the set of pages imported into this repository. Relative snapshot links to topics, link graphs, ledgers, or CSVs that are not in this repository are kept as text mentions. Relative links that target Google batch 1–8 topics or these eight batch 9 topics point at the hub files. The Chinese source records the app-review article as `hl=zh-CN` and the deadlines table as `hl=en`. The English source uses `hl=en` for the app-review article. The snapshot does not record a line-by-line comparison of that `hl=zh-CN` review article or a failed fetch. The Chinese hub text is an editorial router. January 27, 2027 is an upcoming Contacts, location, SMS/Call Log, and geofencing-foreground-service preview. It stays separate from the November 1, 2026 extensions, the December 1, 2026 US External Content Links report, February 1, 2027 16 KB compatibility, March 15, 2027 India merchant KYC, and March 31, 2027 Japan external payments. The offline wiki named in the snapshot is not imported. Evidence level: Operational.

# Find Google Play Policies by App Feature

**Reviewed October 23, 2026.** This is a policy-navigation and release-preparation worksheet, not a compliance finding for a particular app. Answer from actual features, audience, data flows, distribution markets, and SDKs. For “Yes” or “Not sure,” open the linked topic and current official source. Support a “No” answer with product, code, and SDK evidence. Missing a trigger here does not exempt an app from the Developer Program Policy, Developer Distribution Agreement, local law, or Play Console requirements.

## 1. Baseline checks for every Play app

| Check | What to verify | Knowledge-base entry |
| --- | --- | --- |
| Developer and app identity | Verify developer details, identity, package registration, signing, and app ownership. If distribution will continue, check Console for unfinished verification or package-registration tasks. | [Play Console Requirements](../play-console-requirements/play-console-requirements.en-US.md), [Android Developer Verification](../android-developer-verification/android-developer-verification.en-US.md), [Developer Distribution Agreement](../developer-distribution-agreement/developer-distribution-agreement.en-US.md) |
| Policy and market scope | Confirm the app's purpose, content, target markets, audience, and monetization. Review applicable policy, regional restrictions, and legal requirements. | [Consolidated Developer Program Policy](../developer-program-policy/developer-program-policy.en-US.md), [Policy Center catalog](../google-play-developer-policy-center/google-play-developer-policy-center.en-US.md), [Country/region distribution](../country-specific-distribution/country-specific-distribution.en-US.md) |
| App content and review access | Check that ads, privacy policy, Data safety, audience, content rating, permissions, and special declarations match the product; give reviewers working access to every restricted feature. | [App review preparation](../app-review-preparation/app-review-preparation.en-US.md), [Console requirements](../play-console-requirements/play-console-requirements.en-US.md), [Testing and release workflow](../publishing/play-release-workflow.en-US.md) |
| Version and device compatibility | Check current target API, form-factor, 64-bit, and 16 KB page-size gates. Target API and 16 KB compatibility are separate requirements. | [Target API and compatibility deadlines](../target-api/target-api-level.en-US.md), [App quality and form factors](../app-quality-and-form-factor-guidelines/app-quality-and-form-factor-guidelines.en-US.md) |
| Permissions, data, and SDKs | Review the final merged Manifest, runtime permissions, background work, and SDK/library data and network behavior. Keep declarations, privacy materials, and actual behavior aligned. | [Android privacy checklist](../android-privacy-checklist/android-privacy-checklist.en-US.md), [User Data](../user-data/user-data.en-US.md), [Data safety](../data-safety/data-safety.en-US.md), [Third-party SDKs](../sdk-requirements/sdk-requirements.en-US.md) |
| Submission, release, and ongoing status | Retain reproducible builds, test results, reviewer credentials, and declaration status. Recheck declarations after feature, data, SDK, audience, market, or pricing changes; monitor Policy status and official deadlines. | [Release workflow](../publishing/play-release-workflow.en-US.md), [Operations register](../google-play-policy-operations/google-play-policy-operations.en-US.md), Offline Wiki deadline view (snapshot: `google-play-policy-wiki.html`, not imported in this repository) |

## 2. Route by product feature

If an answer is “Yes” or “Not sure,” follow the local links to review policy, implementation guidance, and declaration requirements. Actual applicability depends on current official terms and the tasks shown in the developer's Console.

| Does the app… | Start with | Evidence to prepare |
| --- | --- | --- |
| Target children or may be used by children; include social, dating, anonymous, or random chat features | [Age restrictions and child safety](../age-restricted-child-safety/age-restricted-child-safety.en-US.md), [Content ratings](../content-ratings/content-ratings.en-US.md), [UGC moderation](../user-generated-content/user-generated-content.en-US.md) | Audience rationale, age gate/restriction flow, child-safety declarations, report/block and response records, age-appropriate ads/SDK inventory |
| Let users upload, publish, comment, message, livestream, or share content | [UGC moderation](../user-generated-content/user-generated-content.en-US.md), [Child safety](../age-restricted-child-safety/age-restricted-child-safety.en-US.md), [Inappropriate content](../inappropriate-content/inappropriate-content.en-US.md) | User terms, content rules, report/block paths, moderation coverage and escalation records, examples of enforcement |
| Generate or edit AI content, or show AI output to other users | [AI-generated content and safety practices](../ai-generated-content/ai-generated-content.en-US.md), [UGC](../user-generated-content/user-generated-content.en-US.md), [Inappropriate content](../inappropriate-content/inappropriate-content.en-US.md) | Output-risk tests, filters/moderation rules, in-app reporting, false-positive/negative handling, version records |
| Collect, access, share, or sell personal/sensitive data, including through an SDK | [User Data](../user-data/user-data.en-US.md), [Data safety](../data-safety/data-safety.en-US.md), [Android privacy checklist](../android-privacy-checklist/android-privacy-checklist.en-US.md), [Third-party SDKs](../sdk-requirements/sdk-requirements.en-US.md) | Data-flow and recipient inventory, SDK versions/purposes, privacy policy, Data safety answers, disclosure/consent UI, retention and deletion records |
| Create user accounts or let users connect third-party accounts | [Account and associated-data deletion](../account-deletion/account-deletion.en-US.md), [Data safety](../data-safety/data-safety.en-US.md) | Test the web request in a browser after uninstall; record the in-app path, associated-data/provider deletion, handling time, retention basis/period, and Data safety answers |
| Request Contacts, precise/background location, photos/videos, SMS/Call Log, all-files access, app inventory, Accessibility, package installation, or health permissions | [Sensitive permissions overview](../sensitive-permissions/sensitive-permissions.en-US.md), [Permissions declarations](../permissions-declaration/permissions-declaration.en-US.md), and [Contacts/location](../contacts-location-permissions/contacts-location-permissions.en-US.md), [Photo/video](../photo-video-permissions/photo-video-permissions.en-US.md), [SMS/Call Log](../sms-call-log/sms-call-log.en-US.md), [Background location](../background-location/background-location.en-US.md), [Health/Health Connect](../health-apps-and-health-connect/health-apps-and-health-connect.en-US.md) | Merged Manifest, core-feature rationale, system-alternative tests, permission timing, prominent disclosure/consent, Console declaration and reviewer video |
| Use foreground services, background location, geofencing, or long-running background tasks | [Foreground services and geofencing](../foreground-services-and-geofencing/foreground-services-and-geofencing.en-US.md), [Background location](../background-location/background-location.en-US.md) | Service type/permission, user-visible task rationale, stop path, background-start tests, location disclosure and Console declaration |
| Show ads/sponsored content, promote apps, or acquire users through ratings/reviews/installs | [Ads and promotion](../ads-and-advertising/ads-and-advertising.en-US.md), [Ratings/reviews/installs](../user-ratings-reviews-installs/user-ratings-reviews-installs.en-US.md), [Store listing best practices](../store-listing-best-practices/store-listing-best-practices.en-US.md) | Ad SDK/placement inventory, audience/rating suitability, asset rights, promotion copy, review incentives, install-source review |
| Sell digital content/subscriptions/random virtual items, or link users to off-Play purchases/downloads | [Payments, billing, and subscriptions](../payments/payments-and-subscriptions.en-US.md), [Country/region distribution](../country-specific-distribution/country-specific-distribution.en-US.md) | Play Billing scope, enrollment/approval for the applicable program, pricing/renewal/cancellation, transaction reports, user support, market rules |
| Offer loans/financial services, crypto/NFTs, real-money gambling, health/medical, or news features | [Financial services/loans](../financial-services-and-loans/financial-services-and-loans.en-US.md), [Crypto assets](../crypto-assets-and-nfts/crypto-assets-and-nfts.en-US.md), [Real-money gambling](../real-money-gambling/real-money-gambling.en-US.md), [Health apps](../health-apps-and-health-connect/health-apps-and-health-connect.en-US.md), [News/magazines](../news-and-magazines/news-and-magazines.en-US.md) | Actual feature/category declarations, licenses/regulatory basis, market eligibility, age/region controls, health declarations and supporting material |
| Serve government use cases, reference third-party brands/works, or rely on external content/authorization | [Intellectual property](../intellectual-property/intellectual-property.en-US.md), [Impersonation](../impersonation/impersonation.en-US.md), [Misrepresentation](../misrepresentation/misrepresentation.en-US.md), [Country/region topic](../country-specific-distribution/country-specific-distribution.en-US.md) | Rights chain/written authorization, government authorization/source disclosures, market/territory/term, consistency of store materials |
| Publish e-books or audiobooks through Google Play Books Partner Center | [Play Books publisher content policies](../google-play-books-content-policies/google-play-books-content-policies.en-US.md) | Publication rights, format/preview, mature-content and territory settings, publisher account, complaint-handling records. Evaluate Books publisher requirements separately from Android app policy. |
| Include native `.so` libraries, a game engine, or third-party binary SDK | [Target API and 16 KB pages](../target-api/target-api-level.en-US.md), [Third-party SDKs](../sdk-requirements/sdk-requirements.en-US.md) | Native-library inventory for all shipped ABIs, ZIP/ELF alignment report, vendor compatibility confirmation, 16 KB test results |
| Use a new personal developer account or distribute through certified devices/open-source platforms/third-party stores | [Testing and release workflow](../publishing/play-release-workflow.en-US.md), [Play Console Requirements](../play-console-requirements/play-console-requirements.en-US.md), [Android Developer Verification](../android-developer-verification/android-developer-verification.en-US.md) | Account type/creation date, closed-test records, device verification, package/signing ownership evidence, distribution channels and install flow |

## 3. Prioritize work by date

This is an **October 23, 2026** snapshot. The [official Policy Deadlines page](https://support.google.com/googleplay/android-developer/table/12921780?hl=en) was rechecked on this date and lists four changes effective January 27, 2027; the table also includes program milestones tracked in their official topics. Use dates to prioritize; verify eligibility, extensions, program participation, and app status on official pages and in the developer account.

| Date | Action if applicable | Entry |
| --- | --- | --- |
| November 1, 2026 | If an app received an eligible Target API or Billing Library v7 warning, handle the extension separately in its own Policy status/Console task. The two requests are independent. | [Target API](../target-api/target-api-level.en-US.md), [Payments/subscriptions](../payments/payments-and-subscriptions.en-US.md), [operations register](../google-play-policy-operations/google-play-policy-operations.en-US.md) |
| December 1, 2026 | Only External Content Links participants: verify successful-download reporting and applicable service fees. | [US External Content Links](../us-external-content-links/us-external-content-links.en-US.md), [operations register](../google-play-policy-operations/google-play-policy-operations.en-US.md) |
| January 27, 2027 | If the app uses Contacts, precise location, phone-account verification, SMS/Call Log, or geofencing as an FGS use case, migrate and update declarations as required by the linked topics. | [Contacts/location](../contacts-location-permissions/contacts-location-permissions.en-US.md), [SMS/Call Log](../sms-call-log/sms-call-log.en-US.md), [foreground services](../foreground-services-and-geofencing/foreground-services-and-geofencing.en-US.md) |
| February 1, 2027 | For Play apps targeting API 35+ with 64-bit native libraries, finish 16 KB compatibility checks; incompatible updates cannot be released. | [Target API and 16 KB pages](../target-api/target-api-level.en-US.md) |
| March 15, 2027 | Only India-based merchants selling outside India: check the Payments topic's BillDesk merchant-KYC deadline and account requirements. | [Payments/subscriptions](../payments/payments-and-subscriptions.en-US.md), [operations register](../google-play-policy-operations/google-play-policy-operations.en-US.md) |
| March 31, 2027 | Only existing Japan External Payments participants who want to continue external payment links: complete the transition to Billing Choice. | [Payments/subscriptions](../payments/payments-and-subscriptions.en-US.md), [operations register](../google-play-policy-operations/google-play-policy-operations.en-US.md) |

Deadlines change. See the filterable offline Wiki deadline view (snapshot: `google-play-policy-wiki.html`, not imported in this repository) and [operations register](../google-play-policy-operations/google-play-policy-operations.en-US.md) for the maintained snapshot and historical status; still verify the official page online before release.

## 4. Suggested release-review sequence

1. Record package name, account type, target users, distribution markets, monetization, and actual features. Include uncertain features in the review scope until confirmed otherwise.
2. Check permissions, SDKs, data flows, native libraries, ads, and payment behavior from the final build, not only from source code.
3. Open every triggered topic above and follow its official-source table for declarations, exceptions, and market-specific rules.
4. Compare App content, Data safety, privacy policy, store listing, content rating, reviewer credentials, and Console warnings/deadlines against the current product.
5. Keep evidence that supports each decision, retest after fixes, and repeat the relevant branches after feature, SDK, market, audience, or policy changes.

## 5. Use Play Policy Insights for code review

The [Android Play Policy Insights skill](https://github.com/android/skills/tree/main/play/play-policy-insights) is an automated review tool for Android app repositories; it is not policy text, a Play review decision, or a compliance certification. The installed copy's metadata says it was last updated July 13, 2026. It requires particular attention to Data safety, reviewer login credentials, and restricted permissions. Its `policies.json` lists 16 audit domains and 31 official source URLs; all 31 URLs are present in this knowledge base's source ledger as of October 23, 2026. A URL record does not mean every descendant has been closed.

Run the skill against an Android app repository, not this knowledge-base folder. Map its findings to the topics below, then manually compare them with the final build, merged Manifest, SDK behavior, Data safety/store materials, reviewer credentials, and account-specific Play Console tasks. Static code signals alone cannot prove runtime data flows, account state, or Play approval.

| Skill audit domain | Knowledge-base topics |
| --- | --- |
| Data safety section | [User Data](../user-data/user-data.en-US.md), [Data safety](../data-safety/data-safety.en-US.md) |
| Login credentials | [App review preparation](../app-review-preparation/app-review-preparation.en-US.md), [Play Console Requirements](../play-console-requirements/play-console-requirements.en-US.md) |
| SMS and Call Log | [SMS and Call Log](../sms-call-log/sms-call-log.en-US.md), [Sensitive Permissions](../sensitive-permissions/sensitive-permissions.en-US.md) |
| Package visibility | [Sensitive Permissions](../sensitive-permissions/sensitive-permissions.en-US.md) |
| All files access | [Sensitive Permissions](../sensitive-permissions/sensitive-permissions.en-US.md), [Permissions declaration](../permissions-declaration/permissions-declaration.en-US.md) |
| Photo and video | [Photo and video permissions](../photo-video-permissions/photo-video-permissions.en-US.md), [Sensitive Permissions](../sensitive-permissions/sensitive-permissions.en-US.md) |
| Location | [Contacts and foreground location](../contacts-location-permissions/contacts-location-permissions.en-US.md), [Background location](../background-location/background-location.en-US.md) |
| Contacts | [Contacts and foreground location](../contacts-location-permissions/contacts-location-permissions.en-US.md) |
| Audio recording | [User Data](../user-data/user-data.en-US.md), [Sensitive Permissions](../sensitive-permissions/sensitive-permissions.en-US.md) |
| Files and docs | [Sensitive Permissions](../sensitive-permissions/sensitive-permissions.en-US.md), [Android Privacy Checklist](../android-privacy-checklist/android-privacy-checklist.en-US.md) |
| Prominent disclosure | [User Data](../user-data/user-data.en-US.md), [Android Privacy Checklist](../android-privacy-checklist/android-privacy-checklist.en-US.md) |
| Account deletion | [Account and associated-data deletion](../account-deletion/account-deletion.en-US.md) |
| Target API level | [Target API and compatibility deadlines](../target-api/target-api-level.en-US.md) |
| Accessibility API | [Sensitive Permissions](../sensitive-permissions/sensitive-permissions.en-US.md), [User Data](../user-data/user-data.en-US.md) |
| Exact alarms | [Sensitive Permissions](../sensitive-permissions/sensitive-permissions.en-US.md), [Foreground services and geofencing](../foreground-services-and-geofencing/foreground-services-and-geofencing.en-US.md) |
| Foreground services | [Foreground services and geofencing](../foreground-services-and-geofencing/foreground-services-and-geofencing.en-US.md), [Background location](../background-location/background-location.en-US.md) |

## 6. Scope and related entry points

This router locates selected topics already in the library. Policy Center and Console content changes; signed-in forms, local law, external-program eligibility, and descendants not yet expanded in each topic require online review. “Not sure” is not a violation finding, and “not triggered” is not proof of compliance.

- [Policy Center catalog](../google-play-developer-policy-center/google-play-developer-policy-center.en-US.md) · Recursive link graph (snapshot: `google-play-policy-link-graph-en.md`, not imported in this repository) · Per-URL source ledger (snapshot: `SOURCE_LEDGER-en.md`, not imported in this repository)
- [Policy announcement timeline](../google-play-policy-announcements/google-play-policy-announcements.en-US.md) · [Announcement child-link analysis](../google-play-announcement-resources/google-play-announcement-resources.en-US.md)
- [中文版本 / Chinese version](../app-policy-scope-intake/app-policy-scope-intake.en-US.md)
