---
id: google-play.play-integrity-api
platform: google-play
language: zh-CN
authority: operational
status: current
kb_checked_at: 2026-10-23
review_due: 2027-01-23
regions: [global]
topics: [play-integrity, anti-abuse, user-data, privacy, device-recall]
snapshot_id: play.play-integrity-api
snapshot_package: "GooglePlay-KnowledgeBase-2026-10-24-review.zip"
coverage_status: "detailed-summary"
source_url: "https://developer.android.com/google/play/integrity"
source_url_overview: "https://developer.android.com/google/play/integrity/overview"
source_url_terms: "https://developer.android.com/google/play/integrity/terms"
source_url_device_recall: "https://developer.android.com/google/play/integrity/device-recall"
effective_date: "API terms and implementation guidance; not a Play content-policy effective date; no 2027-01-27"
---

# Google Play Integrity API：数据边界、反滥用与实施实践

> **导入说明（Google batch 8）。** 正文来自已经分开的 2026-10-24 Google Play 知识库快照（`play.play-integrity-api`，核对日 2026-10-23）的改写摘要，不是官方页面的逐字副本。英文官方页面是效力来源。`kb_checked_at` 是快照源文件记录的核对日；本次导入没有重新打开线上官方页面。文中“本知识库”“本库”“本地专题”等说法描述的是该快照库的覆盖范围，不是本仓库已经导入的页面。指向本仓库没有收录的专题、链接图、台账或 CSV 的相对链接改为文字提及。指向 Google batch 1–7 或本批十三个专题的相对链接改为本仓库文件。核对日 2026-10-23。两种语言文件使用不带语言参数的 `developer.android.com` 地址。快照没有记录已核对的中文官方条款页，也没有记录 `hl=zh-CN` 抓取失败。中文是编辑改写。Device Recall 的 Beta 表单未能由抓取工具读取。Go 客户端 API 只作为大型参考打开。没有 2027-01-27。该 API 是可选的反滥用设施。条款禁止用它做个人或设备指纹识别和跟踪。这些条款是 API 调用合同，不是 Play 内容政策，也不完成应用自己的 Data safety 表单。证据等级：集成指导为实现说明；API Terms 是调用方合同。

**核对日期：2026-10-23。** 本专题把 API 服务条款、Terms 页面中的 Data safety 说明和 Android 集成最佳实践并列整理。API 是可选的应用安全/反滥用信号，不是所有应用必须接入的 Play 政策要求，也不构成审核批准或豁免。

## 1. 先看有约束力的用途边界

[Play Integrity API Terms of Service](https://developer.android.com/google/play/integrity/terms)规定，API 用于保护应用安全，以及缓解滥用、欺诈和未授权访问；除 API Terms 外，还受 [Google APIs Terms of Service](https://developers.google.com/terms)约束。开发者**不得用 Play Integrity API 对个人用户或设备做指纹识别或跟踪**。功能资格和请求配额可变化；Google 可在应用或 SDK 不再符合条件时移除功能或降低配额；额外功能/配额批准只适用于获批的特定应用或 SDK，不随转让自动转移。

因此，技术文档中讨论的设备/应用完整性、请求验证和风险分层，必须服务于安全与反滥用目的。不能把 verdict、`requestHash`、`nonce`、Device Recall 值或其组合重新用于跨会话身份解析、广告画像、用户/设备跟踪或敏感属性推断。Device Recall 自身也有同样的用途限制。

## 2. API 处理的数据与 Data safety 申报

Terms 页面列明，API 使用时始终处理：

- 应用在请求中提供的信息，包括 `requestHash` 和 `nonce`；
- 应用元数据：包名、版本号、签名证书；
- 设备上已登录 Play 帐号的该应用 Play 授权状态；
- Google Play services 生成的密钥证明证书和设备证明令牌。

只有应用选择接收 environment details 时，才额外处理用于判断是否存在可截屏/控制设备应用的应用活动信息，以及 Google Play Protect 状态。Terms 页面称这些数据经过加密、不传给第三方，并在固定保留期后删除；页面没有公开具体天数，不能擅自补写期限。

API 的数据处理说明**不能替开发者完成应用级 Data safety 判断**。Google 明确由开发者自行决定如何填写其应用的 Data safety 表单。应把 API 与应用自身、后端、集成 SDK 的数据流一起审视；不要仅因 API 页面列出加密/删除特征，就推断 app 的收集、分享、安全实践或申报义务全部自动满足。详见[数据安全专题](../data-safety/data-safety.zh-CN.md)和[用户数据专题](../user-data/user-data.zh-CN.md)。

## 3. 官方集成建议：验证、最小化、分级响应

[Play Integrity 概览](https://developer.android.com/google/play/integrity/overview)建议将 API 放在真实受保护操作附近，优先考虑适用于多数场景、延迟较低的 Standard 请求；Classic 请求成本和延迟更高、消耗更多数据/电量，宜用于低频、高价值或敏感操作。Standard 也需要按官方设计预热 token provider；两类请求都应由服务端解密/验证并在采取动作前核对 verdict。

实施时至少应做到：

1. 将请求绑定到本次操作。Standard 使用 `requestHash`，Classic 使用服务器生成且不可预测的 `nonce`；只纳入验证所需的请求字段，并校验新鲜度/重放。`requestHash`/`nonce` 中的数据对应用和 Google 都以明文可见，敏感内容应先哈希或加密，不要直接放入。
2. 不缓存完整性 verdict；在希望保护的请求发生时重新取值，减少代理重放风险。
3. 先检查 `requestDetails` 与预期请求匹配，再核对 Play 识别的应用完整性和许可状态，之后才按设备信任标签采取分级处理。
4. 对高信任标签以外的结果设计容错策略；高等级设备信号覆盖设备较少，单一强信号拒绝会影响真实用户。根据风险可采用允许、受限、补充验证/修复对话框、拒绝等多档响应。
5. 在强制拦截前先收集遥测、观察不同设备与发行渠道的结果，并为服务异常、错误码和 Play 服务不可用准备回退路径。对可疑高风险动作，优先考虑挑战/补充验证，而不是一律拒绝。

该组是 Android Developers 的实施最佳实践，不能扩写为 Play 审核政策条款。

## 4. Standard、Classic 与服务端验证流程

| 路径 | 适用方式 | 核心安全检查 |
| --- | --- | --- |
| [Standard 请求](https://developer.android.com/google/play/integrity/standard) | 大多数应用；在服务端请求前按需取 token，先预热 provider，通常响应更快。 | 将当前操作摘要绑定到 `requestHash`；客户端把 token 发给自己的后端；后端向 Google Play 解密/验证并将 verdict 与原请求关联。不要缓存 verdict。 |
| [Classic 请求](https://developer.android.com/google/play/integrity/classic) | 少量、高价值或敏感操作的一次性新鲜检查。每次评估成本更高。 | 服务端产生高熵、一次性 `nonce` 并验证 token 的 nonce、请求上下文和时效；处理重放/外泄风险和有限配额。 |
| [Verdict 格式](https://developer.android.com/google/play/integrity/verdicts) | Standard 与 Classic 返回同一类 JSON 字段，含 request、account、app、device 和可选 environment 信息。 | 解码后先核对 `requestDetails` 是否与原始请求一致，再检查各 verdict；不要仅根据客户端可控字段采取高影响动作。 |

新建或配置接入时需 [Google Cloud 项目与 Console 链接](https://developer.android.com/google/play/integrity/setup)。官方设置页当前列出默认每日请求/解密配额、项目关联条件及应用/SDK 的配置差异；具体配额、SDK 版本、资格和 Console 菜单可能变动，应在实施时重看官方页面。本专题不将当前技术版本数字当作长期政策期限。

## 5. Device Recall：有限用途、保留期和共享范围

[Device Recall](https://developer.android.com/google/play/integrity/device-recall)是需申请加入的 Beta。它为同一设备保存最多三个开发者自定义值；开发者只能读写自己关联的有限值，不会获得设备或用户 ID。它可能用于记录严重滥用、已兑换高价值权益或重复创建滥用账号等安全状态。

- 只能用于保护应用安全并缓解滥用、欺诈和未授权访问；同样禁止指纹识别/跟踪用户或设备，也不得记录性别、年龄、位置等敏感特征。
- 该值存放在 Google 服务器；经验证的 token 最长可在 14 天内用于写入；读/写后保留三年。开发者可将该设备三个值都重置为 `false` 以清除并重置时间戳。
- 同一 Play 开发者账号下的应用共享每设备的三个值；应用转移到另一开发者账号后使用新账号的数据。
- 使用者必须满足支持设备、Play Store/Play services 和 Play 授权等前提；功能处于 Beta，须先提交兴趣表并获得批准。

这些自定义值虽不是用户 ID，仍是可跨安装/重置关联特定设备的状态数据；须严格限制用途和访问，并评估应用自己的披露、保存和用户权益要求。不要把“没有提供硬件 ID”误读为可以任意跟踪。

## 6. 直接链接与当前覆盖状态

| 父页 → 子页 | 内容关系与本轮审计状态 |
| --- | --- |
| [Play Integrity API 首页](https://developer.android.com/google/play/integrity) → 概览、[Setup](https://developer.android.com/google/play/integrity/setup)、[API 类索引](https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/classes)、[IntegrityManager API 参考](https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/integrity/IntegrityManager)、[Additional tools and support](https://developer.android.com/google/play/integrity/additional-tools) | 核对服务目的、入口结构及集成前提；类索引是大型 API 目录，IntegrityManager 只核对请求/对话框相关成员，未逐类/逐成员穷尽。 |
| 概览 → Standard、Classic、Verdicts、[Remediation](https://developer.android.com/google/play/integrity/remediation)、[Error codes](https://developer.android.com/google/play/integrity/error-codes)、Device Recall、Terms | 已读核心请求、核验与策略建议；Remediation 的新 token/服务端检查流程及错误重试只有相关章节选读。Verdicts、错误码和引用页非常长，未逐字段/逐成员穷尽。 |
| Terms → [API Terms 与 Data safety 表单](https://developer.android.com/google/play/integrity/terms) | 已读全部服务条款与 Data safety 表格，确认不得跟踪/指纹识别、用途、收集字段、加密/分享/删除说明及开发者的表单责任；条款页面标注最后修改 2024-05-20，页面更新时间 2026-10-06。 |
| Terms → [Play Developer Help: Data safety](https://support.google.com/googleplay/android-developer/answer/10787469) 与 [消费者 Data safety 说明](https://support.google.com/googleplay/answer/11416267) | 与现有双语 Data safety 专题交叉核对。开发者帮助页是 app 级表单规则，消费者页面解释展示标签；两者不能由 API 自身的处理表格替代。 |
| Terms → [Essential Contacts](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts)、[Play 状态面板](https://status.play.google.com/)、[Integrity release notes](https://developer.android.com/google/play/integrity/reference/com/google/android/play/core/release-notes)、[Play Console 新功能](https://google.play/business/whats-new/)、[Android Developer Newsletters](https://developer.android.com/newsletter)、Android Developers Blog | Essential Contacts 指南建议为账单、法律、安全、产品更新等重要类别指定团队邮箱并定期核对联系人；它帮助接收 Cloud 通知，不是 Play 应用政策。状态页已打开；release notes 只打开目录、未汇总各版本差异；新闻/简报与通用博客目录不扩展为全站递归抓取。 |
| 概览 → [硬件密钥证明](https://developer.android.com/privacy-and-security/security-key-attestation)、[内容绑定](https://developer.android.com/google/play/integrity/standard#bind-integrity-verdicts-to-a-request)、[Classic nonce](https://developer.android.com/google/play/integrity/classic#protect-against-replay-attacks) | 与证明信号、请求绑定和重放防护直接相关。内容绑定与 nonce 小节已核对；密钥证明页面只作选读，Android 安全实现与 API 类型的更深后代仍部分覆盖。 |
| Device Recall → [Beta 兴趣表](https://forms.gle/2d24B4gNyoVrqztG6)、读取/写入、[服务端解码](https://developer.android.com/google/play/integrity/verdicts#decode-the-integrity-verdict) 与 [Go 客户端 API](https://pkg.go.dev/google.golang.org/api/playintegrity/v1) | 重点限制和生命周期已核对。Beta 表单跳转到需要 Google 表单交互的目标，抓取工具无法读取；Go API 是大型技术参考，只打开目标页，未审完成员。它们不等于 Play 政策；所有语言库、代码样例与引用成员未穷尽。 |

官方页面还提供测试响应、设备活动/环境信号、自动保护、签名、ReCAPTCHA 和支持路由。自动保护、Play App Signing、ReCAPTCHA、通用 Android 安全指南各有独立专题或审计；它们不是同一个 Integrity API 功能。Console 设置需登录，个别页面路由未返回可读内容；逐 URL 状态以来源审计台账（快照：`../source-page-audit.csv`，未导入本仓库）为准。

## 与本地专题的关系

- [User Data](../user-data/user-data.zh-CN.md)：标识符、目的限制、透明披露与数据最小化。
- [Advertising ID / App Set ID](../advertising-id/advertising-id.zh-CN.md)：Integrity 用于请求/应用安全检查，不能替代设备广告标识符，也不能用于广告画像/跟踪。
- [Data safety](../data-safety/data-safety.zh-CN.md)：按应用与 SDK 实际数据流申报；API 页面只解释 Google 运营接口自身的数据处理。
- [Device and Network Abuse](../device-and-network-abuse/device-and-network-abuse.zh-CN.md)：安全信号可辅助服务端滥用防护；接入本身不证明应用符合所有设备/网络政策。

本专题是官方英文文档的双语改写，不是条款全文或 API reference 镜像。政策用途限制与技术建议分开标注；大型 API 文档、Console 状态、版本差异和文档后代仍需继续审计。
