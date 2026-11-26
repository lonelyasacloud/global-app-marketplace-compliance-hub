---
id: google-play.families-self-certified-ads-program
platform: google-play
language: zh-CN
authority: operational
status: current
kb_checked_at: 2026-10-24
review_due: 2027-01-24
regions: [global]
topics: [families, child-directed-ads, self-certified-sdk, mediation, sdk]
snapshot_id: play.families-self-certified-ads-program
snapshot_package: "GooglePlay-KnowledgeBase-2026-10-24-review.zip"
coverage_status: "detailed-summary"
source_url: "https://support.google.com/googleplay/android-developer/answer/9900633?hl=en"
source_url_zh: "https://support.google.com/googleplay/android-developer/answer/9900633?hl=zh-Hans"
effective_date: "current-snapshot"
---

# Google Play Families 自认证广告 SDK 计划

> **导入说明（Google batch 3）。** 本页正文取自 2026-10-24 Google Play 知识库快照里已经分开的对应语言改写（`play.families-self-certified-ads-program`，核对日 2026-10-24），不是官方页面的逐字文本。英文官方来源是效力来源。`kb_checked_at` 使用快照源文件记录的核对日；本次导入没有重新打开线上官方页面。文中“本知识库”“本库”“本地专题”描述的是该快照知识库的覆盖范围，不是本仓库已经导入的页面清单。快照里指向尚未导入本仓库的专题、链接图、台账或 CSV 的相对链接，已改为文字提及；指向 Google batch 1、batch 2 或本批九个专题的相对链接已改到本仓库路径。2026-10-24 快照重开了英文和 `zh-Hans` 计划页。水印与测试应用文章的中文直接抓取返回 Internal Error；该文的英文正文已打开。该失败不表示政策已经变更。计划页写明暂停接受新申请，重新开放时间将在该页公布。快照没有记录重新开放日期，暂停也不是对重新开放的预测。现有参加者的要求记为不变。旧页面上关于被拒后三个月再申请的措辞，不能证明申请窗口已经打开。这些计划要求是 `operational`，适用于广告 SDK 向儿童投放广告的情形。它们不替代 Families 政策、User Data，也不转移发布者自己的责任。厂商与 SDK 版本表留在未导入的第三方 SDK 快照专题中，此处不复制。

**核对日期：2026-10-24。** 本专题把计划说明页的适用范围、SDK 提供商要求、发布者责任及正文直链放在一起。它是双语摘要和导航，不是 Google 原文，也不复制现有专题里的完整厂商版本表。2026-10-24 重开英文与 `zh-Hans` 计划页、英文 SDK 政策、现行版本清单和期限表：新申请仍暂停，现有参加者要求不变；清单仍为 14 个 Maven 行、13 个不同供应商目标。2026-10-23 的离线版本表快照未发现变化；它仍不是发布前资格证明。

## 当前状态与适用范围

计划说明页目前写明：**暂停接受新的申请，开放时间和后续指南将在该页公布；现有参加者的计划合规要求维持不变。** 这是 2026-10-23 核对时的状态快照，不是未来重新开放的预测，也不是已知的重新申请日期。

只有应用使用广告 SDK **向儿童投放广告**时，才要求所用版本属于 Google Play 当前列出的自认证版本。若应用受众同时包括儿童和较年长用户，展示给儿童的广告必须全部来自自认证 SDK；页面举例为使用中立年龄筛查。应用的 Play 受众声明、广告对象、SDK 初始化和广告请求路径应相互一致。

页面列出的两种无需 SDK 自认证的场景是：

1. 使用 SDK 管理自有应用、其他自有媒体或商品的站内推广（in-house advertising）。
2. 与广告商直接交易，SDK 仅用于广告库存管理。

这些例外只涉及**广告 SDK 的自认证要求**。开发者仍对广告内容、数据收集和共享负责，且仍须遵守 [User Data](https://support.google.com/googleplay/android-developer/answer/10144311?hl=en)、[Families 政策](https://support.google.com/googleplay/android-developer/answer/9893335?hl=en)及适用法律。计划页面特别说明，Google 不保证 SDK 提供商在自认证过程中提交信息的准确性；采用已列出的 SDK 不会转移应用开发者责任。

## SDK 提供商的要求

| 要求面 | 可核验的计划条件 | 发布者/集成方的检查点 |
| --- | --- | --- |
| 禁止内容与合同 | 在 SDK 条款或政策中定义并禁止不当广告内容和行为；定义应符合 Play 开发者政策。 | 查看 SDK 的广告内容政策和合同边界；供应商声明不能取代应用方审查。 |
| 创意分级 | 建立适龄分级机制，至少包含 Everyone 和 Mature；与 Google 向申请者提供的方法一致。 | 确认所选广告位、创意评级和儿童/全年龄库存的配置。 |
| 儿童定向处理 | 允许发布者按请求或应用要求启用 child-directed treatment，并符合法律；处理须关闭个性化广告、基于兴趣的广告和再营销。 | 在所有儿童广告请求、瀑布流/竞价和中介路径中传递一致的儿童处理信号。 |
| 广告格式 | 提供符合 [Families 广告与变现规则](https://support.google.com/googleplay/android-developer/answer/9893335?hl=en)及 Teacher Approved 计划标准的格式。 | 按儿童实际看到的广告、插页时点、可关闭性、误触风险和商业提示审查。 |
| 实时竞价 | 面向儿童的实时竞价素材须经审核，并向竞价方传播隐私指示。 | 查证竞价链每一跳都能接收并保留适龄/隐私信号。 |
| 申请证据与版本治理 | 提交足够资料和测试应用；及时响应后续资料请求；新 SDK 版本发布时自我认证符合最新政策。 | 不把旧版本的历史审核当作新版本当前认证证明。 |
| 适用法律 | 支持遵守可能适用于出版者的儿童相关法规。 | 按市场、受众、数据和交易逐项评估法律适用；不得把 Help 页示例误作穷尽法律清单。 |

### SDK 与中介提供商的独立政策页

[Families Self-Certified Ads SDK Policy](https://support.google.com/googleplay/android-developer/answer/12918983?hl=en) 是与计划说明不同的正式政策页面，补充 SDK/中介提供商的明确义务：披露对儿童个人/敏感数据的访问、收集、使用和分享，并将用途限制在已披露范围；不得把儿童或年龄未知用户的 AAID、SIM Serial、Build Serial、BSSID、MAC、SSID、IMEI 或 IMSI 传输出去；儿童定向请求须停用个性化广告、兴趣定向和再营销。实时竞价素材须预先审核并把隐私指示传给竞价方。广告还须适龄、清楚可辨，不能误导误触或操纵儿童；干扰正常应用/游戏使用的广告须在 5 秒后可关闭。违反政策可能导致 SDK/中介从计划中除名或暂停。

SDK 提供商还须提交英文版服务条款、隐私政策和发布商集成指南，以及使用最新合规版本、可访问完整实时库存的测试 APK；需及时答复资料请求，并对新版本按最新政策重新自我认证。完整条文、正文直接子链及访问边界见第三方 SDK 要求专题（[Google Play 第三方 SDK 要求与安全集成](../sdk-requirements/sdk-requirements.zh-CN.md)）和递归图 §4.114。SDK 认证不替代应用发布者依照 [User Data](../user-data/user-data.zh-CN.md) 与 [Families 政策](../age-restricted-child-safety/age-restricted-child-safety.zh-CN.md)承担的数据、受众和广告责任。

### 中介平台

儿童广告的中介平台应当只使用 Families 自认证 SDK，**或**实施足以确保经中介投放的所有广告都符合上述要求的保护措施；并须把广告内容评级及适用的儿童定向处理信息传给中介平台。该条款不是“只要采用某个认证 SDK，所有中介层就自动合规”的豁免。

## 认证证据、水印和测试应用

当前逐版本名单见 [Families 自认证广告 SDK 版本清单](https://support.google.com/googleplay/android-developer/answer/12955712?hl=en)，14 个 Maven 行、13 个不同厂商目标和厂商/版本差异已经整理在第三方 SDK 专题（[Google Play 第三方 SDK 要求与安全集成](../sdk-requirements/sdk-requirements.zh-CN.md)）。名单会变动，须在每次发布或升级时回到官方实时页核对；离线快照不能证明某个新版本现在仍获认证。

[水印与测试应用页面](https://support.google.com/googleplay/android-developer/answer/9536665?hl=en)要求：

- 自认证 SDK 应以文字、图像、第三方图标、URL 或跳转页等可辨认方式标识广告素材；水印须出现在该 SDK 库存的**每个广告素材**上。
- 测试应用应使用与线上相同或镜像的库存，并提交可执行的手机形态完整 Android APK。
- 测试应使用最新已发布或即将发布且符合政策的 SDK，实际调用广告获取和展示功能。
- 测试应用应能访问网络上的全部实时投放库存，不得按地理位置限制；混合受众库存须能区分完整库存与儿童/全年龄适用库存，除非由有效中立年龄筛查控制，不得只展示选定广告。
- 仅使用自有广告方案的提供商不适用该自认证流程。

水印页面仍提到拒绝后 3 个月内不能重新申请；但计划总览在本次快照中明确暂停新申请。不能把旧页面的个别申请流程文字解释成当前有开放申请窗口。表单字段也没有公开可读状态，见下表。

## 计划说明页的正文直链逐项登记

以下按页面中可见正文链接顺序登记 11 次链接引用（Help 社区、Contact 和页面侧栏属于 Help 导航，不计入正文 11 项）。某些旧路由会重定向；表中的政策意义以当前可读的目标页为准。

| 正文链接 | 目标页与关系 | 本次访问/边界 |
| --- | --- | --- |
| [Families Policy](https://support.google.com/googleplay/android-developer/answer/9893335) | 上位儿童政策；规定受众声明、儿童数据、SDK、广告和应用功能边界。 | 正文已打开；儿童广告和政策交叉关系见[儿童安全专题](../age-restricted-child-safety/age-restricted-child-safety.zh-CN.md)。 |
| [User Data Policy](https://support.google.com/googleplay/android-developer/answer/9888076) | 计划明确要求开发者仍遵循 User Data 的披露、数据用途和处理义务。旧 URL 重定向至[现行正文](https://support.google.com/googleplay/android-developer/answer/10144311)。 | 目标正文已打开；旧链路与现行页均在逐 URL 台账记录。 |
| [U.S. COPPA](https://www.ftc.gov/tips-advice/business-center/privacy-and-security/children%27s-privacy) | 美国儿童隐私法律资源入口；计划示例要求考虑适用儿童法规。 | 旧地址重定向至 FTC 当前[Children’s Privacy](https://www.ftc.gov/business-guidance/privacy-security/childrens-privacy)入口；具体法律适用按市场和数据判断。 |
| [GDPR](https://gdpr.eu/) | 提供 GDPR 入门背景。该网站声明由 Proton AG 运营、并非欧盟委员会/政府官方资源，也不提供法律意见。 | 本专题沿其官方跳转链接进一步打开[欧盟委员会企业与组织指南](https://commission.europa.eu/law/law-topic/data-protection/information-business-and-organisations_en)及六个下级主题；并把 Article 8 儿童数据、同意年龄、核验边界与 EDPB 指引补入用户数据外部法律参考（[用户数据政策的外部法律与参考资源](../user-data-policy-references/user-data-policy-references.zh-CN.md)）和递归图 §4.120。EUR-Lex 正文、各国 DPA 网站和其他法条/EDPB 后代仍未穷尽。 |
| [Families Ads and Monetization](https://play.google.com/about/families/ads-monetization/) | 旧 Google Play 家庭广告入口；当前可读的权威条文在 Families 政策帮助页。 | 2026-10-23 从 SDK 政策正文再次点击时观察到该旧路由重定向至[当前 Families 政策](https://support.google.com/googleplay/android-developer/answer/9893335)，但抓取工具在跟随跳转时返回错误；当前目标正文已单独打开。该旧路由不构成独立条款。 |
| [Teacher Approved course](https://playacademy.exceedlms.com/sl/044a202e) | Play Academy 课程介绍广告和 IAP 的教师认证标准，并提醒避免让 13 岁以下儿童困惑、分心、受操纵或过度商业化。 | 短链重定向至[课程页面](https://playacademy.exceedlms.com/student/path/22151/activity/32755)；简介可读，课程内容需登录，属于培训资料而非政策正文。 |
| [旧版 interest form](https://docs.google.com/forms/d/e/1FAIpQLSc8msikGDxjTHHFmIECoitMnpudaCbtrb_hhgzpUOznPhDoBw/viewform?p=adnet) | 表单页说明已弃用并指向新版表单。 | 已确认关闭页与新版地址；新版字段无法读取，且计划暂停新申请，不推断申请资格或字段。 |
| [Self-certify](https://support.google.com/googleplay/android-developer/answer/12253906) | 当前点击目标跳转到[Policy Deadlines 表](https://support.google.com/googleplay/android-developer/table/12921780)。 | 目标表正文已打开。表中 Families Policy 的 2026-08-26 行对应匿名聊天应用不得面向儿童的扩展规则；它不是广告 SDK 认证或重新申请期限。 |
| [Watermark and test app requirements](https://support.google.com/googleplay/android-developer/answer/9536665) | SDK 自认证的素材标识和测试 APK 要求。 | 英文正文已打开并在上节概括；本次工具直接打开了英文版，中文直链返回内部错误。 |
| [Families SDK list](https://support.google.com/googleplay/android-developer/answer/9283445) | 历史入口指向现行 SDK/版本列表。 | 重定向至[当前名单](https://support.google.com/googleplay/android-developer/answer/12955712)；14 个 Maven 行、13 个不同厂商目标另见 SDK 专题。 |
| [Share the interest form](https://support.google.com/googleplay/android-developer/?p=adnet) | Help 路由会通向同一个新版申请表。 | 公开抓取未能读取表单内容；没有通过空白/错误响应推断表单字段。 |

## 实操核对顺序

1. 在 Play Console 准确选择目标受众，并确认应用内容确实符合该受众。
2. 追踪每个广告请求到最终展示用户的路径，明确儿童、未知年龄、较年长用户分别走哪些 SDK、中介和竞价供应商。
3. 对儿童展示请求核对 SDK 与具体版本是否仍在[官方当前名单](https://support.google.com/googleplay/android-developer/answer/12955712?hl=en)中，逐项检查 child-directed treatment、关闭个性化/兴趣定向/再营销、评级信号和中介信号。
4. 审查全部儿童可见素材、广告格式、误触/遮挡/过度商业化和 IAP 提示；检查供应商的条款、内容评级、创意审核与变更通知。
5. 对 SDK 收集、使用、分享的数据统一核对 [User Data](../user-data/user-data.zh-CN.md)、[Data safety](../data-safety/data-safety.zh-CN.md)、隐私政策、醒目披露与同意，并按实际分发地区评估当地法律。
6. 发布前再次查看实时 SDK 名单、政策正文及 Play Console 的账号专属通知；发生 SDK 升级、供应商切换或受众/广告路径变化时重新审查。

## 与本知识库其他专题的关系

- 第三方 SDK 要求（[Google Play 第三方 SDK 要求与安全集成](../sdk-requirements/sdk-requirements.zh-CN.md)）：SDK 厂商、版本坐标、公告和深层技术/供应商后代；本专题不复制完整厂商表。
- [年龄限制与儿童安全](../age-restricted-child-safety/age-restricted-child-safety.zh-CN.md)：Families 上位政策、儿童可见内容、受众与社交安全规则。
- [用户数据](../user-data/user-data.zh-CN.md)和用户数据外部法律参考（[用户数据政策的外部法律与参考资源](../user-data-policy-references/user-data-policy-references.zh-CN.md)）：Play 数据义务、GDPR 官方入门指引与外部法源的层级。
- [付款与订阅](../payments/payments-and-subscriptions.zh-CN.md)：Monetization and Ads Help 导航关系；广告 SDK 计划不会改变 Play Billing 或订阅义务。

访问状态、重定向与更深页面边界见逐 URL 来源台账（快照：`../SOURCE_LEDGER.md`，未导入本仓库）和双语递归链接图 §4.114（快照：`../google-play-policy-link-graph.md`，未导入本仓库）。本轮覆盖可读的计划正文和重要直接目标，但不声称 Help 侧栏、课程、表单、厂商页面、GDPR 条文及所有外部后代已递归闭合。
