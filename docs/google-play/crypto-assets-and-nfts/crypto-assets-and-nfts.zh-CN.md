---
id: google-play.crypto-assets-and-nfts
platform: google-play
language: zh-CN
authority: normative
status: current
kb_checked_at: 2026-10-22
review_due: 2027-01-22
regions: [global]
topics: [crypto-assets, nft, blockchain, software-wallet, financial-features]
snapshot_id: play.crypto-assets-and-nfts
snapshot_package: "GooglePlay-KnowledgeBase-2026-10-24-review.zip"
coverage_status: "detailed-summary"
source_url_country_requirements: "https://support.google.com/googleplay/android-developer/answer/16329703?hl=en"
source_url_blockchain_policy: "https://support.google.com/googleplay/android-developer/answer/13607354?hl=en"
source_url_financial_declaration: "https://support.google.com/googleplay/android-developer/answer/13849271?hl=en"
source_url_gambling: "https://support.google.com/googleplay/android-developer/answer/9877032?hl=en"
source_url_gambling_pilots: "https://support.google.com/googleplay/android-developer/answer/12918670?hl=en"
source_url_one_time_products: "https://support.google.com/googleplay/android-developer/answer/16430488?hl=en"
source_url_metadata: "https://support.google.com/googleplay/android-developer/answer/9898842?hl=en"
source_url_country_distribution: "https://support.google.com/googleplay/android-developer/answer/7550024?hl=en"
source_url_country_requirements_zh: "https://support.google.com/googleplay/android-developer/answer/16329703?hl=zh-CN"
source_url_country_distribution_zh: "https://support.google.com/googleplay/android-developer/answer/7550024?hl=zh-CN"
effective_date: "current rules; Liechtenstein, Iceland, and Norway “Starting July 2026” has passed; no 2027-01-27 on this page"
---

# 加密资产交易所、软件钱包与 NFT

> **导入说明（Google batch 6）。** 正文来自已经分开的 2026-10-24 Google Play 知识库快照（`play.crypto-assets-and-nfts`，核对日 2026-10-22）的改写摘要，不是官方页面的逐字副本。英文官方页面是效力来源。`kb_checked_at` 是快照源文件记录的核对日；本次导入没有重新打开线上官方页面。文中“本知识库”“本库”“本地专题”等说法描述的是该快照库的覆盖范围，不是本仓库已经导入的页面。指向本仓库没有收录的专题、链接图、台账或 CSV 的相对链接改为文字提及。指向 Google batch 1–5 或本批九个专题的相对链接改为本仓库文件。核对日 2026-10-22。快照重新打开了英文交易所/软件钱包地区页和英文按国家分发指南。对应的简体中文 Help URL 无法读取。中文摘要依据这些英文正文，不是对中文页面的逐行复核。该访问失败不是政策变更。中文 YAML 仍列出相关政策的 `hl=zh-CN` 地址；链接表记录为已打开的正文是英文。来源把列支敦士登、冰岛和挪威标为“Starting July 2026”起纳入。该日期在核对时已经过去。真钱游戏试点页的生效日 2026-06-04 已经过去，且该页写明当时没有活跃试点。这些日期不是 2027-01-27 预告。本页没有记录 2027-01-27。交易所与钱包资格、金融功能申报和 Blockchain-based Content 是各自独立的 `normative` 要求。非托管钱包不在特殊交易所/软件钱包政策范围内，也不因此豁免其他规则。国家表列出的是 Play 写明的资质，不是当地法律的完整表述。测试轨道的国家目标是 operational 说明，不替代牌照。**

**核对日期：2026-10-22。** Google Play 将加密货币交易/软件钱包的地区资格、金融功能申报、区块链代币化内容和 NFT 游戏分别规定。国家表格是 Play 当前列出的申报/资质条件摘要，不等于所有适用法律的完整清单，也不证明某开发者或应用已获许可。

## 先区分产品类型和义务

| 产品/功能 | 主要规则入口 | 关键动作 |
| --- | --- | --- |
| 加密货币交易所 | Cryptocurrency Exchanges and Software Wallets；Blockchain-based Content | Financial features 申报、逐目标市场许可/登记、必要的地区表单和本地法律核验 |
| 托管型软件钱包 | 同上 | 申报钱包功能；核实目标地区要求和 Play Console 地区表单 |
| 非托管钱包 | 特殊交易所/软件钱包政策明确排除 | 该排除不自动豁免金融功能申报、Blockchain-based Content、其他 Play 政策或当地法律 |
| NFT/代币化数字资产销售、交易或奖励 | Financial features declaration；Blockchain-based Content | 申报 NFT/代币化资产功能；符合适用的游戏、真实货币赌博和元数据规则 |
| 设备端挖矿 | Blockchain-based Content | Play 不允许应用在设备上挖矿；远程管理挖矿的应用可允许，仍须遵守其他适用规则 |

Google 将加密货币的购买、持有或兑换置于受监管地区的认证服务框架内。Play Console 中选择一个国家/地区，表示主动在当地提供和展示应用。未列入下表的地区并非自动豁免：开发者仍需遵守当地法规，Google 也可能要求补充合规证明。

**来源核验：** 本轮重新打开了英文[交易所/软件钱包地区要求页](https://support.google.com/googleplay/android-developer/answer/16329703?hl=en)及其直接链接的[按国家/地区分发应用指南](https://support.google.com/googleplay/android-developer/answer/7550024)。简体中文的两个对应 Help URL 本轮无法由抓取器读取；中文摘要按英文正文整理，不据此声称逐段核实了中文页面。

## Google Play 当前列出的国家/地区资质

下表按官方“Cryptocurrency Exchanges and Software Wallets”帮助页归纳。除香港和泰国行外，公开抓取文本没有把交易所与软件钱包各自的单元格内容清楚拆开；因此此处保留资质原意，不据此推断某类钱包免牌照。发布前应在官方表格及 Play Console 地区表单核对具体适用类型。

| 国家/地区 | Google Play 页面列出的许可/登记 |
| --- | --- |
| 巴林 | 巴林中央银行（CBB）颁发的 Crypto-Asset Services 许可。 |
| 加拿大 | 在 FINTRAC（CANAFE）登记为货币服务企业（MSB）。 |
| 中国香港 | **交易所：**选择加入相关许可制度，并取得香港证监会（SFC）第 1 类（证券交易）及第 7 类（提供自动化交易服务）牌照。**软件钱包：**页面注明不要求。 |
| 印度尼西亚 | 取得印尼金融服务管理局（OJK）颁发的 Digital Financial Asset Trading Provider 许可。 |
| 以色列 | 由 CMISA 许可为金融服务提供者，或由以色列银行许可为银行公司。 |
| 日本 | 在日本金融厅（FSA）正式登记为加密资产交易服务提供商。 |
| 菲律宾 | 取得菲律宾中央银行（BSP）颁发的 Money Services Business Certificate of Authority。 |
| 南非 | 在金融行业行为监管局（FSCA）登记。 |
| 韩国 | 向韩国金融情报机构（KoFIU）专员成功提交虚拟资产服务提供商（VASP）报告。 |
| 泰国 | **交易所：**取得泰国证券交易委员会（SEC）颁发的相关 Digital Asset Business 许可。**软件钱包：**页面注明不要求。 |
| 阿联酋 | 持有下列之一的许可：FSRA、VARA 或 DFSA。 |
| 英国 | 在金融行为监管局（FCA）登记。 |
| 美国 | 在 FinCEN 登记为 MSB 且在州级登记为 money transmitter；或属于联邦/州特许银行实体。 |
| 欧盟成员国，以及页面注明自 2026 年 7 月起的列支敦士登、冰岛、挪威 | 由相关国家主管机关根据 MiCA 授权为加密资产服务提供商（CASP）。其他国家/地区层级限制和要求仍适用。 |

欧盟成员国名单：奥地利、比利时、保加利亚、克罗地亚、塞浦路斯、捷克、丹麦、爱沙尼亚、芬兰、法国、德国、希腊、匈牙利、爱尔兰、意大利、拉脱维亚、立陶宛、卢森堡、马耳他、荷兰、波兰、葡萄牙、罗马尼亚、斯洛伐克、斯洛文尼亚、西班牙、瑞典。官方页面将列支敦士登、冰岛、挪威标为“自 2026 年 7 月起”；截至本页核对日该日期已过，但页面仍使用该表述，应以当前 Console 表单和主管机关状态确认。

官方页面还特别说明：自 2026 年 7 月起，获相关国家主管机关 MiCA CASP 授权、位于列支敦士登/冰岛/挪威的开发者，也可以面向欧盟成员国投放。MiCA 之外的国家和地区层级要求仍适用。

### 申报和国家投放操作

1. 在 Play Console 的 **App content → Financial features** 中按应用实际功能申报加密货币钱包、交易所和/或 NFT/代币化数字资产销售、交易、奖励。金融功能申报帮助页要求所有已发布应用完成申报，包括测试轨道；没有金融功能的应用也须声明无此类功能。历史申报期限已过，不能据旧帮助页的 2023 年日期推断目前无需申报。
2. 在国家/地区列表中，只选择确有资格并准备提供服务的市场。对帮助页列出的市场，按提示填写地区表单；缺少要求的许可或登记时，从目标地区中移除该市场。
3. 对未列市场也做独立许可审查；“不在列表”不代表无需许可。留存牌照主体、开发者账号主体、服务运营主体、合作方及应用实际功能之间的对应材料。
4. 每次政策或市场变更后重新核对许可证有效期、地区可用性、Console 申报和商店资料；Google 可要求补充文件。

### 国家可用性与测试轨道

[按国家/地区分发应用](https://support.google.com/googleplay/android-developer/answer/7550024)是地区要求页直接链接的操作指南。它区分生产轨道的 **app availability** 与开放/封闭测试轨道的 **country targeting**：选择某国为生产可用后，会作用于当前和未来的生产版本；测试轨道默认跟随生产国家，但满足条件时可解除同步并单独设置。内部测试不适用国家目标限制，测试者可从任何地点安装。国家目标按用户的 **Google Play 账号国家**判定，不按用户当下 GPS 所在位置判定。

新增付费应用发行国家时，Play 会自动添加当地价格；订阅仍需检查并设置对应国家/地区价格。该操作指南不会替代加密服务的牌照、登记、当地法律或 Play 地区表单资格判断：目标国家仍须满足本专题上表所列规则和相关法律要求。

## 区块链内容、NFT 和游戏化要求

Google Play 将区块链内容定义为由区块链保障的代币化数字资产。只要应用含有这类内容，就须遵守该政策。

- **申报及商品信息：**应用销售或允许用户赚取代币化数字资产时，必须在 Play Console Financial features declaration 中申报；创建 Play 内商品时，商品详情必须表明其代表 Tokenized Digital Asset。商品信息还须遵守通用 Metadata 规则，准确描述实际功能，不得误导。
- **收益宣传：**不得宣传或美化用户通过游戏或交易活动获得潜在收益。不要把价格升值、投资回报或赚钱机会作为游戏进度/奖励保证。
- **挖矿：**禁止应用在用户设备上挖掘加密货币；可以允许远程管理挖矿的应用。
- **NFT 抽取：**真实货币赌博应用集成 NFT 等代币化资产时，须走赌博应用申请并满足许可、地区、年龄等规则。其他不符合赌博应用资格且不在适用试点内的应用，不得用具有货币价值的东西换取“获得价值未知 NFT”的机会。
- **NFT 在游戏中的用途：**用户购买的 NFT 应在游戏中被消耗或使用，以改善体验或帮助推进游戏；不得将 NFT 用作下注/质押，以换取赢得现实货币价值奖品（包括其他 NFT）的机会。
- **政策列举的违规例子：**出售未披露具体内容和价值的 NFT 盲盒/组合；付费游玩的社交赌场（例如老虎机）向玩家奖励 NFT。

NFT 玩法须与 [Real-Money Gambling, Games, and Contests](https://support.google.com/googleplay/android-developer/answer/9877032?hl=en) 一起判断：获准的赌博应用须提交申请、持有每个目标地区/游戏类型所需的有效牌照、阻止未成年人和无许可地区使用，并满足免费安装、不得使用 Play Billing、AO/IARC 对应分级及负责任赌博披露等条件；政策列举在线赌场、体育博彩、赛马、彩票和 DFS 等类型。其他未获准应用通常不得以真钱或用真钱购买的道具下注以赢得现实价值奖品，除非确属政策允许的项目/试点。该帮助页还覆盖赌博广告、DFS 和游戏化忠诚奖励；本专题只提炼与 NFT 抽取/奖励交叉的部分，其他机制应读完整政策。

截至 2026-10-22 打开的赌博试点页面列明“目前没有正在进行的试点”；该状态会变更。页面记录：日本在线抓娃娃试点 2023-07-11 结束；印度 DFS/Rummy 试点 2023-09-28 结束，试点宽限期于 2026-01-22 结束，此前试点应用如要继续留在印度 Play，须移除真钱功能并符合赌博政策；墨西哥 DFS 试点于 2026-06-04 结束，此后真钱游戏应用须符合赌博政策且属于墨西哥允许的游戏类型。不要把“可能有试点”视为可自行上线的例外；应查当前试点、地区、条款及申请资格。

## 逐页链接与关系

下表优先收录上述政策正文直接链接，以及为理解这些义务而继续打开的关键子页。通用导航、反馈和图片链接不作为政策分支；页面本身的导航目录也不等于政策正文要求。

| 父页面 | 子页面/后代 | 内容与政策关系 / 核对状态 |
| --- | --- | --- |
| [Cryptocurrency Exchanges and Software Wallets country requirements](https://support.google.com/googleplay/android-developer/answer/16329703?hl=en) 正文（3 次链接出现） | [Blockchain-based Content policy](https://support.google.com/googleplay/android-developer/answer/13607354?hl=en)（2 次）及[按国家/地区分发应用](https://support.google.com/googleplay/android-developer/answer/7550024)（1 次） | 英文正文完整打开；3 个正文链接出现去重为 2 个目标。Blockchain 页面已打开并有本地摘要；国家分发指南也已打开。Help 侧栏另列 32 项（含当前页），同级导航与正文目标分开登记。`zh-CN` URL 本轮抓取失败。 |
| [按国家/地区分发应用](https://support.google.com/googleplay/android-developer/answer/7550024) | [开放/封闭/内部测试指南](https://support.google.com/googleplay/android-developer/answer/9845334)、[价格设置](https://support.google.com/googleplay/android-developer/answer/6334373)、[订阅管理](https://support.google.com/googleplay/android-developer/answer/140504)、[分阶段发布](https://support.google.com/googleplay/android-developer/answer/6346149)、[发布准备](https://support.google.com/googleplay/android-developer/answer/9859348) | 英文正文完整打开。正文 9 次链接出现、8 个唯一目标：上述 5 个公开帮助页均已打开或由现行专题核验；另外 3 个 Play Console 轨道入口要求登录。另有 13 项 Help 侧栏（含当前页），不与正文链接混算；这些目标的更深后代仍部分未展开。 |
| 同上：测试轨道目标国家 | Play 账号国家、生产可用国家与测试轨道国家设置 | 生产国家选择影响当前/未来生产版本；测试轨道默认同步生产国家，可在满足条件时解除同步；内部测试不受国家目标限制。目标按用户 Play 账号注册国家判断，而非当前物理位置。 |
| 同上：商品价格与订阅 | [价格设置](https://support.google.com/googleplay/android-developer/answer/6334373) · [订阅管理](https://support.google.com/googleplay/android-developer/answer/140504) | 新增付费应用国家会自动生成当地价格；订阅须另核对/设置当地价格。国家投放操作不授予加密业务的许可资格。 |
| Blockchain-based Content | [Country/region crypto requirements](https://support.google.com/googleplay/android-developer/answer/16329703?hl=en) | 已打开。解释表内市场的许可/登记材料、Financial features 申报和无资质时移除目标市场。 |
| Blockchain-based Content | Play Console Financial features form（正文引用的申报入口）；[Financial features declaration Help](https://support.google.com/googleplay/android-developer/answer/13849271?hl=en) | 政策正文要求在 App Content 填写 Console 表单；另行打开的 Help 说明作为相关背景页，而非误记为正文子链接。Help 页说明所有已发布应用须申报，加密货币钱包、交易所、NFT 销售/交易/奖励均在类别中；表单需登录，旧 2023 期限已过。 |
| Financial features declaration | [Financial Services policy](https://support.google.com/googleplay/android-developer/answer/9876821?hl=en) | 已在[金融服务专题](../financial-services-and-loans/financial-services-and-loans.zh-CN.md)打开并总结。它把金融服务定义延伸至资金和加密货币的管理/投资，并要求符合各目标地法规；二元期权交易不允许。 |
| Blockchain-based Content | [Create an in-app product / one-time product](https://support.google.com/googleplay/android-developer/answer/1153481?hl=en)、[Overview of one-time products](https://support.google.com/googleplay/android-developer/answer/16430488?hl=en) | 已打开。商品详情是填写 Tokenized Digital Asset 标识的 Play 商品入口；新目录模型区分商品、购买选项与优惠，并含地区可用性。产品模型说明不替代代币资产政策，也不意味着任何 NFT 商品都获准。部分功能标为 Early Access。 |
| One-time products | [Metadata policy](https://support.google.com/googleplay/android-developer/answer/9898842?hl=en) | 已打开。标题、图标、描述等需准确、相关、无误导并适合受众；Blockchain-based Content 另要求商品详情说明其为代币化数字资产。 |
| Blockchain-based Content | [Real-Money Gambling, Games, and Contests](https://support.google.com/googleplay/android-developer/answer/9877032?hl=en) | 已打开。符合条件的应用须申请、按每个国家及游戏类型持有效牌照、限制未成年人/未许可地区、免费安装、不使用 Play Billing、具备 AO/IARC 对应分级和负责任赌博信息。其他应用不能协助以现金/有价道具下注赢取现实价值奖品；政策也含 DFS、广告和忠诚奖励规则。 |
| Real-Money Gambling policy | [Gambling application form](https://support.google.com/googleplay/android-developer/contact/gambling) | 表单链接已打开；需由开发者提交申请和许可材料。公开浏览不能确认具体账号/应用获批。 |
| Real-Money Gambling policy | [Real-money gaming pilots](https://support.google.com/googleplay/android-developer/answer/12918670?hl=en) | 已打开；页面生效日为 2026-06-04，核对时写明当前无活跃试点。印度 DFS/Rummy 宽限期于 2026-01-22 结束；墨西哥 DFS 试点于 2026-06-04 结束。 |
| 试点页 | [Online Crane Games](https://support.google.com/googleplay/android-developer/answer/12002615?hl=en) | 已打开；日本试点已于 2023-07-11 结束。现行页面要求提交声明表单；新应用需等声明获接受后才可能上架，旧应用应核对设置，Google 说明约五个工作日内通知结果。该路径不是 NFT 例外。 |
| Financial Services / Developer account | [Play Console 要求](../play-console-requirements/play-console-requirements.zh-CN.md) | 本地双语摘要说明金融产品/服务类业务与组织账号要求；账号资格需按法律主体和实际业务核验。 |

## 发布前核对清单

1. 画清交易所、托管/非托管钱包、NFT 销售/奖励、挖矿管理及游戏玩法边界，并逐项对照申报类别。
2. 按每个目标国家确认牌照、登记、地区表单、发行主体和可服务范围；未达到门槛的市场不要加入投放。
3. 检查商店商品名称/描述、商品详情和游戏内抽取玩法：准确标识代币化资产，不宣传投机收益，不隐瞒随机 NFT 的内容或价值。
4. 对下注、质押、付费抽取、现金/有价 NFT 奖励等机制，单独做真实货币赌博与当地法律审查；不要把试点/持牌应用通道外推至普通 NFT 游戏。
5. 检查设备端代码、SDK 和远端服务，确认应用不在用户设备上挖矿；远程管理功能也需如实披露用途并遵守其他政策。
6. 登录 Play Console 核实申报状态、国家表单、审核通知和当前资格；公开网页无法证明账号或应用的实际批准状态。

本页是截至 2026-10-22 的官方政策改写摘要。加密资产牌照、MiCA/各地实施、Console 字段与游戏试点可能变化；按每个发行市场重新核验官方页面及主管机关要求。本页不构成法律意见，也不是逐字转载。
