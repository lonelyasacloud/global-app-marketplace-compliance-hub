---
id: google-play.play-asset-delivery
platform: google-play
language: zh-CN
authority: operational
status: current
kb_checked_at: 2026-10-24
review_due: 2027-01-24
regions: [global]
topics: [Play Asset Delivery, PAD, asset packs, dataSync, games, Play Core]
snapshot_id: play.asset-delivery-implementation
snapshot_package: "GooglePlay-KnowledgeBase-2026-10-24-review.zip"
coverage_status: "detailed-summary"
source_url: "https://developer.android.com/guide/playcore/asset-delivery"
source_url_java: "https://developer.android.com/guide/playcore/asset-delivery/integrate-java"
source_url_native: "https://developer.android.com/guide/playcore/asset-delivery/integrate-native"
source_url_unity: "https://developer.android.com/guide/playcore/asset-delivery/integrate-unity"
effective_date: "implementation guidance; the narrow dataSync foreground-service exception stays on the device-abuse and foreground-service topics; no 2027-01-27"
---

# Play Asset Delivery：政策边界、交付模式与实现核查

> **导入说明（Google batch 8）。** 正文来自已经分开的 2026-10-24 Google Play 知识库快照（`play.asset-delivery-implementation`，核对日 2026-10-24）的改写摘要，不是官方页面的逐字副本。英文官方页面是效力来源。`kb_checked_at` 是快照源文件记录的核对日；本次导入没有重新打开线上官方页面。文中“本知识库”“本库”“本地专题”等说法描述的是该快照库的覆盖范围，不是本仓库已经导入的页面。指向本仓库没有收录的专题、链接图、台账或 CSV 的相对链接改为文字提及。指向 Google batch 1–7 或本批十三个专题的相对链接改为本仓库文件。核对日 2026-10-24。中文文件把 Device and Network Abuse 父页记为 `hl=zh-CN`。Android PAD 指南使用不带语言参数的 `developer.android.com` 地址。快照没有记录已核对的中文官方 PAD 指南，也没有记录这些 Android 页面的 `hl=zh-CN` 抓取失败。中文是编辑改写。Google Play Instant 总览返回缓存未命中或 Internal Error，没有据此推断 Instant 正文。视频目标没有暴露 URL。这些访问限制不是政策变更。没有 2027-01-27。PAD 是实现说明，不授予 Play 政策豁免。`dataSync` 前台服务例外只适用于 Play Asset Delivery，并留在设备与网络滥用及前台服务专题。证据等级：实现说明。

**核对日期：2026-10-24。** 本专题从 Play 的 [Device and Network Abuse](https://support.google.com/googleplay/android-developer/answer/16559646?hl=zh-CN) 中 `dataSync` 前台服务（FGS）例外出发，展开 Android 官方 [Play Asset Delivery（PAD）指南](https://developer.android.com/guide/playcore/asset-delivery)及 Java/Kotlin、原生 C/C++、Unity 集成页。PAD 是 Android 实现技术；它不单独授予 Play 政策豁免、权限批准或 Console 审批。

## 政策边界

Play 当前列出的 `dataSync` FGS 例外只适用于**使用 Play Asset Delivery 功能**的情形。不能把例外扩展到普通后台同步、一般文件下载、SDK 更新或与 PAD 无关的数据传输。即使技术上使用 PAD，仍须按应用实际目标 SDK、服务类型、Manifest、用户可感知性和 Console 申报要求核对。请与[前台服务专题](../foreground-services-and-geofencing/foreground-services-and-geofencing.zh-CN.md)及[设备与网络滥用专题](../device-and-network-abuse/device-and-network-abuse.zh-CN.md)一起使用。

PAD 指南说明，asset pack 可装游戏纹理、着色器、声音等资源，但**不能含可执行代码**。不要将动态交付的 asset pack 当成应用外代码分发通道。Play 对自我更新、应用外下载可执行代码及第三方 SDK 的一般限制仍须独立遵守，详见[SDK 要求](../sdk-requirements/sdk-requirements.zh-CN.md)。

## 三种交付模式

| 模式 | 可用时机与安装形式 | 用户/应用应处理的事项 |
| --- | --- | --- |
| `install-time` | 与应用一同安装，首次启动即可用；作为 split APK 安装，并计入商店详情显示的应用大小。 | 安装/更新须有足够空间；指南提示可用空间至少为所有 asset pack 总大小的两倍。用户不能像普通下载文件那样移动或删除该 pack。 |
| `fast-follow` | 安装后自动下载，不阻止首次打开；下载后解包到应用私有存储。 | 首屏不能假定资源已就绪；展示进度并允许暂缺时继续使用核心功能。不计入商店详情显示大小；文件可被用户或 Play 管理而移动/删除。 |
| `on-demand` | 应用运行期间按需请求；下载后解包到应用私有存储。 | 请求前查询大小并告知用户；处理暂停、取消、无网络及用户确认。不计入商店详情显示大小；路径及可用性会变化。 |

Google Play 托管资源包并管理压缩、差分更新和下载调度；开发者仍要设计缺失资源时的界面和恢复流程。Instant apps 仅支持 `on-demand`。Texture Compression Format Targeting（TCFT）可按设备支持格式选择资源；限制按每种唯一纹理格式分别计算。详见[纹理压缩格式指南](https://developer.android.com/guide/playcore/asset-delivery/texture-compression)。

## 发布与运行时核查

- **披露下载大小。** Java/Native 集成页要求应用在开始下载前告知用户 asset pack 大小。指南给出的门槛是：通过蜂窝网络下载超过 200 MB 时须先取得用户明确同意；实施时应重新核对当前页面、平台提示行为和应用场景。
- **处理网络中断和确认。** Wi‑Fi 断开可能暂停下载，继续时应处理用户确认。若应用未被识别为 Play 安装（例如侧载），可能返回 `REQUIRES_USER_CONFIRMATION`；用户确认后流程可能更新应用，随后须重新请求资源。
- **每次启动重新查询。** 不缓存 pack 路径来推定文件仍可用。应用更新、清除数据或用户/Play 管理行为可能让旧路径或资源失效；重新查询位置与状态，并在资源不可用时降级或重试。
- **下载资源只读。** 不要修改 PAD 解包文件；更新完整性机制依赖应用不改写这些内容。需要写入的状态或派生文件应放到应用自行管理的目录。
- **容忍更新竞态。** fast-follow/on-demand pack 更新会使旧 pack 失效；偶尔应用二进制先更新、资源补丁尚未就绪。显示“更新进行中”，避免崩溃或锁住用户。
- **明确大小口径。** `install-time` 资源计入商店详情显示的应用大小，fast-follow/on-demand 不计入；Play 与开发者本地估算可能不同，参见[应用大小帮助页](https://support.google.com/googleplay/android-developer/answer/9859372)。

### Play Core SDK 与 Data safety

Play Core 已按功能拆分为各自的库。Gradle 坐标和静态 SDK 下载示例会变化；页面中出现的 `play-core-native-sdk-1.16.0.zip` 等版本较旧，不应当作当前依赖版本。集成前查看当前指南、发行说明和项目构建配置。

原生集成指南说明，上传应用包时 Native SDK 会收集包名、应用版本和 SDK 版本等信息，并提到可移除 `playcore-native-metadata.jar` 选择退出此项收集。这不是应用完整数据流清单。指南明确由开发者自行决定本应用的 [Data safety](../data-safety/data-safety.zh-CN.md) 表单答案；应合并评估应用代码、SDK、服务器、共享接收方、保留期与用户披露，不能据此推定“无需申报”。

[In-app Updates](https://developer.android.com/guide/playcore/in-app-updates) 更新应用二进制，与 PAD 资源包更新是不同功能；它不代替资源包状态检查，也不是 Play Console 对已安装旧版本的远程恢复服务。法律链接也要分清：PAD 页上的 Play Terms 目标是面向消费者的 [Google Play Terms of Service](https://play.google.com/about/play-terms/index.html)，不是开发者分发协议；`/guide/playcore/license` 当前跳回 Play Core 概览，不能据此断言已核实新版 SDK 服务条款。

## 官方页面与直接子链接审计

以下按正文外链整理，不把页眉、页脚、侧栏和通用导航算作政策子链。“已打开”表示读取了目标页，不表示其孙链接/API 成员均已闭合。逐 URL 状态见URL 审计表（快照：`../source-page-audit.csv`，未导入本仓库）及递归链接图 §4.137（快照：`../google-play-policy-link-graph.md#4137-play-asset-delivery政策边界实现指南和直接子链2026-10-24`，未导入本仓库）。

### PAD 主指南的正文目标

| 目标页 | 内容与关系 | 本轮状态/边界 |
| --- | --- | --- |
| [Play Core overview](https://developer.android.com/guide/playcore) | Play Core 已拆分为功能库；集成版本须看当前发行说明。 | 正文已打开；版本/API 后代未全审。 |
| [Google Play Instant overview](https://developer.android.com/gtopic/google-play-instant/overview) | Instant 与 PAD 支持模式的交叉背景。 | 抓取返回 Cache miss/Internal Error；未推断页面内容。 |
| [纹理压缩格式](https://developer.android.com/guide/playcore/asset-delivery/texture-compression) | TCFT、设备格式选择和纹理资源设置；旧路由重定向至此。 | 当前页已打开；引擎/API 示例后代部分未审。 |
| [In-app Updates](https://developer.android.com/guide/playcore/in-app-updates) | 应用二进制灵活/立即更新，与 pack 下载分开；旧路由重定向至此。 | 正文已打开；语言样例/API 后代部分未审。 |
| [应用大小限制](https://support.google.com/googleplay/android-developer/answer/9859372) | 应用和 asset pack 大小展示、Console 指标。 | Help 正文已打开；账号内指标仍需登录。 |
| [Java/Kotlin 集成](https://developer.android.com/guide/playcore/asset-delivery/integrate-java)、[Unity 集成](https://developer.android.com/guide/playcore/asset-delivery/integrate-unity) | Gradle/AssetPackManager，或 Unity Addressables/AssetBundles 与 Play 插件。 | 旧路由已解析至现行页，正文已打开；API/插件后代仍部分覆盖。 |
| [`/guide/playcore/license`](https://developer.android.com/guide/playcore/license) | 主指南标注的 SDK 服务条款入口。 | 当前重定向到 Play Core 概览；未把概览当成条款正文。 |
| [Google Play Terms of Service](https://play.google.com/about/play-terms/index.html) | 消费者服务条款。 | 全文已打开；不是 Developer Distribution Agreement。 |
| 开发者案例：[Devsisters](https://developer.android.com/stories/games/devsisters)、[Cat Daddy](https://developer.android.com/stories/games/cat-daddy)、[CD PROJEKT RED](https://developer.android.com/stories/games/cdpr)、[RV AppStudios](https://developer.android.com/stories/games/rv-appstudios-pad)、[Gameloft](https://developer.android.com/stories/games/gameloft-pad) | PAD 采用案例。 | 五页均已打开；案例不是政策义务、结果保证或审核承诺。 |
| [Android Developers 内容许可](https://developer.android.com/license) | Android 开发者网站内容/示例代码许可。 | 正文已打开；不是 Play 分发政策。 |
| 主指南插图：[distribution](https://developer.android.com/static/images/picto-icons/distribution.svg)、[pathway](https://developer.android.com/static/images/picto-icons/pathway.svg)、[frame](https://developer.android.com/static/images/picto-icons/frame.svg)、[update](https://developer.android.com/static/images/spot-icons/tools-update.svg) | 示意图/图标，无独立政策条文。 | 均已尝试；图像不可读或缓存失败，不从 URL 推断内容。 |
| 正文视频链接 | PAD 说明视频。 | 点击未暴露目标 URL，无法识别或审计目标；未声称读过视频。 |

### 集成页和关键孙链接

| 分支/目标 | 摘要与审计边界 |
| --- | --- |
| [原生 C/C++ 集成](https://developer.android.com/guide/playcore/asset-delivery/integrate-native) | 使用 `play/asset_pack.h` 和 CMake；检查下载状态、大小、网络确认和可失效路径，也说明 Native SDK 元数据收集。页面正文已打开（标注 2026-10-16 更新）；SDK 下载目标未暴露，旧版本/Terms 样例需谨慎。 |
| [Java 集成](https://developer.android.com/guide/playcore/asset-delivery/integrate-java) | `AssetPackManager` 按模式提供流程；每次启动重新查询，披露大小并处理 fast-follow 尚未就绪。正文已打开（标注 2026-10-16 更新）；API 后代部分审阅。 |
| [Unity 集成](https://developer.android.com/guide/playcore/asset-delivery/integrate-unity)、[Unity PAD codelab](https://developer.android.com/codelabs/unity-gamepad) | Addressables/旧版 AssetBundles 与具体实现示例。页面已打开；codelab 和插件版本较旧，需按当前 Unity 项目复核。 |
| [Native PAD sample](https://github.com/android/app-bundle-samples/tree/main/PlayAssetDelivery/NativeSample)、[Native codelab](https://developer.android.com/codelabs/native-gamepad)、[PAD 测试指南](https://developer.android.com/guide/playcore/asset-delivery/test) | 示例涵盖三种交付模式；codelab 是教学实现；测试页讲模式和 bundle 流程。均已打开；示例不是规范，完整测试/API 后代仍部分覆盖。 |
| Java API | [assetpacks package](https://developer.android.com/reference/com/google/android/play/core/assetpacks/package-summary)、[AssetPackManager](https://developer.android.com/reference/com/google/android/play/core/assetpacks/AssetPackManager)、[AssetPackLocation](https://developer.android.com/reference/com/google/android/play/core/assetpacks/AssetPackLocation)、[AssetPackStates](https://developer.android.com/reference/com/google/android/play/core/assetpacks/AssetPackStates)、[AssetPackState](https://developer.android.com/reference/com/google/android/play/core/assetpacks/AssetPackState)、[AssetPackStatus](https://developer.android.com/reference/com/google/android/play/core/assetpacks/model/AssetPackStatus)、[AssetPackErrorCode](https://developer.android.com/reference/com/google/android/play/core/assetpacks/model/AssetPackErrorCode)、[AssetPackStateUpdatedListener](https://developer.android.com/reference/com/google/android/play/core/assetpacks/AssetPackStateUpdatedListener)、[KTX package](https://developer.android.com/reference/com/google/android/play/core/ktx/package-summary)、[AssetManager](https://developer.android.com/reference/android/content/res/AssetManager)。API 页面均已打开并核对 PAD 相关成员；大型目录其他成员/后代未穷尽。 |
| Native API | [Play Core native](https://developer.android.com/reference/native/play/core)、[assetpack group](https://developer.android.com/reference/native/play/core/group/assetpack)、[NDK asset API](https://developer.android.com/ndk/reference/group/asset)、[ANativeActivityCallbacks](https://developer.android.com/ndk/reference/struct/a-native-activity-callbacks)。大型 API 目标已打开并抽查相关符号；无关成员未逐项整理。 |
| Unity API/工具 | [AndroidAssetPacks](https://docs.unity3d.com/ScriptReference/Android.AndroidAssetPacks.html)、[PlayAssetDelivery](https://developer.android.com/reference/unity/class/Google/Play/AssetDelivery/PlayAssetDelivery)、[PlayAssetDelivery namespace](https://developer.android.com/reference/unity/namespace/Google/Play/AssetDelivery)、[PlayAssetBundleRequest](https://developer.android.com/reference/unity/class/Google/Play/AssetDelivery/PlayAssetBundleRequest)、[AssetPackConfig](https://developer.android.com/reference/unity/class/Google/Android/AppBundle/Editor/AssetPackConfig)、[Bundletool](https://developer.android.com/reference/unity/class/Google/Android/AppBundle/Editor/Bundletool)、[Addressables Android package](https://docs.unity3d.com/Packages/com.unity.addressables.android@1.0/manual/index.html)、[Unity PAD manual](https://docs.unity3d.com/Manual/play-asset-delivery.html)、[AssetBundles](https://docs.unity3d.com/Manual/AssetBundlesIntro.html)、[AssetBundle Browser](https://docs.unity3d.com/Packages/com.unity.assetbundlebrowser@1.7/manual/index.html)、[Package Manager](https://docs.unity3d.com/Manual/class-PackageManager.html)、[UPM install](https://docs.unity3d.com/Manual/upm-ui-install.html)、[Coroutines](https://docs.unity3d.com/Manual/Coroutines.html)、[BuildPlayerOptions](https://docs.unity3d.com/ScriptReference/BuildPlayerOptions.html)、[OpenUPM CLI](https://github.com/openupm/openupm-cli)、[Unity PAD plugin v1.9.5](https://github.com/google/play-asset-delivery-unity/releases/tag/v1.9.5)。页面已打开/重定向；特定版本不是“最新版本”保证。 |
| 构建与许可背景 | [命令行构建](https://developer.android.com/build/building-cmdline)、[Android Studio](https://developer.android.com/studio)、[sdkmanager](https://developer.android.com/tools/sdkmanager)、[Studio 更新](https://developer.android.com/studio/intro/update)、[NDK guides](https://developer.android.com/ndk/guides)、[上传 AAB](https://developer.android.com/studio/publish/upload-bundle)、[Google APIs Terms](https://developers.google.com/terms)、[Unity Addressables 介绍](https://unity.com/how-to/simplify-your-content-management-addressables)。目标页已打开；属于工具/实现背景，不代表 Play 审批。 |

## 覆盖范围与未闭合项

PAD 主指南及 Java、Native、Unity 三个集成页均已打开；主指南正文链接已逐项尝试，关键集成页子链接/API 目标已登记。这里的“全文可用”指本地有双语结构化摘要及可追溯官方 URL，不是复制官方全文，也不代表所有 API 成员、示例仓库文件、工具导航或无限层级后代均已穷尽。Native SDK 下载和视频目标未解析；Instant 目标抓取失败；`/guide/playcore/license` 没有到达独立条款正文。Android 工程说明不替代 Play 政策判断。
