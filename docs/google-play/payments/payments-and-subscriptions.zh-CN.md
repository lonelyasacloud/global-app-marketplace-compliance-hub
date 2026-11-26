---
id: google-play.payments-and-subscriptions
platform: google-play
language: zh-CN
authority: normative
status: current
kb_checked_at: 2026-10-24
review_due: 2027-01-24
regions: [global]
topics: [payments, google-play-billing, subscriptions, alternative-billing, service-fees]
snapshot_id: play.payments-subscriptions
snapshot_package: "GooglePlay-KnowledgeBase-2026-10-24-review.zip"
coverage_status: "detailed-summary"
source_url: "https://support.google.com/googleplay/android-developer/answer/9858738?hl=en"
source_url_zh: "https://support.google.com/googleplay/android-developer/answer/9858738?hl=zh-CN"
---

# Google Play 付款、计费与订阅政策

> **导入说明（Google batch 1）。** 本页正文取自 2026-10-24 Google Play 知识库快照里已经分开的中文改写摘要，不是 Google 已发布中文页面的逐字文本。英文官方页面是效力来源。`kb_checked_at` 使用快照源文件记录的核对日；本次导入没有重新打开线上官方页面。文中“本知识库”“本库”“本地专题”描述的是该快照知识库的覆盖范围，不是本仓库已经导入的页面清单。快照里指向尚未导入本仓库的专题、链接图、台账或 CSV 的相对链接，已改为文字提及；指向本批六个专题的相对链接已改到本仓库路径。 本页中文是编辑改写。快照记录英文与简体中文 Payments 帮助正文均已打开；Subscriptions 政策的 `hl=zh-CN` 地址当时不可访问，核对使用了英文页。支持分发地区帮助页的简体中文变体当时不可访问。Merchant guidelines 的英文和简体中文直接入口均返回 Cache miss。EEA External Offers 条款在快照中记录为英文版控制、翻译仅供参考。证据等级：Payments / Subscriptions 政策要求为 `normative`；页内已标明的 Console 操作说明为 operational；Android Billing / API 说明为 implementation note；历史费率与归档对照为 historical。

**核对日期：2026-10-24。** 本专题合并 Payments、Subscriptions 的政策要求及其官方帮助/实现子页。Google Play Billing 是 Play 分发数字商品和服务的默认结算方式；替代计费、站外支付链接属于按国家/地区、产品和项目资格开放的例外。订阅展示、取消和持续价值要求独立适用，即使开发者参加了替代计费项目也不能忽略。

Apps Experience 与 revamped Level Up 是自愿项目，不改变基础付款政策；经审核的项目费率和市场日期见[Apps Experience 与 Level Up](../apps-experience-and-level-up/apps-experience-and-level-up.zh-CN.md)。

## 1. 先判断交易卖的是什么

| 交易/场景 | 规则摘要 |
| --- | --- |
| Play 下载付费应用 | 通过 Google Play 下载的付费应用，须使用 Google Play Billing 处理下载付款。 |
| 应用内数字商品、功能、内容和服务 | 默认须使用 Google Play Billing，包括虚拟货币/道具、额外功能、去广告版、云端软件服务以及健身、教育、游戏、音乐、视频等订阅；只有 Payments 政策列明的例外或获批项目才可改变结算方式。 |
| 实体商品/实体服务 | 食品、衣物、交通、机票、现场活动等不应使用 Google Play Billing；实体商品与数字权益混合的 SKU，若数字部分更多或营销为数字商品，则该 SKU 应使用 Play Billing。实体业务可以按适用产品接入 Google Pay 或其他合规结算方案。 |
| P2P、部分捐赠、账单缴费 | P2P 转账、在线拍卖、免税捐赠、信用卡/公用事业账单等属于政策列明的排除项。面向创作者的直接打赏只有在款项 100% 交给创作者且不换取数字内容/权益（包括徽章、贴纸等）时，才可能按 P2P 处理。 |
| 监管医疗服务、1:1 实时服务 | 符合条件的受监管临床服务、以及仅发生在两个人之间且不会录制/回放/复用的 1:1 在线服务可属于例外；需按 Help 页的完整条件核实，不能泛化成所有医疗/咨询/课程都免用 Play Billing。 |
| 礼品卡和已赚取奖励 | 应用内出售礼品卡不要求使用 Play Billing；已赚取或奖励得到的积分可兑换数字商品，但若应用内出售这些积分/虚拟币，仍须使用 Play Billing。虚拟币仅可在购买它的应用或游戏标题中使用。 |
| 随机付费虚拟物品 | 付费获取随机虚拟物品（如 loot box）时，必须在购买前、且紧邻购买流程，清楚披露获得各物品的概率。 |

Google 的 Payments FAQ 还说明：只提供已在应用外购买内容的 **consumption-only/reader** 应用可以上架，但不能在应用内购买这些内容；此类应用可通过文字说明购买方式，但不能加禁止的直接支付链接。用户在应用外收到的营销信息不受应用内链接规则同样处理。对含有实体和数字权益的组合 SKU，按商品实际构成及面向用户的营销描述判断。

## 2. 应用内引导到其他支付方式的限制

除 Payments 政策的 Section 3、8、9 例外外，应用不能通过商店页、应用内促销、WebView、按钮、链接、消息、广告、注册/登录流程或其他 CTA，把用户引导到 Google Play Billing 以外的数字商品付款方式。单纯在政策允许的范围之外展示“官网更便宜”等文字，也可能构成引导；不能把外链藏在帮助页、价格页或账户创建流程中规避限制。

替代结算不是“接入银行卡就可以上线”：通常须先确认地区/应用/用户资格，向 Play Console 注册并获批，按项目接入 Billing/External Links API，展示必要的信息或选择界面，提供订单与订阅管理、退款和客服路径，并遵守 PCI-DSS（处理银行卡数据时）、当地法律及未成年人保护要求。交易报告和服务费依各项目条款执行。

## 3. 替代计费和站外链接项目不是一套全球通用许可

截至本页核对日期，官方项目名称、市场和迁移节奏正在变化。下面仅是导航矩阵；**按具体应用的 Console enrollment、地区项目条款和现行费用页决定资格及实现**。

| 项目 | 市场/适用范围（官方页面快照） | 核心边界与办理 |
| --- | --- | --- |
| Billing choice program（新项目） | 现行入组页列出：EEA、英国、澳大利亚、日本的扩展选项；美国仍列既有 Alternative Billing 和 External Content Links 项目。页面所列澳大利亚/日本开放日为 2026-09-30，EEA/英国为 2026-06-30。 | 用户需在 Google Play Billing 与应用内替代计费或站外网页链接之间选择。先在 Console 入组/配置，再接 API；链接只可指向开发者自有优惠，并提前解释目标页用途。不可误导/重定向用户，需支持订单、订阅、退款与未授权交易争议；对适用交易在 24 小时内上报。 |
| User Choice Billing（既有试点及国家项目） | 另有面向 EEA、澳大利亚、巴西、印度尼西亚、日本、南非、英国等地的既有试点；韩国和印度有各自页面/项目。EEA 资格可覆盖多种外形设备；其他市场通常限手机/平板或非游戏应用，依具体项目而定。 | 用户在 Play Billing 与替代结算间选择。每个应用在同一地区只能参加一个适用项目；完成项目条款、Console 入组、API 和交易报告。2024 年手动报告迁移期限已过；不要照搬旧页面的费率摘要，应核查 2026 年现行费用表。 |
| EEA Alternative Billing（不提供选择的替代计费） | EEA；官方页允许符合条件的应用/游戏和外形设备使用。 | 这是 EEA 特有的 standalone alternative billing 路径；须注册企业、只面向 EEA 用户、在应用内提供并满足用户保护、PCI-DSS、客服/争议、API、24 小时报告及现行服务费要求。它与 EEA User Choice Billing 是不同项目。 |
| EEA External Offers Program | EEA；任何设备形态的应用或游戏均可申请，不能只面向儿童；开发者须为注册企业。 | 必须先为 Play 应用和关联外部应用入组并获批，且只面向 EEA 用户。已入组应用的应用内购买只能使用“不提供用户选择”的替代计费；不能并用 Play Billing 或 User Choice Billing。链接只能去自有优惠/下载，离开前说明目标及用途，不得误导跳转；下载页需展示应用名、图标、描述、版本、大小和开发者，每次安装须由用户明确操作，并提供公开客服、数据政策和当地法律合规。外部应用及全部落地/下载链接须登记、审核；更新版本获批前不得链接。应用商店详情不得宣传 Play 外购买或未由 Play 分发的应用。对适用授权交易须在交易后 24 小时内上报；用户沿外链后 24 小时内完成的交易/安装适用该页列出的服务费。2026-06-04 起：获客费 0%；标准持续费为自动续订订阅 10%、其他数字优惠 20%、每次安装 €1.20（安装费可定期调整）；新 Apps & Games 费率档的其他数字优惠为 15%，首 100 万美元年收入档列为 10%。本页快照为 2026-10-22；既有参与者 2026-01-28 的历史迁移日期已过，应看现行计划条款与 Console 入组状态。不要与美国 External Content Links 混为一谈。 |
| 美国 Alternative Billing | 美国及领地的手机/平板应用或游戏。 | 可在 Play Billing 之外或取代它提供替代结算；入组、提供订单/订阅管理和客服、API/报告及适用费用。官方 2026-07 更新规定从 2026-10-01 开始报告交易并支付相关 Play 服务费。 |
| 美国 External Content Links | 美国及领地的手机/平板应用或游戏；可链接到应用内数字商品的外部购买或自有应用下载。 | 须先入组并获批、仅面向美国用户、接入外链 API；下载应用需登记、审核并提交链接。若并用 Play Billing，所有用户必须能稳定使用 Play Billing。交易和下载须满足用户保护、客服、退款及费用规定。服务费/交易报告从 2026-10-01 开始；成功下载报告和相关费用的截止日现为 **2026-12-01**。详见[美国 ECL 专题](../us-external-content-links/us-external-content-links.zh-CN.md) · [English](../us-external-content-links/us-external-content-links.en-US.md)，其中区分下载事件期限、24 小时计费窗口、API token 和后端交易报告。 |
| 日本 External Payments Program | 日本手机/平板应用或游戏。 | 日本旧项目自 2026-09-30 起不再接收新注册，计划于 2027-03-31 后停止。现有参与者若继续提供站外支付链接，须在 2027-03-31 前转入 Billing choice program。此项不是 EEA External Offers。 |

### 印度替代计费交叉核对（核对日期：2026-10-22）

[2023-02-22 公告](https://support.google.com/googleplay/android-developer/answer/14551113)称，开发者可面向印度用户，在 Play 分发的手机/平板应用内购买中于 Google Play Billing 旁提供替代计费。现行[付款政策](https://support.google.com/googleplay/android-developer/answer/9858738?hl=en)仍以 Play Billing 为默认，并只允许符合地区/项目条件、完成报名且接受适用条款的替代路径。

[印度专属要求页](https://support.google.com/googleplay/android-developer/answer/13306652?hl=en)是独立地区计划：涵盖手机/平板应用与游戏资格、Console 报名、PCI DSS 与欺诈报告保障、API/交易报告和调整后服务费。该页称 API 报告的授权交易须在 24 小时内提交；尚未集成 API 的开发者可按页面说明每月在第 5 个工作日前手动申报。[User Choice Billing 概览](https://support.google.com/googleplay/android-developer/answer/13821247?hl=en)列印度 API 自 2023-11-14 可用，但手工申报停止日期写为 “TBA”；在把手工申报视为当前可用之前，应结合地区页面和账号专属 Console 条款核实。

不要把印度项目与新的[全球 Billing choice 入组页](https://support.google.com/googleplay/android-developer/answer/17161464?hl=en)合并：截至 2026-10-22，该页列 EEA、英国、澳大利亚、日本及既有美国项目，未列印度。[新费率时间表](https://support.google.com/googleplay/android-developer/answer/16954621?hl=en)把“世界其他地区”排在 2027-09-30。印度页面的 4% 减免和全球分阶段费率都应按各自日期/项目条款阅读；临近 rollout 时复核，勿提前套用未来费率。详见公告链接图第 4.53 节。

### 2026–2027 费用时间表快照

Google 的总费用说明把服务费安排与 Billing choice 扩展分地区上线；日期同时用于区分新安装和现有安装。该表**不是所有地区都获得所有支付项目的许可**。

| 日期 | 费用结构/扩展计划涉及地区 | 新 Apps/Games 项目开放计划 |
| --- | --- | --- |
| 2026-06-30 | EEA、英国、美国 | — |
| 2026-09-30 | 澳大利亚、日本 | 澳大利亚、EEA、日本、英国、美国 |
| 2026-12-31 | 韩国 | 韩国 |
| 2027-09-30 | 其他地区 | 其他地区 |

总费率页在本次核对时列出的标准费率示例：新安装的非周期交易/付费应用为 20%，周期交易为 10%；现有安装的应用内一次性交易为 25%，外部链接一次性交易为 20%，周期交易为 10%，付费应用为 25%。满足条件的首 100 万美元年收入档或 Apps Experience/Games Level Up 项目可适用更低费率；Google Play Billing 在澳大利亚、日本、美国、英国和 EEA 另列 5% billing fee。新旧安装按用户首次从 Play 安装或首次从 Play 更新的日期及地区上线日判定。

费率会因地区、安装批次、订阅/非订阅交易、支付路径、项目档位和单独条款不同而变化；部分地区的站外费率仍在单独项目页中说明。上述是 2026-10-23 的官方费率页快照，不能代替开发者账号的合同、发票和 Console 页面。

[Understanding Google Play's Service Fee](https://support.google.com/googleplay/android-developer/answer/11131145?hl=en) 是服务费的解释性 FAQ：它介绍费用所覆盖的 Play 投资，并称受服务费影响的开发者中 99% 可符合 15% 或以下费率；该比例是概述，不是具体费率表或个别账号承诺。页面中韩国/印度替代计费“统一减 4%”等段落保留了旧说明，不能覆盖 2026 费率与当前项目资格；实际费用以[现行费率页](https://support.google.com/googleplay/android-developer/answer/16954621?hl=en)、适用地区的计划条款及 Console 入组状态为准。

### 分发地区、币种换算与退款：不可混用三类地区清单（2026-10-23）

付款与分发资料涉及三张用途不同、会动态变化的表：开发者能否注册、商户能否收款，以及消费者能否在某个国家/地区购买或下载。不要用其中一张表推导另外两张。

| 链路/来源 | 应如何使用 | 当前覆盖边界 |
| --- | --- | --- |
| [开发者与商户注册地区](https://support.google.com/googleplay/android-developer/answer/9306917?hl=en) | 页面把开发者账号注册、商户注册、开发者默认币种分成独立列；默认币种由付款资料所在地决定。支持商户注册也仍要求购买者处于支持购买的消费者地区。 | 动态地区表已打开；不要把其商户资格列误读为消费者可购范围。具体账户仍须在开户/付款资料操作时核验。 |
| [消费者分发地区帮助](https://support.google.com/googleplay/android-developer/answer/10532353?hl=en) → [Play 支持地区动态表](https://play.google.com/supported-locations?hl=en) | 官方称动态表提供应用可用性、支持币种和价格范围。 | 2026-10-23 复核英文、西班牙文和日文 Help 版本，三者范围说明一致；各自表格目标均无可提取正文或数据行。简体中文 Help 变体本次无法读取。没有国家、币种、价格行可核验；不据此补写静态名单，也不把它当作“未上线 Play Billing 国家”清单。 |
| [多币种销售与付款说明](https://support.google.com/googleplay/android-developer/answer/1169947?hl=en) | 满足商户注册地区条件后，可在 Play Console 提供本地币种价格。买家以本地币种付款，开发者按付款资料关联币种收款；若不一致，Play 按订单时汇率换算，汇率会日内更新。买家本地币种订单退款仍以原币种退回，汇率变动不改变买家退款额；拒付从付款资料扣款时沿用原订单汇率。 | 正文已打开。新增买家币种时，应用和 IAP 的本地价格可按默认价、汇率和当地定价模式自动生成；订阅只有在相应 base plan/offer 启用 New countries/regions 后才会在新地区可售。 |
| [设置应用价格](https://support.google.com/googleplay/android-developer/answer/6334373?hl=en) | 价格必须与目标分发地区匹配；没有选择向某国分发，即使填写该国价格，用户仍无法购买。价目会涉及当地税、币种换算与价格模式。 | 正文顶部说自 2025-10-27 起价格模板已解除关联、未来应按商品改价；后续仍有旧模板步骤，页面内部存在冲突。以当前 Console 能力为准，不能把旧步骤当作仍可用功能。 |
| [订单与退款帮助](https://support.google.com/googleplay/android-developer/answer/2741495?hl=en) | 开发者要维护自己的退款政策并遵守当地法律。可按条件对 IAP/订阅全额或部分退款；付费应用不支持部分退款。取消订阅不等于退款；退最近一笔订阅订单可同时撤销权益并停止后续续费，退较早订单则订阅可继续。部分退款按比例退回相应服务费。 | 页面正文及主要权限/政策后代已打开；正文“Related content”直接链接到 Merchant guidelines。目录目标仅返回标题壳，不能据此推断其子页面；退款和管理订阅需相应 Play Console 权限。 |

### Merchant guidelines 与付款资料操作入口

订单/退款帮助正文把 [Merchant guidelines](https://support.google.com/googleplay/android-developer/topic/3452829?hl=en) 作为更新银行资料、查找 Merchant ID、设置税率的相关入口。点击该正文链接后只取得“Merchant guidelines”标题和通用帮助壳；直接英文路由及简体中文路由曾返回 Cache miss。没有可读正文链接或子页清单，因此不从标题、父页描述或侧栏标签反推目录内容。

另行打开的 [Find your Merchant ID](https://support.google.com/googleplay/android-developer/answer/7163092?hl=en) 说明：建立付款资料时 Google 分配唯一数字 Merchant ID，不能更改；在 Play Console 的 Settings → Payments settings → Manage Settings → Public merchant profile 可查找。 [Verify bank account](https://support.google.com/googleplay/android-developer/answer/7161378?hl=en) 说明使用银行账户收款前须验证：美国 EFT 商户可即时验证；适用地区会收到低于 1 美元的测试入账，银行处理可能需要最多 3 个工作日；电汇收款不发送该测试入账。收到金额后需在 Console 中核对并验证，之后可将该账户设为主要收款账户。上述账户操作需要登录，具体支付方式与地区流程以账号页面为准。

Merchant ID 页的 Payments settings 导航还列出付款资料、公开资料、税务资料、银行账户、验证、VAT/税率、FAQ 与 Merchant guidelines 等 10 个入口。它们是付款资料/收款帮助中的并列导航项，并非已证明属于 Merchant guidelines 目录的直接子页。 [Tax rates and VAT](https://support.google.com/googleplay/android-developer/answer/138000?hl=en) 本身已在递归链接图 §4.5.1单独摘要：国家矩阵会变化，Google 不提供税务建议；此类运营帮助不构成新的内容政策义务。

### 拒付费用分担与 Review Refund（订单日期晚于 2026-08-03）

Google 的[退款保护和拒付成本更新](https://support.google.com/googleplay/android-developer/answer/17068375?hl=en)称，针对 **2026-08-03 之后下单**的拒付，开发者承担订单价扣除 Play 服务费后的金额及金融机构相关拒付费用；Google 继续承担该交易的 Play 服务费。该日期已经生效，适用范围按订单日期而非处理日期阅读。

Google 提供可选的 [Review Refund 集成指南](https://developer.android.com/google/play/billing/provide-refund-and-chargeback-suggestions)。收到需要开发者审核的 `PendingRefundReviewNotification` 后，Android 指南建议在 24 小时内调用 [orders.reviewrefund](https://developers.google.com/android-publisher/api-ref/rest/v3/orders/reviewrefund)，提交退款偏好及购买使用证据。必需字段包括 pending refund token、是否提供过试用/样品/购买前功能说明和退款偏好；可选提供消费比例及消费事件。该 API 提供开发者建议，不是拒付胜负保证，也不应泛化成所有退款申请均有 24 小时期限。

流程依赖 [Real-time developer notifications](https://developer.android.com/google/play/billing/rtdn-reference)：RTDN 只通知状态变化，后端应再调用 Google Play Developer API 获取完整状态；测试指南提供 license tester 模拟“购买后拒付”的方法。API 接入还要求服务账号/OAuth 配置及 Play Console 权限；官方 Getting Started 指南为 Billing API 列出查看财务/订单/取消调查数据和管理订单/订阅两项权限。参见操作期限表及政策链接图的 2026-10-23 分支；RTDN/API 的其他事件类型和字段仍有未逐项覆盖的后代。

### 俄罗斯、白俄罗斯与受制裁地区（动态快照）

Google 的[国际制裁 FAQ](https://support.google.com/googleplay/android-developer/answer/11958934?hl=en)和[俄罗斯/白俄罗斯 Billing 帮助页](https://support.google.com/googleplay/android-developer/answer/11950272?hl=en)都明确提示情况可能快速变化。核对日 **2026-10-22**，帮助页描述的主要影响如下；上线、付款或订阅决策前须重新查看官方页面与地区法律：

- 制裁地区 FAQ 表示受影响地区用户仍可下载免费应用，但不能购买；已下载/购买内容通常仍可访问，订阅在当前周期结束后取消。受影响开发者若原收款银行受制裁或停业，可能需在付款资料中改用可接收款项的银行或电子钱包。
- 俄罗斯/白俄罗斯专题页记录：俄罗斯自 2022-03-10 起暂停 Play Billing；免费应用仍可提供。俄罗斯用户不能购买付费应用/游戏、订阅或数字 IAP；白俄罗斯用户也不能购买付费应用/订阅，但免费应用内的购买/订阅状态另有页面列明的差异。付费应用及付费应用更新在俄罗斯/白俄罗斯受阻；俄罗斯用户只能继续使用已下载到设备的已购付费应用。
- 俄罗斯订阅会延续到当前计费期结束且不能续订；官方页列出在 Play Console 最多延长 30 天宽限期，或通过 Play Developer API 延后最多一年。该页原链接指向已弃用的[旧 `purchases.subscriptions.defer` API](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptions/defer)；技术实现应改查 [`purchases.subscriptionsv2.defer`](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/defer)，并核对当前服务可用性及账户权限。
- 制裁 FAQ、俄罗斯 Billing 暂停和[俄罗斯卖家服务暂停](https://support.google.com/googleplay/android-developer/answer/15685001?hl=en)是不同政策/服务状态；不要把“用户无法购买”“开发者无法收款”和适用支付政策的例外混为一谈。该专题只记录 Play 帮助页面快照，不替代制裁法律、付款资料或账号状态核验。

#### 俄罗斯卖家收款账户暂停（单独的开发者侧规则）

[俄罗斯卖家服务暂停页](https://support.google.com/googleplay/android-developer/answer/15685001?hl=en)适用于**收款银行账户位于俄罗斯的 Play 开发者**，不按开发者国籍或用户位置界定。页面称自 2024-12-26 起无限期暂停这类账号通过 Play 获利：2024-12-25（PST）为全球销售最后计入收入日，2025-01-15 发放最终余额且不受原付款门槛影响；此后无法通过 Google Play Billing 获得新付费应用、IAP 或订阅续订收入。该群体仍可发布/更新免费应用。用户只可继续使用 2024-12-26 前已下载的付费应用；先前买过但当时未下载的应用不可再访问。现有订阅持续到当前周期结束、不再续订并于下次付款日取消；已配置宽限期照常，Console 可延长最多 30 天，API 可延后最多一年；帮助页列出的最后退款日为 2024-12-25。

卖家页链接的[收款门槛说明](https://support.google.com/paymentscenter/answer/7163445)指出常规月结门槛按国家/币种变化，并建议 USD 电汇账号考虑至少 100 美元以抵消银行费用；但这不改变俄罗斯卖家页面规定的最终发款日期和无门槛例外。它链接的[俄罗斯/白俄罗斯 Billing 状态](https://support.google.com/googleplay/android-developer/answer/11950272?hl=en)针对用户市场交易限制，与俄罗斯收款账户暂停是两条不同规则；Billing 暂停本身不影响开发者付款。卖家页的[开发者支持入口](https://support.google.com/googleplay/android-developer/gethelp?utm_campaign=ru-by-seller-support-turndown-q4-2024&utm_medium=msa&utm_source=email)被反机器人页面拦截，[通用付款政策链接](https://support.google.com/googleplay/android-developer/answer/10281818?hl=ru)本次超时。请分别核验开发者收款银行、目标用户地区的购买限制、制裁 FAQ 和 Console 状态。

付款资料中的商户银行账户可参考 [Change or remove a merchant bank account](https://support.google.com/paymentscenter/answer/7162795?hl=en)。该页面说明替换唯一已验证的收款账户前必须先添加、验证并设为主要账户；帮助页不会确认某账户能否通过制裁审查或实际收款。

这几个地区页面的帮助中心侧栏还链接到税务/区域要求、美国和 EEA 支付计划等专题；那些链接是分类导航，并不意味着其项目规则适用于俄罗斯/白俄罗斯。

## 4. 订阅的用户体验和取消要求

- 在应用内促销、启动页、订阅计划选择页等位置准确描述订阅权益；不得用误导或操纵式购买流程诱使用户订阅。
- 购买前要清楚展示订阅服务/内容、实际收费金额、计费周期、自动续订条件、订阅是否为使用应用所必需，以及其他重要条款。用户不应多点一步、展开额外页面才看得到关键价格/续费信息。
- 价格应突出显示真实扣款金额和周期。按月拆算年付/半年付价格、遗漏试用结束后的收费、未说明自动续订、关键条款未本地化、隐藏免费/拒绝选项，均是官方列明的常见违规例子。
- 免费试用、优惠期、intro price 或换购报价须说明试用/优惠时长、结束后的价格与周期、如何取消；折扣和一次性奖励只能补充订阅期间持续提供的价值。
- 订阅必须在整个周期内持续提供经常性价值。一次性虚拟币、大礼包或单次游戏加成应作为一次性商品；不能在用户订阅后移除/弱化经常性权益，把订阅变相改成一次性出售。
- 应用内要清楚说明如何管理或取消，并提供易用的在线取消方式。账户设置页可提供 Google Play Subscription Center 链接（Play Billing 订阅）或直接进入开发者的取消流程。
- 通常取消在当前计费周期结束后生效，用户可继续使用至周期结束，当前周期一般不自动退款；部分国家/地区依法律允许立即取消或按比例退款。开发者仍须遵守适用法律，并告知订阅、取消和退款条款变更。

### 生命周期与权益判断：政策要求和 Play Billing 行为

本小节把**Play 政策强制要求**与 **Android Developers 的 Play Billing/API 行为及实现建议**分开。政策要求见上方披露、持续价值和取消规则；下表中的状态名、通知、配置默认值和 API 字段来自官方实现文档，不能据此推导所有开发者都必须启用同一种订阅方案。官方英文 [Subscriptions 政策](https://support.google.com/googleplay/android-developer/answer/9900533?hl=en)本次可直接打开；对应 `hl=zh-CN` 地址本次返回不可访问。Android Developers 使用 `account hold` 表示续费失败后的账号暂停状态，本文保留英文状态名以免与数据保留期混淆。

| Play Billing 场景/状态 | 官方实现行为 | 权益处理含义 |
| --- | --- | --- |
| 新购和状态同步 | 生命周期指南把 `purchases.subscriptionsv2.get` 视为订阅管理的最新状态来源；处理 `SubscriptionNotification` 时应查询该 API。新购流程要求后端取得状态、验证购买，并仅在 `SUBSCRIPTION_STATE_ACTIVE` 时授予权益。 | 不要只凭客户端回调或通知类型作为最终权益判定；用最新资源状态同步后台权益。 |
| 正常取消但尚未到期 | Play 订阅政策规定，Play Billing 订阅通常在当期结束后取消生效，用户在当期剩余时间继续获得内容。API 资源可处于 `SUBSCRIPTION_STATE_CANCELED`，此时应查看各 `lineItems[].expiryTime`；到期时间在未来，用户仍有权益，到期时间已过则应立即移除权益。生命周期指南明确警告，不得在用户仍有权益时撤销内容访问。 | “已取消”不等于“立即失去权益”。若开发者因退款、撤销或其他原因主动缩短权益，需按对应流程和适用法律/政策处理。 |
| `SUBSCRIPTION_STATE_IN_GRACE_PERIOD`（宽限期） | 默认自动续订基础方案启用宽限期，开发者可在 Play Console 调整时长或关闭。指南说宽限期内用户**应保留**订阅权益；Play 会动态延长 `expiryTime`。用户在宽限期修复付款方式后，续订日期保持原日期。即使把宽限期设为 0 天，Play 仍有 24 小时 silent grace；此期间状态仍为 `ACTIVE`，结束后 Play 按最终状态发送相应 RTDN。 | 这是付款恢复流程，不应与主动取消混为一谈。文档中的 “should” 是实现指南措辞，不是另一项独立的订阅产品资格政策。 |
| `SUBSCRIPTION_STATE_ON_HOLD`（account hold） | 自动续订基础方案和分期方案默认启用 account hold；默认时长由系统按“60 天减宽限期时长”计算，可调整或关闭。进入 account hold 后应停止该订阅权益；如果用户修复付款，资源恢复为 `ACTIVE`、同一购买 token 可复用，且计费日期重置为恢复日。未在该状态期间恢复时，Play 会继续发出取消/过期通知。 | 把 `SUBSCRIPTION_ON_HOLD` RTDN 作为重新查询状态的信号；通知收到后通过 V2 `get` 核对资源。默认时长不是所有账号不可更改的固定保证，缩短它可能减少付款恢复数。 |
| 暂停：排定与生效 | 指南称订阅暂停默认启用，也可在 Console 关闭。用户排定暂停后，当前已付费周期结束前仍有权益；暂停生效后状态为 `SUBSCRIPTION_STATE_PAUSED`，不再有权益且不收续订价。按周期提供的暂停时长为：周方案 1–4 周；月、3 月、6 月和年方案各 1–3 个月；页面注明这些选项可能变化。 | 暂停不是立即取消。暂停期结束后 Play 尝试续费；失败直接进入 account hold。用户提前手动恢复时，计费日期改为手动恢复日。 |
| `SUBSCRIPTION_STATE_EXPIRED` | 订阅过期时，指南要求移除权益并把购买状态记为无效。 | RTDN 后查询 V2 资源并同步后台，而不是仅依赖本地缓存。 |

#### 订阅类型、取消 API 和方案/价格变更

- **预付费方案：** 不会自动续订；要连续获得权益，用户须为同一订阅充值续期。初次购买和每次 top-up 都须 acknowledge：周期至少一周的方案须在 3 天内确认，短于一周的须在方案时长的一半内确认；超过期限时，Play 可撤销 top-up、撤销并取消剩余订阅并退款。这里的期限是 Android Developers 的 Billing 接口要求，不是上述订阅披露政策的新增规则。
- **分期方案取消：** 用户发起取消后，如承诺期仍有分期付款，取消在当前承诺期末生效。API 会先发 `SUBSCRIPTION_CANCELLATION_SCHEDULED`；资源仍为 `ACTIVE`，但带有 `pendingCancellation`，承诺期结束后才依次发取消和过期通知。因而此前“当前计费周期结束”不能概括分期方案的承诺期。
- **`purchases.subscriptionsv2.cancel` 的区别：** API 必填 `cancellationContext.cancellationType`。`USER_REQUESTED_STOP_RENEWALS` 对应用户要求停止续订，可恢复，只停止下一次续订；分期方案仍需完成承诺期。`DEVELOPER_REQUESTED_STOP_PAYMENTS` 是开发者停止付款，不能恢复并停止下一笔付款；对分期方案，用户无需支付下一笔，也无需完成承诺期。此 API 语义不能替代政策要求的易用在线取消入口，也不能推导所有用户取消都可立即失去已付费权益。参见 [`purchases.subscriptionsv2.cancel`](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/cancel)。
- **升级、降级和续订：** Android Developers 建议清楚显示用户当前方案和可变更选项。Billing replacement mode 决定权益何时改变、当前已付费时长如何抵扣：`DEFERRED` 到原方案到期/续订时切换；其他常见模式可立即切换，并按模式决定是否按比例抵扣、立即收费或在续订时收费。已有订阅未 acknowledge 时，Play 会阻止提供的方案变更/重新订阅；新购成功后也须 acknowledge。具体模式和限制以[订阅集成指南](https://developer.android.com/google/play/billing/subscriptions)为准。
- **价格变化：** 改基础方案价格默认不影响既有订阅；既有用户留在旧价格 cohort，除非开发者启动迁移。默认 opt-in 涨价要求用户在首次按新价续订前明确接受，未接受则自动取消；官方指南列举的默认提前期为 37 天，并在首次新价续订前 30 天开始由 Play 通知用户。符合条件的地区可使用 opt-out 涨价，但仅在指定地区及涨幅/频次限制下开放，通知期按国家/地区为 30 或 60 天。分期方案在承诺期内的价格变化要等当前承诺期结束。韩国用户对免费试用或 intro 阶段之后的 price step-up 须提供同意；未同意会自动取消。此处描述的是当前 Billing 行为与韩国地区要求，不能把地区规则外推为全球统一的价格变更流程。详见[订阅价格变更指南](https://developer.android.com/google/play/billing/price-changes)。

### Developer API 订阅延期：接口契约与政策边界

这是一项 Play Developer API 的服务端接口，用于延后订阅续订日期；接口参考描述接口能做什么，不定义开发者是否有资格提供某次延期或促销。当前[订阅政策](https://support.google.com/googleplay/android-developer/answer/9900533?hl=en)仍要求清楚披露订阅条款并在整个订阅期提供持续价值；促销奖励只能补充持续价值。接口成功也不等于替代计费、站外支付或其他政策项目的批准，相关资格仍须按适用项目条款和账号状态核实。

- **方法与资源：** `POST https://androidpublisher.googleapis.com/androidpublisher/v3/applications/{packageName}/purchases/subscriptionsv2/tokens/{token}:defer`。路径必填 `packageName`（购买订阅的应用包名）和 `token`（购买时提供给用户设备的 token）；新方法不在路径中要求旧版的 `subscriptionId`。它作用于 [`purchases.subscriptionsv2`](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2) 的订阅购买资源 `SubscriptionPurchaseV2`。
- **请求：** JSON 根对象包含必填 `deferralContext` 对象，类型为 `DeferralContext`。其必填 `etag` 必须是最新订阅 etag（从 [`purchases.subscriptionsv2.get`](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/get) 返回的 `SubscriptionPurchaseV2` 获取；资源页说明 `etag` 表示当前订阅状态并用于订阅操作）；若 etag 与最新值不匹配，API 会失败。必填 `deferDuration` 是 Protocol Buffers [`Duration`](https://protobuf.dev/reference/protobuf/google.protobuf/) 字符串：以秒为单位、最多 9 位小数并以 `s` 结尾，例如 `"3.5s"`。可选 `validateOnly: true` 只验证延期效果且不更改订阅。
- **响应：** 成功时返回 `itemExpiryTimeDetails[]`，每项类型为 `ItemExpiryTimeDetails`，含 `productId` 和新的 `expiryTime`。该时间是 RFC 3339 [`Timestamp`](https://protobuf.dev/reference/protobuf/google.protobuf/) 字符串；生成值为 Z 归一化，可有 0、3、6 或 9 位小数；Timestamp 类型说明还列出非 `Z` 偏移为可接受形式。
- **授权：** 要求 OAuth scope `https://www.googleapis.com/auth/androidpublisher`。
- **成功后的效果：** [订阅生命周期指南](https://developer.android.com/google/play/billing/lifecycle/subscriptions)说明延期会发送 `SUBSCRIPTION_DEFERRED` RTDN、更新续订日期；延期期间用户继续拥有内容的完整访问权且不会被扣款。带加购项的订阅中，所有订阅项目按相同 duration 延期；预付费方案可用此接口延后到期时间。生命周期示例返回 `SUBSCRIPTION_STATE_ACTIVE`，这是结果示例，不是接口页明示的调用前状态限制。
- **状态、重试和上限：** 接口文档明确的调用前状态前提是 `etag` 必须最新；V2 资源页定义了 `subscriptionState` 枚举，但 defer 方法页没有指定可调用状态。方法页也没有列出最大/累计延期时长、幂等键或重试保证，因此不能据此断言这些条件或保证。俄罗斯/白俄罗斯相关 Help 页面所述“API 最多一年”是该政策上下文中的帮助说明；新方法参考页本身没有给出一年的接口上限。
- **旧版替代关系：** 旧 [`purchases.subscriptions.defer`](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptions/defer) 明确标记 deprecated，并写明使用 V2。旧请求按 `subscriptionId` 路由，以 `expectedExpiryTimeMillis`/`desiredExpiryTimeMillis` 两个 Unix epoch 毫秒值指定期望和目标到期时刻；当前到期值不等于 expected 值时不延期，desired 值必须晚于当前到期。V2 改为订阅 token + 最新 `etag` 和相对 duration，成功响应从单个 `newExpiryTimeMillis` 改为每个订阅项目的产品 ID/到期时间数组。

## 5. Play Console 商品结构和技术实现核对

Play Console 的订阅产品按 **subscription → base plan → offer** 管理；每个订阅需先规划不可修改/不可复用的产品 ID，基础方案决定周期与地区/价格，offer 再配置获客/升级资格及免费试用、intro price 等阶段。一次性商品目录正在迁移到新的 **one-time product → purchase option → offer** 对象模型；购买选项可定义买断或租用及地区价格/可用性，offer 可定义预购、折扣或 Play Games 奖励。部分功能处于 Early Access Program (EAP)，需按具体功能确认资格。

#### 一次性商品：CSV 停用后的迁移路径

旧版[创建应用内商品](https://support.google.com/googleplay/android-developer/answer/1153481?hl=en)帮助页明确：Play Console 自 **2025-05-19** 起停止 CSV 商品导入/导出，批量管理应使用 Publishing API，单个商品可在 Play Console 管理；但该页后半仍保留上传/导出 CSV 的旧步骤。这些步骤与页首通知冲突，不能再当作当前 Console 操作指南。该页的新入口指向[一次性商品概览](https://support.google.com/googleplay/android-developer/answer/16430488?hl=en)。概览开头笼统说现有商品会自动迁移，但其更具体的“Migration of in-app products”章节按目录管理方式区分三种情况；应以该迁移章节为准，并在账号内核对实际提示。

| 现有目录管理方式 | 官方说明的迁移行为 | 操作含义 |
| --- | --- | --- |
| 仅通过 Play Console UI 管理，且从未使用 `inappproducts` 服务 | 现有商品自动迁移到新对象模型 | 确认 Console 中产品/购买选项状态和旧客户端兼容性。 |
| 曾用 `inappproducts` API 管理（包括同时使用 Console） | 不会自动迁移；可通过 Play Console 或新的 `onetimeproducts` 服务迁移 | Console 中简单改商品名不会触发迁移；改价格等字段前须迁移。迁移后该商品不能再通过旧 `inappproducts` 服务读取或管理。 |
| 仅用 `inappproducts` API 管理 | 既有商品可继续由旧服务管理，但要使用新模型功能，Google 建议迁移 | 可通过新的 `onetimeproducts` 服务逐个或批量迁移，并同步改造调用；迁移后的商品不能再由旧服务访问。通过旧服务新建的一次性商品不会因此自动迁移。 |

新模型 API 的[商品资源](https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.onetimeproducts)规定商品 ID、在地化商品信息、税务/合规设置和购买选项；[购买选项资源](https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.onetimeproducts.purchaseOptions)管理选项启停与向旧版 Billing Library 保持兼容；[优惠资源](https://developers.google.com/android-publisher/api-ref/rest/v3/monetization.onetimeproducts.purchaseOptions.offers)包含预购、折扣、游戏奖励及地区价格配置。旧版 [`inappproducts` 资源](https://developers.google.com/android-publisher/api-ref/rest/v3/inappproducts)仍描述旧数据结构；其订阅字段已弃用，订阅应改用独立 Subscriptions API。新旧模型的迁移会改变目录/API 接口，不改变数字商品默认须使用 Google Play Billing 的政策，也不自动授予任何替代计费项目资格。

[Tax and compliance settings](https://support.google.com/googleplay/android-developer/answer/10463498?hl=en) 帮助页要求面向 EEA 用户分发时，把产品分类为 Digital Content 或 Service；该分类会影响 EEA 消费者撤回/退款规则（官方帮助页摘要为数字内容可排除撤回权、服务类购买在特定条件下可在 14 天内退款）。产品类别、地区减税选项和美国流媒体通信/娱乐税设置以 Console 当前表单及当地法规为准；该页说明的税务分类修改仅影响未来交易。

#### EEA 产品分类：法规直链与操作页（2026-10-23 复核）

该帮助页正文共 155 行：若产品可面向 EEA 用户分发，须在 Console 选择 Digital Content 或 Service，并参考 [Directive 2011/83/EU（Consumer Rights Directive）](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32011L0083) 与 [Directive (EU) 2019/770（Digital Content Directive）](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?from=EN&uri=CELEX%3A32019L0770)；无法确定时，Play 帮助页建议选择 Service。2019/770 主要提供数字内容/数字服务定义及供应、符合性和救济框架；14 天撤回期及数字内容/已完全履行服务的例外主要见 2011/83 体系。官方索引显示相关例外依履行状态及消费者事先明确同意/确认等条件，并非仅凭“数字内容”标签就能推导一概免除义务。Play 帮助页的“Service 可在 14 天内退款”是其操作摘要，不等于每笔交易均自动退款；个案须核对当前合并法文本、成员国实施法、合同及 Console 流程。

本轮直接目标的 EUR-Lex 页面均触发 JavaScript/机器人验证；只读到官方搜索索引展示的部分条文，不声称已通读法规全文。Play 页面另指出：新开通的多 SKU 订阅不得混用 Digital Content 与 Service；一个多 SKU 购买中的分类须一致。该限制描述 Google Play Billing 新注册/购买路径，不应扩写成所有既有订阅或所有计费渠道的通用法律规则。

产品操作链接也要和政策来源分开：[Create and manage subscriptions](https://support.google.com/googleplay/android-developer/answer/140504) 已打开，提示在订阅配置中进入 Tax and compliance，并回链到本帮助页；[Create an in-app product](https://support.google.com/googleplay/android-developer/answer/1153481) 已打开，但仍有 CSV 停用公告与旧步骤并存的来源冲突。Tax 页面上的三个 Play Console 操作入口均返回抓取内部错误、未暴露目标 URL；本库没有猜测登录后路由。详细直链和访问状态见递归图 §4.5.4。

### VAT/GST 责任按市场、商户和付款路径判断

官方[税率与 VAT 页面](https://support.google.com/googleplay/android-developer/answer/138000?hl=en)逐国家/地区说明谁负责确定、收取和缴纳 VAT/GST/销售税。责任可能取决于买家所在地、开发者所在地/税务登记状态，以及订单使用 Google Play Billing 还是获准的替代计费；部分市场还会对开发者应付给 Google 的服务费另行计税。部分国家要求商店展示含税总价。不能从“Google 是 Merchant of Record”概括推断所有地区、所有付款路径的税务义务；需按税率页的当前市场条目、付款资料中的税务信息及当地顾问意见核实。

#### 税率页的执行判断与代表性地区差异（2026-10-24 复核）

2026-10-24 按区段读完英文税率页的 **896 行正文**，并逐项点击正文中 8 个不同目标：服务费、付款资料、替代计费/UCB、印度 GST、Merchant of Record、价格设置及应用内商品创建。可读帮助正文已在下表和本专题中概括；付款资料路由要求登录，应用内商品创建的本次页面内点击返回 Internal Error，先前完整读取仍保留。它是会持续更新的国家/地区矩阵；本库保留判断规则和代表性差异，不把某日费率表复制成永久清单。逐笔复核至少应区分：**买家销售地、开发者/商户所在地、对应税种的注册状态、Google Play Billing 或具体获准的替代计费项目、产品税务分类，以及付款资料/Console 中的税率设置**。服务费本身的 VAT/GST 与商品交易税是两件事；同一国家也可能按开发者身份和付款方式分配给不同主体。

| 官方页面中的例子 | Google Play Billing | 替代计费或特别事项 |
| --- | --- | --- |
| 澳大利亚 | 对澳洲境外开发者面向澳洲客户的交易，Google 页面列明由 Google 处理 10% GST；在澳洲的开发者仍负责其澳洲客户交易的 GST。 | 替代计费交易由开发者判断、收取并缴纳应付 GST；澳洲开发者未登记 GST 时，服务费上还可能单独收取 GST。 |
| 欧盟 | Google 对 EU 客户的 Play Billing 数字内容/服务交易负责 VAT 的确定、收取和缴纳，即使开发者不在 EU。 | user-choice 或不提供用户选择的 EEA 替代计费计划下，交易 VAT 由开发者负责；爱尔兰开发者与替代计费服务费另有处理。 |
| 印度 | 印度本地开发者需自行判断 GST/GSTIN 和相关税务，页面另述 Google 可能承担适用的预扣税/GST TCS；印度境外开发者的印度 Play Billing GST 由 Google 处理。 | 页面称替代计费交易所需的印度税款由 Google 向开发者收取并代缴。BillDesk 跨境商户 KYC 是单独义务，见下文。 |
| 日本 | 开发者在日本时，由开发者负责日本客户交易 JCT；境外开发者的 Play Billing 交易由 Google 处理 JCT。 | 替代计费下开发者负责交易 JCT 并开具发票；Google 服务费属于 B2B 服务，开发者还需判断并申报相应 JCT。 |
| 英国 / 美国 | 英国：Google 对 Play Billing 数字商品交易负责 VAT。美国：官方页面列出的州/地区中，Google 对 Play Billing 交易处理销售税。 | 英国：替代计费时开发者成为 merchant of record 并负责 VAT。美国：替代计费交易的销售税由开发者负责。美国州/地区适用清单应查看动态页面。 |

#### Payments Center 销售税帮助：市场界面与 Play 规则之间的关系

从上述 Tax and compliance settings 链接打开的 [Check or change sales tax rates](https://support.google.com/paymentscenter/answer/7161449?hl=en) 正文共 175 行。它说明 Payments Center 可由商户设置加拿大/美国税率，并在部分地区查看而不能修改 Google 代管的税率；美国页面区分指定州的 Play Billing 与替代计费责任，并列出佛罗里达、肯塔基、犹他州的通信/视频/音频类税种。其 “here” 州清单链接回 [Tax rates & VAT](https://support.google.com/googleplay/android-developer/answer/138000?hl=en) 动态矩阵；替代计费链接的点击返回内部错误，未暴露目标 URL，因此不把独立已收录的美国替代计费帮助页假定为该短链的确切目标。

该页还链接到 [Merchant sales tax overview](https://support.google.com/paymentscenter/answer/7158952)（本轮重新打开，87 行）和 [印度 GST / 商户核验 / FIRC](https://support.google.com/paymentscenter/answer/7421525?hl=en)（184 行）。EU VAT 概览讨论 Google Play Store 应用/内容购买的 VAT 处理；它不能覆盖 `138000` 中针对替代计费的单独责任分配。印度页则把印度开发者的 GST/GSTIN 与向印度境外销售前的 BillDesk KYC、FIRC 分开说明。Payments Center 的 Transactional Tax 侧栏及另外两个税务目标已在印度 BillDesk 子链中记录；账户设置和当地税务机关/法律仍未穷尽。逐页关系见递归图 §4.5.4。

价格页还说明：支持含税定价的市场中，Play Console 税率会应用于既有的不含税价格；若开发者负责缴税，收取的税款会转交开发者，服务费按不含税商品价格计算。官方示例使用 100 JPY、20% VAT，列出开发者收款 75 JPY、缴税 17 JPY、按示例 70/30 分成后的净额 58 JPY；这是页面的计算示例，不能替代特定地区的现行费率/合同。其商品税设置允许选择无税、Google 预设税率或自定义税率；设置项本身不免除依法应承担的税务责任。完整含税市场与当前税率应以[在线矩阵](https://support.google.com/googleplay/android-developer/answer/138000?hl=en)及账户资料为准。

价格操作链也有一个值得保留的来源冲突：[设置应用价格](https://support.google.com/googleplay/android-developer/answer/6334373?hl=en)页顶部明确称，定价模板自 **2025-10-27** 起已解除关联，未来价格应在单个商品层级修改；但同页后段仍保留创建、编辑和解绑模板的旧步骤。本库不把旧模板步骤当作当前可用能力，执行前应以实际 Console 为准。该页又直接链接到[创建应用内商品](https://support.google.com/googleplay/android-developer/answer/1153481?hl=en)；其 CSV 导入说明另有 2025 年停用公告与旧步骤冲突，见该页面的独立审计记录。

税率页正文中的重点目标和单独的 10 项 **Payments settings** 帮助侧栏，按正文链接/导航分开记录于递归链接图 §4.5.1。截至本轮，主要政策和帮助目标已重开；个别账户入口需要登录，Merchant guidelines 目录抓取返回 Cache miss；逐国税务机关、地方立法、全部付款资料表单和更深链接仍未闭合。

印度开发者另有跨境收款验证：Google 的[印度商户验证、税务与 FIRC 页面](https://support.google.com/paymentscenter/answer/7421525?hl=en)称，印度开发者向印度境外用户销售须通过 BillDesk 完成商户 KYC。2025-12-31 或更早已收到 Google Play 付款的既有商户，须于 **2027-03-15** 前完成，否则面向印度境外用户的应用与应用内商品销售会暂停；2026-01-01 起开始销售的新商户须在境外销售前完成验证。页面说明 KYC 可能要求提交文件、视频核验和位置核验。此验证与 GST 义务分开：印度商户可能需要自行确定印度客户交易的 GST 责任，并按适用要求向 Google 提交 GSTIN；FIRC 由 BillDesk 协调 Citibank 出具。适用范围、Console 横幅和个案截止时间以商户账户及最新页面为准。

#### 印度 BillDesk 核验页：正文子链接与帮助侧栏

2026-10-22 重开该页并逐项检查正文 **12 次链接出现**（不把帮助中心顶栏、页脚算入）；另把 **4 项 Transactional Tax 导航**单独核对。要区分三类内容：印度商户向境外用户销售前完成 BillDesk KYC 是跨境收款验证；GST/GSTIN 是印度国内交易的税务资料；下方 Google Payments 税务帮助中的部分章节面向 Google 服务购买者，不能直接当作 Play 应用销售者的义务。

| 页面链接/导航 | 与印度 BillDesk 核验的关系 | 核对状态 |
| --- | --- | --- |
| [merchant 词条](https://support.google.com/paymentscenter/answer/7687532) · [merchants 词条](https://support.google.com/paymentscenter/answer/7690110) | 分别解释从 Google/Alphabet 服务收取变现收入的 merchant 概念；不是 BillDesk KYC 流程或身份审核标准。 | 两个词条正文均已打开；后者复用前者定义。 |
| [Play Console 开户资料要求](https://support.google.com/googleplay/android-developer/answer/13628312) | 说明开发者账户身份资料；应与用于收款的 merchant profile 分开判断。 | 正文已打开并纳入开发者身份专题。 |
| [收款方式设置入口](https://payments.google.com/gp/w/home/reauthprompt?rtrp=%2Fhome%2Fpaymentmethods) · [Google Payments Center 首页](https://payments.google.com/payments/home) | 账号内付款资料/收款方式操作入口，不提供公开的 BillDesk 账户状态。 | 两个入口都转至登录或空的 Payments 页面，具体账户内容不可读。 |
| [付款支持](https://support.google.com/paymentscenter/gethelp) · [Contact us](https://support.google.com/paymentscenter/gethelp) | 其中两个正文引用都是 Google Payments 支持路线；该页面仍要求直接将 BillDesk 核验问题发给其指定邮箱。 | 两次点击均转至登录受限支持表单；未提交表单或联系任何人。 |
| [通用 merchant 词条](https://support.google.com/answer/7687532) | 页面用词链接到通用 Help 路径；与前述 Payments Center merchant 定义并非同一 URL。 | 点击后 Cache miss；不推断其未读正文。 |
| [印度政府 GST 注册指南](https://tutorial.gst.gov.in/userguide/registration/) | 用于 GST 注册入口，不能替代商户按自身交易判断税务责任。 | 官方网站返回动态注册界面外壳；未提交资料或推断注册资格。 |
| [Service fees](https://support.google.com/googleplay/android-developer/answer/112622) | 说明 Google Play 服务费，不等于印度 GST，也不替代 BillDesk KYC。 | 正文已打开；现行市场费率与计划资格另见付款专题和动态条款。 |
| [设置应用价格](https://support.google.com/googleplay/android-developer/answer/6334373) | 说明市场定价、税是否含在定价中等控制；价格税务处理不等于 BillDesk 付款核验。 | 正文已打开；含税展示和汇率/价格步骤已纳入付款主题，价格模板变化须按现行 Console 操作。 |
| [“Edit”图标](https://lh3.googleusercontent.com/9gmjKx38tFXeEKMUpDGSH39YEZsODZEMhKIqLWqVOh-oNdGRF88R7PKszCXVD_Zq-A%3Dw36-h36) | 付款资料 GST 编辑按钮旁的界面图标，无独立政策内容。 | 图像资源已打开；只作 UI 图示登记。 |
| [Transactional Tax 导航目录](https://support.google.com/paymentscenter/topic/16659972?hl=en&ref_topic=16659968) | 页面侧栏目录，连接销售税税率、GST 购买税和商户销售税概览。 | 目录已打开；以下三个同级条目均分别点击。 |
| [Check or change sales tax rates](https://support.google.com/paymentscenter/answer/7161449) | 按市场与开发者所在地区分由 Google 或商户设定/缴纳税费，涉及印度 GSTIN 与替代计费路径。 | 正文已打开；当地法规及控制台税率设置的更深子链仍需按市场核对。 |
| [GST on purchases](https://support.google.com/paymentscenter/answer/7398224) | 说明印度付款资料中 GSTIN 与 Bill-to 州匹配，以及 Google 服务采购的 GST；这是购买/付款资料帮助，不应直接套作 Play 商品销售的 GST 结论。 | 正文已打开；付款资料设置路线需登录，政府登记页和当地税法后代未全部展开。 |
| [Merchant sales tax overview](https://support.google.com/paymentscenter/answer/7158952) | 概述商户在多国设定税率及欧盟 VAT 处理，作为一般商户税务背景。 | 正文已打开；其按国税务机关/法规链接仍未逐国展开。 |

Transactional Tax 目录及其三个税务子页正文均已打开；税务页面链接的国家法规、税务机关、登录后资料设置和支持后代仍按具体市场留在部分覆盖状态。Help 页面导航和 Console 可见状态不能证明某个开发者账号已完成 BillDesk KYC。

### 预扣税（WHT）与税务凭证

Google 的[预扣税帮助页](https://support.google.com/googleplay/android-developer/answer/9384608?hl=en)列出下列地区规则（按 2026-10-22 打开的页面整理；费率和资格可能变动）：

| 地区 | 页面列出的适用条件/处理 |
| --- | --- |
| 巴西 | 开发者以非 BRL 收款，且巴西用户购买付费应用或应用内商品时，Google/支付处理方会从收入扣除适用的 IRRF 与 CIDE。所链接的[税务居民资料说明](https://support.google.com/product-documentation/answer/13401799)列出默认按客户价格 25% 计算（15% IRRF + 10% CIDE）；特定辖区可能另加 10% IRRF。获批的双重征税协定资料可能降低 IRRF，但不影响 CIDE；需核对税务居民身份、支持地区、付款资料与当前 Google 审核。 |
| 埃及、科威特、缅甸、斯里兰卡 | 页面针对当地用户通过直接运营商代扣（DCB）的交易分别列出最高 20%、5%、2.5%、10% WHT。 |
| 印度 | 页面对印度开发者列出 PAN 已提交时按不含 GST 的客户价格 0.1%，未提交时 5%；需在 Play Console 付款资料提交 PAN。 |
| 肯尼亚 | 页面列出 Google Play 毛销售收入 5% WHT；需提交并通过验证的 PIN，否则未来付款会暂停。 |
| 台湾 | 页面称缺少台湾 VAT ID、在台湾登记的外国 TIN 或有效免税批准时，适用交易可能扣 3%；资料由 Play Console 付款资料管理。 |
| 坦桑尼亚、越南 | 页面分别列出符合条件的当地开发者毛销售收入 5% WHT，并要求提交 TIN/税码，以供当地税务机关申报。越南条款限定于当地法律定义的 business household 或个人开发者。 |

该页还说明 WHT 会作为收入报告中的项目显示；开发者不能单独选择退出，通常只能停止在适用市场分发。Google 提供年度 WHT 信息表（不是政府税务文件或税务建议）；印度商户账号另有季度 Form 131 预扣税凭证。页面 FAQ 还解释了美国/新加坡 DDA 第 3.6 节的通知场景，聚焦非当地税务居民在当地为订阅内容提供服务；不要把它误读为禁止向美国或新加坡发布应用。当地税务义务请以实时页面、商户账户提示及专业顾问为准。

**WHT 页的直接子链接状态：** [税务居民资料与非美国预扣/申报说明](https://support.google.com/product-documentation/answer/13401799)已打开相关巴西和印度章节，进一步说明税务资料提交流程、巴西协定税率/证明，以及印度 GST/PAN/TCS 分工；这是跨 Google 产品的补充税务说明，不会自动替代 Play 商户规则。[巴西雷亚尔币种与税费页](https://support.google.com/googleplay/android-developer/answer/6106161)已通过官方帮助搜索打开全文，BRL资格、巴西银行账户、迁移条件与余额处理见下文；其付款资料、转移应用等关键后代也已打开。Play Console 的[付款资料](https://play.google.com/console/developers/paymentssettings)和[财务报表](https://play.google.com/console/developers/download-reports/financial)要求登录。收入/取消调查报告还需要[对应的 Play Console 访问权限](https://support.google.com/googleplay/android-developer/answer/9844686)；当前英文权限页全文已打开；财务权限及账号/应用范围详见用户权限专题。页面底部的[税务、合规与地区要求帮助主题索引](https://support.google.com/googleplay/android-developer/topic/15819563?hl=en&ref_topic=3452890)已打开，列有 16 个主题入口，但这是主题导航，不等同于本文正文链接。WHT 页的其他反馈、社区和联系支持入口不作为税务义务的解释来源。

#### 税务居民资料分支的直接后代

沿税务居民资料页继续核对了与巴西协定预扣相关的目标。该通用 Google Payments 帮助页还覆盖其他国家/产品，因此这里只摘录与 Play WHT 直接相关的做法，不把它当作当地税务意见。

| 后代页面 | 内容与核验状态 |
| --- | --- |
| [Update Tax Information](https://support.google.com/product-documentation/answer/15500468) | 正文已打开：到 Google Payments Center 登录，在 Settings 下选择需提供资料的国家/地区或企业所在地并编辑。具体账户是否被要求提交资料仍需账号核实。 |
| [Tax Residency Certificates (TRC)](https://support.google.com/product-documentation/answer/15500364) | 正文已打开：TRC 应由政府签发并用于证明税务居民身份；用于协定待遇的国家须与相应税收协定一致，Google 可能要求英文翻译。 |
| [Tax Treaties](https://support.google.com/product-documentation/answer/15500368) | 正文已打开：Google 不替开发者判定协定资格；应由税务顾问或居住地税务机关指导。即使不申请协定待遇，Google 仍可能依法要求税务资料并预扣/申报。 |
| [巴西税务居民证明样例文档](https://docs.google.com/document/d/1DZQxI_3KdsNvW1RTGLSHUAsVsWfeNAHnue166PsmL-Y/edit?resourcekey=0-871X8qCkR0r_xQPuAG6cUg&tab=t.0) | 页面返回 HTTP 410 Gone，样例不可读取；不从失效文档推断格式或字段。 |


#### 巴西 BRL 币种迁移与直接后代

已重新打开 Google 的[巴西雷亚尔币种与税费帮助页](https://support.google.com/googleplay/android-developer/answer/6106161?hl=en)。它说明只有巴西所在地的 Play 开发者账号可以使用 BRL，收取 BRL 付款须有巴西银行账户；巴西开发者若以非 BRL 为默认币种，向巴西客户销售会产生该页所述预扣税。页面称使用美元的巴西 Play 开发者账号将不再受支持，但没有给出精确生效日。

对向巴西客户提供付费应用、应用内购或订阅的相关账号，页面给出迁移流程：以不同邮箱创建新 Google/Play 开发者账号，使用巴西账单地址的本地付款方式支付 25 美元注册费；新账号登录并建立新的付款资料后，通过支持团队申请转移应用、应用数据和付款历史；转移完成后旧账号会被取消并退还注册费，退款后旧账号不能再登录 Play Console。商户余额不能转移；美元旧账号的未结余额仍按正常付款周期结算，旧账号财务报表仍可访问。迁移后要检查并保存新账号中的 BRL 价格。只有免费应用且无内购的开发者无需为此迁移；页面称评分、评论、下载数、付款历史及其他应用资料会转移。

| BRL 帮助页的直接正文链接 | 内容与访问状态 |
| --- | --- |
| [Withholding tax (WHT)](https://support.google.com/googleplay/android-developer/answer/9384608?hl=en) | 已打开，规则见本节上文。 |
| [Google 账号注册](https://accounts.google.com/SignUp) | 点击后到达 Google 注册错误页；属于账号操作流程，无法读取实际注册步骤。 |
| [Play 开发者注册帮助](https://support.google.com/googleplay/android-developer/answer/113468) | 公开抓取触发 Google 反自动化拦截；未从拦截页推断要求。 |
| [Play Console 开发者注册](https://play.google.com/apps/publish/signup) | 需登录 Google/Play Console；注册页点击重定向到登录流程。 |
| [登录新开发者账号](https://play.google.com/apps/) | 重定向到 Google 账号登录；账号内 Console 状态不能公开读取。 |
| [Create a payments profile](https://support.google.com/googleplay/android-developer/answer/7161426) | 全文已打开：需要法定企业名称/实体地址，禁止 PO Box；付款资料国家不能事后更改，资料创建后自动关联 Play Console。其位置、银行与税务链接另行跟踪。 |
| [Transfer apps to a different developer account](https://support.google.com/googleplay/android-developer/answer/6230247) | 全文已打开。除账户都需有效、$25 新账号注册费、付款资料和交易 ID 外，需先下载不随应用转移的报表；转移会影响服务集成、测试组和订单退款操作，Google 通常在 2 个工作日内回复申请。账户/表单后代仍部分需登录。 |
| [Play Console pricing](https://play.google.com/apps/publish/) | 重定向到 Google Play for business 营销页，不是登录后价格设置界面；实际定价路径见原页 Store presence > Pricing & distribution。 |
| [Contact support](https://support.google.com/googleplay/android-developer/contact/otherbugs) 与 [Contact us](https://support.google.com/googleplay/android-developer/gethelp) | 均重定向到需登录的 Play Console 支持请求/帮助页面，公开抓取不可见具体表单。 |
| [Play Developer Help Community](https://support.google.com/googleplay/android-developer/community?help_center_link=CLHY9AISNkN1cnJlbmN5IHN1cHBvcnQgZm9yIEJyYXppbGlhbiBSZWFsIGFuZCByZXF1aXJlZCB0YXhlcw&hl=en) | 返回 Cache miss；未获得社区正文。 |

这些账户创建、转移和支持链接是迁移操作所需资源，不构成新的税务规则。BRL 页面提到的 USD 账号停止支持没有具体日期，迁移前要核对开发者账号状态、可用市场和 Google 支持回复。

Google Play Billing 的官方典型流程：向用户展示商品 → 启动 Play 购买流程 → 在安全后端验证购买 → 仅在购买状态确认为完成后授予权益 → 通知用户 → 向 Google 确认已处理购买；消耗型商品还需 consume。待处理付款完成前不能先发放权益；同一购买令牌不可重复发权益。Google 要求在购买后 **3 天内 acknowledge**，否则可能自动退款并撤销权益。官方推荐把购买令牌发往安全后端验证，并通过 Real-time Developer Notifications 保持订阅生命周期状态同步。

替代计费项目的安全实现还需检查：Play API 显示的信息/家长控制、开发者自绘选择屏的 UX 规范、24 小时交易报告、外部链接目的地/个人信息保护、付款/订阅管理 URL 和 Console 当前声明。Billing Library 集成细节、支持版本与 API 会更新，发布前查看最新集成页和弃用 FAQ，不要把固定版本号写成永久要求。

**Play Billing Library 版本期限（2026-10-24 核验；FAQ 页脚标注最后更新于 2026-10-20）：** Android 官方[弃用 FAQ](https://developer.android.com/google/play/billing/deprecation-faq)规定各版本采用两年弃用周期，并列出常规与延期日期。当前正文有 9 个不同的直接目标：历史 v3 博客、Billing Library upgrade skill 目录、Android skills 概览、Android CLI 概览、Manifest 合并指南、发布说明、v9 迁移指南、需登录的 Policy status、Content License。升级 skill 和 Android 工具是可选工程资源，不决定 Play 政策义务、账号资格或延期审批；v7 延期表单仍须从对应不支持版本的 Console 警告详情进入。

| 版本 | 新应用/更新常规期限 | 符合资格应用延期期限 |
| --- | --- | --- |
| v5 | 2024-08-31（已过） | 2024-11-01（已过） |
| v6 | 2025-08-31（已过） | 2025-11-01（已过） |
| v7 | 2026-08-31（已过） | **2026-11-01** |
| v8 | 2027-08-31 | 2027-11-01 |
| v9 | 2028-08-31 | 2028-11-01 |

如 Play Console 出现不受支持版本警告，符合资格的应用可在 Policy status 对应警告详情打开延期表单；必须按每个应用确认警告和批准状态。FAQ 说未维护的旧 APK 无需更新、仍可运行，但新应用和更新必须使用受支持版本。检查 `build.gradle` 中的库版本；此依赖仅出现在声明 `com.android.vending.BILLING` 权限的 APK 中。若更新后警告仍存在，检查 `AndroidManifest.xml` 是否含 `com.google.android.play.billingclient.version`，并排查 Manifest merging 是否移除了该属性。不要将延期视为自动获批。

## 6. 发布前检查清单

1. 按每个 SKU 标注数字/实体权益、应用内是否消费、收款路径和适用地区；对混合商品按数字权益和营销方式复核。
2. 找出所有站外支付文案、链接、WebView、按钮、Web 落地页、账户创建流程和广告 CTA；只有进入相应且已获批的国家项目时才保留允许的路径。
3. 若提供 Play 外结算，记录项目名、包名、市场、外形设备、用户选择形式、注册状态、API 版本、交易报告和适用费用；核实 2026-12-01 美国 ECL 期限，以及日本 2027-03-31 项目迁移期限。
4. 逐个订阅套餐检查实际扣款价、周期、自动续订、试用转正、所需条件、本地化、持续价值、取消入口和退款说明。
5. 通过测试轨道检查购买成功、待付款、拒付/退款、恢复购买、跨设备、订阅暂停/宽限期/保留期/过期和 API 通知；确认购买未验证或仍为 PENDING 时不会先给权益。
6. 让 Data safety、隐私政策、金融功能申报、儿童保护、商店描述和账单页对实际支付/数据处理保持一致；牌照/金融服务场景另见[金融服务专题](../financial-services-and-loans/financial-services-and-loans.zh-CN.md)。

## 7. 关键子页面和当前访问状态

### Payments policy 正文直链审计（2026-10-22）

英文与简体中文现行 Help 正文均已打开。正文有 **9 个政策链接锚点、7 个去重目标**；侧栏、页脚、反馈和社区入口另行分类，不计入正文。两条赌博锚点指向同一政策；第 9 节在同一目标上出现两次链接。

| 条款/锚点 | 目标页 | 与付款政策的关系及核对结果 |
| --- | --- | --- |
| §3：Gambling Apps；Real-Money Gambling policy（2 个锚点） | [Real-Money Gambling, Games, and Contests](https://support.google.com/googleplay/android-developer/answer/9877032?hl=en) | 已打开。赌博类交易是 Play Billing 不应处理的类别；应用分发、许可、地区和年龄限制仍由赌博政策独立约束，不构成一般计费豁免。 |
| §3：Payments Center Content Policies | [Google Payments User Policies](https://pay.google.com/intl/en_in/about/policy/) | 从父页点击时读取器报错，随后按精确链接直接打开并在本专题摘要。它约束 Google Payments 服务中的受限交易类别，不是 Play Billing 项目资格，也不扩大 Play 付款政策例外。 |
| §3 注：Google Pay developer | [Google Pay & Wallet developer hub](https://developers.google.com/pay/) | 已打开。此处是 Google Pay/Wallet 的产品与集成入口；不能据此推导 Play 数字商品可绕过 Play Billing。 |
| §8：eligible countries/regions | [Understanding user choice billing](https://support.google.com/googleplay/android-developer/answer/13821247?hl=en) | 从中英文父页点击均超时；精确 URL 可直接打开。目标是保留历史市场和 2024 年迁移期限的旧版 UCB 说明，不应用作当前可用地区清单。当前市场以[现行 Billing choice 入组页](https://support.google.com/googleplay/android-developer/answer/17161464?hl=en)及地区项目页为准。 |
| §8：applicable program | [Alternative Billing Systems 主题目录](https://support.google.com/googleplay/android-developer/topic/16471708) | 本轮重新打开目录正文，核对其全部 6 个直接项目页，见下表。目录本身是导航；具体资格、API、费率和 Console 入组以各项目现行条款为准。 |
| §9：program requirements（2 个锚点） | [Programs for external content 主题目录](https://support.google.com/googleplay/android-developer/topic/16470499) | 本轮重新打开目录正文，核对其 4 个直接项目页；Billing choice 与上一目录重复，见下表。EEA、美国和日本项目地域、审批及费用各自独立。 |
| §10：Help Center | [Understanding Google Play’s Payments policy FAQ](https://support.google.com/googleplay/android-developer/answer/10281818?hl=en) | 已打开并有独立正文摘要及直接链接表。FAQ 侧栏的 32 个推荐帮助主题不属于父页面正文直链，未据此声称其所有后代已闭合。 |

### 两个付款项目目录的全部正文直链

两个目录页本身均已打开。Alternative Billing Systems 有 6 个正文目标；Programs for external content 有 4 个，合并后为 **10 个链接出现、9 个唯一目标**（Billing choice 重复）。除 EEA External Offers 从目录页点击超时、但其精确目标随后直接打开外，目标均已在本库有逐 URL 访问记录。目标页自己的更深子链仍按各自审计记录处理，不把目录页访问误记为无限递归完成。

| 来源目录 | 正文直链目标 | 与现行规则的关系、时间点或审计状态 |
| --- | --- | --- |
| Alternative Billing Systems | [Enrolling in the user choice billing pilot](https://support.google.com/googleplay/android-developer/answer/12570971?hl=en) | 已打开。保留试点资格、Play Billing 并用、API/24 小时报告与服务费要求；其中 2024 年手工申报迁移期限已过，旧市场列表不能替代现行动态入组页。 |
| Alternative Billing Systems | [EEA alternative billing](https://support.google.com/googleplay/android-developer/answer/12348241?hl=en) | 已打开并有地区专题摘要。与外部 External Offers、使用用户选择的 Billing choice 是不同路径；不可跨项目套用资格和 UI 规则。 |
| Alternative Billing Systems | [South Korea billing requirements](https://support.google.com/googleplay/android-developer/answer/11222040?hl=en) | 已打开并有地区专题摘要。韩国替代计费需按现行地区条款、披露、报告和 Play Console 状态核实；旧费率说明不能覆盖新费率。 |
| Alternative Billing Systems | [India billing requirements](https://support.google.com/googleplay/android-developer/answer/13306652?hl=en) | 2026-10-22 重开，并与公告、User Choice Billing 概览、动态 Billing choice 市场及 2026 费率时间表交叉核对。印度有独立手机/平板计划；API 交易在 24 小时内报告，印度页仍描述每月手工申报，而概览把印度手工截止日列为 TBA。须核对 Console 当前条款；不可从新的全球 Billing choice 市场表推断印度资格。 |
| Alternative Billing Systems | [US alternative billing](https://support.google.com/googleplay/android-developer/answer/16497028?hl=en) | 已打开并有现行美国费率摘要。参与计划的交易报告和相关服务费自 **2026-10-01** 起生效；市场资格与美国法院命令相关，须按页面和账号状态复核。 |
| Alternative Billing Systems | [Billing choice enrollment and available markets](https://support.google.com/googleplay/android-developer/answer/17161464?hl=en) | 已打开并有现行市场、费用和 API 摘要。澳大利亚/日本新市场日为 **2026-09-30**，EEA/英国为 **2026-06-30**；美国继续由独立美国项目管理。动态市场表和具体应用 Console 资格优先。 |
| Programs for external content | [EEA External Offers enrollment](https://support.google.com/googleplay/android-developer/answer/14372887?hl=en) | 从目录点击超时，精确 URL 已直接打开。现行页列出 EEA 资格、商家身份、应用及关联外部应用审批、目的地和下载安全要求；已加入的 Play 应用不能同时使用 Play Billing 或 UCB。费率更新自 **2026-06-04** 生效。 |
| Programs for external content | [US External Content Links enrollment](https://support.google.com/googleplay/android-developer/answer/16470497?hl=en) | 已打开并有独立摘要。交易报告和相关费用自 **2026-10-01** 起；成功下载的申报和相关费用期限为 **2026-12-01**。要求美国地区限制、应用及外部应用审核、用户保护和 API 集成。 |
| Programs for external content | [Japan External Payments](https://support.google.com/googleplay/android-developer/answer/16787536?hl=en) | 已打开并有独立摘要。**2026-09-30** 起停止新注册，计划在 **2027-03-31** 后停止；现有参与者须在该日前迁移到 Billing choice 才能继续外部网页链接。 |
| Programs for external content | [Billing choice enrollment and available markets](https://support.google.com/googleplay/android-developer/answer/17161464?hl=en) | 与上表相同目标的重复目录链接；市场、入组和费用摘要见上一行。 |

| 来源页面/分支 | 子页/后代 | 关系与状态 |
| --- | --- | --- |
| Billing choices / 2026 fees | [Understanding user choice billing](https://support.google.com/googleplay/android-developer/answer/13821247?hl=en)、[Understanding lower service fees](https://support.google.com/googleplay/android-developer/answer/16954621?hl=en) | 2026-10-22 重开。概览仍列印度 API 自 2023-11-14 可用、手工停止日期为 “TBA”；新费率页把“世界其他地区”安排在 2027-09-30。印度不在新全球 Billing choice 市场表中，应作为独立地区计划看待。印度的 4% 减免与报告方式按其专属页面阅读，报名/迁移以当前 Console 条款确认。 |
| Service Fee FAQ | [Understanding Google Play's Service Fee](https://support.google.com/googleplay/android-developer/answer/11131145?hl=en) | 正文已打开。页面解释服务费支持的分发、工具、计费和安全投入，并给出开发者比例概述；它不是费率表。韩国/印度减 4% 等历史段落可能落后于 2026 地区计划，不能代替当前费率与具体账号资格。 |
| [Tax rates & VAT](https://support.google.com/googleplay/android-developer/answer/138000?hl=en) | [India merchant verification, taxes, and FIRC](https://support.google.com/paymentscenter/answer/7421525?hl=en)、[Merchant of Record](https://support.google.com/googleplay/android-developer/answer/7645364?hl=en)、[Service fees](https://support.google.com/googleplay/android-developer/answer/112622?hl=en)、[User Choice Billing](https://support.google.com/googleplay/android-developer/answer/12570971?hl=en)、[EEA alternative billing](https://support.google.com/googleplay/android-developer/answer/12348241?hl=en)、[Understanding user choice billing](https://support.google.com/googleplay/android-developer/answer/13821247?hl=en)、[Set up app prices](https://support.google.com/googleplay/android-developer/answer/6334373?hl=en) | VAT 页正文已打开，按买家地区、商户税务状态和计费路径分配交易税；动态国家明细未逐条复制。重点后代已打开/交叉核对。印度 BillDesk KYC 截止期与 GST/FIRC 摘要见上文；当地税务机构、税法和付款资料后代仍按具体市场复核。 |
| [Withholding tax (WHT)](https://support.google.com/googleplay/android-developer/answer/9384608?hl=en) | [Tax residency information / non-US withholding](https://support.google.com/product-documentation/answer/13401799), [Currency support for Brazilian Real](https://support.google.com/googleplay/android-developer/answer/6106161), [Payments profile](https://play.google.com/console/developers/paymentssettings), [Download financial reports](https://play.google.com/console/developers/download-reports/financial), [Play Console users and permissions](https://support.google.com/googleplay/android-developer/answer/9844686) | WHT 正文已完整打开并在上文摘要地区条件、报告凭证、退出限制和 DDA 3.6 FAQ。税务居民说明的巴西/印度部分、BRL 迁移页、付款资料创建、应用转移条件及访问权限说明的财务权限段落均已核对；Console 付款/财务报表和账户专属表单仍需登录。WHT 税率/地区表会变动，且不构成税务建议。 |
| [Payments policy](https://support.google.com/googleplay/android-developer/answer/9858738?hl=en) | [Understanding Payments policy FAQ](https://support.google.com/googleplay/android-developer/answer/10281818?hl=en) | 已打开。展开 consumption-only、外部营销/应用内链接边界、实体/数字混合 SKU、礼品卡、忠诚积分、P2P 打赏、临床/1:1 服务、韩国/印度、EEA 和美国项目等 FAQ。 |
| Payments policy | [Real-Money Gambling policy](https://support.google.com/googleplay/android-developer/answer/9877032?hl=en) | 已打开。经批准的真钱赌博/DFS 应用必须免费安装且不得用 Play Billing；牌照、地区和年龄控制另受该政策约束。 |
| Payments policy | [Google Pay developer site](https://developers.google.com/pay/)；[Google Payments User Policies](https://pay.google.com/intl/en_in/about/policy/) | 两页均已打开。Google Payments 用户政策适用于 Google Payments/Google Pay 服务并列有受限交易类别；它不是 Play Billing 替代计费计划，也不是 Play 应用的一般性豁免。 |
| Payments FAQ / 支付项目导航 | [Alternative Billing Systems](https://support.google.com/googleplay/android-developer/topic/16471708)、[Programs for external content](https://support.google.com/googleplay/android-developer/topic/16470499) | 两个帮助主题目录均已打开。前者列旧试点、EEA、韩国、印度、美国与新 Billing choice；后者列 EEA External Offers、美国 External Content Links、外部付款项目和新 Billing choice。 |
| Subscription policy | [Create and manage subscriptions](https://support.google.com/googleplay/android-developer/answer/140504)、[Create an in-app product](https://support.google.com/googleplay/android-developer/answer/1153481) | 已打开。Console 的 product/base plan/offer 设置、订阅条款提示和取消入口与政策逐项对应；产品配置页面不会替代订阅体验审查。 |
| Subscription policy | [Manage/cancel/refund rules](https://support.google.com/googleplay/android-developer/answer/9900533?hl=en#subscription-management-cancellation--refunds) | 已直接打开政策相应章节，核对在线取消方式、Subscription Center/开发者取消链接、周期结束和退款例外。 |
| Billing choice program | [Current enrollment and market page](https://support.google.com/googleplay/android-developer/answer/17161464?hl=en)、[Billing choice Android guide](https://developer.android.com/google/play/billing/billingchoice)、[developer-rendered screen UX](https://developer.android.com/google/play/billing/billingchoice/ux-guidelines) | 入组/市场页、Android 项目概览和开发者自绘 UX 指南均已打开；UX 指南要求替代选项与 Play Billing 平等呈现、明确商户、实时显示支付方式及披露站外跳转。项目条款仍决定资格、市场和报名，不能把 UX 合规等同获批。 |
| EEA external branch | [EEA alternative billing](https://support.google.com/googleplay/android-developer/answer/12348241?hl=en)、[External Offers](https://support.google.com/googleplay/android-developer/answer/14372887?hl=en) | 均已打开。一个是 EEA 应用内、无用户选择的替代计费；另一个可导出站外 offer/外部应用下载，并有不同的 Play Billing 并用限制。 |
| EEA app distribution notice | [Flexibility for EEA app distribution](https://support.google.com/googleplay/android-developer/answer/16232690?hl=en) → [Previous changes to your contract with Google](https://support.google.com/googleplay/answer/16125693?hl=en) → [European Commission Digital Markets Act](https://digital-markets-act.ec.europa.eu/index_en) | 两篇 Help 正文和欧盟委员会入口已打开。自 2024-01-01 起针对符合条件的 EEA 服务豁免指定 MFN 条款；这不是计费或站外分发项目的加入资格，具体见下文。 |
| 美国 alternative branch | [US alternative billing](https://support.google.com/googleplay/android-developer/answer/16497028?hl=en)、[US External Content Links](https://support.google.com/googleplay/android-developer/answer/16470497?hl=en) | 均已打开。确认手机/平板资格、美国范围、注册/API/费用与 2026-10-01 开始的报告/收费；US ECL 成功下载报告和费用截止日为 2026-12-01。 |
| 日本 external payments | [Japan External Payments Program](https://support.google.com/googleplay/android-developer/answer/16787536?hl=en) | 已打开。2026-09-30 起停止新注册、2027-03-31 后停止；仍参与者需迁移至 Billing choice，且该项目不能同时使用 UCB。 |
| Billing integration | [Play Billing integration](https://developer.android.com/google/play/billing/integrate)、[server backend integration](https://developer.android.com/google/play/billing/backend)、[testing](https://developer.android.com/google/play/billing/test) | 集成、后端、RTDN、反欺诈和测试页已逐项打开；服务端验证 purchase token、仅 `PURCHASED` 时授予、按 `messageId` 去重、处理 voided purchase，并用授权测试者覆盖待处理/拒绝/续费等场景。关键子链见下方新表，API 子孙链仍未完全遍历。 |
| Billing Library support | [Version deprecation FAQ](https://developer.android.com/google/play/billing/deprecation-faq) | 2026-10-24 重开完整正文；页脚标注最后更新于 2026-10-20。包含 v5–v9 常规/延期日期、两年弃用周期、依赖检查、警告修复和表单路径。正文有 9 个不同直达目标：六个原有页面，加上升级 skill 目录、Android skills 概览和 Android CLI 概览。升级 skill 是可选工程工具，不决定政策义务、账号资格或延期审批；v7 延期仍须从对应不支持版本警告进入 Console 表单。
| Billing Library FAQ / 发布说明 / v7/v8→v9 迁移指南 → 可选升级辅助工具 | [Android skills 概览](https://developer.android.com/tools/agents/android-skills) · [Android CLI 概览](https://developer.android.com/tools/agents/android-cli) · [Play Billing Library upgrade skill](https://github.com/android/skills/tree/main/play/play-billing-library-version-upgrade) · [SKILL.md](https://github.com/android/skills/blob/main/play/play-billing-library-version-upgrade/SKILL.md) | FAQ 于 2026-10-20 更新后新增对该可选工程工具的入口。升级 workflow 检查 Gradle 依赖/有效 API、先构建、按版本距离规划直接或分阶段迁移，再对照每个主版本的官方迁移指南与发布说明。命令示例为 `android skills add play-billing-library-version-upgrade`；如果 skill 已安装，Android CLI 的 `skills add` 会更新到最新版本。skill 元数据 last-updated 为 2026-10-06；这套自动化指引不是 Play 政策、资格或延期规则。
| Billing Library upgrade skill → 参考资料 | [Version checklist](https://github.com/android/skills/blob/main/play/play-billing-library-version-upgrade/references/version-checklist.md) · [Migration logic](https://github.com/android/skills/blob/main/play/play-billing-library-version-upgrade/references/migration-logic.md) | 清单横跨 PBL v1–v9，涉及异步购买查询、`SkuDetails`→`ProductDetails`、订阅替换模式、待处理购买、v8 自动重连/回调和 v9 移除 API。迁移逻辑重点包括 v8 自动重连、订阅 base plan/offer、查询结果类型、升级/降级与购买历史；它们是依赖版本相关的实现提示，需对照当前官方迁移指南与发布说明复核。 |
| Billing Library 发布说明与迁移指南 → 实时技术依据 | [Google Play Billing Library release notes](https://developer.android.com/google/play/billing/release-notes) · [PBL 7/8 → 9 migration guide](https://developer.android.com/google/play/billing/migrate-gpblv9) | 发布说明页脚标注 2026-10-20；迁移指南页脚标注 2026-09-08，当前示例版本为 9.1.0。发布说明列 PBL 9.1.0（2026-06-18）新增 Billing Choice 信息/对话框 API；9.0.0（2026-05-19）更新 Play Store 被系统阻止时的错误码、`getLinkUri()` 可空处理、`targetSdkVersion` 与应用内价格涨价消息。迁移指南全文已打开，正文 28 次链接锚点归并为 21 个目标；20 个可解析目标及 1 个 URL 未暴露的代码样例均记录状态。API 参考只核对迁移相关成员，不代表完整遍历。 |

### PBL 7/8 → 9 迁移指南的直接链接

指南页脚标注最后更新于 2026-09-08，当前示例版本为 9.1.0。它是版本迁移与工程实现说明，不授予 Play 政策豁免或账号延期。下表覆盖正文 28 次链接出现、21 个去重目标；不同 API 锚点落到同一类参考页时合并展示。每个可解析目标均已打开，API 参考页只摘要相关成员。

| 直接目标 | 与迁移页的关系、访问状态 |
| --- | --- |
| [Billing Library release notes](https://developer.android.com/google/play/billing/release-notes) | 全文已打开；现列 9.1.0/9.0.0 变更。每一条发布说明的 API 成员与更深后代未逐个遍历。 |
| [Play Billing upgrade skill 仓库](https://github.com/android/skills/tree/main/play/play-billing-library-version-upgrade) | 目录已打开；这是可选的代码升级辅助工具，不决定 Play 项目资格或延期批准。SKILL.md 和其参考文件另有上表记录。 |
| [Android skills 概览](https://developer.android.com/tools/agents/android-skills) | 全文已打开；说明如何安装、更新和运行 Android skills，是开发工作流说明。 |
| [Android CLI 概览](https://developer.android.com/tools/agents/android-cli) | 全文已打开；说明 CLI 工具能力及 skill 命令入口，不新增计费政策义务。 |
| [Android CLI 命令参考](https://developer.android.com/tools/agents/android-cli/commands) | 作为 CLI 概览的子链接于 2026-10-24 打开；列出 `skills` 安装、移除、列出和搜索等命令。它是开发工具文档，不新增 Play 计费义务；其他 CLI 子命令与后代未全部展开。 |
| [`BillingClient`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient) | 大型 API 参考页已打开；核对 `queryProductDetailsAsync`、`queryPurchasesAsync`、`launchBillingFlow` 的迁移关联成员。其他成员和后代未全量审计。 |
| [`QueryProductDetailsResult`](https://developer.android.com/reference/com/android/billingclient/api/QueryProductDetailsResult) | API 参考已打开；查询结果可同时包含成功取得的商品详情和未能获取的商品，应用应处理两类结果。其余成员未全量审计。 |
| [Billing integration guide](https://developer.android.com/google/play/billing/integrate) | 全文已打开；是商品展示与购买流程的现行实现指南，与版本替换表配套。其他章节子链仍按该页审计记录处理。 |
| [Query Purchase History](https://developer.android.com/google/play/billing/query-purchase-history) | 全文已打开；说明购买历史查询的用途边界。迁移指南建议用服务端追踪已消耗购买，并用 Voided Purchases API 处理已撤销交易；订阅优惠资格应从 `ProductDetails` 读取，而非旧购买历史接口推断。 |
| [`ProductDetails`](https://developer.android.com/reference/com/android/billingclient/api/ProductDetails) | API 参考已打开；它取代 `SkuDetails` 并支持一次性商品。免费试用/优惠资格改从 `getSubscriptionOfferDetails()` 获取；其他成员未全量审计。 |
| [`BillingClient.ProductType`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient.ProductType) | API 参考已打开；`INAPP` 与 `SUBS` 分别承接旧 SKU 类型常量的功能语义。未遍历全部成员。 |
| [`QueryProductDetailsParams`](https://developer.android.com/reference/com/android/billingclient/api/QueryProductDetailsParams) | API 参考已打开；与新的 `queryProductDetailsAsync` 配合查询商品。未遍历全部字段及成员后代。 |
| [`ProductDetailsResponseListener`](https://developer.android.com/reference/com/android/billingclient/api/ProductDetailsResponseListener) | API 参考已打开；回调接收 `BillingResult` 和查询结果对象。其余成员后代未全量审计。 |
| [Voided Purchases API](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.voidedpurchases) | API 正文已打开；作为服务端撤销/取消购买核查路径，与迁移页建议的消费购买追踪配套。其他 REST 类型与方法后代未全量展开。 |
| [`BillingFlowParams.Builder`](https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.Builder) | API 参考已打开；核对用 `setProductDetailsParamsList` 传入新商品详情参数的替换方向。其余 Builder 成员未全量审计。 |
| [`BillingClient.Builder`](https://developer.android.com/reference/com/android/billingclient/api/BillingClient.Builder) | 相关 API 段落已打开；`enablePendingPurchases(PendingPurchasesParams)` 替代无参旧方法，自动服务重连为推荐项。其余 Builder 成员未全量审计。 |
| [`BillingResult`](https://developer.android.com/reference/com/android/billingclient/api/BillingResult) | API 参考已打开；PBL 9 的 `launchBillingFlow()` 结果可带更具体的子响应码，包括余额不足、优惠资格不符或默认子码；页面其他成员未全量审计。 |
| [AndroidX Core 发布说明](https://developer.android.com/jetpack/androidx/releases/core) | 页面已打开；只核对迁移指南指出的 Core 1.9+ 前置要求。页面很长，其他版本变更未审计。 |
| [`DeveloperProvidedBillingDetails`](https://developer.android.com/reference/com/android/billingclient/api/DeveloperProvidedBillingDetails) | API 参考已打开；外部付款流程中的 `getLinkUri()` 现可为 `null`，解析/启动浏览器前同时处理 `null` 与空字符串。其他成员未全量审计。 |
| `MigrateGpblv9.kt` 代码样例 | 点击返回 Internal Error，浏览器未暴露可确认的目标 URL，样例内容未读取、未推断。 |
| [About subscriptions](https://developer.android.com/google/play/billing/subscriptions) | 两个可选功能链接实际落到同一页面，故去重为一个目标；相关段落说明预付费计划待处理购买与虚拟分期订阅。它们是可选功能接入说明。 |
| [Android Developers Content License](https://developer.android.com/license) | 全文已打开；用于判断 Android 文档与示例的许可边界，不能据此推定 Google Play Help 或政策正文可离线再分发。 |

迁移要点：PBL 7→9 还需改适配新版商品查询回调；按官方表替换已移除接口；建议启用自动服务重连；识别 `launchBillingFlow()` 的细分子响应码；接受 Play Store 被系统阻止时从 `ERROR` 改为 `BILLING_UNAVAILABLE`（需 AndroidX Core 1.9+）；外部付款场景对 `getLinkUri()` 做空值处理。预付计划待处理购买与虚拟分期订阅属于可选集成。当前版本期限及延期资格仍见弃用 FAQ 和 Play Console 账号警告，不应由这份技术指南代判。
| FAQ 正文直链 → 历史版本公告 | [Meet Google Play Billing Library Version 3](https://android-developers.googleblog.com/2020/06/meet-google-play-billing-library.html) | 全文已打开：该 2020 年博客记录 PBL v3 的历史新应用/更新期限及当时宣布的两年支持窗口。它用于解释政策周期沿革，2021 年日期不得替代 FAQ 当前版本表。博客的 6 个正文子链接已逐项尝试，状态见下方。 |
| FAQ 正文直链 → Android skills / CLI 概览 | [Android skills 概览](https://developer.android.com/tools/agents/android-skills) · [Android CLI 概览](https://developer.android.com/tools/agents/android-cli) | 两页正文已打开，说明 Android skills 的安装、更新与项目使用，以及 Android CLI 的开发工具能力；它们是可选开发工作流，不增加 Play 计费政策义务。 |
| FAQ 正文直链 → Billing Library upgrade skill | [Play Billing Library upgrade skill](https://github.com/android/skills/tree/main/play/play-billing-library-version-upgrade) | 从 FAQ 的 GitHub 入口打开技能目录、`SKILL.md` 与两份参考文件。其版本迁移流程和代码检查项属于工程提示，应按当前 Play Billing 官方迁移指南/发布说明复核；不新增政策义务。详见上方 skill 与参考文件清单。 |
| FAQ 正文直链 → Manifest 合并 | [Manage manifest files](https://developer.android.com/build/manage-manifests) | 2026-10-23 重开完整正文（页面标注更新于 2026-02-26）。正文链接出现 24 次，归一化为 11 个外部目标和 6 个同页锚点；11 个外部目标均已打开或有既存访问记录，目标与关系见下表。它是升级后仍出现弃用警告时检查 `com.google.android.play.billingclient.version` 是否在 Manifest 合并中丢失的诊断资料，不新增计费资格或延期规则。 |
| FAQ 正文直链 → Policy status | [Play Console Policy status](https://play.google.com/console/developers/app/policy-center) | 已点击；重定向到 Google 账号登录。延期表单与应用资格需在开发者账号的对应警告中查看，离线资料无法确认账号状态。 |
| FAQ 正文直链 → 内容许可 | [Android Developers Content License](https://developer.android.com/license) | 正文已打开：Android 文档/代码示例通常使用 Apache 2.0 或页面注明许可，站点其他内容通常为 CC BY 2.5，但商标及部分外链材料除外。该许可不能外推到 Google Play Help 或 Play 政策全文。 |

#### Billing FAQ → Manifest 合并排查链（2026-10-23）

FAQ 的路径是：先在 `build.gradle` 核实 APK 使用的 Billing Library 版本；若已升级但仍收到弃用警告，再确认最终 `AndroidManifest.xml` 含 `com.google.android.play.billingclient.version`，并检查 Manifest merging 是否移除了该项。实际 APK/AAB 中的清单来自多个源文件合并；应用主清单、构建变体和依赖库的声明及优先级会影响最终结果。

排查时按**具体发布变体**打开 Android Studio 的 **Merged Manifest** 视图，检查来源高亮、Merging Log 与 Merging Errors；必要时查看 `build/outputs/logs/manifest-merger-<buildVariant>-report.txt`。再追到引入 Billing Library 的依赖及高优先级 manifest/`tools:*` 规则，确认版本元数据在最终构建产物中保留。不要把 `<uses-sdk>`、设备过滤、权限申报或项目延期资格混为一谈；Manifest 合并是工程诊断，账号是否有延期仍以 Play Console 对应警告/表单为准。

| Manifest 合并页正文直链（规范化目标） | 页面内容、与 FAQ 的关系及审计范围 |
| --- | --- |
| [App manifest overview](https://developer.android.com/guide/topics/manifest/manifest-intro) | 正文说明 Manifest 描述应用给构建工具、Android 系统和 Google Play 使用，并声明组件、权限与设备功能。它解释合并结果为何会影响功能和分发可见性。 |
| [Configure build variants](https://developer.android.com/build/build-variants)（合并了 Build with source sets 的锚点） | 相关段落说明 source set/变体可有各自的 manifest；构建变体优先级决定最终值。两个正文链接归并为同一规范 URL。 |
| [`BaseFlavor.minSdk`](https://developer.android.com/reference/tools/gradle-api/7.2/com/android/build/api/dsl/BaseFlavor) | 这是旧版 Gradle API 7.2 参考；`minSdk`/`minSdkPreview` 属性说明 Android 构建配置可覆盖先前设置。它不是当前 Play 提交门槛的来源。 |
| [`<uses-sdk>`](https://developer.android.com/guide/topics/manifest/uses-sdk-element) | 区分 `minSdkVersion` 与 `targetSdkVersion` 的平台含义；Manifest 合并指南明确 Gradle 构建配置可覆盖相应值。Play 的当前目标 API 截止要求另见目标 API 专题。 |
| [Configure your build](https://developer.android.com/build) | `Manifest entries` 段落说明 build variant 配置可覆盖 Manifest 中相应值，并由合并工具组合多个 manifest；用于解释构建源与最终产物之间的差异。 |
| [`<uses-feature>`](https://developer.android.com/guide/topics/manifest/uses-feature-element) | Google Play 会据 required feature 过滤设备；省略 `android:required` 时按必需处理。硬件权限也可能隐含功能需求。官方建议明确声明需求，并可用 Android SDK 的 `aapt2 dump badging` 检查过滤结果。 |
| [`<uses-library>`](https://developer.android.com/guide/topics/manifest/uses-library-element) | `android:required="true"` 会让缺少该共享库的设备无法安装应用，并影响 Google Play 可见性；这是清单设备兼容性规则，不是 Billing 警告修复手段。 |
| [Permissions on Android](https://developer.android.com/guide/topics/permissions/overview) | Android 权限的声明、运行时请求和替代方案工作流已有权限专题与敏感权限专题；这些开发说明不能单独证明某项权限符合 Play 资格。 |
| [`Manifest.permission`](https://developer.android.com/reference/android/Manifest.permission) | Manifest 合并页中的 `WRITE_EXTERNAL_STORAGE`、`READ_PHONE_STATE`、`READ_CONTACTS`、`READ_CALL_LOG`、`WRITE_CONTACTS`、`WRITE_CALL_LOG` 链接均落到此大型 API 参考页。它列平台常量/保护级别；具体 Play 申报、允许用途和适用条件仍由相应政策决定，完整常量目录未逐项审计。 |
| [Configure the app module](https://developer.android.com/build/configure-app-module) | 页面说明 `applicationId` 是 Play Store 中标识应用的 ID，发布后变更会被视为另一个应用；它帮助排查构建身份，不决定 Billing Library 版本。 |
| [Android Developers Content License](https://developer.android.com/license) | 记录 Android 开发文档与代码示例的许可边界；本知识库保留摘要和来源链接，不把该许可套用于 Google Play Help/政策全文。 |

**边界：** 此轮对 Manifest 合并页 11 个规范化外部目标逐一打开或关联到已有专题；其技术目标自己的导航/API/代码样例后代不等于 Play 政策要求，且没有声称无限递归闭合。每个目标的访问状态和未审计后代分别记录在逐 URL 审计表及来源 URL 台账。

### 历史 PBL v3 博客的正文子链接

下表覆盖 2020 年博客正文中 6 个直接链接锚点。它们是 FAQ → 博客的下一层；仅保留和当前 Billing Library 升级/实施有关的关系，不把 2021 年历史门槛当作当前政策。

| 博客正文链接 | 访问结果与关系 |
| --- | --- |
| [Promo codes](https://developer.android.com/google/play/billing/promo) | 全文已打开。说明一次性商品码与订阅试用码、使用限制、Play 内/应用内兑换，以及站外兑换后购买处理；页面更新于 2026-02-26。此为优惠码功能指南，不改变当前版本期限。 |
| [Google Play Billing Library for Unity](https://developer.android.com/google/play/billing/unity) | 全文已打开。记录 Unity IAP 抽象层、插件导入、构建冲突修复、购买/延迟购买处理和平台分支；页面更新于 2026-09-01。它是实现指南，不能替代 Unity IAP/SDK 当前版本检查。 |
| [旧 AIDL migration guide](https://developer.android.com/google/play/billing/migrate) | 原博客的目标返回 404；没有推断旧迁移步骤。当前迁移应参考 v9 迁移指南和现行 release notes。 |
| [2020 视频 walkthrough](https://www.youtube.com/watch?v=Cj5vq1AOJeQ) | 浏览器读取器无法打开 YouTube 视频；未从标题推断视频内容。 |
| “documentation” → [现行 Billing integration guide](https://developer.android.com/google/play/billing/billing_library_overview) | 旧链接重定向到当前集成指南规范页 `/google/play/billing/integrate`；现行指南已在上方 Billing integration 行摘要。 |
| “contact us” | 点击读取失败，工具未返回可确认的目标 URL 或页面正文；此访问缺口保留为未解析链接。 |

### Billing 后端、计费选择 UX 与测试子链

以下 Android Developers 页面提供实现和测试指导，不会自动授予任何地区替代计费/站外项目资格；资格、国家范围、费率和报名仍须以相应 Play 帮助政策与账号状态为准。

- **后端验证与权益同步：** 建立服务端购买状态系统，使用 RTDN 响应购买/订阅状态变化，按 `messageId` 去重；用购买 token 在 Developer API 验证后再授予权益，`PENDING` 状态不得先发货。有效购买后立即 acknowledge/consume，监控 voided/refunded/charged-back 购买并按需要撤销权益。服务端确认可避免客户端离线或恶意篡改导致的漏确认；未在 3 天内 acknowledge 的购买可能自动退款。
- **订阅/API 生命周期：** [Google Play Developer API](https://developers.google.com/android-publisher)涵盖订阅与一次性购买等资源；订阅延期接口的路径、请求/响应类型、OAuth scope、etag 前提与成功后效果见上方“Developer API 订阅延期”说明。旧 `purchases.subscriptions.defer` 在自己的 API 参考页明确标记 deprecated，并指向 V2。
- **RTDN 生命周期：** [Purchase lifecycle and RTDNs](https://developer.android.com/google/play/billing/lifecycle)说明以 Pub/Sub 接收变更，解码数据、按唯一 `messageId` 去重，再依据一次性购买/订阅事件更新权益；不建议只靠定时轮询。该页链接 setup、push/pull、RTDN 消息结构、一次性购买和订阅生命周期指南，API 技术子孙链仍未逐项展开。
- **反欺诈与内容交付：** [Fight fraud and abuse](https://developer.android.com/google/play/billing/security)建议敏感验证逻辑放服务端、将 purchase token 作为唯一标识并以 Developer API 校验；只在状态为 `PURCHASED` 时授予，拒绝可疑交易时不要确认/消费，使用 API 明确退款/撤销；同步处理 linked token、voided purchases 与内容追回。不要用 order ID 作为唯一键；数字内容可由服务端/实时服务交付，避免将可直接提取的完整内容打包在 APK 内。
- **测试矩阵：** [Billing 测试指南](https://developer.android.com/google/play/billing/test)和[授权测试账号说明](https://support.google.com/googleplay/android-developer/answer/6062777)建议使用 license testers、测试轨道和 Play Billing Lab，覆盖批准/拒绝、重复购买、待处理/取消、chargeback、订阅续期/宽限期/暂停等场景。测试轨道的非授权测试者可能产生真实扣款；license tester 中暂停/重新订阅等特性即使生产 Console 未开放也可能可见，应另用非授权测试账号确认关闭状态。测试购买未及时 acknowledge 可能在 3 分钟自动退款；Billing Lab 的部分模拟配置约 2 小时过期。
- **计费选项的公平呈现：** [开发者自绘 choice screen 指南](https://developer.android.com/google/play/billing/billingchoice/ux-guidelines)要求 Play Billing 与替代选项在按钮尺寸、文本、对比度、标识和位置上平等且相邻；替代计费要让用户辨认实际服务方，Google Play 支付方式由 API 实时读取且不得缓存。引导至站外网页时，需清楚说明将离开应用。该 UI 指南只适用于已获准参加的项目，不能单独作为站外引导许可。
- **User Choice Billing（用户选择计费）：** 仅在相应地区项目资格、报名和 Console 设置都满足时启用。客户端以 `enableUserChoiceBilling` 注册 `UserChoiceBillingListener`；符合用户 Play 国家/地区和项目条件时，Play 显示选择界面，选 Play 的用户走标准 Play Billing；选替代计费时，回调返回 `externalTransactionToken`，应用把 token 安全传给后端并发起开发者结算。完成的交易由后端在 24 小时内向 Developer API 上报。替代计费订阅的升级/降级继续走原结算系统，并关联原 `externalTransactionId`；手工上报迁移期限须看最新项目通知。
- **Alternative Billing only（仅替代计费）：** 不显示 Play Billing 与替代方式的选择。客户端启用 `enableAlternativeBillingOnly`，先用 `isAlternativeBillingOnlyAvailableAsync` 检查可用性；只有返回 `OK` 才继续。开始购买前必须调用 Play 提供的信息弹窗；只有弹窗调用成功才继续。每笔一次性购买、新订阅和订阅升级/降级都生成新 token，后端须在 24 小时内上报。若功能不可用、设备不支持或发生错误，不要继续站外交易。
- **EEA External Offers（欧洲经济区外部优惠）：** 这是站外链接购买/应用下载流程，不等于应用内替代计费。先满足当前项目条款并获准，再启用 `BillingProgram.EXTERNAL_OFFER`；按用户检查 `isBillingProgramAvailableAsync`。每次跳出前立即生成新 token，不缓存跨交易复用；在主线程调用 `launchExternalLink`，处理 Play 可能展示的信息屏。下载链接须已在 Play Console 登记并批准，下载须用 `LAUNCH_IN_EXTERNAL_BROWSER_OR_APP`；若应用自行打开链接，只在回调为 `OK` 后跳转，URI 不得携带个人身份信息。该项目的交易报告走后端 Developer API；同一个外部优惠流程中若有多笔购买，官方集成指南允许复用该 token，具体交易仍要各自生成唯一交易 ID。
- **版本与 UX 适用范围：** 官方 Alternative Billing only 总览写 Billing Library 6.2.1+，其详细接入页写 6.1+，存在版本表述差异；External Offers 总览和接入页均写 8.2.1+，UCB 页写 5.2+。版本要求会变，实施前看当前 Play Billing release notes。按相应 API 接入时，Play 客户端 API 已实现指南要求的信息/选择界面，不需另行套用旧 interim UX；改用手工呈现流程时再按对应地区 interim UX 页面核验。API 实现不替代项目资格或入组审批。
- **站外交易上报的完整性约束：** 仅在用户所在国家/地区及开发者/应用获准参加的项目中发起和上报交易；不支持的项目/地区 API 请求会被拒绝。适用事件包括首次购买、订阅续费、预付套餐充值、升级/降级、退款和应用下载；免费试用与应用安装也须以零金额上报。首次购买、首次订阅周期和应用下载提交 Play Billing Library 提供的 `externalTransactionToken` 及新的唯一 `externalTransactionId`；后续续费/充值生成新的唯一 ID，并填初始交易 ID，后续事件不再传 token。商品变化，或订阅取消/到期后重新购买，需另建交易 ID。ID 不得包含个人身份、专有或机密信息。退款要指向被退的具体交易/订阅周期；部分退款填税前退款金额。
- **站外应用下载及税务字段：** External Offers 的首次优惠交易须带 `ExternalOfferDetails`；应用下载事件按零金额一次性交易上报，标记 `LINK_TO_APP_DOWNLOAD` 并提供安装包名/类别。用户在下载的外部应用内继续交易时，沿用下载事件 token，并用 `appDownloadEventExternalTransactionId` 关联原下载事件。印度交易若税额按邦/行政区变化，需提供 `userTaxAddress.administrativeArea`。旧式手工报告迁移只对历史手工报告参与者开放：迁移活动订阅时提交零金额记录、原始注册时间和 `migratedTransactionProgram`；该字段将在手工报告结束后弃用，不是新交易的通用字段。
- **配额与合作伙伴字段：** ExternalTransactions API 对 `createexternaltransaction` 和 `refundexternaltransaction` 调用设有 1,200 QPM 专项限额；`getexternaltransaction` 不计入此限额，页面未说明两个写方法是否分开计桶。Developer API 通用配额另按独立 bucket 管理，官方配额页列出的默认值为每 bucket 3,000 QPM。Media Experience 等合作项目的合格应用才需提供 `transactionProgramCode`；External Offers 交易不要设置该字段。配额增加表单本轮未解析出目标 URL，不能据此承诺获批或提高额度。

| 关键页面 | 页面关系和核验状态 |
| --- | --- |
| [Google Play Billing system](https://developer.android.com/google/play/billing) | 系统概览：Play Billing Library、服务端 API、purchase token、order ID、Pub/Sub/RTDN；仅适用于数字商品，实体商品/服务见 Google Pay。正文已打开。 |
| [Google Play Developer API](https://developers.google.com/android-publisher) | API 总览区分 Publishing API 与订阅/IAP API、tracks、listings 和事务式 edits。正文已打开；API 参考字段随版本变化。 |
| [Server backend integration](https://developer.android.com/google/play/billing/backend) | 目录、生命周期、voided purchase、账单报表与外部交易入口的父级指南；正文已打开，Last updated 2026-10-20。 |
| [Billing choice UX](https://developer.android.com/google/play/billing/billingchoice/ux-guidelines) | 正文已打开，Last updated 2026-06-18；核验清晰标注、Logo、支付方式、按钮平等/相邻及站外跳转提示。 |
| [Alternative billing APIs overview](https://developer.android.com/google/play/billing/alternative) | 正文已打开（页面注明 2026-04-03 更新）。区分 User Choice Billing 和 Alternative Billing only；调用前都必须先符合对应地区项目资格并完成报名。UCB 记载 Billing Library 5.2+；仅替代计费总览写 6.2.1+。 |
| [UCB in-app integration](https://developer.android.com/google/play/billing/alternative/alternative-billing-with-user-choice-in-app) | 全文已打开（2026-09-08 更新）。选 Play 后继续标准购买；选替代方式时 listener 取得 token、交给后端并发起开发者付款，成功交易 24 小时内上报。订阅升级/降级按原结算系统走；手工报告迁移链接和更深 API/样例后代仍需逐页核验。 |
| [Alternative Billing only in-app integration](https://developer.android.com/google/play/billing/alternative/alternative-billing-without-user-choice-in-app) | 全文已打开（2026-09-09 更新）。接入页写 Billing Library 6.1+，与总览的 6.2.1+ 不一致。可用性检查、必需信息弹窗、token 获取及错误处理章节已重点核对；代码样例和 API 方法后代未全部展开。 |
| [External Offers APIs](https://developer.android.com/google/play/billing/external) / [in-app integration](https://developer.android.com/google/play/billing/external/integration) | 两页正文已打开；总览注明 2026-02-26 更新，接入页注明 2026-09-08 更新，均写 Billing Library 8.2.1+。需先获项目批准、按用户查可用性；每次跳出前生成新 token，不缓存；应用下载 URL 要在 Console 预先登记批准，且必须使用 Play 启动模式。 |
| [BillingClient.Builder](https://developer.android.com/reference/com/android/billingclient/api/BillingClient.Builder) / [UserChoiceBillingListener](https://developer.android.com/reference/com/android/billingclient/api/UserChoiceBillingListener) | 相关 API 章节已打开并摘要：Builder 的旧 `enableExternalOffer` 已弃用，改用 `enableBillingProgram(BillingProgram.EXTERNAL_OFFER)`；UCB callback 负责启动开发者付款流程，完成交易由后端报告。API 类的全部方法与跨引用孙页未遍历。 |
| [LaunchExternalLinkParams](https://developer.android.com/reference/com/android/billingclient/api/LaunchExternalLinkParams)、[Builder](https://developer.android.com/reference/com/android/billingclient/api/LaunchExternalLinkParams.Builder) 与 [LaunchMode](https://developer.android.com/reference/com/android/billingclient/api/LaunchExternalLinkParams.LaunchMode) | Builder 与 LaunchMode 的相关章节已打开：URI、token、link type、program 与 launch mode 均可设置；下载 URL 必须先获批，`LAUNCH_MODE_UNSPECIFIED` 不应使用；若设为 `CALLER_WILL_LAUNCH_LINK`，仅在回调 OK 后由应用跳转。类型/方法交叉引用和完整 API 树仍未穷尽。 |
| [External transactions backend guide](https://developer.android.com/google/play/billing/outside-gpb-backend) | 正文已打开；涵盖首次和后续交易上报、交易 ID 关联及不可含 PII 的约束。市场范围取决于对应 Play 项目。 |
| [Getting ready for Play Billing](https://developer.android.com/google/play/billing/getting-ready) | 正文已打开，Last updated 2026-10-20；说明开发者/付款资料、先发布含 Billing Library 的版本以启用 Console 计费、配置商品、授予 Developer API 财务数据权限，以及按应用配置 Pub/Sub RTDN。收到 RTDN 后仍须调用 Developer API 取完整状态。页面示例版本为 Billing Library 9.1.0，版本号会变化；其 Pub/Sub 权限、推送/拉取和云端配置子页未全部递归展开。 |
| [ExternalTransactions REST resource](https://developers.google.com/android-publisher/api-ref/rest/v3/externaltransactions) 与 [create](https://developers.google.com/android-publisher/api-ref/rest/v3/externaltransactions/createexternaltransaction)、[get](https://developers.google.com/android-publisher/api-ref/rest/v3/externaltransactions/getexternaltransaction)、[refund](https://developers.google.com/android-publisher/api-ref/rest/v3/externaltransactions/refundexternaltransaction) | 资源和三个方法正文已打开。API 支持一次性/周期交易、测试购买（不向 Google 收费）以及创建、查询、全额/部分退款。创建方法要求包名下唯一交易 ID（1–63 字符，字母数字、下划线或连字符）并使用 Developer API OAuth scope；退款必须针对原交易，部分退款金额为税前金额。资源类型/字段页仍有未逐项展开的技术孙链接。 |
| [Developer API quotas](https://developers.google.com/android-publisher/quotas) 与 [External Offers program changes](https://support.google.com/googleplay/android-developer/answer/16505463?hl=zh-CN) | 配额页正文已打开；默认通用配额为每 bucket 3,000 QPM。EEA 变更公告正文已完整打开，是简短的当前 External Offers 指引入口，应与[现行项目条款](https://support.google.com/googleplay/android-developer/answer/14372887?hl=zh-CN)合读。 |
| [Play Billing External Offers program](https://support.google.com/googleplay/android-developer/answer/14372887?hl=zh-CN) 与 [Media Experience Program](https://google.play/business/programs/mediaprogram/) | EEA 页面已完整复核：费用自 2026-06-04 生效，报告时限、目的地和下载应用审核要求见上表。Media Experience 页面列出媒体类型、50 万月活安装、账号良好状态及指定平台/API 集成等资格；15% 或更低费率仅适用于获批计划参与者，不能作为普通外部交易费率。另与 [EEA 通用访问条件](../eea-general-conditions/eea-general-conditions.zh-CN.md)对照后确认：父页 E 部分仍保留“标准费率减 3 个百分点”的旧表述；2026-06-30 后的新/现有安装费率以现行 EEA 替代计费 Help 和 Console 账单为准。 |
| [Play Billing setup support form](https://support.google.com/googleplay/android-developer/contact/additional_billing_system_q) | 帮助表单目标已打开但需登录/账号上下文；只记录为支持入口，无法从公开页面判断个别开发者的资格或配额申请结果。 |
| [V2 defer](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/defer)、[V2 get](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2/get) 与[资源页](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptionsv2)、[旧版 defer 方法](https://developers.google.com/android-publisher/api-ref/rest/v3/purchases.subscriptions/defer)、[订阅生命周期指南](https://developer.android.com/google/play/billing/lifecycle/subscriptions)、[俄罗斯/白俄罗斯 Billing 帮助页](https://support.google.com/googleplay/android-developer/answer/11950272?hl=en)、[俄罗斯卖家服务帮助页](https://support.google.com/googleplay/android-developer/answer/15685001?hl=en)和[订阅政策](https://support.google.com/googleplay/android-developer/answer/9900533?hl=en) | 以上 API、生命周期及政策页面已于 2026-10-22 打开核对；直接关联的 [Protocol Buffers 类型页](https://protobuf.dev/reference/protobuf/google.protobuf/)也已打开。V2 参考确认 POST 路径、必填 `packageName`/`token`、`DeferralContext` 字段、`ItemExpiryTimeDetails` 响应及 `androidpublisher` scope；V2 资源页和 get 页确认 `SubscriptionPurchaseV2` 及其 `etag`。旧方法明确标记弃用并由 V2 替代，且说明以 epoch 毫秒检查预期/目标到期时间。生命周期指南说明 `SUBSCRIPTION_DEFERRED`、延期期间完整访问且不扣款、加购项相同延期时长以及预付费到期延期。俄罗斯/白俄罗斯帮助页中的一年说明属于特定政策上下文，不是 V2 方法参考规定的接口上限；卖家服务帮助页另适用于收款银行账户位于俄罗斯的开发者。方法参考未规定状态白名单、延期时长上限、幂等键或重试保证。 |

### 2020 年 Payments 说明博客及其直链

[Listening to Developer Feedback to Improve Google Play（2020-09-28）](https://android-developers.googleblog.com/2020/09/listening-to-developer-feedback-to.html)是政策历史背景：讨论应用商店选择、Play Billing 适用范围的澄清、同等对待和应用外客户沟通；文中“2021-09-30”迁移宽限期限已过。博客不能代表当前站外引导普遍获准；现行付款政策的第 3/8/9 节及区域计划决定当前例外。正文直链及访问状态：

| 2020 博客直链 | 页面关系和状态 |
| --- | --- |
| [2019 年 Android API/政策反馈博客](https://android-developers.googleblog.com/2019/04/improving-update-process-with-your.html) | 已打开，历史背景涉及权限、声明流程、申诉沟通和开发者反馈；不替代现行权限及执行政策。 |
| [Google Privacy 安全说明](https://privacy.google.com/your-security.html) | 目标页请求返回 cache miss；不据此推断隐私控制细节。 |
| [Payments policy 旧链接](https://play.google.com/about/monetization-ads/payments/) | 重定向至现行 [Google Play Payments policy](https://support.google.com/googleplay/android-developer/answer/9858738)；已打开现行条文，旧政策措辞不单独作为当前例外依据。 |
| [Xbox Game Pass 应用页](https://play.google.com/store/apps/details?hl=en_US&id=com.gamepass) | 应用商店抓取失败；仅为当时云游戏服务案例，不是政策规则。 |
| [2020 Payments update FAQs](https://android-developers.googleblog.com/2020/09/commerce-update-faqs.html) | 返回 HTTP 429；没有将标题/旧说明推断成当前 FAQ。 |

### 日本 External Payments：正文直链及重要后代

日本项目页的正文链接和 Android API 文档已按政策关系展开。该项目适用于符合条件的日本手机/平板应用或游戏，要求先入组获批、仅服务日本用户、并排提供 Play Billing 与外部付款选项、提供退款/客服/争议处理，并遵守目的地要求。官方页面称 **2026-09-30 起不再接受新注册，2027-03-31 后停止**；现有参与者如继续提供外部网页付款链接，须在 2027-03-31 前转入 Billing choice。日本项目不能与 User Choice Billing 同时使用。资格、费用和账号入组以当前项目条款及 Play Console 为准。

| 链接层级 | 目标页 | 摘要与关系 | 核验状态 |
| --- | --- | --- | --- |
| 正文直链 | [Billing choice program](https://support.google.com/googleplay/android-developer/answer/17161464?hl=en) | 日本旧项目的后续迁移路径；按当前入组页确认适用市场、表单和 API，不能把旧项目注册状态当作新项目资格。 | 正文已打开；日本项目页本次跳转超时，沿用此前单独核验结果。 |
| 正文直链 | [Payments policy](https://support.google.com/googleplay/android-developer/answer/9858738?hl=en)；[Play Developer policies](https://support.google.com/googleplay/android-developer/answer/18258653?hl=en) | 前者规定数字商品默认使用 Play Billing 及明示例外；后者为更广泛的开发者政策目录。参与项目不豁免其他政策。 | 两页已打开；政策主题另见本知识库专题页。 |
| 正文直链 | [Developer account contact information](https://support.google.com/googleplay/android-developer/answer/10840893?hl=en) | 开发者账号须维护已验证邮箱和电话；个人/组织账号的公开资料及联系人字段不同。金融等特定服务还要核对组织账号要求。 | 正文已打开；账号资料的实际状态需登录 Console 核验。 |
| 正文直链 | [Play Billing external payments overview](https://developer.android.com/google/play/billing/externalpaymentlinks) | 解释日本外部付款 API、Play 管理的用户选择界面和项目术语；该页当时要求 Play Billing Library 8.3 或更高版本。版本要求会变化。 | 正文已打开；侧栏只作相关导航，不视为正文直链。 |
| 正文直链 | [Value provided by Play](https://google.play/howplayworks/)；[first $1M service-fee explainer](https://support.google.com/googleplay/android-developer/answer/10632485?hl=en) | 前者是 Play 价值说明，不是完整费率表；后者是 2021 年费用背景页，只作历史解释。现行费用看地区项目条款和当前费用页。 | 两页已打开；历史说明不覆盖现行条款。 |
| 正文直链 | [External payments enrollment form](https://support.google.com/googleplay/android-developer/contact/external_payments_program) | 表单涉及开发者账号/包名、注册法人、账单地址、公司域名邮箱、客服和争议处理、PCI DSS 确认及授权签字。 | 表单页已打开；需账号登录提交。 |
| 正文直链 | [Japan External Payments Terms of Service](https://support.google.com/googleplay/android-developer/answer/16787955?hl=en) | 计划条款补充 DDA；交易报告、服务费、账单、审计、客服与退出/终止均按条款执行。当前重开请求未返回正文；摘要依据本轮此前成功读取的页面，实际签约文本需登录核对。 | 本轮此前正文已打开；2026-10-22 后续重开时浏览工具报不可访问。 |
| 孙链接：应用内接入 | [In-app integration guidance](https://developer.android.com/google/play/billing/externalpaymentlinks/integration) | 检查用户资格、使用 Billing Library external-payments API、获取外部交易令牌并遵守 Play 管理的选择/跳转流程；只有用户符合项目资格时才发起站外付款。 | 正文已打开；该页还链接 API 方法、迁移指南和代码示例，未逐一展开所有 API 类型/样例。 |
| 孙链接：后端报告 | [Backend integration guidance](https://developer.android.com/google/play/billing/outside-gpb-backend) | 对符合项目资格的国家和交易使用 Developer API 报告；涵盖首笔、续费、升级/降级、退款和零金额交易。交易 ID 必须唯一且不得包含个人、专有或机密信息。 | 正文已打开；依地区项目页判断范围，不把其他项目/地区规则自动套到日本。 |
| 孙链接：API 参考 | [External transactions REST API](https://developers.google.com/android-publisher/api-ref/rest/v3/externaltransactions) | API 提供 create/get/refund；资源含一次性或周期交易信息及测试购买。该参考页还有大量字段、类型和子节点，本专题只摘要与报告流程相关的部分。 | 正文已打开；API 类型和字段的所有后代未穷举。 |
| 并列项目参考 | [EEA External Offers](https://support.google.com/googleplay/android-developer/answer/14372887?hl=en)；[US External Content Links](https://support.google.com/googleplay/android-developer/answer/16470497?hl=en) | 仅作为地区对照：EEA External Offers、美国 External Content Links 与日本 External Payments 的资格、链接用途、计费并用规则和费用各自独立。 | 两页已打开并在上文分开摘要，不可跨地区类推。 |

日本项目 Help 页面还列有 **16 个侧栏相关主题**；它们是帮助中心推荐，不是正文直链，不能据此宣称其下全部页面和技术孙链接已闭包。条款和项目页面会变更；上述记录是 2026-10-22 核验快照。

### Payments FAQ 正文直接链接核验

以下是 [Payments FAQ](https://support.google.com/googleplay/android-developer/answer/10281818?hl=en) 正文中的直接目标；重复指向同一政策的链接合并记录。该 FAQ 当前显示名为 `Policy education and app requirements` 的 32 项 Help 导航（当前 FAQ 也在列表中，另有一条 FGS 预览链接）；它们是侧栏推荐，不是正文直链，且未在本付款专题逐项展开。此 32 项导航的来源是 Payments FAQ，不是 Play Console Requirements `answer/10788890`。

| 正文直链目标 | 核验结果与关联 |
| --- | --- |
| [Play Billing 集成概览](https://developer.android.com/google/play/billing)；[Android 集成指南](https://developer.android.com/google/play/billing/integrate) | 已打开。分别是计费产品概览和实现指南；实现页涵盖客户端、可信后端、购买验证、订阅和实时通知，属于技术实现资料，不扩展为整个 Android Developers 站点的爬取。 |
| [Payments policy](https://support.google.com/googleplay/android-developer/answer/9858738?hl=en) | 已打开，正式规则以当前合并政策为准；FAQ 是解释和举例，不取代政策正文。 |
| [Google Payments User Policies](https://pay.google.com/intl/en_in/about/policy/) | 已打开。这是 Google Payments/Google Pay 服务的用户与交易政策，列有禁止的交易类别；它不是 Play Billing 的替代支付项目，也不能单独作为 Play 应用豁免依据。当前抓取为 India 英文地区页。 |
| 电信/有线运营商资格表单 | 正文链接点击返回抓取错误，目标 URL 未能可靠解析。FAQ 描述的例外仅适用于符合条件、把特定数字服务计入实体服务账单的运营商场景；保留为未核验表单。 |
| [韩国替代计费](https://support.google.com/googleplay/android-developer/answer/11222040?hl=en)、[印度替代计费](https://support.google.com/googleplay/android-developer/answer/13306652?hl=en)、[User Choice Billing pilot 入组页](https://support.google.com/googleplay/android-developer/answer/12570971?hl=en) | UCB 正文已打开。页面仍保留 2024-03-13 API 迁移期限及旧试点市场清单；后者不是当前入组资格的权威来源。它要求注册企业、合格地区并行提供 Play Billing、卡数据处理符合 PCI-DSS、提供客服/未授权交易争议渠道、使用替代计费 API，并在 24 小时内上报交易。该页明确 EEA/英国/美国自 2026-06-30 起按新安装/现有安装区分费率：标准自动续订 10%，一次性数字项目分别为 20%/25%；首 100 万美元收入档为 10%，参与 Apps Experience 或 Games Level Up 的档位为 10%/15%/20%。不要把旧的 4% 减免外推到这些地区；其他市场及目前可加入的计划按[动态 Billing choice 入组页](https://support.google.com/googleplay/android-developer/answer/17161464?hl=en)和各地区条款核对。 |
| [EEA 替代计费](https://support.google.com/googleplay/android-developer/answer/12348241?hl=en)、[EEA External Offers](https://support.google.com/googleplay/android-developer/answer/14372887?hl=en) | 已打开并在上表分开摘要。前者是 EEA 应用内替代计费；后者是外部优惠/下载计划，适用条件不同。 |
| [美国法院命令下的政策更新](https://support.google.com/googleplay/android-developer/answer/15582165?hl=en)、[美国项目目录](https://support.google.com/googleplay/android-developer/topic/16787812) | 已打开。现行页面称项目于 2025-12-09 推出；2026-03-04 Google 与 Epic 达成新和解并请求法院批准修订禁令，更新页说后续会继续发布变化。因此开发者实施仍应以当前项目条款为准。 |
| [美国永久禁令 PDF](https://storage.googleapis.com/gweb-uniblog-publish-prod/documents/2024.10.07_Dkt._1017_Permanent_Injunction.pdf) | 已打开原始法院文件。其若干条款列出截至 2027-11-01 的期限；Google 的 2026 更新又提到请求修订禁令，故须与最新法院文件和 Play 项目页一起读。 |
| [美国替代计费](https://support.google.com/googleplay/android-developer/answer/16497028?hl=en)、[美国 External Content Links](https://support.google.com/googleplay/android-developer/answer/16470497?hl=en) | 已打开。资格仅面向美国手机/平板应用或游戏；项目需加入、获批、实现 API 并按规则报告。ECL 页面列出目的地、客服/退款、下载应用登记和适用费用要求。 |
| [Google Play 应用目录对第三方美国商店开放的公告](https://support.google.com/googleplay/android-developer/answer/17187609?hl=en)、[Play Catalog Access Program](https://support.google.com/googleplay/android-developer/answer/17117200?hl=en)、[Third-party App Store on Play Program](https://support.google.com/googleplay/android-developer/answer/17118006?hl=en) | 三页均已打开。它们讨论美国第三方商店目录访问、商店入驻与审核，不是普通应用开发者普遍必须办理的支付项目；应用列表默认提供给符合条件的第三方商店，开发者可在 Console 管理退出偏好。商店运营方需满足独立组织、信任安全、政策、审核和费用条件。 |
| [Rest of the world 地区列表](https://support.google.com/googleplay/android-developer/answer/12201481?hl=en) → [Supported locations for distribution](https://support.google.com/googleplay/android-developer/answer/10532353?hl=en) → [Play supported-locations 表](https://play.google.com/supported-locations?hl=en) | 两个 Help 页面已打开；最后的 Play 动态表页面无可提取文本。此链说明分发/货币/价格地区；它不是 Payments FAQ 所称未上线 Play Billing 国家的权威清单，不能据此推导支付豁免。 |
| [Play Console Requirements](https://support.google.com/googleplay/android-developer/answer/10788890?hl=en)、[Prepare your app for review](https://support.google.com/googleplay/android-developer/answer/9859455?hl=en) | Play Console Requirements 已在独立双语条目核验；审核指南此前已打开并摘要。FAQ 本次重开审核指南超时，沿用此前已记录的正文核验状态。 |
| [Blockchain-based Content](https://support.google.com/googleplay/android-developer/answer/13607354?hl=en) | 已打开并在[加密资产与 NFT 专题](../crypto-assets-and-nfts/crypto-assets-and-nfts.zh-CN.md)整理；NFT 等数字内容交易仍需按 Payments 规则判断，另有金融功能申报和博彩限制。 |
| [2020 年 Payments 政策说明](https://android-developers.googleblog.com/2020/09/listening-to-developer-feedback-to.html) | 已打开，仅作历史背景。该文中的旧期限、当时费率和政策表述不是现行要求；当前规范以合并版政策及地区项目页为准。 |

订阅政策还链接到 [Create and manage subscriptions](https://support.google.com/googleplay/android-developer/answer/140504) 和 [Create an in-app product](https://support.google.com/googleplay/android-developer/answer/1153481)，后者另链接到 [Overview of one-time products](https://support.google.com/googleplay/android-developer/answer/16430488?hl=en)。Create/manage subscriptions 的正文链接到[Understanding subscriptions](https://support.google.com/googleplay/android-developer/answer/12154973)：它说明 Subscription、Base plan、Offer 对象模型及自动续订、预付、分期方案；其[近期变更文章](https://support.google.com/googleplay/android-developer/answer/12124625?hl=en)现已打开并摘要如下。设置指南还链接到[Tax and compliance settings](https://support.google.com/googleplay/android-developer/answer/10463498?hl=en)，其 EEA 消费者权益和税务分类摘要见本节第 5 部分。地区帮助链继续到上表中的动态 Play supported-locations 页面。帮助页 UI 步骤可能随 Console 变化，需按当前界面复核。

### Monetization and Ads 共享导航：目录与政策正文分开（核对日期：2026-10-23）

订阅 Help 页的数字导航顺序为 **1/4 Monetization and Ads → 2/4 Payments → 3/4 Ads → 4/4 Subscriptions（当前页）**。这是跨主题导航，不是四项订阅条款。打开 `Monetization and Ads` 目录后，其正文另列 **Payments、Ads、Subscriptions、Families Self-Certified Ads SDK Program** 四个直接入口；Families SDK 是目录正文的额外链接，不是数字导航序列中的第五项。以上目录、序列目标和 Families SDK 目标均已打开；页面内容与适用边界如下。

| Help 导航目标 | 内容与订阅政策的关系 |
| --- | --- |
| [Monetization and Ads 目录](https://support.google.com/googleplay/android-developer/topic/9857752?hl=en) | 介绍 Play 支持付费分发、应用内商品、订阅和广告等变现方式，并把四类 Help 主题列为导航。它是目录，不单独授予支付例外。 |
| [Payments 政策](https://support.google.com/googleplay/android-developer/answer/9858738?hl=en) | 规定数字商品/功能（含订阅）通常须使用 Google Play Billing，另设有限例外和地区项目；还要求价格与条款准确披露、应用内虚拟货币仅限本应用使用，并提前披露随机虚拟商品概率。它决定数字订阅的结算路径，不替代订阅的持续价值、续订披露和取消要求。 |
| [Ads 政策](https://support.google.com/googleplay/android-developer/answer/9857753?hl=en) | 广告属于应用内容，须符合内容分级、受限内容、家庭广告及用户体验规则；页面还涵盖欺骗/干扰式广告、Better Ads、位置数据和广告 ID。若订阅应用同时展示广告，这些是并行适用的广告要求，不是订阅项目的付款例外。 |
| [Subscriptions 政策](https://support.google.com/googleplay/android-developer/answer/9900533?hl=en) | 本页直接要求持续/重复价值，明确披露价格、周期、自动续订和试用转付费，并提供易用的在线管理/取消方式；Google Play Billing 订阅取消通常在当前周期末生效，但当地法律可能要求即时取消/按比例退款。 |
| [Families Self-Certified Ads SDK Program](https://support.google.com/googleplay/android-developer/answer/9900633?hl=en)（目录正文额外链接） | 页面显示当前暂停新申请、既有参与者要求不变。面向儿童展示广告时须使用相应自认证 SDK；混合年龄受众需用中立年龄筛查确保儿童只看到合规广告。具体计划条件、11 个正文链接和访问边界见 Families 自认证广告 SDK 专题，厂商版本及技术后代见儿童安全和 SDK 专题。 |

以上目录导航本身不新增政策义务。Payments 处理交易结算，Subscriptions 约束订阅商品与购买流程；Ads/Families 仅在应用展示广告或服务儿童受众时按各自范围叠加适用。各目标页的更深 API、账号表单和第三方 SDK 后代仍依来源审计中的独立状态管理，不把本次导航核验视为无限递归闭合。

### 近期订阅结构变更：旧版兼容与单向迁移

[Recent changes to subscriptions in Play Console](https://support.google.com/googleplay/android-developer/answer/12124625?hl=en)记录了自 2022 年起的订阅模型迁移：将 Subscription 与 Base plan/Offer 分离，支持预付方案、升级 offers 和自定义资格条件。文章称现有订阅会转换为 base plan 和兼容 offer；旧版应用/API可继续取到兼容视图，但无法使用全部新功能。若 Play Console 勾选“Make subscription editable”将旧商品迁移至新结构，迁移是单向的；之后旧 `inappproducts` API 不能再读取、配置或更新该订阅。迁移前应检查旧客户端、促销码、精选订阅及 Subscribe with Google 等兼容场景，并保留旧客户端依赖的兼容 offer，直到旧版本占比可接受。

文章还说明新国家/地区配置会影响未来上线市场，是否自动启用须核对商品的国家设置；旧 `inappproducts` API 仍可用于未迁移的商品，但不支持新的订阅能力。页面链接到订阅对象概览、Play Console 订阅管理、旧版 API、订阅迁移/集成指南和 Monetization Subscriptions API。本文摘要不表示该文章页面日期之后的所有 Console/API 变更均已覆盖，实施前应查现行 API 文档。

### EEA 分发“灵活性”：仅为指定合同条款豁免

[Flexibility for EEA app distribution](https://support.google.com/googleplay/android-developer/answer/16232690?hl=en)及其[先前合同变更说明](https://support.google.com/googleplay/answer/16125693?hl=en)描述的是《数字市场法案》（DMA）背景下的合同豁免。Google 向可能受最惠国/价格平价（MFN）条款约束的开发者发出豁免通知，豁免自 **2024-01-01** 起生效；只要开发者通过 Play 向 EEA 终端用户提供产品/服务，不以开发者营业地为限。豁免仅移除相关 MFN 条款，协议其余部分继续有效。通知细节通常只对收到通知的企业开放；Help 页面提供 play-bd-ops@google.com 联系方式。

该分支链接至欧盟委员会的 [Digital Markets Act 官方页面](https://digital-markets-act.ec.europa.eu/index_en)。DMA 解释和合同豁免不构成替代计费、External Offers、外部分发或其他 Play 项目的入组许可；这些计划各自仍有市场、资格、API、报告和费用条款。

### EEA External Offers 条款、费用与直接子链（核对日期：2026-10-23）

现行 [EEA External Offers 计划服务条款](https://support.google.com/googleplay/android-developer/answer/14539286?hl=en)的生效日为 **2025-10-28**，是 DDA 的补充条款；若二者就 External Offers 参与事项冲突，以该计划条款为准。条款不是费率表：§3 将费用指向现行 External Offers 页面，故须与[当前项目资格/费率页](https://support.google.com/googleplay/android-developer/answer/14372887?hl=en)和账号内账单合读。

| 条款主题 | 当前规则与实施含义 |
| --- | --- |
| 开发者与用户的交易关系 | 开发者直接与用户订约，是站外交易的 merchant of record；交易完成前须以清晰、醒目语言说明开发者（不是 Google）是商品/服务提供方及交易处理责任方，并说明交易税由谁承担。开发者独自负责客服、投诉和争议处理；项目要求提供退款方式，除非付款前已清楚告知不可退款。另有 EULA 时，它只在用户对商品/服务的权利范围内优先，不等于替代计划资格或其他项目义务。 |
| 账单、税务和凭证 | Google 尽商业上合理努力在每月结束后 15 天内开票；付款到期日为发票日起第 30 个日历日，逾期利息最高按月 1.5%（若法律上限更低则从其规定）。除[税务页面](https://support.google.com/googleplay/android-developer/answer/138000?hl=en)所列条件例外外，开发者须判定、收取、申报并缴纳交易税；服务费税务另计。代理关系或特定服务履行地点变化须至少提前 90 天书面通知；错误申报、分类或延迟披露会触发税务赔偿责任。 |
| 报告、审计和赔偿 | 申报资料与交易报告须持续真实、准确、完整且可支持，开发者对其站外交易全球适用法律负责。Google 可在条款期间及终止后一年审计相关账簿；收到请求后 30 天内提供最新 SOC 1 Type II（或后继）报告，或配合审计；服务费差异超过 5% 时开发者承担审计成本。开发者对因参与项目引发的第三方法律/监管程序承担约定的赔偿责任。 |
| 终止、改约和文本优先级 | 违约、失去良好账号状态或法律要求等可触发终止；Google 在允许时也可提前 30 天通知终止。开发者可通过条款列出的[退出联系表单](https://support.google.com/googleplay/android-developer/contact/alternative_billing_external_offers_q)退出，但本次点击未能读取表单，不能据此确认提交步骤。现有开发者改约通常至少提前 30 天通知，法律要求的变更可立即生效；不同意变更时，唯一约定救济为退出。条款与 DDA 的管辖法条款合用，英文版控制，翻译只供参考。 |

**费率口径须分层：** 当前 EOP 页面列出的费用自 **2026-06-04** 生效：初始获客费 0%；标准持续费为自动续订订阅 10%、其他数字优惠 20%、应用安装每次 €1.20（可定期调整）。新 Apps & Games 档列订阅 10%、其他数字优惠 15%；首 100 万美元年收入档列两类均 10%。后两个费率档的应用安装列未给出金额，不能按空白推断为零费或免收费。另一个[全球 lower service fees 说明](https://support.google.com/googleplay/android-developer/answer/16954621?hl=en)称其费用模型一般覆盖外部网页链接，但同页脚注又称该项目细节将于之后公布；不要把该一般表格的安装/新旧安装费率套到 EOP。适用地区、项目档位及最终应付金额应核对 EOP 专属页、最新 Terms、Console 入组状态和实际发票。

当前页链接的[2024-03-06 存档条款](https://support.google.com/googleplay/android-developer/answer/16604592?hl=en)含旧的 5%/10% 初始获客费、7%/17% 持续费及每月 1% 逾期利息，仅保留为历史版本，不能覆盖 2025-10-28 现行条款或 2026-06-04 现行费率。现行条款正文共核对 11 次链接引用、9 个去重目标：另含 [DDA](https://play.google.com/about/developer-distribution-agreement.html)、EEA 计划资格/地区页、[External Offers API 总览](https://developer.android.com/google/play/billing/external)、VAT、[Enforcement Process](https://support.google.com/googleplay/android-developer/answer/9899234?hl=en)、社区和联系入口。API 总览要求先满足项目入组与资格、使用 Billing Library 8.2.1+，每次外跳前展示用户信息屏，并指向[客户端集成](https://developer.android.com/google/play/billing/external/integration)、[后端报告](https://developer.android.com/google/play/billing/outside-gpb-backend)及[发布说明](https://developer.android.com/google/play/billing/release-notes)；这些技术指南解释如何实现，不替代入组审批。Terms 正文中的上下文社区 URL（`https://support.google.com/googleplay/android-developer/community?help_center_link=CJa09wYSNkRFVkVMT1BFUiBURVJNUyBPRiBTRVJWSUNFIEZPUiBFWFRFUk5BTCBPRkZFUlMgUFJPR1JBTQ&hl=en`）本次 Cache miss；通用社区首页另有独立访问记录。Contact us 跳到账号专属 Console 支持。API 总览还链接 [Android Developers Content License](https://developer.android.com/license)，已读并说明它只界定 Android 文档/代码样例许可，不授予复制 Play Help 政策原文的权利。帮助侧栏六个计费主题作为导航另行交叉索引，未混作正文链接。API 类型/示例、账号表单和更深后代仍部分覆盖，逐 URL 结果见来源台账和链接图 §4.74。

本专题递归覆盖 Payments/Subscriptions 政策直接正文与最相关的项目、FAQ、产品配置和购买安全子页。Google 帮助目录/footer、无关支付产品导航、Console 登录状态、所有国家法例及项目每一个 API 参考节点没有全部复制；访问受限页面保留链接，不把状态写成已读。项目和费率可能快速调整，账号内当前入组与账单具有最终操作效力。

## 来源与关联知识库

- [Google Play Payments policy](https://support.google.com/googleplay/android-developer/answer/9858738?hl=en) · [Policy FAQ](https://support.google.com/googleplay/android-developer/answer/10281818?hl=en)
- [Google Play Subscriptions policy](https://support.google.com/googleplay/android-developer/answer/9900533?hl=en)
- [Billing choice program](https://support.google.com/googleplay/android-developer/answer/17161464?hl=en) · [Lower service fees](https://support.google.com/googleplay/android-developer/answer/16954621?hl=en)
- [US External Content Links](https://support.google.com/googleplay/android-developer/answer/16470497?hl=en) · [Japan External Payments](https://support.google.com/googleplay/android-developer/answer/16787536?hl=en)
- [Google Play Billing integration guide](https://developer.android.com/google/play/billing/integrate)

相关知识库：[金融服务/贷款/EWA](../financial-services-and-loans/financial-services-and-loans.zh-CN.md)、[加密资产/NFT](../crypto-assets-and-nfts/crypto-assets-and-nfts.zh-CN.md)、年龄限制与儿童安全、[用户数据](../user-data/user-data.zh-CN.md)、[Data safety](../data-safety/data-safety.zh-CN.md)。本页为双语结构化摘要，不是政策全文；账号级项目资格、适用费率和地区法律须另行核实。
