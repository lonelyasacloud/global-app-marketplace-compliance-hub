---
id: google-play.app-version-codes-and-apk-distribution
platform: google-play
language: zh-CN
authority: operational
status: current
kb_checked_at: 2026-10-24
review_due: 2027-01-24
regions: [global]
topics: [version-code, app-bundle, apk, device-compatibility, publishing]
snapshot_id: play.version-codes-and-apk-distribution
snapshot_package: "GooglePlay-KnowledgeBase-2026-10-24-review.zip"
coverage_status: "detailed-summary"
source_url: "https://support.google.com/googleplay/android-developer/answer/17367361?hl=en"
effective_date: "current Play versionCode ceiling 2100000000; AAB dates August 2021 and June 2023 are historical format requirements; no 2027-01-27"
---

# Google Play 版本号、App Bundle 与设备筛选

> **导入说明（Google batch 8）。** 正文来自已经分开的 2026-10-24 Google Play 知识库快照（`play.version-codes-and-apk-distribution`，核对日 2026-10-24）的改写摘要，不是官方页面的逐字副本。英文官方页面是效力来源。`kb_checked_at` 是快照源文件记录的核对日；本次导入没有重新打开线上官方页面。文中“本知识库”“本库”“本地专题”等说法描述的是该快照库的覆盖范围，不是本仓库已经导入的页面。指向本仓库没有收录的专题、链接图、台账或 CSV 的相对链接改为文字提及。指向 Google batch 1–7 或本批十三个专题的相对链接改为本仓库文件。核对日 2026-10-24。两种语言文件引用的版本号文章都是英文 `hl=en`。快照没有记录已核对的中文官方版本号页，也没有记录该主文章 `hl=zh-CN` 抓取失败。中文是编辑改写。Android NDK 精确工具页和版本号图示返回缓存未命中，Android compatibility 返回 Internal Error。这些失败不是政策变更。Play 上限 2,100,000,000 是现行上传限制。2021 年 8 月和 2023 年 6 月是已经过去的 App Bundle 格式日期。没有 2027-01-27。版本号上限来自 Play Help。多 APK、Manifest、筛选和 App Bundle 是实现说明，不证明审核已通过。证据等级：Play Help 为 Operational；Android 发布机制为实现说明。

## 范围和证据

本专题从审核准备页的 [Version codes](https://support.google.com/googleplay/android-developer/answer/17367361?hl=en) 展开，继续检查 [Multiple APK support](https://developer.android.com/google/play/publishing/multiple-apks)、[Filters on Google Play](https://developer.android.com/google/play/filters) 和 [Android App Bundles](https://developer.android.com/guide/app-bundle)。2026-10-24 重新打开了版本号页、两个核心 Android 指南、App Bundle 指南、清单与 Licensing 相关页面。正文链接按目标去重；通用页眉/页脚不算本表所列正文链接。逐 URL 访问状态见 source-page-audit.csv（快照：`../source-page-audit.csv`，未导入本仓库），关系见链接图 §4.125。

**边界：** `versionCode` 的上限及发布后果来自 Play Help；APK/AAB、Manifest 和筛选行为是 Android/Play 开发者文档中的技术说明。技术说明可帮助避免误配置，但不代表 Play 政策批准或某账号已通过审核。

## 版本号的 Play 要求

| 项目 | 已核实内容 | 落地检查 |
| --- | --- | --- |
| `versionCode` | 正整数、32 位内部版本号；每次后续发布必须递增，用于系统和 Play 判断新旧。Play 允许的最大值为 **2,100,000,000**。达到或超过上限后，不能再为该应用上传新的 APK 或 App Bundle。 | 预留长期增长空间；检查所有 product flavor、轨道和自动化脚本，阻止重复、回退或越界值。 |
| `versionName` | 面向用户展示的字符串，例如 `1.2.3`；本身不决定更新顺序。 | 让商店说明、应用内版本展示与构建产物一致。 |
| 编号维护 | Play 建议渐进、可持续地递增，持续监测余量，并在构建/发布流程中加入自动告警或拦截。 | 不用时间戳/位段方案消耗过快；CI 至少验证大于已发布版本且低于 Play 上限。 |

Android Manifest 参考页也把 `versionCode` 定义为更新排序值、把 `versionName` 定义为展示文本。Play 上限应以 Play Help 为准，不能仅按 Android 属性本身的类型推导。

## App Bundle 与多 APK：选择路径

- Android App Bundle（AAB）是 Google Play 推荐的发布格式。Play 根据设备配置生成并分发优化后的 APK，通常无需开发者自行维护按设备拆分的 APK。
- Android Developers 文档注明：自 2021-08 起新应用须用 AAB 发布；自 2023-06 起新旧 TV 应用均须用 App Bundle 发布。既有应用的过渡资格和 Console 校验应按当前发布流程、应用类别及账号内提示确认。
- AAB 的安装所需压缩下载总量及后续按需下载须符合 4 GB 限制；AAB 不支持 APK expansion（`.obb`）文件。该限制属于分发格式/技术要求，不是 `versionCode` 上限。
- 多 APK 是高级、边缘方案。Android 指南鼓励多数应用用一个广泛兼容的 APK/AAB；仅当单一产物无法满足设备支持或大小等现实约束时再考虑。相同应用条目下的 APK 要共享 package name 和发布签名密钥；每个 APK 使用唯一 `versionCode`。若设备过滤条件重叠，Play 按版本排序选择适用产物；API 级别较高的变体及其他重叠升级路径须确保更高版本号，避免系统升级后没有可用更新。

### 多 APK 可区分设备的过滤条件

[Filters on Google Play](https://developer.android.com/google/play/filters) 将同一应用清单内多 APK 之间可用于区分变体的过滤类别列为四类：

1. OpenGL 纹理压缩格式；
2. 屏幕尺寸（可选屏幕密度）；
3. API 级别；
4. CPU 架构（ABI）。

Multiple APK Support 页面还单列设备功能集合和 Android Go 的实现示例，而 Filters 页面又说明上述四类以外的过滤器不能单独区分同一应用的 APK。两页当前表述有张力，因此本专题不把“设备功能”或 Go 示例提升为普遍可用的第五/第六种筛选类别；需在实际发布前核对当前文档和 Play Console 的产物校验结果。屏幕差异通常优先用自适应布局/资源，而不是拆 APK；`<compatible-screens>` 会排除未列出的尺寸/密度组合，官方通常建议避免使用。

## 设备可见性和隐式过滤

Google Play 会综合 Manifest、必需共享库、ABI、应用发布状态、国家/地区/价格等 Console 分发设置判断设备兼容性。过滤不只是“能否安装”：不兼容应用可能从搜索、分类浏览乃至应用深链中隐藏；一次更新也可能改变已安装用户看到更新的资格。

- `minSdkVersion` 影响最低兼容 API；`targetSdkVersion` 表示平台行为兼容目标，Play 的年度 target API 提交门槛另见[目标 API 专题](../target-api/target-api-level.zh-CN.md)（不要把两者当成同一规则）。
- 某些硬件相关权限会让 Play 推断应用依赖相应硬件。例如仅在功能确实可选时，才考虑显式声明 `android:required="false"` 以免无意过滤没有该硬件的设备；这不免除敏感权限的政策资格、声明或审核要求，详见[敏感权限专题](../sensitive-permissions/sensitive-permissions.zh-CN.md)。
- `<uses-library android:required="true">` 会筛除没有该共享库的设备；设为 `false` 后，应用应自行在运行时检测库是否存在。
- 不建议靠 `maxSdkVersion` 阻止新版 Android 安装；Android 文档称通常应使用公共 API 保持向前兼容。
- Play 的应用许可服务（Licensing）是开发者可选的运行时许可控制实现，不是 Play 上架/政策要求，也不等于多 APK 的设备筛选。许可文档称开放/封闭测试轨道中的获准测试用户也被视为已授权用户；未发布的 draft 测试已不再受支持。

## 两个源页面的正文直接链接清单

下列计数只覆盖页面正文可见的外部直链，不包括导航和页脚。重复 URL、同页锚点按目标去重；子页面的更深 API/示例树仍不是完整闭包。

### Version codes → Multiple APK support

Multiple APK 页面有 27 个正文链接引用；其中两个是同页章节锚点，按目标归并后有 20 个外部页面/资源目标。`uses-sdk` 等被多次链接的目标只列一次。

| 直接目标 | 页面关系与本轮状态 |
| --- | --- |
| [Android App Bundles](https://developer.android.com/guide/app-bundle) | Play 依设备配置生成优化 APK；AAB、4 GB 压缩下载限制和 OBB 边界已复核。正文完整打开，其他 delivery/API 后代未穷尽。 |
| [Android NDK](https://developer.android.com/tools/sdk/ndk) | 多 APK 的 ABI/原生库背景。精确目标本轮 Cache miss；另有 ABI 指南目标已部分查看，不能视为 NDK 文档已读。 |
| [Prepare & roll out releases（旧链接）](https://support.google.com/googleplay/android-developer/answer/7159011) → [当前发布流程](https://support.google.com/googleplay/android-developer/answer/9859348) | 观察到旧 URL 重定向到现行发布页；既有中英[发布流程专题](../publishing/play-release-workflow.zh-CN.md)覆盖主要流程。当前 Help 重试遇到抓取拦截，Console 状态不据此推断。 |
| [Filters on Google Play](https://developer.android.com/google/play/filters) | 多 APK 变体与设备可见性规则的核心页面；正文已打开并摘要，17 个不同正文直链见下表。 |
| [`<supports-gl-texture>`](https://developer.android.com/guide/topics/manifest/supports-gl-texture-element) | OpenGL 压缩纹理过滤；正文已打开，技术参考后代部分覆盖。 |
| [`<supports-screens>`](https://developer.android.com/guide/topics/manifest/supports-screens-element) | 屏幕支持声明及默认行为；已查看相关段落，完整参考后代部分覆盖。 |
| [`<compatible-screens>`](https://developer.android.com/guide/topics/manifest/compatible-screens-element) | 精确列举尺寸/密度会排除未列配置；已查看相关段落，完整参考后代部分覆盖。 |
| [Build Multiple APKs / APK splits（旧路径）](https://developer.android.com/studio/build/configure-apk-splits) → [当前 APK splits 配置](https://developer.android.com/build/configure-apk-splits) | 旧 Studio URL 重定向到现行 Build 文档；已查看相关配置章节，其他构建变体/API 后代部分覆盖。 |
| [Supporting Multiple Screens](https://developer.android.com/guide/practices/screens_support) | 单一 APK 的自适应屏幕与资源方案；已部分查看，不把该旧入口视为 Play 政策。 |
| [`<uses-sdk>`](https://developer.android.com/guide/topics/manifest/uses-sdk-element) | 同一目标覆盖最低/目标/最高 SDK 多个锚点；当前技术参考已完整打开。年度 Play target API 规则另列专题。 |
| [Distributing to Specific Screens（旧路径）](https://developer.android.com/guide/practices/screens-distribution) → [当前自适应显示尺寸指南](https://developer.android.com/develop/ui/compose/layouts/adaptive/support-different-display-sizes) | 旧路线重定向至当前 Compose 自适应布局指南；本轮只核对相关显示尺寸/可调整窗口段落，通用 Compose API 后代部分覆盖。 |
| [`<uses-feature>`](https://developer.android.com/guide/topics/manifest/uses-feature-element) | Manifest 功能声明和设备过滤；已查看 Play filtering 相关段落，完整参考后代部分覆盖。 |
| [Configure Product Flavors（旧路径）](https://developer.android.com/studio/build/build-variants) → [当前 Build variants 指南](https://developer.android.com/build/build-variants) | 旧 Studio URL 重定向到当前 Build 文档；仅查看与多 APK/变体相关部分。 |
| [`<manifest>`](https://developer.android.com/guide/topics/manifest/manifest-element) | Manifest 中的 `versionCode`/`versionName` 定义已核对；完整页面有打开，通用属性后代不在本轮闭合。 |
| [Android ABI 指南](https://developer.android.com/ndk/guides/abis) | ABI/原生库打包的技术说明；部分查看，NDK/API/示例树未穷尽。 |
| [`<uses-configuration>`](https://developer.android.com/guide/topics/manifest/uses-configuration-element) | 键盘/导航/触屏配置过滤；已查看相关段落，参考后代部分覆盖。 |
| [Android Studio projects（旧路径）](https://developer.android.com/tools/projects) → [当前 Studio projects](https://developer.android.com/studio/projects) | 旧路径重定向至 Studio 项目概览；工程指南，不新增 Play 政策。 |
| [版本号图示资源](https://developer.android.com/static/images/market/version-codes.png) | 图像目标本轮 Cache miss；可读版本规则已由文字正文完整覆盖。 |
| [Multiple APKs by API level](https://developer.android.com/training/multiple-apks/api) | 旧式 API 拆分技术指南；已部分查看。该页本身建议优先考虑 App Bundle，更多 API 后代未穷尽。 |
| [Android Developers Content License](https://developer.android.com/license) | 已打开许可说明：文档/代码与其他站点内容适用不同许可，外链及商标另有边界。本库使用摘要和链接，不镜像全文。 |

### Filters on Google Play 的 17 个不同正文直链

Filters 页面正文有 24 个可见链接引用；相同 `<uses-sdk>` 的不同锚点、重复链接合并后 17 个外部目标。通用 Android 参考后代只核对与 Play 过滤直接相关的章节。

| 直接目标 | 与筛选主题的关系及状态 |
| --- | --- |
| [Google Play 网页应用目录](https://play.google.com/apps) | 网页端按登录用户已登记设备显示安装兼容性；跳转到 Google 登录，公开抓取无法检查具体设备。 |
| [Android manifest 概览](https://developer.android.com/guide/topics/manifest/manifest-intro) | 解释 Manifest 如何声明组件、权限和设备特征；正文完整打开，通用 Manifest 后代仍部分覆盖。 |
| [`<supports-screens>`](https://developer.android.com/guide/topics/manifest/supports-screens-element) | 屏幕尺寸过滤；本轮相关章节部分打开。 |
| [`<uses-sdk>`](https://developer.android.com/guide/topics/manifest/uses-sdk-element) | `minSdkVersion`、`targetSdkVersion` 和 `maxSdkVersion` 锚点归并到同一参考页；本轮复核最低/目标值语义，Play 年度门槛另见独立专题。 |
| [Supporting Multiple Screens](https://developer.android.com/guide/practices/screens_support) | 通过自适应布局/资源维持广泛设备支持；部分查看，旧指南后代未穷尽。 |
| [`<uses-configuration>`](https://developer.android.com/guide/topics/manifest/uses-configuration-element) | 键盘、导航与触摸硬件需求；本轮查看相关段落。 |
| [`<uses-feature>`](https://developer.android.com/guide/topics/manifest/uses-feature-element) | 明确硬件/软件特征依赖；可选功能要与实际能力一致，已查看 Play 相关段落。 |
| [`<uses-permission>`](https://developer.android.com/guide/topics/manifest/uses-permission-element) | Play 读取权限以推断部分硬件需求；精确目标页部分查看。权限获批/允许用途仍由 Play 政策决定。 |
| [`<uses-library>`](https://developer.android.com/guide/topics/manifest/uses-library-element) | `required=true` 可将无该共享库设备过滤；已查看关键要求，其他参考后代部分覆盖。 |
| [`<compatible-screens>`](https://developer.android.com/guide/topics/manifest/compatible-screens-element) | 未列尺寸/密度组合可能被排除；已查看关键段落，官方通常建议避免。 |
| [`<supports-gl-texture>`](https://developer.android.com/guide/topics/manifest/supports-gl-texture-element) | Play 根据纹理压缩格式筛选；页面已完整打开。 |
| [Android NDK](https://developer.android.com/tools/sdk/ndk) | ABI/本地库背景；精确页面本轮 Cache miss。 |
| [Application Licensing](https://developer.android.com/google/play/licensing) | 可选的应用运行时许可机制；正文已完整打开，非 Play 审核或发布必需项。 |
| [Licensing Overview / Copy Protection replacement](https://developer.android.com/google/play/licensing/overview) | Filters 中 Copy Protection 替代方案链接落到此页；已打开。说明 Play Licensing 以购买记录判定授权，开放/封闭测试轨道的获准用户也视为授权用户；旧 draft 测试已停用。 |
| [Android compatibility](https://developer.android.com/guide/practices/compatibility) | 通用 Android 兼容性概览；目标点击返回 Internal Error，本轮未确认其正文，相关具体 Play 规则以 Filters 原文为准。 |
| [Multiple APK support](https://developer.android.com/google/play/publishing/multiple-apks) | 解释同一 Play 条目下的差异化 APK、包名/签名/版本排序；本轮已重新打开，完整直接子链接清单见上一表。 |
| [Android Developers Content License](https://developer.android.com/license) | 文档与代码样例的许可提示；全文已打开并记录许可边界。 |

## 发布前核对清单

1. 从 Play Console 已发布产物读取最高 `versionCode`，对所有 variant/轨道执行唯一、严格递增和 `≤ 2,100,000,000` 校验。
2. 将 `versionName` 与 `versionCode` 分开管理；不通过修改展示字符串试图触发更新。
3. 优先使用 AAB 和一套广泛兼容的应用；若选择多 APK，记录每个变体的设备过滤条件、签名、包名和可升级路径。
4. 对比 merged manifest 与 Play 生成的设备兼容报告，检查必需 feature、permission 推断、共享库、ABI、屏幕声明、国家/价格设置。
5. 在新旧 Android、不同 ABI/屏幕/硬件上验证可见性、安装和升级；特别测试系统升级后用户是否能收到更高 `versionCode` 的目标 APK。
6. 对 `CAMERA` 等可能隐式指示硬件的权限做两项独立审查：设备可用范围，以及 Play 敏感权限用途/声明资格。

## 未完成范围

本轮逐项尝试了 Multiple APK 页面 27 个正文链接引用（20 个不同目标，其中 2 个是同页锚点）及 Filters 页面 24 个链接引用（17 个不同外部目标）。版本号、AAB、Filters、Manifest 概览、Licensing、Licensing Overview 和 Content License 已读到对应正文；Android NDK 的精确工具页及版本号图示 Cache miss，Android compatibility 点击 Internal Error，旧链接重定向目标和若干 Manifest/构建参考只检查相关章节。通用 API、Gradle、NDK 样例、库和 Android 版本参考的孙链接仍部分未审；本专题不宣称无限递归闭合。
