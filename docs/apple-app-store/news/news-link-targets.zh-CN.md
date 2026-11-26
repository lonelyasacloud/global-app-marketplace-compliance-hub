---
id: apple.news.link-targets
platform: apple
language: zh-CN
authority: operational
status: partial
kb_checked_at: 2026-11-09
review_due: 2027-02-09
snapshot_package: 2026-11-10
regions: [global]
topics: [news, sources, change-history]
editorial_note: "Operational and historical source-to-target index, not an Apple policy rule. Checked 2026-11-09 (package 2026-11-10). RSS XML was not parsed. Many targets were only partially read or not read. This import did not re-open the live pages. English guidelines in the snapshot are dated 2026-10-16; the Simplified Chinese official guidelines page shows 2026-06-08. The supplied /cn/ license URL rendered English on 2026-11-09."
---

# 新闻公告直链与目标页分析 / News Body Links and Target-Page Analysis

## 范围与判读方法

本页登记[新闻索引](news-rss-index.zh-CN.md)里本轮纳入的 2026 年公告正文直链，并概括当时能打开的目标页，以及它和来源公告的关系。证据等级是**操作性 / 历史性索引**，不是审核规则，也不是必读清单。重复目标合并为同一个目标编号。公告映射仍保留每篇文章对它的引用。2026-07-09 的年龄分级公告是 2026-09-09 提交公告的直接目标，因此单独列出。

**RSS 边界仍未核实。** 两个 RSS 地址返回 `application/rss+xml`，当时的读取器无法解析。英文和中文新闻列表的近期条目也不完全一致。这份映射覆盖索引中的近期公告，以及被明确链接的年龄分级公告。它不是全部历史 RSS 条目的镜像，也不确定 feed 的精确边界。全站导航、页眉页脚、图片、CDN、社交分享按钮和同页锚点不算公告正文直链。目标页里的下一层链接，本轮没有递归展开。

**已读**表示打开并概括了正文。**部分**表示读了落地页或当时能取得的部分。**未读**表示目标可见，但读取器没有取到正文。未读目标的关系只限于链接文字和公告上下文，不能把链接标题当成已核实政策。

只在与 App 或本次发布相关时，才查阅审核规则、提交、年龄分级、付款、隐私和协议页面。活动页、通讯、一般开发资源、视频和论坛是背景链接，本身不构成 App Review 义务。

知识库核查日为 2026-11-09（包日期 2026-11-10）。本次导入没有重新打开这些页面。快照记录的入口：[英文新闻](https://developer.apple.com/news/)、[简体中文最新动态](https://developer.apple.com/cn/news/)、[英文 RSS](https://developer.apple.com/news/rss/news.rss)、[简体中文 RSS](https://developer.apple.com/cn/news/rss/news.rss)。

只在英文 URL 上出现的公告，下表中文是编辑摘要。

## 公告到直接目标的映射

| 公告 | 正文直接链接目标 |
| --- | --- |
| 2026-11-04 — [Now available: Retention messages for subscriptions](https://developer.apple.com/news/?id=fk9ps3gv) | [T53](#t53-retention-messaging-api) Retention Messaging API；[T54](#t54-configure-retention-messages) App Store Connect 配置页；[T55](#t55-auto-renewable-subscriptions) 自动续期订阅总览 |
| 2026-11-03 — [Siri AI is now open to all developers](https://developer.apple.com/news/?id=gdk2umrf) | [T56](#t56-siri-ai-developer-preview) Siri AI Developer Preview 文档；[T57](#t57-apple-intelligence-terms) Apple Intelligence 条款入口 |
| 2026-11-02 — [Upcoming: New age rating content descriptors in App Store Connect](https://developer.apple.com/news/?id=yxkh08us) | [T43](#t43-age-rating-values) 年龄分级值与定义；[T46](#t46-brazil-classification) 巴西司法与公共安全部官方分类入口；[T51](#t51-brazil-classification-guide) 巴西分类指南。公告说明所有 App 须在 2027-01-12 前完成新声明，并允许在适用条件下申请巴西官方评级。本行只有英文公告 URL，中文是编辑摘要 |
| 2026-11-03 — [使用最新 Beta 版本，做好充足准备](https://developer.apple.com/cn/news/?id=6gpufove) · [English](https://developer.apple.com/news/?id=6gpufove) | [T19](#t19-releases) 下载与发布说明；[T22](#t22-testing-a-beta-os) Beta OS 测试；[T23](#t23-feedback-assistant) 反馈入口。Beta 资源不构成独立审核义务 |
| 2026-10-29 — [Adjustments to the Taiwan storefront of the App Store on iOS and iPadOS](https://developer.apple.com/news/?id=w9mxlhek) | [T47](#t47-taiwan-storefront) 台湾繁体中文说明页；[T02](#t02-agreements-index) 协议索引；[T03](#t03-license-agreement) 当前协议；[T04](#t04-account-sign-in) 登录查看账户条款状态 |
| 2026-10-28 — [Say hello to Touch on Mac](https://developer.apple.com/news/?id=i9boeiqc) | [T52](#t52-touch-on-mac) Touch on Mac 资源页。背景资源，不构成单独上架义务 |
| 2026-10-22 — [Offer your subscriptions to businesses and schools](https://developer.apple.com/news/?id=yfo21au) | [T48](#t48-subscription-purchase-options) App Store Connect 购买选项帮助；[T49](#t49-multiseat-api) App Store Connect API 文档；[T50](#t50-wwdc-subscriptions) WWDC26 视频 |
| 2026-10-16 — [Updated App Review Guidelines are now available](https://developer.apple.com/news/?id=92th7e5i) | [T01](#t01-app-review-guidelines)。“Apple Developer website”的译文链接也指向同一指南 |
| 2026-10-16 — [Strengthening App Review Guidelines against nonconsensual intimate imagery and bait-and-switch apps](https://developer.apple.com/news/?id=vvzx6cul) | [T01](#t01-app-review-guidelines)，完整条款 |
| 2026-10-13 — [更新后的 Apple Developer Program 许可协议](https://developer.apple.com/cn/news/?id=17mwd36z) | [T02](#t02-agreements-index) 协议索引；[T03](#t03-license-agreement) 当前协议；[T04](#t04-account-sign-in) 登录以查看或接受条款 |
| 2026-10-06 — [Hello Developer: October 2026](https://developer.apple.com/news/?id=gv788oj6) | [T05](#t05-hello-developer) 专题汇总页（“Read now”） |
| 2026-10-05 — [为 iPhone Duo 准备并提交你的 App](https://developer.apple.com/cn/news/?id=kkphp5qo) | [T06](#t06-xcode) Xcode；[T07](#t07-iphone-duo-prepare) 三步准备指南；[T08](#t08-iphone-duo) iPhone Duo 页面；[T09](#t09-asset-best-practices) 素材最佳做法；[T10](#t10-manage-assets) 素材管理；[T11](#t11-app-preview) 预览规范；[T12](#t12-screenshots) 截屏规范；[T13](#t13-submitting) 提交指南；[T14](#t14-creative-assets-notice) 新素材公告 |
| 2026-10-05 — [借助 App Store 上的全新素材展示你的 App](https://developer.apple.com/cn/news/?id=ljpl7kyn) | [T09](#t09-asset-best-practices)；[T15](#t15-creative-asset-specs) 创意素材技术规范；[T11](#t11-app-preview)；[T12](#t12-screenshots)；[T16](#t16-screenshot-review-help) 截屏问题审核帮助；[T10](#t10-manage-assets) |
| 2026-10-02 — [macOS 中完全磁盘访问权限的更新](https://developer.apple.com/cn/news/?id=p6zjojqw) | 正文未发现指向独立内容页的直接链接。公告本身描述未来权限控制和完全磁盘访问风险 |
| 2026-10-01 — [Upcoming expiration of Developer ID Certification Authority (Sub-CA)](https://developer.apple.com/news/?id=w4atic4c) | [T17](#t17-certificates) 证书账户页；[T18](#t18-replace-developer-id) 更换证书指南 |
| 2026-09-18 — [使用新资源为 iPhone Duo 构建](https://developer.apple.com/cn/news/?id=nyuppv9r) | [T19](#t19-releases) Xcode 与系统发布版本；[T20](#t20-design-resources) 设计套件；[T21](#t21-workshops) 研讨会日历；[T08](#t08-iphone-duo) |
| 2026-09-16 — [使用最新 Beta 版本，做好充足准备](https://developer.apple.com/cn/news/?id=rfb1rooi) | [T19](#t19-releases) Beta 与发布说明；[T22](#t22-testing-a-beta-os)；[T23](#t23-feedback-assistant) |
| 2026-09-16 — [让你的订阅为 iOS 27 做好准备](https://developer.apple.com/cn/news/?id=likeohx4) | [T24](#t24-bundles-suites) 套装与套件规则；[T25](#t25-offer-bundles) 申请入口；[T26](#t26-bundles-video) 视频；[T27](#t27-purchase-options) 购买选项；[T28](#t28-group-subscriptions-video) WWDC 订阅视频 |
| 2026-09-16 — [App Tracking Transparency 在欧盟地区的更新](https://developer.apple.com/cn/news/?id=idsft9ai) | [T29](#t29-user-privacy)。中文文章 URL 返回 Internal Error。已读取英文对应正文，目标页 T29 可访问 |
| 2026-09-09 — [为 iPhone Duo 做好准备](https://developer.apple.com/cn/news/?id=vn8abkxx) | [T08](#t08-iphone-duo) 视频、实验室和准备资源 |
| 2026-09-09 — [App Store 现已接受适用于最新版操作系统的 App 和游戏提交](https://developer.apple.com/cn/news/?id=k1mtkt1k) | [T30](#t30-apple-silicon) Apple 芯片优化文档；[T31](#t31-age-questionnaire-notice) 年龄问卷公告；[T09](#t09-asset-best-practices)；[T13](#t13-submitting) |
| 2026-09-01 — [对基于 Intel 的 macOS App 的 Rosetta 支持即将发生变化](https://developer.apple.com/cn/news/?id=w5ngl9k2) | [T32](#t32-rosetta) Rosetta 环境；[T30](#t30-apple-silicon)；[T33](#t33-porting) 移植指南；[T34](#t34-forums) 开发者论坛 |
| 2026-08-27 — [App、App 内购买项目及订阅的税务和价格信息更新](https://developer.apple.com/cn/news/?id=artln8br) | [T35](#t35-tax-self-link)。“进一步了解”在本次解析中指回同一公告，没有独立目标页 |
| 2026-08-26 — [亮新篇，来耀眼](https://developer.apple.com/cn/news/?id=s6spdug0) | [T36](#t36-apple-event)。中文公告只将 apple.com.cn 显示为直接链接，“Apple TV”是普通文本。英文版把 apple.com 设为直接链接。可读取文本里，Apple TV 和 YouTube Live 不是独立锚点 |
| 2026-08-24 — [更新：“通过 Apple 登录”的新域名](https://developer.apple.com/cn/news/?id=1ptvdtcm) | [T37](#t37-sign-in-with-apple-hig) Sign in with Apple 人机界面指南；[T38](#t38-private-relay) 私密中继技术文档 |
| 2026-08-18 — [适用于欧盟 App 的变更](https://developer.apple.com/cn/news/?id=gmws0jgp) | [T39](#t39-eu-terms) 欧盟条款与分发、付款说明；[T40](#t40-eu-events) 预约沟通日历 |
| 2026-08-18 — [更新后的 Apple Developer Program 许可协议](https://developer.apple.com/cn/news/?id=0cgo95n6) | [T03](#t03-license-agreement) 附件 14；[T04](#t04-account-sign-in) 接受条款；[T02](#t02-agreements-index)。历史公告，见新闻索引 |
| 2026-08-12 — [韩国的年龄分级更新](https://developer.apple.com/cn/news/?id=oj3r9pvw) | [T41](#t41-grac) GRAC 官方站；[T42](#t42-set-age-rating) 年龄分级覆盖操作；[T43](#t43-age-rating-values) |
| 2026-08-05 — [为 App Store 上的全新创意素材资源做好准备](https://developer.apple.com/cn/news/?id=kug6m2ea) · [English](https://developer.apple.com/news/?id=kug6m2ea) | [T45](#t45-app-store-whats-new) 6 月宣布的 App Store 新功能概览；[T09](#t09-asset-best-practices)。中英文正文中的两个直接链接均已打开，并分别核对到对应语言的目标页 |
| 2026-07-09 — [年龄分级调查问卷现在包含社交媒体问题](https://developer.apple.com/cn/news/?id=tlur8uvi)（关联目标页，不界定 RSS 边界） | [T44](#t44-time-allowances) Time Allowances 说明；[T42](#t42-set-age-rating)；[T43](#t43-age-rating-values) |

## 目标页摘要与关系

### 审核指南、协议与账号

<a id="t01-app-review-guidelines"></a>

#### T01 — App Review Guidelines

- **目标：** [英文](https://developer.apple.com/app-store/review/guidelines/) · [简体中文](https://developer.apple.com/cn/app-store/review/guidelines/) — **已读**
- **内容：** 英文页是 2026-10-16 的当前基准，涵盖 UGC 与 AI 内容治理、创意素材、隐藏功能、外部购买链接及严重安全违规。中文页仍为 2026-06-08。
- **关系：** 两篇 10 月 16 日公告都把该页作为规范正文。第一篇列出具体修订条款，第二篇解释非自愿私密影像、bait-and-switch 和执行后果。知识库摘要见[审核指南摘要](../app-review-guidelines/guidelines-summary.zh-CN.md)。

<a id="t02-agreements-index"></a>

#### T02 — 许可协议索引

- **目标：** [英文](https://developer.apple.com/support/terms/) · [简体中文](https://developer.apple.com/cn/support/terms/) — **已读**
- **内容：** Apple 协议、许可条款和相关准则的入口页。
- **关系：** 两篇协议更新公告指向该索引。公告里的变更应与当前协议正文和附件一起核对。

<a id="t03-license-agreement"></a>

#### T03 — Apple Developer Program 许可协议

- **目标：** [当前英文协议](https://developer.apple.com/support/terms/apple-developer-program-license-agreement/) · [提供的中文路径；2026-11-09 页面正文为英文](https://developer.apple.com/cn/support/terms/apple-developer-program-license-agreement/) — **已读**
- **内容：** 说明 Apple 软件与服务许可、开发和测试用途、分发方式、开发者义务及附件或计划条款。快照核对到的当前文本包括 Live Assistance API、App Replacement Entitlement、HomeView 与 CarPlay 小组件、多席位订阅和税务信息处理。
- **关系：** 10 月 13 日公告逐条列出协议变化。8 月 18 日公告说明附件 14 与欧盟条款的生效日期。协议是约束性文本，新闻摘要不能替代协议。知识库摘要见[许可协议](../developer-program/license-agreement.zh-CN.md)，其中文是编辑摘要，不是 Apple 的正式译文。

<a id="t04-account-sign-in"></a>

#### T04 — 账户登录

- **目标：** [登录账户](https://developer.apple.com/account/) · [账户资源](https://developer.apple.com/account/resources/) — **未读：登录墙 / 读取器 Internal Error**
- **内容：** 需要已授权的开发者账户。读取器返回 Internal Error，无法查看账户内的协议状态。
- **关系：** 公告要求 Account Holder 或有权限的人员查看并接受更新条款。具体权限和待接受状态必须登录后确认。

<a id="t46-brazil-classification"></a>

#### T46 — 巴西官方分类

- **目标：** [Classind — Ministério da Justiça e Segurança Pública](https://www.gov.br/mj/pt-br/assuntos/seus-direitos/classificacao-1) — **部分**
- **内容：** 巴西司法与公共安全部的官方“Classificação Indicativa”入口，提供分类说明、申请服务和联系渠道。这是监管来源，不是 Apple 规则正文。
- **关系：** 11 月 2 日年龄分级公告说明，如果共享位置 App 在巴西有合理的更低分级理由，可向 MJSP 申请官方评级。核验后，Apple 会展示官方地区评级。本页是该申请路径的官方入口，不能用普通的 Apple 问卷结果代替。

<a id="t51-brazil-classification-guide"></a>

#### T51 — 巴西分类指南

- **目标：** [Guia de Classificação — Ministério da Justiça e Segurança Pública](https://www.gov.br/mj/pt-br/assuntos/seus-direitos/classificacao-1/paginas-classificacao-indicativa/guia-de-classificacao) — **已读**
- **内容：** MJSP 的分类指南页，列出 2025 年第 5 版《视听、应用和 RPG 实用分类指南》，说明 ClassInd 年龄段和内容描述符标准，以及在数字平台、网站和广告中展示分类的要求。监管来源。
- **关系：** 11 月 2 日公告把该页作为巴西官方评级申请的监管材料入口。它可以帮助准备本地分类证据，但不能替代 App Store Connect 问卷或 App Review。

<a id="t47-taiwan-storefront"></a>

#### T47 — 台湾店面调整说明

- **目标：** [台湾店面调整说明（繁体中文）](https://developer.apple.com/tw/support/adjustments-to-the-taiwan-storefront/) — **部分**
- **内容：** 繁体中文目标链接已确认，当时的读取器没有展开完整正文。根据公告，该页是 iOS/iPadOS 台湾店面标准 App 内购买和付费 App 交易佣金调整的本地化说明。
- **关系：** 10 月 29 日公告的本地化目标页。与公告及当前许可协议一起阅读。该调整只针对台湾店面和公告列明的交易类型，不是全球费率。

<a id="t48-subscription-purchase-options"></a>

#### T48 — 自动续期订阅购买选项

- **目标：** [Manage purchase options for an auto-renewable subscription](https://developer.apple.com/help/app-store-connect/manage-subscriptions/manage-purchase-options-for-auto-renewable-subscriptions) — **已读**
- **内容：** App Store Connect 帮助页，说明如何配置自动续期订阅的购买可用性，并管理 App Store、Apple Business 和 Apple School Manager 等渠道。
- **关系：** 10 月 22 日公告说明多席位购买默认启用且可调整。本页是该项设置的操作入口。产品不提供组织或学校购买时，应核对是否需要关闭相应可用性。

<a id="t49-multiseat-api"></a>

#### T49 — 组织多席位订阅 API

- **目标：** [App Store Connect API: Configuring multiseat subscriptions for organizations](https://developer.apple.com/documentation/appstoreconnectapi/configuring-multi-seat-subscriptions-for-organizations) — **部分**
- **内容：** 用于自动化配置组织多席位订阅的 API 文档入口。读取器只取得 JavaScript 文档壳，没有展开完整参数和权限说明。
- **关系：** 公告把它作为组织批量购买的技术入口。开发前必须用浏览器或本地文档核对 API 版本、角色权限，以及沙盒与生产环境的限制。

<a id="t50-wwdc-subscriptions"></a>

#### T50 — 群组和组织订阅视频

- **目标：** [Offer subscriptions to groups and organizations — WWDC26](https://developer.apple.com/videos/play/wwdc2026/391/) — **已读**
- **内容：** WWDC26 视频，补充群组购买、组织购买和多席位订阅的产品与实现背景。
- **关系：** 10 月 22 日公告的延伸学习材料。视频属于背景，不单独产生 App Review 义务，但可与 T48、T49 一起用于设计和测试。

<a id="t52-touch-on-mac"></a>

#### T52 — Touch on Mac 资源页

- **目标：** [Get ready for Touch on Mac](https://developer.apple.com/touch-on-mac/) — **已读**
- **内容：** 汇总触控 Mac App 的视频、Group Labs、Xcode 27.3 Beta 资源，以及手势识别、拖放和 macOS 设计文档。
- **关系：** 10 月 28 日公告的 “Explore now” 目标页。它是平台适配学习资源，不是审核政策。仅当产品适配 MacBook Pro 触控输入时纳入工程计划。

<a id="t53-retention-messaging-api"></a>

#### T53 — Retention Messaging API

- **目标：** [Retention Messaging API](https://developer.apple.com/documentation/retentionmessaging/) — **部分**
- **内容：** API 文档入口当时只返回 JavaScript 页面壳。公告说明可依据订阅详情选择向用户展示的挽留信息，API 访问需申请。
- **关系：** 11 月 4 日公告的自动化技术入口。开发前应在可读文档或账户权限页面确认 API 版本、授权范围和审核流程。

<a id="t54-configure-retention-messages"></a>

#### T54 — 配置订阅挽留信息

- **目标：** [Configure retention messages in App Store Connect](https://developer.apple.com/help/app-store-connect/manage-subscriptions/configure-retention-messages/) — **已读**
- **内容：** 每个 App 最多可创建 10 条挽留信息。信息包含必填文案，以及可选图片或挽留优惠。一条信息可关联多个订阅，但每个订阅一次只能有一条有效挽留信息。创建、修改和提交审核需要相应的 App Store Connect 角色。
- **关系：** 该页把公告中的订阅者资格和等待时间落成操作步骤，并写明直接约束：文案必须准确、相关、不令人反感，不得包含具体价格或折扣，不得使用强迫性或无法验证的结果声称。

<a id="t55-auto-renewable-subscriptions"></a>

#### T55 — 自动续期订阅总览

- **目标：** [Auto-renewable Subscriptions](https://developer.apple.com/app-store/subscriptions/) — **部分**
- **内容：** 自动续期订阅的产品与技术总览，作为挽留信息、订阅优惠和 StoreKit 能力的导航入口。
- **关系：** 公告用它作为订阅能力的背景入口。具体挽留文案、优惠和审核要求以 T54 为准。

<a id="t56-siri-ai-developer-preview"></a>

#### T56 — Siri AI Developer Preview

- **目标：** [Siri AI Developer Preview](https://developer.apple.com/documentation/appintents/siri-ai-developer-preview) — **部分**
- **内容：** Siri AI 与 App Intents 的开发者预览文档入口。读取器只返回 JavaScript 页面壳。
- **关系：** 11 月 3 日公告的技术入口。该能力仍处于 iOS、iPadOS、macOS 和 visionOS 27.3 Beta。欧盟的 iOS、iPadOS 和 watchOS 暂不可用，13 岁以下用户不可用，并且 Apple 写明后续还会发布使用条款和政策。不应把它当作当前普遍上架要求。

<a id="t57-apple-intelligence-terms"></a>

#### T57 — Apple Intelligence 条款

- **目标：** [Apple Intelligence and Siri terms](https://support.apple.com/148587) — **未读：support.apple.com 返回 HTTP 429**
- **内容：** Siri AI 公告将该页作为 Apple Intelligence 条款入口。支持站点对读取器限流，正文未能展开。
- **关系：** 接入 Siri AI 前必须回到该页核对地区、年龄、账户、数据和使用限制。不能只依据开发者新闻摘要上线。

### iPhone Duo、素材与提交

<a id="t05-hello-developer"></a>

#### T05 — Hello Developer: October 2026

- **目标：** [Hello Developer October 2026](https://developer.apple.com/hello/october26) — **已读**
- **内容：** 专题汇总 iPhone Duo 提交三步、Group Labs、性能与效率活动、新增的八种文档语言、App Store 创意素材、Apple Pay 合作伙伴、Xcode 新项目格式，以及 Duo 设计与开发文档。
- **关系：** 10 月 6 日简讯的 “Read now” 指向此页。它是资源导航，不是独立审核规则。其中 iPhone Duo 与素材主题会再链到本表的相关公告和指南。

<a id="t06-xcode"></a>

#### T06 — Xcode

- **目标：** [Xcode](https://developer.apple.com/cn/xcode/) — **已读**
- **内容：** Apple 开发工具产品页，提供 Xcode 下载、版本信息和开发者资源。快照记录的是这个中文路径。
- **关系：** iPhone Duo 公告要求使用支持该设备的 Xcode 27.1 重新编译，并检查不同姿态和方向。它是公告中的工具下载入口。

<a id="t07-iphone-duo-prepare"></a>

#### T07 — iPhone Duo 三步准备指南

- **目标：** [Prepare — iPhone Duo](https://developer.apple.com/iphone-duo/prepare/) — **已读**
- **内容：** 如何检查 Duo 的动态窗口和屏幕尺寸、设备姿态和方向，并用适配式布局避免硬编码尺寸或方向假设造成的界面问题。
- **关系：** 为 10 月 5 日的重新构建和测试建议提供技术细节。这是兼容性准备，不是审核条款。

<a id="t08-iphone-duo"></a>

#### T08 — iPhone Duo 准备资源页

- **目标：** [iPhone Duo — Apple Developer](https://developer.apple.com/cn/iphone-duo/) — **已读**
- **内容：** 设备适配信息、视频、开发资源和开发者活动入口。快照记录的是这个中文路径。
- **关系：** 9 月两篇 Duo 公告和 10 月准备公告都用它汇集技术准备入口。

<a id="t09-asset-best-practices"></a>

#### T09 — App Store 素材最佳做法

- **目标：** [英文](https://developer.apple.com/app-store/asset-best-practices/) · [简体中文](https://developer.apple.com/cn/app-store/asset-best-practices/) — **两页均已读**
- **内容：** 素材须准确体现 App 内容、功能或品牌，适合 4+ 受众，并聚焦核心体验。避免具体价格、折扣、URL、无法核实的奖项、其他平台标识和误导性内容。图片和视频应清晰、适配设备方向，并在静音状态下可理解。
- **关系：** 8 月 5 日的中英文公告都把此页作为“推荐做法和资源”的直接目标，其中包括设计模板。它也支撑两篇 10 月 5 日素材公告和 9 月 9 日提交公告。新素材不只是技术规格，还受元数据准确性、受众适宜性和审核政策约束。

<a id="t10-manage-assets"></a>

#### T10 — 管理 App Store 素材

- **目标：** [管理 App Store 素材](https://developer.apple.com/cn/help/app-store-connect/manage-app-information/manage-your-app-store-assets) — **已读**
- **内容：** 在 App Store Connect 素材库集中查看、编辑和整理素材及相关元数据，管理使用位置、状态、复用或归档。
- **关系：** 10 月 5 日的 Duo 公告和创意素材公告都指向此帮助。它把“新资产可集中管理、可提前提交审核”落到 App Store Connect 工作流。

<a id="t11-app-preview"></a>

#### T11 — App 预览规范

- **目标：** [App 预览规范](https://developer.apple.com/cn/help/app-store-connect/reference/app-information/app-preview-specifications) — **已读**
- **内容：** 说明 App 预览适用的平台、语言和设备尺寸，以及数量、视频方向、时长和文件格式限制。
- **关系：** Duo 公告要求更新预览以适配设备方向。素材公告说明预览可与新创意素材一起呈现。

<a id="t12-screenshots"></a>

#### T12 — 截屏规范

- **目标：** [截屏规范](https://developer.apple.com/cn/help/app-store-connect/reference/app-information/screenshot-specifications) — **已读**
- **内容：** 规定各平台和设备尺寸的截屏要求、支持格式和数量上限，并要求截屏准确展示 App 实际体验。
- **关系：** 两篇 10 月 5 日公告把它作为提交新设备素材的规范依据。Duo 公告给出自 2027 年 4 月起必须包含 Duo 截屏的时间要求。

<a id="t13-submitting"></a>

#### T13 — 提交 App

- **目标：** [App Store 提交](https://developer.apple.com/cn/app-store/submitting/) — **已读**
- **内容：** 汇总提交到 App Store 的准备、构建、审核与发布流程，并列出未来的 Xcode 与 SDK 最低提交要求。
- **关系：** 9 月 9 日公告写明自 2027 年 4 月起各平台需使用 27 系列 SDK。10 月 Duo 公告另增加 Duo 截屏要求。本页提供提交流程，公告提供生效日期。

<a id="t14-creative-assets-notice"></a>

#### T14 — 新创意素材公告

- **目标：** [借助 App Store 上的全新素材展示你的 App](https://developer.apple.com/cn/news/?id=ljpl7kyn) — **已读**
- **内容：** 说明产品页顶部横幅、搜索结果素材和素材库管理，以及提交前跨设备、方向和深色模式的预览。
- **关系：** 是 10 月 Duo 提交公告中的关联新闻，也是创意素材各项操作规范的概览。

<a id="t15-creative-asset-specs"></a>

#### T15 — 创意素材规范

- **目标：** [创意素材规范](https://developer.apple.com/cn/help/app-store-connect/reference/app-information/creative-assets-specifications) — **已读**
- **内容：** 定义新产品页和搜索等创意素材的类型、尺寸、文件和展示要求。
- **关系：** 为 10 月创意素材公告中的新图片和视频入口提供可提交的规格基准。与 T09 的内容要求一起使用。

<a id="t16-screenshot-review-help"></a>

#### T16 — App Review 截屏帮助

- **目标：** [App Review Help: screenshots](https://developer.apple.com/cn/help/app-review/guideline-reference/2-3-3-screenshots) — **已读**（中文路径显示英文标题）
- **内容：** 截屏应展示真实 App 界面和核心功能，不应以不准确或误导性的内容呈现应用。
- **关系：** 10 月创意素材公告把它作为避免常见截屏审核问题的帮助页。它补充 T12 的格式规格，重点是内容是否真实。

### 证书、测试与订阅

<a id="t17-certificates"></a>

#### T17 — Certificates, Identifiers & Profiles

- **目标：** 公告锚点是开发者账户里的 Certificates, Identifiers & Profiles。**读取器未能解析目标 URL，因此这里不记录猜测地址。**
- **状态：** **未读：读取器 Internal Error**
- **内容：** 目标是 Developer Account 中的证书管理区域。由于没有取得 URL 和账户页正文，不推断证书状态或操作步骤。
- **关系：** 证书到期公告要求在该账户区域检查 2027-02-01 前到期的证书。实际检查需要登录。

<a id="t18-replace-developer-id"></a>

#### T18 — 更换旧 Sub-CA Developer ID 证书

- **目标：** [更换由先前 Sub-CA 颁发的 Developer ID 证书](https://developer.apple.com/cn/help/account/certificates/replace-developer-id-certificates) — **已读**
- **内容：** 说明如何识别受影响证书、申请 G2 Sub-CA 替代证书，并按发行物重新签名。`.pkg` 与已经公证的 Mac App 所受影响不同。
- **关系：** 落实 10 月 1 日到期公告：在期限前重签安装包，后续 Mac App 更新改用新证书并保留安全时间戳。

<a id="t19-releases"></a>

#### T19 — 发布版本与下载

- **目标：** [Apple Developer releases](https://developer.apple.com/cn/news/releases/) — **已读**
- **内容：** 汇总 Xcode 和 Apple 平台正式版与 Beta 版的下载及发布说明。
- **关系：** 9 月 16 日 Beta 公告和 9 月 18 日 Duo 资源公告用它定位 Xcode 27.1、27.2 与系统 Beta。

<a id="t20-design-resources"></a>

#### T20 — Apple 设计资源

- **目标：** [Apple Design Resources](https://developer.apple.com/cn/design/resources/) — **已读**
- **内容：** 提供 Apple 平台设计模板和 UI 资源，包括 Figma 与 Sketch 资源。
- **关系：** Duo 资源公告把它作为设备设计套件的下载入口，用来制作适配新设备的界面和商店素材。

<a id="t21-workshops"></a>

#### T21 — 与 Apple 会面的研讨会日历

- **目标：** [Workshop schedule](https://developer.apple.com/events/view/upcoming-events?search=workshop) — **未读：动态页面没有返回内容**
- **内容：** 按 workshop 过滤的活动日历。读取器返回 0 行，无法确认当时可报名的场次。
- **关系：** Duo 资源公告指向全球研讨会日程，供开发者了解适配工作。

<a id="t22-testing-a-beta-os"></a>

#### T22 — 测试 Beta 操作系统

- **目标：** [Testing a beta OS](https://developer.apple.com/documentation/xcode/testing-a-beta-os) — **未读：读取器 Internal Error**
- **内容：** 链接标题表明这是 Xcode 文档中的 Beta OS 测试指南，但没有读到正文。
- **关系：** 9 月 16 日公告建议在新 Beta 系统上验证 App。具体步骤需在能够打开的 Apple 文档里复核。

<a id="t23-feedback-assistant"></a>

#### T23 — 反馈助理

- **目标：** [Feedback Assistant](https://developer.apple.com/cn/feedback-assistant/) — **未读：读取器 Internal Error**
- **内容：** Apple 的问题反馈入口。页面正文未能读取。
- **关系：** Beta 公告建议通过该入口报告系统或兼容性问题。

<a id="t24-bundles-suites"></a>

#### T24 — 自动续期订阅的套装和套件

- **目标：** [为自动续期订阅创建套装和套件](https://developer.apple.com/cn/app-store/subscriptions/bundles-and-suites/) — **已读**
- **内容：** 解释单开发者与多开发者 Bundle，以及单开发者 Suite。要求使用 StoreKit 2，并支持相应的 27 系列系统。一个 Bundle 最多 5 项订阅，一个 Suite 最多覆盖 15 个 App。页面还说明申请与审批、多开发者法律附件、升级、取消和订阅变更。
- **关系：** 9 月 16 日订阅公告里“套装和套件”的规则与技术要求来源。公告还提到多席位购买，需结合 T27 和 T28。

<a id="t25-offer-bundles"></a>

#### T25 — 申请套装和套件

- **目标：** 公告中的“提供套装和套件”控件。读取器点击后回到 T24，没有确认单独的 App Store Connect 表单 URL，因此不记录猜测地址。
- **状态：** **未读：动态目标未解析**
- **关系：** T24 说明需要提交申请并等待 Apple 审核。实际入口要在已登录的 App Store Connect 或官方页面上确认。

<a id="t26-bundles-video"></a>

#### T26 — 套装和套件视频

- **目标：** 尝试打开的中文地址：[WWDC26 视频](https://developer.apple.com/cn/videos/play/wwdc2026/210/?time=530) — **未读：cache miss**。快照记录的英文入口：[WWDC26 视频](https://developer.apple.com/videos/play/wwdc2026/210/)。
- **内容：** 视频未能稳定加载，不根据标题扩写内容。
- **关系：** 订阅公告把它作为 Bundle 与 Suite 的演示补充。可访问后再核对技术细节。

<a id="t27-purchase-options"></a>

#### T27 — 管理自动续期订阅的购买选项

- **目标：** [App Store Connect 帮助](https://developer.apple.com/cn/help/app-store-connect/manage-subscriptions/manage-purchase-options-for-auto-renewable-subscriptions/) — **已读**
- **内容：** 在 App Store Connect 中配置自动续期订阅的购买选项、可用性和相关销售渠道。这条关系在快照里使用带尾部斜线的 `/cn/` 帮助页。10 月 22 日公告所引的英文路径帮助页是 T48。
- **关系：** 9 月 16 日公告指出多席位购买默认开启，开发者可按 App Store、Apple Business 和 Apple School Manager 管理可用性。该帮助页是实际配置入口。

<a id="t28-group-subscriptions-video"></a>

#### T28 — 向群组和组织提供订阅

- **目标：** [WWDC26 视频](https://developer.apple.com/cn/videos/play/wwdc2026/391/) — **已读**
- **内容：** 介绍面向群组和机构的订阅分发，包括群组购买、批量购买、席位分配和组织使用场景。快照记录的是这个中文路径。10 月 22 日公告所引的英文路径视频是 T50。
- **关系：** 补充 9 月 16 日公告中的多席位购买，用来区分个人邀请共享和通过 Apple Business 或 School Manager 的批量配置。

### 隐私、年龄分级与平台过渡

<a id="t29-user-privacy"></a>

#### T29 — 用户隐私与数据使用

- **目标：** [Apple 用户隐私与数据使用](https://developer.apple.com/cn/app-store/user-privacy-and-data-use/) — **已读**
- **内容：** 汇总 App 隐私标签、App 隐私报告、跟踪定义，以及 App Tracking Transparency 的用户许可原则。
- **关系：** 欧盟 ATT 公告只改变指定地区的系统提示形态。本页用来理解隐私和用户许可背景。公告明确：跟踪何时需要征得许可的规则没有变化。

<a id="t30-apple-silicon"></a>

#### T30 — Apple silicon 文档入口

- **目标：** [公告中的中文链接](https://developer.apple.com/cn/documentation/apple-silicon) · [English](https://developer.apple.com/documentation/apple-silicon) — **未读：需要 JavaScript 的文档**
- **内容：** 页面要求 JavaScript。可见 Markdown 入口，但读取器不支持 `text/markdown`，因此没有取得正文。
- **关系：** 9 月提交公告指向 Apple 芯片优化。Rosetta 公告也要求增加原生 Apple silicon 支持。链接标题和公告上下文表明这是架构适配文档入口。正文未经核实。

<a id="t31-age-questionnaire-notice"></a>

#### T31 — 年龄分级问卷与社交媒体

- **目标：** [年龄分级调查问卷现在包含社交媒体问题](https://developer.apple.com/cn/news/?id=tlur8uvi) — **已读**
- **内容：** 社交媒体功能按内容的发现、传播或互动能力判断，而不是按 App Store 主类别。相关 App 的产品页会显示新描述符。若社交功能对未满 13 岁的用户关闭，会影响该年龄段的 Time Allowances 分类。自 2026 年 9 月起，新 App、更新和替代分发公证需要回答问卷。
- **关系：** 9 月 9 日操作系统提交公告直接链接此页。它解释“回答年龄分级问题”的背景，以及如何判定社交功能。

<a id="t32-rosetta"></a>

#### T32 — Rosetta 转换环境

- **目标：** [About the Rosetta translation environment](https://developer.apple.com/documentation/apple-silicon/about-the-rosetta-translation-environment) — **未读：需要 JavaScript 的文档**
- **内容：** 文档页需要 JavaScript，Markdown 内容无法由当时的读取器读取。
- **关系：** 9 月 1 日公告把它作为 Rosetta 支持结束的背景资料。迁移细节应在能够打开的文档里复核。

<a id="t33-porting"></a>

#### T33 — 将 macOS App 移植到 Apple silicon

- **目标：** [Porting your macOS apps to Apple silicon](https://developer.apple.com/documentation/apple-silicon/porting-your-macos-apps-to-apple-silicon) — **未读：需要 JavaScript 的文档**
- **内容：** JavaScript 页面没有提供正文，无法核对具体的迁移或构建指令。
- **关系：** Rosetta 公告建议制作 Universal 或原生 Apple silicon 构建。此页是公告指向的移植指南。本轮没有核实其中的步骤。

<a id="t34-forums"></a>

#### T34 — Apple Developer Forums

- **目标：** [Apple Developer Forums](https://developer.apple.com/forums/) — **部分**
- **内容：** 读到了论坛分类和讨论列表，但没有具体的 Rosetta 讨论串 URL。
- **关系：** 公告把论坛作为开发者提问入口，不是规范来源。具体问题仍要查论坛里的相关主题。社区材料的用法见[社区经验](../community-evidence/community-evidence.zh-CN.md)。

<a id="t35-tax-self-link"></a>

#### T35 — 税务和价格公告（自链接）

- **目标：** [App、App 内购买项目及订阅的税务和价格信息更新](https://developer.apple.com/cn/news/?id=artln8br) — **已读：同一页**
- **内容：** 公告说明因税法和汇率变化而调整各店面价格或收入，并提示检查税务，以及自动定价和手动定价的差异。
- **关系：** 正文“进一步了解”在本次提取中指回同一公告，因此没有额外的独立帮助页。

<a id="t36-apple-event"></a>

#### T36 — Apple 活动站点

- **目标：** [Apple 中国大陆官网](https://apple.com.cn/) · [英文 Apple 首页](https://www.apple.com/) — **部分**
- **内容：** Apple 官网首页可以打开。没有从该首页核验活动回放页。
- **关系：** 8 月 26 日公告用于宣传 9 月 9 日活动的观看入口，与 App 审核规则无关。中文正文里的 Apple TV 是纯文本，不是链接。

<a id="t37-sign-in-with-apple-hig"></a>

#### T37 — “通过 Apple 登录”人机界面指南

- **目标：** [Sign in with Apple — Human Interface Guidelines](https://developer.apple.com/cn/design/human-interface-guidelines/sign-in-with-apple) — **未读：需要 JavaScript**
- **内容：** 页面要求 JavaScript。读取器只返回需要启用脚本的提示。
- **关系：** 8 月 24 日公告要求系统接受新的 `private.icloud.com` 地址。该 HIG 链接是 Sign in with Apple 在界面和设计层面的入口。正文未读。

<a id="t38-private-relay"></a>

#### T38 — 私密电子邮件中继文档

- **目标：** [Communicating using the private email relay service](https://developer.apple.com/documentation/signinwithapple/communicating-using-the-private-email-relay-service/) — **未读：JavaScript / 不支持 Markdown**
- **内容：** JavaScript 页面提供 Markdown 链接，但读取器不支持 `text/markdown`。
- **关系：** 公告用该技术文档说明如何通过私密中继通信，并要求更新邮箱域名白名单和验证逻辑。文档正文未读。

<a id="t39-eu-terms"></a>

#### T39 — 欧盟 App 业务条款页面

- **目标：** [Changes for apps in the European Union](https://developer.apple.com/cn/support/apps-in-the-eu/) — **已读**
- **内容：** 汇总欧盟条款、App Store 与替代付款、替代分发与网页分发、费用与佣金、儿童安全措施、公证及资格条件。具体适用取决于分发路径、店面、所选条款和相应附件。
- **关系：** 8 月 18 日欧盟公告的直接目标。它展开公告中的统一条款、5% 核心技术佣金、替代付款和分发资格变化。

<a id="t40-eu-events"></a>

#### T40 — 欧盟专题预约日历

- **目标：** [Meet with Apple — European events](https://developer.apple.com/events/view/upcoming-events?search=European) — **未读：动态页面没有返回内容**
- **内容：** 活动日历过滤条件为 European。读取器没有返回场次内容。
- **关系：** 欧盟公告里与 Apple 预约沟通的可选入口，不是条款解释，也不是合规依据。

<a id="t41-grac"></a>

#### T41 — 韩国 GRAC

- **目标：** [Game Rating and Administration Committee — English](https://www.grac.or.kr/english/) — **部分**
- **内容：** 打开了韩国游戏评级和管理委员会的英文官方站首页，没有从首页取得具体的分类编号记录。监管来源。
- **关系：** 韩国公告要求符合条件的游戏和娱乐 App 在后续版本中提供官方 RCN。分类编号和授权范围应由 GRAC 的官方记录确认。

<a id="t42-set-age-rating"></a>

#### T42 — 设置 App 年龄分级

- **目标：** [App Store Connect 帮助](https://developer.apple.com/cn/help/app-store-connect/manage-app-information/set-an-app-age-rating) — **已读**
- **内容：** 说明年龄分级问卷、内容与功能及其出现频率、分级如何生成、地区覆盖，以及相关提交操作。
- **关系：** 7 月 9 日社交媒体公告和韩国 RCN 公告都链接该操作指南。前者关注问卷字段，后者关注韩国地区覆盖。

<a id="t43-age-rating-values"></a>

#### T43 — 年龄分级的值和定义

- **目标：** [英文](https://developer.apple.com/help/app-store-connect/reference/app-information/age-ratings-values-and-definitions) · [简体中文](https://developer.apple.com/cn/help/app-store-connect/reference/app-information/age-ratings-values-and-definitions) — **已读**
- **内容：** 定义问卷中的内容与功能类别、当前与旧系统的年龄分级值，以及澳大利亚、巴西、韩国、越南等地区评级。快照没有记录这两个帮助页之间的更新日期差。
- **关系：** 韩国公告用该页解释本地分级值。社交媒体公告用它判断社交、UGC 和年龄控制等答案。11 月 2 日公告把它作为共享位置、约会与恋爱关系新声明的定义和地区分级背景。知识库摘要见[年龄分级](../age-ratings/age-ratings.zh-CN.md)。

<a id="t44-time-allowances"></a>

#### T44 — “时间额度”功能公告

- **目标：** [“时间额度”功能介绍](https://developer.apple.com/cn/news/?id=0d2gpmml) — **已读**
- **内容：** 介绍 iOS、iPadOS 和 macOS 27 的家长时间管理类别。社交媒体类别按 App 功能确定，而不是按 App Store 类别。若社交功能只对 13 岁及以上用户开放，仍须通过问卷和年龄范围机制表达。
- **关系：** 7 月 9 日社交媒体问卷公告的背景页，用来解释 Apple 为什么在 App Store Connect 加入社交媒体问题。与 T31、T42、T43 一起阅读。

<a id="t45-app-store-whats-new"></a>

#### T45 — App Store 新功能概览

- **目标：** [英文 What’s New](https://developer.apple.com/app-store/whats-new/) · [简体中文 App Store 新功能](https://developer.apple.com/cn/app-store/whats-new/) — **两页均已读**
- **内容：** 汇总创意素材展示位、Asset Library、产品页预览、订阅套装与套件、多席位购买，也介绍 Apple Intelligence、评分摘要、游戏工具和家长时间管理。快照核对时，英文页把素材、素材库和预览标为“现已推出”，并写明自 2027 年 4 月起提交的 App 和游戏须包含 iPhone Duo 截屏。简体中文页对相关素材功能仍标为“今年秋季推出”，而且该页没有出现 iPhone Duo 截屏期限。年龄部分说明社交媒体功能会影响“时间额度”分类和年龄问卷。
- **关系：** 8 月 5 日中英文素材公告都把“6 月份宣布”的推广方式链接到此概览，两种语言分别指向对应语言页面。概览会持续更新。不要把后来加到概览页上的事项回写成 8 月公告的原文。中英文页面的推出状态当时有时间差。执行前应再核实当前官方页面和提交要求。素材政策和规格仍以 T09、T15 等专门页面为准。

## 怎么使用这份映射

1. 新闻公告说明发生了什么、何时生效、应该看哪一页。被链接的规范页或帮助页提供资格、参数和操作。新闻日期和生效日期分开记录。
2. 截图和创意素材把 T09、T15、T16、T11、T12、T10 一起使用：先确认内容真实、适龄，再核规格、预览不同设备和方向，最后在 App Store Connect 管理并提交。
3. 订阅把 T24、T27、T28 与 T48、T49、T50 以及当前许可协议附件一起读。功能开放日期、资格审核、多席位默认设置和组织席位支持，可能影响商业和支持流程。
4. 订阅挽留信息先用 T54 审文案、优惠和本地化，再决定是否申请 T53 API。挽留信息是商业功能，文案仍按 App Review 的元数据规则审核。
5. Siri AI 用 T56 做 Beta 资格、地区、年龄和隐私隔离评估。公告已写明后续还会补充专门条款，不要把预览行为当作稳定政策。
6. 年龄分级要把问卷事实、内容频率、社交功能和地区要求放在一起维护。T42 是填写流程，T43 是答案含义，T41 是韩国监管来源。知识库页是[年龄分级](../age-ratings/age-ratings.zh-CN.md)。
7. 标为未读或部分的目标仍然未经完整核实。恢复可读后再补录正文，不要仅凭链接标题把它视为已核实政策。

本目录不建立 Privacy Manifest、Required Reason API、IAP、外部购买或地区条款专题。这些全文不在本次快照包中。提到付款或隐私的行，只定位该公告自己的链接。
