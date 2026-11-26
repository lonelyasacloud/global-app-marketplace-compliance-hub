---
id: google-play.android-privacy-checklist
platform: google-play
language: zh-CN
authority: operational
status: current
kb_checked_at: 2026-10-24
review_due: 2027-01-24
regions: [global]
topics: [android-privacy, permission-minimization, prominent-disclosure, identifiers, security]
snapshot_id: play.android-privacy-checklist
snapshot_package: "GooglePlay-KnowledgeBase-2026-10-24-review.zip"
coverage_status: "detailed-summary"
source_url: "https://developer.android.com/privacy-and-security/about"
source_url_permissions: "https://developer.android.com/privacy-and-security/minimize-permission-requests"
source_url_play_disclosure: "https://support.google.com/googleplay/android-developer/answer/11150561"
effective_date: "android-checklist; referenced 2027-01-27 Play dates stay on their own topics"
---

# Android 隐私清单、权限最小化与数据保护

> **导入说明（Google batch 5）。** 正文来自已经分开的 2026-10-24 Google Play 知识库快照（`play.android-privacy-checklist`，核对日 2026-10-24）的改写摘要，不是官方页面的逐字副本。英文官方页面是效力来源。`kb_checked_at` 是快照源文件记录的核对日；本次导入没有重新打开线上官方页面。文中“本知识库”“本库”“本地专题”等说法描述的是该快照库的覆盖范围，不是本仓库已经导入的页面。指向本仓库没有收录的专题、链接图、台账或 CSV 的相对链接改为文字提及。指向 Google batch 1–4 或本批八个专题的相对链接改为本仓库文件。 本页是 Android 实现清单，不是 Google Play 政策。根清单最后更新于 2026-09-21；权限概览和权限最佳实践页最后更新于 2026-10-16。这些是 Android 页面日期，不是未来的 Play 生效日。两种语言文件使用的都是不带语言参数的 `developer.android.com` 地址。快照称正文为双语改写，没有记录已核对的中文官方隐私清单页面，也没有记录本清单主页面 `hl=zh-CN` 抓取失败。本仓库中文正文是快照的编辑改写，不是 Google 已发布的中文页面文本。清单指向的 Play 日期留在各自专题：API 37 联系人变更、地理围栏前台服务变更，以及 `READ_CALL_LOG` 预告，快照都记为 2027-01-27。这些日期不是本清单的现行规则，也不是新的隐私清单生效日。平台 API 建议不等于 Play 已批准该用途。证据等级是实现说明。Play 的 User Data、Data safety 和权限政策在各自页面仍是 `normative`。

**核对日期：2026-10-24。** 这是 Android 官方技术最佳实践的双语改写，兼作 Google Play 用户数据、权限、Data safety 和后台位置政策的实现导航。根页面最后更新于 2026-09-21；Android 权限概览最后更新于 2026-10-16；Android 最佳实践帮助页最后更新于 2026-10-16。**平台 API 建议不等于 Play 审核批准**，仍须分别满足 Google Play 政策并查看 Play Console 当前要求。

## Android 清单给出的核心原则

- 只请求某个用户可见功能真正需要的最少权限；在具体功能触发时解释并请求，不要在启动时一次性索取一批权限。
- 如果用户拒绝或撤回权限，允许用户继续使用应用，并让缺少该权限的功能以合理方式降级；不要反复打扰用户。
- 定期核对 Manifest、运行时调用及 SDK/库的权限。用户通常会把 SDK 的数据访问视为应用行为；移除不再需要的权限。
- 位置、联系人、照片、媒体和电话等数据优先使用系统 Picker、临时 URI、意图或用途专用 API，避免宽泛权限。
- 对后台位置，先问它是否是核心功能不可缺少、是否提供清晰用户收益、用户是否能理解访问时机。Android 文档明确指出，采用这些最佳实践也**不能保证** Google Play 批准后台位置用途。
- 对应用数据、披露、隐私政策、Data safety、权限声明和第三方 SDK 数据流保持一致。平台运行时授权不是 Play Console 敏感权限申报的替代品。

## Android 权限工作流与高影响子链

Android 官方[权限概览](https://developer.android.com/guide/topics/permissions/overview)将处理流程分成“先判断是否有无权限替代方案、再声明所需权限、按权限类型请求并核验授权”。运行时权限须在每次使用前检查；不能把曾经授权当作永久授权。权限组只是系统界面组织方式，组成员可能随 Android 版本变化，不应用组名或成员关系代替逐项权限判断。

| 工作流/直接子页 | 应落实的检查 | 与 Play 审核的边界 |
| --- | --- | --- |
| [最小化请求](https://developer.android.com/privacy-and-security/minimize-permission-requests) | 优先 Picker、Intent、粗略/前台访问和用途专用 API；只取当前功能必需的数据 | API 替代方案可减少范围，但不免除 Data safety、披露或敏感权限申报 |
| [声明权限](https://developer.android.com/training/permissions/declaring) 与 [`<uses-permission>`](https://developer.android.com/guide/topics/manifest/uses-permission-element.html) | 审查合并后的 Manifest；删除未用权限；仅在必要时声明硬件特性，并正确设置可选特性 | Manifest 声明不是 Play 用途资格批准 |
| [运行时请求](https://developer.android.com/training/permissions/requesting) | 在用户触发的功能点请求；先解释用途；每次访问前检查；拒绝、重复拒绝和设置页撤销后都能合理降级 | 运行时授权不替代 Play 的显著披露、同意、数据安全或受限权限申报 |
| [解释敏感访问](https://developer.android.com/training/permissions/explaining-access) 与[特殊权限](https://developer.android.com/training/permissions/requesting-special) | 说明访问目的；按具体特殊权限检查系统设置授权；关注 Privacy Dashboard、传感器指示器和系统开关 | Android 的系统授权路径与 Play Console 审核/申报是两套检查 |
| [跨应用交互限制](https://developer.android.com/training/permissions/restrict-interactions) | 对导出的 Activity、Service、Provider、Receiver 使用最小组件权限和安全配置 | 组件访问控制补充应用数据保护，不会使敏感数据用途自动合规 |
| [App permissions best practices](https://developer.android.com/training/permissions/usage-notes) | 不在启动时批量索权；解释拒绝影响；审计 SDK；测试授权/拒绝/撤销组合；后台位置须对核心功能必要；短信/通话权限遵循默认处理器流程 | 页面是 Android 实现指导；SMS/Call Log、后台位置、前台服务仍须分别满足对应 Play 政策 |

### 权限参考页与实现边界

- [`Manifest.permission`](https://developer.android.com/reference/android/Manifest.permission) 是大型平台权限目录；本知识库只核对与位置、联系人、媒体、电话及相关前台服务有关的条目，不声称逐项摘要全部常量。
- [`<permission-group>`](https://developer.android.com/guide/topics/manifest/permission-group-element.html) 将权限归入系统界面类别；[`<manifest>`](https://developer.android.com/guide/topics/manifest/manifest-element.html)、[`<permission>`](https://developer.android.com/guide/topics/manifest/permission-element.html)、[`<permission-tree>`](https://developer.android.com/guide/topics/manifest/permission-tree-element.html) 及 [`<uses-permission>`](https://developer.android.com/guide/topics/manifest/uses-permission-element.html) 是 Manifest 元素参考。自定义权限主要保护应用组件/能力，与申请用户个人数据权限不是同一概念。
- [Android 权限示例仓库](https://github.com/android/platform-samples/tree/main/samples/privacy/permissions)的 [README](https://github.com/android/platform-samples/blob/main/samples/privacy/permissions/README.md)、[`SinglePermission.kt`](https://github.com/android/platform-samples/blob/main/samples/privacy/permissions/src/main/java/com/example/platform/privacy/permissions/SinglePermission.kt)、[`MultiplePermissions.kt`](https://github.com/android/platform-samples/blob/main/samples/privacy/permissions/src/main/java/com/example/platform/privacy/permissions/MultiplePermissions.kt)、[`ComposePermissions.kt`](https://github.com/android/platform-samples/blob/main/samples/privacy/permissions/src/main/java/com/example/platform/privacy/permissions/ComposePermissions.kt) 和 [`build.gradle.kts`](https://github.com/android/platform-samples/blob/main/samples/privacy/permissions/build.gradle.kts) 已逐项阅读。样例用 Activity Result 权限合约演示单项/多项授权及 Compose 状态；多项样例在相机获准、麦克风被拒时仍可无声录制，并在恢复前台时刷新权限状态。README 明示样例和 UX 为简洁而简化，且同一示例应用共享权限状态；这不是生产实现的完整清单或 Play 用途批准。Compose 示例采用标为 experimental 的 Accompanist API；仓库其余文件树、`src/main` 和公共 UI 支持目录仍有 Cache miss，主分支也会变化。详见递归链接图 §4.101（快照：`../google-play-policy-link-graph.md`，未导入本仓库）和逐 URL 审计表。 [ADB](https://developer.android.com/tools/adb) 可用于测试授权与撤销，命令和设备/API 组合应在目标环境验证。
- [AOSP 安全功能索引](https://source.android.com/docs/security/features)概述应用 UID 沙箱、签名、加密、Keystore、SELinux、TEE 和 Verified Boot 等平台基线；这些机制不构成 Play 政策合规证明。Android 文档中嵌入的图片不是页面目标；一个外部设计旧链接只有重定向，权限教学视频在本次读取中未能取到字幕。

## 更小权限范围的实现选择

| 用户任务 | Android 首选方案 | 与 Play 政策的关系 |
| --- | --- | --- |
| 偶尔选照片/视频 | Photo Picker；让系统只把用户选中的媒体临时授权给应用 | 可减少对整个照片/视频库的访问；仍须按照片/视频权限规则和用户数据政策处理数据 |
| 挑联系人或地址 | Contact Picker；声明要用的字段，只读取用户选中的联系人数据 | 对 2027-01-27 起的 API 37 联系人权限规则尤为关键；见[联系人与前台位置专题](../contacts-location-permissions/contacts-location-permissions.zh-CN.md) |
| 临时精确位置 | Android Location Button；一次会话、用户点击后授权 | 适合单次搜索附近/填地址等操作；不代替持续或后台定位审批 |
| 打开用户选定文件 | Storage Access Framework、系统文件选择器或应用自己的文件 | 不要为单文件选择而索取整库文件访问权限 |
| 拍摄照片/视频 | 若由预装相机完成，使用相机 Intent，而非为了该操作常驻申请 `CAMERA` | 应用自己需要持续控制相机时另按实际功能判断权限 |
| 附近蓝牙设备配对 | Companion Device Manager | 可避免仅为配对设备而请求位置权限；连接/扫描的实际 API 仍须核对 Android 版本要求 |
| 短信验证码/读取单条短信 | SMS Retriever；格式不受控时用 SMS User Consent | 见[SMS/通话权限专题](../sms-call-log/sms-call-log.zh-CN.md)；不要默认请求 `READ_SMS` |
| 输入手机号、筛查来电、拨号 | Phone Number Hint、Digital Credentials、`CallScreeningService` 或 `ACTION_DIAL` 等用途专用能力 | 不要把手机状态/通话权限扩大到非核心用途；SMS/通话受限权限仍要符合 Play 规则 |
| 扫描条码 | Google Code Scanner；需要定制体验时评估 ML Kit | 可避免应用自行取得相机图像流；数据收集/第三方 SDK 披露仍适用 |

替代 API 能减少权限范围，但并不免除数据安全、商店披露和 SDK 责任。应按最小字段、最短访问时限和具体用户操作选实现，并测试拒绝、撤回和只给粗略位置等状态。

## 用户数据、显著披露和同意

Android 隐私清单要求在 Play 数据安全表单中如实说明数据收集和共享；它还提示应检查密码输入、身份认证、WebView、自动填充、数据访问审计、第三方库等不易从权限清单直接看出的数据流。Android 的 Data safety 辅助指南也明确：类别/权限/API 示例是**非穷尽**的；开发者需根据实际行为申报 SDK/库收集或分享的数据；若实际行为与申报不符，Google 可采取执行措施。见[Data safety 专题](../data-safety/data-safety.zh-CN.md)。

### Declare your app's data use：把实现线索映射到申报类别

Android 官方[数据使用申报指南](https://developer.android.com/privacy-and-security/declare-data-use)于 **2026-03-06** 更新，是 Google Play Data safety 表单的技术补充。指南按 14 个表单数据类别列出常见权限、API、SDK 和界面线索；它明确说示例不穷尽，且开发者仍独自负责准确申报。下表是把页面例子整理成核对入口，不是“看见某权限就必定申报收集”的自动规则：应继续确认实际读取的数据、是否离开设备、是否交给第三方以及 SDK 的处理行为。

| Data safety 类别 | 指南举出的实现线索 | 本库的交叉核对入口 |
| --- | --- | --- |
| 位置 | `ACCESS_COARSE_LOCATION`、`ACCESS_FINE_LOCATION`、`ACCESS_MEDIA_LOCATION`；也可能由 IP 或接入点名称推导 | [前台/后台位置](../background-location/background-location.zh-CN.md)、[联系人与位置权限](../contacts-location-permissions/contacts-location-permissions.zh-CN.md) |
| 个人信息 | `BIND_AUTOFILL_SERVICE`、`GET_ACCOUNTS`、`AccountManager`；电话号码还可能涉及电话/SMS 权限、默认拨号器或短信应用、运营商权限 | [用户数据](../user-data/user-data.zh-CN.md)、[SMS/通话权限](../sms-call-log/sms-call-log.zh-CN.md) |
| 财务信息 | Google Play Billing Library、Google Pay API、自动填充 | [付款、计费与订阅](../payments/payments-and-subscriptions.zh-CN.md)；支付 SDK 收到的数据仍须按实际数据流判断 |
| 健康与健身 | `ACTIVITY_RECOGNITION`、`BODY_SENSORS`、`BODY_SENSORS_BACKGROUND`、Health Connect、Google Fit、Sleep API | [健康应用与 Health Connect](../health-apps-and-health-connect/health-apps-and-health-connect.zh-CN.md) |
| 消息 | `READ_SMS`、`RECEIVE_MMS`、`RECEIVE_SMS`、`RECEIVE_WAP_PUSH`、`SEND_SMS` 等 | [SMS/通话权限](../sms-call-log/sms-call-log.zh-CN.md)；受限权限资格与 Data safety 分类是两项独立核验 |
| 照片与视频 | Android Photo Picker、媒体/存储权限、媒体文件工作流、HDR 视频录制 | [照片与视频权限](../photo-video-permissions/photo-video-permissions.zh-CN.md)；优先核对用户选择范围和临时授权 |
| 音频文件 | `RECORD_AUDIO`、`CAPTURE_AUDIO_OUTPUT`、共享存储中的音频工作流 | [敏感权限](../sensitive-permissions/sensitive-permissions.zh-CN.md)；记录音频和读取用户音频文件是不同数据流 |
| 文件与文档 | 读取/写入共享存储、`MANAGE_EXTERNAL_STORAGE`、文件存储及备份工作流 | [敏感权限](../sensitive-permissions/sensitive-permissions.zh-CN.md)；Play 对“所有文件访问”另有准入和申报要求 |
| 日历 | `READ_CALENDAR`、`WRITE_CALENDAR` | 仅当应用或其 SDK 实际访问/传输日历数据时，按具体流程判定 |
| 联系人 | `READ_CONTACTS`、`WRITE_CONTACTS` 及电话/SMS 类权限线索 | [联系人与位置权限](../contacts-location-permissions/contacts-location-permissions.zh-CN.md)；新规则下还要判断 Contact Picker 是否足够 |
| 应用活动 | `AccessibilityService`、`QUERY_ALL_PACKAGES`/已安装应用查询、搜索界面、Shortcuts Integration、`Instrumentation` | [敏感权限](../sensitive-permissions/sensitive-permissions.zh-CN.md)；Accessibility 与广泛包可见性另受 Play 政策限制 |
| 网页浏览 | 默认浏览器流程、浏览缓存或 Cookie、搜索界面 | 若应用控制 WebView 提供的代码/行为，另检查其收集和向第三方传输的数据 |
| 应用信息与性能 | 崩溃/诊断用途的 `ActivityManager`、`ApplicationErrorReport`、`ApplicationExitInfo`、`BatteryManager`、`Debug`、`PowerManager`、`StrictMode`、`AudioManager` 等 API | [Data safety](../data-safety/data-safety.zh-CN.md)、[第三方 SDK 要求](../sdk-requirements/sdk-requirements.zh-CN.md)；逐项核对 SDK、用途、保留和接收方 |
| 设备或其他 ID | IMEI、MAC、Widevine Device ID、Firebase Installation ID、Advertising ID；`AD_ID` 和 IP/接入点推导也是线索 | [广告 ID](../advertising-id/advertising-id.zh-CN.md)、[用户数据](../user-data/user-data.zh-CN.md)；可重置 ID 与永久标识符的关联规则不同 |

关键边界：Manifest 中声明权限、调用某 API 或集成某 SDK，都只是数据流排查线索；最终按 Play 的“收集/分享”定义和真实运行行为申报。设备本地处理、端到端加密、服务提供商等边界见[Data safety 专题](../data-safety/data-safety.zh-CN.md)，权限本身是否可用则另按相应 Play 政策判断。

显著披露与同意是独立义务，不能用隐私政策或 Data safety 页面替代。Google Play 的[显著披露最佳实践](https://support.google.com/googleplay/android-developer/answer/11150561)要求：

1. 在应用内、接近权限或能力请求之前展示；不能只放在商店描述或网站上。
2. 清楚解释为什么需要该能力、涉及什么数据、数据如何服务核心功能；若 SDK 会把数据交给第三方，也要说明数据类型、用途和第三方共享。
3. 至少给出同意和拒绝/稍后决定两种选择；拒绝/撤回后让不依赖该数据的功能继续可用，并尊重用户多次拒绝后的选择。
4. 文案清楚易懂（指南以约 13 岁读者为参考），不模拟 Android 系统权限弹窗，避免误导用户以为平台已替应用同意。
5. Play Console 权限声明需要视频时，视频应展示启动应用、完整披露文本、用户同意和拒绝流程、再次进入披露的流程，以及真实核心功能怎样使用该能力。

隐私政策仍须按 Play 要求同时在 Console 和应用内提供；Data safety 申报、运行时权限弹窗、显著披露/肯定同意和开发者隐私政策是不同环节，应相互一致。

界面细节、Why/What/How 示例、SDK 第三方共享文案和申报视频检查点见[用户数据政策外部参考专题](../user-data-policy-references/user-data-policy-references.zh-CN.md)。该指南属于最佳实践；相关强制要求仍以 User Data 政策正文为准。

## 位置、后台任务和前台服务

- 许多功能只需用户正在使用应用时的位置；能用粗略位置就不要请求精确位置。配对附近设备优先看 Companion Device Manager。
- 若确须后台定位，访问应对核心功能必要、用户收益明确且对用户可见；代码清单还应检查 SDK、WorkManager/JobScheduler、AlarmManager、服务和 PendingIntent 中的定位调用。
- Android 8.0/API 26 及以上会限制后台更新，通常每小时只有少数定位回调；不要把地理围栏当成精确秒级定位承诺。
- 用户发起并需持续可感知的位置任务，可按平台 FGS 规则在应用仍可见时启动服务；但该服务仍受 Play 前台服务类型申报、后台位置政策和**2027-01-27 地理围栏 FGS 用例变化**约束。参见[后台位置](../background-location/background-location.zh-CN.md)和[前台服务与地理围栏迁移](../foreground-services-and-geofencing/foreground-services-and-geofencing.zh-CN.md)。

## 标识符、存储和安全

- 优先可重置、应用范围内的标识符。Android 指南通常建议非广告用途采用 Firebase Installation ID 或应用私有 GUID；避免 IMEI、序列号、MAC 等长期设备标识符。
- Advertising ID 仅限广告和用户分析；每次读取检查退出设置，尊重重置/删除，并按用途遵守 PII 与持久标识符关联限制。儿童和混合受众另有 Families 限制。见[AAID 专题](../advertising-id/advertising-id.zh-CN.md)。
- 只共享数据时用受限 ContentProvider/显式 Intent；敏感数据尽量使用一次性授权。不要把敏感数据写入 Logcat 或日志。
- 内部存储默认比共享外部存储更受保护；外部存储内容可能被其他应用读取/修改。ContentProvider 应尽量不导出，必要时以最小权限开放。
- 对网络传输使用 HTTPS；处理外部文件和 Intent 数据时执行输入校验。下文补充 Android 官方安全最佳实践指南中的跨应用通信、网络、WebView、权限委托、存储和依赖更新做法。

## Android 应用安全最佳实践：保护跨应用数据和本地存储

Android 官方[提升应用安全性指南](https://developer.android.com/privacy-and-security/security-best-practices)最后更新于 **2026-10-16**。该页是 Android 实现建议，不是独立的 Google Play 通过标准；它有助于减少数据泄露和权限范围，但不能代替 User Data、Data safety 或敏感权限政策审查。

| 风险面 | 可落实的 Android 做法 | 与 Play 数据义务的关系 |
| --- | --- | --- |
| 应用间传输 | 由隐式 Intent 交给其他应用时显示系统选择器；在自有应用之间使用签名级权限；默认不导出不需跨应用访问的 ContentProvider。展示敏感或付费内容前可要求 PIN、密码或生物识别。 | 接收方、数据字段和用户预期仍需纳入数据流图；组件权限只控制访问面，不构成 Play 数据用途批准。 |
| 网络与 WebView | 服务端连接使用 TLS/HTTPS；自定义 CA 使用 Network Security Configuration，避免接受任意证书。WebView 限制到受控来源；仅当内容完全可信且受控时启用 JavaScript bridge，较新的通信场景优先评估 HTML message channels。 | 传输加密可支持 Data safety 的安全实践描述，但不能掩盖收集/共享；目的地、SDK 与 Web 内容仍按真实数据流申报。 |
| 权限委托与文件共享 | 能由其他应用完成的动作优先用 Intent；文件选择使用系统提供的 URI 授权，跨应用共享采用 `content://`、`FileProvider` 和按需只读/只写的一次性 URI 授权，避免 `file://`。 | Picker/Intent 可缩小权限，但不会免除 Data safety、显著披露或受限权限要求。 |
| 存储 | 私密数据优先放应用内部沙箱；非敏感且仅供应用使用的文件才考虑应用专属外部目录；跨应用媒体用 MediaStore、其他文档用 Storage Access Framework。检查可移除存储是否仍可用，并校验外部文件内容。敏感缓存放内部缓存，SharedPreferences 使用 `MODE_PRIVATE`。 | 存储位置和访问控制是保护措施；还需按是否外传、留存、共享及删除路径申报。 |
| 平台安全组件与依赖 | 使用 Google Play services 的应用按指南异步检查设备安全提供方更新；发布前更新 Android 工具、第三方 SDK 和依赖并应用安全补丁。 | 第三方 SDK 的数据行为由开发者负责；结合[第三方 SDK 专题](../sdk-requirements/sdk-requirements.zh-CN.md)核对权限、传输、留存和披露。 |

正文还链接了大量 Android API 参考与代码示例。已打开并登记与上述做法直接相关的 Intent/Provider、网络安全、WebView、权限和文件存储子页；大型 API 目录及其更深成员链接仍是部分覆盖，逐项状态见递归链接图 §4.104（快照：`../google-play-policy-link-graph.md`，未导入本仓库）和来源台账。

### Google Play App Security Improvement 活动

[App Security Improvement Program](https://developer.android.com/privacy-and-security/googleplay-asi) 会扫描应用并通过邮件/Play Console 通知潜在安全问题；部分通知含账号专属整改期限，部分问题可能阻止后续更新。其活动表里的日期是历史活动启动日期，不是当前统一截止日。35 个支持目标、正文访问状态和修复摘要见活动与整改专题（快照：`android-app-security-improvement-campaigns.md`，未导入本仓库）；每个活动页的技术后代仍部分未审阅。实务上应以对应应用 Console 告警确定目标版本、期限和发布影响。

## 直接链接与覆盖记录

| 官方目标页 | 本专题摘要及关系 | 状态 |
| --- | --- | --- |
| [Permissions on Android](https://developer.android.com/guide/topics/permissions/overview) | 先找无权限替代方案，再声明并按权限类型请求；运行时权限须在每次访问前检查；权限组成员可能变化，不应假设组关系稳定。正文 15 个链接实例、12 个唯一外部目标及 2 个页内锚点；图片不计页面 | 正文已复核；官方标注更新于 2026-10-16；12 个唯一外部目标均已打开或交叉到专题。样例仓库 README 与三个代码文件已读，Activity/Fragment/Accompanist 关键子页已分析；动态目录其余文件、公共 UI 源码及大 API 参考仍部分覆盖，见§4.101 |
| [Privacy checklist](https://developer.android.com/privacy-and-security/about) | 权限最小化、位置、数据安全、重置标识符、面向用户的隐私功能；页面列出 Play User Data、Data safety 及 Android API 最佳实践 | 正文已打开；最后更新 2026-09-21；通用页的部分技术后代未逐个深挖 |
| [Minimize your permission requests](https://developer.android.com/privacy-and-security/minimize-permission-requests) | 用粗略位置、Picker、意图、系统功能或用途专用 API 代替宽权限；涵盖文件、相机、蓝牙、短信/电话及条码 | 正文已打开；最后更新 2026-08-19；主要替代方案已整理，个别 API 的代码样例/版本后代保留官方链接 |
| [Request runtime permissions](https://developer.android.com/training/permissions/requesting) | 在具体功能情境申请、给可取消的理由说明、每次操作重新检查授权、处理拒绝与撤回 | 正文已打开；复杂 API/代码样例后代未全部复制 |
| [App permissions best practices](https://developer.android.com/training/permissions/usage-notes) | 请求应对应用户动作；解释拒绝的影响、处理撤销、审核 SDK 权限；后台位置应为核心功能所需；SMS/通话权限按默认处理器流程；测试授权组合 | 2026-10-24 重开正文；页面最后更新 2026-10-16。13 个正文链接实例归并为 11 个目标；默认处理器、后台位置、ADB、运行时、标识符和许可页已交叉核对。旧 Material 页面只重定向，视频未取到字幕；详见递归图 §4.59。 |
| [Permissions used only in default handlers](https://developer.android.com/guide/topics/permissions/default-handlers) | 先确认应用确实实现短信/电话/Assistant 等默认处理器核心功能，提供隐私政策和清楚的商店功能说明，只申请与用途相称的权限；先取得用户默认角色，再请求关联运行时权限。还要满足 Play 资格、申报/审核及失去默认角色后停止使用等要求。 | 2026-10-24 重开；正文 205 行，更新于 2026-02-26。7 个链接实例归并为 6 个目标并逐项尝试；两个旧路由的重定向关系已交叉核对，三张示意图未能取回（其中一张未暴露 URL）。短信/通话规则和 2027-01-27 `READ_CALL_LOG` 变更见[专题](../sms-call-log/sms-call-log.zh-CN.md)与递归图 §4.59。 |
| [Android `<permission-group>` element](https://developer.android.com/guide/topics/manifest/permission-group-element.html) | 权限组只是系统界面的逻辑分类；不要将组成员当作固定集合或授权判断 | 正文已打开；[`<manifest>`](https://developer.android.com/guide/topics/manifest/manifest-element.html)、[`<permission>`](https://developer.android.com/guide/topics/manifest/permission-element.html)、[`<permission-tree>`](https://developer.android.com/guide/topics/manifest/permission-tree-element.html)、[`<uses-permission>`](https://developer.android.com/guide/topics/manifest/uses-permission-element.html) 均已打开；更深 API 后代部分覆盖 |
| [Prominent disclosure and consent](https://support.google.com/googleplay/android-developer/answer/11150561) | Play 对时机、清楚文案、同意/拒绝、第三方共享和 Console 视频展示的具体最佳实践 | 英文正文已完整打开并整理；关联政策在 User Data 专题 |
| [Declare your app's data use](https://developer.android.com/privacy-and-security/declare-data-use) | 将权限/API/SDK 数据访问映射到 14 个 Data safety 类别；技术例子非穷尽，开发者负责准确申报 | 2026-10-23 重开 471 行正文（页面标注 2026-03-06 更新）并逐项尝试正文外链；14 类和关键线索已整理于上表。Widevine Device ID 旧目标此前直接打开为 404，父页早先点击为 Cache miss，本次父页重试仍为 404；另读[Widevine 总览](https://developers.google.com/widevine/drm/overview)，仅作 DRM 产品背景，不替代 ID 资料。大型 API 参考仍未逐成员摘要。 |
| [Best practices for unique identifiers](https://developer.android.com/identity/user-data-ids) | 可重置 ID、禁止桥接广告 ID 重置、应用范围 FID/GUID、避免硬件标识符及跟踪关联 | 正文相关章节已打开；硬件/账号/广告标识符的全部技术分支仍保留官方页 |
| [Android Security checklist](https://developer.android.com/privacy-and-security/security-tips) | 应用沙箱、身份验证、Play Integrity、存储/ContentProvider、权限和网络安全 | 已打开相关章节；全文范围涵盖更广的 Android 安全指南，本专题只摘录与数据/权限直接相关部分 |
| [Improve your app's security](https://developer.android.com/privacy-and-security/security-best-practices) | 跨应用通信、TLS/网络配置、WebView、权限委托、URI 授权、私有存储、缓存和依赖更新 | 2026-10-23 打开完整 646 行正文；页面标注更新于 2026-10-16。核心做法已整理于上节；政策相关技术子页已抽查并登记，但完整 Android API/代码后代仍部分覆盖；这不是 Play 审批标准 |
| [Manifest.permission reference](https://developer.android.com/reference/android/Manifest.permission) | Android 平台权限定义，不代表 Play 审核批准 | 6,738 行 API 参考已打开；核对 ACCESS_BACKGROUND_LOCATION、READ_CONTACTS、READ_MEDIA_IMAGES/VIDEO、USE_LOCATION_BUTTON 与 FGS 权限等关联字段；不是对每项权限的全文摘要 |
| [User Data policy](https://support.google.com/googleplay/android-developer/answer/10144311?hl=en)、[Data safety](https://support.google.com/googleplay/android-developer/answer/10787469?hl=en) | 正式 Play 数据处理义务与申报要求 | 正文已有[用户数据专题](../user-data/user-data.zh-CN.md)和[Data safety 专题](../data-safety/data-safety.zh-CN.md)，与平台实现建议交叉关联 |
| [Background location](https://developer.android.com/develop/sensors-and-location/location/background) 与 [Foreground service types](https://developer.android.com/develop/background-work/services/fgs/service-types) | 核心功能/用户收益、平台后台更新限制、类型权限和目的专用替代 API | 两页已打开；核心章节见[位置专题](../background-location/background-location.zh-CN.md)和[前台服务专题](../foreground-services-and-geofencing/foreground-services-and-geofencing.zh-CN.md)，API 逐类型示例及所有技术后代未穷尽 |

Android Privacy Checklist 的页面内链接还包括 PDF 隐私速查表、Android 版本文档、日志、包可见性、存储、传感器指示器、Play Academy/帮助入口等。对 Data-use 指南正文的直接链接逐项点击后，[SMS/Call Log](https://support.google.com/googleplay/android-developer/answer/10208820?hl=en) 目标经规范 URL 重试成功，[Macrobenchmark](https://developer.android.com/topic/performance/benchmarking/macrobenchmark-overview) 旧目标经官方搜索解析到现行指南。对[Widevine Device ID 旧地址](https://developers.google.com/widevine/drm/client/android/vendor-extensions)，此前精确 URL 直接打开和本次父页点击均返回 404，另一次父页点击曾返回 Cache miss；因此目标正文和其后代仍未审阅。另行阅读的[Widevine DRM 总览](https://developers.google.com/widevine/drm/overview)介绍 DRM 产品、支持平台及许可流程，但没有解释 Device ID；它只是背景资料，不是旧目标的替代页。当前资料不足以判定该 ID 的获取方式、持久性或特定 API 关联。大型 API 参考及其成员、课程、视频和通用 Android 导航未全部离线归档；Android 技术线索也不等同于 Play 强制条款。

## 关联专题

- [用户数据](../user-data/user-data.zh-CN.md) · [Data safety](../data-safety/data-safety.zh-CN.md) · [敏感权限与 API](../sensitive-permissions/sensitive-permissions.zh-CN.md)
- [联系人与前台位置最小范围](../contacts-location-permissions/contacts-location-permissions.zh-CN.md) · [后台位置](../background-location/background-location.zh-CN.md) · [前台服务与地理围栏迁移](../foreground-services-and-geofencing/foreground-services-and-geofencing.zh-CN.md)
- [健康应用与 Health Connect](../health-apps-and-health-connect/health-apps-and-health-connect.zh-CN.md) · [SMS 与通话记录权限](../sms-call-log/sms-call-log.zh-CN.md) · [第三方 SDK 要求](../sdk-requirements/sdk-requirements.zh-CN.md)
