---
id: google-play.mobile-unwanted-software
platform: google-play
language: zh-CN
authority: normative
status: current
kb_checked_at: 2026-10-22
review_due: 2027-01-22
regions: [global]
topics: [muws, ad-fraud, hostile-downloader, social-engineering, invalid-traffic]
snapshot_id: play.mobile-unwanted-software
snapshot_package: "GooglePlay-KnowledgeBase-2026-10-24-review.zip"
coverage_status: "detailed-summary"
source_url: "https://support.google.com/googleplay/android-developer/answer/9970222?hl=en"
effective_date: "current-policy"
---

# 移动垃圾软件（MUwS）、广告欺诈与欺骗性行为

> **导入说明（Google batch 4）。** 本页正文取自 2026-10-24 Google Play 知识库快照里已经分开的中文改写（`play.mobile-unwanted-software`，核对日 2026-10-22）。它不是官方页面的逐字文本。英文官方来源是效力来源。`kb_checked_at` 使用快照源文件记录的核对日；本次导入没有重新打开线上官方页面。文中“本知识库”“本库”“本地专题”描述的是该快照知识库的覆盖范围，不是本仓库已经导入的页面清单。快照里指向尚未导入本仓库的专题、链接图、台账或 CSV 的相对链接，已改为文字提及；指向 Google batch 1–3 或本批十二个专题的相对链接已改到本仓库路径。快照写明英文 MUwS 正文已打开，中文 URL 缓存未命中，中文摘要据英文正文改写。Hostile Downloaders 的中文页未能抓取；Ad Fraud、系统功能仿冒的中文 URL 缓存未命中；Social Engineering 的中文 URL 未能访问。这些抓取失败不表示政策已经变更。本中文页是快照的编辑改写，不是 Google 已发布中文页面的逐字文本。本政策没有记录未来生效日。Android 测试广告文档标注 2026-10-20 更新，AdMob 行为政策页标注 2024-08-16，都是来源页面日期，不是新的 Play 截止日期。Play 的 MUwS 与广告欺诈规则是 `normative`。AdMob 无效流量、版位指南、测试广告和账户暂停/停用是广告变现账户体系的操作或实现说明，不等于 Play 对应用的下架或暂停。一般 Unwanted Software Policy 与 Software Principles 是背景原则，不是额外的 Play 专项程序。

**核对日期：2026-10-22。** Google Play 的 Mobile Unwanted Software（MUwS）政策把 Google 的一般不良软件原则应用到 Android/Play 生态。它覆盖应用、二进制代码、框架修改和集成 SDK；代码不必属于传统病毒，只要存在欺骗、隐蔽安装、隐瞒核心功能、不安全数据处理、意外系统影响、广告欺诈或破坏用户体验等特征，也可能触及政策。

## MUwS 的通用底线

- **兑现承诺、透明说明。** 应用应交付商店和安装流程承诺的功能；明确说明核心用途、捆绑软件、重要安装选项和系统设置变更，安装/启用由用户清楚选择并可审阅。
- **不伪造设备状态或来源。** 不得用虚假的病毒、系统故障或安全警告诱导用户操作；不得冒充其他应用/开发者/实体，也不得让广告看起来像系统通知。
- **安全处理用户数据。** 清楚披露数据访问、收集、使用和分享，限于用户合理预期且合规的功能，并采取安全措施。第三方 SDK/代码仍由应用开发者负责。
- **不破坏设备和其他应用。** 不得干扰设备正常功能、拦截/重定向网络、压制其他应用或系统的安全提示、规避 Play Protect，或在未经用户明确知情选择时削弱保护措施。
- **广告应可识别、可关闭、由真实用户意图触发。** 广告不得以意外弹窗、遮挡、虚假关闭按钮、系统通知仿冒、站外展示或其他会导致误触的方式破坏体验。
- **安装、更新和移除均应可控。** 不得暗中下载/安装额外软件、隐藏行为或捆绑组件；卸载应清晰、直接，不得以恐吓、收费或“仅隐藏”来阻止移除。

Google 的一般 [Unwanted Software Policy](https://www.google.com/about/unwanted-software-policy.html) 和 [Software Principles](https://www.google.com/about/software-principles.html) 提供背景原则；Google Play 的 MUwS 正文才是 Play 分发判断的直接来源。Android.com 的 MUwS 页面链接在本轮返回缓存未命中，未将其未读取内容推断成额外 Play 要求。

## 五项 Play 政策分支

### 1. 恶意下载程序（Hostile Downloaders）

即使下载器本身不是不良软件，只要它传播其他 MUwS，也可能违规。页面列出两类判定信号：有理由认为代码旨在传播 MUwS，并且已下载 MUwS 或包含可下载/安装应用的代码；或者其至少 **5%** 的已观察应用下载属于 MUwS，且观察样本至少为 **500 次下载**（至少 25 次 MUwS 下载）。浏览器和文件分享应用只有在不主动驱动下载、且每次软件下载均由用户同意并发起时，才适用页面列出的窄范围说明。

### 2. 广告欺诈（Ad Fraud）

不得制造看似真实用户兴趣、实为欺骗广告网络的广告交互。常见情形包括不可见/隐藏广告、自动或非人工点击、虚假安装归因、用户不在应用界面时弹出广告，以及向广告网络谎报设备类型、包名或广告库存。接入广告 SDK 不免除开发者对广告实现、实际流量和应用身份信息的责任。

### 3. 未经授权使用或仿冒系统功能

应用或广告不得模仿、干扰操作系统通知/警告。系统级通知只能用于本应用的核心功能，并应明确标示来源；不要借系统通知推广无关应用或第三方服务，也不要制作看起来像操作系统发出的警告。

### 4. 社会工程（Social Engineering）

不得假扮另一款应用，诱使用户在错误对象/上下文中执行原本打算交给可信原应用的操作。该 Help 条目只有一条简短禁止规则，没有详细案例；发布核查时可检查名称、图标、界面、通知、深层链接和关键操作流是否把用户的预期对象换成另一个应用。

### 5. 与其他 Play 政策的交叉适用

MUwS 正文直接要求遵守 [User Data](https://support.google.com/googleplay/android-developer/answer/10144311?hl=en)、[敏感权限和 API](https://support.google.com/googleplay/android-developer/answer/16558241?hl=en)、[Spyware](https://support.google.com/googleplay/android-developer/answer/14745000?hl=en) 与 [SDK Requirements](https://support.google.com/googleplay/android-developer/answer/13323374?hl=en)。广告另受 [Ads](https://support.google.com/googleplay/android-developer/answer/9857753?hl=en) 规则约束；这些对应本知识库已有的[用户数据](../user-data/user-data.zh-CN.md)、[敏感权限](../sensitive-permissions/sensitive-permissions.zh-CN.md)、[Spyware](../spyware-and-data-exfiltration/spyware-and-data-exfiltration.zh-CN.md)、第三方 SDK（[Google Play 第三方 SDK 要求与安全集成](../sdk-requirements/sdk-requirements.zh-CN.md)）和[广告专题](../ads-and-advertising/ads-and-advertising.zh-CN.md)。

## Ad Fraud：无效流量与实施最佳实践

Play 的 [Ad Fraud 政策](https://support.google.com/googleplay/android-developer/answer/9969955?hl=en)把诱使广告网络误认为广告交互来自真实用户兴趣的行为定义为广告欺诈，例子包括隐藏广告、自动/机器人点击、虚假安装归因、应用外弹窗和虚报应用身份。其链接的 AdMob [Invalid traffic](https://support.google.com/admob/answer/3342054?hl=en)同时涵盖蓄意欺诈和意外点击/展示，如发布者点击自家真实广告、重复点击、鼓励点击、诱导或误触版位、机器人流量。即使第三方在发布者不知情时产生流量，发布者仍须确保流量有效；高水平无效流量可导致限投、暂停或停用 AdMob 账户。AdMob 变现账户处置与 Play 应用分发执行是不同流程。

已打开的 [How you can prevent invalid activity](https://support.google.com/admob/answer/3342099?hl=en) 给出以下操作建议：

1. 开发和测试使用 Google 测试广告或测试设备；不要点击自己应用里的真实广告。最新版 [Android 测试广告指南](https://developers.google.com/admob/android/next-gen/test-ads)和 [iOS 测试广告指南](https://developers.google.com/admob/ios/test-ads)说明示例广告单元、测试设备、测试广告标记及 mediation 测试注意事项；Android 文档标注 2026-10-20 更新，iOS 模拟器默认是测试设备。
2. 按应用、广告单元和国家/地区切分流量报表，观察来源和用户行为变化；对高风险异常做调查。
3. 避免低质量广告网络或应用推广合作方引入无效流量。
4. 遵循 [AdMob Implementation guidance](https://support.google.com/admob/answer/2936217?hl=en)、[Banner ad guidance](https://support.google.com/admob/answer/6128877?hl=en)和[Interstitial ad guidance](https://support.google.com/admob/answer/6066980?hl=en)：选择自然过渡位置、预留稳定版位、避免广告紧邻交互控件或内容、避免诱导/误触，并按广告格式/设备正确放置。
5. Google 的 [Ad Traffic Quality Resource Center](https://www.google.com/ads/adtrafficquality/) 介绍无效流量识别与防护；它和 AdMob 实施文章属于广告生态最佳实践，不是独立的 Play Console 申报表。

测试广告和流量质量建议是帮助实现政策的操作指导。AdMob 对账户的无效流量处置、Play 对应用的政策执行属于相关但不同的流程。

### AdMob 账户处置与直接后代

AdMob 的 [Invalid traffic](https://support.google.com/admob/answer/3342054?hl=en) 正文直接链接到无效活动防护、AdMob/AdSense 发布者规则、暂停与停用账户、最终收入说明及报告表单。以下按目标页本身记录关系；这些账户资源不属于 Play 应用分发政策。正文里还出现一条名为“Encouraging accidental clicks | Google Publisher Policies”的 YouTube 链接，但浏览器未返回该目标 URL，故不凭标题猜测视频地址或内容。

| 目标页 | 摘要、关系与状态 |
| --- | --- |
| [Google 如何防范无效活动](https://support.google.com/admob/answer/3342135?hl=en) | 说明自动过滤加人工审核；不披露账户级检测细节。它解释 AdMob 变现流量审核机制，不是 Play 审核流程。 |
| [如何预防无效活动](https://support.google.com/admob/answer/3342099?hl=en) | 直接子页给出测试广告、流量来源监测、可信合作方和避免误触的操作建议；下方继续记录其 Android/iOS 测试广告、Firebase Analytics 与版位指南链接。 |
| [AdMob 行为政策](https://support.google.com/admob/answer/2753860) | 将发布者参加 AdMob 的资格、禁止自点/人工或自动虚增点击、广告版位和账户停用放在 AdSense/AdMob 发布者条款中；页面标注 2024-08-16 更新。它不是 Play Developer Program Policy。 |
| [无效活动导致账户暂停](https://support.google.com/admob/answer/6213019) | 说明暂停期供发布者排查来源、屏蔽可疑流量并修复流程；该页称此类暂停不可申诉，持续问题可能进一步限投或停用账户。 |
| [无效活动导致账户停用](https://support.google.com/admob/answer/6197403) | 页面说明可按原账户提交申诉，但不保证恢复；因无效活动被停用的发布者不得另开账户。它直链到[无效流量申诉表单](https://support.google.com/adsense/contact/appeal_form_adsense_admob)，公开表单要求发布者 ID、活跃应用/网站、流量获取方式、问题原因、整改计划和可疑流量日志等；通常 72 个工作小时内审核，流量较大时可能一周或更久，提交不保证恢复，后续申诉也可能不再受理。 |
| [预估收入与最终收入](https://support.google.com/admob/answer/6147072) | 月末最终收入会调整无效点击/展示并在适当情况下退还广告主；报告时区也可能造成小额差异。该信息仅解释 AdMob 结算，不是 Play 应用下架规则。 |
| [报告无效流量表单](https://support.google.com/admob/contact/invalid_activity) | 这是用于报告第三方疑似无效流量的独立表单，目标跳转到 Google 账号登录；表单字段无法公开读取，不推断问题或账号处理步骤。不要与上一行的账户停用申诉表单混淆。 |
| [无效流量申诉表单](https://support.google.com/adsense/contact/appeal_form_adsense_admob) | 用于对 Ad Traffic Quality 团队作出的账户停用决定提出申诉；公开可读字段包括发布者身份/ID、应用或网站、购流与推广方式、政策违规、无效流量原因、整改方案及流量日志。页面说明审核通常需 72 个工作小时，也可能超过一周；不保证恢复，已作决定后可能不再受理后续申诉。 |

### 申诉表单的进一步链接

| 目标页 | 摘要、关系与范围 |
| --- | --- |
| [Find your publisher ID](https://support.google.com/adsense/answer/105516) | 申诉表单要求的发布者 ID 可从 AdSense 账户、帮助中心账户页、Google 官方邮件或网站广告代码中查找。它是表单填写说明，不是 Play 政策。 |
| [AdSense account closed by Google for invalid traffic](https://support.google.com/adsense/answer/57153) | AdSense 通用账户处置页解释申诉、拒绝后不得重开账户，以及停用后适用情况下至少 30 天的最终付款核算期；恢复后广告投放可能还需最多 48 小时。上述付款期是 AdSense 页面说明，不自动套用于 AdMob 或 Play。 |
| [Top invalid traffic and policy violations that lead to account closure](https://support.google.com/adsense/answer/2660562) | 列出 AdSense/发布者生态常见但非穷尽的关户原因，包括自点/重复点击、机器人或购流、奖励式流量、操纵投放、误触版位和应用内错误嵌入；其中也含网站内容规则。用作变现风险参考，不能当作 Google Play 政策文本。 |

### 预防指南的直接后代

| 目标页 | 摘要、关系与状态 |
| --- | --- |
| [Android 测试广告](https://developers.google.com/admob/android/next-gen/test-ads) · [iOS 测试广告](https://developers.google.com/admob/ios/test-ads) | 开发测试阶段使用 Google 示例广告单元或设备测试模式，不点真实广告；上线前替换示例单元。Android/iOS 模拟器与真机测试配置不同；mediation 网络也需各自测试配置。这是 AdMob 账户安全操作建议，不是 Play Console 声明。 |
| [About Firebase and AdMob](https://support.google.com/admob/answer/3508177?hl=en) | 解释将应用关联 Firebase 并集成 Analytics SDK 后，AdMob 与 Analytics 可共享收入/用户指标并提供报告；是否采用取决于产品需要。该页不是政策义务。 |
| [Android Analytics SDK 路由](https://developers.google.com/analytics/devguides/collection/firebase/android/start) 与 [iOS Analytics SDK 路由](https://developers.google.com/analytics/devguides/collection/firebase/ios/start) → 当前 [Firebase Analytics 起步指南](https://firebase.google.com/docs/analytics/get-started) | 两条平台旧路由均跳转到当前统一起步页；该技术文档有大量平台/API 后代，本专题仅记录其用于流量调查的关系，不宣称技术孙链已穷尽。 |
| [Ad Traffic Quality Resource Center](https://www.google.com/ads/adtrafficquality/) | 提供广告流量质量与无效活动背景说明，不是 Play Console 申报入口。 |
| [Implementation](https://support.google.com/admob/answer/2936217?hl=en) · [Banner](https://support.google.com/admob/answer/6128877?hl=en) · [Interstitial](https://support.google.com/admob/answer/6066980?hl=en) | 预防页明确推荐这三类版位指南；专题下方另逐项登记实现帮助中心的 8 篇相关页面。指南是 AdMob 实施指导，需与 Play 应用政策区分。 |

### 广告位置指南：区分政策与实施建议

AdMob 的实现帮助中心列出 8 篇相邻指南：[Implementation](https://support.google.com/admob/answer/2936217?hl=en)、[Banner](https://support.google.com/admob/answer/6128877?hl=en)、[Discouraged banner implementations](https://support.google.com/admob/answer/6275345?hl=en&ref_topic=2936214)、[Recommended banner implementations](https://support.google.com/admob/answer/6275335?hl=en&ref_topic=2936214)、[300×250 banner](https://support.google.com/admob/answer/6293636?hl=en&ref_topic=2936214)、[Interstitial](https://support.google.com/admob/answer/6066980?hl=en)、[Disallowed interstitial implementations](https://support.google.com/admob/answer/6201362)和[Recommended interstitial implementations](https://support.google.com/admob/answer/6201350)。八篇正文现均已打开。最后补读的[推荐插页实现指南](https://support.google.com/admob/answer/6201350)建议将插页放在自然的内容/关卡间断点，最好出现在断点页面之前，避免用户点“继续”后才突然出现；对频繁点击型交互可在关卡结束与插页之间留短暂停顿，并考虑广告加载延迟与预加载。其直接 Android/iOS SDK 指引也已打开并摘要；SDK 代码示例/API 后代仍只作选择性跟进。该页是 AdMob 版位建议，不增加 Play Ads 的政策条款。

- **横幅广告：** 推荐与可交互控件/内容留出明显间隔；边框应不可点击；预留固定广告区域，避免广告加载后把原内容顶进广告区域；用自适应横幅适配屏幕尺寸。AdMob 将广告紧邻交互控件列为高误触风险；广告浮在内容上方、随内容滚动覆盖菜单等做法明确标为违反 AdMob 政策。300×250 指南还明确禁止广告仿冒或覆盖应用内容、出现在无内容的“死路”页面，或紧邻导航、聊天、图库、游戏操作和自定义关闭按钮。该指南也区分了“不推荐”与明文违规示例；前者仍可能造成无效流量或广告投放受限。
- **插页式广告：** 不得在应用启动或退出时展示插页广告；应放在内容之间的自然断点。AdMob 还要求每两次应用内用户操作最多展示一次插页，不能每次点击/滑动后展示或在用户关闭一条插页后立即再展示，也不能阻挡核心内容和导航。[应用打开广告](https://support.google.com/admob/answer/9620632)是专为启动/切回场景设计的独立格式，不能把它理解为插页式广告的通用例外；使用前仍需核对 AdMob 与 Play 的适用政策，Families 合规应用不能使用该格式。
- **技术实现：** 已打开 [Android 横幅 SDK](https://developers.google.com/admob/android/banner)、[Android 插页式 SDK](https://developers.google.com/admob/android/interstitial)和[iOS 插页式 SDK](https://developers.google.com/admob/ios/interstitial)指南；页面涉及测试广告、加载时机和格式实现。这些技术文档含有许多 SDK/API、代码示例、平台分支和导航链接；本专题不复制代码，也不宣称技术孙链接已穷尽，具体实现应按正在使用的 SDK 版本查官方文档。
- **视频与未读目标：** [Banner 最佳实践](https://www.youtube.com/watch?v=yTnqcz6RJ-4)、[Interstitial 最佳实践](https://www.youtube.com/watch?v=Ccrj8D0m1KA)、[横幅覆盖内容违规说明](https://www.youtube.com/watch?v=KsPhOYShSPw)和[插页意外弹出违规说明](https://www.youtube.com/watch?v=C5FW0lRAT3k)视频均已登记，但自动抓取失败。无效流量页中的“Encouraging accidental clicks”视频链接点击后浏览器未返回目标 URL；Android.com MUwS 页面返回缓存未命中。推荐插页实现页现已打开，不再标为受限。

## 直接链接与页面关系审计

| 父页 / 目标 | 本次核验与关系 |
| --- | --- |
| [MUwS 正文](https://support.google.com/googleplay/android-developer/answer/9970222?hl=en) | 英文全文已打开；概括透明行为、数据保护、用户体验、Play Protect、广告和 SDK 责任。中文 URL 缓存未命中，中文摘要据英文正文改写。 |
| [MUwS 帮助中心目录](https://support.google.com/googleplay/android-developer/topic/9969691?hl=en&ref_topic=9858052) | 目录页已打开，列出 MUwS、Hostile Downloaders、Ad Fraud、系统功能仿冒、Social Engineering；也链接 [官方培训视频](https://www.youtube.com/watch?v=MUhH5h8YgL4)（自动抓取失败）和 [Android.com 政策页](https://www.android.com/mobile-unwanted-software-policy/)（缓存未命中）。 |
| [Hostile Downloaders](https://support.google.com/googleplay/android-developer/answer/11189134?hl=en) | 英文全文已打开；含 5% 阈值及最小观察样本 500 的规则，以及浏览器/文件分享应用的用户发起下载条件。中文页未能抓取。 |
| [Ad Fraud](https://support.google.com/googleplay/android-developer/answer/9969955?hl=en) | 英文全文已打开；隐藏广告、自动点击、虚假安装归因、应用外弹窗、虚报包名/设备类型均有明确例子。中文 URL 缓存未命中。 |
| [Unauthorized Use or Imitation of System Functionality](https://support.google.com/googleplay/android-developer/answer/9969861?hl=en) | 英文全文已打开；限制仿冒通知/警告，允许系统通知用于应用核心功能，并建议清楚标示来源。中文 URL 缓存未命中。 |
| [Social Engineering](https://support.google.com/googleplay/android-developer/answer/10148323?hl=en) | 英文正文已打开；仅一句禁止假冒另一应用并欺骗用户执行原本想交给可信应用的操作。中文 URL 未能访问。 |
| Google [Unwanted Software Policy](https://www.google.com/about/unwanted-software-policy.html) 与 [Software Principles](https://www.google.com/about/software-principles.html) | 两页完整正文已打开，提供安装透明、易卸载、明确行为、披露数据和避免隐瞒捆绑的通用背景；其范围比 Play MUwS 广，不当作额外的 Play 专项程序。 |
| [User Data](https://support.google.com/googleplay/android-developer/answer/10144311?hl=en)、[Sensitive Permissions](https://support.google.com/googleplay/android-developer/answer/16558241?hl=en)、[Malware](https://support.google.com/googleplay/android-developer/answer/9888380?hl=en)、[Spyware](https://support.google.com/googleplay/android-developer/answer/14745000?hl=en)、[SDK Requirements](https://support.google.com/googleplay/android-developer/answer/13323374?hl=en) | 这些直接引用目标有可读正文或本地专题；旧敏感权限链接重定向到当前 `answer/16558241`。按各自专题追踪，不在此重复复制其完整正文。 |
| [Ads policy](https://support.google.com/googleplay/android-developer/answer/9857753?hl=en) | 英文全文已打开；涵盖误导/扰乱广告、广告欺诈、内容分级、Families 和位置广告等；见本地[广告专题](../ads-and-advertising/ads-and-advertising.zh-CN.md)。 |
| [Ad Fraud](https://support.google.com/googleplay/android-developer/answer/9969955?hl=en) → [Invalid traffic](https://support.google.com/admob/answer/3342054?hl=en) → [How you can prevent invalid activity](https://support.google.com/admob/answer/3342099?hl=en) | Play 政策、无效流量页和预防指引均已打开；直接后代包括测试广告、Android/iOS Analytics 路由、Firebase/AdMob 报告说明、账户处置和版位指南。8 篇格式/位置指南正文均已打开，推荐插页页已成功重试；Analytics 技术/API 深层后代仍部分。 |
| [How Google prevents invalid activity](https://support.google.com/admob/answer/3342135?hl=en) 与 [Ad Traffic Quality Resource Center](https://www.google.com/ads/adtrafficquality/) | 两页已打开。前者只概述自动过滤和人工审核机制，不披露检测细节；资源中心概述流量质量工作，不等于开发者侧申报义务。 |
| AdMob [Implementation](https://support.google.com/admob/answer/2936217?hl=en)、[Banner](https://support.google.com/admob/answer/6128877?hl=en)、[Discouraged banner](https://support.google.com/admob/answer/6275345?hl=en&ref_topic=2936214)、[Recommended banner](https://support.google.com/admob/answer/6275335?hl=en&ref_topic=2936214)、[Banner 300×250](https://support.google.com/admob/answer/6293636?hl=en&ref_topic=2936214)、[Interstitial](https://support.google.com/admob/answer/6066980?hl=en)、[Disallowed interstitial](https://support.google.com/admob/answer/6201362)、[Recommended interstitial](https://support.google.com/admob/answer/6201350) | 八篇侧栏实现指南逐项登记，八篇正文均已打开；横幅重叠和插页意外弹出视频链接已登记但抓取失败。AdMob [政策与限制](https://support.google.com/admob/answer/6128543)属于独立的广告变现规则；Android 横幅及 Android/iOS 插页 SDK 指南已打开，其代码示例和深层技术链接仍未穷尽。 |

## 发布前检查

1. 盘点应用、SDK、远程代码、下载/更新器、广告合作方和服务端是否会静默安装、捆绑或触发额外操作。
2. 对应用名称、图标、通知、系统弹窗、加载/退出流程逐项排查欺骗、假系统提示、假病毒警告及对可信应用的仿冒。
3. 核对用户数据/权限用途、披露和同意、SDK 行为与隐私/Data safety 内容；不得诱导关闭 Play Protect。
4. 检查广告是否清晰可见、位于应用内、可关闭、不会误触；所有点击和安装归因都应来自真实用户意图。
5. 测试期间使用测试广告；监控渠道、国家和广告单元流量；清理下载器及广告 SDK 的不可信来源。

**覆盖边界：** MUwS 及四个专项政策英文正文已打开；简体中文目标大多缓存未命中，故中文为据英文官方原文改写。相关数据/权限/SDK/Spyware/Ads 页面在其他专题中覆盖。无效流量分支已打开 AdMob 无效流量/预防/处置说明、Google 资源中心、Android/iOS 测试广告、Firebase/Analytics 参考、8 项广告格式帮助指南和若干 Android/iOS SDK 技术页；推荐插页帮助页现已打开。无效流量页所链意外点击视频的目标地址未被浏览器返回；另有横幅重叠、插页意外弹出及 MUwS 培训视频抓取失败。Analytics 平台文档、iOS 横幅、SDK 示例代码和第三方技术后代仍未完整递归。本页不宣称是全部后代闭包。
