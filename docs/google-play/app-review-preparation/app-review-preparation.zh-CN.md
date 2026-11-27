---
id: google-play.app-review-preparation
platform: google-play
language: zh-CN
authority: operational
status: current
kb_checked_at: 2026-10-24
review_due: 2027-01-24
regions: [global]
topics: [app-content, app-review, declarations, sign-in-details, publishing]
snapshot_id: play.app-review-preparation
snapshot_package: "GooglePlay-KnowledgeBase-2026-10-24-review.zip"
coverage_status: "detailed-summary"
source_url: "https://support.google.com/googleplay/android-developer/answer/9859455?hl=en"
effective_date: "operational preparation; 2026-10-27 Contacts/Location tool date kept separate from the 2027-01-27 policy preview; Watch Face Format requirement since January 2026 has passed"
---

# Play Console App content 与应用审核准备

> **导入说明（Google batch 7）。** 正文来自已经分开的 2026-10-24 Google Play 知识库快照（`play.app-review-preparation`，核对日 2026-10-24）的改写摘要，不是官方页面的逐字副本。英文官方页面是效力来源。`kb_checked_at` 是快照源文件记录的核对日；本次导入没有重新打开线上官方页面。文中“本知识库”“本库”“本地专题”等说法描述的是该快照库的覆盖范围，不是本仓库已经导入的页面。指向本仓库没有收录的专题、链接图、台账或 CSV 的相对链接改为文字提及。指向 Google batch 1–6 或本批十二个专题的相对链接改为本仓库文件。核对日 2026-10-24。两种语言文件引用的都是英文“Prepare your app for review”文章 `hl=en`。快照没有记录已核对的该文章中文官方页面。本仓库中文正文是编辑改写。所链接的 Shorts 指南中文 locale 不可用，其安全区域文档和提案演示文稿返回缓存未命中。这些限制属于 Shorts 专题，该专题未导入本仓库。中文源文件写明一条旧的高风险权限帮助路由重定向后无法读取，一条旧的 User Data 路由重定向后无法读取。现行规则留在敏感权限和 User Data 专题。快照记录联系人与位置工具检查安排在 2026-10-27。那是工具推出日期，不是政策截止日，而且通用帮助文章没有确认这些检查已经上线。它不是 2027-01-27 的权限预告。自 2026 年 1 月起，在 Wear OS 设备上安装表盘必须使用 Watch Face Format。该日期已经过去。2027-01-27 不是本页的规则。本页是 operational 的 App content 与审核准备说明。申报不替代开发者计划政策。公开文章不能核验登录后的 Console 状态。

## 范围和核对口径

依据官方 [Prepare your app for review](https://support.google.com/googleplay/android-developer/answer/9859455?hl=en)，于 2026-10-24 重新打开正文及导航。当前导航有 30 个编号项（含 Help Center 首页和本页），第 30 项为 Version codes；编号清单之后另有未编号的 [Developer Guide: Getting Started with Google Play Shorts](https://support.google.com/googleplay/android-developer/answer/18611720?hl=en)链接。该 Shorts 指南已打开，见Shorts 双语专题[Google Play Shorts](../google-play-shorts-creative-guidelines/google-play-shorts-creative-guidelines.zh-CN.md)。页面说明 App content 用于收集应用内容、目标用户、权限、数据安全和审核访问信息；实际表单取决于应用及账号状态。公开帮助页无法证明某个应用已完成申报、获批或满足当地法律。

本文是双语改写摘要，不是官方全文。请同时查看[开发者计划政策](../developer-program-policy/developer-program-policy.zh-CN.md)、[Play Console 要求](../play-console-requirements/play-console-requirements.zh-CN.md)和具体专题。

若要先按商店资料、功能兑现、审核访问、测试与拒审修复做整体自查，可从[上架准备与发布最佳实践](../app-publishing-readiness/app-publishing-readiness.zh-CN.md)开始；本页则展开 App content 声明和审核访问材料。

## App content 申报要点

| 申报项 | 官方页面说明 | 发布前核对 |
| --- | --- | --- |
| Needs attention / Actioned | 前者列待处理声明，开发者须在对应期限前完成；后者显示已处理项目。Google 可能继续检查，开发者应定期复核准确性。 | 每次功能、受众、数据流、广告 SDK 或权限发生变化后复查，不把“Actioned”视为永久合规证明。 |
| 隐私政策 | 请求敏感权限/数据的应用须在商店详情和应用内提供有效隐私政策；目标受众包含儿童时，无论是否访问个人或敏感数据，都须同时提供。政策应说明应用收集、使用、共享的数据及接收方，并与应用内披露相互一致。 | 检查公开 URL 可访问、内容适用于本应用、第三方 SDK/AI 数据处理及共享对象均已说明。 |
| 是否含广告 | 要申报是否含广告；第三方广告 SDK、横幅、插页和原生广告都计入。只在主菜单提供不干扰使用的“更多应用”入口，不一定属于此标签所指的广告。付费植入/促销仍须遵守当地法律。 | 逐个核对 SDK、广告位、广告墙、自家推广和广告标签；不把“不显示第三方广告”误判成“没有广告”。 |
| 审核登录信息 | 若全部或部分功能受到账号、会员、地区或其他认证限制，须提供审核人员进入所需功能的说明和凭证；页面说明最多可添加五组指令，可注明一次性密码、多重验证或多字段登录。 | 提供可用、可重复使用、审核地区可访问的凭证和步骤；密码/OTP 失效、仅本地可用或必须联系开发者都会阻断审核。登录要求详见[官方凭证指南](https://support.google.com/googleplay/android-developer/answer/15748846)。 |
| 目标受众和内容 | 必须准确申报目标年龄组。选择包含儿童会触发 [Families 政策](https://support.google.com/googleplay/android-developer/answer/9893335)及相关要求。 | 以实际内容、功能和营销呈现申报；同步检查儿童安全、SDK、广告和数据规则，见[年龄限制与儿童安全](../age-restricted-child-safety/age-restricted-child-safety.zh-CN.md)。 |
| 权限声明 | 上传 App Bundle 后，若应用请求高风险或敏感权限，可能需要完成 Permissions Declaration Form 并获得 Google Play 批准。 | 对照合并政策和[权限声明专题](../permissions-declaration/permissions-declaration.zh-CN.md)，核对 Manifest、合并产物、全部轨道、测试账号、视频证据和替代方案。 |
| 内容分级 | 每个应用都应完成内容分级问卷，避免应用以“未评级”状态留在 Play；评级需与实际内容和功能一致。 | 内容或功能改变影响问卷答案时重新提交；评级不替代儿童隐私、年龄门槛或广告适配审查。见[内容分级专题](../content-ratings/content-ratings.zh-CN.md)。 |
| COVID-19 声明 | 该帮助页仍列有 COVID-19 接触追踪/状态功能声明，并要求符合专门要求；相关功能还链接至审核团队预先通知表单。 | 这是页面仍列出的特定功能流程，不应泛化到普通应用；若确有此类功能，先在当前 Console 和官方帮助页核实现行流程。 |
| 新闻与杂志 | 按 Console 中的 News and Magazines 类别/描述条件判断是否属于该类应用，并完成自我声明。 | 与[新闻和杂志专题](../news-and-magazines/news-and-magazines.zh-CN.md)对照，检查来源、更新频率、联系信息、第三方来源披露及付费内容预览。 |

## 正文直接链接：目标页与关系

官方正文链接按目标去重；同一政策可能以多个锚文本出现。以下逐项保留可识别的目标，区分政策原文、Console 账号内页面和学习/支持资源。

| 正文目标 | 页面内容及其与审核的关系 | 本库状态 |
| --- | --- | --- |
| [Developer Program Policy / Google Play policies](https://play.google/developer-content-policy/) | 政策目录入口；指向与《开发者分发协议》共同构成的政策框架。目录中各专项政策需按功能逐项核对。 | 已有政策中心（[开发者政策中心](../google-play-developer-policy-center/google-play-developer-policy-center.zh-CN.md)）和[合并版政策](../developer-program-policy/developer-program-policy.zh-CN.md)。 |
| [High-risk or sensitive permissions](https://support.google.com/googleplay/android-developer/answer/16324062) | 原 Help 链路重定向后无法读取；当前权限要求应回到合并版政策和现行敏感权限专题，不从旧跳转页推断规则。 | 旧链接重定向不可读；现行规则见[敏感权限](../sensitive-permissions/sensitive-permissions.zh-CN.md)。 |
| [SMS / Call Log permissions](https://support.google.com/googleplay/android-developer/answer/9876150) | 公共抓取被 Google 验证页拦截；同一政策已有现行专题，覆盖允许用途、默认处理器、例外、替代方案和声明。 | 已有[短信和通话记录权限专题](../sms-call-log/sms-call-log.zh-CN.md)；以正文中的现行 URL 为准。 |
| [News and Magazines policy](https://support.google.com/googleplay/android-developer/answer/9935326) | 规定哪些应用须申报，以及文章来源、定期更新、联系信息、第三方来源和付费预览要求。 | 正文已打开；见[新闻和杂志专题](../news-and-magazines/news-and-magazines.zh-CN.md)。 |
| [User Data](https://support.google.com/googleplay/android-developer/answer/10144311) | 应用及集成 SDK 对用户数据收集、使用、共享、披露、同意和安全负责。 | 旧 Play 页面跳转不可读；现行政策和细化要求已纳入[用户数据专题](../user-data/user-data.zh-CN.md)。 |
| [Play Console App content](https://play.google.com/console/developers/app/app-content) | 个性化声明页面，需要账号及应用访问权限；公开网页不能核验某个开发者的状态或表单字段。 | 账号内页面，不推断状态；参见[Play Console 要求](../play-console-requirements/play-console-requirements.zh-CN.md)。 |
| [Ads policy](https://support.google.com/googleplay/android-developer/answer/9857753) | 广告内容、受众适配、欺骗/干扰性展示、儿童广告、位置数据和广告标识符规则均会影响申报真实性。 | 正文已打开；见[广告专题](../ads-and-advertising/ads-and-advertising.zh-CN.md)。 |
| [Contact support](https://support.google.com/googleplay/android-developer/gethelp) | 账号支持入口，不是公开政策正文；具体工单和账号通知仅在登录后可见。 | 不记录个案内容。 |
| [Sign-in details requirements](https://support.google.com/googleplay/android-developer/answer/15748846) | 说明提交可供审核人员使用的登录凭证、限制因素和操作说明；其三个正文直链已逐项打开并在下节记录。 | 正文和三个正文目标已检查；具体规则见本页“审核登录要求的直接后代”。 |
| [Console sign-in details](https://play.google.com/console/developers/app/app-content/testing-credentials) | 账号内填写审核凭证和访问说明的路由。 | 重定向到 Google 登录，无法公开核验。 |
| [Console Publishing overview](https://play.google.com/console/developers/app/publishing) | 账号内查看待处理变更并提交审核的路由。 | 重定向到 Google 登录，无法公开核验。 |
| [Control when changes are reviewed and published](https://support.google.com/googleplay/android-developer/answer/9859654) | 区分何时送审与何时发布；Managed publishing 控制已批准变更的发布时间，不能代替完成审核。 | 正文已打开并摘要，见[发布流程](../publishing/play-release-workflow.zh-CN.md)。 |
| [Families policy](https://support.google.com/googleplay/android-developer/answer/9893335) | 目标受众含儿童时适用；覆盖适龄内容、SDK/API 数据处理、儿童广告和社交功能等要求。 | 已有[儿童安全与 Families 专题](../age-restricted-child-safety/age-restricted-child-safety.zh-CN.md)。 |
| [Target audience and content settings](https://support.google.com/googleplay/android-developer/answer/9867159) | 说明 App content 中目标受众问卷的设置和年龄受众申报。 | 正文已打开；关联[内容分级与目标受众](../content-ratings/content-ratings.zh-CN.md)。 |
| [Academy for App Success](https://playacademy.exceedlms.com/student/catalog/list?category_ids=2558) | Families 学习目录公开列出课程标题和学习目标；课程主体须登录。 | 仅保存公开课程元数据，见政策课程目录（[Play Academy 政策课程](../play-academy-policy-courses/play-academy-policy-courses.zh-CN.md)）。 |
| [Android App Bundle](https://developer.android.com/guide/app-bundle) | 应用包发布格式和 Play 分发机制的技术资料；上传应用包会触发适用的权限审查流程。 | 技术材料，不是权限获批证明。 |
| [Permissions Declaration Form](https://support.google.com/googleplay/android-developer/answer/9214102) | 说明声明表单、审核和相关发布操作；敏感权限是否合格仍取决于政策用途和应用事实。 | 正文已打开；见[权限声明专题](../permissions-declaration/permissions-declaration.zh-CN.md)。 |
| [Content rating requirements](https://support.google.com/googleplay/android-developer/answer/9859655) | 同一目标由多个锚点指向，覆盖分级问卷、地区评级机构与应用内广告评级关系。 | 正文已打开；见[内容分级专题](../content-ratings/content-ratings.zh-CN.md)。 |
| [COVID-19 app requirements](https://support.google.com/googleplay/android-developer/answer/9889712) / [advance notice form](https://support.google.com/googleplay/android-developer/contact/adv_note) | 专门功能要求和审核团队预先通知表单；表单需动态填写，公开页不能证明提交状态。 | 两个目标已打开；按特定功能条件适用。 |
| [News and magazine app requirements](https://support.google.com/googleplay/android-developer/answer/10523915) | 新闻/杂志应用的资格和申报要求，与上方政策页及 Console 声明共同核对。 | 已有双语[新闻和杂志专题](../news-and-magazines/news-and-magazines.zh-CN.md)。 |
| [About the Families program](https://support.google.com/googleplay/android-developer/topic/9877766) | Families 计划资源入口，与政策正文不同；需根据应用是否面向儿童决定适用规则。 | 入口已打开；与[Families 专题](../age-restricted-child-safety/age-restricted-child-safety.zh-CN.md)相连。 |

## 审核登录要求：直接链接与相关页面

于 2026-10-24 重新打开 [Sign-in details requirements](https://support.google.com/googleplay/android-developer/answer/15748846?hl=en)。按该页正文链接，直接目标是 Play Console Requirements、登录后的 Console 凭证填写路由和 Play Academy 课程；`Prepare your app for review`（answer/9859455）是指向本登录要求页的上游 App content 指南，不是它的子链接。

登录凭证须始终可访问、可重复使用、在审核人员所在地有效，并持续保持无错误；若通常使用 OTP/两步验证，应提供可绕过动态验证且不会失效的凭证，否则无法审核并可能导致拒绝。提交英文凭证和说明；非字母数字 QR/条码应使用静态 URL 上传。用户自设 PIN 要给出清晰步骤；第三方账号登录须提供全部账号信息及操作步骤；地区限制须提供跨地区可用的主账号；即使没有登录页，若主要内容受订阅墙限制，也须提供允许审核人员完整、免费访问的说明或方式。

| answer/15748846 正文直接目标 | 与审核凭证要求的关系 | 本库状态 |
| --- | --- | --- |
| [Play Console Requirements](https://support.google.com/googleplay/android-developer/answer/10788890) | 提交前须提供有效演示账号、登录信息及审核资源；关键注意事项还明确不要提交过期登录信息。页面同时规定账号资料、组织账号类别、隐私政策、Data safety 和 Android 包名登记。 | 2026-10-24 重开全文；见[Play Console 要求专题](../play-console-requirements/play-console-requirements.zh-CN.md)。政策摘要与账号操作后代分别链接，递归覆盖仍未闭合。 |
| [在 Play Console 中填写登录详情](https://play.google.com/console/developers/app/app-content/testing-credentials) | 账号内录入审核凭证和访问说明的实际路由。 | 打开后重定向至 Google 登录；登录后字段及具体开发者账号状态无法公开核验。 |
| [Comply with Google Play's sign in details requirement](https://playacademy.exceedlms.com/student/activity/1955729) | Play Academy 15 分钟初级课程；公开简介列出可复用且不过期凭证、跨地区访问、英文说明、静态 QR/条码 URL 四项目标。 | 落地页于 2026-10-24 重开；课程显示 2026-06-05 发布，实际课程须登录，未将隐藏正文当作已读政策。 |

相关上游指南 [Prepare your app for review](https://support.google.com/googleplay/android-developer/answer/9859455) 说明 App content 填写步骤：最多添加五组说明；OTP/MFA/多字段登录的特殊步骤写入 “Any other instructions”。拒绝或移除后，可更新登录详情、保存，再到 Publishing overview 的 “Changes ready to send for review” 选择 Send for review；页面明确可直接重提，无需等待政策支持团队答复。该指南的正文、其他链接及目标状态见本专题上方。

该帮助页还展示 [Policy education and app requirements](https://support.google.com/googleplay/android-developer/topic/12798386?hl=en&ref_topic=2364761) 目录（32 个政策教育/应用要求条目，包含当前文章）；这是 Help 导航目录，不计入 answer/15748846 的三个正文目标。目录及其目标状态按共享导航台账分别追踪；未在本轮重新遍历全部目录后代。

## Play Console Help 导航：30 个编号项（29 个文章目标）

下表列出 `Prepare your app for review` 的 29 个文章目标；官方编号导航还将 Help Center 首页计为第 1 项，因此共有 30 个编号项。本页自身包含在 29 个文章目标中；每项均已点击或检索。表后另有一条未编号的 Shorts 指南链接（不是第 31 个侧栏项），它属于精选素材/内容审核指导，不是通用上架政策。动态 Console、目录和不可读目标单独标记；侧栏文章的更深链接尚未全部递归闭合。

| 侧栏目标 | 与审核/发布的关系及本库链接 |
| --- | --- |
| [Create and set up your app](https://support.google.com/googleplay/android-developer/answer/9859152) | 创建向导、永久包名、App Bundle/版本/目标 API、商店详情、签名条款和用户支持要求见独立[创建应用专题](../play-console-app-setup/play-console-app-setup.zh-CN.md)；Console 状态仍需账号登录。 |
| [App testing requirements for new personal developer accounts](https://support.google.com/googleplay/android-developer/answer/14151465) | 新个人开发者账号的闭测/生产权限门槛；见[Play Console 要求](../play-console-requirements/play-console-requirements.zh-CN.md)。 |
| [Device verification requirements for new developer accounts](https://support.google.com/googleplay/android-developer/answer/14316361) | 新账号设备验证流程；见Android 开发者验证[Android 开发者验证](../android-developer-verification/android-developer-verification.zh-CN.md)。 |
| [Set up your app on the app dashboard](https://support.google.com/googleplay/android-developer/answer/9859454) | Dashboard 作为设置与待处理事项入口；账号页面需登录。 |
| [Inspect app versions](https://support.google.com/googleplay/android-developer/answer/9844279) | App Bundle Explorer 中查看不同版本和设备配置；见[发布流程](../publishing/play-release-workflow.zh-CN.md)。 |
| [Prepare and roll out a release](https://support.google.com/googleplay/android-developer/answer/9859348) | 创建、检查和发布 release 的主流程；见[测试、审核与发布流程](../publishing/play-release-workflow.zh-CN.md)。 |
| [About your submission activity](https://support.google.com/googleplay/android-developer/answer/17118609) | 每组送审变更有独立 ID、来源、状态与时间戳；最多保留一年历史。拒绝记录可跳转 Policy status。详细状态、直接子页与支持入口见[发布流程专题](../publishing/play-release-workflow.zh-CN.md)。 |
| [Halting a fully rolled-out release](https://support.google.com/googleplay/android-developer/answer/16285429) | 发生严重问题时停止 100% 发布版本的继续安装/更新；排除内部测试轨道。旧版本只有在可作为回退版本时才重新提供。见下方[版本停止说明](../publishing/play-release-workflow.zh-CN.md)。 |
| [Detect app issues early with pre-review checks](https://support.google.com/googleplay/android-developer/answer/14807773) | Console 自动运行必填声明与质量检查；严重问题须先解决，可延期项目会记录理由，预检不等同正式审核。Google 另称联系人/位置专属预检计划于 2026-10-27 提供；该日期是工具上线计划，不是政策期限，且通用帮助页不能确认专属检查已上线。见[联系人/位置专题](../contacts-location-permissions/contacts-location-permissions.zh-CN.md)时间线；正文子链接和限制见[发布流程专题](../publishing/play-release-workflow.zh-CN.md)。 |
| [Publish your app](https://support.google.com/googleplay/android-developer/answer/9859751) | 解释 App、update、item 状态、拒绝状态和标准/Managed 发布；状态矩阵及其政策、发布、权限子链接见[发布流程](../publishing/play-release-workflow.zh-CN.md)。 |
| [Helpful tips to get your app published](https://support.google.com/googleplay/android-developer/answer/15191715) | 提交前的发布实践，已在公告资源表（[公告子链接目录](../google-play-announcement-resources/google-play-announcement-resources.zh-CN.md)）逐项分析正文直链。 |
| [Best Practices for White Label Developers](https://support.google.com/googleplay/android-developer/answer/15884185) | 白标应用账号隔离、原创价值、审核账号和发布实践；见公告资源表（[公告子链接目录](../google-play-announcement-resources/google-play-announcement-resources.zh-CN.md)）。 |
| [Update or unpublish your app](https://support.google.com/googleplay/android-developer/answer/9859350) | 应用更新、取消公开和可见性行为；须区分“取消发布”与仅因 target API 过旧而对新系统用户隐藏。 |
| [Control when app changes are reviewed and published](https://support.google.com/googleplay/android-developer/answer/9859654) | 控制送审和已获批变更的上线时间；见[发布流程](../publishing/play-release-workflow.zh-CN.md)。 |
| [Release app updates with staged rollouts](https://support.google.com/googleplay/android-developer/answer/6346149) | 分阶段向部分用户发布更新并监控；出问题时结合 halt rollout 处理。 |
| [Prompt users to update to your latest app version](https://support.google.com/googleplay/android-developer/answer/13812041) | Play Console Recovery 工具可按旧版本、国家/地区或 Android 版本提示用户升级；仅支持 Play App Signing + AAB，且新版本须覆盖所有含旧版本的轨道。Wear OS、Android TV、Automotive OS 发行版及若干保护/密钥配置不支持此 Recovery 功能。Android In-app updates 仅支持手机、平板和 ChromeOS，且不兼容 APK expansion 文件。见下方直链摘要。 |
| [Manage your store listings](https://support.google.com/googleplay/android-developer/topic/3450987) | 商店详情帮助主题目录；见[商店详情最佳实践](../store-listing-best-practices/store-listing-best-practices.zh-CN.md)。 |
| [Distribute your instant experience](https://support.google.com/googleplay/android-developer/answer/7381861) | Instant Experience 旧发布指南仍可见；项目状态与现行可用性须以Instant Apps 历史专题[Android Instant Apps](../android-instant-apps/android-instant-apps.zh-CN.md)为准。 |
| [Manage form-factor releases](https://support.google.com/googleplay/android-developer/answer/13295490) | Wear OS 旧移动轨道自 2023-09 起不能再更新，须迁移到专用轨道；TV 专用轨道可选但属最佳实践；Automotive 是否须专用轨道按类别而异；XR 专用轨道可选。Publishing API 轨道名采用 `wear:production`、`tv:beta`、`automotive:qa`、`android_xr:production` 等前缀格式。见下方直链摘要及应用质量与设备形态[应用质量与设备形态](../app-quality-and-form-factor-guidelines/app-quality-and-form-factor-guidelines.zh-CN.md)。 |
| [Add or test APK expansion files](https://support.google.com/googleplay/android-developer/answer/2481797) | APK 扩展文件的历史/技术帮助；对现代 App Bundle 流程的适用性需单独确认。 |
| [Google Play game services](https://support.google.com/googleplay/android-developer/topic/7071327) | 游戏服务帮助目录；项目登录与各 API 条款未在该目录页证明。 |
| [Using third-party SDKs](https://support.google.com/googleplay/android-developer/answer/10358880) | SDK 集成与开发者责任；见[SDK 要求专题](../sdk-requirements/sdk-requirements.zh-CN.md)。 |
| [Target API requirements](https://support.google.com/googleplay/android-developer/answer/11926878) | 年度 API 门槛和既有应用可见性；见[目标 API 专题](../target-api/target-api-level.zh-CN.md)。 |
| [Create and distribute a watch face](https://support.google.com/googleplay/android-developer/answer/13560201) | Wear OS 表盘的商店详情、测试轨道、分发条款、质量审核与生产发布步骤；自 2026-01 起所有 Wear OS 设备安装表盘须使用 Watch Face Format。见下方直链摘要及应用质量与设备形态[应用质量与设备形态](../app-quality-and-form-factor-guidelines/app-quality-and-form-factor-guidelines.zh-CN.md)。 |
| [Declare permissions](https://support.google.com/googleplay/android-developer/answer/9214102) | 权限声明入口；见[权限声明专题](../permissions-declaration/permissions-declaration.zh-CN.md)。 |
| [Prepare your app for review](https://support.google.com/googleplay/android-developer/answer/9859455) | 当前页面自身；App content 逐项要求见本页上文。 |
| [Request more time to complete a policy declaration](https://support.google.com/googleplay/android-developer/answer/15644220) | 仅当适用政策/Console 允许时申请延期；不能假设所有声明都有延期。 |
| [Manage store listing, experiments, and event graphics](https://support.google.com/googleplay/android-developer/answer/16386748) | Asset Library 可复用、裁切、搜索和按语言/类型/用途/标签筛选素材；它是 Console 工具说明，不是素材合规规则。素材要求见[商店详情最佳实践](../store-listing-best-practices/store-listing-best-practices.zh-CN.md)。 |
| [Version codes](https://support.google.com/googleplay/android-developer/answer/17367361) | `versionCode` 是每次发布递增的 32 位整数，Play 上限为 2,100,000,000；`versionName` 是面向用户的版本字符串。编号策略、多 APK 排序、设备过滤和 AAB 关系见版本号与 APK 分发专题[版本号与 APK 分发](../app-version-codes-and-apk-distribution/app-version-codes-and-apk-distribution.zh-CN.md)。 |

### 编号导航清单之后的 Shorts 指南链接

当前页的 30 个编号导航项之后另列 [Developer Guide: Getting Started with Google Play Shorts](https://support.google.com/googleplay/android-developer/answer/18611720?hl=en)。它已打开并纳入双语 Shorts 专题[Google Play Shorts](../google-play-shorts-creative-guidelines/google-play-shorts-creative-guidelines.zh-CN.md)，覆盖创意最佳实践、四类内容审核维度、技术规格和平台安全边界。这是额外的未编号指南链接，不计入侧栏编号，也不构成所有应用的上架要求。

## 操作性帮助页的直链摘要：发布轨道、恢复提示与素材

以下是审核准备页侧栏中最有操作价值的帮助页。它们解释 Play Console 和 Android 发布工具的使用方式，不应与 Developer Program Policy 的违规条款混为一谈。所列链接为这些目标正文中的政策/发布相关直链；通用页眉、帮助侧栏和账户内 Console 路由不作为政策义务。

| 帮助页 | 正文要点与直接关联链接 |
| --- | --- |
| [Manage different form-factor releases](https://support.google.com/googleplay/android-developer/answer/13295490) | Wear OS 旧移动轨道仍可能服务现有用户，但自 2023-09 起不能继续更新，须改用 Wear OS 专用轨道；TV 专用轨道是可选最佳实践，加入前须为所有商店详情上传 TV 截图并接受 TV 质量审核；Automotive 专用轨道按应用类别可能必需或可选，且 manifest 需声明 `android.hardware.type.automotive`；XR 专用轨道可选，但须声明 `android.software.xr.api.spatial` 或 `android.software.xr.api.openxr`，并仅面向支持该特性的设备。切分轨道后，发布自动化须改用新的[Publishing API 形态轨道 ID](https://developers.google.com/android-publisher/tracks)。相关审核依据见 [TV](https://developer.android.com/docs/quality-guidelines/tv-app-quality)、[Wear OS](https://developer.android.com/docs/quality-guidelines/wear-app-quality)、[Cars](https://developer.android.com/docs/quality-guidelines/car-app-quality) 质量指南及 [Cars 分发指南](https://developer.android.com/training/cars/distribute)。同一帮助页的“取消发布”步骤要求接受最新版 DDA、先解决内容分级/目标受众缺项，并关闭 Managed publishing。 |
| [Create and distribute a watch face](https://support.google.com/googleplay/android-developer/answer/13560201) | 流程包括应用和完整商店详情、Wear OS 测试轨道、截图与 AAB、接受 Wear OS 分发条款、质量审核，再发布到 Wear OS Production；建议先测试，更新版可设分阶段比例。页面直链至 [Watch Face Format](https://developer.android.com/training/wearables/wff)、表盘[预览素材](https://support.google.com/googleplay/android-developer/answer/9866151)、[表盘详情最佳实践](https://support.google.com/googleplay/android-developer/answer/13393723)、[Watch Face Studio](https://developer.android.com/training/wearables/wfs) 和 [Wear OS 质量指南](https://developer.android.com/docs/quality-guidelines/wear-app-quality)。Android Developers 现行指南注明，自 2026-01 起所有 Wear OS 设备安装表盘都要求 Watch Face Format；表盘分类/标签链接本次超时，未推测其内容。 |
| [Prompt users to update](https://support.google.com/googleplay/android-developer/answer/13812041) | Recovery 提示要求 Play App Signing 和 AAB；被提示的旧版本所在每条轨道都必须有可升级的新版本。可覆盖所有用户、指定国家/地区或 Android 版本；可以查看进度、扩大范围、编辑或取消，取消/编辑只影响尚未更新者。当前不支持 Wear OS、TV、Automotive OS 发行版，以及使用 Code Transparency、Play Automatic Protections 或 Key Upgrade 的应用；升级签名密钥后不能启动新的 Recovery。正文直链包括 [Play App Signing](https://support.google.com/googleplay/android-developer/answer/9842756)、[App Bundle](https://developer.android.com/guide/app-bundle)、App Bundle Explorer/Release overview 账户页，以及 [In-app updates](https://developer.android.com/guide/playcore/in-app-updates)。In-app updates 仅支持手机、平板和 ChromeOS，且不兼容 `.obb` APK expansion 文件；它须由开发者在未来版本内实现，可控制提示时机并采用较少打断的界面，不是对已安装旧版本的远程恢复功能。 |
| [Asset Library](https://support.google.com/googleplay/android-developer/answer/16386748) | 集中管理主/自定义商店详情、实验和活动素材；可从本地或 Drive 导入、将裁切结果另存为副本、按比例/语言/素材类型/使用位置/标签筛选。素材的强制格式与“高度建议”分别见[预览素材规则](https://support.google.com/googleplay/android-developer/answer/9866151)：该页明确强制要求不符合时可能导致素材移除或应用暂停；建议项不满足可能影响展示/推广机会，不必然影响商店详情页面。该素材页还关联 DDA 中 Brand Features and Publicity 授权说明。|
| [Version codes](https://support.google.com/googleplay/android-developer/answer/17367361) | 32 位 `versionCode` 每次发布递增，用于判断新旧；最大值 2,100,000,000，耗尽后无法再上传该应用的新 APK/AAB。该页直链至 [Multiple APKs and Version Codes](https://developer.android.com/google/play/publishing/multiple-apks)；完整的多 APK、设备筛选、App Bundle 和正文子链接分析见版本号与 APK 分发专题[版本号与 APK 分发](../app-version-codes-and-apk-distribution/app-version-codes-and-apk-distribution.zh-CN.md)。 |
| [Developer Guide: Getting Started with Google Play Shorts](https://support.google.com/googleplay/android-developer/answer/18611720?hl=en) | 新出现的创意/素材审核指南；总结 Play Shorts 的真实性、制作质量、平台安全、首页适宜性和上传规格，见双语 Shorts 专题[Google Play Shorts](../google-play-shorts-creative-guidelines/google-play-shorts-creative-guidelines.zh-CN.md)。英文正文已打开，中文 locale 本次不可访问；安全区域文档和提案演示文稿返回 Cache miss。 |

上表的素材格式、车载/Wear OS/TV 质量规则可能具有真正的审核或分发后果；其余 Console 路径与工程建议属于执行流程。页面中还存在需登录的 Console 控件、通用 Help 导航和非政策实现资料，逐页访问状态记在来源台账。旧版 [Instant Experience 发布帮助](https://support.google.com/googleplay/android-developer/answer/7381861) 虽仍可打开，但不能据此判断 Instant Apps 目前仍可新发；须按Instant Apps 历史专题[Android Instant Apps](../android-instant-apps/android-instant-apps.zh-CN.md)核对项目停用状态。

## 发布前核对清单

1. 按真实数据流、SDK、广告、年龄受众和功能完成 App content 声明；变更后复查已完成项目。
2. 对受限功能提供审核可用凭证、认证/地区说明和必要演示材料；至少用新设备或审核账号复测。
3. 隐私政策、Data safety、店铺详情、权限声明、受众、分级和实际构建保持一致。
4. 为有审核风险的上架计划预留审核时间；需要控制发布日期时使用 Managed publishing，但不要误以为它能绕过审核。
5. 对提交前预检、正式审核、拒绝修复、分阶段发布与全量停止分别保留状态证据；遇到账号级个案回到 Play Console。

## 覆盖限制

正文、30 个编号导航项和额外的未编号 Shorts 指南链接已登记；部分官方目标因登录、重定向或反机器人机制无法公开读取。导航目标的子页内链、帮助中心动态目录以及账户内表单仍未递归穷尽。此页帮助准备审核材料，不构成审核通过或应用合规结论。
