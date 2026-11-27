---
id: google-play.play-console-app-setup
platform: google-play
language: zh-CN
authority: operational
status: current
kb_checked_at: 2026-10-24
review_due: 2027-01-24
regions: [global]
topics: [app-setup, app-bundle, app-signing, store-listing, testing, release]
snapshot_id: play.app-setup
snapshot_package: "GooglePlay-KnowledgeBase-2026-10-24-review.zip"
coverage_status: "detailed-summary"
source_url: "https://support.google.com/googleplay/android-developer/answer/9859152?hl=en"
source_url_search_discoverability: "https://support.google.com/googleplay/android-developer/answer/4448378?hl=en"
effective_date: "operational setup; Personal-account closed-test gate applies to accounts created after 2023-11-13; target-API extension 2026-11-01 kept separate from 2027-01-27"
---

# Google Play Console 创建应用与上架准备

> **导入说明（Google batch 7）。** 正文来自已经分开的 2026-10-24 Google Play 知识库快照（`play.app-setup`，核对日 2026-10-24）的改写摘要，不是官方页面的逐字副本。英文官方页面是效力来源。`kb_checked_at` 是快照源文件记录的核对日；本次导入没有重新打开线上官方页面。文中“本知识库”“本库”“本地专题”等说法描述的是该快照库的覆盖范围，不是本仓库已经导入的页面。指向本仓库没有收录的专题、链接图、台账或 CSV 的相对链接改为文字提及。指向 Google batch 1–6 或本批十二个专题的相对链接改为本仓库文件。核对日 2026-10-24。两种语言文件都把创建应用的 `source_url` 记为 `hl=en`。快照没有记录已核对的中文官方创建应用页，也没有记录该主文章 `hl=zh-CN` 路由抓取失败。本仓库中文正文是编辑改写。中文文件的部分后代链接使用 `hl=zh-CN`。“Creating a compelling store listing” 的点击返回 Internal Error，没有暴露 href。帮助社区和 Contact us 抓取失败。旧的订阅 `revoke` 与 `refund` API 路径返回 404。这些访问限制不是政策变更。目标 API 延期到 2026-11-01 与要求页记录的是同一个目标 API 日期。按本源文件引用的 2026-10-22 核对，该日期当时仍未到来，也不是 2027-01-27 预告。2023-11-13 之后创建的个人账号封闭测试是该账号群体的现行门槛，不是未来预告。本页没有记录 2027-01-27。本页是 operational 的设置指南。接受条款或完成仪表盘任务不表示应用已通过审核。版本号和 App Bundle 材料是 implementation note。

**核对日期：2026-10-24。** 本文依据官方[创建和设置应用](https://support.google.com/googleplay/android-developer/answer/9859152?hl=en)页面整理，覆盖新建应用、Dashboard 准备任务、构建与签名、商店详情、联系人和它直接指向的重要帮助页。评分发现度子链另行核验了分析群组、测试反馈、回复权限与 API 范围。页面是操作指南，不等于对某个应用的审核结论；账号状态、动态政策期限和 Console 表单需在对应开发者账号中核验。

## 从创建到上线

| 阶段 | 官方要求或流程 | 与审核/政策的关系 |
| --- | --- | --- |
| 创建应用 | 在 Play Console 新建应用，选择默认语言、应用/游戏类型和免费/付费类型，填写用户联系邮箱，并确认 Developer Program Policies、美国出口法律声明和 Play App Signing 服务条款。默认语言可后改；游戏类型页面也称可后改。 | 创建动作要求先有 Play Console 开发者账号；接受服务条款是签名服务的合同步骤，政策声明则关联当前开发者政策。不要把点击确认误作应用已通过政策审核。 |
| 创建后准备 | Dashboard 按 App content、商店详情、测试/版本、发布和推广组织任务；必须完成的任务会标示状态，完成后更新进度。发布后仍可回 Dashboard 看指标与趋势。 | 具体待办依应用和账号而变；账号登录页面无法证明任何特定应用的声明已提交或获批。申报细目见[审核准备专题](../app-review-preparation/app-review-preparation.zh-CN.md)。 |
| 测试与发布 | 先管理预发布、测试和推广，再向 Production 发布。新建于 **2023-11-13 之后的个人开发者账号**须先满足封闭测试要求，才能申请生产权限；不要把该门槛套用到组织账号或其他创建日期。 | 当前帮助页列出至少 12 名测试者连续 opt-in 14 天及生产权限问卷，详见[新个人账号测试专题](../publishing/play-release-workflow.zh-CN.md)。正式提交、预检和上线是不同阶段，见[发布流程](../publishing/play-release-workflow.zh-CN.md)。 |

## 包名、构建产物与版本

- **包名不可回收：** Play 要求应用文件的 package name 唯一且永久；创建时仔细选择，不能删除后给另一应用重用。新 Play 应用与 Android 开发者验证的包名登记关联，详见开发者验证专题[Android 开发者验证](../android-developer-verification/android-developer-verification.zh-CN.md)。
- **AAB 与生成 APK：** Play 使用 Android App Bundle 为不同设备配置生成优化 APK；开发者上传一个签名 bundle，Play 负责分发 APK。新应用的 App Bundle、Play App Signing 和生成/交付状态见下方直链表及[发布流程中的签名专题](../publishing/play-release-workflow.zh-CN.md)。
- **产物状态：** 来源帮助页用 Draft、Active、Archived 描述未向用户提供、正在提供和曾经提供但不再提供的 APK。新版 Console 的 App Bundle Explorer 可按版本检查 Details、Downloads、Delivery；这是账号内工具，用户级状态须登录查看。
- **[版本号](../app-version-codes-and-apk-distribution/app-version-codes-and-apk-distribution.zh-CN.md)：** `versionCode` 随每次更新递增；Play Console 当前帮助页规定最大值为 **2,100,000,000**，超出会阻止提交新 App Bundle。Android `MAXINT` 与 Play 上传限制不是一回事，版本规划应留出后续更新空间。
- **Target API：** 每个上传的 bundle 都须符合当期 target API 要求。截止本次核对日，官方页列出的 2026-08-31 提交门槛、设备形态例外、旧应用可见性和 2026-11-01 延期，应以[目标 API 专题](../target-api/target-api-level.zh-CN.md)和当前 Console 警告为准，不将静态摘要当作下一年度规则。
- **下载大小：** Play 按压缩后的下载体积评估 App Bundle、feature module 和 asset pack。当前帮助页列出 base module/单个 feature module 各 500 MB、单个 asset pack 1.5 GB、安装时累计 4 GB、fast-follow/on-demand 累计 30 GB、应用总计 34 GB；超过 200 MB 时移动网络安装会出现非阻塞提示。超过 1 GB 的应用须将 minSdk 设为 API 21 或更高。旧 APK 路径仍受 100 MB 限制。数字和打包规则可能更新，应重查[官方大小限制页](https://support.google.com/googleplay/android-developer/answer/9859372?hl=en)；生产发布后才能在 App size 页面查看实际下载大小趋势。

## 商店详情、语言和联系信息

商店详情跨测试轨道共用。主详情页当前字段上限为应用名 **30**、简短说明 **80**、完整说明 **4,000** 个字符；全角与半角字符按相同上限计算。帮助页警告，标题/说明/宣传语中反复或无关堆砌关键词可能造成糟糕体验并导致应用暂停。素材的类型、规格和准确性见[商店详情与素材最佳实践](../store-listing-best-practices/store-listing-best-practices.zh-CN.md)。

应用默认语言为 en-US。开发者可添加应用信息翻译和对应截图/图形素材；用户语言偏好匹配时会显示相应版本。若未提供自有翻译，Play 可能显示机器翻译并注明其自动生成；该帮助页列出 Armenian、Raeto-romance、Tagalog、Zulu 暂不支持自动翻译。另有商店详情/商品翻译服务及 Gemini 应用字符串翻译选项，具体语言、账号资格和费用以[翻译与本地化帮助页](https://support.google.com/googleplay/android-developer/answer/9844778?hl=en)及当前 Console 为准。

分类应反映应用主要用途；最多选 5 个相关标签，标签与商店详情或首次使用体验之间应有清晰关系。内容或功能显著变化时重新评估。无障碍标签可帮助用户识别屏幕阅读器、视觉、听力、学习、运动或沟通辅助能力。详情见[分类与标签帮助页](https://support.google.com/googleplay/android-developer/answer/9859673?hl=en)和本库[商店详情专题](../store-listing-best-practices/store-listing-best-practices.zh-CN.md)。

每个应用必须提供有效且准确的支持邮箱；Google 强烈建议同时提供可联系网站，电话为可填写的补充信息。用户会在商店详情中看到这些联系方式。单独的用户支持帮助页还要求：付费应用/应用内购买问题通常须在 **3 个工作日内**回复；Google 联系开发者处理紧急产品问题时须在 **24 小时内**回复；退款须按适用法律及开发者退款政策处理，并及时告知政策变更。FAQ、网站或持续维护的论坛有助于自助支持。该帮助页直接指向消费者[Google Play 退款政策](https://support.google.com/googleplay/answer/2479637)和[Play Console 订单/退款管理旧入口](https://support.google.com/googleplay/android-developer/answer/9859683)，后者重定向至[现行退款操作页](https://support.google.com/googleplay/android-developer/answer/2741495)。这两类页面分别解释买家退款路径与开发者账单操作；退款/取消规则不应混为一谈。另见[付款/退款专题](../payments/payments-and-subscriptions.zh-CN.md)。

## 正文直接链接：目标页内容与关系

以下覆盖来源页正文里的直接链接，重复的链接按目标合并。账号内路由、公开帮助正文和培训材料分别标明；相关政策内容优先跳转到已有双语专题，避免重复复制。

| 直接链接目标 | 目标页内容及与创建/发布的关系 | 本库核验结果 |
| --- | --- | --- |
| [Play Console](https://play.google.com/console/)；[App Bundle Explorer](https://play.google.com/console/developers/app/bundle-explorer-selector)；[Main store listing](https://play.google.com/console/developers/app/main-store-listing)；[Store settings](https://play.google.com/console/developers/app/store-settings) | 创建应用、浏览 bundle 与版本、编辑详情和联系人信息的实际入口。 | Console 首页本次跳转到 Play for Business 公开营销页；具体应用/账号状态均需登录，不能从公开页推断。 |
| [Developer Program Policy 旧入口](https://play.google.com/about/developer-content-policy/) → [现行政策中心](https://play.google/developer-content-policy/)；[DDA 旧入口](https://play.google.com/about/developer-distribution-agreement.html) → [现行 DDA](https://play.google/developer-distribution-agreement.html) | 创建时分别确认政策与协议；素材用于 Google Play 推广的许可关系见 DDA 第 6 节 Brand Features and Publicity。 | 旧入口均重定向到现行正文；已分别纳入政策中心（[开发者政策中心](../google-play-developer-policy-center/google-play-developer-policy-center.zh-CN.md)）、[合并版政策](../developer-program-policy/developer-program-policy.zh-CN.md)和[DDA](../developer-distribution-agreement/developer-distribution-agreement.zh-CN.md)。 |
| [Play App Signing Terms 原入口](https://play.google.com/about/play-app-signing-updated-terms/) → [现行服务条款](https://play.google/play-app-signing-terms/) | AAB/签名服务的专门合同条款与 DDA、Developer Program Policies 并行；条款说明开发者可提供密钥或让 Google 生成/保管密钥，Google 可为生成分发 APK 使用 App Bundle 并为性能、安全或体积优化 APK。加入服务后，交给/由 Google 生成的密钥不能取回；签名服务条款冲突时优先适用于该服务。 | 旧入口已跳转到现行条款页，正文已打开并提取上述对发布影响最大的条款；密钥管理和轮换另见[Play App Signing 专题](../publishing/play-release-workflow.zh-CN.md)。不是全部合同逐字转载。 |
| [新个人账号测试门槛](https://support.google.com/googleplay/android-developer/answer/14151465?hl=en)；[Dashboard 设置说明](https://support.google.com/googleplay/android-developer/answer/9859454?hl=en) | 前者定义特定新个人账号的闭测与申请生产权限步骤；后者说明 Dashboard 强制任务、进度、App content/商店详情/测试/预注册/正式发布顺序和上线后指标。 | 两页正文已打开；测试要求和 Dashboard 入口已与[发布流程](../publishing/play-release-workflow.zh-CN.md)交叉整理。个人账号表单需登录，任务和指标因应用而异。 |
| [Google Play Games on PC](https://developer.android.com/games/playgames/overview) | 创建帮助页称免费游戏默认同时出现在 Play Games on PC；付费游戏需要开发者另行发布。该目标是 PC 游戏分发/兼容性入口，不是一般 Play 上架政策。 | Android Developers 页面已打开；仅保留与创建向导相关的免费/付费区别，PC 兼容和发布子流程见官方指南。 |
| [Android App Bundles](https://developer.android.com/guide/app-bundle/)；[Inspect app versions](https://support.google.com/googleplay/android-developer/answer/9844279?hl=en)；[Optimize app size](https://support.google.com/googleplay/android-developer/answer/9859372?hl=en) | AAB 生成设备优化 APK；App Bundle Explorer 的 Details/Downloads/Delivery 展示版本、下载物和条件交付；大小帮助页说明压缩体积限制、参考设备/配置范围、同类比较与历史趋势。 | AAB/版本页和 App size 帮助正文已打开；账号内 Explorer 与实际下载数据不能公开访问。大小上限列在本页上方，并须发布前重核。 |
| 大小帮助页下游：[bundletool](https://developer.android.com/tools/bundletool) 与 [Play Console App size](https://play.google.com/console/u/0/developers/app/vitals/app-size) | `bundletool` 是 Android Studio/Gradle/Play 构建 AAB 的底层工具，可本地生成设备配置 APK 并估算压缩下载大小；Play Console App size 展示生产应用的实测下载大小和设备范围。 | bundletool 正文已打开，2026-08-28 更新；其估算与 Play 上传侧计算相近但不完全相同。App size 路由跳转 Google 登录，实际数据需账号。 |
| [Android Studio signing guide 旧入口](https://developer.android.com/tools/publishing/app-signing.html) → [现行签名指南](https://developer.android.com/studio/publish/app-signing)；[Use Play App Signing](https://support.google.com/googleplay/android-developer/answer/9842756?hl=en) | 前者说明本地签名密钥和上传流程；后者区分开发者持有 upload key 与 Google Play 持有的 app signing key、AAB 签名服务和密钥升级。最终分发 APK 的证书指纹可能与本地上传证书不同。 | 旧 Android Developers 链接重定向到现行签名指南；两个正文均已打开。本地密钥操作、密钥托管和第三方 API 指纹风险见[签名与发布专题](../publishing/play-release-workflow.zh-CN.md)。 |
| [Version your app](https://developer.android.com/studio/publish/versioning.html)；[Target API level requirements](https://support.google.com/googleplay/android-developer/answer/11926878?hl=en) | Android 版本指南解释 minSdk/targetSdk/versionCode 的构建配置；Play 页面另列年度新应用/更新提交门槛、既有应用对新系统用户的可见性规则、设备形态例外和延期流程。 | Android 版本资料用于实现；Play 当前门槛已在[目标 API 专题](../target-api/target-api-level.zh-CN.md)逐项整理。每年 deadline 会变。 |
| [Testing tracks](https://support.google.com/googleplay/android-developer/answer/9845334?hl=en) | 说明 Internal、Closed、Open 与 Production 轨道的测试/发布用途和访问方式。 | 已在[测试与发布流程](../publishing/play-release-workflow.zh-CN.md)摘要；轨道分配和账号权限以 Console 为准。 |
| [Preview assets](https://support.google.com/googleplay/android-developer/answer/9866151?hl=en)；[Translate and localize](https://support.google.com/googleplay/android-developer/answer/9844778?hl=en)；[Categories and tags](https://support.google.com/googleplay/android-developer/answer/9859673?hl=en) | 预览素材帮助覆盖图标、短说明、截图和视频；翻译页说明详情/应用内商品/字符串本地化；分类页要求最多 5 个高度相关标签，并支持无障碍标签。 | 三个目标已读；正文要点分别见[商店详情最佳实践](../store-listing-best-practices/store-listing-best-practices.zh-CN.md)与本页上方。 |
| [How to support your app's users 旧入口](https://support.google.com/googleplay/android-developer/answer/9859041?hl=en) → [现行用户支持页](https://support.google.com/googleplay/android-developer/answer/113477?hl=en) | 用户支持邮箱必填；付费/内购支持 3 个工作日内回复，紧急产品问题 24 小时；依政策退款并维护用户可用的支持资源。直接子链接还包括消费者退款政策、订单退款管理、DDA/开发者政策与账号内 Store settings。 | 用户支持旧 URL 重定向后正文已打开；退款/订单两篇直接子页已打开。Console 路由仍需登录。可能适用的消费者法义务见[付款与订阅专题](../payments/payments-and-subscriptions.zh-CN.md)。 |
| [Prepare your app for review](https://support.google.com/googleplay/android-developer/answer/9859455?hl=en)；[Publish your app](https://support.google.com/googleplay/android-developer/answer/9859751?hl=en)；[Managed publishing](https://support.google.com/googleplay/android-developer/answer/9859654?hl=en) | 前者列 App content 声明和审核访问要求；后两者区分审核获批与实际发布时间。 | 正文已打开并在[应用审核准备](../app-review-preparation/app-review-preparation.zh-CN.md)和[发布流程](../publishing/play-release-workflow.zh-CN.md)分别摘要。 |
| [Store listing A/B experiments 旧入口](https://support.google.com/googleplay/android-developer/answer/9859351) → [现行实验帮助页](https://support.google.com/googleplay/android-developer/answer/12053285?hl=en) | 允许测试商店详情素材/文案变体，帮助比较转化效果；不替代 Listing 政策要求。 | 旧链接已跳转至现行实验帮助页，正文已打开；试验设计和素材规则见[商店详情专题](../store-listing-best-practices/store-listing-best-practices.zh-CN.md)。 |
| “Creating a compelling store listing” | 来源页以此文字链接到额外实践指南。浏览器点击该链接返回 Internal Error，未能确认其目标 URL 或读取正文。 | 记录为未解析直接目标；可先看本库[商店详情最佳实践](../store-listing-best-practices/store-listing-best-practices.zh-CN.md)，不把它冒充成该未读取目标的全文摘要。 |
| [Academy for App Success](https://playacademy.exceedlms.com/student/collection/260728-prepare) | 提供开发者培训目录，补充创建、准备与发布流程。 | 公开课程入口已打开；课程正文需登录，未将其标记为已读政策。 |
| [Help Community](https://support.google.com/googleplay/android-developer/community?help_center_link=CNDg2QQSGkNyZWF0ZSBhbmQgc2V0IHVwIHlvdXIgYXBw&hl=en)；[Contact support](https://support.google.com/googleplay/android-developer/gethelp) | 社区讨论和账号支持入口，不构成政策正文。 | 社区页可见动态论坛入口；支持路线转至账号/Console 流程，未推断个案内容。 |

## 相关公开指南：Google Play 搜索发现度

官方搜索索引还找到公开帮助页[在 Google Play 搜索中提高发现度](https://support.google.com/googleplay/android-developer/answer/4448378?hl=en)。它是与创建应用页“打造吸引力商店详情”提示相关的另一篇帮助正文；由于原创建页无法打开且没有暴露该锚点的 href，**不能确认它就是原文未解析链接的精确目标**。

该页建议标题独特、易读、聚焦应用本身；描述先讲用户能得到什么，把重要文字放在首屏，并遵守垃圾内容、关键词堆砌、知识产权和冒充规则；截图应展示受支持设备上的真实体验并填写每张截图的独特替代文本；可用人工翻译改善不同市场的理解。它还说 Play 搜索会综合应用整体体验、用户行为与反馈，信号包括评分、评价、下载等，但权重和值属于专有算法。可执行的建议是维护有意义的体验、持续改进、倾听用户反馈并处理问题；不能从该页推导关键词密度或其他公开排名公式。

| 相关页正文直链 | 目标页内容及与 Play 搜索的关系 | 本库核验结果 |
| --- | --- | --- |
| [Creating a compelling store listing](https://developer.android.com/distribute/best-practices/launch/store-listing.html) | 该相邻帮助页的同名链接仍指向旧 Android Developers 路径；当前跳到 Play Console 的高质量应用/游戏页面。 | 目标路径需登录才能读取。它与 `9859152` 中同名文本可能相关，但原页面没有提供可确认的 href，故不将两者强行等同。 |
| [SEO best practices](https://support.google.com/webmasters/answer/35291) → [Do you need an SEO?](https://developers.google.com/search/docs/fundamentals/do-i-need-seo) | Google Search Central 页面谈的是网站在 Google 网页搜索中的 SEO 服务和风险，不是 Play 商店搜索的排名规则。Play Help 同时要求避免垃圾关键词并提醒无人能保证网页搜索第一名。 | 旧 Help URL 跳至当前 Search Central 正文，相关章节已读；将其作为网站 SEO 范围提示，不移植成 Play 排名算法说明。 |
| [Google Play Developer Policy Center](https://play.google.com/developer-content-policy/) | 搜索指南将描述优化限定在内容政策、垃圾内容和知识产权边界内。 | 目标页已读并由政策中心专题（[开发者政策中心](../google-play-developer-policy-center/google-play-developer-policy-center.zh-CN.md)）和[合并版政策](../developer-program-policy/developer-program-policy.zh-CN.md)承接。 |
| [Add preview assets](https://support.google.com/googleplay/android-developer/answer/9866151?hl=en) | 目标页解释图标、短说明、主宣传图、截图和视频的必需规格及推荐规范；素材会出现在各测试轨道。必需项不合规可能导致移除或暂停；推荐项主要影响展示/推荐机会。提交素材也授予 Google 协议约定的宣传使用许可。 | 正文本轮重新打开；部分 Android 图标与自适应布局子页已跟进。完整规格及后代见[商店详情与素材专题](../store-listing-best-practices/store-listing-best-practices.zh-CN.md)。 |
| [Translate and localize your app](https://support.google.com/googleplay/android-developer/answer/9844778?hl=en) | 目标页覆盖详情页、商品、应用字符串与本地化图形；商店详情可以自译或购买人工翻译，字符串可选择 Gemini 自动翻译。页内还引向 App Translation Service、地区定向自定义详情页及 Android 本地化工程指南。 | 正文本轮完整打开；可用语言、价格和处理时长以 Console 当前报价为准。该条不是 Google 必须替开发者翻译的承诺。 |
| [View and analyze ratings and reviews](https://support.google.com/googleplay/android-developer/answer/138230?hl=en) | 说明评分延迟、可见性、近期评分权重、分组分析、回复和评论政策；新评分通常约 24 小时后公开，发现可疑活动时可能暂停更多内容。 | 正文本轮完整打开；跨语言产品体验与排名信号不能与“操纵评分”混为一谈。政策与反操纵规则见[评分、评价与安装量专题](../user-ratings-reviews-installs/user-ratings-reviews-installs.zh-CN.md)及[评论发布政策专题](../play-store-review-posting/play-store-review-posting.zh-CN.md)。 |
| 帮助社区与 Contact us | 原页面显示社区和支持入口，但目标页抓取失败，未取得可核验 href。 | 记为两个未解析支持目标；不推断论坛内容或账号个案。 |

### 搜索指南后代：翻译、评分及反馈

- [App Translation Service 简介](https://support.google.com/l10n/answer/6359997)说明人工译者/服务商、商店文案、应用字符串和内购商品可在 Console 集成下单，并提及复用既有译文。该介绍页给出“典型约 50 美元、通常 4–5 个工作日”的估值；较新的 Play 帮助页则写“每词低至 0.07 美元、通常 7 天内完成”。两者是不同口径，不能视为固定报价或 SLA；订单前应看 Console 对目标语言和字数的实时报价/交付日期。
- [自定义商店详情页](https://support.google.com/googleplay/android-developer/answer/9867158)可按国家/地区、关键词、广告流量、预注册、流失/未购买用户和自定义受众展示不同素材；最多 50 个。自定义详情页不会自动翻译，联系方式、隐私政策和类别仍在各变体间共用；每个版本依然须遵守元数据规则。具体条件及孙链接见[商店详情专题](../store-listing-best-practices/store-listing-best-practices.zh-CN.md)。
- [Android Localize your app](https://developer.android.com/guide/topics/resources/localization)是工程指南，不是 Play 审核条款。本轮抽读了默认资源回退、`res/values/strings.xml`、本地化资源文件、给译者提供上下文和用 XLIFF 标记占位符等部分；缺少完整默认资源可能使未覆盖语言下的应用无法启动。大型指南的所有 API/示例后代仍未遍历。
- [View and analyze ratings and reviews](https://support.google.com/googleplay/android-developer/answer/138230?hl=en)的直接后代还包括用户如何评价/编辑评论、Console 中的评分和评论工作区、测试反馈、发布政策、举报违规评论及月度报告。消费者页面只说明用户评论流程；[举报不当评价](https://support.google.com/googleplay/android-developer/answer/7318385)要求仅举报违反 Comment Posting Policy 的内容，是否移除由专员审核；[月度报告](https://support.google.com/googleplay/android-developer/answer/6135870)提供评分/评价等报告，但 Cloud Storage 报告与具体应用数据受账号权限控制。
- [自定义同类群组比较](https://support.google.com/googleplay/android-developer/answer/9842755?hl=zh-CN)可分别建立一个评分群组和一个 Android vitals 群组；Vitals 群组每月最多编辑 3 次、需选 8–12 个应用。不可用的同类应用会被系统推荐项替代。退出 Vitals 同类比较不会移除该应用进入总体类别评分比较的数据。这是分析口径说明，不是评分政策或排名公式。测试轨道反馈另见[测试轨道帮助](https://support.google.com/googleplay/android-developer/answer/9845334?hl=zh-CN)：测试用户反馈不进入公开评分。
- 消费者版[抢先体验和测试版说明](https://support.google.com/googleplay/answer/7003180?hl=zh-CN)补充了反馈可见性：测试者对 Early Access/Beta 应用的私密反馈仅开发者可见，且必须同时评分并填写评论才可提交；这与开发者侧“测试反馈不计入公开评分”相互印证，但消费者页面不是新开发者义务。其[退出测试版帮助](https://support.google.com/googleplay/answer/15654751?hl=zh-CN)说离开测试并卸载时可能丢失进度/自定义内容，名额开放后不保证可重新加入；改用公开版要卸载测试版并安装公开版。对应的[卸载](https://support.google.com/googleplay/answer/13627402?hl=zh-CN)和[重新安装/启用应用](https://support.google.com/googleplay/answer/113410?hl=zh-CN)页是消费者操作指引，不是商店审核要求。
- 测试版说明也链接到消费者版[Data safety 介绍](https://support.google.com/googleplay/answer/11416267?hl=zh-CN)：面向用户解释开发者公开呈现的收集/分享、安全做法和删除信息；该页面说权限清单与 Data safety 声明来源不同，因而可能不一致。它与本地[Data safety 政策专题](../data-safety/data-safety.zh-CN.md)互补：前者讲消费者如何读详情，后者讲开发者申报规则。Data safety 页的全部类型词条与 40 余个相关资源后代仍未在本分支逐一展开。
- [账号用户与权限](https://support.google.com/googleplay/android-developer/answer/9844686?hl=zh-CN)把“Reply to reviews”列为单独权限：有权限者可回复并更改建议回复所用联系信息；没有该权限仍可查看评分/评论，但不能回复。权限可按账号或应用分配；邀请时可设到期日，不设则持续有效。此为 Console 访问控制，不改变评论政策。
- [Reply to Reviews API](https://developers.google.com/android-publisher/reply-to-reviews)仅访问正式版中带文字评论的近期反馈（只可取最近 7 天内新建或修改的评论）；测试版反馈须在 Console 查看。公开 API 回复上限为 350 字符，回复会公开显示，不能放入用户敏感信息；Google 不建议先用自动回复、之后再人工替换。按应用限额为 GET 每小时 200 次、POST 每天 2,000 次。使用 OAuth 或服务账号；服务账号需启用 Reply to reviews 权限。API 不取代 Console 中的完整历史评论 CSV。
- API 的[Getting Started](https://developers.google.com/android-publisher/getting_started)指南要求在 Google Cloud 建项目并启用 Developer API，再用服务账号或 OAuth 配置访问；当前说明已不要求先把 Play 开发者账号关联到 Cloud 项目。账号/应用权限仍由 Play Console 控制，服务账号密钥须保存在安全的服务器环境。其账号内入口仍须登录。
- 评分指南引用的旧 Android “Reviews” 页面已跳到 [Google Play Reviews 商务介绍页](https://google.play/business/reviews/)。该营销页建议及时回复、报告违规评价、按设备筛选和导出分析；其宣传性指标不是政策承诺或任何应用的排名保证。`answer/138230` 的另一条“Google Play Business and Program Policies”链接本轮观察到它跳到 Google Play 用户《服务条款》页面；评论发布规则仍以本地政策专题所链接的现行开发者政策目标为准。

**本节范围：** `4448378` 正文可见 8 个外链位置，其中 5 个目标页已打开，1 个跳到登录页，社区/联系支持 2 个目标无法读取；SEO、素材、翻译和评分的高影响子页已逐页总结。素材、翻译和评分帮助正文的更深技术/API/Console 后代仍只按政策相关性抽查，未宣称无限递归闭合。逐 URL 状态见人工审计表（快照：`source-page-audit.csv`，未导入本仓库）和离线首页的 URL 审计。

### 用户支持帮助页的下游：退款、订单与订阅

用户支持说明继续链接到退款与订单资料。以下是这些下一层页面的政策关系；消费者帮助中心介绍买家如何申请退款，不能当成开发者必然须批准退款的承诺。

| 下游目标 | 页面摘要与关系 | 核验结果 |
| --- | --- | --- |
| [Google Play refund policies](https://support.google.com/googleplay/answer/2479637) → [Apps, games, and in-app purchases refunds](https://support.google.com/googleplay/answer/15574908) | 退款受商品、支付方式、购买时间及地区影响。消费者页面称多数购买不退款；部分购买可在 48 小时内提交申请，之后通常联系开发者，由开发者按其政策和适用法律处理。属于消费者流程，不是 Play 对所有订单的退款保证。 | 两页已打开；退款界面与地区/商品相关页面仍可能变化。 |
| [Refund timelines](https://support.google.com/googleplay/answer/15576193) | 退款获批后退回原支付方式；处理时间依支付方式而异。页面提供 EEA/英国支付方式的估算天数，并要求消费者通过 Google Pay/订单状态核查。 | 正文已打开；时限是估计值，不是开发者客服 SLA。 |
| [Manage orders and issue refunds 旧入口](https://support.google.com/googleplay/android-developer/answer/9859683) → [现行操作页](https://support.google.com/googleplay/android-developer/answer/2741495) | Play Console 订单管理可处理全额/部分退款和订阅取消；取消订阅**不会**单独退款。最近一次订阅扣款可退款并撤销权益/停止后续续订；对旧周期退款时订阅可继续有效。部分退款不适用于付费应用，只支持符合页面条件的 IAP/订阅订单。退款不可逆，可能影响后续结算。 | 旧地址重定向后现行正文已打开；订单搜索、权限、退款、取消和结算影响已摘要。Console 操作需账号权限。 |
| [Subscriptions policy 旧入口](https://play.google.com/about/monetization-ads/subscriptions/) → [现行 Subscriptions 政策](https://support.google.com/googleplay/android-developer/answer/9900533) | 订阅须清楚披露价格、周期、自动续订、是否为使用应用所必需等重要条款，并提供持续/重复价值；应用中须提供易用的在线取消路径。Play Billing 订阅取消一般在当前周期结束后生效，当前周期通常不退款；部分地区法律允许立即取消或比例退款。 | 旧入口已重定向到现行正文；详细购买/取消条款见[付款与订阅专题](../payments/payments-and-subscriptions.zh-CN.md)。 |
| [Service fees](https://support.google.com/googleplay/android-developer/answer/112622) | 订单退款也会影响结算和服务费；官方费率按地区、交易类型、安装群组和入组项目变化。帮助页当前描述 2026 年分地区 rollout，应以[付款与订阅专题](../payments/payments-and-subscriptions.zh-CN.md)及当期条款为准。 | 正文已打开并与付款专题交叉核对；不把静态费率表当作所有国家/账号的报价。 |
| Developer API subscription [`revoke`](https://developers.google.com/android-publisher/api-ref/purchases/subscriptions/revoke) 与 [`refund`](https://developers.google.com/android-publisher/api-ref/purchases/subscriptions/refund) | 订单帮助页为退款/撤销提供 API 链接，但这两个旧端点当前返回 404。 | 目标无法读取；不猜测旧方法替代品。退款 API 的现行资源见[付款与订阅专题](../payments/payments-and-subscriptions.zh-CN.md)。 |

## 发布前检查

1. 固定唯一 package name，并保存 bundle、上传密钥和版本号规划；在首次 rollout 前复核签名选择与服务端/第三方证书指纹。
2. 用当前 target API 门槛、AAB 大小、设备形态和测试要求校验构建；新个人账号先核实是否适用 12 人/14 天闭测门槛。
3. 确认 Listing 真实反映应用功能、受众、类别、标签、价格类型、语言版本和各设备素材；测试轨道与 Production 共用主详情，不能用未完成素材误导审核。
4. 填写有效支持邮箱，确保付费/内购支持能满足时限；审核需要登录的应用必须另行提供可用审核凭证，见[应用审核专题](../app-review-preparation/app-review-preparation.zh-CN.md)。
5. App content、政策/出口声明、DDA、Play App Signing Terms 是不同事项；分别核对，不把一个复选框当作其他事项的替代。

## 覆盖边界

主帮助页正文已完整打开。其可访问的直接目标已在上表按内容与关系整理；Play Console 应用路由要求登录，“creating a compelling store listing”链接点击返回 Internal Error，课程正文需登录。其他子页面的更深层链接只在相关专题和来源台账中按高影响分支递归，未宣称无限深闭合。本专题为中英双语改写，不是 Google 官方原文全文。
