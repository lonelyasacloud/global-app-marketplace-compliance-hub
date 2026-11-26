---
id: google-play.play-release-workflow
platform: google-play
language: zh-CN
authority: operational
status: current
kb_checked_at: 2026-10-22
review_due: 2027-01-22
regions: [global]
topics: [release-workflow, play-console, testing, app-review, staged-rollout]
snapshot_id: play.release-workflow
snapshot_package: "GooglePlay-KnowledgeBase-2026-10-24-review.zip"
coverage_status: "detailed-summary"
source_url: "https://support.google.com/googleplay/android-developer/answer/9859348?hl=en"
---

# Google Play 测试、审核与发布流程

> **导入说明（Google batch 1）。** 本页正文取自 2026-10-24 Google Play 知识库快照里已经分开的中文改写摘要，不是 Google 已发布中文页面的逐字文本。英文官方页面是效力来源。`kb_checked_at` 使用快照源文件记录的核对日；本次导入没有重新打开线上官方页面。文中“本知识库”“本库”“本地专题”描述的是该快照知识库的覆盖范围，不是本仓库已经导入的页面清单。快照里指向尚未导入本仓库的专题、链接图、台账或 CSV 的相对链接，已改为文字提及；指向本批六个专题的相对链接已改到本仓库路径。 快照把本页主要来源记为英文《Prepare and roll out a release》帮助页，核对日 **2026-10-22**。本页中文是对该英文指南及相关帮助页的编辑改写。快照没有另记这份主指南的中英文官方页面滞后；中文源文件里部分白标公告 URL 使用 `hl=zh-CN`。本页描述 Play Console 操作，不替代开发者计划政策或开发者分发协议。证据等级：`operational`。

## 范围与核对口径

本页依据官方《Prepare and roll out a release》及其测试、权限声明、Managed publishing、分阶段发布和国家/地区投放帮助页整理，核对日期为 2026-10-22。它描述 Play Console 操作流程，不替代《开发者计划政策》或单项政策。审核资格、目标 API 要求和实际发布状态仍以当前官方页面与账号 Console 为准。

快速查看商店资料、审核可访问性和拒审后的修复关口，可参见上架准备与发布最佳实践；本页继续展开 Play Console 测试轨道和发布操作。

## 发布前检查

创建 release 前，先完成商品详情、App content 审核材料、定价和 Dashboard 上的必需设置。创建版本的用户须有对应轨道发布权限。准备审核所需的登录凭证、演示材料和申报内容，见 Play Console 要求；商店素材见商店详情最佳实践。

Play 提供 Open、Closed、Internal 测试轨道和 Production 正式轨道。Internal testing 每个应用最多可添加 100 名测试者。新建于 2023-11-13 之后的个人开发者账号，在申请生产权限前必须完成至少 12 名测试者连续 opt-in 满 14 天的封闭测试，并提交生产权限申请问答；不要将该特定门槛泛化到组织账号或其他创建日期。参见[测试轨道指南](https://support.google.com/googleplay/android-developer/answer/9845334?hl=en)和[新个人账号测试要求](https://support.google.com/googleplay/android-developer/answer/14151465?hl=en)。


### 白标/模板应用的账号、商店页与审核

2025-02-10 的[白标开发者最佳实践公告](https://support.google.com/googleplay/android-developer/answer/15931448)只有一个正文直链；目标指南有 11 个正文文本链接和 4 个示例图片链接，逐项摘要与访问状态见公告 11 子链接表。通用侧栏 30 项单独计数，不混入正文链接。实务上应把这条链当作四个检查面：

- **账号风险隔离：** Google 强烈推荐按客户或客户组采用分散账号，可由客户自行管理（unmanaged）或授权白标服务商保留管理权限（managed）。中心账号的所有应用会显示同一开发者资料；单个应用的问题也可能扩散至同账号其他应用。分散账号是强烈建议，不是普遍强制要求；金融、健康、VPN 和政府服务另须核对组织账号规定，见 Play Console 要求。
- **真实差异化：** 每个模板应用都应有独特描述、图标、图片和相关截图；说明真实可用的功能、区域差异和目标用户，截图须能在审核中重现。避免重复文案、堆关键词、未发布功能声明或仅替换品牌名；可用预填模板提高 Console 申报一致性，但仍要逐应用核实。见商店详情最佳实践与 Spam/功能性专题。
- **可审查和可用：** 提交完整可运行的应用，检查安装、启动、核心流程和第三方 SDK；提供长期有效的演示凭证、必要访问步骤及审核资源，不提交生产用户凭证。新个人账号的测试门槛与组织账号不同，应按账号类别核对。
- **审核和上线：** 官方建议审核期间冻结代码/内容变更并持续查看 Policy status。审核可能需数小时至 7 天，特殊情况更久；Managed publishing 帮助页建议至少预留一周，并说明新产品若要用该功能，强烈建议先发布到封闭测试轨道。该功能需要特定发布/商店权限，用于已上架应用的更新，首次发布不适用；它会暂缓大多数变更，但少数例外不受暂缓。白标服务商还可记录反复出现的问题和解决办法，作为客户发布前检查表。

其中“账号分散”“审核冻结”和使用 Managed publishing 属最佳实践建议；类别资格、账号资料、内容准确性、应用可运行、审核凭证及具体政策才是逐项核实的正式要求。

## 创建并准备版本

1. 在目标轨道创建 release。若先前版本仍有未完成发布，先完成 rollout，或在 Publishing overview 撤回/丢弃未发布变更。
2. 上传 Android App Bundle。官方指南说明，2021 年 8 月前创建的旧应用可能仍可在更新时使用 APK。首次发布时配置 Play App Signing。新应用可以在版本 rollout 到 Open testing 或 Production 前更改初始 app-signing key；发布后如需增强密钥，应按 Play Console 的 key-upgrade 流程办理，而不是把 upload-key reset 当成 app-signing-key 轮换。更换/轮换会影响既有测试用户、旧构建和依赖证书指纹的 API 服务。参见[Play App Signing](https://support.google.com/googleplay/android-developer/answer/9842756?hl=en)。
3. 检查 App bundle enhancements。Automatic protection 需要 Play App Signing 和 AAB；高级防篡改/设备检查只对部分合作伙伴开放，应先核实资格并在各轨道回归。它是可选保护能力，不是通用上架要求。参见[Automatic protection](https://support.google.com/googleplay/android-developer/answer/10183279?hl=en)。
4. 填写 Play Console 内部可见的 release name 和面向用户的本地化 release notes。每种语言最多 500 个 Unicode 字符；release notes 用来说明本次更新，不应用于促销或要求用户采取行动。新增支持语言时先配置翻译。
5. 检查 AAB/APK 权限。Play 在发布流程中评估权限；高风险/敏感权限可能要求 App content 中的 Permissions Declaration Form 和 Google Play 批准。应先最小化 manifest/SDK 权限，并与实际功能逐项比对。参见权限声明专题和敏感权限专题。

### 高风险权限可能阻塞整个应用的发布

若任何活动轨道中的 AAB 含有尚未完成声明的受限权限，Play Console 可能在 App content 显示警报。官方权限声明页说明，在解决前，其他应用变更（包括商店展示、价格和分发设置）也可能无法发布。可完成声明并获批，或移除该权限并重新上传适当构建。官方当前说明权限审核可能需要数周；通过 Publishing API 发布但权限尚未获批时可能报错，需先在 Play Console 网页界面完成声明/审核流程。

权限申报通常要求说明核心功能、权限用途和审查步骤，提供演示视频及受限功能的测试访问说明。仅提供专用测试账号凭证，不提供生产用户凭证。字段会因权限/应用情况变化，按 Console 当前表单填写。

### 提交前的 Play Policy Insights 检查

[Android Studio Play Policy Insights](https://developer.android.com/studio/publish/insights)以 lint 检查形式提示部分权限/功能可能涉及的 Play 政策、常见注意事项和官方来源。可在 **Code > Inspect for Play Policy Insights** 查看；CI 可添加 `com.google.play.policy.insights:insights-lint` 的当前稳定版作为 `lintChecks` 依赖。当前 Android Studio 文档（2026-10-01 更新）称，最新稳定通道和过去 10 个月发布的主版本及补丁受支持，当前最早支持 Panda 1。

这项功能的阶段记录要按日期理解：2025-06-11 博客介绍 Canary Beta；2025-12-11 官方博客随后称已向 Android Studio 开发者推出。当前 Studio 指南是安装/支持窗口和使用方法的优先来源。Play Console Help 的静态说明仍写着 Narwhal Release 3 和“initial launch”权限清单，与之后推广及现行 Studio 文档时间不同，故只作为初始覆盖的历史说明，不据此判定现时政策覆盖全集。2026-04-15 博客还预告联系人/位置相关提示，具体计划是 10 月 27 日启动 Console 预审检查；这与联系人声明提示（现行帮助页称 9 月开始）及精确位置申报表单（现行帮助页称预计 11 月开放）是不同节点，详见联系人与前台位置专题。

这些提示是预审辅助，不覆盖所有政策、不做最终应用审核，也通常没有自动修复；有些问题要通过产品设计、实现调整或 Play Console 声明解决。须打开对应政策全文核对，不能把 lint 无告警当成获批。项目也可使用已安装的 [Play Policy Insights Android Skills](https://github.com/android/skills/tree/main/play/play-policy-insights)（[本仓库专题](../play-policy-insights-skill/play-policy-insights-skill.zh-CN.md)）做源码审阅；它与 Android Studio lint、Console 声明互补，任何结论都要回到当前官方政策验证。

2026-04-15 的[官方政策更新博客](https://android-developers.googleblog.com/2026/04/giving-users-clearer-choice-and-everyone-a-safer-more-trusted-app-ecosystem.html)称，联系人/位置权限的 Play Console 预审检查计划于 **2026-10-27** 开始提供。通用[预审检查帮助页](https://support.google.com/googleplay/android-developer/answer/14807773?hl=en)解释检查流程，但未确认这组专属检查已上线。截至 2026-10-22 核对日，该计划日期尚未来到；届时需在实际 Console 核实开放状态和应用提示。申报提示、位置申报表单及正式生效日期见联系人与前台位置专题。

| Policy Insights 相关正文链接 | 关系与访问状态 |
| --- | --- |
| [Android Studio 和 Cloud services 兼容性](https://developer.android.com/studio/cloud-services/compatibility) | 当前链接跳转到 Android Studio 发布/更新页；2026-10-22 页面显示稳定版 Rabbit 1（2026.2.1）。工具支持版本会滚动变化，勿长期硬编码。 |
| [Google Play Policy Center](https://play.google/developer-content-policy/) | Lint 检查链接到现行政策中心；本库已有开发者政策双语专题。所有工具提示须回到正式条文核验。 |
| [Google Maven Repository](https://maven.google.com/web/index.html?q=com.google.play.policy.insights) | 用于解析 `com.google.play.policy.insights:insights-lint` 版本；Repository 页面已打开，具体版本会更新，应使用届时发布的版本。 |
| [Android Studio lint 指南](https://developer.android.com/studio/write/lint) | 正文已打开相关章节：可用 `./gradlew lint` 运行，输出 XML/HTML 报告；官方建议把 lint 加入 CI。该页说明的是通用静态检查机制。 |
| [Android Studio 报告问题](https://developer.android.com/studio/report-bugs) | 工具反馈入口已打开；可报告 IDE/检查器问题，不是 Play 审核申诉渠道。 |
| [2025-06-11 Beta 博客](https://android-developers.googleblog.com/2025/06/making-it-easier-to-build-safer-apps-google-play.html)、[2025-12-11 全面推广回顾](https://android-developers.googleblog.com/2025/12/building-safer-android-and-google-play.html) | 两篇博客正文均已打开；前者是 Canary Beta 历史，后者记述推出到 Android Studio 开发者。博客用于核对时间线，当前安装/版本要求以 Android Studio 指南为准。 |
| [Play Console Help：Policy Insights](https://support.google.com/googleplay/android-developer/answer/16297427) | 正文已打开，列出 Ads/Advertising ID 与 10 类敏感权限初始覆盖，但页面仍称 Narwhal Release 3；与更晚的 Studio 文档/推广回顾存在时序差异，不作为当前覆盖清单。 |

## 送审、托管发布与上线时间

准备完草稿后进入 Preview and confirm 并解决所有错误。存在错误时不能发布；警告或轻微问题可能允许继续。是否直接发布或进入待送审队列，取决于变更类型和 Publishing overview 状态。

[Publishing overview 指南](https://support.google.com/googleplay/android-developer/answer/9859654?hl=en)区分未送审、审核中和批准待发布的变更。保存变更不一定等于已送审；需要时须主动检查并点按 **Send for review**。开启 Managed publishing 后，多数变更会在审核通过后等待开发者手动发布；首次发布应用不能使用该功能。例外包括把既有分阶段 rollout 提高到 100%、更新 release notes、取消发布等。Google 表示处理可能需数小时至 7 天，特殊情况更久，并建议在提交与计划上线之间预留至少一周；这是计划建议，不是审核时限承诺。

### App、Update、Item 状态：定位发布卡点

官方[发布状态说明](https://support.google.com/googleplay/android-developer/answer/9859751?hl=en)把状态拆成三个层级：**App status** 表示应用整体对哪些用户可用；**Update status** 表示最近一次更新的处理状态；**Item status** 表示某个具体条目（例如 release、内容分级或商店实验）的状态。排查时应先确认卡在哪一层，再进入 Publishing overview 或相应条目，不要把某个 Item 的状态当成整款 App 的最终状态。

| 层级 | 代表状态 | 含义与操作 |
| --- | --- | --- |
| App | Draft、Internal/Closed/Open testing、Pre-registration、Production | 显示草稿、各测试轨道、预注册或正式发布的整体可用范围。 |
| App | No active releases、Unpublished | 没有当前有效发布（例如没有 rollout 或更新被拒）；或开发者主动取消公开，新用户不可发现，但既有用户仍可见，且更新仅面向既有用户。 |
| App | Removed by Google、Suspended by Google | Google 移除或暂停应用；页面均称应用不会被发现，需要分别按违规修复/申诉流程处理，暂停状态需成功申诉才可恢复。 |
| Update | No pending changes、Changes not yet sent for review、In review、Previous | 分别表示无待提交变更、变更尚未送审、审核中或历史有效更新。尚未送审的变更不会自动进入审核；需要时在 Publishing overview 点 **Send for review**。 |
| Update | Update rejected、App rejected | 均表示不符合政策或 DDA；**App rejected** 专指应用仍为 Draft、正在首次发布的情形。修正后重提，或在适用时申诉。 |
| Item | Draft、In review、Available、Previous、Update rejected/App rejected | 表示具体条目是否曾送审、审核中、当前可用、被后续版本替代，或随更新被拒。 |

首次发布草稿时，若审核摘要出现 **Errors summary**，须展开并解决阻止发布的错误；只有警告或轻微问题时仍可能发布，但官方建议先处理。标准发布会在获批后尽快处理上线；Managed publishing 适用于已有应用的更新，获批后由开发者决定何时发布。前者的审核可能延长至 7 天以上，不能把状态页当作固定时限承诺。

该状态页的直接关系：它链接到[开发者政策中心](https://play.google.com/developer-content-policy/)和[开发者分发协议](https://play.google.com/about/developer-distribution-agreement.html)，说明拒绝状态的规则基础；[准备并发布版本](https://support.google.com/googleplay/android-developer/answer/9859348?hl=en)、[审核与上线控制](https://support.google.com/googleplay/android-developer/answer/9859654?hl=en)和[更新或取消发布](https://support.google.com/googleplay/android-developer/answer/9859350?hl=en)是对应操作指南；[Play Console 用户权限](https://support.google.com/googleplay/android-developer/answer/9844686?hl=en)解释生产、测试轨道、测试者、Play Games Services 与组织私有应用等操作所需权限。Publishing overview 和权限设置本身需要账号访问；[Play Academy 上线课程](https://playacademy.exceedlms.com/student/path/4914)是补充培训，不是政策条款。该页面的 29 项相关帮助侧栏属于另一层目录，详见应用审核准备专题。

### Submission activity：按单次送审追踪审核记录

官方[About your submission activity](https://support.google.com/googleplay/android-developer/answer/17118609?hl=en)把每组送审变更记录成一个唯一 submission。详情包含 submission ID、提交来源（Play Console 或 Publishing API）、收到时间、状态更新时间和生命周期状态，可用于定位该次送审究竟包含哪些变更及何时流转。官方说明自 **2026-05-01** 起展示 submission 记录，并保留最多一年的历史。

| Submission 状态 | 官方含义与后续动作 |
| --- | --- |
| In review | Google 正在评估该次 submission；状态持续到必要审核完成。 |
| Ready to publish | 已通过所有审核；准备好后仍须手动发布。 |
| Published | 此 submission 已在 Google Play 上线。 |
| Rejected | 该组变更不符合政策且未发布；如果它是更新，最后一个已批准版本仍保持上线。 |
| Cancelled | submission 已撤回；可能是开发者手动移除变更、较新的 submission 取代仍在审核的旧 submission，或应用被封锁/暂停。 |

这些是**单次 submission 的流程状态**，与上文 App、Update、Item 的聚合状态相关但不等同。一个 submission 可能包含多项应用变更，故排查时先用 ID 和来源确认提交记录，再对照 Publishing overview 中各项变更。最近一次被拒的 submission 会链接到 [Policy status](https://support.google.com/googleplay/android-developer/answer/9842754?hl=en)，以查看政策问题与整改说明；该账号内逐应用页面的直接子链接和执法关系见执行处置与申诉专题。

| Submission activity 页面链接 | 用途与核验结果 |
| --- | --- |
| [Policy status](https://support.google.com/googleplay/android-developer/answer/9842754?hl=en) | 最新拒绝记录可跳转查看违规原因、下架/暂停状态及整改指引；正文已打开，子链接在执行处置专题登记。 |
| [Help Community](https://support.google.com/googleplay/android-developer/community?help_center_link=CJHrlAgSHkFib3V0IHlvdXIgc3VibWlzc2lvbiBhY3Rpdml0eQ&hl=en) 与[联系支持](https://support.google.com/googleplay/android-developer/gethelp) | 通用页脚支持入口；Community 返回 cache miss，联系支持转到账号内 Console。 |
| 29 项 Play Console Help 侧栏推荐 | 与应用审核准备专题中的发布帮助侧栏目录相同；这些是相关内容导航，不等同正文链接，页面自己的后代未全部递归。 |

该帮助页是审核记录使用说明，不构成额外的政策义务，也不会公开某个开发者账号的实际 submission 历史。获批、拒绝和最终上线状态须以相关账号中的记录为准。

该 Academy 路径公开列出五节入门课程。页面提供课程简介、时长和难度；开始学习按钮要求登录，因此这里记录的是公开课程目录，不把未登录的互动课件当作已读取政策全文。

| Academy 课程 | 公开简介与关系 | 访问状态 |
| --- | --- | --- |
| [Plan and prepare for app review times](https://playacademy.exceedlms.com/student/path/4914/activity/30051)（7 分钟，入门） | 说明部分应用类别（包括面向儿童的应用）可能接受扩展审核，并介绍审核流程和计划安排。 | 简介页可读；课件需登录。 |
| [Beginner's guide to publishing your app](https://playacademy.exceedlms.com/student/path/4914/activity/345650)（4 分钟，入门） | 介绍发布术语、要求、界面和顺利发布的实践。 | 简介页可读；课件需登录。 |
| [Introduction to release management](https://playacademy.exceedlms.com/student/path/4914/activity/7701)（8 分钟，入门） | 概述测试、发布和跟踪版本，以及 rollout 时间、节奏和设备范围控制。 | 简介页可读；课件需登录。 |
| [Roll out a release and publish an app](https://playacademy.exceedlms.com/student/path/4914/activity/28512)（7 分钟，入门） | 介绍为可信用户测试及向目标市场正式发布而创建和推出版本。 | 简介页可读；课件需登录。 |
| [Optimize your store listing with experiments](https://playacademy.exceedlms.com/student/path/4914/activity/345651)（10 分钟，中级） | 介绍通过商店详情实验比较图形与文案、配置实验并解读结果。 | 简介页可读；课件需登录。 |

### 自动预检：先排明显阻塞，再送正式审核

官方[提交前预检帮助页](https://support.google.com/googleplay/android-developer/answer/14807773?hl=en)说明，Play Console 会在 Publishing overview 的 **Changes not yet sent for review** 区域自动运行预检；该区域仅在最近一次送审后又有新变更时出现。检查开始后会显示进度估计。开发者可以在检查完成前点 **Send for review**，Play 会先完成检查；当前帮助页称所有检查会在 15 分钟内完成，多数更快。

预检包含政策完整性和技术质量两类信号，例如检查 App content 必填声明、应用必需信息、部分设备或 Android 版本上的高崩溃率，以及跨 Android 版本兼容性。问题可立即显示，解决路径可能是直接修改 Console 声明，也可能需要改代码、重新构建上传，或更新开发者网站。

| 预检结果 | Console 处理 | 审核含义 |
| --- | --- | --- |
| Critical issue / mandatory check | 必须解决后才能继续发布；例如缺少必填 App content 声明或应用资料。 | 不是可随意跳过的软警告。 |
| 其他可延期问题 | 若 Console 允许，可点 **Proceed anyway** 并选择原因；有时须确认已在 Console 外修复。理由会记入 Activity log；若不修复，问题可能在后续预检再次出现。 | 回答本身不直接决定审核结果，但问题若仍在、导致应用不可用或违反质量政策，正式审核仍可能拒绝。 |
| 检查仍在运行 | 可先发起送审，后台会继续检查；无严重问题时，检查结束后自动提交正式审核。 | 不能据此推断已绕过检查或已获批准。 |

预检不是正式审核，也不覆盖正式审核的全部检查；全部通过仍可能被拒。帮助页称大多数检查在 Play Console 网站运行，只有几乎即时返回的子集可通过 API 取得结果。允许选择 **Proceed anyway** 的账号，至少须有生产发布、测试轨道发布、测试者管理、商店信息管理或 Admin（全部权限）之一；具体权限详情见[Play Console 用户权限](https://support.google.com/googleplay/android-developer/answer/9844686?hl=en)。

#### 预检帮助页的直接目标与访问边界

| 直接目标 | 与预检的关系 | 核验结果 |
| --- | --- | --- |
| [准备应用更新／更新或取消发布](https://support.google.com/googleplay/android-developer/answer/9859350) | 更新需保持相同 package name 和签名，version code 高于现有版本；取消发布需接受最新 DDA、解决 App content 错误且关闭 Managed publishing。 | 正文已打开；完整操作见本页更新流程与应用审核准备。 |
| [Publishing overview](https://play.google.com/console/developers/app/publishing)、[Activity log](https://play.google.com/console/developers/activity-log)、[App content 页面](https://play.google.com/console/developers/app/app-content/overview) | 查看预检、选择提交/延期理由、检查声明。 | 三个均跳转账号登录；需有相应 Play Console 访问权限。 |
| [Ensuring app quality Help](https://support.google.com/googleplay/android-developer/answer/13965279?hl=en) | 解释应用质量对用户满意度、下载、留存和安全的作用，并链接 Android 质量四支柱及功能、欺骗、冒充、Spam、Ads 五篇现行政策。 | 正文和直接政策目标已打开/交叉核对；Android 工程建议及其与正式 Play 政策的边界见应用质量与设备形态专题。 |
| [Minimum Functionality／Functionality, Content, and User Experience](https://support.google.com/googleplay/android-developer/answer/9898783) | 正式政策举例说明应用崩溃、无基本用途、内容过少或体验失常可能被拒。 | 正文已打开；见 Spam、功能性与用户体验专题。 |
| [Play Console 权限说明](https://support.google.com/googleplay/android-developer/answer/9844686) | 说明选择 **Proceed anyway** 所需角色。 | 当前英文正文已打开；生产、测试、Tester、商店信息和 Admin 权限见用户权限专题。实际账号授权仍以 Console 为准。 |
| [Developer Program Policy](https://support.google.com/googleplay/android-developer/answer/17190352?hl=en) | 预检的政策覆盖依据。 | 旧目标重定向到当前合并版政策 [18258653](https://support.google.com/googleplay/android-developer/answer/18258653)，已在本库[开发者计划政策专题](../developer-program-policy/developer-program-policy.zh-CN.md)总结。 |
| [Managed publishing](https://support.google.com/googleplay/android-developer/answer/9859654) 与 [Play Academy 的审核计划课程](https://playacademy.exceedlms.com/student/page/357850-planning-for-app-reviews-what-happens-to-your-app-after-you-submit-it) | 前者控制获批后何时发布；后者讲解如何规划审核和预定上线。 | Help 正文已打开；课程简介可读，内嵌视频正文未转录，课程页中的 YouTube/短链接曾返回 cache miss。 |
| [预检示意图 1](https://lh3.googleusercontent.com/bwK06lFapeQaHhG62mHD7aM4a_X0Gbzc1Bf2tBGq5vg7MU1f4T8FjvUhgFT6koz7zzA%3Dw895)、[预检示意图 2](https://lh3.googleusercontent.com/keFAiRCGhPeN5Sf3ydHGhMpiMx5pjYrkr1cisESQ9tfLJ4OIhdLfcJOboAryid4zcA%3Dw895) | 界面示例图，不是政策条文。 | 图片链接可打开；无单独政策摘要。 |
| [Help Community](https://support.google.com/googleplay/android-developer/community?help_center_link=CN3lhwcSLkRldGVjdCBhcHAgaXNzdWVzIGVhcmx5IHdpdGggcHJlLXJldmlldyBjaGVja3M&hl=en) 与[联系支持](https://support.google.com/googleplay/android-developer/gethelp) | 通用讨论/支持入口。 | Community 返回 cache miss；联系支持跳转账号内 Console。 |

Academy 课程页的后代链接也逐项尝试：它嵌入的 [YouTube 视频](https://www.youtube.com/embed/OxhDgxoB5pQ?enablejsapi=1&v=OxhDgxoB5pQ)以及指向 [PolicyBytes 选题建议](https://goo.gle/policybytestopics)、[Developer Policy Center](https://g.co/play/policy)、[Play Console](https://goo.gle/playconsole)和[Made for India Academy 路径](https://g.co/playacademy/india)的短链/路径均发生 cache miss，故只记录可见的课程简介，视频和动态内容未摘要。帮助页的 29 项 Help 侧栏与应用审核准备专题中已登记的同一目录一致；各侧栏页面的所有后代仍未闭合。

更新版本可设置分阶段 rollout；首次 Production 发布没有 rollout 百分比选项。Production 的国家可用性作用于当前和未来生产版本；Open/Closed 测试轨道默认跟随生产国家，满足前提时可解除同步后单独设置；Internal 测试不受国家目标限制。国家依据用户的 Play 账号国家/地区，不按当前 GPS 判断。增加付费应用发行国家会自动加入当地价格；订阅价格需另行核对和设置。见[国家/地区投放指南](https://support.google.com/googleplay/android-developer/answer/7550024?hl=en)。

分阶段 rollout 只适用于更新，不适用于首次发布。用户随机入选，百分比不会自动增加；暂停后恢复仍影响同一批用户。暂停只阻止更多用户收到该版本，不会自动回退已收到版本的用户。扩大比例前要观察崩溃、ANR、性能和反馈；需要修复时通常创建新 release。参见[分阶段发布帮助页](https://support.google.com/googleplay/android-developer/answer/6346149?hl=en)。

## 发布指南正文直接链接清单

下表覆盖该指南正文中的直接目标。Console 账号内页面无法公开核验；课程只核实到入口。页面“已打开”不代表其子链接已全部递归完成。

| 正文目标 | 与发布流程的关系 | 核验状态 |
| --- | --- | --- |
| [Android App Bundles](https://developer.android.com/guide/app-bundle/)、[创建和设置应用](https://support.google.com/googleplay/android-developer/answer/9859152?hl=en)、[应用定价](https://support.google.com/googleplay/android-developer/answer/6334373?hl=en) | AAB 会由 Play 按设备生成优化 APK；创建设置页说明包名永久唯一、版本号与 target API 门槛及商品详情字段；定价按市场货币、当地税费和价格规则生成。定价页提示自 2025-10-27 起价格模板已解除关联，但其后文仍保留价格模板旧操作说明，故遇到模板操作应以当前 Console 为准。 | 三页已打开；只整理与发布相关的技术/操作内容，并记录价格帮助页内部的新旧说明冲突。 |
| [Prepare your app for review](https://support.google.com/googleplay/android-developer/answer/9859455) | App content 和审核材料。 | 英文正文已于 2026-10-22 打开；详见 Play Console 要求中的直接子链接表及 App content 申报矩阵。其 29 项侧栏推荐与正文直链区分。 |
| [Release apps to testing tracks 权限说明](https://support.google.com/googleplay/android-developer/answer/9844686) | 说明哪些 Play Console 角色可创建测试轨道版本。 | 已在用户权限专题核对：测试轨道发布权限不包含生产发布权限。 |
| [Publishing overview](https://play.google.com/console/developers/app/publishing)、[Open testing](https://play.google.com/console/developers/app/tracks/open-testing)、[Closed testing](https://play.google.com/console/developers/app/closed-testing)、[Internal testing](https://play.google.com/console/developers/app/tracks/internal-testing)、[Production](https://play.google.com/console/developers/app/tracks/production)、[Dashboard](https://play.google.com/console/developers/app/app-dashboard)、[All app bundles](https://play.google.com/console/developers/app/bundle-explorer-selector) 和 [Latest releases and bundles](https://play.google.com/console/developers/app/releases/overview) | 账号权限、各轨道、草稿/已发布构建和审核控制。 | 每个目标均尝试打开并跳转到 Google 账号登录；账号内状态与字段无法公开核验。 |
| [发布流程中的示意图标](https://lh3.googleusercontent.com/8Y3QmjrLbXy9SXyyHMfopmZ7h9zlMiRCJ1z5wUuXcqbbkczYqvDzPmW_SFzV64-nJw%3Dw18) | 正文“More”菜单的界面图标，不承载政策或操作说明。 | 图片资源已确认；不另作政策摘要。 |
| [新个人账号测试要求](https://support.google.com/googleplay/android-developer/answer/14151465?hl=en)、[测试轨道设置](https://support.google.com/googleplay/android-developer/answer/9845334?hl=en) | 生产门槛、测试者管理和轨道间版本资格。内部轨道最多 100 人；测试版评价不会计入公开评分；Internal 测试者不能同时接收 Open/Closed 测试版本。 | 新个人账号页的 14 个正文目标已逐项核对；重点内容、账号内入口及预发布报告限制见下方专题表。Android 测试资料仍有更深的非政策后代未遍历。 |
| [Play App Signing](https://support.google.com/googleplay/android-developer/answer/9842756?hl=en)、[Automatic protection](https://support.google.com/googleplay/android-developer/answer/10183279?hl=en)、[Play Games Sidekick](https://developer.android.com/games/pgs/play-games-sidekick) | 签名密钥、可选反盗版增强和游戏专属增强。 | 三页均已打开；只摘录发布相关条件。高级防篡改资格以 Console 通知为准。 |
| [反混淆/符号化崩溃堆栈](https://support.google.com/googleplay/android-developer/answer/9848633?hl=en) | 上传 mapping/debug symbols，支持上线后故障诊断；AAB 配合 Android Gradle Plugin 4.1+ 可自动带入符号文件，APK 场景通常按版本上传。 | 已打开；属于质量运营辅助内容，不是上架政策门槛。 |
| [敏感权限与 API](https://support.google.com/googleplay/android-developer/answer/16558241?hl=en)、[Permissions Declaration Form](https://support.google.com/googleplay/android-developer/answer/9214102?hl=en) | 权限审核、申报、演示视频和测试账号。 | 两页已打开；声明步骤、发布阻塞和延时已摘要，并链接到双语专题。 |
| [添加翻译](https://support.google.com/googleplay/android-developer/answer/9844778?hl=en)、[Managed publishing](https://support.google.com/googleplay/android-developer/answer/9859654?hl=en)、[分阶段发布](https://support.google.com/googleplay/android-developer/answer/6346149?hl=en)、[国家/地区投放](https://support.google.com/googleplay/android-developer/answer/7550024?hl=en) | 可本地化商品详情、图形素材和应用内商品；Console 提供部分商店内容机器翻译与 Gemini 应用字符串翻译，可预览/修改。其余三页分别管控送审/生效时间、灰度比例和市场选择。 | 四页已打开并整理发布相关内容；市场法规、付款资格和当地政策仍须查对应专题。 |
| [Play Academy 分阶段发布课程](https://playacademy.exceedlms.com/student/collection/260728-prepare) | 补充培训。 | 课程入口已打开；正文需要登录，未归档。 |

### 新个人账号测试要求与预发布报告直链

2026-10-22 重新打开[新个人开发者账号测试要求](https://support.google.com/googleplay/android-developer/answer/14151465?hl=en)。**仅适用于 2023-11-13 后创建的个人开发者账号**：在申请 Production 权限时，必须有至少 12 名测试者连续加入封闭测试满 14 天；这 12 人须在申请时仍连续 opt-in。测试者退出后再加入，其连续天数重新计算。达到人数/天数只让开发者提交生产权限申请，不保证获批；若参与人数或测试互动不足，Google 可要求继续测试。

| 轨道/阶段 | 条件与关系 |
| --- | --- |
| Internal testing | 可先用于小范围快速分发；不构成上述个人账号的生产权限门槛。 |
| Closed testing | 完成应用设置后可运行；适用账号须满足 12 人/14 天连续测试，才能申请 Production。 |
| Open testing | 该页称在获得 Production 权限后才开放。 |
| Production / Pre-registration | 个人账号完成测试要求前，这些 Console 功能保持禁用；Pre-registration 不是绕过闭测门槛的替代入口。 |

### 生产权限申请问答与审核

申请表分三部分：

1. **关于封闭测试：** 招募测试者的难易度、测试者是否使用了各项功能、测试行为是否接近预期真实用户（若不同需说明）、收集到的反馈及收集方式。
2. **关于应用/游戏：** 目标受众、价值主张、第一年预计安装量。官方说明这些答案不会公开展示，也不改变应用可见性或开发者计划资格。
3. **关于生产准备：** 根据测试反馈做了哪些改动，以及如何判断产品已准备好正式发布。

每部分必须点 **Next** 才保存；离开/Discard 会丢失未保存内容，最后必须点 **Apply**。审核通常 7 天以内，但有时更久；结果发给账号所有者。人数不足或互动不充分时可能要求继续封测。提交前还须自行核对内容/功能/变现政策、目标受众与内容分级、稳定性及可用审核凭证；正式审核不是替开发者排查违规的步骤。

### 封测最佳实践与 Play 预发布报告

该帮助页建议招募能代表未来目标用户、背景多样的测试者；给出明确的功能测试和反馈说明，设置可用反馈渠道，观察测试者是否实际使用关键功能，记录并归纳反馈，在封测中修复问题。它要求至少 14 天持续 opt-in，但没有规定一个固定的每日活跃次数或统一的“足够互动”数值。Android 测试指南建议覆盖功能、性能、无障碍和设备/API 兼容性，并组合本地/单元、集成及设备端测试；这些是工程实践，不是额外的 Play 测试者资格条款。

[Play 预发布报告](https://support.google.com/googleplay/android-developer/answer/9842757)可在设备实验室容量允许时，于上传 AAB/APK 或保存 Production 版本后自动运行。自动爬虫会安装应用并模拟输入、点击和滑动，主要发现稳定性、兼容性、性能和无障碍问题；[结果解读页](https://support.google.com/googleplay/android-developer/answer/9844487)明确提醒它不能保证发现所有问题，不能替代封闭测试、人工验收或真实设备回归。

| 预发布报告能力/边界 | 已核实要点 |
| --- | --- |
| 登录与测试路径 | 如需爬虫进入登录后内容，可提供专用测试账号；不建议提供正式账号凭证。自动填入主要支持标准 Android 控件，不保证覆盖 OpenGL 自定义控件或 WebView 登录。也可配置 Robo 脚本、游戏循环，并最多补充 3 个深层链接入口（每个额外爬取约 30 秒）。 |
| 报告语言与结果 | 首次报告后可选最多 5 种测试语言；报告按稳定性、性能、无障碍等类别展示错误、警告和轻微问题，并提供截图、视频、堆栈等可用细节。上传后通常约一小时可见结果，偶尔更久；官方建议超过两天仍未完成时重新上传触发新报告。 |
| 设备/场景限制 | 当前帮助页称设备在美国，支持手机、平板、Wear OS 和 Chromebook 等桌面设备，覆盖 Android 9+；不能直接在 Android Automotive OS 或 Android TV 上测试。测试不支持购买应用内商品，也不能运行无主启动 Activity 的启动器、Widget、键盘、表盘等应用；不能模拟 root 设备检查。地理围栏/国家校验可能需要测试专用代码路径。 |
| 结果边界 | 设备集合会变化；报告能辅助发现问题，不是发布通过证明。未命中问题不能推出没有兼容性、质量或政策风险。 |

### 新个人账号测试页：14 个正文直接目标

以下只计该页正文的 14 个链接目标；页脚社区/支持控件和 Help Center 推荐侧栏另计。登录后的 Console 页面无法公开验证账号内字段。

| 正文直接目标 | 与测试/发布门槛的关系 | 核验状态 |
| --- | --- | --- |
| [Production 页面](https://play.google.com/console/developers/app/tracks/production) · [Pre-registration 页面](https://play.google.com/console/developers/app/pre-registration) · [Dashboard](https://play.google.com/console/developers/app/app-dashboard) · [Testing feedback](https://play.google.com/console/developers/app/user-feedback/beta-feedback) · [Open testing](https://play.google.com/console/developers/app/tracks/open-testing) | 实际申请、生产/预注册入口、测试者反馈查看与开放测试入口。 | 5 个均转到账号登录；记录为 Console 操作入口，不推断具体账号状态。 |
| [Test apps on Android](https://developer.android.com/training/testing) | Android 测试总览及工程测试入口。 | 正文已打开；介绍一致测试的价值，链接到 Fundamentals、单元/仪器化/UI/截图/屏幕尺寸测试、样例与 Codelab；更深的实现资料未全部展开。 |
| [Fundamentals of testing Android apps](https://developer.android.com/training/testing/fundamentals) | 解释测试类型、范围、本地与设备端执行及可测试架构。 | 正文已打开；其 What to test、Testing strategies、Codelabs 等后代未全量遍历。 |
| [Use a pre-launch report](https://support.google.com/googleplay/android-developer/answer/9842757) · [Understand your pre-launch report](https://support.google.com/googleplay/android-developer/answer/9844487) | Play 自动预检配置与错误/警告结果解释。 | 两页正文已打开并摘要；预发布报告页还链接登录后的设置页、App content、Firebase、深链、符号化和测试明细等，相关高价值子页部分另有审计，完整技术后代仍未闭合。 |
| [Set up an open, closed, or internal test](https://support.google.com/googleplay/android-developer/answer/9845334) | 各测试轨道创建和测试者管理。 | 正文已打开并在本专题摘要主要轨道规则；其表单/Android 技术后代部分未遍历。 |
| [App quality](https://developer.android.com/quality) | Android 应用质量总览。 | 页面已打开；具体 Play 最低质量要求见应用质量与设备形态专题。 |
| [Google Play Developer Content Policies](https://play.google/developer-content-policy/) | Production 权限申请前应自行遵守的正式政策。 | 正文和后代入口已有[合并政策专题](../developer-program-policy/developer-program-policy.zh-CN.md)与政策链接图；此处不把审核准备说明误写成新增政策。 |
| [Google Play Console 网站](https://play.google.com/console/about/) · [Google Play Academy](https://playacademy.withgoogle.com/) | 通用开发者产品/培训入口。 | Console about 地址重定向至 Google Play 商业资源页；Academy 首页可读，具体课程可能要求登录；二者不是 Play 政策条文。 |

页面页脚还链接 Help Community 与 Contact us：社区可读但属于用户讨论，不是正式政策；支持入口转到需账号登录的 Console。该页面另有 29 项 Help Center 相关内容侧栏，**不属于上述 14 个正文链接**；侧栏中的政策目标与本文/应用审核专题已有交叉引用，但未把 29 项及其所有后代重新递归一遍。

#### 测试轨道指南：政策与设备分发后代

2026-10-22 重开[开放、封闭和内部测试设置指南](https://support.google.com/googleplay/android-developer/answer/9845334?hl=en)全文。该页是操作指南，不新增独立政策，但包含影响政策申报和可用范围的轨道差异：内部测试每个应用最多 100 名测试者；测试者可来自任意国家；付费应用的内部测试安装免费，但应用内购买通常仍须付费，除非将测试者加入 license testers；内部轨道测试版评价不进入公开评分。页面还提示内部测试可能不受标准 Play 政策或安全审查，并且活跃于内部测试轨道的应用可免于 Data safety 展示。此例外只针对内部测试，不应泛化到 Open、Closed 或 Production。

| 直接目标/后代 | 与轨道规则的关系 | 已核验内容与覆盖边界 |
| --- | --- | --- |
| [新个人开发者账号测试要求](https://support.google.com/googleplay/android-developer/answer/14151465?hl=en) | 生产权限的账号类型专属门槛。 | 仅适用于 2023-11-13 后创建的个人账号；至少 12 名测试者连续 opt-in 满 14 天，再申请 Production。完整表单、最佳实践及 14 个正文目标见上方专题表。 |
| [Google Play Data safety 表单](https://support.google.com/googleplay/android-developer/answer/10787469) | 哪些轨道必须填写 Data safety。 | Help 正文要求所有发布到 Play 的应用完成表单，包括 Closed、Open、Production；只活跃于 Internal testing 的应用可免。即便不收集数据，通常仍须填表并提供隐私政策；System services 和 private apps 另有例外。与[Data safety 双语专题](../data-safety/data-safety.zh-CN.md)对照。 |
| [查看和限制兼容设备](https://support.google.com/googleplay/android-developer/answer/7353455) | 设备目录、manifest 支持范围和 Console 排除规则。 | 目标设备由 manifest 与 Console exclusions 共同决定；排除规则优先于 manifest，并可按设备型号或属性规则设置。内部测试者不受设备排除规则限制。该页全文已打开；这是分发控制，不是设备/API 政策豁免。 |
| [Protected with Play](https://support.google.com/googleplay/android-developer/answer/13857328)（设备页的子链接） | 设备完整性检查与商店详情可见性。 | 现行 Help 将其描述为旧 App integrity 页的集中入口。可选的 Store listing device checks 会按设备完整性决定 Play 商店详情/安装资格，不要求应用集成 Play Integrity API，也不能阻止用户通过其他渠道或侧载取得应用；它与运行时 Play Integrity API、Automatic protection 是不同控制。正文已打开；账户配置及其余 API/支持后代仍需登录或继续审计。 |
| [应用许可测试和 Billing](https://support.google.com/googleplay/android-developer/answer/6062777) | 测试者名单与测试购买。 | Help 正文已打开；可用 Google 账号/Google Groups 管理许可测试者并测试应用内 Billing/订阅集成。实际名单设置需要 Play Console。测试轨道指南对“付费应用安装”和“应用内购买”作了区分。 |
| [按国家/地区分发](https://support.google.com/googleplay/android-developer/answer/7550024) · [分阶段发布](https://support.google.com/googleplay/android-developer/answer/6346149) · [发布准备](https://support.google.com/googleplay/android-developer/answer/9859348) | 市场范围、更新 rollout 和发布工作流。 | 三页已有双语摘要和独立访问记录：测试轨道国家可用性与 Production 默认同步，符合条件时可解除；Internal 不受国家限制；rollout 只用于更新且百分比不会自动扩大。更深操作后代仍部分未闭合。 |
| [预发布报告配置](https://support.google.com/googleplay/android-developer/answer/9842757) · [结果解读](https://support.google.com/googleplay/android-developer/answer/9844487) | 自动化技术/兼容性测试。 | 已有双语摘要及结果边界；不能替代真实测试，也不保证发现所有问题。Console 设置、Android/Firebase 技术孙链接和相关侧栏仍有未完成项。 |
| [Android 测试总览](https://developer.android.com/training/testing) · [Android App Bundles](https://developer.android.com/guide/app-bundle) · Managed Google Play/私有应用 | 实现、构建格式和组织测试者入口。 | Android/Firebase 内容是工程指导；Managed Google Play 的组织配置和私有应用发布在Play Console 要求专题另行整理。它们不会改变 Play 政策中各测试轨道的资格范围。 |
| [Android (Go edition) 低容量设备最佳实践（原始链接，现跳转到现行路径）](https://developer.android.com/docs/quality-guidelines/building-for-billions-device-capacity) | 设备排除页提供 Go 设备分发选项；Android 指南建议先优化主应用以适配低容量设备，而不是随意拆分体验。 | 现行目标页正文注明 Android Go 为 Android 8.1/API 27+、约 1 GB RAM 及以下；Android 指南最后更新于 2023-05-09，建议 app 包体小于 40 MB、PSS 内存不超过 90 MB（游戏 150 MB）、启动少于 5 秒，并检测 PIP/悬浮窗能力后优雅降级。指南建议优先优化同一个应用；若发布独立 Go APK，要求相应低 RAM feature 声明、API target 至少 26、版本号高于非 Go APK。上述是有日期的工程建议，不是现行 Play 上架门槛；采用前应复核。|

以上是已核验的高影响正文链接及设备页子链接，不代表该测试指南的全部正文锚点、页脚、Help 侧栏和技术后代已闭合。未公开 Console 路由、培训页和通用 API 目录继续按访问状态记录；本轮不从无法读取的账号页面推断字段。

#### Play 预发布报告页面的直接后代

沿着上表的[预发布报告配置页](https://support.google.com/googleplay/android-developer/answer/9842757)继续打开其正文链接。下表只总结这层直接后代中与测试、审核或发布准备有关的目标；Firebase、Android Developers 的技术目录仍有大量非政策文档，不把它们误称为 Play 要求。

| 预发布报告的子链接 | 与 Play 发布的关系 | 核验状态 |
| --- | --- | --- |
| [Understand your pre-launch report](https://support.google.com/googleplay/android-developer/answer/9844487) | 解释错误、警告、轻微问题、测试设备及稳定性/性能/无障碍报告；报告不能保证发现所有缺陷。 | 正文已打开并摘要；页面内部的 API/问题类后代未全递归。 |
| FAQ 锚点 | 回答运行时长、美国测试设备、国家校验、应用购买、设备形态和授权测试等边界。 | 锚点位于同一篇帮助页，不重复计为独立目标；相关问答已摘要在上文。 |
| [Prepare your app for review](https://support.google.com/googleplay/android-developer/answer/9859455) 与 App content 表单 | 提供审核凭证、隐私政策、广告/受众/权限等声明；这与预发布报告的测试账号入口可能共用资料，但属于不同控制点。 | Help 正文已打开并在审核准备/Console 要求专题总结；表单需登录。 |
| [Pre-launch report settings](https://play.google.com/console/developers/app/pre-launch-report/overview/settings) / [details](https://play.google.com/console/developers/app/pre-launch-report/overview/details) Console 页面；[Play Console](https://play.google.com/console/) | 设置测试账号凭证、Robo 脚本、游戏循环、语言及查看详细结果。 | Settings、Details 和 Play Console 均为账号内操作入口；公开浏览器无法读取账号字段，Console 首页跳转到 Google Play 商业介绍页。 |
| [Robo test (Android)](https://firebase.google.com/docs/test-lab/android/robo-ux-test) | Firebase Test Lab 的自动 UI 爬虫可重复模拟交互并输出日志、截图和视频；Robo Script 可控制路径。 | 正文已打开；这是工程测试能力，不是 Play 测试资格规则；SDK/工具后代部分未遍历。 |
| [Deep links guide](https://developer.android.com/training/app-links/create-deeplinks) | 说明 Intent filter、自定义链接、Web links 与已验证 App Links；报告的最多 3 个入口必须与应用路由相符。 | 正文已打开，页面最后更新 2026-10-01；进一步 API 参考和示例未全量遍历。 |
| [Firebase Game Loop guide linked from the Android page](https://firebase.google.com/docs/test-lab/game-loop) | 页面标题是 iOS Game Loop 指南，不能直接作为 Android 实现说明；Firebase Test Lab 首页另列 Android Game Loop 入口。 | 目标已打开并确认平台不匹配；应从其 Android 文档入口继续，不能照抄 iOS 步骤。 |
| [Firebase Test Lab](https://firebase.google.com/docs/test-lab/) · [Android Studio integration](https://firebase.google.com/docs/test-lab/android/android-studio) | 云端真机测试、仪器化测试、截图、`firebase.test.lab` 系统变量及 Gradle Managed Devices/分片。 | 两页正文已打开；Firebase 提醒 Test Lab 不适用于后端负载测试。工具及 CI API 子树仍部分覆盖。 |
| Firebase 相关直链：[Robo Script 指南](https://firebase.google.com/docs/test-lab/android/robo-ux-test)、[Game Loop](https://firebase.google.com/docs/test-lab/game-loop)、[Test Lab 总览](https://firebase.google.com/docs/test-lab/) 与 [Android Studio 集成](https://firebase.google.com/docs/test-lab/android/android-studio) | 解释自定义爬虫路径、游戏循环、设备实验室与仪器化测试；属于工程测试能力，不增加 Play 测试资格门槛。 | Robo、Test Lab 总览及 Android Studio 页面正文已打开；`game-loop` 当前页标题为 iOS，不能照搬为 Android 指南。技术工具和 CI 后代仍部分覆盖。 |
| [Android 深层链接指南（原始地址）](https://developer.android.com/training/app-links/deep-linking.html) | 预发布报告最多可追加 3 个入口，每个入口增加约 30 秒爬取；官方旧链接现跳转到 Create deep links 指南。 | 目标页已打开，记录了 Intent filter、自定义链接、Web links 与已验证 App Links；更深 API/示例未全遍历。 |
| [Get started testing for Android with Firebase Test Lab（旧链接）](https://developers.google.com/cloud-test-lab/best-practices) | 原锚文本涉及自动测试中的广告欺诈；旧链接现转到通用 Android Test Lab 入门页。 | 重定向目标已打开；没有取得独立的广告反作弊指南，不能把锚文本当作现行政策。 |
| [Upload deobfuscation or symbolication files](https://support.google.com/googleplay/android-developer/answer/9848633) | 将预发布/线上崩溃堆栈映射回源码，支持问题诊断。 | 本轮点击返回内部错误；既有发布流程专题含摘要，仍以该目标独立审计状态为准。 |

该帮助页正文还直接链接到 App content 凭证页；公开点击没有返回可解析的独立 URL，因此只记录目标名称和失败状态，不猜测账号内路由。正文 FAQ 是同页锚点，折叠/展开控件也不会产生新页面。帮助社区、Contact us 和 15 项相关内容侧栏单独看待；侧栏不是正文的政策要求，未逐项递归。上表中的 Android/Firebase 资料属于实现指南，非额外 Play 资格门槛。

### Play App Signing 与 Automatic protection：正文摘要和重要直接后代

[Play App Signing](https://support.google.com/googleplay/android-developer/answer/9842756?hl=en) 区分开发者保管的 upload key 与 Google Play 用于签署最终 APK 的 app signing key。两把密钥都应妥善保护；Google 管理 app signing key 时，丢失 upload key 可申请重置。启用 Play App Signing 也让 AAB 应用使用 Play 的发布增强功能。当前页面说明新应用默认采用 quantum-ready hybrid signing；Android 17/API 37 设备验证混合签名，旧设备继续使用经典签名。因此使用 OAuth、Maps、App Links 等服务时，要把 Play Console 中实际 app-signing fingerprints（适用时包括三把密钥的指纹）登记到 API 提供方和 `assetlinks.json`，不能只登记本地 upload key。变更 app signing key 前，应核对所有共享签名身份的应用、旧 Android 版本行为和依赖签名指纹的服务。

若 app signing key 泄露或需要更强算法，官方页面目前允许为 Android 17/API 37+ 用户申请年度密钥升级；升级后需更新 API 提供方指纹。Play Console 访问应为所有用户启用两步验证。自托管 Cloud KMS 是不推荐的特殊方案，会把签名操作和灾难恢复责任交还给开发者，部分 Play 发布增强可能不可用。

[Automatic protection](https://support.google.com/googleplay/android-developer/answer/10183279?hl=en) 的基础安装来源检查可在用户从未知渠道安装时引导其前往 Play。自动防篡改和 device check 仅对部分合作伙伴开放；该页面截至核对日列出资格门槛：每月消费支出至少 25,000 美元，或此前六个日历月每月消费支出均至少 20,000 美元；或者敏感类别应用 MAU 至少 100 万；或者参与 Google Play 项目（例如 Play Pass）。资格可能变化，以 Console 通知为准。功能要求 Play App Signing、AAB 和最低 API 24；基础保护离线可用，但 Play Store 长时间离线后，安装来源检查可能需要联网。device check 依赖 anti-tamper，并会代管商店详情可见性。页面还列出与 App Bundle code transparency 不兼容、Internal App Sharing 构建不附加保护等限制。启用后应在所有轨道测试启动、性能、崩溃和原生代码回调；如果应用依赖完整性保护，不应把未保护版本发布到开放测试或 Production。防篡改不能保证完全阻止破解。

| 直接后代 | 与签名/保护页的关系 | 覆盖状态 |
| --- | --- | --- |
| [APK Signature Scheme v3.2](https://source.android.com/docs/security/features/apksigning/v3-2)、[v3.1](https://source.android.com/docs/security/features/apksigning/v3-1) | 解释经典密钥轮换与 Android 17 混合后量子签名验证；是平台技术规范，不是额外 Play 政策。 | 两页均由 Play App Signing 正文链接；v3.2 已打开并总结迁移、回退与签名沿袭要求，v3.1 仅登记。 |
| [Android Studio signing guide](https://developer.android.com/studio/publish/app-signing)、[命令行构建与签名](https://developer.android.com/build/building-cmdline) | 指导生成 keystore、选择 upload key、上传签名及本地签名配置。 | Android Studio 签名指南已打开；原 Play Help 的 `keytool` 链接被 Google Search 错误接收并只显示搜索页，已改记为失效目标，并补充当前 Android 命令行构建说明。 |
| [Automatic protection 与反篡改配置](https://support.google.com/googleplay/android-developer/answer/10183279?hl=en)、[自定义反篡改保护](https://support.google.com/googleplay/android-developer/answer/17104169) | 前者说明开启、测试、资格、回退和自定义商店展示；后者配置客户端秘密保护和性能开销。 | Automatic protection 与自定义页面正文均已打开；账号内具体 Console 控件仍需登录验证。 |
| [Android App Bundles](https://developer.android.com/guide/app-bundle)、[App Bundle code transparency](https://developer.android.com/guide/app-bundle/code-transparency) | AAB 是自动保护的前置条件；code transparency 与自动保护不兼容，须先决定发布与验证方案。 | AAB 技术指南已在其他专题打开；code transparency 正文已打开并确认功能关系，其更深实现指南未全部展开。 |
| [Google Play Integrity and signing services](https://developer.android.com/google/play/integrity) | 汇总 Play Integrity、签名及保护相关开发者方案；可与完整性保护配合评估，但不等同于开启自动保护。 | 直接页面已打开；具体 API、Play Integrity verdict 和服务器集成指南未在本专题递归。 |
| [How app updates work](https://developer.android.com/google/play/app-updates) 与 [Internal App Sharing](https://support.google.com/googleplay/android-developer/answer/9844679) | 解释跨渠道更新和测试构建；Internal App Sharing 文件会用独立 IAS key 重新签名、不进入测试/正式轨道，一个链接最多供 100 人下载且 60 天过期；Automatic protection 不会附加到 IAS 上传。 | 两个目标均已打开；账号操作及其子链接仍需另行核查。 |
| [Cloud KMS key import](https://cloud.google.com/kms/docs/importing-a-key)、Play Developer API [`appsigning.enrollApp`](https://developers.google.com/android-publisher/api-ref/rest/v3/appsigning/enrollApp) 与 [`appsigning.rotateAppSigningKey`](https://developers.google.com/android-publisher/api-ref/rest/v3/appsigning/rotateAppSigningKey) | 仅适用于不推荐的自托管签名配置；配置 IAM、导入密钥并通过 API 注册/轮换。 | 三个页面均打开；Cloud KMS 目标重定向到 docs.google.com，API 方法页面已确认用途，IAM 与 KMS 后代没有逐项展开。 |
| [Play Games Sidekick](https://developer.android.com/games/pgs/play-games-sidekick) | 游戏可选增强；需结合 Play Games Services/Play Points 资格，建议小比例 rollout 观察稳定性、参与和收入。 | 正文已打开；Sidekick 的 SDK、任务、视频、奖励及配置后代仍有独立技术链未完整展开。 |
| [Play as you Download](https://developer.android.com/google/play/play-as-you-download)、[付费游戏免费试用](https://support.google.com/googleplay/android-developer/answer/16923846?hl=en)、[应用翻译与本地化](https://support.google.com/googleplay/android-developer/answer/9844778?hl=en) | 这些是 Play App Signing 解锁的产品增强：按首次文件访问模式后台下载资源；合资格付费游戏可提供 60 分钟试玩并由 Play 管理付费墙；Play Console 可管理商店文本、商品翻译和 Gemini 应用字符串翻译。它们是可选分发/商品功能，不是通用政策义务。 | 三个目标正文已打开并作范围摘要；免费试玩的支持设备、付费转化统计和 App Bundle/API 门槛已在来源页核实；本地化可用语言与账号控件仍会变化。 |
| Automatic protection 的其余正文直链：[Google 隐私政策](https://policies.google.com/privacy)、[Google Play Licensing](https://developer.android.com/google/play/licensing)、[Gradle native build](https://developer.android.com/studio/projects/gradle-external-native-builds)、[Android vitals](https://support.google.com/googleplay/android-developer/answer/9844486)、[Generated APKs API](https://developers.google.com/android-publisher/api-ref/rest/v3/generatedapks/list)、[Protected with Play](https://play.google.com/console/about/app-integrity/) | 分别关联遥测隐私、自动保护替代旧 Licensing 检查、native ABI 配置、发布后质量监控、下载未保护的 Play 签名 APK、Play 完整性设置入口。该 Help 页还直接链接轨道测试与发布流程。 | 隐私政策、Licensing、Gradle、Android vitals、Generated APK API 和 Protected with Play 落地页均已打开；指标口径、阈值和技术子页见应用质量与 Android Vitals 专题。轨道/发布流程已在本专题其他段落总结。Custom Store Listing 与 support 页面点击返回内部错误，只记为受限入口。 |
| [Google Cloud Security Whitepaper](https://cloud.google.com/security/overview/whitepaper)、APK Signature Scheme v4 链接、[IAM/KMS 角色](https://cloud.google.com/kms/docs/reference/permissions-and-roles)与 QPS 配额 | 说明密钥基础设施、签名版本和自托管 Cloud KMS 的细项。 | Play App Signing 正文直接包含这些链接；白皮书只作安全基础设施说明，v4 与 `keytool` 目标当前跳转到 Google 搜索页，三个 KMS 角色链接合并到同一权限文档，QPS 配额链接抓取失败。均不作为一般上架义务。 |

这批来源包含实现最佳实践，而非新增通用上架门槛。Play Console 的密钥状态、自动保护资格、各应用 API 指纹和受保护构建只能在相应开发者账号中确认；上表是当前直接关系摘要，不代表第三方技术网站的全部孙级链接已闭包。

该页另有通用 Help Center 侧栏推荐条目。它们不是正文中明确引用的发布步骤；仅在与政策或发布操作直接相关时纳入台账，不把整套帮助中心无限展开。

## 发布核对清单

- [ ] 应用资料、价格、App content、审核账号/演示材料、包名和 target API 已核实。
- [ ] 轨道选取正确；如适用新个人账号规则，完成 12 人连续 14 天封闭测试及生产权限申请。
- [ ] AAB、签名密钥、版本号、mapping/debug symbols、release notes 和各语言字符数已检查。
- [ ] 移除无用测试轨道和不必要权限；受限权限已申报/获批，给审核留出时间。
- [ ] 运行 Android Studio Play Policy Insights 或 CI lint 检查，并逐条核对对应的官方政策与 Play Console 声明。
- [ ] Publishing overview 中该送审的变更已主动提交；发布计划留有审核缓冲。
- [ ] 国家/地区、当地价格、rollout 百分比和监控计划已核对；根据稳定性再逐步扩大 rollout。

## 相关专题

- Play Console 要求
- 权限声明与审核
- 敏感权限与 API
- 商店详情与素材最佳实践
- 目标 API 级别要求

### 停止已全量发布的版本

官方[Halting a fully rolled-out release](https://support.google.com/googleplay/android-developer/answer/16285429?hl=en)说明：发现严重问题后，可在非 Internal testing 轨道停止已向 100% 用户发布的版本，阻止新用户安装及未处于该版本的用户更新到该版本；若有可用的先前全量版本，Play 会让该版本重新提供给新用户及符合条件的用户。修复问题后可按比例恢复发布。

限制：不能停止轨道上的第一个版本；若先前版本有政策违规，也不能作为替代版本。若新版本已发布较久或大量用户已更新，停止发布未必能消除已安装版本的影响。此功能是事故缓解，不等于保证把已安装新版本的用户强制降级。该帮助页此前在相关侧栏抓取中报错；2026-10-22 通过官方帮助搜索结果定位并核对正文。
## 仅出现在快照元数据中的官方 URL

下列 URL 写在快照 YAML 中，正文没有同一链接。中文源文件对这两条使用 `hl=zh-CN`。

- [白标最佳实践（`source_url_white_label_best_practices`）](https://support.google.com/googleplay/android-developer/answer/15884185?hl=zh-CN)
- [发布提示（`source_url_publishing_tips`）](https://support.google.com/googleplay/android-developer/answer/15191715?hl=zh-CN)
