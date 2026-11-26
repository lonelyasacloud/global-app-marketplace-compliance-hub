---
id: apple.news.rss-index
platform: apple
language: zh-CN
authority: operational
status: partial
kb_checked_at: 2026-11-09
review_due: 2027-02-09
snapshot_package: 2026-11-10
regions: [global]
topics: [news, change-history, deadlines, review]
editorial_note: "Operational and historical news index, not an Apple policy rule. Checked 2026-11-09 (package 2026-11-10). RSS XML was not parsed; the feed boundary is unverified. This import did not re-open live news pages. English guidelines in the snapshot are dated 2026-10-16; the Simplified Chinese official guidelines page shows 2026-06-08. Chinese summaries of English-only notices are editorial summaries."
---

# Apple Developer News 索引 / Apple Developer News Index

## 这页是什么

本页是**操作性 / 历史性索引**，不是审核规则。公告不能覆盖当前英文指南、现行协议或 App Store Connect 里的实际状态。P3 是背景，H 只用于追溯。

知识库核查日为 2026-11-09（包日期 2026-11-10）。本次导入没有重新打开实时新闻页。

来源页：

- [英文新闻列表](https://developer.apple.com/news/)
- [简体中文最新动态](https://developer.apple.com/cn/news/)
- [英文 RSS](https://developer.apple.com/news/rss/news.rss)
- [简体中文 RSS](https://developer.apple.com/cn/news/rss/news.rss)

## 采集状态

用户提供的两个 RSS 地址通过网页读取器打开时返回 `application/rss+xml`，读取器不支持该内容类型。当时的运行环境也不能直接下载并解析 Apple 域名上的 XML。因此本索引依据 Apple 官方英文和简体中文新闻列表，并打开了本轮纳入的近期公告。

英文列表和中文列表的最新可见日期与条目不完全一致。下表是双语页面的合并工作集，**不是 RSS XML 的逐项镜像**。XML 条目数、截断边界、完整 `pubDate` 和未展开的旧条目都还没有直接验证。状态为 `partial`。

表中是本轮从页面快照里选取并打开的 2026 年近期条目，包括只出现在英文页的公告，以及两种语言都有的公告。若以后有 XML 导出，应按文章 ID 补齐并校验。不含网站导航、分享按钮或图片 CDN。

每篇公告的正文直链、目标页、关系和访问状态见[新闻目标页分析](news-link-targets.zh-CN.md)。

只在英文 URL 上出现的公告，表中的中文摘要是该英文公告的**编辑摘要**，不是 Apple 已发布的中文新闻正文。两种语言都有 URL 时，中文摘要按快照所记的中文公告。

英文《App 审核指南》在快照中的日期是 2026-10-16。简体中文官方指南仍显示 2026-06-08。翻译延迟不表示政策不适用。见[审核指南摘要](../app-review-guidelines/guidelines-summary.zh-CN.md)。

## 优先级

- **P1 — 上架 / 合规动作。** 可能影响审核规则、必填信息、提交材料、协议接受或明确的发布截止日期。先看。
- **P2 — 条件适用。** 仅当 App 使用相关功能、API、平台、地区或分发方式时处理。
- **P3 — 背景。** 新闻、活动或测试资源，没有直接新增合规义务。不纳入常规上架审查。
- **H — 历史。** 旧版政策或较早协议更新，只用于追溯。不得作为当前条款依据。

适用提示是知识库的执行说明，不是 Apple 规则。组内按日期倒序。

## P1 — 上架与合规动作

| 日期 | 优先级 | 新闻 | 摘要 | 适用提示 |
| --- | --- | --- | --- | --- |
| 2026-11-02 | P1 — 年龄分级新字段 | [Upcoming: New age rating content descriptors in App Store Connect](https://developer.apple.com/news/?id=yxkh08us) | 自 2026-11-16 起，年龄分级问卷新增“共享位置”和“约会与恋爱关系”声明。所有 App 须在 2027-01-12 前完成。包含约会与恋爱关系的 App 最低分级为 18+。巴西对共享位置要求 A16，对约会与恋爱关系要求 A18。本行只有英文公告 URL，中文是编辑摘要。 | 在下一次提交或修改年龄分级问卷时补答。现在就盘点实时位置共享、真人约会和带性或恋爱内容的虚拟伴侣。详见[年龄分级](../age-ratings/age-ratings.zh-CN.md)。 |
| 2026-10-16 | P1 — 规则更新 | [Updated App Review Guidelines are now available](https://developer.apple.com/news/?id=92th7e5i) | 更新涉及用户生成内容与 AI 内容、App Store 创意素材、隐藏功能、外部购买链接，以及人口贩卖或儿童剥削相关处置。本行只有英文公告 URL，中文是编辑摘要。 | 英文指南是当前规则基线。中文指南仍待 Apple 翻译更新。见[审核指南摘要](../app-review-guidelines/guidelines-summary.zh-CN.md)。 |
| 2026-10-16 | P1 — 执法风险 | [Strengthening App Review Guidelines against nonconsensual intimate imagery and bait-and-switch apps](https://developer.apple.com/news/?id=vvzx6cul) | 公告强调必须主动防止和移除非自愿私密影像，包括 AI 生成内容。审核通过后才启用未申报的有害功能属于 bait-and-switch。相关违规可能导致下架、移出开发者计划或禁止替代分发。本行只有英文公告 URL，中文是编辑摘要。 | 与 2026-10-16 指南更新并读。一篇说明执行风险，一篇定位正式条款。重点看指南 1.2、2.5.19 和第 5 节。 |
| 2026-10-13 | P1 — 当前协议 | [更新后的《Apple Developer Program 许可协议》现已发布](https://developer.apple.com/cn/news/?id=17mwd36z) · [English](https://developer.apple.com/news/?id=17mwd36z) | 修订了 Apple 软件和服务的安全要求、Live Assistance API、App Replacement Entitlement、CarPlay 与 Apple HomeView 小组件、订阅多席位购买，以及税务数据的报告和使用范围。 | 计划管理员应检查并接受新条款。使用相关 API、CarPlay、小组件或机构订阅的团队应逐项核对。协议摘要见[许可协议](../developer-program/license-agreement.zh-CN.md)。快照中的 `/cn/` 协议页在 2026-11-09 显示英文正文。 |
| 2026-10-05 | P1 — 提交要求 | [为 iPhone Duo 准备并提交你的 App](https://developer.apple.com/cn/news/?id=kkphp5qo) · [English](https://developer.apple.com/news/?id=kkphp5qo) | 使用 Xcode 27.1 重新构建并检查设备姿态和方向。更新产品页素材。可提前提交优化版截图。从 2027 年 4 月起，提交的 App 和游戏需包含 iPhone Duo 截图。 | 影响提交包、截图资产和兼容性测试计划。把素材迁移安排在 2027-04 之前。 |
| 2026-10-05 | P1 — 素材政策 | [借助 App Store 上的全新素材展示你的 App](https://developer.apple.com/cn/news/?id=ljpl7kyn) · [English](https://developer.apple.com/news/?id=ljpl7kyn) | App Store 新增产品页顶部和搜索结果创意素材。可用 App Store Connect 素材库统一管理，并在提交前预览不同设备、方向和深色模式。 | 创意素材须与 App 内容、品牌和功能保持准确一致，并遵守指南 2.3.14。 |
| 2026-09-09 | P1 — SDK 截止日期 | [App Store 现已接受适用于最新版操作系统的 App 和游戏提交](https://developer.apple.com/cn/news/?id=k1mtkt1k) · [English](https://developer.apple.com/news/?id=k1mtkt1k) | 可以提交针对 iOS 27 等新系统的 App。自 2027 年 4 月起，iOS、iPadOS、tvOS、visionOS 和 watchOS 提交需分别使用 27 系列 SDK 或更新版本。 | 把 SDK 最低版本列入发布流水线门禁，并同步升级 CI 和 Xcode。 |
| 2026-07-09 | P1 — 年龄问卷 | [年龄分级调查问卷现在包含社交媒体问题](https://developer.apple.com/cn/news/?id=tlur8uvi) · [English](https://developer.apple.com/news/?id=tlur8uvi) | 年龄问卷新增社交媒体功能问题。是否属于社交媒体，按对 UGC 的发现、传播和互动能力判断，而不是按 App 类别。未满 13 岁禁用社交功能，会影响该年龄段的“时间额度”分类。 | 自 2026 年 9 月起，提交新 App、更新或替代分发公证时需要回答。见[年龄分级](../age-ratings/age-ratings.zh-CN.md)。 |

## P2 — 条件适用

| 日期 | 优先级 | 新闻 | 摘要 | 适用提示 |
| --- | --- | --- | --- | --- |
| 2026-11-04 | P2 — 订阅挽留信息 | [Now available: Retention messages for subscriptions](https://developer.apple.com/news/?id=fk9ps3gv) | 自动续期订阅可在取消流程中显示挽留信息，包括文案、图片和挽留优惠。App Store Connect 可按订阅者资格和等待时间配置。Retention Messaging API 需申请访问。本行只有英文公告 URL，中文是编辑摘要。 | 只在提供自动续期订阅并启用挽留信息时适用。文案必须准确、相关、不令人反感，不得写具体价格或折扣，不得作强迫性或无法验证的结果声称，并且需要提交审核。 |
| 2026-11-03 | P2 — Siri AI 预览 | [Siri AI is now open to all developers](https://developer.apple.com/news/?id=gdk2umrf) | iOS、iPadOS、macOS 和 visionOS 27.3 Beta 开放 Siri AI Developer Preview。App 可通过 App Intents 和 skills 接入。当前不适用于欧盟的 iOS、iPadOS 和 watchOS，也不面向 13 岁以下用户。条款和使用政策仍待后续发布。本行只有英文公告 URL，中文是编辑摘要。 | 这是条件性平台能力，不是当前普遍上架要求。若接入，先按 Beta、地区、年龄、Apple Intelligence 条款和隐私披露做隔离测试。 |
| 2026-10-29 | P2 — 台湾店面费率 | [Adjustments to the Taiwan storefront of the App Store on iOS and iPadOS](https://developer.apple.com/news/?id=w9mxlhek) | 台湾 iOS/iPadOS 店面的标准 App 内购买和付费 App 交易佣金，自 2026-10-31 由 30% 调整为 26%。配套协议已修订。在该日期前签署新条款，不是获得该费率的前置条件。本行只有英文公告 URL，中文是编辑摘要。地区敏感。 | 只影响台湾店面。复核收入预测、税务和结算，以及账户里的协议状态。 |
| 2026-10-22 | P2 — 企业 / 学校订阅 | [Offer your subscriptions to businesses and schools](https://developer.apple.com/news/?id=yfo21au) | 组织和教育机构可通过 Apple 商务和 Apple 校园教务管理批量购买自动续期订阅。多席位购买在 App Store Connect 默认启用，可调整店面可用性。2026 年 11 月起可在沙盒测试群组购买。本行只有英文公告 URL，中文是编辑摘要。 | 若提供订阅，确认席位分配、增减席位、组织购买和支持流程。不提供此模式时，可关闭对应可用性。 |
| 2026-10-02 | P2 — macOS 隐私 | [macOS 中完全磁盘访问权限的更新](https://developer.apple.com/cn/news/?id=p6zjojqw) · [English](https://developer.apple.com/news/?id=p6zjojqw) | 完全磁盘访问权限可能暴露文件、邮件、信息和浏览记录。Apple 将增加更明确的授权控制，以降低高权限与自主 AI 智能体带来的隐私风险。 | Mac App 应解释权限用途、尽量缩小访问范围，并在用户明确知情后再取得授权。 |
| 2026-10-01 | P2 — Mac 证书 | [Upcoming expiration of Developer ID Certification Authority (Sub-CA)](https://developer.apple.com/news/?id=w4atic4c) | 旧 Developer ID Sub-CA 将于 2027-02-01 到期。受影响证书签名的 `.pkg` 之后将无法安装。已签名并带安全时间戳的 Mac App 继续可用。后续版本应改用 G2 证书重新签名。本行只有英文公告 URL，中文是编辑摘要。 | 检查证书颁发机构、签发时间和安装包。在截止日期前更新证书和签名流程。 |
| 2026-09-18 | P2 — 设备专项 | [使用新资源为 iPhone Duo 构建](https://developer.apple.com/cn/news/?id=nyuppv9r) · [English](https://developer.apple.com/news/?id=nyuppv9r) | 发布配合 iPhone Duo 的 Xcode 27.1 Beta，以及相关设计与测试资源。 | 设备适配和提交素材的准备信息。 |
| 2026-09-16 | P2 — 订阅功能 | [让你的订阅为 iOS 27 做好准备](https://developer.apple.com/cn/news/?id=likeohx4) · [English](https://developer.apple.com/news/?id=likeohx4) | StoreKit 2 支持新的 Bundles、Suites 和多席位订阅购买。组织可经 Apple Business 和 Apple School Manager 批量购买。个人也可在一次购买中邀请多人共享席位。 | 检查订阅结构、席位分配、邀请和退出，以及客户支持流程。按协议附件和 App Store Connect 资格要求申请。 |
| 2026-09-16 | P2 — 欧盟适用 | [App Tracking Transparency 在欧盟地区的更新](https://developer.apple.com/cn/news/?id=idsft9ai) · [English](https://developer.apple.com/news/?id=idsft9ai) | 自 iOS/iPadOS 27.2 起，欧盟开发者可使用替代版 ATT 系统提示。必须取得跟踪许可的规则不变。在德国、法国、意大利、波兰和罗马尼亚发行的 App 只能使用替代提示。快照记录：中文文章 URL 在目标页分析中曾返回 Internal Error，已改读英文正文。地区敏感。 | 把地区、系统版本和提示样式分别纳入隐私测试。公告直链的页面是[用户隐私与数据使用](https://developer.apple.com/cn/app-store/user-privacy-and-data-use/)。 |
| 2026-09-09 | P2 — 设备专项 | [为 iPhone Duo 做好准备](https://developer.apple.com/cn/news/?id=vn8abkxx) · [English](https://developer.apple.com/news/?id=vn8abkxx) | 提供 iPhone Duo 视频、实验室和论坛问答入口。 | 开发者支持资源。 |
| 2026-09-01 | P2 — macOS 迁移 | [对基于 Intel 的 macOS App 的 Rosetta 支持即将发生变化](https://developer.apple.com/cn/news/?id=w5ngl9k2) · [English](https://developer.apple.com/news/?id=w5ngl9k2) | macOS 27 是支持 Rosetta 的最后一个系统版本。此后，Apple 芯片设备将不再运行仅含 Intel 架构的 App。已停止维护的部分旧游戏有例外。 | 将 Mac App 改为 Universal 或 Apple silicon 原生构建，并按用户设备分布安排迁移沟通。 |
| 2026-08-27 | P2 — 店面价格与税务 | [App、App 内购买项目及订阅的税务和价格信息更新](https://developer.apple.com/cn/news/?id=artln8br) · [English](https://developer.apple.com/news/?id=artln8br) | 因税法和汇率变化，摩洛哥、刚果共和国、坦桑尼亚等市场的税务或价格发生更新。自动续期订阅和手动管理价格的处理方式不同。 | 在 App Store Connect 检查基准国家或地区、税务责任和价格变动。不要假定所有商品都会自动调价。 |
| 2026-08-24 | P2 — 使用“通过 Apple 登录”时 | [更新：“通过 Apple 登录”的新域名](https://developer.apple.com/cn/news/?id=1ptvdtcm) · [English](https://developer.apple.com/news/?id=1ptvdtcm) | 新建的“通过 Apple 登录”私密中继地址将使用 `private.icloud.com`。现有 `privaterelay.appleid.com` 地址继续有效。iCloud+“隐藏邮件地址”仍使用 `icloud.com`。 | 更新邮箱域名白名单、验证和账户恢复逻辑，避免域名校验拒绝用户。 |
| 2026-08-18 | P2 — 欧盟适用 | [适用于欧盟 App 的变更](https://developer.apple.com/cn/news/?id=gmws0jgp) · [English](https://developer.apple.com/news/?id=gmws0jgp) | 欧盟开发者业务条款整合为一套。替代分发的数字交易引入 5% 核心技术佣金，并取消初始用户获取费和商店服务费。地区敏感。 | 按分发渠道和支付路径评估条款。以最新协议附件和区域规则为准。 |
| 2026-08-12 | P2 — 韩国适用 | [韩国的年龄分级更新](https://developer.apple.com/cn/news/?id=oj3r9pvw) · [English](https://developer.apple.com/news/?id=oj3r9pvw) | 在韩国发行的游戏和娱乐类 App，可在后续版本提交时提供 GRAC 分类编号，以申请覆盖 App Store 的地区年龄分级。地区敏感。 | 年龄分级问卷和监管编号必须准确。只适用于相应类别和韩国店面。 |
| 2026-08-05 | P2 — 素材规划 | [为 App Store 上的全新创意素材资源做好准备](https://developer.apple.com/cn/news/?id=kug6m2ea) · [English](https://developer.apple.com/news/?id=kug6m2ea) | 介绍产品页标题、搜索结果和 App 内活动等新素材位置，并链接素材最佳做法与设计模板。 | 与 10 月 5 日素材公告配套。8 月公告用于预告和规划，10 月公告补充资产管理、预览和规格。 |

## P3 — 背景

| 日期 | 优先级 | 新闻 | 摘要 | 适用提示 |
| --- | --- | --- | --- | --- |
| 2026-11-03 | P3 — Beta 资源 | [使用最新 Beta 版本，做好充足准备](https://developer.apple.com/cn/news/?id=6gpufove) · [English](https://developer.apple.com/news/?id=6gpufove) | iOS、iPadOS、macOS、tvOS、visionOS、watchOS 27.3 Beta 和 Xcode 27.3 已推出。 | Beta 测试资源本身不改变上架政策。只有目标 App 需要适配新系统时才纳入测试计划。 |
| 2026-10-28 | P3 — Mac 触控资源 | [Say hello to Touch on Mac](https://developer.apple.com/news/?id=i9boeiqc) | 面向 MacBook Pro 触控输入的开发者视频、Group Labs、文档和设计资源。本行只有英文公告 URL，中文是编辑摘要。 | 资源与活动公告。只有产品确实适配 Mac 触控输入时才查看。不构成单独的 App Review 义务。 |
| 2026-10-06 | P3 — 月度通讯 | [开发者你好：2026 年 10 月](https://developer.apple.com/cn/news/?id=gv788oj6) · [English](https://developer.apple.com/news/?id=gv788oj6) | 月度通讯汇总 iPhone Duo 提交建议、小组实验室、开发者活动、本地化文档和 App Store 创意素材。 | 信息型通讯。需要时再进入对应专题。 |
| 2026-09-16 | P3 — Beta 资源 | [使用最新 Beta 版本，做好充足准备](https://developer.apple.com/cn/news/?id=rfb1rooi) · [English](https://developer.apple.com/news/?id=rfb1rooi) | iOS、iPadOS、macOS、tvOS、visionOS、watchOS 27.2 Beta 已推出，用 Xcode 27.2 构建测试。文章另说明 iPhone Duo 将运行 iOS 27.1。 | 用真实 Beta 设备和 TestFlight 做回归。Beta 行为不代替正式系统验证。 |
| 2026-08-26 | P3 — 活动信息 | [亮新篇，来耀眼](https://developer.apple.com/cn/news/?id=s6spdug0) · [English](https://developer.apple.com/news/?id=s6spdug0) | 宣布 9 月 9 日 Apple 特别活动及观看入口。 | 信息型公告，不产生上架政策要求。正文中的 Apple 官网链接，以及没有做成链接的观看方式，见目标页分析。 |

## H — 历史版本

| 日期 | 优先级 | 新闻 | 摘要 | 适用提示 |
| --- | --- | --- | --- | --- |
| 2026-08-18 | H — 较早协议修订 | [更新后的《Apple Developer Program 许可协议》现已发布](https://developer.apple.com/cn/news/?id=0cgo95n6) · [English](https://developer.apple.com/news/?id=0cgo95n6) | 新增附件 14，规定欧盟替代分发、替代付款方式和业务条款。公告称自 2026-10-01 生效。 | 只用于修订时间线。当前条款以实时协议和之后的修订公告为准。 |

## 怎么读这些更新

1. 先分开新闻日期和实际生效日期。公告日期不一定是规则生效日期。
2. 付款，以及欧盟、中国大陆、韩国等地区规则，要同时读当前许可协议、相应附件和 App Store Connect 帮助页。
3. Xcode、SDK、截图和设备支持要求，分别建立构建、测试和产品页素材的发布门禁。
4. 隐私和权限新闻要审查是否真的需要该权限、用户如何理解并授权，以及授权后数据如何使用。
5. 以后的 RSS 更新按文章 ID 去重，并分开保留英文和中文的发布或更新日期。

2026-07-09 的年龄分级公告也作为 2026-09-09 提交公告的关联目标，写在目标页分析里。它不代替、也不界定 RSS 的条目边界。
