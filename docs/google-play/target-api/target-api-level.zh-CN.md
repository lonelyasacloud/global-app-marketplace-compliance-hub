---
id: google-play.target-api-level
platform: google-play
language: zh-CN
authority: normative
status: current
kb_checked_at: 2026-10-24
review_due: 2027-01-24
regions: [global]
topics: [target-api, target-sdk, android-migration, release-deadline]
snapshot_id: play.target-api-level
snapshot_package: "GooglePlay-KnowledgeBase-2026-10-24-review.zip"
coverage_status: "detailed-summary"
source_url: "https://support.google.com/googleplay/android-developer/answer/11926878?hl=en"
source_url_zh: "https://support.google.com/googleplay/android-developer/answer/11926878?hl=zh-CN"
---

# Google Play 目标 API 级别要求与 Android 迁移

> **导入说明（Google batch 2）。** 本页正文取自 2026-10-24 Google Play 知识库快照里已经分开的中文改写（`play.target-api-level`，核对日 2026-10-24），不是 Google 已发布中文页面的逐字文本。英文官方页面是效力来源。`kb_checked_at` 使用快照源文件记录的核对日；本次导入没有重新打开线上官方页面。文中“本知识库”“本库”“本地专题”描述的是该快照知识库的覆盖范围，不是本仓库已经导入的页面清单。快照里指向尚未导入本仓库的专题、链接图、台账或 CSV 的相对链接，已改为文字提及；指向 Google batch 1 或本批七个专题的相对链接已改到本仓库路径。快照记录 Play Help 的 `?hl=zh-CN` 页面仍无法读取，因此 Play 规则的中文摘要依据可读的英文正文。抓取失败不表示政策已经变更。Android 迁移指南的英文和简体中文视图都已阅读且仍然一致；页脚分别显示 2026-10-16 与“最后更新时间 (UTC)：2026-10-17”，快照没有记录对应的政策内容差异。本页 Play 提交与可见性要求的证据等级是 `normative`。Android 迁移和行为变更指南是 implementation note，不能单独证明 Play 分发资格。不同设备形态的门槛保持分开，本页不把规则收成单一 API 级别。

**核对日期：2026-10-24。** Google Play 用目标 API 规则推动新应用和更新适配近期 Android 版本。它有两种不同后果：新应用/更新可能被阻止提交；旧应用可能对运行较新 Android 版本的新用户不可见。具体门槛按外形设备不同，不能只看一张“API 36”表。

**2026-10-24 双语来源复核：**重新打开当前 Target API Help，并从页面尾随链接打开 Google Play Shorts 指南；API 门槛、旧应用可见性和 2026-11-01 延期终点未见实质变化。Help 的 `?hl=zh-CN` 页面仍无法读取，因此 Play 规则中文摘要继续依据可读英文正文。Android 官方迁移指南的英文和简体中文视图仍一致；页脚分别显示 2026-10-16 与“最后更新时间 (UTC)：2026-10-17”，未发现政策内容差异。Target API 帮助导航明确编号为 1–30（含 Help Center 首页和本页），第 30 项是 Version codes；编号清单之后另有一个未编号的 Shorts 指南链接。该 Shorts 页面已打开并纳入既有双语专题；它是精选素材/内容审核指南，不是 Target API 要求。延期表单仍只对收到不合规警告/问题通知的受影响应用开放；请在账号内核验。

## 当前门槛

### 新应用和更新的提交门槛

自 **2026-08-31** 起，新应用和更新必须满足以下目标 API 才能提交。具体规则以 Play 的最新日期表为准。

| 应用类型 | 目标 API 级别 | 生效日期 |
| --- | ---: | --- |
| 手机、平板及 Android Auto | Android 16 / API 36 或更高 | 2026-08-31 |
| Wear OS | Android 15 / API 35 或更高 | 2026-08-31 |
| Android Automotive OS | Android 15 / API 35 或更高 | 2026-08-31 |
| Android TV | Android 14 / API 34 或更高 | 2025-08-31 |
| Android XR | Android 14 / API 34 或更高 | 2026-08-31 |

### 旧应用对新用户的可见性门槛

这是另一项规则：旧应用目标 API 过低时，不会面向运行高于其目标 API 的 Android 版本的新用户提供。已安装用户不因此失去使用、重新发现或重新安装应用的资格；应用仍需受其自身支持的 Android 版本限制。

| 应用类型 | 旧应用最低目标 API | 低于门槛时的影响 |
| --- | ---: | --- |
| 手机、平板及 Android Auto | Android 15 / API 35 | 对运行高于应用目标 API 的设备新用户不可见 |
| Wear OS | Android 14 / API 34 | 同上 |
| Android TV | Android 13 / API 33 | 同上 |
| Android XR | Android 14 / API 34 | 同上 |
| Android Automotive OS | Android 12L / API 32 | 同上 |

系统版本不高于应用目标 API 的新用户仍可能看到旧应用。用户通过商店深链进入时，Google Play 可能告知该应用是为较旧 Android 版本构建、无法在其设备安装。

## 延期、资格和退出分发

- 受影响且不符合规则的应用可以申请将广泛分发延至 **2026-11-01**。Google 说明，只有不符合政策的应用会收到 Play Console 警告/通知；表单入口位于相应警告或 Policy status 问题详情中。它不是所有开发者都可通用提交的公开表单。
- 公开帮助页不能确认某个开发者账号或包名是否收到表单、是否符合资格或延期是否已获批；应在对应 Play Console 通知和 Policy status 页面核实。
- 被限制的旧应用不会影响已安装用户；Google 说明这些用户仍可发现、重新安装，并在应用支持的 Android 版本上使用。
- 若不再向新用户提供应用，可在 Console 取消发布。取消发布后，现有用户仍可使用应用并接收应用更新；新用户不会在 Google Play 找到并下载它。具体操作和账号状态需登录 Console。
- 明示例外是**永久私有且仅供特定组织内部使用**的应用。仅仅称为“企业应用”或存在登录限制，不足以据此认定符合该例外。

## 目标 API 与最低系统版本

`targetSdkVersion`（Gradle 配置或 Manifest 中的目标 API）声明应用针对哪些 Android 行为规则进行适配。它不同于 `minSdkVersion`：提高目标 API 不会自动阻止应用在较旧系统运行；实际最低兼容系统由 `minSdkVersion` 等配置决定。也不要只检查源码：核对最终构建包和合并后的 Manifest，确认提交到 Play 的版本使用了预期值。

### 单独的 Google Play 兼容性发布门槛：16 KB 内存页

这是与 API 36 日期矩阵分开的发布要求：在 Google Play 上分发、目标为 Android 15 / API 35 或更高的应用，必须支持 64 位设备的 16 KB 内存页。自 **2027-02-01** 起，不支持 16 KB 的应用更新将无法发布。Android 16 的 4 KB 兼容模式只是设备端兼容运行和测试辅助，不能当作这项 Play 发布要求的长期替代方案。

若应用只使用 Java/Kotlin（包括其全部 SDK/依赖），官方称其已支持 16 KB；若应用、第三方 SDK 或应用构建器包含 `.so` 原生库，则需逐个检查并更新。核对 AAB 中原生库的 ZIP/ELF 对齐和最终 Play 生成包，在 16 KB 环境测试。官方建议 AGP 8.5.1+、NDK r28+ 并确认预编译依赖兼容。详见 [Support 16 KB page sizes](https://developer.android.com/guide/practices/page-sizes)。这是一个有独立截止日期的 Play 兼容性门槛，不等同于“目标 API 级别达到 API 36”。

### 16 KB 迁移的直接工具与引擎指南

这些是实现/测试指导，不会改变 Play 的 2027-02-01 发布门槛。Android 官方指南的重点是检查**最终包中的每个原生库和所有 ABI**，而非只看源码或某个 SDK 声称兼容：

- **打包与 ELF：** 对未压缩 `.so`，推荐 AGP 8.5.1+；官方警告 AGP 8.3–8.5 的构建即使本机看似可运行，`bundletool` 生成的 Play APK 仍可能因 ZIP 未对齐而无法安装。NDK r28+ 默认使用 16 KB ELF 对齐；NDK r27 及更旧版本需按官方指引设置链接器参数。所有预编译 `.so` 也须换成兼容版本或重新构建；逐 ABI 检查供应商 SDK。压缩 `.so` 是旧 AGP 的备选方案，但会增加安装占用，可能增加低存储设备安装失败风险。
- **验证：** 在 Android 15 SDK 或更高版本的模拟器/设备上测试；`adb shell getconf PAGE_SIZE` 应返回 `16384`。在 AAB 上运行 `bundletool dump config --bundle=<app.aab> | grep alignment`，确认包含 `PAGE_ALIGNMENT_16K`；再对最终 APK 使用 `zipalign -c -P 16 -v 4 app.apk`。逐个检查每个 64 位原生库的所有 ELF `LOAD` 段，不要只看 AAB 设置或单个库；检查代码是否硬编码 4096 或依赖固定页大小，需要运行时页大小时使用 `sysconf(_SC_PAGESIZE)` 或 `getpagesize()`。Play Console App Bundle Explorer 可作为另一处构建兼容性线索，不能替代 16 KB 环境运行测试。
- **RELRO 与运行崩溃：** NDK r27 及更旧版本构建的 `.so` 若 RELRO 区段不适配 16 KB 页，可能在运行时段错误。官方建议用 `llvm-readelf -Wl` 检查 `GNU_RELRO`；当它与后续可写数据共用 `LOAD` 段时，按 `(VirtAddr + MemSz) % 0x4000 == 0` 检查边界。若 RELRO 独占一个 `LOAD` 段，则还需结合相邻可写段的起始边界判断，不能机械套用同一取模结果。此类 ELF 检查是运行测试的补充。
- **游戏引擎：** Android Developers 当前 [Unity 指南](https://developer.android.com/games/engines/unity/unity-on-android)（更新于 2026-02-26）列出 Unity 2021、2022 和 Unity 6 支持；[Unity 6000.0 Android 手册](https://docs.unity3d.com/6000.0/Documentation/Manual/android-requirements-and-compatibility.html)建议使用 6000.0.38f1 或更高、更新原生插件，并注意 Unity Editor 会在 `.so` 不对齐时给出构建警告。Unity 官方平台帖列出的旧 LTS 补丁号受支持渠道/版本更新影响，使用前应回查 Unity 当前版本说明。Android Developers [Unreal on Android](https://developer.android.com/games/engines/unreal/unreal-on-android) 页面（更新于 2026-10-07）称 Unreal 5.6+ 支持 16 KB；它链接的 Epic 5.6 release notes 本次抓取超时，未从该链接推断额外细节。
- **构建升级：** [Android Gradle Plugin Upgrade Assistant](https://developer.android.com/build/agp-upgrade-assistant) 可协助升级 AGP 与匹配 Gradle/第三方插件；升级前备份，检查必需/推荐步骤，升级后同步、构建并测试。它只辅助升级，不会替代对 AAB/APK 的 16 KB 兼容验证。
- **相关参考与脚本边界：** [NDK 预编译库指南](https://developer.android.com/ndk/guides/prebuilts)说明预编译库需按 ABI 选择；[zipalign 工具文档](https://developer.android.com/tools/zipalign)说明 `-P 16` 以及 APK 签名顺序。Android 文档链接的 `check_elf_alignment.sh` 在 Code Search 页面无法直接读取，但已从 [AOSP Gitiles 当前分支](https://android.googlesource.com/platform/system/extras/+/refs/heads/main/tools/check_elf_alignment.sh)打开源码。源码当前实现用 `head -1` 只取每个 ELF 的第一个 `LOAD` 对齐值，因此脚本显示 `ALIGNED` 不足以证明其余 `LOAD` 段均符合要求；请按 Android 指南逐项检查 `objdump -p` 输出。脚本内提示的 Build Tools `35.0.0-rc3` 安装命令可能过时，当前 Android 指南要求 Build Tools 35.0.0 或更高版本。源码页面可能更新，使用时以当前 Android 指南为准。

对自定义内存分配器（不是 Android 标准 `scudo` 分配器）还需按运行时页大小调整释放阈值、优先填满已有页、将内存池按页大小对齐，并及时归还大型缓存页；具体做法见上述 Android 官方 16 KB 指南。普通 Java/Kotlin 应用无需照搬这些原生内存优化步骤，但仍可在 16 KB 环境回归测试。

## Android 16 行为变化清单（官方页面更新于 2026-10-16）

提高目标 API 会启用一部分按 `targetSdkVersion` 生效的平台行为；另一些变化对所有在 Android 16 上运行的应用生效。下表把两类分开。大多数条目是平台兼容性/实现事项；Android 16 行为清单本身不会自动增加 Play 义务，但 16 KB 页面大小另有独立 Play 发布门槛（见上文）。涉及健康、照片或网络权限时，也要另行检查 Play 的权限、隐私和 Data safety 要求。迁移指南建议至少提前三个月开始并逐个大版本验证。

### 仅适用于目标 API 36+ 的变化

| 领域 | 变化与迁移要点 |
| --- | --- |
| 系统栏与边缘到边缘 | Android 16 上，目标 API 36 的应用不能再退出 edge-to-edge；Android 15 上该退出开关仍有效。验证状态栏、导航栏、挖孔屏、键盘 Insets 与可点击区域；实现参考 [Compose window insets](https://developer.android.com/develop/ui/compose/system/insets) 和 [Views edge-to-edge](https://developer.android.com/develop/ui/views/layout/edge-to-edge)。 |
| 返回导航与字体 | 预测性返回动画默认启用，旧 `onBackPressed` 不再调用且 `KEYCODE_BACK` 不再分发；迁移到受支持 API，临时退出只作过渡。`elegantTextHeight` 在目标 API 36 时会被忽略；检查阿拉伯文、老挝文、缅甸文、泰米尔文等文字布局。参考 [Predictive Back 迁移指南](https://developer.android.com/guide/navigation/custom-back/predictive-back-gesture)。 |
| 大屏自适应 | 最小宽度至少 600dp 的大屏上，方向、可调整大小和宽高比限制被忽略，窗口按全屏/多窗口尺寸呈现；例外包括游戏、用户在系统设置中明确选择旧行为及小于 `sw600dp` 的屏幕。测试折叠、旋转、多窗口与状态保存；退出兼容模式只是临时措施，API 37 起不会继续适用。参见 [Adaptive Apps](https://developer.android.com/adaptive-apps)。 |
| 固定频率工作 | `scheduleAtFixedRate` 因进程生命周期而错过多次后，应用恢复时最多立即补跑一次，不再集中补齐所有遗漏次数。检查依赖补跑次数的计时/同步逻辑。 |
| 健康权限 | 对目标 API 36+ 的应用，相关健康 API 从 `BODY_SENSORS` / `BODY_SENSORS_BACKGROUND` 改用细分的 `android.permission.health` 权限，例如 `READ_HEART_RATE`、`READ_HEALTH_DATA_IN_BACKGROUND`。移动应用还需在健康权限流程中提供展示隐私政策的 Activity 和权限理由；与 [Health Connect 指南](https://developer.android.com/health-and-fitness/health-connect)及健康数据 Play 声明一起核对。 |
| 本地网络隐私 | Android 16 文档描述的是分阶段、开发者选择加入的本地网络保护测试，不等同于 API 36 的强制 Play 申报期限。被保护的本地 TCP/UDP、组播/广播及 `.local` 发现流量可能要求附近设备权限；投屏、设备发现要验证用户拒绝/撤销路径，并跟踪平台后续权限方案。 |
| 照片和视频选择 | Android 16 设备上，目标 SDK 36+ 应用请求照片/视频访问时，系统照片选择器会预选应用自有媒体；用户可取消选择，取消会撤销应用对相应媒体的访问。不能把预选理解成永久授权；每次按实际 URI 授权处理。 |
| 蓝牙与安全 | 文档增加配对丢失/加密变化广播及关联设备移除 bond 的公开 API；不同 OEM 的广播实现可能不同，应保留兼容处理。`MediaStore#getVersion()` 改为每个应用唯一，不可从版本字符串推断设备信息；Safer Intents 在 API 36 是显式启用的严格匹配选项。Mali GPU IOCTL 过滤描述针对特定 Pixel/Mali 设备，不应泛化为所有应用的 Play 审核规则。 |

### 对所有运行 Android 16 的应用生效的变化

| 领域 | 变化与迁移要点 |
| --- | --- |
| 后台任务配额 | JobScheduler 配额会受待机桶、任务开始时是否前台及是否与前台服务并行影响，WorkManager、JobScheduler、DownloadManager 均可能受影响。检查停止原因；用户发起的数据传输评估 [User-Initiated Data Transfer jobs](https://developer.android.com/develop/background-work/background-tasks/uidt)，不要以通用 FGS 绕过任务配额。官方还建议使用 `getPendingJobReasonsHistory` 辅助诊断。 |
| Job 生命周期 | 未持有 `JobParameters` 强引用而遗弃的任务可能返回 `STOP_REASON_TIMEOUT_ABANDONED`；频发时系统会降低其调度频率。WorkManager、AsyncTask、DownloadManager 管理生命周期的场景不受此特定问题影响。`setImportantWhileForeground()` 不再有效，`isImportantWhileForeground()` 返回 `false`。 |
| 广播顺序与 ART | 不同进程之间的广播优先级不再保证全局排序，优先级限于系统边界内；跨进程协调需换显式协调机制。避免依赖非 SDK/ART 内部结构，因为 ART 模块也能通过 Google Play 系统更新推送到旧 Android 版本设备。参见 [非 SDK 接口限制](https://developer.android.com/guide/app-compatibility/restrictions-non-sdk-interfaces)。 |
| 16 KB 内存页（平台行为） | Android 16 为 4 KB 对齐应用提供兼容运行模式和提示；这只说明部分应用可在设备上兼容运行。另有独立的 Google Play 发布门槛：目标 API 35+ 的应用自 2027-02-01 起，未支持 16 KB 的更新不能发布，见上文和[官方指南](https://developer.android.com/guide/practices/page-sizes)。 |
| 无障碍与导航 | `announceForAccessibility` / `TYPE_ANNOUNCEMENT` 被弃用；按界面变化、关键状态或错误选择窗格标题、Live Region 或错误语义等替代方案。对已正确迁移预测性返回的应用，三键导航长按返回也可预览返回动画。 |
| 图标和大屏投影 | Android 16 QPR 2 起，系统可为未提供单色层的应用图标自动套用主题。虚拟设备所有者也可在受管理的虚拟设备上覆盖方向/宽高比/可调整大小限制；测试车载显示屏、Chromebook 等投影场景。 |
| Intent 与配对隐私 | Intent 重定向防护默认增强；只有确认合法兼容需求时才考虑关闭防护。伴侣设备配对不再直接向应用告知发现超时，系统先向用户显示对话框，用户关闭后应用收到 `RESULT_USER_REJECTED`。 |
| 蓝牙配对丢失 | 重新连接鉴权失败时，系统断开链路、保留本机配对信息并提示用户重新配对，减少应用自行重配导致的意外体验；同时结合目标 API 页的新广播说明处理 OEM 差异。 |

以上两类清单不能替代完整迁移链：仍需查看从当前目标版本到 API 36 的每个 Android 主版本行为变化，以及应用实际使用的 SDK/API。权限变化要与[敏感权限](../sensitive-permissions/sensitive-permissions.zh-CN.md)、健康数据（快照：`health-apps-and-health-connect.md`，未导入本仓库）、[照片/视频权限](../photo-video-permissions/photo-video-permissions.zh-CN.md)、[后台位置](../background-location/background-location.zh-CN.md)和[权限声明审核](../permissions-declaration/permissions-declaration.zh-CN.md)交叉核对。

权限、健康数据、位置、照片/视频和前台服务等迁移可能同时触发独立 Play 政策或申报要求。API 升级通过不代表敏感权限审核、Data safety 或 Console 声明自动通过，参见[敏感权限与 API](../sensitive-permissions/sensitive-permissions.zh-CN.md)、[照片/视频权限](../photo-video-permissions/photo-video-permissions.zh-CN.md)、[后台位置](../background-location/background-location.zh-CN.md)和[权限声明审核](../permissions-declaration/permissions-declaration.zh-CN.md)。

## 建议的迁移顺序

1. 在 Play Console/工件中确认应用类别、外形设备、所有活跃包和轨道，并记录当前 `targetSdkVersion`、`minSdkVersion` 与目标门槛。
2. 用 Android 迁移指南按当前 API 到目标 API 的每个大版本检查行为变化；不要只跳读 API 36 页面。
3. 更新 Android Gradle Plugin、构建工具、SDK 和依赖库；检查第三方 SDK 的兼容版本及合并后的 Manifest 权限。
4. 为 edge-to-edge、返回导航、大屏/折叠屏、后台工作、Intent 安全、本地网络、健康和照片权限拒绝路径制定测试场景；在 Android 16 真机/模拟器和支持的历史系统上验证。
5. 核对所有 Play 政策表单、敏感权限声明、隐私披露、健康/照片/位置权限与目标 API 变更是否一致。
6. 检查最终 AAB 的目标 API、版本和所有外形设备轨道，再安排发布；保留测试结果和 Console 处理记录。

## 官方帮助页正文直链清单（2026-10-24）

以下只统计文章正文中的链接锚点；不把顶部账户通知、反馈控件、帮助社区/联系支持入口、插图或帮助中心推荐侧栏计入政策正文。截至 2026-10-24，简体中文 Play Help URL（`?hl=zh-CN`）仍无法通过浏览工具读取；以下 Play 规则中文说明以可读取的英文官方正文为依据，不表示已完成 Help 两种语言逐句比对。Android 官方迁移指南另有可读取的[简体中文视图](https://developer.android.com/google/play/requirements/target-sdk?hl=zh-cn)，其门槛和延期内容与英文视图一致；两种语言页脚的更新时间相差一天，见下方来源记录。

| 来源页与正文锚点 | 出现次数 / 唯一目标 | 目标页核验及其与本政策的关系 |
| --- | ---: | --- |
| [Target API requirements](https://support.google.com/googleplay/android-developer/answer/11926878?hl=en) → “Permanently private apps”（例外段及 FAQ） | 2 / 1 | [永久私有应用说明](https://support.google.com/googleplay/work/answer/9563481?hl=en)已打开；要求应用只供特定组织使用、仅用于内部发布。该页的直接子链接——Android Enterprise [Developer guide](https://developer.android.com/work/guide)、[Publish private apps](https://support.google.com/work/android/topic/9496238?hl=en)、[Distribute private apps](https://support.google.com/work/android/answer/9495634?hl=en) 和 [App hosting for private apps](https://support.google.com/work/android/topic/9495939?hl=en)——均已打开；分发页说明最多 1,000 个组织，改为公开应用须使用不同包名。Developer guide 仅复核与工作资料、托管配置、专用设备和 SSO 相关的章节，其通用 Android 技术后代未全部递归。发布方法和最佳实践另见下方链接状态表。 |
| 同页 → “migration guide” | 1 / 1 | 旧帮助页链接重定向至 [Android target SDK migration guide](https://developer.android.com/google/play/requirements/target-sdk)；用于 API 升级技术迁移，不改变 Play 的日期门槛。 |
| 同页 → FAQ 中 “unpublish your app” 与 “this Help Center article” | 2 / 1 | 两个锚点指向同一 [取消发布说明](https://support.google.com/googleplay/android-developer/answer/9859350?hl=en)。该页已打开：取消发布会阻止新用户找到/下载应用；目标 API 不合规则只会影响高于应用目标 API 的新用户设备，两者范围不同。一次正文锚点点击遭 Google 反自动化拦截，规范目标页此前已直接打开。 |
| 同页 → “Policy status” | 1 / 1 | [Play Console Policy status](https://play.google.com/console/developers/app/policy-centre)跳转到登录；FAQ 称只有不合规应用会收到通知，延期表单从该警告/问题详情进入，公众页面不能验证某个包是否有资格或是否获批。 |
| [Target API Level Policy](https://support.google.com/googleplay/android-developer/answer/16561298?hl=en) → “Help Center article” | 2 / 1 | 两处锚点均指回上面的现行日期/外形设备门槛页；用于把“新应用和更新一年内、未更新旧应用两年内”的概括规则映射到具体生效日及例外。 |
| 同页 → “migration guide” | 1 / 1 | 指向同一 [Android target SDK migration guide](https://developer.android.com/google/play/requirements/target-sdk)。 |
| 同页 → “2-minute survey” | 1 / 1 | [政策反馈问卷](https://google.qualtrics.com/jfe/form/SV_9YPSYrwjw03d7cG/?Source=11917020)点击返回错误（Cache miss）；这是反馈入口，不是合规要求或政策例外。 |

**正文直链计数：** `answer/11926878` 正文有 6 次锚点、4 个唯一目标；`answer/16561298` 正文有 4 次锚点、3 个唯一目标（两个 Help Center 锚点重复指向同一目标）。帮助中心导航另行核对，不计入正文政策链接：Target API 页有 30 个编号导航项，含 [Help Center 首页](https://support.google.com/googleplay/android-developer?hl=en)和本页；第 30 项为 [Version codes](https://support.google.com/googleplay/android-developer/answer/17367361)，其余 27 个同级文章与该页统一列于应用审核准备专题的相关页面清单（快照：`app-review-preparation.md`，未导入本仓库）。30 项清单之后另有未编号的 [Developer Guide: Getting Started with Google Play Shorts](https://support.google.com/googleplay/android-developer/answer/18611720?hl=en)链接；该指南已打开，详见Shorts 双语专题（快照：`google-play-shorts-creative-guidelines.md`，未导入本仓库），属于功能专项创意/审核指导，不改变 Target API 规则。`Create and set up your app` 首次点击超时后已通过规范 URL 打开全文；`Google Play game services` 只到帮助目录，目录下服务文章未逐项遍历。

政策概览页 `answer/16561298` 的 7 项侧栏（含当前页）也已单独核对，作为政策导航而非正文新增条款：

| 政策侧栏目标 | 与本专题的关系 / 核验状态 |
| --- | --- |
| [Privacy, Deception and Device Abuse](https://support.google.com/googleplay/android-developer/topic/9877467?hl=en) | 已打开的政策分类目录；其 User Data、Sensitive Permissions、Device and Network Abuse、Deceptive Behavior、Misrepresentation 和 Target API 子项分别关联下列专题。本轮一个旧的 Device and Network Abuse 点击返回错误，但现行规范目标已有完整专题和正文审计。 |
| [User Data](https://support.google.com/googleplay/android-developer/answer/10144311?hl=en) | 已打开；见[用户数据专题](../user-data/user-data.zh-CN.md)。它与目标 API 的连接主要在数据收集、披露和权限迁移，不改变 API 日期门槛。 |
| [Permissions and APIs that Access Sensitive Information](https://support.google.com/googleplay/android-developer/answer/16558241?hl=en) | 已打开现行合并页；见[敏感权限专题](../sensitive-permissions/sensitive-permissions.zh-CN.md)。目标 API 改动可能触发新的平台权限行为，但权限资格与申报单独判断。 |
| [Device and Network Abuse](https://support.google.com/googleplay/android-developer/answer/16559646?hl=en) | 现行规范页已有完整正文审计；见设备与网络滥用专题（快照：`device-and-network-abuse.md`，未导入本仓库）。一次侧栏点击失败不表示目标页未审。 |
| [Deceptive Behavior](https://support.google.com/googleplay/android-developer/answer/17006354?hl=en) | 已打开；见欺骗性行为专题（快照：`deceptive-behavior.md`，未导入本仓库）。它与 API 升级的联系限于应用实际行为、兼容性和用户呈现，非同一项政策。 |
| [Misrepresentation](https://support.google.com/googleplay/android-developer/answer/9888689?hl=en) | 已打开；见虚假陈述专题（快照：`misrepresentation.md`，未导入本仓库）。主要用于核对商店资料和实际功能的一致性。 |
| 当前 Target API 页面 | 当前页自身，已打开全文并纳入上面的正文锚点清单。 |

延期日期为 2026-11-01；帮助页一般段落仍写“later this year”，FAQ 给出只有受影响应用能从 Console 警告详情进入的具体路径。应以账号内实际警告/表单为准。以上侧栏页面的更深后代仍按逐页审计状态处理，不宣称递归闭合。

## 本专题的链接范围与核验状态

| 父页/子页 | 关键目标页 | 关系与状态 |
| --- | --- | --- |
| Play 目标 API 帮助页 | [Target API level requirements](https://support.google.com/googleplay/android-developer/answer/11926878?hl=en) | 2026-10-24 重开全文；逐项核对提交门槛、外形设备矩阵、旧应用可见性、仅限警告详情的延期入口、用户影响和永久私有应用例外。页面 30 个编号导航项后的独立未编号 Shorts 链接也已打开，见Shorts 双语专题（快照：`google-play-shorts-creative-guidelines.md`，未导入本仓库）。 |
| Play 目标 API 帮助页 | [Target API Level Policy](https://support.google.com/googleplay/android-developer/answer/16561298?hl=en) | 已打开。政策概述新应用/更新按最新 Android 大版本一年内、未更新旧应用按两年内的原则；具体日期和外形设备例外以帮助页日期表为准。建议至少提前三个月迁移属于官方建议。 |
| Play 目标 API 帮助页/政策页 | [Android target SDK migration guide（英文）](https://developer.android.com/google/play/requirements/target-sdk)；[简体中文视图](https://developer.android.com/google/play/requirements/target-sdk?hl=zh-cn) | 2026-10-23 已打开两种语言视图；英文页脚显示最后更新于 2026-10-16，简体中文页显示最后更新时间（UTC）为 2026-10-17。两页现行外形设备门槛、2026-11-01 延期和目标 API 配置说明一致；跟进 Android 13–16 行为变化。该一天的页脚差异未显示为政策内容差异。仅展开与 Play 目标 API 迁移有关的技术后代；API 示例等仍未全量递归。 |
| Android 迁移指南 | [Android 16 target behavior changes](https://developer.android.com/about/versions/16/behavior-changes-16)；[Android 16 all-app behavior changes](https://developer.android.com/about/versions/16/behavior-changes-all)；[Android 15 behavior changes](https://developer.android.com/about/versions/15/behavior-changes-15) | 已打开并核对关键差异。Android 16 目标专属变化与所有 Android 16 应用变化分开记录；Android 15 是逐版本迁移链路的一环。 |
| Android 16 两份行为页 | [Compose Insets](https://developer.android.com/develop/ui/compose/system/insets)、[Views edge-to-edge](https://developer.android.com/develop/ui/views/layout/edge-to-edge)、[Predictive Back](https://developer.android.com/guide/navigation/custom-back/predictive-back-gesture)、[Adaptive Apps](https://developer.android.com/adaptive-apps)、[Health Connect](https://developer.android.com/health-and-fitness/health-connect)、[User-Initiated Data Transfer](https://developer.android.com/develop/background-work/background-tasks/uidt)、[Power management resource limits](https://developer.android.com/topic/performance/power/power-details)、[Optimize battery use](https://developer.android.com/develop/background-work/background-tasks/optimize-battery)、[Non-SDK interface restrictions](https://developer.android.com/guide/app-compatibility/restrictions-non-sdk-interfaces)、[16 KB page sizes](https://developer.android.com/guide/practices/page-sizes) | 两个行为源页正文于 2026-10-22 打开；上述高关联技术后代已沿直接链接打开并摘要。16 KB 指南全文已打开，并确认独立 Play 门槛为目标 API 35+ 应用在 64 位设备支持 16 KB、自 2027-02-01 起阻止不兼容更新。这里只展开目标 API / 迁移决策相关分支，不递归 API 参考、代码示例、导航和其他技术后代。 |
| 16 KB 指南直接子页与工具 | [AGP Upgrade Assistant](https://developer.android.com/build/agp-upgrade-assistant)、[Unity on Android](https://developer.android.com/games/engines/unity/unity-on-android)、[Unreal on Android](https://developer.android.com/games/engines/unreal/unreal-on-android)、[NDK prebuilt libraries](https://developer.android.com/ndk/guides/prebuilts)、[zipalign](https://developer.android.com/tools/zipalign)、[Unity 6000.0 Android requirements](https://docs.unity3d.com/6000.0/Documentation/Manual/android-requirements-and-compatibility.html)、[Unity 16 KB support post](https://discussions.unity.com/t/android-unity-engine-support-for-16-kb-memory-page-sizes-android-15/1589588)、[Epic Unreal 5.6 release notes](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-5-6-release-notes?application_version=5.6)、[check_elf_alignment.sh](https://cs.android.com/android/platform/superproject/main/%2B/main%3Asystem/extras/tools/check_elf_alignment.sh) | Android/Unity/NDK/zipalign 的目标页已按 16 KB 相关内容打开并摘要；Epic 5.6 页面超时，Android 源代码浏览器未展示 alignment 脚本正文。Unity 帖与版本手册是有版本时间戳的引擎说明，不是 Play 政策；其余引擎/工具 API、代码示例及孙链接仍未全部展开。 |
| 目标 API 延期 | [Play Console Policy status](https://play.google.com/console/developers/app/policy-centre) | 需开发者账号登录；公开页面不能核实包名级别资格、表单是否开放或审批结果。 |
| 永久私有应用例外 | [Permanently private apps](https://support.google.com/googleplay/work/answer/9563481?hl=en) | 英文正文已打开：私有应用仅对特定组织可见，不进入公开 Play 商店；已展开发布、分发、托管和最佳实践子页。仅限组织内部的目标 API 例外不等于未受管理设备上的 Android 开发者验证豁免，详见开发者验证专题（快照：`../android-developer-verification.md`，未导入本仓库）。 |
| 退出分发 | [Update or unpublish your app](https://support.google.com/googleplay/android-developer/answer/9859350?hl=en) | 已打开。取消发布后现有用户仍可使用和接收更新，新用户无法在 Play 找到/下载。 |

本页覆盖目标 API 规则以及迁移指南中与 API 目标升级直接相关的技术后代，不是 Android Developers 网站所有链接的递归镜像。Google 可调整截止日期和技术行为；发布前应复核官方页面及账号内通知。

## 来源与关联知识库

- [Google Play：Target API level requirements](https://support.google.com/googleplay/android-developer/answer/11926878?hl=en)
- [Google Play：Target API Level Policy](https://support.google.com/googleplay/android-developer/answer/16561298?hl=en)
- [Android Developers：Meet target API requirements](https://developer.android.com/google/play/requirements/target-sdk)
- [Android 16：面向 API 36+ 的行为变化](https://developer.android.com/about/versions/16/behavior-changes-16)
- [Android 16：对所有应用的行为变化](https://developer.android.com/about/versions/16/behavior-changes-all)
- [Google Play：取消发布应用](https://support.google.com/googleplay/android-developer/answer/9859350?hl=en)

相关知识库：[敏感权限与 API](../sensitive-permissions/sensitive-permissions.zh-CN.md)、[权限声明与审核](../permissions-declaration/permissions-declaration.zh-CN.md)、联系人与前台位置（快照：`contacts-location-permissions.md`，未导入本仓库）、[照片/视频权限](../photo-video-permissions/photo-video-permissions.zh-CN.md)、[后台位置](../background-location/background-location.zh-CN.md)。本页是双语结构化摘要，不是政策逐字全文；账户专属状态须登录 Console 核验。
