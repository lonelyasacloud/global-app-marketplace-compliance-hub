---
id: google-play.account-ownership-transfer
platform: google-play
language: zh-CN
authority: operational
status: current
kb_checked_at: 2026-10-24
review_due: 2027-01-24
regions: [global]
topics: [account-transfer, developer-account, ownership, identity-verification, play-console]
snapshot_id: play.account-ownership-transfer
snapshot_package: "GooglePlay-KnowledgeBase-2026-10-24-review.zip"
coverage_status: "detailed-summary"
source_url: "https://support.google.com/googleplay/android-developer/answer/10788890?hl=en"
source_url_announcement: "https://support.google.com/googleplay/android-developer/answer/16926792?hl=en"
source_url_announcement_alias: "https://support.google.com/googleplay/android-developer/answer/16911971?hl=en"
source_url_owner_transfer: "https://support.google.com/googleplay/android-developer/answer/16909862?hl=en"
source_url_identity_verification: "https://support.google.com/googleplay/android-developer/answer/10841920?hl=en"
source_url_app_transfer: "https://support.google.com/googleplay/android-developer/answer/6230247?hl=en"
source_url_policy_blog: "https://android-developers.googleblog.com/2026/04/giving-users-clearer-choice-and-everyone-a-safer-more-trusted-app-ecosystem.html"
source_url_transfer_form: "https://support.google.com/googleplay/android-developer/contact/general_contact"
effective_date: "official feature required from 2026-05-27, which has passed; announcement 30-day wording kept separate; no 2027-01-27"
---

# Google Play 开发者账号所有权转移

> **导入说明（Google batch 7）。** 正文来自已经分开的 2026-10-24 Google Play 知识库快照（`play.account-ownership-transfer`，核对日 2026-10-24）的改写摘要，不是官方页面的逐字副本。英文官方页面是效力来源。`kb_checked_at` 是快照源文件记录的核对日；本次导入没有重新打开线上官方页面。文中“本知识库”“本库”“本地专题”等说法描述的是该快照库的覆盖范围，不是本仓库已经导入的页面。指向本仓库没有收录的专题、链接图、台账或 CSV 的相对链接改为文字提及。指向 Google batch 1–6 或本批十二个专题的相对链接改为本仓库文件。核对日 2026-10-24。两种语言文件引用的都是英文 `hl=en` 帮助 URL。快照写明简体中文帮助路由无法访问。本仓库中文正文是编辑改写。该访问失败不是政策变更。政策于 2026-04-15 公告。官方博客写明自 2026-05-27 起，所有权变更必须使用官方功能。该日期已经过去。公告中的“至少 30 天”与博客的功能切换日保持分开。公告原来的目标 `answer/16911971` 重定向到 Play Console 要求。它不是另一份政策。本页没有记录 2027-01-27。本页是 operational 的所有权流程。它不替代单个应用转移。不能使用本流程的变现个人账号应改走应用转移。公开帮助页不能核验登录后的资格。

**核对日期：2026-10-24。** 本页归纳账号所有权变更的政策边界与当前公开操作说明。它是[Play Console 要求](../play-console-requirements/play-console-requirements.zh-CN.md)中的独立导航专题，依据英文官方正文整理；本轮中文本地化帮助页抓取失败。它不是账号申请或转让表单，也不能替代登录后的 Play Console 对资格、验证进度或个案状态的判断。

## 先区分两种转移

| 目标 | 应使用的流程 | 主要边界 |
| --- | --- | --- |
| 转移整个开发者账号的所有权 | Play Console 的 **Users and permissions → Manage → Make account owner** 流程 | 仅现有账号所有者可发起；接收人是账号内现有用户，并须满足资格和身份验证要求。 |
| 只迁移一个或多个应用 | [单个应用转移流程](https://support.google.com/googleplay/android-developer/answer/6230247?hl=zh-CN) | 这是独立的应用迁移请求，涉及原/目标账号有效状态、注册交易 ID、签名、付款和集成服务等；细节见[Play Console 要求专题](../play-console-requirements/play-console-requirements.zh-CN.md#单个应用转移前置条件和影响)。 |

不要为迁移应用而交出整个开发者账号。反之，如果业务变更确实要转移整个账号的控制权，也不能用只迁移应用来假装完成账号所有权变更。

## 政策要求与时间

Google Play 要求开发者账号的所有权保持透明、可追责。收购、组织重组、人员变动等正当业务原因可以触发正式转移；转让方和接收方均须对转移期间（包括过渡期）的账号行为负责。账号转移必须使用 Play Console 正式流程。

- **禁止的做法：** 通过第三方市场或其他不正当方式购买、出售或租用开发者账号；分享登录凭证进行非正式转让也不允许。
- **生效/流程日期：** 2026-04-15 公告宣布新政策；Google 官方博客明确自 **2026-05-27** 起，账号所有权变更必须使用官方功能。该日期已过。公告中的“至少 30 天”与博客给出的功能切换日期是不同表述，执行时应以现行正式政策和账号内通知为准。
- **公告链接现状：** 公告内的 Account Transfer 链接原始目标为 [answer/16911971](https://support.google.com/googleplay/android-developer/answer/16911971)，目前重定向到[Play Console Requirements](https://support.google.com/googleplay/android-developer/answer/10788890)。当前政策正文在该帮助页的 **Account Transfers** 部分；具体步骤见[所有权转移操作帮助页](https://support.google.com/googleplay/android-developer/answer/16909862?hl=en)。

## 资格与主要阻断条件

| 情形 | 当前帮助页说明 |
| --- | --- |
| 可走直接所有权变更 | Organization 账号，以及不通过应用变现的 Personal 账号；须提交要求的信息并通过适用的身份验证。 |
| 不能走直接变更 | 正在变现应用的个人开发者账号目前不符合直接转移资格；须创建另一个开发者账号，再单独迁移应用。 |
| 账号或流程可能被阻断 | 账号有待完成的验证或不符合良好状态要求；付款资料更改或账号类型切换待处理；上传密钥重置或应用转移正在进行；或者接收人已有其他 Play Console 开发者账号。具体资格提示由 Console 按账号状态显示。 |
| 现所有者无法联系 | 当前不能通过自助流程完成；通过 Play Console Help 联系支持。没有 Console 访问权时，可查看[公开问题报告表](https://support.google.com/googleplay/android-developer/contact/general_contact)；页面虽可公开阅读，但提交及个案处理需要提供账号信息。 |

## 账号所有者变更的操作阶段

1. **由现所有者发起。** 现所有者登录 Play Console，进入 **Users and permissions**，在接收人的 **Manage** 页面选择 **Make account owner**。接收人必须是账号内的既有用户；Console 会判断其是否符合所有者资格。
2. **按账号类型选择变更关系。** Organization 账号要说明接收人仍属于同一组织还是来自新实体。同组织转移可复用现有账号资料，但接收人须对所需 Google Payments 资料拥有管理员权限；不同实体需选择付款资料用于身份核验。个人账号接收人须选择或创建一个仅用于身份核验的付款资料。
3. **提交并进入 7 天安全等待期。** 发起后，现所有者和拥有全部应用访问权限的管理员会收到邮件，团队成员会收到 Console 通知。等待期间账号内任何用户都可取消请求；这段时间用于发现错误或未经授权的接管。
4. **由接收人完成最终设置。** 7 天结束后，接收人会收到完成邀请。接收人开始最终转移步骤后，账号其他用户不能再取消。设置向导可能要求付款资料、组织类型/规模和组织电话（网站可选）、联系人姓名、经一次性验证码验证的联系邮箱和电话，以及面向用户展示的开发者电话和邮箱。
5. **按需完成额外身份核验。** Google 可能要求接收人提交身份证明文件，并通过后续邮件告知上传方式。文件不符合要求会被拒绝；帮助页没有给出适用于所有地区/账号的统一审核结果或时长。

### 7 天等待期的责任与安全含义

等待期是账号安全措施，不是 Google 对买卖账号或业务交易的批准。转让方与接收方在整个过渡阶段仍须遵守 Play 政策，并对各自账号操作负责。开始最终转移前，应确认接收人身份、组织归属、付款资料权限和待处理验证；如出现非本人请求，应在等待期内取消并联系支持。

## 直接来源与子链接关系

| 页面/目标 | 本专题中的作用与核验状态 |
| --- | --- |
| [Account Transfer 公告](https://support.google.com/googleplay/android-developer/answer/16926792?hl=en) → [原始政策链接 answer/16911971](https://support.google.com/googleplay/android-developer/answer/16911971) → [当前 Play Console Requirements](https://support.google.com/googleplay/android-developer/answer/10788890?hl=en) | 公告说明新政策；原始目标已重定向至当前要求页，`Account Transfers` 正文包含所有权透明、正式流程、过渡责任、禁用非正式市场转让以及单应用迁移的分流。 |
| [Transferring ownership of a Play Console developer account](https://support.google.com/googleplay/android-developer/answer/16909862?hl=en) | 2026-10-24 已重开完整正文。它展开 UI 步骤、组织/个人账号资料分支、七天等待期、最终向导、资格和阻断条件；其账号表单和状态仍需登录验证。 |
| [Verify your developer identity information](https://support.google.com/googleplay/android-developer/answer/10841920) | 所有权转移向导的“资料与验证要求”直链。该目标已有身份资料、联系资料、文件和地区差异专题；地区文件选择器及部分支持流程仍不完全覆盖。 |
| [Transfer apps to a different developer account](https://support.google.com/googleplay/android-developer/answer/6230247?hl=en) | 变现个人账号不能直接转移所有权时的替代路线，也适用于只迁移应用。正文和 18 个可见文章级目标均在台账中有访问状态；更深 API/服务后代仍部分覆盖。 |
| [Report an Issue 表单](https://support.google.com/googleplay/android-developer/contact/general_contact) | 公开表单说明适用的账号/支持问题路径；本库已读取字段和说明但未提交。帮助页另一“联系支持”点击在抓取时返回 Internal Error，未暴露可核实目标 URL。 |

所有权操作帮助页的 10 项通用侧栏导航与正文链接分开登记。本文已跟进高影响政策、身份验证和单应用迁移子页，但没有递归展开身份资料专题的全部地区文件、Console 表单和各类外部后代；逐 URL 的当前状态见来源审计表（快照：`source-page-audit.csv`，未导入本仓库）。

## 相关本地专题

- [Play Console 要求：账号资格、身份信息和应用迁移](../play-console-requirements/play-console-requirements.zh-CN.md)
- Android 开发者验证[Android 开发者验证](../android-developer-verification/android-developer-verification.zh-CN.md)
- [Google Play 开发者计划政策](../developer-program-policy/developer-program-policy.zh-CN.md)
