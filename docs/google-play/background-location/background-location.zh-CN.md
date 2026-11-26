---
id: google-play.background-location
platform: google-play
language: zh-CN
authority: normative
status: current
kb_checked_at: 2026-10-23
review_due: 2027-01-23
regions: [global]
topics: [background-location, location-permission, disclosure, permissions-declaration, foreground-service]
snapshot_id: play.background-location
snapshot_package: "GooglePlay-KnowledgeBase-2026-10-24-review.zip"
coverage_status: "detailed-summary"
source_url: "https://support.google.com/googleplay/android-developer/answer/9799150?hl=en"
source_url_zh: "https://support.google.com/googleplay/android-developer/answer/9799150?hl=zh-CN"
---

# 后台位置访问与声明审核

> **导入说明（Google batch 2）。** 本页正文取自 2026-10-24 Google Play 知识库快照里已经分开的中文改写（`play.background-location`，核对日 2026-10-23），不是 Google 已发布中文页面的逐字文本。英文官方页面是效力来源。`kb_checked_at` 使用快照源文件记录的核对日；本次导入没有重新打开线上官方页面。文中“本知识库”“本库”“本地专题”描述的是该快照知识库的覆盖范围，不是本仓库已经导入的页面清单。快照里指向尚未导入本仓库的专题、链接图、台账或 CSV 的相对链接，已改为文字提及；指向 Google batch 1 或本批七个专题的相对链接已改到本仓库路径。快照记录现行英文正文已经打开。它没有把这篇主帮助页记为 `hl=zh-CN` 抓取失败，也没有记录中英文内容滞后。本中文页是快照中的结构化改写。后代路由上的抓取错误，包括一条旧 User Data URL，是正文里记录的访问限制，不是政策变更。Play 将地理围栏移出获批前台服务用例的日期是 2027-01-27，正文单独标注，不并入当前后台位置规则。本页 Play 位置规则的证据等级是 `normative`。Android 位置、前台服务和闹钟材料是 implementation note，不能单独证明 Play 分发资格。系统权限授权不等于 Play 政策批准。

**核对日期：2026-10-23。** Google Play 把设备位置视为个人和敏感数据。后台位置只适用于对用户有明显价值、且与应用核心功能直接相关的场景；需要在 Play Console 完成权限申报并通过审核。Android 系统运行时授权与 Play 审核是两层要求，拿到系统授权不代表通过 Play 政策审核。

## 先判断是否真的需要后台访问

- 核心功能必须显著展示在应用和商店页中；缺少该功能时，应用的主要用途应当受损或无法使用。后台访问还必须带来清晰、显著的用户利益，并符合用户对该功能的合理预期。
- 能以前台位置、粗略位置或 Android Location Button 完成的功能，应优先选范围更窄的方式。附近好友建议（仅在应用打开时）、本地内容个性化、区域内容限制、用户侧配送/服务状态和只在前台进行的导航，常可用前台位置完成。这些例子不自动导致拒绝；如果它们是唯一理由，则应重新设计，避免申请后台位置。
- 仅为广告或分析申请位置不允许。不得在当前功能不再需要时继续访问；不得出售位置数据，第三方 SDK 的位置访问也由应用承担合规责任。
- 面向儿童的应用须满足 Families 政策；儿童目标应用不得请求设备位置权限。混合受众还需控制儿童/未知年龄用户的数据访问和 SDK 行为。

家庭持续位置分享、儿童离开地理围栏时触发安全告警等场景可能带来更直接的安全利益，但仍须逐应用证明核心功能、用户预期、最小范围和透明披露，示例并非自动批准清单。

### Play 审核中的用户价值判断

官方审核示例把人身安全、感知安全和健康/健身列为较显著的用户利益；广告或优惠、分析、个性化、娱乐和便利通常属于较弱利益。审核还会问：该功能是否属于应用核心目的、用户是否预期后台取位、是否能用前台位置提供相同体验，以及隐私政策是否提交到 Console 并放在应用内。下面的前台替代例子不是一律拒绝后台权限；若它们是唯一理由，应优先重做功能范围：

- 只在用户使用应用时推荐附近好友或玩家；
- 只在应用打开时按位置个性化内容，且关闭应用后不触发通知或功能；
- 区域数字版权限制；
- 面向消费者的配送/服务跟踪（不包括司机侧持续跟踪）；
- 仅在应用内进行的逐向导航，不包括离开应用后被动记录路线/步数或识别开始/停止驾驶；
- 汇总位置以展示交通拥堵或附近网络速度。

逐项判断仍由 Google Play 按已声明的核心功能评估；列入示例不等于自动通过或自动拒绝。

## Console 申报与审核材料

在 Play Console 的 **App content → Sensitive app permissions → Location permissions** 完成声明。需要先处理 Console 要求的 App access 或 Authority declaration 等前置表单。申报说明应选取**一个**最能代表应用核心功能的位置功能，解释为何无法用前台/较低范围方案满足，并描述用户价值。一次申报多个后台位置功能可能导致拒绝；获批范围是整个应用的权限使用审查，不只限于该功能。

申报包至少准备：

1. **权限声明表**：说明应用主要用途、唯一选定的后台位置功能、必要性、替代方案为何不足。
2. **演示视频**：建议不超过 30 秒；展示 Android 应用中如何启动该功能、后台实际效果、显著披露和紧接其后的系统运行时授权提示。没有可见界面的功能要展示其影响/通知；提交 Android 行为，不要用 iOS 视频代替。
3. **显著应用内披露**：在常规使用流程中、位置运行时权限之前呈现；不能只放隐私政策、条款或设置菜单，也不应混在无关披露中。Play 页面说明该披露本身不必再设置一个“我同意”按钮，用户同意由随后系统权限提示承接。
4. **隐私政策和商店披露**：在应用内及商店详情页都提供隐私政策；使用有效、非 PDF、不可编辑的 URL，清楚标明为本应用/开发者的隐私政策，并具体说明位置数据的访问、收集、使用、共享对象及用途。
5. **所有轨道的核验**：审核覆盖所有有效轨道的 App Bundle/APK，包括公开、开放和封闭测试轨道。若决定不再申请，需从全部版本及相关代码中移除权限/访问，而不是只从生产包移除。

## 显著披露的必要信息

披露必须写在应用内，并在应用描述及网站等面向用户的材料中清楚展示后台位置用途。应用内披露需在正常使用路径中直接出现，说明访问/收集哪些位置数据、如何使用或共享，并包含：

- 明确出现“位置”一词；
- 明确说明应用关闭、未使用或后台时仍访问位置；
- 列出所有使用后台位置的功能；
- 若实际用途包含广告，准确说明支持广告用途，并另行遵守位置广告政策。

建议围绕官方结构自行撰写：“此应用会在应用关闭或未使用时收集位置数据，以支持【具体功能】。”这是结构提示，不是所有应用都可直接照抄的合规保证；功能和 SDK 实际行为必须一致。

## Android 系统授权与代码清查

| 检查对象 | 应核对的要点 |
| --- | --- |
| Manifest | Android 10/API 29+ 若确需后台位置，查 `ACCESS_BACKGROUND_LOCATION`；同时检查 `ACCESS_COARSE_LOCATION`、`ACCESS_FINE_LOCATION` 是否真的需要。 |
| 代码路径 | 搜索 Fused Location Provider、Geofencing API、`LocationManager` 在后台服务、`WorkManager`、`JobScheduler`、`AlarmManager`、`JobIntentService` 和 PendingIntent/桌面组件中的使用。 |
| 调度器与小组件 | 检查 [App widgets](https://developer.android.com/develop/ui/views/appwidgets)、[AlarmManager API](https://developer.android.com/reference/android/app/AlarmManager)、[Schedule alarms](https://developer.android.com/develop/background-work/services/alarms)、[JobScheduler API](https://developer.android.com/reference/android/app/job/JobScheduler) 与 [Android 12 行为变化](https://developer.android.com/about/versions/12/behavior-changes-12) 文档和代码。核对 provider/host、系统广播、周期更新、PendingIntent 及调度器触发链，确认是否间接启动定位。闹钟指南建议可延期任务用非精确闹钟，较长后台工作用 WorkManager/JobScheduler。 |
| SDK/库 | SDK 访问位置视同应用访问。检查传递依赖、广告和分析 SDK 文档及合并后 Manifest。 |
| Android 10/API 29 | 系统授权界面可提供“始终允许”选项；Play 仍要求独立的 Console 审核和披露。 |
| Android 11/API 30+ | 系统对话框不直接提供“始终允许”；用户需前往系统设置授权。请求前先解释用途、显示本地化的设置选项名称，并允许用户拒绝后继续使用不依赖该权限的功能。 |
| 精度 | 用户只同意粗略位置时，后台访问也只能获得粗略位置。应用应尽量在只授予粗略位置时仍可工作。 |
| 后台刷新 | Android 8/API 26+ 对后台位置更新有限频；Android 最佳实践页指出后台运行时可能每小时仅获得少数更新。不要把频繁轮询设计成必要政策前提。 |

Android 官方清查清单建议从 Manifest 与定位 API 入手，继续检查后台服务、任务调度器、闹钟、组件 PendingIntent 和 SDK。Google Play 也明确指出，各有效轨道均会被审核。

### AlarmManager 与后台位置是两类权限问题

`AlarmManager` 只安排何时触发操作；精确闹钟访问权不授予位置权限，也不构成 Google Play 后台位置资格或豁免。闹钟即使在应用未运行时触发，接收器/服务读取位置仍须满足相应 Android 位置授权、后台位置限制和 Play 后台位置政策。Android 对“由用户请求的精确闹钟触发操作”有前台服务后台启动限制的例外；该例外只涉及启动前台服务，不能替代位置权限或后台位置审核。Android 14+ 若该服务需要“仅在使用时”授予的位置权限，后台创建服务仍受独立限制，除非另行符合该类权限限制的例外。

精确闹钟按 Android 版本和 target SDK 选择 `SCHEDULE_EXACT_ALARM` 或 `USE_EXACT_ALARM`，其 Play 资格与申报规则另见[敏感权限专题](../sensitive-permissions/sensitive-permissions.zh-CN.md)。不得因某个定位任务由闹钟、WorkManager 或 JobScheduler 触发，就把它认定为获准后台定位。

## 前台服务是相关但不同的路径

前台服务需由应用内用户主动操作延续启动，在用户发起的目标任务完成后立即停止。对 Android 14+，还需为每个前台服务声明有效类型及对应权限并按 Play Console 要求申报。若通过前台服务实现的持续定位在行为上等同于后台位置，仍适用后台位置的核心功能、披露和审核要求；不能把权限名称或服务类型当作规避手段。Play 将于 2027-01-27 移除地理围栏作为获批 FGS 用例；Android Geofence API 的迁移、最佳实践和边界见前台服务与地理围栏专题（快照：`foreground-services-and-geofencing.md`，未导入本仓库）。

Android 17/API 37 的前台精确位置最小范围要求另见联系人与前台位置专题（快照：`contacts-location-permissions.md`，未导入本仓库）：一次性精确定位使用 Location Button；后台位置仍按本页的严格条件判断。前台服务地理围栏用例也须按 [Policy Deadlines](https://support.google.com/googleplay/android-developer/table/12921780?hl=en) 的 2027-01-27 期限检查 Geofence API 替代路径。

## 发布前核对清单

1. 对所有产品功能、Manifest、源码、合并 Manifest 和 SDK 依赖搜查后台位置访问；为每一处记录触发时机、数据精度、频率、接收方和轨道。
2. 只有能证明后台访问是核心功能所必需并显著造福用户时才保留；为可用前台、粗略位置或 Location Button 满足的场景移除宽范围权限。
3. 若申请，Console 只申报一个核心位置功能；让声明、应用内流程、商店介绍、隐私政策、视频演示和 SDK 行为彼此一致。
4. 在运行时权限前呈现显著披露；权限被拒绝时保留合理的不依赖位置功能，提供系统所需的设置引导但不误导用户。
5. 检查所有生产和测试轨道、第三方 SDK、儿童/混合受众影响，并保留申报材料及审核变更记录。

## 本页直接引用的子页

下表聚焦《Understanding location in the background permissions》正文中的政策、申报和实现目标；页内导航锚点、示意图片和帮助中心页脚不是独立政策页。目标页的摘要若已存在于专题中，直接复用并交叉链接，避免把平台实现建议误写成 Google Play 批准规则。

| 子页类别 | 本页直接引用的目标 | 与后台位置规则的关系与访问状态 |
| --- | --- | --- |
| 前台最小范围与 Android 隐私最佳实践 | [Location Permissions](https://support.google.com/googleplay/android-developer/answer/16558241?hl=en#location-permissions)、[Minimum Scope / Location Button](https://support.google.com/googleplay/android-developer/answer/17033915?hl=en)、[Minimize your use of location](https://developer.android.com/privacy-and-security/about)、[Access location in the background checklist](https://developer.android.com/develop/sensors-and-location/location/background)、[Android privacy checklist](https://developer.android.com/privacy-and-security/about) | Play 政策决定资格、披露和审核；Android 页面提供权限最小化、Manifest/SDK/任务调度清查及降级处理建议。正文已打开，见联系人与前台位置专题（快照：`contacts-location-permissions.md`，未导入本仓库）和Android 隐私清单（快照：`android-privacy-checklist.md`，未导入本仓库）。Android 最佳实践不保证 Play 审批。 |
| 声明、审查和用户披露 | [Permissions Declaration Help](https://support.google.com/googleplay/android-developer/answer/9214102?hl=en)、[Prepare your app for review](https://support.google.com/googleplay/android-developer/answer/9859455?hl=en)、[Prominent disclosure and consent](https://support.google.com/googleplay/android-developer/answer/11150561?hl=en)、[Sensitive Permissions](https://support.google.com/googleplay/android-developer/answer/16558241?hl=en)、[User Data](https://support.google.com/googleplay/android-developer/answer/10144311?hl=en) | 已有正文摘要并与本页交叉核对：一个核心位置功能、可核验视频、运行时提示前的显著披露、隐私政策及应用审核材料。父页还直接引用旧 User Data 路径 `answer/9888076` 和旧 Play Policy Center 用户数据路由；它们均指向现行 User Data 规则，旧路由按重定向状态单列。实际 Console 表单要登录；政策详情见[权限声明](../permissions-declaration/permissions-declaration.zh-CN.md)、[用户数据](../user-data/user-data.zh-CN.md)和[敏感权限](../sensitive-permissions/sensitive-permissions.zh-CN.md)。 |
| 儿童政策与培训 | [Google Play Families Policies](https://support.google.com/googleplay/android-developer/answer/9893335?hl=en)、[Families Academy 课程目录](https://playacademy.exceedlms.com/student/catalog/list?category_ids=2558)、[Declare your use of device location data](https://playacademy.exceedlms.com/student/path/64266/activity/88785) | Families 政策正文可读并已在年龄限制和儿童安全专题（快照：`age-restricted-child-safety.md`，未导入本仓库）摘要。定位课程目录显示 11 分钟课程及“最小化位置”“位置后台审核”“申报与披露”等大纲；课程登录页/后续活动返回 Cache miss，课程内容未推断。 |
| 位置实现与相邻政策 | [Build location-aware apps](https://developer.android.com/develop/sensors-and-location/location)、[Permissions on Android](https://developer.android.com/guide/topics/permissions/overview)、[Foreground Services policy](https://support.google.com/googleplay/android-developer/answer/16559646?hl=en#foreground-services)、[Ads policy](https://support.google.com/googleplay/android-developer/answer/9857753?hl=en) | Android 定位/权限页面给出系统 API、功耗和实现入口；Play 的 FGS、位置及广告条款仍是独立约束。Ads 页面还会引到儿童广告、受限内容和内容分级要求；广告与后台位置关系见广告专题（快照：`ads-and-advertising.md`，未导入本仓库）。定位与 FGS 关系见前台服务与地理围栏专题（快照：`foreground-services-and-geofencing.md`，未导入本仓库）。 |
| 移除权限与轨道修复 | Play Console 的 App content、App bundle explorer，以及[Prepare and roll out a release](https://support.google.com/googleplay/android-developer/answer/9859348?hl=en)和[Release app updates with staged rollouts](https://support.google.com/googleplay/android-developer/answer/6346149?hl=en) | Console 路由需账号登录；公开发布指南与分阶段发布帮助页均已打开并在[发布流程专题](../publishing/play-release-workflow.zh-CN.md)摘要。后台权限移除需核对所有有效轨道；分阶段发布说明发布比例并不自动递增，不能把阶段性发布当作移除旧 APK 的替代。 |
| Console 与支持流程 | [Play Console 入口](https://play.google.com/apps/publish/)、[声明表的 Console 页面](https://play.google.com/console/developers/app/app-content/permission-declarations)；App content、App bundle explorer 的具体入口在正文中呈现为账号内操作 | 正文所链接的旧 Console 首页实际跳转到 [Google Play for Business 产品页](https://google.play/business/)，不是可读取的 Console 操作页；声明表路由要求登录。App content/App bundle explorer 点击未返回可用正文或稳定目标链接；Academy for App Success、Help Community 和 Contact us 也未给出可复核的公开目标正文。 |
| 视频与代码示例 | [YouTube 短链视频](https://youtu.be/b0I1Xq_iSK4)、[同一视频的标准播放链接](https://www.youtube.com/watch?v=b0I1Xq_iSK4)、[Android 后台位置示例目录](https://github.com/android/platform-samples/tree/main/samples/location/src/main/java/com/example/platform/location/bglocationaccess) | 两个视频链接打开同一播放页，但抓取只得到 YouTube 页面壳、没有可核验字幕；示例目录可访问但 Kotlin 文件未逐个阅读。它们是辅助材料，不替代政策正文。 |

### 2026-10-23 正文链接逐项核查

现行英文正文打开为 407 行。已尝试链接引用 17–54 共 38 次（含重复链接、图片和支持控件）；正文目录引用 3–15 是本页锚点，不是独立子页；介绍视频引用 16 与正文视频引用 46 汇入同一 YouTube 视频；帮助侧栏引用 55 另行分类。10 次点击返回抓取错误：声明表跳转到登录、一个旧 User Data URL 显示了到现行 User Data 页的重定向但未能从错误页读正文，两个 Console 入口与 Academy for App Success/社区/Contact us 未提供可复核的公开正文，视频没有可读字幕，两张图片也未能作为政策文本读取。链接目标、重定向和访问边界都按下表及source-page-audit.csv（快照：`../source-page-audit.csv`，未导入本仓库）登记；错误响应不用于推断未显示的 URL。

| 正文中的旧路由或短链 | 观测到的目标 | 状态与含义 |
| --- | --- | --- |
| [Location Permissions 旧入口](https://support.google.com/googleplay/android-developer/answer/9888170) | [现行 Sensitive Permissions](https://support.google.com/googleplay/android-developer/answer/16558241?hl=en) | 已确认重定向；不能按旧 ID 当作另一份现行政策。 |
| [Prepare for review 旧入口](https://support.google.com/googleplay/android-developer/answer/9815348) | [现行 Prepare your app for review](https://support.google.com/googleplay/android-developer/answer/9859455?hl=en) | 已确认重定向；正文另有这一现行帮助页的直接引用。 |
| [User Data 旧帮助入口](https://support.google.com/googleplay/android-developer/answer/9888076)；[旧 Policy Center 路由](https://play.google.com/about/privacy-security-deception/user-data/) | [现行 User Data](https://support.google.com/googleplay/android-developer/answer/10144311?hl=en) | 两个旧入口都通向现行 User Data 规则；Policy Center 路由的重定向目标在抓取错误中显示，现行正文由另一链接独立打开。 |
| [Foreground Services Android 旧文档路由](https://developer.android.com/guide/components/foreground-services) | [现行 FGS 总览](https://developer.android.com/develop/background-work/services/fgs) | 已确认重定向；Android 启动/类型规则与 Play 的位置后台资格分别判断。 |
| [Android 后台位置清单旧路由](https://developer.android.com/training/location/background) | [现行后台位置清单](https://developer.android.com/develop/sensors-and-location/location/background) | 已确认重定向；技术清查建议不保证 Play 审批。 |
| [Android 位置总览旧路由](https://developer.android.com/training/location) | [现行位置开发总览](https://developer.android.com/develop/sensors-and-location/location) | 已确认重定向；其子页面和样例目录的深层技术后代仍有未读范围。 |
| [Android 权限总览旧路由](https://developer.android.com/training/basics/permissions) | [现行 Permissions on Android](https://developer.android.com/guide/topics/permissions/overview) | 已确认重定向；系统权限类型与 Play 的用途审核不可互相替代。 |
| [Android 隐私清单旧路由](https://developer.android.com/privacy/best-practices) | [现行 Privacy checklist](https://developer.android.com/privacy-and-security/about) | 已确认重定向；位置相关分支见下表，其他 API/PDF/视频和一般站点导航仍未全量递归。 |
| [Play Console 旧首页路由](https://play.google.com/apps/publish/) | [Google Play for Business 产品页](https://google.play/business/) | 观察到它跳转到公开营销页，不是可检查的 Console 表单；真实声明表单仍要求开发者账号登录。 |
| [YouTube 短链](https://youtu.be/b0I1Xq_iSK4) | [同一标准播放 URL](https://www.youtube.com/watch?v=b0I1Xq_iSK4) | 短链已打开并确认去向，但未取得可核验字幕或视频正文。 |

### Android Privacy checklist 的后台位置孙链接

2026-10-23 重新打开 [Android Privacy checklist](https://developer.android.com/privacy-and-security/about)，并沿其位置最小化条目打开直接链接及关键实现后代。此处只保留与位置权限范围、请求时机、拒绝处理和 Play 审查有关的页面；Android 站点导航、通用 API 成员和代码样例不是完整镜像。

| 关系路径 | 目标页面 | 与后台位置的关系 | 状态与边界 |
| --- | --- | --- | --- |
| Privacy checklist → 后台位置访问清单 | [Access location in the background](https://developer.android.com/develop/sensors-and-location/location/background) | 清查 Manifest 中的粗略/精确/后台位置权限，并搜索 Fused Location Provider、Geofencing、LocationManager 在 Service、JobIntentService、WorkManager/JobScheduler、AlarmManager、App Widget 及 SDK 中的使用。若非核心功能所需应移除后台访问；可能时改为仅应用可见时定位。 | 正文已打开；平台最佳实践不保证 Google Play 审批。 |
| Privacy checklist → 请求运行时权限 → 位置权限 | [Request runtime permissions](https://developer.android.com/training/permissions/requesting) → [Request location permissions](https://developer.android.com/develop/sensors-and-location/location/permissions) | 在用户启动具体功能时申请、每次操作前检查授权、拒绝/撤回后优雅降级；位置指南区分前台/后台与粗略/精确，单次或限定时段的会话位置应使用 Location Button。Android 17 / API 37+ 目标应用若只有会话位置功能，Play 政策另要求使用该按钮。 | 两篇正文均已打开；系统把前台服务运行期间的定位视作 Android 前台位置，但 Play 仍会按实际用途判断其是否等同后台访问。见联系人与前台位置专题（快照：`contacts-location-permissions.md`，未导入本仓库）。 |
| Privacy checklist → 应用权限最佳实践 | [App permissions best practices](https://developer.android.com/training/permissions/usage-notes) | 权限应在功能需要时请求而非启动时一次性索取；解释拒绝影响、处理设置中撤销，并审查第三方库是否引入不必要的位置权限。该页还连接 SMS/通话默认处理器规则，属相邻敏感权限分支。 | 正文已打开；更深的 API/测试链接见Android 隐私清单（快照：`android-privacy-checklist.md`，未导入本仓库），未把整棵 Android 文档树标为闭合。 |
| Privacy checklist → 附近设备替代方案 | [Companion device pairing](https://developer.android.com/develop/connectivity/bluetooth/companion-device-pairing) | Android 8 / API 26+ 的配套设备配对可代应用扫描附近蓝牙或 Wi-Fi 设备，初始配对无需 `ACCESS_FINE_LOCATION`；仍需开启 Location Services，且配对本身不提供持续扫描或连接。只在该功能确属配套设备初始配置时适用。 | 正文已打开；具体设备筛选器/API 示例未逐项复录。 |
| Privacy checklist → 启动前台服务 | [Services overview](https://developer.android.com/develop/background-work/services) | 前台服务必须显示持续通知；若工作只需在用户仍使用应用时运行，可用界面内线程；许多可调度后台任务应评估 WorkManager。该 Android 页面不决定 Play 的 FGS 类型、启动条件或位置资格。 | 正文已打开；Play 侧约束见前台服务与地理围栏迁移（快照：`foreground-services-and-geofencing.md`，未导入本仓库）。 |

**政策交叉点：** Android 指南区分系统权限模型和推荐实现；Play 规则另看核心功能、用户获益、合理预期、最小范围、显著披露、Console 申报及所有活跃发布轨道。使用前台服务或改用平台 API 都不能单独证明政策合规。后台位置短链本轮仍返回 HTTP 429；All files 短链仍为 Cache miss，二者没有按 slug 推断规范目标。

## 来源、子链接与关联

- [Google Play：Understanding location in the background permissions](https://support.google.com/googleplay/android-developer/answer/9799150?hl=en)
- [现行综合政策：Location Permissions](https://support.google.com/googleplay/android-developer/answer/16558241?hl=en#location-permissions)
- [Android：Access location in the background（代码清查清单）](https://developer.android.com/develop/sensors-and-location/location/background)
- [Android：Request background location（系统授权行为）](https://developer.android.com/develop/sensors-and-location/location/permissions/background)
  - [Android 官方后台定位示例](https://github.com/android/platform-samples/tree/main/samples/location/src/main/java/com/example/platform/location/bglocationaccess)（目录可访问，Kotlin 示例文件未逐个读取）
  - [后台位置使用检查视频](https://www.youtube.com/watch?v=xTVeFJZQ28c)（视频抓取失败，无字幕内容可核验）
- [Android：Request location permissions](https://developer.android.com/develop/sensors-and-location/location/permissions)
- [Android：Schedule alarms（闹钟的系统行为）](https://developer.android.com/develop/background-work/services/alarms) · [Android 14：Schedule exact alarms are denied by default](https://developer.android.com/about/versions/14/changes/schedule-exact-alarms)
- [Google Play：Exact Alarm Permission（现行资格与申报要求）](https://support.google.com/googleplay/android-developer/answer/16558241?hl=en#exact-alarm-permission)
- [Google Play：Foreground Services policy](https://support.google.com/googleplay/android-developer/answer/16559646?hl=en#foreground-services)
- [Google Play：Minimum Scope / Location Button](https://support.google.com/googleplay/android-developer/answer/17033915?hl=en)
- [Google Play Console（声明表需登录）](https://play.google.com/console/)
- [Policy Deadlines](https://support.google.com/googleplay/android-developer/table/12921780?hl=en)

相关知识库：[敏感权限与 API](../sensitive-permissions/sensitive-permissions.zh-CN.md)、[权限声明与审核](../permissions-declaration/permissions-declaration.zh-CN.md)、联系人和前台位置（快照：`contacts-location-permissions.md`，未导入本仓库）、[用户数据](../user-data/user-data.zh-CN.md)、年龄限制和儿童安全（快照：`age-restricted-child-safety.md`，未导入本仓库）。本页为核对后的结构化改写摘要，不是政策全文；账号专属 Console 状态和当地法律需另行确认。

### Android 定位开发总览的直链与实现边界（2026-10-23）

沿 User Data 正文指向的旧 Android 定位 URL，确认其重定向至现行[Build location-aware apps](https://developer.android.com/develop/sensors-and-location/location)总览。现行总览列出权限请求、位置更新、功耗优化、地图/地点、Android 10 定位 codelab 和六个位置样例；页面标注最后更新 2024-07-01。为使旧的 User Data 子链可继续点击，本段记录这些直接目标及可读状态；它们是 Android 实现资料，不是 Play 政策批准。

| 直接目标 | 页面关系与本轮结果 |
| --- | --- |
| [Request location permissions](https://developer.android.com/develop/sensors-and-location/location/permissions) | 页面已重开。按功能区分前台/后台、粗略/精确位置；Android 17 / API 37 及以上仅有会话级位置功能时，另有 Play Location Button 要求。代码/API 后代仍部分覆盖；当前政策适用边界见联系人与位置专题（快照：`contacts-location-permissions.md`，未导入本仓库）。 |
| [Request location updates](https://developer.android.com/develop/sensors-and-location/location/request-updates) 与 [Get the last known location](https://developer.android.com/develop/sensors-and-location/location/retrieve-current) | 两页已打开。前者解释 Fused Location Provider、请求参数、生命周期停止更新与状态恢复；后者说明 `getLastLocation()` 可能返回 `null` 或旧缓存，单次位置可评估 `getCurrentLocation()`。两者均引用大量 Play services API，成员级后代未穷尽。 |
| [About background location and battery life](https://developer.android.com/develop/sensors-and-location/location/battery) | Android 8.0 起后台位置会节流，围栏响应也会变慢；准确度、频率和延迟共同影响耗电。一般优先选满足功能的较低功耗精度、较长间隔和可接受批量延迟；API 参数只是平台优化建议，不会改变 Play 的后台位置资格。文中“Recommendations”和“Use cases”后代尚未逐页核完。 |
| [Maps and places](https://developer.android.com/develop/sensors-and-location/location/maps-and-places) | 页面介绍 Maps SDK、标记/相机/Street View 与 Places SDK。地图显示、地点搜索与读取设备位置是相关但不等同的操作；需要用户位置时，仍须按具体功能单独判断权限和 Play 政策。SDK/API 参考与服务条款后代仍待展开。 |
| [Receive location updates in Android with Kotlin](https://codelabs.developers.google.com/codelabs/while-in-use-location/) | 已阅读关键流程：以 Android 10/11、API 29/30 为示例，讲解前台位置、用户离开界面时的定位前台服务、通知、订阅/取消订阅。教程保留旧 SDK 目标和旧代码模式，不能当成当前平台版本建议或现行 Play 政策；示例仓库与代码文件未逐个审完。 |
| [Android Platform Samples 仓库](https://github.com/android/platform-samples) → [Location 模块 README](https://github.com/android/platform-samples/tree/main/samples/location) | 仓库 README 明示样例用于隔离展示特定功能，代码可能简化，不是可直接投产的代码；Location README 列出权限、当前位置、位置更新、后台访问、地理围栏和活动识别六个独立样例，并指向 Android 文档。仓库 `main` 分支可变。 |
| 六个位置样例目录：[权限](https://github.com/android/platform-samples/tree/main/samples/location/src/main/java/com/example/platform/location/permission)、[当前位置](https://github.com/android/platform-samples/tree/main/samples/location/src/main/java/com/example/platform/location/currentLocation)、[持续更新](https://github.com/android/platform-samples/tree/main/samples/location/src/main/java/com/example/platform/location/locationupdates)、[后台访问](https://github.com/android/platform-samples/tree/main/samples/location/src/main/java/com/example/platform/location/bglocationaccess)、[地理围栏](https://github.com/android/platform-samples/tree/main/samples/location/src/main/java/com/example/platform/location/geofencing)、[活动识别](https://github.com/android/platform-samples/tree/main/samples/location/src/main/java/com/example/platform/location/useractivityrecog) | 六个目录均已逐个尝试。地理围栏目录及三个 Kotlin 文件已在图谱 §4.37（快照：`../google-play-policy-link-graph.md`，未导入本仓库）分析；后台目录可见，但 Kotlin 文件未逐项读；权限、当前位置、持续更新和活动识别目录本轮只返回 GitHub 加载错误，未推断文件或代码内容。各仓库路径/访问结果见逐 URL 台账。 |

这次补的是 Android 定位总览的直接后代，不等于闭合它们的全部 API、Maps/Places 服务文档、codelab 源码、仓库 README/许可证/Issue 与 GitHub 动态树。Android 实现示例只能帮助检查实际权限流；Google Play 的核心功能必要性、最小范围、披露、申报和审核仍以现行 Play 政策正文为准。
