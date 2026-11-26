---
id: google-play.advertising-id
platform: google-play
language: zh-CN
authority: normative
status: current
kb_checked_at: 2026-10-23
review_due: 2027-01-23
regions: [global]
topics: [advertising-id, aaid, app-set-id, identifiers, privacy, ads]
snapshot_id: play.advertising-id
snapshot_package: "GooglePlay-KnowledgeBase-2026-10-24-review.zip"
coverage_status: "detailed-summary"
source_url: "https://support.google.com/googleplay/android-developer/answer/6048248?hl=en"
effective_date: "consolidated-policy-2026-09-30-current; Help 2021/2022 timeline is historical"
---

# Google Play 广告 ID（AAID）与设备标识符

> **导入说明（Google batch 4）。** 本页正文取自 2026-10-24 Google Play 知识库快照里已经分开的中文改写（`play.advertising-id`）。YAML `reviewed_on` 是 2026-10-23，开篇写核对日 2026-10-22。这两个快照日期不表示政策已经变更。它不是官方页面的逐字文本。英文官方来源是效力来源。`kb_checked_at` 使用 YAML 记录的核对日；本次导入没有重新打开线上官方页面。文中“本知识库”“本库”“本地专题”描述的是该快照知识库的覆盖范围，不是本仓库已经导入的页面清单。快照里指向尚未导入本仓库的专题、链接图、台账或 CSV 的相对链接，已改为文字提及；指向 Google batch 1–3 或本批十二个专题的相对链接已改到本仓库路径。中文源文件的 Advertising ID 帮助页地址是 `hl=zh-Hans`。快照没有记录该主帮助页的 `hl=zh-CN` 抓取失败，也没有记录已核对的中文官方页面与英文页面之间的差异。本中文页是快照的编辑改写，不是 Google 已发布中文页面的逐字文本。现行 Play 规则在快照中以 2026-09-30 生效的合并版 Developer Program Policy 为准；该日期已经过去，是现行条文。帮助页上的 2021/2022 推出时间线是历史日期，不是待完成的新期限。Android 唯一标识符指南标注最后更新 2026-10-16，App Set ID 指南标注 2026-10-21，`AdvertisingIdClient.Info` 标注 2026-01-27 更新。这些是 Android 或 API 参考的页面日期，不是未来的 Play 生效日。本页没有记录未来的 Play AAID 截止日期。Play 对 AAID 的目的、关联、重置、退出和披露要求是 `normative`。AdvertisingIdClient、Manifest 合并、App Set ID、Firebase 和 Play Integrity 的 API 材料是实现说明，不单独构成 Play 资格或审核批准。

**核对日期：2026-10-22。** 本页把 Play 的 AAID 使用规则与 Android API 实现建议分开整理。现行规则以 [2026-09-30 生效的合并版 Developer Program Policy](https://support.google.com/googleplay/android-developer/answer/18258653?hl=en) 为准；[Advertising ID 帮助页](https://support.google.com/googleplay/android-developer/answer/6048248?hl=zh-Hans)仍保留 2021/2022 年推出时间线，不能把那些历史日期当成待完成的新期限。

## 先选对标识符

| 用途 | 首选/限制 | 边界 |
| --- | --- | --- |
| 广告投放、归因、广告欺诈检测 | 设备提供时使用 AAID；不可改用 IMEI、SSAID、MAC 等其他设备标识符做广告用途 | 仍须遵守用户的广告个性化选择、重置/删除和披露要求 |
| 不涉及广告的应用分析、防欺诈 | Android 文档建议考虑 App Set ID、Firebase Installation ID 或应用私有 GUID | App Set ID 不得用于广告个性化或广告衡量；FID/GUID 范围更窄 |
| 设备真实性/反滥用 | 评估 Play Integrity API | 不是跨应用广告标识符，也不免除数据披露义务 |

## Play 对 AAID 的现行要求

- **目的限制：** AAID 仅可用于广告和用户分析；每次读取都要检查用户是否关闭了基于兴趣的广告或广告个性化。
- **分析用途的关联限制：** 不得为分析目的把 AAID 关联到个人身份信息或持久设备标识符。
- **广告用途的关联限制：** 不得为广告目的把 AAID 关联到持久设备标识符。只有取得用户明确同意，才可将其关联到个人身份信息。
- **尊重重置：** 重置后，新 AAID 不得在未经明确同意的情况下连接到旧 AAID 或旧标识符衍生的数据。
- **尊重退出和删除：** 用户退出后，不得用 AAID 建立广告用户画像或投放个性化广告；情境广告、频次控制、转化跟踪、报告、安全与欺诈检测仍属于政策列出的允许活动。删除后，较新设备上的 API 返回全零值，不得将无 AAID 的设备重新连接到旧 AAID 派生数据。
- **披露与 SDK：** 在符合法律要求的隐私通知中说明收集和使用；开发者对共享 AAID 的 SDK/业务伙伴也负有责任。Data safety、隐私政策和实际 SDK 数据流应一致。
- **广告标识符优先：** 设备提供 AAID 时，Google Play 上的应用须在广告用途使用 AAID，而非其他设备标识符。

## 儿童与混合受众

Families 的限制须单独检查：儿童专用应用不得传输儿童标识符；目标 API 33 或更高版本的儿童专用应用不得请求 AD_ID 权限。混合受众应用不得传输儿童或年龄未知用户的标识符。分流受众、第三方 SDK、广告中介和实际数据流均应纳入审核；不能因 AAID 是“标准广告 ID”就绕过 Families 或 User Data 规则。参见[年龄限制与儿童安全](../age-restricted-child-safety/age-restricted-child-safety.zh-CN.md)及 [Families 政策](https://support.google.com/googleplay/android-developer/answer/9893335?hl=en)。

## Android 实现核对

- 面向 Android 13/API 33 或更高版本，并通过 Google Play services 使用 AAID 的应用，需在最终合并的 Manifest 中包含一般权限 **com.google.android.gms.permission.AD_ID**。广告 SDK 的库 Manifest 可能会合并该权限；在 Android Studio 的 Merged Manifest 中核实实际结果。
- 缺少 AD_ID 时，相关 API 会返回全零值。它是安装时授予的一般权限，不是运行时危险权限。
- **AdvertisingIdClient.getAdvertisingIdInfo(Context)** 不可在主线程调用；需处理 Play services 不可用、连接失败或可恢复异常。读取 **Info.getId()** 时也要检查 **Info.isLimitAdTrackingEnabled()** 并执行相应退出行为。
- 每次需要时重新读取标识符，不要长期缓存；设计无 Google Play services、无 ID、退出个性化、重置和删除等状态的降级行为。
- App Set ID 应仅用于必要的非广告分析/防欺诈。Play 安装应用可能共享开发者范围 ID；非 Play 安装、无法识别开发者账号或无 Play services 时为应用范围。若连续超过 13 个月未访问、卸载最后一个相关应用或恢复出厂设置，ID 可能重置；每次需要时通过 SDK 获取，不依赖缓存值。

## 帮助页正文直接链接：目标与关系

对 [Advertising ID 帮助页](https://support.google.com/googleplay/android-developer/answer/6048248?hl=zh-Hans)正文的 13 次正文链接出现（其中政策入口重复一次）逐项去重后，得到 11 个有 URL 的不同目标。下表区分页面内容、政策作用和跳转结果；帮助页的“联系支持”控件没有暴露稳定的公开目标 URL。链接目标页的通用导航、无关 API 和站内其他页面仍不视为已经无限递归闭合。

| 正文链接目标 | 与 AAID 的关系及核验 |
| --- | --- |
| [唯一标识符最佳实践](https://developer.android.com/identity/user-data-ids)（Help 原链接：[旧入口](https://developer.android.com/training/articles/user-data-ids)会跳转至此） | Android 技术建议：按用途选择限制最严格的标识符；广告 ID 仅供广告/画像，尊重退出、不可串联重置；分析、防欺诈可评估 App Set ID/FID。它是实现指引，不是审核批准。Play Integrity API 专题（快照：`play-integrity-api.md`，未导入本仓库）补充服务条款明确禁止用 Integrity 做个人/设备指纹识别或跟踪，也整理请求数据、Device Recall 与服务端验证边界。2026-10-16 更新的正文、用途矩阵和 31 个正文链接已另在下文核验。 |
| [App Set ID 指南](https://developer.android.com/identity/app-set-id)（Help 原链接：[旧入口](https://developer.android.com/training/articles/app-set-id)会跳转至此） | 说明开发者范围/应用范围、重置条件、异步读取及不要依赖缓存。与 Play 现行政策合读：只用于必要的非广告用途，并遵循披露和关联限制。 |
| [Manifest 合并指南](https://developer.android.com/build/manage-manifests)（Help 原链接：[旧入口](https://developer.android.com/studio/build/manifest-merge)会跳转至此） | 解释应用、构建变体和 SDK 清单优先级以及合并冲突；据此检查广告 SDK 是否注入 AD_ID。它不决定应用是否有资格使用该权限。 |
| [AdvertisingIdClient.Info API](https://developers.google.com/android/reference/com/google/android/gms/ads/identifier/AdvertisingIdClient.Info) | 记录 getId() 与 isLimitAdTrackingEnabled()；缺少适用的 AD_ID 声明或用户关闭跟踪时会返回零值。页面标注 2026-01-27 更新。 |
| [AdvertisingIdClient API](https://developers.google.com/android/reference/com/google/android/gms/ads/identifier/AdvertisingIdClient)（Help 原链接：[旧 Android Developers API 路径](https://developer.android.com/google/play-services/id.html)会跳转至此） | getAdvertisingIdInfo() 不能在主线程调用，并可能因缺少/无法连接 Play services 而抛异常；只抽取 AAID 调用相关方法，不把整个 Google API 目录视为政策子树。 |
| [唯一标识符最佳实践的原始旧入口](https://developer.android.com/training/articles/user-data-ids) | 与上方现行页面是同一目标；旧路由已跳转到 /identity/user-data-ids。 |
| [Developer Program Policy 旧入口](https://play.google.com/about/monetization.html) 与[现行合并政策](https://support.google.com/googleplay/android-developer/answer/18258653?hl=en) | 旧入口实际跳转到 Help Center 的政策目录，不是 AAID 条文正文；以现行合并政策的“Usage of Android Advertising ID”条款为准。 |
| [Ads 政策](https://support.google.com/googleplay/android-developer/answer/9857753?hl=en) | 位置数据用于广告时的披露、不得仅为广告请求位置等相邻要求；不是 AAID 条款的替代品。 |
| [应用审核准备：隐私政策入口](https://support.google.com/googleplay/android-developer/answer/9859455) | 帮助页中的隐私政策链接跳到 App content/审核准备说明，解释在 Console 提供隐私政策等操作要求；不构成独立隐私政策范本。 |
| [创建并设置应用：隐私政策入口](https://support.google.com/googleplay/android-developer/answer/9859152) | 同一帮助页的另一个隐私政策链接跳到应用设置说明；是 Console 操作导航。 |
| [Developer Distribution Agreement](https://play.google.com/developer-distribution-agreement.html) | 合同层面的数据处理与法律义务背景；与 Developer Program Policy 分开适用和引用。 |
| [Advertising ID 问题排查表](https://support.google.com/googleplay/android-developer/troubleshooter/6070997) | 动态表单用于选择 SDK 违规警告、技术协助或申诉路径；不是新的政策条文，个案/账号状态需登录处理。 |

### Android 唯一标识符指南：用途矩阵与直接子链接

2026-10-22 重开现行 [Android Developers 唯一标识符最佳实践](https://developer.android.com/identity/user-data-ids)全文。页面最后更新于 **2026-10-16**。正文 **31 个链接锚点**（ID 15–45）均已尝试；重复政策/API 目标按实际落点归并；一个 Universal Analytics `Tracker.html` 方法目标返回 cache miss。页脚的 [Android Developers 内容许可](https://developer.android.com/license)另行打开。此页属于 Android 实现指导，不会扩张 Play 政策，也不构成审核通过或政策豁免。

指南的核心是：选择满足产品功能的**最窄范围、最易重置**标识符，避免无法由用户重置的硬件 ID；广告用途使用 AAID、尊重用户退出并禁止串接重置；多数非广告场景采用应用实例级 FID 或私有 GUID。标识符应按范围、持久性/重置方式、唯一性以及防伪/不可否认性一起评估，而非只比较“是否唯一”。Android 10 起 IMEI/序列号访问受限于设备/工作资料所有者、运营商特权或特权权限；普通第三方应用在 Android 6+ 不能读取设备 MAC。Android 11 的 Passpoint MAC 随配置随机化，网络信息需求宜优先走 `ConnectivityManager` 等高层 API。

| 具体用途 | 指南推荐/平台参考 | 与 Play 规则的关系 |
| --- | --- | --- |
| 运营商通话/SMS 功能 | 有真实运营商用途时可涉及 IMEI/IMSI/Line1；普通应用优先由用户登录后在服务端取运营商资料，并优雅处理权限拒绝。 | 这是 Android 技术建议；Play 的 User Data 和敏感权限规则仍独立适用。运营商权限例外需满足平台访问条件。 |
| SIM/订阅状态 | 使用 `SubscriptionInfo` / Subscription ID；`READ_PHONE_STATE` 是访问门槛之一。 | 文档建议从旧 ICCID 迁移，因 ICCID 属全局且不可重置标识符、较新 Android 限制了读取。具体设备/API 兼容性按 API 参考核验。 |
| 单点登录 | 使用账号管理器兼容的身份连接；只请求所需 OAuth scope。 | OAuth/账号链接是登录身份，不等同于广告 ID，也不自动授予 Play 对敏感数据的许可。桌面 OAuth 指南把本地客户端视为无法保密的 public client，建议 PKCE。 |
| 广告定向、广告衡量、转化、再营销和广告欺诈 | 使用可重置 AAID；衡量/转化也可评估 Play Install Referrer。 | Play 广告 ID 政策规定广告用途不能以不可重置硬件 ID 替代 AAID；Data safety 仍须申报广告用途。 |
| 跨本开发者应用的非广告分析 | 在不用于广告的前提下可考虑 App Set ID；应用实例级分析常用 FID。 | App Set ID 不得用于广告个性化/衡量；FID/Guid 属 Android/Firebase 技术建议，仍需纳入数据披露和 SDK 评估。 |
| 崩溃、性能、测试、跨设备安装、偏好 | 崩溃/测试可用 FID 或 App Set ID；性能可用 Firebase Performance Monitoring；跨设备 app-install 识别可用 FID/GUID；未登录偏好优先用 FID/GUID，避免跨卸载持久保存。 | 这些是按场景匹配的工程建议，不是 Play 必须采用的 SDK 清单。偏好在重装后重置可符合用户预期。 |
| 后端滥用检测与 DRM 内容保护 | Play Integrity token 用于判断请求/设备完整性；付费媒体保护使用 DRM API。 | Integrity 与 DRM 是专用 API，不是跨应用广告 ID，也不代替 User Data/Data safety 披露。 |

#### 唯一标识符指南的直接链接目标

下表单独记录该 Android 指南的直接链接及其落点；API/reference 页面仅核对与上文用途有关的内容，不把整份 Android API 导航当作 Play 政策。

| 直接链接目标 | 关系与核验结果 |
| --- | --- |
| [Android 权限概览](https://developer.android.com/guide/topics/permissions/overview) 与 [App permissions best practices](https://developer.android.com/training/permissions/usage-notes) | 旧概览路由跳转至现行权限概览；最佳实践建议按具体功能按需请求、解释拒绝后的影响、处理拒绝/撤销、审查 SDK 带入的权限，并在多种授权组合下测试。仅 SMS/通话核心功能可先按适用流程设为默认处理程序。均已打开；默认处理程序子页仍在对应短信/权限专题核对。 |
| [Device/profile owner apps](https://source.android.com/docs/devices/admin/managed-profiles) 与 [UICC carrier privileges](https://source.android.com/docs/core/connect/uicc) | AOSP 技术页面说明设备/资料所有者与运营商特权的系统语境，帮助界定 IMEI 等非重置 ID 的平台访问例外；它们不是一般应用可申请的普通运行时权限。页面已打开，具体 carrier 配置细节不在本 Play 政策摘要内。 |
| [AdvertisingIdClient](https://developers.google.com/android/reference/com/google/android/gms/ads/identifier/AdvertisingIdClient) 与 [AdvertisingIdClient.Info](https://developers.google.com/android/reference/com/google/android/gms/ads/identifier/AdvertisingIdClient.Info.html) | API 实现 AAID 获取及用户个性化限制状态读取；只检查与 AAID 有关的成员，不把 API 目录当政策。两个参考页已打开，并与上方“不在主线程调用/尊重退出”要求互链。 |
| [Ads policy](https://support.google.com/googleplay/android-developer/answer/9857753) 与 [Prominent disclosure and consent best practices](https://support.google.com/googleplay/android-developer/answer/11150561) | 前者是政策；指南中的旧 Play Ads 路由已重定向至此。后者给出应用内披露与同意界面最佳实践，不能取代 AAID/User Data 强制条文。两页正文已打开。 |
| [Developer Policy Center](https://play.google.com/developer-content-policy/) 的两个旧入口：[无扩展名路由](https://play.google.com/about/developer-content-policy)及[带 `.html` 路由](https://play.google.com/about/developer-content-policy.html) | 正文两处链接均重定向至当前政策中心；读当前 DPP 中的 Android Advertising ID 条文，不将旧 URL 误记为两个不同现行政策。 |
| [Advertising ID Help](https://support.google.com/googleplay/android-developer/answer/6048248) 与 [Data safety 表单帮助](https://support.google.com/googleplay/android-developer/answer/10787469) | 前者说明 AAID/Manifest 和用户设置；其中 2021/2022 日期是历史发布计划。后者要求 Data safety 反映广告用途和 SDK 数据流。两篇当前帮助正文均已有专题并已打开。 |
| [Android DRM API](https://source.android.com/docs/core/media/drm) 与 [Play Integrity API 概览](https://developer.android.com/google/play/integrity/overview) | 分别支持内容保护和完整性/滥用检测；它们不是 Android 硬件标识符的替代性广告用途。两页已打开，API 深层成员仍部分核验。 |
| [Google Analytics `enableAdvertisingIdCollection()` 目标](https://developers.google.com/android/reference/com/google/android/gms/analytics/Tracker.html) 与 [Analytics SDK policy](https://developers.google.com/analytics/devguides/collection/android/v4/policy) | 前者在打开时返回 cache miss；后者明确是 Universal Analytics 旧版政策页面，并说明 UA 于 2024-07-01 停止服务。不得把这两条旧链接当作当前 GA4 API/政策依据。 |
| [Firebase Installations Android API](https://firebase.google.com/docs/reference/android/com/google/firebase/installations/package-summary) 与 [Manage Firebase installations and IDs](https://firebase.google.com/docs/projects/manage-installations) | FID 按每个 app installation 区分；官方指南说明 Firebase 服务如何使用 FID、如何删除及检索。删除 installation ID 后，关联数据的线上/备份清除最长可到 180 天；新 FID 可能几天后生成；删除 FID **不会删除 Google Analytics for Firebase 数据**，应另走 Analytics 删除流程。已打开；SDK 产品及后代需按实际依赖审阅。 |
| [Android data and file storage overview](https://developer.android.com/training/data-storage) | 说明 app-private internal storage、共享存储、偏好和数据库等选项；GUID 等 app-private ID 应保存在应用私有存储以避免跨应用共享。正文已打开；各存储 API 样例未全量展开。 |
| [Linux `getifaddrs()`](https://android.googlesource.com/platform/bionic/+/master/libc/include/ifaddrs.h)、[NetworkInterface](https://developer.android.com/reference/java/net/NetworkInterface)、[ConnectivityManager](https://developer.android.com/reference/android/net/ConnectivityManager) 与 [LinkProperties](https://developer.android.com/reference/android/net/LinkProperties) | 这些是指南在 MAC 地址受限后给出的技术调用上下文。链接已打开；网络路由用例优先考虑 ConnectivityManager/network callback 与 LinkProperties，高层 API 参考不意味着可读取被限制的硬件 MAC。 |
| [SubscriptionInfo](https://developer.android.com/reference/android/telephony/SubscriptionInfo) 的订阅/ICCID链接与 [Manifest.permission](https://developer.android.com/reference/android/Manifest.permission) | 对照 Subscription ID、ICCID 和 `READ_PHONE_STATE` 权限定义；同一 API 页面在正文重复引用。大型 API 参考已打开，全部成员和版本兼容性未逐项复核。 |
| [Google Account Linking](https://developers.google.com/identity/account-linking) 与 [OAuth 2.0 for native/desktop apps](https://developers.google.com/identity/protocols/oauth2/native-app) | 前者提供用户主动关联/解除账号的流程；后者解释 OAuth scope 最小化、public-client 和 PKCE。它们说明认证/授权方案，不能替代 Play User Data 数据最小化、披露或删除要求。两页已打开。 |
| [Firebase Performance Monitoring](https://firebase.google.com/products/performance) | 按性能报告场景推荐的 Firebase 产品入口；产品页已打开。实际 SDK 数据收集/分享应另核 SDK 文档和 Data safety。 |
| [Android Developers Content License](https://developer.android.com/license)（源指南页脚） | Android 文档内容的许可规则按 documentation 与 other site content 分类，且链接出去的内容不会自动继承 Android 文档许可；这只是 Android Developers 站点自己的内容许可说明，不代表 Play Help/Developer Policy 全文可离线再发布。 |

#### App Set ID 指南 → API 与异步读取后代

2026-10-23 重新打开了 [App Set ID 指南](https://developer.android.com/identity/app-set-id)（页面标注 2026-10-21 更新），并继续核对其正文中的 API、异步任务、Google Play services、UUID 和许可链接。Android 实现建议只能解释如何读取及其技术范围，不能单独授予 Play 数据收集资格。

| 父页 → 直接目标 | 内容及与 Play/AAID 的关系 | 核验状态 |
| --- | --- | --- |
| App Set ID 指南 → [Google Play services](https://developers.google.com/android) | 产品入口介绍 Google Play services 的 Android API 能力；它不是 App Set ID 专属规则页，也不是 Play 开发者政策。 | 入口页已打开；通用产品目录及其 API 后代没有穷尽。 |
| App Set ID 指南代码示例 → [`AppSet` API 与 `getClient(Context)`](https://developers.google.com/android/reference/com/google/android/gms/appset/AppSet) | `AppSet` 是 API 入口，静态 `getClient(Context)` 返回 `AppSetIdClient`。这是技术调用链，不是读取用户数据的 Play 许可。 | 类正文、唯一公开方法及 `AppSetIdClient`/`Context` 类型目标已核对；共享 API 目录导航不在本轮穷尽范围。 |
| `AppSet.getClient()` → [`AppSetIdClient`](https://developers.google.com/android/reference/com/google/android/gms/appset/AppSetIdClient) | 客户端仅公开 `getAppSetIdInfo()`，异步返回 `Task<AppSetIdInfo>`；调用后从结果读取 ID 与 scope。按 Tasks 指南处理失败和生命周期，避免阻塞 UI。 | 方法签名和直接类型链接已核对；通用 `Task` 类型的完整成员/后代仍按 Tasks 专题另行跟进。 |
| App Set ID 指南 → [`AppSetIdInfo` API](https://developers.google.com/android/reference/com/google/android/gms/appset/AppSetIdInfo)（含 `getScope()`） | `getScope()` 返回 `SCOPE_APP`（值 `1`）或 `SCOPE_DEVELOPER`（值 `2`）；`getId()` 返回当前范围的 ID。Play 安装且可识别开发者账号时可使用开发者范围，同一开发者在同一设备上的应用可共享该范围；其他安装来源、无法识别账号或无 Play services 时为应用范围。范围和返回值是实现信息，不改变儿童/未知年龄用户的 Play 规则。 | 大型 API 参考已打开并核对该类及相关成员；其他类成员、版本和 API 目录未逐项审计。 |
| `AppSetIdInfo.getScope()` → [`AppSetIdInfo.Scope` 注解](https://developers.google.com/android/reference/com/google/android/gms/appset/AppSetIdInfo.Scope) | `Scope` 只允许 `SCOPE_APP` 与 `SCOPE_DEVELOPER` 两个常量，分别表示应用范围和商店开发者账号范围；它没有新增 Play 政策例外或额外用途授权。 | 注解参考及常量目标已打开；继承自 Java `Annotation` 的通用方法只作 API 类型背景，未展开其完整继承树。 |
| App Set ID 指南 → [Google Play services Tasks](https://developers.google.com/android/guides/tasks) | App Set ID 通过异步 `Task` 获取。指南说明成功/失败/完成监听、默认在主/UI 线程回调、Activity 生命周期范围的监听，以及在后台线程等待和与 Kotlin 协程互操作。实现需处理失败/服务不可用，不要阻塞主线程。 | 已审阅异步结果、回调线程、生命周期和协程相关段落；通用示例、完整任务指南及其后代仍部分覆盖。 |
| App Set ID 指南 → [UUID 参考](https://en.wikipedia.org/wiki/Universally_unique_identifier) | 第三方格式背景资料，不是 Android/Google Play 官方政策，也不用于推导 App Set ID 的合规资格。 | 仅打开相关内容作背景核对；不作为规则依据，页面后代未审计。 |
| App Set ID 指南 → [Android Developers Content License](https://developer.android.com/license) | Android 文档与其他站点内容可能适用不同许可，外链页面不会自动继承 Android 文档许可。该说明不代表 Play Help 或 Developer Policy 可全文复制再发布。 | 正文已重新打开；本知识库保留改写摘要与官方链接，不据此主张 Play 来源全文的再发布权。 |

**Play 政策边界：**App Set ID 的开发者范围、可重置性或 Android API 示例都不是对特定数据流的 Play 批准。广告用途禁用 App Set ID；儿童或年龄未知受众还要满足现行 Families、User Data、Data safety 与 SDK 要求，并检查实际 SDK 是否向外传输。每次需要时通过 SDK 获取并处理 ID 重置，不以本地缓存绕过重置/删除。

递归边界：本节现已把 Families 数据实践页 → App Set ID 指南 → `AppSet` → `AppSetIdClient` → `AppSetIdInfo`/`Scope` 的相关调用链补到可读 API 成员层，并登记通用类型关系。Google Play services 通用目录、API 全量成员、Tasks 示例/子链接和 Firebase 各 SDK 供应商后代仍按目标类型分层递进，不声称无限闭合。Android Guides 内容的许可范围按 [Content License](https://developer.android.com/license) 原文判断；政策摘要继续改写并保留官方链接。

## 发布前检查

1. 从 AAB、依赖树和最终合并 Manifest 核实 AAID SDK、AD_ID 权限和各变体差异。
2. 逐项测试用户退出、重置、删除、无 ID、无 Play services 和儿童/年龄未知受众下的 SDK 行为。
3. 检查广告与分析数据管道没有禁止的 AAID—PII/持久标识符连接；验证旧 ID 派生数据不会绕过重置或删除。
4. 对照隐私政策、应用内披露、Data safety 和 SDK/广告中介实际网络行为。
5. 保留 SDK 版本、权限结果、同意状态、测试记录和 Play Console 通知，便于申诉或复审。

相关专题：[广告与推广](../ads-and-advertising/ads-and-advertising.zh-CN.md) · [用户数据](../user-data/user-data.zh-CN.md) · Android 隐私清单（快照：`android-privacy-checklist.md`，未导入本仓库） · [年龄限制与儿童安全](../age-restricted-child-safety/age-restricted-child-safety.zh-CN.md) · 第三方 SDK（快照：`sdk-requirements.md`，未导入本仓库）
