---
id: google-play.financial-services-and-loans
platform: google-play
language: zh-CN
authority: normative
status: current
kb_checked_at: 2026-10-23
review_due: 2027-01-23
regions: [global]
topics: [financial-services, personal-loans, earned-wage-access, financial-features-declaration, sensitive-permissions]
snapshot_id: play.financial-services
snapshot_package: "GooglePlay-KnowledgeBase-2026-10-24-review.zip"
coverage_status: "detailed-summary"
source_url: "https://support.google.com/googleplay/android-developer/answer/9876821?hl=en"
source_url_declaration: "https://support.google.com/googleplay/android-developer/answer/13849271?hl=en"
source_url_india: "https://support.google.com/googleplay/android-developer/answer/16604194?hl=en"
source_url_update_line_of_credit: "https://support.google.com/googleplay/android-developer/answer/15899442?hl=en"
source_url_update_short_term_loans: "https://support.google.com/googleplay/android-developer/answer/16296680?hl=en"
source_url_update_thailand: "https://support.google.com/googleplay/android-developer/answer/16797260?hl=en"
source_url_update_ewa: "https://support.google.com/googleplay/android-developer/answer/17134731?hl=en"
source_url_zh: "https://support.google.com/googleplay/android-developer/answer/9876821?hl=zh-CN"
effective_date: "current policy; Thailand existing-app date 2026-03-04 has passed; no 2027-01-27 on this page"
---

# 金融服务声明、个人贷款与工资预支

> **导入说明（Google batch 6）。** 正文来自已经分开的 2026-10-24 Google Play 知识库快照（`play.financial-services`，核对日 2026-10-23）的改写摘要，不是官方页面的逐字副本。英文官方页面是效力来源。`kb_checked_at` 是快照源文件记录的核对日；本次导入没有重新打开线上官方页面。文中“本知识库”“本库”“本地专题”等说法描述的是该快照库的覆盖范围，不是本仓库已经导入的页面。指向本仓库没有收录的专题、链接图、台账或 CSV 的相对链接改为文字提及。指向 Google batch 1–5 或本批九个专题的相对链接改为本仓库文件。快照 YAML 的 `reviewed_on` 是 2026-10-23。开篇写核对日为 2026-10-22。这些快照日期不是政策变更。中文源文件记录的是 `hl=zh-CN` 帮助地址。英文源文件和链接表使用 `hl=en`。快照没有记录 `hl=zh-CN` 抓取失败，也没有记录已逐行核对的中文官方金融服务页面。本仓库中文正文是快照的编辑改写。泰国既有应用的合规日 2026-03-04 已经过去。RBI 名录日期是监管背景，不是 Play 生效日。预测市场 2026-06-01 的期限已经过去，留在该专题。本页没有记录 2027-01-27。金融服务政策是 `normative`。声明帮助文章和 Console 步骤是 operational。Play 申报不是当地金融牌照。个人贷款的权限限制与敏感权限页上的一般金融安全例外分开。**

**核对日期：2026-10-22。** Google Play 的金融服务政策覆盖资金/加密资产管理与投资、个性化金融建议和贷款服务。所有含金融功能的应用都须在 Play Console 提交 Financial features declaration；个人贷款、贷款导流和工资预支（EWA）另受商店资料、许可文件、敏感权限和目标市场当地规则约束。金融申报并不等于当地金融牌照，也不代表 Google 已批准每个市场的经营资格。

## 每个应用都要完成的金融功能声明

有 Google Play 已发布应用的开发者必须在 **App content → Financial features** 准确申报功能；即使没有任何金融功能，也要选择“应用不提供金融功能”。要求涵盖封闭测试、开放测试和生产轨道，以及通过 Play 更新的预装应用。官方帮助页列明的例外为符合定义的 system services 和 private apps；一般预装应用或企业应用不能仅凭名称自行认定豁免。

表单功能类别包括：

| 类别 | 申报例子 |
| --- | --- |
| 银行业务与贷款 | 个人贷款直接放贷、贷款撮合、发薪日贷款、银行业务、信用额度、工资预支、微型金融 |
| 支付与转账 | 移动支付/数字钱包、汇款和电汇 |
| 购买协议 | 奖励积分/里程等激励、先买后付（BNPL） |
| 交易与基金 | 加密货币钱包/交易所、NFT 销售/交易/奖励、股票交易/投资组合管理、众筹/Chit Fund |
| 支持服务 | 信用监控/报告、金融建议、保险、其他 |

所有贷款相关申报需准确体现直接放贷、导流/撮合或第三方合作方模式。个人贷款相关应用还须提供合作贷款方及其与开发者业务关系；目标市场要求额外材料时，按国家上传有效牌照或证明。申报内容、商店资料、合作方名单和应用真实功能必须一致。

## 个人贷款与信用额度

Play 将个人贷款定义为向个人消费者非经常性借款，不包括为购买固定资产或教育融资。帮助页例子包括个人贷款、发薪日贷款、点对点贷款和产权抵押贷款；房贷、车贷及循环信用额度（如信用卡和个人信用额度）不在该定义的例子中。2025 年公告又说明个人贷款规则扩展至信用额度应用；现行规则明确将以撮合个人贷款/信用额度为主要用途的应用纳入敏感数据限制。具体产品分类须结合真实金融结构及当前政策，不能仅依营销名称判断。

个人贷款直接放贷方、贷款导流方和连接第三方贷款机构的应用必须：

- Play 商店应用类别设为 **Finance**。
- 在商店资料披露最短/最长还款期、最高 APR、包含本金与全部适用费用的代表性总成本示例，以及完整说明个人/敏感数据访问、收集、使用和共享情况的隐私政策。
- APR 通常包括利息、费用和年度其他成本；若当地法律规定不同算法，按当地法律一致计算并重新核对披露。
- 按所有投放地区取得并维持所需许可，且能证明牌照与 Play 开发者账号/合作主体关系。

原则上不允许要求在放款后 **60 天或更短时间内全额偿还**的短期个人贷款。2025-07 政策公告说明，只有巴基斯坦可能存在受当地法规明确要求、且依当地法律法规提供的有限例外；这不是一般豁免，仍须满足巴基斯坦 SECP 审批及国家条款。

**美国：**个人贷款 APR 达到或超过 **36%** 的应用不允许上架；最高 APR 须按 Truth in Lending Act（TILA）一致计算并披露。直接贷款、贷款导流和连接第三方贷款机构都适用。

## Earned Wage Access（EWA，工资预支）

现行政策将 EWA 描述为用户提取本工资周期内已经挣得、但尚未发放的工资。Play 在政策文本中的典型特征是：金额限于已挣工资；通常通过工资扣款或关联银行账户自动还款，自动扣款失败不应额外产生利息、罚金或费用；通常不收利息，而以低额固定费或按次费用为主；通常不向信用机构报告交易，避免影响信用评分或形成长期债务。政策页面给出 $1–$5/笔或预支金额 1–5% 作为费用量级示例；这些是政策对 EWA 典型模式的描述，不是跨市场的法定上限或“安全港”，仍须检查当地法规及收费透明度。

EWA 直接提供者、导流方和第三方连接服务同样须设 Finance 类别，并在商店资料披露还款条件、所有费用（含订阅费/交易费）、含全部费用的代表性总成本示例和隐私政策。2026-07 公告重申 EWA 须满足与其他金融服务同等级别的透明度和隐私保护。

## 金融贷款应用的敏感数据/权限禁区

个人贷款应用、以撮合个人贷款或信用额度为主要用途的应用、贷款/信用额度计算器或指南等辅助应用，以及 EWA 应用，不得访问政策列出的敏感信息，并不得声明以下权限：

`READ_EXTERNAL_STORAGE`、`READ_MEDIA_IMAGES`、`READ_CONTACTS`、`ACCESS_FINE_LOCATION`、`READ_PHONE_NUMBERS`、`READ_MEDIA_VIDEO`、`QUERY_ALL_PACKAGES`、`WRITE_EXTERNAL_STORAGE`。

这项专项限制与一般敏感权限政策、User Data、隐私政策和 Data safety 要求叠加适用。权限清单中未出现某项权限，并不自动代表该权限可以使用；例如 SMS/通话记录还受默认处理器和用途限制。对文件/联系人等用户主动提供的数据，应评估[系统 Photo Picker](../photo-video-permissions/photo-video-permissions.zh-CN.md)、联系人选择器或其他最小范围替代方案，并按其他适用政策判断。

## 国家/地区贷款材料（现行 Help 页清单）

以下是 Google Play 金融服务帮助页截至核对日列明的重点条件摘要；这不是当地法律的完整清单，监管机构要求会变化。

| 市场 | Google Play 要求摘要 |
| --- | --- |
| 美国 | 个人贷款 APR <36%；最高 APR 按 TILA 计算并披露。 |
| 印度 | 具备 RBI 相关许可，并列入 Reserve Bank of India 的 “DLAs deployed by Regulated Entities” 名单。2025-10-30 起新上架应用须先在名单内；既有上架应用须在 2026-01-28 前列入，日期已过。贷款撮合应用须如实申报，并在商店说明中显著披露所有合作 NBFC/银行名称。RBI 另说明该名录数据由受监管实体直接提交并随其报告新增/删除而更新；名录登记与 Play 明确要求的有效许可是两项检查，不能只凭名录条目替代牌照核验。 |
| 印度尼西亚 | 适用 OJK 互联网借贷规则的业务提交有效许可。 |
| 菲律宾 | 在线贷款公司需 SEC 注册号和 Certificate of Authority；商店说明披露公司/商业名称、注册号及许可；贷款型众筹交易须经 SEC 注册的众筹中介。 |
| 尼日利亚 | Digital Money Lenders 按 FCCPC 规定完成框架并提交可核验批准文件；贷款聚合方提供相关证明及每个合作 DML 联系方式。 |
| 肯尼亚 | Digital Credit Provider 取得 CBK 许可；撮合方提交合作方许可。Play 当前仅接受 CBK 官方目录中实体的申报/牌照。 |
| 巴基斯坦 | 提交 SECP 对放贷/撮合数字贷款的批准；每家 NBFC 仅可发布一个 Digital Lending App，违规可能导致开发者及关联账号终止。短期贷款原则上不允许，有限例外以当地法律明确规定为前提。 |
| 泰国 | 利率达到 15% 或以上的个人贷款需 BoT/MoF 相关许可和证明。所有个人贷款应用的商店资料须显示贷款服务方、开发者法定主体、最高利率和全部费用；低于 15% 的还要写明 “This is a non-regulated loan provider under the BoT/FPO”。现有应用的 2026-03-04 合规期限已过。 |

印度的 Play 专页还要求核实 RBI DLA 名单；实际牌照、市场可用性和当前监管登记必须在发行前向监管机构及 Play Console 双重核对。

## 加密资产、其他金融功能和开发者账号

金融声明还覆盖数字钱包、转账、BNPL、加密钱包/交易所、NFT、股票交易、众筹、保险等。金融服务政策禁止二元期权交易。加密交易与软件钱包另受 Blockchain-based Content/加密交易所规则约束；设备端挖矿不允许，远程管理挖矿可按相应规则评估；代币化数字资产销售/奖励需申报。它们不是贷款政策的附属豁免。国家牌照表、NFT 游戏规则及相关子孙页面已在[加密资产与 NFT 专题](../crypto-assets-and-nfts/crypto-assets-and-nfts.zh-CN.md)独立整理。真钱预测市场另有 Google Play 限时试点，须与普通金融声明、真钱赌博路线区分；试点资格、美国牌照范围、组织账号、18+、AO/IARC、责任使用和已过期的 2026-06-01 既有应用期限见[预测市场试点专题](../prediction-market-pilot/prediction-market-pilot.zh-CN.md)。

Play Console 要求将金融服务列为应使用 Organization 类型开发者账号的业务之一；另须核对账号法律主体、公开开发者资料和监管牌照主体之间的一致性，参见Play Console 要求（快照：`../play-console-requirements.md`，未导入本仓库）。

## 子链接与政策关系

| 来源页 | 目标页 | 关系与核对状态 |
| --- | --- | --- |
| 金融功能声明操作帮助（本专题补充资料；并非 `answer/9876821` 正文 URL） | [Financial features declaration Help](https://support.google.com/googleplay/android-developer/answer/13849271?hl=en) | 帮助正文于 2026-10-22 完整打开：所有已发布应用（包括封闭/开放测试、生产及通过 Play 更新的预装应用）都要申报；无金融功能也须选择对应项。个人贷款功能还须说明贷款方与业务关系，适用市场上传有效许可。2023-08-31 与后续 2024-01-15 过渡期限均已过；当前任务是保持准确申报。 |
| Financial features declaration Help | [System services](https://support.google.com/googleplay/android-developer/answer/12085265?hl=en)、[App content](https://play.google.com/console/app/app-content/summary)、[Financial features form](https://play.google.com/console/) | 已读 System services：仅预装/捆绑且支撑系统核心功能的软件，OEM/芯片厂商/运营商须通过 Partner Center 核实资格。表单、Partner Center、私有应用例外和具体应用状态须登录；公开页面不能证明某账号已提交或获批。 |
| Financial Services policy 正文的旧权限链接 | [原始目标](https://support.google.com/googleplay/android-developer/answer/9888170) → [现行 Sensitive permissions and APIs](https://support.google.com/googleplay/android-developer/answer/16558241?hl=en) | 已核实旧入口重定向到合并政策。金融贷款专项禁止清单与通用权限政策叠加，见上方逐项列表；短信/通话权限另见本库 [SMS/Call Log](../sms-call-log/sms-call-log.zh-CN.md)。 |
| 印度贷款专项 | [Personal Loans in India](https://support.google.com/googleplay/android-developer/answer/16604194?hl=en)、[Reserve Bank of India](https://www.rbi.org.in/)、[RBI DLA 名单入口](https://data.rbi.org.in/BOE/OpenDocument/opendoc/custom.jsp?iDocID=ARfEgy.WNSVIvFfvSIVmBCw&sIDType=CUID)、[RBI 目录说明（2024-08-08）](https://www.rbi.org.in/scripts/BS_PressReleaseDisplay.aspx?prid=58449) | Play 专页于 2026-10-23 完整重开：新应用自 2025-10-30 起须列入 RBI 名单；既有应用须于 2026-01-28 前列入（期限已过）；撮合方须准确申报并披露合作 NBFC/银行。RBI 2024 公告说明目录数据由受监管实体直接报送、RBI 不介入该数据提交，并随实体报告新增/删除而更新。首页可见 Citizen’s Corner 的动态目录入口；本次重开后的目录仍跳到带令牌交互页且没有可读行。Google Play 另行要求有效 RBI 许可，因此目录存在记录不能替代许可核验。 |
| 禁止药品示例清单 | [Prohibited pharmaceuticals and supplements](https://support.google.com/googleplay/android-developer/answer/9217430?hl=en) | 2026-10-22 经健康政策直链打开全文；动态目录按未批准药品/补充剂、减重、麻黄和合成代谢类固醇相关示例分组。长名单未复制；发布前应回查在线清单。详见[健康应用专题](../health-apps-and-health-connect/health-apps-and-health-connect.zh-CN.md)。 |
| 美国计算依据 | [Truth in Lending Act, Regulation Z](https://www.ecfr.gov/current/title-12/chapter-X/part-1026?toc=1) | 已打开 eCFR 官方法规入口；具体 APR 计算需结合现行法规和贷款产品结构由法律/合规人员核验。 |
| 2025-04-10 公告 | [Policy announcement: April 10, 2025](https://support.google.com/googleplay/android-developer/answer/15899442?hl=en) | 已读：个人贷款政策纳入信用额度应用；与金融服务页的敏感权限限制对照。 |
| 2025-07-10 公告 | [Policy announcement: July 10, 2025](https://support.google.com/googleplay/android-developer/answer/16296680?hl=en) | 已读：短期贷款有限例外仅可能适用于巴基斯坦且须当地法规明确要求；同公告的加密资产国家要求见独立主题。 |
| 2026-01-28 泰国公告 | [Policy announcement: January 28, 2026](https://support.google.com/googleplay/android-developer/answer/16797260?hl=en)、[Financial Services — Thailand](https://support.google.com/googleplay/android-developer/answer/9876821?hl=en#country-specific-requirements) | 已读：泰国商店资料需披露贷款方、最高利率和全部费用；2026-03-04 既有应用期限已过。 |
| 2026-07-15 EWA 公告 | [Policy announcement: July 15, 2026](https://support.google.com/googleplay/android-developer/answer/17134731?hl=en)、[Personal Loans/EWA](https://support.google.com/googleplay/android-developer/answer/9876821?hl=en#earned-wage-access) | 已读：将 EWA 透明度和隐私保护与其他金融服务要求对齐；公告说明属于澄清，执行标准不因此改变。 |
| 加密资产相邻分支 | [Cryptocurrency Exchanges and Software Wallets](https://support.google.com/googleplay/android-developer/answer/16329703?hl=en)、[Blockchain-based Content](https://support.google.com/googleplay/android-developer/answer/13607354?hl=en) | 已读并扩展为[独立加密资产/NFT 专题](../crypto-assets-and-nfts/crypto-assets-and-nfts.zh-CN.md)：收录国家/地区许可、Financial features 申报、商品标识、NFT 游戏与试点子页。国家法规和指定国家分发帮助页仍需分别核验。 |

### Financial Services 正文直链及印度子页

2026-10-23 重新打开现行 [Financial Services policy](https://support.google.com/googleplay/android-developer/answer/9876821?hl=en)：正文除了金融功能申报入口，还直链到受限权限政策、TILA 法规及印度专项贷款页。以下按正文、同页反馈控件和 Help Center 导航分层登记；登录表单和侧栏不等同于正文政策要求。

| 来源与目标 | 关系 | 访问/覆盖状态 |
| --- | --- | --- |
| Financial Services 正文 → [Financial features Console 表单](https://play.google.com/console/app/app-content/financial-features) | 所有含金融功能的应用须完成声明；具体应用字段和提交状态只能在开发者账号内核对。 | 页面跳转到需登录的 Console 路由；未推断任何账号状态。 |
| Financial Services 正文 → [权限与 API 政策的原始链接](https://support.google.com/googleplay/android-developer/answer/9888170) → [现行合并政策](https://support.google.com/googleplay/android-developer/answer/16558241) | 贷款/EWA 的专项禁用权限与通用敏感权限要求叠加适用。 | 原始旧链接已核实重定向到现行合并页；现行页已打开并在[敏感权限专题](../sensitive-permissions/sensitive-permissions.zh-CN.md)总结。 |
| Financial Services 正文 → [TILA / Regulation Z](https://www.ecfr.gov/current/title-12/chapter-X/part-1026?toc=1) | 美国 APR 计算引用法规文本；需要按贷款结构和现行法规核算。 | eCFR 官方法规入口已打开；不把法律条文重复改写成 Play 专项政策。 |
| Financial Services 正文 → [Personal Loans in India](https://support.google.com/googleplay/android-developer/answer/16604194?hl=en) | 印度个人贷款在全球金融服务要求外，还须有 RBI 许可并列入公开 DLA 名单。 | 全文已重新打开；新应用日期和既有应用期限已按当前页复核，期限分别为 2025-10-30 和 2026-01-28，均已过去。 |
| Financial Services 正文 → [2-minute policy survey](https://google.qualtrics.com/jfe/form/SV_9YPSYrwjw03d7cG/?Source=9876821) | 收集政策页面反馈，与资格或审核无关。 | 外部问卷重定向至需 JavaScript 的空页面；不将其作为政策来源。 |
| Financial Services 正文/印度专项页 → [Financial declaration Console route](https://play.google.com/console/app/app-content/finance-declaration) | 印度贷款方/撮合方须准确填写金融声明。 | 跳转到账号登录；表单内容和具体申报状态公开不可见。 |

印度专项页的正文链接及可达孙链接：

| 来源与目标 | 关系 | 访问/覆盖状态 |
| --- | --- | --- |
| [Personal Loans in India](https://support.google.com/googleplay/android-developer/answer/16604194?hl=en) → [global Financial Services policy](https://support.google.com/googleplay/android-developer/answer/9876821?hl=en) | 明确印度要求叠加于全球贷款政策。 | 已打开并交叉核对；全球政策的完整国家表和权限清单见本页上文。 |
| [Personal Loans in India](https://support.google.com/googleplay/android-developer/answer/16604194?hl=en) → [Reserve Bank of India（来源原始入口）](https://website.rbi.org.in/en/web/rbi) → [DLA deployed by Regulated Entities directory](https://data.rbi.org.in/BOE/OpenDocument/opendoc/custom.jsp?iDocID=ARfEgy.WNSVIvFfvSIVmBCw&sIDType=CUID) | RBI 主页 Citizen’s Corner 提供动态 DLA 名单入口，用于核验受监管实体部署的贷款应用。 | RBI 主页原始地址重定向至 `www.rbi.org.in`，2026-10-23 重开仍可见目录入口；DLA 名单再次跳到带临时令牌的交互式 `openDocument` 页面，仅返回空壳，无可读名单行。RBI 2024 公告说明目录依据受监管实体报送并随其报告更新；Play 同时要求有效许可，故不能以目录登记替代牌照核验。 |
| RBI 官网公告（与 Play 子链的关系：监管背景，不是 Play 政策正文直链）→ [Public Repository of Digital Lending Apps](https://www.rbi.org.in/scripts/BS_PressReleaseDisplay.aspx?prid=58449) | 解释 RBI DLA 公开目录的数据来源与更新机制。 | RBI 于 2024-08-08 表示，受监管实体直接提交目录数据，RBI 不介入该提交；新增/删除信息随实体报告更新。该说明用于界定目录证据的含义，不证明某个应用的实际条目或牌照状态。 |
| RBI 官网公告（2025-05-08，监管背景，不是 Play 政策正文直链）→ [Digital Lending Directions, 2025 发布说明](https://www.rbi.org.in/Scripts/BS_PressReleaseDisplay.aspx?prid=60403) | 说明 DLA 公开目录的上线和初始报送安排。 | RBI 说明受监管实体通过 CIMS 报送，初始数据期限为 2025-06-15，公开名录预计不迟于 2025-07-01 上线；数据按提交原样公开、不由 RBI 另行验证，并随机构新增/移除应用的报告自动更新。上述日期已过。该发布说明不是 Google Play 政策条文。 |
| RBI《Digital Lending Directions, 2025》→ [第 17 段及同页 Annex I](https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=12848&Mode=0) | 规定受监管实体向 CIMS 报送其自有及 LSP 运营的 DLA、更新名录并核验数据的职责；Annex I 列出应用名称、所有者/LSP、商店/网站链接、申诉联系人等字段。 | 正文及 Annex I 已打开。第 17 段自 2025-06-15 生效；指定合规负责人须认证数据准确及合规，RBI 自动发布且不验证/背书名录条目；应用纳入名录不构成注册、授权或认可。这里只摘要与 DLA 目录有关的段落，不把 RBI 全部数字贷款监管要求并入 Play 政策。 |
| [Personal Loans in India](https://support.google.com/googleplay/android-developer/answer/16604194?hl=en) → [Financial declaration Console route](https://play.google.com/console/app/app-content/finance-declaration) | 贷款撮合方需准确申报角色，并在商店说明显著列出所有合作 NBFC/银行名称。 | Console 路由要求登录；无法核验具体应用是否提交或获批。 |

印度专项页的页脚社区链接本次返回 Cache miss，Contact us 跳转账号专属支持。另有 10 项 Help Center 侧栏和一个独立的 AI 声明链接；本轮已逐一打开下列导航目标，并与现有双语专题/来源状态交叉登记。它们是帮助导航，不自动构成印度贷款新增义务：

| 侧栏/导航目标 | 与本专题的关系与后续覆盖 |
| --- | --- |
| [Play Console Help 首页](https://support.google.com/googleplay/android-developer?hl=en) | 通用 Help 目录，含大量账号、发布和政策帮助入口；不是金融政策页，本轮未递归其全部目录链接。 |
| [Manage policy violations](https://support.google.com/googleplay/android-developer/topic/3453554?hl=en&ref_topic=2364761) | 违规处理目录的 11 个目标已逐项尝试；详见[执行与申诉专题](../enforcement-and-appeals/enforcement-and-appeals.zh-CN.md)，联系流程仍有账号门槛。 |
| [App management](https://support.google.com/googleplay/android-developer/topic/12796572?hl=en&ref_topic=2364761) | 通用应用管理 Help 目录；其文章属于发布/管理支持，不是金融贷款政策，已有链接状态保留在来源台账。 |
| [Use of app permissions and APIs](https://support.google.com/googleplay/android-developer/topic/12798286?hl=en&ref_topic=2364761) | 12 个权限帮助目标已打开或与现有文章核对；可见目录详见[敏感权限专题](../sensitive-permissions/sensitive-permissions.zh-CN.md)，更深 API/技术后代仍部分覆盖。 |
| [Policy education and app requirements](https://support.google.com/googleplay/android-developer/topic/12798386?hl=en&ref_topic=2364761) | 31 个帮助文章及一个预览入口已尝试；金融声明、国家分发、Data safety 等现有主题已交叉链接，目录不是单一政策条款，后代状态各异。 |
| [Google Play programs](https://support.google.com/googleplay/android-developer/topic/12796472?hl=en&ref_topic=2364761) | 目录列出五个项目：[Online Crane Games](https://support.google.com/googleplay/android-developer/answer/12002615?hl=en&ref_topic=12796472)（正文现可读；日本试点于 2023-07-11 结束，但全球分发仍须提交并获接受的[独立声明表](https://support.google.com/googleplay/android-developer/contact/ocgform)；年龄核验、消费限额、仅娱乐性付款、奖品限值/禁转售、公平和广告要求见[真钱赌博专题](../real-money-gambling/real-money-gambling.zh-CN.md)）；[真钱游戏试点概览](https://support.google.com/googleplay/android-developer/answer/12918670?hl=en&ref_topic=12796472)（生效日 2026-06-04，现称没有活跃试点；印度 DFS/Rummy 过渡期于 2026-01-22 结束，墨西哥 DFS 试点于 2026-06-04 结束；正文另链当前赌博政策、OCG 与[地区许可表](https://support.google.com/googleplay/android-developer/answer/12256011?hl=en)，墨西哥表列线上赌场、体育博彩和彩票但仍须满足牌照及当地法律）；[Strike Removal](https://support.google.com/googleplay/android-developer/answer/12186827?hl=en&ref_topic=12796472)、[Prediction Markets pilot](https://support.google.com/googleplay/android-developer/answer/16902027?hl=en&ref_topic=12796472)、[Apps Experience / Level Up](https://support.google.com/googleplay/android-developer/answer/18018581?hl=en&ref_topic=12796472)。本次重试解决 OCG 和试点概览此前的抓取错误；五项目标的审计状态均有记录。它们是独立计划/运营入口，不是贷款政策条款。 |
| [Data safety and prominent disclosure](https://support.google.com/googleplay/android-developer/topic/12797379?hl=en&ref_topic=2364761) | 目录的 3 个目标已分别归入 Data safety、Families 与 User Data 专题；显著披露和同意详见[用户数据专题](../user-data/user-data.zh-CN.md)。 |
| [Google Play Policy Insights in Android Studio](https://support.google.com/googleplay/android-developer/answer/16297427?hl=en&ref_topic=2364761) | Help 页自称只覆盖部分政策、不作审核决定；列举的初始权限/Ads 范围和版本说明并非全政策目录。可作编码期提示，不能替代完整政策或 Play 审核。 |
| [Understanding Your Tax Responsibilities on Google Play](https://support.google.com/googleplay/android-developer/answer/16408159?hl=en&ref_topic=2364761) → [Tax rates and VAT by country](https://support.google.com/googleplay/android-developer/answer/138000?hl=en&ref_topic=15819563) | 属于交易税务/产品税分类运营帮助，不是金融贷款审批条款。税务页有动态国家矩阵和大量 Console/计费链接；本轮读取到部分国家章节，未逐市场复录，需按销售地、开发者所在地和计费路径复核。 |
| [Personal Loans in India](https://support.google.com/googleplay/android-developer/answer/16604194?hl=en&ref_topic=2364761) | 即本专题的印度专项子页；正文直链和 RBI 孙链状态见上表。 |
| 单独链接：[Declaring AI-generated content in Play Console](https://support.google.com/googleplay/android-developer/answer/17262077?hl=en&ref_topic=2364761) | 只针对商店资料/促销等提交资产的 AI 标签申报，不是贷款资质规则；完整 AI 内容政策见[AI 生成内容专题](../ai-generated-content/ai-generated-content.zh-CN.md)。 |

RBI 监管文件和本地法律属于外部国家法规范围，需另按市场核验；Play Help 页面并未将它们全部列为直接链接。

## 发布前核对清单

1. 按应用的实际收付款、授信、建议、交易、钱包、保险和奖励功能逐项填写 Financial features declaration；不要只按应用名称或商店类别判断。
2. 个人贷款/EWA/贷款撮合应用确认 Finance 类别、所有合作方、牌照文件、商店条款/费用披露和隐私政策。
3. 在 Manifest、合并 Manifest、SDK、所有构建变体与发行轨道中检查并移除不允许的贷款敏感权限；另检查 SDK/服务端的数据收集。
4. 按每个目标国家建许可和披露矩阵；核对国家监管机构、名单、牌照主体、到期日和 Play Console 所需证明。
5. 将金融声明、隐私政策、Data safety、商店说明、App content、目标市场和实际上线版本交叉核对。
6. 登录 Console 确认当前声明、审核意见和政策状态；公开 Help 页面不能证明具体应用获批或满足本地法律。

本页为 2026-10-23 官方政策摘要快照。国家表格、监管规定和 Play Console 表单会变更；分发前应逐市场复核官方现行页面并取得适当法律/合规意见。
