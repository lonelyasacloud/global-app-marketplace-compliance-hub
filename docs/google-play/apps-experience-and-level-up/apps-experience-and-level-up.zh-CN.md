---
id: google-play.apps-experience-and-level-up
platform: google-play
language: zh-CN
authority: operational
status: current
kb_checked_at: 2026-10-23
review_due: 2027-01-23
regions: [global]
topics: [apps-experience, level-up, voluntary-program, rate-card, app-quality, form-factors]
snapshot_id: play.apps-experience-level-up
snapshot_package: "GooglePlay-KnowledgeBase-2026-10-24-review.zip"
coverage_status: "detailed-summary"
source_url_enrollment: "https://support.google.com/googleplay/android-developer/answer/18018581?hl=en"
source_url_aep_overview: "https://developer.android.com/distribute/aep/aep-guidelines-overview"
source_url_aep_planner: "https://developer.android.com/distribute/aep/aep-integration-planner"
source_url_aep_program: "https://google.play/business/programs/appsexperience/"
source_url_level_up_program: "https://google.play/business/levelup/"
source_url_level_up_guidelines: "https://developer.android.com/games/guidelines"
source_url_aep_form_factor: "https://developer.android.com/distribute/aep/aep-req-form-factor-support"
source_url_aep_stability: "https://developer.android.com/distribute/aep/aep-req-stability"
source_url_aep_android_mcp: "https://developer.android.com/distribute/aep/aep-req-android-mcp"
source_url_credential_manager: "https://developer.android.com/identity/credential-manager"
source_url_sign_in_google: "https://developer.android.com/identity/sign-in/credential-manager-siwg"
source_url_legacy_sign_in_migration: "https://developer.android.com/identity/sign-in/legacy-gsi-migration"
source_url_restore_credentials: "https://developer.android.com/identity/sign-in/restore-credentials"
source_url_block_store: "https://developer.android.com/identity/block-store"
source_url_engage_sdk_guide: "https://developer.android.com/guide/playcore/engage"
source_url_premium_growth_tools: "https://google.play/business/guides/premium-growth-tools/"
source_url_youtube_play_videos: "https://support.google.com/googleplay/android-developer/answer/15501235"
source_url_promotional_content: "https://support.google.com/googleplay/android-developer/topic/12932623"
effective_date: "voluntary program dates include 2026-09-30, 2027-03-01, February 2027, and 2027-09-30; none of these is the 2027-01-27 permissions preview"
---

# Apps Experience 与 revamped Level Up 自愿计划

> **导入说明（Google batch 8）。** 正文来自已经分开的 2026-10-24 Google Play 知识库快照（`play.apps-experience-level-up`，核对日 2026-10-23）的改写摘要，不是官方页面的逐字副本。英文官方页面是效力来源。`kb_checked_at` 是快照源文件记录的核对日；本次导入没有重新打开线上官方页面。文中“本知识库”“本库”“本地专题”等说法描述的是该快照库的覆盖范围，不是本仓库已经导入的页面。指向本仓库没有收录的专题、链接图、台账或 CSV 的相对链接改为文字提及。指向 Google batch 1–7 或本批十三个专题的相对链接改为本仓库文件。核对日 2026-10-23。两种语言文件引用的入组文章都是英文 `hl=en`。快照没有记录已核对的中文官方入组页，也没有记录 `hl=zh-CN` 抓取失败。中文是编辑改写。入组文章那一轮有 3 个帮助、社区或支持目标返回内部错误，没有推断登录后的内容。与 2027-01-27 权限预告分开的计划日期包括：2026-09-30；Apps Experience 形态支持中的 Googlebook 为 2027-03-01；动态内存预计 2027 年 2 月执行；Android MCP 执法延后至 2027-03-01 或自助注册开放后三个月；Level Up 奖励自 2027-03-01 起；Level Up 的 XR、TV、Googlebook 和 Auto 分发自 2027-09-30 起。旧的 2027-03-01 Googlebook 日期不沿用到当前 Level Up 设备分发行。这是自愿计划，不替代开发者计划政策或付款政策。项目费率不是基础 Play 政策。证据等级：Operational。

**核对日期：2026-10-23。** 本专题汇总 Android Apps Experience Program（AEP）与 revamped Google Play Games Level Up。两者是可自愿申请的专项计划，符合条件并经 Google 审核后可获得项目费率；它们不是所有 Google Play 开发者的基础政策，也不取代 Developer Program Policy、付款政策、当地法律或 Play Console 审核。

## 1. 先分清计划与基础政策

| 项目 | 面向对象 | 主要目标 | 状态边界 |
| --- | --- | --- | --- |
| Apps Experience Program（AEP） | 应用 | 跨 Android 设备形态提供一致、丰富、稳定的体验 | 需要满足适用于该应用的 AEP 指南并通过逐应用审核 |
| revamped Level Up | 游戏 | 游戏体验、跨屏可用性、玩家互动和稳定性 | 需要满足适用于该游戏的 Level Up 指南并通过逐游戏审核 |
| Google Play 基础政策 | 所有适用的应用/开发者 | 内容、数据、权限、付款、安全、商店资料、执行处置等 | 无须参加上述计划；仍须持续遵守 |

参加 AEP 或 Level Up **不会提升商店排名**；公布的福利是合格交易适用的费率卡。高质量体验可能有一般产品价值，但不能把计划资格等同于搜索排名承诺。指南和福利可能更新；以申请时的 Play Console 条款、适用说明及审查结果为准。

## 2. 申请资格、审查和持续资格

官方入组帮助页目前列出的流程要点：

1. **开放时间与账号门槛：** Play Console 自 2026-09-01 开放申请；目前仅向过去 12 个月开发者账号组收入至少 100 万美元的账号组开放。申请人需有 Admin 或 account owner 权限。
2. **应用/游戏门槛：** 必须已在 Google Play 正式版发布，并至少连续 6 个月保持良好状态（包括遵守适用 Play 政策）；计划资格是逐应用或逐游戏审批，不是账号整体获准。
3. **准备材料：** 提供可让审核人员登录并访问全部功能的凭证；先对照适用的项目指南；如有资格例外，在正式申请前递交豁免申请。
4. **审查和费率生效：** 仅在 Google 核实满足所有适用指南后才获准项目费率。审查通常最长 14 天，特殊情况可能更久；费率卡从合格市场的项目开放日或完成入组后 24 小时起（取较晚者），并以 Google 验证/批准为条件。
5. **拒绝与复核：** 先修复所有问题，再提交“已修复”“申诉”或“部分修复并申诉”的复核请求；申诉权限也须满足 Console 的相应角色要求。
6. **维持资格：** 获准后仍须满足项目指南并保持 Play 政策良好状态。Console 警告会给出整改期限；逾期未复核可被移出计划并失去项目费率。恢复良好状态后通常还需等待 6 个月才能重新取得项目费率资格。

申请规划器只根据问卷生成**初步**适用指南/豁免建议，并非 Google 最终裁定。应以指南原文、Console 中针对该应用的要求和审核结果为准。

## 3. 项目费率和地区开放时间

下表为截至核对日官方公开费率卡的摘要。金额按交易发生地、交易类别、新/既有安装、年度收入档以及项目核准状态判断；Billing 费用（如适用）另计。不要用开发者注册地址代替买方所在地，也不要把项目费率推广成全球、自动适用的收费标准。

| 收入/资格档 | 自动续订订阅 | 其他交易：新安装 | 其他交易：既有安装 | 外部网页链接交易 |
| --- | ---: | ---: | ---: | ---: |
| 年度收入首 100 万美元 | 10% | 10% | 10% | 依适用项目条款核对 |
| 标准档（年度收入超过 100 万美元） | 10% | 20% | 25% | 20% |
| AEP 或 Level Up 项目合格费率 | 10% | 15% | 20% | 15% |

项目费率对买方所在地区分阶段开放：

| 地区 | 官方公布的开放日期 |
| --- | --- |
| 美国、英国、日本、欧洲经济区、澳大利亚 | 2026-09-30 |
| 韩国 | 2026-12-31 |
| 其他地区 | 2027-09-30 |

自愿申请与收入档、Play Billing 适用性、税费、外部链接项目之间的关系仍须分别判断。Play Console 月度收入报告及订单信息是核对实际费率的操作入口。

## 4. Apps Experience Program：26 项指南按三类查看

AEP 总览将指南分为一致/丰富体验、设备形态覆盖、稳定/现代体验三类。**不是每条指南都适用于每个应用**；适用性取决于核心用例、是否要求登录、是否提供可比较的跨平台体验以及所支持的设备形态。26 个直接指南目标均已点击并登记；下表依总览描述概括，关键目标已另行核对正文。每个条目都链接到 Google 官方指南页。

### 一致且丰富的用户体验

| 指南 | 实施重点与适用边界 |
| --- | --- |
| [Phishing Resistant Authentication](https://developer.android.com/distribute/aep/aep-req-phishing-resistant-auth) | 需要登录的应用提供 passkey 或受认可的 SSO，登录入口应同等明显；passkey/Sign in with Google 按 Credential Manager 接入。适用于手机、平板、折叠屏、XR、Wear 和 Auto；无登录态应用不适用。受认可 SSO 清单会变化。 |
| [Restore Credentials](https://developer.android.com/distribute/aep/aep-req-restore-credentials) | 对支持登录的手机、平板、折叠屏应用实现 Restore Credentials API，使换机/恢复时能找回登录状态。无账号、高安全/监管限制、2026-09-30 前已用 Block Store 恢复登录的应用有列明豁免。 |
| [Engage SDK](https://developer.android.com/distribute/aep/aep-req-engage-sdk) | 对合格的媒体、社交、健康、旅行、购物、餐饮、图书/漫画、教育等手机/平板应用，在 Google surfaces 提供个性化推荐与继续观看/使用内容；继续内容在用户操作后 10 分钟内更新，推荐至少每 3 天刷新，登出/删号时删除外显内容。没有登录、原生推荐或继续体验的应用可按指南申请对应豁免。 |
| [Play Content](https://developer.android.com/distribute/aep/aep-req-play-content) | 手机、平板、折叠屏和桌面应用需满足一种内容发现路径：允许 Play 访问既有内容 feed，或每季度提交至少 2 项通过质量审核的 Promo Content、Play Shorts 等内容。工具/实用程序、聊天/通信/直播等类型可能不适用。 |
| [Title Availability](https://developer.android.com/distribute/aep/aep-req-new-title-availability) | 新产品需与可比较的非 Android 平台同步在适用 Android 形态上线；未同步可能导致 6 个月等待期。硬件/技术不适配、上线宽限和 EEA 情况有单独规则。 |
| [Feature Availability](https://developer.android.com/distribute/aep/aep-req-feature-availability) | 同一国家/地区内，非 Android 平台完整发布的功能应在 3 周内于 Android 完整推出，并保持核心功能等价；技术不可行或经认可的生产故障可申请豁免。 |
| [Material UX](https://developer.android.com/distribute/aep/aep-req-material-ux) | 对在非 Android 平台提供可比较设计系统的应用，使用 Compose Material 3；Wear OS 使用 Wear Compose Material 3。该指南列明无豁免。 |
| [System Emoji](https://developer.android.com/distribute/aep/aep-req-system-emojis) | 对会渲染用户表情符号的应用，确保输入框、评论、消息、反应和图像文本中的 Emoji 与系统键盘/系统界面一致；可放大的表情使用相应界面可用的高分辨率字体。 |
| [Dark Theme Support](https://developer.android.com/distribute/aep/aep-req-dark-theme) | 对有可比较跨平台深色体验的应用，所有页面、浮层和系统组件支持系统深色偏好；文字/图标对比度至少 4.5:1，并响应系统 uiMode 变化。 |
| [Themed App Icons](https://developer.android.com/distribute/aep/aep-req-theme-app-icons) | 为支持主题图标的 Android 系统提供自适应、可随用户主题着色的应用图标；详见目标指南的资源和豁免条件。 |
| [Physics Based Motion](https://developer.android.com/distribute/aep/aep-req-physics-based-motion) | 对有可比较跨平台动效的应用，核心导航/状态变化不能是 0 毫秒突变；用可中断、保持上下文的过渡表现手势动量。 |
| [Share Sheet](https://developer.android.com/distribute/aep/aep-req-share-sheet) | 对有可比较外部分享功能的应用，外部分享使用 Android Sharesheet/system chooser；应用内转发不属于此要求的外部分享。 |

### 覆盖 Android 设备形态

| 指南 | 实施重点与适用边界 |
| --- | --- |
| [Form Factor Support](https://developer.android.com/distribute/aep/aep-req-form-factor-support) | 所有应用须达到 Adaptive App Tier 2：入组时支持手机、平板、折叠屏和 XR；**2027-03-01 前支持 Googlebook**。TV、Wear、Auto 根据应用用例增加相应质量要求；质量规范更新后通常有 12 个月迁移宽限。适用豁免有硬件/技术约束、无逻辑用例和地区设备不可用等情况；该要求本身不等于必须通过 Play 在这些设备分发。 |

### 稳定、现代和按用例适用的体验

| 指南 | 实施重点与适用边界 |
| --- | --- |
| [Stability](https://developer.android.com/distribute/aep/aep-req-stability) | AEP 专项阈值：参考设备平均 crash <1%、4GB+ 设备 <2%；ANR 分别 <2%/<3%；参考设备 Excessive Slow Frames <2%。按滚动 28 天、经批准的设备集合且至少 1,500 个会话计算。此值不同于影响 Play 商店展示的一般 bad-behaviour threshold。动态内存门槛预计自 2027 年 2 月执行，需查看实时技术质量页面。 |
| [Quality — Jetpack Compose](https://developer.android.com/distribute/aep/aep-req-jetpack-compose) | 现代、可扩展的高质量 UI 实现指南；按该指南判断 Compose 与等效方案的接受标准。 |
| [Predictive Back](https://developer.android.com/distribute/aep/aep-req-predictive-background) | 使用 Android 预测性返回能力，为返回动作提供目的地预览并避免误退出。 |
| [Edge to Edge](https://developer.android.com/distribute/aep/aep-req-edge-to-edge) | 采用现代 edge-to-edge 窗口行为，充分使用屏幕空间并正确处理系统栏/安全区域。 |
| [Android MCP](https://developer.android.com/distribute/aep/aep-req-android-mcp) | 对指南列出的通信、笔记、日历、任务、健康、购物、旅行、创作、媒体和系统工具用例，使用 AppFunctions 暴露至少一个相关能力并通过集成测试。Early Access 期间目前可选；执法延后至 **2027-03-01 或 Android MCP 自助注册开放后三个月，两者取较晚**，参与者将提前收到通知。 |
| [Media3](https://developer.android.com/distribute/aep/aep-req-media-3) | 对相关媒体播放用例核对 Media3 播放与会话指南。 |
| [CameraX](https://developer.android.com/distribute/aep/aep-req-camera-x) | 对相机中心用例核对 CameraX 的跨设备捕获指南。 |
| [Cast Support](https://developer.android.com/distribute/aep/aep-req-cast-support) | 对投放/大屏体验核对 Cast 支持指南。 |
| [Photo Picker](https://developer.android.com/distribute/aep/aep-req-photo-picker) | 对照片/视频选择用例核对系统 Photo Picker 与媒体最小访问方案。 |
| [Preload Caching](https://developer.android.com/distribute/aep/aep-req-preload-caching) | 对滚动媒体 feed 核对预加载/缓存要求，重点是降低播放启动延迟。 |
| [Night Mode](https://developer.android.com/distribute/aep/aep-req-night-mode) | 对夜景静态摄影用例核对硬件加速低照度拍摄指南。 |
| [Android Telecom Framework](https://developer.android.com/distribute/aep/aep-req-telecom-api) | 对 VoIP 通话用例核对 Telecom Framework 注册和系统集成要求。 |
| [Picture in Picture Support (PiP)](https://developer.android.com/distribute/aep/aep-req-picture-in-picture) | 对视频播放、通话或导航等适用体验核对 PiP 指南。 |

上述 8 项按功能/垂类适用；Android Developers 表示兼容的等效框架可以申请评估，但须达到相近质量、能力、稳定性与生态兼容性。不要把技术指南作为 Google Play 基础政策的替代依据。

## 5. Revamped Level Up：游戏体验要求

Level Up 页面把游戏要求分成三组；项目费率要求游戏满足全部适用的新版指南。当前页面已更新，不能把旧版的 2027-03-01 Googlebook 节点沿用到整个 Level Up 的设备分发项。

| 主题 | 主要检查项 | 例外/期限提示 |
| --- | --- | --- |
| 一致的玩家体验 | 启动时集成 Play Games Services v2；按指南启用 Sidekick；生命周期内至少 10 项成就，且为 Quests 至少 4 项可在首小时内合理达成；接入 Game Stats、Rewards 和云存档/进度冲突处理。Play Games Services (PGS) v2 平台身份不要求使用 Google 身份，也不要求游戏自建账号。 | 主要面向 13 岁及以上的游戏；以 13 岁以下儿童为主要受众的游戏可豁免此组多项要求。已付费游戏及其他用例亦有各指南明确的奖励/云存档豁免。 |
| 跨屏覆盖 | 支持大屏重排/窗口变化和精确输入；满足 Google Play Games on PC、表单因子分发、标题可用性等条目。 | 2026-09-30 起手机、折叠屏、平板；当前页面列出 XR、TV、Googlebook、Auto 自 2027-09-30 起。无需因此强制在 Play Store 对所有设备分发；位置/传感器依赖、硬件不足、地区设备不可用及知识产权许可等可能有豁免。 |
| 稳定、流畅游戏 | 按指南核对 stability、performance、memory、Vulkan/图形 API 和参考设备测试。 | 参考机型和例外会变；按当前指南、游戏引擎、设备能力与申请状态逐项处理。 |

时间点：Reward 指南要求至少 2 项一次性 Play Games Reward，自 2026-09-30 起；自 **2027-03-01** 起还需至少 1 项可重复奖励，供社交挑战完成后发放，每位玩家每周最多 1 次。主要面向 13 岁以下儿童的游戏和付费游戏有列明豁免。游戏形态分发的后续日期目前为 **2027-09-30**，见上表。标题/功能未同步发布可能触发 6 个月的项目费率等待期；符合条件的旧发布时间或经批准例外可能改变结果。

## 6. 实用核对顺序

1. 先判断是否要参加 AEP 或 Level Up；若不参加，仍按基础 Play 政策发布。
2. 建立用例清单：登录、内容/推荐、媒体/相机/通讯、跨平台发布、目标设备形态、儿童主要受众、商业模式。
3. 用 [AEP 指南规划器](https://developer.android.com/distribute/aep/aep-integration-planner)作初筛，再逐条打开本专题列出的官方指南核实适用条件、豁免、迁移期限和测试标准。
4. 对项目申请准备正式版、连续 6 个月良好状态、审查登录凭证、逐指南证据和豁免材料；用分项验收表保存通过证据。
5. 审核通过后按买方地区、交易种类、安装状态、收入档以及月度订单报告核对费率；用 Console 警告跟踪维持资格。

## 7. 2026-10-13 官方产品更新：发现、深链与游戏互动

[Android Developers 博客](https://android-developers.googleblog.com/2026/10/new-tools-for-discovery-and-engagement.html)发布了一份面向开发者的产品更新清单，介绍 Ask Play 应用比较、Game Finder、Gemini/Play 内容发现、Sprints、Playbacks、Quests 及质量计划。它是产品/工具更新，不是新的 Developer Program Policy 公告；下表保留正文直接链接的目标及其与本专题的关系。

| 博客正文直链 | 目标页内容与关系 | 边界 |
| --- | --- | --- |
| [“More than a store” 产品更新](https://blog.google/products-and-platforms/platforms/google-play/google-play-updates-october-2026/) | 介绍 Ask Play、Game Finder、跨设备发现、48 小时 Sprints 和个人 AI 应用。个人应用先限本人设备/特定市场及 18 岁以上用户；若公开面向全球发布，仍需专业开发者账号，并经过相同 Trust & Safety 审查和质量标准。 | 这是产品范围说明，不构成对公开上架的审核豁免。产品可用地区/日期应以当前实际发布说明为准。 |
| [I/O 2026 Google Play 更新](https://android-developers.googleblog.com/2026/05/io-2026-whats-new-in-google-play.html) | 回顾 Gemini 发现、Engage SDK、Play Shorts、Sidekick、Play Console AI/经营分析功能以及订阅恢复工具，是 10 月产品更新的前情背景。 | 博文描述路线图、能力和示例效果，不取代支付、订阅、数据或用户体验政策。该文其余产品链接属于独立分支，未在本节穷尽。 |
| [Verify and maintain deep links](https://support.google.com/googleplay/android-developer/answer/12463044) | Play Console Deep links 页面可查看网站 URL 与应用版本映射、检查 intent filters、预览并修复深链；Play Console 可对设置创建补丁，但补丁不会进入未来应用版本，需回到 Manifest/正式版本验证。 | 本轮直接打开了正文目标和 Android App Links 子页。其[Deep links Console 路由](https://play.google.com/console/developers/app/deeplinks)跳至 Google 登录，不能读取账号数据；[Google Ads 链接](https://ads.google.com/)跳转到 Ads 商业首页。Ads 数据仅在关联账号后可见。文章的 15 项通用侧栏并未逐项穷尽。 |
| [Engage SDK 计划页](https://google.play/business/programs/EngageSDK/) | 介绍 Apps Home、You tab、商店列表、Collections、平板和 Google TV 等分发面；9 个内容类别须满足资格，并通过申请加入开发者预览。推荐继续旅程、及时个性化推荐和精选内容簇；FAQ 指向资格、意向表单和各垂类集成指南。 | “接入 SDK”是发现/互动方案，不是所有应用的普遍义务或排序保证；AEP 条件、预览资格和技术集成应分开核验。 |
| [Game Stats 指南锚点](https://developer.android.com/games/guidelines) 与 [Play Games Rewards 指南锚点](https://developer.android.com/games/guidelines) | 两条博客链接都落在新版 Level Up 指南的不同章节。它们关联的是自愿参加 Level Up 的游戏资格标准，而非每款 Play 游戏的普遍政策要求；具体标准、例外和实现见下节。 | 链接目标相同，图谱按章节关系区分，不把锚点计成两个 URL。 |
| [Apps Experience Program](https://google.play/business/programs/appsexperience/) 与 [Level Up 项目介绍](https://google.play/business/levelup/) | 两个计划通过费率卡奖励满足项目条件的应用/游戏。项目介绍页说明各自适用地区、申报及资格；Level Up 指南提供实际体验标准。 | 入组自愿；不得把项目费率条件写成全体开发者的政策门槛，也不得把产品宣传中的增长案例视作效果保证。 |
| [Play Console 首页和导航更新](https://support.google.com/googleplay/android-developer/answer/18742903) | 说明新版首页过滤器、应用切换和账号级页面位置，帮助开发者找到发布/政策待办和管理入口。 | 是 Console 界面导航说明，不新增政策要求；账号内显示内容可能因权限不同。 |

博客建议开发者更新商店详情、标签和推广活动；上传适配多屏的高分辨率素材；用 Play Console 深链模拟器预览/测试链接；在符合资格时集成 Engage SDK。对游戏，博客介绍 48 小时、匹配 2–5 名相近水平玩家的 Sprints，以及通过 Game Stats 和 Play Games Rewards 提供挑战/奖励的路径。以上是产品最佳实践和工具建议，应与正式政策、项目条件及账号审核分开标注。

## 8. Game Stats 与 Play Games Rewards：Level Up 子链和实现核对

### Game Stats

新版 [Level Up 指南](https://developer.android.com/games/guidelines)要求入组游戏提供至少 5 项代表常见核心玩法的重复统计，其中至少 1 项可用于竞技互动；若有主要进度机制，还需提供至少 1 项进度统计。主要面向 13 岁以下儿童的游戏不启用相关功能；没有明确进度机制、或符合原生 PC Early Access 例外的游戏按指南分别评估。

[Game Stats 正式指南](https://developer.android.com/games/pgs/gamestats)把统计显示在玩家 Gamer profile，并要求统计不依赖购买或看广告、不只是打开/设置等一般使用、不含个人/敏感数据或攻击性/色情/暴力/仇恨内容，且对所有玩家可用；每款游戏最多配置 50 项。重复统计应发送每次事件的离散值，再按 `SUM`/`COUNT` 聚合；`MAX` 只用于单次峰值。不能发送已累计的终身总数并用 `MAX` 伪装峰值，否则虽可能显示在资料页，却无法用于 Leagues、Quests、Sprints 等互动机制。

### Play Games Rewards

Level Up 指南当前要求：自 **2026-09-30** 起至少提供 2 个一次性奖励；自 **2027-03-01** 起至少有 1 个可重复奖励，每位玩家每周最多 1 次。奖励须对发布地区的所有玩家可用且有实际价值。主要面向 13 岁以下儿童的游戏及付费游戏有明确豁免；应按游戏是否属于例外判断，不把日期条件扩大为所有游戏的 Play 基础政策。

[Rewards 实现指南](https://developer.android.com/games/rewards)进一步要求在 Play Console 选择/创建 SKU，并用 Play Billing Library 的站外购买领取流程发放 Play 提供的奖励。**这不要求开发者改用 Play Billing 处理自己的付费交易**；即使采用替代计费，也仍须按指南把 SKU 和 Play Billing Library 接入奖励发放流程。游戏在启动/回到前台时应检查未确认奖励、及时验证并发放；玩家需在 3 天内领取。若支持多个游戏内身份，必须让玩家选择发给哪个身份，且 PGS ID 与 Play Billing 账号须匹配。

### 上线前实现顺序与不可逆项

| 资源 | 本轮已核对内容 | 实际核对建议 |
| --- | --- | --- |
| [Integrate Game Stats](https://developer.android.com/games/pgs/integrate-gamestats) | Play Console 事件/统计配置、CSV/ZIP 导入、内部测试、日志、发布流程；事件名、统计 ID、进度方向、单位和关联事件等字段有不可编辑限制。已发布的统计不能删除；测试态事件/统计可删除。 | 先定义事件和计算/显示口径，核对隐私和 50 项上限；在发布前使用内部测试、查看事件校验日志。发布前评审 schema，因为统计发布后不可删除。 |
| [Android Game Stats API 指南](https://developer.android.com/games/pgs/android/gamestats) | 说明客户端/服务器事件上报路径、事件字段和进度更新；大型实现页面中还列出 PGS API 约束和样例。 | 这里只覆盖主要模型与接口方向，未穷尽每种 SDK、API 字段和游戏引擎示例。敏感/个人数据禁止项仍按 Play User Data 规则核对。 |
| [Rewards / Play Billing 集成指南](https://developer.android.com/google/play/billing/integrate) | Rewards 页面把验单、授予 entitlement、通知用户和确认处理连接到 Play Billing Library 的站外购买流程；开发者还要处理购买状态和重复发放保护。 | 这是奖励发放集成，不等同于替代计费项目的付款路径；Console SKU 配置与游戏身份映射需分开验证。 |
| [内部测试轨道](https://support.google.com/googleplay/android-developer/answer/9845334) | 在正式发布前向有限测试者验证事件、统计可见性和 PGS 登录状态。 | Play Console/测试账号具有账号权限要求；测试记录不等于正式审核或资格批准。 |

Game Stats 指南仍保留一句“UI 将于 2026 年 9 月开放”的未来式说明，而页面标注最近更新时间为 2026-10-22，日期已过。本轮不据此断言 UI 已上线或未上线；实际可见性需在当前 Console/玩家端核实。Google 在公告中引用的安装/消费提升是特定合作案例与统计窗口，不保证因集成即产生同样因果效果。

## 9. 已核对的部分孙级实施资源

这些页面是 AEP 总览指南的孙级链接，补充说明部分项目标准如何落到 Android 实现或 Play Console 操作。

| 父指南 | 子页面 | 对项目要求的补充 |
| --- | --- | --- |
| Phishing Resistant Authentication | [Credential Manager](https://developer.android.com/identity/credential-manager)、[Sign in with Google](https://developer.android.com/identity/sign-in/credential-manager-siwg)、[从旧版 Google Sign-In 迁移](https://developer.android.com/identity/sign-in/legacy-gsi-migration) | Credential Manager 是 Android 推荐的统一 API，支持 passkey、密码和联邦登录。Google 登录迁移把身份验证与后续授权拆分；不改变 AEP 对抗钓鱼登录方式的要求。 |
| Restore Credentials | [Restore Credentials 指南](https://developer.android.com/identity/sign-in/restore-credentials)、[Block Store](https://developer.android.com/identity/block-store) | 登录后生成 restore key，可通过云备份或设备到设备传输恢复；云恢复依赖 Google 账号、Android 备份和设备锁定设置。Block Store 保存会话数据/令牌，是旧方案；Android 当前指南建议优先考虑 passkey 与 Credential Manager。 |
| Engage SDK | [Engage SDK 指南](https://developer.android.com/guide/playcore/engage) | 在 Google surfaces 提供个性化推荐与继续体验，并按垂类提供集成指南。该指南还指向资格、覆盖和意向表单；仍需单独核对计划/Console 资格。 |
| Play Content | [Premium growth tools](https://google.play/business/guides/premium-growth-tools/)、[Google Play 上的 YouTube 视频](https://support.google.com/googleplay/android-developer/answer/15501235)、[推广内容目录](https://support.google.com/googleplay/android-developer/topic/12932623) | Premium growth tools 除账号良好状态外还有指标与类别门槛。公开基准示例包括连续三个月 160 万日活及活跃安装，或达到月度消费额门槛；顶级合作方和约会应用另有档位。YouTube 提交内容应由应用/游戏拥有、公开、可嵌入、无广告变现、非直播、版权清晰且符合目标展示位的新鲜度要求。推广内容涵盖活动和应用内精选商品，另有内容质量与提交审核流程。 |

上列 7 个目标已打开并概括。它们自身的代码示例、垂类集成页、表单和质量资源尚未全部递归核验；剩余分支边界见链接图 §4.93。


## 10. 来源与后代链接覆盖

| 来源 | 在本专题中的作用 | 已核对/未闭合边界 |
| --- | --- | --- |
| [入组和维持帮助页](https://support.google.com/googleplay/android-developer/answer/18018581?hl=en) | 资格、入组、豁免、审查、申诉、维持状态、费率起算和财务报告 | 正文链接共 19 次，归一化约 16 个目标；可读目标已展开。3 个帮助/社区/支持入口在该轮抓取返回内部错误，未推断其登录后内容。 |
| [AEP 指南总览](https://developer.android.com/distribute/aep/aep-guidelines-overview) | 26 个 AEP 直接指南的分类与适用概览 | 26 个目标均已点击并登记；主要资格/阈值页已读正文。技术指南各自的更深代码/API/最佳实践链接尚未逐个闭合，见递归链接图 §4.93（快照：`../google-play-policy-link-graph.md`，未导入本仓库）。 |
| [AEP Guidelines Planner](https://developer.android.com/distribute/aep/aep-integration-planner) | 用例问卷和初步豁免识别 | 明确非正式/最终裁定；最终适用范围仍由官方指南和 Play 审核决定。 |
| [AEP 项目介绍与费率卡](https://google.play/business/programs/appsexperience/) | 区域费率表、可用地区和排名说明 | 项目营销/介绍页；资格仍以 Console 申请和官方指南为准。 |
| [Level Up 项目介绍](https://google.play/business/levelup/) 与[新版指南](https://developer.android.com/games/guidelines) | 游戏费率、三组指南、日期和例外 | 指南正文含大量同页锚点与技术后代；本专题覆盖项目条款的关键分支，不声称递归抓取了所有 Android API、游戏引擎文档或参考机型页面。 |
| [2026-10-13 Android Developers 产品更新](https://android-developers.googleblog.com/2026/10/new-tools-for-discovery-and-engagement.html) | Ask Play、Game Finder、Engage、Sprints、Game Stats/Rewards 和 Console 视觉更新的产品公告入口 | 正文的全部外部页面链接已逐目标打开；其 Game Stats、Rewards 与 Engage 子链在本节/图 §4.98 作关系摘要。I/O 博客和 Google Blog 的更深产品链接、Engage 九类垂直集成页、全量 Game Stats SDK/API 成员及 Reward 后代仍未全部闭合。 |

本地页面是双语改写摘要，不是来源站全文镜像。来源更新、适用范围、豁免或账号专属审批有变时，必须重新访问官方页面和 Play Console。可从[付款/订阅](../payments/payments-and-subscriptions.zh-CN.md)、[应用质量/设备形态](../app-quality-and-form-factor-guidelines/app-quality-and-form-factor-guidelines.zh-CN.md)、期限总表（快照：`../google-play-policy-operations.md`，未导入本仓库）继续跳转。
