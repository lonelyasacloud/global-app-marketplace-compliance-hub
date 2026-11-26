---
id: google-play.ai-generated-content
platform: google-play
language: zh-CN
authority: normative
status: current
kb_checked_at: 2026-10-24
review_due: 2027-01-24
regions: [global]
topics: [ai, generative-ai, content-safety, restricted-content, moderation]
snapshot_id: play.ai-generated-content
snapshot_package: "GooglePlay-KnowledgeBase-2026-10-24-review.zip"
coverage_status: "detailed-summary"
source_url: "https://support.google.com/googleplay/android-developer/answer/13985936?hl=en"
effective_date: "current-policy"
---

# Google Play AI 生成内容政策与安全实践

> **导入说明（Google batch 4）。** 本页正文取自 2026-10-24 Google Play 知识库快照里已经分开的中文改写（`play.ai-generated-content`，核对日 2026-10-24）。它不是官方页面的逐字文本。英文官方来源是效力来源。`kb_checked_at` 使用快照源文件记录的核对日；本次导入没有重新打开线上官方页面。文中“本知识库”“本库”“本地专题”描述的是该快照知识库的覆盖范围，不是本仓库已经导入的页面清单。快照里指向尚未导入本仓库的专题、链接图、台账或 CSV 的相对链接，已改为文字提及；指向 Google batch 1–3 或本批十二个专题的相对链接已改到本仓库路径。快照记录的政策、范围说明、最佳实践和 2026-08-25 安全博客都是英文官方地址。快照没有记录已核对的中文官方 AI 生成内容页面。本中文页是快照的编辑改写，不是 Google 已发布中文页面的逐字文本。本政策没有记录未来生效日。该博客重申现行禁止事项，并写明没有新增日期或固定审核时限。OWASP GenAI Red Teaming Manual v1.0 的 2026-10-20 是来源日期，不是 Play 截止日期。博客所链的旧政策路由 `answer/13823020` 返回 404；快照改以可访问的现行页 `answer/13985936` 为准，且不把主题相同当成两条路由等价。该抓取失败不表示政策已经变更。应用内举报、受限输出预防和遵守其他 Play 政策是 `normative`。SAIF、OWASP、模型供应商文档和 Android 提示注入指南是实现或行业参考，不是 Play 义务或认证。OWASP 手册一节保留快照中的 CC BY-SA 4.0 改写说明；该许可说明只覆盖快照对那份手册的改写摘要。

**核对日期：2026-10-24。** 本专题整理 Google Play 的 AI 生成内容政策、适用范围说明和安全最佳实践，并把政策义务与实施参考分开。本文为双语改写摘要，不是官方政策全文。

## 核心要求

| 类型 | 要求 |
| --- | --- |
| 政策义务 | 生成式 AI 应用须遵守所有适用的 Google Play 开发者政策，并防止生成受限内容，包括危害儿童或帮助欺骗用户的内容。 |
| 政策义务 | 应用须提供应用内举报或标记功能，让用户无需离开应用即可报告冒犯性输出。 |
| 政策义务 | 开发者应利用用户报告改进内容过滤和审核。 |
| 最佳实践 | Google Play 建议采用符合行业标准的安全测试与安全实践；过滤器和分类器可用于阻止有害输入和输出。 |
| 最佳实践参考 | 可参考 Google SAIF 与 OWASP GenAI Red Teaming Guide。供应商文档是实现参考，不代表 Google Play 对某个产品的认可或强制要求。 |

## 适用范围

政策中的 AI 生成内容，是生成式 AI 模型根据用户提示创建的内容。当前说明涵盖文字、语音和图像提示的不同组合，示例包括：

- AI 聊天机器人对话是应用核心功能的文字生成应用。
- 根据文字、图像或语音提示生成图像或视频的应用。
- 使用 AI 生成真实人物声音或视频记录的应用。

官方范围说明目前不针对以下有限用途应用：

- 只能托管 AI 生成内容、不能使用 AI 创作内容的应用；若此类应用提供 UGC，仍须核对[用户生成内容政策](../user-generated-content/user-generated-content.zh-CN.md)。
- 唯一功能是概括非 AI 生成内容的应用，例如搜索结果或书籍摘要。
- 仅用 AI 改进既有功能的生产力应用，例如邮件草稿建议。

这些是官方说明截至本次核对时列出的范围例子。“目前不涵盖”不构成其他政策的豁免；产品加入新的生成、分享、推荐或变现功能时，应重新评估适用政策。

## 违规输出示例

官方列举的示例并非穷尽清单，包括：未经同意的性深度伪造、协助诈骗的真实人物声音或视频、鼓励危险活动或自残的内容、明显虚假或欺骗性的选举内容、用于霸凌或骚扰的输出、主要用于性满足的生成式 AI 应用、助长不诚实行为的伪造官方文件，以及恶意代码生成。

判断时应结合 [不当内容政策](../inappropriate-content/inappropriate-content.zh-CN.md)、[儿童安全与年龄限制专题](../age-restricted-child-safety/age-restricted-child-safety.zh-CN.md)、[欺骗性行为政策](../deceptive-behavior/deceptive-behavior.zh-CN.md)及其他适用政策；示例不能替代对具体输出、提示词和应用功能的审核。

## 上线与持续运营核对清单

1. 盘点所有模型、提示入口和生成媒介，包括文字、语音、图像与视频；标明生成内容是否涉及真实人物。
2. 为可能触发受限内容的输入和输出设计防护，并针对滥用场景测试过滤和分类效果。此项是落实安全责任的工程建议，不是官方指定的模型或阈值。
3. 在生成内容旁提供容易找到的应用内举报/标记入口；确认用户不必跳出应用才能提交。
4. 让举报进入有人负责的审核流程，记录类别、处理结果与复发情况，并据此迭代过滤和审核。
5. 把安全评估覆盖到模型、应用实现、基础设施和运行时行为；定期重测模型或提示流程变更造成的风险。
6. 若输出可被其他用户查看、分享、评论或推荐，同时核对 [UGC 与内容审核专题](../user-generated-content/user-generated-content.zh-CN.md)以及儿童、隐私和分级要求。
7. 功能、模型、目标用户或内容分发方式改变时，重新审查 Developer Policy Center 和 Play Console 中的相关申报。

## 政策正文、范围说明与直接链接审计

### AI-Generated Content 政策正文

| 正文直接链接 | 与本政策的关系 |
| --- | --- |
| [Policy Coverage](https://support.google.com/googleplay/android-developer/answer/10146128?hl=en) | 说明 Play 政策适用于应用展示或链接的内容、广告、UGC 和公开开发者资料。 |
| [Restricted Content](https://support.google.com/googleplay/android-developer/topic/9877467?hl=en) | 受限内容政策集合；具体主题在下表列出。 |
| [Child Endangerment](https://support.google.com/googleplay/android-developer/answer/9878809?hl=en) | AI 输出涉及儿童剥削或虐待内容时适用；见[儿童安全专题](../age-restricted-child-safety/age-restricted-child-safety.zh-CN.md)。 |
| [Deceptive Behavior](https://support.google.com/googleplay/android-developer/answer/17006354?hl=en) | 约束助长欺骗或不诚实行为的输出；见[本地专题](../deceptive-behavior/deceptive-behavior.zh-CN.md)。 |
| [Best Practices to Safeguard AI-Generated Content](https://support.google.com/googleplay/android-developer/answer/16353813?hl=en) | Google Play 的 AI 安全最佳实践文章；其直接外部资源见下节。 |

政策页面的 Restricted Content 导航列出以下 10 个主题。它们是主题目录链接；AI 安全应用须按其内容和功能判断哪些主题适用。

| 政策主题 | 官方页面 | 本地专题 |
| --- | --- | --- |
| Child Endangerment | [官方页面](https://support.google.com/googleplay/android-developer/answer/9878809?hl=en) | [儿童安全与年龄限制](../age-restricted-child-safety/age-restricted-child-safety.zh-CN.md) |
| Inappropriate Content | [官方页面](https://support.google.com/googleplay/android-developer/answer/9878810?hl=en) | [不当内容](../inappropriate-content/inappropriate-content.zh-CN.md) |
| Financial Services | [官方页面](https://support.google.com/googleplay/android-developer/answer/9876821?hl=en) | [金融服务与贷款](../financial-services-and-loans/financial-services-and-loans.zh-CN.md) |
| Real-Money Gambling, Games, and Contests | [官方页面](https://support.google.com/googleplay/android-developer/answer/9877032?hl=en) | [真钱赌博](../real-money-gambling/real-money-gambling.zh-CN.md) |
| Illegal Activities | [官方页面](https://support.google.com/googleplay/android-developer/answer/9878877?hl=en) | [非法活动](../illegal-activities/illegal-activities.zh-CN.md) |
| User Generated Content | [官方页面](https://support.google.com/googleplay/android-developer/answer/9876937?hl=en) | [UGC 与内容审核](../user-generated-content/user-generated-content.zh-CN.md) |
| Health Content and Services | [官方页面](https://support.google.com/googleplay/android-developer/answer/16679511?hl=en) | 健康应用与 Health Connect（快照：`health-apps-and-health-connect.md`，未导入本仓库） |
| Blockchain-based Content | [官方页面](https://support.google.com/googleplay/android-developer/answer/13607354?hl=en) | [加密资产与 NFT](../crypto-assets-and-nfts/crypto-assets-and-nfts.zh-CN.md) |
| AI-Generated Content | [官方页面](https://support.google.com/googleplay/android-developer/answer/13985936?hl=en) | 本专题 |
| Age-Restricted Content and Functionality | [官方页面](https://support.google.com/googleplay/android-developer/answer/16302250?hl=en) | [儿童安全与年龄限制](../age-restricted-child-safety/age-restricted-child-safety.zh-CN.md) |

### 适用范围说明页面

[Understanding Google Play’s AI-Generated Content policy](https://support.google.com/googleplay/android-developer/answer/14094294?hl=en) 直接关联不当内容、儿童剥削/虐待内容、欺骗性行为和 Developer Policy Center；正文还指出纯托管 AI UGC 时应核对 [User Generated Content](https://support.google.com/googleplay/android-developer/answer/9876937?hl=en)。其 Related Content 导航还列出 AI policy、Restricted Content、Deceptive Behavior 和 Families Policies。对应的关键中文专题已分别交叉链接；Help Center 的通用 32 项学习侧栏不等同于该文章正文子链接。

### 最佳实践页面的直接安全资源

[Best Practices to Safeguard AI-Generated Content](https://support.google.com/googleplay/android-developer/answer/16353813?hl=en) 的正文直接列出 SAIF、OWASP，以及 8 家提供方的安全资源。Google Play 将它们作为安全参考；除 Play 自己的规则外，不能将第三方文档转述为 Play 合规义务。

| 资源 | 页面 | 与 Play 要求的关系 |
| --- | --- | --- |
| Google Secure AI Framework（SAIF） | [框架总览](https://saif.google/secure-ai-framework) | 以数据、基础设施、模型和应用等维度组织 AI 风险与控制。已打开[地图说明](https://saif.google/secure-ai-framework/saif-map)、[组件](https://saif.google/secure-ai-framework/components)、[风险](https://saif.google/secure-ai-framework/risks)、[控制](https://saif.google/secure-ai-framework/controls)、[AI 开发入门](https://saif.google/ai-development-primer)和[风险自评](https://saif.google/risk-self-assessment)。页面还直接链接[CoSAI Risk Map 开源仓库](https://github.com/cosai-oasis/secure-ai-tooling/tree/main/risk-map)，已打开；面向 Agent 的[专用图示](https://gweb-saif-stg.appspot.com/focus-on-agents)跳转 Google 登录，本次无法读取。SAIF 明确说明其内容用于行业参考，不代表 Google 当前技术实现。 |
| OWASP GenAI Red Teaming Guide | [指南介绍](https://genai.owasp.org/resource/genai-red-teaming-guide/) · [指南 PDF](https://genai.owasp.org/download/44859/) | 指南介绍页涵盖模型评估、实现测试、基础设施评估和运行时行为；2025 PDF 曾打开，本次重新点击下载超时。该资源还链接 [GenAI Red Teaming Manual v1.0（2026-10-20）](https://genai.owasp.org/resource/genai-red-teaming-manual-version-1-0/)及其[144 页 PDF](https://genai.owasp.org/download/58204/)，本专题已打开并概括与 AI 内容安全相关的章节（见下节）；同时列出 [Agent Control Standard](https://genai.owasp.org/resource/agent-control-standard-acs/) 和 [GenAI Security Industry Framework Crosswalk](https://genai.owasp.org/resource/genai-security-industry-framework-crosswalk/)。这些均为 OWASP 参考，不是 Play 义务或认证。 |
| Google Responsible GenAI Toolkit | [资源](https://ai.google.dev/responsible) | Google 开发者侧的责任 AI 设计、评测和防护资料；属于实施参考。 |
| Microsoft AI Content Safety | [产品资料](https://azure.microsoft.com/en-us/products/ai-services/ai-content-safety) | 厂商内容过滤资料；不是 Play 认证。 |
| OpenAI Safety best practices | [开发者指南](https://developers.openai.com/api/docs/guides/safety-best-practices) | API 实施安全建议；不是 Play 政策。 |
| Anthropic Content Moderation | [使用场景指南](https://platform.claude.com/docs/en/about-claude/use-case-guides/content-moderation) | 厂商审核建议；不是 Play 政策。 |
| AWS Responsible Content Moderation | [方案资料](https://docs.aws.amazon.com/solutions/responsible-content-moderation-with-ai-services-on-aws/) | AWS 方案参考；不是 Play 政策。 |
| Meta Responsible Use Guide | [指南 PDF](https://ai.meta.com/static-resource/responsible-use-guide/) | Meta 责任使用参考；不是 Play 政策。 |
| Salesforce Trusted AI | [资源](https://www.salesforce.com/artificial-intelligence/trusted-ai/) | Salesforce 信任与安全资料；不是 Play 政策。 |
| Cohere Safety Modes | [文档](https://docs.cohere.com/docs/safety-modes) | Cohere 特定模型的安全模式资料；不是 Play 政策。 |

### OWASP GenAI Red Teaming Manual v1.0（2026-10）

[OWASP 资源介绍页](https://genai.owasp.org/resource/genai-red-teaming-manual-version-1-0/)于 2026-10-20 发布；其[144 页 PDF](https://genai.owasp.org/download/58204/)标为 Version 1.0、2026 年 10 月。本摘要打开并审阅了目录、许可和与 AI 应用安全/内容安全相关章节，不是对 144 页逐页转写。手册没有制定 Google Play 规则；它扩展了 Play 最佳实践中对 OWASP 安全测试参考的指引，不构成 Play 审核标准、认证或新增合规义务。

该手册按八阶段组织红队工作：

1. **Planning & Scoping（计划与范围）**：约定系统、模型、数据、身份权限、测试目标、成功判据、规则和停止条件；记录不在范围内的外部服务。
2. **Reconnaissance & Fingerprinting（侦察与指纹识别）**：整理公开资料、依赖与供应链线索，并标注哪些判断仍是假设。
3. **Surface Mapping（攻击面映射）**：梳理模型编排、检索/RAG、工具接口、信任边界和数据流，形成威胁模型。
4. **Exploitation & Impact（利用与影响）**：按风险检查直接模型弱点、应用调用路径、多模态输入、Agent 动作、资源耗尽，以及输入/输出护栏和安全分类器的绕过。
5. **Persistence & Escalation（持久化与权限提升）**：检查数据外泄、Agent 权限提升和跨轮次/状态持久化。
6. **Post-Exploitation（利用后评估）**：验证攻击者实际能力、影响范围、业务与安全后果、严重度及应急遏制方案。
7. **Evaluation & Reporting（评估与报告）**：预先定义通过/失败/需人工判断的标准；保存可复现证据、测试覆盖、预算和局限。日志或遥测缺失不能当作防护通过。
8. **Post-Engagement & Remediation（测试后修复）**：修复护栏和架构缺口，复测修复效果，把已确认攻击转成回归用例，并更新监控与响应流程。

**对 Google Play AI 应用的落地关系：** 按应用实际输入、输出、检索和工具路径设计测试；把 Play 明确禁止的受限内容类别作为测试范围参考，并验证用户能在应用内报告/标记冒犯性输出、开发者有后续审核处理流程。发版前、接入新模型或功能后，以及调整模型/护栏/检索/Agent 工具后都可运行回归。优先使用隔离环境、专用测试账户、合成数据和模拟工具，避免测试触达真实用户数据或生产操作。以上是对 OWASP 方法的应用建议；Play 的报告/标记和内容政策义务仍以 Google 官方政策为准。

**来源许可：** 原手册标注 [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/legalcode)。本节为基于 OWASP GenAI Security Project《GenAI Red Teaming Manual v1.0》（2026-10）的中文改写摘要，并非官方原文；本节摘要遵循相同许可。知识库其他部分的来源及许可须分别查看各自原文。

最佳实践文章的 Related Content 还链接 AI-Generated Content、Restricted Content、Deceptive Behavior 和 [Google Play Families Policies](https://support.google.com/googleplay/android-developer/answer/9893335?hl=en)。上述 SAIF/OWASP 页面和供应商资料自身仍有更深的站内链接；本专题只把已打开的关键后代列出，不宣称这些外部站点已递归闭包。官方页面的 Help Center 32 项通用侧栏也不作为正文直链计算。

### 官方 AI 安全博客：非自愿私密影像与审核准备（2026-08-25）

[Ensuring Safety in the Generative AI Ecosystem: Protecting Users from Non-Consensual Intimate Content](https://developer.android.com/blog/posts/ensuring-safety-in-the-generative-ai-ecosystem-protecting-users-from-non-consensual-intimate-content) 是 Google Play/Android 官方开发者博客，不属于 Help Center 的 58 条公告目录。文章重申 Play 禁止协助、创建或传播未经同意的性内容，并针对生成式 AI 的非自愿私密影像（NCII）、“nudify/undress”功能、深度伪造和露骨图像编辑提出审核准备与安全实践；没有新增日期或固定审核时限。

| 正文直接链接 | 页面内容与关系 | 访问与范围 |
| --- | --- | --- |
| [Priority Flagger Program](https://transparency.google/intl/en_uk/tools-programs/partner-programs/) | 自愿的组织合作项目，为符合条件的机构提供专门举报渠道和政策交流；举报会优先审阅，但不会自动删除，也不适用不同内容标准。 | 正文目标已读；页面的 DSA、版权与儿童安全工具子链见递归图 §4.142（快照：`../google-play-policy-link-graph.md`，未导入本仓库）。 |
| [Sexual Content and Profanity / Inappropriate Content](https://support.google.com/googleplay/android-developer/answer/9878810?hl=en) | 正式 Play 政策禁止未经同意的性内容，以及声称“脱衣/透视衣物”的应用和通过深伪制作的非自愿性内容；对应[不当内容专题](../inappropriate-content/inappropriate-content.zh-CN.md)。 | 现行政策正文及示例已读；博客中的 NCII 说明与现行条文交叉核对。 |
| [AI-Generated Content policy（博客所链 answer/13823020）](https://support.google.com/googleplay/android-developer/answer/13823020) | 博客明确把 AI 内容政策作为依据；但所链 ID 本次返回 404。知识库另有可访问的现行 [AI-Generated Content 页面 answer/13985936](https://support.google.com/googleplay/android-developer/answer/13985936?hl=en)，不能仅据主题相同就认定两条路由等价。 | 原始目标无法读取；以当前可访问政策页为准，旧链接关系仍待 Google 修复/确认。 |
| [Best Practices to Safeguard AI-Generated Content](https://support.google.com/googleplay/android-developer/answer/16353813?hl=en) | Play 建议依行业标准开展安全测试，可组合过滤器/分类器，并参考 SAIF、OWASP 与模型供应商资料；开发者仍对应用输出负责。 | 已有正文和 10 个直接安全资源摘要，见本专题“最佳实践页面的直接安全资源”及 §4.142。 |
| [App Promotion policy](https://support.google.com/googleplay/android-developer/answer/9899004?hl=en) | 即使应用本身没有“脱衣”功能，在商店外宣传此类能力也可能违反应用推广政策；推广内容须准确反映真实应用。 | 已有双语政策摘要；具体适用仍依现行政策与宣传内容判断。 |
| [Google Ads: Inappropriate content](https://support.google.com/adspolicy/answer/6015406?hl=en) | Google Ads 另行禁止推广合成露骨/裸露内容；页面说明严重违规可导致 Ads 账号停用。博客同时提醒开发者对应用广告负责，含授权第三方制作的广告。 | Ads 页面已打开；这是 Ads 投放政策和账号执法，不等同于 Play 上架政策。 |
| [Android core practices（实际目标：Mitigate prompt injection attacks）](https://developer.android.com/privacy-and-security/risks/ai-risks/prompt-injection) | Android 指南建议限制模型权限、隔离不可信输入、校验输出、对高风险动作要求人工确认并定期做对抗测试。 | 正文的 6 个参考链接位置归并为 5 个目标槽位，其中 4 个 href 可核验；另一个 Vertex AI 锚点未暴露 href。属于 Android 安全实施参考，不是 Play 新义务，摘要见 §4.142。 |
| [Report a Policy Violation](https://support.google.com/googleplay/android-developer/contact/policy_violation_report?rd=1) | 面向 Google Play 已发布应用的政策违规举报入口；要求选择问题类别并提供包名和善意、可支持的举报信息。 | 表单已打开；它是举报渠道，不是政策正文或违规裁定。 |

**应用检查要点（博客建议）：** 审核测试账号应能完整使用 AI 功能，包括付费或地区限制功能，不要让订阅墙阻断审核；保留对抗提示、边界情况及模型拒绝能力的测试证据，特别覆盖 nudify/undress、深伪和露骨图像编辑/生成；不要只依赖底层模型自带过滤，需在应用输入/输出加控制并持续监测用户反馈与失败提示。文章表示复杂 AI 安全评估和申诉有时会更久，但没有承诺或规定具体时长。把这些作为审核准备和工程操作检查点，不误写成新增截止日期或政策条款。

**递归边界：** 本次覆盖博客正文 8 个唯一目标、Android 提示注入指南的 6 个参考链接位置（5 个去重目标槽位，其中 4 个 href 可验证）、Priority Flagger 页面 4 个正文子目标，以及一篇“Continue reading”关联文章。AI 政策旧目标返回 404，DSA Trusted Flagger 入门页需要指定身份且本次不可读；OWASP 研究文献、Android/Google 工程资源自身的全部外部后代及通用导航没有穷尽。目标级状态见 source-page-audit.csv（快照：`../source-page-audit.csv`，未导入本仓库）。

## 来源与关联专题

- [AI-Generated Content policy](https://support.google.com/googleplay/android-developer/answer/13985936?hl=en) · [范围说明](https://support.google.com/googleplay/android-developer/answer/14094294?hl=en) · [安全最佳实践](https://support.google.com/googleplay/android-developer/answer/16353813?hl=en)
- [Policy Coverage](https://support.google.com/googleplay/android-developer/answer/10146128?hl=en) · [Restricted Content](https://support.google.com/googleplay/android-developer/topic/9877467?hl=en) · [Developer Policy Center](https://play.google.com/about/developer-content-policy/)
- [UGC 与内容审核](../user-generated-content/user-generated-content.zh-CN.md) · [不当内容](../inappropriate-content/inappropriate-content.zh-CN.md) · [欺骗性行为](../deceptive-behavior/deceptive-behavior.zh-CN.md) · [儿童安全与年龄限制](../age-restricted-child-safety/age-restricted-child-safety.zh-CN.md)
