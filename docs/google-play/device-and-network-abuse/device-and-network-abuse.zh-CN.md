---
id: google-play.device-and-network-abuse
platform: google-play
language: zh-CN
authority: normative
status: current
kb_checked_at: 2026-10-24
review_due: 2027-01-24
regions: [global]
topics: [device-network-abuse, executable-code, foreground-service, uidt, flag-secure, require-secure-env]
snapshot_id: play.device-network-abuse
snapshot_package: "GooglePlay-KnowledgeBase-2026-10-24-review.zip"
coverage_status: "detailed-summary"
source_url: "https://support.google.com/googleplay/android-developer/answer/16559646?hl=en"
effective_date: "current-policy; geofencing FGS preview 2027-01-27 kept separate"
---

# 设备与网络滥用、前台服务与安全环境

> **导入说明（Google batch 4）。** 本页正文取自 2026-10-24 Google Play 知识库快照里已经分开的中文改写（`play.device-network-abuse`，核对日 2026-10-24）。它不是官方页面的逐字文本。英文官方来源是效力来源。`kb_checked_at` 使用快照源文件记录的核对日；本次导入没有重新打开线上官方页面。文中“本知识库”“本库”“本地专题”描述的是该快照知识库的覆盖范围，不是本仓库已经导入的页面清单。快照里指向尚未导入本仓库的专题、链接图、台账或 CSV 的相对链接，已改为文字提及；指向 Google batch 1–3 或本批十二个专题的相对链接已改到本仓库路径。快照记录的 Device and Network Abuse 主文是英文帮助页。它没有记录已核对的中文官方 Device and Network Abuse 帮助页。本中文页是快照的编辑改写，不是 Google 已发布中文页面的逐字文本。例外是 Android Application Sandbox：快照于 2026-10-24 重开了英文和简体中文 AOSP 正文，页面标注 2026-09-30 更新。该 AOSP 页是实现背景，不自行产生 Play 资格。现行设备与网络滥用规则与未来日期分开。地理围栏前台服务用例另有 2027-01-27 的未来变更，属于快照中的前台服务专题，不是本政策的现行文本；该前台服务专题未导入本仓库。页面底部的权限政策预览是未来联系人/位置要求，日期应与当前合并政策区分；本页没有重述该预览的生效日。已导入的敏感权限与欺骗性行为专题把该预览记为 2027-01-27。FCM `AndroidConfigV2` 迁移指南标注 Preview/Pre-GA。其中 20 秒通知回调和后台 25% 抑制阈值可能在 GA 前变化，不是稳定的 Play 要求。旧 payload 链接返回 404，快照没有把它记为已验证的重定向。这些访问限制不表示 Play 政策已经变更。`REQUIRE_SECURE_ENV` 用例指南（标注 2026-03-05）写明任意 Android 版本都可使用该标志。通用 Manifest `<property>` 参考的 API 31 标注不是 Play 对此标志新增的最低版本。该标志没有技术强制拦截。设备与网络滥用、前台服务用途和不得绕过沙盒的要求是 `normative`。Doze、UIDT、FGS 类型、JobScheduler 和容器加载指南是 Android 实现说明。Manifest 声明或技术条件不等于 Play 批准。

**核对日期：2026-10-24。** Google Play 当前的 [Device and Network Abuse](https://support.google.com/googleplay/android-developer/answer/16559646?hl=en) 页面把多个主题放在同一条目中：设备/网络/API 滥用、前台服务权限、用户发起的数据传输、`FLAG_SECURE` 和设备端 Android 容器。旧入口 [answer/9888379](https://support.google.com/googleplay/android-developer/answer/9888379?hl=en) 已确认重定向到现行页。正文提示其摘要和 Key Considerations 只是概览，冲突时以完整政策正文为准。

## 核心禁止行为

政策禁止应用或其第三方 SDK 未经授权访问、干扰、中断或损坏用户设备、其他设备、服务器、网络、API、服务、设备上的其他应用、Google 服务或授权运营商网络。重点风险包括：

- 在 Play 更新机制之外自我修改、替换或更新应用；从 Play 以外下载可执行代码（如 DEX、JAR、`.so`）。政策保留虚拟机/解释器通过间接方式访问 Android API 的例外；但运行时加载的解释型代码仍不得让应用违反 Play 政策。
- 利用安全漏洞、协助黑客攻击、制作影响其他应用的游戏作弊工具，或以违反服务条款的方式使用 API/服务。
- 阻止其他应用展示广告、未经用户事先同意安装其他应用、传播或协助安装恶意软件，或在不符合条件时绕过 Android 电源管理。
- 通过代理服务向第三方提供服务，除非该代理服务本身是应用面向用户的主要核心用途。
- 在含 JavaScript Interface 的 WebView 中加载不可信网页或来源不可信的 URL；或借 `FULL_SCREEN_INTENT` 强迫用户与干扰性广告/通知互动。
- 绕过 Android 沙盒，从其他应用推断用户活动或身份。

Android 系统优化要求须结合 [Core App Quality](https://developer.android.com/docs/quality-guidelines/core-app-quality) 和系统电源管理指南理解。远程内容、解释器和 SDK 不是天然违规，但必须避免引入可执行代码、未披露行为、漏洞或其他政策违规；应用开发者仍对集成代码和 SDK 行为负责。

## 前台服务（FGS）

面向 Android 14/API 34 及更高版本的应用须为每个 FGS 声明准确的 Manifest 服务类型及匹配权限，并在 Play Console 申报实际用例。只有在服务支撑对用户有益且与核心功能相关的功能、由用户发起或持续可感知、用户能停止、无法安全延迟/中断且只运行必要时长时，才可申报相应用途。Play 页面列出 `systemExempted`、`shortService`，以及仅用于 Play Asset Delivery 功能时的 `dataSync` 例外；这不是所有同类型服务的通用豁免。

申报需说明功能、延迟/中断的用户影响和用例，并提供用户触发该功能的视频。Android 类型/权限/启动条件及 Console 审核是两层要求；Manifest 声明本身不等于 Play 批准。完整迁移说明见前台服务与地理围栏专题（快照：`foreground-services-and-geofencing.md`，未导入本仓库）。地理围栏 FGS 用例另有 2027-01-27 的未来变更，应按该专题和政策期限表（快照：`../google-play-policy-link-graph.md`，未导入本仓库）检查。

## 用户发起的数据传输（UIDT）

UIDT 是 Android 14 / API 34 起由 `JobScheduler` 提供的长时网络传输任务类型，不是 Play 的权限或合规豁免。应同时满足三个实质条件：传输由用户明确发起、任务确实通过网络上传/下载数据、用户需要看到进度且被系统延迟或中断会损害体验。自动备份/同步、非网络任务、短时且可中断工作、仅为保持进程存活的常驻任务都不应借 UIDT 获得更高优先级。Play 的 Device and Network Abuse 与 FGS 条款仍独立适用；UIDT 不豁免 Play 对应用外下载可执行代码等行为的限制。

### API 选择与实现检查

| 工作特征 | 优先考虑 | 边界 |
| --- | --- | --- |
| 可延后、短时、可中断，或由应用/系统自动发起的同步 | [WorkManager](https://developer.android.com/develop/background-work/background-tasks/persistent) | 约束、重试和跨重启持久调度更合适；需要尽快执行时再评估 expedited work。长时 worker 仍受到 FGS 和系统配额/限制。 |
| 用户点击后开始的长时网络上传/下载，进度必须持续可见，且安全中断会损害体验 | [UIDT `JobScheduler` job](https://developer.android.com/develop/background-work/background-tasks/uidt) | Android 14/API 34+；安排任务时应用须可见或满足允许的后台启动条件。该条件不等同于后台启动 FGS 豁免。 |
| 很短且关键、约三分钟内能完成的工作，且其他调度 API 不合适 | FGS 的 `shortService` 或适用的专用 API | Android 的类型/启动限制与 Play 的 FGS 用途申报、用户价值、可停止性和审核均须单独满足；不能因通知可见就默认合规。 |
| 有专门设备/业务 API 的传输 | 专用 API | 优先评估系统集成更好的专用能力，例如本地设备传输的 Companion Device 路径；不要仅因“传数据”就选通用后台任务。 |

UIDT 的关键实现核对点：

- Manifest 注册 `JobService`，由 `android.permission.BIND_JOB_SERVICE` 保护；同时声明 `android.permission.RUN_USER_INITIATED_JOBS`，构造 `JobInfo` 时调用 API 34 起提供的 `setUserInitiated(true)`。安排失败（例如不满足前台/允许条件）须处理 `RESULT_FAILURE`。
- 尽可能准确地提供上传/下载字节估算（`setEstimatedNetworkBytes()`），并按业务需要配置网络、充电、电量与存储约束；估算未知或变化时再按指南更新。约束减少不合适的执行窗口，但系统健康状态仍可停止任务。
- 在 `onStartJob()` 中异步执行传输，持续通过 `JobService.setNotification()` 告知状态/进度；成功或失败后都及时 `jobFinished()`。实现 `onStopJob()` 处理系统停止和可恢复状态；不要把 `getStopReason()` 用作关键业务分支，它主要用于诊断/日志。
- Task Manager 的用户停止会立即杀掉整个应用进程，不调用 `onStopJob()`，且不会允许该用户可见任务自行重新排队。通知应提供合适的停止/继续控制，上传/下载须持久化可恢复的断点和任务状态，重新启动时从安全位置恢复。
- Android UIDT 指南截至 2026-10-16 说明目前没有 Jetpack 库支持 UIDT；低于 API 34 时需选兼容方案。若回退到 WorkManager 的前台服务实现，FGS 的 Android 启动规则和 Play 政策申报仍适用。

Google Maps 的官方案例报告称，将离线下载从 FGS 迁移到 UIDT 后，下载失败率改善超过 10%；这是单个产品的回顾性实验结果，不是所有应用的效果保证，也不代表 Play 对具体用途的批准。

Android 实现入口、API 和子链逐页核验见递归链接图 4.69（快照：`../google-play-policy-link-graph.md`，未导入本仓库） 与 4.70（快照：`../google-play-policy-link-graph.md#470-%E6%95%B0%E6%8D%AE%E4%BC%A0%E8%BE%93%E5%90%8E%E5%8F%B0%E4%BB%BB%E5%8A%A1%E4%B8%8E-fcm-%E6%8C%87%E5%8D%97`，未导入本仓库）。本轮复核 Android UIDT 指南（页面标注 2026-10-16 更新）中的 **21 个相关链接位置**：20 个外链位置去重为 15 个直接目标，另有 1 个页内锚点；WorkManager 与后台 Activity 两个旧入口已记录重定向及现行目标。另复核数据传输选择页的 25 个正文链接位置（7 个页内锚点、18 次外链、14 个不同目标），并沿 FCM 文章核对 12 次正文链接、7 个不同目标。WorkManager 的重试/约束、Doze 测试、通知处理及 FCM v1/v2 迁移提示见 4.70。大型 API 参考、所有通用导航和更深示例后代仍未穷尽；FCM/Android 实现建议不是 Play 政策批准，Play 政策资格仍以本页上方的现行政策正文为准。

## `FLAG_SECURE`

应用必须尊重其他应用为敏感界面声明的 `FLAG_SECURE`，不得提供绕过或变相捕获受保护内容的功能。符合条件的无障碍工具仅在不把受保护内容传输、保存或缓存到设备外时适用所列例外。Android API 参考为 [WindowManager.LayoutParams](https://developer.android.com/reference/android/view/WindowManager.LayoutParams)；完整条文和例外见上方 Play 政策。

## 设备端 Android 容器与 `REQUIRE_SECURE_ENV`

设备端 Android 容器可把第三方 APK 加载进自身进程/空间，并截获或代理 API，使其看起来像在正常 Android 环境运行。应用可在 Manifest 声明 `REQUIRE_SECURE_ENV`，表达不应在此类容器中运行。该标志不具备技术层面的强制拦截能力；Play 政策要求在 Play 分发的容器应用检查目标应用 Manifest，不加载声明该标志的应用，不代理其调用，也不得通过加载旧版本等方式绕过。

Help FAQ 进一步说明：提供隔离工作资料且需要设备管理员权限的企业应用不因此被视为此处定义的容器；是否声明该标志由应用开发者根据自身安全/隐私需要决定。对容器实现，可参阅 [Android 限制容器加载指南](https://developer.android.com/training/basics/intents/limit-play-loading)；该指南是技术实现资料，不替代 Play 政策。

Android 指南（页面标注 2026-03-05 更新）给出的用法是在 `<application>` 中声明：

```xml
<application>
    <property android:name="REQUIRE_SECURE_ENV" android:value="1" />
</application>
```

该用例指南明确说，应用运行在哪个 Android 版本都可以使用此标记。通用 [Manifest `<property>` 参考](https://developer.android.com/guide/topics/manifest/property-element)则把这个通用元素标注为 API 31 起，并说明 `android:value` 与资源 ID 属性 `android:resource` 的语义不同、同一 `<property>` 不应同时设置两者。两条说明谈的是不同层面：不要把 API 参考的通用版本标注改写成 Google Play 对此标志新增的最低版本要求，也不要把标志说成 Android 系统会强制阻止容器加载。该标志是应用发布者表达限制、容器运营者按 Play 政策检查并尊重的声明。

本轮逐页复核了该指南的直接目标和 Manifest 参考的相关后代；目标、链接计数及 `WindowProperties` 抓取失败边界见递归图 4.84（快照：`../google-play-policy-link-graph.md#484-requiresecureenv-android-容器指南与-manifest-property-后代`，未导入本仓库）。

## 电量优化豁免：政策适用与实现边界

Play 禁止不符合 allowlisting 资格的应用绕过系统电源管理；Android Doze 指南进一步说明 Android 6.0+ 不得在核心功能不会受损时直接请求忽略电池优化。只有“后台任务重要”不足以证明资格。优先验证 FCM `RemoteNotification`、可延后/可恢复任务和专用 API 是否满足核心场景；确因技术依赖无法使用 FCM，或 Doze/App Standby 会实际破坏核心功能时，再按官方用例表说明必要性。安全、核心任务自动化及持续为外围设备提供互联网连接的伴侣应用是文档列出的可接受类别；周期性同步、标准蓝牙耳机连接和可由 FCM 处理的普通即时通讯场景被列为不可接受。类别不是个案预批准，完整矩阵及 `Settings`/`PowerManager` 解释见递归图 4.71。

`ACTION_IGNORE_BATTERY_OPTIMIZATION_SETTINGS` 打开系统设置；`ACTION_REQUEST_IGNORE_BATTERY_OPTIMIZATIONS` 才是直接申请加入电量优化豁免名单的 Intent，并要求相应 Manifest 权限。`isIgnoringBatteryOptimizations()` 只查询系统名单状态，不证明 Play 资格。FGS 也不是维持进程存活或逃避 idle 的通用替代品。

2026-10-23 重试 Doze 正文中的 wake-lock 与 FCM 链接，现已打开 [`PowerManager.WakeLock`](https://developer.android.com/reference/android/os/PowerManager.WakeLock) 相关 acquire/release 说明，以及标注 Preview/Pre-GA 的 [AndroidConfigV2 迁移指南](https://firebase.google.com/docs/cloud-messaging/send/v2-api)。官方迁移指南中的 20 秒通知回调和后台 25% 抑制阈值可能在 GA 前变化，不应视为稳定 Play 要求。旧 payload 链接返回 404；通过 Firebase 官方文档搜索另行找到[消息类型说明](https://firebase.google.com/docs/cloud-messaging/customize-messages/set-message-type)，不是经验证的重定向。全部父子关系和余留缓存/登录限制见递归链接图 4.71（快照：`../google-play-policy-link-graph.md`，未导入本仓库）。FCM 实现选项不改变个人/敏感数据的 User Data、Data safety 义务。

## 页面正文链接与核验状态

下表按目标页去重；同一链接在正文多处出现时，引用台账仍分别保留。通用帮助页脚、问卷/图片和账户支持控件不作为政策义务；短链接目标未能恢复时明确列为未解析。

| 直接目标 | 与本政策的关系及核验状态 |
| --- | --- |
| [Core App Quality guidelines](https://developer.android.com/docs/quality-guidelines/core-app-quality) | Play 指向的应用质量/系统优化指南。2026-10-23 补核隐私与权限的 8 个正文锚点/7 个目标，并沿 Common intents → 联系人选择、Security checklist → 存储/日志跟进；长文全部测试、Android API/示例后代未遍历，见应用质量专题[应用质量与设备形态](../app-quality-and-form-factor-guidelines/app-quality-and-form-factor-guidelines.zh-CN.md)。 |
| [App Security Improvement Program](https://developer.android.com/privacy-and-security/googleplay-asi) | Android 安全修复计划入口；已有独立摘要。历史漏洞活动日期不应当作新的现行 Play 截止期。 |
| [Doze and App Standby / system power management](https://developer.android.com/training/monitoring-device-state/doze-standby.html) 与[现行无 `.html` 入口](https://developer.android.com/training/monitoring-device-state/doze-standby) | Android 系统指南说明 Doze 会暂停网络并延后作业；现行页面（2026-10-22 更新）增加 FCM AndroidConfigV2 类型建议、Doze/App Standby 测试，并明确不符合资格时不得直接请求忽略电量优化。它与上方“不得在不符合资格时绕过 Android 电源管理”的 Play 条款互相印证；豁免用例、FCM 替代方案、Intent/API 及直接子链接核验见递归图 4.71（快照：`../google-play-policy-link-graph.md`，未导入本仓库）；关键资格判断如下。技术后代仍部分未闭合。 |
| [Android 14 behavior changes](https://developer.android.com/about/versions/14/behavior-changes-14) | 与 `FULL_SCREEN_INTENT` 等平台规则相关的 Android 版本指南；目标已打开，本专题不把平台兼容要求改写成额外 Play 政策。 |
| [Android Application Sandbox](https://source.android.com/docs/security/app-sandbox)（[简体中文](https://source.android.com/docs/security/app-sandbox?hl=zh-cn)） | 2026-10-24 重开英文与简体中文正文（AOSP 页面标注 2026-09-30 更新）。它解释每应用 UID、内核隔离及 SELinux/seccomp 等纵深防御；Play 对应的明确义务是不得绕过沙盒推断其他应用中的活动或身份。正文 10 个链接位置去重为 9 个目标，文件/媒体/权限子链已按政策相关性分流；Android 存储 API 是实现背景，不会自行产生 Play 资格或额外政策义务。见递归链接图 §4.141（快照：`../google-play-policy-link-graph.md#4141-device-and-network-abuse-android-application-sandbox-文件分享后代2026-10-24`，未导入本仓库）。 |
| [`WindowManager.LayoutParams`](https://developer.android.com/reference/android/view/WindowManager.LayoutParams) | `FLAG_SECURE` API 参考；大型 API 文档，只核对该政策引用及相关常量，不展开无关成员。 |
| [Limit loading in on-device Android containers](https://developer.android.com/training/basics/intents/limit-play-loading) | Android 指南 2026-03-05 更新，明确 `REQUIRE_SECURE_ENV` 位于 `<application>` 且可用于任意 Android 版本；其 4 个政策/Manifest 正文目标均已打开。沿 `<property>` 参考又核对 21 个链接位置、11 个规范化目标（含本页自链）；`WindowProperties` 目标不可访问。详见递归图 4.84（快照：`../google-play-policy-link-graph.md#484-requiresecureenv-android-容器指南与-manifest-property-后代`，未导入本仓库）。 |
| [Manifest `<property>` element](https://developer.android.com/guide/topics/manifest/property-element) and [`<application>` element](https://developer.android.com/guide/topics/manifest/application-element) | Android 通用参考说明属性可放入父组件；此 Play 标志的具体指南明确指定 `<application>`。参考页的 API 31 标签与用例指南的“任意 Android 版本”原文并列记录，不推定系统强制拦截。 |
| [Other manifest component references: `<activity>`](https://developer.android.com/guide/topics/manifest/activity-element), [`<activity-alias>`](https://developer.android.com/guide/topics/manifest/activity-alias-element), [`<provider>`](https://developer.android.com/guide/topics/manifest/provider-element), [`<receiver>`](https://developer.android.com/guide/topics/manifest/receiver-element), and [`<service>`](https://developer.android.com/guide/topics/manifest/service-element) | `<property>` 通用语法页把这些列为可包含属性子元素的组件；它们不是本用例指南对 `REQUIRE_SECURE_ENV` 的推荐放置位置。仅核对相关 Manifest 条目入口，通用组件/API 后代未遍历。 |
| [User-initiated data transfer](https://developer.android.com/develop/background-work/background-tasks/uidt) | 页面标注 2026-10-16 更新；21 个相关链接位置中，20 个外链位置去重为 15 个目标，另有 1 个页内条件锚点。指南与直接子页的角色、关系和核验边界见递归链接图 4.69（快照：`../google-play-policy-link-graph.md#469-uidt-android-实现指南-api-选择与-play-政策边界`，未导入本仓库）；WorkManager/FCM 后续实现链见4.70（快照：`../google-play-policy-link-graph.md#470-%E6%95%B0%E6%8D%AE%E4%BC%A0%E8%BE%93%E5%90%8E%E5%8F%B0%E4%BB%BB%E5%8A%A1%E4%B8%8E-fcm-%E6%8C%87%E5%8D%97`，未导入本仓库）。JobScheduler/JobService 等大型 API 只核对相关方法，非政策技术后代仍部分未审。 |
| [Foreground Services policy](https://support.google.com/googleplay/android-developer/answer/13392821?hl=en) | 与同页 FGS 章节并行的 Play Help 说明；已有独立双语专题和全文审计，本次从合并政策链接重开时超时。 |
| [`Manifest.permission`](https://developer.android.com/reference/android/Manifest.permission) 与 [Foreground service types are required](https://developer.android.com/about/versions/14/changes/fgs-types-required) | FGS 权限常量和 Android 14 类型声明技术参考；API 目录大型且 Android 版本示例很多，分别按选定权限/类型核对，其他技术后代部分未读。 |
| [Play Asset Delivery](https://developer.android.com/guide/playcore/asset-delivery) | PAD 与 `dataSync` 窄例外的技术范围；不得扩展为普通同步/下载豁免。主指南与 Java、Native、Unity 实现及直接子链接见双语 PAD 专题[Play Asset Delivery](../play-asset-delivery/play-asset-delivery.zh-CN.md)和递归图 §4.137（快照：`../google-play-policy-link-graph.md#4137-play-asset-delivery政策边界实现指南和直接子链2026-10-24`，未导入本仓库）；API 孙链仍部分未闭合。 |
| [AccessibilityService policy](https://support.google.com/googleplay/android-developer/answer/10964491?hl=en) | 与 `FLAG_SECURE` 例外相关；已有独立全文审计。无障碍工具仍不得把受保护内容传输、保存或缓存到设备外。 |
| [Android security features](https://source.android.com/docs/security/features) | Android 安全架构背景资料；已打开，属于技术背景而非独立 Play 审批/豁免。 |
| [On-device Android container apps and `REQUIRE_SECURE_ENV`](https://support.google.com/googleplay/android-developer/answer/13609005?hl=en) | Play FAQ 已完整打开：定义容器、标志用途、企业工作资料排除项、无技术强制拦截及容器运营方必须检查并尊重标志。FAQ 的 32 项帮助侧栏不属于本政策正文闭包。 |
| [Play Console FGS 声明短链](https://goo.gle/play-permission-decl-form) → [权限声明帮助 answer/9214102](https://support.google.com/googleplay/android-developer/answer/9214102?hl=en) | 现行合并政策把 FGS 申报作为 Android 14+ 开发者的 Console 步骤；该短链指向通用权限声明帮助，实际 FGS 表单字段与资格仍须按对应应用的 Console 流程核验。详见前台服务专题（快照：`foreground-services-and-geofencing.md`，未导入本仓库）。 | 短链返回 Internal Error，但错误响应暴露了规范目标；`answer/9214102` 已单独打开。账号内真实表单未读取，未推断字段。 |

## 相关政策导航（页面底部侧栏）

- [用户数据](../user-data/user-data.zh-CN.md)与[敏感信息权限](../sensitive-permissions/sensitive-permissions.zh-CN.md)：数据用途、用户披露/同意及受限权限边界。
- [欺骗性行为](../deceptive-behavior/deceptive-behavior.zh-CN.md)与[虚假陈述](../misrepresentation/misrepresentation.zh-CN.md)：协同欺骗、身份/功能误导和其他设备滥用风险的关联规则。
- [目标 API 要求](../target-api/target-api-level.zh-CN.md)：Android 版本兼容与 Play 分发要求；是并行政策主题，不等同于设备/网络滥用条文。
- [权限政策预览](https://support.google.com/googleplay/android-developer/answer/16909972?hl=en)：未来联系人/位置要求的预览，日期应与当前合并政策区分。

## 交叉判断

| 场景 | 应分别核对 |
| --- | --- |
| 第三方 SDK 下载/执行代码 | Device and Network Abuse、SDK 要求（快照：`sdk-requirements.md`，未导入本仓库）、恶意软件/MUwS；不能仅因“SDK 自带下载器”而把责任转给供应商。 |
| 后台长任务或定位 | Android FGS 启动和类型规则、Play FGS 声明、[后台位置政策](../background-location/background-location.zh-CN.md)；满足技术条件不代表通过 Play 审核。 |
| 需要用户点击后上传/下载 | UIDT 的用户触发、网络传输与运行时长条件；自动备份/同步不因此自动符合 UIDT。 |
| 屏幕捕获、录屏、容器/多开 | `FLAG_SECURE` 与 `REQUIRE_SECURE_ENV` 的不同保护对象；一个保护敏感界面，一个声明不应在安全功能不完整的容器环境运行。 |

本专题是双语改写与目标页关系索引，不是原文逐字副本。通用 Android 文档和代码样例持续变化；涉及审核时应查看当日 Play Console 表单及官方现行政策全文。
