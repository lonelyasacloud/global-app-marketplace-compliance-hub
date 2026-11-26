---
id: apple.app-review.embedded-links
platform: apple
language: en-US
authority: operational
status: partial
kb_checked_at: 2026-11-09
review_due: 2027-02-09
snapshot_package: 2026-11-10
regions: [global]
topics: [review, sources, guidelines]
editorial_note: "Operational link catalog, not a policy rule. The catalog crawl inside the snapshot is dated 2026-10-21. kb_checked_at is the package check 2026-11-09. This import did not re-crawl the links. English guidelines in the snapshot are dated 2026-10-16; the Simplified Chinese official page shows 2026-06-08. Some form URLs did not resolve, and some design links returned a crawler 404. The supplied /cn/ license URL rendered English on 2026-11-09; that later fact is noted below and does not rewrite the 2026-10-21 catalog row."
---

# Embedded Links Index

## What this page is

This page is an operational link catalog, not a review rule. It lists direct links in the body of both guideline pages, including the “Before You Submit” and “After You Submit” sections. Duplicate destinations are merged. Header, footer, global navigation, same-page anchors, and second-level links from linked pages are not embedded guideline links.

English URLs are the canonical references. A Simplified Chinese page is listed when this crawl confirmed it. A listed resource does not mean the feature applies to every app or storefront.

The catalog’s own crawl date is **2026-10-21**. `kb_checked_at` is the snapshot package check on **2026-11-09** (package dated 2026-11-10). This import did not re-crawl the links.

Source pages:

- [App Review Guidelines (English)](https://developer.apple.com/app-store/review/guidelines/), page date in the snapshot: October 16, 2026
- [App Review Guidelines (Simplified Chinese)](https://developer.apple.com/cn/app-store/review/guidelines/), still showing June 8, 2026 in the snapshot

The English page is the current policy baseline. The Chinese official page is an older translation. The creative-asset link for guideline 2.3.14 appeared only on the English guidelines in this crawl; the Chinese guidelines page had not yet been updated. The rule summary is the [guidelines summary](guidelines-summary.en-US.md).

## 1. Distribution, notarization, and eligibility

| Resource | English source | Chinese source | Guideline context |
| --- | --- | --- | --- |
| Alternative app marketplaces | [Apple Developer Documentation](https://developer.apple.com/documentation/marketplacekit/participating-in-alternative-distribution-for-specific-regions) | The Chinese guidelines page links to the same English document | Introduction |
| Web distribution | [Apple Developer Documentation](https://developer.apple.com/documentation/marketplacekit/distributing-your-app-from-your-website) | The Chinese guidelines page links to the same English document | Introduction |
| Submit an iOS/iPadOS app for notarization | [App Store Connect Help](https://developer.apple.com/help/app-store-connect/managing-alternative-distribution/submit-for-notarization) | [提交至公证审核](https://developer.apple.com/cn/help/app-store-connect/managing-alternative-distribution/submit-for-notarization) | Introduction and notarization-scoped rules |
| Entitlements | [Entitlements documentation](https://developer.apple.com/documentation/bundleresources/entitlements) | Same English document | Introduction; alternative browser engines |
| App Store Improvements | [App Review Help](https://developer.apple.com/help/app-review/safe-and-trusted-store/app-store-improvements) | [Chinese help page](https://developer.apple.com/cn/help/app-review/safe-and-trusted-store/app-store-improvements) | Before submission; ongoing maintenance |
| Changes for apps in the EU | [Apple Developer Support](https://developer.apple.com/support/apps-in-the-eu) | [Chinese support page](https://developer.apple.com/cn/support/apps-in-the-eu) | Distribution, payments, and regional scope |
| Alternative browser-engine entitlements (EU and Japan) | [Using alternative browser engines in the EU](https://developer.apple.com/support/alternative-browser-engines/) | [Chinese EU page](https://developer.apple.com/cn/support/alternative-browser-engines/) | Guideline 2.5.6 |

## 2. Preparation, review information, and developer docs

| Resource | English source | Chinese source | Guideline context |
| --- | --- | --- | --- |
| Test compatible devices | [App Review Help](https://developer.apple.com/help/app-review/before-submitting-for-review/test-compatible-devices) | — | Before You Submit |
| Configure In-App Purchases for review | [App Review Help](https://developer.apple.com/help/app-review/before-submitting-for-review/configure-in-app-purchases) | — | Before You Submit |
| Complete-review information and regulatory documents | [App Review Help](https://developer.apple.com/help/app-review/before-submitting-for-review/complete-review) | — | Before You Submit; the required-document link resolves to this help topic |
| SwiftUI | [Apple Developer Documentation](https://developer.apple.com/documentation/swiftui) | Same English document | Developer documentation |
| Public API documentation entry | [Documentation](https://developer.apple.com/documentation/) | The Chinese guidelines page uses the same entry point | Guideline 2.5.1 |
| UIKit | [Apple Developer Documentation](https://developer.apple.com/documentation/uikit) | Same English document | Developer documentation |
| AppKit | [Apple Developer Documentation](https://developer.apple.com/documentation/appkit) | Same English document | Developer documentation |
| App extensions | [Apple Developer Documentation](https://developer.apple.com/documentation/technologyoverviews/app-extensions) | Same English document | Developer documentation; extensions |
| Optimize app data for iCloud Backup | [Apple Developer Documentation](https://developer.apple.com/documentation/foundation/optimizing-your-app-s-data-for-icloud-backup) | Same English document | Developer documentation |
| Apple File System | [Apple Developer Documentation](https://developer.apple.com/documentation/foundation/about-apple-file-system) | Same English document | Developer documentation; macOS sandbox |
| App Store Connect Help | [Help center](https://developer.apple.com/help/app-store-connect/) | [Chinese help](https://developer.apple.com/cn/help/app-store-connect/) | Before You Submit |
| App Review Help | [Help center](https://developer.apple.com/help/app-review/) | [Chinese help](https://developer.apple.com/cn/help/app-review/) | Before and after submission |
| Developer Account Help | [Help center](https://developer.apple.com/help/account/) | [Chinese help](https://developer.apple.com/cn/help/account/) | Before You Submit |
| Human Interface Guidelines | [Apple Design](https://developer.apple.com/design/human-interface-guidelines/) | [Chinese entry](https://developer.apple.com/cn/design/human-interface-guidelines/) | Before You Submit; Apple Pay; location; Apple products |
| App Store Marketing Resources and Identity Guidelines | [Apple Developer](https://developer.apple.com/app-store/marketing/guidelines/) | [Chinese guidelines](https://developer.apple.com/cn/app-store/marketing/guidelines/) | Before You Submit |
| Apple Pay Marketing Guidelines | [Apple Developer](https://developer.apple.com/apple-pay/marketing/) | [Chinese guidelines](https://developer.apple.com/cn/apple-pay/marketing/) | Before You Submit; Apple Pay |
| Add to Apple Wallet badge | [Apple Developer](https://developer.apple.com/wallet/add-to-apple-wallet-guidelines/) | [Chinese guidelines](https://developer.apple.com/cn/wallet/add-to-apple-wallet-guidelines/) | Before You Submit; Wallet passes |
| Apple Trademark and Copyright Guidelines | [Apple Legal](https://www.apple.com/legal/intellectual-property/guidelinesfor3rdparties.html) | [Apple Legal (Chinese)](https://www.apple.com.cn/legal/intellectual-property/guidelinesfor3rdparties.html) | Before You Submit; intellectual property |
| Kids and age-appropriate experiences | [Apple Developer](https://developer.apple.com/kids/) | [Chinese page](https://developer.apple.com/cn/kids/) | Guideline 1.3; parental gates |

## 3. Store presentation, metadata, and discoverability

| Resource | English source | Chinese source | Guideline context |
| --- | --- | --- | --- |
| Promoting In-App Purchases | [Apple Developer](https://developer.apple.com/app-store/promoting-in-app-purchases/) | [Chinese page](https://developer.apple.com/cn/app-store/promoting-in-app-purchases/) | 2.3.2 |
| StoreKit payment-queue method | [Apple Developer Documentation](https://developer.apple.com/documentation/storekit/skpaymenttransactionobserver/paymentqueue(_:shouldaddstorepayment:for:)) | Same English document | 2.3.2 |
| Show the app in use with screenshots | [App Review Help](https://developer.apple.com/help/app-review/guideline-reference/2-3-3-screenshots) | — | 2.3.3 |
| App Store categories | [Apple Developer](https://developer.apple.com/app-store/categories/) | [Chinese page](https://developer.apple.com/cn/app-store/categories/) | 2.3.5 |
| In-App Events | [Apple Developer](https://developer.apple.com/app-store/in-app-events/) | [Chinese page](https://developer.apple.com/cn/app-store/in-app-events/) | 2.3.13 |
| App Store asset best practices | [Apple Developer](https://developer.apple.com/app-store/asset-best-practices/) | — (added with English guideline 2.3.14 in October 2026; the Chinese guidelines page in this crawl was still awaiting an update and had no matching Chinese link) | 2.3.14 |
| Supported devices and multiplatform setup | [Xcode documentation](https://developer.apple.com/documentation/xcode/configuring-a-multiplatform-app-target) | Same English document | 2.4.1 |
| macOS files and directories | [File System Programming Guide (archive)](https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/FileSystemProgrammingGuide/Introduction/Introduction.html) | Same archived English document | 2.4.5 |

## 4. Payments, subscriptions, and business models

This section only records direct links from the guideline body. It is not an IAP, subscription, external-purchase, or regional-terms topic. Those topics are not in this snapshot package.

| Resource | English source | Chinese source | Guideline context |
| --- | --- | --- | --- |
| Choosing a receipt-validation technique | [Apple Developer Documentation](https://developer.apple.com/documentation/storekit/choosing-a-receipt-validation-technique) | Same English document | 3.1.1 trial and access management |
| DeviceCheck | [Apple Developer Documentation](https://developer.apple.com/documentation/devicecheck) | Same English document | 3.1.1 trial and access management |
| External Purchase API | [Apple Developer Documentation](https://developer.apple.com/documentation/storekit/external-purchase) | Same English document | 3.1.1(a) |
| Offer a subscription across multiple apps | [Apple Developer Documentation](https://developer.apple.com/documentation/storekit/offering-a-subscription-across-multiple-apps) | Same English document | 3.1.2 |
| Auto-renewable subscriptions | [Apple Developer](https://developer.apple.com/app-store/subscriptions/) | [Chinese page](https://developer.apple.com/cn/app-store/subscriptions/) | 3.1.2 |
| Apple Developer Program License Agreement | [Current agreement](https://developer.apple.com/support/terms/apple-developer-program-license-agreement/) | [Chinese-path URL recorded in the snapshot](https://developer.apple.com/cn/support/terms/apple-developer-program-license-agreement/) | 3.1.2(c); privacy; fees and terms |
| Reader apps and the External Link Account Entitlement | [Apple Developer Support](https://developer.apple.com/support/reader-apps/) | [Chinese support page](https://developer.apple.com/cn/support/reader-apps/) | 3.1.3(a) |
| Apple Pay for nonprofit donations | [Apple Developer](https://developer.apple.com/apple-pay/nonprofits/) | — | 3.2.1 |

The 2026-10-21 catalog lists the `/cn/` agreement path in the Chinese-source column. When the license was checked on 2026-11-09, that URL rendered English. Do not treat the Chinese column as Apple’s published Chinese agreement. See the [license summary](../developer-program/license-agreement.en-US.md).

## 5. Design, Apple services, and platform APIs

| Resource | English source | Chinese source | Guideline context |
| --- | --- | --- | --- |
| Preventing copycat and impersonation rejections | [App Review Help](https://developer.apple.com/help/app-review/guideline-reference/4-1-prevent-copycat-rejection) | — | 4.1 |
| App Extension Programming Guide | [Apple Developer Archive](https://developer.apple.com/library/archive/documentation/General/Conceptual/ExtensibilityPG/index.html) | — | 4.4 |
| Safari App Extensions | [Apple Developer Documentation](https://developer.apple.com/documentation/safariservices/safari-app-extensions) | Same English document | 4.4 |
| Safari Web Extensions | [Apple Developer Documentation](https://developer.apple.com/documentation/safariservices/safari-web-extensions) | Same English document | 4.4 |
| MusicKit | [Apple Developer](https://developer.apple.com/musickit/) | [MusicKit Chinese](https://developer.apple.com/cn/musickit/) | 4.5.2 |
| Apple Music Identity Guidelines | [Apple Marketing](https://marketing.services.apple/apple-music-identity-guidelines) | — | 4.5.2 |
| Protecting the User’s Privacy | [UIKit documentation](https://developer.apple.com/documentation/uikit/protecting-the-user-s-privacy) | Same English document | 5.1 privacy |
| HIG privacy and location reference | [Linked HIG path](https://developer.apple.com/design/human-interface-guidelines/patterns/accessing-private-data/) | [Chinese privacy guidelines entry](https://developer.apple.com/cn/design/human-interface-guidelines/privacy) | 5.1.5 location; the linked path returned a crawler 404 |
| HIG workout-ring reference | [Linked HIG path](https://developer.apple.com/design/human-interface-guidelines/patterns/workouts/) | — (no Chinese target confirmed) | 5.2.5 Apple products; the linked path returned a crawler 404 |
| Write clear purpose strings | [App Review Help](https://developer.apple.com/help/app-review/guideline-reference/5-1-1-purpose-strings) | — | 5.1.1(ii) |
| Account deletion in the app | [App Review Help](https://developer.apple.com/help/app-review/guideline-reference/5-1-1-account-deletion) | [Chinese help](https://developer.apple.com/cn/help/app-review/guideline-reference/5-1-1-account-deletion) | 5.1.1(v) |
| User Privacy and Data Use | [Apple Developer](https://developer.apple.com/app-store/user-privacy-and-data-use/) | [Chinese page](https://developer.apple.com/cn/app-store/user-privacy-and-data-use/) | 5.1.2 and privacy |
| CallKit | [Apple Developer Documentation](https://developer.apple.com/documentation/callkit) | Same English document | 2.5.12 |
| HealthKit | [Apple Developer Documentation](https://developer.apple.com/documentation/healthkit) | Same English document | 5.1 health data |
| ClassKit | [Apple Developer Documentation](https://developer.apple.com/documentation/classkit) | Same English document | 2.5.18 ad targeting |
| ARKit | [Apple Developer Documentation](https://developer.apple.com/documentation/arkit) | [ARKit Chinese](https://developer.apple.com/cn/documentation/arkit) | 2.5.13 facial authentication |
| WeatherKit | [Apple Developer](https://developer.apple.com/weatherkit/) | [WeatherKit Chinese](https://developer.apple.com/cn/weatherkit/) | 5.2.5 Apple weather attribution |
| NEVPNManager | [Apple Developer Documentation](https://developer.apple.com/documentation/networkextension/nevpnmanager) | Same English document | 5.4 VPN apps |
| Apple intellectual-property dispute form | [Apple Legal](https://www.apple.com/legal/intellectual-property/dispute-forms/index.html) | [Apple Legal (Chinese)](https://www.apple.com.cn/legal/intellectual-property/dispute-forms/) | 5.2 IP complaints |
| Matter certification body | [CSA-IoT](https://csa-iot.org/) | [CSA-IoT Chinese](https://csa-iot.org/zh-CN/) | 2.5.17 Matter |

## 6. After-submission communication and appeals

| Resource | English source | Chinese source | Guideline context |
| --- | --- | --- | --- |
| App Review overview | [Apple Developer](https://developer.apple.com/distribute/app-review/) | [Chinese overview](https://developer.apple.com/cn/distribute/app-review/) | After You Submit |
| Track a submission’s review status | [App Review Help](https://developer.apple.com/help/app-review/after-submitting-for-review/review-status) | — | After You Submit |
| Request an expedited review | [App Review Help](https://developer.apple.com/help/app-review/after-submitting-for-review/request-expedited-review) | — | After You Submit |
| Contact App Review | [App Review Help](https://developer.apple.com/help/app-review/after-submitting-for-review/contact-app-review) | — | After You Submit |
| Appeal to the App Review Board | [App Review Help](https://developer.apple.com/help/app-review/after-submitting-for-review/appeal-to-the-app-review-board) | — | After You Submit |
| Suggest guideline changes | [App Review Help](https://developer.apple.com/help/app-review/after-submitting-for-review/improve-guidelines) | — | After You Submit |
| Accept Bug Fix Submission offers | [App Review Help](https://developer.apple.com/help/app-review/after-submitting-for-review/bug-fix-submissions) | — | After You Submit |
| October 2026 update notice | [Apple Developer News](https://developer.apple.com/news/?id=92th7e5i) | — | Last Updated; the latest rule-change notice recorded in this crawl |
| June 2026 Chinese update notice | [English announcement](https://developer.apple.com/news/?id=a233fmpw) | [Chinese update notice](https://developer.apple.com/cn/news/?id=a233fmpw) | Last-updated link on the Chinese guidelines page |

This crawl did not resolve URLs for the forms and entry points below, so no guessed address is recorded:

| Resource | Crawl result | Help page that can be checked now |
| --- | --- | --- |
| Expedited-review request form | The form link did not resolve on either language of the guidelines | [Request an expedited review](https://developer.apple.com/help/app-review/after-submitting-for-review/request-expedited-review) |
| Appeal entry point | The entry link did not resolve on either language of the guidelines | [Appeal to the App Review Board](https://developer.apple.com/help/app-review/after-submitting-for-review/appeal-to-the-app-review-board) |
| Guideline-change suggestion form | The form link did not resolve on either language of the guidelines | [Suggest changes to the guidelines](https://developer.apple.com/help/app-review/after-submitting-for-review/improve-guidelines) |

The hub procedure for appeals is [rejection and appeals](../../operations/rejection-and-appeals/README.md). That page is an internal workflow, not Apple’s appeal text.

## Link-check notes

- Some Apple Developer Documentation pages require JavaScript in a normal browser. A crawler may show only a shell even when the link itself resolves.
- During this check, a small number of design or documentation links in the guidelines returned a crawler 404 or a JavaScript-only shell. The catalog keeps the URL when it was visible in the guideline body. Verify it in a browser before relying on it.
- Payment, alternative-distribution, subscription, privacy, and region-specific resources can change independently of the guidelines. Recheck the linked page and the agreement before applying a rule to a release.
- A separate set of announcement-body links is in the [news target-page analysis](../news/news-link-targets.en-US.md). Do not merge the two catalogs.
