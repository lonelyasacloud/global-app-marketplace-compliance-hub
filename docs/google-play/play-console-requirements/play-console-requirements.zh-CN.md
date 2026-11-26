---
id: google-play.play-console-requirements
platform: google-play
language: zh-CN
authority: operational
status: current
kb_checked_at: 2026-10-24
review_due: 2027-01-24
regions: [global]
topics: [play-console, developer-account, package-registration, app-content, account-transfer]
snapshot_id: play.console-requirements
snapshot_package: "GooglePlay-KnowledgeBase-2026-10-24-review.zip"
coverage_status: "detailed-summary"
source_url: "https://support.google.com/googleplay/android-developer/answer/10788890?hl=en"
source_url_identity_verification: "https://support.google.com/googleplay/android-developer/answer/10841920?hl=en"
source_url_account_transfer: "https://support.google.com/googleplay/android-developer/answer/16909862?hl=en"
source_url_app_transfer: "https://support.google.com/googleplay/android-developer/answer/6230247?hl=en"
source_url_transfer_orders_api: "https://developers.google.com/android-publisher/api-ref/rest/v3/orders?hl=en"
source_url_transfer_order_refund: "https://developers.google.com/android-publisher/api-ref/rest/v3/orders/refund?hl=en"
source_url_voided_purchases: "https://developers.google.com/android-publisher/voided-purchases?hl=en"
source_url_voided_purchases_list: "https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.voidedpurchases/list?hl=en"
source_url_release_workflow: "https://support.google.com/googleplay/android-developer/answer/9859348?hl=en"
source_url_account_group: "https://support.google.com/googleplay/android-developer/answer/10627869"
source_url_service_fees: "https://support.google.com/googleplay/android-developer/answer/112622?hl=en"
source_url_lower_service_fees: "https://support.google.com/googleplay/android-developer/answer/16954621?hl=en"
source_url_payments_profile: "https://support.google.com/googleplay/android-developer/answer/3092739"
source_url_create_payments_profile: "https://support.google.com/googleplay/android-developer/answer/7161426"
source_url_supported_locations: "https://support.google.com/googleplay/android-developer/answer/9306917"
source_url_linked_services: "https://support.google.com/googleplay/android-developer/answer/6110967"
source_url_private_apps: "https://support.google.com/googleplay/android-developer/answer/9874937"
source_url_private_apps_verification: "https://support.google.com/work/android/answer/17266330?hl=en"
source_url_account_type: "https://support.google.com/googleplay/android-developer/answer/13634885"
source_url_zh: "https://support.google.com/googleplay/android-developer/answer/10788890?hl=zh-CN"
source_url_identity_verification_zh: "https://support.google.com/googleplay/android-developer/answer/10841920?hl=zh-CN"
source_url_account_transfer_zh: "https://support.google.com/googleplay/android-developer/answer/16909862?hl=zh-CN"
source_url_app_transfer_zh: "https://support.google.com/googleplay/android-developer/answer/6230247?hl=zh-CN"
source_url_transfer_orders_api_zh: "https://developers.google.com/android-publisher/api-ref/rest/v3/orders?hl=zh-CN"
source_url_transfer_order_refund_zh: "https://developers.google.com/android-publisher/api-ref/rest/v3/orders/refund?hl=zh-CN"
source_url_voided_purchases_zh: "https://developers.google.com/android-publisher/voided-purchases?hl=zh-CN"
source_url_voided_purchases_list_zh: "https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.voidedpurchases/list?hl=zh-CN"
effective_date: "requirements article effective 2026-09-30; target-API extension 2026-11-01 was still ahead of the 2026-10-24 review and is not 2027-01-27; fee rollout includes 2027-09-30 for other regions"
---

# Play Console 要求

> **导入说明（Google batch 7）。** 正文来自已经分开的 2026-10-24 Google Play 知识库快照（`play.console-requirements`，核对日 2026-10-24）的改写摘要，不是官方页面的逐字副本。英文官方页面是效力来源。`kb_checked_at` 是快照源文件记录的核对日；本次导入没有重新打开线上官方页面。文中“本知识库”“本库”“本地专题”等说法描述的是该快照库的覆盖范围，不是本仓库已经导入的页面。指向本仓库没有收录的专题、链接图、台账或 CSV 的相对链接改为文字提及。指向 Google batch 1–6 或本批十二个专题的相对链接改为本仓库文件。英文要求文章于 2026-10-24 重新打开。中文源文件把要求文章、身份核验、账号转移、应用转移和若干 Developer API 路由记为 `hl=zh-CN`。身份核验一节写明当时可读的是英文帮助页，中文 URL 未能稳定打开。本仓库中文正文是编辑改写。中文开篇写核对日 2026-10-23，YAML 的 `reviewed_on` 是 2026-10-24。这些快照日期不是政策变更。要求文章自 2026-09-30 起生效，与快照记录的合并版开发者计划政策日期相同。截至 2026-10-24 的核对，年度目标 API 截止日 2026-08-31 已经过去。受影响的应用可从 Console 警告申请延期到 2026-11-01。该延期日在核对日仍未到来。它是目标 API 日期，不是 2027-01-27 预告。本页记录的费率推出日是：EEA、英国和美国 2026-06-30；澳大利亚和日本 2026-09-30；韩国 2026-12-31；其他地区 2027-09-30。2021 年 15% 费率页是历史材料。2026-12-31 和 2027-09-30 的费率日期都不是 2027-01-27 的权限预告。官方账号所有权功能自 2026-05-27 起必须使用，该日期在核对时已经过去。公告中的“至少 30 天”与这个功能切换日保持分开。标注为 Preview: Play Console Requirements 的 `answer/17125096` 会重定向到本文，不是另一份未来政策。本页是 operational 的 Console 说明。它不替代开发者分发协议或开发者计划政策。Android 与 Play Developer API 材料是 implementation note。D-U-N-S 查询页不是 Play 政策页。

## 来源与版本

- 官方文章：[Play Console 要求](https://support.google.com/googleplay/android-developer/answer/10788890)
- 该页面当前版本标注自 2026-09-30 起生效；与其交叉引用的合并版政策见[开发者计划政策条目](../developer-program-policy/developer-program-policy.zh-CN.md)。
- 用户提供的两个 URL（一个含默认语言/访问参数，另一个显式含 `hl=en`）解析为同一篇文章；本条目使用不含追踪参数的规范链接。
- 核对日期：2026-10-23
- 文章说明“政策摘要”和“关键注意事项”只是概览，若与完整政策冲突，以完整政策为准。

## 正文直链与导航关系审计（2026-10-24）

我重新打开了英文[Play Console 要求](https://support.google.com/googleplay/android-developer/answer/10788890?hl=en)正文，并逐项核对正文链接、同页“Account Transfers”链接和 Help 导航。表内状态描述目标页本身；访问、摘要和子链接审核分别记录在来源链接台账（快照：`SOURCE_LEDGER.md`，未导入本仓库）与逐 URL 审计表（快照：`source-page-audit.csv`，未导入本仓库）。

| 正文直接目标 | 与本文关系 | 目标页状态及本地覆盖 |
| --- | --- | --- |
| [Google Play 上展示的信息](https://support.google.com/googleplay/android-developer/answer/10841920?hl=en) | 解释已验证开发者资料中哪些信息会向用户展示。 | 正文已打开；见身份核验段和开发者验证专题。 |
| [选择开发者账号类型](https://support.google.com/googleplay/android-developer/answer/13634885?hl=en)、[Financial Services](https://support.google.com/googleplay/android-developer/answer/9876821?hl=en)、[Health app categories](https://support.google.com/googleplay/android-developer/answer/13996367?hl=en) | 组织账号门槛及金融、健康服务分类。 | 三页正文均已打开；金融和健康分类另有专题及政策交叉链接。 |
| [Android VpnService API](https://developer.android.com/reference/android/net/VpnService) 与 [VPN Service policy](https://support.google.com/googleplay/android-developer/answer/16558241?hl=en) | 区分技术 API 与 Play 政策条件；获准使用 VpnService 的应用须登记为 Organization。 | API 参考和现行敏感权限政策均已打开；API 内容是技术语境，不会单独授予 Play 批准。 |
| [D-U-N-S 查找/服务入口](https://service.dnb.com/home) | 组织账号资料与 Dun & Bradstreet 记录保持一致。 | 外部 D&B 落地页已打开；不是 Google Play 政策页，也不能替代 Console 身份核验。 |
| [审核登录详情](https://support.google.com/googleplay/android-developer/answer/15748846?hl=en) | 受账号或地区限制的应用须提供审核人员可用的账号、步骤和资源。 | 正文已打开；见审核准备和发布流程专题。 |
| [Android developer verification 总览](https://developer.android.com/developer-verification?hl=en)、[Play 包名登记帮助](https://support.google.com/googleplay/android-developer/answer/16984799?hl=en) | 提交前登记包名；总览说明平台机制，Help 页说明 Play Console 操作。 | 两页均已打开；登记流程与密钥证明见开发者验证专题[Android 开发者验证](../android-developer-verification/android-developer-verification.zh-CN.md)。 |
| [Developer Program Policy](https://play.google.com/about/developer-content-policy/) 与 [Families policy](https://support.google.com/googleplay/android-developer/answer/9893335?hl=en) | 应用、广告网络、分析服务和第三方 SDK 都要符合完整政策；受众含儿童时附加 Families 要求。 | 政策中心和 Families 正文已覆盖；旧政策中心 URL 会转到当前中心。 |
| [Developer Distribution Agreement](https://play.google.com/intl/ALL_us/developer-distribution-agreement.html) | 开发者还须履行分发协议。 | 此次从本页点击时抓取器返回内部错误；现行 DDA 已由独立专题全文核对，不将此次失败说成 DDA 未读。 |
| [正式转移开发者账号所有权](https://support.google.com/googleplay/android-developer/answer/16909862?hl=en) 与 [转移单个应用](https://support.google.com/googleplay/android-developer/answer/6230247?hl=en) | 分别处理整个账号的所有权变更与应用迁移。 | 两页正文已打开，并在本专题后文分开总结；不得用非正式方式买卖或租用账号。 |
| [2 分钟文章调查](https://google.qualtrics.com/jfe/form/SV_9YPSYrwjw03d7cG?Source=10788890) | 帮助文章反馈。 | 目标要求 JavaScript；问题表单未读取或提交，不属于政策义务。 |

页面中的 `full policy` 是当前文章自身的同页链接。两处重复出现的政策中心/包名登记链接保留在链接图中，但目标按 URL 去重。文章底部的[帮助社区](https://support.google.com/googleplay/android-developer/community?help_center_link=CJrAkgUSGVBsYXkgQ29uc29sZSBSZXF1aXJlbWVudHM&hl=en)和[联系支持](https://support.google.com/googleplay/android-developer/gethelp)是动态问答/账号专属支持入口，不作为正文政策链接计数；社区只读到动态落地页，联系入口转入登录后流程。

### Enforcement 目录与预览别名

本文当前可见的 Enforcement Help 导航有四个同级页面：[Policy Coverage](https://support.google.com/googleplay/android-developer/answer/10146128?hl=en)、[Enforcement Process](https://support.google.com/googleplay/android-developer/answer/9899234?hl=en)、[Managing Policy Violations and Appeals](https://support.google.com/googleplay/android-developer/answer/9899142?hl=en) 和本文自身。另从 [Enforcement 目录](https://support.google.com/googleplay/android-developer/topic/9877468?hl=en&ref_topic=9858052)核到“see violations”指向[举报违规](https://support.google.com/googleplay/android-developer/answer/1085703)，而“managing a violation”打开[Manage policy violations 目录](https://support.google.com/googleplay/android-developer/topic/3453554?hl=en)。该目录列出 11 个目的页，已在[执行处置专题](../enforcement-and-appeals/enforcement-and-appeals.zh-CN.md)逐项关联。

Enforcement 目录中的 [Preview: Play Console Requirements](https://support.google.com/googleplay/android-developer/answer/17125096) 已实测重定向到本页 `answer/10788890`，所以它是预览别名，不是独立政策。此前审计里把“32 个侧栏目标”和“一页超时”挂在本页名下的记录已更正：当前正文的 Enforcement 导航为四个同级页；32 项 `Policy education and app requirements` 导航实际显示在[Payments Help](../payments/payments-and-subscriptions.zh-CN.md) `answer/10281818`，不是本页。该帮助页的目录后代仍按独立目标逐项管理，不混入本文正文链接数。

## 开发者账号和资料

Google Play 提供个人和组织两类开发者账号；选择账号类型并完成账号及关联资料验证后，部分已验证信息会显示给用户。以下类别的开发者在创建账号时必须选择组织类型：

- 金融产品或服务（例如银行、贷款、股票交易、投资基金、加密货币钱包或交易所）；
- 健康应用（例如医疗应用和人体受试者研究应用；详见[健康应用与 Health Connect 专题](../health-apps-and-health-connect/health-apps-and-health-connect.zh-CN.md)）；
- 获准使用 `VpnService` 类的应用；
- 政府应用，包括由政府机构开发或代表政府机构开发的应用。

账号资料须准确，包括法定名称和地址；组织账号通常须提供 D-U-N-S 编号（政府组织适用例外）；联系邮箱和电话；适用时展示在 Google Play 上的开发者邮箱和电话；适用的付款方式；以及关联的 Google 付款资料。组织账号资料应保持最新，并与 Dun & Bradstreet 资料一致。

### 开发者身份信息核验

[开发者身份信息验证](https://support.google.com/googleplay/android-developer/answer/10841920?hl=zh-CN)把用户可见资料与 Google 内部联络资料分开：所有开发者都须验证展示在 Play 上的开发者邮箱；组织账号还须验证展示的开发者电话号码。另须验证 Google 用于联系账号所有者的邮箱和电话，这组内部联络方式不会显示给 Play 用户。更改电话或邮箱后通常须重新验证。

身份核验依赖绑定的 Google 付款资料。付款资料未验证时，个人账号通常需提交政府身份证件；组织账号通常需提交 D-U-N-S 编号、政府身份证件和组织正式文件。已知政府机构可申请 D-U-N-S 例外；D-U-N-S 申请本身免费。身份证明文件必须与付款资料一致，能否接受哪些文件按国家/地区变化。组织账号需先完成网站验证，个人账号需先完成设备验证，之后才能验证相应电话号码；韩国个人账号另有公开电话号码要求。开发者可在个人截止日前 60 天开始完成验证；若资料无法验证，开发者资料和应用可能从 Play 移除，验证完成前也可能无法重新发布。

当前可读到的是英文版身份帮助页；本次中文 URL 未能稳定打开。上面是英文原文的双语改写要点，不代替 Console 实际待办和本地区证件清单。

## 提交应用前

开发者须提供准确的应用信息和元数据，上传隐私政策并填写“数据安全”部分，提供有效的演示账号/登录资料及审核所需资源（例如二维码）。还须按 Android 开发者验证要求在 Play 管理中心注册应用软件包名称。应用应提供稳定、易用且响应良好的体验；应用本身以及广告网络、分析服务和第三方 SDK 都须符合《开发者计划政策》。若目标受众包含儿童，还需遵守家庭政策。开发者仍须自行核对《开发者分发协议》和全部适用政策。

### App content 申报与审核材料

官方[Prepare your app for review](https://support.google.com/googleplay/android-developer/answer/9859455)将 App content 作为维护应用安全、政策合规和法律申报的入口。字段会按应用功能和适用政策显示；每次功能、数据、受众或商店信息发生变化后，应重新检查。

| 申报/材料 | 核心检查点 | 官方说明 |
| --- | --- | --- |
| 隐私政策 | 在 Play Console 和应用内提供可访问、适用于该应用的隐私政策；与应用内披露一起说明数据访问、收集、使用、共享、安全、保留和删除。儿童受众应用即使不处理敏感数据也须提供。 | [User Data policy](https://support.google.com/googleplay/android-developer/answer/10144311) |
| 广告 | 准确声明是否含广告，包括广告 SDK、横幅、插屏、原生/赞助内容及 house ads；该声明产生商店“含广告”标记，不等于其他商业内容声明。广告也必须适合应用受众和内容分级。 | [Prepare for review](https://support.google.com/googleplay/android-developer/answer/9859455)、[Ads policy](https://support.google.com/googleplay/android-developer/answer/9857753) |
| 审核访问权限 | 若应用或其功能受账号、会员、地区或其他认证限制，提供可用登录凭证、OTP/MFA 步骤和访问说明；审核期间保持凭证可用。 | [Sign-in details for app review](https://support.google.com/googleplay/android-developer/answer/15748846) |
| 目标受众与内容 | 按真实用户群选择年龄段；只要受众包含儿童即触发 Families 要求，儿童广告还涉及自我认证 SDK/中立年龄屏幕等条件。 | [Target audience and content](https://support.google.com/googleplay/android-developer/answer/9867159)、[Families policy](https://support.google.com/googleplay/android-developer/answer/9893335) |
| 权限声明 | 高风险/敏感权限（如 SMS/Call Log）可能要求 Permissions Declaration Form 并获批；声明应说明核心功能需要，代码、商店描述、隐私披露与实际用途一致。 | [Permissions Declaration Form](https://support.google.com/googleplay/android-developer/answer/9214102)、[Sensitive permissions](https://support.google.com/googleplay/android-developer/answer/10208820) |
| 内容分级 | 每个应用都须完成 IARC 分级问卷；内容或功能变化影响答案时重新提交。未评级应用不允许在 Play 上架。应用广告不应明显高于应用内容的成熟度。 | [Content Ratings](https://support.google.com/googleplay/android-developer/answer/9898843) |
| 数据安全与删除 | 每个已发布应用均须准确申报应用及 SDK 的数据收集、共享、处理和安全实践；仅内部测试轨道的应用有例外。支持应用内建号的应用还须提供应用内删除路径和网页删除请求资源，并回答 Data safety 删除问题。 | [Data safety form](https://support.google.com/googleplay/android-developer/answer/10787469)、[Account deletion](https://support.google.com/googleplay/android-developer/answer/13327111) |
| 类别专属申报 | 新闻/杂志、健康、金融功能、COVID-19 接触追踪、儿童安全等功能可能显示单独申报或通知要求；不要因未看到字段就推定无需遵守对应政策。 | [Prepare for review](https://support.google.com/googleplay/android-developer/answer/9859455)、[Health apps](https://support.google.com/googleplay/android-developer/answer/16679511)、[News/Magazine](https://support.google.com/googleplay/android-developer/answer/10523915) |

### App content 审核页的直接子链接

我于 2026-10-22 打开并核对了英文版 [Prepare your app for review](https://support.google.com/googleplay/android-developer/answer/9859455?hl=en) 正文。政策目标与登录后 Console 目标分开记录；右侧 Help Center 的“相关内容”推荐不是正文直接链接，不混入下表。

| 正文直接目标 | 与审核入口的关系 | 当前核验与本地关联 |
| --- | --- | --- |
| [Developer Program Policy](https://play.google.com/about/developer-content-policy/) | App content 用于收集政策和法律申报；应用还受完整政策约束。 | 已有[政策合并版](../developer-program-policy/developer-program-policy.zh-CN.md)专题；分发协议见[独立专题](../developer-distribution-agreement/developer-distribution-agreement.zh-CN.md)。 |
| [Sensitive permissions and APIs](https://support.google.com/googleplay/android-developer/answer/16558241) 与 [SMS/Call Log permissions](https://support.google.com/googleplay/android-developer/answer/10208820) | 说明高风险/敏感权限用途，可能触发声明、审核和审批。 | 目标已打开或由对应[敏感权限](../sensitive-permissions/sensitive-permissions.zh-CN.md)和[短信/通话记录](../sms-call-log/sms-call-log.zh-CN.md)专题覆盖；子页后代仍未穷尽。 |
| [User Data policy](https://support.google.com/googleplay/android-developer/answer/10144311) | 说明隐私政策、应用内披露、数据处理和 SDK 数据实践的基础要求。 | 正文已打开并纳入[用户数据专题](../user-data/user-data.zh-CN.md)。 |
| [Sign-in details for app review](https://support.google.com/googleplay/android-developer/answer/15748846) | 受登录、会员、地区或其他认证限制的功能须提供审核访问资料。 | 正文已打开：凭证须长期有效、可重用、跨地区可用并以英文提交；最多可加 5 组说明。详见发布流程页。 |
| [Target audience and content](https://support.google.com/googleplay/android-developer/answer/9867159) 与 [Families policies](https://support.google.com/googleplay/android-developer/answer/9893335) | 准确申报年龄组；只要受众包含儿童便可能适用 Families 要求。 | 两页正文已打开并与[儿童安全专题](../age-restricted-child-safety/age-restricted-child-safety.zh-CN.md)交叉核对。目标受众表单要求先完成广告声明、审核访问说明和隐私政策。 |
| [Permissions Declaration Form](https://support.google.com/googleplay/android-developer/answer/9214102) | 高风险/敏感权限可能要申报并获 Google Play 批准。 | 正文已打开并纳入[权限声明专题](../permissions-declaration/permissions-declaration.zh-CN.md)。 |
| [Content Ratings](https://support.google.com/googleplay/android-developer/answer/9898843)、[ratings authorities](https://support.google.com/googleplay/android-developer/answer/9859655) 与问卷说明 | IARC 为应用分配当地适用内容分级；新应用与活跃应用均须完成，内容变化后更新。 | 9898843 正文已打开并摘要；9859655 曾打开，详细整理仍排队。未评级应用可能从 Play 移除。 |
| [COVID-19 guidelines](https://support.google.com/googleplay/android-developer/answer/9889712) 与 [advance notice form](https://support.google.com/googleplay/android-developer/contact/adv_note) | App content 帮助正文仍列 COVID 接触追踪/状态申报及通知入口。 | 两页均已打开。COVID 更新页标注 2023-10-25，并称带健康功能/健康数据的 COVID 应用适用 Health Apps 政策；因此旧字段与更新说明可能不一致，需以当前 Console 字段和现行健康政策核实，不能照搬旧提示。 |
| [News & Magazines](https://support.google.com/googleplay/android-developer/answer/9935326) 与 [Requirements for news and magazine apps](https://support.google.com/googleplay/android-developer/answer/10523915) | 识别新闻/杂志应用并完成专属声明。 | 两页正文已打开并纳入[新闻与杂志专题](../news-and-magazines/news-and-magazines.zh-CN.md)。 |
当前 Prepare your app for review 页面有 30 个编号导航项（含 Help Center 首页），并在编号清单后另列一个未编号 Shorts 指南链接；这两类导航均不是审核正文中的政策链接。逐项关系和目标状态见[审核准备专题](../app-review-preparation/app-review-preparation.zh-CN.md)。

App content 的广告声明、隐私政策、登录详情、年龄组、权限和内容分级等表单区块是文章描述的 Console 功能，不都对应独立的正文超链接。实际表单需开发者登录；公开抓取无法确认具体账号当前显示的字段、截止期或提交状态。广告具体要求见[广告与推广专题](../ads-and-advertising/ads-and-advertising.zh-CN.md)。

Play Console 的“Needs attention/Actioned”显示待处理和已处理申报；即使曾通过审核，也要定期复核并保持答案准确。

### 申报期限延期

[Request more time to complete a policy declaration](https://support.google.com/googleplay/android-developer/answer/15644220) 说明：只有 Google 指定的部分复杂申报可申请延期；在 Play Console **App content** 对应声明中选择“Request additional time”、选择原因并提交。获批后新期限会显示在该声明的 Timeline 中。每项政策可申请的延展时长固定，且并非所有声明都提供此选项；已完成或不适用的申报通常不会显示入口。延期只延后完成时间，不免除申报或合规要求，也不应被当作自动批准。

该帮助页的正文直链包括登录后的 [App content](https://play.google.com/console/app/app-content/summary) 与 [Prepare your app for review](https://support.google.com/googleplay/android-developer/answer/9859455)；两者关系、其他申报和审核子链接见上方 App content 表。此延期页另有 27 项 Help Center 侧栏推荐；它们不是正文直链，未计入本页延期操作范围。Console 表单和每个应用的资格/新期限需登录账号确认。

### 新个人开发者账号的测试门槛

- **生产权限：** 2023-11-13 后创建的个人开发者账号，在申请生产权限前须对应用运行封闭测试；至少 12 名测试者连续选择加入满 14 天，然后在 Play Console 回答测试、应用设计和生产准备度问题。测试者退出后重新加入会重新计算连续天数。组织账号不适用这项特定门槛。
- **设备验证：** 新个人账号须通过 Play Console 手机应用验证拥有真实 Android 设备访问权。官方页面要求非 root 的实体 Android 手机/平板，系统为 Android 10 或更高版本。
- 来源：[App testing requirements](https://support.google.com/googleplay/android-developer/answer/14151465)、[Device verification requirements](https://support.google.com/googleplay/android-developer/answer/14316361)。要求可能按账号类型和创建日期变化。

设备验证帮助页的正文步骤只链接登录后的 Play Console Home；实际执行还要从网页版账户所有者页面扫描二维码，在 Play Console 手机应用中选择同一开发者账号并验证。该页有 29 项 Help Center 侧栏推荐，均与正文链接分开登记；账户任务与验证结果需登录检查。

### 2026 年 target API 当前期限

截至 2026-10-24，Google Play 的年度 target API 门槛已于 2026-08-31 到期：新应用和更新通常须 target Android 16/API 36；Wear OS 和 Android Automotive OS 为 API 35；Android TV 和 Android XR 为 API 34。既有应用为保持在更新系统设备上的新用户可见性，最低目标按类型分别为：一般应用 API 35、Wear OS API 34、Android TV API 33、Android Automotive OS API 32L、Android XR API 34。只有收到相应不合规警告的受影响应用，才可从 Play Console 警告/问题详情申请延期至 **2026-11-01**；以账号通知和[官方 target API 要求](https://support.google.com/googleplay/android-developer/answer/11926878)为准。Android 官方[迁移指南](https://developer.android.com/google/play/requirements/target-sdk)概述各版本行为变化、权限/后台/存储调整、SDK 兼容性和回归测试；其所链的完整技术文档未在本知识库逐页展开。

## 账号所有权转移

详细双语整理见[账号所有权转移专题](../account-ownership-transfer/account-ownership-transfer.zh-CN.md) · [English](../account-ownership-transfer/account-ownership-transfer.en-US.md)。本节保留其与 Play Console 要求、账号资格和单个应用迁移之间的关系。

账号所有权变更必须走 Google Play 的正式转移流程。转让方和接收方对转移期间的账号行为都负有责任。通过第三方市场等非正式渠道买卖、租用或取得账号不允许。若只需把应用转到另一个账号，应使用独立的应用转移流程，而非转移整个开发者账号。

### 所有权转移指南的当前流程与资格

Play Console 帮助页[转移开发者账号所有权](https://support.google.com/googleplay/android-developer/answer/16909862?hl=en)已于 2026-10-24 重新完整打开。只有现有账号所有者可在 **Users and permissions → Manage → Make account owner** 指定现有用户。组织账号需说明接收方属于同一组织还是新实体：同一组织可复用现有账号资料；不同实体须选择付款资料用于身份验证；同组织转移时，接收方还必须拥有相关付款资料管理员权限。个人账号接收方须选择或创建只用于身份验证的付款资料。等待期后，设置向导还会收集组织类型/规模、组织电话和可选网站、联系人姓名、经一次性验证码验证的邮箱/电话，以及开发者联系电话和邮箱；Google 可能另行要求身份文件，文件不受支持会被拒绝。

| 资格/环节 | 当前帮助页说明 |
| --- | --- |
| 可直接转移 | 组织开发者账号，以及不通过应用变现的个人账号，在提交资料并完成适用身份验证后可转移所有权。 |
| 不适用直接流程 | 正在变现应用的个人开发者账号目前不能直接变更所有者；须创建新开发者账号，再单独转移应用。 |
| 七天安全等待 | 提交后现有所有者和全体应用管理员会收到邮件、团队成员会收到 Console 通知；随后有 7 天安全等待期，任何账号用户均可取消。等待期后接收方通过邮件完成设置；接收方开始最终流程后，其他用户不能再取消。 |
| 可能阻止转移 | 账号未完成验证或不合规、付款资料更改/账号类型变更待处理、上传密钥重置或应用转移正在进行、接收方已拥有另一个 Play Console 账号。 |
| 原所有者无法联系 | 当前不能使用自助转移；须通过 Play Console Help 或公开在线表单联系支持。 |

这属于账号级操作流程；它不等同于[单个应用转移](https://support.google.com/googleplay/android-developer/answer/6230247?hl=zh-CN)。2026-04-15 的[政策公告](https://support.google.com/googleplay/android-developer/answer/16926792)列出新账户转移政策；其[官方博客](https://android-developers.googleblog.com/2026/04/giving-users-clearer-choice-and-everyone-a-safer-more-trusted-app-ecosystem.html)明确说自 **2026-05-27** 起账号所有权变更必须使用该官方功能，凭证共享及第三方市场买卖账号不允许。公告笼统所述“至少 30 天”与博客写明的功能切换日是两种不同时间口径；本库将 2026-05-27 作为所有权变更流程要求日期，账号状态和资格仍须在登录后的 Console 核验。

| 所有权转移指南的正文直接链接 | 关联与核验状态 |
| --- | --- |
| [开发者身份信息验证](https://support.google.com/googleplay/android-developer/answer/10841920) | 所有权设置向导所链接的资料与身份验证要求；正文和地区文件/联系信息子页已有独立整理。 |
| [将应用转移至其他开发者账号](https://support.google.com/googleplay/android-developer/answer/6230247?hl=zh-CN) | 是变现个人账号等不能直接转移所有权时的另一流程；正文与转移影响已在本页下文整理。 |
| Play Console Help 与在线联系表 | 账号所有者失联时的支持路线；需要登录或提交账号信息，公开页面不能核实请求资格与处理状态。 |

### 单个应用转移：前置条件和影响

[将应用转移到其他开发者账号](https://support.google.com/googleplay/android-developer/answer/6230247?hl=zh-CN)的正文已打开。官方要求原账号与目标账号均有效、要转移的应用符合政策，并先下载将来仍需使用的批量导出、付款和收入报告。目标账号需提供注册交易 ID；支持团队会在目标开发者审核接受后处理请求，页面当前说明通常在 2 个工作日内回复。

| 转移内容/例外 | 操作影响 |
| --- | --- |
| 会随应用转移 | 用户、下载统计、评分/评价、内容分级、商品详情、订阅及 Android 开发者验证关联的软件包名/签名密钥；政策申报和 App content 中过去提交的信息也可能一并转移。 |
| 不会随应用转移 | 批量导出、估算销售和收入报告；促销活动；开放/封闭/内部测试组和内部分享配置；集成服务权限/关联设置。封闭测试组需在新账号重建，测试用户可能要重新加入。 |
| 订单与退款 | 转移前建立的订单保留在原账号；要退款时回原账号操作，或使用 Google Play Developer API。 |
| Play App Signing | 上传密钥可在目标账号请求更换；应用签名密钥可为新安装应用申请升级。实施前需核对密钥轮换影响。 |
| 付费应用/IAP | 目标账号需有有效付款资料。默认货币变化时，含 IAP 的应用可能先取消发布以核价；付费应用价格可能自动调整。 |
| 外部服务 | 逐项更新 Google Analytics、Google Cloud 项目、Firebase、广告 SDK（包括 AdMob）和其他集成；待处理翻译项目应先完成。Google Play 企业专用应用需满足组织关联要求，iframe 创建的专用应用不能转移。 |
| 15% 服务费账户群组 | 若账号属于不同群组，转移应用当年收入可能同时计入转出和转入群组。该说明依赖账号群组/费用计划，费用条款应以当前政策和 Console 为准。 |

### 应用转移页面的直接子链接

| 子页面/目标 | 与转移的关系 | 核对状态 |
| --- | --- | --- |
| [Developer Policy Center](https://play.google.com/developer-content-policy/) | 转移前原账号和应用必须遵守现行政策。 | 页面已打开，政策中心另有双语专题。 |
| [2021 年 15% 服务费层级](https://support.google.com/googleplay/android-developer/answer/10632485) 与 [Account Group](https://support.google.com/googleplay/android-developer/answer/10627869) | 解释群组、关联账号和收入合并；2021 文章是历史说明，不能代替当前费用规则。 | 两个正文均已打开并在下节展开；当前分地区费率须看 [Service fees](https://support.google.com/googleplay/android-developer/answer/112622?hl=en) 与 [2026 lower-fee changes](https://support.google.com/googleplay/android-developer/answer/16954621?hl=en)。 |
| [Play App Signing](https://support.google.com/googleplay/android-developer/answer/9842756) | 上传密钥和应用签名密钥管理/轮换。 | 目标页已打开；密钥替换影响需按应用当前签名配置核对。 |
| [付款资料](https://support.google.com/googleplay/android-developer/answer/3092739) | 转入含付费应用或 IAP 的账号需有有效付款资料。 | 目标页已打开并在下节展开；付款账户的实际状态需账号登录确认。 |
| [Analytics 用户/权限帮助（旧 UA）](https://support.google.com/analytics/answer/1009702)、[GA4 用户和访问权限](https://support.google.com/analytics/answer/9305788)、[Cloud 访问控制](https://docs.cloud.google.com/compute/docs/access) 与 [Google Cloud Console](https://console.cloud.google.com/) | 转移后重授外部服务和项目访问权限。旧 UA 页面现标记为 Legacy，并引导至 GA4。GA4 按账号/媒体资源层级授予用户与角色，权限可向下继承；管理员负责添加和修改用户，部分删除操作需要账号管理员。Cloud IAM 支持预定义、基本和自定义角色，资源权限可继承；应按最小权限原则优先授予适当资源层级。Console 本身跳转至登录页，具体项目及成员权限须在目标账号核验。 |
| [将开发者账号关联到 Google 服务](https://support.google.com/googleplay/android-developer/answer/6110967)、Firebase 项目解除关联/重连 | 更新 Analytics、Google API 和 Firebase 集成关系。 | Play 帮助页已打开并在下节展开；Firebase 具体项目权限/操作需要目标项目权限，逐项目确认。 |
| [发布专用应用](https://support.google.com/googleplay/android-developer/answer/9874937) | 企业专用应用有组织关系和可转移性限制。 | 页面已打开并在下节展开；iframe 创建的专用应用不可转移。 |
| [Google Play Developer API](https://developers.google.com/android-publisher) → [Orders 资源](https://developers.google.com/android-publisher/api-ref/rest/v3/orders?hl=zh-CN) → [orders.refund](https://developers.google.com/android-publisher/api-ref/rest/v3/orders/refund?hl=zh-CN)；[Voided Purchases API](https://developers.google.com/android-publisher/voided-purchases?hl=zh-CN) → [purchases.voidedpurchases.list](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.voidedpurchases/list?hl=zh-CN) | 将历史订单退款操作与退款/拒付后的撤销核对分开：`orders.refund` 可退款一次性购买或订阅，超过 3 年的订单不可退款；`revoke=true` 会立即终止项目访问和后续订阅扣款，已消耗的一次性商品仍须由应用处理。Voided Purchases API 仅返回需要撤销的订单；开发者退款若未设置 revoke，不会出现在该列表。 | API 根页、Orders 资源、退款方法、Voided Purchases 总览和 list 方法均已打开/核对（2026-10-23）；需有对应开发者 API/财务权限。旧版 `purchases/subscriptions/refund` 路径此前返回 404；此处新路径由当前 REST 目录独立确认，不声称旧链接重定向到它。API 成员和更深的权限/示例后代仍部分覆盖。 |
| [Android 开发者验证](https://developer.android.com/developer-verification?hl=zh-cn) | 已注册软件包名和关联密钥随应用迁移。 | 已另见开发者验证专题[Android 开发者验证](../android-developer-verification/android-developer-verification.zh-CN.md)。 |
| Play Console 的 App content、提交转移请求与支持入口 | 账号登录后查看转移表单、接受方确认和政策申报。 | 页面跳转到登录或账号专属入口，无法用公开网页核实具体字段/状态。 |
| [Play Developer Account Basics](https://playacademy.exceedlms.com/student/path/6420) | 账号管理培训材料。 | 入口已打开；课程内容需登录，未归档全文。 |



**逐链接核对（2026-10-23）：** 英文帮助正文、补充链接和支持入口中共尝试 20 个链接引用。下表按页面出现顺序列出直接目标与关系；其中 18 个可确认目标，2 个内部错误没有暴露目标 URL。Help 侧栏另有 10 项导航，不混入正文链接计数。

| # | 页面锚文本/直接目标 | 页面内容及与应用转移的关系 | 访问结果 |
| --- | --- | --- | --- |
| 1 | [policy guidelines](https://play.google.com/about/developer-content-policy/) | 原账号和待转移应用必须遵守 Play 政策。 | 跳转到现行 Developer Policy Center；已由独立双语专题覆盖。 |
| 2 | [15% service fee tier](https://support.google.com/googleplay/android-developer/answer/10632485) | 历史服务费计划与关联账号收入累计示例。 | 正文已打开；2021 计划说明不代替当前费用条款。 |
| 3 | [Account Group](https://support.google.com/googleplay/android-developer/answer/10627869) | 账户群组和关联开发者账号；跨组转移可能使应用当年收入计入两组。 | 正文已打开并在本专题总结。 |
| 4 | [Google Payments](https://payments.google.com/) | 查询新开发者账号注册交易 ID 的账号内付款入口。 | 重定向至登录后 Payments 页面；无法核验订单或个人资料。 |
| 5 | [Use Play App Signing](https://support.google.com/googleplay/android-developer/answer/9842756) | 上传密钥与应用签名密钥的管理/升级。 | Help 正文已打开；操作需按目标账号的应用签名状态决定。 |
| 6 | [Payments Profile](https://support.google.com/googleplay/android-developer/answer/3092739) | 目标账号转入付费应用或 IAP 时需要有效付款资料。 | 正文已打开；实际资料状态需要登录核验。 |
| 7 | [Add permissions](https://support.google.com/analytics/answer/1009702) | 给目标账号配置 Analytics 用户访问。 | 正文已打开，但该 UA 页面标记为 Legacy；不当作当前 GA4 指南。 |
| 8 | [Google Analytics](https://www.google.com/analytics/) | Analytics 产品入口。 | 重定向至 [Google Marketing Platform Analytics 产品页](https://marketingplatform.google.com/about/analytics/)（页面已打开）；这是产品介绍，不是 GA4 权限配置说明。 |
| 9 | [Google Developers Console projects: access](https://developers.google.com/compute/docs/access) | 为目标账号配置 Google Cloud 项目所有者/访问。 | 跳转至现行 Google Cloud 访问控制文档；IAM 权限按资源层级设置。 |
| 10 | [Google Developers Console](https://console.developers.google.com/) | API/项目控制台操作入口。 | 跳转到 Google 登录；项目和权限状态账号专属。 |
| 11 | [Firebase project link/unlink](https://support.google.com/googleplay/android-developer/answer/6110967) | 变更 Play、Firebase、Analytics、Ads/GMP 与付款服务的关联。 | Play Help 正文已打开并另作双语摘要；项目级 Firebase 权限需账号访问。 |
| 12 | [private app](https://support.google.com/googleplay/android-developer/answer/9874937) | Managed Google Play 专用应用的组织限制和转移边界。 | 正文已打开；iframe 创建的专用应用不可转至其他开发者账号。 |
| 13 | [contact our support team](https://support.google.com/googleplay/android-developer/contact/otherbugs) | 转移 Google Play Games Services 项目时的支持入口。 | 转至账号专属 Console 工单，需登录；未提交工单。 |
| 14 | [Google Play Developer API](https://developers.google.com/android-publisher) | 处理转移前留在原账号的订单退款。 | API 总览已打开；当前 refund 与 voided-purchases 后代见本页更新及递归图 §4.100。 |
| 15 | [App content](https://play.google.com/console/app/app-content/summary) | 查看可能随应用迁移的政策申报/App content 资料。 | 跳转到登录后的 Play Console；表单字段和应用状态不可公开读取。 |
| 16 | [Android Developer Verification guide](https://developer.android.com/developer-verification/guides/android-developer-console) | 说明仅在 Play 外分发时的 Android Developer Console 身份/软件包登记。 | 页面可读；这是外部分发/平台流程，不替代 Play 账号转移审核。 |
| 17 | Submit your transfer request | 向新开发者发起应用迁移。 | 点击返回 Internal Error，未暴露 href；不推测请求端点。 |
| 18 | [Academy for App Success](https://playacademy.exceedlms.com/student/path/6420) | Play Console 账号管理学习材料。 | 公开入口元数据可读；具体课程需登录。 |
| 19 | [Help Community](https://support.google.com/googleplay/android-developer/community?help_center_link=COeh_AISLlRyYW5zZmVyIGFwcHMgdG8gYSBkaWZmZXJlbnQgZGV2ZWxvcGVyIGFjY291bnQ&hl=en) | 开发者互助讨论入口。 | 精确上下文页面已打开，是含精选帖子、分类和提问入口的动态互助社区；不是正式政策，也不显示本账号转移案件状态。 |
| 20 | Contact us | 账号转移帮助入口。 | 点击返回 Internal Error，未暴露 href；不将其推定为另一联系入口。 |

该转移指南有许多通用 Google 服务或账号内链接。以上已将直接链接按与 Play 发布/转移的关系分类；其中登录、外部服务和课程目标只登记了用途及访问状态，没有把其全部二级/三级链接无限展开。

## 账户群组、付款资料、关联服务与专用应用

以下页面是账号资格、收入费用、付款和 Managed Google Play 的操作要求。它们不应与开发者计划政策条款混为一谈；费用和地区状态以各计划最新页面及 Play Console 为准。正文和关键后代于 2026-10-22 核对。

| 分支 | 正文摘要与实务影响 | 后代与访问状态 |
| --- | --- | --- |
| [Account Group](https://support.google.com/googleplay/android-developer/answer/10627869) | 关联账号包括开发者本人拥有的账号、由其控制且使用相同/相似品牌特征的子公司账号，以及特定共同控制下的关联公司账号；页面把“Control”界定为至少 50% 的投票权或所有权。账户群组需覆盖符合定义的账号，并由每个账号管理员同意。主账号可管理群组、代全组参加计划并查看同意加入者的联系邮箱，但不会因此获得其他成员账号的应用发布或财务权限；这些权限仍由各成员账号管理员单独授予。退出、删除或跨群组迁移可能影响计划资格和当年累计收入。 | [2021 年 15% 服务费说明](https://support.google.com/googleplay/android-developer/answer/10632485)已打开；其中品牌定义以 [DDA](https://play.google.com/developer-distribution-agreement.html) 为准。群组和申请操作入口须登录 Console；用户访问范围、财务/发布权限区别及邀请/撤权流程见[Play Console 用户权限专题](../play-console-user-permissions/play-console-user-permissions.zh-CN.md)。 |
| [Play Console 用户和权限](https://support.google.com/googleplay/android-developer/answer/9844686?hl=en) | 账号所有者、Admin、User 的权限；账号级与应用级访问范围；生产发布、测试轨道、财务、订单退款、政策声明等细分权限；邀请过期、权限组、用户清单导出。 | 英文正文和直接子页面已打开并整理为[双语用户权限专题](../play-console-user-permissions/play-console-user-permissions.zh-CN.md)。账号内的 Users and permissions、Payments Center 和 Google Developers Console 仍须分别登录/授权。 |
| 当前费用入口 | 旧的 [2021 费用层级页](https://support.google.com/googleplay/android-developer/answer/10632485)描述首个 100 万美元的历史计划。当前 [Service fees](https://support.google.com/googleplay/android-developer/answer/112622?hl=en) 和 [2026 lower service fees](https://support.google.com/googleplay/android-developer/answer/16954621?hl=en)按地区、新旧安装、交易类型和计划资格分层；公开时间表包括 EEA/UK/US 2026-06-30、澳大利亚/日本 2026-09-30、韩国 2026-12-31、其他地区 2027-09-30。 | 两个当前费用页已打开，并已在[付款/订阅专题](../payments/payments-and-subscriptions.zh-CN.md)展开。费用表会随计划和地区变化，2021 数字不能独立用作当前费率。 |
| [付款资料关联](https://support.google.com/googleplay/android-developer/answer/3092739) 与[创建付款资料](https://support.google.com/googleplay/android-developer/answer/7161426) | 付费应用和 IAP 需要付款资料。创建流程要求法定企业名称、有效实体地址、授权联系人和商家公开信息；不接受邮政信箱。资料创建后自动关联 Play Console；账户与付款资料只能关联一次，变更国家通常要新建付款资料及开发者账号并转移应用。 | [开发者/商户注册地区表](https://support.google.com/googleplay/android-developer/answer/9306917)已打开，分别区分开发者注册、商户注册和默认币种；地区和币种是动态表格，不宜复制成长期有效的硬编码清单。银行资料要求页 `paymentscenter/answer/7161440` 抓取超时；[销售税设置说明](https://support.google.com/paymentscenter/answer/7161449)已打开，但具体税务责任须按所在国及交易方式核对。 |
| [关联 Google 服务](https://support.google.com/googleplay/android-developer/answer/6110967) | 可关联 Google Ads、Firebase、Google Marketing Platform 和付款资料。Google Ads 关联可能开放自动生成的再营销名单；Firebase 可共享崩溃、分发、收入/受众数据；Google Marketing Platform 的请求由 Console 管理员批准/拒绝。解除关联会停止相应数据导出或追踪，但过去导出的数据仍可能留在接收产品。 | [Firebase 关联说明](https://support.google.com/firebase/answer/6392038)已打开；Google Ads 帮助中心已打开；这些厂商产品各自的 API、隐私和账号设置后代尚未全部展开。 |
| [发布 Managed Google Play 专用应用](https://support.google.com/googleplay/android-developer/answer/9874937) | 开发者账号可发布仅对指定组织可见的私有应用；每个应用最多登记 1,000 个组织。发布后几分钟内可在 EMM 中搜索/分发。第三方开发者可在客户授权下使用组织 ID 发布；设为仅限组织后，若要公开发布，须以不同软件包名建立新应用。通过企业 EMM iframe 创建的应用不能转移。 | [Android App Bundle 指南](https://developer.android.com/guide/app-bundle)、[发布与 rollout 流程](https://support.google.com/googleplay/android-developer/answer/9859348)及 [Custom App Publishing API](https://developers.google.com/android/work/play/custom-app-api/)已打开；正文中的 Admin Console 与第三方 EMM 入口返回内部错误，未能核实当前界面步骤。 |
| [Tax, compliance & regional requirements 索引](https://support.google.com/googleplay/android-developer/topic/15819563) | 此帮助主题归集税务、付款合规和地区要求；本次主题页本身返回缓存未命中。 | 该索引的 16 个直接子目标按政策链接图 4.5（快照：`google-play-policy-link-graph.md`，未导入本仓库）逐项记录；15 个正文已摘要，仅 WHT 仍受限。VAT 页的重点后代已在 §4.5.1 摘要；逐国家法规/税务机关仍未穷尽。 |

账户注册类别页 [Choose a developer account type](https://support.google.com/googleplay/android-developer/answer/13634885) 也已打开：提供金融/健康服务、使用获批 `VpnService` 或代表政府机构发布应用时，应使用组织账号；组织资料要求 D-U-N-S 编号，申请 D-U-N-S 本身免费。此页另链到本库已有的金融、健康、VPN 和政府应用要求专题。账号专属权限和状态仍须管理员在 Console 核实。

### Managed Google Play 私有应用：正文与最佳实践子页

Managed Google Play 私有应用不在面向消费者的公开 Play 商店展示，只允许指定组织的用户访问。它可以通过 Managed Play iframe、Play Console 或 Custom App Publishing API 发布；每个应用最多关联 1,000 个组织。私有应用改为公开分发通常须使用新的软件包名；iframe 创建的应用不能转移到其他开发者账号。目标 API 对“永久私有、仅供组织内部使用”的例外，和 Android 开发者验证对受管理设备的适用范围，是不同规则，详见Android 开发者验证专题[Android 开发者验证](../android-developer-verification/android-developer-verification.zh-CN.md)。

| 私有应用页面/后代 | 关键要求与关系 | 核验状态 |
| --- | --- | --- |
| [Managed Google Play 私有应用总览](https://support.google.com/googleplay/work/answer/9563481?hl=en) | 定义仅限指定组织内部使用、不在公开 Play Store 上展示的应用；通往发布、分发、托管和开发者验证操作页。 | 英文正文已打开；本表扩展其政策相关子链。 |
| [发布私有应用](https://support.google.com/work/android/topic/9496238?hl=en) | 可用 Managed Play iframe、Play Console 或 Custom App Publishing API；AAB/API 能力和是否可转移取决于发布方式，iframe 创建的应用不可转移、不可原位转公开。 | 正文已打开；EMM/Admin 内嵌控制台路径需账号权限。 |
| [分发私有应用](https://support.google.com/work/android/answer/9495634?hl=en) | 应用与组织关联后可由 EMM/Managed Play 搜索与分发；同一 Workspace/Cloud Identity 下的 EMM 绑定具自动批准行为。 | 正文已打开；组织绑定和实际设备策略需管理员账号核实。 |
| [私有应用托管](https://support.google.com/work/android/topic/9495939?hl=en) | 推荐由 Google Play 托管；外部托管受限制，且相关发布路径限于 Play Console。 | 正文已打开；托管能力依发布方式而异。 |
| [私有应用最佳实践](https://support.google.com/googleplay/work/answer/9496237?hl=en) | 处理 Play Console/iframe 警告；软件包名须在 Play 全局唯一；APK 使用 `zipalign`；谨慎选择长期签名密钥；了解 AAB/Play App Signing、签名密钥升级及 iframe 的密钥重置限制。使用第三方或商标内容前，应先向 Play App Review 提交书面许可并等待回复。 | 正文已打开。技术后代见 [zipalign](https://developer.android.com/tools/zipalign)、[Play App Signing](https://developer.android.com/studio/publish/app-signing.html)；书面授权流程见[Advance Notice](https://support.google.com/googleplay/android-developer/answer/6320428?hl=en)。 |
| [通过 EMM 内嵌 Managed Play 发布私有应用](https://support.google.com/googleplay/work/answer/9146439?hl=en) | iframe 发布可免收开发者注册费，但发布量、签名密钥、AAB、转移和转公开能力有特定限制；现行帮助页列出每天最多发布 15 个应用。 | 正文已打开；该路径的 EMM 操作入口需组织管理员权限。 |
| [私有应用开发者验证](https://support.google.com/work/android/answer/17266330?hl=en) | 2026-09-30 起，未受管理的 Play Protect 认证设备上的私有应用须关联已验证开发者身份并登记包名；全托管设备和工作资料适用设备侧豁免。 | Android Enterprise Help 英文正文已打开；与目标 API 私有应用例外分开判断。 |

相关 Android Enterprise 指南包括 [开发者指南](https://developer.android.com/work/guide)、[企业术语](https://developers.google.com/android/work/terminology)、[认证设备说明](https://www.android.com/certified/)和[管理方案概览](https://www.android.com/enterprise/management/)。这些帮助企业开发者理解工作资料、全托管设备和 EMM；它们不是 Play 政策条文。[内嵌发布 API 指南](https://developers.google.com/android/work/play/emm-api/managed-play-iframe)已部分打开；Android Developer Console 入口要求登录。

**勿与预装系统服务豁免混淆：** System services 专题[系统服务与预装软件](../system-services-and-preinstalled-software/system-services-and-preinstalled-software.zh-CN.md)解释了另一条仅供运营商、SoC 供应商和 OEM 核验的 Partner Center 资格路径。Managed Play 私有应用的组织可见性、目标 API 永久私有例外和系统服务豁免不是同一个规则。

## 审核状态与申诉

在 Play Console 的 **Policy status** 查看拒绝、移除、暂停及相关理由；拒绝通常保留最后成功发布版本，移除会使应用下架，暂停会使应用不可用。修正违规前不要重复提交被拒/移除的相同版本；若认为判断有误，按通知或 Console 正式申诉。参考：[Check your app’s policy status](https://support.google.com/googleplay/android-developer/answer/9842754)。

## 快速核对

| 应做 | 避免 |
| --- | --- |
| 填写可核验的法定与联系资料；按应用类别选择组织账号；注册软件包名称；提交有效的审核登录资料 | 遗漏账号或应用信息；填写不准确/无法核验的资料；提交过期的登录资料；通过非正式渠道转让账号 |

发布测试轨道、权限声明、送审、托管发布和分阶段 rollout 的操作顺序，另见[Google Play 测试、审核与发布流程](../publishing/play-release-workflow.zh-CN.md)。

## 相关官方资料

- [Play Console 要求](https://support.google.com/googleplay/android-developer/answer/10788890)
- [Android 开发者验证](https://developer.android.com/developer-verification?hl=zh-cn)
- [转移 Play Console 开发者账号所有权](https://support.google.com/googleplay/android-developer/answer/16909862)
- [将应用转移到其他开发者账号](https://support.google.com/googleplay/android-developer/answer/6230247?hl=zh-CN)
- [审核前准备 App content](https://support.google.com/googleplay/android-developer/answer/9859455)
- [新个人账号测试要求](https://support.google.com/googleplay/android-developer/answer/14151465)
- [新开发者账号设备验证](https://support.google.com/googleplay/android-developer/answer/14316361)
- [Google Play target API 要求](https://support.google.com/googleplay/android-developer/answer/11926878)
- [应用政策状态](https://support.google.com/googleplay/android-developer/answer/9842754)
- [合并版 Developer Program Policy](https://support.google.com/googleplay/android-developer/answer/18258653?hl=en)
- [开发者身份信息验证](https://support.google.com/googleplay/android-developer/answer/10841920)
- [商店详情与素材最佳实践](../store-listing-best-practices/store-listing-best-practices.zh-CN.md)
- [测试、审核与发布流程](../publishing/play-release-workflow.zh-CN.md)
