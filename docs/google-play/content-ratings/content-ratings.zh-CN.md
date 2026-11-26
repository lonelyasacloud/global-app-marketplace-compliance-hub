---
id: google-play.content-ratings
platform: google-play
language: zh-CN
authority: operational
status: current
kb_checked_at: 2026-10-23
review_due: 2027-01-23
regions: [global]
topics: [content-ratings, target-audience, ads, iarc, families, store-listing]
snapshot_id: play.content-ratings
snapshot_package: "GooglePlay-KnowledgeBase-2026-10-24-review.zip"
coverage_status: "detailed-summary"
source_url: "https://support.google.com/googleplay/android-developer/answer/9859655?hl=en"
source_url_zh: "https://support.google.com/googleplay/android-developer/answer/9859655?hl=zh-CN"
---

# Google Play 内容分级、目标受众与广告适配

> **导入说明（Google batch 3）。** 本页正文取自 2026-10-24 Google Play 知识库快照里已经分开的对应语言改写（`play.content-ratings`，核对日 2026-10-23），不是官方页面的逐字文本。英文官方来源是效力来源。`kb_checked_at` 使用快照源文件记录的核对日；本次导入没有重新打开线上官方页面。文中“本知识库”“本库”“本地专题”描述的是该快照知识库的覆盖范围，不是本仓库已经导入的页面清单。快照里指向尚未导入本仓库的专题、链接图、台账或 CSV 的相对链接，已改为文字提及；指向 Google batch 1、batch 2 或本批九个专题的相对链接已改到本仓库路径。快照 YAML 的 `reviewed_on` 是 2026-10-23。英文开篇写核对日 2026-10-22，中文开篇写 2026-10-23。这两个快照日期不视为政策变更。该次复核中简体中文页面不可读取；本中文页是对英文来源的改写，不是已核对的中文官方页面。该访问失败不表示政策已经变更。分级规则没有记录未来生效的 Play 日期。政策摘要页上的 IARC 要求是 `normative`。问卷、目标受众和 Console 步骤是 operational，不替代 Families 规则、年龄限制或广告适配。

**核对日期：2026-10-23。** 本专题整理了 Play Console Help 的英文内容分级要求正文及其主要政策/执行链接。简体中文页面在本次访问中不可读取；中文内容为对英文来源的改写摘要。分级结果由各地区评级机构依据开发者问卷独立生成，不能用一个市场的标签代替所有市场，也不能把内容分级当作目标受众声明或年龄限制的替代品。

2017 年 8 月公告的“Content rating guidelines”直链当前落到 [Content Ratings 政策摘要页](https://support.google.com/googleplay/android-developer/answer/9898843?hl=en)。该页明确：所有上架应用都须有 IARC 内容分级；每个新应用与现有应用都要准确填写 Play Console 问卷，内容/功能变化影响答案时需重填；无评级应用可能被移除；应用内广告不得显著高于应用主体内容的成熟度。它还链接到[Ads 政策（其中含不当广告要求）](https://support.google.com/googleplay/android-developer/answer/9857753?hl=en)和[内容分级详细帮助页](https://support.google.com/googleplay/android-developer/answer/9859655?hl=en)。两页分别侧重政策概述和执行流程；冲突时以完整政策为准。 注意 `answer/9878810` 当前是“Inappropriate Content（不当内容）”，不是此摘要页所链接的广告政策目标。

## 先区分三个声明/控制

| 项目 | 作用 | 不能替代什么 |
| --- | --- | --- |
| 内容分级问卷 | 依据应用实际内容，为各地区生成当地熟悉的年龄/内容标签；用于搜索/浏览筛选、未成年人访问控制和部分项目资格判断。 | 不能代替目标年龄组声明、Families 要求、广告适配或当地法规。 |
| 目标受众与应用内容 | 声明应用实际为哪些年龄组设计；选择包含儿童的年龄组会触发 Families 规则、儿童广告 SDK/中性年龄屏幕等额外义务。 | 不能仅为扩大覆盖而勾选应用没有针对设计的年龄段。 |
| Restrict Minor Access / 年龄限制 | 对仅适合成人或政策要求设限的应用限制被识别为未成年人的用户查找、下载或购买；既有安装者仍可能继续使用，但不能续订或进行新购买。 | 不能用高内容分级标签自动实现；需在 Console 明确启用并满足相应政策。 |

## 何时需要填写或更新问卷

Play 要求新提交的应用、在 Play 上架但尚无分级的现有应用，以及会改变问卷答案的内容/功能更新，都完成内容分级问卷。开发者必须准确、完整地描述应用内容；虚假陈述可能导致更新被拒或应用被暂停。提交后，多个评级机构会按各自方法和地区标准给出结果。

基本流程：

1. 在 Play Console 打开 **Policy → App content**，进入“Target audience and content”，在内容分级部分开始问卷。
2. 填写用于 IARC 往来的邮箱，选择类别，并完整回答所有内容问题；分段可以保存草稿，每个应用同一时间只有一个草稿。
3. 检查 Summary 中计算出的各地区分级并提交；如回答有误，可编辑或启动新问卷。
4. 在 App content 页面查看问卷及已提交评级。更新内容或功能后，重新判断问卷答案是否需要变更。
5. 如对某评级机构的结果有异议，使用评级证书邮件中的链接直接申诉；其他 IARC 问题使用其联系渠道。

计算出的 Summary 分级可能不同于 Google Play 最终向用户展示的分级；机构可以在复核后覆盖结果。当地法律也可能要求为特定市场生成相应评级。分级图标属于各评级机构的商标，使用时须遵守其图标规范。

2025 年政策公告进一步澄清：分级问卷只评估应用本身的内容，不评估广告、附加用户协议或隐私做法；广告是否符合应用分级仍是独立的广告政策检查。见[2025-07-10 公告](https://support.google.com/googleplay/android-developer/answer/16296680?hl=zh-CN)及公告知识库摘要（快照：`../google-play-announcement-resources.md`，未导入本仓库）。

## 广告及广告优惠也必须匹配应用分级

应用里展示的广告及关联优惠都视作应用的一部分。它们必须符合应用自己的内容分级，即使应用本身符合政策也一样；例如广告推广下载另一款成熟级应用，也可能不适合当前应用的分级。

- 与广告服务商确认广告系列只展示适合当前分级的创意；使用 AdMob 时，配置最大广告内容分级和屏蔽控制。
- AdMob 允许设账号级或单应用最大分级；单应用设定覆盖账号级默认值，广告请求中的 SDK 设定又可能覆盖界面配置。分级是累积的，例如选到 T 也会允许低于 T 的级别。
- Families 应用有更严格上限：主要面向儿童的应用广告上限由系统设为 G；混合受众的上限最高为 PG。界面设置可能被覆盖，广告仍须由相应自我认证 SDK 提供。
- 若使用实时竞价，广告素材应在交付前经审查/评级，或只接入合格的自我认证来源。

关联政策见广告与推广专题（快照：`ads-and-advertising.md`，未导入本仓库）、[年龄限制与儿童安全专题](../age-restricted-child-safety/age-restricted-child-safety.zh-CN.md)及评分/评价/安装量专题（快照：`user-ratings-reviews-installs.md`，未导入本仓库）。

## 各地区评级体系：同一应用可能有不同结果

Google Play 页面列出不同地区的评级机构、游戏/应用适用范围和当地标签。机构按自己的标准独立判断，以下市场分配和标签以核对日的官方表格为准；目标市场与分级表可能随政策和当地法规变化。

| 评级机构/系统 | Play 帮助页列出的适用范围 | 页面中的常见标签/边界 |
| --- | --- | --- |
| ESRB | 美洲一组市场（包括美国、加拿大、墨西哥和中南美洲多个市场）。 | E、E10+、T、M、AO；评级分类之外还可能显示内容描述符和互动元素。 |
| PEGI | 欧洲和中东列出的一组国家/地区。 | PEGI 3、7、12、16、18；另有适用于可访问大量可变内容的“建议家长指导”标识。 |
| USK | 德国。 | USK 0、6、12、16、18。 |
| Australian Classification Board (ACB) | 澳大利亚；该页说明这套 ACB 分级仅用于游戏，其他应用落入其他国家/地区类别。 | G、PG、M、MA15+、R18+；年龄门槛与法律限制类别不同。 |
| ClassInd | 巴西。 | Livre/全年龄、6、10、12、14、16、18。 |
| GRAC | 韩国游戏；页面指出韩国应用另用 Google Play Rating。 | ALL、12、15、19。 |
| IARC 通用分级 | 没有由参与机构单独代表的其他地区。 | 3+、7+、12+、16+、18+。 |
| Google Play Rating | 韩国应用（不含游戏）及俄罗斯市场的单独评级表。 | 韩国应用列 3+、7+、12+、16+、19+；俄罗斯列 3+、7+、12+、16+、18+。 |

Google Play 页面还列出了 ESRB 和 PEGI 的适用国家清单：ESRB 覆盖安提瓜和巴布达、阿根廷、巴哈马、巴巴多斯、伯利兹、玻利维亚、加拿大、智利、哥伦比亚、哥斯达黎加、古巴、多米尼克、多米尼加共和国、厄瓜多尔、萨尔瓦多、格陵兰、格林纳达、危地马拉、圭亚那、海地、洪都拉斯、牙买加、墨西哥、尼加拉瓜、巴拿马、巴拉圭、秘鲁、圣基茨和尼维斯、圣卢西亚、圣文森特和格林纳丁斯、苏里南、特立尼达和多巴哥、美国、乌拉圭、委内瑞拉。PEGI 清单为阿尔巴尼亚、安道尔、奥地利、比利时、波斯尼亚和黑塞哥维那、保加利亚、克罗地亚、塞浦路斯、捷克、丹麦、爱沙尼亚、芬兰、法国、希腊、匈牙利、冰岛、爱尔兰、以色列、意大利、科索沃、拉脱维亚、列支敦士登、立陶宛、卢森堡、北马其顿、马耳他、摩尔多瓦、摩纳哥、黑山、荷兰、挪威、波兰、葡萄牙、罗马尼亚、圣马力诺、塞尔维亚、斯洛伐克、斯洛文尼亚、西班牙、瑞典、瑞士、土耳其、阿联酋、英国和梵蒂冈。

若评级机构在特定地区拒绝分级，该应用/游戏不得在该地区发行；Play Console 会显示“Refused Classification”，Google Play 只在相应地区移除该内容。申诉仍按 IARC 邮件提供的入口联系评级机构。

## 页面链接与目标页关系

原文开头目录的 10 项链接是指向本页不同章节的页内锚点；其余政策与执行目标按用途归纳如下。帮助中心图片、问卷示意图、通用反馈表单、全站导航和账户登录控件不当作政策条款。

| 直接目标 | 内容及与本页的关系 | 核验状态 |
| --- | --- | --- |
| [Content Ratings 政策摘要页](https://support.google.com/googleplay/android-developer/answer/9898843?hl=en) | 2017 年 8 月公告的直接目标。要求每个应用都有 IARC 分级、准确完成问卷并在内容变化时更新，且广告不得显著高于应用内容的成熟度。 | 正文已完整打开；IARC、广告政策和详细操作帮助目标已交叉核对。帮助中心侧栏的 5 个主题另作导航处理。 |
| [Target audience and app content settings](https://support.google.com/googleplay/android-developer/answer/9867159?hl=en) | 目标年龄组的选择、年龄适配、Families 触发、中性年龄屏幕、个人信息、广告 SDK、成人访问限制。 | 正文已打开；已有[年龄限制与儿童安全专题](../age-restricted-child-safety/age-restricted-child-safety.zh-CN.md)。 |
| [Families policy topic](https://support.google.com/googleplay/android-developer/topic/9877766?hl=en) | 含儿童目标受众时的 Families 要求。 | 本次 Help 请求超时；以已整理的 Families/儿童安全主题交叉参考。 |
| [Families Self-Certified Ads SDK program](https://support.google.com/googleplay/android-developer/answer/12955712?hl=en) | 列出可用于儿童广告的自我认证 SDK 与版本，并说明混合受众、中性年龄屏幕、开发者责任及名录变化。 | 正文已打开；页面说明暂停新申请，既有参加者要求不变，实时 SDK 版本表需发布前复查。 |
| [Ads policy](https://support.google.com/googleplay/android-developer/answer/9857753?hl=en) 与 [AdMob 最大广告分级设置](https://support.google.com/admob/answer/7562142?hl=en) | 前者规定广告内容、骚扰式/欺骗式广告及广告分级；后者说明账号/应用/广告请求的分级优先级、广告量影响和 Families 覆盖。 | 两页已打开；Play 广告要求另见广告专题（快照：`ads-and-advertising.md`，未导入本仓库）。 |
| [Developer Program Policy](https://play.google/developer-content-policy/) 与[开发者分发协议](https://play.google/developer-distribution-agreement.html) | 通用政策约束与合同条款；内容分级还须与当地法律一致。 | 两项已有双语知识库条目；此处保留源链接。 |
| [Prepare your app for review](https://support.google.com/googleplay/android-developer/answer/9859455?hl=en) 中的广告/隐私申报说明、[App access instructions](https://support.google.com/googleplay/android-developer/answer/9815348?hl=en) 与 [Play Console App content](https://play.google.com/console/app/app-content/summary) | 开始目标受众与内容申报前，需先处理是否含广告、应用访问说明和隐私政策；Console 页面是实际填报入口。 | Prepare 正文已打开并整理；App access 目标被自动化抓取页拦截；Console 入口跳转登录。 |
| [IARC 首页](https://www.globalratings.com/)、[Ratings Definitions](https://www.globalratings.com/ratings-definitions/) 与[联系方式](https://www.globalratings.com/contact-us/) | 首页导向流程、参与机构、平台、FAQ 和机构信息；Definitions 解释地区评级标签；Contact 提供一般咨询及各评级机构查询入口。 | 2026-10-23 重开三页。首页有六个主导航子页，另有 Definitions 与 Contact 两个实质链接；首页指标与 About 页口径不一致，不用于合规结论。Contact 表单说明提交的个人信息会传输至美国；九个地区机构链接及台湾法规分支见下文。 |
| [各评级机构网站](https://www.esrb.org/)、[Australian Classification](https://www.classification.gov.au/)、[PEGI](https://www.pegi.info/)、[USK](https://www.usk.de/iarc/)、[ClassInd](https://www.justica.gov.br/seus-direitos/classificacao)、[GRAC](https://www.grac.or.kr/english/) | 地方评级体系和官方分级解释。 | Play Help 直链点击：ESRB、ACB 已打开；PEGI 返回 503、USK 缓存未命中、旧 ClassInd URL 502、GRAC 被防火墙拦截。IARC 定义页的当前/相关机构链接状态另列如下。它们是外部评级机构资料，不是 Play 新增的开发者规则。 |
| [旧 IARC display guidelines 链接](https://www.globalratings.com/display.aspx) | 内容分级图标展示规则链接。 | 目标返回 404；不要将旧地址当作有效图标使用许可，需从评级机构当前规范确认。 |
| Play Academy（页面内视频链接） | 政策培训材料。 | 链接点击未解析出可读取的目标；不影响问卷、分级或广告政策义务。 |

### IARC Ratings Definitions 页面：比 Help 文章再深一层

IARC 定义页链接到以下九个评级机构网站。这里记录目标和可读取范围；机构网站自己的菜单、新闻、隐私条款及无关资源尚未递归镜像。

| IARC 目标 | 核验状态与关系 |
| --- | --- |
| [Australian Classification Board](https://www.classification.gov.au/) | 官方首页已打开；“What do the ratings mean?” 子页也已打开。Play Help 指明该体系用于澳大利亚游戏。 |
| [ClassInd 当前巴西司法部入口](https://www.gov.br/mj/pt-br/assuntos/seus-direitos/classificacao-1) | 官方部门门户已打开；本轮未抽取其评级标准。Play Help 原有 `justica.gov.br` 旧链接返回 502。 |
| [台湾 DGSC](https://www.gamerating.org.tw/) | 2026-10-23 重开后正文可读：台湾数位发展部数位产业署网站列出五级本地游戏分级，并有法规、级别评量和游戏查询入口。其本地法规/工具后代见下节；不等同 Play/IARC 的全球政策。 |
| [ESRB Ratings Guide](https://www.esrb.org/ratings-guide/) | 完整页面已打开，涵盖年龄类别、内容描述符、互动元素和评级摘要；用于解释 ESRB 标签，不新增 Play 义务。 |
| [沙特 Gmedia](https://gmedia.gov.sa/ar) | IARC 定义页列出 Gmedia 五个年龄标签和简要内容描述，并将“Read More”链接到此官方阿语首页；点击后正文为零行。英文[首页](https://gmedia.gov.sa/en)抓取仅见标题，[Age Classification](https://gmedia.gov.sa/en/age-classification)也无可读正文。下表是 IARC 的标签摘要，不是已核实的 Gmedia 完整规则。 |
| [韩国 GRAC](https://www.grac.or.kr/english/) | 目标可达，但防火墙阻止读取正文；标签仅根据 IARC/Play Help 摘要。 |
| [印度尼西亚 IGRS](https://igrs.id/) | 目标只返回页面标题，无可读正文；标签仅根据 IARC 定义页摘要。 |
| [PEGI](https://pegi.info/) | 现行站点已打开，可读取年龄分级和内容描述符；Play Help 的 `www.pegi.info` 直链在同次核验返回 503。 |
| [德国 USK](https://www.usk.de/iarc/) | Play Help 的 `/iarc/` 旧路径仍不可读；IARC Contact 另链 `www.usk.de/`，其规范主机首页及[USK 的 IARC 专页](https://usk.de/fuer-unternehmen/spiele-und-apps-pruefen-lassen/spiele-und-apps-im-iarc-system/)现可读。该专页称 Google Play 等联网游戏平台须展示评级，并说明德国 IARC 流程；这是德国本地分类法律/监管语境，不是新增的全球 Play 规则。后代见下节。 |

### 沙特 Gmedia 年龄标签：目前可读的是 IARC 摘要

IARC 的 [Ratings Definitions](https://www.globalratings.com/ratings-definitions/) 页面在 Gmedia 名下展示以下五个标签及内容示例。该页的“Read More”链接会跳到 [Gmedia 官方阿语首页](https://gmedia.gov.sa/ar)，但本轮打开后没有可读正文；英文 [Age Classification 页面](https://gmedia.gov.sa/en/age-classification)也只显示标题。因此，下表是对 IARC 页面阿语说明的转述，不代表已核验 Gmedia 的完整、现行法规或评分细则。

| IARC 页面所列标签 | IARC 对内容的概述（中文转述） |
| --- | --- |
| 3+ | 面向各年龄段；示例为体育游戏。可能出现适合儿童的卡通语境暴力。 |
| 7+ | 可能出现令人害怕的画面/声音、暗示性暴力，或角色以不现实方式经历暴力（例如死亡后消失）。 |
| 12+ | 可能出现恐怖音效/视觉效果，或轻微伤口细节。 |
| 16+ | 可能出现针对人类或拟人角色的写实暴力、被正面呈现或没有负面后果的犯罪行为，以及不当语言。 |
| 18+ | 可能出现极强暴力（例如细致呈现酷刑或肢解），并展示毒品、烟草或酒精使用。 |

**解读边界：** 这是帮助理解 IARC 所列沙特标签的摘要，不是对当地年龄限制、发行义务或 Gmedia 评分流程的法律结论；不要把它替代 Gmedia 现行官方标准，也不要将当地评级标准扩展成 Google Play 的全球政策要求。市场上线决策应再核验可读取的 Gmedia 官方规则和适用法律。

### IARC 官网的直接子页

Content Ratings Help 还链接 IARC 首页。2026-10-23 重开首页的六个主导航目标（How IARC Works、Participants、Storefronts、FAQ、About、Milestones），另打开 Ratings Definitions 与 Contact，共八个实质页面链接；首页另有一个 Watch Video 链接，点击返回 Internal Error，工具未暴露目标 URL。Storefronts 地区矩阵为图片，文本视图不可读。全站 Privacy/Cookie/Terms 页脚不属于 Google Play 分级政策；以下页面解释 IARC 流程，不新增 Play 义务。

| IARC 子页 | 摘要与后代状态 |
| --- | --- |
| [How IARC Works](https://globalratings.com/how-iarc-works/) | 单次问卷为各地区生成年龄分级、内容描述符和互动元素；评级机构可以在发布后更正，开发者可在其他参与平台复用 IARC 证书 ID。页面的跨站导航指向已登记的 FAQ、Participants、Storefronts、Definitions 和 Contact。 |
| [Participants](https://globalratings.com/participants/) | 列出九个参与评级机构及各自网站，已与上方 IARC Definitions 的九个后代目标合并核对。其巴西 ClassInd 链接指向 [classindportal.mj.gov.br](https://classindportal.mj.gov.br/home)，本次仅取得标题、无正文。 |
| [Storefronts](https://globalratings.com/storefronts/) | 页面列出参与平台和区域分级展示矩阵，但矩阵由图片构成，文本抓取无法读出平台/地区单元；表格内容未据此推断。 |
| [IARC FAQ](https://globalratings.com/faq/) | 2026-10-23 重开：问卷只能通过参与的数字商店/平台入口填写；目前对开发者免费，提交后即时生成各地评级；评级机构可能在发布后复核/修改。开发者可申请 rating check，说明希望调整的理由，并可能被要求提供证据；IARC 证书码通常可在另一家参与平台复用。FAQ 链接回到本专题已登记节点。 |
| [About IARC](https://globalratings.com/about/) | 介绍多机构共同建立问卷、地区化评级以及内容描述符/互动元素；没有新增开发者流程。 |
| [IARC Milestones](https://globalratings.com/milestones/) | 历史时间线记录 Google Play 于 2015 年开始接入 IARC、2023–2024 年新增台湾 DGSC/印尼 IGRS/沙特 Gmedia 等参与机构，并称 Gmedia 于 2026 年开始正式评级。属于机构历史，不是新的 Play 期限。 |

**申诉路径需区分：** Play Help 指示开发者使用评级证书邮件中的链接向相应 IARC 评级机构提出 appeal；IARC FAQ 将复核请求称为 rating check，并说可能要求理由或佐证。两者都指向评级机构处理，但资料没有证明正式申诉与一般 rating-check 流程完全相同；应按证书邮件和相应机构说明操作。IARC Contact 一般表单要求姓名、邮箱和问题内容，并说明提交的个人信息会传输至美国。本次未填写或发送表单。

**IARC 页面总量提示：** 首页与 About 页显示的受众/开发者/评级数量口径不一致；这些机构宣传统计不作为政策事实。

### IARC Contact → 台湾本地分级法规与评量工具

IARC Contact 页列出九个地区评级机构联系入口。九个目标均已逐一打开或记录访问限制；其中台湾 DGSC 站可继续通向法规索引和分级评量工具。这是台湾本地游戏分类法律与操作资料，不是 Google Play 全球政策，也不能代替 IARC/Play Console 问卷。

| 台湾后代页面 | 页面内容、访问状态与适用边界 |
| --- | --- |
| [台湾数位娱乐软件分级查询网](https://www.gamerating.org.tw/) | 2026-10-23 正文可读；页面概述台湾数位发展部数位产业署监督的游戏分级制度，并显示“普、护、辅12、辅15、限”五级。该本地分类须与 Google Play 页面展示的 IARC 地区评级分开记录。 |
| [关于我们](https://www.gamerating.org.tw/Page?itemid=10&mid=5) | 说明本地制度法律依据及网站用途：业者登记游戏评级与情节，公众查询或检举；沉浸式体验场域也纳入本地分级管理。 |
| [法规政策与公告索引](https://www.gamerating.org.tw/Message?itemid=1&mid=6) | 索引显示 502 条记录，并列出 2019 年《游戏软件分级管理办法》及 2026 年公告。本次没有逐页审查全部 502 条。 |
| [分级级别评量说明](https://www.gamerating.org.tw/Assess?itemid=2&mid=21) 与[交互式评量表](https://www.gamerating.org.tw/Assess/Type?itemid=2&mid=21) | 工具称其结果为参考建议；输入页列性、暴力、恐怖、烟酒、毒品、不当言语、反社会、棋奕、牌类/益智娱乐、恋爱交友等类别。本次只看公开表单，未作答/提交；不推断登记结果或官方决定。 |
| [台湾《游戏软件分级管理办法》文本](https://www.gamerating.org.tw/Message/MessageView?GroupName=%E6%B3%95%E4%BB%A4%E8%A6%8F%E7%AB%A0&itemid=1936&mid=6&page=0) | 网站收录版本标注 2019-05-23；列五个法定年龄级别，并规定上市前分级/登记、游戏说明/下载/起始页标示、情节与警语、广告显示级别及限制级接触防护。这是台湾本地法规，不是全球 Play 规则；法律适用需按当前官方法令核对。 |
| [游戏软件分级参照表短链](https://reurl.cc/024E6A) | 点击后只显示短链站中间页，未给出最终目标或可读表格；不推断参照表内容。 |

九个评级机构入口及访问限制见上方 IARC 机构表和 `source-page-audit.csv`。

### IARC 联系页 → 德国 USK 的 IARC 流程、标签与本地法律

IARC Contact 的 USK 入口先到 USK 首页；首页的企业入口进一步区分实体零售、一般在线发行和接入 IARC 的商店。USK 的 IARC 专页说明：IARC 问卷在参与商店发布流程中填写，并按各地区规则生成标签；该页将 Google Play 列为参与平台之一。页面另称德国 2021 年《青少年保护法》修订后，大型游戏平台有年龄标识义务，USK 的 IARC 在线评级获德国州青年部门于 2025 年 4 月认可。此为 USK 对德国法制的说明，不能推广成 Google Play 全球要求。

| USK 后代目标 | 摘要、关系与访问限制 |
| --- | --- |
| [USK 游戏与应用 IARC 流程](https://usk.de/fuer-unternehmen/spiele-und-apps-pruefen-lassen/spiele-und-apps-im-iarc-system/) | 正文可读。流程为在接入商店提交应用、填写 IARC 问卷、由矩阵生成地区评级；同时披露聊天/购买等在线风险提示。它解释德国 USK 如何参与 IARC，不替代 Play 问卷。页面还区分面向线上游戏/应用的 JMStV 依据与实体零售游戏的 JuSchG 程序。 |
| [USK 年龄标识与内容/使用提示](https://usk.de/die-usk-alterskennzeichen/) | 正文可读，解释年龄级别、分级原因和使用提示。使用提示涉及购买/随机物品、聊天、位置共享、网络访问；内容提示含暴力、恐怖、性、语言、物质、广告和购买压力等。可以帮助识别需进一步核对的 Play 专题，但 USK 分类词不能直接等同 Play 的问卷答案或政策判定。 |
| [USK 分级原则与法律资料索引](https://usk.de/die-usk/grundlagen-und-struktur/grundlagen/) | 页面区分 USK 审查原则、JuSchG 下的流程及线上游戏/应用适用的 JMStV 补充原则，并提供法令/原则 PDF。页面的两个法律 PDF 链接触发不支持的二进制抓取，本次没有读取或复述 PDF 条文。 |
| [USK 年龄标识词条目录](https://usk.de/alle-lexikonbegriffe/category/usk-alterskennzeichen/) | 正文目录可读，列 USK 0、6、12、16、18 五种本地年龄标识，跳转到逐级词条；此处只核对目录，未逐篇抓取每个词条。 |
| [USK 游戏与应用申请入口](https://usk.de/fuer-unternehmen/spiele-und-apps-pruefen-lassen/) | 企业入口正文可读，分别指向标准审查、IARC 游戏应用、其他在线发行、费用、申请表和标识图稿等流程；费用、申请及图稿的全部后代未在本轮展开。 |

**边界：** USK 关于德国在线平台义务的说明与台湾本地分级法规均作为地区法律背景独立归档；它们不是 IARC 或 Google Play 的全球规则。两个法令 PDF、USK 全部分级词条及企业申请/费用/标识后代仍未闭合，访问状态逐项记录在来源审计表。

## 帮助中心侧栏：商店展示相关导航

内容分级页面的侧栏共有 7 个主题项（含本页，另 6 个相关项目），以及父级[Manage your store listings](https://support.google.com/googleplay/android-developer/topic/3450987?hl=en)主题索引。六个相邻帮助主题是[分类与标签](https://support.google.com/googleplay/android-developer/answer/9859673?hl=en)、[展示应用预览素材](https://support.google.com/googleplay/android-developer/answer/9866151?hl=en)、[自定义商店详情](https://support.google.com/googleplay/android-developer/answer/9867158?hl=en)、[商店详情最佳实践](https://support.google.com/googleplay/android-developer/answer/13393723?hl=en)、[目标受众设置](https://support.google.com/googleplay/android-developer/answer/9867159?hl=en)和[在 Play Console 管理 Play Shorts](https://support.google.com/googleplay/android-developer/answer/17165227?hl=en)。前五个已有知识库摘要；Play Shorts 页面已打开，说明自 2026 年 6 月起视频改由 Play Console 上传、目前仅对部分合作伙伴且只在美国展示，并分开跟踪文件处理状态与政策/质量审核状态。撤下视频可能延迟 2–3 天生效。Play Shorts 是运营/素材流程，不是内容分级规则。

AdMob 最大分级文章正文还链接至[通过 AdMob 遵守 Families](https://support.google.com/admob/answer/6223431)和[广告请求的年龄处理标签](https://support.google.com/admob/answer/6219315)。两页均已打开：前者包含儿童受众与混合受众的请求示例，但其中较旧的 TFCD 代码应对照现行 TFAT 指南核实；后者说明 TFCD/TFUA 已弃用，并介绍 CHILD、TEEN、UNSPECIFIED 处理方式。这些属于实现指导。AdMob 页的“More about apps”侧栏有 6 项（含当前页），相关条目包括上述两篇和 Content mapping；其他 AdMob 帮助后代尚未全部登记。

本地关联条目：商店详情与素材最佳实践（快照：`store-listing-best-practices.md`，未导入本仓库） · 用户评分/评价/安装量政策（快照：`user-ratings-reviews-installs.md`，未导入本仓库） · 广告与推广（快照：`ads-and-advertising.md`，未导入本仓库） · [年龄限制与儿童安全](../age-restricted-child-safety/age-restricted-child-safety.zh-CN.md)。

本专题是基于官方页面的双语改写，不逐字复制全部地区评级描述。地区分级映射、图标商标、目标受众和广告合规均需在目标市场发布前对照官方现行页面及 Play Console 核实。
