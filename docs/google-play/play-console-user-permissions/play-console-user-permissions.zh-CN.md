---
id: google-play.play-console-user-permissions
platform: google-play
language: zh-CN
authority: operational
status: current
kb_checked_at: 2026-10-22
review_due: 2027-01-22
regions: [global]
topics: [play-console, users, permissions, account-access, audit]
snapshot_id: play.console-user-permissions
snapshot_package: "GooglePlay-KnowledgeBase-2026-10-24-review.zip"
coverage_status: "detailed-summary"
source_url: "https://support.google.com/googleplay/android-developer/answer/9844686?hl=en"
source_url_zh: "https://support.google.com/googleplay/android-developer/answer/9844686?hl=zh-CN"
effective_date: "current-as-reviewed on 2026-10-22; no 2027-01-27"
---

# Play Console 用户、权限与访问审计

> **导入说明（Google batch 7）。** 正文来自已经分开的 2026-10-24 Google Play 知识库快照（`play.console-user-permissions`，核对日 2026-10-22）的改写摘要，不是官方页面的逐字副本。英文官方页面是效力来源。`kb_checked_at` 是快照源文件记录的核对日；本次导入没有重新打开线上官方页面。文中“本知识库”“本库”“本地专题”等说法描述的是该快照库的覆盖范围，不是本仓库已经导入的页面。指向本仓库没有收录的专题、链接图、台账或 CSV 的相对链接改为文字提及。指向 Google batch 1–6 或本批十二个专题的相对链接改为本仓库文件。核对日 2026-10-22。英文帮助文章已打开。`hl=zh-CN` URL 无法访问，因此本仓库中文正文是编辑改写，不是对中文官方页面的逐行核对。该访问失败不是政策变更。源文件把 `effective_date` 记为 `current-as-reviewed`。本页没有记录 2027-01-27。组织验证 PDF 提供简体中文、英文、日文、韩文和巴西葡萄牙语。快照打开了入口，没有复录 PDF 内部步骤。开发者账号设置目录页抓取失败。本页是 operational 的 Console 访问说明。它不是开发者计划政策，也不能证明某个账号的实时授权。应用权限声明仍是独立专题。

**核对日期：2026-10-22。** 官方英文帮助页[添加开发者账号用户并管理权限](https://support.google.com/googleplay/android-developer/answer/9844686?hl=en)全文已打开并整理。简体中文 URL 本轮无法访问，因此以下中文为英文官方页的双语改写，不代表已核对中文译文与英文逐句一致。此页说明 Play Console 的账号操作权限；它不是独立的开发者计划政策，也不能代替账号登录后的实际授权状态。

## 访问层级与授权范围

| 层级 | 官方页面定义 | 关键边界 |
| --- | --- | --- |
| Account owner（账号所有者） | 开发者账号最初注册者，拥有 Play Console 全部访问权，可邀请/移除用户并管理权限。 | 只有所有者可以关联销售用 Google Payments profile，并访问/编辑 Play Console 的 Payments settings。 |
| Admin（管理员） | 持有 Admin（all permissions）权限，可按账号或应用范围授权；可邀请/移除用户并管理权限。 | 全局 Admin 可管理访问期限并查看 Activity log；应用级 Admin 不能移除拥有全局权限的用户。只有所有者能做部分账号级操作。 |
| User（用户） | 可获账号级或指定应用的不同权限。 | 不能邀请用户或编辑他人权限。 |

账号级权限作用于开发者账号中的所有应用（通常也涵盖之后新增的应用）；应用级权限只作用于被选中的应用。部分权限只在其中一个范围提供，不能仅凭名称推断范围。

## 关键权限：按风险与作用区分

| 权限 | 能做什么 | 重要边界 |
| --- | --- | --- |
| Admin（all permissions） | 邀请/移除用户、管理权限；获得其他权限。 | 高权限，应限制给确实负责账号管理的人。应用级 Admin 的可见/管理范围受应用范围限制。 |
| View app information（read-only） | 查看应用信息、关联的 Play Games Services 项目。 | 不含财务数据；应用级权限。账号级对应项是查看所有应用信息并下载批量报告。 |
| View app quality information（read-only） | 查看 Android vitals、预发布报告和基本构建/轨道/版本信息。 | 只读，不允许修改。 |
| View app information and download bulk reports（read-only） | 查看所有应用信息并下载批量报告。 | 账号级；不含财务数据。创建新应用还需要此权限与创建草稿应用权限的组合。 |
| Edit and delete draft apps / Create, edit, and delete draft apps | 修改或删除草稿应用；账号级版本可创建草稿。 | 草稿权限不允许发布应用或启动版本发布；账号级新建应用还要求查看应用信息权限。 |
| Manage policy declarations | 编辑/提交 Data safety、权限声明等政策申报，并查看相关通知。 | 申报权限不是政策豁免；实际声明仍须符合对应政策并由 Google 审核。 |
| View financial data / View financial data, orders, and cancellation survey responses | 查看财务/销售报表、Purchases API 和关联 Play Games Services 收入；账号级版本还包括订单和取消调查书面回复。 | 财务数据与普通应用只读权限分开授予。收入、报表或取消调查数据需要相应范围的财务权限。 |
| Manage orders and subscriptions | 查看订单、退款、取消订阅。 | 单独授予不允许查看汇总财务报表；该能力另需 View financial data。 |
| Release to production, exclude devices, and use Play App Signing | 创建、编辑、发布生产版本；取消/恢复发布；设备排除；使用 Play App Signing。 | 这是明确包含生产发布的权限。 |
| Release apps to testing tracks | 上传草稿、创建/发布测试轨道版本、修改 OBB、编辑未生产应用的版本说明，也可上传内部分享 APK。 | 不允许发布生产版本。 |
| Manage testing tracks and edit tester lists | 更改内部/开放/封闭测试配置，管理测试者名单。 | 不允许发布生产版本；测试者管理与版本发布是不同权限。 |
| Manage store presence | 编辑商店详情和实验、价格、应用内商品、分发/内容分级、促销等。 | 不允许在设备目录中排除设备。 |
| Reply to reviews | 回复 Google Play 评价并更改建议回复联系人。 | 没有该权限仍可查看评分和评价，但不能回复。 |
| Managed Google Play private apps | 为组织创建、编辑和发布私有应用。 | 不包含管理内部测试轨道，也不允许发布公开应用。 |
| Google Play Games Services | 编辑或发布 Play Games Services 项目。 | 仅账号级；除 Play Console 权限外，相关 Google Developers Console 项目也要单独授权。访问部分游戏财务数据还需同时具备账号级和关联应用级财务权限。 |

## 邀请、权限组、到期和移除

- 受邀者必须用管理员填写的同一邮箱登录；换邮箱需要管理员重发邀请。
- 邀请发出后 30 天内未接受并登录会过期，管理员需要重发。
- 个人用户和权限组都可设置到期日。个人用户未设到期日时会持续拥有权限；权限组未设到期日时，组权限不会自行过期，需移除用户或权限组。
- 账号所有者/管理员可批量或逐人授予账号级与应用级权限；注意同一用户可同时持有两种范围。
- 移除用户或缩短权限前，应确认该账号不会因此失去必要的生产发布、审核、支持或账务工作能力。

## 导出用户清单与审计变更

账号所有者可在 Users and permissions 导出用户 CSV。表格可以按权限、应用、邀请状态、邮箱域名或姓名筛选。CSV 包含邮箱、邀请/访问状态、邀请时间、到期时间、应用级权限和账号级权限；管理员只能看到其负责范围内的应用数据。各权限代码与界面名称的映射见官方[导出用户清单说明](https://support.google.com/googleplay/android-developer/answer/10019561?hl=en)。

建议把该 CSV 用于账号访问复核：先核对 Admin、生产发布、财务、订单和政策申报权限，再确认临时协作者的到期日；检查权限时以 CSV 的账号级/应用级列分别核对。此处是运维建议，不是 Google Play 新增的政策义务。

Activity log 的[官方说明](https://support.google.com/googleplay/android-developer/answer/9859273?hl=en)称，账号所有者可查看开发者账号生命周期内的变更；页面默认最多显示 200 条，可按应用和变更项目筛选，记录显示应用、变更位置、变更内容、操作者邮箱及本地时区日期/时间。该页面链接经重定向落到旧 URL `answer/6053184`，台账保留跳转关系。

## 正文直接链接：目标页与关系

| 正文链接 | 目标页内容与本页关系 | 访问/覆盖状态 |
| --- | --- | --- |
| [关联 Google Payments profile](https://support.google.com/googleplay/android-developer/answer/9875344) | 付费应用/应用内购买的商户设置；Play Console 与付款资料只能关联一次，变更通常需新付款资料/开发者账号并转移应用。 | 页面打开，重定向到 `answer/3092739`；本地摘要见[Play Console 要求](../play-console-requirements/play-console-requirements.zh-CN.md)。 |
| [Activity log](https://support.google.com/googleplay/android-developer/answer/9859273?hl=en) | 账号变更审计；补足权限页的全局 Admin/所有者审计能力说明。 | 页面打开，重定向到 `answer/6053184`；其筛选和记录字段已在上节摘要。 |
| [Publish private apps](https://support.google.com/googleplay/android-developer/answer/9874937) | Managed Google Play 私有应用发布、组织 ID、组织可见范围和私有转公开的限制。 | 正文已完整打开；见[Play Console 要求](../play-console-requirements/play-console-requirements.zh-CN.md)。 |
| [Play Console 首页](https://play.google.com/console) / [Users and permissions](https://play.google.com/console/developers/users-and-permissions) | 账号内的用户邀请和权限设置入口。 | 首页链接跳到 Play 商业介绍页；Users and permissions 转登录页。读取网页不能代替检查当前账号授权。 |
| [Google Developers Console](https://console.developers.google.com/) | Play Games Services 项目的独立访问控制。 | 点击后转登录；需由项目管理员另行授予。 |
| [Google Payments Center](https://payments.google.com/payments/) | 付款中心报告用户权限需要在 Payments Center 单独设置，与 Play Console 权限分开。 | 目标跳转到付款中心账号页，无公开帮助正文可供离线整理。 |
| [Play Academy 账号基础课程](https://playacademy.exceedlms.com/student/path/6420) | 补充账号基础培训。 | 课程入口已打开；课程正文需要登录，不能从公开入口确认具体教学内容。 |
| [帮助社区](https://support.google.com/googleplay/android-developer/community?hl=en)、[Contact us](https://support.google.com/googleplay/android-developer/gethelp) 及图像/页内锚点 | 支持反馈、联系入口、界面说明和本文内权限定义跳转。 | 社区返回 Cache miss；Contact us 转账号内支持；页内锚点不是新政策页。 |

## “Set up your developer account”帮助侧栏（15 项，含当前页）

侧栏是[开发者账号设置目录](https://support.google.com/googleplay/android-developer/topic/7072535)，与正文权限义务分层。其余 14 个目标均已点击；可直接关联到本库的账号资料/身份核验专题。目录页本身抓取失败；访问同级页面不代表这些页面的所有后代已递归闭合。

| 侧栏目标 | 与用户权限的关系 | 本地阅读入口 / 状态 |
| --- | --- | --- |
| [Developer account registration payment methods and receipts](https://support.google.com/googleplay/android-developer/answer/9875040) | 注册费付款方式、收据和交易记录。 | 已打开；账号注册/付款背景见[Play Console 要求](../play-console-requirements/play-console-requirements.zh-CN.md)。 |
| [Choose a developer account type](https://support.google.com/googleplay/android-developer/answer/13634885) | 个人/组织账号选择；金融、健康、获准 VPN、政府应用等场景应选组织类型。 | 已打开；见[Play Console 要求](../play-console-requirements/play-console-requirements.zh-CN.md)。 |
| [Contact information requirements](https://support.google.com/googleplay/android-developer/answer/10840893) | 公开开发者资料与供 Google 联系的已验证邮箱/电话。 | 已打开；见[Play Console 要求](../play-console-requirements/play-console-requirements.zh-CN.md)。 |
| [View and manage account information for verified accounts](https://support.google.com/googleplay/android-developer/answer/13634081) | 仅适用于通过 Play Console Requirements 验证的账号；只有所有者可变更开发者账号资料。 | 已打开；与[Play Console 要求](../play-console-requirements/play-console-requirements.zh-CN.md)及开发者验证[Android 开发者验证](../android-developer-verification/android-developer-verification.zh-CN.md)相连。 |
| [Verify accounts created before September 2023](https://support.google.com/googleplay/android-developer/answer/14177239) | 旧账号验证流程及历史分批期限。 | 已打开；历史时间表不是当前账号个人期限，当前状态须登录 Console 查看；见开发者验证[Android 开发者验证](../android-developer-verification/android-developer-verification.zh-CN.md)。 |
| [Verify developer identity information](https://support.google.com/googleplay/android-developer/answer/10841920) | 身份资料、联系方式、付款资料和验证顺序。 | 英文页已打开；见开发者验证[Android 开发者验证](../android-developer-verification/android-developer-verification.zh-CN.md)及[Play Console 要求](../play-console-requirements/play-console-requirements.zh-CN.md)。 |
| [Organization verification guide](https://support.google.com/googleplay/android-developer/answer/15574489) | 组织账号旧账号验证流程的 PDF 指南，提供简体中文、英文、日文、韩文及巴西葡萄牙语。 | 入口已打开；仅记录语言和用途，PDF 内部所有链接/步骤未逐项复录。 |
| [Create and manage an Account Group](https://support.google.com/googleplay/android-developer/answer/10627869) | 关联账号群组与计划资格；群组成员关系不会自动转移应用或财务权限。 | 已打开；见[Play Console 要求](../play-console-requirements/play-console-requirements.zh-CN.md)。 |
| [Export a list of users with account access](https://support.google.com/googleplay/android-developer/answer/10019561) | CSV 用户与权限审计。 | 已打开并摘要；见本页上方“导出用户清单与审计变更”一节。 |
| [Create or update your developer profile](https://support.google.com/googleplay/android-developer/answer/9873827) | 可选的公开开发者品牌页；至少要有一个已发布应用。 | 已打开；非权限授予。详细素材规格和更新等待时间见官方目标页。 |
| [Required information to create a developer account](https://support.google.com/googleplay/android-developer/answer/13628312) | 创建个人/组织账号需要的身份、联系和付款资料。 | 已完整打开；见开发者验证[Android 开发者验证](../android-developer-verification/android-developer-verification.zh-CN.md)。 |
| [Keeping developer account information up to date](https://support.google.com/googleplay/android-developer/answer/13634888) | 维护账号法律身份、公开资料和联络信息，避免账号受限。 | 已完整打开；见[Play Console 要求](../play-console-requirements/play-console-requirements.zh-CN.md)。 |
| [Manage email recipients](https://support.google.com/googleplay/android-developer/answer/15771712) | 管理员可让组织内相关人员收政策、付款/税务、提示或问卷邮件，而无需授予 Play Console 登录权限。 | 已打开；邮件收件人不是 Play Console 用户权限，不应为了收通知而授予更广账号访问。 |
| [Update identity details managed by a Payments profile](https://support.google.com/googleplay/android-developer/answer/16260648) | 所有者可更新付款资料管理的法定名称/地址；国家、组织类型、D-U-N-S 变更通常需新付款资料并验证后关联。 | 已打开；与[Play Console 要求](../play-console-requirements/play-console-requirements.zh-CN.md)的付款资料/身份验证部分相连。 |

## 实务核对建议（非独立政策条款）

1. 先按职责分配最窄的账号或应用范围；给单应用协作者优先考虑应用级权限。
2. 把生产发布、Admin、财务数据、订单退款和政策申报权限单独复核，避免将“只读”误认为包含财务数据。
3. 为临时协作设置到期日；每次人员离岗或职责变化时重看用户清单、权限组和通知收件人。
4. 对有 Play Console 用户权限但不应查看账号资料的人，检查是否意外继承账号级权限；Payments Center 与 Google Developers Console 另做单独访问复核。
5. 把“测试发布”和“生产发布”权限分开确认；草稿管理、测试轨道管理和生产发布不是同一项能力。

## 关联主题

| 主题 | 关系 |
| --- | --- |
| [Play Console 要求](../play-console-requirements/play-console-requirements.zh-CN.md) | 开发者账号、付款资料、验证和发布前要求。 |
| [测试、审核与发布流程](../publishing/play-release-workflow.zh-CN.md) | 测试轨道、生产发布、审核状态和可执行这些操作的权限。 |
| [Play Console 权限声明与审核](../permissions-declaration/permissions-declaration.zh-CN.md) | 使用 Manage policy declarations 权限编辑申报，不改变受限权限政策的审核要求。 |
| [付款与订阅](../payments/payments-and-subscriptions.zh-CN.md) | 财务报告、订单与取消调查数据权限的商业操作背景。 |

## 覆盖边界

当前英文权限页、正文可解析链接和 15 项帮助侧栏已核对；其中 Play Console/Payments/Developers Console 的账号内操作仍需登录。Google Play Academy 课程、PDF 指南的内部链接，以及 14 个侧栏同级页面各自的所有后代没有在此页递归穷尽。官方权限名称、账号状态和 Console UI 会变动，执行前应打开当前帮助页并检查目标账号。
