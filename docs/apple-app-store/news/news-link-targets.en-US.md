---
id: apple.news.link-targets
platform: apple
language: en-US
authority: operational
status: partial
kb_checked_at: 2026-11-09
review_due: 2027-02-09
snapshot_package: 2026-11-10
regions: [global]
topics: [news, sources, change-history]
editorial_note: "Operational and historical source-to-target index, not an Apple policy rule. Checked 2026-11-09 (package 2026-11-10). RSS XML was not parsed. Many targets were only partially read or not read. This import did not re-open the live pages. English guidelines in the snapshot are dated 2026-10-16; the Simplified Chinese official guidelines page shows 2026-06-08. The supplied /cn/ license URL rendered English on 2026-11-09. Where the snapshot wrote a relation only in Chinese, this page uses the English wording of that note."
---

# News Body Links and Target-Page Analysis

## Scope and method

This page maps direct body links in the 2026 announcements included in the [news index](news-rss-index.en-US.md). It is an **operational / historical index**, not a list of rules and not mandatory reading. In that pass, each resolvable target was opened and summarized against its source announcement. Duplicate destinations share one target ID. The announcement map still records every relationship. The July 9 age-rating notice is included because the September 9 submission notice links to it.

**The RSS boundary is still unverified.** Both feeds return `application/rss+xml`, which that reader could not parse, and the English and Chinese news lists do not have identical recent entries. This map covers the recent announcements listed in the index and the explicitly linked age-rating notice. It is not a mirror of every historical RSS item and does not establish the exact feed boundary. Global navigation, headers, footers, images, CDN assets, social-sharing controls, and same-page anchors are excluded. Links inside target pages were not followed recursively.

**Read** means the page body was opened and summarized. **Partial** means a landing page or the available portion was read. **Unread** means the destination was visible but the reader could not retrieve the content. For an unread target, the relationship is limited to the link label and the surrounding announcement text. Do not treat an unread link label as confirmed policy.

Use policy, submission, age-rating, payment, privacy, and agreement targets only when they match the app or the release. Event pages, newsletters, generic developer resources, videos, and forums are background links. They do not create App Review obligations by themselves.

The knowledge-base check date is 2026-11-09 (package dated 2026-11-10). This import did not reopen these pages. Entry points recorded in the snapshot: [English News](https://developer.apple.com/news/), [Simplified Chinese news](https://developer.apple.com/cn/news/), [English RSS](https://developer.apple.com/news/rss/news.rss), [Simplified Chinese RSS](https://developer.apple.com/cn/news/rss/news.rss).

## Announcement-to-target map

| Announcement | Direct body-link targets |
| --- | --- |
| 2026-11-04 — [Now available: Retention messages for subscriptions](https://developer.apple.com/news/?id=fk9ps3gv) | [T53](#t53-retention-messaging-api) Retention Messaging API; [T54](#t54-configure-retention-messages) App Store Connect configuration; [T55](#t55-auto-renewable-subscriptions) auto-renewable subscriptions overview |
| 2026-11-03 — [Siri AI is now open to all developers](https://developer.apple.com/news/?id=gdk2umrf) | [T56](#t56-siri-ai-developer-preview) Siri AI Developer Preview documentation; [T57](#t57-apple-intelligence-terms) Apple Intelligence terms entry |
| 2026-11-02 — [Upcoming: New age rating content descriptors in App Store Connect](https://developer.apple.com/news/?id=yxkh08us) | [T43](#t43-age-rating-values) age-rating values and definitions; [T46](#t46-brazil-classification) Brazil Ministry of Justice classification entry; [T51](#t51-brazil-classification-guide) Brazil classification guide. The notice says every app must complete the new declarations by 2027-01-12, and that an official Brazil rating may be requested when the stated conditions apply |
| 2026-11-03 — [使用最新 Beta 版本，做好充足准备](https://developer.apple.com/cn/news/?id=6gpufove) · [English](https://developer.apple.com/news/?id=6gpufove) | [T19](#t19-releases) downloads and release notes; [T22](#t22-testing-a-beta-os) testing a beta OS; [T23](#t23-feedback-assistant) feedback entry. Beta resources are not an independent review obligation |
| 2026-10-29 — [Adjustments to the Taiwan storefront of the App Store on iOS and iPadOS](https://developer.apple.com/news/?id=w9mxlhek) | [T47](#t47-taiwan-storefront) Traditional Chinese explanation; [T02](#t02-agreements-index) agreements index; [T03](#t03-license-agreement) current English agreement; [T04](#t04-account-sign-in) sign in to see account terms |
| 2026-10-28 — [Say hello to Touch on Mac](https://developer.apple.com/news/?id=i9boeiqc) | [T52](#t52-touch-on-mac) Touch on Mac resources. Background only. Not a separate submission obligation |
| 2026-10-22 — [Offer your subscriptions to businesses and schools](https://developer.apple.com/news/?id=yfo21au) | [T48](#t48-subscription-purchase-options) App Store Connect purchase options; [T49](#t49-multiseat-api) App Store Connect API; [T50](#t50-wwdc-subscriptions) WWDC26 video |
| 2026-10-16 — [Updated App Review Guidelines are now available](https://developer.apple.com/news/?id=92th7e5i) | [T01](#t01-app-review-guidelines). The “Apple Developer website” translation link also points at the same guidelines |
| 2026-10-16 — [Strengthening App Review Guidelines against nonconsensual intimate imagery and bait-and-switch apps](https://developer.apple.com/news/?id=vvzx6cul) | [T01](#t01-app-review-guidelines), the full guidelines |
| 2026-10-13 — [更新后的 Apple Developer Program 许可协议](https://developer.apple.com/cn/news/?id=17mwd36z) | [T02](#t02-agreements-index); [T03](#t03-license-agreement); [T04](#t04-account-sign-in) |
| 2026-10-06 — [Hello Developer: October 2026](https://developer.apple.com/news/?id=gv788oj6) | [T05](#t05-hello-developer) digest page (“Read now”) |
| 2026-10-05 — [为 iPhone Duo 准备并提交你的 App](https://developer.apple.com/cn/news/?id=kkphp5qo) | [T06](#t06-xcode); [T07](#t07-iphone-duo-prepare); [T08](#t08-iphone-duo); [T09](#t09-asset-best-practices); [T10](#t10-manage-assets); [T11](#t11-app-preview); [T12](#t12-screenshots); [T13](#t13-submitting); [T14](#t14-creative-assets-notice) |
| 2026-10-05 — [借助 App Store 上的全新素材展示你的 App](https://developer.apple.com/cn/news/?id=ljpl7kyn) | [T09](#t09-asset-best-practices); [T15](#t15-creative-asset-specs); [T11](#t11-app-preview); [T12](#t12-screenshots); [T16](#t16-screenshot-review-help); [T10](#t10-manage-assets) |
| 2026-10-02 — [macOS 中完全磁盘访问权限的更新](https://developer.apple.com/cn/news/?id=p6zjojqw) | No direct link to a separate content page was found. The announcement itself describes future permission controls and Full Disk Access risk |
| 2026-10-01 — [Upcoming expiration of Developer ID Certification Authority (Sub-CA)](https://developer.apple.com/news/?id=w4atic4c) | [T17](#t17-certificates) certificate account area; [T18](#t18-replace-developer-id) certificate-replacement guide |
| 2026-09-18 — [使用新资源为 iPhone Duo 构建](https://developer.apple.com/cn/news/?id=nyuppv9r) | [T19](#t19-releases); [T20](#t20-design-resources); [T21](#t21-workshops); [T08](#t08-iphone-duo) |
| 2026-09-16 — [使用最新 Beta 版本，做好充足准备](https://developer.apple.com/cn/news/?id=rfb1rooi) | [T19](#t19-releases); [T22](#t22-testing-a-beta-os); [T23](#t23-feedback-assistant) |
| 2026-09-16 — [让你的订阅为 iOS 27 做好准备](https://developer.apple.com/cn/news/?id=likeohx4) | [T24](#t24-bundles-suites); [T25](#t25-offer-bundles); [T26](#t26-bundles-video); [T27](#t27-purchase-options); [T28](#t28-group-subscriptions-video) |
| 2026-09-16 — [App Tracking Transparency 在欧盟地区的更新](https://developer.apple.com/cn/news/?id=idsft9ai) | [T29](#t29-user-privacy). The Chinese article URL returned Internal Error. The English body was read, and T29 was accessible |
| 2026-09-09 — [为 iPhone Duo 做好准备](https://developer.apple.com/cn/news/?id=vn8abkxx) | [T08](#t08-iphone-duo) videos, labs, and preparation resources |
| 2026-09-09 — [App Store 现已接受适用于最新版操作系统的 App 和游戏提交](https://developer.apple.com/cn/news/?id=k1mtkt1k) | [T30](#t30-apple-silicon); [T31](#t31-age-questionnaire-notice); [T09](#t09-asset-best-practices); [T13](#t13-submitting) |
| 2026-09-01 — [对基于 Intel 的 macOS App 的 Rosetta 支持即将发生变化](https://developer.apple.com/cn/news/?id=w5ngl9k2) | [T32](#t32-rosetta); [T30](#t30-apple-silicon); [T33](#t33-porting); [T34](#t34-forums) |
| 2026-08-27 — [App、App 内购买项目及订阅的税务和价格信息更新](https://developer.apple.com/cn/news/?id=artln8br) | [T35](#t35-tax-self-link). “Learn more” resolved to the same announcement. No separate target page |
| 2026-08-26 — [亮新篇，来耀眼](https://developer.apple.com/cn/news/?id=s6spdug0) | [T36](#t36-apple-event). The Chinese notice links apple.com.cn only. “Apple TV” is plain text. The English notice links apple.com. Apple TV and YouTube Live were not separate anchors in the readable text |
| 2026-08-24 — [更新：“通过 Apple 登录”的新域名](https://developer.apple.com/cn/news/?id=1ptvdtcm) | [T37](#t37-sign-in-with-apple-hig); [T38](#t38-private-relay) |
| 2026-08-18 — [适用于欧盟 App 的变更](https://developer.apple.com/cn/news/?id=gmws0jgp) | [T39](#t39-eu-terms); [T40](#t40-eu-events) |
| 2026-08-18 — [更新后的 Apple Developer Program 许可协议](https://developer.apple.com/cn/news/?id=0cgo95n6) | [T03](#t03-license-agreement) Attachment 14; [T04](#t04-account-sign-in); [T02](#t02-agreements-index). Historical. See the news index |
| 2026-08-12 — [韩国的年龄分级更新](https://developer.apple.com/cn/news/?id=oj3r9pvw) | [T41](#t41-grac); [T42](#t42-set-age-rating); [T43](#t43-age-rating-values) |
| 2026-08-05 — [为 App Store 上的全新创意素材资源做好准备](https://developer.apple.com/cn/news/?id=kug6m2ea) · [English](https://developer.apple.com/news/?id=kug6m2ea) | [T45](#t45-app-store-whats-new); [T09](#t09-asset-best-practices). Both direct links in the Chinese and English bodies were opened, each on the matching language of the target |
| 2026-07-09 — [年龄分级调查问卷现在包含社交媒体问题](https://developer.apple.com/cn/news/?id=tlur8uvi) (linked target, not a boundary for the feed) | [T44](#t44-time-allowances); [T42](#t42-set-age-rating); [T43](#t43-age-rating-values) |

## Target-page summaries

### Review guidelines, agreement, and account

<a id="t01-app-review-guidelines"></a>

#### T01 — App Review Guidelines

- **Target:** [English](https://developer.apple.com/app-store/review/guidelines/) · [Simplified Chinese](https://developer.apple.com/cn/app-store/review/guidelines/) — **Read**
- **Content:** The English page is the October 16, 2026 baseline. It covers UGC and AI moderation, creative assets, hidden functionality, external-purchase links, and serious safety violations. The Chinese page still shows June 8, 2026.
- **Relation:** Both October 16 notices use this page as the normative text. The first lists the revised clauses. The second explains nonconsensual intimate imagery, bait-and-switch behavior, and enforcement consequences. Hub summary: [guidelines summary](../app-review-guidelines/guidelines-summary.en-US.md).

<a id="t02-agreements-index"></a>

#### T02 — Agreements and Guidelines index

- **Target:** [English](https://developer.apple.com/support/terms/) · [Simplified Chinese](https://developer.apple.com/cn/support/terms/) — **Read**
- **Content:** Apple’s index of developer agreements, license terms, and related guidelines.
- **Relation:** Both agreement-update notices point at this index. Check a change described in a notice against the current agreement and its attachments.

<a id="t03-license-agreement"></a>

#### T03 — Apple Developer Program License Agreement

- **Target:** [English current agreement](https://developer.apple.com/support/terms/apple-developer-program-license-agreement/) · [Supplied Chinese path; the page body rendered English on 2026-11-09](https://developer.apple.com/cn/support/terms/apple-developer-program-license-agreement/) — **Read**
- **Content:** Licensing, development and testing use, distribution channels, developer obligations, and schedules or attachments. The text reviewed in the snapshot includes Live Assistance API, App Replacement Entitlement, HomeView and CarPlay widgets, multiseat subscriptions, and tax-information handling.
- **Relation:** The October 13 notice lists agreement changes item by item. The August 18 notice describes Attachment 14 and the effective date of the EU terms. The agreement is the binding text. A news summary does not replace it. Hub summary: [license agreement](../developer-program/license-agreement.en-US.md). The Chinese page there is an editorial summary.

<a id="t04-account-sign-in"></a>

#### T04 — Sign in to the developer account

- **Target:** [Sign in](https://developer.apple.com/account/) · [Account resources](https://developer.apple.com/account/resources/) — **Unread: sign-in wall / reader Internal Error**
- **Content:** Requires an authorized developer account. The reader returned Internal Error and could not inspect account-specific agreement status.
- **Relation:** The notices tell the Account Holder, or a person with permission, to view and accept updated terms. Permissions and any pending acceptance have to be confirmed after sign-in.

<a id="t46-brazil-classification"></a>

#### T46 — Brazil official classification

- **Target:** [Classind — Ministério da Justiça e Segurança Pública](https://www.gov.br/mj/pt-br/assuntos/seus-direitos/classificacao-1) — **Partial**
- **Content:** Official Brazil Ministry of Justice and Public Security page for Classificação Indicativa, including classification information, application services, and contact channels. This is a regulator source, not Apple rule text.
- **Relation:** The November 2 age-rating notice says that if a shared-location app has a reasonable basis for a lower rating in Brazil, the developer may apply to MJSP. After verification, Apple displays the official regional rating. This page is that application entry. It is not replaced by Apple’s ordinary questionnaire result.

<a id="t51-brazil-classification-guide"></a>

#### T51 — Brazil classification guide

- **Target:** [Guia de Classificação — Ministério da Justiça e Segurança Pública](https://www.gov.br/mj/pt-br/assuntos/seus-direitos/classificacao-1/paginas-classificacao-indicativa/guia-de-classificacao) — **Read**
- **Content:** MJSP page for the 2025 5th-edition practical guide for audiovisual works, applications, and RPGs. It describes ClassInd age and content-descriptor criteria and how distributors should display ratings on digital platforms, websites, and advertising. Regulator source.
- **Relation:** The November 2 notice points here for material related to an official Brazil rating application. It can help prepare local classification evidence. It does not replace the App Store Connect questionnaire or App Review.

<a id="t47-taiwan-storefront"></a>

#### T47 — Taiwan storefront adjustment

- **Target:** [Taiwan storefront adjustment (Traditional Chinese)](https://developer.apple.com/tw/support/adjustments-to-the-taiwan-storefront/) — **Partial**
- **Content:** The Traditional Chinese target link is confirmed. The reader did not expand the full body. The announcement identifies the page as the localized explanation of the Taiwan iOS/iPadOS storefront commission adjustment for standard In-App Purchases and paid apps.
- **Relation:** Localized target of the October 29 notice. Read it with the announcement and the current license agreement. The adjustment is limited to the Taiwan storefront and the transaction types named in the notice. It is not a global rate.

<a id="t48-subscription-purchase-options"></a>

#### T48 — Auto-renewable subscription purchase options

- **Target:** [Manage purchase options for an auto-renewable subscription](https://developer.apple.com/help/app-store-connect/manage-subscriptions/manage-purchase-options-for-auto-renewable-subscriptions) — **Read**
- **Content:** App Store Connect help for purchase availability of an auto-renewable subscription across the App Store, Apple Business, and Apple School Manager.
- **Relation:** The October 22 notice says multiseat purchasing is on by default and can be adjusted. This page is the operational entry. If the product does not offer organization or school purchasing, check whether that availability should be turned off.

<a id="t49-multiseat-api"></a>

#### T49 — Organization multiseat subscription API

- **Target:** [App Store Connect API: Configuring multiseat subscriptions for organizations](https://developer.apple.com/documentation/appstoreconnectapi/configuring-multi-seat-subscriptions-for-organizations) — **Partial**
- **Content:** API entry for automating organization multiseat subscription configuration. The reader retrieved only the JavaScript documentation shell, not the parameter or permission detail.
- **Relation:** Technical entry in the notice for organizational volume purchasing. Before building, confirm API version, role permissions, and Sandbox versus production limits in a browser or local docs.

<a id="t50-wwdc-subscriptions"></a>

#### T50 — Subscriptions for groups and organizations (video)

- **Target:** [Offer subscriptions to groups and organizations — WWDC26](https://developer.apple.com/videos/play/wwdc2026/391/) — **Read**
- **Content:** WWDC26 session on Group Purchases, organizational purchases, and multiseat subscriptions.
- **Relation:** Further learning material for the October 22 notice. The video is background and does not by itself create an App Review obligation. It can be used with T48 and T49 for design and testing.

<a id="t52-touch-on-mac"></a>

#### T52 — Touch on Mac resources

- **Target:** [Get ready for Touch on Mac](https://developer.apple.com/touch-on-mac/) — **Read**
- **Content:** Videos, Group Labs, Xcode 27.3 beta resources, and documentation for gesture recognition, drag and drop, and macOS design.
- **Relation:** “Explore now” target of the October 28 notice. Platform-adaptation material, not review policy. Include it in an engineering plan only when the product adapts to MacBook Pro touch input.

<a id="t53-retention-messaging-api"></a>

#### T53 — Retention Messaging API

- **Target:** [Retention Messaging API](https://developer.apple.com/documentation/retentionmessaging/) — **Partial**
- **Content:** The documentation entry returned only a JavaScript shell. The announcement says the API can choose a retention message from subscription details and that access is by request.
- **Relation:** Automation entry for the November 4 notice. Before development, confirm API version, authorization scope, and the review process on a readable document or the account-permission page.

<a id="t54-configure-retention-messages"></a>

#### T54 — Configure retention messages

- **Target:** [Configure retention messages in App Store Connect](https://developer.apple.com/help/app-store-connect/manage-subscriptions/configure-retention-messages/) — **Read**
- **Content:** An app can create up to 10 retention messages. Each message has required text and optional images or a retention offer. A message can be associated with multiple subscriptions, but each subscription has only one active message at a time. Creating, editing, and submitting for review require the appropriate App Store Connect role.
- **Relation:** Turns the notice’s subscriber-eligibility and wait-time points into steps. The help page also states direct constraints: copy must be accurate, relevant, and inoffensive; it must not include a specific price or discount; and it must not use coercive or unverifiable outcome claims.

<a id="t55-auto-renewable-subscriptions"></a>

#### T55 — Auto-renewable subscriptions overview

- **Target:** [Auto-renewable Subscriptions](https://developer.apple.com/app-store/subscriptions/) — **Partial**
- **Content:** Product and technology overview, used as navigation for retention messages, offers, and StoreKit capabilities.
- **Relation:** Background entry in the notice. Specific retention copy, offers, and review requirements follow T54.

<a id="t56-siri-ai-developer-preview"></a>

#### T56 — Siri AI Developer Preview

- **Target:** [Siri AI Developer Preview](https://developer.apple.com/documentation/appintents/siri-ai-developer-preview) — **Partial**
- **Content:** Developer Preview entry for Siri AI and App Intents. The reader returned only a JavaScript shell.
- **Relation:** Technical entry for the November 3 notice. The capability is in the iOS, iPadOS, macOS, and visionOS 27.3 betas. It is currently unavailable in the EU on iOS, iPadOS, and watchOS, unavailable to users under 13, and Apple says further terms and usage policies will be published. Do not treat it as a current general submission requirement.

<a id="t57-apple-intelligence-terms"></a>

#### T57 — Apple Intelligence terms

- **Target:** [Apple Intelligence and Siri terms](https://support.apple.com/148587) — **Unread: support.apple.com returned HTTP 429**
- **Content:** The Siri AI notice points here for Apple Intelligence terms. The support site rate-limited the reader, so the body was not read.
- **Relation:** Before integrating Siri AI, check region, age, account, data, and use limits on this page. Do not ship from the developer-news summary alone.

### iPhone Duo, assets, and submission

<a id="t05-hello-developer"></a>

#### T05 — Hello Developer: October 2026

- **Target:** [Hello Developer October 2026](https://developer.apple.com/hello/october26) — **Read**
- **Content:** Digest of the three iPhone Duo submission steps, Group Labs, performance and efficiency events, documentation in eight additional languages, App Store creative assets, Apple Pay partner resources, the new Xcode project format, and Duo design and development documentation.
- **Relation:** “Read now” target of the October 6 newsletter. A resource index, not an independent review rule. iPhone Duo and asset topics link on to related notices and guides in this table.

<a id="t06-xcode"></a>

#### T06 — Xcode

- **Target:** [Xcode](https://developer.apple.com/cn/xcode/) — **Read**
- **Content:** Apple’s developer-tool page, with Xcode downloads, version information, and developer resources. The snapshot recorded this Chinese-path URL.
- **Relation:** The iPhone Duo notice says to rebuild with Xcode 27.1 and check device poses and orientations. This is the download entry named in that notice.

<a id="t07-iphone-duo-prepare"></a>

#### T07 — Three steps to prepare for iPhone Duo

- **Target:** [Prepare — iPhone Duo](https://developer.apple.com/iphone-duo/prepare/) — **Read**
- **Content:** How to check Duo’s changing window and screen sizes, poses, and orientations, and how adaptive layout avoids problems from hard-coded dimensions or orientation assumptions.
- **Relation:** Technical detail behind the October 5 rebuild and test advice. Compatibility preparation, not a review clause.

<a id="t08-iphone-duo"></a>

#### T08 — iPhone Duo preparation page

- **Target:** [iPhone Duo — Apple Developer](https://developer.apple.com/cn/iphone-duo/) — **Read**
- **Content:** Device-adaptation information, videos, development resources, and event links. The snapshot recorded this Chinese-path URL.
- **Relation:** Both September Duo notices and the October preparation notice use it as the collection of technical-preparation entries.

<a id="t09-asset-best-practices"></a>

#### T09 — App Store asset best practices

- **Target:** [English](https://developer.apple.com/app-store/asset-best-practices/) · [Simplified Chinese](https://developer.apple.com/cn/app-store/asset-best-practices/) — **Both read**
- **Content:** Assets must accurately represent app content, functionality, or brand, and stay suitable for a 4+ audience, focused on the core experience. Avoid specific prices, discounts, URLs, unverifiable awards, other-platform marks, and misleading claims. Visuals should be clear, orientation-aware, and understandable without audio.
- **Relation:** Both language versions of the August 5 notice use this page as the direct target for recommended practices and resources, including design templates. It also supports the two October 5 asset notices and the September 9 submission notice. New assets are constrained by metadata accuracy, audience suitability, and review policy, not only by file specifications.

<a id="t10-manage-assets"></a>

#### T10 — Manage App Store assets

- **Target:** [管理 App Store 素材](https://developer.apple.com/cn/help/app-store-connect/manage-app-information/manage-your-app-store-assets) — **Read**
- **Content:** App Store Connect asset library for viewing, editing, and organizing assets and related metadata, and for managing placement, status, reuse, and archiving.
- **Relation:** Both October 5 notices point here. It is the workflow for the announced ability to manage new assets in one place and submit them for review ahead of time.

<a id="t11-app-preview"></a>

#### T11 — App preview specifications

- **Target:** [App 预览规范](https://developer.apple.com/cn/help/app-store-connect/reference/app-information/app-preview-specifications) — **Read**
- **Content:** Supported platforms, localizations, and device sizes, plus limits on count, video orientation, duration, and file format.
- **Relation:** The Duo notice asks teams to update previews for device orientation. The asset notice says previews can be shown with the new creative assets.

<a id="t12-screenshots"></a>

#### T12 — Screenshot specifications

- **Target:** [截屏规范](https://developer.apple.com/cn/help/app-store-connect/reference/app-information/screenshot-specifications) — **Read**
- **Content:** Screenshot requirements by platform and device size, accepted formats, maximum counts, and the requirement that screenshots accurately depict the app.
- **Relation:** Both October 5 notices use it as the specification for new-device assets. The Duo notice states that submissions must include Duo screenshots from April 2027.

<a id="t13-submitting"></a>

#### T13 — Submitting an app

- **Target:** [App Store 提交](https://developer.apple.com/cn/app-store/submitting/) — **Read**
- **Content:** Preparation, build, review, and release flow for App Store submission, including future minimum Xcode and SDK requirements.
- **Relation:** The September 9 notice says that from April 2027 each platform must use a 27-series SDK. The October Duo notice adds the Duo screenshot requirement. This page is the submission flow. The notices supply the effective dates.

<a id="t14-creative-assets-notice"></a>

#### T14 — New creative-assets announcement

- **Target:** [借助 App Store 上的全新素材展示你的 App](https://developer.apple.com/cn/news/?id=ljpl7kyn) — **Read**
- **Content:** Product-page header, search-result assets, asset-library management, and pre-submission previews across devices, orientations, and Dark Mode.
- **Relation:** Related news inside the October Duo submission notice, and an overview of the operational specifications for the creative-asset entries.

<a id="t15-creative-asset-specs"></a>

#### T15 — Creative asset specifications

- **Target:** [创意素材规范](https://developer.apple.com/cn/help/app-store-connect/reference/app-information/creative-assets-specifications) — **Read**
- **Content:** Types, dimensions, file requirements, and placements for the new product-page and search creative assets.
- **Relation:** Specification baseline for the new image and video entries in the October creative-asset notice. Use it with the content expectations in T09.

<a id="t16-screenshot-review-help"></a>

#### T16 — App Review screenshot help

- **Target:** [App Review Help: screenshots](https://developer.apple.com/cn/help/app-review/guideline-reference/2-3-3-screenshots) — **Read** (the Chinese path showed an English title)
- **Content:** Screenshots should show the real app interface and core functionality, and should not present the app inaccurately or misleadingly.
- **Relation:** The October creative-asset notice uses it as help for common screenshot review problems. It supplements T12’s format rules and focuses on whether the content is truthful.

### Certificates, testing, and subscriptions

<a id="t17-certificates"></a>

#### T17 — Certificates, Identifiers & Profiles

- **Target:** The announcement’s anchor is the Certificates, Identifiers & Profiles area of the developer account. **The reader could not resolve a target URL.** None is recorded here.
- **Status:** **Unread: reader Internal Error**
- **Content:** Certificate management inside the Developer Account. Because the URL and the account page were not retrieved, no certificate status or procedure is inferred.
- **Relation:** The expiration notice says to inspect certificates that expire before 2027-02-01 in that account area. The check requires sign-in.

<a id="t18-replace-developer-id"></a>

#### T18 — Replace Developer ID certificates from the previous Sub-CA

- **Target:** [更换由先前 Sub-CA 颁发的 Developer ID 证书](https://developer.apple.com/cn/help/account/certificates/replace-developer-id-certificates) — **Read**
- **Content:** How to identify affected certificates, create a G2 Sub-CA replacement, and re-sign by distribution type. `.pkg` installers and already-notarized Mac apps are affected differently.
- **Relation:** The action list for the October 1 expiration notice: re-sign installers before the deadline, and sign later Mac app updates with the new certificate and a secure timestamp.

<a id="t19-releases"></a>

#### T19 — Releases and downloads

- **Target:** [Apple Developer releases](https://developer.apple.com/cn/news/releases/) — **Read**
- **Content:** Xcode and Apple-platform release and beta downloads, with release notes.
- **Relation:** The September 16 Beta notice and the September 18 Duo resources notice use it to locate Xcode 27.1 and 27.2 and the OS betas.

<a id="t20-design-resources"></a>

#### T20 — Apple Design Resources

- **Target:** [Apple Design Resources](https://developer.apple.com/cn/design/resources/) — **Read**
- **Content:** Apple-platform design templates and UI resources, including Figma and Sketch kits.
- **Relation:** Download entry in the Duo resources notice for the device design kit used to adapt interfaces and store assets.

<a id="t21-workshops"></a>

#### T21 — Meet with Apple workshop calendar

- **Target:** [Workshop schedule](https://developer.apple.com/events/view/upcoming-events?search=workshop) — **Unread: dynamic page returned no content**
- **Content:** Event calendar filtered for workshops. The reader returned no rows, so current sessions could not be confirmed.
- **Relation:** The Duo resources notice points at the global workshop schedule for adaptation sessions.

<a id="t22-testing-a-beta-os"></a>

#### T22 — Testing a beta OS

- **Target:** [Testing a beta OS](https://developer.apple.com/documentation/xcode/testing-a-beta-os) — **Unread: reader Internal Error**
- **Content:** The link title identifies an Xcode guide for testing beta operating systems. The body was not retrieved.
- **Relation:** The September 16 notice suggests validating the app on the new Beta OS. Recheck the steps in documentation that can actually be read.

<a id="t23-feedback-assistant"></a>

#### T23 — Feedback Assistant

- **Target:** [Feedback Assistant](https://developer.apple.com/cn/feedback-assistant/) — **Unread: reader Internal Error**
- **Content:** Apple’s issue-reporting entry. The page body was not retrieved.
- **Relation:** The Beta notice suggests reporting OS or compatibility issues here.

<a id="t24-bundles-suites"></a>

#### T24 — Bundles and Suites for auto-renewable subscriptions

- **Target:** [为自动续期订阅创建套装和套件](https://developer.apple.com/cn/app-store/subscriptions/bundles-and-suites/) — **Read**
- **Content:** Single-developer and multi-developer Bundles, and single-developer Suites. Requires StoreKit 2 and supported 27-series OS versions. A Bundle includes up to five subscriptions. A Suite can cover up to 15 apps. The page also covers application and approval, multi-developer addenda, upgrades, cancellation, and subscription changes.
- **Relation:** Rule and technical-requirement source for Bundles and Suites in the September 16 subscription notice. Multiseat purchasing in that notice should be read with T27 and T28.

<a id="t25-offer-bundles"></a>

#### T25 — Offer Bundles and Suites

- **Target:** The “Offer Bundles and Suites” control in the announcement. In this reader it resolved back to T24. A separate App Store Connect form URL was not confirmed, so none is recorded.
- **Status:** **Unread: unresolved dynamic destination**
- **Relation:** T24 says the team submits a request and waits for Apple’s review. Confirm the live entry while signed in to App Store Connect or on the official page.

<a id="t26-bundles-video"></a>

#### T26 — Bundles and Suites video

- **Target:** Chinese URL attempted: [WWDC26 video](https://developer.apple.com/cn/videos/play/wwdc2026/210/?time=530) — **Unread: cache miss**. English entry recorded in the snapshot: [WWDC26 video](https://developer.apple.com/videos/play/wwdc2026/210/).
- **Content:** The video did not load reliably. Its content is not inferred from the title.
- **Relation:** Demo supplement in the subscription notice for Bundle and Suite behavior. Recheck technical detail when the video is accessible.

<a id="t27-purchase-options"></a>

#### T27 — Manage auto-renewable subscription purchase options

- **Target:** [App Store Connect Help](https://developer.apple.com/cn/help/app-store-connect/manage-subscriptions/manage-purchase-options-for-auto-renewable-subscriptions/) — **Read**
- **Content:** How to configure purchase options, availability, and sales channels for an auto-renewable subscription. The snapshot’s URL for this relationship includes the trailing slash and the `/cn/` path. T48 is the English-path help page cited by the later October 22 notice.
- **Relation:** The September 16 notice says multiseat purchasing is on by default and can be managed per App Store, Apple Business, and Apple School Manager. This help page is that configuration entry.

<a id="t28-group-subscriptions-video"></a>

#### T28 — Offer subscriptions to groups and organizations

- **Target:** [WWDC26 video](https://developer.apple.com/cn/videos/play/wwdc2026/391/) — **Read**
- **Content:** Subscription distribution for groups and organizations, including Group Purchases, Volume Purchasing, seat assignment, and organizational use. The snapshot recorded this Chinese-path video URL. T50 is the English-path video cited by the October 22 notice.
- **Relation:** Supplements multiseat purchase in the September 16 notice, including the difference between an individual inviting people to share seats and volume setup in Apple Business or School Manager.

### Privacy, age ratings, and platform transition

<a id="t29-user-privacy"></a>

#### T29 — User privacy and data use

- **Target:** [Apple 用户隐私与数据使用](https://developer.apple.com/cn/app-store/user-privacy-and-data-use/) — **Read**
- **Content:** App privacy labels, App Privacy Report, the definition of tracking, and the App Tracking Transparency consent model.
- **Relation:** The EU ATT notice changes the system-prompt form in the named storefronts. This page is the privacy and consent background. The notice says the rule for when tracking requires permission does not change.

<a id="t30-apple-silicon"></a>

#### T30 — Apple silicon documentation

- **Target:** [Chinese path recorded in the notice](https://developer.apple.com/cn/documentation/apple-silicon) · [English](https://developer.apple.com/documentation/apple-silicon) — **Unread: JavaScript-rendered docs**
- **Content:** The page requires JavaScript. A Markdown link is exposed, but the reader does not support `text/markdown`, so the body was unavailable.
- **Relation:** The September submission notice points at Apple silicon optimization. The Rosetta notice also asks for native Apple silicon support. The link title and the announcement context identify this as the architecture-adaptation entry. The body was not verified.

<a id="t31-age-questionnaire-notice"></a>

#### T31 — Age-rating questionnaire and social media

- **Target:** [年龄分级调查问卷现在包含社交媒体问题](https://developer.apple.com/cn/news/?id=tlur8uvi) — **Read**
- **Content:** Social-media status depends on discovery, amplification, or interaction with UGC, not the App Store category. A new product-page descriptor applies. Disabling the feature for users under 13 affects that age group’s Time Allowances classification. From September 2026 the questionnaire is required for new apps, updates, and notarization for alternative distribution.
- **Relation:** The September 9 OS-submission notice links here. It is the background for “answer the age-rating questions” and for how social features are classified.

<a id="t32-rosetta"></a>

#### T32 — Rosetta translation environment

- **Target:** [About the Rosetta translation environment](https://developer.apple.com/documentation/apple-silicon/about-the-rosetta-translation-environment) — **Unread: JavaScript-rendered docs**
- **Content:** The documentation page requires JavaScript. Its Markdown content could not be read.
- **Relation:** Background for the end of Rosetta support in the September 1 notice. Recheck migration detail in documentation that can be read.

<a id="t33-porting"></a>

#### T33 — Porting macOS apps to Apple silicon

- **Target:** [Porting your macOS apps to Apple silicon](https://developer.apple.com/documentation/apple-silicon/porting-your-macos-apps-to-apple-silicon) — **Unread: JavaScript-rendered docs**
- **Content:** The JavaScript page exposed no body, so specific migration or build instructions were not checked.
- **Relation:** The Rosetta notice recommends a Universal or native Apple silicon build. This is the porting guide that notice points to. Its steps were not verified in this pass.

<a id="t34-forums"></a>

#### T34 — Apple Developer Forums

- **Target:** [Apple Developer Forums](https://developer.apple.com/forums/) — **Partial**
- **Content:** Forum categories and the discussion list were readable. No specific Rosetta thread URL was present.
- **Relation:** The notice uses the forums as a place to ask questions. That is not a normative source. A specific issue still needs the relevant forum topic. Community use is limited as described in [community evidence](../community-evidence/community-evidence.en-US.md).

<a id="t35-tax-self-link"></a>

#### T35 — Tax and price announcement (self-link)

- **Target:** [App、App 内购买项目及订阅的税务和价格信息更新](https://developer.apple.com/cn/news/?id=artln8br) — **Read: same page**
- **Content:** The announcement explains storefront price and proceeds changes caused by tax law and exchange rates, and tells developers to review tax handling and the difference between automatic and manual pricing.
- **Relation:** “Learn more” in this extraction points back at the same announcement. There is no separate help-page target.

<a id="t36-apple-event"></a>

#### T36 — Apple event site

- **Target:** [Apple storefront site for mainland China](https://apple.com.cn/) · [English Apple homepage](https://www.apple.com/) — **Partial**
- **Content:** The Apple homepage opened. An event-replay page was not verified from that homepage.
- **Relation:** The August 26 notice promotes where to watch the September 9 event. It is unrelated to App Review rules. Apple TV is plain text in the Chinese body, not a link.

<a id="t37-sign-in-with-apple-hig"></a>

#### T37 — Sign in with Apple Human Interface Guidelines

- **Target:** [Sign in with Apple — Human Interface Guidelines](https://developer.apple.com/cn/design/human-interface-guidelines/sign-in-with-apple) — **Unread: JavaScript required**
- **Content:** The page requires JavaScript. The reader only returned a notice to enable scripting.
- **Relation:** The August 24 notice says systems must accept new `private.icloud.com` addresses. This HIG link is the interface and design entry for Sign in with Apple. The body was not read.

<a id="t38-private-relay"></a>

#### T38 — Private email relay documentation

- **Target:** [Communicating using the private email relay service](https://developer.apple.com/documentation/signinwithapple/communicating-using-the-private-email-relay-service/) — **Unread: JavaScript / Markdown unsupported**
- **Content:** The JavaScript page exposes a Markdown link. The reader does not support the `text/markdown` response.
- **Relation:** The notice points at this document for communicating through the private relay, and it also says to update email-domain allowlists and validation. The document body was not read.

<a id="t39-eu-terms"></a>

#### T39 — EU terms hub

- **Target:** [Changes for apps in the European Union](https://developer.apple.com/cn/support/apps-in-the-eu/) — **Read**
- **Content:** EU terms, App Store and alternative payments, alternative and web distribution, fees and commissions, child-safety measures, notarization, and eligibility. What applies depends on distribution path, storefront, the terms selected, and the attachment.
- **Relation:** Direct target of the August 18 EU notice. It expands the unified terms, the 5% Core Technology Commission, alternative payments, and distribution eligibility described in the notice.

<a id="t40-eu-events"></a>

#### T40 — EU event schedule

- **Target:** [Meet with Apple — European events](https://developer.apple.com/events/view/upcoming-events?search=European) — **Unread: dynamic page returned no content**
- **Content:** Event calendar filtered for European events. The reader returned no session details.
- **Relation:** Optional scheduling entry in the EU notice. Not an interpretation of the terms and not a compliance basis.

<a id="t41-grac"></a>

#### T41 — Korea’s GRAC

- **Target:** [Game Rating and Administration Committee — English](https://www.grac.or.kr/english/) — **Partial**
- **Content:** The English official GRAC homepage opened. No specific Rating Classification Number record was retrieved from that homepage. Regulator source.
- **Relation:** The Korea notice says eligible games and entertainment apps can supply an official RCN on a later version. Confirm the number and the scope of authorization from GRAC’s own record.

<a id="t42-set-age-rating"></a>

#### T42 — Set an app age rating

- **Target:** [App Store Connect Help](https://developer.apple.com/cn/help/app-store-connect/manage-app-information/set-an-app-age-rating) — **Read**
- **Content:** The age-rating questionnaire, answers for content, features, and frequency, how the rating is generated, regional overrides, and the related submission steps.
- **Relation:** Linked from both the July 9 social-media notice and the Korea RCN notice. The first is about questionnaire fields. The second is about a regional override for Korea.

<a id="t43-age-rating-values"></a>

#### T43 — Age rating values and definitions

- **Target:** [English](https://developer.apple.com/help/app-store-connect/reference/app-information/age-ratings-values-and-definitions) · [Simplified Chinese](https://developer.apple.com/cn/help/app-store-connect/reference/app-information/age-ratings-values-and-definitions) — **Read**
- **Content:** Questionnaire categories, current and legacy rating scales, and regional ratings including Australia, Brazil, Korea, and Vietnam. The snapshot does not record a date lag between these two Help pages.
- **Relation:** The Korea notice uses the page for local rating values. The social-media notice uses it for social, UGC, and age-control answers. The November 2 notice uses it as the definition and regional background for Shared Location and Dating and Relationships. The hub summary is [age ratings](../age-ratings/age-ratings.en-US.md).

<a id="t44-time-allowances"></a>

#### T44 — Time Allowances notice

- **Target:** [“时间额度”功能介绍](https://developer.apple.com/cn/news/?id=0d2gpmml) — **Read**
- **Content:** Parental Time Allowances categories on iOS, iPadOS, and macOS 27. The social-media category depends on app functionality, not the App Store category. If social features are available only to users 13 and older, the app still has to say so through the questionnaire and age-range controls.
- **Relation:** Background page for the July 9 social-media questionnaire notice. It explains why the social-media questions were added in App Store Connect. Read it with T31, T42, and T43.

<a id="t45-app-store-whats-new"></a>

#### T45 — What’s New in the App Store

- **Target:** [English](https://developer.apple.com/app-store/whats-new/) · [Simplified Chinese](https://developer.apple.com/cn/app-store/whats-new/) — **Both read**
- **Content:** Creative-asset placements, Asset Library, product-page preview, subscription Bundles and Suites, and multiseat purchases, plus Apple Intelligence, ratings summaries, game tools, and parental time management. At the time of the snapshot, the English page marked creative assets, Asset Library, and previews as available, and said submissions from April 2027 must include iPhone Duo screenshots. The Simplified Chinese page still labeled the related asset features as launching “this fall” and did not mention the iPhone Duo screenshot deadline. The age section explains how social-media capabilities affect Time Allowances and the age questionnaire.
- **Relation:** Both language versions of the August 5 asset notice link the “announced in June” placements to this overview, each to its own language. The overview keeps changing. Do not read a later addition on this page back into the August notice as if the notice had said it. English and Chinese launch status differed. Recheck the current official page and the submission requirement before acting. Asset policy and specifications still follow dedicated pages such as T09 and T15.

## How to use the map

1. A news notice says what changed, when it takes effect, and which page to read. The linked policy or help page supplies qualifications, parameters, and procedures. Keep the publication date and the effective date separate.
2. For screenshots and creative assets, use T09, T15, T16, T11, T12, and T10 together: check that the asset is truthful and suitable for the audience, check specifications, preview devices and orientations, then manage and submit in App Store Connect.
3. For subscriptions, read T24, T27, and T28 with T48, T49, T50, and the current agreement attachments. Availability dates, eligibility review, the multiseat default, and organizational seat support can affect commercial and support work.
4. For retention messages, use T54 to review copy, offers, and localizations before requesting the T53 API. The feature is commercial, and the copy is still reviewed under App Review metadata rules.
5. For Siri AI, use T56 to assess Beta eligibility, region, age, and privacy isolation. The notice says dedicated terms and usage policies are still forthcoming, so preview behavior is not stable policy.
6. For age ratings, keep questionnaire facts, content frequency, social features, and regional requirements together. T42 is the workflow, T43 defines the answers, and T41 is the Korea regulator source. The hub page is [age ratings](../age-ratings/age-ratings.en-US.md).
7. Targets marked unread or partial stay unverified. When they can be read, record the actual content. Do not treat the link label as confirmed policy.

This catalog does not create Privacy Manifest, Required Reason API, IAP, external-purchase, or regional-terms topics. Those full sources are not in this snapshot package. Rows that mention payments or privacy only locate the announcement’s own links.
