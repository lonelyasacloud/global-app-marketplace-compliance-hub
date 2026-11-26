---
id: google-play.app-quality-and-form-factor-guidelines
platform: google-play
language: zh-CN
authority: operational
status: current
kb_checked_at: 2026-10-24
review_due: 2027-01-24
regions: [global]
topics: [app-quality, form-factors, adaptive-apps, android-tv, wear-os, android-auto, automotive, android-xr]
snapshot_id: play.app-quality-form-factor
snapshot_package: "GooglePlay-KnowledgeBase-2026-10-24-review.zip"
coverage_status: "detailed-summary"
source_url: "https://support.google.com/googleplay/android-developer/answer/9877021?hl=zh-CN"
source_url_quality_index: "https://support.google.com/googleplay/android-developer/answer/9877021?hl=en"
source_url_discovery: "https://support.google.com/googleplay/android-developer/answer/9958766?hl=zh-CN"
source_url_android_vitals: "https://support.google.com/googleplay/android-developer/answer/9844486?hl=en"
source_url_vitals_reporting_api: "https://developers.google.com/play/developer/reporting"
source_url_vitals_anr_legacy: "https://developer.android.com/topic/performance/vitals/anr.html"
source_url_vitals_anr_current: "https://developer.android.com/topic/performance/issues/anr"
source_url_vitals_crashes: "https://developer.android.com/topic/performance/vitals/crash.html"
source_url_vitals_startup_legacy: "https://developer.android.com/topic/performance/launch-time.html"
source_url_vitals_startup_current: "https://developer.android.com/topic/performance/vitals/launch-time"
source_url_vitals_slow_sessions_legacy: "https://developer.android.com/topic/performance/vitals/slow-session"
source_url_vitals_slow_sessions_current: "https://developer.android.com/topic/performance/issues/slow-session"
source_url_vitals_ui_testing_legacy: "https://developer.android.com/training/testing/performance.html"
source_url_vitals_ui_testing_current: "https://developer.android.com/training/testing/fundamentals"
source_url_vitals_power_manager: "https://developer.android.com/reference/android/os/PowerManager.html"
source_url_vitals_alarm_manager: "https://developer.android.com/reference/android/app/AlarmManager.html"
source_url_vitals_diagnostics_optin: "https://support.google.com/accounts/answer/6078260"
source_url_vitals_surfaceflinger: "https://source.android.com/docs/core/graphics/surfaceflinger-windowmanager"
source_url_vitals_excessive_battery_legacy: "https://developer.android.com/topic/performance/vitals/excessive-battery-usage"
source_url_vitals_excessive_battery_current: "https://developer.android.com/topic/performance/issues/excessive-battery-usage"
source_url_ensuring_quality: "https://support.google.com/googleplay/android-developer/answer/13965279?hl=en"
source_url_android_quality_overview: "https://developer.android.com/quality"
source_url_quality_core_value: "https://developer.android.com/quality/core-value"
source_url_quality_user_experience: "https://developer.android.com/quality/user-experience"
source_url_quality_technical: "https://developer.android.com/quality/technical"
source_url_quality_privacy_security: "https://developer.android.com/quality/privacy-and-security"
source_url_core: "https://developer.android.com/docs/quality-guidelines/core-app-quality"
source_url_adaptive: "https://developer.android.com/docs/quality-guidelines/adaptive-app-quality"
source_url_wear: "https://developer.android.com/docs/quality-guidelines/wear-app-quality"
source_url_tv: "https://developer.android.com/docs/quality-guidelines/tv-app-quality"
source_url_car: "https://developer.android.com/docs/quality-guidelines/car-app-quality"
source_url_daydream: "https://developers.google.com/vr/distribute/daydream/app-quality"
source_url_en: "https://support.google.com/googleplay/android-developer/answer/9877021?hl=en"
source_url_discovery_en: "https://support.google.com/googleplay/android-developer/answer/9958766?hl=en"
effective_date: "quality guidance; linked 2027 contacts preview stays on the contacts topic; no 2027-01-27 quality effective date"
---

# Google Play 应用质量与设备形态指南

> **导入说明（Google batch 8）。** 正文来自已经分开的 2026-10-24 Google Play 知识库快照（`play.app-quality-form-factor`，核对日 2026-10-24）的改写摘要，不是官方页面的逐字副本。英文官方页面是效力来源。`kb_checked_at` 是快照源文件记录的核对日；本次导入没有重新打开线上官方页面。文中“本知识库”“本库”“本地专题”等说法描述的是该快照库的覆盖范围，不是本仓库已经导入的页面。指向本仓库没有收录的专题、链接图、台账或 CSV 的相对链接改为文字提及。指向 Google batch 1–7 或本批十三个专题的相对链接改为本仓库文件。YAML 核对日是 2026-10-24，开篇写 2026-10-22。这两个快照日期不表示政策变更。英文 App Discovery 正文已打开，其 `hl=zh-CN` 返回 Internal Error，因此发现与排名一节的中文依据英文正文。快照记录 Android XR 出现在英文开发者政策中心，简体中文政策中心目录没有对应入口。本仓库中文是编辑改写。帮助社区重试和部分 Vitals 视频的缓存未命中是访问限制，不是政策变更。所链接的联系人权限变更在联系人专题记为 2027-01-27，不是本质量指南的现行生效日。Desktop Preview 是 Android Studio 预览通道，不是 Play 生效日。某一设备形态的验收标准可能影响该形态的审核或分发。Android 质量支柱、Vitals 阈值和帧率建议是实现说明，不是统一的 Play 违规门槛。所链接的 Play 政策在各自页面仍是 normative。证据等级：Play Help 质量索引为 Operational；Android 工程指导为实现说明。

**核对日期：2026-10-22。** Play Console Help 的“Other Resources”不是一份单一政策，而是把内容分级、Families 和 Android 各设备形态的质量指南放在同一目录。正式 Developer Program Policy、设备形态质量门槛和一般实现建议应分开判断：有些质量清单会影响该形态应用的审核或发布；一般建议不自动等于所有应用必须满足的 Play 政策。

## Play Help：“Ensuring app quality”

已打开 [Ensuring app quality](https://support.google.com/googleplay/android-developer/answer/13965279?hl=en)。它说明应用质量与用户满意度、下载、留存和安全相关，建议在多种设备/系统上充分测试、保持界面直观、回应用户反馈、持续提供安全更新，并遵守适用法律和 Google Play 政策。它是导览页，不是新增的独立政策条款。

### 正文政策链接

| 页面中的链接 | 目标页和关系 | 本地核对 |
| --- | --- | --- |
| [Android app quality overview](https://developer.android.com/quality) | 把 Android 应用质量分为核心价值、用户体验、技术质量、隐私与安全四个支柱；另有设备形态指南。 | 总览及四个支柱页均已打开；关键实践见下表。Android 实现指南不是 Play 的独立政策。 |
| [Functionality, Content, and User Experience](https://support.google.com/googleplay/android-developer/answer/9898783?hl=en) | 正文分为有限功能/内容和功能故障两节；静态文本或 PDF、内容很少、无法安装/加载/响应、崩溃或冻结是例子。 | 现行正文及编号已在[垃圾信息、功能与体验专题](../spam-and-functionality/spam-and-functionality.zh-CN.md)核对；摘要/Key Considerations 与完整政策冲突时以完整政策为准。 |
| [Deceptive Behavior](https://support.google.com/googleplay/android-developer/answer/9888077?hl=en) | 防止虚假功能、误导元数据、未经同意且不可逆的设备设置更改，以及隐藏或规避审核行为。 | 旧链接重定向到现行答案 17006354；见[欺骗性行为专题](../deceptive-behavior/deceptive-behavior.zh-CN.md)。 |
| [Impersonation](https://support.google.com/googleplay/android-developer/answer/9888374?hl=en) | 防止冒充开发者、公司、政府、实体或其他应用。 | 已纳入[冒充身份专题](../impersonation/impersonation.zh-CN.md)。 |
| [Spam](https://support.google.com/googleplay/android-developer/answer/9899034?hl=en) | 涵盖未经用户确认代发信息、未经授权的 WebView/导流及重复低价值应用等。 | 正文、图示链接和课程入口见[垃圾信息、功能与体验专题](../spam-and-functionality/spam-and-functionality.zh-CN.md)；课程内容仍部分受登录限制。 |
| [Ads](https://support.google.com/googleplay/android-developer/answer/9857753?hl=en) | 广告内容、受众、体验、行为、安全与隐私均影响应用体验；儿童受众还受 Families 规则约束。 | 见[广告与推广专题](../ads-and-advertising/ads-and-advertising.zh-CN.md)和[儿童安全专题](../age-restricted-child-safety/age-restricted-child-safety.zh-CN.md)。 |
| [Google Play Academy policy courses](https://playacademy.withgoogle.com/courses/google-play-policy/) | 政策培训入口；FAQ 将课程描述为帮助理解隐私友好设计、政策违规、受限内容、变现和知识产权的学习材料。 | 页面与 FAQ 已打开；链接的课程/视频部分需要登录或无法提取。培训不是政策正文或豁免。 |

Help 页底部的 Community/Contact 是支持入口，不构成要求；抓取未取得可用的社区目标，联系流程需要账户访问。右侧 “App management” 导航及其“支持用户”“查看/购买自己的应用”“许可证密钥”三篇帮助文章也不是质量政策；本次重试均返回 Cache miss，其中“支持用户”页面已有先前打开的摘要，另外两篇的正文未取得，状态见来源审计表。

### Android 质量四支柱：可执行的最佳实践

以下内容来自 [Android App quality](https://developer.android.com/quality) 及其四个支柱页（[Core value](https://developer.android.com/quality/core-value)、[User experience](https://developer.android.com/quality/user-experience)、[Technical quality](https://developer.android.com/quality/technical)、[Design for Safety](https://developer.android.com/quality/privacy-and-security)）。该系列同时列有大量 API、设备和测试后代；本表总结与 Play 审核、用户体验和发布风险直接相关的原则，不把工程建议说成强制政策。

| 支柱 | 指南摘要 | 在本知识库中的对应内容 |
| --- | --- | --- |
| 核心价值 | 为目标受众解决真实问题或提供乐趣；功能深度应匹配使用场景，不要为增加功能造成菜单混乱、内容过时或缺陷；商店素材应准确描述实际价值；优先观察评分、参与和留存等质量指标，不能把买量或获客量当作核心价值本身。 | [商店详情最佳实践](../store-listing-best-practices/store-listing-best-practices.zh-CN.md)、[评分与评价](../user-ratings-reviews-installs/user-ratings-reviews-installs.zh-CN.md)、本页的应用发现与排名部分。 |
| 用户体验 | 使用熟悉且一致的控件；按支持的屏幕、设备姿态和形态适配；做好无障碍、本地化、引导、分享/备份和可直达内容的深链。预先说明付费条件；广告的时长、频率和位置应与内容相称，避免误触，开发者仍对 SDK 展示内容负责。 | 本页的设备形态指南、[付款与订阅](../payments/payments-and-subscriptions.zh-CN.md)、[广告](../ads-and-advertising/ads-and-advertising.zh-CN.md)、[目标受众与儿童安全](../age-restricted-child-safety/age-restricted-child-safety.zh-CN.md)。 |
| 技术质量 | 按设备监控崩溃、ANR、低内存终止、启动、渲染、电量、网络和应用体积；可用 Android Vitals/Reporting API 观察设备差异并通过分阶段测试、发布和监控减少生产故障。指南给出的帧率与优化方法是体验建议，不是全应用统一的 Play 政策阈值。 | 本页的 Android Vitals 部分、[测试与发布流程](../publishing/play-release-workflow.zh-CN.md)。 |
| 隐私与安全 | 尽量减少权限、位置精度/频率、可见的已安装应用和不可重置标识；优先用系统 Picker、专用目录和配对 API；在功能需要时请求权限、记录权限使用并尊重拒绝；保护数据传输和存储，管理身份验证、完整性与 SDK 依赖。 | [用户数据](../user-data/user-data.zh-CN.md)、[Android 隐私清单](../android-privacy-checklist/android-privacy-checklist.zh-CN.md)、[敏感权限](../sensitive-permissions/sensitive-permissions.zh-CN.md)、[第三方 SDK](../sdk-requirements/sdk-requirements.zh-CN.md)。 |

**边界：** Google Play Help 页链接到五篇政策正文；这些政策自身有约束力。Android 四支柱页提供工程质量建议，并未把每个推荐项变成政策审核条件；例如帧率建议、性能优化手段不能直接当作统一的违规判定标准。逐项 API/指南后代仍未穷尽，按功能走对应专题和官方原文。

## 按设备形态查当前指南

| 范围 | 当前指南与主要用途 | 与 Play 发布的关系 |
| --- | --- | --- |
| 所有 Android 应用 | [Core app quality](https://developer.android.com/docs/quality-guidelines/core-app-quality) 汇总基础可用性、兼容性、性能、隐私和测试检查。本文只记录与 Help 目录关系最强的部分；该长指南及其所有测试后代未逐项复制。 | 提供基础质量参考；特定设备/类别清单可能有单独审核条件。 |
| 手机、平板、折叠屏和桌面 | [Adaptive app quality](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality) 将体验分为 Tier 3 Adaptive ready、Tier 2 Adaptive optimized、Tier 1 Adaptive differentiated，并提供不同屏幕/窗口模式兼容测试。该指南说明它替代并扩展旧 large-screen 指南；Help 旧“Tablet App Quality”链接是否精确重定向到此页，本次未能确认。 | 按实际功能采用适用检查，不应把整个交互式清单解释为所有应用的统一审核条款。 |
| Wear OS | [Wear OS app quality](https://developer.android.com/docs/quality-guidelines/wear-app-quality) 含应用与表盘的交互、可访问性、稳定性、发布和测试条件。页面列出 2026-09-15 起 64 位支持要求、2026 年表盘 Watch Face Format 要求及表盘商店图标要求。 | 页面明确说明不符合适用质量要求可能导致 Wear OS 应用被拒；形态专属审核也可能阻塞跨设备商店详情更新。 |
| Android TV | [TV app quality](https://developer.android.com/docs/quality-guidelines/tv-app-quality) 按 TV Ready / Optimized / Differentiated 分层，涵盖遥控导航、布局、清单、广告、媒体播放和审核。 | 页面列出 Android TV 的 AAB、64 位和 16 KB 页面大小要求；64 位与 16 KB 要求自 2026-08-01 起适用。电视形态审核未通过时，商店详情更新可能被阻塞。 |
| Android Auto / Android Automotive OS | [Car app quality](https://developer.android.com/docs/quality-guidelines/car-app-quality) 按应用类别和 Car ready / optimized / differentiated 分层，分别核对 Android Auto 与 Android Automotive OS；须按实际类别筛选并测试。 | Google 对车载应用执行额外质量审查；页面说明审核未通过时，后续应用更新可能无法分发。Android Auto（手机投屏）和 Automotive OS（车机系统）不可混为一类。 |
| Android XR 头戴设备、有线 XR 眼镜、音频/显示眼镜 | 英文 Developer Policy Center 现列出 [Android XR 应用质量指南](https://developer.android.com/docs/quality-guidelines/android-xr)；按沉浸式与增强体验分别链接专页。专页包含明确的相机/麦克风旁观者保护、LED/防篡改和智能眼镜手势要求。 | XR 指南中的“Android XR App Policies”与全体 Play 政策并行适用；具体隐私/安全要求见[独立双语 XR 专题](../android-xr-app-quality-and-policies/android-xr-app-quality-and-policies.zh-CN.md)。Android XR 目前未出现在简体中文政策中心目录中。 |
| Android Auto / Automotive 分发条款 | [Android for Cars DDA Addendum](https://play.google/auto/developer-distribution-agreement-addendum/)（2024-08-30）为 Android Auto / Automotive OS 的分发附加条款，与 DDA、Developer Program Policies 和 Google APIs Terms 一并适用；与主协议冲突时，就车载分发以本 Addendum 为准。 | 车载产品可能须经独立审核/批准；是否审核及是否批准由 Google 决定，Google 可随时阻止产品在车载环境中使用。它是专项合同条件，不替代通用 Play 政策。 |
| Wear OS 表盘市场 | [Watch Face Push](https://developer.android.com/training/wearables/watch-face-push) 是 Wear OS 6 面向表盘市场应用的安装/更新 API，不是普通表盘发布的必需方案。表盘须用 Watch Face Format；专属包名、APK 内容/minSdk、官方验证器与独立签名密钥均有约束。 | 市场应用负责通过官方验证工具检查推送表盘的格式和性能；这些实现条件与普通 Play 表盘审核并存，不能互相替代。 |

通用迁移时还要单独遵守[目标 API 专题](../target-api/target-api-level.zh-CN.md)和[商店详情/截图要求](../store-listing-best-practices/store-listing-best-practices.zh-CN.md)。设备形态质量指南中的技术测试、商店素材要求及 Play 政策各有适用范围，不因链接出现在同一目录就自动互相替代。

### Adaptive app quality：2026-10-21 更新、兼容层级与测试矩阵

2026-10-24 重开 Android Developers 的[Adaptive app quality guidelines](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality)（页面标注最后更新 2026-10-21）。指南覆盖手机、平板、折叠屏、桌面、车载屏、电视和 XR，并考虑多窗口、多显示器、多实例、画中画及折叠姿态。它要求先参考兼容性清单和测试，但明确说明并非每个应用都要满足全部项目：只实现与应用用例相符的检查。

| 层级 | 页面概述 | 实施理解 |
| --- | --- | --- |
| Tier 3 — Adaptive ready | 应用在各种设备上全屏/完整窗口运行，不被 letterbox，也不处于兼容模式；关键流程可完成；对键盘、鼠标、触控板和手写笔提供基础支持。 | 先确保可用和关键流程不断；布局可能还不理想。 |
| Tier 2 — Adaptive optimized | 对屏幕尺寸和设备配置做响应式/自适应布局优化，并增强外接输入支持。 | 指南建议达到 Tier 2，以便在各种 Android 设备上获得良好体验。 |
| Tier 1 — Adaptive differentiated | 为正在使用的设备/显示器设计体验；适用时支持多任务、折叠姿态、拖放和手写笔。 | 用于折叠屏和桌面等大屏差异化体验；不是所有应用都必须支持每一种能力。 |

当前兼容性测试建议至少覆盖：Googlebook（160 ppi）、折叠屏（841×701 dp）、8 英寸平板（1024×640 dp）、10.5 英寸平板（1280×800 dp）和 13 英寸 Chromebook（1600×900 dp）。官方模拟器建议为 Pixel Fold、Medium Tablet 和 Desktop (Preview)；桌面预览模拟器须使用 Android Studio Canary，并按预览版安装说明并行安装。页面还链接到可调整尺寸模拟器，便于检查多种窗口大小。该矩阵是工程验证参考，不能直接转换成统一的 Play 审核义务。

#### 指南的直接链接及关系

主指南正文的兼容性清单/测试及 Tier 3/2/1 是页内锚点，不是额外政策页面。其余 8 个不同正文目标均已逐一打开；较旧大屏档案和旧版模拟器说明仍按历史材料处理。Play 商店素材具体规格以 Play Help 为准，Android 工程指南的素材建议不自动新增一项普遍政策义务。

| 直接目标页 | 页面内容与主指南的关系 | 本轮访问与范围 |
| --- | --- | --- |
| [Large screen app quality（2026-01-21 档案）](https://developer.android.com/docs/quality-guidelines/archive/adaptive/large-screen-app-quality) | 保存旧版大屏 Tier 3/2/1 清单和测试。旧版详细覆盖配置与状态保留、多窗口/多恢复、相机/媒体投影、键盘/鼠标/触控板、手写笔、响应式布局等；新版把对象扩到更多形态并更新测试尺寸/模拟器。 | 页面已打开；核对 Tier 3、Tier 2 和兼容性测试段落。该长页的全部测试链接及工程后代尚未逐一展开。 |
| [Play 商店预览素材 Help](https://support.google.com/googleplay/android-developer/answer/9866151?hl=en) | 解释应用图标、简短说明、宣传图、截图及视频的提交规格/展示建议；应与自适应指南的“展示平板/折叠屏截图、在说明中提及 XR 特性”建议配合。 | 具体强制规格、推荐做法及设备形态差异见[商店详情最佳实践](../store-listing-best-practices/store-listing-best-practices.zh-CN.md)；不要把该 Android 指南本身当作素材规格来源。 |
| [旧 gallery 地址](https://developer.android.com/large-screens/gallery) → [现行 Adaptive layout gallery](https://developer.android.com/design/ui/gallery) | 展示不同屏幕大小的布局灵感，提供交互式样例筛选。 | 官方旧路径重定向到现行 gallery；入口已打开，但动态样例未从抓取文本中提取，作为设计参考而非政策清单。 |
| [Android Studio Preview](https://developer.android.com/studio/preview) | Android Studio Canary/RC 预览版本入口；当前下载频道和版本号会变化。 | 预览目录已打开；具体 Canary/RC 子版本和下载链接是动态信息，使用前查实时页面。 |
| [Install a preview version of Android Studio](https://developer.android.com/studio/preview/install-preview) | 说明预览版可与稳定版并行安装；各版本设置目录分开，但通常共用 SDK 路径；较新 IDE 可能改写项目配置。 | 正文步骤已打开；Mac/Windows/Linux 安装说明已归纳。保持稳定版作为备用是工程建议，不是 Play 政策。 |
| [Get 12L：可调整尺寸模拟器](https://developer.android.com/about/versions/12/12L/get#resizable-emulator) | 旧版 12L 说明可用 Resizable device definition 在手机、折叠屏、平板和桌面参考设备间切换，并可切换折叠状态。 | 相关段落已打开；页面其余设备/GSI/合作伙伴章节不属于当前桌面 Preview 的安装说明，未纳入本摘要。 |
| [Tier 2 — Adaptive optimized（2026-04-07 档案）](https://developer.android.com/docs/quality-guidelines/archive/adaptive/tier-2-2026-04-07) | 展开 Tier 2：按窗口大小类构建响应式/自适应布局、多窗格、适配次级控件、至少 48 dp 触控目标、外接键盘导航/快捷键/媒体控制、右键菜单、缩放与 hover 状态；附对应测试步骤。 | 归档正文和主要检查/测试段落已打开；更深的 Material、可访问性和代码示例链接未全量追踪。 |
| [Large-screen → Adaptive ID map](https://developer.android.com/docs/quality-guidelines/archive/adaptive/id-map-ls-adaptive) | 逐项映射旧 `LS-*`/`T3-*`/`T2-*` ID 到新 Adaptive checklist/test ID；还列出新增桌面、折叠屏、打印/文件管理、跨设备、离线、相机/音频等 Tier 1 检查。 | 映射表已打开；适合迁移旧测试计划，映射本身不新增 Play 政策条款。 |

**政策边界与递归状态：** 该 Android 页面是适配设计/测试指导，并声明按用例选择检查；Play Help 中明确列出的素材规格、各设备形态单独要求、Developer Program Policy 和合同条款仍分别适用。主指南的 8 个外部正文目标均已定位并打开；Play Help 素材页已有单独专题。旧 large-screen 长页、Tier 2 归档、Android Studio 页面及 ID map 的全部子链接和更深 API/代码示例仍未闭合，见来源页审计表（快照：`../source-page-audit.csv`，未导入本仓库）及递归关系记录 §4.132（快照：`../google-play-policy-link-graph.md#4132-adaptive-app-quality2026-10-21-指南更新兼容层级与直接子页2026-10-24`，未导入本仓库）。

### Core app quality 的隐私与权限直链

Core app quality 把“所有应用的最低质量检查”与 Play 的数据政策、权限实现指南并列呈现。阅读时应按来源性质分层：Play 政策决定数据处理和敏感权限的资格，Android Developers 页面解释较少权限的实现方案；平台 API 可用不等于 Play 已批准该用途。

| Core app quality 中的目标 | 性质及与质量指南的关系 | 知识库处理与访问状态 |
| --- | --- | --- |
| [User Data policy 原始目标](https://play.google.com/about/privacy-security/user-data) → [现行 Help 正文](https://support.google.com/googleplay/android-developer/answer/10144311?hl=en) | Play 的正式数据处理要求；Core app quality 用它说明隐私和用户数据保护属于基本质量范围。 | 原始链接跳转到现行 Help 目标，但浏览器未能从旧跳转页直接读取正文；现行政策正文已打开并整理在[用户数据专题](../user-data/user-data.zh-CN.md)。 |
| [SMS and Call Log permission groups](https://support.google.com/googleplay/android-developer/answer/10208820?hl=en) | Play 对短信和通话记录权限用途的资格、申报和替代方案要求；它不是一般 Android 权限 API 的使用许可。 | 正文与主要替代方案已打开并详见[短信和通话记录权限专题](../sms-call-log/sms-call-log.zh-CN.md)；API 和供应商实现后代仍按该专题标记为部分覆盖。 |
| [Minimize your permission requests](https://developer.android.com/privacy-and-security/minimize-permission-requests) | Android 实施建议：按需用粗略位置、系统 Picker、SAF、Intent 或用途专用 API 代替宽权限，并在用户拒绝时优雅降级。 | 正文已打开，最后更新 2026-08-19；主要替代方案已在[Android 隐私清单](../android-privacy-checklist/android-privacy-checklist.zh-CN.md)归纳，个别代码/API 后代未穷尽。它不能替代 Play 的敏感权限资格审查。 |
| [location 权限参考：Request runtime permissions](https://developer.android.com/training/permissions/requesting) | Core app quality 用它说明在用户触发功能时请求权限、解释用途、处理拒绝；页面另区分前台/后台和粗略/精确位置。 | 2026-10-23 重开全文并核对位置分支；运行时/API 示例后代仍部分覆盖。对应 Play 资格和申报见[后台位置](../background-location/background-location.zh-CN.md)、[联系人与位置权限](../contacts-location-permissions/contacts-location-permissions.zh-CN.md)。 |
| [implicit intent → Common intents](https://developer.android.com/guide/components/intents-common) | 用系统应用/用户选择流程完成联系人、短信/拨号等任务，减少直接读取个人数据所需权限。 | 全文已打开；本轮补看 Contacts/people 章节：`ACTION_PICK` 可让用户选联系人并授予临时 URI 访问；读取基本资料通常不需 `READ_CONTACTS`，读取特定号码/邮箱时可能需要。详见下方后代关系；这不是 Play 受限权限豁免。 |
| Core app quality 的两条数据存储/日志链接 → [Android Security checklist](https://developer.android.com/privacy-and-security/security-tips) | 指向同一篇 Android 安全指南：默认内部存储通常仅本应用可访问；外部存储可能被其他应用读取/修改，敏感数据不应放在那里；系统日志不应写入个人或敏感数据。 | 相关正文段落于 2026-10-23 重开；大篇安全指南的全部认证、网络、IPC、API 后代未穷尽。见[Android 隐私清单](../android-privacy-checklist/android-privacy-checklist.zh-CN.md)。 |
| [Best practices for unique identifiers](https://developer.android.com/identity/user-data-ids) | Core app quality 禁止为身份识别使用 IMEI 等不可重置硬件 ID；该指南按用途比较广告 ID、App Set ID、FID/GUID 等标识符。 | 31 个正文链接已尝试，完整用途矩阵见[广告 ID 与标识符专题](../advertising-id/advertising-id.zh-CN.md)；标识符选择属于 Android 指引，Play 数据/广告政策仍单独适用。 |

关联核对还应跳转到[敏感权限政策](../sensitive-permissions/sensitive-permissions.zh-CN.md)及[后台位置专题](../background-location/background-location.zh-CN.md)。上表涵盖隐私/权限段落的 **8 个正文锚点、7 个不同目标**（存储与日志两个锚点合并到同一安全指南）。Core 指南中的 `T-*` 条目是质量测试/实现检查；本轮没有逐一打开 619 行页面的全部测试锚点、Android API 和示例后代。

### implicit intent → 联系人选择的后代

Core quality 的联系人替代方案链接到 [Common intents](https://developer.android.com/guide/components/intents-common) 的 Contacts/people 章节。该章节把联系人访问拆成“用户选择”和“应用查询完整/指定资料”两类：

- 使用 `ACTION_PICK` 与 `Contacts.CONTENT_TYPE`，用户选择联系人后，系统返回 `content:` URI 并给应用临时访问；对显示名等基本资料，指南通常不要求 `READ_CONTACTS`。
- 若只需一个字段，可指定 `CommonDataKinds.Phone.CONTENT_TYPE` 等更窄 MIME 类型；读取电话号码、邮箱等特定资料时可能仍须 `READ_CONTACTS`。不要把 Picker 当作读取完整联系人库的授权。
- [Contacts Provider（旧链接）](https://developer.android.com/guide/topics/providers/contacts-provider) 已跳转到[现行 Contacts Provider 指南](https://developer.android.com/identity/providers/contacts-provider)。本轮只核对联系人数据表结构、选中 URI 的读取关系及其 `ContactsContract`/Content Provider 后代入口；1368 行的同步适配器、写入、账户和 API 参考未逐项审完。
- `READ_CONTACTS` 的平台常量见 [`Manifest.permission`](https://developer.android.com/reference/android/Manifest.permission#READ_CONTACTS)。平台能授予 URI 或运行时权限，不代表 Play 允许任意用途；仍须按核心功能、披露、最小范围和[2027 联系人权限变更](../contacts-location-permissions/contacts-location-permissions.zh-CN.md)分别评估。

## 应用发现与排名：相关性、质量和 Play 内展示

**核对日期：2026-10-22。** [App Discovery and Ranking](https://support.google.com/googleplay/android-developer/answer/9958766?hl=en) 是开发者资源说明页，解释 Play 如何理解应用并组织搜索、浏览、编辑推荐和广告展示；它不是排名算法公式，也不是执行/反操纵条文。英文正文已打开；简体中文 URL 本轮返回 Internal Error，因此以下是按英文现行正文整理的中文摘要。

页面列出五组因素：

| 因素 | 页面说明 | 可控的开发者工作 | 边界 |
| --- | --- | --- | --- |
| 用户相关性 | 浏览页面、搜索词、意图及同义词；应用可用的国家、设备和形态；用户表达的受众兴趣及个性化推荐。越宽泛的搜索，候选应用越多。 | 维护准确的标题、描述、类别、受众与市场/设备分发范围；按真实目标用户做好本地化。 | 页面没有披露查询权重、个性化参数或保证排名的办法。 |
| 应用体验质量 | 技术表现和应用内体验；图标、标题、截图、视频、描述、链接等安装前信息；功能、兼容性、稳定性、响应和客户支持。 | 持续修复崩溃/ANR、保证核心功能完整、让素材准确代表产品，并处理用户支持问题。 | Android 质量指南、特定设备形态审核和正式 Play 政策需按各自适用条件判断。 |
| 编辑价值 | Play 编辑团队人工策展和推荐；考虑新颖度、设计、实用性、受众广度，也可能考虑时效、本地相关性和活动主题。 | 提供有辨识度、真实、设计良好的体验，并维持稳定的内容质量。 | 这是编辑选择说明，不是开发者可申请或保证获得推荐的承诺。 |
| 广告 | 开发者可以购买展示位；广告应清楚标注为广告或赞助内容，并与普通内容并列展示。 | 若投放应用广告，按 Google Ads 的真实广告流程操作，并避免把广告伪装成自然排名。 | 页面没有说投放广告会提升自然搜索排名。 |
| Play 内用户体验 | 页面分组、结果展示数量与样式、广告位置及导航设计均会影响用户体验。 | 提供稳定、可理解的应用体验；遵守广告、元数据、垃圾内容和评价政策。 | Play 页面布局和排名权重会持续测试优化；不同入口、设备和用户偏好可能不同。 |

主要因素会按 Google Play 的展示页面、设备和用户偏好采用不同权重：Top Charts 更受受欢迎程度影响，搜索结果更看重与查询的相关性；为特定设备优化的应用可能在该设备上更合适。页面也说明，较窄受众的应用可能只在查询/浏览状态明确相关时获得突出展示。以上是排序解释，不应被改写成可操纵的排名公式。

### 正文直链：16 个锚点、15 个不同目标

链接计数只覆盖正文中的 16 次链接出现（Activity controls 在正文出现两次）和 15 个不同的原始目标。Help Community/Contact 两个通用页脚入口点击后未返回可用目标 URL，故单独记为未解析；页顶部的“Google Play Works for Developers”轮播是共享导航，不混入正文链接数。轮播另指向[How Google Play Works for Developers](https://support.google.com/googleplay/android-developer/topic/9958765)、[Helping Developers Succeed](https://support.google.com/googleplay/android-developer/answer/9969970)、[Data Access](https://support.google.com/googleplay/android-developer/answer/9959470)、[Availability of Features and Services](https://support.google.com/googleplay/android-developer/answer/9959788)及[日文版 Data Access](https://support.google.com/googleplay/android-developer/answer/16799586?hl=en)。其中三个英文主题已有独立摘要；日文页现已通过 `hl=en` 入口读到日文正文并在下文摘要。重新点击 Availability 返回 Cache miss。各目标的访问状态另见人工审计表（快照：`../source-page-audit.csv`，未导入本仓库）。

| 正文链接 | 内容及与发现/排名页的关系 | 核验状态 |
| --- | --- | --- |
| [Teacher Approved program](https://developer.android.com/google-play/guides/teacher-approved-apps) | 儿童应用策展/标识入口。 | 链接跳转至 [Play Console Teacher Approved](https://play.google.com/console/about/teacherapproved/) 后浏览器失败；不推断其当前计划或审核条件。 |
| [Google Privacy Policy](https://policies.google.com/privacy) | 说明 Google 的信息收集、用途、个性化及用户隐私控制；用于解释个性化推荐背景。 | 正文已部分读取；这是面向 Google 服务的一般隐私政策，不是 Play 排名规则，未递归其长篇链接树。 |
| [Activity controls](https://myaccount.google.com/activitycontrols) | 用户管理 Web & App Activity 等账号活动设置的入口。 | 重定向 Google 登录；用户账号专属，开发者资格不可据此判断。 |
| [Delete your activity](https://support.google.com/accounts/answer/465) | 用户查看或删除账号中已保存活动的帮助页。 | 目标正文已打开；属于用户控制资料，不新增 Play 开发者义务。 |
| [Google account information](https://account.google.com/) | 账号管理/安全信息入口。 | 跳转至 `www.google.com/account/about/`；页面是通用账号说明，不是排名要求。 |
| [Web & App Activity](https://support.google.com/websearch/answer/54068?hl=en) | 用户可查看、暂停或管理网页与应用活动保存设置。 | Help 正文已打开；这是用户账号控制说明，不是开发者排名申诉或数据接口。 |
| [Core app quality](https://developer.android.com/docs/quality-guidelines/core-app-quality) | 基础可用性、功能、性能/稳定性、隐私安全和测试指南，解释质量为何会影响推荐。 | 长指南已打开并核对相关段落；其中测试清单及大量 Android 技术后代未逐项闭合，详见下方质量范围说明。 |
| [Play Games Services quality checklist（旧地址）](https://developers.google.com/games/services/checklist) → [现行页面](https://developer.android.com/games/pgs/quality) | PGS 游戏兼容清单区分 Required 与 Best practices，涉及认证、成就、排行榜、好友、配额和云端存档。 | 旧地址已重定向，现行正文已打开。这里的 Required 仅是 PGS 兼容清单中的要求，不代表所有 Play 应用的通用内容政策；API 后代仍部分。 |
| [Closed testing（旧地址）](https://developer.android.com/distribute/best-practices/launch/test-tracks) → [现行页面](https://google.play/business/closed-testing/) | 选定测试者、收集私密反馈、使用 pre-launch report 等发布前实践。 | 已重定向到 Google Play 现行页面并打开。此页的自愿最佳实践与新个人开发者账号特定的 12 人/14 天闭测要求分开处理。 |
| [Build a high-quality app or game（旧地址）](https://developer.android.com/distribute/best-practices/launch/store-listing) → [现行页面](https://google.play/business/guides/build-a-high-quality-app-or-game/) | 汇总内容深度、定期更新、广告体验、商店详情实验、素材准确性、技术质量和隐私安全建议。 | 旧地址重定向后正文已打开；页面另列多条报告、视频和 Play Academy 链接，未把整条营销资源树误列为政策。 |
| [Learn about improving app quality — Play Academy](https://playacademy.exceedlms.com/student/catalog/list?category_ids=1788-learn-about-improving-app-quality) | 动态课程目录当时列出 App Bundle、Play 政策、应用测试和技术性能四项课程。 | 目录已打开；课程正文/登录后材料未读取。 |
| [View app statistics](https://support.google.com/googleplay/android-developer/answer/139628) | Console 提供安装/卸载、评分、收入、崩溃、商店转化和同类应用对比报告；同类数据经过归一化。 | Help 正文已打开；报告中的应用数据需要对应 Play Console 权限，统计报告不披露排名公式。 |
| [Android vitals（旧地址）](https://support.google.com/googleplay/android-developer/answer/7385505) → [现行帮助页](https://support.google.com/googleplay/android-developer/answer/9844486) | 将技术质量与某些 Play 展示/可发现性影响联系起来。 | 旧地址重定向到现行页面；核心阈值、样本范围和限制已在本专题下一节独立整理。 |
| [Ratings and reviews analysis（旧地址）](https://developer.android.com/distribute/best-practices/engage/user-reviews) → [现行页面](https://google.play/business/reviews/) | 用户反馈、回复、设备维度分析及 In-App Review API 入口。 | 旧地址重定向后正文已打开；评价真实性、不得操纵评分等正式要求见[评分/评价政策专题](../user-ratings-reviews-installs/user-ratings-reviews-installs.zh-CN.md)。 |
| [Google Ads app campaign Help target](https://support.google.com/googleplay/android-developer/answer/6262700) | 原文称用于创建 Google Ads 应用广告系列。 | 目标现已回落至通用 Play Help 首页；未读到原文章正文，不推断投放设置或政策细节。 |

**关系边界：** App Discovery 页面是发现/排名机制的解释，不是让应用迎合某个未公开算法的操作手册。与它直接相关的可执行条款仍以[商店详情/元数据](../store-listing-best-practices/store-listing-best-practices.zh-CN.md)、[评分、评价和安装](../user-ratings-reviews-installs/user-ratings-reviews-installs.zh-CN.md)、[垃圾内容](../spam-and-functionality/spam-and-functionality.zh-CN.md)、下方 Android Vitals 章节及适用设备形态质量条件为准。页面中的个性化账号链接讲的是用户控制；不可据此推断开发者能访问个人账号活动数据。

### 日文版“数据访问与使用”轮播页面

**核对日期：2026-10-22。**[日文页面](https://support.google.com/googleplay/android-developer/answer/16799586?hl=en)讲的是 Google 自身的数据访问与内部控制。页面介绍集中管理的标准、按流程限制和管理数据访问、技术保障、员工培训，以及其称于 2024 年 3 月在全球推出的扩展访问控制框架。页面称这些控制适用于 Google，并帮助其依据适用法律处理相关数据，其中包括日本《特定软件竞争促进法》。

它不是开发者数据处理清单，也不同于英文版 [Data Access 页面](https://support.google.com/googleplay/android-developer/answer/9959470)：后者说明开发者可通过 Play 工具访问哪些数据，以及对其他开发者非公开数据的限制。日文页面的政策正文没有链接；Help Community 操作返回 Cache miss，Contact us 则进入需要登录的 Play Console 支持页。这些通用求助入口不属于政策后代。详见链接图第 4.52 节（快照：`../google-play-policy-link-graph.md#452-日文版数据访问与使用页面`，未导入本仓库）。

## Android Vitals：上线后的质量信号与可发现性

**核对日期：2026-10-22。** [Android Vitals 帮助页](https://support.google.com/googleplay/android-developer/answer/9844486?hl=en)是发布后的质量监测和改进入口，不是另一份内容政策。它说明核心稳定性/电池指标越过坏行为阈值时，应用可能降低 Play 可发现性；特定设备型号可能被引导至其他应用，商店详情也可能出现提示。Play 通常评估最近 28 天，发生突增时可能提前行动。以下数值是当日页面快照，阈值可能调整，发布前应在实时帮助页和 Play Console 复核。

### 数据范围和解释

- Console 显示最近 90 天；[Play Developer Reporting API](https://developers.google.com/play/developer/reporting)提供最多 3 年的报告历史，并可用于内部分析和自动化工作流。Android Vitals 每日更新；没有数据通常表示所选筛选下样本不足。
- 数据来自一部分设备上选择自动共享使用情况与诊断数据的用户；未通过 Google Play 安装的应用版本和未认证设备型号产生的技术问题不计入这组 Vitals 指标。用户可在 [Google 账号帮助](https://support.google.com/accounts/answer/6078260)查看和更改设备诊断共享设置。
- 通用维度包括应用版本、Android 版本、设备形态、设备型号和国家/地区；部分指标还可以按 wake lock 名称、闹钟唤醒名称、ANR Activity 和 ANR 类型拆分。`No data` 或总体指标正常不排除少数设备/版本上的集中故障。

### Play 明确列出的核心阈值

| 指标 | 2026-10-22 页面给出的阈值 | 页面描述的 Play 影响 |
| --- | --- | --- |
| 用户可感知 ANR | 所有设备合计至少 **0.47%** 的每日活跃用户；单一设备型号至少 **8%** | 越过阈值属于坏行为，可能降低可发现性；可能按设备型号定向减少推荐。 |
| 用户可感知崩溃 | 所有设备合计至少 **1.09%** 的每日用户；单一设备型号至少 **8%** | 同上；先按影响用户数修复 Crashes and ANRs 中的高影响集群。 |
| 表盘过度耗电 | 所有设备合计或单一设备型号中，超过 **1%** 的表盘会话达到过度耗电定义 | 这是表盘专属核心质量信号；不要扩展成手机应用阈值。 |
| 过度部分 wake lock（Beta） | 超过 **5%** 的电池会话出现累计超过 **3 小时** 的部分 wake lock | 指标列在核心指标中，但帮助页明确 Beta 期间越线目前**不会**降低 Play 可发现性。 |

“核心价值”另列两项可能影响商店展示的信号：DAU/MAU 未达到 **8%** 阈值、或用户流失率超过 **5%** 时，可能出现商店提示，且应用可能失去部分 Play 展示面的资格。这些是页面所述的发现/展示机制；不能据此推导为内容政策违规或账号处罚。

### 非核心质量诊断指标

Android Vitals 还展示 ANR、崩溃、低内存终止、启动时间、游戏帧率、UI 卡顿/冻结、wake lock、闹钟唤醒、后台 Wi‑Fi/网络使用和权限拒绝。页面所称“慢启动”界限是冷启动 ≥5 秒、温启动 ≥2 秒、热启动 ≥1 秒；游戏慢会话以超过 25% 帧低于选定的 30/20 FPS 档位统计，页面建议多数游戏以 30 FPS 为目标，若无法达到则单次会话至少 75% 帧应达到 20 FPS。UI Toolkit 指标以 16 毫秒帧截止时间及 700 毫秒冻结帧定义呈现问题。这些是性能测量与建议，不能都当作适用于每个应用的强制 Play 阈值。

该帮助页对部分后台指标给出触发定义：卡住的部分 wake lock 超过 1 小时；每小时超过 10 次唤醒；后台每小时超过 4 次 Wi‑Fi 扫描；以及设备未充电时后台每天超过 50 MB 网络用量。页面也记录表盘设备未充电且没有应用使用时超过 4.44%/小时的耗电情形。Android 的独立表盘电池指南建议 80% 会话低于 3.2%/小时、总体过度耗电会话低于 1%；这些是表盘工程建议，不适用于普通手机应用。权限拒绝指标是 UX 诊断，不等于应请求更多权限。

### 正文直链及后代核验

页面里 Play Console 入口、实现指导、API 参考和帮助中心导航需要分开读。被称为“Android Vitals performance and stability best practices”的链接点击后重定向回本帮助页本身；它不是独立的最佳实践文章。

| 页面直链/后代 | 内容与和 Vitals 的关系 | 核验状态 |
| --- | --- | --- |
| [Android Vitals overview](https://play.google.com/console/developers/app/vitals/metrics/overview)；[Crashes and ANRs](https://play.google.com/console/developers/app/vitals/crashes?days=28&isUserPerceived=true) | 查看应用自己的指标、版本/设备维度和崩溃集群。 | 两个 Console 路由都重定向 Google 登录；无法读取账号数据。 |
| [Play Developer Reporting API](https://developers.google.com/play/developer/reporting) | 以 API 读取 Play Console 质量数据用于内部报告、分析和自动化；官方概览列出崩溃、ANR、wake-up/wake-lock 和错误堆栈等类别。 | 概览正文已打开；方法、指标字段和 API 示例的后代未全量展开。 |
| [ANR 指南旧地址](https://developer.android.com/topic/performance/vitals/anr.html) → [现行 ANR 指南](https://developer.android.com/topic/performance/issues/anr)；[Crash 指南](https://developer.android.com/topic/performance/vitals/crash.html) | Android 实现诊断：主线程长时间 I/O/计算、慢服务或广播、死锁和未完成 JobService 回调等可造成 ANR；Crash 指南用于分类和修复崩溃。Play Vitals 的用户可感知口径与平台错误诊断需结合使用。 | ANR 旧地址已重定向并打开现行正文；Crash 正文已打开。两篇技术指南自己的 API/示例子链接尚未全部核验。 |
| [启动时间旧地址](https://developer.android.com/topic/performance/launch-time.html) → [现行启动时间指南](https://developer.android.com/topic/performance/vitals/launch-time)；[游戏慢会话旧地址](https://developer.android.com/topic/performance/vitals/slow-session) → [现行慢会话指南](https://developer.android.com/topic/performance/issues/slow-session) | 解释启动状态、首帧/慢启动优化，以及游戏帧率与慢会话诊断。 | 两个旧地址均重定向到现行 Android Developers 页面；正文已打开，深层实现示例未穷尽。 |
| [UI 性能测试旧地址](https://developer.android.com/training/testing/performance.html) → [现行测试基础指南](https://developer.android.com/training/testing/fundamentals)；[SurfaceFlinger and WindowManager](https://source.android.com/docs/core/graphics/surfaceflinger-windowmanager) | UI 卡顿的测试背景；SurfaceFlinger 页面说明应用 buffer、合成与 VSync 的显示链路，是游戏帧率指标的技术背景。 | 两页正文已打开；平台参考页的侧栏/代码后代未全部访问。 |
| [PowerManager API](https://developer.android.com/reference/android/os/PowerManager.html)；[AlarmManager API](https://developer.android.com/reference/android/app/AlarmManager.html) | 分别对应部分 wake lock 与闹钟唤醒指标；工程上应识别获取原因、缩短后台持有时间并减少非必要唤醒。 | 两份 API 参考正文已打开；各类常量、方法和样例尚未全量整理。 |
| [Excessive battery usage 旧地址](https://developer.android.com/topic/performance/vitals/excessive-battery-usage) → [现行电池使用指南](https://developer.android.com/topic/performance/issues/excessive-battery-usage) | 指向 Android Developers 的电池使用诊断指南。 | 旧链接重定向到现行指南且正文已打开；其进一步技术链接未穷尽。 |
| Core Vitals/阈值和用户可感知指标的正文锚点；自定义 peer group 链接 | 阈值锚点仍在本帮助页；peer group 用于选定同类应用比较，不是政策豁免。 | 阈值内容已在父页阅读；peer group 点击返回 Internal Error，未猜测其目标地址。 |
| UI 帧率 60 FPS 视频、若干后台唤醒/Wi‑Fi/网络/权限优化链接 | 补充工程最佳实践，不增加独立的 Play 政策要求。 | 点击其中多个 Android Developers/视频链接返回 Internal Error，浏览器没有暴露目标 URL；不把未读资料当成已摘要。 |

该帮助页另有 20 项“Statistics & insights”侧栏推荐。这些是共享导航项，不是正文直接义务；只在与发布质量直接相关处交叉链接，不把导航列表混计为正文链接。发布后可按版本、Android/设备型号和地区复核趋势，并用最有影响的崩溃/ANR 集群安排修复；对缺少用户样本的指标应标记为未知，而不是推断为零问题。更多发布检查见[测试、审核与发布流程](../publishing/play-release-workflow.zh-CN.md)。

## Help Center“Other Resources”页的 10 个正文链接

该目录页（[Other Resources](https://support.google.com/googleplay/android-developer/answer/9877021?hl=en)）正文列出 10 个入口；页眉/页脚和 Help 侧栏导航另行区分。以下记录本轮逐项点击或查找结果：

| 目录中的链接 | 页面关系和访问结果 |
| --- | --- |
| [Content ratings](https://support.google.com/googleplay/android-developer/answer/9859655) | 旧链接 `answer/188189` 重定向至现行内容分级要求页；见[内容分级专题](../content-ratings/content-ratings.zh-CN.md)。 |
| Designed for Families program requirements and ads policies | 目录链接点击后落到通用 Help Center 首页；具体原始目标未由浏览器返回。当前 Families 政策另见[Families 页面](https://support.google.com/googleplay/android-developer/answer/9893335)，已在儿童安全专题交叉整理。 |
| [Core app quality](https://developer.android.com/docs/quality-guidelines/core-app-quality) | 已打开当前指南并核对与 Play 质量相关的范围；全文很长，仅选取核心背景，测试清单和后代技术链接仍未穷尽。 |
| Tablet App Quality | 旧目录链接点击返回 Internal Error，浏览器没有暴露目标地址。当前[Adaptive app quality](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality) 明确替代并扩展旧 large-screen 指南，但未确认它就是该旧链接的重定向目标。 |
| Wear App Quality | 目录链接点击失败；当前 [Wear OS quality guide](https://developer.android.com/docs/quality-guidelines/wear-app-quality) 已通过 Android Developers 官方目录找到并打开，是否为原始链接的精确目标未确认。 |
| [TV App Quality](https://developer.android.com/docs/quality-guidelines/tv-app-quality) | 旧地址 `/distribute/essentials/quality/tv.html` 已验证重定向至当前 TV 清单。 |
| Auto App Quality | 目录链接点击失败；当前 [Car app quality guide](https://developer.android.com/docs/quality-guidelines/car-app-quality) 已通过 Android Developers 官方目录找到并打开，未把它冒充为已验证的旧 URL 重定向。 |
| [Daydream App Quality Requirements](https://developers.google.com/vr/distribute/daydream/app-quality) | 官方旧 VR 指南仍可读取，涵盖舒适度、控制器、稳定性和发布素材；页面最后更新于 2024-10-09。作为历史平台参考，不据此推导现行通用 Play 要求。 |
| Tango Developer Overview | 目录链接点击返回 Internal Error，目标地址和正文均未恢复；不据此推断其当前状态。 |
| Instant Apps Requirements | 目录链接点击返回 Internal Error，目标地址未恢复。Instant Apps 是已停用项目，相关历史政策和技术状态见 [Android Instant Apps 专题](../android-instant-apps/android-instant-apps.zh-CN.md)。 |

页面旁栏另显示内容分级、Families、开发者政策等推荐入口；这些并非上述 10 个正文目标的替代计数。原始目标地址未返回、需登录或属于旧平台的链接均保留为覆盖缺口，不以相似标题页冒充已验证重定向。

## 其他资源目录的关联入口

- [Updates and Other Resources](https://support.google.com/googleplay/android-developer/topic/9877065) 是导航索引，正文通向 Policy Deadlines、Other Resources、开发者支持、Policy Archive、PolicyBytes Hub 和合并版 Developer Program Policy。该页同时提示欧盟开发者可申请与 Google Play 解决争议的调解；除法律要求外，调解为自愿且双方均无义务和解。
- [Monetization and Ads](https://support.google.com/googleplay/android-developer/topic/9857752) 是 Payments、Ads、Subscriptions 和 Families Self-Certified Ads SDK Program 四项规则的目录入口。对应正文已有单独专题或来源记录；目录本身不构成支付/广告豁免。

## 来源与边界

- [Other Resources — Play Console Help](https://support.google.com/googleplay/android-developer/answer/9877021?hl=en)
- [Adaptive app quality — Android Developers](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality)
- [Wear OS app quality — Android Developers](https://developer.android.com/docs/quality-guidelines/wear-app-quality)
- [TV app quality — Android Developers](https://developer.android.com/docs/quality-guidelines/tv-app-quality)
- [Car app quality — Android Developers](https://developer.android.com/docs/quality-guidelines/car-app-quality)
- [Android XR app quality — Android Developers](https://developer.android.com/docs/quality-guidelines/android-xr)
- [Daydream app quality — Google for Developers](https://developers.google.com/vr/distribute/daydream/app-quality)

本专题整理 Help 资源页的可访问范围和当前设备形态指南，不是 Android Developers 全站链接的递归镜像。发布前应按实际分发设备、应用类别、最新日期和 Play Console 内的审核结果复查。
