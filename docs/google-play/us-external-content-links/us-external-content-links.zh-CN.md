---
id: google-play.us-external-content-links
platform: google-play
language: zh-CN
authority: operational
status: current
kb_checked_at: 2026-10-22
review_due: 2027-01-22
regions: [US]
topics: [us, external-content-links, billing, transaction-reporting, service-fees]
snapshot_id: play.us-external-content-links
snapshot_package: "GooglePlay-KnowledgeBase-2026-10-24-review.zip"
coverage_status: "detailed-summary"
source_url: "https://support.google.com/googleplay/android-developer/answer/16470497?hl=en"
source_url_zh: "https://support.google.com/googleplay/android-developer/answer/16470497?hl=zh-CN"
source_url_us_policy_update: "https://support.google.com/googleplay/android-developer/answer/15582165?hl=en"
source_url_play_policy_center: "https://play.google/developer-content-policy/"
source_url_alternative_billing_apis: "https://developer.android.com/google/play/billing/alternative"
source_url_api_overview: "https://developer.android.com/google/play/billing/externalcontentlinks"
source_url_billing_release_notes: "https://developer.android.com/google/play/billing/release-notes"
source_url_in_app_integration: "https://developer.android.com/google/play/billing/externalcontentlinks/integration"
source_url_backend_integration: "https://developer.android.com/google/play/billing/outside-gpb-backend"
source_url_external_transactions_api: "https://developers.google.com/android-publisher/api-ref/rest/v3/externaltransactions"
source_url_external_links_form: "https://support.google.com/googleplay/android-developer/contact/external_content_links"
source_url_program_terms: "https://support.google.com/googleplay/android-developer/answer/16471405"
source_url_external_offers_eea: "https://support.google.com/googleplay/android-developer/answer/14372887?hl=en"
effective_date: "ECL terms effective 2025-12-09; other qualifying transactions from 2026-10-01; successful-download reporting deadline 2026-12-01 kept separate from 2027-01-27"
---

# 美国 Google Play 外部内容链接（External Content Links）计划

> **导入说明（Google batch 6）。** 正文来自已经分开的 2026-10-24 Google Play 知识库快照（`play.us-external-content-links`，核对日 2026-10-22）的改写摘要，不是官方页面的逐字副本。英文官方页面是效力来源。`kb_checked_at` 是快照源文件记录的核对日；本次导入没有重新打开线上官方页面。文中“本知识库”“本库”“本地专题”等说法描述的是该快照库的覆盖范围，不是本仓库已经导入的页面。指向本仓库没有收录的专题、链接图、台账或 CSV 的相对链接改为文字提及。指向 Google batch 1–5 或本批九个专题的相对链接改为本仓库文件。核对日 2026-10-22。中文源文件把 `source_url` 记为 `hl=zh-CN`，并同时记录英文 URL。英文文件两者都有。中文结尾把英文 ECL 页面作为官方来源，并称中文是结构化摘要。快照没有记录对 `hl=zh-CN` 页面的逐行核对，也没有记录该路由抓取失败。ECL 开发者条款于 2025-12-09 生效。英文版本具有控制力，译文仅供参考。除成功下载以外的合格交易，其报告和费用自 2026-10-01 起。成功应用下载事件的报告及相关费用截止日是 2026-12-01。该下载报告延期不推迟其他合格交易自 2026-10-01 起的报告和费用。这两个日期都不是 2027-01-27 预告。本页没有记录 2027-01-27。2026-03-04 的和解请求在本快照中不替代现行计划条款。本页是 operational 计划说明。Android 计费 API 是 implementation note。美国 ECL、美国替代计费和 EEA External Offers 保持分开。抓取到的费率表没有把三个列标题和抽出的两个百分比可靠对齐，因此本页不推断哪个百分比属于哪一列。**

**核对日期：2026-10-22。** 本页把美国 External Content Links（ECL）计划条款与 Android / Play Billing 实现资料分开说明。ECL 是美国及领地的可选项目，允许符合资格并获批的 Play 应用链接到应用外的数字商品购买页或非 Play 管理的应用下载页；它不是全球通用的站外支付许可，也不替代其他地区的项目资格。

## 1. 适用范围、地区与法律背景

- 资格范围是**面向美国及其领地用户的手机或平板应用/游戏**。开发者可以位于其他国家/地区，但 ECL 链接只能服务美国及领地用户。游戏和普通应用都可申请；不使用外部内容链接则无需加入。
- 可链接到应用内数字商品或服务的站外购买，也可链接到不由 Google Play 管理安装和更新的应用下载。数字商品购买链接可以与 Play Billing 并用，也可按项目条款取代它。
- 使用前必须完成项目入组，并让 Play 应用及任何被链接的外部应用获批。若同一应用也提供 Play Billing，所有用户仍须能**稳定、一致地访问 Play Billing**。
- 项目与美国法院命令有关；Google 明示可随命令变化而修改或终止项目。Google 的[美国政策更新页](https://support.google.com/googleplay/android-developer/answer/15582165?hl=en)记载，2026-03-04 Google 与 Epic 达成新和解并请求法院批准修订禁令；截至本次核对，该页称现行政策和项目继续有效。需同时查看最新法院状态与项目条款。
- ECL 和美国替代计费可以同时参加，但两个项目须分别满足资格、入组和实现要求。EEA External Offers 是另一套项目，不可把美国规则、费率或 API 要求搬到 EEA。

### ECL 另有一份开发者服务条款

[External Content Links Developer Terms of Service](https://support.google.com/googleplay/android-developer/answer/16471405)于 **2025-12-09** 生效，补充而非替代[Developer Distribution Agreement](https://play.google.com/about/developer-distribution-agreement.html)；如两者针对 ECL 参与发生冲突，ECL 专项条款优先。英语版控制解释，翻译仅供参考。条款中的报告、服务费、付款和审计章节按其原文在项目实际收取服务费时适用；目前项目已开始收取相应费用。

- 开发者直接向用户提供外部交易，并负责法定披露、收据/发票、交易税、产品交付和客服；Google 不作为这些交易的 merchant of record，也不处理用户付款或外部应用分发。
- Google 按月开具服务费/税款账单，尽商业上合理努力在月末后 15 个日历日内开出；付款到期日为对应发票日期起第 30 个日历日。逾期付款可按每月 1.5%（或法律允许的更低上限）计息，条款还允许在适用范围内抵销应付款。
- 开发者对外部交易税负和适用税务文件承担责任；条款另含审计权、陈述与保证、违约终止、Google 更新条款的通知与退出机制。持续参与可视为接受变更；不同意时条款规定的救济方式是退出项目。
- 条款对 ECL 用户交易、Linked External App、开发者和 Google 的角色作定义，并明确开发者需自行处理投诉、授权交易争议、退款以及当地法律责任。逐笔上报和用户保护要求仍须同时参照项目 Help 页面。

## 2. 外链目的地与用户保护

### 数字商品购买链接

- 购买页可以在浏览器、WebView 或用户设备上已安装的其他应用商店中打开。
- 跳转前须在应用内告知目的地页面及其用途。实际落地页不得与展示的目标不同，不得误导或以虚假信息促成跳转。
- 外链 URL 不得以缺少充分安全/加密保护的方式暴露用户个人身份信息。

### 应用下载链接

下载链接可以打开浏览器或设备上已安装的其他应用商店；目的地只能提供已获 ECL 批准的应用下载。下载目的地还须：

1. 具有分发所列应用的权利，并清楚展示应用名称、图标、说明、版本号、下载大小和开发者信息。
2. 每次安装都由用户知情并明确主动操作，且使用清晰可见、标签明确的界面控件。
3. 提供直接、公开且容易找到的终端用户客服渠道和用户数据政策。
4. 遵守适用的当地法律、法规和条例。

项目条款同时要求 Play 应用与被链接的外部应用遵守 Play Developer Policies；只有对外部应用不适用的政策（例如某些付款政策）不套用。应用内需通过 API 呈现 Play 信息页并支持家长控制。开发者还要为站外交易/下载提供客服、未授权交易争议处理，以及退款路径；若购买前已清楚披露不可退款，才可不提供退款方式。

## 3. 入组与外部应用下载审核

在实际展示链接前完成以下流程：

1. 对照本页资格和目的地要求，提交[External Content Links 声明表](https://support.google.com/googleplay/android-developer/contact/external_content_links)，并按 Google 支持团队要求完成 onboarding。
2. 在应用中接入外链 API。
3. 在 Play Console **Settings → External content links** 选择参加项目的 Play 应用。
4. 如果链接到外部应用下载，在 Console **Settings → Register external apps** 登记外部应用的所有版本；审查可能需要最多 7 天，特殊情况下更久。
5. 在 **Monitor and improve → Policy and programs → App content → External apps declaration** 填入已成功登记的包名、所有面向用户的落地页 URL 和实际 APK 下载 URL。目标页上所有可下载的外部应用都需要登记。
6. 每次外部应用或 APK 更新后重新提交更新版本，并等其通过审核后再把用户链接到新版本。

申报表、Console 设置、外部应用注册、Publishing overview 和 Policy status 含账号级状态；公开知识库无法确认某个包名是否获准、是否已入组或是否存在待处理问题。

## 4. 报告期限与费用

### 期限口径

- US ECL 参与者的交易报告和相关 Play 服务费从 **2026-10-01** 开始。
- 成功应用下载事件的报告及相应费用截止日已延至 **2026-12-01**。这项延期明确针对成功下载；不要据此推迟 2026-10-01 起其他符合条件交易的报告与费用。
- 对数字商品购买，项目 FAQ 要求报告外链后完成的所有交易，包括 $0 免费试用，以及新购买、租赁、续订、充值、升级和降级。

### 24 小时关联窗口与费率快照

费用适用于用户跟随 ECL 外链后 24 小时内，在应用外完成的合格交易或应用安装。新安装/现有安装按美国用户首次从 Play 安装该应用，或首次从 Play 更新该应用的日期判定：2026-06-30 当日及之后为新安装，之前为现有安装。

官方 Help 正文将应用内数字商品费率表的三类列标题显示为“周期性订阅 / 新安装的其他优惠 / 现有安装的其他优惠”，但本次网页正文抽取每行只返回两个百分比，无法可靠对齐三个费率列。因此保留页面可见值而**不推断各列对应关系**；按账号和交易类型核算时须打开[官方 ECL 页面](https://support.google.com/googleplay/android-developer/answer/16470497?hl=en)的原始费率表及开发者 Console。

| 官方表格行 | 正文抽取到的费率值 | 适用列映射 |
| --- | --- | --- |
| 首 100 万美元年收入 | 10%、10% | 抽取文本缺失一列的明确数值，需看官方表格/账号条款 |
| 标准服务费 | 10%、20% | 同上 |
| Play Games Level Up 或 Apps Experience 计划参与者 | 10%、15% | 同上 |

应用下载另有按安装收取的固定费用，金额可能定期调整；2026-10-22 官方页面列为 Games **$3.65/次安装**、Apps **$2.85/次安装**，申报时还需声明所安装外部应用的类别。

**下载费和交易费不要重复套算：** 用户从 Play 应用的外链首次下载外部应用时，只收固定下载费；由这个最初下载链接带来的后续购买，即使在 24 小时内，也不另收交易服务费。但下载后若用户再次从 Play 应用中的独立购买链接跳转，则该新 linkout 独立判断并适用交易费。

## 5. Android 客户端集成

当前[应用内集成指南](https://developer.android.com/google/play/billing/externalcontentlinks/integration)要求 Play Billing Library **8.2.1 或更高版本**。它是 API 技术前提，不等于项目资格或入组获批。

| 顺序 | 客户端实施要点 | 合规意义/常见误区 |
| --- | --- | --- |
| 初始化 | 用 `BillingProgram.EXTERNAL_CONTENT_LINK` 调用 `enableBillingProgram()`；此流程不需要 `PurchasesUpdatedListener`。 | 不要把普通 Play Billing 购买回调误当作 ECL 链路。 |
| 检查可用性 | 连接 Play 后调用 `isBillingProgramAvailableAsync()`；只有返回 `BillingResponseCode.OK` 才继续。 | 国家、账号入组或设备不支持时不得绕过 Play 直接打开站外页。 |
| 生成 token | 每次跳转前调用 `createBillingProgramReportingDetailsAsync()` 生成新 `externalTransactionToken`，紧接跳转使用；不可缓存或复用。 | token 关联后续交易报告；每个 linkout 都要新 token。 |
| 启动链接 | 调用 `launchExternalLink()`，传入已登记/批准的 URI、链接类型、`BillingProgram.EXTERNAL_CONTENT_LINK` 和启动模式。下载链接必须使用 `LAUNCH_IN_EXTERNAL_BROWSER_OR_APP`。 | 只能跳往用户事先看到的目的地；下载 URL 必须经过 Console 审批。 |
| 处理返回值 | `OK` 表示 Play 已把用户带到应用外，**不表示已完成购买**。对 `BILLING_UNAVAILABLE`、`FEATURE_NOT_SUPPORTED`、`DEVELOPER_ERROR`、`USER_CANCELED` 和可重试网络/连接错误分别处理。 | 不得根据跳转成功回调虚构交易；交易确认/报告要由外部交易系统完成。 |
| 测试 | 使用 license testers 验证流程；官方指南说测试账号发起的交易不会向开发者开账单。 | 测试仍需覆盖设备/国家资格、取消、网络重试和目的地版本审核。 |

## 6. 后端交易报告与退款

[Google Play 后端集成指南](https://developer.android.com/google/play/billing/outside-gpb-backend)说明通过 Google Play Developer API 的 [`externaltransactions` 资源](https://developers.google.com/android-publisher/api-ref/rest/v3/externaltransactions)报告合格站外交易。该指南同时服务多个地区计费/链接项目，具体资格和时间应以 US ECL 条款为准。

- 按适用项目报告所有合格交易；包括零金额免费试用、初次购买、续订、充值、升级/降级和应用下载事件。只有地区/用户符合项目条件时才可报告；不符合条件的 API 请求会被拒绝。
- 初次购买、一次性购买和应用下载需关联客户端取得的 `externalTransactionToken`。每笔报告使用开发者生成的唯一 `externalTransactionId`；不得在 ID 中放入个人身份、专有或机密信息。
- 后续续订/充值使用新的交易 ID，并用 `initialExternalTransactionId` 关联初始交易。产品变更，或订阅取消/过期后再次购买时，应创建新的交易链。
- 退款按已报告的具体交易 ID 逐笔提交；退款订阅时要指向被退款的具体续订。部分退款需报退款的税前金额。
- `createexternaltransaction` 与 `refundexternaltransaction` 另有每分钟 1,200 次调用上限；`getexternaltransaction` 不计入这一附加上限，Developer API 通用配额仍单独适用。
- 后端文档中 `ExternalOfferDetails`、`appDownloadEventExternalTransactionId` 等示例属于 EEA External Offers。本轮已对照 Developer API schema：US ECL 使用互斥的 `externalContentLinkDetails`，下载时填 `LINK_TO_APP_DOWNLOAD` 及必需的外部应用包名/类别；EEA 的 `appDownloadEventExternalTransactionId` 不属于 US ECL 对象。US 下载事件金额的端到端样例仍未找到，不能从 EEA 样例推断。

### US ECL 的 ExternalTransaction API 字段（2026-10-24 复核）

Google Play Developer API 的 [`externaltransactions` REST 资源](https://developers.google.com/android-publisher/api-ref/rest/v3/externaltransactions)（资源页标注 2026-09-28 更新）将 ECL 与 EEA External Offers 明确建模为不同、互斥的详情对象：一次 ExternalTransaction 至多设置 `externalContentLinkDetails` 或 `externalOfferDetails` 其中之一。

- US ECL 使用 `externalContentLinkDetails`。其 `linkType` 必填，可为 `LINK_TO_DIGITAL_CONTENT_OFFER` 或 `LINK_TO_APP_DOWNLOAD`；当类型为 app install 时，还必须提供 `installedAppPackage` 和 `externalAppCategory`。类别仅为 `APP` 或 `GAME`，且须与 Play Console 外部应用验证时提交的类别一致。
- EEA External Offers 使用不同的 `externalOfferDetails`、`ExternalOfferLinkType` 和 `installedAppCategory` 字段。`appDownloadEventExternalTransactionId` 属于 EEA `ExternalOfferDetails`，不属于 US ECL 的 `ExternalContentLinkDetails`；不能把 EEA 后端示例原样复制为 US 请求。
- 创建接口要求 `externalTransactionId` 在同一应用内唯一，长度 1–63 个字符且限 ASCII 字母、数字、下划线、连字符；不得放入 PII。请求使用 `androidpublisher` OAuth scope。常见必填交易字段还包括原始税前金额、原始税额、交易时间、用户税务地址和一次性/周期性交易对象；一次性交易 token 由客户端外部链接流程提供。
- 查询接口按 `applications/{packageName}/externalTransactions/{externalTransactionId}` 读取交易且无请求体。退款接口按交易资源名 POST，要求 `refundTime`，并在 `fullRefund` 与 `partialRefund` 中二选一；部分退款要有该交易内唯一的 `refundId` 和低于剩余税前金额的退款额。
- US ECL Help 要求记录符合条件的应用安装，并说明 app-download reporting 会申报外部应用类别；成功下载报告与相关费用的截止日为 **2026-12-01**，其他符合条件交易/费用从 **2026-10-01** 起。API 资源虽列出字段，但没有提供可确认 US 下载事件金额填法的端到端示例；因此本专题不从 EEA 示例推断下载事件应填零金额，也不推断 US ECL 后续外部应用内交易的关联字段。

逐项方法页：[createexternaltransaction](https://developers.google.com/android-publisher/api-ref/rest/v3/externaltransactions/createexternaltransaction) · [getexternaltransaction](https://developers.google.com/android-publisher/api-ref/rest/v3/externaltransactions/getexternaltransaction) · [refundexternaltransaction](https://developers.google.com/android-publisher/api-ref/rest/v3/externaltransactions/refundexternaltransaction)。方法和关键 ECL 类型已打开；Price、所有其他 API 类型成员、完整调用样例及账号内要求仍未全部遍历。

## 7. 政策正文直链及其子页

“正文直链”指 ECL 页面正文指向的政策、实现、表单等页面；Help Center 的“Tax, compliance & regional requirements”侧栏是站内导航，单独记录，不视为 ECL 正文要求。页面正文的账户入口只审阅其公开说明，不能证明任何开发者账号的状态。

| 来源页/直链 | 与 ECL 的关系及核验状态 |
| --- | --- |
| ECL 正文中的“US policy update”和“District Court order” → 同一[美国政策更新页](https://support.google.com/googleplay/android-developer/answer/15582165?hl=en) → [2024 年永久禁令 PDF](https://storage.googleapis.com/gweb-uniblog-publish-prod/documents/2024.10.07_Dkt._1017_Permanent_Injunction.pdf) | 正文两个锚文本实际指向同一更新页；PDF 是更新页的下一层链接，不是 ECL 正文直接链接。两页均已打开并在美国政策分支摘要。更新页记录 2026-03-04 的修订禁令请求、2026-07-22 费用与报告启动、2026-09-17 下载期限更新；命令和项目条款未来可能再变。 |
| [Developer Policy Center](https://play.google/developer-content-policy/)；[Payments policy](https://support.google.com/googleplay/android-developer/answer/9858738?hl=en) | Policy Center 正文已打开；其中各项政策在其他双语专题继续展开。Play 应用与链接的外部应用均受适用政策约束；Payments 政策对外部应用可能不适用的部分不应扩展成主 Play 应用的通用豁免。 |
| [External Content Links API 概览](https://developer.android.com/google/play/billing/externalcontentlinks) → [Play Billing Library 版本说明](https://developer.android.com/google/play/billing/release-notes) → [应用内集成指南](https://developer.android.com/google/play/billing/externalcontentlinks/integration) → [后端报告指南](https://developer.android.com/google/play/billing/outside-gpb-backend) | 全文已打开。版本说明显示 PBL 8.2.0 引入外部内容链接 API、8.2.1 修复 eligibility/token 方法问题；当前版本说明页还列出 9.1.0。ECL 专用集成页确认最低 8.2.1+；概览确认 US 计划和 Console 外部应用审批；集成页说明 eligibility、token、linkout 和错误处理；后端页说明交易 ID、零金额事件、续订/退款及 API 配额。API 方法类型和全部示例后代仍未穷尽。 |
| [External Content Links 声明表](https://support.google.com/googleplay/android-developer/contact/external_content_links) → [ECL Developer Terms of Service](https://support.google.com/googleplay/android-developer/answer/16471405) → [DDA](https://play.google.com/about/developer-distribution-agreement.html) | 声明表和 ECL 条款全文已打开。表单要求开发者账号 ID、注册实体/地址、包名、账单地址/公司域名邮箱、联系人、可用的用户支持联系方式、PCI DSS 或不处理卡数据的确认、未授权交易争议路径，以及代表实体签署的授权声明。专项条款 2025-12-09 生效并补充 DDA；按月开票、30 天付款、交易税、开发者对用户的直接责任、审计及退出机制已摘要。 |
| ECL 条款 → [Enforcement Process](https://support.google.com/googleplay/android-developer/answer/9899234)、[退出/计费与链接项目支持表单](https://support.google.com/googleplay/android-developer/contact/billing_and_linkouts_program_q) | Enforcement Process 本轮点击超时；执行政策已有独立专题。退出表单已打开但重定向至通用 alternative billing/link-out 联系入口；需提供账号 ID、应用包名和问题描述，实际请求需登录。 |
| [官方费率依据：How Google Play Works](https://google.play/howplayworks/)；页面内 FAQ 和目的地要求 | 已打开概览页。费率表和 FAQ 在主 ECL Help 页内；本专题逐项摘要其 24 小时窗口、安装费与下载后交易费规则。 |
| ECL Help → [Alternative billing APIs](https://developer.android.com/google/play/billing/alternative) | 页面已打开；概括的是 User Choice / alternative billing API 和信息/选择屏幕，文内 PBL 5.2/6.2.1 版本要求针对替代计费，不适用于 ECL。ECL 版本以[专用集成页](https://developer.android.com/google/play/billing/externalcontentlinks/integration)为准：PBL 8.2.1+。 |
| ECL Help → [Play Console](https://play.google.com/console/developers) | 点击后跳转到 Google Play for business 公共入口，未暴露开发者账号；正文所列 Settings/App content 路径仍须登录 Console。 |
| ECL Help → Help Community、[Contact us](https://support.google.com/googleplay/android-developer/contact/billing_and_linkouts_program_q) | Help Community 点击返回内部错误，未解析出稳定目标 URL；Contact us 跳到多项目支持表单，提交需要账号信息。 |
| [EEA External Offers](https://support.google.com/googleplay/android-developer/answer/14372887?hl=en) | 已打开并在[付款专题](../payments/payments-and-subscriptions.zh-CN.md)单独总结；仅作为地区对照，不能套用到美国。 |
| API 子页：Play Billing 8 迁移、`BillingClient`、`LaunchExternalLinkParams`、license testing、[`externaltransactions` 资源](https://developers.google.com/android-publisher/api-ref/rest/v3/externaltransactions)及其 [create](https://developers.google.com/android-publisher/api-ref/rest/v3/externaltransactions/createexternaltransaction)、[get](https://developers.google.com/android-publisher/api-ref/rest/v3/externaltransactions/getexternaltransaction)、[refund](https://developers.google.com/android-publisher/api-ref/rest/v3/externaltransactions/refundexternaltransaction) 方法 | 资源页及三个方法页均已打开；补入 US `externalContentLinkDetails` 与 EEA `externalOfferDetails` 的互斥关系、下载类别/包名条件、创建 ID 与 OAuth、查询和退款请求形状。其他 API 类型成员、所有代码样例与生成客户端后代仍未逐页审阅，详见来源链接审计台账（快照：`../source-page-audit.csv`，未导入本仓库）。 |
| PBL 版本说明 → [Android skills 概览](https://developer.android.com/tools/agents/android-skills) 与 [Android CLI 概览](https://developer.android.com/tools/agents/android-cli) | 两页已打开；它们说明 Android skills/CLI 的安装方式与用途，属于可选开发者工具，不额外创设 Play ECL 政策义务。版本说明中的升级 skill 提示可用于维护 Billing Library，但是否采用取决于开发团队工作流。 |
| ECL Help 页的 16 项地区/税务侧栏及 Android Developers 站点页眉/页脚链接 | 属于导航，不等同正文里的 ECL 政策要求；台账保留这些 URL 的引用/审计状态，但本轮没有逐一展开所有侧栏目标及其后代。 |

**递归边界：** 当前已打开 ECL 条款页、API 概览、关键应用内/后端集成页、声明表、更新页和 API 资源页，并逐项汇总会影响资格、用户流程、报告、退款及费用的关系。Play Billing API 类型、所有 code sample、Google Play Developer API schema 的每个字段，以及 16 项地区侧栏后代仍未完全闭合；来源台账保留逐 URL 访问状态，不据此宣称整个 Google Play 链接图已穷尽。

## 8. 相关知识库页面

- [付款、计费与订阅政策](../payments/payments-and-subscriptions.zh-CN.md) · [English](../payments/payments-and-subscriptions.en-US.md)
- 递归政策链接图（快照：`../google-play-policy-link-graph.md`，未导入本仓库）
- 政策执行期限总表（[政策执行控制总表](../google-play-policy-operations/google-play-policy-operations.zh-CN.md)）

官方来源：[美国 ECL 计划条款](https://support.google.com/googleplay/android-developer/answer/16470497?hl=en) · [应用内集成](https://developer.android.com/google/play/billing/externalcontentlinks/integration) · [后端报告](https://developer.android.com/google/play/billing/outside-gpb-backend)。这是官方材料的结构化摘要，不是完整逐字副本；费率、账号资格、法院状态及 Console 入组结果应在发布/计费前回到实时官方页面核实。
