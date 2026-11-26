---
id: apple.news.rss-index
platform: apple
language: en-US
authority: operational
status: partial
kb_checked_at: 2026-11-09
review_due: 2027-02-09
snapshot_package: 2026-11-10
regions: [global]
topics: [news, change-history, deadlines, review]
editorial_note: "Operational and historical news index, not an Apple policy rule. Checked 2026-11-09 (package 2026-11-10). RSS XML was not parsed; the feed boundary is unverified. This import did not re-open live news pages. English guidelines in the snapshot are dated 2026-10-16; the Simplified Chinese official guidelines page shows 2026-06-08. Practical notes are the English wording of the snapshot's Chinese implementation notes."
---

# Apple Developer News Index

## What this page is

This page is an **operational and historical index**, not a review rule. An announcement does not override the current English guidelines, the current agreement, or the live state in App Store Connect. P3 is background. H is change history only.

The knowledge-base check date is 2026-11-09 (package dated 2026-11-10). This import did not reopen the live news pages.

Source pages:

- [English news list](https://developer.apple.com/news/)
- [Simplified Chinese news list](https://developer.apple.com/cn/news/)
- [English RSS](https://developer.apple.com/news/rss/news.rss)
- [Simplified Chinese RSS](https://developer.apple.com/cn/news/rss/news.rss)

## Retrieval status

The supplied RSS URLs returned `application/rss+xml`, which the available web reader could not parse. That runtime also could not download and parse XML from Apple’s domain. This index is therefore based on Apple’s rendered English and Simplified Chinese news lists, with the included recent announcements opened in that pass.

The two lists do not have identical latest visible dates or entries. The table is a bilingual working set. **It is not an item-by-item mirror of the RSS XML.** The XML item count, feed boundary, raw `pubDate` values, and unexpanded older items remain unverified. Status is `partial`.

The table records the recent 2026 posts selected and opened from those page snapshots, including English-only notices and items published in both languages. If a raw XML export is later available, reconcile it by article ID. Site navigation, sharing controls, and image-CDN assets are excluded.

Direct body links, target pages, relationships, and access status are in the [news target-page analysis](news-link-targets.en-US.md).

Practical notes below are the English wording of the snapshot’s Chinese implementation notes. They are not Apple policy text. Summaries are the snapshot’s English summary of each notice.

In this snapshot the English App Review Guidelines are dated October 16, 2026. The Simplified Chinese official guidelines page still shows June 8, 2026. A translation delay does not make a policy inapplicable. See the [guidelines summary](../app-review-guidelines/guidelines-summary.en-US.md).

## Relevance tiers

- **P1 — Release or compliance action.** May affect review policy, required information, submission materials, agreement acceptance, or a stated release deadline. Read first.
- **P2 — Conditional.** Applies only when the app uses a relevant feature, API, platform, storefront, or distribution route.
- **P3 — Background.** News, events, or testing resources that add no direct compliance obligation. Omit them from routine submission review.
- **H — Historical.** An older policy or earlier agreement update, kept for change history only. Do not treat it as current terms.

Rows are sorted newest first within each group.

## P1 — Submission and compliance actions

| Date | Tier | Article | Summary | Practical note |
| --- | --- | --- | --- | --- |
| 2026-11-02 | P1 — New age descriptors | [Upcoming: New age rating content descriptors in App Store Connect](https://developer.apple.com/news/?id=yxkh08us) | Starting November 16, 2026, the questionnaire adds Shared Location and Dating and Relationships declarations. Every app must complete them by January 12, 2027. Dating and Relationships sets a minimum 18+ rating. Brazil requires A16 for Shared Location and A18 for Dating and Relationships. English-only URL in this index. | Answer the new questions on the next submission or when the age-rating questionnaire is edited. Inventory real-time location sharing, in-person dating, and virtual companions that engage in sexual or romantic content. See [age ratings](../age-ratings/age-ratings.en-US.md). |
| 2026-10-16 | P1 — Rule update | [Updated App Review Guidelines are now available](https://developer.apple.com/news/?id=92th7e5i) | The update covers UGC and AI-generated content, App Store creative assets, hidden functionality, external purchase links, and enforcement against trafficking or child exploitation. | The English guidelines are the current rule baseline. The Chinese guidelines still await Apple’s translation update. See the [guidelines summary](../app-review-guidelines/guidelines-summary.en-US.md). |
| 2026-10-16 | P1 — Enforcement | [Strengthening App Review Guidelines against nonconsensual intimate imagery and bait-and-switch apps](https://developer.apple.com/news/?id=vvzx6cul) | The notice addresses nonconsensual intimate imagery, including AI-generated imagery, hidden harmful functionality enabled only after approval, and enforcement consequences that can include removal, removal from the developer program, or a block on alternative distribution. | Read it with the October 16 guidelines update. One notice explains enforcement risk; the other locates the formal rules. Focus on guidelines 1.2, 2.5.19, and section 5. |
| 2026-10-13 | P1 — Current agreement | [更新后的《Apple Developer Program 许可协议》现已发布](https://developer.apple.com/cn/news/?id=17mwd36z) · [English](https://developer.apple.com/news/?id=17mwd36z) | The revision clarifies security requirements for Apple software and services, Live Assistance API and App Replacement Entitlement terms, widgets on CarPlay and Apple HomeView, multiseat subscriptions, and tax-data reporting and use. | Program administrators should review and accept the new terms. Teams using the related APIs, CarPlay, widgets, or organizational subscriptions should check each change. See the [license summary](../developer-program/license-agreement.en-US.md). The supplied `/cn/` agreement URL rendered English on 2026-11-09. |
| 2026-10-05 | P1 — Submission | [为 iPhone Duo 准备并提交你的 App](https://developer.apple.com/cn/news/?id=kkphp5qo) · [English](https://developer.apple.com/news/?id=kkphp5qo) | Rebuild with Xcode 27.1 and check device poses and orientations, refresh product-page assets, and submit optimized screenshots. From April 2027, submissions must include iPhone Duo screenshots. | Affects the submission build, screenshot assets, and the compatibility test plan. Schedule the asset migration before April 2027. |
| 2026-10-05 | P1 — Asset policy | [借助 App Store 上的全新素材展示你的 App](https://developer.apple.com/cn/news/?id=ljpl7kyn) · [English](https://developer.apple.com/news/?id=ljpl7kyn) | New product-page header and search-result creative assets complement screenshots and previews. App Store Connect adds centralized asset management and pre-submission previews across devices, orientations, and Dark Mode. | Creative assets need to stay accurate to the app’s content, brand, and functionality, and follow guideline 2.3.14. |
| 2026-09-09 | P1 — SDK deadline | [App Store 现已接受适用于最新版操作系统的 App 和游戏提交](https://developer.apple.com/cn/news/?id=k1mtkt1k) · [English](https://developer.apple.com/news/?id=k1mtkt1k) | Submissions for the latest OS releases, including iOS 27, are open. Beginning April 2027, iOS, iPadOS, tvOS, visionOS, and watchOS uploads must use the corresponding 27-series SDK or later. | Put the minimum SDK into the release-pipeline gate and upgrade CI and Xcode with it. |
| 2026-07-09 | P1 — Age questionnaire | [年龄分级调查问卷现在包含社交媒体问题](https://developer.apple.com/cn/news/?id=tlur8uvi) · [English](https://developer.apple.com/news/?id=tlur8uvi) | The questionnaire adds social-media questions based on discovery, amplification, and interaction with UGC rather than the app category. Disabling social features for under-13 users affects that age group’s Time Allowances classification. | From September 2026, answer these questions when submitting a new app, an update, or notarization for alternative distribution. See [age ratings](../age-ratings/age-ratings.en-US.md). |

## P2 — Conditional on app, platform, or storefront

| Date | Tier | Article | Summary | Practical note |
| --- | --- | --- | --- | --- |
| 2026-11-04 | P2 — Subscription retention messages | [Now available: Retention messages for subscriptions](https://developer.apple.com/news/?id=fk9ps3gv) | Auto-renewable subscriptions can show retention messages during cancellation, with text, images, and retention offers. App Store Connect supports subscriber eligibility and wait-time configuration. Retention Messaging API access is by request. | Applies only when the app offers auto-renewable subscriptions and enables retention messages. Copy must be accurate, relevant, and inoffensive. It must not state a specific price or discount, or claim a coercive or unverifiable result, and it must be submitted for review. |
| 2026-11-03 | P2 — Siri AI preview | [Siri AI is now open to all developers](https://developer.apple.com/news/?id=gdk2umrf) | The iOS, iPadOS, macOS, and visionOS 27.3 betas open the Siri AI Developer Preview to all developers through App Intents and skills. It is currently unavailable in the EU on iOS, iPadOS, and watchOS, and unavailable to users under 13. Terms and usage policies are still forthcoming. | A conditional platform capability, not a current general submission requirement. If you integrate it, isolate tests for Beta, region, age, Apple Intelligence terms, and privacy disclosure. |
| 2026-10-29 | P2 — Taiwan storefront rate | [Adjustments to the Taiwan storefront of the App Store on iOS and iPadOS](https://developer.apple.com/news/?id=w9mxlhek) | The Taiwan iOS/iPadOS storefront commission for standard In-App Purchase and paid-app transactions changed from 30% to 26% on October 31, 2026. The agreement was revised. Signing by that date was not required to receive the rate change. Region-sensitive. | Affects the Taiwan storefront only. Recheck revenue forecasts, tax and settlement, and the agreement status in the account. |
| 2026-10-22 | P2 — Business and school subscriptions | [Offer your subscriptions to businesses and schools](https://developer.apple.com/news/?id=yfo21au) | Organizations and educational institutions can buy auto-renewable subscriptions in volume through Apple Business and Apple School Manager. Multiseat purchasing is enabled by default in App Store Connect and storefront availability can be adjusted. Group purchases can be tested in Sandbox from November 2026. | If you offer subscriptions, confirm seat assignment, adding and removing seats, organizational purchasing, and support. If you do not offer this model, the corresponding availability can be turned off. |
| 2026-10-02 | P2 — macOS privacy | [macOS 中完全磁盘访问权限的更新](https://developer.apple.com/cn/news/?id=p6zjojqw) · [English](https://developer.apple.com/news/?id=p6zjojqw) | Full Disk Access can expose files, email, messages, and browsing history. Apple plans stronger, more explicit consent controls as high-privilege access becomes riskier with autonomous agents. | A Mac app should explain why it needs the permission, narrow the access, and obtain authorization only after the user clearly understands it. |
| 2026-10-01 | P2 — Mac certificates | [Upcoming expiration of Developer ID Certification Authority (Sub-CA)](https://developer.apple.com/news/?id=w4atic4c) | The previous Developer ID Sub-CA expires on February 1, 2027. Affected `.pkg` installers will stop installing. Already signed and timestamped Mac apps continue to work. Future updates should use a G2 certificate. | Check the issuing authority, issue date, and installer packages. Update certificates and signing before the deadline. |
| 2026-09-18 | P2 — Device-specific | [使用新资源为 iPhone Duo 构建](https://developer.apple.com/cn/news/?id=nyuppv9r) · [English](https://developer.apple.com/news/?id=nyuppv9r) | New iPhone Duo design and testing resources accompany the Xcode 27.1 beta. | Preparation information for device adaptation and submission assets. |
| 2026-09-16 | P2 — Subscription feature | [让你的订阅为 iOS 27 做好准备](https://developer.apple.com/cn/news/?id=likeohx4) · [English](https://developer.apple.com/news/?id=likeohx4) | StoreKit 2 supports subscription Bundles, Suites, and multiseat purchases. Organizations can buy in volume through Apple Business and Apple School Manager. An individual purchase can also invite other people to share seats. | Check subscription structure, seat assignment, invite and leave flows, and customer support. Apply under the agreement attachments and App Store Connect eligibility rules. |
| 2026-09-16 | P2 — EU-specific | [App Tracking Transparency 在欧盟地区的更新](https://developer.apple.com/cn/news/?id=idsft9ai) · [English](https://developer.apple.com/news/?id=idsft9ai) | An alternative ATT prompt becomes available in the EU with iOS/iPadOS 27.2. Consent requirements stay the same. Apps distributed in Germany, France, Italy, Poland, and Romania must use the alternative prompt. The target-page notes record that the Chinese article URL returned Internal Error and the English body was read instead. Region-sensitive. | Include storefront, OS version, and prompt style in privacy tests. The page linked from the announcement is [User Privacy and Data Use](https://developer.apple.com/cn/app-store/user-privacy-and-data-use/). |
| 2026-09-09 | P2 — Device-specific | [为 iPhone Duo 做好准备](https://developer.apple.com/cn/news/?id=vn8abkxx) · [English](https://developer.apple.com/news/?id=vn8abkxx) | Provides preparation videos, group labs, and developer-forum Q&A for iPhone Duo. | Developer support resources. |
| 2026-09-01 | P2 — macOS migration | [对基于 Intel 的 macOS App 的 Rosetta 支持即将发生变化](https://developer.apple.com/cn/news/?id=w5ngl9k2) · [English](https://developer.apple.com/news/?id=w5ngl9k2) | macOS 27 is the final Rosetta-supported release. Intel-only apps will no longer run on Apple silicon afterward, with a limited exception for certain unmaintained legacy games. | Move the Mac app to a Universal or Apple-silicon-native build, and plan migration communication from the mix of user devices. |
| 2026-08-27 | P2 — Storefront tax and pricing | [App、App 内购买项目及订阅的税务和价格信息更新](https://developer.apple.com/cn/news/?id=artln8br) · [English](https://developer.apple.com/news/?id=artln8br) | Tax or price updates affect Morocco, the Republic of the Congo, Tanzania, and other storefronts. Auto-renewable subscriptions and manually managed prices are treated differently. | In App Store Connect, check the base country or region, tax responsibility, and price changes. Do not assume every product reprices automatically. |
| 2026-08-24 | P2 — If using Sign in with Apple | [更新：“通过 Apple 登录”的新域名](https://developer.apple.com/cn/news/?id=1ptvdtcm) · [English](https://developer.apple.com/news/?id=1ptvdtcm) | New Sign in with Apple relay addresses will use `private.icloud.com`. Existing `privaterelay.appleid.com` addresses continue to work. iCloud+ Hide My Email remains on `icloud.com`. | Update email-domain allowlists, verification, and account recovery so a domain check does not reject users. |
| 2026-08-18 | P2 — EU-specific | [适用于欧盟 App 的变更](https://developer.apple.com/cn/news/?id=gmws0jgp) · [English](https://developer.apple.com/news/?id=gmws0jgp) | EU business terms move to a single model. A 5% Core Technology Commission applies to digital transactions for apps distributed outside the App Store, replacing the Core Technology Fee, while the Initial Acquisition Fee and the Store Services Fee are removed. Region-sensitive. | Assess the terms against the distribution channel and payment path. The latest agreement attachments and regional rules control. |
| 2026-08-12 | P2 — Korea-specific | [韩国的年龄分级更新](https://developer.apple.com/cn/news/?id=oj3r9pvw) · [English](https://developer.apple.com/news/?id=oj3r9pvw) | Games and entertainment apps distributed in Korea can submit a GRAC Rating Classification Number with a subsequent version to apply a region-specific rating. Region-sensitive. | The age-rating questionnaire and the regulator’s number must be accurate. This applies only to the stated categories and the Korea storefront. |
| 2026-08-05 | P2 — Asset planning | [为 App Store 上的全新创意素材资源做好准备](https://developer.apple.com/cn/news/?id=kug6m2ea) · [English](https://developer.apple.com/news/?id=kug6m2ea) | Introduces new App Store asset placements, including product-page headers, search results, and In-App Events, with asset guidance and templates. | Read with the October 5 asset notices. The August notice previews and plans assets. The October notices add asset management, previews, and specifications. |

## P3 — Background only

| Date | Tier | Article | Summary | Practical note |
| --- | --- | --- | --- | --- |
| 2026-11-03 | P3 — Beta resources | [使用最新 Beta 版本，做好充足准备](https://developer.apple.com/cn/news/?id=6gpufove) · [English](https://developer.apple.com/news/?id=6gpufove) | The 27.3 betas for iOS, iPadOS, macOS, tvOS, visionOS, and watchOS, and Xcode 27.3, are available for compatibility testing. | Beta resources do not change submission policy by themselves. Add them to the test plan only when the target app must adapt to the new OS. |
| 2026-10-28 | P3 — Touch on Mac resources | [Say hello to Touch on Mac](https://developer.apple.com/news/?id=i9boeiqc) | Developer videos, Group Labs, documentation, and design resources for touch input on MacBook Pro. | A resources and events notice. Read it only if the product adapts to Mac touch input. It is not a separate App Review obligation. |
| 2026-10-06 | P3 — Monthly digest | [开发者你好：2026 年 10 月](https://developer.apple.com/cn/news/?id=gv788oj6) · [English](https://developer.apple.com/news/?id=gv788oj6) | The monthly digest points to iPhone Duo submission advice, group labs, developer events, localized documentation, and App Store creative assets. | An informational digest. Open the linked topic only when you need it. |
| 2026-09-16 | P3 — Beta resources | [使用最新 Beta 版本，做好充足准备](https://developer.apple.com/cn/news/?id=rfb1rooi) · [English](https://developer.apple.com/news/?id=rfb1rooi) | The 27.2 platform betas are available for compatibility testing with Xcode 27.2. The article also says iPhone Duo is planned to ship with iOS 27.1. | Regress on real Beta devices and TestFlight. Beta behavior does not replace verification on the release OS. |
| 2026-08-26 | P3 — Event notice | [亮新篇，来耀眼](https://developer.apple.com/cn/news/?id=s6spdug0) · [English](https://developer.apple.com/news/?id=s6spdug0) | Announces the September 9 Apple Event and viewing options. | An informational notice. It creates no submission-policy requirement. The Apple website link, and viewing options that were plain text rather than links, are in the target-page analysis. |

## H — Historical versions

| Date | Tier | Article | Summary | Practical note |
| --- | --- | --- | --- | --- |
| 2026-08-18 | H — Earlier agreement notice | [更新后的《Apple Developer Program 许可协议》现已发布](https://developer.apple.com/cn/news/?id=0cgo95n6) · [English](https://developer.apple.com/news/?id=0cgo95n6) | Attachment 14 adds EU terms for alternative distribution, alternative payments, and business terms. The announcement gives October 1, 2026 as the effective date. | Timeline only. Use the live agreement and later amendment notices for current terms. |

## How to use these updates

1. Separate the announcement date from the effective date. They may differ.
2. For payment rules and for regional rules such as the EU, mainland China, and Korea, read the current agreement, the applicable attachment, and the relevant App Store Connect help page together.
3. Turn Xcode, SDK, screenshot, and device-support requirements into separate build, test, and product-page release gates.
4. For privacy and permission news, review whether the permission is actually needed, how the user understands and grants it, and how data is used after consent.
5. Deduplicate later feed updates by article ID, and keep English and Chinese publication or update dates separate.

The July 9, 2026 age-rating notice is also analyzed as a linked target of the September 9, 2026 submission notice. It does not define or replace the RSS feed boundary.
