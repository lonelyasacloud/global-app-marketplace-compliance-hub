---
id: google-play.foreground-services-and-geofencing
platform: google-play
language: zh-CN
authority: normative
status: current
kb_checked_at: 2026-10-24
review_due: 2027-01-24
regions: [global]
topics: [foreground-service, geofencing, background-location, uidt, android-14]
snapshot_id: play.foreground-services
snapshot_package: "GooglePlay-KnowledgeBase-2026-10-24-review.zip"
coverage_status: "detailed-summary"
source_url: "https://support.google.com/googleplay/android-developer/answer/16559646?hl=en"
source_url_fgs: "https://support.google.com/googleplay/android-developer/answer/13392821?hl=en"
source_url_zh: "https://support.google.com/googleplay/android-developer/answer/16559646?hl=zh-CN"
source_url_fgs_zh: "https://support.google.com/googleplay/android-developer/answer/13392821?hl=zh-CN"
source_url_preview: "https://support.google.com/googleplay/android-developer/answer/16965181?hl=en"
effective_date: "current FGS policy; geofencing FGS change 2027-01-27 kept separate; precise-location compliance 2027-01-27 kept separate"
---

# 前台服务与地理围栏迁移

> **导入说明（Google batch 5）。** 正文来自已经分开的 2026-10-24 Google Play 知识库快照（`play.foreground-services`，核对日 2026-10-24）的改写摘要，不是官方页面的逐字副本。英文官方页面是效力来源。`kb_checked_at` 是快照源文件记录的核对日；本次导入没有重新打开线上官方页面。文中“本知识库”“本库”“本地专题”等说法描述的是该快照库的覆盖范围，不是本仓库已经导入的页面。指向本仓库没有收录的专题、链接图、台账或 CSV 的相对链接改为文字提及。指向 Google batch 1–4 或本批八个专题的相对链接改为本仓库文件。 YAML 的 `reviewed_on` 是 2026-10-24。开篇写前台服务与 Android 系统行为分支复核于 2026-10-23。这两个快照日期不是政策变更。英文文件的 Play 地址使用 `hl=en`。中文文件的 YAML 记录了 `hl=zh-CN` 的 Play 帮助地址和 `hl=zh-cn` 的 Android 地址。快照正文没有记录对中文官方 Play 前台服务页面的逐项核对，也没有记录这些 `hl=zh-CN` 路由抓取失败。本仓库中文正文是快照的编辑改写，不是 Google 已发布的中文页面文本。现行前台服务资格、申报和 Android 启动规则与更晚的日期分开。地理围栏自 2027-01-27 起不再是获准的前台服务用例。该日期不是现行政策文本。另一项前台精确位置最小范围政策把 Play Console 的 `ACCESS_FINE_LOCATION` 声明安排为 2026 年 11 月开放，合规自 2027-01-27 起。Location Button 不替代后台位置审核，也不改变地理围栏日期。Android 允许由地理围栏事件在后台启动前台服务，并不表示 Play 允许该用途。没有记录中文页面核对，并不表示政策已经变更。Play 前台服务规则是 `normative`。Android 服务类型、UIDT、Doze 和 Geofence API 是实现说明。Manifest 类型或系统启动豁免不是 Play 批准。

**FGS 与 Android 系统行为分支复核日期：2026-10-23。** Google Play 的前台服务（Foreground Service，FGS）规则同时涉及 Android 运行条件和 Play 政策审核。两者都满足才够：Manifest 写了服务类型不等于 Play 已批准；Play 表单提交了，也不等于 Android 允许该时机启动服务。

## Play 政策判断：这项工作是否真的需要 FGS

除政策明确豁免的少数类型/用途外，FGS 必须同时符合这些条件：

- 支撑对用户有益、且与应用核心功能相关的功能；
- 由用户发起，或在运行过程中持续对用户可感知，例如正在播放的音频、明确的持续通知或用户要求的上传；
- 用户可以停止；
- 若被系统延迟或中断，会破坏用户预期或造成负面体验；
- 任务完成后立即停止服务，只运行完成任务所需的时间。

“有常驻通知”本身并不足以证明适合 FGS。若系统稍后执行仍不会破坏体验，应优先使用 WorkManager 等后台任务 API；只有用户明确发起、传输网络数据、且用户需要持续看到进度并会因中断而受损的工作，才考虑 Android 14+ UIDT。UIDT 是 Android 调度 API，不等于 Play 批准或 FGS 豁免；详见[设备与网络滥用专题](../device-and-network-abuse/device-and-network-abuse.zh-CN.md)。具体选择还要符合各 API 自己的边界。

现行 Play 政策把 `systemExempted`、`shortService` 类型，以及仅在使用 Play Asset Delivery 功能时的 `dataSync` 列为上述一般 FGS 标准的例外。Android 仍分别检查服务类型能否在系统上运行：当前 Android 类型指南的 `systemExempted` 条件列出系统应用、特定集成，以及在系统 Settings 中配置的 VPN 应用；它还列出持有 `SCHEDULE_EXACT_ALARM` 或 `USE_EXACT_ALARM` 等条件。不符合平台条件时系统会抛异常。此平台资格不表示所有使用 `VpnService` 的应用都自动获 Play FGS 政策豁免或 Console 批准。`shortService` 是约 3 分钟的短时类型，不需类型专属权限但仍需基础 `FOREGROUND_SERVICE` 权限。`specialUse` 不是通用绕过类型，需在 Manifest 提供子类型并接受 Play Console 审核；AOSP ToyVpn 样例使用 `specialUse`、子类型 `vpn` 的边界另见[专门专题](../vpnservice-policy-and-implementation/vpnservice-policy-and-implementation.zh-CN.md)，应针对实际应用核对。Play 的类型例外、Android 类型资格和 Play Console 申报是不同规则；不能从系统接受某一类型推断 Play 表单获批。`USE_EXACT_ALARM` 还受单独的 Play 权限政策约束，见[敏感权限专题](../sensitive-permissions/sensitive-permissions.zh-CN.md)。

## Android 14+ 的技术声明与 Play Console 表单

当应用面向 Android 14/API 34 或更高版本时，应为每项服务在 Manifest 声明准确的 `android:foregroundServiceType`，并声明所需的基础 `FOREGROUND_SERVICE` 和该类型对应的权限（例如 `location` 对应 `FOREGROUND_SERVICE_LOCATION`）。服务还可能需要位置、麦克风、摄像头或身体传感器等单独运行时权限。

面向 Android 14+ 的应用还需在 Play Console 的 **Monitor and improve → App content** 声明实际使用的服务类型。每种类型要提交：

1. 说明使用该类型的应用功能；
2. 说明系统延迟启动、暂停或重启任务会对用户造成什么影响；
3. 提供演示视频，展示用户在应用内如何触发该功能；
4. 选择最贴合的具体用例。列表不是穷尽清单，未列明的用例可自行说明。

技术类型必须与真正执行的工作相符，不要为通过审核而选择语义相近但不准确的类型；申报说明、视频、商店所述核心功能和实际代码/SDK 行为应能相互印证。

## Android 启动限制和位置权限边界

- Android 12/API 31 起，从后台启动 FGS 通常受限，系统只在规定的豁免情形放行。Android 14/API 34 对依赖“使用时”权限的服务增加启动时检查。
- 需要摄像头、麦克风、位置或部分身体传感器权限的 FGS，通常要在应用有可见 Activity 时启动。个别系统定义的豁免和后台权限会改变技术可行性，但不自动豁免 Play 政策审核。
- Android 的 `checkSelfPermission()` 对“使用时”权限可能在应用处于后台时仍返回 `PERMISSION_GRANTED`，这仅表示应用在使用时拥有该权限，并不证明此时可以创建相关 FGS；Android 14+ 可能在创建时直接抛出 `SecurityException`。不要把权限检查结果误当作后台启动许可。
- `location` 类型要求系统位置服务已开启，且应用已获粗略或精确位置权限。若应用从后台启动位置 FGS，Android 可能还要求 `ACCESS_BACKGROUND_LOCATION`。
- 如果 FGS 的实际行为构成后台位置访问，仍要满足[后台位置专题](../background-location/background-location.zh-CN.md)中的核心功能、最小范围、显著披露和 Play Console 审核要求。FGS 不能用来规避后台位置政策。

Android 的一般后台启动豁免和“使用时”位置权限访问是两组平台条件：即使某事件满足后台 FGS 启动例外，也不因此自动满足后台位置 FGS 的位置访问条件。Android 文档分别列出闹钟/地理围栏等启动事件、while-in-use 权限限制及 `ACCESS_BACKGROUND_LOCATION` 条件；Play 的 FGS 资格和位置政策仍独立适用。特别是，Android 将地理围栏事件列为一种 FGS 后台启动情形，但 Play 预告自 **2027-01-27** 起不再接受地理围栏作为 FGS 用例；平台能启动不代表 Play 允许该用途。

精确闹钟也只是 Android 的一项条件式启动例外：应用调用 exact alarm 必须是为了完成用户请求的操作。该平台例外不授予精确闹钟访问，也不代表 Play 已接受 `USE_EXACT_ALARM` 权限用途；Android 的[闹钟调度指南](https://developer.android.com/develop/background-work/services/alarms)说明系统 API 与时序行为，Play 精确闹钟资格仍按[敏感权限专题](../sensitive-permissions/sensitive-permissions.zh-CN.md)核对。

### Location FGS 的额外 Play 位置审核

Play 对 location FGS 另有位置权限审核条件。当前[后台位置权限帮助页](https://support.google.com/googleplay/android-developer/answer/9799150?hl=en)说明，部分 FGS 用途可获批准，但须作为应用内用户发起操作的延续，并在该操作完成后立即停止；若 FGS 位置行为等同于 `ACCESS_BACKGROUND_LOCATION` 或属于后台位置访问，还必须通过后台位置权限审核并提交相应声明、视频、显著披露和隐私政策。Android `location` 类型、后台启动豁免或系统权限授予都不等于 Play 批准。

另有一条前台精确位置的 Play 最小范围政策：[Play 当前说明](https://support.google.com/googleplay/android-developer/answer/17033915?hl=en)称，面向 Android 17/API 37+、仅需一次性精确位置的功能须使用 Android Location Button；其 Play Console `ACCESS_FINE_LOCATION` 声明预计于 **2026 年 11 月**开放，并要求自 **2027-01-27** 起合规。Location Button 只用于前台、事务性访问，不取代后台位置审核，也不改变地理围栏 FGS 的独立期限。Android 的 [Location Button 文档](https://developer.android.com/guide/topics/permissions/private-alternatives/location-button)只解释实现和 Manifest 条件；Play 资格与申报以 Play 政策页为准。

### 系统电量管理、后台启动和 Play allowlisting

Play 的 [Device and Network Abuse](https://support.google.com/googleplay/android-developer/answer/16559646?hl=en) 正文要求符合其 [Core App Quality guidelines](https://developer.android.com/docs/quality-guidelines/core-app-quality) 中的默认 Android 系统优化要求，并禁止不符合 allowlisting 资格的应用绕过系统电量管理。Core App Quality 还要求避免不必要的长时间后台服务；Android 的 [Doze 与 App Standby 指南](https://developer.android.com/training/monitoring-device-state/doze-standby.html)解释了后台任务、作业和普通闹钟如何被延后，并明确指出不能仅为避免应用被判为空闲而启动 FGS；直接请求忽略电池优化也只适用于该指南列出的情形。Android 后台启动文档把“用户关闭电池优化”列为一项 FGS 启动例外，这不等于 Play allowlisting 资格，也不等于 Doze 的全面豁免。按任务的可延迟性选择适当后台 API，并分别核实系统启动条件和 Play 资格。

## Android 15/API 35 的额外运行限制

以下是面向 Android 15 或更高版本应用的系统行为变化；它们补充 FGS 技术边界，不会替代 Play 对用户受益、核心功能和 Console 申报的判断。

- `dataSync` 与 `mediaProcessing` 各自在滚动 24 小时内最多运行 6 小时；同一类型的多个服务共享该类型的时长配额。应用回到前台时计时重置。到期后系统调用 `Service.onTimeout(int, int)`；服务必须在几秒内调用 `stopSelf()`，否则会发生系统异常。配额耗尽后，除非用户再次将应用带到前台，否则不能再启动同类型服务。
- `mediaProcessing` 用于诸如媒体转码的长时间处理；不能把它当作一般下载或后台计算的替代名义。若任务能延后，优先采用 WorkManager 等适当 API。
- Android 15 起，`BOOT_COMPLETED` 接收器不能启动 `dataSync`、`camera`、`mediaPlayback`、`phoneCall`、`mediaProjection` 等前台服务；麦克风类型的限制此前已从 Android 14 开始。
- 对目标 Android 15 的应用，`SYSTEM_ALERT_WINDOW` 不再单独豁免后台启动 FGS。若依赖此例外，必须先有实际可见的 overlay window，再启动服务；否则可能收到 `ForegroundServiceStartNotAllowedException`。

Android 官方建议实现超时回调、在测试设备上启用对应兼容性开关，并在回归测试中覆盖超时、重启广播与 overlay 可见性。具体 API、可用的后台替代项和测试命令见[Android 15 行为变化](https://developer.android.com/about/versions/15/behavior-changes-15)、[Android 15 前台服务类型](https://developer.android.com/about/versions/15/changes/foreground-service-types)和[Service API](https://developer.android.com/reference/android/app/Service)。

### Android 16/API 36：FGS 启动的后台作业仍受配额约束

对运行在 Android 16 或更高版本上的应用，此项变化不取决于 target API：即使后台作业由 FGS 启动，也仍受该作业类型的运行配额约束；Android 文档明确包含 `JobScheduler` 直接创建的作业及 WorkManager、DownloadManager 等库创建的作业。对用户操作触发的数据传输，Android 建议评估 UIDT；UIDT 不受普通作业配额影响，但仍受系统健康条件和停止规则约束。Play 的 UIDT 政策仍要求网络传输由用户发起且只运行到任务完成；选择 UIDT 不等于 Play 批准 FGS，也不会扩大 Play FGS 例外范围。详见[Android FGS 版本变化](https://developer.android.com/develop/background-work/services/fgs/changes)、[UIDT 指南](https://developer.android.com/develop/background-work/background-tasks/uidt)和[后台数据传输选型](https://developer.android.com/develop/background-work/background-tasks/data-transfer-options)。

## 地理围栏：2027-01-27 起的 Play 变化

Google 在 2026 年 4 月发布的政策预告中说明：自 **2027-01-27** 起，地理围栏不再是 Play 批准的 FGS 用例，建议改用 Android Geofence API。Policy Deadlines 表同时列出该日期。迁移应在期限前完成代码、权限、Play Console 声明和披露复核。

Geofence API 用位置服务监测进入/离开事件，并通过 `PendingIntent` 通知应用；接收端可启动适合的短时后台工作或发出通知。它减少了持续运行位置 FGS 的需要，但**不等于取消后台位置权限和政策要求**：地理围栏会在应用未使用时处理位置。若功能需要 `ACCESS_BACKGROUND_LOCATION`，仍要按位置政策证明必要性并做好显著披露；同时核对 Android 版本、用户授权、SDK 与 Play 审核轨道。

### 地理围栏的 Android 最佳实践

- Android 当前指南把地理围栏列为后台位置用法。只在核心功能确实需要时启用；能用前台/粗略位置就优先用更小范围，向用户解释功能为何需要后台访问，并在拒绝或撤回权限后合理降级。Android 的最佳实践不保证 Play 批准。
- Geofencing 指南列出 `ACCESS_FINE_LOCATION`，并指出 target Android 10/API 29+ 时还需 `ACCESS_BACKGROUND_LOCATION`；结合当前 Android 版本、应用实际精度需求和 Play 后台位置政策逐项核对，不能把系统授权视为 Play 许可。
- 指南建议半径至少约 **100–150 米**。Wi-Fi、室内条件、网络定位可用性和设备状态都会影响精度与触发；后台事件通常以分钟计，不能承诺秒级到达。Wear OS 上不建议使用 Geofencing API，因为其耗电效率较差。
- 对可容忍延迟的功能提高 notification responsiveness、在常驻地点适当放大半径；用 `DWELL`/loitering delay 减少短暂经过边界产生的告警。响应时间是尽力而为，不是准点 SLA。
- 功能关闭或不再需要时移除围栏；也可设置有效期让系统到期自动清理。系统会在 Google Play services 升级、因资源限制被重启或 location 进程崩溃后恢复注册；**这些情况通常不需要应用主动重注册**。设备重启、卸载后重装、应用/Play services 数据清除，或收到 `GEOFENCE_NOT_AVAILABLE` 时，如果功能仍需要，才按文档重新注册。
- 故障排查先确认权限、位置服务/Location Accuracy、围栏是否过小、Wi-Fi/网络定位及数据连接。`GEOFENCE_NOT_AVAILABLE` 表示服务当前不可用；应解释系统设置需求并让用户自行选择是否开启，不能静默改系统设置。Android 10+ 普通应用不能直接打开 Wi-Fi，应使用系统 Settings Panel。
- 如果用户发起的位置任务需要离开界面后持续访问位置，Android 隐私指南建议在 Activity 仍可见时启动符合条件的 location FGS；该实现路径仍须满足 Play FGS 规则，且地理围栏 FGS 用例仍受 2027-01-27 变更约束。

这些是 Android 技术和体验建议；Play 的核心功能、必要性、用户预期、权限申报和位置披露规则仍单独适用。

### Geofencing 操作指南的直接链接

以下是 Android [Create and monitor geofences](https://developer.android.com/develop/sensors-and-location/location/geofencing) 正文链接的目标及关系。API 参考页已打开并按地理围栏所需的类/方法/状态码作摘要；不把每个 API 成员、Java/Kotlin 示例或它们的站点导航当作新增 Play 政策。

| 目标页 | 内容与关系 | 核验范围 |
| --- | --- | --- |
| [Request location permissions](https://developer.android.com/develop/sensors-and-location/location/permissions)、[Access location in the background](https://developer.android.com/develop/sensors-and-location/location/background)、[Android Privacy checklist](https://developer.android.com/privacy-and-security/about) | 前者区分前台/后台、精确/大致位置，并说明 geofencing 的后台位置属性；后台位置清单要求核查 Manifest、位置 API、后台任务和 SDK；隐私清单建议尽量不使用位置、能用粗略则不用精确、优先用户可见时访问、后台访问须必要且明显。 | 三页正文均已打开；后台位置和隐私要求与现有双语专题交叉引用。 |
| [BroadcastReceiver](https://developer.android.com/reference/android/content/BroadcastReceiver)、[PendingIntent](https://developer.android.com/reference/android/app/PendingIntent)、[Manifest.permission](https://developer.android.com/reference/android/Manifest.permission) | 事件接收、交付事件的 Intent 令牌、精确/后台位置权限常量；参考页解释 Android 实现接口，不决定 Play 审核资格。 | 顶层 API 参考页已打开；只摘要与 geofencing 相关的用法。 |
| [Geofence](https://developers.google.com/android/reference/com/google/android/gms/location/Geofence)、[Geofence.Builder](https://developers.google.com/android/reference/com/google/android/gms/location/Geofence.Builder)、[GeofencingRequest](https://developers.google.com/android/reference/com/google/android/gms/location/GeofencingRequest)、[GeofencingRequest.Builder](https://developers.google.com/android/reference/com/google/android/gms/location/GeofencingRequest.Builder)、[GeofencingClient](https://developers.google.com/android/reference/com/google/android/gms/location/GeofencingClient)、[GeofenceStatusCodes](https://developers.google.com/android/reference/com/google/android/gms/location/GeofenceStatusCodes) | 描述围栏半径、时效、转移类型、通知响应时间/驻留延迟、初始触发、添加/移除围栏及错误状态；状态码含权限不足、服务不可用、添加过频和超过围栏数量上限。 | 参考页已打开；`GeofencingRequest.Builder` 首次点击抓取失败，后用官方索引目标核对。仅整理本专题涉及的成员/常量，不穷举整个 Play services API。 |
| [SettingsClient](https://developers.google.com/android/reference/com/google/android/gms/location/SettingsClient)、[Android 10 features and APIs](https://developer.android.com/about/versions/10/features)、[Build a device policy controller](https://developer.android.com/work/dpc/build-dpc) | 检查位置设置是否满足请求，可经系统面板请用户更改；DPC 仅适用于企业设备管理场景，不能作为普通应用静默开启系统设置的通道。 | 目标页均已打开；普通应用应使用系统 Settings Panel。 |
| [Android Geofencing sample directory](https://github.com/android/platform-samples/tree/main/samples/location/src/main/java/com/example/platform/location/geofencing)：[GeofenceManager.kt](https://github.com/android/platform-samples/blob/main/samples/location/src/main/java/com/example/platform/location/geofencing/GeofenceManager.kt)、[GeofenceBroadcastReceiver.kt](https://github.com/android/platform-samples/blob/main/samples/location/src/main/java/com/example/platform/location/geofencing/GeofenceBroadcastReceiver.kt)、[GeofencingScreen.kt](https://github.com/android/platform-samples/blob/main/samples/location/src/main/java/com/example/platform/location/geofencing/GeofencingScreen.kt) | 官方示例展示围栏注册/注销、事件解析和权限 UI。示例 manager 的默认值为 100 米和 30 分钟有效期；这是演示参数，不应覆盖指南建议的半径范围或按真实功能设定生命周期。 | 目录和三个 Kotlin 文件均已打开；文件头标注 Apache-2.0。仅记录实现关系，不复制代码；仓库 `main` 会变化。 |
| [Wear OS conserve-power guide](https://developer.android.com/training/wearables/apps/power)、[Detect activity transitions](https://developer.android.com/develop/sensors-and-location/location/transitions)、[Android documentation content license](https://developer.android.com/license) | 前者解释页面为何不建议在 Wear 上用 geofencing；活动识别是相邻 API 教程，不等于位置围栏；许可页规定 Android 文档/代码样例的使用边界。 | 页面已打开。相邻教程仅作导航背景；线下包默认保留摘要、来源与链接。 |

## 发布前清单

1. 按每个 Service、SDK 和合并 Manifest 盘点服务类型、触发入口、运行时长、通知和所有权限。
2. 逐项解释为何任务必须立即执行或持续可见；可延迟/可合并的工作改用 WorkManager 等后台 API。
3. 面向 Android 14+ 时，逐类型核对 Manifest 权限和 Console 申报；让描述、用户影响、用例与视频展示同一条真实流程。
4. 对 location FGS、地理围栏和其他后台定位分别评估 `ACCESS_BACKGROUND_LOCATION`、Play 位置申报、显著披露、隐私政策和 SDK 行为。
5. 在 **2027-01-27** 前移除把 Geofencing 申报为 FGS 用例的实现/表单材料，迁移到 Geofence API，并重新审查位置权限。
6. 将 `USE_FULL_SCREEN_INTENT` 当作独立政策主题处理；它与 FGS 的服务类型声明不是同一权限/审批。

## 关键子链接、内容与覆盖状态

| 官方目标页 | 本专题提取的内容及关系 | 状态 |
| --- | --- | --- |
| [Device and Network Abuse：Permissions for Foreground Services](https://support.google.com/googleplay/android-developer/answer/16559646?hl=en) | Play 的用户受益、核心功能、用户发起/可感知、可停止、不可延迟/中断及最短运行时长标准；列出豁免和替代 API 建议。 | 关键 FGS 章节已打开并整理；同页其他 Device/Network Abuse 章节不在本专题重复展开。 |
| [Foreground service and full-screen intent requirements](https://support.google.com/googleplay/android-developer/answer/13392821?hl=en) 与[2026 政策预告](https://support.google.com/googleplay/android-developer/answer/16965181?hl=en) | Android 14 服务类型、Play Console 每类型字段/视频及可选用例；预告地理围栏 2027-01-27 变更。 | 两页 FGS 正文均已读取；FSI 作为独立主题标出。 |
| [Policy Deadlines](https://support.google.com/googleplay/android-developer/table/12921780?hl=en) | 同一 2027-01-27 截止日期和迁移指向。 | 日期行已核对。 |
| [Foreground services overview](https://developer.android.com/develop/background-work/services/fgs) | FGS 只用于用户可感知工作；通知说明资源使用；低重要度工作改用其他后台选项。正文还列出声明/请求权限、启动、停止、用户停止、后台启动限制、服务类型、超时和故障排除等直接分支。 | 概览正文于 2026-10-22 打开，官方标注 2026-10-16 更新；直接分支已登记。关键后台启动限制页已打开，其他 Android 技术分支未全部递归。 |
| [Foreground service types](https://developer.android.com/develop/background-work/services/fgs/service-types) | Android 14 类型/权限、location 与 while-in-use 前提、Geofence API 替代建议、purpose-built API 与 specialUse 申报。 | 相关章节已整理；其余类型细节可从原文链接查询。 |
| [Foreground service types are required](https://developer.android.com/about/versions/14/changes/fgs-types-required) | Android 14 的类型迁移背景和必须声明类型的系统侧要求。 | 已打开并作为类型/权限规则的技术补充；代码示例不全文复制。 |
| [Restrictions on starting FGS from background](https://developer.android.com/develop/background-work/services/fgs/restrictions-bg-start) | Android 12+ 后台启动限制、系统豁免和 Android 14 while-in-use 权限创建时检查。即使 `checkSelfPermission()` 返回 `PERMISSION_GRANTED`，后台创建仍可能因无当前访问权限而抛出异常。 | 正文于 2026-10-22 打开，页面标注 2026-10-16 更新；启动限制、例外和位置/相机/麦克风权限章节已核对。其他豁免技术分支和 API 示例后代仍部分覆盖。 |
| [Android 15 target behavior changes](https://developer.android.com/about/versions/15/behavior-changes-15) | 目标 Android 15+ 时 dataSync/mediaProcessing 的 6 小时配额与超时回调；重启广播不能启动的服务类型；SYSTEM_ALERT_WINDOW 豁免须有可见 overlay。 | 页面已打开并对 FGS 相关章节作详细摘要；Android 15 的其他行为变化不在本专题穷举。 |
| [Android 15 FGS type changes](https://developer.android.com/about/versions/15/changes/foreground-service-types) and [Service API](https://developer.android.com/reference/android/app/Service) | 解释 `mediaProcessing` 适用工作及服务超时回调等系统 API。 | 目标页已打开/登记；更深入的代码示例和每个 API 参考成员未逐项复制。 |
| [Google Developers: Geofencing API](https://developers.google.com/location-context/geofencing) | 面向产品的 API 总览：按兴趣地点设置围栏，收到进入/离开通知；强调利用设备传感器节能。 | 总览已读；与以下 Android 操作指南分开记录；Geofence 实现不等于 Play 后台位置豁免。 |
| [Fused Location Provider API](https://developers.google.com/location-context/fused-location-provider) | Google Play services 融合 GPS、Wi-Fi 等信号，按所需准确度/耗电服务质量返回位置；概览连到 last-known location、settings 和 location updates。 | 总览已读；部分子页已在后台定位专题核验。选择 API 不改变 Play 对实际定位范围和用途的审核。 |
| [Create and monitor geofences](https://developer.android.com/develop/sensors-and-location/location/geofencing) | 事件接收、撤销围栏、电量/半径/dwell/延迟与重注册最佳实践，关联后台定位和隐私清单；另有正式 Android sample、SettingsClient 和 API 参考。 | 正文及关键直接链接已打开；API 顶层页面已核对并仅摘要相关类/状态。完整源码、API 全成员和更深 Android 技术页仍只保留来源链接。 |
| [Background Location Limits](https://developer.android.com/about/versions/oreo/background-location-limits) and [Android Privacy checklist](https://developer.android.com/privacy-and-security/about) | Android 8+ 对所有目标版本的应用施加后台更新频率限制；位置更新一般每小时少数几次，地理围栏平均约每几分钟触发。适用于实时告警时应评估前台服务、Geofencing API 或批量 FLP 等路径，并注意后台启动位置服务可能需要 `ACCESS_BACKGROUND_LOCATION`。 | 两个由地理围栏文档直接链接的目标页均已打开并摘要；Location Limits 页面标注 2024-04-29 更新，具体 Android 版本行为应以新系统指南为准。隐私清单见[Android 隐私专题](../android-privacy-checklist/android-privacy-checklist.zh-CN.md)，更深 API 参考仍未展开。 |

### 2026-10-23 FGS 高风险直接目标复核

下表只记录本次重新打开、且会影响 FGS 资格、申报、系统启动或地理围栏期限判断的官方目标。Play 条款判断资格/申报/期限；Android 页面说明系统运行条件。可访问 Android 页面也不等于 Play 批准。

| 官方目标 URL | 规则边界及关联 | 访问状态、未覆盖后代 | 核对日 |
| --- | --- | --- | --- |
| https://support.google.com/googleplay/android-developer/answer/16559646?hl=en | Play 当前 Device and Network Abuse 正文：FGS 一般须用户受益、与核心功能相关、用户发起或可感知、可停止、不能无害延迟/中断且只运行必要时长；列出 `systemExempted`、`shortService` 及 PAD `dataSync` 例外；同页另禁止不合资格时绕过系统电量管理。 | 正文已打开并核对 FGS、power-management 两节；其他 Device and Network Abuse 条款未在本分支递归审计。 | 2026-10-23 |
| https://support.google.com/googleplay/android-developer/answer/13392821?hl=en | Play Console FGS 类型申报说明：target Android 14+ 时申报每个实际类型，说明功能、延迟/中断影响、视频和用例。该页仍含 2023 申报开放日期及旧 FSI 日期，应以当前政策和期限页核对现状。 | 正文已打开；表单跳转要求登录，未能查看具体应用表单或审核状态。该页的推荐文章侧栏及所有后代不属于本次范围。 | 2026-10-23 |
| https://play.google.com/console/app/app-content/summary | Play Console App content 表单入口；账号专属页面，不是公开政策文本。 | 尝试打开；重定向到 Google 账号登录，工具无法访问表单字段或提交状态。 | 2026-10-23 |
| https://support.google.com/googleplay/android-developer/answer/16965181?hl=en | Play 政策预告：自 2027-01-27 起地理围栏不再是获批的 FGS 用例，建议转用 Geofence API。 | 正文可读；本次核对了生效日及迁移表述，未审计其非 FGS 子链。 | 2026-10-23 |
| https://support.google.com/googleplay/android-developer/table/12921780?hl=en | Play Policy Deadlines 的 2027-01-27 行再次确认同一期限和迁移目标。 | 页面可读；日期行已核对。 | 2026-10-23 |
| https://support.google.com/googleplay/android-developer/answer/9799150?hl=en | Play 后台位置审核对 location FGS 的额外条件：须延续应用内用户发起操作并在完成后立即停止；若等同后台位置访问则进入后台位置声明、视频、披露和隐私政策审核。 | 正文可读；FGS/后台位置边界及申报材料已核对。其余位置政策后代未穷举；表单直达地址要求 Play Console 登录。 | 2026-10-23 |
| https://support.google.com/googleplay/android-developer/answer/17033915?hl=en | Play 前台精确位置最小范围政策：Android 17/API 37+ 一次性精确定位使用 Location Button；`ACCESS_FINE_LOCATION` Console 声明按页面时间线于 2026-11 开放、2027-01-27 起要求合规。该政策与后台位置审核及地理围栏 FGS 期限分开适用。 | 正文可读；精确权限、Location Button 适用范围和两个日期已核对。未递归其 FAQ 的所有链接及 Console 声明流程。 | 2026-10-23 |
| https://play.google.com/console/developers/app/app-content/permission-declarations | Play 后台位置/精确位置申报表单的账号专属入口；不构成公开资格规则。 | 从 Play 后台位置政策页直达时跳转 Google 登录，工具无法读取表单或提交状态。 | 2026-10-23 |
| https://developer.android.com/guide/topics/permissions/private-alternatives/location-button | Android 17+ session-based precise location 的 Location Button 实现指南；说明 Android 库、Manifest 与系统实现，不决定 Play 对持续/后台定位的批准。 | 页面可读；适用范围、`USE_LOCATION_BUTTON` 与 `onlyForLocationButton` 说明已核对；库/API 示例和更深链接未穷举。 | 2026-10-23 |
| https://developer.android.com/develop/background-work/services/fgs/service-types | Android 类型、Manifest/类型权限及运行时前提；`systemExempted` 的平台条件包括在系统 Settings 中配置的 VPN 应用；`shortService` 有约 3 分钟时限；`specialUse` 子类型由 Play Console 审核。 | 2026-10-24 重开并核对 `specialUse`、`systemExempted` 条件；其他类型、替代 API、示例及更深 API 参考未逐项打开。 | 2026-10-24 |
| https://developer.android.com/develop/background-work/services/fgs/restrictions-bg-start | Android 12+ 后台启动例外与 Android 14+ while-in-use 权限检查；一般启动例外不自动满足位置访问要求。 | 正文可读；一般例外和位置权限边界已核对。各例外子页、广播限制子页和代码示例未全部递归打开。 | 2026-10-23 |
| https://developer.android.com/develop/background-work/services/alarms | Android 闹钟 API 技术指南；与后台启动页的“完成用户请求操作的 exact alarm”例外相关。Android 精确闹钟平台权限不等于 Play `USE_EXACT_ALARM` 资格。 | 页面可读；exact/inexact 闹钟和 Android 12+ 权限段已核对；完整 API/示例后代未穷举。 | 2026-10-23 |
| https://developer.android.com/develop/background-work/services/fgs/changes | Android FGS 跨版本变化总览：Android 16 起，FGS 启动的后台作业仍须遵守各自运行配额；Android 15/14/12 的其他版本门槛也在此汇总。 | 页面可读；Android 16 配额与 Android 12–15 对应段已核对；其他代码、测试及版本子页未全审。 | 2026-10-23 |
| https://developer.android.com/develop/background-work/background-tasks/data-transfer-options | Android 后台数据传输选型：按是否用户发起、能否延后及是否有专用 API 选择 WorkManager、UIDT 或 FGS。属于平台实现选择，不豁免 Play FGS/UIDT 条件。 | 页面可读（从旧版 `datasync-migration` 链接重定向）；选型表和 UIDT/WorkManager 条件已核对，全部 API 后代未穷举。 | 2026-10-23 |
| https://developer.android.com/docs/quality-guidelines/core-app-quality | Play Device and Network Abuse 正文直接引用的 Android Core App Quality 基线；其中有后台服务优化和 Doze/App Standby 要求。它解释系统行为和质量基线，不授予 Play allowlisting 资格。 | 正文可读（从旧版 Core App Quality URL 重定向）；后台服务优化与 power management 条目已核对，其他质量维度未纳入本专题。 | 2026-10-23 |
| https://developer.android.com/training/monitoring-device-state/doze-standby.html | Android Doze/App Standby 的系统延迟、allowlisting 和 direct battery-optimization 请求条件；FGS 不能仅用于阻止 App Standby 将应用视为空闲。 | 页面可读；电量管理、FGS/App Standby 及 Play 限制段落已核对。页面其余 FCM、测试和所有链接后代未穷举。 | 2026-10-23 |
| https://developer.android.com/develop/sensors-and-location/location/background | Android 后台位置清查和核心功能/明显性建议；该页明确指出遵循 Android 最佳实践不保证 Play 批准。 | 正文可读；Manifest、后台位置服务/闹钟/作业/SDK 检查段已核对；位置 API 和示例后代未穷举。 | 2026-10-23 |
| https://developer.android.com/develop/sensors-and-location/location/permissions/background | Android 位置权限设置流程依 target SDK 而变；描述系统用户授权行为，不决定 Play 后台位置资格。 | 正文可读；Android 10 与 Android 11+ 设置路径已核对；代码样例和进一步权限后代未穷举。 | 2026-10-23 |
| https://developer.android.com/develop/background-work/background-tasks/uidt | Android 14+ 的用户发起数据传输 JobScheduler 替代方案；仅网络传输、用户触发，并需通知/满足调度条件。它不是 Play FGS 批准或豁免。 | 正文可读；适用范围和调度条件已核对；JobScheduler 示例及更深调度后代未穷举。 | 2026-10-23 |
| https://developer.android.com/guide/playcore/asset-delivery | Android PAD 技术与 Play FGS `dataSync` 窄例外的关系；PAD 指南不授予 Play 资格。完整双语摘要及直链审计见PAD 专题（快照：`play-asset-delivery.md`，未导入本仓库）。 | 主指南与 Java、Native、Unity 集成页已打开；正文直接目标已逐项尝试，API 后代仍部分未闭合。 | 2026-10-24 |

Play FGS 政策正文中的“declaration form”短链接本次返回 Internal Error，工具未暴露其目标 URL，故不猜测或补写跳转地址；后台/精确位置申报直达入口也要求登录。尚未穷举的后代包括 Android FGS 各类型替代 API、所有后台启动例外子页、示例代码，以及 Play 后台位置文章的所有位置政策/申报更新链接。应按需回查这些后代；它们不能取代 Play 当前资格、Console 声明或 2027-01-27 期限。

### FGS Help 正文的 14 个直接目标（24 个链接锚点）

以下只统计 [FGS Help 正文](https://support.google.com/googleplay/android-developer/answer/13392821?hl=en)中的链接，不把页眉、反馈控件、页脚或 32 项推荐文章侧栏算作正文链接。重复锚点合并到同一目标；旧 URL 的重定向链保留在来源台账。

| 正文锚点 | 直接目标 | 内容与关系 | 访问/覆盖状态 |
| --- | --- | --- | --- |
| 4 | [Android 14：必须声明前台服务类型](https://developer.android.com/about/versions/14/changes/fgs-types-required) | 面向 Android 14/API 34 的类型、Manifest 权限和运行时前置条件；技术要求支撑 Play 申报，但不等于 Play 审批。 | 正文已打开；类型清单、权限及启动顺序已核对，示例和各类型后代部分覆盖。 |
| 2 | [Device and Network Abuse](https://support.google.com/googleplay/android-developer/answer/13315670) → [现行政策 answer/16559646](https://support.google.com/googleplay/android-developer/answer/16559646?hl=en) | 旧入口重定向到现行合并政策；FGS 必须用户受益、属于核心功能、用户发起或可感知、可停止且不可无害延迟，并仅运行必要时长。 | 现行政策全文已打开并摘要；本专题仅复用 FGS 章节。 |
| 1 | [Play Console App content 表单](https://play.google.com/console/app/app-content/summary) | Android 14+ 服务类型声明入口；每种类型要说明功能、延迟/中断影响、触发流程视频和具体用例。 | 目标跳转到账号登录；表单字段、提交状态和应用资格不能从公开页面确认。 |
| 1 | [Foreground service types](https://developer.android.com/guide/components/fg-service-types) → [当前 Android 指南](https://developer.android.com/develop/background-work/services/fgs/service-types) | 类型与用途匹配、权限和系统条件，以及可替代 FGS 的专用 API。 | 旧路径已重定向；正文已打开并整理相关章节，未穷举所有类型和技术后代。 |
| 1 | [MediaProjection API](https://developer.android.com/reference/android/media/projection/MediaProjection) | 屏幕采集/投影的 Android API 参考，帮助界定 `mediaProjection` 服务类型的技术用途。 | 大型 API 页面已打开；只记录与该入口有关的边界，未逐成员归档。 |
| 1 | [Notification.Builder API](https://developer.android.com/reference/android/app/Notification.Builder) | 通知构造 API；为 Help 页中通知/全屏意图示例提供实现参考。 | 大型 API 页面已打开；所有成员、示例和后代未逐项整理。 |
| 2 | [Sensitive permissions 旧入口 answer/9888170](https://support.google.com/googleplay/android-developer/answer/9888170) → [现行政策 answer/16558241](https://support.google.com/googleplay/android-developer/answer/16558241?hl=en) | 历史敏感权限入口已并入现行合并政策；重定向本身不代表 FSI 获批，也不替代 Android 系统授权。 | 重定向目标和现行政策正文已核对；FSI 仍按独立规则分析。 |
| 1 | [AOSP：Full-screen intent limits](https://source.android.com/docs/core/permissions/fsi-limits) | Android 14+ 的系统默认授权边界：默认保留给闹钟和通话类应用；Play 安装流程会撤销其他应用的默认 FSI 授权，用户可在系统设置管理。 | 页面正文已打开；系统技术行为与 Play 审核资格分开记录。 |
| 4 | [Manifest.permission API](https://developer.android.com/reference/android/Manifest.permission) | Android 权限常量参考，包括 FGS 类型权限和位置/摄像头等运行时权限。 | 大型 API 目录已打开，仅核对本页引用的条目；不能从 API 存在推导 Play 资格。 |
| 3 | [Permissions on Android](https://developer.android.com/guide/topics/permissions/overview) | 权限类别、声明/运行时请求流程及最小化、情境化、依赖审查、透明披露等最佳实践。 | 正文已打开（Android 标注 2026-10-16 更新）；本页高影响子链见下表，完整 API/示例树仍部分覆盖。 |
| 1 | [Google Play target API requirements](https://developer.android.com/google/play/requirements/target-sdk) | 目标 API 迁移与发布门槛；目标版本决定哪些 Android 行为变化适用，但不替代 FGS 资格和申报。 | 正文已打开并在[目标 API 专题](../target-api/target-api-level.zh-CN.md)摘要。 |
| 1 | [Manifest `<service>` element](https://developer.android.com/guide/topics/manifest/service-element) | Android Manifest 中的 service 配置和 `android:foregroundServiceType` 属性，是 FGS 声明的实现位置。 | 正文已打开；完整属性和组件交互后代未在本专题逐项归档。 |
| 1 | [JobScheduler API](https://developer.android.com/reference/android/app/job/JobScheduler) | 延后/约束式后台工作的调度 API 参考，用于评估任务是否可脱离持续 FGS。 | 正文已打开；只摘要相关调度边界，完整 API 后代未穷举。 |
| 1 | [Request special permissions](https://developer.android.com/training/permissions/requesting-special) | Android 特殊应用访问设置的申请流程；这是 FSI 等特殊权限的系统授权路径，不是 Play 自动批准。 | 正文已打开；更多系统设置与代码示例后代部分覆盖。 |

旧版 FGS Help 还保留“申报预计 2023 年 11 月开放”以及 2024/2025 年 FSI 过渡日期。这些是历史说明，不能作为当前开放状态或未来期限；地理围栏迁移期限以 2026 年预告和 Policy Deadlines 表的 **2027-01-27** 为准。正文的 32 项推荐文章另列在侧栏，不计入以上 24 个锚点。

### FGS Help 的 32 项“政策教育与应用要求”侧栏

2026-10-23 重新打开当前 [FGS Help 页面](https://support.google.com/googleplay/android-developer/answer/13392821?hl=en)，逐项核对其 32 个推荐帮助目标，并与已有逐 URL 审计记录及双语专题对应。**这是 Help Center 导航侧栏，不是 FGS 正文要求，也不表示每个目标页的全部后代已闭合。**“与本专题关系”列只说明为何从 FGS 页面导航到该主题；具体规则、访问边界和子链状态见所列专题及 URL 审计。Health Permissions FAQ `answer/12991134` 的本次侧栏重试返回 Internal Error；其 2026-10-22 全文核验记录仍保留，本次失败不作为页面内容发生变化的证据。

| # | 侧栏目标 | 与 FGS/本专题的关系 | 知识库交叉入口 |
| --- | --- | --- | --- |
| 1 | [Payments policy](https://support.google.com/googleplay/android-developer/answer/10281818?hl=en) | 付费、应用内购买与支付规则；FGS 本身不决定计费方式。 | [付款与订阅](../payments/payments-and-subscriptions.zh-CN.md)；[儿童与年龄限制](../age-restricted-child-safety/age-restricted-child-safety.zh-CN.md) |
| 2 | [Service Fee](https://support.google.com/googleplay/android-developer/answer/11131145?hl=en) | Play 服务费解释，与 FGS 技术和资格无直接关系。 | [付款与订阅](../payments/payments-and-subscriptions.zh-CN.md) |
| 3 | [Better Ads Experiences](https://support.google.com/googleplay/android-developer/answer/12271244?hl=en) | 广告体验要求；仅当 FGS 功能含广告时作为相邻产品规则核对。 | [广告与推广](../ads-and-advertising/ads-and-advertising.zh-CN.md) |
| 4 | [VpnService policy](https://support.google.com/googleplay/android-developer/answer/12564964?hl=en) | VPN 服务的用途、披露和申报；与 FGS 是不同的服务/权限政策。 | [敏感权限](../sensitive-permissions/sensitive-permissions.zh-CN.md) |
| 5 | [Moderation for incidental sexual content in UGC](https://support.google.com/googleplay/android-developer/answer/12923286?hl=en) | 用户生成内容审核要求，与 FGS 资格无直接关系。 | [用户生成内容与审核](../user-generated-content/user-generated-content.zh-CN.md) |
| 6 | [Account deletion](https://support.google.com/googleplay/android-developer/answer/13327111?hl=en) | 账号删除与数据生命周期规则；可影响 FGS 处理数据后的退出和删除体验。 | [账号删除](../account-deletion/account-deletion.zh-CN.md)；[User Data](../user-data/user-data.zh-CN.md) |
| 7 | [Foreground service and full-screen intent requirements](https://support.google.com/googleplay/android-developer/answer/13392821?hl=en) | 当前页面；FGS/FSI 政策说明。 | [本专题](../foreground-services-and-geofencing/foreground-services-and-geofencing.zh-CN.md) |
| 8 | [Spyware](https://support.google.com/googleplay/android-developer/answer/14745000?hl=en) | 监控、隐蔽收集和数据外传限制；对持续后台服务尤其相关。 | [间谍软件与数据外传](../spyware-and-data-exfiltration/spyware-and-data-exfiltration.zh-CN.md)；[移动垃圾软件](../mobile-unwanted-software/mobile-unwanted-software.zh-CN.md)；[敏感权限](../sensitive-permissions/sensitive-permissions.zh-CN.md) |
| 9 | [News and magazine apps](https://support.google.com/googleplay/android-developer/answer/10523915?hl=en) | 新闻/杂志类别与商店信息要求；仅适用于相应应用。 | [新闻与杂志](../news-and-magazines/news-and-magazines.zh-CN.md) |
| 10 | [COVID-19 guidelines](https://support.google.com/googleplay/android-developer/answer/9889712?hl=en) | 疫情时期的历史审核说明；应视为历史上下文，不当作当前通用 FGS 规则。 | 审核准备[审核准备](../app-review-preparation/app-review-preparation.zh-CN.md)；政策档案（快照：`../google-play-policy-archive.md`，未导入本仓库） |
| 11 | [Apps in specific countries or regions](https://support.google.com/googleplay/android-developer/answer/6223646?hl=en) | 国家/地区分发与当地要求；可能影响 FGS 功能上线地域。 | [国家/地区分发](../country-specific-distribution/country-specific-distribution.zh-CN.md) |
| 12 | [Apps that communicate government information](https://support.google.com/googleplay/android-developer/answer/9514050?hl=en) | 政府关联证明、来源披露及身份声明；与 FGS 无直接关系。 | [虚假陈述](../misrepresentation/misrepresentation.zh-CN.md)；创建应用与账号要求[应用设置](../play-console-app-setup/play-console-app-setup.zh-CN.md) |
| 13 | [Android Health Permissions FAQ](https://support.google.com/googleplay/android-developer/answer/12991134?hl=en) | 健康数据/身体传感器权限与健康功能要求；若 FGS 使用健康或身体传感器数据需并行核对。 | [健康应用与 Health Connect](../health-apps-and-health-connect/health-apps-and-health-connect.zh-CN.md)；[敏感权限](../sensitive-permissions/sensitive-permissions.zh-CN.md) |
| 14 | [Financial features declaration](https://support.google.com/googleplay/android-developer/answer/13849271?hl=en) | 金融功能申报；和 FGS 是独立政策域。 | [金融服务与贷款](../financial-services-and-loans/financial-services-and-loans.zh-CN.md)；[加密资产与 NFT](../crypto-assets-and-nfts/crypto-assets-and-nfts.zh-CN.md) |
| 15 | [Country/region allowances for gambling apps](https://support.google.com/googleplay/android-developer/answer/12256011?hl=en) | 真钱赌博产品的市场准入；仅对相应应用适用。 | [真钱赌博、游戏与竞赛](../real-money-gambling/real-money-gambling.zh-CN.md) |
| 16 | [Advertising ID](https://support.google.com/googleplay/android-developer/answer/6048248?hl=en) | 广告标识符使用、重置和声明；后台服务若处理广告标识符需遵循数据规则。 | [Advertising ID](../advertising-id/advertising-id.zh-CN.md)；[广告与推广](../ads-and-advertising/ads-and-advertising.zh-CN.md) |
| 17 | [System services](https://support.google.com/googleplay/android-developer/answer/12085265?hl=en) | 系统服务应用的资格/声明边界；FGS 类型与系统服务资格不能互相替代。 | 系统服务与预装软件（快照：`system-services-and-preinstalled-software.md`，未导入本仓库） |
| 18 | [Using SDKs safely and securely](https://support.google.com/googleplay/android-developer/answer/13326895?hl=en) | SDK 权限、数据流和安全责任；SDK 发起/维持的 FGS 也须纳入开发者审查。 | [第三方 SDK 要求](../sdk-requirements/sdk-requirements.zh-CN.md) |
| 19 | [On-device Android container apps](https://support.google.com/googleplay/android-developer/answer/13609005?hl=en) | Android 容器、第三方 APK 隔离与安全环境；与 FGS 是不同政策域。 | [设备与网络滥用](../device-and-network-abuse/device-and-network-abuse.zh-CN.md) |
| 20 | [Health app categories and additional information](https://support.google.com/googleplay/android-developer/answer/13996367?hl=en) | 健康应用分类、研究伦理和申报；在健康 FGS 场景下并行检查。 | [健康应用与 Health Connect](../health-apps-and-health-connect/health-apps-and-health-connect.zh-CN.md) |
| 21 | [AI-generated content policy](https://support.google.com/googleplay/android-developer/answer/14094294?hl=en) | AI 输出与用户报告/审核规则；若 FGS 支撑 AI 处理，仍须独立满足本政策。 | [AI 生成内容与安全实践](../ai-generated-content/ai-generated-content.zh-CN.md) |
| 22 | [EEA general conditions](https://support.google.com/googleplay/android-developer/answer/14659200?hl=en) | EEA 分发和合同条件；与 FGS 的技术/审核标准分开适用。 | EEA [通用访问条件](../eea-general-conditions/eea-general-conditions.zh-CN.md) |
| 23 | [Child Safety Standards](https://support.google.com/googleplay/android-developer/answer/14747720?hl=en) | 儿童安全组织标准与应用内保护；若 FGS 涉及儿童用户或相关数据须并行评估。 | [儿童安全与 DSA 透明度](../child-safety-dsa-transparency/child-safety-dsa-transparency.zh-CN.md)；[用户生成内容](../user-generated-content/user-generated-content.zh-CN.md) |
| 24 | [Sign-in details for app review](https://support.google.com/googleplay/android-developer/answer/15748846?hl=en) | 向审核人员提供登录/访问说明；审核时应让 FGS 功能可被正确触发和验证。 | 审核准备[审核准备](../app-review-preparation/app-review-preparation.zh-CN.md)；[预测市场试点](../prediction-market-pilot/prediction-market-pilot.zh-CN.md) |
| 25 | [Declaring a news or magazine app](https://support.google.com/googleplay/android-developer/answer/16189314?hl=en) | 新闻/杂志类别申报及相关字段；仅适用于相应应用。 | [新闻与杂志](../news-and-magazines/news-and-magazines.zh-CN.md) |
| 26 | [Crypto exchanges and software wallets](https://support.google.com/googleplay/android-developer/answer/16329703?hl=en) | 加密交易所/钱包地区资质与金融申报；与 FGS 独立。 | [加密资产与 NFT](../crypto-assets-and-nfts/crypto-assets-and-nfts.zh-CN.md)；[金融服务与贷款](../financial-services-and-loans/financial-services-and-loans.zh-CN.md) |
| 27 | [Flexibility for EEA app distribution](https://support.google.com/googleplay/android-developer/answer/16232690?hl=en) | EEA 的合同/分发条件变化；不等于替代计费或 FGS 政策豁免。 | EEA [通用访问条件](../eea-general-conditions/eea-general-conditions.zh-CN.md)；[付款与订阅](../payments/payments-and-subscriptions.zh-CN.md) |
| 28 | [AI safety best practices](https://support.google.com/googleplay/android-developer/answer/16353813?hl=en) | AI 安全最佳实践与外部资源；是风险控制指导，不是 FGS 审批依据。 | [AI 生成内容与安全实践](../ai-generated-content/ai-generated-content.zh-CN.md) |
| 29 | [Changes to EEA external offers](https://support.google.com/googleplay/android-developer/answer/16505463?hl=en) | EEA 外部优惠/链接计划更新；与 FGS 是独立规则。 | [付款与订阅](../payments/payments-and-subscriptions.zh-CN.md)；EEA [通用访问条件](../eea-general-conditions/eea-general-conditions.zh-CN.md) |
| 30 | [App-store bills in U.S. states](https://support.google.com/googleplay/android-developer/answer/16569691?hl=en) | 美国州级年龄保障法律与 Play 年龄信号工具说明；不是 FGS 要求。 | [儿童与年龄限制](../age-restricted-child-safety/age-restricted-child-safety.zh-CN.md) |
| 31 | [Apps with incidental dating or matchmaking](https://support.google.com/googleplay/android-developer/answer/16838200?hl=en) | 约会/匹配功能的未成年人访问限制；如应用兼有后台功能仍须单独检查。 | [儿童与年龄限制](../age-restricted-child-safety/age-restricted-child-safety.zh-CN.md) |
| 32 | [FGS/FSI policy preview](https://support.google.com/googleplay/android-developer/answer/16965181?hl=en) | FGS/FSI 预告；明确 2027-01-27 起地理围栏不再是获批 FGS 用例。 | [本专题](../foreground-services-and-geofencing/foreground-services-and-geofencing.zh-CN.md)；政策期限（快照：`../google-play-policy-operations.md`，未导入本仓库） |

本轮确认 32 项侧栏目标均已有单独 URL 访问状态及主题摘要记录；这只表示入口目标已有记录，不表示它们各自的所有正文链接、相关内容侧栏和更深后代都已递归完成。

### Android 权限概览的最佳实践子链

下表记录从权限概览页直接打开的高影响子页。此 Android 技术文档有其他权限类型、示例和设计链接；下表不是其全部后代的封闭清单。

| 子链目标 | 对 FGS/Play 权限审查的帮助 | 状态 |
| --- | --- | --- |
| [Minimize your permission requests](https://developer.android.com/privacy-and-security/minimize-permission-requests) | 能用粗略位置、Location Button、Photo/Contact Picker、SAF、专用 API 或 Intent 完成时，不要索取更广权限；解释拒绝后的降级。 | 全文已打开；主要替代方案已整理，API 示例后代部分覆盖。 |
| [Declare app permissions](https://developer.android.com/training/permissions/declaring) | 只在 Manifest 声明功能真正需要的权限；硬件并非必需时标为可选并处理降级。 | 正文已打开；Manifest 语法与硬件可选性已核对。 |
| [Request runtime permissions](https://developer.android.com/training/permissions/requesting) | 在用户进入具体功能时请求；解释用途、重新检查授权，并在拒绝或撤销时优雅降级。 | 正文已打开；实现示例和 API 后代部分覆盖。 |
| [Restrict interactions with other apps](https://developer.android.com/training/permissions/restrict-interactions) | 配置 Activity、Service、Provider、Receiver 的跨应用访问边界；与“本应用申请设备权限”是不同问题。 | 正文已打开；组件示例和代码后代部分覆盖。 |
| [App permissions best practices](https://developer.android.com/training/permissions/usage-notes) | 仅在具体功能需要时请求，不在启动时一次性索取；请求前后解释、处理设置中撤销、盘点 SDK 权限并测试授权/拒绝组合。 | 正文已打开（2026-10-16 更新）；默认处理器、设计和测试子链仍部分覆盖。 |
| [Request special permissions](https://developer.android.com/training/permissions/requesting-special) | 对系统设置控制的特殊权限，引导用户到对应设置并处理未授权情形；与 Play 对 FSI 核心用途的审核分开。 | 正文已打开；深层系统流程部分覆盖。 |
| [Manifest.permission API reference](https://developer.android.com/reference/android/Manifest.permission) | 查阅具体权限常量、保护级别和版本信息；API 定义不等于政策资格。 | 大型 API 参考已打开；未逐成员归档。 |
| [Android permissions samples](https://github.com/android/platform-samples/tree/main/samples/privacy/permissions) | 官方示例仓库入口，可辅助理解权限工作流；示例代码不是 Play 政策。 | 仓库目录已打开；GitHub 动态文件树和每个示例未全部读取。 |

本页是双语结构化改写摘要，不是政策全文副本；技术 API 文档更新更频繁，改动代码前应回到 Android 文档和 Play Console 当前表单复核。关联页面：[后台位置访问](../background-location/background-location.zh-CN.md)、[敏感权限与 API](../sensitive-permissions/sensitive-permissions.zh-CN.md)、[目标 API 迁移](../target-api/target-api-level.zh-CN.md)、[联系人与前台位置最小范围](../contacts-location-permissions/contacts-location-permissions.zh-CN.md)。
