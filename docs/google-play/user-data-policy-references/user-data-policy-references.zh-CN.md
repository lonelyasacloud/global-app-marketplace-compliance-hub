---
id: google-play.user-data-policy-references
platform: google-play
language: zh-CN
authority: regulatory
status: current
kb_checked_at: 2026-10-24
review_due: 2027-01-24
regions: [global]
topics: [user-data, prominent-disclosure, cnil, gdpr, dpf, reference]
snapshot_id: play.user-data-references
snapshot_package: "GooglePlay-KnowledgeBase-2026-10-24-review.zip"
coverage_status: "detailed-reference-summary"
source_url: "https://support.google.com/googleplay/android-developer/answer/10144311?hl=en"
source_url_zh: "https://support.google.com/googleplay/android-developer/answer/10144311?hl=zh-Hans"
source_url_disclosure: "https://support.google.com/googleplay/android-developer/answer/11150561?hl=en"
source_url_cnil_pdf: "https://www.cnil.fr/sites/cnil/files/2025-04/recommandation-applications-mobiles-modifiee.pdf"
effective_date: "reference-compilation; not a Play policy; Privacy Shield is historical"
---

# 用户数据政策的外部法律与参考资源

> **导入说明（Google batch 5）。** 正文来自已经分开的 2026-10-24 Google Play 知识库快照（`play.user-data-references`，核对日 2026-10-24）的改写摘要，不是官方页面的逐字副本。英文官方页面是效力来源。`kb_checked_at` 是快照源文件记录的核对日；本次导入没有重新打开线上官方页面。文中“本知识库”“本库”“本地专题”等说法描述的是该快照库的覆盖范围，不是本仓库已经导入的页面。指向本仓库没有收录的专题、链接图、台账或 CSV 的相对链接改为文字提及。指向 Google batch 1–4 或本批八个专题的相对链接改为本仓库文件。 本页是参考汇编。它本身不是 Google Play 规则，不是法律意见，也不是官方全文。英文 User Data 政策是 Play 的效力来源。快照把可读的简体中文 User Data 路由记为 `hl=zh-Hans`。2017 年 6 月公告的英文路由仍返回 HTTP 429；2026-10-24 打开的简体中文 `zh-Hans` 短正文是历史性的 Privacy Shield 文本。CNIL 的英文 PDF 是礼貌译本，只有法文文本具有法律效力。快照没有记录 CNIL、GDPR、EDPB 或 Data Privacy Framework 材料的已核对中文官方页面。这些外部来源的中文枢纽正文是快照的编辑改写。Légifrance 返回 HTTP 403，部分 CNIL 标签页返回 HTTP 503。EUR-Lex 的机器人校验和其他抓取失败是访问限制，不是法律或 Play 政策的变更。Privacy Shield 已于 2020-07-16 被认定无效，属于历史材料。2023-07-10 的 EU–U.S. Data Privacy Framework 充分性决定是快照记录的传输机制，不是未来的 Play 生效日。源文件中的会话回放咨询截止日期 2026-04-22 已经过去，且不是 Play 日期。本页没有记录 2027-01-27。Play 的显著披露最佳实践是操作指导；有约束力的 Play 义务留在 User Data 政策（该页为 `normative`）。CNIL、GDPR、EDPB 和 DPF 材料是监管要求或传输机制，不会因为被链接就并入 Play 政策。

**核对日期：2026-10-24。** 本页承接[用户数据政策](../user-data/user-data.zh-CN.md)中的直接链接，解释每份材料的适用对象、政策关系和访问边界。这里是双语改写与索引，不是官方全文，也不是法律意见。

## 先区分四类要求

| 类型 | 本页资源 | 使用方法 |
| --- | --- | --- |
| Google Play 分发政策 | [User Data](https://support.google.com/googleplay/android-developer/answer/10144311?hl=en) | 决定 Play 分发审核的披露、数据用途、安全、SDK、隐私政策、Data safety 和删除要求；以官方现行正文为准。 |
| Play 最佳实践 | [醒目披露与同意最佳实践](https://support.google.com/googleplay/android-developer/answer/11150561?hl=en) | 说明如何设计披露界面和申报视频；它是实践指南，相关强制义务来自 User Data 等政策条款。 |
| 适用法律及监管指引 | [CNIL 移动应用建议（法文正式文本）](https://www.cnil.fr/sites/cnil/files/2025-04/recommandation-applications-mobiles-modifiee.pdf)、[英文礼貌译本](https://www.cnil.fr/sites/cnil/files/2025-05/recommendation-mobiles-app.pdf) | 对法国/欧洲经济区相关个人数据处理提供移动应用场景的角色分析、解释和建议。英文版便于阅读，但仅法文版具有法律效力；须区分其中的法律义务、建议和良好实践。 |
| 数据传输或合同机制 | [Data Privacy Framework](https://www.dataprivacyframework.gov/program-articles/Participation-Requirements-Data-Privacy-Framework-%28DPF%29-Principles)、[Google Controller Terms](https://business.safety.google/controllerterms/) | 仅在具体数据、参与方、服务、协议和适用机制范围内评估；不能据此推断所有开发者自动受其覆盖。 |

## 醒目披露与同意：把政策变成可检查的界面

Google Play 的最佳实践指南建议：

- 在应用内、接近权限或敏感能力请求的流程中展示；不能只放在商店描述或网站。
- 提供明确的同意以及拒绝/稍后决定选项；用户拒绝或撤回后，应让不依赖该数据的部分继续可用，并尊重重复拒绝。
- 不要仿造 Android 系统权限弹窗。文案应清晰、友善，能让约 13 岁读者理解；可以适当写长，避免术语。
- 用 Why / What / How 组织说明：为何需要能力、涉及哪些数据、数据如何支持核心功能。若 SDK 收集或向第三方分享数据，写清数据类型、用途和接收方。
- 若 Play Console 权限声明要求视频，展示启动应用、到达披露页、完整文字（缓慢滚动到末尾）、同意与拒绝/再次进入的流程，以及使用该能力的核心功能；功能用途不明显时加字幕或旁白。

这是**最佳实践指南**，不能代替强制政策。也不能用它代替隐私政策、Data safety 申报、Android 运行时权限或法律要求的同意；这些是不同控制点，应当彼此一致。指南链接的 Play Academy 课程[Declared permissions and in-app disclosures](https://playacademy.exceedlms.com/student/activity/66910)只有可见课程简介，课程正文/视频无法公开读取；Play Console 声明表需要账号权限。

## CNIL 移动应用建议：补充法国/欧洲隐私合规视角

### 版本与适用边界

现行法文正式文本是 CNIL 2025 年 4 月 8 日发布的[修订版 98 页建议书 PDF](https://www.cnil.fr/sites/cnil/files/2025-04/recommandation-applications-mobiles-modifiee.pdf)。它由 2025 年 3 月 27 日第 2025-024 号决定修订；该决定第 1 条废止 2024 年第 2024-061 号旧决定，第 2 条通过修订版。CNIL 的[修订公告页](https://www.cnil.fr/fr/recommandations-applications-mobiles-modifiee)可读取，并列出正式 PDF、[100 页修订标注版](https://www.cnil.fr/sites/default/files/2025-04/recommandation-applications-mobiles-modifiee_suivi.pdf)和 Légifrance 决定链接。公告称修改主要是纠错、补漏和澄清，未改变整体实质；官方决定记录的搜索索引摘录列出三项重点：修正 SDK 为应用发布者处理定位数据的角色示例；用流程图替换 CMP/系统权限组合顺序的旧表；澄清 SDK 为自身目的处理数据时应在集成合同中约定。Légifrance 目标直开返回 403；上述具体修改来自 CNIL 公告与官方搜索索引摘录，不声称已读到受限的 Légifrance 全文。

从 User Data 原始英文新闻页的“Read the recommendation”链接打开了[93 页英文礼貌译本](https://www.cnil.fr/sites/cnil/files/2025-05/recommendation-mobiles-app.pdf)。封面标注它对应 2025-04-08 的修订建议，但明确说明只有法文版具有法律效力。该译本便于查阅和交叉核对，不替代法文正式文本。建议书面向应用发布者、开发者、SDK 提供商、OS 提供商和应用商店，帮助各方识别 GDPR/ePrivacy 等适用法律下的角色和责任。它把法律义务解释、监管建议与良好实践并列；CNIL 检查清单明确提示其中并非每一项都是强制义务。Google Play User Data 只把 CNIL 资源列作可能有帮助的参考，没有将整份建议书并入 Play 政策。

User Data 正文直接指向的[英文 CNIL 新闻页](https://www.cnil.fr/en/mobile-applications-cnil-publishes-its-recommendations-better-privacy-protection)本轮重新打开：它介绍咨询后发布的移动应用最终建议，说明 CNIL 自 2025 年起会在执法中考虑该建议，并将应用发布者、开发者、SDK、OS 与应用商店列为生态参与方。页面的“阅读建议”链接打开上方 93 页英文礼貌译本。新闻页是监管背景入口，不是 Google Play 政策，也没有把 CNIL 建议自动并入 Play 规则。

### 与 Play 数据要求最相关的内容

| 主题 | CNIL 指引要点 | 与 Play 的关系 |
| --- | --- | --- |
| 角色与 SDK 责任 | 识别发布者、开发者、SDK、OS 和商店各自是控制者、共同控制者还是处理者；建立合作方/SDK 清单，明确指令、合同和责任。 | 与 Play 要求开发者对应用内第三方代码负责相呼应；不能把 SDK 的处理从数据流清单中排除。 |
| 数据最小化与设计 | 盘点数据、权限、用途、保存时间和接收方；只处理服务所需数据；评估本地处理、较低精度/较窄权限和更少数据的实现。 | 支持 Play 的合理预期、必要性、权限最小化和准确申报；CNIL 的工程建议本身不等于 Play 批准。 |
| 用户信息与同意 | 在合适时点用容易找到、易懂的信息说明处理；区分服务必需功能、可选便利功能和为开发者/第三方利益开展的用途；拒绝和撤回应可行且不受强迫。 | 应与 Play 的醒目披露、肯定同意和运行时权限顺序交叉核对；GDPR 同意与 Android 技术权限并非同一概念。 |
| 权限交互 | 对每项权限核实是否必要、是否可替代、能否本地处理、是否能缩短授权范围；考虑用户选择较低精度或部分信息的方案。 | 可用于设计审查，但 Play 对特定权限/敏感 API 仍有自己的声明、用途和审核规则。 |
| 生命周期和安全 | 更新 SDK/依赖，监控新版本，建立安全修复和持续合规流程；让开发者与发布者对隐私影响较大的技术/界面决策留存书面协作。 | 有助于落实持续监控与 SDK 管理，不替代 Play 的具体政策或期限。 |

英文译本的高价值阅读路径：§§2–4（适用范围和参与方角色）、§5.2–5.5（合作方清单、同意/权利、生命周期、权限）、§§6–7（开发者与 SDK）、§9（应用商店）。这些内容用于理解 User Data 的角色与数据流背景；其中 CNIL 的建议不自动变成 Play 的审核条款。

| 对象与章节 | 可执行复核项（改写摘要） | 与 Google Play 的边界 |
| --- | --- | --- |
| 应用发布者（§5） | 为每项处理记录数据、目的、法律依据、接收方和保存期限；确认默认设置尽量少收集；绘制服务商/SDK 关系；评估权限、拒绝后的替代路径、同意与权利流程；对 SDK、功能、用途和同意机制变更设审批与记录更新流程。 | 对应 User Data 的实际数据流、最小化、披露、Data safety 和隐私政策核对；CNIL 核对清单本身写明部分项仅属建议/良好实践。 |
| 应用开发者（§6） | 明确其在具体处理中的角色；架构/SDK/权限或界面决定若影响隐私，应与发布者协商并留存指令；把 SDK 的处理目的、权限和拒绝替代方案交给发布者；若作为处理者委托子处理者，应取得必要书面授权并将保护要求传递到下游。 | 不能仅因外包开发或接入 SDK 就把 Play 责任移出应用开发者/开发者账号；具体法律角色依实际处理与合同判断。 |
| SDK 提供商（§7） | 让集成方能按配置识别 SDK 涉及的全部处理、接收方和传输；区分为应用提供功能与 SDK 自身目的处理；尽量不依赖非必要权限；提供支持同意撤回、删除和权利请求的接口/资料；变更和安全问题及时通知客户。 | 便于开发者核实 SDK Index、User Data 与 Data safety；SDK 自身处理/跨客户用途仍应独立建模，不能只看 SDK 的功能名称。 |
| OS 提供商（§8） | 说明自身处理及保护措施；权限交互应帮助应用解释资源范围并支持用户作出、撤回选择；提供支持权利与同意的工具及安全平台。 | OS 权限只是系统访问控制；它不自动证明 Play 披露/肯定同意成立，也不决定 Play 对某权限用途是否批准。 |
| 应用商店提供商（§9） | 面向欧盟应用，CNIL 建议商店评估发布者提供的数据类别/目的、第三方和 SDK、完整权限清单及必要性/用途、数据存储国家和更新历史；还建议鼓励按功能上下文请求运行时权限、减少过宽或过时 API，并按风险采用静态/动态分析。 | 这些是向应用商店提供方提出的透明度和审核建议，不是对 Play 开发者新增的普遍申报条款，也不能替代 Google Play 的实际审核标准。 |

CNIL 的 §§5.6、6.5、7.5、8.5、9.4 清单仅用于指引；原文提醒其中部分检查项可能只是建议或良好实践。开发者可把它们用作内部排查表，但要回到具体法律条文、Google Play 当前政策和 Console 声明分别定性。

### CNIL 新闻页正文链接逐项复核（2026-10-24）

重开 User Data 直链的 CNIL 英文新闻页，并逐项检查正文链接 ID 1–13。下表记录目标页与父页的关系；脚注、站内导航和其他主题后代仍未无限递归。

| 正文链接 | 子页内容与父页关系 | 访问 / 后代状态 |
| --- | --- | --- |
| ID 1 [定向广告定义](https://www.cnil.fr/fr/definition/publicite-ciblee) | 说明按个人特征/画像选择广告，解释新闻页将广告定向举作非必要处理的原因；不是 Play 规则。 | 正文已打开；程序化广告、相关文章和标签未追。 |
| ID 2 [2025 英文礼貌译本](https://www.cnil.fr/sites/cnil/files/2025-05/recommendation-mobiles-app.pdf) | 93 页，确认对应 2025-04-08 修订版；仅法文有法律效力。§§2–9 与五方清单已摘要，本轮补充权限、模块化和网络审计提示。 | 全文可读；脚注目标未全提取。 |
| ID 3 [“French version”](https://www.cnil.fr/sites/cnil/files/2024-09/recommandation-applications-mobiles.pdf) | 实际落到 2024 原始版；现行版为[2025 法文修订版](https://www.cnil.fr/sites/cnil/files/2025-04/recommandation-applications-mobiles-modifiee.pdf)。 | 历史 PDF 已读。 |
| ID 4 [数据收集经济议题咨询摘要](https://www.cnil.fr/sites/cnil/files/2023-07/collecte_de_donnees_dans_les_applications_mobiles-les_enjeux_economiques-synthese_des_contributions.pdf) | 8 页、汇总 26 份意见，解释经济激励和数据链条如何影响建议起草；不是义务清单。 | PDF 全文已读；意见提交者引用未全追。 |
| ID 5 [已关闭的 2023 公众咨询页](https://www.cnil.fr/en/closed-mobile-applications-cnil-launches-public-consultation-its-draft-recommendation) → [95 页咨询草案](https://www.cnil.fr/sites/cnil/files/2023-07/projet_recommandation_applications_mobiles.pdf) | 咨询于 2023-10-08 截止；PDF 明确标为草案，不能取代 2025 现行版。 | 页面及 PDF 全文已读；草案引文后代未全追。 |
| ID 6 [2024 公众咨询意见摘要](https://www.cnil.fr/sites/cnil/files/2024-09/applications-mobiles-synthese-contributions.pdf) | 7 页、18 份意见；说明对义务/建议/良好实践及竞争/DMA 边界的澄清。 | PDF 全文已读；历史咨询材料。 |
| ID 7 [CNIL 与法国竞争管理局联合声明](https://www.cnil.fr/en/data-protection-and-competition-cnil-and-autorite-de-la-concurrence-sign-joint-declaration) → ID 8 [移动应用合作文件](https://www.cnil.fr/sites/cnil/files/2024-09/applications-mobiles-cooperation-autorite-de-la-concurrence.pdf) | 说明隐私与竞争监管协作；5 页文件讨论应用商店隐私评分的透明/独立及避免固化市场优势。解释竞争法/DMA 保留语句，不新增 Play 开发者义务。 | 网页和 PDF 全文已读；引文后代未全追。 |
| ID 9 [CNIL 执法流程旧链接](https://www.cnil.fr/en/steps-cnils-law-enforcement-process) → [当前页面](https://www.cnil.fr/en/investigation-powers-cnil/steps-cnils-law-enforcement-process) | 重定向到介绍线索、调查及可能命令/制裁的通用监管说明；不是 Play 审核流程。 | 目标全文已读；导航/案例未递归。 |
| ID 10 [2023 调查优先主题旧链接](https://www.cnil.fr/en/priority-topics-investigations-2023-smart-cameras-mobile-apps-bank-and-medical-records) → [当前页面](https://www.cnil.fr/en/priority-topics-investigations-2023) | 记录 2023 年对移动应用追踪和系统广告标识符的检查，尤其关注缺少告知/同意；属于历史重点，不是未来期限或 Play 规则。 | 当前页全文已读；其他主题未递归。 |
| ID 11 [法文新闻旧路由](https://www.cnil.fr/fr/applications-mobiles-la-cnil-publie-ses-recommandations-pour-mieux-proteger-la-vie-privee) → [当前法文说明页](https://www.cnil.fr/fr/recommandations-applications-mobiles) | 保留 2024-09-24 日期，并注明 2025-04-08 发布修订版；与修订公告合读可厘清版本。 | 重定向目标全文已读；页脚/相关文章未追。 |
| ID 12 [消费者版说明](https://www.cnil.fr/fr/applications-mobiles-votre-vie-privee-devra-etre-mieux-protegee) | 从用户视角解释敏感权限、位置/共享、定向广告和权利；区分配送与广告用途。是风险背景，不是开发者政策。 | 正文已读；通用消费者权利后代未全追。 |
| ID 13 [Légifrance 决定 2025-024](https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000051448685) | 修订建议官方决定入口，与 CNIL 修订公告和法文 PDF 构成版本链。 | 直开 HTTP 403；只记录公告/官方索引的有限信息，未读全文。 |

### “Read more”与标签目标

ID 14–20 是“Read more”、分类标签或相关文章卡片，不是上述 13 条正文内容链接；仍逐项记录，且不因页面相邻而视为 Play 要求。

| 页面元素 | 内容与访问状态 |
| --- | --- |
| ID 14 [Recommendations 标签](https://www.cnil.fr/fr/tag/Recommendations) | 打开为 CNIL 单条结果目录；目录下其他建议未纳入。 |
| ID 15 [法文 Mobile applications 标签](https://www.cnil.fr/fr/tag/Mobile%2Bapplications)、ID 17 [Consultation 标签](https://www.cnil.fr/en/tag/Consultation)、ID 19 [英文 Mobile applications 标签](https://www.cnil.fr/en/tag/Mobile%2Bapplications) | 站内分类页均 HTTP 503；没有按标题推断内容。 |
| ID 16 [Session replay 相关文章](https://www.cnil.fr/en/session-replay-cnil-launches-public-consultation-its-draft-recommendation) → [2026 英文咨询草案](https://www.cnil.fr/sites/default/files/2026-02/recommendation_draft_session_replay.pdf) | 12 页译本涵盖参与方、告知/同意、权利、最小化、留存和安全；咨询于 2026-04-22 截止。是另一项监管草案，不是 Play 政策。 | 文章/PDF 全文已读；引文/后代未穷尽。 |
| ID 18 [FantomApp 社交媒体隐私工具文章](https://www.cnil.fr/en/fantomapp-cnils-application-to-protect-oneself-on-social-media) | 相关卡片介绍青少年隐私教育工具。 | HTTP 503；只见有限官方索引摘要，不计作全文已读。 |
| ID 20 [FantomApp 项目页](https://www.cnil.fr/en/fantomapp) | 青少年隐私教育应用；FAQ 称 IP、配置和设备类型为安全目的保留 6 个月。 | 全文已读；产品站/商店链接未追。 |

### 最佳实践：让 SDK 与敏感权限复核可验证

英文译本 §6.3（约 pp. 52–54）可转成工程团队的**隐私审查提示**。按原文分别定性为法律义务、建议或良好实践，不混成一类：

1. 对照 SDK 文档、合并 Manifest 和运行时行为，记录权限、用途、数据、接收方与角色；区分核心功能严格需要与仅提升便利性的权限，并验证拒绝可选权限后核心功能是否仍可用。
2. 评估较窄权限、较低精度、设备端处理等替代方案；拆分 SDK 的不同用途。可行时按功能模块集成，避免带入未用组件、权限和攻击面。
3. 覆盖同意前后、逐目的同意/拒绝、撤回及 SDK 更新。CNIL 提出可考虑拦截网络通信审计：非豁免读写不应在同意前发生；SDK 应遵从目的选择；实际数据应符合处理记录；受保护资源只由获准功能访问；撤回应生效。
4. 将 SDK 版本变化纳入审批；更新后重跑数据流和授权检查，并要求供应商提供处理活动、权限和追踪技术文档。

这些提示可辅助核对 Google Play User Data、醒目披露、Data safety、权限申报及 SDK Index；它们不是统一测试规程，也不替代 Play Console 的表单/视频要求。Play 强制义务仍以对应现行政策为准。

本轮检查了 13 个正文链接和 7 个“Read more”/标签/相关文章目标。正文目标均已打开摘要或登记明确失败。建议书、咨询材料和监管页的脚注、引文、所有站内导航及相关主题后代仍未穷尽；Légifrance 403、3 个标签 503、FantomApp 文章 503 均未按标题推断。CNIL 材料不是 Play 规则，保留法国/欧盟隐私法适用边界。

2026-10-24 复核时，[CNIL 移动应用建议入口](https://www.cnil.fr/fr/applications-mobiles-les-recommandations-de-la-cnil)、[英文新闻页](https://www.cnil.fr/en/mobile-applications-cnil-publishes-its-recommendations-better-privacy-protection)、[法文修订公告](https://www.cnil.fr/fr/recommandations-applications-mobiles-modifiee)和[权限说明文章](https://www.cnil.fr/fr/permissions-applications-mobiles-recommandations-de-la-cnil-pour-respecter-la-vie-privee)均可读取。修订公告页直接列出 2025 现行法文 PDF、修订标注版及决定链接。User Data 新闻页的“French version”链接仍解析到 2024 原始 PDF；2024 年法文公告页注明后来已于 2025-04-08 修改发布，因此 2024 文件仅作历史版本。英文译本是 93 页礼貌译本，只有法文文本具有法律效力。Légifrance 决定 URL 直开仍返回 403；官方搜索索引可见决定标题、日期、废止旧版及三项修改说明，但不是完整正文。权限文章还直接链接到[2024 原始建议书 PDF](https://www.cnil.fr/sites/cnil/files/2024-09/recommandation-applications-mobiles.pdf)，其状态与版本关系已单独记录。[技术开发网络研讨会页面](https://www.cnil.fr/fr/revoir-le-webinaire-applications-mobiles-recommandations-developpements-techniques)仍超时，视频未提取。

## 后续核对：技术权限与地理位置

### OS 权限、法律同意与 Play 披露是不同控制点

CNIL 的[权限说明文章](https://www.cnil.fr/fr/permissions-applications-mobiles-recommandations-de-la-cnil-pour-respecter-la-vie-privee)于 2025-01-14 发布，正文本轮已直接打开。它把 Android/iOS 系统权限解释为对相机、位置、通讯录等终端资源的**技术访问控制**：它本身通常不表达数据处理目的，也不当然构成 GDPR/法国法意义上的有效同意。应用方要分别判断某处理是否依法需要同意；在多数需同意的情形，CMP 应补足系统权限请求。只有单一权限同时覆盖一个处理、一项目的和一个数据接收方等有限情形，权限提示才可能足以承载同意。

CNIL 建议按上下文请求同意，而非一开始用单一总屏；CMP 与系统权限可先后出现，但顺序不应使用户困惑。如果其中一项被拒，应避免再弹出另一项无用请求。对系统权限设计的建议包括按目的选择最低侵入权限、细化精度/数据范围/授权时长。其[一页权限与 CMP 流程图](https://www.cnil.fr/sites/cnil/files/2025-01/infographie_permissions_et_cmp.pdf)显示两种授权缺一不可时的两种展示顺序。以上是 CNIL 的法国/欧洲隐私指导；Google Play 的醒目披露与肯定同意义务、Android 运行时权限仍需分别核对。

[CNIL 对 OS 的定义页](https://www.cnil.fr/fr/definition/systeme-dexploitation-ou-operating-system-os)说明 OS 管理终端硬件资源、应用沙盒和权限系统。它是术语解释，不是 Android 权限 API 指南或 Play 审核条款。

### 2026 年 CNIL 地理位置合规提醒

CNIL 于 2026-07-07 发布[应用地理位置处理的专业规则页](https://www.cnil.fr/fr/geolocalisation-applications-mobiles-quelles-regles)，将可识别个人的定位作为个人数据，重点涉及 GDPR 与法国电子通信隐私规则。应用方应说明目的、接收方、保存期限和权利；当定位并非提供用户所请求服务的严格必要条件（例如广告定向或向数据经纪商出售）时，CNIL 指出应取得有效同意。即使已取得同意，也仍须最小化精度、用途和留存；可行时优先在设备本地处理，不应在功能不需要时持续后台收集。OS 的精确/近似、前台/后台技术授权本身不等于法律同意。

另有同日面向公众的[地理位置隐私建议](https://www.cnil.fr/fr/geolocalisation-applications-mobiles-proteger-vos-donnees)：优先“仅在使用应用时”授权，核查数据用途和第三方共享，撤销不需要的权限并定期清理历史记录。该页是用户指导，不能作为开发者义务或 Google Play 规则的唯一依据。

这些材料与 Play 的[用户数据政策](../user-data/user-data.zh-CN.md)、[后台位置专题](../background-location/background-location.zh-CN.md)和[精确位置/联系人权限预览](../contacts-location-permissions/contacts-location-permissions.zh-CN.md)交叉使用：Play 审核、Android 系统访问控制、GDPR/ePrivacy 法律依据必须分别满足，任何一层的批准或许可都不替代另一层。

### 地理位置专业规则页的直接子链接

下表逐项记录 CNIL 2026 专业规则页正文的 12 个直接链接目标。本轮逐个打开目标；HTTP 503/Internal Error 项只登记目标与失败状态，不按标题补写内容。辅助文章的孙链接尚未全部递归读取。

| 直接子页面 | 读取到的内容及与父页的关系 | 状态/边界 |
| --- | --- | --- |
| [与亲友分享位置的 CNIL 用户指南](https://www.cnil.fr/fr/partage-geolocalisation-conseils-de-la-cnil) | 解释实时位置分享的隐私、家庭压力与数据经纪商风险；建议限时分享、关闭不需要的后台访问、定期检查接收者。 | 正文已打开；公众建议，不是 Play 政策或专业法律规则。 |
| [移动应用建议修订公告](https://www.cnil.fr/fr/recommandations-applications-mobiles-modifiee) | 地理位置专业页指向移动应用建议的修订入口。 | HTTP 503；现行内容改查官方[主题入口](https://www.cnil.fr/fr/applications-mobiles-les-recommandations-de-la-cnil)和 2025 PDF，不推断失败页正文。 |
| [GeoTrouveTous 位置重识别研究](https://linc.cnil.fr/geotrouvetous-projet-de-reidentification-par-geolocalisation) | CNIL LINC 2023 研究以数据经纪商位置轨迹演示，即使只有技术标识和若干位置点，也可能大规模重识别个人。 | 正文已打开；研究示例，不是法律条款或 Play 审核标准。 |
| [合法性与法律依据](https://www.cnil.fr/fr/les-bases-legales/liceite-essentiel-sur-les-bases-legales) | 父页用于解释处理活动应选择适用的法律依据。 | HTTP 503；只记录目标标题，不推断正文。 |
| [告知与透明度](https://www.cnil.fr/fr/conformite-rgpd-information-des-personnes-et-transparence) | CNIL 2019 页面说明直接/间接收集时点、目的、法律依据、接收方、期限、权利和联系点，并强调信息应清楚、易找、适配场景。 | 正文已打开；此为通用 RGPD 指引，应用界面仍需结合现行法律和 Play 披露要求。 |
| [确定处理目的](https://www.cnil.fr/fr/passer-laction/definir-une-finalite) | 目的须明确、合法、具体且在处理过程中保持一致；目的帮助判断必要数据与保存期。 | 正文已打开；一般处理登记指南，适用性须结合具体业务。 |
| [数据保存期限](https://www.cnil.fr/fr/passer-laction/les-durees-de-conservation-des-donnees) | CNIL 页面标记 2026-04-02；区分活跃库、受限的中间归档和永久归档，强调按目的确定期限，并区分法律强制期限与建议性参考期限。 | 正文已打开；页面列出的健康、社福、人事等期限参考并非定位应用通用期限。 |
| [个人数据权利入口](https://www.cnil.fr/fr/respecter-les-droits-des-personnes) | 权利专题入口提示须告知用户并让其能行使权利；与定位访问、删除、反对和撤回同意相关。 | 入口正文已打开；其下“具体权利/如何答复”子文章尚未全部打开。 |
| [收集有效同意](https://www.cnil.fr/fr/les-bases-legales/consentement) | CNIL 2018 页面概述同意为六种法律依据之一；必须自由、具体、知情、明确，并能证明有效性，目的/数据/保留变化时需重新评估。 | 正文已打开；文章较早，法律实践应核对现行法与监管指引。 |
| [权限与隐私说明](https://www.cnil.fr/fr/permissions-applications-mobiles-recommandations-de-la-cnil-pour-respecter-la-vie-privee) | 父页推荐与法律同意分开处理；见上文权限分析。 | 本轮正文完整打开；相关 2024 PDF、OS 定义和流程图均已登记。 |
| [数据最小化](https://www.cnil.fr/fr/minimiser-les-donnees-collectees) | CNIL 2020 页面要求仅收集目的所需数据、提前记录必要性、控制日志和精度、为可选定位功能保留选择，并按期限自动删除。 | 正文已打开；文章后续开发者/安全指南链接尚未全部递归核对。 |
| [CNIL 检查与执法](https://www.cnil.fr/fr/les-controles-de-la-cnil) | 父页用于说明违反透明、期限、安全或权利义务可能引发监管检查。 | 本轮返回 Internal Error；未据标题补写流程或处罚细节。 |

地理位置专业页还引用 GDPR 与法国《信息技术与自由法》作为法律来源；本专题记录的是 CNIL 指引与其对 Play 用户数据审核的关系，不替代完整法规、成员国法律分析或法律意见。已读辅助页的更多子链接（例如其自身的 RGPD 条文、模板、参考期限和开发者指南）尚未全部遍历，具体访问状态见逐 URL 来源台账（快照：`../SOURCE_LEDGER.md`，未导入本仓库）。

### 历史链接校准：Privacy Shield 已失效

Google Play 的[2017 年 6 月政策公告](https://support.google.com/googleplay/android-developer/answer/14554580)曾称新增 EU–U.S. Privacy Shield 数据保护指引。英文路由仍返回 HTTP 429；2026-10-24 成功打开的[简体中文 `zh-Hans` 正文](https://support.google.com/googleplay/android-developer/answer/14554580?hl=zh-Hans)只有一段历史说明，并链接到旧 User Data 路由 `answer/9888076`；该旧路由的既有审计记录显示它转向当前 `answer/10144311`。欧盟法院于 2020-07-16 在 Schrems II 案中判定 Privacy Shield 充分性决定 2016/1250 无效。欧盟委员会于 2023-07-10 通过 EU–U.S. Data Privacy Framework (DPF) [充分性实施决定 (EU) 2023/1795](https://eur-lex.europa.eu/eli/dec_impl/2023/1795/oj)；截至 2026-10-23，委员会的[充分性决定目录](https://commission.europa.eu/law/law-topic/data-protection/international-dimension-data-protection/adequacy-decisions_en)仍将美国商业组织中参加 EU–U.S. DPF 的组织列为可依该决定接收相关数据的对象。委员会 2024 年首轮审查认为框架所需结构和程序已建立，同时指出当时实际运行经验仍有限、需加强合规监测，并建议三年后进行下一次定期审查。

这条时间线用于校准旧 Play 公告的历史引用，不会把 DPF 变成 Google Play 的独立审核条款。它也不意味着所有美国公司、开发者或数据流自动受到 DPF 覆盖；应核验组织当前认证、数据和服务范围，并继续遵守适用法律、合同、User Data 与 Data safety 要求。来源：[欧盟法院判决新闻稿](https://curia.europa.eu/site/upload/docs/application/pdf/2020-07/cp200091en.pdf)、[欧盟委员会 DPF 首轮审查报告（2024）](https://commission.europa.eu/document/download/25695177-8073-4ce3-bf81-eb816dc6b468_en?filename=Report+on+the+first+periodic+review+of+the+functioning+of+the+adequacy+decision+on+the+EU-US+Data+Privacy+Framework.pdf)。法院新闻稿与报告均作为外部法律背景摘要；其脚注、诉讼和相关机构页面未在本分支全部递归展开。

## Data Privacy Framework：跨境传输框架的适用条件

User Data 政策要求对由 Google 提供、可识别个人且源自 EEA、英国或瑞士的个人信息遵守适用法律和相应传输机制。Google 的[数据传输框架说明](https://policies.google.com/privacy/frameworks)（页面标明自 2025-08-23 生效）称，Google LLC 已认证遵守 EU-U.S. 与 Swiss-U.S. DPF 及 UK 扩展，并在必要且不受充分性决定覆盖时使用标准合同条款（SCC）。这是 Google 对其数据处理/传输机制的说明；不要推断开发者因此自动获得 DPF 认证，或自己的所有跨境传输已经合规。

美国商务部的 [DPF Principles 说明页](https://www.dataprivacyframework.gov/program-articles/Participation-Requirements-Data-Privacy-Framework-%28DPF%29-Principles)和 [EU-U.S. DPF 全文入口](https://www.dataprivacyframework.gov/EU-US-Framework)直接打开仍返回 JavaScript 壳。2026-10-24 的官方索引显示七项核心原则、16 项补充原则标题、EU-U.S./英国扩展与 Swiss-U.S. 两套目录，以及附件 I 仲裁示范模型；全文入口还列出商务部、ITA、FTC（含 Appendix A）、DOT、ODNI 和 DOJ 的监督/执法材料，但没有暴露原页面附件的精确 URL，“Download Full Text”控件也未提供可读取的下载地址。

本轮通过[欧盟委员会实施决定 (EU) 2023/1795](https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX%3A32023D1795)附件 II–VII 逐项核读了 EU-U.S. DPF 的商务部长转呈函、ITA 管理说明、FTC 执法函、DOT 执法函、DOJ 政府访问说明和 ODNI 国家安全保障函；FTC 的 [Appendix A](https://www.ftc.gov/system/files/ftc_gov/pdf/appendix-a-privacy-shield-and-safe-harbor-enforcement.pdf)另在 FTC 官网打开。另核对[英国政府的 UK-U.S. data bridge supporting documents 页面](https://www.gov.uk/government/publications/uk-us-data-bridge-supporting-documents)，其中以 Annex A–H 提供原则全文、UK Extension 对应函件和术语表。它们是可阅读的官方配套出版物；英国附件针对 UK Extension，不能与 EU-U.S. 正文混作同一版本，也不能据此声称已观察到美国商务部动态页的原始附件 href。两套材料说明相应主体、机制和边界如下：

| 正式材料 | 摘要及与 User Data / Play 的关系 |
| --- | --- |
| [DPF Principles 全文，英国政府 Annex A（35 页）](https://assets.publishing.service.gov.uk/media/65040bf25b07380013029f51/annex_a_ue-us_dpf_principles.pdf) | 七项核心原则、16 项补充原则和仲裁附件的可读全文；仅适用于依其自我认证、公开承诺的合格美国组织及对应数据范围。Principles 摘要见下文；不构成 Play 的独立审核条款。 |
| [商务部长转呈函，英国政府 Annex B（2 页）](https://assets.publishing.service.gov.uk/media/65040c1e5b07380013029f53/annex_B_doc_letter_uk_extension_to_the_eu-us_dpf.pdf) | 说明 UK Extension 文件包与 EO 14086、28 CFR Part 201（含 Data Protection Review Court）的关系，并列举 ITA、FTC、DOT、DOJ 与 ODNI 配套函；属于框架背景。 |
| [ITA 管理与监督函，英国政府 Annex C（13 页）](https://assets.publishing.service.gov.uk/media/65040c43702634001389b915/annex_c_ita_letter_uk_extension_to_the_eu-us_dpf.pdf) | 解释商务部如何维护参与/退出名录、审核初次和年度自我认证、调查虚假参加声明、抽查合规并处理投诉；UK Extension 还要求组织明确选择覆盖英国/直布罗陀数据。既有数据在退出后仍受原则约束，直至不再保留。 |
| [FTC 执法函，英国政府 Annex D-1（7 页）](https://assets.publishing.service.gov.uk/media/65040cec5b0738000d029f66/annex_d-1_ftc_letter_uk_extension_to_the_eu-us_dpf.pdf) | FTC 承诺优先调查、寻求并监督执法命令，并与英国 ICO 合作；其范围是 FTC 管辖的商业隐私执法，与 ITA 的名录/认证管理不同。 |
| [FTC Appendix A（4 页）](https://assets.publishing.service.gov.uk/media/65040cf597d3960014482f56/annex_d-2_ftc_letter_appendix_a.pdf) | 列有 68 项 Safe Harbor / Privacy Shield 历史执法事项，包括 Twitter、CafePress、Flo Health；它是历史案件索引，不是现行 DPF 条文。个案正文未全部打开。 |
| [DOT 执法函，英国政府 Annex E（5 页）](https://assets.publishing.service.gov.uk/media/65040d725b07380013029f59/annex_e_dot_letter_uk_extension_to_the_us-us_dpf.pdf) | DOT 依 49 U.S.C. §41712 处理航空承运人及机票代理商的相关隐私承诺，包含优先调查、处理虚假参加声明和公开执法命令；不适用于一般 Play 应用开发者。 |
| [DOJ 政府访问说明，英国政府 Annex F（5 页）](https://assets.publishing.service.gov.uk/media/65040d995b07380013029f5a/annex_f_doj_letter_uk_extension_to_the_eu-us_dpf.pdf) | 概述刑事及公共利益（民事/监管）场景下的传票、搜查令、Stored Communications Act 等取数路径与限制，并说明企业可在法院挑战程序。脚注明确该信不讨论国家安全调查工具；相关主题由 ODNI 函件处理。 |
| [ODNI 国家安全保障函，英国政府 Annex G（4 页）](https://assets.publishing.service.gov.uk/media/65040dbe5b07380013029f5b/annex_g_odni_letter_dpf.pdf) | 该 PDF 在抓取器中没有可读正文；已通过 EUR-Lex 决定 Annex VII 核读对应函件。它解释 EO 14086 对情报活动的合法目标、禁止目标、必要性/比例性和政策更新要求，并说明符合条件个人的独立、有约束力救济机制；并非开发者操作清单。 |
| [UK data bridge 术语表，英国政府 Annex H](https://www.gov.uk/government/publications/uk-us-data-bridge-supporting-documents/uk-us-data-bridge-glossary-of-terms-annex-h) | 解释 DPF、DPF List、DPRC、ITA、ICO 等缩写；用于阅读 UK Extension 文件，未增加独立政策义务。 |

该政府材料页还列有 [英国组织 factsheet](https://assets.publishing.service.gov.uk/media/650c4c7efbd7bc000de54786/factsheet_for_uk_organisations.pdf)、[ICO 对英国充分性评估的意见](https://ico.org.uk/about-the-ico/what-we-do/information-commissioners-opinions/information-commissioners-opinions-on-adequacy/the-uk-government-s-assessment-of-adequacy-for-the-uk-extension-to-the-eu-us-data-privacy-framework/)、[英国作为 EO 14086 qualifying state 的支持材料](https://assets.publishing.service.gov.uk/media/650805fedec5be0014c35fad/uk_government_paper_support_of_our_designation_qualifying_state_under_us_executive_order_14086.pdf)和 [133 页 UK Extension 充分性分析](https://assets.publishing.service.gov.uk/media/650801f6fc63f60014957399/analysis_of_the_uk_extension_to_the_eu-us_data_privacy_framework.pdf)。factsheet 提醒：依英国数据桥传输前须核验组织处于有效名录、明确参加 UK Extension，且 HR 数据在其认证范围内；不应假定任何美国接收方均可适用。ICO 认为政府作出充分性决定有合理依据，同时指出敏感数据识别、刑事定罪记录、重大自动化决定以及删除/撤回同意权等四个执行风险需持续监测。支持材料和 133 页分析用于理解 UK Extension 评估及政府访问保障；本次只检查了导言、范围、主要附件与部分章节，脚注、法律引用及更深后代尚未全部递归展开。

欧盟委员会[实施决定 (EU) 2023/1795](https://eur-lex.europa.eu/eli/dec_impl/2023/1795/oj)的 ELI 直链和[标准 PDF 地址](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX%3A32023D1795)触发机器人验证；通过 EUR-Lex 官方索引提供的同一 CELEX PDF 变体可读到 112 页全文。本次定向核对附件 I 的 7 项核心原则、16 项补充原则及仲裁示范附件的结构，并按条目改写如下。没有逐字复制原文，也未逐条审阅决定正文的全部 112 页及所有脚注。EU-U.S. DPF 原则也用于英国扩展；Swiss-U.S. DPF 另有对应版本，两者的监管机构名称和少数执行细节不同。

### 监管机构官方函件：执法范围及与 Play 的关系

官方 [DOT 2023-07-06 函件](https://www.transportation.gov/sites/dot.gov/files/2024-03/DOT%20letter_EU-U.S.%20DPF.pdf)共 5 页。函件称，DOT 在 49 U.S.C. § 41712 航空消费者保护权限内，对参加 DPF 的航空承运人和机票代理商执行相关原则，并承诺优先调查 DPF 投诉、处理虚假或误导性参加声明、监测并公开执法命令。适用对象是受其监管的承运人和票务代理；它不是面向 Play 应用发布者的新规则。PDF 的两个脚注 URL 指向 DOT 的 [Air Consumer Privacy 页面](https://www.transportation.gov/individuals/aviation-consumer-protection/privacy)和旧版[隐私投诉路由](http://www.transportation.gov/airconsumer/privacy-complaints)。隐私页面正文已打开，标注最后更新于 2025-09-29；旧投诉路由返回 404。本次读取未能从该页当前投诉按钮解析出可读的目标地址。

官方 [FTC DPF 页面](https://www.ftc.gov/business-guidance/privacy-security/data-privacy-framework)说明企业须向商务部自行认证；参加者违反 DPF 原则也可能构成 FTC Act § 5 下的不公平或欺骗行为。其链接的[FTC 2023-06-09 执法函](https://www.ftc.gov/system/files/ftc_gov/pdf/2023.06.08letter-to-commissioner-reynders.pdf)共 6 页，承诺优先处理转介和调查、寻求并监督执法命令、与欧盟数据保护机构合作。其 [Appendix A](https://www.ftc.gov/system/files/ftc_gov/pdf/appendix-a-privacy-shield-and-safe-harbor-enforcement.pdf)共 4 页，列出 68 起 Privacy Shield/Safe Harbor 历史执法事项，包括 Twitter、CafePress 和 Flo Health。这些材料解释监管机关承诺和历史执法案例；不新增 Play 义务，也不能证明某应用的数据传输受到 DPF 覆盖。从 DOT 页面到达的 [DPF 项目入口](https://www.dataprivacyframework.gov/s/)只返回 JavaScript 壳；函件脚注和 Appendix A 中列出的案件未全部递归打开。

| # | 七项核心原则 |
| ---: | --- |
| 1 | 告知（Notice）：在首次收集或可行的尽早时间，用清楚醒目的隐私说明讲明参加 DPF、数据类别和用途、覆盖实体、第三方及其用途、个人权利与选择、投诉/免费救济渠道、监管执法、可能的仲裁、公共机关依法调取以及后续转移责任；最迟须早于不兼容的新用途或首次向第三方披露。 |
| 2 | 选择（Choice）：对向控制者第三方披露或实质不同的新用途，通常提供可用的退出机制；敏感信息向第三方披露或改作新用途，通常要求明确肯定同意。仅代表组织按指示处理的代理人例外于选择，但仍须签约。 |
| 3 | 后续转移责任（Accountability for Onward Transfer）：按接收方是控制者还是代理/处理者分别建立限制目的、同等保护、审查与补救机制；代理仅按指示处理，组织须采取合理措施确认执行并在发现失守时停止或纠正。 |
| 4 | 安全（Security）：按处理风险和数据性质采取合理、适当措施，防范丢失、滥用及未经授权的访问、披露、修改或毁损。 |
| 5 | 数据完整性与目的限制（Data Integrity and Purpose Limitation）：只保留与目的相关的数据，不作不兼容处理；在目的需要范围内保持可靠、准确、完整、最新，并且只以可识别形式保存到处理目的仍需要为止。允许特定公共利益档案、新闻、艺术、科学/历史研究和统计用途延长，但其他原则仍适用。 |
| 6 | 访问（Access）：个人可确认是否处理其信息、取得信息并要求更正、补充或删除不准确或违规处理的信息；仅在规定的第三方权利、严重不成比例负担等例外中限制，且应尽力提供可分离部分。 |
| 7 | 救济、执法与责任（Recourse, Enforcement and Liability）：建立免费、可及、独立的投诉救济；验证公开承诺确已实施；设置足够有效的纠正和制裁。满足程序条件的未解决个案可进入有约束力仲裁；参与组织对其代理人的违规处理原则上仍负责任。 |

| # | 16 项补充原则（主题） |
| ---: | --- |
| 1 | 敏感数据：明确肯定同意通常是基线；列出生命重大利益、诉讼主张/抗辩、医疗照护、特定非营利机构成员关系、劳动法义务及个人明显公开数据等例外。 |
| 2 | 新闻业例外：依美国新闻自由保护平衡；为新闻出版/播出/公共传播收集的信息（无论最终是否发布）及媒体档案中既有材料，不适用这些原则。 |
| 3 | 次级责任：仅代他方传输、路由、交换或缓存数据的 ISP、电信承运商等通道，不因此承担 DPF 次级责任；前提是其未决定个人数据的处理目的和方式。 |
| 4 | 尽职调查与审计：在审计、合规调查、并购等场景，可能在个人不知情时处理信息；只有在满足法定/公共利益要求，或告知会实质损害组织正当利益的必要范围和期间内，才允许例外。 |
| 5 | 监管机构角色：EU-U.S. 参与者可在认证中承诺与欧盟 DPA 合作、接受其调查与建议并完成补救；DPA 小组一般以 60 天为处理目标，未在要求期限内落实建议可能触发转介或严重违约后果。Swiss-U.S. 对应监管者为瑞士联邦数据保护与信息专员。 |
| 6 | 自我认证：组织先完成商务部审核并进入名录后才获得 DPF 保障，至少每年重新认证；退出后，已接收数据的保护承诺继续适用，除非转用其他获认可机制或返还/删除数据。 |
| 7 | 核验：可采用自我评估或外部合规审查；至少每年确认隐私说明准确、完整且实际落实，并覆盖培训、员工问责、客观复核和证据留存。 |
| 8 | 访问：补充身份核实、合理响应时限、重复请求、费用、商业机密和第三方权利等细节；能分离时应遮蔽受保护部分并提供其余数据，不要求向个人开放组织数据库，也不凭此产生保留或重组数据的义务。 |
| 9 | 人力资源数据：涵盖欧盟员工/前员工的可识别记录；转出前的收集处理及成员国限制仍适用。非雇佣用途和第三方披露受告知/选择规则约束，选择不得导致职场报复；美国接收方须支持员工访问和适用的 DPA 合作。 |
| 10 | 后续转移的强制合同：纯处理目的的传输仍需处理合同，明确按指示处理、安全措施和权利请求协助；集团内控制者可在连续保护有保障时采用其他工具；控制者间转移须以合同维持相当保护。 |
| 11 | 争议解决与执法：组织应在 45 天内答复个人投诉，并提供免费独立救济和公开程序/年度统计；未解决的特定个人剩余争议可仲裁，裁决救济限于个人化非金钱措施。违规可触发公开认定、删除、暂停标志、赔偿/禁令、FTC/DOT 执法，持续不合规会被移出名录。 |
| 12 | 选择与退出时点：直销退出权应随时可用；因操作原因不能在首次使用前提供时，应尽快且免费地给出后续拒收选项并遵从个人选择。 |
| 13 | 旅行信息：乘客、酒店、常旅客和辅助需求等数据可在符合条件时依 DPF 转移；数据出口方仍须遵守适用成员国对敏感数据的要求。 |
| 14 | 药品与医疗产品：转移前的采集/处理仍受欧盟或成员国法管辖；研究再利用通常要在最初告知未来用途并按目的兼容性取得选择/新同意。为满足药物安全、疗效监管报告要求，可在必要限度内例外于若干告知、选择、后续转移和访问要求；编码数据仍可能属于个人数据。 |
| 15 | 公共记录与公开可用信息：安全、目的限制和救济仍适用；在未与非公开数据混合且遵守查询条件时，告知/选择/后续转移及部分访问义务可有例外。故意违规公开数据以借用例外会失去 DPF 资格。 |
| 16 | 公共机关访问请求：组织可在法律允许范围内自愿发布执法/国家安全调取的汇总透明度报告；告知中未提及某请求，不妨碍响应合法命令。 |

EU-U.S. 实施决定附件 I 的仲裁示范规则还规定适用范围、先前救济、仲裁通知/资格、仲裁庭组成、程序和费用，并把仲裁限制在其他机制未解决的个人剩余请求；仲裁庭可以命令针对该个人的非金钱衡平救济，不能据此挑战充分性决定本身。本次只作结构与关键限制摘要，不是完整仲裁规则释义。组织一旦公开承诺并被列入名录，承诺即有约束力；不再参加时，已接收且仍保留的数据必须继续适用原则或改用其他获认可保障，否则返还/删除。

这不是所有 GDPR 义务的替代物。商务部 FAQ 明确说，EU-U.S. DPF 是允许参加组织在 GDPR 第 V 章下进行特定对美传输的机制，不是 GDPR 整体合规机制；只为控制者处理数据时，合同义务也不会因为处理方参加 DPF 而自动消失。核验某组织时，应在[参与组织名录](https://www.dataprivacyframework.gov/list)打开组织记录，查看参与计划、覆盖的美国实体/子公司、相关隐私政策和争议解决渠道；名录在本次读取中仅显示 JavaScript 提示，未核验任何具体组织。

补充的官方核验和解释材料：[如何核验组织的 DPF 承诺](https://www.dataprivacyframework.gov/program-articles/How-to-Verify-an-Organization-s-Privacy-Data-Privacy-Framework-%28DPF%29-Commitments)、[DPF 一般 FAQ](https://www.dataprivacyframework.gov/program-articles/FAQs%E2%80%93General)、[仅用于处理目的时的合同要求](https://www.dataprivacyframework.gov/program-articles/Contract-Requirements-for-Data-Transfers-to-a-Processor)、[后续转移 FAQ](https://www.dataprivacyframework.gov/program-articles/FAQs%20%E2%80%93%20Onward-Transfer-Principle)。这些页面的搜索索引正文可读，但直接页面抓取也落到动态壳；摘要据已索引官方内容，不替代完整条款或个案法律判断。

## Google Controller-Controller Terms：只适用于纳入该合同的服务关系

[Google Controller-Controller Data Protection Terms](https://business.safety.google/controllerterms/)当前页面显示 Version 11，日期为 2026-05-07。定义中的 Controller Services 是在服务条款/其他协议中引用纳入这些条款的服务；条款只适用于双方同意的相关服务，例如 Partner 点击接受的服务，或协议明确纳入的服务。Terms Effective Date 是 Partner 接受或双方另行同意之日，不是所有开发者统一适用的日期。条款将双方描述为独立控制者，各自决定其处理目的与方式并承担适用法律义务；第 6.2 条也明确不影响其他服务关系下单独的控制者—处理者等条款。

Google 的[服务清单](https://business.safety.google/services/)最后更新于 2026-04-27，列出 **Google Play 为 Controller Service**，但这仍须结合服务协议是否纳入条款及实际接受情况。该表还将 **Managed Google Play 与 Android Management API** 单独列为 Subprocessor Data Protection Addendum 下的 Google Processor Products；它们对应另一种处理者关系，不能与 Google Play 的 Controller Service 分类混为一谈。该服务清单可能更新；这份合同也不是 Developer Program Policy，不能推断每个普通应用开发者都是 Google 的合同 Partner。

| Controller Terms 正文链接 | 页面内容与关系 | 已核验边界 |
| --- | --- | --- |
| [服务清单](https://business.safety.google/services/) | 依数据服务条款分类列出 Controller Services、Data Processing Services 和 Subprocessor Data Protection Addendum 下的 Processor Products。 | 完整现行名单已打开；名单动态更新，历史服务表未逐个分析。 |
| [美国州隐私法清单](https://business.safety.google/usdataprotectionlaws/) | 列明美国州隐私法；页面最后更新于 2025-07-01。 | 仅服务于引用该页面的协议，且只在具体法律适用时生效；不是所有开发者的独立通用义务。 |
| [Partner sites/apps 数据使用说明](https://policies.google.com/technologies/partner-sites) | 举例包括页面 URL、IP、应用名称和广告 ID；用途包括提供/改进服务、测量广告、安全及依设置个性化广告，并列出用户控制项。 | 这是 Google 面向用户的隐私说明，不是 Play 开发者政策；无痕模式并不阻止 Google 服务收集访问相关数据。其 cookies、广告设置、My Activity、Analytics 和广告 ID 等正文子链接仍有后代未逐项分析。 |
| [控制者到控制者 SCC](https://business.safety.google/gdprcontrollerterms/sccs/eu-c2c/) | Controller Terms 的欧洲数据转移合同条款；附录先看是否采用适用的 Data Transfer Solution，否则按相应受限转移情形适用 SCC，并分别处理 EU/EEA、英国路径。 | 仅适用于相关 Controller Terms 协议、个人数据和具体跨境转移，不是通用 Play 要求；SCC 后续法律/监管资源未穷尽。 |
| [Google 数据传输框架说明](https://policies.google.com/privacy/frameworks) | Google 说明其适用的数据传输框架与 SCC。Controller Terms 将该页作为 Google 及关联方采纳/认证状态的参考。 | 描述 Google 的机制，不证明开发者自己的传输已合规或其组织已获 DPF 认证。 |
| [Partner Information Protection Addendum（PIPA）](https://business.safety.google/pipa/) | 日本隐私法附录引用该文件的部分控制者义务。 | Controller Terms 的日本附录仅在数据主体为日本公民的范围适用；本轮打开 PIPA 页面，其他法律与执行细节未穷尽。 |
| [巴西控制者 SCC](https://business.safety.google/lgpd/controllerterms/sccs/c2c/) | Controller Terms 的 LGPD 部分定义巴西转移方案及控制者 SCC；适用转移方案时不走该 SCC 路径。 | 仅在 LGPD 对相关个人数据处理适用时生效；合同文本为葡萄牙语，地区法律细节未作完整法律分析。 |

正文还列出 11 份历史版本（2018-05-25 至 2026-02-17）。2026-10-23 复核后，11 个历史链接的确切目标均已从当前 Version 11 页面解析并逐一直接尝试：7 份 PDF 正文在既有审计中可读，4 个目标返回 Cache miss。本轮重新打开 2018-05-25、2020-08-27、2023-01-23、2025-08-22 和 2026-02-17 五份 PDF，并与现行 Version 11 做结构层面的高层比较；这不是逐条差异表，也不声称覆盖所有中间版本。2021-09-27 与 2024-06-04 的正文在既有审计中可读，但本轮重开分别返回 Internal Error，因此保留既有可读状态，不把这两份正文作为下表比较依据。下表逐项记录版本日期、官方目标和读取边界；不从无法读取的页面推断条款。所有相关页面及后代的逐 URL 状态见来源台账。

| 版本日期 | 官方历史版本目标 | 本轮状态与边界 |
| --- | --- | --- |
| 2018-05-25 | [PDF](https://www.gstatic.com/marketing-cms/fd/e8/cfdc7e984bf6b6ecb0d4737c12d5/controllerterms-20180525.pdf) | 正文可读（5 页）；已纳入下方结构比较，不是逐条红线。 |
| 2019-10-31 | [PDF](https://www.gstatic.com/marketing-cms/53/0c/c222cabd4699ad7afa199238e0c5/controllerterms-20191031.pdf) | 直接目标已确认；本轮 Cache miss，正文未读，不推断条款。 |
| 2020-08-27 | [PDF](https://www.gstatic.com/marketing-cms/fd/68/920fa3384639b452b90ec596e57d/controllerterms-20200827.pdf) | 正文可读（7 页）；已纳入下方结构比较，不是逐条红线。 |
| 2021-06-15 | [历史版本页](https://business.safety.google/controllerterms-20210615) | 直接目标已确认；本轮 Cache miss，正文未读，不推断条款。 |
| 2021-09-27 | [PDF](https://www.gstatic.com/marketing-cms/67/07/44aa75e24244b4205993c2758ecd/controllerterms-20210927.pdf) | 既有审计记录为正文可读（1 页）；本轮重开返回 Internal Error，保留原访问状态，未纳入本轮结构比较。 |
| 2022-09-22 | [PDF](https://www.gstatic.com/marketing-cms/ca/a7/0872ffd8411887be5f7b126cec37/controllerterms-20220922.pdf) | 直接目标已确认；本轮 Cache miss，正文未读，不推断条款。 |
| 2023-01-23 | [PDF](https://www.gstatic.com/marketing-cms/7c/8e/7ea6ff8f48a9aea988fcd8598fe1/controllerterms-20230123.pdf) | 正文可读（4 页）；已纳入下方结构比较，不是逐条红线。 |
| 2023-09-01 | [PDF](https://www.gstatic.com/marketing-cms/80/cf/e603306b46c98cb670b8a866a7db/controllerterms-20230901.pdf) | 直接目标已确认；本轮 Cache miss，正文未读，不推断条款。 |
| 2024-06-04 | [PDF](https://www.gstatic.com/marketing-cms/6d/63/9dc96637433a827307739d3b0ba3/controllerterms-20240604.pdf) | 既有审计记录为正文可读（14 页）；本轮重开返回 Internal Error，保留原访问状态，未纳入本轮结构比较。 |
| 2025-08-22 | [PDF](https://www.gstatic.com/marketing-cms/db/49/b12928c44315ac5ce1ea2d4a879e/google-controller-controller-data-protection-terms.pdf) | 正文可读（16 页）；已纳入下方结构比较，不是逐条红线。 |
| 2026-02-17 | [PDF](https://www.gstatic.com/marketing-cms/8a/9d/ecff146d4257ab9994adcf9fd58a/google-controller-controller-data-protection-terms.pdf) | 正文可读（16 页）；已纳入下方结构比较，不是逐条红线。 |


### 历史版本演变：可读快照的结构比较（非逐条红线）

本比较依据上表标为“已纳入下方结构比较”的五份可读快照和现行 [Version 11](https://business.safety.google/controllerterms/)。版本发布日是合同文本的版本时间，不是所有开发者共同的整改截止日。

| 快照 | 可核实的结构变化 | 对 Google Play 知识库的意义 |
| --- | --- | --- |
| [2018-05-25](https://www.gstatic.com/marketing-cms/fd/e8/cfdc7e984bf6b6ecb0d4737c12d5/controllerterms-20180525.pdf) | 早期版本以 GDPR 与瑞士 1992 年联邦数据保护法为核心；写有 Privacy Shield 认证通知和 Privacy Shield 后续转移条款。合同仍只适用于双方同意的 Controller Services，双方以独立控制者身份各自履责。 | 这是历史传输框架背景；Privacy Shield 文字不能当作当前传输机制。服务纳入和双方同意的范围限制从早期版本已存在。 |
| [2020-08-27](https://www.gstatic.com/marketing-cms/fd/68/920fa3384639b452b90ec596e57d/controllerterms-20200827.pdf) | 可读快照将欧洲与非欧洲数据保护法分开定义，加入 EEA、英国 GDPR/英国数据主体及非欧洲附加条款，并规定欧洲标准合同条款路径；同时继续保留“仅适用于双方同意的服务”及独立控制者架构。 | 增加地区/法律分流，不代表所有非欧洲法律对每个服务或每个开发者自动适用。须按个人数据、适用法律、服务和实际协议判断。 |
| [2023-01-23](https://www.gstatic.com/marketing-cms/7c/8e/7ea6ff8f48a9aea988fcd8598fe1/controllerterms-20230123.pdf) | 明确 Alternative Transfer Solution、Adequate Country 与 Controller SCCs：若 Google 为受限欧洲传输采用合格替代方案，该类传输不走 Controller SCC；未采用或停止采用时，SCC 条款作为相应路径。文本也区分欧洲与英国数据流向及相关 Google End Controller。 | 不能把“有 SCC 链接”简化为所有传输一律用 SCC；需核对适用版本、传输方向、充分性/替代方案及协议。 |
| [2025-08-22](https://www.gstatic.com/marketing-cms/db/49/b12928c44315ac5ce1ea2d4a879e/google-controller-controller-data-protection-terms.pdf) | “Applicable Data Protection Legislation”扩展为跨法域类别，并以附录分别处理美国州隐私法/CCPA、日本 PIPA 义务和巴西 LGPD/Controller SCC；各附录以对应法律适用为前提。 | 地区附录是条件条款，不表示每个 Partner 都受每个地区法约束；美国州法清单和服务范围仍要对照实际数据与协议。 |
| [2026-02-17](https://www.gstatic.com/marketing-cms/8a/9d/ecff146d4257ab9994adcf9fd58a/google-controller-controller-data-protection-terms.pdf) | Version 10 的“Applicable Data Protection Legislation”定义新增 Bulk Sensitive Data，并将其指向美国司法部 28 C.F.R. Part 202 的受关注国家/受覆盖主体规则。 | 这是特定美国敏感数据/政府相关数据的合同定义入口；不要把它泛化成所有 Play 用户数据的新披露规则。 |
| [现行 Version 11（2026-05-07）](https://business.safety.google/controllerterms/) | 在适用法律总定义中列入 NDPA，并将其定义为尼日利亚 2023 年《数据保护法》及 2025 年《一般适用与实施指令》；欧洲传输定义当前列举 EU-U.S.、英国扩展、Swiss-U.S. DPF 及其他合格框架。 | 这是现行合同文本列举的适用法律与 Google 传输机制；是否约束某 Partner 仍由服务纳入、接受、具体数据流和法律范围决定。 |

**共同边界与核对步骤：** 各快照维持了“独立控制者”合同模型，但它不会抹去协议中的用途限制，也不会改写其他服务关系下独立的处理者条款。当前服务清单把 Google Play 列为 Controller Service；Managed Google Play 与 Android Management API 则分别列在处理者产品体系下。开发者应先核对自己签署/接受的协议及服务类别，再确定数据主体、数据类型、角色、传输方向和适用法律；对欧洲或巴西跨境流仅在条件满足时判断 DPF/充分性或 SCC 路径，并单独履行 Play User Data、Data safety 与当地法律义务。该合同不是 Play Developer Program Policy，也不等于 Google 对每位 Play 开发者的自动承诺。

**比较边界：** 这里只对五份可直接重开的历史快照做了高层结构比较，不是逐条合同红线，不覆盖 2019、2021、2022、2023-09 等不可读快照，也未逐条分析 2021-09 和 2024-06 的页面文本。历史 PDF 的脚注、附件交叉引用及其全部后代链接仍未穷尽；遇到合同争议应以双方实际接受的当前文本为准。

## GDPR 链接链：从 Play 示例到欧盟委员会官方企业指南

Families 自认证广告 SDK 计划的正文把 [GDPR.eu](https://gdpr.eu/) 列为儿童广告法规示例。GDPR.eu 自己说明：网站由 Proton AG 运营，不是欧盟委员会或政府的官方资源，也不构成法律意见。应把它当作入门背景，而不是正式法源或监管机关解释。

该站“About GDPR.EU”里的官方跳转链接指向[欧盟委员会《企业与组织的数据保护信息》](https://commission.europa.eu/law/law-topic/data-protection/information-business-and-organisations_en)。我们打开了该目录正文及六个主题目标；可把它作为 GDPR 企业合规的官方说明入口，但最终法律义务仍须回到 GDPR 正文、适用法律和个案事实。

| 欧盟委员会主题 | 页面概括 | 对 Play 开发者审查的关系 | 访问边界 |
| --- | --- | --- | --- |
| [GDPR 适用范围](https://commission.europa.eu/law/law-topic/data-protection/information-business-and-organisations/application-gdpr_en) | 解释个人数据、处理活动和 GDPR 对哪些组织/处理活动适用；在线标识符、广告 ID、IP、Cookie ID 等可能构成个人数据；去标识/假名化数据若可重新识别，仍可能属于个人数据。 | 先识别实际数据、用户、控制者/处理者角色与地域范围，再决定法律义务；SDK 数据流不能因由第三方代码处理而忽略。 | 英文正文已打开；页面引用的法规条款后代未逐条展开。 |
| [GDPR 原则](https://commission.europa.eu/law/law-topic/data-protection/information-business-and-organisations/principles-gdpr_en) | 汇总合法、公平、透明；目的限制；数据最小化；准确性；存储限制；完整性与保密性；问责制七项原则。 | 可用作设计数据清单、用途、保留期、安全控制及可说明性复核的框架；不是 Play 表单字段的替代物。 | 英文正文已打开；后续法条和监管解释未穷尽。 |
| [处理数据的法律依据](https://commission.europa.eu/law/law-topic/data-protection/information-business-and-organisations/legal-grounds-processing-data_en) | 列出六类合法依据。若使用同意，同意须自由、知情、具体、明确肯定、易懂且可撤回；特殊类别数据另有条件。 | 不要把 Android 运行时权限、Play 的醒目披露/同意和 GDPR 合法依据当作同一控制点。采用合法利益等依据也不自动免除 Play 披露或其他政策义务。 | 英文正文已打开；此处概述不能替代按处理目的逐项判断合法依据。 |
| [企业与组织的义务](https://commission.europa.eu/law/law-topic/data-protection/information-business-and-organisations/obligations_en) | 说明信息告知、透明度、设计与默认保护、风险导向安全、数据泄露通知和数据保护官等责任；页面指出适用情况下 72 小时通知监管机关的要求。 | 帮助把用户告知、SDK 治理、安全和事件响应纳入发布/运维流程；Play 政策要求与 GDPR 法律义务需分别核验。 | 英文正文已打开；DPO 与各法规条款的全部适用条件未在本专题穷尽。 |
| [执法与制裁](https://commission.europa.eu/law/law-topic/data-protection/information-business-and-organisations/enforcement-and-sanctions_en) | 概述各国数据保护监管机构的调查、纠正和罚款权限；GDPR 最高档行政罚款可达到 2,000 万欧元或全球年营业额 4% 的相应上限。 | 说明法律风险由主管机关依法判断；它不是 Play 对违规采取措施的同一套流程或金额表。 | 英文正文已打开；实际处罚需按条款、情节和监管机关判断。 |
| [处理个人权利请求](https://commission.europa.eu/law/law-topic/data-protection/information-business-and-organisations/dealing-requests-individuals_en) | 介绍收到访问、更正、删除等权利请求后的处理；原则上应在一个月内回复，拒绝时需说明理由与救济途径，明显无根据或过度的请求可适用有限例外。 | 可与 Play 账号/数据删除流程、支持入口和隐私政策流程交叉核对；不能把 Play 的删除规则简化成 GDPR 的全部权利。 | 直接打开报 Internal Error；仅官方搜索索引摘录可读，故标为部分读取，不作为页面全文。 |

## GDPR 儿童个人数据：Article 8 的适用范围、年龄核验与 Play 映射

本分支跟进 Families 计划所举的 GDPR 示例，重点打开欧盟委员会的[儿童数据特别保障说明](https://commission.europa.eu/law/law-topic/data-protection/information-business-and-organisations/legal-grounds-processing-data/are-there-any-specific-safeguards-data-about-children_en)和面向个人的[GDPR 权利说明](https://commission.europa.eu/law/law-topic/data-protection/information-individuals_en)，再沿其儿童数据段落进入 EDPB《[Guidelines 05/2020 on consent](https://www.edpb.europa.eu/documents/guideline/guidelines-052020-on-consent-under-regulation-2016679_en)》。这些材料解释适用法律；它们不会自动变成 Play 审核的新条款。

### Article 8 的触发条件不是“凡儿童数据都要家长同意”

欧盟委员会面向公众的页面概括：当处理儿童数据所依据的是同意时，未达到各成员国所定数字同意年龄的儿童需要父母/监护人授权；具体年龄在 13–16 岁之间，并应核对目标国家门槛。EDPB 指引进一步说明，GDPR Article 8 的这项特别规则须同时满足两个条件：处理与**直接向儿童提供的信息社会服务**相关，且该处理**以 GDPR 同意为法律依据**。GDPR 的其他儿童保护、透明度和一般合法性要求并不因此消失，但 Article 8 不能被简化成所有儿童数据处理或所有应用的统一年龄闸门。

- Article 8 的默认年龄是 16 岁；成员国可以通过法律下调，但不能低于 13 岁。跨境服务应核查服务面向的成员国及各地规则，EDPB 提醒不能一概只看控制者主要营业地的法律。
- “直接向儿童提供”要结合服务定位、内容和营销证据判断。明确仅面向 18 岁以上的服务、且实际内容/推广不与此矛盾时，可能不属于直接向儿童提供；线上服务组件可能符合信息社会服务定义，实物交付本身则不是。
- 对儿童的告知须以儿童能理解的清楚、平实语言呈现。Recital 38 特别提及营销、画像及直接向儿童提供服务时的数据，但 EDPB 指引说明儿童保护不只限于营销或画像。

### 年龄和家长授权核验：按风险、可用技术和数据最小化设计

EDPB 05/2020 指引第 7.1 节（33 页 PDF 的选定部分）要求采取与处理风险相称的合理核验措施，并避免为了证明年龄或家长责任而过度收集个人数据。低风险情形可考虑出生年份/自我声明或父母邮箱等较轻方式，但出生年份并非在所有情形都可靠；高风险处理可能需要更强证明。可信第三方验证也可减少服务方本身接触的数据。GDPR 未统一规定唯一的验证技术，父母责任也不必然只由生物学父母承担。

父母授权不等于永久替代儿童本人控制：儿童达到适用的数字同意年龄后，可以确认、修改或撤回先前的授权同意；控制者应告知其这一选择。直接向儿童提供的预防或咨询服务，在指引所述范围内不需要事先取得父母授权。GDPR 个人数据同意规则与未成年人签订合同的能力是并行但不同的问题。

EDPB《[同意指引全文（PDF）](https://www.edpb.europa.eu/system/files/documents/files/file1/edpb_guidelines_202005_consent_en.pdf)》除儿童专题外，还要求控制者在处理前确定每一目的所依据的合法基础；如果曾选择同意，不能在同意无效或撤回后再追溯改称合法利益来补救。可读的[三页摘要（2026 年 4 月）](https://www.edpb.europa.eu/system/files/2026-04/edpb-summary-consent_en.pdf)把有效同意概括为自由、具体、知情、明确四项累积条件，并说明撤回应与给予同意一样容易。

### 合法利益材料的版本边界

欧盟委员会的法律依据页链接 EDPB《[Guidelines 1/2024 on legitimate interest](https://www.edpb.europa.eu/documents/guideline/guidelines-12024-on-processing-of-personal-data-based-on-article-61f-gdpr_en)》。该页当前仍列出 2024 年公众咨询材料；已打开的[1.0 版全文 PDF](https://www.edpb.europa.eu/system/files/2024-10/edpb_guidelines_202401_legitimateinterest_en.pdf)标注为“公众咨询版本”，不能写成最终版定稿。其三项累积判断是：存在具体、当前且合法的利益；处理对该利益确有必要；数据主体的权利和利益未压过该利益，并须事前评估和记录。EDPB 的[两页摘要](https://www.edpb.europa.eu/system/files/2024-10/edpb_summary_202401_legitimateinterest_en.pdf)提供简表。它帮助理解 Article 6(1)(f)，不改变 Article 8 的触发条件，也不是无效同意的追溯替代方案。

### 儿童子链的直接链接审计与读取边界

| 父页 → 子页 | 内容与关系 | 访问结果 |
| --- | --- | --- |
| [欧盟委员会儿童保障页](https://commission.europa.eu/law/law-topic/data-protection/information-business-and-organisations/legal-grounds-processing-data/are-there-any-specific-safeguards-data-about-children_en) → Article 8、Article 12、Recitals 38/58 | 这 3 个法规引用链接都指向同一个 [EUR-Lex GDPR 正文目标](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?from=EN&uri=CELEX:32016R0679)，是 Article 8 与儿童可理解告知的法条入口。 | 已尝试全部引用；EUR-Lex 仍返回 JavaScript/机器人验证页，本文没有声称直接读到完整 GDPR 正文。 |
| 儿童保障页引用的法规 → [EUR-Lex 替代 CELEX 页面（02016R0679-20160504）](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02016R0679-20160504) | 官方 EUR-Lex 搜索索引返回法规标题及 Article 8 摘要，显示同意处理的默认年龄为 16 岁、成员国可依法下调但不得低于 13 岁，并指出未达门槛时需父母责任人授权。 | 2026-10-23 直接打开该替代 URL 仍只返回 JavaScript/机器人验证页。仅把官方索引摘要作为有限交叉印证；没有读到该 URL 的正文，也不据此声称全文或现行整部 GDPR 已核验。 |
| 同一儿童保障页 → 国家 DPA、网站反馈 | 页面要求按成员国核对年龄门槛；DPA 入口目标为[旧欧委会目录](https://ec.europa.eu/justice/data-protection/bodies/authorities/index_en.htm)，另有[网站反馈表](https://ec.europa.eu/eusurvey/runner/feedback_randUX_survey)。 | 旧目录请求超时；反馈表打开后显示这是匿名的欧委会网站体验调查，未提交。 |
| [Information for individuals](https://commission.europa.eu/law/law-topic/data-protection/information-individuals_en) 的儿童数据段落 → Article 8、Recitals 38/58、国家 DPA | 与儿童保障页交叉说明 13–16 岁门槛、可用技术下的合理核验、儿童友好语言和预防/咨询服务例外。 | 全文已打开；儿童段落里的 3 个法规引用归并到 EUR-Lex 同一目标。DPA 旧路由 [旧 EDPB 地址](https://www.edpb.europa.eu/about-edpb/about-edpb/members_en)实际重定向到 [EDPB Our members 目录](https://www.edpb.europa.eu/about-edpb/our-members_en)，该目录列出成员监管机构；未逐一打开每个国家机构网站。 |
| [EDPB Consent 05/2020 页面](https://www.edpb.europa.eu/documents/guideline/guidelines-052020-on-consent-under-regulation-2016679_en) → 指引 PDF、摘要、乌克兰语礼貌译本、Legal basis 主题 | 正文第 7.1 节是 Article 8 的关键解释；[PDF](https://www.edpb.europa.eu/system/files/documents/files/file1/edpb_guidelines_202005_consent_en.pdf) 33 页，[2026 摘要](https://www.edpb.europa.eu/system/files/2026-04/edpb-summary-consent_en.pdf) 3 页。 | 官方英文 PDF 的第 6 节和 7.1 节定向读取；摘要全文打开。乌克兰语礼貌译本已打开但未用于英文权威文本；格鲁吉亚语下载点击失败且未暴露 URL；[EDPB Legal basis 页面](https://www.edpb.europa.eu/topics/key-gdpr-concepts/legal-basis_en)已打开。全文其他章节与脚注后代未逐项穷尽。 |
| Commission 法律依据页 → [Guidelines 1/2024 页面](https://www.edpb.europa.eu/public-consultations/guidelines-12024-on-processing-of-personal-data-based-on-article-61f-gdpr_en)、[现行文档页](https://www.edpb.europa.eu/documents/guideline/guidelines-12024-on-processing-of-personal-data-based-on-article-61f-gdpr_en)、PDF 与摘要 | 补充说明合法利益的适用判断及其与同意基础的边界。 | 页面和摘要已打开；全文仅读取重点段落，版本标记为 1.0 公众咨询稿。公众反馈附件、全部引文和后续版本未逐项展开。 |
| [透明度指南索引](https://ec.europa.eu/newsroom/article29/items/622227) | Commission 的个人信息说明页还链接到 Article 29 Working Party 2018 Transparency 指南页面，关联儿童告知的清楚、平实语言背景。 | 标题/日期页已打开；其 PDF 与 ZIP 下载未能读取，因此不把指南全文内容算作已总结。 |

**对 Play 审查的落点：**先按实际目标国家、受众、服务形态和每种处理目的确定适用法律及合法基础；只有 Article 8 两个条件都满足时，才按各成员国数字同意年龄实施父母授权和相称的年龄/授权核验。随后检查面向儿童的隐私告知、数据最小化、授权达到年龄后的控制路径，以及 SDK/广告数据流。再分别核对 Play Families、User Data、醒目披露/同意和 Data safety；任何一组满足都不代替另一组。

该分支的关键判断是“官方程度”和“适用边界”：Google Play 计划页对法律的举例不会使所有应用自动落入 GDPR；GDPR.eu 的易读材料也不会替代官方法规。欧盟委员会六页是说明性指南，而非整部法规的替代文本。现在已补入 Article 8 儿童数据子链及两组 EDPB 指引的相关章节；EUR-Lex 原始 HTML 与替代 CELEX 页面仍未能直接打开，官方搜索索引只提供有限 Article 8 摘要。其他条文/监管指南、GDPR.eu 的 FAQ、清单、模板、新闻和各国监管机构的外部页面仍未全部递归。

## 建议的核对顺序

1. 先按[用户数据政策](../user-data/user-data.zh-CN.md)核查 Google Play 强制义务、SDK 数据流、Data safety、隐私政策、披露/同意和删除。
2. 用[醒目披露最佳实践](https://support.google.com/googleplay/android-developer/answer/11150561?hl=en)检查界面、拒绝路径和声明视频。
3. 对法国/欧洲适用情形，先依据欧盟委员会企业指南、GDPR 正文和本页儿童 Article 8 分析判断地域、角色、服务和法律基础；再结合 CNIL 建议书、ePrivacy 和本地法律核实权限、同意与用户权利。Families SDK 专题引用的 GDPR.eu 仅作非官方入门背景。
4. 遇到由 Google 提供的 EEA/英国/瑞士来源个人信息或跨境传输时，再检查 User Data 条款、具体合同、Google 服务适用的传输机制和开发者自身义务；分别确认 DPF 组织/数据范围和 Controller Terms 的服务纳入/接受状态。

本页与[Android 隐私清单](../android-privacy-checklist/android-privacy-checklist.zh-CN.md)、[第三方 SDK 要求](../sdk-requirements/sdk-requirements.zh-CN.md)、[Data safety 表单](../data-safety/data-safety.zh-CN.md)和[账号删除](../account-deletion/account-deletion.zh-CN.md)互链。目标页和后代访问状态见逐 URL 来源台账（快照：`../SOURCE_LEDGER.md`，未导入本仓库）及双语递归链接图（快照：`../google-play-policy-link-graph.md`，未导入本仓库）。
