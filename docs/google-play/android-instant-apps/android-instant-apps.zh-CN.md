---
id: google-play.android-instant-apps
platform: google-play
language: zh-CN
authority: historical
status: historical
kb_checked_at: 2026-10-22
review_due: 2027-01-22
regions: [global]
topics: [instant-apps, retired-program, deep-links, credential-manager, historical-policy]
snapshot_id: play.android-instant-apps
snapshot_package: "GooglePlay-KnowledgeBase-2026-10-24-review.zip"
coverage_status: "detailed-summary"
source_url_policy: "https://support.google.com/googleplay/android-developer/answer/9900182?hl=en"
source_url_technical_requirements: "https://developer.android.com/topic/google-play-instant/tech-requirements"
source_url_ux_best_practices: "https://developer.android.com/topic/google-play-instant/best-practices/apps"
source_url_smart_lock: "https://developers.google.com/identity/smartlock-passwords/android/overview"
source_url_credential_manager: "https://developer.android.com/training/sign-in/passkeys/"
source_url_deep_links_console: "https://support.google.com/googleplay/android-developer/answer/12463044"
source_url_android_app_links: "https://developer.android.com/training/app-links"
effective_date: "retired December 2025; checklist pages updated 2026-06-24 do not revive the program; no 2027-01-27"
---

# Android Instant Apps（已停用）：政策与历史实现指南

> **导入说明（Google batch 8）。** 正文来自已经分开的 2026-10-24 Google Play 知识库快照（`play.android-instant-apps`，核对日 2026-10-22）的改写摘要，不是官方页面的逐字副本。英文官方页面是效力来源。`kb_checked_at` 是快照源文件记录的核对日；本次导入没有重新打开线上官方页面。文中“本知识库”“本库”“本地专题”等说法描述的是该快照库的覆盖范围，不是本仓库已经导入的页面。指向本仓库没有收录的专题、链接图、台账或 CSV 的相对链接改为文字提及。指向 Google batch 1–7 或本批十三个专题的相对链接改为本仓库文件。核对日 2026-10-22。两种语言文件引用的 Instant Apps 帮助页都是英文 `hl=en`。快照没有记录已核对的中文官方政策页，也没有记录 `hl=zh-CN` 抓取失败。中文是编辑改写。该项目已于 2025 年 12 月停用。不能再通过 Google Play 发布 Instant App，Instant API 不再工作，Play 也不再以任何机制提供 Instant Apps。技术和体验页标注 2026-06-24 更新，但仍载明停用通知。这些更新日期不表示项目恢复。没有 2027-01-27。历史 Instant 条款不是现行发布要求。已安装应用仍适用现行开发者计划政策、用户数据和权限规则。证据等级：Historical。

**复核日期：2026-10-22。** Google Play 的 Android Instant Apps 政策帮助页仍可打开，但它引用的项目已停止。Android Developers 当前技术清单明确：自 **2025 年 12 月起**，不能再通过 Google Play 发布 Instant App，Google Play services 的 Instant APIs 不再工作，Play 也不再以任何机制向用户提供 Instant App。因此，本专题把 `answer/9900182` 的具体规则作为**历史政策和旧实现资料**保存，不把它们当作当前新应用的上架要求。

## 当前状态与迁移方向

- Instant Apps 项目已停用；如果维护的应用/游戏仍含 Instant App 模块或 Google Play services Instant API 调用，应先核查并移除失效依赖。
- Android Developers 建议把用户导向常规已安装应用，并在适用时用深层链接直接打开相应功能。针对网站 URL，Android App Links 是官方推荐方案之一。
- 如果旧实现依赖 Smart Lock for Passwords，所链接的 Google 身份文档已标记该技术弃用，并建议迁移到 Credential Manager。该身份验证指导适用于常规 Android 登录迁移，不构成仍可发布 Instant Apps 的证据。
- 现行开发仍须遵循通用 Developer Program Policy、数据/权限、欺骗行为和适用的 Android 技术规则；旧 Instant Apps 专项条款不替代这些现行要求。

## `answer/9900182` 的历史政策内容

帮助页把以下项目列为 Instant Apps 的专项要求。由于项目已停用，下面只用于理解旧应用代码、历史审核材料和迁移原因：

| 历史政策主题 | 原帮助页所述要求 | 当前解释 |
| --- | --- | --- |
| 身份验证 | 含登录功能的 Instant App 使用 Smart Lock for Passwords。 | 所链接 Smart Lock 技术文档现标记为 deprecated；新登录实现应评估 Credential Manager。旧政策页未同步更新。 |
| 链接处理 | 若链接可能解析到 Instant App，应正确路由到 Instant App，不能由应用用 WebView 截获。 | Instant App 目标已不存在；网站到普通安装应用的路由应改用当前深层链接/App Links 方案并测试浏览器/Play fallback。 |
| 安装提示 | 安装完整应用不能成为 Instant App 的主要目的；安装按钮使用 “install” 与指定图标；隐式安装提示不超过 2–3 次；不得用广告式横幅诱导安装。 | 仅作旧体验规则记录，不是现行 Play Instant 发布控制。 |
| 设备状态与可见性 | Instant App 不得造成超出会话的持久设备更改；应用运行时应持续对用户可见。 | 这是退役产品的专项规则。普通安装应用仍须遵循适用的用户数据、权限和透明度政策。 |
| 设备标识符 | 禁止访问会话结束后仍存在且不能由用户重置的标识符（例如 build serial、MAC、IMEI/IMSI）；不得通过其他方式 fingerprint 用户。手机号仅可在运行时权限下获取。 | 作为旧实现的隐私审查线索；当前设备标识符使用应另按 User Data、敏感权限和 Android 平台规则核对。 |
| 网络流量 | Instant App 网络流量须通过 TLS（如 HTTPS）加密。 | 属于历史页面的明确要求；当前应用仍应按适用的网络安全与数据保护要求实现安全传输。 |

## 正文直接链接及其后代

`answer/9900182` 正文还链接 Developer Program Policies、Smart Lock、WebView、Instant 技术清单、Material “get app” 图标和 UX 最佳实践。以下把正文链接、技术资源和访问边界分开记录：

| 目标页 | 内容、与父页关系及访问状态 |
| --- | --- |
| [Google Play Developer Program Policies（旧链接）](https://support.google.com/googleplay/android-developer/answer/9904549) | 从 Instant Apps 页面点击后返回 HTTP 404。现行综合政策请使用项目中的[Developer Program Policy 双语页](../developer-program-policy/developer-program-policy.zh-CN.md)，并从官方政策中心核对现行原文。 |
| [Smart Lock for Passwords：Android integration flow](https://developers.google.com/identity/smartlock-passwords/android/overview) | 旧 URL 重定向到集成流程页。页面标记 Smart Lock 已弃用，并推荐迁移到 [Credential Manager](https://developer.android.com/training/sign-in/passkeys/)。流程说明旧凭证的获取、保存、hint 和退出登录行为；不要把旧 API 调用直接视作新项目建议。 |
| [Credential Manager：用户登录](https://developer.android.com/training/sign-in/passkeys/) | Smart Lock 文档所链的迁移方向；页面覆盖密码、passkey、联合身份登录等 Credential Manager 指南。这里只记录其作为替代技术的关系，不把整套 Android 身份 API 文档复制进 Play 政策库。 |
| [Android `WebView` API 参考](https://developer.android.com/reference/android/webkit/WebView.html) | Instant Apps 政策把 WebView 作为“不要截获本应解析到 Instant App 的链接”的反例。API 页面是大型通用参考，不是 Instant Apps 审核指南；其全部 API 成员和后代未展开。 |
| [Google Play Instant 技术要求清单](https://developer.android.com/topic/google-play-instant/tech-requirements) | 页面顶部明确项目于 2025-12 停用。清单把要求区分为 Required、Best practice 和 Good to have；历史示例包括下载体积不超过 15 MB、设备存储不超过 150 MB、未缓存网络体验的推荐加载时间、返回/退出、广告样式、购买与已安装版状态迁移。全部数值和 UX 项目均属归档背景，不再作为现行 Play 上架门槛。页面于 2026-06-24 更新，顶部退役说明优先于后续历史清单。 |
| [Material Design icons（旧“get app”目标）](https://m2.material.io/icons/) | 点击后重定向至通用 Material icons 目录，未得到 Instant Apps 专属图标说明正文；旧图标和按钮标签要求按历史规则记录。 |
| [Google Play Instant UX best practices](https://developer.android.com/topic/google-play-instant/best-practices/apps) | 页面同样带有 2025-12 停用提示，标注 2026-06-24 更新。旧建议包括提供有意义的落地页、先让用户完成任务再提示安装、延后登录、安装后保留状态、不加多余 splash screen、保持安装版/即时版 UI 一致、明确安装按钮、删除不可用功能，以及区分自有内容与第三方外链。只作为旧体验原则摘要。 |
| [Verify and maintain deep links](https://support.google.com/googleplay/android-developer/answer/12463044) | 从 UX 指南所链的 Android 深层链接指南进一步进入。当前 Play Console 页面可检查域名关联、Manifest intent filters、Web URL 覆盖，并能对现有版本创建链接 patch；patch 不会自动保留到未来版本，Manifest 改动仍需发新版。账户内数据需要登录。 |
| [Android App Links 指南](https://developer.android.com/training/app-links) | 深层链接页面的 Android 技术子链；概述普通 deep link 与已验证 Android App Links 的区别，并推荐网站 URL 使用 App Links。页面于 2026-10-16 更新；适合作为退役 Instant 链接迁移后的现行技术起点。 |
| [Google Play services Instant API 参考](https://developers.google.com/android/reference/com/google/android/gms/instantapps/package-summary) | 技术清单还链接至 Instant API package summary。参考目录仍可访问，但项目退役说明称 Instant APIs 不再工作；目录可读不表示服务仍可用。API 包下完整成员树未递归。 |

页面另有 Other Programs 侧栏和 Help Community/Contact us 页脚入口；它们与 Instant Apps 正文规则分开。登录后 Console、其他程序的全部侧栏后代、WebView API 全量成员及 UX 指南所有外链未全部递归，逐 URL 状态见来源台账。

## 旧项目迁移检查

以下是工程迁移建议，不是 Google Play 新增政策条款：

1. 搜索应用模块、Gradle 依赖、Manifest 和运行时代码中的 Instant App/Instant API 引用，确认不会调用已停止的服务。
2. 把原有即时体验入口改为常规应用安装、网页 fallback 或普通 Android App Links；验证域名 `assetlinks.json`、intent filters、Play Console 深层链接诊断及各浏览器打开结果。
3. 若仍用 Smart Lock，按当前 Credential Manager 指南迁移登录流程，并验证凭证保存、用户退出和多账号切换行为。
4. 重新按现行 Developer Program Policy、权限/数据政策和具体产品功能检查，不以历史 Instant Apps 清单代替当前政策审查。

本专题是退役政策页、官方技术清单及 UX 指南的双语历史摘要，不是完整原文镜像，也不代表旧 Instant App 可以继续发布或运行。
