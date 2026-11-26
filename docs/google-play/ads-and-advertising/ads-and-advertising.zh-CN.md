---
id: google-play.ads-and-advertising
platform: google-play
language: zh-CN
authority: normative
status: current
kb_checked_at: 2026-10-23
review_due: 2027-01-23
regions: [global]
topics: [ads, app-promotion, ad-fraud, advertising-id, monetization, better-ads]
snapshot_id: play.ads-and-advertising
snapshot_package: "GooglePlay-KnowledgeBase-2026-10-24-review.zip"
coverage_status: "detailed-summary"
source_url: "https://support.google.com/googleplay/android-developer/answer/9857753?hl=en"
effective_date: "current-policy"
---

# Google Play 广告与推广

> **导入说明（Google batch 4）。** 本页正文取自 2026-10-24 Google Play 知识库快照里已经分开的中文改写（`play.ads-and-advertising`，YAML `reviewed_on` 为 2026-10-23）。它不是官方页面的逐字文本。英文官方来源是效力来源。`kb_checked_at` 使用快照源文件记录的核对日；本次导入没有重新打开线上官方页面。文中“本知识库”“本库”“本地专题”描述的是该快照知识库的覆盖范围，不是本仓库已经导入的页面清单。快照里指向尚未导入本仓库的专题、链接图、台账或 CSV 的相对链接，已改为文字提及；指向 Google batch 1–3 或本批十二个专题的相对链接已改到本仓库路径。快照 YAML 记录了 Ads、App Promotion 和 Ad Fraud 的 `hl=zh-CN` 来源地址，以及 Advertising ID 帮助页和中文稿里 Better Ads Experiences 说明页的 `hl=zh-Hans` 地址；正文复核打开的是英文 Ads 帮助页。快照没有记录主 Ads 文章的 `hl=zh-CN` 抓取失败，也没有记录已逐行核对的中文官方 Ads 页面与英文页面的差异。本中文页是快照的编辑改写，不是 Google 已发布中文页面的逐字文本。Ads 政策本身没有记录未来生效日。Coalition for Better Ads 写明采纳者最早可于 2026-05-15 将其 2026 网页标准更新视为生效；该日期是外部行业安排，不是 Google Play 截止日期或 Play 政策变更。CBA 标准、研究、短视频“前 6 秒 / 前 5 秒”的材料差异，以及 IAB 指南，都是行业资料，不替代 Play Ads 条文，也不把网页广告密度阈值移植为原生应用规则。AdMob 无效流量和账户处置是另一套变现账户体系，不等于 Play 对应用的下架或暂停。本页 Play Ads 义务是 `normative`；Android/广告 SDK 实现和外部标准是实现或行业说明。

## 来源与适用范围

本专题综合 [Ads 政策](https://support.google.com/googleplay/android-developer/answer/9857753?hl=en)、[App Promotion 政策](https://support.google.com/googleplay/android-developer/answer/9899004?hl=en)及广告欺诈、位置、Advertising ID 的直接子页。核对日期：2026-10-23。Google 将广告及其推广商品视为应用体验的一部分；应用、广告网络和联盟推广均须符合适用的 Play 政策。页面摘要不是合同或政策原文，争议时以官方现行全文为准。

## 广告体验要求

- **广告内容与年龄分级：** 广告和广告落地页/推广的其他应用必须适合本应用的内容分级；不能因为广告本身未单独违规就忽略其年龄适配。儿童受众应用还须遵守 Families 广告与变现规则。
- **清楚标示广告：** 广告不得伪装成应用界面、系统通知、警告或正常功能；用户应能识别广告由哪个应用展示。
- **不得干扰用户：** 不能强迫点击、索取广告用途的个人信息作为使用应用前提，不能在宿主应用之外展示广告或抢占系统按键/退出流程。干扰正常操作的广告须可轻易关闭，不得以虚假关闭按钮或误触布局诱导点击。
- **插屏时机和时长：** 不得在用户未预期时展示全屏插屏，尤其不能在关卡/内容刚开始时打断，或在应用 splash/loading 之前显示全屏视频广告。非用户主动选择、会打断操作的全屏插屏超过 15 秒仍不可关闭不允许；明确 opt-in 的奖励广告及不打断当前操作的插屏适用页面所述例外。
- **锁屏变现：** 除专门用途为锁屏的应用外，不得在锁定屏幕引入广告或变现功能。
- **广告欺诈：** 禁止隐藏广告、自动/非真实用户点击、伪造安装归因、应用界面外弹广告，以及向广告网络虚报包名、设备或广告库存。
- **广告与位置/设备标识：** 不得仅为广告或分析请求位置权限。若位置数据用于广告，须在显著披露/隐私政策中清楚说明并链接相关广告网络的隐私规则。AAID 仅可用于广告与用户分析；每次读取都检查退出设置。分析用途不得关联个人身份信息或持久标识符；广告用途不得关联持久标识符，与个人身份信息关联须有明确同意。重置后不得串联旧 ID 或其衍生数据（除非取得明确同意）；退出后禁止画像/个性化定向，但允许情境广告、频控、转化跟踪、报告、安全和欺诈检测。详见[AAID 专题](../advertising-id/advertising-id.zh-CN.md)。

### Better Ads Experiences：插屏的预期性

[Better Ads Experiences 说明页](https://support.google.com/googleplay/android-developer/answer/12271244?hl=en)进一步解释“意外的全屏插屏”：在用户正执行其他操作时打断，或点击本应开始某段流程的按钮后先出现广告，都可能属于意外。关卡/内容片段刚开始时通常不自然；完成关卡、章节或其他内容段落后的自然停顿更合适。若产品没有明显自然停顿，开发者应以用户体验判断安排时机；集成式或非全屏广告通常干扰较小。

用户主动选择观看并换取应用内奖励的广告，不受“意外展示”这一原则约束，但仍须符合其他 Developer Program Policies 和 Ads 政策。应用加载完成后可展示静态插屏；若应用没有 splash/loading 页面，应等主页加载后再展示。开发者对集成的第三方广告 SDK/库行为仍负责任。该说明以 [Coalition for Better Ads 的体验研究](https://www.betterads.org/)为参考，但执行时应区分 Play 正式 [Ads policy](https://support.google.com/googleplay/android-developer/answer/9857753?hl=en) 与外部 [Better Ads Standards](https://www.betterads.org/standards/)；行业标准解释用户体验，不自动取代 Play 条文。

## “含广告”商店标签

Play Console 的“含广告”问题须准确回答。广告 SDK、横幅、插屏、原生/赞助内容和 house ads 通常都属于广告；该标签面向 Play 用户。只有主菜单中独立、不干扰游戏且不嵌入玩法的“更多应用/更多游戏”等交叉推广区块，页面列明可不按该标签申报。Google 可能复核并自行显示标签；误报广告状态可能导致应用暂停。该标记不替代数据安全、付款、赞助内容或其他适用申报。

### Ad Fraud 与无效流量：执行范围不同

Play 的 [Ad Fraud 政策](https://support.google.com/googleplay/android-developer/answer/9969955?hl=en)禁止让广告网络误以为广告交互来自真实用户兴趣的行为，包括隐藏广告、自动点击、虚假安装归因、应用外弹窗和虚报应用身份。它链接的 AdMob [Invalid traffic 指引](https://support.google.com/admob/answer/3342054?hl=en)还包括意外点击、重复点击、鼓励点击、发布者点击自己的真实广告和机器人流量；发布者即使不知道第三方产生了流量，仍负责流量质量。

AdMob 是另一个广告变现/发布者账户体系：无效流量可能造成广告投放限制、账户暂停或停用，也会调整月末最终收入；这些账户处置不等同于 Play 对应用的下架/暂停。预防建议、Android/iOS 测试广告、广告版位指南、账户申诉与收入结算后代见[移动垃圾软件与广告欺诈专题](../mobile-unwanted-software/mobile-unwanted-software.zh-CN.md)。Google 的识别介绍仅说明自动过滤和人工审核，不披露账户级检测细节。

## Ads Help 正文直接链接盘点

2026-10-23 重开现行 [Ads Help 正文](https://support.google.com/googleplay/android-developer/answer/9857753?hl=en)。正文中与政策/行业标准有关的链接出现 14 次，涉及 12 个不同链接 URL；其中两个旧 Help URL 跳转到已登记的现行页面，合并后为 11 个当前目标。每个目标均在本轮打开或以已保存的全文审计复核。该页的图片示例、反馈调查、帮助社区、账号化 Contact 和帮助中心侧栏另作 UI/导航处理，不混入正文政策直链计数。

| Ads 正文直链 | 与广告规则的关系及目标状态 |
| --- | --- |
| [Store Listing and Promotion 主题索引](https://support.google.com/googleplay/android-developer/topic/9877064?hl=en) | 目标正文可读，列 App Promotion、Metadata、User Ratings、Content Ratings、News & Magazines 五个政策入口；当前还显示一个独立视频链接。该索引不是额外 Ads 条文。 |
| [App Promotion](https://support.google.com/googleplay/android-developer/answer/9899004?hl=en) | 正文可读；禁止欺骗/有害推广、强迫安装、未获知情操作的重定向、未经请求的短信推广和误导商店元数据，并由开发者对广告网络/联盟负责。其“deceptive promotion practices”链接是该政策的说明目标；更深关系见下方孙链接表。 |
| [Restricted Content 目录](https://support.google.com/googleplay/android-developer/topic/9877466) | 正文可读，列 10 个受限内容政策入口；本地儿童、金融、赌博、非法活动、UGC、健康、区块链、AI、年龄限制和不当内容专题已链接。目录下的技术/地区/表单后代仍非全部闭合。 |
| [Real-Money Gambling policy](https://support.google.com/googleplay/android-developer/answer/9877032) | Ads 正文点击本轮被 Google 验证页拦截；此目标此前已完成全文和 53 个正文目标审计。保留先前成功全文状态，并记录本次临时访问失败，不能将其解释为页面或规则变更。 |
| [Content Ratings](https://support.google.com/googleplay/android-developer/answer/9898843) | 本轮全文已打开；广告/关联优惠须适配宿主内容分级，摘要页直接链接到它。当前中英文专题已扩展至 IARC、台湾 DGSC 和德国 USK 地区机构分支。 |
| [Families Ads and Monetization Requirements](https://support.google.com/googleplay/android-developer/answer/9893335?hl=en) | 本轮全文已打开；儿童/混合受众会带来广告 SDK、个性化广告、中立年龄屏幕及数据处理要求。Families 相关子链见双语儿童安全专题。 |
| [Ad Fraud](https://support.google.com/googleplay/android-developer/answer/9969955?hl=en) | 本轮正文可读；禁止隐藏广告、自动点击、虚假安装归因、应用外广告和向广告网络虚报应用/设备/库存。其 [AdMob invalid-traffic 指引](https://support.google.com/admob/answer/3342054?hl=en) 是下一层外部变现指导，已在移动垃圾软件/广告欺诈专题审计。 |
| [Personal and Sensitive Information / User Data（旧入口）](https://support.google.com/googleplay/android-developer/answer/9888076) | 当前页面标题为 User Data，并跳转到现行 `answer/10144311`；链接别名已在来源规范化器中登记。用户数据专题覆盖披露、限制用途、SDK 责任与 AAID 规则。 |
| [Location Permissions（旧入口）](https://support.google.com/googleplay/android-developer/answer/9888170) | 旧入口跳转到现行 [Sensitive Permissions](https://support.google.com/googleplay/android-developer/answer/16558241)。广告不得单独成为申请位置权限的理由；后台位置另见[位置专题](../background-location/background-location.zh-CN.md)。 |
| [User Data policy](https://support.google.com/googleplay/android-developer/answer/10144311?hl=en) | Ads 正文另有三个用户数据链接引用（含旧/现行 URL 变体）；现行正文本轮打开。AAID、数据披露、SDK 共享和广告用途边界见[用户数据](../user-data/user-data.zh-CN.md)与[广告标识符](../advertising-id/advertising-id.zh-CN.md)。 |
| [Better Ads Standards](https://www.betterads.org/standards/) | 外部体验标准全文已打开；其 23 个示例页、研究/方法、内容环境、解释委员会、翻译及治理链接已逐项登记并在递归链接图 §4.77 摘要。该标准解释用户体验，不自动成为 Play 规则。 |
| [Coalition for Better Ads](https://www.betterads.org/) | 外部组织首页可读；本轮继续打开联系、关于、隐私、站点地图和标准/研究/计划分支。它不增加 Google Play 义务；外部站点页眉、页脚及所有博客/归档未作全站穷举。 |

**跨层级说明：** 14 次正文引用归并到 12 个被点击的 URL；`answer/9888076` 跳至 User Data `answer/10144311`，`answer/9888170` 跳至 Sensitive Permissions `answer/16558241`。正文另有三处 User Data 交叉引用。Better Ads Standards 和 Coalition 是外部解释资料；App Promotion 下的 Deceptive Behavior 以及 Ad Fraud 下的 AdMob 无效流量是孙链接，不能误标为 Ads 正文直链。帮助中心 4 项 Monetization and Ads 侧栏、图片示例、反馈/社区/Contact 不属于上述正文政策目标；深层后代仍按下文边界标记。

## 直接子链接与关系

下表覆盖 Ads 政策正文中与规则有关的主要直接目标；帮助中心侧栏、反馈控件和示意图片不视为政策要求。已打开只表示本次可读取正文，不等于所有后代页都已关闭审计。

| 直接链接 | 与 Ads 的关系 | 核验/本地关联 |
| --- | --- | --- |
| [Understanding Google Play's Better Ads Experiences policy](https://support.google.com/googleplay/android-developer/answer/12271244?hl=en) | 以“用户是否正在进行其他事情”和场景是否自然解释全屏插屏的预期性；自愿奖励广告例外仅针对意外性原则。 | 正文已打开并按场景摘要；仍须遵守 Ads 正式政策和其他开发者政策，SDK 提供方违规不免除开发者责任。 |
| [App Promotion](https://support.google.com/googleplay/android-developer/answer/9899004) 与 [Store Listing and Promotion 目录](https://support.google.com/googleplay/android-developer/topic/9877064) | 推广不得欺骗或伤害用户；禁止强迫安装、未经同意跳转、相似系统通知、未经请求的短信推广，且开发者对广告网络/联盟负责。 | 正文已打开；素材要求见商店详情专题（快照：`store-listing-best-practices.md`，未导入本仓库），后代政策仍需逐页审计。 |
| [Deceptive Behavior](https://support.google.com/googleplay/android-developer/answer/17006354) | App Promotion 的孙链接，覆盖以广告/推广诱导、冒充或误导用户的行为。 | 目标页已打开。本仓库在 Google batch 3 已单独收录[欺骗性行为](../deceptive-behavior/deceptive-behavior.zh-CN.md)；快照撰写时尚未把该页拆成独立文件。与 Ads 中广告伪装规则交叉引用。 |
| [Restricted Content 目录](https://support.google.com/googleplay/android-developer/topic/9877466) | 将广告内容接入儿童安全、不当内容、金融、赌博、非法活动、UGC、健康、区块链、AI 和年龄限制等政策域。 | 目录已打开；其中金融、健康、区块链、儿童安全等已有本地专题，目录下其他专题仍需逐项核对。 |
| [Real-Money Gambling, Games, and Contests](https://support.google.com/googleplay/android-developer/answer/9877032) | 赌博广告只有在当地许可、年龄和受众限制、内容及落地页要求全部满足时才可能出现。 | 正文已打开并单独整理为真钱赌博专题（快照：`real-money-gambling.md`，未导入本仓库）。 |
| [Content Ratings](https://support.google.com/googleplay/android-developer/answer/9898843) | 广告及其推广的其他应用不得明显高于宿主应用内容分级。 | 正文已打开；每个新应用和活跃应用需完成 IARC 问卷，变化后更新。 |
| [Families Policies](https://support.google.com/googleplay/android-developer/answer/9893335) | 儿童或混合受众应用的广告 SDK、个性化广告和中立年龄屏幕要求。 | 正文已打开；详见[年龄限制与儿童安全](../age-restricted-child-safety/age-restricted-child-safety.zh-CN.md)。 |
| [Ad Fraud](https://support.google.com/googleplay/android-developer/answer/9969955) → [AdMob Invalid traffic](https://support.google.com/admob/answer/3342054?hl=en) | Play 禁止伪造真实用户兴趣的广告交互；AdMob 指引补充意外点击、发布者责任及账户层面的广告投放/收入处理。 | Play 正文、无效流量、预防、Google 防护、账户暂停/停用和最终收入等目标已打开并接入[移动垃圾软件与广告欺诈专题](../mobile-unwanted-software/mobile-unwanted-software.zh-CN.md)。AdMob 变现处置与 Play 应用政策处置分开。 |
| [Permissions and APIs that Access Sensitive Information](https://support.google.com/googleplay/android-developer/answer/16558241) 与 [Background location](https://support.google.com/googleplay/android-developer/answer/9799150) | 位置数据属于敏感数据；不得仅为广告/分析请求权限，后台位置另须核心功能理由、披露和审核。 | 两页已打开；详见[敏感权限](../sensitive-permissions/sensitive-permissions.zh-CN.md)、[后台位置](../background-location/background-location.zh-CN.md)与前台位置最小范围（快照：`contacts-location-permissions.md`，未导入本仓库）。 |
| [User Data policy](https://support.google.com/googleplay/android-developer/answer/10144311) | AAID、永久标识符、披露、SDK 共享及数据处理义务。 | 正文已打开并有[用户数据专题](../user-data/user-data.zh-CN.md)；广告标识符的 Android API/SDK 实现后代尚未穷尽。 |
| [Better Ads Standards: Mobile App Experiences](https://www.betterads.org/standards/) 与 [Coalition for Better Ads](https://www.betterads.org/) | Ads 政策引用的用户体验研究来源；该标准跨网页、短视频和应用环境列出体验类别。 | 23 个体验示例及标准页重要后代已分别打开/标记状态，详见下节与递归链接图 §4.77；作为外部行业资料，不替代 Play 正式执行规则。 |

## 审核与实现检查

1. 从 AAB、SDK 清单和运行时流量确认所有广告形式及库存，逐一对照“含广告”申报。
2. 在游戏开局、内容开始、应用加载、返回/退出和宿主应用外场景检查插屏、关闭按钮与误触位置。
3. 验证广告 SDK 的受众分层、年龄屏蔽、同意/退出、AAID 重置、位置数据以及隐私政策披露。
4. 检查推广素材与落地页的分级、商标授权、真实用户操作和联盟方行为；对受监管的赌博广告另查市场许可与 Play 审批。

## 相关专题

- [用户数据](../user-data/user-data.zh-CN.md) · [敏感权限](../sensitive-permissions/sensitive-permissions.zh-CN.md) · [儿童安全](../age-restricted-child-safety/age-restricted-child-safety.zh-CN.md)
- 商店详情与素材（快照：`store-listing-best-practices.md`，未导入本仓库） · 真钱赌博（快照：`real-money-gambling.md`，未导入本仓库） · [付款与订阅](../payments/payments-and-subscriptions.zh-CN.md)

## Better Ads Standards 后代：示例、研究、期限与治理

### 规则层级

Google Play 的 [Ads 正式政策](https://support.google.com/googleplay/android-developer/answer/9857753?hl=en)是应用分发政策；[Better Ads Experiences 说明页](https://support.google.com/googleplay/android-developer/answer/12271244?hl=zh-Hans)解释“意外全屏插屏”的场景并给出自然停顿、奖励广告和加载完成后的静态插屏示例。Coalition for Better Ads（CBA）的 [Better Ads Standards](https://www.betterads.org/standards/)是以消费者研究形成的外部行业标准。Play 说明称其标准“受 CBA 启发”，不等于把 CBA 的每个网页/视频判定整体并入 Play。若某个体验未列入 CBA 的特定环境标准，也不能据此推断符合 Play；反之，CBA 的网页广告密度阈值也不是原生 Android 应用广告的 Play 限值。

Play Ads 正文另有独立且可执行的要求：广告与优惠均属于应用；广告不得伪装成系统/应用界面、强迫点击或打断系统操作；打断正常使用时须易于关闭；意外全屏插屏不得在关卡/内容片段刚开始时出现，视频不得早于 splash/loading；非自愿、打断操作的全屏插屏 15 秒后仍不可关闭不允许。显式选择的奖励广告及不打断当前操作的情形，只按正式条文中的相应范围理解，不能外推成全面豁免。

### CBA 的 23 个示例页

CBA 标准入口列出 6 个桌面网页、10 个移动网页、3 个短视频和 4 个移动应用示例。23 个目标都已打开并逐 URL 记录。下列网页密度/黏附广告阈值只在 CBA 标准的相应网页环境内解释，不移植为 Play 应用政策阈值。

| 标准环境 | 示例页（均为 CBA 外部标准） | 本库归纳 |
| --- | --- | --- |
| 桌面网页（6） | [弹窗](https://www.betterads.org/desktop-pop-up-ad/) · [自动播放且带声音的视频](https://www.betterads.org/desktop-auto-playing-video-ad-with-sound/) · [带倒计时的前贴片](https://www.betterads.org/desktop-prestitial-ad-with-countdown/) · [大型黏附广告](https://www.betterads.org/desktop-large-sticky-ad/) · [广告密度超过 50%](https://www.betterads.org/desktop-ad-density-over-50-percent) · [广告密度超过 30% 且伴随黏附视频](https://www.betterads.org/desktop-ad-density-above-30-percent-sticky-video) | 这些是 CBA 网页体验类别；密度按其内容环境和测量方法理解，不是 Play 原生应用的广告占屏比例规则。 |
| 移动网页（10） | [弹窗](https://www.betterads.org/mobile-pop-up-ad/) · [前贴片](https://www.betterads.org/mobile-prestitial-ad/) · [广告密度超过 30%](https://www.betterads.org/mobile-ad-density-higher-than-30/) · [闪烁动画](https://www.betterads.org/mobile-flashing-animated-ad/) · [自动播放且带声音的视频](https://www.betterads.org/mobile-auto-playing-video-ad-with-sound/) · [带倒计时的后贴片](https://www.betterads.org/mobile-postitial-ad-with-countdown/) · [全屏滚动覆盖广告](https://www.betterads.org/mobile-full-screen-scrollover-ad/) · [大型黏附广告](https://www.betterads.org/mobile-large-sticky-ad/) · [黏附弹出视频](https://www.betterads.org/mobile-sticky-pop-out-video-ads) · [黏附视频与大型内嵌广告](https://www.betterads.org/mobile-sticky-video-large-inline-ad) | 与桌面网页标准一样，适用环境是移动网页；广告密度不应被误当成 Android 应用政策的通用阈值。 |
| 短视频（3） | [不可跳过的长前贴片](https://www.betterads.org/short-form-video-long-preroll) · [中插广告](https://www.betterads.org/short-form-video-midroll) · [大型展示广告](https://www.betterads.org/short-form-video-large-display) | CBA 2020 正式公告将短视频定义为不超过 8 分钟；低于其标准的形式包括中插、超过 31 秒且前 6 秒不能跳过的前贴片，以及位于视频中间三分之一或超过视频画面 20% 的非线性广告。此为 CBA 短视频标准，非 Play 视频/应用政策的替代文本。 |
| 移动应用（4） | [打断式插屏](https://www.betterads.org/mobile-app-interruptive-interstitials) · [打断式视频插屏](https://www.betterads.org/mobile-app-interruptive-video-interstitials) · [不可跳过的打断式视频插屏](https://www.betterads.org/mobile-app-non-skippable-video-interruptive-interstitials) · [打开应用时的视频插屏](https://www.betterads.org/mobile-app-video-interstitial-opening-app) | CBA 将“关卡/内容开始时意外出现”的插屏/视频视为破坏体验；其视频示例页称结尾或成绩屏后未低于该 CBA 标准。Play 仍单独禁止 splash/loading 前的全屏视频，并适用 Play 自身的时长、可关闭性和其他规则。 |

短视频的历史材料有一处不一致：2020 年 CBA 新闻稿及现行示例页的描述为前 6 秒内不可跳过；CBA 2020 年 8 月博客曾写“前 5 秒”。本库按新闻稿/当前标准页记录 6 秒，同时保留博客冲突，不把任一数值表述为 Play 规则。

### 研究与解释材料

- [CBA 研究方法页](https://www.betterads.org/research/)说明其以消费者评分/排序、烦扰与分心度等数据识别低接受度体验；其网页研究覆盖超过 66,000 名消费者、代表全球约 70% 的在线广告支出市场。标准页另称累计 150,000 多人参与不同环境研究，两者是不同页面/统计口径，不合并为单一可比数字。
- 研究页列出六项论文入口：[消费者在线广告体验实验方法](https://www.betterads.org/research/perceptionpaper/)、[按消费者感知排序 N 种广告体验](https://www.betterads.org/research/rankingpaper/)、[依据用户体验数据确定标准](https://www.betterads.org/research/standardpaper/)、[短视频广告感知实验方法](https://www.betterads.org/research/ad-perception-short-form-video)、[应用内广告感知实验方法](https://www.betterads.org/research/mobile-app-ads)、[2025 网页环境消费者广告感知复核](https://www.betterads.org/research/consumer-perceptions-web)。六个目标页均已打开并记录为研究论文入口/元数据页；工具提取到的正文不足以核验 PDF 全文，不把它们标作全文已读。
- [标准内容环境 PDF](https://www.betterads.org/hubfs/Better-Ads-Standards-Content-Environments-11-10-2021.pdf)、[解释委员会决定 PDF](https://www.betterads.org/hubfs/Better_Ads_August2018/PDF/Interpretation%20Panel%20Decisions.pdf)及 [2017 弹窗解释建议 PDF](https://www.betterads.org/hubfs/4231068/Better_Ads_August2018/PDF/CBA-Interpretative-Advisory-9-15-17-3.pdf)均已打开。它们用于理解 CBA 的研究场景/历史解释；不构成 Play 的例外或授权。
- [2026 网页标准更新公告](https://www.betterads.org/blog/cba-updates-desktop-mobile-web-standards)称，在 55,000 多名受访者研究后，新增桌面网页广告密度 >50%、桌面网页 >30% 与黏附视频组合，以及两种移动网页黏附视频形式；CBA 至少设置四个月行业调整期，并称采纳者最早可于 2026-05-15 将其视为生效。该日期是 CBA 更新安排，不是 Google Play 截止日期或 Play 合规变更。
- [标准翻译页](https://www.betterads.org/translated-better-ads-standards)仅列出韩文文件；链接 PDF 本次返回 Cache miss。标准页提示翻译措辞有歧义时以英文版为准。

### 最佳实践、计划与外部治理

- CBA [移动应用标准发布公告](https://www.betterads.org/press-releases/cba-new-standard-mobile-apps)称其移动应用标准于 2022 年发布、应用 CBA Experience Program 的日期不早于 2022-03-02；[短视频公告](https://www.betterads.org/press-releases/cba-announces-better-ads-standard-short-form-video)写明相关计划适用不早于 2020-06-05。二者是 CBA 自愿行业计划时间，不是 Google Play 政策期限。
- CBA [2023 年回顾](https://www.betterads.org/blog/2023-year-review)曾计划于 2024 年发布如何沟通标准、hard/soft walls、用户消息与项目标识的最佳实践文件。本轮复查当前网站与站点地图未找到该文件；只能记为“未定位到”，不推断其从未发布。
- CBA [Better Ads Experience Program](https://www.betterads.org/program/)和 [2018 项目框架 PDF](https://www.betterads.org/hubfs/Better_Ads_August2018/PDF/Framework%20for%20a%20Better%20Ads%20Experience%20Program%20%28October%202018%29.pdf)描述自愿参与、注册和评估；[注册目录](https://www.betterads.org/registry/)的发布者登记 iframe 本次 Cache miss。该项目面向参与者/出版商，不是 Play 开发者必须加入的项目。
- [争议解决页](https://www.betterads.org/dispute-resolution/)和 [2020 年争议解决程序 PDF](https://www.betterads.org/hubfs/Better_Ads_August2018/PDF/Better-Ads-Experience-Program-Dispute-Resolution-Mechanism-Procedures-July-2018.pdf)说明参与项目后的复核流程、整改/时限与争议机制；这是 CBA 计划历史程序，不是 Play 申诉规则。
- [IAB Europe 2022 应用内广告指南](https://iabeurope.eu/wp-content/uploads/2022/02/IAB-Europe-Guide-to-In-app-advertising.pptx.pdf)和 [2023 游戏内广告指南](https://iabeurope.eu/wp-content/uploads/IAB-Europe-Guide-to-In-Gaming-April-2023-1.pdf)提供广告格式、测量、隐私及买方实践背景；内容属行业资料且有版本时效，不能覆盖 Play 的禁止性条款。旧指南提到的 Splash Ads 不构成 Play 对 splash 前全屏视频广告的许可。
- CBA [联系](https://www.betterads.org/contact/)、[关于](https://www.betterads.org/about/)、[隐私](https://www.betterads.org/privacy/)和[站点地图](https://www.betterads.org/sitemap/)页面已打开；它们是组织/网站治理信息。广告发布者政策 [Google Publisher Policies](https://support.google.com/publisherpolicies/answer/11127848?hl=en)是另一套产品规则：它规定 Google-served ads 的发布者/页面要求，不应与 Play 应用审核规则混为一谈；其术语目录被反机器人限制。

逐 URL 的打开、部分读取、缓存/登录/防机器人限制见来源审计表（快照：`../source-page-audit.csv`，未导入本仓库），链路关系与未闭合后代见递归链接图 §4.77（快照：`../google-play-policy-link-graph.md`，未导入本仓库）。CBA 站点其他博客、页眉页脚、注册者资料、搜索结果和第三方站点的全部导航仍不属于已穷尽范围。
