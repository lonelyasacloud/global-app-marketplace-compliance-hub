---
id: google-play.real-money-gambling
platform: google-play
language: zh-CN
authority: normative
status: current
kb_checked_at: 2026-10-23
review_due: 2027-01-23
regions: [global]
topics: [gambling, licensing, age-rating, daily-fantasy-sports, contests]
snapshot_id: play.real-money-gambling
snapshot_package: "GooglePlay-KnowledgeBase-2026-10-24-review.zip"
coverage_status: "detailed-summary"
source_url: "https://support.google.com/googleplay/android-developer/answer/9877032?hl=en"
source_url_application: "https://support.google.com/googleplay/android-developer/contact/gambling"
source_url_dfs_application: "https://support.google.com/googleplay/android-developer/contact/dfsform"
source_url_country_allowances: "https://support.google.com/googleplay/android-developer/answer/12256011?hl=en"
source_url_common_violations: "https://support.google.com/googleplay/android-developer/answer/13381106?hl=en"
source_url_zh: "https://support.google.com/googleplay/android-developer/answer/9877032?hl=zh-CN"
effective_date: "current policy; ended pilots are historical; no 2027-01-27 on this page"
---

# Google Play 真钱赌博、游戏与竞赛

> **导入说明（Google batch 6）。** 正文来自已经分开的 2026-10-24 Google Play 知识库快照（`play.real-money-gambling`，核对日 2026-10-23）的改写摘要，不是官方页面的逐字副本。英文官方页面是效力来源。`kb_checked_at` 是快照源文件记录的核对日；本次导入没有重新打开线上官方页面。文中“本知识库”“本库”“本地专题”等说法描述的是该快照库的覆盖范围，不是本仓库已经导入的页面。指向本仓库没有收录的专题、链接图、台账或 CSV 的相对链接改为文字提及。指向 Google batch 1–5 或本批九个专题的相对链接改为本仓库文件。快照 YAML 的 `reviewed_on` 是 2026-10-23。政策结构一段写核对日为 2026-10-22。常见违规文章于 2026-10-23 打开。这些快照日期不是政策变更。中文源文件把政策地址记为 `hl=zh-CN`。其中的地区许可表和常见违规地址是 `hl=en`。快照没有记录 `hl=zh-CN` 抓取失败，也没有记录中英文逐行对照。本仓库中文正文是快照的编辑改写。已经结束的试点是历史材料，不是现行上架例外：印度 DFS/Rummy 宽限期于 2026-01-22 结束，墨西哥 DFS 试点于 2026-06-04 结束，2026-06-04 生效的真钱游戏试点概览写明当时没有活跃试点，日本在线抓娃娃试点于 2023-07-11 结束。本页没有记录 2027-01-27。赌博政策是 `normative`。常见违规文章是 operational 审核清单。地区许可和牌照不是全球 Play 许可。预测市场试点入组是另一项计划。**

## 规则结构

官方[真钱赌博、游戏与竞赛政策](https://support.google.com/googleplay/android-developer/answer/9877032?hl=en)通常禁止促成真钱投注/赌博的应用；只有在 Google Play 支持的国家/地区、产品类型和项目流程内，完成申请并通过审核的合资格应用才可例外分发。该专题核对日期：2026-10-22。许可国家、州/省、产品类别和项目随时间变化；本页附有 2026-10-22 的地区范围快照，具体资格仍以当前政策、申请表动态选项和当地许可证为准。

## 获准真钱赌博应用的主要条件

| 领域 | 要求 |
| --- | --- |
| 产品与地区 | 仅限政策列出的在线赌场、体育博彩、赛马、彩票、Daily Fantasy Sports 等适用类别；当地法律允许且 Google Play 支持该国家/地区和产品。 |
| Play 审批 | 先提交相应赌博应用申请并获批；每个应用、市场/州和类别遵循当前申请表要求。所有权、许可或分发市场变化时可能需要重新认证。申请表称认证和审核通常至少一周或更久。 |
| 许可证 | 开发者须持有相应国家/州/地区和产品的有效运营许可，且应用不得超出许可范围。 |
| 未成年人及地理屏蔽 | 应阻止未成年人使用，并阻止许可范围之外的地区访问或参与。 |
| 价格与支付 | 允许的真钱赌博应用必须免费下载安装，不得作为 Play 付费应用出售，也不得使用 Google Play Billing 购买赌博服务。 |
| 分级与责任信息 | 应取得 AO（Adults Only）或 IARC 等效内容分级，并在应用及商店详情清楚展示负责任赌博信息。 |
| 其他规则 | 同时遵守所有适用法律、行业标准、开发者计划政策和当地广告限制。绕过认证或严重/重复违规可能导致整个应用被移除。 |

不符合真钱赌博例外的应用，不得让用户用真钱（含用真钱购买的应用内商品）投注/下注或参与以现实货币或现实价值奖品为结果的游戏、竞赛或锦标赛。导航入口、WebView、按钮或“立即下注/注册”等行动号召也可能构成促成行为。

## 赌博广告、忠诚计划与 DFS

- **赌博广告：** 只有达到政策全部条件的应用才可展示赌博/真钱游戏广告。广告、广告主和展示地点须符合当地法律与许可；不得向已知未满 18 岁用户展示，应用不得加入 Designed for Families 或面向未成年人；还禁止模拟赌博内容、赌博辅助/伴侣功能及在应用内容中导流到赌博服务。合资格赌博应用和 DFS 应用还须满足政策规定的例外条件。
- **游戏化忠诚计划：** 奖励须从属于一笔真实、独立的商品/服务交易，不能把交易的一部分变成入场费/赌注或以高于正常价格的交易购买参与机会。游戏应用只能用固定比例/进度发放相关奖励，不能由游戏表现或概率玩法放大；非游戏应用的机会型奖励须满足官方规则、中奖人数/期限/奖品日期及概率或选择方法披露要求。
- **Daily Fantasy Sports (DFS)：** 另有申请流程，且美国与其他市场适用的资格路径不同；当地许可、未成年人限制、免费下载安装、不使用 Play Billing、AO/IARC 分级和负责任游戏信息等条件仍适用。
- **试点项目：** Google 可能在部分地区开设限时项目，但现行[试点概览](https://support.google.com/googleplay/android-developer/answer/12918670)称**目前没有活跃试点**（页面生效日 2026-06-04；2026-10-23 复核）。历史试点结束和过渡日期见下表；旧试点不构成当前参与授权。
- **预测市场试点：** 与持有真钱赌博/游戏牌照的路线分开；预测市场试点当前仅列美国金融或等效牌照，截止日期和实时资格见[预测市场专题](../prediction-market-pilot/prediction-market-pilot.zh-CN.md)。

### 历史真钱游戏试点的当前状态

| 试点 | 官方当前状态 | 现在的含义 |
| --- | --- | --- |
| 日本在线抓娃娃 | 试点于 2023-07-11 结束；2023-07-12 起有独立声明流程。 | 需接受并提交声明表、保持 Play 账号良好状态；新应用须等声明获批后才能发布。仍须遵守当地法律和现行条款。 |
| 印度 DFS/Rummy | 试点于 2023-09-28 结束，过渡期于 2026-01-22 结束。 | 旧试点应用若要继续在印度上架，必须移除真钱功能并遵守[真钱赌博政策](https://support.google.com/googleplay/android-developer/answer/9877032)。旧公告不是持续有效的发行例外。 |
| 墨西哥 DFS | 试点于 2026-06-04 结束。 | [国家/地区许可表](https://support.google.com/googleplay/android-developer/answer/12256011?hl=en)另列墨西哥的线上赌场、体育博彩和彩票，仍须遵守总政策、当地牌照和 Play 审核。这些常规政策类别不等同仍在进行的试点。 |

当前概览明确称没有活跃试点。作地区决策前应查看实时概览和国家许可表；历史试点记录不会产生现行资格。

### 赌博应用常见审查失败与最佳实践

官方 [Common violations for gambling apps](https://support.google.com/googleplay/android-developer/answer/13381106?hl=en) 帮助页于 2026-10-23 全文打开。它是审核问题清单，不是独立政策；每项仍以真钱赌博政策、国家/地区许可表及适用法律为准。它列出以下十类常见问题：

1. **发布前置条件不全：** 每个分发国家/州/地区都要有有效赌博牌照；按实填写赌博应用申请表；取得 AO 或 IARC 等效分级。
2. **牌照类别不匹配：** 实际提供的赌博产品必须落在牌照授权范围内。
3. **地理围栏不足：** 不仅阻止未获准地区的新注册，也要阻止已有账号在该地区访问或使用相关功能。
4. **年龄门槛不足：** 阻止未成年人注册和使用应用。
5. **缺少责任博彩信息：** 应用内要清楚展示责任博彩声明，并提供指向外部求助资源的链接。页面举例建议按国家/地区替换联系信息；**最佳实践**是在应用页脚或顶层菜单放置声明，确保用户容易找到。
6. **审核轨道错误：** 赌博应用须提交到 production 轨道供审核，不能仅上传到测试轨道。
7. **应用不可用或不完整：** 应能加载并提供商店宣传的功能；不完整、不稳定或功能失效的版本应先修复再送审。
8. **违反评分、评价和安装规则：** 商店说明不得以安装奖励作为卖点，不能以金钱等价物换安装；标题、图标和开发者名称不得宣称 Play 商店表现/排名，也不得暗示与既有 Google Play 项目的关系。
9. **违反付款政策：** 不得将赌博应用作为 Play 付费应用售卖，也不得使用 Google Play Billing。
10. **把旧应用改造成真钱赌博应用：** 曾以低于 AO 的分级发布的应用，不可通过更新加入真钱赌博功能；须以新应用和新包名提交。用户仍可能重装旧应用，因此不能把旧应用改名或隐藏当作替代。

| 该审核清单的正文直链 | 在清单中的作用 | 目标页与本地状态 |
| --- | --- | --- |
| [真钱赌博、游戏与竞赛政策](https://support.google.com/googleplay/android-developer/answer/9877032) | 控制许可、产品范围、地理/年龄限制、分发与责任信息的主规则。 | 正文已打开并由本专题详细总结。 |
| [赌博应用国家/地区许可表](https://support.google.com/googleplay/android-developer/answer/12256011) | 核对每个市场和产品类别是否可申请，以及地区性例外。 | 英文正文已打开；含 45 个市场和 53 个正文目标的访问记录，动态资源表见上方快照。 |
| [Gambling Application Form](https://support.google.com/googleplay/android-developer/contact/gambling) | 提交应用、市场、牌照与资格资料的申请入口。 | 动态表单已打开、字段及市场范围已读；未填写或提交。 |
| [IARC 内容评级](https://www.globalratings.com/) | “IARC equivalent”评级体系入口；符合条件的赌博应用仍须达到 AO 或等效分级。 | 外部入口已登记；Play [Content Ratings 帮助页](https://support.google.com/googleplay/android-developer/answer/9898843)另有专题摘要，IARC 网站内部流程未递归展开。 |
| [User ratings, reviews and installs](https://support.google.com/googleplay/android-developer/answer/9898684) | 支持安装奖励、商店表现/排名和项目关系标示相关的审核判断。 | 正文已打开并有[评分、评价与安装量](../user-ratings-reviews-installs/user-ratings-reviews-installs.zh-CN.md)；这是本文提到的相关政策链接。 |
| [Understanding Google Play’s Payments policy](https://support.google.com/googleplay/android-developer/answer/10281818) | 支持付费应用与 Play Billing 禁止条件的解释。 | 正文已打开并有[付款政策专题](../payments/payments-and-subscriptions.zh-CN.md)；赌博支付限制仍以上述专门赌博条款为准。 |

此清单的“helpful links”旁栏又指回[Manage policy violations 目录](https://support.google.com/googleplay/android-developer/topic/3453554?hl=en)，并有帮助社区/联系入口；目录里的 11 个目标见[执行处置专题](../enforcement-and-appeals/enforcement-and-appeals.zh-CN.md)。不把旁栏、社区和账号专属联系流程误记为该审核清单的政策正文。

## 正文直接链接和关键后代

| 目标 | 与主政策的关系 | 状态 |
| --- | --- | --- |
| [Gambling Application Form](https://support.google.com/googleplay/android-developer/contact/gambling) | 申请真钱赌博应用的 Play 认证；当前表单列出 45 个市场，并按应用、市场/州和产品类别申请，需提供许可主体与证明。 | 表单正文已打开；市场表动态更新，未提交申请。 |
| [Daily Fantasy Sports Application Form](https://support.google.com/googleplay/android-developer/contact/dfsform) | 美国 DFS 独立认证；需州/地区牌照或登记证明、应用包名、许可主体关系和牌照日期；每表最多 20 个州。 | 正文及 DFS 条款区已打开；实际提交和账号资格未验证。 |
| [IARC 内容评级](https://www.globalratings.com/) | 申请提交前须达到 AO 或等效分级。 | 目标已登记；Play 的 [Content Ratings](https://support.google.com/googleplay/android-developer/answer/9898843)正文已读，IARC 外部流程未在本轮展开。 |
| [Country/region allowances](https://support.google.com/googleplay/android-developer/answer/12256011?hl=en) | 45 个市场的产品范围、州/省例外及本地责任博彩资源示例；附 2026-10-22 离线快照。 | 英文正文已打开；53 个正文目标逐项尝试，产品和资源状态见下节；地区表仍需在线复核。 |
| [Real-money gaming pilot overview](https://support.google.com/googleplay/android-developer/answer/12918670) | 正文称没有活跃试点；印度 DFS/Rummy 过渡期于 2026-01-22 结束，墨西哥 DFS 于 2026-06-04 结束。 | 正文和三个不同政策目标已打开；见上方日期状态表。侧栏另行统计。 |
| [Online Crane Games](https://support.google.com/googleplay/android-developer/answer/12002615) | 日本在线抓娃娃历史试点说明。 | 已打开；试点已于 2023-07-11 结束。 |
| [Online Crane Games declaration form](https://support.google.com/googleplay/android-developer/contact/ocgform) | 在线抓娃娃在全球分发（受当地法律约束）的声明和准入流程。 | 表单正文及关键直链已打开；未填写或提交。主要资格、运营条件和直链见下节。 |
| [Ads policy](https://support.google.com/googleplay/android-developer/answer/9857753) 与其 Deceptive Ads 规则 | 赌博广告仍须遵守 Play 广告内容、年龄和反欺骗要求。 | Ads 正文已读；参见[广告专题](../ads-and-advertising/ads-and-advertising.zh-CN.md)。 |
| [Android WebView API](https://developer.android.com/reference/android/webkit/WebView) | 赌博政策把嵌入 WebView 的导流行为列为可能违规示例。 | 技术 API 参考已打开；属于实现资料而非赌博准入政策。 |
| [Real-Money Gaming pilots](https://support.google.com/googleplay/android-developer/answer/12918670) 的限时项目子页与[地区许可表] | 确定产品、市场和法律例外。 | 地区/许可状态可能变化；应以当前赌博申请表和相应监管机构为准。 |

### 在线抓娃娃声明及其直接链接

Play 将在线抓娃娃（OCG）定义为：用户通过手机或电脑远程操作运营方在实体场所布置的实体抓娃娃机。日本限时试点虽然已结束，声明页仍要求开发者在遵守当地法律的前提下完成该流程，不能把“试点结束”理解成声明流程也结束。2026-10-23 从 Google Play programs 目录重新打开了该页和声明表；现行试点概览同日确认目前没有活跃的真钱游戏试点。

声明页（2023-07-12 起生效）要求由有权代表提交人填写并接受条款，开发者账号须保持良好状态；Google 表示在收到完整材料后通常于五个工作日内通知审核结果。必填信息包括代表人姓名、联系邮箱、Play 开发者账号名称、Console 登录邮箱、包名、应用名称；如适用，还包括运营代理、公司名称/成立日期及日本法人编号。新应用须等声明获接受后方可发布；现有应用需按要求更新 Console 设置。未提交或不完整的声明可能导致无法分发或移除。

核心运营承诺包括：

- 在 Play Console 将应用分类为 Game；有效核验用户年龄，并设置适龄消费限额及超限提示。
- 收款仅用于娱乐/游戏，不得作为赌注、下注或赢取有现实货币价值奖品的对价；奖品须符合法律和当地抓娃娃机常见价值限额，且不得转售或促成第三方转售。
- 提供有效申诉/救济与客服；不得暗中降低玩家获奖机会；广告不得误述玩法或获奖可能性。
- 遵守全部 Play 政策（含 Payments）、DDA 和声明条款；提交信息须真实、准确、完整。若信息变化、发生相关诉讼/监管调查或受到监管裁定，应立即书面告知 Google。
- Google 可因违反条款、法律要求、账号状态或风险等原因暂停/终止上架，也保留按国家/地区或全球停止允许 OCG 的权利。

| 表单中的链接 | 页面用途及关系 | 访问/处理状态 |
| --- | --- | --- |
| [日本法人编号说明（日本国税厅）](https://www.houjin-bangou.nta.go.jp/en/setsumei/) | 表单要求日本分发者填写法人编号。国税厅说明该编号为 13 位；企业/组织可通过官网检索名称、地址和编号，也提供 Web API 与批量下载。它解释字段，不是 Play 审批规则。 | 官方说明页已打开。 |
| [Google Play Developer Policy Center](https://play.google.com/developer-content-policy/) | 表单将遵守开发者政策作为资格条件；政策中心汇总内容、用户数据、权限、支付、广告、商店展示、执行等政策。 | 已打开当前政策中心；具体条款按各专题页核验。 |
| [Developer Distribution Agreement](https://play.google/developer-distribution-agreement.html) | 声明将 DDA 纳入条款。尤其关联 §4.7 客服责任、准确支持联系信息以及付费/应用内交易的响应时限。 | 当前 DDA 已有双语专题；本次交叉核验。 |
| [类别和标签说明](https://support.google.com/googleplay/android-developer/answer/9859673?hl=en) | 表单要求把 OCG 设为 Game；帮助页说明分类/标签用于发现，标签须对陌生用户明显相关，最多五项，重大功能/内容变化后应复核。 | 正文已打开，已有商店展示专题。 |
| [Play Developer Account](https://play.google.com/console/u/0/signup)；[Google Play 商店](https://play.google.com/store/games)；[Developer Console](https://play.google.com/console/u/0/developers/app/app-dashboard) | 帮助申请人创建/登录开发者账号并定位包名。商店链接展示消费者应用页；账号和 Console 链接需 Google 登录。 | 商店页已打开；账号注册和 Console 均受登录门槛限制，账号内页面不可公开核验。 |
| [Google 隐私政策](https://policies.google.com/privacy?hl=en)；[Google 服务条款](https://policies.google.com/terms?hl=en) | 表单页脚的支持/账号信息处理说明链接；属于 Google 的通用隐私和服务条款，不是 OCG 的开发者资格条款，也不能代替应用隐私政策。 | 两页已有逐 URL 审计；表单没有提交。 |

表单页面还说明，申请数据和支持沟通可能用于支持质量、培训、技术问题处理及产品改进，聊天/邮件可能使用翻译服务。表单抓取结果出现“Your email has been sent”的动态界面文字，但本次没有填写或点击提交；这不是本次实际提交的证据。

## 地区许可快照与直接链接核验（2026-10-22）

官方[国家/地区许可帮助页](https://support.google.com/googleplay/android-developer/answer/12256011?hl=en)列出 45 个市场。下表是该日英文帮助页中产品范围的离线快照，用于检索，不代表开发者已获当地许可或 Play 认证；州/省、许可证和申请表选项会变化，发布前必须回查当前表单。

**每款真钱赌博应用都必须在商店详情描述和应用内同时展示负责任赌博声明，并包含本地第三方问题赌博求助资源的联系方式**；还须遵守当地对声明内容和许可的要求。Google 列出的机构只是示例，不代表 Google Play 认证或背书。

产品缩写：C=线上赌场；S=体育博彩；H=赛马；L=彩票；DFS=每日梦幻体育。除表内注明外，H 通常要求与体育博彩分开监管，DFS 只在当地法律及 Play 资格允许时适用。

| 国家/地区 | 该页列出的可分发产品（快照） | 例示的本地责任博彩资源与直达核验状态 |
| --- | --- | --- |
| 澳大利亚 | 澳大利亚：体育博彩（DFS 仅在当地法律允许时）和彩票。 | [Gambling Help Online](https://www.gamblinghelponline.org.au/)（HTTP 403）；[Gamblers Anonymous Australia](https://gaaustralia.org.au/)（超时） |
| 奥地利 | 奥地利：线上赌场、体育博彩、单独监管的赛马；彩票仅政府运营方。 | [Federal Ministry of Finance: player protection](https://www.bmf.gv.at/themen/gluecksspiel-spielerschutz/spielerschutz-hilfsangebote.html)（已打开目标页） |
| 比利时 | 比利时：线上赌场、体育博彩；彩票仅政府运营方。 | [Gokhulp](https://gokhulp.be/begeleiding)（已打开目标页）；[Joueurs Aide-en-Ligne](https://joueurs.aide-en-ligne.be/)（已打开目标页） |
| 巴西 | 巴西：赛马；彩票仅限 Caixa Econômica Federal 发布的获批应用。 | [Gamblers Anonymous Brazil](https://www.gamblersanonymous.org/ga/addresses)（HTTP 404：目标未找到） |
| 保加利亚 | 保加利亚：线上赌场、体育博彩（DFS 仅限当地法律允许）、单独监管的赛马和彩票。 | [Solidarnost Association](https://www.solidarnost-bg.org/)（已重定向并打开） |
| 加拿大 | 加拿大：安大略省外（不含阿尔伯塔）赌场、体育博彩和彩票仅政府运营方；安大略省允许赌场/体育博彩，彩票仅政府运营方；阿尔伯塔允许赌场/体育博彩。 | [National Problem Gambling Helpline](https://www.ncpgambling.org/help-treatment/about-the-national-problem-gambling-helpline/)（已重定向并打开）；[Canada Safety Council](https://canadasafetycouncil.org/gambling-addiction/)（已打开目标页） |
| 哥伦比亚 | 哥伦比亚：线上赌场、体育博彩；彩票仅政府运营方。 | [Jugadores Anónimos Colombia](https://jugadoresanonimoscolombia.org/)（已打开目标页） |
| 克罗地亚 | 克罗地亚：线上赌场、体育博彩和彩票。 | [Andrija Štampar Public Health Institute](https://stampar.hr/hr/novosti/kada-zabava-prelazi-u-ovisnost-kockanje-i-kladenje)（已打开目标页） |
| 捷克 | 捷克：线上赌场、体育博彩、单独监管的赛马和彩票。 | [Anonymní Gambleři Česko](https://www.anonymnigambleri.cz/)（缓存未命中，正文未获取） |
| 丹麦 | 丹麦：线上赌场、体育博彩和彩票。 | [Spillemyndigheden treatment search](https://spillemyndigheden.dk/borgere-og-spillere/soeg-behandling)（已重定向并打开） |
| 埃塞俄比亚 | 埃塞俄比亚：线上赌场和彩票。 | [Amanuel Mental Specialized Hospital](https://amsh.gov.et/)（仅返回页面标题，未获取正文） |
| 芬兰 | 芬兰：线上赌场、体育博彩和彩票均限政府运营方。 | [Peluuri](https://www.peluuri.fi/)（已打开目标页） |
| 法国 | 法国：线上赌场、体育博彩、单独监管的赛马；彩票仅政府运营方。 | [Joueurs Info Service](https://www.joueurs-info-service.fr/)（HTTP 503 服务暂不可用） |
| 德国 | 德国：体育博彩、单独监管的赛马；彩票仅政府运营方或关联签约运营方。 | [FAGS Glücksspielsucht](https://www.gluecksspielsucht.de/)（已打开目标页） |
| 加纳 | 加纳：线上赌场、体育博彩和彩票。 | [Gaming Commission of Ghana](https://gamingcommission.gov.gh/)（超时） |
| 希腊 | 希腊：线上赌场、体育博彩、DFS 和彩票。 | [KETHEA Helpline 1114](https://www.kethea.gr/kethea/therapeftika-programmata/grammi-voitheias-1114/)（HTTP 502） |
| 匈牙利 | 匈牙利：线上赌场、彩票、体育博彩（DFS 仅在当地法律允许时）和赛马。 | [Szerencsejáték-függőség Megelőzési Segítő Központ](https://szmsk.hu/szolgaltatasaink/)（已打开目标页） |
| 爱尔兰 | 爱尔兰：线上赌场、体育博彩；彩票仅政府或慈善运营方。 | [GambleAware Ireland](https://www.gambleaware.ie/)（超时） |
| 意大利 | 意大利：仅彩票。 | [Istituto Superiore di Sanità: Uscire dal Gioco](https://usciredalgioco.iss.it/)（HTTP 404） |
| 日本 | 日本：仅政府运营的体育博彩（赛马、摩托艇、自行车、汽车/自行车竞赛及足球彩票）和政府运营彩票。 | [Gambling Addiction Prevention and Recovery Support Center](https://www.gaprsc.or.jp/)（已打开目标页） |
| 肯尼亚 | 肯尼亚：线上赌场、体育博彩、单独监管的赛马和彩票。 | [Responsible Gambling Kenya](https://www.responsiblegambling.or.ke/)（已重定向并打开） |
| 拉脱维亚 | 拉脱维亚：仅彩票。 | [Spēles Brīvība](https://www.spelesbriviba.lv/)（已打开目标页） |
| 立陶宛 | 立陶宛：仅彩票。 | [Nebenoriu lošti](https://nebenoriu-losti.lt/)（已打开目标页） |
| 墨西哥 | 墨西哥：线上赌场、体育博彩和彩票。 | [Grupo Punto de Partida](https://grupopuntodepartida.com/en/)（已重定向并打开） |
| 荷兰 | 荷兰：线上赌场、彩票和体育博彩。 | [Open Over Gokken](https://www.loketkansspel.nl/index.html)（HTTP 502 网关错误） |
| 新西兰 | 新西兰：体育博彩和彩票仅政府运营方。 | [Gambling Helpline Aotearoa](https://gamblinghelpline.co.nz/)（已打开目标页）；[Choice Not Chance](https://www.choicenotchance.org.nz/understand-gambling)（缓存未命中，正文未获取） |
| 尼日利亚 | 尼日利亚：仅部分州；线上赌场、体育博彩（DFS 仅在法律允许时）、单独监管的赛马和彩票。若州或产品未出现在申请表中，当前不得分发。 | [Gamble Alert](https://gamblealert.org/)（已打开目标页）；[Gamble Pause](https://gamblepause.com/)（返回空正文） |
| 挪威 | 挪威：线上赌场、彩票；体育博彩仅政府运营方。 | [Hjelpelinjen](https://hjelpelinjen.no/)（已打开目标页）；[Spillavhengighet Norge](https://spillavhengighet.no/)（已重定向并打开） |
| 巴拿马 | 巴拿马：线上赌场、体育博彩（DFS 仅在当地法律允许时）、单独监管的赛马和彩票。 | Responsible-gambling contact listed by Play（原文只显示邮箱文本，没有超链接） |
| 秘鲁 | 秘鲁：仅彩票。 | [Ministry of Health: Línea 113](https://www.gob.pe/555-linea-113-salud-recibir-orientacion-e-informacion-en-salud)（HTTP 418，正文未获取） |
| 菲律宾 | 菲律宾：仅彩票。 | [PAGCOR Responsible Gaming](https://www.pagcor.ph/regulatory/responsible-gaming.php)（已打开目标页） |
| 波兰 | 波兰：仅彩票。 | [Uzależnienia Behawioralne](https://uzaleznieniabehawioralne.pl/)（已打开目标页） |
| 葡萄牙 | 葡萄牙：线上赌场、体育博彩、单独监管的赛马；彩票仅限 Santa Casa da Misericórdia de Lisboa 发布的获批应用。 | [Serviço de Regulação e Inspeção de Jogos](https://www.srij.turismodeportugal.pt/pt/jogo-responsavel/politica-de-jogo-responsavel/)（缓存未命中，正文未获取） |
| 罗马尼亚 | 罗马尼亚：线上赌场、体育博彩；彩票仅政府运营方。 | [Clinica Aliat](https://www.clinica-aliat.ro/jocuri-de-noroc/)（缓存未命中，正文未获取） |
| 塞尔维亚 | 塞尔维亚：线上赌场、体育博彩（DFS 仅在当地法律允许时）；彩票仅政府运营方。 | [Special Hospital for Addiction Diseases](https://www.drajzerova.org.rs/)（已打开目标页） |
| 新加坡 | 新加坡：仅彩票。 | [National Council on Problem Gambling](https://www.msf.gov.sg/ncpg)（重定向后仅有简短正文） |
| 斯洛伐克 | 斯洛伐克：线上赌场、体育博彩（DFS 仅在当地法律允许时）、单独监管的赛马和彩票。 | [Centrum pre liečbu drogových závislostí](https://cpldz.sk/)（超时） |
| 西班牙 | 西班牙：线上赌场、体育博彩（DFS 仅在当地法律允许时）、单独监管的赛马；彩票仅政府运营方。 | [FEJAR](https://fejar.org/)（已打开目标页）；[Clínicas CITA](https://www.clinicascita.com/tratamiento-ludopatia/)（缓存未命中，正文未获取） |
| 瑞典 | 瑞典：线上赌场、体育博彩；彩票仅政府运营方。 | [Stödlinjen](https://stodlinjen.se/)（已重定向并打开） |
| 瑞士 | 瑞士：线上赌场、体育博彩和彩票。 | [SOS-Spielsucht](https://www.sos-spielsucht.ch/en/)（已打开目标页） |
| 坦桑尼亚 | 坦桑尼亚：线上赌场、体育博彩（DFS 仅在当地法律允许时）和彩票。 | [Gaming Board of Tanzania](https://www.gamingboard.go.tz/)（超时） |
| 土耳其 | 土耳其：线上赌场、体育博彩和彩票。 | [Yeşilay gambling-addiction resource](https://www.yesilay.org.tr/bagimlilik/kumar-bagimliligi/)（已重定向并打开） |
| 乌克兰 | 乌克兰：仅彩票。 | [State Agency PlayCity: gambling-addiction prevention](https://playcity.gov.ua/borotba-z-ihrovoiu-zalezhnistiu)（已打开目标页） |
| 英国 | 英国：线上赌场、体育博彩（DFS 仅在当地法律允许时）和彩票。 | [GambleAware](https://www.gambleaware.org/)（已重定向并打开） |
| 美国 | 美国：线上赌场、体育博彩、单独监管的赛马和彩票（含彩票代购）仅限当地合法且有适当许可的州；另允许符合 NIGC 批准部落博彩条例的 II 类部落博彩。州/产品是否支持以申请表为准；DFS 可能按州被视为赌博，须另满足 DFS 政策。 | [National Council on Problem Gambling: help by state](https://www.ncpgambling.org/help-treatment/help-by-state/)（已重定向并打开） |

### 页面直接子链接的关系与审计边界

该页正文发现并逐项尝试了 53 个不同目标：1 个真钱赌博申请表、1 个当前真钱赌博政策页、51 个按市场列出的第三方/监管机构求助资源。51 个资源中 33 个返回了可读正文或落地页（其中埃塞俄比亚目标仅返回页面标题），17 个遇到 403/404/418/502/503、超时、缓存未命中或内部读取错误，1 个返回空正文；官方原页的全部 51 个目标地址现已通过页面链接/抓取输出核对并写入下表。可读页的共同关系是本地求助/监管信息示例，不构成 Google Play 认证、政策解释或对机构的背书。另尝试正文外的社区/客服入口（未读取成功）；侧栏 32 项帮助索引是共享导航，不计入这页的正文义务。**资源网站的孙链接不递归抓取**，它们不属于 Google Play 政策条文。

| 目标页 | 读到的内容与关系 | 状态 |
| --- | --- | --- |
| [Gambling Application Form](https://support.google.com/googleplay/android-developer/contact/gambling) | 显示 45 个支持市场，并含美国州/产品、尼日利亚州/产品矩阵。申请以应用、市场/州、产品类别为粒度；所有权或许可变更需重新认证。表单读取开发者/授权代表、应用包名、许可主体/地址/类别/地域和许可证证明；审核至少一周或更久。 | 表单正文已打开；市场选项为动态状态；未提交申请。 |
| [Daily Fantasy Sports Application Form](https://support.google.com/googleplay/android-developer/contact/dfsform) | 美国 DFS 单独认证；需美国州/地区有效牌照或登记证明、开发者与许可主体关系、应用包名和牌照日期。一个表单最多添加 20 个州；须遵守 DFS 条款，不得聚合第三方 DFS，许可证终止/变更、监管裁定或地理/年龄门控故障须及时报告/限制服务。 | 正文及条款区已打开；实际资格和提交状态未验证。 |
| [Content rating requirements](https://support.google.com/googleplay/android-developer/answer/9859655?hl=en) | 表单要求 A/O 或等效评级；Play 评级帮助页已跳转到现行 9859655 文章，双语内容见[内容分级专题](../content-ratings/content-ratings.zh-CN.md)。 | 现行帮助页已打开；外部 IARC 评级流程未递归审计。 |
| [Developer Policy Center](https://play.google.com/about/developer-content-policy/) | 赌博申请同时受开发者计划政策和 DDA 约束；完整政策已在本库入口页维护。 | 动态链接本轮抓取失败；本地政策页可继续浏览。 |

## 项目审查顺序

1. 先判断应用是否涉及真实价值投注/奖品、下注辅助、模拟赌博或赌博广告；不要只按应用商店类别判定。
2. 按每个目标市场和产品类型确认政府许可及 Play 是否接受申请；记录许可主体、有效期、地理范围与产品范围。
3. 用当前 Play 申请表完成相应认证；分别检查应用市场、用户年龄、IARC 等级、负责任赌博披露和支付路径。
4. 对广告、DFS、忠诚奖励、WebView/外链做独立审查，避免主应用不下注但仍通过广告/辅助功能促成赌博。
5. 发布前重查地区表和申请状态；国家/地区法律变化后重新评估资格。

## 相关专题

- [广告与推广](../ads-and-advertising/ads-and-advertising.zh-CN.md) · [金融服务与贷款](../financial-services-and-loans/financial-services-and-loans.zh-CN.md)
- [加密资产与 NFT](../crypto-assets-and-nfts/crypto-assets-and-nfts.zh-CN.md) · [付款与订阅](../payments/payments-and-subscriptions.zh-CN.md)
