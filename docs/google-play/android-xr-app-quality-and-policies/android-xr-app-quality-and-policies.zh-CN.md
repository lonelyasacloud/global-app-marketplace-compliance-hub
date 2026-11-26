---
id: google-play.android-xr-app-quality-and-policies
platform: google-play
language: zh-CN
authority: normative
status: current
kb_checked_at: 2026-10-22
review_due: 2027-01-22
regions: [global]
topics: [android-xr, app-quality, privacy, camera, microphone, wearable-devices]
snapshot_id: play.android-xr-policy
snapshot_package: "GooglePlay-KnowledgeBase-2026-10-24-review.zip"
coverage_status: "detailed-summary"
source_url: "https://developer.android.com/docs/quality-guidelines/android-xr?hl=zh-cn"
source_url_english: "https://developer.android.com/docs/quality-guidelines/android-xr"
source_url_immersive_zh: "https://developer.android.com/docs/quality-guidelines/android-xr/immersive?hl=zh-cn"
source_url_immersive_en: "https://developer.android.com/docs/quality-guidelines/android-xr/immersive"
source_url_augmented_en: "https://developer.android.com/docs/quality-guidelines/android-xr/augmented"
source_url_devices: "https://developer.android.com/develop/xr/devices"
source_url_en: "https://developer.android.com/docs/quality-guidelines/android-xr"
source_url_chinese_en: "https://developer.android.com/docs/quality-guidelines/android-xr?hl=zh-cn"
source_url_immersive_chinese_en: "https://developer.android.com/docs/quality-guidelines/android-xr/immersive?hl=zh-cn"
effective_date: "Android XR app policies alongside general Play policy; pages last updated 2026-10-20 UTC; no separate effective date and no 2027-01-27"
---

# Android XR 应用质量与政策要求

> **导入说明（Google batch 8）。** 正文来自已经分开的 2026-10-24 Google Play 知识库快照（`play.android-xr-policy`，核对日 2026-10-22）的改写摘要，不是官方页面的逐字副本。英文官方页面是效力来源。`kb_checked_at` 是快照源文件记录的核对日；本次导入没有重新打开线上官方页面。文中“本知识库”“本库”“本地专题”等说法描述的是该快照库的覆盖范围，不是本仓库已经导入的页面。指向本仓库没有收录的专题、链接图、台账或 CSV 的相对链接改为文字提及。指向 Google batch 1–7 或本批十三个专题的相对链接改为本仓库文件。YAML 核对日是 2026-10-22，开篇写 2026-10-24。这两个快照日期不表示政策变更。英文开发者政策中心列出 Android XR。快照中的简体中文政策中心目录没有对应入口。沉浸式指南的英文和简体中文都已打开。增强体验指南的中文目标返回缓存未命中，因此该节中文依据英文官方页面。该缓存未命中不是政策变更。页面最后更新为 2026-10-20 UTC，没有单独的生效期限。没有 2027-01-27。Android XR App Policies 与全体 Play 政策并行适用。质量清单是操作指导和实现说明，不是合并版开发者计划政策里的新文章。证据等级：XR 应用政策为 Normative；质量和模拟器指导为 Operational 与实现说明。

**核对日期：2026-10-24。** 英文 [Google Play Developer Policy Center](https://play.google/developer-content-policy/) 的 “Other Programs” 列出了 Android XR，并链接到 Android Developers 的质量指南；简体中文政策中心当前没有这个入口。指南同时包含设备形态质量清单和明确的 “Android XR App Policies”。它是 Play 政策目录指向的 Android XR 专项要求，不是合并版 Developer Program Policy 中新增的一篇独立政策。

## 适用设备与体验

| 设备/体验 | 官方指南 | 目录关系 |
| --- | --- | --- |
| XR 头戴设备、有线 XR 眼镜上的全沉浸/半沉浸体验 | [沉浸式体验质量与政策](https://developer.android.com/docs/quality-guidelines/android-xr/immersive) | 英文与简体中文指南均已打开；有线设备让用户直接看见真实环境，必须格外注意旁观者隐私和空间安全。 |
| 音频眼镜、显示眼镜上的轻量增强体验 | [增强体验质量与政策](https://developer.android.com/docs/quality-guidelines/android-xr/augmented) | 英文正文已打开；简体中文目标尝试访问但浏览器返回 Cache miss，因此本页中文摘要依据英文官方正文编译。 |
| 头戴设备、有线 XR 眼镜、音频/显示眼镜的能力差异 | [Android XR 设备类型](https://developer.android.com/develop/xr/devices) | 头戴设备主要支持沉浸式体验；音频/显示眼镜是全天佩戴的智能眼镜，可能带有相机、麦克风和触控板。该页是平台能力说明，不是 Play 准入政策。 |

## 所有 XR 应用都应先遵守的 Play 规则

沉浸式指南明确要求通过 Google Play 分发的应用遵守全部 [Google Play 开发者政策](https://play.google/developer-content-policy/)。XR 专项安全规则进一步禁止应用协助或宣传以下行为：

- 人肉搜索；人脸识别或生物识别身份识别；监视；未经当事人同意的私密图像（NCII）的创建或传播。
- 使用相机识别旁观者并显示其个人身份信息，例如姓名、住址、电话或雇主；利用相机协助制作 NCII 或其他非法内容（包括 CSAM）。
- 在用户未主动参与用户发起任务时持续于后台录音或转写；用麦克风识别非佩戴者或旁观者的声音。
- 更改、调暗或关闭系统强制控制的面向用户/外界 LED，或指示用户这样做；绕过或干扰 LED 被遮挡/损坏时停止录制的防篡改机制。

## 智能眼镜音频体验的相机边界

增强体验页对可穿戴相机给出了更具体的允许/禁止情形：

| 允许 | 禁止 |
| --- | --- |
| 视频通话；环境感知和场景理解。 | 用可穿戴相机进行实时一对多公开直播、公开广播或投放到公开信息流/开放频道；实时识别旁观者身份并披露其个人信息；制作 NCII 或非法内容。 |

麦克风阵列不得持续后台窃听或识别旁观者；应用也不得更改/关闭系统降噪器，或指导用户如此操作。上面“公开直播”的限制来自智能眼镜增强体验页面，不能不加区分地外推为所有 XR 头显/所有视频通话的统一禁令。

## 音频眼镜手势与退出行为

这些条款适用于智能眼镜的 audio-only 体验；不可自动套用到所有 XR 头显的控制方式。

| 输入 | 必须/允许 | 禁止 |
| --- | --- | --- |
| 单击触控板 | 播放与用户当前情境相关的提示、重复最近的语音消息、暂停/停止播放，或明确反馈麦克风静音状态。 | 用于广告或无关信息；充当高频游戏控制器；触发犯罪、暴力或自残指令。 |
| 相机实体按键快速双击 | 真正启动相机并向应用提供传感器数据；首次授权/设置前要向用户说明实际用途，数据仅用于用户明确同意的用途。 | 重新映射为非相机功能；截获按钮却丢弃/屏蔽相机数据；未披露或欺骗性使用相机。 |
| 单指向后滑动 | 必须触发 `onBack()`，退出当前体验或回到上一状态；退出后停止或暂停主要传感器使用。 | 劫持退出操作、启动广告/媒体，或假装退出但继续秘密收听/监视。 |

## 设备资格、体验质量与发布判断

- 现有移动应用若没有声明 XR 不支持的必需硬件/软件功能，可作为兼容移动应用自动在 XR 上提供基础体验；若必需功能不受支持，应用无法通过 Play Store 安装。功能声明会参与 Play 的设备过滤，详见 Android 的 [`<uses-feature>`](https://developer.android.com/guide/topics/manifest/uses-feature-element) 说明。
- 已达到平板、桌面或折叠屏 Tier 2 / Tier 1 质量层级的应用，可自动成为 XR 兼容自适应应用。Android XR 差异化应用则须实现至少一项 XR 专属功能/内容并达到适用质量指标；符合条件的应用会获得 Play 商店 “Made for XR” 标记。
- 沉浸式体验清单给出的参考值包括：90Hz 时每帧低于 11.1ms、72Hz 时低于 13.8ms；平均冷启动低于 2 秒、温启动低于 1 秒；ANR 目标为 99.5% 的每日会话少于 1 次；崩溃率约 1%。这些是 XR 质量指南中的指标/目标，不应当改写成所有 Play 应用统一的政策数值。
- 空间体验应减少可能造成晕动症的突然视角移动；注意真实空间边界、中央视野遮挡、触控目标尺寸和清晰退出路径。智能眼镜体验应以用户主动发起为核心，在移动/公共场所减少干扰，摄像头用例采用能满足用途的最低帧率/分辨率，并减少非必要高耗电传感器使用。
- 眼镜相机/麦克风权限应通过 [XR 眼镜硬件权限 API](https://developer.android.com/develop/xr/jetpack-xr-sdk/request-hardware-permissions) 请求；即使手机端已有同名授权，眼镜硬件仍要单独运行时请求并由配对手机/宿主设备呈现系统同意界面。该实现仍须符合[用户数据政策](../user-data/user-data.zh-CN.md)和适用的敏感权限要求。
- 兼容级应用应使用标准 `NotificationManager` 和 Live Updates，让及时通知可被眼镜转为简洁视觉提示或语音读出；差异化体验还应检查音频焦点、辅助输入、不同环境测试和传感器生命周期。

## 正文直接链接：目标页与关系

以下列出根页和两篇体验指南正文中与设备分类、政策义务或可执行的 XR 实现直接相关的目标。页面内的章节锚点（如 compatibility tiers、checklists、audio-only policies）不是独立页面；Android Developers 页面还包含大量测试用例、API 参考和通用导航，完整技术后代仍未穷尽。

| 父页面 → 直接链接 | 目标内容及与 Play/XR 的关系 | 核验状态 |
| --- | --- | --- |
| [Android XR 总览](https://developer.android.com/docs/quality-guidelines/android-xr) → [设备类型](https://developer.android.com/develop/xr/devices)、[沉浸式指南](https://developer.android.com/docs/quality-guidelines/android-xr/immersive)、[增强指南](https://developer.android.com/docs/quality-guidelines/android-xr/augmented) | 用设备和体验类型选择对应要求；这三项是英文政策中心 XR 入口的主要后代。 | 三个英文目标正文已打开；总览与沉浸式指南的简体中文版本也已打开。 |
| 沉浸式指南 → [Core app quality](https://developer.android.com/docs/quality-guidelines/core-app-quality)、[Adaptive app quality](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality) | XR 质量基线继承 Android 核心质量；自适应等级决定兼容自适应应用资格。两者是 Android 质量参考，不替代 Play 政策。 | 两页已打开；Core app quality 有大型测试/API 链接树，只摘要政策相关段落。 |
| 沉浸式指南 → [`<uses-feature>`](https://developer.android.com/guide/topics/manifest/uses-feature-element) | Play 可按应用清单声明的设备特性过滤可见设备；XR 不支持的必需特性可能让应用不可安装。 | 正文链接已打开；它是 Android 实现指南。 |
| 沉浸式指南 → [XR 设计指南](https://developer.android.com/design/ui/xr/guides/get-started)、[辅助功能指南](https://developer.android.com/guide/topics/ui/accessibility)、[启动时间](https://developer.android.com/topic/performance/issues/launch-time)、[崩溃处理](https://developer.android.com/topic/performance/issues/crash)、[Play 预发布报告](https://google.play/business/pre-launchreports/) | 提供空间舒适度/交互建议、基础无障碍、性能诊断与发布前测试；不构成政策豁免或审核通过保证。 | 目标页已打开；已在本页采用其与 XR 质量控制相关的用途摘要，深层技术/API链接未全部追踪。 |
| 增强指南 → [Compose Glimmer](https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer)、[Jetpack Projected 硬件访问](https://developer.android.com/develop/xr/jetpack-xr-sdk/access-hardware)、[硬件权限请求](https://developer.android.com/develop/xr/jetpack-xr-sdk/request-hardware-permissions)、[ARCore for Jetpack XR](https://developer.android.com/develop/xr/jetpack-xr-sdk/arcore) | 面向显示眼镜的低干扰 UI、手机/眼镜投射设备协作、宿主端权限同意和环境感知功能。权限/API 可用不等于 Play 对数据用途已批准。 | 正文目标均已打开；权限与数据政策须同时交叉核对。 |
| 增强指南 → [NotificationManager](https://developer.android.com/reference/kotlin/android/app/NotificationManager)、[Live Updates](https://developer.android.com/develop/ui/compose/notifications/live-update)、[后台任务概览](https://developer.android.com/develop/background-work/background-tasks)、[音频焦点](https://developer.android.com/media/optimize/audio-focus) | 标准通知/持续活动呈现、后台任务调度和音频焦点；有助于降低误提醒、耗电及后台传感器滥用风险。 | 页面已打开，作为技术实施参考；更深 API 成员未逐个摘要。 |
| 增强指南 → [眼镜模拟器](https://developer.android.com/develop/xr/jetpack-xr-sdk/run/create-avds/glasses)、[Glimmer composable 预览](https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/preview) | 测试眼镜端显示与交互，并覆盖不同场景/光照。 | 页面已打开；模拟器系统镜像和后续工具链仍会变化。 |
| 增强指南 → [Google Play Developer Policies](https://play.google/developer-content-policy/)、[User Data](https://support.google.com/googleplay/android-developer/answer/10144311)、[Bullying and Harassment](https://support.google.com/googleplay/android-developer/answer/9878810) | XR 相机/眼镜行为须与一般 Play 政策、数据处理要求和反霸凌/骚扰规则同时满足；旁观者识别、曝光身份信息和公开剥削行为交叉涉及这些要求。 | Policy Center 与 User Data 均已打开并有双语摘要；Bullying 目标本次点击失败，但当前政策正文已纳入[不当内容专题](../inappropriate-content/inappropriate-content.zh-CN.md)。 |

### 眼镜权限请求与 Projected context 的后代（2026-10-24）

重开 [Request hardware permissions](https://developer.android.com/develop/xr/jetpack-xr-sdk/request-hardware-permissions)（页面标注 2026-10-19 更新）并沿其设备、Manifest、运行时权限、API、示例及相邻硬件指南继续追踪。下表总结与摄像头/麦克风用途直接相关的目标；Android 实现文档不是 Play 对该用途的许可。

| 链路 / 目标 | 内容及关系 | 核验状态 |
| --- | --- | --- |
| 权限指南 → [`ProjectedActivityCompat`](https://developer.android.com/reference/androidx/xr/projected/ProjectedActivityCompat) → [XR Projected 发布记录](https://developer.android.com/jetpack/androidx/releases/xr-projected) | 从投射眼镜 Activity 请求时使用 `ProjectedActivityCompat.requestPermissions`，由眼镜提示转到宿主手机系统授权；结果回到发起请求的 Activity。API 参考标注 API 35+、工作线程调用，并列出投射服务不可用/Activity 非投射设备等失败条件。发布记录显示当前为 `1.0.0-alpha14`（2026-10-21），仍是 alpha；`ProjectedPermissionsResultContract` 已废弃，旧 `androidx.xr.projected.permissions.*` 已移除。 | API 正文定点打开；发布记录正文打开。官方 API 标注与发布历史对请求 API 首次加入版本的标记并不完全一致，按当前发布版和 API 参考实施；不把 alpha 版本写成稳定版。 |
| 权限指南 → [Declare app permissions](https://developer.android.com/training/permissions/declaring) → [`<uses-permission>`](https://developer.android.com/guide/topics/manifest/uses-permission-element) → [Request runtime permissions](https://developer.android.com/training/permissions/requesting) | 只声明实际需要的权限；在用户触发对应功能时申请，每次执行敏感操作前检查，按需说明理由，并为拒绝/撤回提供可继续使用应用的降级路径。硬件权限可能影响 Play 设备过滤：如果摄像头并非应用必需能力，应在 Manifest 显式将相机特性设为 optional，再检查设备是否有该硬件。 | 声明、Manifest 与运行时权限正文均已打开或交叉核对；这部分是 Android 最小权限/兼容性实践，与 Play 的 XR 隐私条款分别记录。 |
| 权限指南 → [`Activity.requestPermissions(..., deviceId)`](https://developer.android.com/reference/kotlin/android/app/Activity)；[Android XR 设备类型](https://developer.android.com/develop/xr/devices) | 若从手机 Activity 请求眼镜权限，应传入投射设备 ID；结果回调也使用能区分设备上下文的重载。不要把宿主手机对相机/麦克风的授权误当作眼镜硬件授权。 | Activity 大型 API 参考仅针对方法打开；眼镜类型页全文打开。指南中的两个 GitHub 代码样例点击返回 Internal Error，读取器未给出可核对的目标 URL。 |
| [Access hardware](https://developer.android.com/develop/xr/jetpack-xr-sdk/access-hardware) → [Use a projected context](https://developer.android.com/develop/xr/jetpack-xr-sdk/access-hardware-projected-context) → [`ProjectedContext`](https://developer.android.com/reference/androidx/xr/projected/ProjectedContext) | 投射 Activity 的上下文可直接访问眼镜硬件；手机 Activity/Service 应在设备连接时创建 projected context，断开时释放相机等资源，重连后重新创建。API 搜索摘录也说明应用级 Context 的设备 ID 可能随最近前台 Activity 切换，优先用 Activity Context。 | 硬件指南相关正文已打开；ProjectedContext API 直连失败，相关成员依据 Android Developers 官方搜索索引摘录，故仅作部分读取。示例文件 href 未暴露。 |
| Projected context → [AudioManager](https://developer.android.com/reference/kotlin/android/media/AudioManager)、[AudioDeviceInfo](https://developer.android.com/reference/kotlin/android/media/AudioDeviceInfo)、[Bluetooth overview](https://developer.android.com/develop/connectivity/bluetooth)、[CameraX overview](https://developer.android.com/media/camera/camerax) | 硬件访问页将眼镜相机指向 CameraX，并建议检查相机可用性；蓝牙 HFP 音频录制走宿主手机的 `RECORD_AUDIO` / `BLUETOOTH_CONNECT` 运行时授权和 `AudioManager` 路由。HFP 是普通蓝牙设备链路，不能据此替代眼镜专属相机授权。 | 目标页已打开或定点核查；大篇幅 API、CameraX 用例和蓝牙权限孙链仍未穷尽。 |

**剩余边界：** 权限指南的两个 GitHub 样例目标不可读且 href 未暴露；Activity/ProjectedContext/AudioManager 等大型 API 只对相关成员定点审阅；示例仓库、CameraX、蓝牙和所有导航后代未穷尽。当前 Jetpack XR API 仍是 alpha。以上平台流程不改变 Play 对用途必要性、数据披露、用户同意、后台采集和旁观者隐私的要求。

## 覆盖边界

本页已双语整理 Android XR 两类体验的政策核心和重要直接后代，并将高影响政策目标关联到已有专题。Android Developers 的测试条目、脚注、导航、SDK/API 的所有后代链接没有全部展开；增强指南的中文本地化页面本次抓取失败。页面最后更新为 2026-10-20 UTC；没有单独的生效期限。发布前仍应核对现行英文/中文来源、应用形态、Play Console 设备过滤与适用的账号级政策状态。
