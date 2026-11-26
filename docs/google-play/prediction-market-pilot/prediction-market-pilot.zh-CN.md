---
id: google-play.prediction-market-pilot
platform: google-play
language: zh-CN
authority: operational
status: current
kb_checked_at: 2026-10-22
review_due: 2027-01-22
regions: [global]
topics: [prediction-markets, real-money, licensing, pilot, financial-features]
snapshot_id: play.prediction-market-pilot
snapshot_package: "GooglePlay-KnowledgeBase-2026-10-24-review.zip"
coverage_status: "detailed-summary"
source_url: "https://support.google.com/googleplay/android-developer/answer/16902027?hl=en"
source_url_application: "https://support.google.com/googleplay/android-developer/contact/Application_Pilot_Program_for_Prediction_Market_Apps"
effective_date: "pilot; 2026-06-01 deadline for apps already on Play has passed; no recorded end date; no 2027-01-27"
---

# Google Play 预测市场真钱功能试点

> **导入说明（Google batch 6）。** 正文来自已经分开的 2026-10-24 Google Play 知识库快照（`play.prediction-market-pilot`，核对日 2026-10-22）的改写摘要，不是官方页面的逐字副本。英文官方页面是效力来源。`kb_checked_at` 是快照源文件记录的核对日；本次导入没有重新打开线上官方页面。文中“本知识库”“本库”“本地专题”等说法描述的是该快照库的覆盖范围，不是本仓库已经导入的页面。指向本仓库没有收录的专题、链接图、台账或 CSV 的相对链接改为文字提及。指向 Google batch 1–5 或本批九个专题的相对链接改为本仓库文件。核对日 2026-10-22。两种语言文件引用的都是英文帮助页 `hl=en`。快照没有记录中文官方 URL，也没有记录已核对的中文官方试点页。本仓库中文正文是英文来源的编辑改写。已经在 Play 上的应用须在 2026-06-01 前加入试点的期限已经过去。帮助页没有写明试点结束日。Google 可以修改、暂停或终止试点。本页没有记录 2027-01-27。本试点是 operational 计划说明。它不替代真钱赌博政策。以赌博或博彩牌照提供预测市场的应用不在本试点内，应走该政策。全球试点公告不是每个市场的现行资格。截至本次核对，帮助页只接受面向美国、持有美国金融或同等牌照的应用。**

## 当前状态

官方[预测市场试点帮助页](https://support.google.com/googleplay/android-developer/answer/16902027?hl=en)于 2026-10-22 核验。2026-04-15 公告要求当时已在 Play 上提供真钱预测市场功能的应用在 **2026-06-01 前**加入试点；该期限已经过去。现行帮助页仍说明申请按滚动方式评估，但未规定试点何时结束，并称 Google 可修改、暂停或终止试点。是否仍能提交、应用能否参加，应以当前表单与 Play Console 的实际状态为准。

公告称试点面向全球开发者，现行帮助页进一步限定：截至本次核验，项目**仅接受面向美国市场的美国金融或等效牌照**；其他国家/地区可能在试点期间评估加入。不可把“全球试点”理解成各市场都已获准。

## 适用范围与分流

| 应用形态 | 处理方式 |
| --- | --- |
| 接受金钱或加密资产等现实价值，并围绕事件结果/未发生提供现实价值的交换或交易 | 属于预测市场真钱功能；必须加入试点后才可在 Play 提供该功能。 |
| 只展示预测市场资讯、没有现实价值交易 | 不属于该试点的入组范围；仍须符合其他 Play 政策。 |
| 通过按钮、导航入口或其他 CTA 引导用户参与站外真钱交易 | 仍受试点规则/限制约束，不能仅因交易发生在应用外就视为豁免。 |
| 依据真钱赌博或游戏牌照提供预测市场 | 不加入预测市场试点；应符合[真钱赌博、游戏与竞赛政策](../real-money-gambling/real-money-gambling.zh-CN.md)及其审批条件。 |
| 接受加密货币付款 | 还须遵守[区块链内容政策](../crypto-assets-and-nfts/crypto-assets-and-nfts.zh-CN.md)及金融功能申报要求。 |

## 入组条件

- **开发者与申请：** 必须持有已验证的组织开发者账号；个人账号不符合试点资格。完成 Play Console 金融功能申报中的“Prediction markets”选项，提交试点申请、牌照/注册材料，并提供审核所需的登录信息。
- **牌照与市场：** 对每个目标市场提供有效的金融、商品或等效监管机构许可/注册。美国示例包括 CFTC 注册的 Designated Contract Market、NFA 注册的 Introducing Broker 或 Futures Commission Merchant。特定开发者/应用的 CFTC No-Action letter 可作为认证材料，但必须能在 CFTC 数据库公开查到。应用只能面向试点涵盖、持有有效许可且当地法律允许的地区。
- **年龄和分级：** 应达到 Adults Only (AO) 或 IARC 18+ 等效评级，并有效阻止未成年人使用。混合内容应用可能需要调整整体分级，或将预测市场功能拆分到单独的 AO 应用。
- **价格与负责任使用：** 应用须免费下载；在应用及商店详情披露负责任使用提示，并允许用户设置账户限制，例如存款、获利、亏损上限或自我排除。
- **交易透明度：** 申请条款要求在交易执行前清楚列出费用、合约条款和结算规则。许可失效、未成年人可访问或不再符合试点条款时，Google Play 可立即移除应用。
- **交叉合规：** 还须遵守所有 Developer Program Policies、Developer Distribution Agreement、适用法律和试点条款；试点接受不替代当地金融/博彩法律判断。

## 公告正文链接及目标页关系

2026-10-22 对试点帮助页正文中的 **11 个链接锚点、9 个不同目标**逐项处理。申请表锚点出现两次，Blockchain policy 锚点也出现两次。帮助页页脚的通用社区/联系入口未计入正文链接。

| 正文直接目标 | 关系、核验结果与后代 |
| --- | --- |
| [Prediction Market pilot application form](https://support.google.com/googleplay/android-developer/contact/Application_Pilot_Program_for_Prediction_Market_Apps) | 表单公开部分要求授权代表、组织/牌照名称、国家地区、牌照类型、Play 开发者账号、包名和应用名称；条款要求按许可地区限制真钱功能、交易前披露费用/条款/结算方式，并允许因牌照失效、分级/未成年人控制或其他不合规立即下架。表单显示只有 Google 接受申请后才形成有约束力的参与关系。表单页还链接 [Google 隐私政策](https://policies.google.com/privacy?hl=en) 和 [Google 服务条款](https://policies.google.com/terms?hl=en)；它们是支持表单的通用条款，不构成额外 Play 试点资格。表单内“account and system information”在本次点击中返回同一表单地址，未解析出独立目标。 |
| [Play Console Financial features declaration](https://play.google.com/console/developers/app/app-content/financial-features) | 试点申报入口；跳转到账号登录，应用级申报状态和实际选项不能公开核验。 |
| [Requirements for providing sign-in details for review](https://support.google.com/googleplay/android-developer/answer/15748846) | 审核凭证要求：账号需可重复使用、持续有效、跨地区可访问；以英文提供，且为 OTP/双重验证准备可重复使用的绕过凭证或静态访问链接。参见[Play Console 审核准备](https://support.google.com/googleplay/android-developer/answer/9859455)。凭证须在 Play Console 账号内维护。 |
| [Real-Money Gambling, Games, and Contests](https://support.google.com/googleplay/android-developer/answer/9877032) | 若属于真钱赌博许可路线，按该政策及其独立申请流程审核；试点帮助页明确二者不可混为一类。详见[真钱赌博专题](../real-money-gambling/real-money-gambling.zh-CN.md)。 |
| [Google Play Developer Policy Center](https://play.google/developer-content-policy/) | 汇总 51 个政策主题入口，知识库政策链接图（快照：`../google-play-policy-link-graph.md`，未导入本仓库）已登记；目录子页的后代状态以各专题页和来源台账为准。 |
| [Inappropriate Content](https://support.google.com/googleplay/android-developer/answer/9878810) | 试点条款要求同时遵守的一般内容政策；见[不当内容专题](../inappropriate-content/inappropriate-content.zh-CN.md)。 |
| [Blockchain-based Content](https://support.google.com/googleplay/android-developer/answer/13607354) | 接受加密货币时的额外政策；涵盖金融功能申报、代币化资产标识、服务许可及 NFT 赌博边界；见[加密资产与 NFT 专题](../crypto-assets-and-nfts/crypto-assets-and-nfts.zh-CN.md)。此链接在主文中重复出现，两个位置均已计入锚点数。 |
| [Google Play Developer Distribution Agreement](https://play.google/developer-distribution-agreement.html) | 试点申请并入的开发者分发协议；当前协议摘要及核验日期见[中英文协议专题](../developer-distribution-agreement/developer-distribution-agreement.zh-CN.md)。 |
| [CFTC Staff Letters 数据库](https://www.cftc.gov/LawRegulation/CFTCStaffLetters/letters.htm?field_csl_letter_types_target_id%5B%5D=636) | 官方 No-Action letter 动态目录。2026-10-22 页面按 No-Action 筛选，但当前列表首项涉及 perpetual futures，并非预测市场许可；须检查具体开发者/应用的函件，不能把“目录中有函件”当作入组批准。 |

## 核验边界与复查提示

- Play Console 金融功能表单需要登录；试点期限不明确，项目范围会动态变化。
- 申请表的 Google 隐私政策与 Google 服务条款属于通用条款，其后代链接不纳入 Play 试点政策闭包。
- Developer Policy Center 的 51 个政策入口和本专题直接政策目标已在知识库其他页面整理；每个专题页面的深层 API、地区法规、表单及侧栏推荐仍不代表递归闭合。
- CFTC No-Action letter 目录随时更新。每份函件适用对象和条件不同，必须核对是否明确针对该应用/主体。

## 关联主题

- [真钱赌博、游戏与竞赛](../real-money-gambling/real-money-gambling.zh-CN.md) · [金融服务与贷款](../financial-services-and-loans/financial-services-and-loans.zh-CN.md)
- [加密资产与 NFT](../crypto-assets-and-nfts/crypto-assets-and-nfts.zh-CN.md) · [年龄限制与儿童安全](../age-restricted-child-safety/age-restricted-child-safety.zh-CN.md)
- Play Console 要求[Play Console 要求](../play-console-requirements/play-console-requirements.zh-CN.md) · 2026-04-15 公告与全部直链摘要（快照：`../google-play-announcement-resources.md`，未导入本仓库）
