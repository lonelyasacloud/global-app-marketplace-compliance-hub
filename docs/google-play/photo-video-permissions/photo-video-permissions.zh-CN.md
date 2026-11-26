---
id: google-play.photo-video-permissions
platform: google-play
language: zh-CN
authority: normative
status: current
kb_checked_at: 2026-10-23
review_due: 2027-01-23
regions: [global]
topics: [photo-picker, media-permissions, minimum-scope, privacy]
snapshot_id: play.photo-video-permissions
snapshot_package: "GooglePlay-KnowledgeBase-2026-10-24-review.zip"
coverage_status: "detailed-summary"
source_url: "https://support.google.com/googleplay/android-developer/answer/16935362?hl=en"
source_url_zh: "https://support.google.com/googleplay/android-developer/answer/16935362?hl=zh-CN"
---

# 照片与视频权限、Photo Picker 和最小范围访问

> **导入说明（Google batch 2）。** 本页正文取自 2026-10-24 Google Play 知识库快照里已经分开的中文改写（`play.photo-video-permissions`，核对日 2026-10-23），不是 Google 已发布中文页面的逐字文本。英文官方页面是效力来源。`kb_checked_at` 使用快照 YAML 的 `reviewed_on` 2026-10-23；本次导入没有重新打开线上官方页面。正文保留来源里“2026-10-22 打开共用母页全文”的说法，文末又把改写依据写成 2026-10-23 可访问的官方页面。这两个快照日期不视为政策变更。文中“本知识库”“本库”“本地专题”描述的是该快照知识库的覆盖范围，不是本仓库已经导入的页面清单。快照里指向尚未导入本仓库的专题、链接图、台账或 CSV 的相对链接，已改为文字提及；指向 Google batch 1 或本批七个专题的相对链接已改到本仓库路径。快照把本页称为按当日可访问官方页面编写的双语改写，没有把这篇主文记为 `hl=zh-CN` 抓取失败。同一母页还写明联系人规则于 2027-01-27 生效；照片与视频的全面合规日在来源中是 2025-05-28，快照记为已经过去。这些日期必须分开。Play 照片与视频权限规则的证据等级是 `normative`。Photo Picker 和其他 Android 存储说明是 implementation note，不能单独证明 Play 分发资格。

**核对日期：2026-10-23。** Google Play 把用户照片视为个人和敏感数据。对于目标 API 33（Android 13）及以上的应用，只有当系统选择器（例如 Android Photo Picker）不足以支持应用核心功能时，才可请求 `READ_MEDIA_IMAGES` 或 `READ_MEDIA_VIDEO`。继续申请这些权限的应用必须在 Play Console 提交声明，说明照片/视频访问需求及 Photo Picker 或其他替代方案为什么不足；Play 会审核访问理由。2025-05-28 的全面合规期限已经过去。

## 判断规则

| 应用需求 | 推荐或要求 |
| --- | --- |
| 偶尔选择头像、上传一张图片/视频、提交票据等 | 使用系统 Photo Picker 或其他合适系统选择器，只把用户选中的媒体 URI 交给功能；不要为偶发选择保留整个媒体库权限。 |
| 核心功能必须持续或频繁访问共享存储中的大量照片/视频 | 评估是否确实无法用系统选择器实现；如保留 `READ_MEDIA_IMAGES` / `READ_MEDIA_VIDEO`，提交声明并说明核心功能、访问频率/范围和替代方案的技术不足，等待 Play 审核。 |
| 使用自制图片选择界面 | 自定义 UI 本身不构成宽泛权限的准入理由。若 Photo Picker 或其他方案能支持核心功能，仍应使用较窄方案；若不能，声明中要解释具体技术限制。 |
| 用户拒绝宽泛访问 | 应合理支持用户，可提供按次选择的系统选择器，或降级为仍可使用的体验；不要因非关键权限被拒绝而直接封锁全部功能。 |

Play 帮助页以图库/媒体管理和系统选择器功能无法满足的核心需求举例，但每个应用是否符合资格由其实际功能和审核决定。普通的“上传媒体”按钮或偏好自定义 UI，不应直接推导出读取整个图库的必要性。私人应用和企业设备管理应用有此项政策要求的例外；须先确认应用确属该类别。

## Photo Picker 的实现与范围

Android Photo Picker 让用户浏览本机媒体，并只授予应用所选项目的读取 URI；它不要求应用先取得整个媒体库的存储权限。Android 官方指南建议通过 `androidx.activity` 的 `PickVisualMedia` 或 `PickMultipleVisualMedia` 合约启动；若设备上 Photo Picker 不可用，库会退回 `ACTION_OPEN_DOCUMENT`。可限制媒体类型或多选数量。Photo Picker 还可显示符合条件的云端媒体提供方内容。

- 兼容性：Photo Picker 在具备 Google System Updates 的 Android 11/API 30+ 设备上可用；部分旧 Android 4.4–10 和 Android Go 设备可通过 Google Play services 获得回移版本。集成前核实目标设备与库的当前支持范围。
- URI 生命周期：系统选择的媒体通过 URI 授权读取；默认授权有生命周期限制。长时间后台上传等任务若确有需要，可使用 `takePersistableUriPermission()` 延长 URI 读取许可，并在任务完成后按产品需要清理访问状态。
- 产品体验：在用户触发具体功能时才打开选择器，限定照片/视频类型和选择数量；允许取消、重新选择和部分完成。选择器返回的 URI 仅代表用户明确选择的项目，应用仍需按 User Data 政策安全处理、披露和申报上传或共享。

### 多选回退、持久授权和 HDR 视频

Android Photo Picker 指南于 **2026-10-16** 更新。使用 `PickMultipleVisualMedia` 时，库会在可用的系统 Photo Picker 和旧设备的 `ACTION_OPEN_DOCUMENT` 回退之间选择；回退选择器不保证执行应用要求的最大选择数。因此，产品不能把 `maxItems` 当作跨设备强制上限，若上限是业务或安全条件，还应在结果处理端校验并给出清晰提示。系统多选上限可通过 [`MediaStore.getPickImagesMaxLimit()`](https://developer.android.com/reference/android/provider/MediaStore#getPickImagesMaxLimit%28%29) 查询；该 API 从 Android 13/API 33 或 R Extensions 2 提供，针对 `ACTION_PICK_IMAGES`，不能据此推断文档选择器也执行相同限制。

需要判断当前设备是否支持 Picker 时，应使用带 `Context` 的 [`isPhotoPickerAvailable(context)`](https://developer.android.com/reference/androidx/activity/result/contract/ActivityResultContracts.PickVisualMedia)：它会检查系统版本、SDK extension，以及实现回退 Picker action 的系统应用。旧的无参检查不会检测系统应用回退，且已弃用。

选择器 URI 默认授权会在应用停止或设备重启后失效。只有当返回的 URI grant 本身允许持久化时，应用才可调用 [`ContentResolver.takePersistableUriPermission()`](https://developer.android.com/reference/android/content/ContentResolver#takePersistableUriPermission%28android.net.Uri%2Cint%29)；Android 选择器的已持久媒体授权最多保留 5,000 项，超过后系统会移除最早的一项。后台上传应处理授权过期、URI 不可用和失败重选，不应把持久授权理解为永久媒体库访问。

Photo Picker 的 HDR 视频转 SDR 是**可选且默认关闭**的兼容能力：Android 13/API 33+ 可通过 AndroidX Activity 的 `MediaCapabilities` 告知支持格式，再让选择器按需转码；该 API 已包含在稳定版 `androidx.activity` **1.11.0** 中。转码会消耗时间与存储，指南给出的处理上限为 1 分钟；需要时应明确声明能力并测试原始/转码 URI。它是媒体兼容实现细节，不是 Google Play 的额外权限条件。若用多选合约，Activity 页面还提示依赖至少 1.7.0；依赖版本应按项目当前稳定版和目标设备复核。

### Android 14 的“用户选中照片”权限

Android 14/API 34 引入 `READ_MEDIA_VISUAL_USER_SELECTED` 和“所选照片访问”，让自行维护图库 UI 的应用可以处理用户授予部分访问的情形。需要遵循 Android 的权限状态、重新选择和界面刷新要求；不得假设用户曾选择的所有照片以后仍可访问。这个系统运行时能力是 Android 的实现路径，**不会替代** Google Play 对 `READ_MEDIA_IMAGES` / `READ_MEDIA_VIDEO` 广泛访问的核心功能判断和 Play Console 声明。若产品只是让用户挑选某些文件，优先使用 Photo Picker。

## 申报、审核与版本清查

如果应用保留广泛媒体权限：

1. 将权限逐项关联到商店页明确描述的核心功能，写清它为何需要频繁/持续的整库访问。
2. 解释 Photo Picker、`ACTION_OPEN_DOCUMENT` 或其他系统方案在哪个明确的技术要求上无法满足功能；“已经做了自定义 Picker”不够。
3. 在 Play Console 完成照片/视频权限声明并提交审核材料；声明应与 Manifest、实际运行行为、隐私政策和 Data safety 答案一致。
4. 检查应用和所有 SDK 的 Manifest 合并结果、动态功能模块、构建变体及 Play 的生产/测试轨道。若不符合条件，移除所有仍分发版本中的广泛权限，而非只改某一个 APK 或单一轨道。
5. 记录审核状态和被拒原因；代码或 SDK 行为变化后重新核对声明，不以旧审批覆盖新用途。

官方 2025 提醒曾要求开发者在 2025-01-22 前提交声明或移除权限，并允许申请至 2025-05-28 的延期。两项日期均已过；截至本页核对日，当前合并政策仍要求符合条件的广泛权限申请具有 Console 声明。实际应用的提交状态和 Play 审核结果只能在对应开发者账号中确认。

## 页面链接关系与覆盖状态

共用母页 [Understanding Restricted Permissions with minimum scope alternatives](https://support.google.com/googleplay/android-developer/answer/16935362?hl=en) 已于 2026-10-22 打开全文。该页合并说明 Contacts（API 37+）和 Photo/Video（API 33+）两组规则：联系人声明提示自 2026 年 9 月起在 Console 出现，联系人政策于 2027-01-27 生效并有 30 天自行延期；媒体权限的全面合规期限为 2025-05-28，已过期。其 12 项相关权限帮助侧栏与正文子链接分开记账，侧栏目标见递归链接图（快照：`../google-play-policy-link-graph.md`，未导入本仓库）第 4.1/4.2 节。

| 父页面/来源 | 目标链接 | 与本专题的关系和状态 |
| --- | --- | --- |
| 当前 Restricted Permissions 最小范围帮助页 | [User Data policy — Personal and Sensitive User Data](https://support.google.com/googleplay/android-developer/answer/10144311?hl=en) | 已读。把照片纳入个人/敏感数据规则：限制为预期功能所需用途、使用 Android 权限、确保安全，并在非预期的访问/收集情形下满足显著披露和同意要求；SDK 数据行为也由开发者负责。 |
| 当前 Restricted Permissions 最小范围帮助页 | [Android Sharesheet — Send data to other apps](https://developer.android.com/develop/ui/compose/sharing/send) | 正文已打开并纳入最小权限替代方案：Sharesheet 面向用户主动把内容发送到其他应用/联系人；若功能是从媒体库挑选或导入照片/视频，应改用 Photo Picker，而不是把 Sharesheet 当作媒体选择器。 |
| 当前 Restricted Permissions 最小范围帮助页 | [Android Photo Picker](https://developer.android.com/training/data-storage/shared/photo-picker)、[AndroidX Activity release notes](https://developer.android.com/jetpack/androidx/releases/activity) | 两页已打开。Photo Picker 以 `PickVisualMedia`/`PickMultipleVisualMedia` 限定用户选择；Activity 发布页用于核对 Picker 合约和依赖版本。该发布页内容多且持续变化，除 Picker 相关记录外不作完整版本日志镜像。 |
| Photo Picker 兼容性子链 | [Mainline / Modular System Components](https://source.android.com/docs/core/ota/modular-system)、[Google System Updates release notes](https://support.google.com/product-documentation/answer/11412553) | 均已打开并查看 Photo Picker 回移/系统更新相关内容：Mainline 允许选定系统模块独立更新；Google System Updates 记录 Photo Picker 回移。仅作兼容性依据，不扩展为新的 Play 资格条件。 |
| 当前合并版 Developer Program Policy | [Photo and Video Permissions](https://support.google.com/googleplay/android-developer/answer/18258653?hl=en#restricted-permissions-with-minimum-scope-alternatives) | 已读。确认 Android 13/API 33+ 的权限边界、系统选择器不足的核心功能测试、以及保留广泛权限时必须声明的要求。 |
| 2025-04-10 政策公告的旧照片/视频目标 | [公告](https://support.google.com/googleplay/android-developer/answer/15899442?hl=en) → [原始目标 answer/13986130](https://support.google.com/googleplay/android-developer/answer/13986130) → [现行合并敏感权限政策](https://support.google.com/googleplay/android-developer/answer/16558241?hl=en) | 2026-10-23 重试确认旧目标重定向到现行综合页；当前照片/视频章节仍要求 API 33+ 广泛权限有核心功能理由并提交声明。独立最小范围帮助页记录 2025-05-28 全面合规日已过，并列出私有/企业设备管理例外；不得将公告日期写成当前宽限期。 |
| 2023-10-25 政策公告 | [Android Photo Picker](https://developer.android.com/training/data-storage/shared/photo-picker)、[`READ_MEDIA_IMAGES`](https://developer.android.com/reference/android/Manifest.permission#READ_MEDIA_IMAGES)、[`READ_MEDIA_VIDEO`](https://developer.android.com/reference/android/Manifest.permission#READ_MEDIA_VIDEO) | 已读公告：只为与应用功能直接相关的目的访问媒体；一次或不频繁需求应使用系统选择器。公告是政策历史背景，现行要求以当前帮助页和合并政策为准。 |
| Android Photo Picker 实现指南 | [Android Privacy Codelab](https://developer.android.com/codelabs/android-privacy-codelab)、[云端媒体提供方](https://developer.android.com/guide/topics/providers/cloud-media-provider)、[AndroidX Activity 发布说明](https://developer.android.com/jetpack/androidx/releases/activity)、[Modular System Components](https://source.android.com/docs/core/ota/modular-system)、[Google System Updates](https://support.google.com/product-documentation/answer/11412553) | 2026-10-23 重开 Picker 正文及上述目标的相关章节。Codelab 展示上下文内请求权限、减少位置范围、使用 Photo Picker 和数据访问审计；其“Learn more”现跳转至 [Android Privacy & Security](https://developer.android.com/quality/privacy-and-security) 总览。云端媒体提供方目前属于 OEM 提名试点：每家 OEM 最多提名 3 个应用，入选者需满足技术和质量测试，且每个 Android profile 同时只有一个活动提供方；普通应用不能仅凭实现该 API 推出自己符合资格。若服务不是用户主要的云端照片备份/取回来源，可评估 [Document Provider](https://developer.android.com/guide/topics/providers/create-document-provider)。Activity 版本页核对到稳定版 1.11.0 已含 HDR `MediaCapabilities`；系统组件和更新页仅解释 Picker 的兼容性，属于技术后代，不新增 Play 政策资格。 |
| Photo Picker → 选择器、设备检测、多选、URI 与转码 API | [`PickVisualMedia`](https://developer.android.com/reference/androidx/activity/result/contract/ActivityResultContracts.PickVisualMedia)、[`PickMultipleVisualMedia`](https://developer.android.com/reference/androidx/activity/result/contract/ActivityResultContracts.PickMultipleVisualMedia)、[`MediaStore.getPickImagesMaxLimit()`](https://developer.android.com/reference/android/provider/MediaStore#getPickImagesMaxLimit%28%29)、[`ContentResolver.takePersistableUriPermission()`](https://developer.android.com/reference/android/content/ContentResolver#takePersistableUriPermission%28android.net.Uri%2Cint%29)、[`MediaCapabilities`](https://developer.android.com/reference/androidx/activity/result/contract/ActivityResultContracts.PickVisualMedia.MediaCapabilities) | 两个 `ActivityResultContracts` 目标均以大型 API 参考打开，并核对相关合约、设备检测与回退章节；无参 `isPhotoPickerAvailable()` 自 1.7 弃用，带 Context 的版本也检查 OEM system-app fallback。`MediaStore` 和 `ContentResolver` 相关章节已打开；`MediaCapabilities` 参考确认其自稳定版 Activity 1.11.0 提供。多选上限取合约与请求参数的较小值，但最终 `ACTION_OPEN_DOCUMENT` 回退不限制数量；Picker 页面另规定最多 5,000 项持久授权，超额时移除最早的一项。其他 API 成员和示例仍未逐项展开。 |
| Android 14 运行时分支 | [Grant partial access to photos and videos](https://developer.android.com/about/versions/14/changes/partial-photo-video-access) | 已读。说明 `READ_MEDIA_VISUAL_USER_SELECTED`、部分授权/重新选择和界面刷新；它不能取代 Play 对广泛媒体权限的声明审核。 |
| 历史期限提醒 | [Required actions by January 22, 2025](https://support.google.com/googleplay/android-developer/answer/15800983?hl=en) | 已读。声明或移除权限、覆盖测试/生产轨道、以及 2025-05-28 延期终点均为已过期迁移时限。 |
| Play Console | [App content / permissions declaration](https://play.google.com/console/) | 登录后查看具体应用表单和审核状态；公开网页无法证明某个包名获批。 |

上述链接覆盖本专题发现的政策直链与最相关的 Android 实现后代。母页的 Developer Help Community 可访问请求失败；“Contact us”点击未返回可验证目标 URL，均已记为受限。AndroidX、云媒体提供方和系统组件页面还存在一般 API 导航与工程链接；这些不作为新的 Google Play 政策分支继续无限展开。

## 发布前核对

1. 搜索 Manifest、合并 Manifest、Gradle 依赖、SDK、动态功能和所有发行轨道中的 `READ_MEDIA_IMAGES`、`READ_MEDIA_VIDEO`、`READ_MEDIA_VISUAL_USER_SELECTED` 与旧存储权限。
2. 逐项确认权限对应到何种真实功能；偶发选择改用 Photo Picker 或文件选择器。
3. 若保留广泛权限，准备核心功能证据、替代方案不足的技术说明并提交 Console 声明；在审核获准前不要把技术上可请求误认为 Play 已批准。
4. 在授权、拒绝、部分选择、撤销和应用重启/后台上传场景验证 URI 生命周期与可用性。
5. 对照隐私政策、应用内显著披露、Data safety 和 SDK 数据流，说明媒体是否上传、共享、保留或删除。

## 来源

- [Understanding Restricted Permissions with minimum scope alternatives](https://support.google.com/googleplay/android-developer/answer/16935362?hl=en)
- [Consolidated Developer Program Policy](https://support.google.com/googleplay/android-developer/answer/18258653?hl=en)
- [Policy announcement: October 25, 2023](https://support.google.com/googleplay/android-developer/answer/14016515?hl=en)
- [Android Photo Picker](https://developer.android.com/training/data-storage/shared/photo-picker)
- [Android 14 partial photo/video access](https://developer.android.com/about/versions/14/changes/partial-photo-video-access)
- [Google Play User Data](https://support.google.com/googleplay/android-developer/answer/10144311?hl=en)

本页是按 2026-10-23 可访问的官方页面编写的双语改写摘要，不是政策全文副本。Play Console 实际申报和审批状态应由对应应用的开发者账号核实。
