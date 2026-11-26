---
id: google-play.sensitive-permissions
platform: google-play
language: zh-CN
authority: normative
status: current
kb_checked_at: 2026-10-24
review_due: 2027-01-24
regions: [global]
topics: [permissions, sensitive-data, privacy, declaration, android-api]
snapshot_id: play.sensitive-permissions
snapshot_package: "GooglePlay-KnowledgeBase-2026-10-24-review.zip"
coverage_status: "detailed-summary"
source_url: "https://support.google.com/googleplay/android-developer/answer/16558241?hl=en"
source_url_zh: "https://support.google.com/googleplay/android-developer/answer/16558241?hl=zh-CN"
effective_date: "mixed-current-and-2027-01-27"
---

# 敏感信息权限与 API

> **导入说明（Google batch 2）。** 本页正文取自 2026-10-24 Google Play 知识库快照里已经分开的中文改写（`play.sensitive-permissions`，核对日 2026-10-24），不是 Google 已发布中文页面的逐字文本。英文官方页面是效力来源。`kb_checked_at` 使用快照源文件记录的核对日；本次导入没有重新打开线上官方页面。文中“本知识库”“本库”“本地专题”描述的是该快照知识库的覆盖范围，不是本仓库已经导入的页面清单。快照里指向尚未导入本仓库的专题、链接图、台账或 CSV 的相对链接，已改为文字提及；指向 Google batch 1 或本批七个专题的相对链接已改到本仓库路径。快照记录本轮已重新打开英文现行综合页面及其政策预览。现行 `hl=zh-CN` 页面无法通过抓取器读取，因此本中文页是按英文官方正文和已读预览作的结构化翻译，不是对中文官方网页的独立逐段校验。抓取失败不表示政策已经变更。官方页面同时展示已生效规则和 2027-01-27 生效的变更预告，两类日期必须分开。本页 Play 政策条款的证据等级是 `normative`。Android API、闹钟、VPN 与无障碍实现说明是 implementation note，不能单独证明 Play 分发资格。

**核对日期：2026-10-24。** 本页按当前综合权限政策的章节整理。官方页面同时展示已生效规则和 2027-01-27 生效的变更预告，需按日期区分。

**来源核验：** 本轮已重新打开英文现行综合页面和其链接的[政策预览](https://support.google.com/googleplay/android-developer/answer/16909972?hl=en)。现行页面不是旧版别名；旧权限入口会重定向到此页。`zh-CN` 版本的现行页面本轮无法通过抓取器读取，因此本中文专题是按英文官方正文和已读预览作结构化翻译，并非对该中文网页的独立逐段校验。

## 通用规则

只有为商店详情页已推广、当前已实现的核心功能所必需，才可请求访问敏感信息的权限或 API。不得为未实现、未披露或不允许的功能申请。应在实际使用情境中逐步请求，仅将数据用于用户已同意的用途；如果之后增加用途，应另行披露并取得用户肯定同意。权限访问的数据属于个人和敏感用户数据，必须同时遵守[用户数据政策](../user-data/user-data.zh-CN.md)。

受限权限还要求尊重用户拒绝，不得操纵或强迫用户授权非关键用途，并尽合理努力提供可行替代方案。违规使用权限规避平台安全/隐私控制或滥用提升权限的行为禁止。

## 按权限/数据类型的专项要求

| 专项 | 规则要点 |
| --- | --- |
| 照片与视频 | Android 13 / API 33+ 应用只有在系统 Photo Picker 等选择器不足以实现核心功能时，才可申请 READ_MEDIA_IMAGES / READ_MEDIA_VIDEO；仍申请时须在 Play Console 申报必要性及为何选择器不够。 |
| SMS 与通话记录 | 应用须实际注册为默认 SMS、电话或 Assistant 处理器，且在提示权限前已成为默认处理器；失去默认身份后立即停止使用。仅限商店说明中明确宣传、缺少数据就会失去主要用途的核心功能；需申报。禁止广告等其他用途，也禁止用其他权限/API/第三方来源绕道推导 SMS/Call Log 数据。应优先评估 SMS Retriever 等替代方案。详见 [SMS 与通话记录权限专题](../sms-call-log/sms-call-log.zh-CN.md)。 |
| 位置 | 请求最小范围（粗略优先于精确、前台优先于后台），且使用情境应使用户合理预期需要该精度。数据不再为当前功能所需时即停止访问；不得只为广告或分析请求。后台位置限于对用户有益并与核心功能相关的功能，通常需要有力理由及 Console 申报。前台服务使用前台位置须由应用内用户操作启动，并在该操作完成后立即停止。儿童定向应用另须符合 Families 政策。 |
| 所有文件访问 | Android 11 / API 30+ 的广泛存储访问属于高风险；仅核心用户功能确需时才可申请 MANAGE_EXTERNAL_STORAGE，须经审查并引导用户到“特殊应用权限”设置。优先 Storage Access Framework、MediaStore 等更窄方案；不能为第三方需求申请，也不能以该权限代替用户选择单个文件。 |
| 已安装应用可见性 | 已安装应用清单是敏感数据。优先使用定向、有限的包可见性声明；QUERY_ALL_PACKAGES 仅限核心功能确需与任意已安装应用互操作/启动/搜索的情况，并须申报和说明。不得通过其他方式规避广泛可见性限制；不得出售或为广告/分析变现而分享清单数据。 |
| Accessibility API | 服务必须符合 API 设计目的，不得未经授权更改系统设置、阻止用户禁用/卸载、绕过安全/隐私控制、操纵界面欺骗用户、录制远程通话音频，或自主规划/执行决策。只有核心功能直接帮助残障用户的应用可声明 isAccessibilityTool=true 并适用相应披露例外；其他使用须 Console 申报、醒目披露和肯定同意。商店页须准确描述用途；能用更窄 API 时应优先替代。 |
| 请求安装应用包 | REQUEST_INSTALL_PACKAGES 仅用于核心功能包含发送/接收应用包并让用户主动发起安装的应用，例如浏览/搜索、带附件通信、文件管理、企业设备管理、备份恢复、设备迁移或穿戴设备配套。不得用于自更新、偷偷安装、改变自身功能或无用户明确动作地安装；核心功能和权限用途须在商店说明及申报中明确。 |
| 身体传感器 | 心率、血氧、皮肤温度等数据属于敏感数据，受 User Data 和 Health apps 政策约束。Android 16 起，面向 Android 16+ 的应用应由 BODY_SENSORS 迁移到更细粒度 health 权限，并只申请直接支持核心用户功能的必要类型。 |
| Health Connect | 仅适用于获准且对用户健康/健身有益的用例，如健身健康、奖励、教练、企业健康、医疗护理、健康研究和游戏；访问范围须与用户可见功能相关并最小化。需申报并解释用途，完整披露身份、数据类型、用途/分享、管理删除方式和安全措施。未经明确同意不得对外分享，且禁止广告、数据经纪、信用评估等用途。不得用于生命关键/高风险系统、仅面向儿童的应用或无可识别界面的无头应用。适用 HIPAA/GDPR 等法律时还须满足其要求。 |
| VPN Service | 仅当 VPN 是应用核心功能，或符合家长控制、企业管理、设备安全、应用使用追踪、网络工具/远程访问、浏览器、运营商等列明资格时使用。须在商店页说明、加密设备至 VPN 端点的流量，并完成 Play Console 声明。不得为了变现重定向或操纵其他应用流量；访问/收集个人敏感数据须在应用内醒目单独披露、说明用途/共享并取得肯定同意。详见下方申报说明及 [VpnService 政策解释](https://support.google.com/googleplay/android-developer/answer/12564964?hl=en)。 |
| 间谍软件与 SDK 数据外传 | 仅能访问、收集、使用、分享与用户预期或同意的合规功能相关的数据。SDK 传输与功能无关的录音、窃取其他应用通知、后台外传联系人/非应用自有文件/邮件/通话或短信记录/其他应用私有目录数据，均是官方列举的风险例子；贷款/预算应用外传非金融或个人短信历史亦被点名。见间谍软件专题（[间谍软件、数据外传与监控类应用](../spyware-and-data-exfiltration/spyware-and-data-exfiltration.zh-CN.md)）。 |
| 精确闹钟 | Android 13/API 33+ 且 target API 33+ 时可选 `USE_EXACT_ALARM` 或 `SCHEDULE_EXACT_ALARM`。Play 现行政策将 `USE_EXACT_ALARM` 列为受限权限，仅当核心、面向用户的功能确需精准时刻（如闹钟/计时器，或显示事件通知的日历）才符合资格并须申报/审核；其他用例可评估用户授予的 `SCHEDULE_EXACT_ALARM`，但它不是 Play 审批或后台位置豁免。Android [闹钟指南](https://developer.android.com/develop/background-work/services/alarms)关于“Play 政策即将出台”的文字已滞后，以[现行 Play 专项条款](https://support.google.com/googleplay/android-developer/answer/16558241?hl=en#exact-alarm-permission)为准。详细系统行为及链接审计见下文。 |
| 全屏意图 | Android 14 / target API 34+ 的 USE_FULL_SCREEN_INTENT 是特殊访问权限。只有核心功能为闹钟或电话/视频通话才自动授予；其他用途须由用户明确授权并说明原因，且须经 Play 审查。不得以广告或低优先级通知打扰用户、干扰设备或其他应用。 |
| Age Signals API | 只能将 API 提供的年龄和家长同意信息用于接收该数据的应用内履行法律/监管义务、提供适龄体验。禁止用于广告/营销、个性化、分析、用户画像、商业智能或对外转移（法律强制要求除外）。 |

## 精确闹钟：Android 系统行为与 Play 政策

Android 的授权模型回答“系统是否允许设置闹钟”；Google Play 的政策回答“应用是否可在 Play 分发此权限以及需提交何种申报”。二者不能互相替代。

| Android 版本、设备与 target SDK | 系统行为 | Play 政策关系 |
| --- | --- | --- |
| Android 11/API 30 及更早 | 系统尚无 Android 12 引入的 `SCHEDULE_EXACT_ALARM` 特殊应用访问模型；Android 4.4/API 19 起重复闹钟一律非精确，Android 6/API 23 起 Doze 会延迟一般闹钟。 | Play 的 `USE_EXACT_ALARM` 受限权限规则仍按应用实际提交的 Manifest/target SDK 评估；旧系统不改变 Play 对发布包的政策要求。 |
| Android 12/API 31+，应用 target API 31+ | 精确闹钟需声明 `SCHEDULE_EXACT_ALARM` 特殊应用访问；未获授权而调用需该权限的精确 API 会触发 `SecurityException`。在 Android 13+ 且 target API 33+ 时还可选择 `USE_EXACT_ALARM`。 | Android 特殊访问获批并不代表 Play 允许 `USE_EXACT_ALARM`；Play 资格单独审查。 |
| Android 13/API 33+，应用 target API 33+ | `USE_EXACT_ALARM` 安装时自动授予，用户不能撤销；`SCHEDULE_EXACT_ALARM` 由用户在“闹钟与提醒”特殊访问设置中授予。新安装不应假定 `SCHEDULE_EXACT_ALARM` 已预授予；检查实际状态。 | `USE_EXACT_ALARM` 是 Play 受限权限，当前许可限于核心用户功能确需精确时刻的闹钟/计时器或日历事件提醒，且需 Play Console 声明并接受审核。不符合这些核心用例时，Play 当前条款建议评估 `SCHEDULE_EXACT_ALARM`。 |
| Android 14/API 34+，应用 target API 33+ | 大多数新安装默认不授予 `SCHEDULE_EXACT_ALARM`；从备份恢复到 Android 14 也保持拒绝。若应用在设备升级到 Android 14 前已获该权限，则升级时预授予。Android 13+ 日历/闹钟应用应评估 `USE_EXACT_ALARM`。 | Android 系统默认授权状态不会放宽 Play 对 `USE_EXACT_ALARM` 的用途限制。Play 综合页还要求提交声明以说明闹钟功能；通用声明帮助页说明，表单会按应用包实际请求且尚未声明的权限显示。应在本应用 Console 核对实际表单，不能推断 `SCHEDULE_EXACT_ALARM` 自动获得 Play 批准。 |
| 撤销与生命周期 | 用户或系统均可撤销 `SCHEDULE_EXACT_ALARM`。用 `AlarmManager.canScheduleExactAlarms()` 检查；撤销时应用进程停止，所有未来的精确闹钟被取消。获批广播到达后仍须重新检查授权状态并按应用状态重排闹钟。以 `OnAlarmListener` 设置的特定闹钟不需要 `SCHEDULE_EXACT_ALARM`。 | 用户拒绝或撤销必须得到尊重；使用较宽松调度或降级体验，不要诱导用户授权。 |

### 非精确替代、后台任务与电量

- Android 4.4/API 19 起，所有重复闹钟均为非精确闹钟；系统可合并它们以减少唤醒。`set()` 等非精确闹钟不会早于触发时刻，但会延后；面向 Android 12/API 31+ 的应用，`setWindow()` 最小时间窗为 10 分钟，通常会裁切到该下限。电池节省限制或 Doze 会继续延迟闹钟。
- 多数可延期任务用非精确闹钟。较长、可延迟或周期性后台工作用 WorkManager/JobScheduler；闹钟接收器可以提交作业。WorkManager 周期工作有至少 15 分钟的重复间隔且允许弹性窗口，不保证精确时刻。短时、只需在进程存活期间完成的计时优先考虑 `Handler` 等进程内机制。
- 精确闹钟不易批处理，会增加电量和系统资源消耗。普通 `setExact()` 不能保证在所有省电状态下按点触发；只有确需在空闲/低功耗时段准点执行的用户请求才评估 `setExactAndAllowWhileIdle()`；`setAlarmClock()` 用于用户可见的真正闹钟，必要时系统可退出低功耗模式交付。精确性不应被当成后台运行保证。

### Android 闹钟指南直接链接审计

已打开 Android [Schedule alarms 指南](https://developer.android.com/develop/background-work/services/alarms)正文（页面标注最后更新 2026-10-21 UTC），并尝试正文中的直接链接。API 方法链接多次指向同一 API 页面，以下按唯一目标合并；导航栏/页脚链接不作为正文子目标。

| 直接目标 URL | 访问状态与关系 |
| --- | --- |
| https://developer.android.com/reference/android/app/AlarmManager | 可读。闹钟 API、`set`、`setExact`、`setAndAllowWhileIdle`、`setAlarmClock`、重复调度和取消方法的同一 API 参考页。 |
| https://developer.android.com/reference/android/app/job/JobScheduler | 可读。工作调度 API；与闹钟接收器提交较长后台工作相关。 |
| https://developer.android.com/develop/background-work/background-tasks/persistent | 可读。WorkManager/后台任务调度概览。 |
| https://developer.android.com/develop/background-work/background-tasks/persistent/getting-started/define-work | 可读。WorkManager 工作定义与周期调度细节。 |
| https://developer.android.com/reference/android/os/Handler | 可读。应用进程存活期间的计时替代。 |
| https://developer.android.com/reference/java/util/Timer | 可读。进程内计时参考。 |
| https://developer.android.com/reference/java/lang/Thread | 可读。进程内线程参考。 |
| https://developer.android.com/reference/android/os/SystemClock | 可读。`Handler` 定时所用系统 uptime 与 real-time 时钟参考。 |
| https://developer.android.com/training/monitoring-device-state/doze-standby | 可读。Doze 和 App Standby 电量限制。 |
| https://developer.android.com/about/versions/pie/power | 可读。省电模式与电源管理。 |
| https://developer.android.com/reference/android/Manifest.permission | 可读。`SCHEDULE_EXACT_ALARM`、`USE_EXACT_ALARM` 与 `RECEIVE_BOOT_COMPLETED` 的 Manifest 权限参考。 |
| https://developer.android.com/reference/java/lang/SecurityException | 可读。缺少所需闹钟访问时的异常参考。 |
| https://developer.android.com/reference/android/app/AlarmManager.OnAlarmListener | 可读。`OnAlarmListener` 监听器 API。 |
| https://developer.android.com/develop/background-work/background-tasks/broadcasts | 可读。广播接收器概览。 |
| https://developer.android.com/reference/android/content/Intent | 可读。`ACTION_BOOT_COMPLETED` 等 Intent 常量/API。 |
| https://developer.android.com/reference/android/provider/Settings | 可读。闹钟特殊访问设置 Intent/API。 |
| https://developer.android.com/reference/android/app/PendingIntent | 可读。闹钟触发操作和取消所用 PendingIntent API。 |
| https://developer.android.com/reference/android/content/BroadcastReceiver | 可读。闹钟及开机广播接收器 API。 |
| https://developer.android.com/develop/background-work/services/fgs/restrictions-bg-start | 可读。精确闹钟触发用户请求操作是后台启动前台服务限制的例外；同页另述 while-in-use 位置仍受限，不能把此例外当作后台定位授权。 |
| https://support.google.com/googleplay/android-developer/answer/12253906 | 可读；本次点击重定向至 https://support.google.com/googleplay/android-developer/table/12921780?visit_id=639281946821696112-2087406460&rd=2（规范化页面：https://support.google.com/googleplay/android-developer/table/12921780?hl=en）。目标是通用 Policy Deadlines 页面；它不支撑 Android 指南所称“Play 政策即将出台”的当前资格判断。请用上方现行综合政策条款判断。 |
| https://github.com/android/snippets/blob/7d9def909f18781bd1cacfe46e68b27c6df1d124/backgroundwork/src/main/java/com/example/snippets/backgroundwork/Alarms.kt | 无法读取：正文代码示例链接多次尝试均返回 `Cache miss`。只记录链接目标，不依据未读代码作推断。 |

正文内链接到同一指南章节（如 exact/inexact 用例、类型选择）的锚点回到已打开的主页面。设置页说明图的图片请求返回 Internal Error，工具未提供其图片 URL。当前 Play 条款见[Permissions and APIs that Access Sensitive Information → Exact Alarm Permission](https://support.google.com/googleplay/android-developer/answer/16558241?hl=en#exact-alarm-permission)；Play Console 的[权限声明帮助页](https://support.google.com/googleplay/android-developer/answer/9214102?hl=en)说明表单会按应用包内未声明的权限触发。Android 指南仍写“upcoming Google Play policy”，这是滞后措辞，不能覆盖现行 Play 规则。

### 特殊应用访问请求指南及精确闹钟后代

2026-10-24 重开 Android [Request special permissions](https://developer.android.com/training/permissions/requesting-special)（页面标注 2026-10-16 更新），并沿其精确闹钟示例扩展到 `AlarmManager`、`Settings`、`Manifest.permission` 和 `PowerManager`。正文中通向 6 个不同外部目标的政策相关链接均已打开；权限概览中的同页锚点、上一页/下一页导航和站点页脚不计作新政策目标。

平台指南的可执行顺序是：Manifest 只声明确实需要的特殊权限；把权限和用户明确发起的功能动作绑定；等用户进入该动作后再解释权限用途、提供返回/取消选项并跳转到系统 Special app access；从 Settings 返回时在 `onResume()` 重新检查。每次执行受保护操作之前都要再次检查权限。拒绝后须优雅降级。与普通运行时权限不同，特殊访问由用户在系统设置页授予，不出现普通权限弹窗；Android 平台流程本身不等于 Play 允许该用途。

| 特殊权限指南的直接目标 | 关系与已核实内容 |
| --- | --- |
| [Permissions on Android](https://developer.android.com/guide/topics/permissions/overview) | 解释安装时、运行时和特殊权限类别；建议先找无需权限的方案，只请求当前动作所需的最小集合，并盘点依赖库引入的权限。页内还链接最小化请求、Manifest 声明、运行时请求、权限 API 和示例仓库；API 目录与全部示例后代未穷尽。 |
| [Declare app permissions](https://developer.android.com/training/permissions/declaring) | 用 Manifest 的 `<uses-permission>` 声明确需权限；指南提醒只添加有用户价值且必要的权限。技术声明不代表 Play 资格。硬件特征、样例和更深 Manifest/API 后代仍部分覆盖。 |
| [Request runtime permissions](https://developer.android.com/training/permissions/requesting) | 与特殊权限指南中“等用户触发功能”和“拒绝后降级”的链接共用此页面。它描述运行时弹窗流程；特殊应用访问则跳转 Settings，返回后复查。权限模型和示例树此前已部分审阅。 |
| [Manifest.permission](https://developer.android.com/reference/android/Manifest.permission) | `SCHEDULE_EXACT_ALARM` 自 API 31 提供，可被用户或系统撤销；面向 API 33+ 且核心功能依赖精确闹钟时可评估 `USE_EXACT_ALARM`。该 API 页要求同一设备只请求其中一种，并说明 `USE_EXACT_ALARM` 是强权限、应用商店可能审查。该 6,738 行权限目录仅抽查相关常量。 |
| [`AlarmManager.canScheduleExactAlarms()`](https://developer.android.com/reference/android/app/AlarmManager#canScheduleExactAlarms) | API 31 起可用于检查精确闹钟可用性；对 target API 31+，系统文档列出 `SCHEDULE_EXACT_ALARM` 或设备电量豁免作为可调度条件。API 同页列出 `setExact`、`setExactAndAllowWhileIdle`、`setAlarmClock` 及权限状态广播。用户撤销 SCHEDULE 后，这些已排闹钟会被删除；授予广播到达后仍需重查，再安排真正必要的闹钟。全部 `AlarmManager` 成员未穷尽。 |
| [`Environment.isExternalStorageManager()`](https://developer.android.com/reference/android/os/Environment#isExternalStorageManager) | 特殊权限指南以 `MANAGE_EXTERNAL_STORAGE` 展示“每种特殊权限使用自己的检查方法”；这是 All files 分支示例，与精确闹钟无关。详情见[All files 子链审计](#所有文件访问正文子链接与关键后代)。 |

**从 `AlarmManager` 再延伸的 API 后代：** 精确闹钟检查方法的 “See also” 链接还指向以下两个 API 页面；它们是 `AlarmManager` 的孙链接，不属于 Request special permissions 页的 6 个直接外部目标。

| `AlarmManager` 后代 | 与精确闹钟的关系 |
| --- | --- |
| [`Settings.ACTION_REQUEST_SCHEDULE_EXACT_ALARM`](https://developer.android.com/reference/android/provider/Settings#ACTION_REQUEST_SCHEDULE_EXACT_ALARM) | API 31 起打开对应 Settings 页面；可用 package URI 直接定位应用，提供 URI 时 Activity result 区分授予或取消。它是系统授权入口，不是 Play 审批入口。 |
| [`PowerManager.isIgnoringBatteryOptimizations()`](https://developer.android.com/reference/android/os/PowerManager#isIgnoringBatteryOptimizations) | `AlarmManager` 的 “See also” 链接，返回应用是否位于设备电量优化豁免名单；这是电量机制参考，不能与 `USE_EXACT_ALARM` 的 Play 用途资格混为一谈。大型 API 其他成员未审。 |

**Play 边界：** 当前 [Exact Alarm Permission](https://support.google.com/googleplay/android-developer/answer/16558241?hl=en#exact-alarm-permission) 将 `USE_EXACT_ALARM` 限于核心、面向用户且确实要求准点执行的闹钟/计时器应用，或显示事件通知的日历应用；要求 Play Console 声明并接受审核。未满足这些核心用途时，政策建议评估用户授予的 `SCHEDULE_EXACT_ALARM`。Android 权限 API、系统设置授权、后台启动例外或电量豁免都不能替代该 Play 审查。Android 闹钟指南中的 “upcoming Google Play policy” 与现行条款冲突，应以后者为准。

## Restricted Permissions 帮助页的直接目标

[Understanding Restricted Permissions with minimum scope alternatives](https://support.google.com/googleplay/android-developer/answer/16935362?hl=en) 的正文和 12 项“Use of app permissions and APIs”相关帮助链接已于 2026-10-22 逐项核验。下表补充其中 5 个曾缺少单独访问记录的专项页面；Android 实现指南和各页更深 API/示例子链仍在递归台账中另行跟踪。

| 直接目标页 | 适用范围、申报与例外 | 与最小权限母页的关系 |
| --- | --- | --- |
| [All files access (`MANAGE_EXTERNAL_STORAGE`)](https://support.google.com/googleplay/android-developer/answer/10467955?hl=en) | 仅 Android 11/API 30+ 应用适用；仅限核心功能需要广泛访问的文件管理、备份恢复、反病毒、文档管理、设备搜索、加密/锁定和设备迁移等用途，并须在 Console 证明 SAF/MediaStore 不足。媒体访问和用户逐项选择文件不得用该权限。运营商/OEM 与 Managed Google Play 私有应用有列明例外。 | 先用 MediaStore 访问媒体，逐项导入/处理走 Storage Access Framework；改变用途须更新权限声明。 |
| [Broad package visibility (`QUERY_ALL_PACKAGES`)](https://support.google.com/googleplay/android-developer/answer/10158779?hl=en) | Android 11/API 30+ 上获取已安装应用清单属于敏感数据；仅设备搜索、反病毒、文件管理器、浏览器等核心用途可能获批。临时例外涉及合规地理围栏所需真钱赌博，以及受监管金融交易的安全用途；个人贷款/信贷不适用金融例外。不得用于非核心用途、出售、广告/分析变现或可由较窄查询完成的任务；P2P 分享须本身是核心用途才可能符合。 | 优先定向 `<queries>`/包可见性过滤；仍申请时须声明并遵守 User Data 披露同意要求。 |
| [Request Install Packages (`REQUEST_INSTALL_PACKAGES`)](https://support.google.com/googleplay/android-developer/answer/12085295?hl=en) | 仅当核心功能包含发送/接收安装包并让用户主动安装时适用；列明用途包括网页浏览/搜索、带附件通信、文件分享/传输/管理、企业设备管理、备份恢复及设备迁移。不得用于非核心 P2P、静默安装或绕过 Google Play 自我更新；用途变化须更新声明。页面列出的 2022-07-11 是历史生效日。 | 需要声明和用户数据披露；使用者应评估 `Intent.ACTION_INSTALL_PACKAGE`/`PackageInstaller` 的实际流程，避免把技术能力当成 Play 资格。 |
| [AccessibilityService API](https://support.google.com/googleplay/android-developer/answer/10964491?hl=en) | 只有主要目的在于帮助残障用户的工具才可声明 `isAccessibilityTool=true`；一般助手、反病毒、自动化、监控、清理器、密码管理器和启动器不因此成为无障碍工具。其他应用须在正常使用流程中单独显著披露数据和用途并取得肯定同意，提交声明和视频。自动化只能执行边界清楚的确定性脚本，不得自行规划/决定/执行动作；已验证无障碍工具在核心助残功能范围内除外。 | `isAccessibilityTool` 不是一般应用免申报标志；声明视频应展示打开应用、披露、同意和拒绝路径、授权流程及核心功能。该旧帮助页仍含 2021 年 Android 12/target API 31 申报起始文字，不能将其当作现行触发条件；以当前综合政策、现行表单及账号 Console 状态核实。 |
| [Sensitive JavaScript Interface vulnerability remediation](https://support.google.com/googleplay/android-developer/answer/10768383?hl=en) | 属于逐应用安全整改通知：在 Play Console/邮件指定期限前修复并重新提交，逾期未修复版本可能下架；公开页不能确认账号收到的包名和期限。整改可移除不可信 WebView 的 JavaScript bridge、在加载不可信内容前移除 bridge，或避免暴露敏感功能并限制只加载自有可信 URL。 | SDK/运行时 JavaScript 也可能触发 User Data 或 Malware 风险；权限/短信/无障碍等敏感 API 不应暴露给不可信网页脚本。 |

这五个帮助页均已打开正文。JavaScript 接口整改页的政策相关直链和关键 Android 后代见下节；其余专项页的 Android API、Manifest 与示例链接仍未全部打开。各页完整 URL 和人工访问状态见来源页审计表（快照：`../source-page-audit.csv`，未导入本仓库）与递归链接图（快照：`../google-play-policy-link-graph.md`，未导入本仓库）第 4.1/4.2 节。

### AccessibilityService 政策页 → Android 实现与无障碍最佳实践子链

2026-10-24 重开 [Use of the AccessibilityService API](https://support.google.com/googleplay/android-developer/answer/10964491?hl=en)，其正文 10 次链接（Help 正文 ID 3–12）均已重新尝试：7 次目标正文可读或可打开，`isAccessibilityTool`、`AccessibilityService_description` 和 `AccessibilityService_htmlDescription` 三个锚点指向同一个超过 4 MiB 的 `R.styleable` API 大页，抓取均被大小上限拒绝。通过官方 `AccessibilityServiceInfo` API 参考搜索核验：`isAccessibilityTool` 表示服务是否用于帮助残障用户；description/htmlDescription 是系统设置中的服务描述，不能代替应用内显著披露。正文直链[权限声明帮助页](https://support.google.com/googleplay/android-developer/answer/9214102?hl=en)已打开：申报需说明核心功能、审核步骤和视频；受限内容用测试凭据。开放、封闭或内部测试轨道中活跃且需申报权限的 App Bundle，可能阻止发布所有应用改动（包括商店资料、定价和分发），直到补交声明或移除权限；可停用不用且不合规的测试轨道。多 APK 例外仅适用于无法再修改且请求 SMS/Call Log 的旧 APK 变体，其他不合规变体须停用。滚动发布后可能经历数周扩展审核；未经批准不能直接用 Publishing API 发布，初次及新增权限声明须走 Console UI。详情及该帮助页的 14 次正文链接审计见[权限声明专题](../permissions-declaration/permissions-declaration.zh-CN.md)。这些流程说明不取代 AccessibilityService 资格判断或账号内实际表单。12 项权限 Help 侧栏与登录式实际申报入口另行区分。一般 app 的无障碍体验应通过标准 Android/Compose 可访问性 API 构建，不能为了自动化便利而扩大 AccessibilityService 的数据与控制范围。

此 Help 页仍显示 2021 年 Android 12 / target API 31 的声明起始时间。那是历史说明，不应当作当前 Android 版本触发规则；当前适用义务要按[现行综合敏感权限政策](https://support.google.com/googleplay/android-developer/answer/16558241?hl=en)、Play Console 实际申报表单和账号通知判断。现行综合页还明确禁止未经许可更改系统设置或阻止用户停用/卸载、绕过 Android 安全/隐私控制和通知、以欺骗方式操纵界面，以及用该 API 录制远程通话音频或自主发起/规划/执行操作与决策；商店页须记录 Accessibility API 用途，能用更窄 API 时应优先替代。已验证无障碍工具仅在核心助残功能范围内享有政策明确的特定例外；仍须遵守 User Data、Malware、Device and Network Abuse、Deceptive Behavior 等其他政策。

| 直接目标/后代 | 内容摘要及与 Play 的关系 | 审计范围 |
| --- | --- | --- |
| Android [Create an accessibility service](https://developer.android.com/guide/topics/ui/accessibility/service) 与 [Views 专用旧版指南](https://developer.android.com/guide/topics/ui/accessibility/views/service) | 新指南明确 AccessibilityService 是专门的助残工具，不是让普通 app 自身 UI 可访问的通用办法；通常应给 TalkBack 等既有服务提供语义。服务只能由系统管理、用户在系统设置中显式启用；Manifest 需声明 Service、专用 intent 和 `BIND_ACCESSIBILITY_SERVICE`。配置应只接收必要事件/包；只有确需检查屏幕内容时才启用 `canRetrieveWindowContent`，避免无差别 `typeAllMask`。 | 新指南正文完整打开，最后更新 2026-04-17；Views 页 939 行完整打开，同日更新。它们是 Android 实现约束，不等同于 Play 的资格决定。 |
| [AccessibilityService](https://developer.android.com/reference/kotlin/android/accessibilityservice/AccessibilityService)、[`AccessibilityServiceInfo`](https://developer.android.com/reference/kotlin/android/accessibilityservice/AccessibilityServiceInfo)、[Manifest.permission](https://developer.android.com/reference/kotlin/android/Manifest.permission)、[`AccessibilityNodeInfo`](https://developer.android.com/reference/kotlin/android/view/accessibility/AccessibilityNodeInfo) API | API 说明服务通过事件/节点树读取界面并代用户执行动作；`isAccessibilityTool` 描述服务的助残用途，不是普通应用自行声明便可获得 Play 豁免的标记。节点数据可能包含界面文字/状态；须把读取、动作、事件范围限制在核心助残功能需要内。 | API 页分别为 4,000–6,700 行级大型参考；核对服务生命周期、`isAccessibilityTool`、BIND 权限及相关节点/事件概念，不声称逐成员归档。 |
| `AccessibilityService_description` / `htmlDescription` 属性 → [`R.styleable`](https://developer.android.com/reference/android/R.styleable) | 系统设置里的服务说明可描述用途、可用性或限制；Google Play Help 明确说这种系统服务说明不能替代 app 内显著披露。 | `R.styleable` 页面超过读取器 4 MiB 上限，正文未打开；属性含义用 `AccessibilityServiceInfo` 摘要和官方搜索片段交叉确认，列为部分可读。Play Console 表单短链未暴露公开目标，账号表单仍须在 Console 核实。 |
| [Accessibility in Jetpack Compose](https://developer.android.com/develop/ui/compose/accessibility) → [API defaults](https://developer.android.com/develop/ui/compose/accessibility/api-defaults)、[Semantics](https://developer.android.com/develop/ui/compose/accessibility/semantics)、[traversal order](https://developer.android.com/develop/ui/compose/accessibility/traversal)、[scalable content](https://developer.android.com/develop/ui/compose/accessibility/scalable-content)、[merging/clearing](https://developer.android.com/develop/ui/compose/accessibility/merging-clearing)、[inspect/debug](https://developer.android.com/develop/ui/compose/accessibility/inspect-debug)、[testing](https://developer.android.com/develop/ui/compose/accessibility/testing) | 给常规 app 界面补充语义角色/状态、可理解标签、合理焦点顺序、文字与布局缩放和可测试无障碍节点；用 Layout Inspector、TalkBack、自动检查组合核验。 | 七个页面均已打开；核心 Compose 最佳实践页最后更新 2026-10-19。它们是 Android UX/质量指导，不会使 AccessibilityService 用途自动获 Play 批准。 |
| [Build accessible apps](https://developer.android.com/guide/topics/ui/accessibility)、[Make apps more accessible](https://developer.android.com/guide/topics/ui/accessibility/apps)、[Principles](https://developer.android.com/guide/topics/ui/accessibility/principles)、[Test accessibility](https://developer.android.com/guide/topics/ui/accessibility/testing) | 普通 app 应优先改进自身 UI 的标签、对比度、触控目标和可理解性，并用真实辅助技术验证主流程；不能把“app 自身需要无障碍”误作采集其他 app 屏幕的理由。 | 四个页面均已打开；总览/实现/测试内容分别更新于 2026-04-22、2026-10-19、2026-10-19 和 2026-04-16。仅保留政策相关操作点，非 Play 强制条文。 |
| [Compose quick guide](https://developer.android.com/develop/ui/compose/quick-guides/content/video/accessibility-in-compose)、[Compose accessibility codelab](https://developer.android.com/codelabs/jetpack-compose-accessibility)、[Accessibility learning pathway](https://developer.android.com/courses/pathways/make-your-android-app-accessible) | 快速指南/课程用真实测试和样例演示 Compose 可访问性实践；codelab 包括语义和触控目标练习，可用 TalkBack/其他辅助技术手动测试，Accessibility Scanner 只能发现部分常见问题。 | 页面/课程入口已打开；其代码仓库及完整课程后代未逐个归档；Compose 教学视频目标本次未能取到可读字幕。 |

**政策—平台边界：** Play Help 对 AccessibilityService 的审批、显著披露、同意、视频和自动化边界决定 Play 分发条件；Android 开发指南约束服务的正确/最小化实现；Compose/Android app-quality 页面帮助普通应用提供可访问的 UI。三类材料不能互相替代。Help 页旧版 API 31 时间、平台 API 行为和账号专属申报以来源审计表分别记录，未从无法读取的 Console 表单推断具体答案。

## 敏感 JavaScript 接口漏洞：政策要求与 WebView 实现链

2026-10-22 重新打开 [Sensitive JavaScript Interface vulnerability remediation](https://support.google.com/googleplay/android-developer/answer/10768383?hl=en)。它是逐应用安全整改通知：受影响包名和截止日以开发者账号收到的 Play Console 通知/邮件为准；开发者须修复并重新提交，重新审核通过后才算完成，逾期未修复的版本可能被下架。公开文章不能确认某个账号的受影响应用或期限。

该页正文有 10 次链接引用、9 个唯一政策/实现目标（`WebView` API 被引用两次）；另有 12 项 Help 侧栏、1 个 SMS 政策预览入口和 2 个求助控件，侧栏与求助入口不等同于正文规则。下表只摘录与此整改直接相关的政策和安全实现目标；Android 指南的其他一般性 API、示例和站点导航仍按来源台账标注，不声称已穷尽所有技术后代。

| 直接目标 | 页面要点与本整改的关系 | 核验边界 |
| --- | --- | --- |
| [Device and Network Abuse（现行合并页）](https://support.google.com/googleplay/android-developer/answer/16559646?hl=en) | Play 明确要求运行时加载的 JavaScript（包括第三方代码/SDK）不得促成其他开发者政策违规；这是桥接风险的政策依据。 | 正文已打开并有双语专题；它的 Android 技术后代仍部分未展开。 |
| [User Data](https://support.google.com/googleplay/android-developer/answer/10144311?hl=en) 与 [Malware](https://support.google.com/googleplay/android-developer/answer/9888380?hl=en) | JavaScript bridge 可能导致意外收集或外传用户数据，也可能使应用表现为有害软件；具体适用类别取决于实际行为，不能把“存在 WebView bridge”本身直接等同于违规。 | 两个政策正文均已打开并有专题摘要。 |
| Play 页链接的旧版 [Build web apps in WebView](https://developer.android.com/guide/webapps/webview) → [当前 Android 指南](https://developer.android.com/develop/ui/views/layout/webapps/webview) | 当前指南称 JavaScript 默认关闭；`addJavascriptInterface` 会让网页脚本调用原生代码。只有在 WebView 中的 HTML/JS 都由开发者编写时才使用该旧接口；不要让 WebView 导航到外部网页，外部链接交给系统浏览器。导航时应限定自有 host。 | 旧 URL 已核实重定向到新路径；指南正文已打开。仅追踪了与桥接/导航安全相关的子链接。 |
| [`WebView.addJavascriptInterface` 与 `removeJavascriptInterface`](https://developer.android.com/reference/android/webkit/WebView.html) | 注入对象会暴露给所有 frame，包括 iframe；原生端无法获知调用方 frame 的 origin。`removeJavascriptInterface` 的移除要到下一次页面加载/重载才会反映到 JavaScript。target SDK 上的 `@JavascriptInterface` 可见性限制不构成来源校验。 | 相关 API 成员已打开；该大型 API 参考的其他成员未穷尽。 |
| [`WebViewClient.shouldInterceptRequest`](https://developer.android.com/reference/android/webkit/WebViewClient) | Play 页面将其列为不可信内容加载前移除 bridge 的时机。当前 API 参考区分 `WebResourceRequest` 与旧 `String` 重载；回调不在 UI 线程，某些 URL scheme 不会回调，重定向只检查初始请求。因此要结合导航控制和重载时序验证实际修复，不能只因实现了回调就认为任意导航均已拦截。 | 对应方法说明已打开；未复制整份 API 参考。 |
| [Access native APIs with JavaScript bridge](https://developer.android.com/develop/ui/views/layout/webapps/native-api-access-jsbridge) 与 [`WebViewCompat` API](https://developer.android.com/reference/androidx/webkit/WebViewCompat) | Android 当前指南推荐 `addWebMessageListener`：配置精确的 `allowedOriginRules`、检查 `WebViewFeature.WEB_MESSAGE_LISTENER` 是否支持，并在页面导航前注册。API 会把对象注入 origin 匹配的 frame；HTTPS 更安全，通配符 `*` 会对所有来源开放。此为 Android 技术建议，不是 Play 强制指定的唯一实现，也不会自动证明政策合规。 | 指南正文及对应 API 方法已打开；其他示例/API 后代仍部分未展开。 |
| [Prominent disclosure and consent best practices](https://support.google.com/googleplay/android-developer/answer/11150561?hl=en) | 如果应用仍合法处理敏感数据或功能，须按 User Data 规则在应用内、请求能力前提供独立显著披露和肯定同意；允许拒绝/取消并优雅降级。解释 Why/What/How，包含 SDK 的第三方共享。披露不替代隐私政策或 Data safety。 | 最佳实践正文已打开；申报视频与账号内表单继续按该页审计记录处理。 |
| [Console remediation notice](https://play.google.com/console)、[Policy support](https://support.google.com/googleplay/android-developer/contact/app_vuln)、[Community](https://support.google.com/googleplay/android-developer/community?help_center_link=CP-fkQUSPFJlbWVkaWF0aW9uIGZvciBTZW5zaXRpdmUgSmF2YVNjcmlwdCBJbnRlcmZhY2UgVnVsbmVyYWJpbGl0eQ&hl=en)、[Contact support](https://support.google.com/googleplay/android-developer/gethelp) | Console 入口落到公开业务页，无法查看账号通知；Policy support 跳转登录后的 Policy Center；社区链接抓取 cache miss，Contact support 跳转账号专属支持页。均为流程/求助入口，不是新增政策义务。 | 跳转与不可读原因已写入逐 URL 审计。 |

### 同页的权限帮助侧栏与 SMS 预览入口

对该页面中 “Use of app permissions and APIs” 目录及侧栏链接逐项打开。12 个导航目标（含目录页和当前整改页）是相关帮助内容的导航，不是 12 条新的权限规则；另一个 SMS/Call Log 预览页是提案内容，应与现行 SMS 政策分开阅读。

| 导航目标 | 本地专题/处理方式 |
| --- | --- |
| [Use of app permissions and APIs 目录](https://support.google.com/googleplay/android-developer/topic/12798286?hl=en&ref_topic=2364761) | 页面列出同组权限帮助文章；不另作政策摘要。 |
| [Declare permissions](https://support.google.com/googleplay/android-developer/answer/9214102?hl=en) | [权限声明专题](../permissions-declaration/permissions-declaration.zh-CN.md)；表单、轨道阻断及账号内步骤。 |
| [Background location](https://support.google.com/googleplay/android-developer/answer/9799150?hl=en) | [后台位置专题](../background-location/background-location.zh-CN.md)。 |
| [All files access](https://support.google.com/googleplay/android-developer/answer/10467955?hl=en) | 本专题“所有文件访问”部分。 |
| [Broad package visibility](https://support.google.com/googleplay/android-developer/answer/10158779?hl=en) | 本专题“已安装应用可见性”部分及 Android `<queries>` 指南。 |
| [Request Install Packages](https://support.google.com/googleplay/android-developer/answer/12085295?hl=en) | 本专题 Restricted Permissions 直链表。 |
| [SMS or Call Log permission groups](https://support.google.com/googleplay/android-developer/answer/10208820?hl=en) | [短信与通话记录权限专题](../sms-call-log/sms-call-log.zh-CN.md)。 |
| [AccessibilityService API](https://support.google.com/googleplay/android-developer/answer/10964491?hl=en) | 本专题专项摘要；完整声明与披露视频仍以 Play Console 要求为准。 |
| [Sensitive JavaScript Interface remediation](https://support.google.com/googleplay/android-developer/answer/10768383?hl=en) | 当前小节。 |
| [Use of the `isMonitoringTool` Flag](https://support.google.com/googleplay/android-developer/answer/12955211?hl=en) | Malware 专题（[Google Play 恶意软件（Malware）与 Play Protect 威胁分类](../malware/malware.zh-CN.md)）。 |
| [Restricted Permissions with minimum-scope alternatives](https://support.google.com/googleplay/android-developer/answer/16935362?hl=en) | 本专题 Restricted Permissions 直链表及照片/视频最小范围专题。 |
| [Minimum Scope: Foreground Location Access and the Location Button](https://support.google.com/googleplay/android-developer/answer/17033915?hl=en) | 联系人与前台位置专题（[联系人与前台位置权限：最小范围和替代方案](../contacts-location-permissions/contacts-location-permissions.zh-CN.md)）及[后台位置专题](../background-location/background-location.zh-CN.md)。 |
| [SMS/Call Log policy preview](https://support.google.com/googleplay/android-developer/answer/17225965?hl=en) | [短信与通话记录专题](../sms-call-log/sms-call-log.zh-CN.md)中的未来变更说明；不是现行条款。 |

### 整改核对顺序

1. 盘点应用和 SDK 中所有 `addJavascriptInterface`、运行时加载的脚本、WebView 导航和 iframe 来源；按实际资源链确认哪些内容可控。
2. 对不可信内容不注入 bridge；若复用 WebView，先在应用侧控制导航、移除接口并确保新页面重新加载后再开放内容。优先评估带 origin 白名单的 `addWebMessageListener`。
3. 不通过网页脚本暴露短信、无障碍或其他敏感权限/API；将仍需的功能移回应用代码，并按 User Data 规则披露、取得同意。
4. 查看 Console/邮件中的具体受影响包和期限，提交修复版本并跟踪复审结果。

这些核对项是 Play 整改说明与 Android 实现文档的交叉整理；账号通知、设备 WebView 版本、重定向/子 frame 行为仍需在目标应用中核实。

## 所有文件访问：正文子链接与关键后代

2026-10-23 重新打开 [Use of All files access (`MANAGE_EXTERNAL_STORAGE`)](https://support.google.com/googleplay/android-developer/answer/10467955?hl=en) 的完整正文，并按链接用途区分 Play 政策、申报流程、Android 实现和帮助/导航入口。正文适用 Android 11/API 30+ 且声明该权限的应用；`READ_EXTERNAL_STORAGE` 不受这篇 Play 专项规则影响。申请前应先从 Manifest 移除不需要的权限；适用时必须提交权限声明并获得 Play 审批。

2026-10-24 从现行[合并版 Developer Program Policy](https://support.google.com/googleplay/android-developer/answer/18258653?hl=en)的 All Files Access 条款再次跟到帮助页：正文链接 `answer/9956427` 已观察重定向到当前 `answer/10467955`。这条父页路径与 `goo.gle/play-help-all-files-access` 短链不同；后者仍为 Cache miss，不能据相邻链接推定目标。当前 All files Help 的另一条“高风险或敏感权限”链接经 `play.google.com/about/privacy-security-deception/permissions/`、旧帮助路由 `answer/16324062` 到现行合并政策 `answer/16558241`，各跳转已逐级核验。重新打开 Help 正文后，其 10 个正文外部链接目标 ID 归并为 9 个不同 URL；同页 Alternatives 锚点、帮助社区/联系支持控件与 12 项政策侧栏另行计数。Help 正文明确把“设备迁移/手机传输”列为可申请用途之一，但应用核心目的必须是帮助用户迁移，且仍须 Play 审核批准。详见递归链接图（快照：`../google-play-policy-link-graph.md`，未导入本仓库） §4.129。

| 层级/类别 | 正文链接目标 | 页面要点及其与父页的关系 | 核验状态 |
| --- | --- | --- | --- |
| Play 政策 | [高风险或敏感权限政策入口](https://play.google.com/about/privacy-security-deception/permissions/) → [现行敏感信息权限政策](https://support.google.com/googleplay/android-developer/answer/16558241?hl=en) | 旧入口依次跳转到旧 Help 路由 `answer/16324062`，再跳到现行合并版 `answer/16558241`。2026-10-24 从本页再次点击并单独打开旧路由，确认最终目标；当前资格判断以现行合并政策及适用专项条款为准。 | 跳转链已核验；最终现行政策正文已打开并有本地专题。 |
| Play 申报 | [Declare permissions for your app](https://support.google.com/googleplay/android-developer/answer/9214102?hl=en) | Play Console 表单要求说明权限用途与核心功能；审核材料、测试登录信息和未申报权限造成的发布/商店资料变更阻塞见[权限声明专题](../permissions-declaration/permissions-declaration.zh-CN.md)。申报获批是 Play 分发要求，不等于 Android 系统访问已自动授予。 | 完整正文已打开；专题已摘要；更深的表单后代仍部分核验。 |
| Android 系统行为 | [Storage updates in Android 11](https://developer.android.com/about/versions/11/privacy/storage) | API 30 引入/加强 scoped storage；Android 11 起不得访问其他应用的私有目录；SAF 对内部存储根目录、可靠 SD 卡根目录、`Download` 及 `Android/data`/`Android/obb` 有目标版本限制。页面明确把 all-files access 留给无法有效采用隐私友好最佳实践的核心场景。 | 旧 `/preview/privacy/storage` 路径跳转至现行页；完整正文已打开，页面标注 2026-10-01 更新。 |
| Android 访问模型 | [Manage all files on a storage device](https://developer.android.com/training/data-storage/manage-all-files) | 说明 Manifest 权限、跳转到系统“管理所有文件”设置、`Environment.isExternalStorageManager()` 检查及技术可读写范围。系统授权仍不让应用访问其他应用的 `Android/data` 私有目录；Play 的用途资格和审批仍要另行满足。 | 完整正文已打开；页面标注 2026-10-16 更新；不是 Play 审核标准的替代来源。 |
| Android 设备迁移后代 | 该指南的 [旧版 Device-to-device data migration 链接](https://developer.android.com/guide/topics/data/testingbackup) 重定向至当前 [Test backup and restore](https://developer.android.com/identity/data/testingbackup) | 这是测试 Android 云备份及设备到设备迁移的技术指南，要求在主要版本发布前测试备份/恢复；Android 12 起该页记载 D2D 数据量上限高于云备份（2 GB 对 2 MB）。它说明系统传输机制，不证明某应用必须申请 All files，也不等于 Play 已批准。 | 2026-10-24 重试先前未暴露 href 的链接，现已打开重定向目标完整 377 行正文；7 个正文直链均点击，详见下文。 |
| Android 方案总览 | [Data and file storage overview](https://developer.android.com/training/data-storage) | 按应用私有数据、共享文件和媒体等情境选择存储方式，给出 API/指南入口。 | 完整正文已打开；技术/API 后代未逐项展开。 |
| Android 最佳实践 | [Storage use cases and best practices](https://developer.android.com/training/data-storage/use-cases) | 将媒体与非媒体文件分开处理：针对媒体优先 MediaStore；用户挑选单个文件时使用系统 Picker/SAF；应用私有数据放在 app-specific storage。指南中的示例和 API 链接数量较多，后代仅按政策相关性优先记录。 | 2026-10-23 重开 407 行正文（页面标注 2026-10-16 更新）；存储总览、运行时权限、共享媒体、SAF 与 FileProvider 关键子页已复核；所有代码示例/API 后代未全部打开。 |
| Android 用户选取文件 | [Storage Access Framework](https://developer.android.com/guide/topics/providers/document-provider) | 通过系统 Picker 让用户选择文件/目录，以 URI grant 提供用户授权范围；可导入单个文件，或在用户选择后持久访问文档。它通常适合文件导入、传输和处理，不代表应用可任意扫描共享存储。自建 `DocumentsProvider` 仅适用于暴露应用自有文件服务，不是 all-files 权限替代资格。 | SAF 文件页及 custom `DocumentProvider` 正文已读；后者 69 次外链引用归并为 22 个目标，18 个打开，4 个抓取失败。实现建议、API 后代及限制见递归图 §4.73、§4.105；完整 API/样例树仍部分覆盖。 |
| Android 媒体访问 | [MediaStore API](https://developer.android.com/training/data-storage/shared/media) | 媒体集合可独立查询、添加和更新；图像/视频权限仍受 Play 专项用途限制，Photo Picker 可进一步缩小用户授权范围。它是媒体文件访问的首选替代路径，媒体访问本身不能作为 `MANAGE_EXTERNAL_STORAGE` 的理由。 | 1080 行完整页面已打开；主要集合、Photo Picker 和权限关系已核对，完整 API 成员/代码示例未逐项摘录。 |
| Android 应用私有文件 | [Access app-specific files](https://developer.android.com/training/data-storage/app-specific) | 只供本应用使用的数据优先放内部或外部 app-specific 目录；卸载时这些文件会移除。需要用户可跨应用/卸载保留的内容应转向共享存储。 | 490 行完整页面已打开；Manifest/API 示例后代未全部展开。 |
| 企业分发例外背景 | [Android for enterprise / Managed Google Play](https://developer.android.com/work) | All files 专项政策另提运营商/OEM 服务与 Managed Google Play 私有应用；此 Android Enterprise 页面说明企业分发背景，不会让普通公开 Play 应用自动满足例外资格。 | 旧 `/distribute/google-play/work` 路径跳转至现行 `/work`；页面已打开。 |
| 帮助/支持入口 | [Developer Help Community](https://support.google.com/googleplay/android-developer/community)；[Contact us](https://support.google.com/googleplay/android-developer/gethelp) | 社区和联系支持链接是求助渠道，不是权限资格或技术实现规则。2026-10-24 从本页重试社区仍为 Cache miss；Contact us 暴露 Play Console 账号内支持路由。 | 社区不可读；联系入口需登录；未据此推断政策。 |

### Android 存储最佳实践指南：关键后代

2026-10-23 从 All files access 帮助页继续打开 Android [存储用例与最佳实践](https://developer.android.com/training/data-storage/use-cases)，并复核其[存储总览](https://developer.android.com/training/data-storage)、[运行时权限请求](https://developer.android.com/training/permissions/requesting)、[共享媒体](https://developer.android.com/training/data-storage/shared/media)、[SAF 文档选择](https://developer.android.com/training/data-storage/shared/documents-files)及 [FileProvider 文件共享](https://developer.android.com/training/secure-file-sharing/setup-sharing)直链。Android 指南说明如何选择/实现 API；Play 是否允许申请 `MANAGE_EXTERNAL_STORAGE` 仍由前述 Play 专项资格和申报审核决定。

| 后代 | 对 All files 判断的意义 | 核验边界 |
| --- | --- | --- |
| [Data and file storage overview](https://developer.android.com/training/data-storage) | 按数据性质区分仅供本应用使用的文件、跨应用共享的媒体/文档、偏好设置和结构化数据库；敏感私有数据优先内部存储/数据库。Android 11/API 30+ 面向高版本的应用中，`WRITE_EXTERNAL_STORAGE` 不会扩大存储访问；广泛访问由 `MANAGE_EXTERNAL_STORAGE` 单独控制，说明多数用例不需要它。 | 完整正文已打开；该页标注 2026-10-16 更新。相关权限段落已核对，其他存储/API 后代仍部分覆盖。 |
| [Request runtime permissions](https://developer.android.com/training/permissions/requesting) | 在用户进入需要权限的功能时按情境请求；每次执行受保护操作前检查授权。拒绝后应允许取消教育流程并优雅降级；不要依赖权限组的成员或系统弹窗行为。它支持“尊重拒绝/提供替代”的实现方式，但不证明某项权限符合 Play 资格。 | 正文和权限申请流程已打开；大型 AndroidX/API 参考后代未穷尽。 |
| [Setting up file sharing with FileProvider](https://developer.android.com/training/secure-file-sharing/setup-sharing) → [FileProvider API](https://developer.android.com/reference/androidx/core/content/FileProvider) | 对只需把本应用生成/持有的文件交给另一应用的场景，使用 content URI 和临时 URI 授权；XML `<paths>` 明确限定可分享目录。系统共享机制比扫描全盘更窄。 | 设置指南完整打开；页面要求 `exported=false` 与 `grantUriPermissions=true`，只配置需要共享的路径。它的 Provider/manifest/content-URI 元素与 FileProvider/Core 参考目标已直接点击；大 API 成员未穷尽。 |
| [Android 13 target behavior](https://developer.android.com/about/versions/13/behavior-changes-13#granular-media-permissions) → [MediaStore guide](https://developer.android.com/training/data-storage/shared/media) | target API 33+ 且需读取其他应用媒体时，应按类型申请 `READ_MEDIA_IMAGES`、`READ_MEDIA_VIDEO` 或 `READ_MEDIA_AUDIO`，而不是 `READ_EXTERNAL_STORAGE`；若只需用户挑选图片/视频，Android 建议 Photo Picker。Google Play 仍另要求 Photo Picker 不足以支持核心功能时才申请受限照片/视频权限，并完成 Console 声明。媒体权限与广泛目录权限 `MANAGE_EXTERNAL_STORAGE` 是不同政策判断。 | Android 13 行为页及 MediaStore 相关段落已打开；MediaStore 是大型指南，其他代码/API后代部分覆盖。 |
| [Intent API](https://developer.android.com/reference/android/content/Intent) 与 SAF | 用户选择单个文件时由 `ACTION_GET_CONTENT` / `ACTION_OPEN_DOCUMENT` 启动系统 Picker；访问权由用户选取结果和 URI grant 限定。 | Intent 为大型 API 目录，只核对与 Picker 相关的入口；SAF 的选择器限制和孙链接见本专题及递归图 §4.73（快照：`../google-play-policy-link-graph.md`，未导入本仓库）。 |
| FileProvider 设置页的存储链接：[Storage Options](https://developer.android.com/training/data-storage)；[Saving Files（旧路由）](https://developer.android.com/training/basics/data-storage/files) | Storage Options 跳转到当前 Data and file storage overview。独立的 Saving Files 目标仍返回旧文档正文（2025-01-09 更新），其媒体权限表述不应覆盖 Android 13+ target 的细粒度权限规则。 | 两个目标均已打开；旧页只核对与存储权限相关的段落，并作为历史/过时技术路线记录，不作为现行权限矩阵。 |

存储用例指南还包含多个 API 版本分支和示例（例如 `READ_EXTERNAL_STORAGE`、`WRITE_EXTERNAL_STORAGE`、旧版 scoped-storage opt-out、`MediaStore`、下载与导出）。这些例子不能不经目标 Android 版本核对就作为新版本的权限清单；本专题仅把它们作为实现线索，不据此扩大 Play 的权限资格。FileProvider 的直链包括 `<provider>`、`<manifest>`、`<meta-data>`、content-provider 基础、FileProvider API、AndroidX Core release notes、Storage Options 和 Saving Files；其直接目标均已点击并按系统实现/旧文档分类，API 的更深成员仍部分覆盖。完整外链清单尚在逐层扩展，详见该页的逐 URL 审计记录（快照：`../source-page-audit.csv`，未导入本仓库）和递归图 §4.73。

页面底部另列 [Use of app permissions and APIs](https://support.google.com/googleplay/android-developer/topic/12798286?hl=en) 帮助导航目录及 12 个权限帮助目标；它们不是额外的 All files 正文条款。12 个目标已在本专题上表/其他政策专题中逐项登记。正文里的“Alternatives”锚点返回同一页；折叠/展开控件、页眉搜索及站点导航不是独立政策目标。

**决策顺序：** 先判断用户是否选择单个文件、是否处理媒体、是否只需本应用私有数据；分别优先 SAF/Picker、MediaStore/Photo Picker、app-specific storage。只有这些方案无法有效支持已披露的核心功能时，才评估 all-files access；再单独完成 Play 声明、资格论证和审查。Android 系统设置里的授权、技术上可访问与 Play 审批是三个不同判断。

### Android `Manage all files` 实现指南的直接后代

2026-10-23 继续核验 [Android `Manage all files` 指南](https://developer.android.com/training/data-storage/manage-all-files)中的 `Environment.isExternalStorageManager()`。本次从指南直接点击该方法链接（正文链接 ID 10）成功打开[Environment API 参考](https://developer.android.com/reference/android/os/Environment)，页面标注 2026-08-03 更新。只针对相关成员检查：无参和 `File path` 两个重载均自 API 30 起，分别检查主共享/外部存储或指定路径是否已有 All files access；声明 `MANAGE_EXTERNAL_STORAGE` 本身不足以取得授权。API 页这两个方法又指向 [Manifest 权限目录](https://developer.android.com/reference/android/Manifest.permission)、[Settings API](https://developer.android.com/reference/android/provider/Settings) 和 `File` 参数类型。Manifest 条目显示 API 30 及 `signature|appop|preinstalled` 保护级别；Settings 的应用专属 Intent 同样自 API 30 起，数据 URI 必须指定 `package:<应用包名>`，发起该页面还要求声明对应权限，系统上也可能没有匹配 Activity。系统设置授予状态、Play 允许用途和 Play 审核批准仍是不同检查。Environment/Settings/Manifest 都是大型 API 目录；本轮只审阅相关成员；已通过正文链接 ID 10 确认父页精确目标。该指南的 17 次正文链接引用归并为 14 个目标；2026-10-24 已补开此前未解析的设备迁移目标并确认其跳转到 Android 备份/恢复测试指南。API 成员和更深技术后代仍未穷尽。

| 后代目标 | 内容、与权限政策的关系及状态 |
| --- | --- |
| [Manifest.permission API](https://developer.android.com/reference/android/Manifest.permission) | 核实 `MANAGE_EXTERNAL_STORAGE` 自 API 30 引入，平台描述为 scoped storage 下的广泛外部存储访问，保护级别为 `signature|appop|preinstalled`；同一 API 参考也定义 `QUERY_ALL_PACKAGES`。这是平台常量参考，不代表普通应用因此取得系统授权或 Play 资格。 |
| [Settings API](https://developer.android.com/reference/android/provider/Settings) | `ACTION_MANAGE_ALL_FILES_ACCESS_PERMISSION` 自 API 30 起打开控制存储管理权限的设置页；针对单个应用的 `ACTION_MANAGE_APP_ALL_FILES_ACCESS_PERMISSION` 需要传入应用包名数据 URI。文档提醒目标 Activity 在某些情况下可能不存在。Settings API 本身不授予 Play 审批。 |
| [`Environment.isExternalStorageManager()`](https://developer.android.com/reference/android/os/Environment) | 本轮成功打开 2669 行 API 页面（标注 2026-08-03 更新），并检查相关的两个 API 30 重载：无参版本检查主共享/外部存储；`File path` 版本检查指定路径。页面明确声明 `MANAGE_EXTERNAL_STORAGE` 不足以获得访问。两个成员分别链接到已打开的 [Manifest 权限常量](https://developer.android.com/reference/android/Manifest.permission)与 [Settings Intent](https://developer.android.com/reference/android/provider/Settings)：后者要求 `package:<应用包名>` 数据 URI、声明对应权限，且可能没有匹配 Activity。系统权限状态不等于 Play 用途资格/审核批准。本次从父指南正文链接 ID 10 直接打开此 API 页面，已确认精确目标；大型 API 页其余成员未穷尽。 |
| [Shared storage 概览](https://developer.android.com/training/data-storage/shared) | Android 将可跨应用或卸载后保留的数据分为媒体（MediaStore）、文档/其他文件（SAF）和共享数据集（BlobStoreManager）。这解释了为什么大多数常规用途可采用更窄的存储 API。页面标注 2026-03-05 更新。 |
| [MediaStore.Files API](https://developer.android.com/reference/android/provider/MediaStore.Files) 与 [MediaStore API](https://developer.android.com/reference/android/provider/MediaStore) | `MediaStore.Files` 索引媒体存储中的媒体及非媒体文件；API 参考说明访问方法，不单独授予广泛访问权限。Play 专项页仍把 MediaStore 作为适用场景的窄替代方案，而不是对任何文件管理用途的审批保证。大型 API 页仅核对相关类/方法。 |
| [SAF：Access documents and other files](https://developer.android.com/training/data-storage/shared/documents-files) | 指南（2026-10-16 更新）用系统 Picker 让用户选择文件/目录，再以 URI grant 访问所选范围，不需通用存储权限；API 19 起可创建/打开单文件，API 21 起可授权用户选定目录树。URI 权限通常在设备重启前有效；仅当系统给出 persistable 标记时才可持久保存，文件被移动/删除后仍需用户重新选择。Android 11/API 30 起，单文件 Picker 不能选 `Android/data`、`Android/obb`；目录 Picker 也不能选内部卷根、设备认定可靠的 SD 卡根、`Download` 或上述私有目录。应按 `Document.COLUMN_FLAGS` 判断写/删能力；`DocumentFile.canWrite()` 可能只因支持删除就返回 true。虚拟文档需检查标志并请求 provider 支持的 MIME；`MediaStore.getMediaUri()` 不授予新权限。正文 24 个外链引用归并为 18 个唯一目标，本轮打开 17 个，YouTube 目标 href 未暴露；摘要、访问状态及 API/样例后代见递归图 §4.73（快照：`../google-play-policy-link-graph.md`，未导入本仓库）。大型 API、样例源码及更深后代仍部分覆盖。 |
| [StorageManager API](https://developer.android.com/reference/android/os/storage/StorageManager) 与 [PendingIntent API](https://developer.android.com/reference/android/app/PendingIntent) | Android 12/API 31 起，`getManageSpaceActivityIntent()` 可启动另一应用自己实现的存储管理界面；Android 指南说明 file manager 场景还需 `MANAGE_EXTERNAL_STORAGE` 与 `QUERY_ALL_PACKAGES`。前者和后者分别受自己的 Play 专项资格审查；不能因该系统 API 存在就默认两项均可申报。大型 API 参考只核验了相关方法与返回类型。 |
| [Play All files access Help](https://support.google.com/googleplay/android-developer/answer/10467955?hl=en) | Android 指南内的 Google Play notice 回链到已独立摘要的政策页；核心用途、替代方案、申报及审批仍以该 Play 帮助页为准。 |

### 设备迁移、系统备份与 All files 资格的交叉核验

2026-10-24 重试 Android [Manage all files 指南](https://developer.android.com/training/data-storage/manage-all-files)里先前未能解析的“Device-to-device data migration”子链，链接最终跳转到 [Test backup and restore](https://developer.android.com/identity/data/testingbackup)。这条技术文档的 377 行正文介绍云备份与设备到设备（D2D）传输的测试流程；D2D 需要源设备和目标设备，Android 12 及以上的页面说明给出的数据量上限为 2 GB，而云备份为 2 MB。测试指南建议每次主要版本发布都验证备份/恢复；页面内容是 Android 平台测试指导，不是 Play 许可结论。

| Test backup and restore 正文子链接 | 内容与关系 | 覆盖状态 |
| --- | --- | --- |
| [BackupManager API](https://developer.android.com/reference/android/app/backup/BackupManager) | 说明应用通过 Android Backup Service 发起备份/恢复，`dataChanged()` 安排后续备份；大型 API 参考还列出 `BackupAgent`、`android:allowBackup` 等相关入口。只把相关类说明用于理解迁移/测试链。 | API 正文已打开并核对类概要、重要属性及方法；API 成员树未穷尽。 |
| Test backup and restore → 旧版 [Auto Backup 链接](https://developer.android.com/guide/topics/data/autobackup) → 当前 [Auto Backup 指南](https://developer.android.com/identity/data/autobackup) | Android 6.0+ 应用默认参与 Auto Backup；常见 app 私有目录数据可默认纳入，支持按云备份与 D2D 分别用规则包含/排除。可针对敏感本地数据配置备份条件或排除；Android 12/API 31+ 在部分 OEM 设备上将 `android:allowBackup="false"` 设为 false 仍不一定禁用设备到设备传输，因此需单独核对 `data-extraction-rules`。这些是 Android 行为，不替代 Play User Data、Data safety 或账户删除义务。 | 正文链接旧路径已确认跳转；打开目标后重核默认文件范围、停用备份、Android 12+ 规则及设备差异段落；代码/API 后代仍部分覆盖。 |
| BackupManager API → 旧版 [Data backup overview 链接](https://developer.android.com/guide/topics/data/backup) → 当前 [Data backup overview](https://developer.android.com/identity/data/backup) | 区分身份、用户生成内容和设置数据，并比较 Auto Backup 与 key-value backup；页面记载 Auto Backup 每应用 25 MB、key-value backup 每应用 5 MB。权限可能在 Android 7.0+ 的系统恢复中还原，但卸载会清掉已授予权限，重新安装后用户须再次授权。 | API 页 Developer Guides 中的链接已点开并确认跳转；完整 255 行目标正文已读，页面标注 2026-08-26 更新；其余备份 API 和服务后代未穷尽。 |
| `bmgr` → 旧版 [key-value backup 指南](https://developer.android.com/guide/topics/data/keyvaluebackup) → 当前[同一指南](https://developer.android.com/identity/data/keyvaluebackup) | 应用要显式定义备份键值数据，页面记载每用户上限为 5 MB；通常应选 Auto Backup，两种备份实现不能同时启用。若用 key-value，须实现 BackupAgent；BackupAgentHelper 可处理 SharedPreferences 和内部文件。它只描述应用自有数据的备份实现。 | `bmgr` 中的链接已点击并确认旧版路由跳转；690 行指南的主要实现章节已打开，完整 helper/API 链接树未穷尽。 |
| [BackupAgent API](https://developer.android.com/reference/android/app/backup/BackupAgent) | 自定义备份/恢复回调接口，属于 BackupManager 的实现后代；它帮助开发者实现或测试自己的 app 数据备份，不授予扫描其他 app 私有目录的能力。 | 大型 API 参考已打开；仅确认目标及其实现角色，其他 API 成员未穷尽。 |
| [Google Mobile Services](https://www.android.com/gms/)、[ADB](https://developer.android.com/tools/adb)、[`bmgr`](https://developer.android.com/tools/bmgr)、[Logcat](https://developer.android.com/tools/logcat) 与 [Application API](https://developer.android.com/reference/android/app/Application) | 是测试指南中的传输平台背景、测试命令/日志工具和应用启动上下文；不另行定义 Google Play 权限资格。`bmgr` 页另链 Auto Backup、key-value backup、ADB、Logcat、测试指南和 Data backup overview；Auto Backup 与 encrypted-backup 锚点归并至同一页面目标。 | 直接目标均已点击；`bmgr` 的 7 次正文链接引用归并为 6 个目标，均已打开或解析；ADB、Logcat 和 `Application` 是大型开发工具/API 页面，非备份条款后代仍未展开。 |

**关系判断：** Play Help 将“备份与恢复”和“设备迁移/手机传输”列为可能符合 `MANAGE_EXTERNAL_STORAGE` 的用途，但要求它们是应用核心用途并通过 Play 审批；设备迁移技术页本身只说明 Android D2D 的系统流程。通过 Picker 让用户逐项选择文件仍不能因此申请 all-files；备份/迁移应用也必须证明 SAF/MediaStore 等更窄方案不满足其核心功能，并按实际数据流履行 User Data 和 Data safety 义务。

**递归边界：** All files Help 的正文子链接已逐项登记；其主要 Android 指南正文和本表列出的高影响后代均已打开或注明访问限制。API 大型类页、代码示例、其他存储用例、视频/博客和导航后代仍部分未展开；这一轮不把技术文档递归标为穷尽。完整访问状态见来源页审计表（快照：`../source-page-audit.csv`，未导入本仓库），边关系会随重建写入 CSV 和离线 Wiki。

### Android 备份安全最佳实践（平台指导，不是 Play 政策）

2026-10-24 核对 [Security recommendations for backups](https://developer.android.com/privacy-and-security/risks/backup-best-practices)（该页标注 2024-10-25 更新）。Android 建议优先使用 Standard Android Backup。云端备份会在传输中和静态存储时加密；Android 9+ 且设备设置了锁屏时，备份还可使用 Google 不掌握的密钥进行端到端加密。特别敏感的数据应从备份排除；无法排除时，应按系统版本要求备份仅在支持端到端加密时才启用。

- Android 11/API 30 及以下规则可用 `requireFlags="clientSideEncryption"` 限制敏感数据备份。
- Android 12/API 31+ 使用 `data-extraction-rules`，并分别配置 `<cloud-backup>` 与 `<device-transfer>`；云端可设 `disableIfNoEncryptionCapabilities="true"`。这会在缺少加密能力时阻止云端备份，但不会关闭不经过服务器的 D2D 传输。
- 即使应用 target API 31+，仍要提供 Android 11 及以下设备使用的旧式 `fullBackupContent` 规则。若省略 `<device-transfer>`，D2D 默认仍会迁移应用数据（缓存和 no-backup 目录除外）；一旦使用 `<include>`，默认“全部包含”会变为仅包含明列路径，`<exclude>` 优先于 `<include>`。
- 如果确实要自行导出或实现非标准备份，需安全存放副本、控制其他应用的读取路径、排除不应迁移的数据并定期测试；这类实现更容易因疏漏泄露数据。Auto Backup 还建议不要备份设备专属标识或调试文件，并为大型数据留意 25 MB 云备份配额。

Auto Backup 的新版本还记载 Android 16 QPR2（API 36.1）起可通过 `<cross-platform-transfer platform="ios">` 配置与 iOS 的数据迁移，需声明 `bundleId`、`teamId` 和 `contentVersion`；定制 `BackupAgent` 可通过 `FLAG_CROSS_PLATFORM_TRANSFER_IOS` 和新的恢复回调识别该传输。这是 Android 数据迁移能力，不是 Google Play 政策要求。

| Android 安全/实现来源 | 与敏感权限和数据保护的关系 |
| --- | --- |
| [Sensitive Data Stored in External Storage](https://developer.android.com/privacy-and-security/risks/sensitive-data-external-storage) | 面向 Android 10/API 29 及以下的存储说明：有相应读取权限的其他应用可能读取外部存储敏感数据，写权限还带来篡改风险。建议敏感内容放内部存储；确需外置时用 Android Keystore 保护密钥并验证完整性。Android 11+ scoped storage 缩小访问面，但不取代备份规则或 Play 审核。 |
| [Android Cryptography](https://developer.android.com/privacy-and-security/cryptography) 与 [Android Keystore](https://developer.android.com/privacy-and-security/keystore) | 解释加密算法、provider 与密钥保护；Keystore 可让密钥材料不可导出，并按设备能力由 TEE/安全硬件保护。属于 Android 实现指导，不是 Play 许可规则。 |
| [File-based encryption](https://source.android.com/docs/security/features/encryption/file-based) 与 [Android 12 备份行为](https://developer.android.com/about/versions/12/behavior-changes-12#backup-restore) | 帮助区分设备存储加密、云备份和 D2D：FBE/锁屏保护设备上的文件，不自动等于备份端到端加密；Android 12+ 的 cloud 和 D2D 规则需要分开评估。 |
| [Understanding PII in Google's contracts and policies](https://support.google.com/analytics/answer/7686480?hl=en) | 这是 Google 广告/测量产品合同术语的 PII 解释，不是 Google Play Developer Program Policy 或 Data safety 定义；其排除某些标识符的说明不能替代适用的 Play、隐私法或产品条款。 |

**边界：** Android 安全建议不构成 Play 政策条款、权限用途资格或审核批准。应用仍需按真实数据流履行 Play User Data、Data safety、披露/同意和账户删除义务；详见递归链接图 §4.131（快照：`../google-play-policy-link-graph.md`，未导入本仓库）。

## `QUERY_ALL_PACKAGES`：Play 资格与 Android 包可见性替代方案

[Play 的广泛应用可见性政策](https://support.google.com/googleplay/android-developer/answer/10158779?hl=en)适用于 Android 11/API 30 及以上设备上、target API 30+ 的应用。已安装应用清单属于个人和敏感数据；只有需要发现所有已安装应用、且更窄的可见性无法支持商店页清楚宣传的核心功能时，才可能有资格申请。声明需如实解释核心用途；用途变化后要更新申报。未获资格或未提交声明可能导致应用下架；欺骗性或未申报用途还可能导致暂停或账号终止。

Play 列举的可能合格用途包括设备搜索、反病毒、文件管理器和浏览器。临时例外还可能适用于为满足地理围栏法规而必须检查应用清单的真钱赌博核心功能，或受监管金融交易的安全用途；**个人贷款、信用额度、贷款导流及相关辅助工具不适用该例外**。金融服务政策进一步禁止个人贷款、贷款/信用额度导流、辅助贷款工具和 EWA 应用访问 `QUERY_ALL_PACKAGES`；不得出售应用清单，也不得为广告或分析变现而收集/分享清单。非核心 P2P 分享、可由更窄方法完成的任务也不合格。

Android 11 起，面向 API 30+ 的应用默认只能查询部分应用；少数系统包会自动可见，但具体列表随设备变化。**启动另一个应用的 Activity 通常不要求先查询它是否可见**：直接调用 Intent 并处理 `ActivityNotFoundException`；只有界面必须事先知道目标是否存在时，才在 Manifest 使用 `<queries>`。可按具体包名、Intent 签名或 Content Provider authority 声明；库也能在 AAR Manifest 提供所需声明。`QUERY_ALL_PACKAGES` 是罕见兜底，并且 Android 能力不等于 Play 获批。

| Play 政策页的正文链接 | 页面内容与关系 | 核验状态 |
| --- | --- | --- |
| [高风险/敏感权限政策入口](https://play.google.com/about/privacy-security-deception/permissions/) → [现行权限政策](https://support.google.com/googleplay/android-developer/answer/16558241?hl=en) | 旧入口跳至旧 Help 路由，再转到现行综合政策；以现行页面为准。 | 跳转链已核验；现行页面已收录。 |
| [Declare permissions for your app](https://support.google.com/googleplay/android-developer/answer/9214102?hl=en) | 活跃测试或发布轨道的 AAB 若含未申报的受限权限，可能阻止应用和商店资料变更；申报材料包括核心功能、审核说明、演示视频及受限内容的测试凭证。审核可能需数周；未经 Play Console UI 首次获批时，Publishing API 发布会报错；增加权限后还要用 UI 更新申报。 | 正文已打开，详见[权限声明专题](../permissions-declaration/permissions-declaration.zh-CN.md)。 |
| [Permissions Declaration Form](https://play.google.com/console/developers/app/app-content/permission-declarations) | 账号内表单和应用专属资格/状态。 | 跳转到 Google 登录；字段及账号状态不可由公开页面验证。 |
| [User Data](https://support.google.com/googleplay/android-developer/answer/10144311?hl=en) | 明确把已安装应用清单列为敏感数据，适用数据最小化、安全、披露/同意和禁止出售等要求。 | 正文已打开，详见[用户数据专题](../user-data/user-data.zh-CN.md)。 |
| [Financial Services](https://support.google.com/googleplay/android-developer/answer/9876821?hl=en) | 除广义金融安全例外外，个人贷款、信用额度/贷款导流、辅助贷款工具和 EWA 应用不得使用 `QUERY_ALL_PACKAGES`；另列出照片、联系人、精确位置等禁用权限。 | 正文已打开；本页与[金融服务专题](../financial-services-and-loans/financial-services-and-loans.zh-CN.md)交叉核对。 |
| [Package visibility filtering on Android](https://developer.android.com/training/package-visibility) | Android 11+ 默认过滤应用清单；逐项说明自动可见包、精确声明可见性、常见交互用例和测试。 | 正文已打开；下表登记其政策相关直接目标。 |

### Android 包可见性指南的正文子链接

指南在三处 `PackageManager` 方法链接（`queryIntentActivities()`、`getPackageInfo()`、`getInstalledApplications()`）中指向同一 API 参考页面。Android 官方文档称 target API 30+ 时该类的查询结果受包可见性过滤；这里核对了上述方法的 API 说明，未逐项整理整个大型 API 参考。

| 目标页 | 最佳实践与本专题关系 | 核验状态 |
| --- | --- | --- |
| [PackageManager API reference](https://developer.android.com/reference/android/content/pm/PackageManager) | 已安装应用和 Intent 匹配查询会受默认过滤；应根据实际交互范围选择相应 API 与 `<queries>`，不能把空结果误判为应用不存在。 | 页面已打开；检查了 `getInstalledApplications`、`getInstalledPackages`、`queryIntentActivities` 相关段落，其余 API 成员未穷尽。 |
| [Know which packages are visible automatically](https://developer.android.com/training/package-visibility/automatic) | 自有应用、部分系统包、安装器、与本应用交互的应用等可能自动可见；设备相关系统包可用 `adb shell dumpsys package queries` 查看 `forceQueryable`。 | 正文已打开；技术子链接未全部追踪。 |
| [Declare package visibility needs](https://developer.android.com/training/package-visibility/declaring) | 已知应用用包名，不知包名但需发现一类应用时用 Intent 签名，需要特定 Provider 时按 authority 声明；允许通配符有限，避免用宽泛查询代替真实交互需求。 | 2026-10-24 重开正文并核对 14 个外链目标、3 个同页锚点；AAR、Service、Intent filter、Provider 专题子页已补读，继续后代仍部分覆盖。 |
| [`<queries>` manifest element](https://developer.android.com/guide/topics/manifest/queries-element) | Manifest 中仅声明应用预期交互对象；支持 `<package>`、`<intent>`、`<provider>`，自 API 30 引入。 | 正文已打开；部分元素说明回链至上面的声明指南。 |
| [Fulfill common use cases with limited visibility](https://developer.android.com/training/package-visibility/use-cases) | 直接启动 Intent 并处理 `ActivityNotFoundException` 通常不需 `<queries>`；打开 URL 时可先用 `FLAG_ACTIVITY_REQUIRE_NON_BROWSER`，失败再退回 Custom Tabs。只有界面必须提前显示可用应用、或需选定浏览器/服务时才加精确 `<queries>`；还给出 TTS、语音识别、媒体服务、SMS、sharesheet、文本选择和联系人行等例子。 | 正文已打开；这是 Android 实现建议，API/外部供应商后代仍部分覆盖。 |
| [Test package visibility behavior](https://developer.android.com/training/package-visibility/testing) | 用 target API 30+ 且不含 `<queries>` 的构建复现过滤，再添加满足功能所需的最窄声明；可打开包可见性日志定位被过滤项，测试结束关闭日志以免影响性能。 | 正文已打开；涉及的 Android Studio/API 子链接未全部展开。 |
| [Play 的 `QUERY_ALL_PACKAGES` 专项政策](https://support.google.com/googleplay/android-developer/answer/10158779?hl=en) | Android 技术文档回链到政策页；Android `<queries>` 不构成 Play 审核豁免。 | 正文已打开，见上表。 |
| [Package visibility in Android 11](https://medium.com/androiddevelopers/package-visibility-in-android-11-cc857f221cd9) | Android Developers 的历史背景文章（2020-06-30）；说明 Android 11 默认过滤安装应用并以 `<queries>` 缩小可见范围。 | 正文已打开；作为历史背景，不替代现行 Android 文档或 Play 政策。 |
| [Android Developers Content License](https://developer.android.com/license) | Android 文档和代码样例许可信息。 | 正文已打开；不是 Play 权限政策。 |

### AAR、Service、Intent filter、Provider 与合并 Manifest 的后代核验

这组页面解释 Android 的清单和跨应用交互机制；它们不会增加 `QUERY_ALL_PACKAGES` 的 Play 用途资格。声明指南的三个同页锚点（包名、Intent 签名、Provider authority）不是新页面；本轮把正文中的外链目标与关键后代分开核验。

| 页面/链接关系 | 页面要点及与包可见性的关系 | 核验状态 |
| --- | --- | --- |
| [Create an Android library / AAR](https://developer.android.com/studio/projects/android-library) | AAR 可携带 `AndroidManifest.xml`；库可在该 Manifest 中声明与应用相同作用的 `<queries>`。该文档还链接 [Manifest merge guide](https://developer.android.com/studio/build/manifest-merge)，后者跳转到[现行合并说明](https://developer.android.com/build/manage-manifests)。 | AAR 正文已打开；已沿正文链接重开 Manifest merge guide。该大型 Android Studio/依赖文档的其他导航与样例未穷尽。 |
| [Bound services（原始链接）](https://developer.android.com/guide/components/bound-services) → [现行 Bound services 页面](https://developer.android.com/develop/background-work/services/bound-services) | 原链接重定向到现行页面。若 AAR 要绑定宿主应用的 service，声明指南建议在 `<queries>` 里写宿主 package；绑定时须使用显式 Intent，按调用方生命周期配对 `bindService()`/`unbindService()`。 | 原始路由和现行正文已尝试/打开；ServiceConnection、完整生命周期示例及其他服务/API 后代未全读。 |
| [Context API：`bindService`](https://developer.android.com/reference/android/content/Context) | 当前 API 要求服务 Intent 指定显式 component；返回值区分系统是否正在建立绑定，调用方仍须释放连接。与 `PackageManager` 可见性查询不同，绑定本身也受目标服务权限/导出规则约束。 | 8,206 行大型 API 页；只定点核对 `bindService(Intent, ServiceConnection, int)`，其余成员未穷尽。 |
| [Intent filter signatures 指南](https://developer.android.com/training/basics/intents/filters) 与 [`<intent-filter>` Manifest 参考](https://developer.android.com/guide/topics/manifest/intent-filter-element) | 本应用自己的 `<intent-filter>` 宣告组件能接收哪些入站 Intent；`<queries><intent>` 则让本应用发现其他应用中匹配的组件，二者不能混为一谈。Intent filter 应尽量精确；隐式 Activity 启动还要按指南设置 `CATEGORY_DEFAULT`。 | 两个目标均已打开相关正文；通用 Intent、组件和 API 后代部分覆盖。 |
| [Content provider basics](https://developer.android.com/guide/topics/providers/content-provider-basics) 与 [`<provider>` Manifest 参考](https://developer.android.com/guide/topics/manifest/provider-element) | `<queries><provider android:authorities="…">` 仅解决按 authority 发现应用；它**不授予读取 Provider 数据的权利**。实际访问仍受 Provider 的 `readPermission`、`exported` 等规则控制。需要单条用户选择数据时，应优先采用 Picker/URI 授权；Intent 的 URI grant 只覆盖特定 URI，不等于读取整个 Provider。target API 30+ 的接收方带 URI grant 时还会获得该 Provider 所属应用的 package visibility。 | 两页的权限、exported、URI grant 关键段已抽查；854 行 Provider 指南和 API/示例后代未穷尽。 |
| [Manifest.permission API](https://developer.android.com/reference/android/Manifest.permission) | API 参考把 `QUERY_ALL_PACKAGES` 记为 API 30 新增、platform protection level `normal`。这只描述 Android 平台权限模型；Play 仍把该用途列为受限权限并要求符合资格、申报，不能由 `normal` 推导 Play 获批。 | 6,738 行权限目录已打开并定点核对该常量；其他权限成员未穷尽。 |
| [2020 Gradle 包可见性博客](https://android-developers.googleblog.com/2020/07/preparing-your-build-for-package-visibility-in-android-11.html) → [Android 11 包可见性概览](https://developer.android.com/about/versions/11/privacy/package-visibility)；[官方 Medium 文章](https://medium.com/androiddevelopers/package-visibility-in-android-11-cc857f221cd9) | 博客解释 Android 11 默认过滤、`<queries>` 与历史构建工具报错。旧文的 AGP 4.1 Beta/补丁版建议属于 2020 年背景；对应[旧插件路由](https://developer.android.com/studio/releases/gradle-plugin)现在指向[AGP 9.4.0 release notes](https://developer.android.com/build/releases/agp-9-4-0-release-notes)，但该目标本轮超时，不能据此补写其正文。Medium 文章是历史背景；其当前用例链仍应以[现行 package-visibility use cases](https://developer.android.com/training/package-visibility/use-cases)为准。 | 博客及 Medium 正文已打开；两个旧合并文档路由已确认跳转。AGP 9.4.0 目标可观察到页面标题/重定向，但正文抓取超时。 |
| [Android 11 package visibility 页面](https://developer.android.com/about/versions/11/privacy/package-visibility) | Android 11 行为变更只影响 target Android 11 的应用，并回链现行包可见性指南；作为平台版本背景，不是 Play 权限资格规则。 | 现行页面已打开；该版本专题的大量其他导航目标未递归。 |
| [Android Developers Content License](https://developer.android.com/license) | Android 开发者文档和代码样例的许可信息，不是 Play 权限政策。 | 页面可打开；通用许可页的其他链接不属于本专题政策判断。 |

**发布审查结论：**除盘点源码 Manifest 外，还要在 Android Studio 的 Merged Manifest 中检查最终 release variant，确认 `<queries>` 和权限是否来自主应用、构建 variant 或某个 AAR/SDK；合并日志可用于定位来源。以实际功能为依据收窄 package、Intent 或 authority；不要把应用自有 `<intent-filter>` 当作查询授权。Provider 可见性、URI grant、Provider 读权限和 Play 的 `QUERY_ALL_PACKAGES` 申报是四个不同边界。仅当更窄方法无法满足合格核心功能时，才评估广泛权限并准备 Play 声明/证据。

**递归状态：**Play 页面正文的政策相关直链、声明指南的 14 个外链目标和 3 个同页锚点均已重新核对；AAR、Service、Intent filter、Provider、权限 API、Manifest merge、历史博客和其主要直接链接已补入本专题/链接图。8,206 行 Context API、6,738 行 Manifest.permission、Provider/Service 的更深 API、样例和通用导航仍未穷尽；AGP 9.4.0 release-note 正文抓取超时。不能据此宣称无限递归闭合。逐 URL 状态见来源页审计表（快照：`../source-page-audit.csv`，未导入本仓库）和递归链接图（快照：`../google-play-policy-link-graph.md`，未导入本仓库）。

## VpnService 声明与审核材料

[VpnService 政策解释页](https://support.google.com/googleplay/android-developer/answer/12564964?hl=en)要求使用此 API 的应用提交 Play Console 声明。该页所写 **2023-08-31** 是历史截止日，已经过去；它不意味着今天可跳过声明，应用当前是否已声明/获批须在 Console 核对。声明会询问 VPN 是否为核心功能；若不是，须选择实际适用的许可类别。若不符合许可类别，政策解释页要求说明依据或从所有有效版本/轨道移除 VpnService。

审核材料包括不超过 90 秒展示应用打开及 VPN 工作方式的视频；若数据收集披露不明显，还需另一段不超过 90 秒的视频，展示从打开应用到完整披露、同意、允许及拒绝后再访问披露页面的路径。声明还询问通过 VpnService 收集/分享的数据类别及是否为变现操纵其他应用流量。改变 API 用途后须更新声明；欺骗性或未申报使用可导致应用暂停或开发者账号终止。



### Android API 与 VPN 开发指南

Android [`VpnService` API](https://developer.android.com/reference/android/net/VpnService) 与[VPN 开发指南](https://developer.android.com/develop/connectivity/vpn)解释系统实现流程：应用须通过 `VpnService.prepare()` 请求用户授权；使用 `Builder` 配置并建立 TUN 接口；用 `VpnService.protect()` 让 VPN 隧道 socket 不再次进入自身 VPN，避免循环；调用 `onRevoke()` 时关闭文件描述符并停止隧道。服务须在 Manifest 中受 `BIND_VPN_SERVICE` 保护并声明 `android.net.VpnService` intent filter；指南要求 VPN 网关间的流量使用强加密。连接启动/停止控制、活动时的不可划除通知，以及状态栏系统标记，帮助用户识别和控制 VPN。每个用户或工作资料同一时刻只运行一个 VPN 服务；Android 8.0+ 后台启动后，VPN 服务须及时提升为前台服务。

这些是 Android 技术和用户体验指南；它们不能替代 Play 的用途资格、流量处理限制、数据披露、同意和 Console 申报。API 页面原有的 [VPN guide 路径](https://developer.android.com/guide/topics/connectivity/vpn)会跳转到上面的现行路径。当前 [`VpnService.Builder` API 参考](https://developer.android.com/reference/android/net/VpnService.Builder)现已打开，并抽查了 `establish()`、地址/路由、允许/排除应用名单、`allowBypass()` 和地址族成员；通用 API 成员及版本兼容性仍未穷尽。完整的政策与工程交叉核对、逐链接清单和覆盖边界见VpnService 政策与实现专题（[Google Play VpnService 政策与 Android VPN 实现](../vpnservice-policy-and-implementation/vpnservice-policy-and-implementation.zh-CN.md)）。

该说明页正文有 7 次链接引用、6 个不同目标：VpnService API、Policy Center 目录、Ad Fraud、Permissions、Malware 和 User Data（两次）。本次 `Permissions` 链接点击返回 Internal Error，没有暴露目标 URL；当前[敏感权限政策正文](https://support.google.com/googleplay/android-developer/answer/16558241?hl=en)是单独核对的相关页面，不能据此断言它就是该链接的已验证重定向。说明页没有直接链接到醒目披露最佳实践；该最佳实践由 [User Data 页面](https://support.google.com/googleplay/android-developer/answer/10144311?hl=en)的后续链接引出。其余可见直链及访问限制见VpnService 专题（[Google Play VpnService 政策与 Android VPN 实现](../vpnservice-policy-and-implementation/vpnservice-policy-and-implementation.zh-CN.md)）。

## 2027-01-27 生效的更新

- **联系人广泛访问：** 综合页面预告新政策于 2027-01-27 生效，并链接到详细预览。预览规定，目标 Android 17/API 37+ 的应用仅在 Contact Picker 不足以支持核心功能时可申请 `READ_CONTACTS`，并须提交 Play Console 声明；不得在未获联系人数据主体授权时披露或发布非公开联系人数据。完整条件与例外见联系人和前台位置专题（[联系人与前台位置权限：最小范围和替代方案](../contacts-location-permissions/contacts-location-permissions.zh-CN.md)）。
- **精确位置：** Location Button 被列为精确位置最小范围的推荐方案。目标 API 37+ 的一次性精确定位须用该按钮；所有申请 `ACCESS_FINE_LOCATION` 的应用都须按最小范围页提交 Play Console 声明。按钮专用 Manifest 仍可能声明该权限并加 `onlyForLocationButton`，该 flag 限制 Android 访问路径，但不是已公布的 Play 申报豁免。常规持续访问还须说明为何粗略位置和按钮均不足。完整区别见联系人与前台位置专题（[联系人与前台位置权限：最小范围和替代方案](../contacts-location-permissions/contacts-location-permissions.zh-CN.md)）。

## 现行综合页正文直链核查

**核对日期：2026-10-22。** 已打开现行英文正文，并逐项尝试页面返回的链接引用（包含重复目的地及帮助中心导航）。下表按政策章节合并重复目标；每个目标的访问、重定向或抓取失败状态以 来源台账（快照：`../source-page-audit.csv`，未导入本仓库） 为准。Android 文档解释平台权限/API 和替代实现，不能单独证明 Google Play 的分发资格。

| 正文章节 | 直接链接目标 | 与政策的关系及本地摘要 |
| --- | --- | --- |
| 2027 更新预告 | [政策公告目录](https://support.google.com/googleplay/android-developer/announcements/13412212)、[政策预览](https://support.google.com/googleplay/android-developer/answer/16909972?hl=en)、[Location Button](https://developer.android.com/guide/topics/permissions/private-alternatives/location-button)、[Android Contact Picker](https://developer.android.com/about/versions/17/features/contact-picker) | 联系人和位置政策预告于 2027-01-27 生效。资格、替代方案和期限见联系人与前台位置专题（[联系人与前台位置权限：最小范围和替代方案](../contacts-location-permissions/contacts-location-permissions.zh-CN.md)）及期限表。 |
| 通用规则与受限权限 | [Android 权限概览](https://developer.android.com/guide/topics/permissions/overview)、[User Data](https://support.google.com/googleplay/android-developer/answer/10144311?hl=en)、[Malware / Elevated Privilege Abuse](https://support.google.com/googleplay/android-developer/answer/9888380?hl=en#elevated-privilege-abuse) | Android 的 dangerous、special、signature 分类与 Play 的受限权限审查是不同层次；须尊重拒绝、提供替代，并遵守数据用途限制。 |
| 照片与视频 | [最小范围替代方案](https://support.google.com/googleplay/android-developer/answer/16935362?hl=en)、[Android Photo Picker](https://developer.android.com/training/data-storage/shared/photo-picker)、[Android Sharesheet](https://developer.android.com/develop/ui/compose/sharing/send)、[User Data](https://support.google.com/googleplay/android-developer/answer/10144311?hl=en) | 先用系统选择器或用户主动分享来减少读取范围；仍需广泛媒体权限时须证明核心功能需要并申报。见[照片/视频专题](../photo-video-permissions/photo-video-permissions.zh-CN.md)。 |
| SMS 与通话记录 | [SMS/Call Log 政策](https://support.google.com/googleplay/android-developer/answer/10208820?hl=en)、[允许用途与例外](https://support.google.com/googleplay/android-developer/answer/10208820?hl=en#zippy=%2Calternatives-to-common-uses)、[SMS Retriever API](https://developers.google.com/identity/sms-retriever/overview) | 约束默认处理器身份、核心用途、停止访问、禁止广告和间接推导；申报表短链接本轮无法恢复目标。见[短信与通话记录专题](../sms-call-log/sms-call-log.zh-CN.md)。 |
| 位置 | [Android 位置指南](https://developer.android.com/develop/sensors-and-location/location)、[后台位置政策](https://support.google.com/googleplay/android-developer/answer/9799150?hl=en)、[Ads](https://support.google.com/googleplay/android-developer/answer/9857753)、[Families](https://support.google.com/googleplay/android-developer/answer/9893335) | 最小化精度与使用时段；后台位置须符合核心功能资格，广告、儿童定向和前台服务规则同时适用。申报入口需登录或由 Console 表单生成。见[后台位置专题](../background-location/background-location.zh-CN.md)。 |
| 所有文件访问 | [All files access 政策](https://support.google.com/googleplay/android-developer/answer/10467955)、[Android 11 存储变更](https://developer.android.com/about/versions/11/privacy/storage)、[Storage Access Framework](https://developer.android.com/guide/topics/providers/document-provider)、[MediaStore](https://developer.android.com/training/data-storage/shared/media)、[MANAGE_EXTERNAL_STORAGE 指南](https://developer.android.com/training/data-storage/manage-all-files) | 广泛存储访问只适用于符合条件的核心功能；优先使用系统文件选择器或媒体集合。平台设置访问不等于 Play 审核通过。 |
| 已安装应用可见性 | [Android package visibility](https://developer.android.com/training/package-visibility)、[QUERY_ALL_PACKAGES 政策](https://support.google.com/googleplay/android-developer/answer/10158779)、[Data safety](https://support.google.com/googleplay/android-developer/answer/10787469?hl=en)、[Manifest.permission API](https://developer.android.com/reference/android/Manifest.permission) | 优先有限的 `<queries>`；广泛清单仅限符合条件的核心用途并申报。应用清单数据不得用于广告/分析变现。 |
| Accessibility 与安装应用包 | [AccessibilityService 政策](https://support.google.com/googleplay/android-developer/answer/10964491?hl=en)、[Device and Network Abuse](https://support.google.com/googleplay/android-developer/answer/16559646?hl=en)、[Android 权限/API 参考](https://developer.android.com/reference/android/Manifest.permission)、[特殊权限请求指南](https://developer.android.com/training/permissions/requesting-special) | Accessibility 的披露、同意和用途限制，与 `REQUEST_INSTALL_PACKAGES` 的用户主动安装要求分别判断；申报表需要在 Play Console 核实。 |
| 身体传感器与 Health Connect | [Android 16 行为变更](https://developer.android.com/about/versions/16/behavior-changes-16)、[Health Permissions FAQ](https://support.google.com/googleplay/android-developer/answer/12991134)、[Health Content and Services](https://support.google.com/googleplay/android-developer/answer/16679511)、[Health Connect 开发指南与数据类型](https://developer.android.com/health-and-fitness/health-connect) | 从宽泛身体传感器权限迁移到必要的细粒度权限；Health Connect 另受获准用途、最小数据类型、用户同意及 Console 声明约束。详见健康应用与 Health Connect 专题（[健康应用、健康数据与 Health Connect](../health-apps-and-health-connect/health-apps-and-health-connect.zh-CN.md)）。 |
| VPN、精确闹钟与全屏意图 | [VpnService API](https://developer.android.com/reference/android/net/VpnService)、[VPN 政策解释](https://support.google.com/googleplay/android-developer/answer/12564964?hl=en)、[Android 闹钟指南](https://developer.android.com/develop/background-work/services/alarms)、[特殊权限指南](https://developer.android.com/training/permissions/requesting-special)、[前台服务/全屏意图要求](https://support.google.com/googleplay/android-developer/answer/13392821?hl=en)、[Ads / Malware / Device and Network Abuse](https://support.google.com/googleplay/android-developer/answer/9857753) | VPN 用途、加密和流量处理；`USE_EXACT_ALARM` 核心用途；`USE_FULL_SCREEN_INTENT` 自动授予范围、用户同意和申报必须分别对照 Play 条款，Android API 行为不能替代 Play 审查。 |
| Age Signals | [Play Age Signals API](https://developer.android.com/google/play/age-signals/overview)、[美国州应用商店法律变更说明](https://support.google.com/googleplay/android-developer/answer/16569691)、[User Data](https://support.google.com/googleplay/android-developer/answer/10144311?hl=en) | 年龄/家长同意数据限于接收应用内的法定年龄合规用途；禁止广告、分析、画像及一般性对外分享。 |

正文末尾的调查、帮助社区、联系支持及七项 Privacy/Deception/Device Abuse 侧栏已与政策正文目标区分。本轮重新核对了声明表短链、后台位置/所有文件短链、反馈问卷、社区和联系支持入口：声明表短链暴露了指向既有 `answer/9214102` 的重定向目标；2026-10-24 再次直开后台位置和所有文件两个精确短链，前者仍 HTTP 429、后者仍 Cache miss，均未暴露重定向。另从综合权限政策页的独立 Help 链接观察到旧路由 `answer/9956427` 重定向到现行 `answer/10467955`；这证明的是该 Help 路由，不证明失败的 `goo.gle/play-help-all-files-access` 短链与之等价。各目标访问结果和与现有专题的关系见下表及逐 URL 审计台账（快照：`../source-page-audit.csv`，未导入本仓库）。抓取失败不代表申报义务不存在，账号专属表单须在开发者账号中核实。

### 当前综合页末尾的短链、反馈与支持目标

| 页面直链 | 目标页与本政策的关系 | 核验状态 |
| --- | --- | --- |
| [权限声明表单短链](https://goo.gle/play-permission-decl-form) → [Play Console 权限声明帮助](https://support.google.com/googleplay/android-developer/answer/9214102?hl=en) | 短链错误响应暴露了规范帮助页重定向目标；规范帮助页已在[权限声明专题](../permissions-declaration/permissions-declaration.zh-CN.md)单独打开和分析。它解释 Console 声明流程，不是新的权限资格豁免。 | 短链请求返回 Internal Error；重定向目的地可识别，正文通过规范 URL 单独核验。 |
| [后台位置帮助短链](https://goo.gle/play-help-background-location) | 综合权限页的“important permission requirements”锚点 35 指向此短链；相邻锚点 36 直接打开 [Background Location Help](https://support.google.com/googleplay/android-developer/answer/9799150?hl=en)，但不能据此认定短链与规范页相同。 | 2026-10-23 从现行父页重试锚点 35 返回 HTTP 429；2026-10-24 精确短链直开仍 HTTP 429。附加 `?hl=en` 的请求不被抓取工具接受，未观察到重定向。目标仍未确认，不能按 slug 推断；规范帮助页是独立已核验目标。 |
| [所有文件访问帮助短链](https://goo.gle/play-help-all-files-access) | 综合权限页“Android R requirements”锚点 43 指向此短链；另一个独立 Help 锚点 39 经旧路由 `answer/9956427` 重定向至现行 [All files access Help](https://support.google.com/googleplay/android-developer/answer/10467955)。两条路由不得合并推断。 | 2026-10-23 从现行父页重试锚点 43 为 Cache miss；2026-10-24 精确短链直开仍为 Cache miss，均未暴露重定向。锚点 39 的旧路由→现行页跳转已直接观察。短链目标仍未确认，不能按 slug 推断。 |
| 综合权限页的 All files Help 路由：[answer/9956427](https://support.google.com/googleplay/android-developer/answer/9956427) → [answer/10467955](https://support.google.com/googleplay/android-developer/answer/10467955) | 综合权限页另一个可见 Help 链接实际跳转至现行 All files access 正文。正文限定 Android 11/API 30+ 的 `MANAGE_EXTERNAL_STORAGE`；`READ_EXTERNAL_STORAGE` 不受该规则影响。 | 跳转链于 2026-10-23 直接观察；`answer/10467955` 正文已重开。它与上一行失败的 goo.gle 短链分开记录。 |
| [政策反馈问卷](https://google.qualtrics.com/jfe/form/SV_9YPSYrwjw03d7cG/?Source=9888170) | 页面反馈入口，不是申报步骤、政策条款或延期申请。 | 缓存未命中；无问卷正文或政策后代可审阅。 |
| [帮助社区入口](https://support.google.com/googleplay/android-developer/community?help_center_link=CKHR8gcSNlBlcm1pc3Npb25zIGFuZCBBUElzIHRoYXQgQWNjZXNzIFNlbnNpdGl2ZSBJbmZvcm1hdGlvbg&hl=en) | 动态社区导航，不是权威政策正文。 | 缓存未命中；未读取社区讨论。 |
| [联系支持](https://support.google.com/googleplay/android-developer/gethelp) → [Play Console 帮助与支持](https://play.google.com/console/u/0/developers/help-and-support) | 重定向到需要开发者账号的支持流程；不是公开政策页。 | 账号登录受限；未提交支持请求。 |

七项 Privacy/Deception/Device Abuse 侧栏与政策正文链接分开记录，且对应主题已有独立政策页或 URL 审计。上表目标及失败/重定向细节同步见递归链接图（快照：`../google-play-policy-link-graph.md`，未导入本仓库）第 4.62 节。高价值子页已在上表关联专题中摘要，Android API、示例、导航页和更深后代仍按台账标注为部分覆盖；不声称无限递归闭合。

## Android 权限最小化最佳实践与扫码替代方案

**核对日期：2026-10-23。** 这条分支从综合权限政策的 Android 权限概览与“最小化权限请求”建议展开，跟进运行时授权最佳实践，并重点核对相机权限的扫码替代方案。Android 指南解释实现方式；Play 资格、受限权限、醒目披露、Data safety 和 Console 声明仍须分别按 Play 条款判断。

| 链路 | 目标页内容及与 Play 政策的关系 | 核验范围 |
| --- | --- | --- |
| [Minimize your permission requests](https://developer.android.com/privacy-and-security/minimize-permission-requests) → [Request runtime permissions](https://developer.android.com/training/permissions/requesting) · [App permissions best practices](https://developer.android.com/training/permissions/usage-notes) | 仅在功能确实需要时、由用户进入该功能后请求；先评估粗略位置、Photo/Contact Picker、SAF、系统 Intent、用途专用 API 等窄范围方案。拒绝或撤销后应停止相应访问并提供合理降级，不应预先假定权限组会固定授权组内所有权限。最佳实践还要求盘点 SDK 权限；后台位置应对核心功能不可或缺；SMS/通话权限须满足默认处理器条件。 | 最小化指南最近更新于 2026-08-19；权限最佳实践页最近更新于 2026-10-16。主要正文与关键直链已核验；全部代码/API 后代仍未穷尽。 |
| 最小化指南 → [`Intent.ACTION_DIAL`](https://developer.android.com/reference/android/content/Intent#ACTION_DIAL) | Android 将号码交给拨号界面，由用户明确发起通话；相较直接拨号的 `ACTION_CALL`，该用户确认流程可避免声明 `CALL_PHONE`。若应用本身承担默认拨号器角色，官方 API 另指向 `TelecomManager.placeCall()`；应按实际角色和产品流程选 API。 | 父页带 `authuser=4` 的参考页点击返回 Cache miss；规范 `Intent` API 页面已单独打开并核对 `ACTION_DIAL` / `ACTION_CALL` 成员，其他近万行 API 成员未穷尽。 |
| 最小化指南 → [Google Code Scanner（Android）](https://developers.google.com/ml-kit/vision/barcode-scanning/code-scanner) → [ML Kit Android 扫码指南](https://developers.google.com/ml-kit/vision/barcode-scanning/android) · [ML Kit 条码扫描总览](https://developers.google.com/ml-kit/vision/barcode-scanning) | 只需标准扫码界面时，Google Code Scanner 通过 Google Play 服务完成取景和识别，应用无需请求 `CAMERA`；官方称图像处理在设备端完成，Google 不存储图像或扫描结果。需要自定义 UI 或更复杂流程时可用 ML Kit Barcode Scanning API；应按实际图像来源和相机实现核对权限，不能把自定义 API 一概视为无相机权限。 | 两个实现指南与条码总览已打开。扫码 API 文档列举结果中可能包含 URL、联系人、Wi‑Fi、电话、短信等值；只读取功能所需结果并按[用户数据政策](../user-data/user-data.zh-CN.md)判断告知、用途和分享。 |
| Code Scanner → [ML Kit 模型安装路径](https://developers.google.com/ml-kit/tips/installation-paths) → [Google Play 服务按需模块安装](https://developers.google.com/android/guides/module-install-apis) | Code Scanner 使用可按需下载的未打包模块；可配置安装期下载，也可通过 `ModuleInstallClient` 检查可用性、请求安装、跟踪进度和处理错误。ML Kit 还提供打包模型：体积较大但可立即使用；按需模块较小，但首次使用可能要等待下载。应处理模块未就绪/失败，不能假定设备已安装。 | 安装路径指南与模块安装指南的相关章节已读；所有模块 API、其他模型类型及示例的更深技术后代仍为部分覆盖。 |
| 扫码指南 → [Barcode 结果对象](https://developers.google.com/android/reference/com/google/mlkit/vision/barcode/common/Barcode) · [Google Code Scanner options](https://developers.google.com/android/reference/com/google/mlkit/vision/codescanner/GmsBarcodeScannerOptions.Builder) · [Google Code Scanner client](https://developers.google.com/android/reference/com/google/mlkit/vision/codescanner/GmsBarcodeScanner) · [ML Kit BarcodeScanner options](https://developers.google.com/android/reference/com/google/mlkit/vision/barcode/BarcodeScannerOptions.Builder) | 参考页显示结果对象可暴露原始值、格式及解析后的联系人、Wi‑Fi、位置、电话、短信和 URL 等类型；配置项可限制识别格式、启用自动缩放或调整扫描选项。只扫描应用实际支持的格式可减少不必要处理并提升速度，但不替代结果数据的用途和披露审查。 | 参考页是大型 API 索引；本轮选读与扫码相关的类/方法，不代表所有成员、继承方法或相邻 API 均已审阅。 |
| ML Kit Android 扫码指南 → [Kotlin 示例](https://github.com/googlesamples/mlkit/blob/f1047837fe1e02d58063bfc30b830fad23ffbc35/android/android-snippets/app/src/main/java/com/google/example/mlkit/kotlin/BarcodeScanningActivity.kt) · [Java 示例](https://github.com/googlesamples/mlkit/blob/f1047837fe1e02d58063bfc30b830fad23ffbc35/android/android-snippets/app/src/main/java/com/google/example/mlkit/BarcodeScanningActivity.java) → [Quickstart 目录](https://github.com/googlesamples/mlkit/tree/master/android/vision-quickstart) · [Material Showcase 目录](https://github.com/googlesamples/mlkit/tree/master/android/material-showcase) | Kotlin/Java 代码样例按用户传入的 `InputImage` 扫描，并演示读取原始值、URL 和 Wi‑Fi 字段（包括 SSID/密码）；这是实现示例，不是 Play 权限批准或可直接照搬的产品数据处理方案。动态仓库目录已尝试打开；目录内其余文件与构建配置未逐项审阅。 | 两份代码文件已读取；两个 GitHub 示例目录的页面框架已打开，完整仓库文件树和后代未展开。 |
| Code Scanner → [Google Maven Repository](https://maven.google.com/web/index.html) · [Maven Central](https://search.maven.org/artifact) · [ML Kit community](https://developers.google.com/ml-kit/community) | 这些链接提供依赖仓库与 SDK 支持入口，不是权限资格或政策解释。Google Maven 返回动态目录壳；Maven Central 本轮只返回 JavaScript 不可用提示；ML Kit 社区页列出发布说明、Stack Overflow 和问题跟踪渠道。 | 均已单独尝试并写入逐 URL 审计台账（快照：`../source-page-audit.csv`，未导入本仓库）；仓库中实际 SDK 版本、发布状态和许可证应在构建/发布时重新核对。 |

**实施核对顺序：** 从用户触发的功能开始评估最窄 API；需要扫码时先判断系统 Code Scanner 是否满足，不满足再评估自定义 ML Kit 和相机权限；盘点应用与 SDK 的 Manifest/数据读取；限制对扫描结果的解析、留存和分享；在模块首次下载、用户取消/拒绝及扫描失败时提供可理解的降级；最后独立校验 Play Console 声明、隐私政策、显著披露与 Data safety 一致性。Android 示例、API 或系统权限获准都不能替代 Play 审核。

本分支核验了权限最小化与扫码替代路径的主要正文、关键 API、模型安装章节、样例代码及支持入口。大型 API 的全部成员、动态仓库与 GitHub 仓库的所有文件、视频/页脚导航及其更深后代仍未穷尽；逐目标状态以来源台账为准，不声称递归闭合。

## 推荐审查流程

1. 从 Manifest、代码、SDK 和远程配置列出权限及实际数据读取点。
2. 对每个权限写明对应的已实现核心功能、商店页说明、用户预期和是否有更窄替代。
3. 标注敏感数据用途、是否后台访问、第三方接收方和同意流程。
4. 检查 Play Console 声明/视频/审核材料；对 SMS/Call Log、All files、QUERY_ALL_PACKAGES、Accessibility、Health Connect、精确闹钟等受限事项重点复核。
5. 在用户拒绝、撤回或失去默认处理器状态时验证应用是否停止访问并保持合理可用。
6. 按 2027-01-27 前置完成联系人和 Location Button 的产品、代码、披露及申报迁移。

## 关联页面

- [用户数据政策](../user-data/user-data.zh-CN.md) · [Data safety 表单](../data-safety/data-safety.zh-CN.md)
- [最小权限替代方案](https://support.google.com/googleplay/android-developer/answer/16935362?hl=zh-CN)
- [SMS 和通话记录权限](https://support.google.com/googleplay/android-developer/answer/10208820?hl=zh-CN)
- [SMS 和通话记录专题摘要](../sms-call-log/sms-call-log.zh-CN.md)
- [Play Console 权限声明与审核](../permissions-declaration/permissions-declaration.zh-CN.md)
- [后台位置信息](https://support.google.com/googleplay/android-developer/answer/9799150?hl=zh-CN)
- [健康应用政策](https://support.google.com/googleplay/android-developer/answer/16679511?hl=zh-CN)
- [Contacts Picker](https://developer.android.com/about/versions/17/features/contact-picker) · [Location Button](https://developer.android.com/guide/topics/permissions/private-alternatives/location-button)
- 官方：[Permissions and APIs that Access Sensitive Information](https://support.google.com/googleplay/android-developer/answer/16558241?hl=en) · [Policy Deadlines](https://support.google.com/googleplay/android-developer/table/12921780?hl=en)

## 覆盖状态

已整理综合帮助页的主要专项章节，并深入跟进 `QUERY_ALL_PACKAGES` 的 Play 资格、个人贷款禁用规则、Android 11+ 默认过滤、`<queries>` 最小声明和测试流程。包可见性主指南及五个核心后代已打开；大型 PackageManager API 的相关方法已选读，AAR/Provider/Intent/Service 的技术后代仍部分未展开。联系人规则的生效预告及详细预览已复核，核心资格、Contact Picker 替代方案、声明要求和数据披露边界见联系人和前台位置专题（[联系人与前台位置权限：最小范围和替代方案](../contacts-location-permissions/contacts-location-permissions.zh-CN.md)）；现行综合页面的中文版本未能独立读取，其他政策/技术后代也仍有未闭合分支。逐 URL 状态以台账为准。
