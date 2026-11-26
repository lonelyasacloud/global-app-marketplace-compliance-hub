---
id: google-play.country-specific-distribution
platform: google-play
language: zh-CN
authority: operational
status: current
kb_checked_at: 2026-10-23
review_due: 2027-01-23
regions: [global]
topics: [country-requirements, distribution, age-signals, licensing, regional-compliance]
snapshot_id: play.country-specific-distribution
snapshot_package: "GooglePlay-KnowledgeBase-2026-10-24-review.zip"
coverage_status: "detailed-summary"
source_url: "https://support.google.com/googleplay/android-developer/answer/6223646?hl=en"
source_url_brazil_eca: "https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/l15211.htm"
source_url_age_signals: "https://developer.android.com/google/play/age-signals/overview"
source_url_eu_geo_blocking: "https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX:32018R0302"
source_url_japan_fsa: "https://www.fsa.go.jp/common/about/pamphlet/2022purika.pdf"
source_url_korea_grac: "https://www.grac.or.kr/english/"
source_url_india_online_gaming_act: "https://www.meity.gov.in/static/uploads/2025/10/8a7f103cefc68ed8aaa2ebc9a2ed7c13.pdf"
source_url_vietnam_game_licensing: "https://giayphep.abei.gov.vn/"
source_url_zh: "https://support.google.com/googleplay/android-developer/answer/6223646?hl=zh-CN"
effective_date: "Help snapshot; India Act commencement is not asserted from Play Help alone; no 2027-01-27"
---

# Google Play 特定国家/地区分发要求

> **导入说明（Google batch 6）。** 正文来自已经分开的 2026-10-24 Google Play 知识库快照（`play.country-specific-distribution`，核对日 2026-10-23）的改写摘要，不是官方页面的逐字副本。英文官方页面是效力来源。`kb_checked_at` 是快照源文件记录的核对日；本次导入没有重新打开线上官方页面。文中“本知识库”“本库”“本地专题”等说法描述的是该快照库的覆盖范围，不是本仓库已经导入的页面。指向本仓库没有收录的专题、链接图、台账或 CSV 的相对链接改为文字提及。指向 Google batch 1–5 或本批九个专题的相对链接改为本仓库文件。核对日 2026-10-23。英文来源地址是 `hl=en`。中文来源地址是 `hl=zh-CN`。快照没有记录该 `hl=zh-CN` Play 帮助路由抓取失败，也没有记录中英文逐行对照。本仓库中文正文是快照的编辑改写。该差距不是政策变更。Play 帮助页写明它不是法律要求的完整清单。所链接的印度《Promotion and Regulation of Online Gaming Act, 2025》正文 §1(3) 写明，法律自中央政府另行公告的日期起施行。本页记录的是 Play 帮助页表述，不把该帮助页当作法律已经施行的证明。韩国 MOGEF 返回缓存未命中，KCC 请求超时，GRAC 指引页被拦截，日本 CAA 链接无法打开，越南 ABEI 主站返回内部错误。这些外部站点限制不是 Play 政策变更。本页没有记录 2027-01-27。本页是 operational 的 Play 帮助，加上 regulatory 引用。某一市场的一行不是全球 Play 许可，也不是完整的当地法律意见。Age Signals 材料是 implementation note。**

**核对日期：2026-10-23。** Google Play 的[特定国家/地区帮助页](https://support.google.com/googleplay/android-developer/answer/6223646?hl=en)明确说明，页面不是发布应用所需法律要求的完整清单，也不能单独用来判断法律或 Play 政策合规。以下是该页当前列出的重点市场快照；国家规则、Console 表单、许可证、费率、年龄工具和执法状态均可能变化。

## 国家/地区要求快照

| 市场 | Google Play 帮助页当前列出的要求 | 主要影响 |
| --- | --- | --- |
| 巴西：商户验证 | 全球商户只要在巴西销售应用或应用内商品，都可能需要提交企业名称、地址、最终受益所有人（持股/投票权超过 25%）、高管、授权代表、地址证明，且可能补交出生日期或照片证件；巴西本地企业另需 CPF/CNPJ。Google 会通过邮件、Play Console 与 Payments 页面提示。 | 这是收款/商户验证，资料不全可能影响付款或账户状态；不要只检查巴西注册企业。 |
| 巴西：Digital ECA、年龄信号和 loot box | Google 帮助页称，面向儿童/青少年或可能被其访问的应用须接收应用商店提供的年龄段；此类游戏不得提供 loot box。Play Age Signals API（beta）在用户或受监督用户家长同意共享时返回年龄段。Google Play 还会对判定为未成年人的用户屏蔽或过滤 18+ 应用/游戏。可能需要重新提交 IARC 问卷以获得更新的 ClassInd 分级，尤其是有 loot box 的游戏。 | 年龄段可用性、同意状态、家庭监督、当地分类和 Play 商店屏蔽要一起评估。Age Signals 不替代开发者自身法律义务，也不得超范围用于营销或画像；详见[儿童安全](../age-restricted-child-safety/age-restricted-child-safety.zh-CN.md)与[内容分级](../content-ratings/content-ratings.zh-CN.md)。 |
| 欧盟：地理封锁 | 分发至欧盟时，不得因用户国籍、居住地或营业地而无正当理由地理封锁。Google 的示例要求服务原则上可在欧盟范围访问，但受其他适用法律限制；以提供受版权保护作品访问为主要服务的情形被列作例外。 | 按销售对象、服务类型、版权内容与法定例外逐市场评估；不能把欧盟规则泛化为所有服务都必须无条件覆盖所有地区。 |
| 日本：交易者信息与金融/游戏规则 | 面向日本消费者提供付费应用或应用内购买，须展示经营者名称、电话及实体地址（特定商业交易法）。2023-08-31 前创建的账号可在 Console 账号详情/开发者页面维护（或在商店详情链接到载有资料的网站）；较新账号信息取自绑定的 Payments profile。还须按适用法律满足《资金结算法》等要求；游戏开发者可能需通知当地财务局，并应考虑未成年人保护。 | 账号建立日期决定资料来源和维护路径；Console 公开信息与实体公司登记应一致。 |
| 韩国：游戏评级、概率型物品、年龄验证和位置服务 | 未适合未满 19 岁者的游戏，须依韩国 GRAC 评级/许可证规则；含模拟赌博的游戏被视为不适合未成年人，分发前须取得 GRAC 评级。付费随机虚拟物品须在购买前、紧邻购买步骤披露概率，并遵守韩国概率型物品披露规则。被 MOGEF 指定为“有害青少年”的内容按韩国法和 Play 的年龄/真实姓名核验流程处理。为基于位置的服务收集韩国用户位置可能须取得 KCC 许可、报告服务/收集/使用/费用信息，并取得用户同意。 | 博彩模拟、概率道具、成熟内容和位置服务分别对应不同审批/申报，不能只看 IARC 年龄标签。 |
| 韩国：开发者联系资料 | 2023-08-31 前创建的账号按 Account Details/Developer page 填资料；较新账号从开发者账号/付款资料流程维护。韩国开发者销售付费应用或应用内商品时，页面列出商业登记号、电商许可证号及签发机构；韩国个人账号另须验证并展示开发者电话。 | 账号创建日期影响路径；企业实体、许可证与 Console 资料须一致。 |
| 以色列：开发者身份验证 | 帐单地址在以色列的开发者须在 Google 指定时间内完成身份核验。收入在滚动六个月超过 50,000 ILS 的个人/组织账号须做增强级 KYC；个人需提供证件，组织需提供注册、授权代表及亲笔签署文件，并安排约 10 分钟 Google Meet 现场身份确认。未按时完成可能导致暂停付款、限制分发/销售。 | 以 Google 的账号邮件/Console 横幅和实际截止时间为准；不能从公开帮助页推导所有账号的统一期限。 |
| 印度：在线游戏 | Google Play 页面称，印度游戏应用须遵守《Promotion and Regulation of Online Gaming Act, 2025》，并禁止分发该法定义的 online money games；页面把 online social games 和 e-sports 列作该禁令之外的类别。 | Google Play 帮助页的操作要求应认真对待；但本轮链接的 Act 原文 §1(3) 写明法律自中央政府另行公告的日期起施行。因此此处记录的是 Google Play 帮助页表述，不据此单独断言 Act 的法定生效状态；需核对 Gazette 生效公告和后续法律状态。 |
| 印度：股票/投资应用 | 股票交易、投资或证券市场应用须遵守 SEBI 管理的适用法规。Google 列出 SEBI-verified 徽章条件：完整填写 Financial features declaration，SEBI 有效注册且保持认可交易所会员身份，Play 商店信息出现在相关交易所的授权移动应用名册，Console 企业/联系人与监管申报一致；不得误用注册编号或暗示超范围的官方背书。页面链接 BSE、NSE、MCX、NCDEX 名册。 | 徽章展示条件不是完整的法律/许可清单；具体牌照、交易所和金融申报需按业务模式核对。 |
| 越南：在线游戏 | 自 2024-12-25 起，Google 页面指向 Decree 147/2024/ND-CP 的在线游戏许可和展示信息要求。开发者应咨询越南广播与电子信息局 ABEI 及许可证查询/办理入口，取得许可后留存数字文件备查。 | 许可证类别依游戏和服务形态而异；Google 页面本身提醒不要仅据其摘要判断越南法律合规。 |

## 年龄信号的技术子链

Google Play Age Signals API 的 [Overview](https://developer.android.com/google/play/age-signals/overview) 与 [Use the API](https://developer.android.com/google/play/age-signals/use-age-signals-api) 是巴西页面直接链接的技术解释。2026-10-22 核验时，Android 文档标示 SDK 0.0.4；API 先返回 `SHARED`、`NOT_SHARED` 或 `VERIFICATION_REQUIRED` 状态，只有共享状态才请求年龄信号。默认年龄段为 0–12、13–15、16–17、18+，可配置自定义区间。用户拒绝时应用不能获得年龄信号；适用地区强制年龄核验时，用户可能要到 Play 商店完成核验/监督设置。API 文档还提到美国部分州的强制年龄分享流程，因此该技术后代并非巴西专用。年龄信号只应按 Play Data/User Data 政策和适用法律限定用途。API 的共享偏好、响应字段、显著变更、撤销批准和用户控制页面已单列到[年龄信号技术子链](../age-restricted-child-safety/age-restricted-child-safety.zh-CN.md)。

## 直接子链接与访问状态

当前帮助页正文有 30 次政策/地区/账号相关链接，指向 29 个不同目标；表格合并重复目标。另行点击了正文末尾的 Contact support 和页脚控件：Contact support 指向 [otherbugs 支持入口](https://support.google.com/googleplay/android-developer/contact/otherbugs)，随后重定向到需登录的 [Play Console 工单表单](https://play.google.com/console/u/0/developers/create-support-ticket?form=3)；页脚 [Help Community](https://support.google.com/googleplay/android-developer/community?help_center_link=CJ7u-wISQFJlcXVpcmVtcyBmb3IgZGlzdHJpYnV0aW5nIGFwcHMgaW4gc3BlY2lmaWMgY291bnRyaWVz&hl=en) 返回 Cache miss，[Contact us](https://support.google.com/googleplay/android-developer/gethelp) 重定向到需登录的 Play Console 帮助与支持页。帮助中心另有共享的 [Policy education and app requirements 索引](https://support.google.com/googleplay/android-developer/topic/12798386?hl=en)，列出 32 项相关帮助资源；该侧栏与国家页面正文要求分开，目标已在递归链接图和逐 URL 台账中登记。支持/社区及 Console 入口不是新增公开政策条文，未提交工单或社区帖子。

| 目标页 | 页面关系与本次核验 |
| --- | --- |
| [Digital Child and Adolescent Statute / Lei 15.211](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/l15211.htm) | 官方法律全文已打开。§1(3) 写明由中央政府以 Gazette 公告指定施行日；记录法条文本与 Play 页面要求的差异，不推断当前 commencement。 |
| [Play Age Signals API Overview](https://developer.android.com/google/play/age-signals/overview)、[API usage](https://developer.android.com/google/play/age-signals/use-age-signals-api) | 两页已打开；前者介绍 API/版本/年龄段，后者给出共享状态、请求流程、美国州强制分享分支和代码示例。 |
| [Content rating requirements](https://support.google.com/googleplay/android-developer/answer/9859655) 与 [Content Ratings](https://support.google.com/googleplay/android-developer/answer/9898843) → [IARC](https://www.globalratings.com/) | 两篇 Play 帮助页已打开；前者解释问卷、地区过滤、广告适配和申诉，后者说明 IARC 评级、重填问卷及评级申诉；后者再链接 IARC。Google 页面提示 ClassInd 可能需要更新。 |
| [EU Geo-blocking Regulation (EU) 2018/302](https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX:32018R0302) 与 [European Commission Geo-blocking overview](https://digital-strategy.ec.europa.eu/en/policies/geoblocking) | 欧盟法规目标因读取接口返回极短内容，未提取全文；欧委会说明页已打开。Play Help 将规则简述为不得无正当理由按国籍、居住地或营业地歧视，并指出版权服务等边界。 |
| Japan Consumer Affairs Agency 原始直链 [no-trouble.go.jp](https://www.no-trouble.go.jp/)；日本金融厅 [2019 prepaid/payment PDF](https://www.fsa.go.jp/common/about/pamphlet/2019purika.pdf)、[2022 consumer-contract PDF](https://www.fsa.go.jp/common/about/pamphlet/2022purika.pdf) 与 [game-developer PDF](https://www.fsa.go.jp/common/about/pamphlet/game.pdf) | Play 帮助页显示的 CAA 目标是 `www.no-trouble.go.jp`，但抓取工具无法打开。三份 FSA PDF 已打开；它们是法律说明/行业材料，不替代日本法条和律师判断。 |
| [Korea GRAC](https://www.grac.or.kr/english/)、[概率型物品披露指引](https://www.grac.or.kr/board/Inform.aspx?bno=823&searchtext=&searchtype=004&type=view)、[Play Payments policy](https://support.google.com/googleplay/android-developer/answer/9858738?hl=en) | Play Payments 已打开；GRAC 主站只返回单行，具体指引页被网站防火墙限制。韩国要求摘要以 Google Play 帮助页为依据，GRAC 目标保留为官方后续核查入口。 |
| [Korea MOGEF](https://english.mogef.go.kr/index.jsp) 与 [KCC](https://eng.kcc.go.kr/) | MOGEF 缓存未命中、KCC 请求超时；保留官方机构入口，未推断其站点具体流程。 |
| [India Promotion and Regulation of Online Gaming Act, 2025](https://www.meity.gov.in/static/uploads/2025/10/8a7f103cefc68ed8aaa2ebc9a2ed7c13.pdf) | 官方法案 PDF 已打开；列明 online money game 定义、禁令、广告/资金限制及 e-sports/social-game 章节。Act §1(3) 留待核对中央政府 commencement notification。 |
| 印度交易所应用名册：[BSE](https://www.bseindia.com/investors/mobiletradingmember)、[NSE](https://www.nseindia.com/trade/members-compliance/list-of-mobile-applications)、[MCX](https://www.mcxindia.com/technology/ctcl/mobile-applications-of-trading-members)、[NCDEX](https://ncdex.com/ctcl/listing-of-trading-members-mobile-application) | NSE 和 MCX 页面已打开；BSE 返回 403、NCDEX 页面已打开。它们是交易所的动态名册，不是 Google Play 对某开发者资格的批准。 |
| 越南 [ABEI](https://abei.gov.vn/) 与[游戏许可查询/办理入口](https://giayphep.abei.gov.vn/) | 许可入口已打开；ABEI 主站请求返回内部错误。页面未复制各许可表格或法规全文。 |
| [Payments Center](https://payments.google.com/) 与 [Find your Merchant ID](https://support.google.com/paymentscenter/answer/7163092) | Payments Center 是账号专属付款资料入口；Merchant ID 帮助页已打开。该分支解释如何找到巴西商户验证所用 ID，不产生新的内容政策要求。 |
| [Google Privacy Policy](https://policies.google.com/privacy) | 已打开；帮助页用它说明提交给 Google 的材料将按 Google 隐私政策处理。这是 Google 自身数据处理说明，不是开发者的 Play 隐私政策。 |
| [Play Console Production](https://play.google.com/console/developers/app/tracks/production)、[Account details](https://play.google.com/console/developers/contact-details)、[Developer page](https://play.google.com/console/developers/accountdetails) | 均重定向到登录页，无法公开读取；页面流程和账号数据须由开发者登录检查。 |

## 使用边界与相关专题

国家页是导航快照，不是当地法律的完整清单。对上线决策应逐国确认商户/开发者资格、年龄分级、许可证、披露、税务、消费者权益和新法规公告。印度 Act 的生效条件、韩国许可和各市场金融牌照尤其应在发布前重查。

- [年龄限制与儿童安全](../age-restricted-child-safety/age-restricted-child-safety.zh-CN.md) · [内容分级](../content-ratings/content-ratings.zh-CN.md) · [真钱赌博](../real-money-gambling/real-money-gambling.zh-CN.md)
- [金融服务与贷款](../financial-services-and-loans/financial-services-and-loans.zh-CN.md) · [加密资产/NFT](../crypto-assets-and-nfts/crypto-assets-and-nfts.zh-CN.md) · [付款与订阅](../payments/payments-and-subscriptions.zh-CN.md)

本轮覆盖 Google 国家/地区帮助页的列出内容、主要正文直链及年龄信号 API 子链；交易所公告、全套本地法规、每个外部站点的站内导航、Console 私有材料与所有更深孙链接仍需按具体市场/应用继续核查。动态名册及法律生效状态不能作为永久静态副本。
