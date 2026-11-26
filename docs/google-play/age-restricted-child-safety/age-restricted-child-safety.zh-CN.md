---
id: google-play.age-restricted-child-safety
platform: google-play
language: zh-CN
authority: normative
status: current
kb_checked_at: 2026-10-24
review_due: 2027-01-24
regions: [global]
topics: [age-restriction, minors, child-safety, anonymous-chat, random-chat, families, ugc]
snapshot_id: play.age-restricted-child-safety
snapshot_package: "GooglePlay-KnowledgeBase-2026-10-24-review.zip"
coverage_status: "detailed-summary"
source_url: "https://support.google.com/googleplay/android-developer/answer/16302250?hl=en"
source_url_zh: "https://support.google.com/googleplay/android-developer/answer/16302250?hl=zh-Hans"
effective_date: "2026-08-26"
---

# 年龄限制、匿名聊天与儿童安全

> **导入说明（Google batch 3）。** 本页正文取自 2026-10-24 Google Play 知识库快照里已经分开的对应语言改写（`play.age-restricted-child-safety`，核对日 2026-10-24），不是官方页面的逐字文本。英文官方来源是效力来源。`kb_checked_at` 使用快照源文件记录的核对日；本次导入没有重新打开线上官方页面。文中“本知识库”“本库”“本地专题”描述的是该快照知识库的覆盖范围，不是本仓库已经导入的页面清单。快照里指向尚未导入本仓库的专题、链接图、台账或 CSV 的相对链接，已改为文字提及；指向 Google batch 1、batch 2 或本批九个专题的相对链接已改到本仓库路径。快照的 `effective_date` 是 2026-08-26。源文件写明该日期已经生效，是政策更新生效日，不代表某个应用已经通过审核。2026-10-22 同时重开了英文年龄限制政策和简体中文 `hl=zh-Hans` 页面。Google 提示中文页可能使用 AI 翻译且可能不准确，实质判断以英文措辞为准。Families 数据实践页于 2026-10-24 以英文和 `zh-Hans` 打开，同样带有 AI 翻译提示。`zh-Hans` Data safety 目录请求返回 Cache miss；该访问限制不表示政策已经变更。COPPA 一般合规日 2026-04-22 和 16 CFR Part 312 的 2025-06-23 生效日在源文件中记为已过。Texas SB 2420 的 2026-01-01 生效日及源文件摘要的诉讼状态是 regulatory 说明，不是 Play 政策。Age Signals 的“未来生效日”是重大变更通知的 Console 字段，不是 Play 政策预告。所链接的前台服务预览是未导入本仓库的另一快照专题，不是儿童安全的生效日。本页的年龄限制、Child Safety Standards 和 Families 规则是 `normative`。COPPA、GDPR、DSA 和州法段落是 regulatory，不替代这些 Play 规则。Age Signals API 与 AdMob 配置步骤是 implementation note。

**核对日期：2026-10-24。** Google Play 自 **2026-08-26** 起将年龄限制、Child Safety Standards 和 Families 政策扩展到匿名聊天/随机聊天应用。该日期已经生效。适用范围要按 Google 对不同应用类别的判定方式分别核对：匿名/随机聊天看核心功能；Social/Dating 则按 Play Console 中申报的类别判断。商店类别和应用体验仍须如实匹配，年龄门槛或“仅限成人”声明本身不会豁免儿童安全标准。

## 先判定应用属于哪条规则

| 应用功能 | 主要 Play 要求 |
| --- | --- |
| 促成真钱赌博、游戏或竞赛 | 使用 Play Console 的 Restrict Minor Access 工具屏蔽未成年人，并满足对应真钱赌博政策/许可 |
| 核心功能是约会或匹配 | 使用 Restrict Minor Access 屏蔽未成年人 |
| 核心功能是随机连接陌生人并即时聊天 | 使用 Restrict Minor Access；并遵守适用 Child Safety Standards |
| 核心功能是匿名沟通，且刻意隐藏一方或多方身份 | 使用 Restrict Minor Access；并遵守适用 Child Safety Standards；不得把匿名聊天应用申报为儿童目标应用 |
| 约会/匹配只是附属功能 | 不一定要屏蔽整个应用，但必须用有效的年龄门槛限制未成年人进入该具体功能 |
| 社交/约会/匿名或随机聊天功能面向儿童 | 须遵守 Families 及儿童安全规则；匿名聊天应用不得以儿童为目标受众 |

**重要区别：** Restrict Minor Access 屏蔽整款应用；附属约会功能的年龄门槛只限制该功能。填写 IARC 内容分级或把目标年龄设置为“18+”本身，不等于已经完成 Play Console 的 Restrict Minor Access 操作。

### 年龄限制政策正文的直接子链接

2026-10-22 重新打开了[英文正文](https://support.google.com/googleplay/android-developer/answer/16302250?hl=en)和[简体中文页面](https://support.google.com/googleplay/android-developer/answer/16302250?hl=zh-Hans)。两种语言都列出真钱赌博、核心约会/匹配、随机陌生人即时聊天、核心匿名沟通四类应用；中文帮助页提示其内容可能由 AI 翻译，中文只作辅助核对，实质判断以英文正文为准。正文中的三个唯一目标及其与本规则的关系如下：

| 正文链接目标 | 与年龄限制规则的关系 | 核验状态 |
| --- | --- | --- |
| [Play Console 的目标受众与应用内容设置](https://support.google.com/googleplay/android-developer/answer/9867159?hl=en) | 操作页说明如何申报目标年龄组，并在适用时选择仅 18+、另外启用 Restrict Minor Access；只选 18+ 不会自动启用屏蔽。 | 英文与简体中文政策页的链接均指向此操作目标；目标正文已打开并摘要，另见下文的目标受众专题。 |
| [Real-Money Gambling, Games, and Contests](https://support.google.com/googleplay/android-developer/answer/9877032?hl=en) | 赌博是年龄屏蔽适用类别之一；该独立政策还要求获准应用满足许可、地理限制、免费安装、不使用 Play Billing、AO/IARC 等条件。年龄屏蔽不能代替赌博认证或其他准入要求。 | 两种语言页面的链接均已解析到现行赌博政策；[完整政策和申请/地区后代见真钱赌博专题](../real-money-gambling/real-money-gambling.zh-CN.md)。 |
| [Apps with incidental dating or matchmaking features](https://support.google.com/googleplay/android-developer/answer/16838200?hl=en) | 区分核心约会应用的整款应用屏蔽与约会只是附属功能时的功能级年龄门槛；不强制某种技术，但机制应有效且不易绕过。 | 两种语言页面的链接点击均返回内部错误；按精确目标地址重新打开后，正文及其两个政策/操作子链接已核验，见下文。 |

帮助页另有 10 项“受限内容”侧栏导航（含当前页自身）；这是共享政策目录，不计入正文直接链接。社区、联系支持和反馈控件也单独记账，不作为年龄屏蔽政策义务。

## Restrict Minor Access：整款应用的未成年人屏蔽

- 对政策列出的适用应用，在 Play Console 的 Target audience and content 设置中，将目标年龄设为仅 **18 岁及以上**，并开启 Restrict Minor Access。
- Google 根据 Google 账号年龄信息或其系统判断识别未成年人。被识别为未成年人的用户不能在 Play 上搜索、下载或购买该应用。
- 已安装应用的未成年人可能仍能继续使用，但不能续订现有订阅或进行新购买；这与完全封禁所有既有安装用户不同。
- 年龄限制工具不替代目标受众、内容分级、Families、儿童安全、当地年龄/消费者法律等其他申报和义务。

官方政策把“核心功能”作为适用判断的重要边界。若匹配、约会或匿名交流只是附加模块，应对该功能实施有效年龄门槛，不能让未成年人绕过后进入。中性年龄屏幕不应预填成人出生日期，也不应提示用户填写某个特定年龄以获得访问。

### 附带约会/匹配功能帮助页的子链接

[附带约会或匹配功能要求](https://support.google.com/googleplay/android-developer/answer/16838200?hl=en)于 2026-10-22 重新打开全文。该页正文的两个政策/操作链接分别指向本专题所述的[年龄限制政策](https://support.google.com/googleplay/android-developer/answer/16302250?hl=en)和 [Play Console 目标受众与应用内容设置](https://support.google.com/googleplay/android-developer/answer/9867159?hl=en)：

| 后代目标 | 与本规则的关系 | 核验状态 |
| --- | --- | --- |
| [Age-Restricted Content and Functionality](https://support.google.com/googleplay/android-developer/answer/16302250?hl=en) | 核心功能为约会/匹配的应用须使用 Play Console 的 Restrict Minor Access；约会只是附属功能时，可用有效年龄门槛阻止未成年人进入该功能。 | 正文于 2026-10-22 打开；政策正文另有随机聊天/匿名沟通等类别。 |
| [Manage target audience and app content settings](https://support.google.com/googleplay/android-developer/answer/9867159?hl=en) | 目标受众必须依真实设计选择；在填写 Target audience and content 前，需先申报广告、提供审核访问说明并添加隐私政策。若受众包含儿童，还触发 Families 要求。按年龄限制政策须屏蔽未成年人的应用，应仅选 18+ 并另行启用 Restrict Minor Access；只选择 18+ 年龄组本身不等于启用了该功能。 | 正文于 2026-10-22 打开；其链接后代与侧栏在来源台账逐项登记，后续技术实现及课程分支未全部递归。 |
| Help Community / Contact us | 是帮助与支持页脚入口，不属于约会年龄门槛的政策义务。 | 页面可见；支持路由可能因登录和账号状态而不同。 |

该约会帮助页没有规定具体年龄门槛技术，但要求机制合理有效、能阻止未成年人访问且不易绕过。其 Help Center 侧栏推荐另行记录，不与正文的两个子链接混算。

## 目标受众申报与按年龄段设计指南

[目标受众与应用内容设置指南](https://support.google.com/googleplay/android-developer/answer/9867159?hl=en)已于 2026-10-22 重新打开全文。新应用和每次应用更新都要申报目标年龄组；选择多个年龄组，前提是应用确实为这些年龄层设计且适龄。提交 Target audience and content 前，先完成广告声明、审核访问说明和隐私政策；Google 会审查申报是否准确，部分账号/应用类别可能需要 7 天以上审核。未满 21 岁的受众还应按目标地区法律判断其是否属于儿童。

页面里的年龄段建议用于产品设计和受众选择，不是独立的 Play 许可类别或一套全球统一的法定年龄表。5 岁及以下、6–8 岁和 9–12 岁在多数地区会被视为儿童；13–15 岁和 16–17 岁在部分地区也可能属于儿童。凡目标受众包含儿童，须额外满足 Families 要求；面向混合受众投放儿童广告时，要采取中性年龄屏幕等措施，并对儿童与未知年龄用户使用符合要求的广告 SDK。

| 年龄段 | Google 给出的设计适配方向 | 需要谨慎的常见内容/交互 |
| --- | --- | --- |
| 5 岁及以下 | 支持非读者/初读者；少文字、简单导航和大触控目标；适合感官探索、假装游戏、简单问题解决；让家长有清晰参与方式。 | 阴暗恐怖场景、快速反应/精细操作、抽象记忆任务、惩罚机制、暴力或轻度性暗示、过多分散注意的功能。 |
| 6–8 岁 | 面向早期阅读/书写；提供正向反馈、幽默故事/角色、积极榜样、徽章/解锁等适龄目标及基础教育内容。 | 为幼儿设计的视觉与音乐、外貌刻板印象、物化/性化表达、现实暴力/伤害、搜索功能。 |
| 9–12 岁 | 适度逻辑/空间推理、该年龄常见学科、创造表达和个性化；分享功能应有限且受监督。 | 过于幼稚或单调的内容、粗俗语言、外貌刻板印象、现实暴力/伤害、未受约束的用户直接互动。 |
| 13–15 岁 | 更复杂的叙事、挑战和机制；年龄适宜的社交、身份与青春期信息。 | 美化暴力/贬损/高度性化表达，或鼓励可能导致身体伤害的冒险挑战。 |
| 16–17 岁 | 更复杂的问题解决、学业内容、青少年兴趣与年龄适宜社交；帮助表达情绪。 | 极端暴力、性暴力/家庭暴力、成瘾式设计或很高的消费门槛。 |
| 18 岁及以上 | 面向成年人的内容仍须合法且符合 Play 政策。年龄限制政策要求屏蔽未成年人的应用，还必须另行启用 Restrict Minor Access。 | 仅在申报表中选 18+ 不等于已启用屏蔽功能，也不自动豁免其他政策。 |

所有年龄段还要核对成品质量、功能是否适龄、内容传达的信息、广告和应用内购。设计建议与正式政策分开判断：选了某年龄段，不会替代内容评级、Families、隐私/数据、年龄限制或广告规则。

### 目标受众指南的直接链接与关键后代

| 父页链接/后代 | 目标页面及本地关系 | 核验状态与边界 |
| --- | --- | --- |
| 目标受众指南 → 内容评级问卷 | [Content rating requirements](https://support.google.com/googleplay/android-developer/answer/9859655) · [本地内容分级专题](../content-ratings/content-ratings.zh-CN.md) | 正文已完整打开并由内容分级专题总结；IARC 内容分级、目标年龄申报和 Restrict Minor Access 是不同控制。 |
| 目标受众指南 → Families 与广告 SDK | [Families Policy Requirements](https://support.google.com/googleplay/android-developer/answer/9893335) · [Families 自认证广告 SDK 计划专题](../families-self-certified-ads-program/families-self-certified-ads-program.zh-CN.md) · [Families Self-Certified Ads SDK 列表](https://support.google.com/googleplay/android-developer/answer/12955712) | 上位政策和动态名单已打开；计划暂停新申请（2026-10-23 状态快照）。发布前须重新核对具体版本；计划正文与所有直接链接见独立专题。 |
| 目标受众指南 → 开发者规则与合同 | [现行 Developer Program Policy](https://support.google.com/googleplay/android-developer/answer/18258653) · [Developer Distribution Agreement](../developer-distribution-agreement/developer-distribution-agreement.zh-CN.md) | 两者已分别在知识库全文改写摘要；点击目标受众页中的 DDA 外链时抓取器返回 Internal Error，因此以已独立核验的合同页交叉引用，不把这次失败说成目标正文不可访问。 |
| 目标受众指南 → 填报前置资料 | [Prepare your app for review](https://support.google.com/googleplay/android-developer/answer/9859455) · [App content Console 表单](https://play.google.com/console/app/app-content/summary) | Prepare 正文已打开，涵盖广告声明、审核访问说明、隐私政策和其它 App content 声明；实际 App content 表单要求开发者账号登录。目标受众页上的广告/隐私单独链接本次返回 Internal Error，相关规范以 Prepare 指南和现行专题为准。 |
| 目标受众指南 → Google 账号年龄保护说明 | [How Google helps provide an age-appropriate experience](https://support.google.com/accounts/answer/11061638) | 已完整打开。该消费者帮助页称 Google 可结合账号年限、活动和付款资料估计年龄状态；无法确认时会应用更安全的设置。系统判断可能未满 18 岁时，Google Search 默认 SafeSearch Filter，Search/YouTube 不提供个性化广告；这不代表 Play 应用内的年龄门槛或广告规则。页面提及部分地区法律可能要求应用商店核验年龄、取得家长同意并向开发者提供年龄信息，但这不是普遍 API/法定义务说明。它不是开发者年龄查询接口，也不替代 Console 申报；年龄验证、Family Link、SafeSearch、举报、安全中心和青少年隐私直接子页已复核，账号内状态仍需登录。 |
| Google 账号年龄帮助 → 年龄验证方式 | [Access age-restricted content & features](https://support.google.com/accounts/answer/10071085) | 消费者可见的验证方式包括政府证件、合作方自拍、电子邮件和信用卡验证；实际方式及证件要求按地区、账号和功能变化。页面说明证件成功核验后删除、生日资料写入账号/付款资料，并分别介绍 Private ID 与 VerifyMy 的数据传递。它说明 Google 账号用户流程，不证明开发者能读取这些原始材料或状态。合作方[Private ID 使用条款](https://g.privateid.com/terms-of-use)与[隐私政策](https://g.privateid.com/privacy)本次返回 404；[VerifyMy 隐私说明](https://verifymyage.com/google-age-assurance-privacy-policy)和[年龄估算说明](https://www.verifymyage.com/email-address-age-estimation)返回 403，未推断其内容。 |
| Google 账号年龄帮助 → 账号生日、年龄与活动设置 | [生日](https://myaccount.google.com/birthday) · [年龄验证](https://myaccount.google.com/age-verification) · [Web 与应用活动设置](https://myactivity.google.com/personalization/settings/waa) | 均重定向到 Google 登录或账号专属页面；无法核实账户当前生日、验证结果、活动设置或开发者可见性。 |
| Google 账号年龄保护 → Family Link 家长监督 | [Get started with Family Link](https://support.google.com/families/answer/7101025) · [Google Safety Center：家长控制](https://safety.google/intl/en_us/settings/parental-controls/) | Family Link 可管理受监督账号的应用、权限、使用时间与部分内容设置；适用地区和设备有限，购买批准只适用于 Google Play Billing。Safety Center 是消费者功能介绍。它们是用户/家长侧控制，不是开发者年龄验证、Play Console 年龄申报或政策豁免。 |
| Family Link → Google Play 家长内容限制 | [How to set up content restrictions on Google Play](https://support.google.com/families/answer/1075738) | 按成熟度分级限制指定 Android 设备上的下载/购买；设置不阻止搜索结果或直接链接显示受限内容，且适用范围按设备/地区而异。此消费者过滤功能不能替代开发者年龄门槛、Restrict Minor Access 或 Families 合规。 |
| Google 账号年龄保护 → SafeSearch | [Make Google Search safer with SafeSearch](https://support.google.com/websearch/answer/510) · [Fix problems with SafeSearch](https://support.google.com/websearch/answer/9448272) | SafeSearch 仅过滤 Google Search；系统认为用户未满 18 岁时可能默认 Filter，且家长、学校、设备或网络可锁定设置。它不控制 Play 应用内部内容，也不是开发者的年龄判断或内容过滤 API。 |
| Google 账号年龄保护 → 家庭/儿童内容举报 | [Report inappropriate content or behavior toward children](https://support.google.com/families/answer/7182800) · [Family content 举报表单](https://support.google.com/googleplay/contact/rap_family) | 用户帮助页列出 Play 中应用、游戏、音乐和家庭内容的举报步骤；专用家庭内容表单跳转至 Google 登录，无法读取。该消费者举报入口不同于开发者的 Child Safety Standards、应用内举报/处置流程或政策申报。Help 侧栏中的一般联系与产品设置后代未全部遍历。 |
| Google 账号年龄保护 → 青少年隐私说明 | [Teen Privacy Guide](https://policies.google.com/privacy/teens)（父页短链 [g.co/teenprivacy](https://g.co/teenprivacy)，经 [www.google.com/policies/privacy/teens/](https://www.google.com/policies/privacy/teens/) 跳转） | 面向青少年的 Google 隐私解释，涉及位置、分享、数据个性化和控制选项；它不是 Developer Program Policy、User Data 或数据安全表单的替代。其通用隐私政策后代未在本年龄分支穷尽。 |
| 目标受众指南 → 年龄门槛与用户数据 | [Age-Restricted Content and Functionality](https://support.google.com/googleplay/android-developer/answer/16302250) · [User Data 专题](../user-data/user-data.zh-CN.md) | 年龄限制政策已完整打开；指南中的旧 User Data 链接跳转到 Privacy, Deception and Device Abuse 主题入口，现行用户数据正文及其他链接见双语 User Data 专题。 |
| 目标受众指南 → 年龄门槛外部法律参考 | [FTC COPPA FAQ](https://www.ftc.gov/business-guidance/resources/complying-coppa-frequently-asked-questions) | 已打开。FTC 对一般受众服务的年龄询问、对 13 岁以下儿童的实际知情及家长同意作美国 COPPA 解释；这是美国法律参考，不是 Play 规则，也不能用来降低 Play 年龄限制政策要求。FAQ 的州执法、举报和 Safe Harbor 后代未全部展开。 |
| 目标受众指南 → 商店素材与儿童吸引力 | [Add preview assets](https://support.google.com/googleplay/android-developer/answer/9866151) · 商店详情最佳实践[商店详情与素材最佳实践](../store-listing-best-practices/store-listing-best-practices.zh-CN.md) | 预览素材帮助页已完整打开；商店素材里的年轻角色、动画或文案可能影响 Google 对受众申报的判断，具体与 Play 审核政策的关系见商店详情专题。 |
| 目标受众指南 → 可选 Teacher Approved 计划 | [Teacher Approved 介绍](https://google.play/business/programs/teacherapproved/) | 旧 Console 链现已重定向到公开介绍页。它是可选的儿童应用质量评议/展示计划，不是强制合规或获批保证；评价包含适龄设计、内容、广告、应用内购和交叉推广。页面链接的课程只公开课程简介，正式课件须登录。 |

### Google Developers 儿童产品最佳实践及子孙链接

目标受众指南和 Teacher Approved 入口都链接 [Building for kids](https://developers.google.com/building-for-kids)；它是 Google Developers 的工程/设计建议，不是 Google Play 的强制政策条文。其三个直接子页均已完整打开：

| 子页 | 摘要 | 继续跟进的链接与状态 |
| --- | --- | --- |
| [Designing engaging apps](https://developers.google.com/building-for-kids/designing-engaging-apps) | 为不同年龄和能力设计；用儿童与家长研究验证假设；保持导航、手势和触控目标简单一致；减少干扰、提供清楚的视听反馈、重视无障碍，并让家长能参与和管理设置。 | 链接 [Be Internet Awesome](https://beinternetawesome.withgoogle.com/en_us)，正文已打开并归纳分享隐私、反诈、密码、安全沟通、反霸凌和向可信成人求助；链接的课程/Interland/下载资源尚未逐项展开。[Material Accessibility](https://m2.material.io/design/usability/accessibility.html) 只返回“需要 JavaScript”。 |
| [Developing thoughtful content](https://developers.google.com/building-for-kids/developing-thoughtful-content) | 按儿童发展阶段选择故事、角色、语言和主题，避免令人困惑/恐惧的内容及无意刻板印象；与家长沟通时清楚说明披露、家长控制和重要体验。 | 页面只有本系列导航与页脚链接；页面内直接关联的两个系列主题均已作为同级页面打开。年龄分组建议为通用发展指导，不取代当地法律或 Play 内容政策。 |
| [Building safer apps](https://developers.google.com/building-for-kids/building-safer-apps) | 对聊天和 UGC 做威胁建模；建议审核/预先批准内容、举报/屏蔽、家长管理和适当审核；也给出 Android 受监督账号下跳转家长控制的实现示例。 | 链接 [FOSI 与儿童讨论网络安全的建议](https://www.fosi.org/good-digital-parenting/talking-to-kids/) 返回 Cache miss；Be Internet Awesome 目标已在上行登记。Play 对 UGC、儿童安全的强制要求见本地 [UGC](../user-generated-content/user-generated-content.zh-CN.md) 和[儿童安全标准](#child-safety-standards儿童安全标准)，不能以工程建议替代。 |

[Teacher Approved 页面](https://google.play/business/programs/teacherapproved/)另列 3 个 Play Academy 课程：高质量儿童应用最佳实践、内容适龄标准、广告与应用内购标准。三页课程简介均已打开，正文课程需登录；高质量儿童应用课程另链接回目标受众指南，内容适龄课程还链接 Families 政策及下一门广告/IAP 课程。另一个 Families 课程目录列出 5 门课程，其中 4 个课程页本次均返回 Cache miss；不据标题推断未读取的课件内容。Teacher Approved 评价标准可辅助自查，但计划资格、展示和具体规则以当前 Play 页面为准。

## Child Safety Standards：儿童安全标准

Google Play 当前 Child Endangerment 页面要求匿名聊天、随机聊天、社交和约会应用遵守 Child Safety Standards。应把以下要求落实为实际产品、审核和响应流程：

1. **公开规则：** 在服务条款、社区准则或其他公开用户规则中明确禁止儿童性剥削和虐待（CSAE）。
2. **应用内反馈/举报：** 提供用户可在应用中提交安全问题、举报或反馈的机制，并在适用的 Play Console 自我认证中如实申报。
3. **CSAM 处置：** 对已实际知悉的儿童性虐待材料采取适当行动，包括按公开标准和适用法律移除/处理。
4. **依法报告：** 建立确认 CSAM 的报告流程，按适用法律向 NCMEC 或相关地区主管机构报告。
5. **儿童安全联系人：** 指定能够接收 Google Play 通知、说明审核/执法流程并推动处置的联系人。

匿名/随机聊天仅靠年龄门槛并不足够：还要管理 UGC 风险、举报队列、升级/响应、证据处理、重复违规者和地区法律要求。CSAE/CSAM 属严重安全议题，实际处置流程应由负责的信任与安全团队及法律顾问确认。

## Child Endangerment 政策正文直链

2026-10-22 重开 [Child Endangerment](https://support.google.com/googleplay/android-developer/answer/9878809?hl=en) 全文，并尝试正文 5 次链接出现、4 个唯一目标（重复的地区组织链接合并）；页脚帮助社区/客服和 10 项 Restricted Content 侧栏另行分类，不混作正文要求。

| 正文直链 | 打开结果与摘要 | 与 Play 要求的关系 |
| --- | --- | --- |
| [Report abuse on a Google product](https://support.google.com/googleplay/contact/rap_family) | 重定向到 Google 账号登录；未能读取表单。 | 是向 Google 举报其产品上的儿童安全内容的入口；不同于应用内反馈机制或开发者在 Play Console 的自我认证。 |
| [Appropriate agency in your country](https://support.google.com/websearch/answer/148666) | 2026-10-24 已打开正文。目录按地区列出 48 个国家/地区，正文有 45 个地区组织网站链接，并另列 NCMEC 与 INHOPE。其“立即危险时联系警方、未列国家可联系 INHOPE”的说明和 45 个直链的访问结果见[地区举报渠道目录专题](../child-safety-regional-reporting/child-safety-regional-reporting.zh-CN.md)。 | 这是 Google Search Help 提供的公开举报渠道导航，不是 Play 对所有开发者指定的统一举报对象或时限；开发者义务仍须按适用法律与 Play 条款分别判断。 |
| [NCMEC CyberTipline](https://report.cybertip.org/) | 官方公开落地页介绍儿童性剥削举报入口；注册和后续操作须核对 NCMEC 当前说明与适用法律。 | 这是 Play 正文点名的美国举报渠道，不代表所有地区开发者都有相同路径或时限。 |
| [Learning more about Child Safety Standards](https://support.google.com/googleplay/android-developer/answer/14747720?hl=en) | 正文全文已读，包含适用范围、CSAE/CSAM 定义、公开标准、应用内反馈、处置和联系人 FAQ。 | Google Play 的政策说明与自我认证指导；以其现行要求判断开发者义务，外部行业材料仅作补充。 |

## 儿童安全标准的落地最佳实践与子链接

Google 的[Child Safety Standards 说明页](https://support.google.com/googleplay/android-developer/answer/14747720?hl=en)已于 2026-10-24 重新打开。它将适用范围分成两种判定：匿名/随机聊天按核心功能；Social/Dating 按 Play Console 申报的类别。是否有儿童用户、是否只面向成人或是否设置年龄门槛，都不改变该标准适用性。[类别和标签指南](https://support.google.com/googleplay/android-developer/answer/9859673)要求类别/标签应准确反映主要功能，并建议在内容或功能有重大变化后重新检查；这是准确设置商店信息的操作指导，不是儿童安全认证。公开标准页面须全球可访问、正常加载、与 CSAE/儿童安全相关，并写明商店中的应用或开发者名称；应用内反馈机制须能在不离开应用的情况下使用；CSAM 处置按已公布流程和相关法律执行；须在 Play Console 自我认证并指定可说明预防、审核和处置流程的个人联系人。

Google Search Help 的[地区举报渠道目录](../child-safety-regional-reporting/child-safety-regional-reporting.zh-CN.md)列出各地区的组织及网站。目录入口、页面可访问性和与 Play 义务的边界均已单独登记；可读的外部站点正文及其更深链接仍按逐 URL 审计状态继续核验。

Google 将 Tech Coalition 的[开发者防治在线儿童性剥削与虐待最佳实践](https://technologycoalition.org/resources/developer-good-practices-combating-online-child-sexual-exploitation-and-abuse/)列为补充指导。该指南发表于 2024-10-14，属于跨行业建议，不是 Google Play 新增的强制技术方案，也不构成法律意见或统一的标准照护。其建议可整理为以下运营链：

1. **把规则和内部流程写清楚：** 在服务条款、可接受使用政策或社区准则中公开禁止 OCSEA；另建供审核人员使用的内部定义、处置标准和一致性指南。
2. **让用户可举报，并准备识别能力：** 在产品各相关界面提供举报入口；按产品风险和能力评估哈希匹配、图像/视频/文本分类、关键词与 URL 规则，同时配备适当人工复核资源。
3. **按所在地建立事件响应：** 指南对美国公司列出 NCMEC CyberTipline，并提及电子服务提供商注册、报告 API/人工表单及数据保全；美国以外可通过 INHOPE 查找本地热线。具体报告义务、证据保存和执法请求须按当地法律确定。
4. **把安全前置到产品设计：** 在产品开发期间评估 OCSEA 风险；建立执法联络和响应流程，并通过用户安全教育、适当的透明度报告持续审查风险和措施。

| 子链目标 | 已核验内容 | 与 Play 政策的关系 / 访问边界 |
| --- | --- | --- |
| [Google: Learning more about Child Safety Standards](https://support.google.com/googleplay/android-developer/answer/14747720?hl=en) | 全文已打开；包含适用范围、CSAE/CSAM 定义、公开规则标准、应用内反馈、CSAM 处置和联系人 FAQ。 | 这是 Google Play 的政策解释与自我认证操作说明，优先于外部最佳实践。 |
| [Tech Coalition: Developer good practices](https://technologycoalition.org/resources/developer-good-practices-combating-online-child-sexual-exploitation-and-abuse/) | 全文已打开；内容含 OCSEA 风险类型、规则/举报/检测/审核/执法响应、安全设计、透明度报告及用户教育。 | 行业实践建议；指南自身说明不定义标准照护，也不提供法律或监管合规意见。 |
| [Tech Coalition Pathways](https://technologycoalition.org/programs/pathways/) | 计划介绍页已打开：为托管 UGC 或通信服务的科技公司员工提供免费资源、咨询与同业交流，主题包括内容政策、举报、全球法规、哈希检测、NCMEC 报告及执法响应。 | 参加计划不是 Play 要求；资源库需申请/加入后访问，供应商若不管理用户内容不符合其页面列出的参与范围。 |
| [NCMEC CyberTipline](https://report.cybertip.org/) 与 [Electronic Service Provider 注册入口](https://esp.ncmec.org/Registration) | CyberTipline 对外提供儿童性剥削举报；ESP 注册页已打开，但自动抓取未返回正文。 | 适用主体、报告时限、信息范围与保存义务应以所在地法律及 NCMEC 当前说明为准；不能仅凭知识库推定所有开发者均适用同一报告程序。 |
| [INHOPE 国家热线目录](https://inhope.org/) | 目录正文可见按国家/地区列出的热线；具体渠道随辖区而异。 | Tech Coalition 指南为美国以外公司提供的热线导航，不替代当地主管机关或法律意见。 |
| [Assessing OCSEA harms in product development](https://technologycoalition.org/resources/assessing-ocsea-harms-in-product-development/) 与 [Trust: Voluntary Framework for Industry Transparency](https://technologycoalition.org/resources/trust-voluntary-framework-for-industry-transparency/) | OCSEA 评估文章于 2023-11-02 发布，当前落地页及其 14 页 PDF 均已打开；旧 `www` URL 重定向至当前页。Trust 网页介绍称框架于 2024 年更新，当前完整框架为 2025 PDF。 | 可用于产品风险评估和透明度流程设计；均不是 Google Play 自我认证的替代品。OCSEA 方法及引用资料见下文；Trust 框架、实施指南、模板、DSA 对照及访问状态见[儿童安全外部法规与透明度专题](../child-safety-dsa-transparency/child-safety-dsa-transparency.zh-CN.md)。 |
| [Google: CSAM transparency FAQs](https://support.google.com/transparencyreport/answer/10330933?hl=en) | 已打开 Google 自身平台的检测、移除、NCMEC 报告和安全工具说明。 | 这是 Google 自身平台的做法说明，不是要求开发者复制 Google 的检测系统或政策义务。 |
| Google 页面标注的 [Tech Coalition Child Safety Standards](https://technologycoalition.org/membership/criteria/) | 点击后实际落到 Tech Coalition **会员资格标准**，内容要求会员具备公开规则、接收举报并行动、技术方案、透明度、人权/儿童权利、民间组织协作及持续参与。 | 这是会员准入标准，不是 Google Play 政策条文，也不是普通开发者必须加入 Tech Coalition 的要求；Google 链接标签与当前落地页内容不一致，已按实际目标记录。 |
| [Tech Coalition Child Safety Best Practices](https://technologycoalition.org/resources/child-safety-best-practices/) | 2024-09-15 的公开指南，逐项讲到公开规则、内部政策、举报、检测与人工审核、NCMEC、执法响应、安全设计、透明报告和教育。 | 与 2024-10-14 开发者指南内容相近但不是同一页面；未发现官方声明称后者取代前者。两者均为自愿行业建议。 |

## NCMEC CyberTipline：举报渠道、ESP API 与美国法定边界

2026-10-23 沿 Play 的 [Child Endangerment](https://support.google.com/googleplay/android-developer/answer/9878809?hl=en) 和 Child Safety Standards 说明页继续到 NCMEC：公开 CyberTipline → [FAQ](https://report.cybertip.org/faqs) → [Other Resources](https://report.cybertip.org/other-resources) → [Take It Down](https://takeitdown.ncmec.org/) 的 FAQ、隐私说明、参与平台清单和一页说明。也重开 [CyberTipline Reporting API 文档](https://report.cybertip.org/ispws/documentation/index.html)、[18 U.S.C. § 2258A](https://www.govinfo.gov/content/pkg/USCODE-2024-title18/html/USCODE-2024-title18-partI-chap110-sec2258A.htm)、提供者定义 [§ 2258E](https://www.govinfo.gov/content/pkg/USCODE-2024-title18/html/USCODE-2024-title18-partI-chap110-sec2258E.htm) 和 2024 年 [REPORT Act](https://www.govinfo.gov/app/details/PLAW-118publ59)。这些是法律、技术与受害者支持背景；它们不把某个 API、举报时限或处理方式自动变成全球 Google Play 义务。

**先分清三套机制：**

1. **Google Play Child Safety Standards** 要求适用开发者公开儿童安全标准、提供应用内反馈、处置已发现的 CSAM、按适用法律报告，并完成 Play Console 自我认证、指定联系人。这是 Play 平台政策。
2. **NCMEC 面向公众的 CyberTipline 表单**接受有关儿童性剥削的举报；NCMEC FAQ 说任何人都可举报、不要求居住在美国，也不要求必须填写姓名或联系方式。提供事件地点和举报人所在位置可帮助分流。NCMEC 会审阅并在可识别管辖区时提供给执法机关。公共举报入口不等同于所有 Play 开发者的统一法定报告程序。
3. **CyberTipline Reporting API** 是 NCMEC 面向符合条件服务提供者的自动化通道。文档要求 HTTPS 和 NCMEC 提供的账号凭据，并区分生产、测试环境；状态与 XSD 路由也需认证。报告流程为 `submit`，按需 `upload` 文件及 `fileinfo`，最后 `finish`；完成前可 `retract`。未完成草稿会在打开后 24 小时或最后修改后 1 小时（取较晚者）自动删除。API 文档称，除事件类别、日期/时间外，经 API 提供的其他数据由 ESP 自主决定；这是对接口字段的说明，不应改写成法律上可以省略法定报告内容的通用结论。

### 美国法第 2258A 条的范围和保存期限

可读的[美国法典文本](https://www.govinfo.gov/content/pkg/USCODE-2024-title18/html/USCODE-2024-title18-partI-chap110-sec2258A.htm)写明，法定义务适用于 § 2258E 定义的 provider，即电子通信服务提供者或远程计算服务；具体服务/实体是否符合定义须由法律顾问结合事实判断，不能推定每个 Play 开发者都适用。§ 2258A(a) 对实际知悉特定明显违法事实规定“尽快合理地”向 NCMEC CyberTipline 提交报告；对可能计划或即将发生的违法情形使用“可以”报告措辞。§ 2258A(f) 明确本条本身不要求服务提供者监控用户或通信，也不要求主动搜索、筛查或扫描相关事实；这不排除其他法律、司法程序、合同或 Play 政策另有要求。

完成的 CyberTipline 报告依 § 2258A(h) 被视为要求保存提交内容 **1 年**；可访问、且能为报告材料或涉事人员提供上下文的混合内容也须保存，并应安全存放、限制内部访问。REPORT Act（Pub. L. 118-59，2024-05-07）把旧的 90 天改为 1 年，并加入依 NIST Cybersecurity Framework 保存材料的要求，实施期限为该项修法颁布后 1 年（2025-05-07，已过）。2024 版法典正文和修订注记可读；众议院当前 preliminary Code 页面搜索索引显示法律状态更新至 2026-09-13，但页面直开本轮返回 HTTP 500。此处用于识别规则与版本边界，不替代美国律师对适用主体、触发条件、保存对象、例外及后续修法的核对。

| NCMEC 后代页面 | 已核实的内容 | 与 Play/开发者的关系和审计边界 |
| --- | --- | --- |
| [CyberTipline FAQ](https://report.cybertip.org/faqs) → [Other Resources](https://report.cybertip.org/other-resources) | 公众可以不留联系方式举报；NCMEC 审阅并向执法机关转交；页面还链接受害者支持和平台移除资源。[CCRI](https://cybercivilrights.org/ccri-crisis-helpline/) 与 [StopNCII](https://stopncii.org/) 成人非自愿影像求助页已打开；[FBI IC3](https://www.ic3.gov/Home/ComplaintChoice/default.aspx/) 本轮返回 Cache miss。 | 公众举报/受害者支持，不是 Play 开发者认证。成人影像渠道不属于儿童安全政策要求；NCMEC 其他页眉、页脚和机构导航未穷尽。 |
| [CyberTipline Reporting API](https://report.cybertip.org/ispws/documentation/index.html) → [生产入口](https://report.cybertip.org/ispws)、[测试入口](https://exttest.cybertip.org/ispws)、[公开表单](https://report.cybertip.org/cybertip/)、[curl 文档](https://curl.se/docs/) | API 正文、40 个内部目录章节、工作流和 schema 附录已阅读。生产根路径跳回文档，测试路径经文档链接跳到测试版文档；status 与生产 XSD 需认证；未登录、未注册、未发起报告，也未提交表单。公开表单目标无可提取正文；curl 官方文档总览已打开。 | API 使用资格与凭据由 NCMEC 控制。XML 字段和动态 XSD 未逐字段审计；访问细节见逐 URL 台账（快照：`../source-page-audit.csv`，未导入本仓库）。 |
| [Take It Down](https://takeitdown.ncmec.org/) → [FAQ](https://takeitdown.ncmec.org/faq/)、[隐私说明](https://takeitdown.ncmec.org/privacy-policy/)、[参与平台](https://takeitdown.ncmec.org/participants/)、[资源与支持](https://takeitdown.ncmec.org/resources-and-support/)、[一页指南 PDF](https://takeitdown.ncmec.org/wp-content/uploads/2026/07/takeitdown-how-it-works-handout_updated_6-24-26.pdf) | 免费工具面向图像拍摄时未满 18 岁的人，包括现在已成年的幸存者；原图留在设备上、当地生成哈希，参与平台可在公开/未加密服务比对。FAQ 强调只选设备上已有图像，不要为提交而下载或转发；服务不能保证阻止所有网站传播。动态参与者页本轮列出 25 家。资源页把 NCMEC CyberTipline、直接联系平台和美国境内支持分别列为不同路径。 | 可选的受害者支持/移除途径，不替代开发者举报、Play 处置流程或法律义务。开发者不应要求受害者把图像上传到应用来使用此工具。首页“Get Started”链接目标 [tidsubmit.ncmec.org](https://tidsubmit.ncmec.org/) 于 2026-10-23 直接打开，但抓取结果无正文（0 行）；未开始表单、未选择或上传图像。流程边界依据可读首页、FAQ 和隐私说明，不推测该动态表单的字段。 |
| Take It Down [隐私说明](https://takeitdown.ncmec.org/privacy-policy/) | 与首页“仅向 NCMEC 提供哈希”的简述合读后发现：隐私说明补充 NCMEC 可能读取所选文件名，建议文件名不要含姓名、生日等识别信息；还说明必要 Cookie、服务商披露和保留期限。 | 工具自身的隐私实践。应同时保留“图像本身不上传”和“文件名可能可见”，避免只摘首页而漏掉隐私限定。 |
| [Is Your Explicit Content Out There?](https://www.missingkids.org/gethelpnow/isyourexplicitcontentoutthere) → [Victim, Survivor & Family Support](https://www.missingkids.org/gethelpnow/support) | NCMEC 将 CyberTipline、Take It Down、直接联系平台列为不同可选途径；平台指引数量较多。美国境内另有受害者/家庭心理支持与转介页。 | 受害者求助和内容移除导航，不是 Google Play 开发者政策；逐平台页面和全部后代未穷尽。 |
| [18 U.S.C. § 2258A](https://www.govinfo.gov/content/pkg/USCODE-2024-title18/html/USCODE-2024-title18-partI-chap110-sec2258A.htm) · [§ 2258E](https://www.govinfo.gov/content/pkg/USCODE-2024-title18/html/USCODE-2024-title18-partI-chap110-sec2258E.htm) · [REPORT Act](https://www.govinfo.gov/app/details/PLAW-118publ59) | 官方 U.S. Code / GovInfo 页面全文可读。§2258A 含报告触发点、可选报告信息、不主动监控条款、一年保存和安全访问约束；§2258E 定义法定 provider；GovInfo 确认 Pub. L. 118-59 于 2024-05-07 批准。 | 美国联邦法按法定服务、主体及触发条件适用；其他辖区另行判断。它与 Play 平台政策并行，不能相互替代。 |

**产品团队核对项：**确认服务是否可能属于美国法定义的电子通信/远程计算服务；由律师确认 § 2258A 触发、报告和一年保存范围；如使用 NCMEC API，另核对凭据、字段、草稿/完成语义、数据存放/删除和访问控制。Play 侧仍独立落实公开标准、应用内反馈、内容处置、Console 自我认证和儿童安全联系人。不要把 Tech Coalition 对“美国企业”的描述推广成普遍法律结论，也不要因 §2258A(f) 推断其他法律或 Play 政策没有监测/响应要求。

以上页面及认证/抓取限制逐 URL 登记。完整 XML 字段目录、NCMEC 注册内容、全部受害者支持与社交平台页仍部分未展开；这里扩展 Play 政策相关后代，不声称递归覆盖 NCMEC、GovInfo 或第三方站点的所有链接。

## OCSEA 产品风险评估、工具与引文子链

Tech Coalition 的[评估介绍页](https://technologycoalition.org/resources/assessing-ocsea-harms-in-product-development/)于 2023-11-02 发布，并提供完整的[14 页产品开发评估 PDF](https://technologycoalition.org/wp-content/uploads/Assessing_OCSEA_Harms_in_Product_Development_FINAL.pdf)。介绍页明确说明，该材料聚焦 OCSEA，是用于内部讨论的自愿资源，不构成法律/监管意见或统一标准照护。PDF 给出一个可按产品修改的四步流程：

1. **定义功能场景：** 写明具体功能、目标和实际用户（包括儿童是否可能使用）、内容/数据、促成的关系，以及儿童和恶意行为者可能采取的下一步。
2. **枚举伤害与情境：** 使用 4Cs——内容（content）、接触（contact）、行为（conduct）、合同/商业关系（contract）——分析暴露、互动、行为、商业和过度使用风险；考虑匿名/临时内容、加密、支付、多媒体、语音视频、位置、个人信息、广告/第三方共享、通知和推荐等风险修饰因素。
3. **估计固有风险：** PDF 举例将各类伤害可能性与对发现 OCSEA 能力的影响相加，再乘以未成年人使用该功能的可能性；示例为 `(2+3+2+1+0)×3=24`。作者把分值、权重和量表定位为可调整的讨论工具，并提醒区分年龄段、留意偏差、随产品变化重复评估；这个数字不是 Play 风险等级或合格阈值。
4. **选择并验证缓解措施：** 结合政策、举报、可信度较高的主动检测和人工复核、安全教育、减少强迫使用的设计、年龄/行为限制等措施评估残余风险；持续检查措施效果、规避方式和风险变化。

该评估模型可帮助团队把风险分析落实到功能和迭代，但不能替代 Play 的公开儿童安全标准、应用内反馈、CSAM 处置、适用法律合规、Play Console 自我认证及联系人要求。评分模型也不应被当成量化安全保证。

| 评估分支中的页面/引用 | 本轮核验与摘要 | 关系和限制 |
| --- | --- | --- |
| [Tech Coalition Child Safety Best Practices](https://technologycoalition.org/resources/child-safety-best-practices/) | 2024-09-15 的另一篇公开指南已读；包含 NCMEC 注册/报告 API 的建议以及类似的举报、检测、执行和安全设计链。 | 与 2024-10-14 开发者指南并列记录；不推断新旧优先级，也不把建议提升为 Play 强制条款。 |
| [Pathways](https://technologycoalition.org/programs/pathways/) 的[条款](https://technologycoalition.org/programs/pathways/terms-and-conditions/)与[隐私说明](https://technologycoalition.org/privacy/) | 项目页说明面向管理 UGC/通信服务的科技公司员工，提供咨询、资源和同业学习。条款涉及账号责任、保密、材料的个人/非商业内部使用及无担保/非法律意见；隐私页解释表单、Cookie、分析数据和跨境处理。 | 计划参与是自愿且不属于 Play 要求；本轮没有提交申请表或创建账号。使用其材料须遵守页面条款，不能把会员/私有资源视为已审阅。 |
| [NCMEC ESP 注册](https://esp.ncmec.org/registration) 与 [CyberTipline](https://report.cybertip.org/) | CyberTipline 公共入口已有单独摘要；本轮再次打开 ESP 注册目标仍未返回可提取正文。 | 注册资格、报告义务、时限和保存规则不能从空白页面或行业指南推定，应查适用法律及当前 NCMEC 说明。 |
| [INHOPE 国家热线目录](https://inhope.org/) | 动态目录可打开并列出各国/地区热线；国家目的页未逐一展开。 | 路由辅助信息，不替代当地主管机关或法律意见。 |
| [5Rights：But How Do They Know It Is a Child?](https://5rightsfoundation.com/uploads/But_How_Do_They_Know_It_is_a_Child.pdf) | 57 页指南已打开；强调年龄保障并非万能方案，需兼顾数据最少化、隐私保护、比例性、可用性、包容性、安全、申诉、透明和儿童权利。 | 英国/儿童权利与年龄保障指导；不是 Google Play 年龄核验技术标准。该 PDF 的全部脚注后代未穷尽。 |
| [eSafety Safety by Design assessment tools](https://www.esafety.gov.au/industry/safety-by-design/assessment-tools) 与[隐私说明](https://www.esafety.gov.au/industry/safety-by-design/privacy) | 澳洲 eSafety 页面介绍 Start-up 与 Enterprise 两套自评工具、约 45–90 分钟模块及结果报告；隐私说明称答案聚合并有删除期限。登录/代码入口可见但工具内部题目未抓取。 | 可作产品治理自评参考，不是 Play 认证或法律判断。 |
| [eSafety: Anonymity](https://www.esafety.gov.au/industry/tech-trends-and-challenges/anonymity) | 页面同时描述匿名带来的隐私/表达/防骚扰益处和虚假账号、诱骗、重复账号规避风险；单纯取消匿名不能消除滥用。 | 风险平衡背景资料；不能据此推导 Play 对所有产品的身份核验要求。 |
| [NIST 固有风险](https://csrc.nist.gov/glossary/term/inherent_risk) / [残余风险](https://csrc.nist.gov/glossary/term/residual_risk) | 两个词汇表定义均已打开；分别指没有直接风险应对措施时的风险，以及实施安全控制/响应后仍保留的风险。 | 仅帮助解释 PDF 的风险术语，不是儿童安全规则。 |
| [World Economic Forum 在线伤害分类工具包](https://www.weforum.org/reports/toolkit-for-digital-safety-design-interventions-and-innovations-typology-of-online-harms/) 及[2023 PDF](https://www3.weforum.org/docs/WEF_Typology_of_Online_Harms_2023.pdf) | 原引用页缓存未命中；官方 PDF 搜索摘要可见，但完整 PDF 打开超时。 | 仅登记可核对的书目信息/摘要，不把未读内容作为分析依据。 |
| [4Cs of Online Risk](https://core-evidence.eu/posts/4-cs-of-online-risk) 与[联合国《儿童权利公约》](https://www.ohchr.org/en/instruments-mechanisms/instruments/convention-rights-child) | Tech Coalition PDF 所引 CO:RE 旧 4Cs URL 返回 404；另找到 CO:RE 当前 4Cs 页面并读全文。OHCHR 公约页返回 403。 | 旧 CO:RE URL 本身不可读，现行替代页已在下一行单独核验；OHCHR 公约原文未能读取，未据此推断条约内容。 |
| [CO:RE 现行 4Cs 短报告页](https://core-evidence.eu/updating-the-4cs-of-online-risk/) | 当前页全文已打开：定义 content/contact/conduct/contract，并指出儿童隐私、健康、公平待遇等横切风险；类别会交叠、混合，分类旨在组织讨论和进一步调查。 | 这是研究分类，不是法律判定或 Play 分类；旧 `/posts/4-cs-of-online-risk` 返回 404，没有观察到旧 URL 自动跳转。 |
| [CO:RE《Understanding online risks for children》](https://core-evidence.eu/posts/online-risks-takeaways) | 全文已读；介绍多学科的在线风险视角，强调概率与严重程度、情境差异、儿童参与/机会与风险并看，并链接 4Cs 新分类。 | 背景研究材料。页面还链接了历史论文、演讲资料和 EU/UN 儿童权利资料，未穷尽所有脚注与通用导航。 |
| CO:RE 4Cs 更新页 → [儿童安全从业者论坛报告 PDF](https://core-evidence-eu.s3.amazonaws.com/documents/WP5_online-forum-III_event-report.pdf) | 2021 年 9 页报告已读；记录 Insafe/INHOPE 从业者认为分类有助于比较、趋势、沟通和培训，同时指出分类须适应商业化、数据化、混合风险与各年龄/辖区差异。 | 研究/实践者讨论，不是监管义务或 Play 审核标准。 |
| CO:RE 在线风险页面 → [演讲资料 PDF](https://core-evidence-eu.s3.amazonaws.com/documents/speaker-presentations-pdf.pdf) | 25 页活动演讲材料已打开；包括犯罪学、法律、传播学和心理学视角。 | 仅作为研究背景；没有将演讲材料扩写为 Google Play 要求。 |
| [LSE《Classifying and responding to online risk to children》](https://www.lse.ac.uk/business/consulting/reports/classifying-and-responding-to-online-risk-to-children) 与[报告 PDF](https://www2.lse.ac.uk/business/consulting/assets/documents/Classifying-and-responding-to-online-risk-to-children-Good-practice-guide.pdf) | 2023-02 的官方报告介绍页已读；介绍其面向欧洲儿童在线风险的从业者指南，含内容、接触、行为、合同四类及案例/支持建议。下载 PDF 目标超时；搜索索引仅显示部分摘要，不能当成全文。 | 欧洲委员会/European Schoolnet 项目背景下的专业实践资料，不是 Play 政策；报告全文仍未读。 |
| [LSE 对《General Comment No. 25》的说明](https://blogs.lse.ac.uk/parenting4digitalfuture/2021/03/24/general-comment-25/) 与 [UN Treaty Body Database 条目](https://tbinternet.ohchr.org/_layouts/15/treatybodyexternal/Download.aspx?Lang=en&symbolno=CRC%2FC%2FGC%2F25) | LSE 页面已读，概述儿童在数字环境中的隐私、平等、保护、教育、游戏等权利；官方入口显示 GC 25 多语种文档列表，但抓取未拿到正文附件。 | LSE 页面是解释性文章，联合国文件是权利背景；均不等同于 Google Play Child Safety Standards。 |
| [欧盟儿童权利战略与欧洲儿童保障](https://commission.europa.eu/strategy-and-policy/policies/justice-and-fundamental-rights/rights-child/eu-strategy-rights-child-and-european-child-guarantee_en) | 从 CO:RE 页面进入后观察到旧欧委会 URL 重定向至当前页面；本轮打开政策框架介绍及部分正文，提到 2021 战略、儿童参与及跨部门保护。 | 欧盟政策背景，正文和其数十个项目/政策子链并非本轮 Play 政策范围，不把它们写作全球开发者义务。 |
| [LSE 2023 儿童在线风险指南介绍博客](https://blogs.lse.ac.uk/parenting4digitalfuture/2023/02/08/4cs-guide/) | 直接打开返回 403；搜索索引显示该页介绍 2023 Good Practice Guide、四类案例和从业者建议。 | 仅保留索引级摘要；不替代可读的 LSE 官方报告介绍页，也不推断其未显示正文。 |
| [PHVSpec 视频感知哈希基准](https://technologycoalition.org/resources/phvspec-a-benchmark-based-analysis-of-perceptual-hash-systems-for-videos/) 与 [Lantern 2023 透明度报告](https://technologycoalition.org/resources/lantern-transparency-2023/) | 两个 Tech Coalition 相关资源介绍页已打开。PHVSpec 是视频感知哈希系统比较研究；Lantern 页面是截至 2023-12-31 的历史项目统计。 | 研究/项目背景，不要求开发者采用特定检测产品；Lantern 统计不是普通 Play 应用的基准或目标。 |

**来源与递归边界：** 2024-09-15、2024-10-14 两篇指南、2023 风险评估介绍页和 PDF 及上表中可读的一层引用已纳入台账。对引用材料的脚注、工具供应商 API、动态目录中每个国家热线、第三方站点的通用导航/全部后代没有作无限递归声明；受限和失败目标逐 URL 记在 source-page-audit.csv（快照：`../source-page-audit.csv`，未导入本仓库）。外部自愿建议、澳洲/英国材料和研究资料都与 Google Play 强制条款分层呈现。

Google 帮助页另有 32 条 “Policy education and app requirements” 推荐。它们是页面侧栏推荐，不是政策正文强制条款；32 个条目含当前页自身这一重复目标。以下逐项登记实际链接，括号中标出本地专题或访问状态。首次批量核验时 31/32 次返回目标页正文；金融功能申报页 `13849271` 随后重试已成功打开并补入[金融与贷款](../financial-services-and-loans/financial-services-and-loans.zh-CN.md)专题。成功打开仅表示目标可访问，不代表每一行都有独立全文摘要；尚需单独专题的条目仍留在工作队列。

| # | 侧栏目标 | 本地专题与状态 |
| --- | --- | --- |
| 1 | [Understanding Google Play’s Payments policy](https://support.google.com/googleplay/android-developer/answer/10281818) | [付款与订阅](../payments/payments-and-subscriptions.zh-CN.md)；正文已打开，专题含主要付款规则。 |
| 2 | [Understanding Google Play's Service Fee](https://support.google.com/googleplay/android-developer/answer/11131145) | [付款与订阅](../payments/payments-and-subscriptions.zh-CN.md)；已摘要服务费说明及比例概述，并标注旧的韩国/印度 4% 说明不覆盖现行费率。 |
| 3 | [Understanding Google Play's Better Ads Experiences policy](https://support.google.com/googleplay/android-developer/answer/12271244) | 广告与推广（快照：`ads-and-advertising.md`，未导入本仓库）；已摘要插屏时机、自然停顿、奖励广告、启动后展示及 SDK 责任，并区分外部 Better Ads 标准。 |
| 4 | [Understanding Google Play's VpnService policy](https://support.google.com/googleplay/android-developer/answer/12564964) | [敏感权限](../sensitive-permissions/sensitive-permissions.zh-CN.md)；已摘要许可类别、声明、披露同意与两段审核视频；2023-08-31 是已过期历史期限。 |
| 5 | [Moderation requirements and incidental sexual content in UGC apps](https://support.google.com/googleplay/android-developer/answer/12923286) | [UGC 与审核](../user-generated-content/user-generated-content.zh-CN.md)；正文和最佳实践已整理。 |
| 6 | [App account deletion requirements](https://support.google.com/googleplay/android-developer/answer/13327111) | [账号删除](../account-deletion/account-deletion.zh-CN.md)；正文和主要操作要求已整理。 |
| 7 | [Foreground service and full-screen intent requirements](https://support.google.com/googleplay/android-developer/answer/13392821) | 前台服务与地理围栏（快照：`foreground-services-and-geofencing.md`，未导入本仓库）；正文已整理。 |
| 8 | [Understanding Google Play’s Spyware policy](https://support.google.com/googleplay/android-developer/answer/14745000) | 间谍软件专题（快照：`spyware-and-data-exfiltration.md`，未导入本仓库）；已独立摘要数据外传/SDK 例子、监控应用边界、isMonitoringTool 和直接子资源。 |
| 9 | [Requirements for news and magazine apps](https://support.google.com/googleplay/android-developer/answer/10523915) | [新闻与杂志](../news-and-magazines/news-and-magazines.zh-CN.md)；正文和申报要求已整理。 |
| 10 | [Update on COVID-19 guidelines](https://support.google.com/googleplay/android-developer/answer/9889712) | 健康应用（快照：`health-apps-and-health-connect.md`，未导入本仓库）；页面说明健康功能转由现行 Health Apps policy 管辖，已交叉登记。 |
| 11 | [Requirements for distributing apps in specific countries/regions](https://support.google.com/googleplay/android-developer/answer/6223646) | [国家/地区分发要求](../country-specific-distribution/country-specific-distribution.zh-CN.md)；已逐市场摘要巴西、欧盟、日本、韩国、以色列、印度、越南，并登记主要法律/API/机构子链和访问限制。 |
| 12 | [Requirements for apps that communicate government information](https://support.google.com/googleplay/android-developer/answer/9514050) | 本轮已打开；政府关联应用可能需提交授权证明，未关联应用须标明信息来源且不得暗示官方身份；须完成政府应用声明。 |
| 13 | [Android Health Permissions: Guidance and FAQs](https://support.google.com/googleplay/android-developer/answer/12991134) | 健康应用（快照：`health-apps-and-health-connect.md`，未导入本仓库）；权限用途和健康声明已交叉整理。 |
| 14 | [Financial features declaration](https://support.google.com/googleplay/android-developer/answer/13849271) | [金融与贷款](../financial-services-and-loans/financial-services-and-loans.zh-CN.md)、[加密资产](../crypto-assets-and-nfts/crypto-assets-and-nfts.zh-CN.md)；本轮重试已完整打开，确认所有已发布应用均需申报、无金融功能也要申报，贷款功能还需提供合作方关系和适用牌照。表单及账号状态需登录。 |
| 15 | [Country/region allowances for gambling apps](https://support.google.com/googleplay/android-developer/answer/12256011) | 正文与 45 市场快照见[真钱赌博专题](../real-money-gambling/real-money-gambling.zh-CN.md)；在线申请表与当地许可仍须发布前复核。 |
| 16 | [Advertising ID](https://support.google.com/googleplay/android-developer/answer/6048248) | AAID 专题（快照：`advertising-id.md`，未导入本仓库）；已逐项登记 11 个正文目标。儿童专用应用不得传输儿童标识符；目标 API 33+ 时不得请求 AD_ID。混合受众不得传输儿童或年龄未知用户的标识符。旧页日期为历史上线说明。 |
| 17 | [System services](https://support.google.com/googleplay/android-developer/answer/12085265) | 系统服务与预装软件豁免专题（快照：`system-services-and-preinstalled-software.md`，未导入本仓库）；公开定义仅确认“支持核心系统功能的预装软件”，资格和豁免范围需在 Partner Center 核实。 |
| 18 | [Using SDKs safely and securely](https://support.google.com/googleplay/android-developer/answer/13326895) | 第三方 SDK（快照：`sdk-requirements.md`，未导入本仓库）；开发者对 SDK 数据/权限与合规负责，已整理。 |
| 19 | [On-device Android container apps and REQUIRE_SECURE_ENV](https://support.google.com/googleplay/android-developer/answer/13609005) | 设备与网络滥用专题（快照：`device-and-network-abuse.md`，未导入本仓库）已总结容器定义、`REQUIRE_SECURE_ENV`、企业工作资料例外，以及容器应用检查并尊重该标志的要求。 |
| 20 | [Health app categories and additional information](https://support.google.com/googleplay/android-developer/answer/13996367) | 健康应用（快照：`health-apps-and-health-connect.md`，未导入本仓库）；类别与申报要求已交叉整理。 |
| 21 | [Understanding Google Play's AI-Generated Content policy](https://support.google.com/googleplay/android-developer/answer/14094294) | [UGC 与审核](../user-generated-content/user-generated-content.zh-CN.md)；AI 生成内容规则已整理。 |
| 22 | [General conditions of access for Google Play in the EEA](https://support.google.com/googleplay/android-developer/answer/14659200) | EEA [通用访问条件](../eea-general-conditions/eea-general-conditions.zh-CN.md)；正文 38 个链接/锚点均已尝试，付款、项目、DDA、申诉、产品导航和受限目标分别归类；与 DDA/项目条款的关系及费率差异已整理。 |
| 23 | [Learning more about Child Safety Standards](https://support.google.com/googleplay/android-developer/answer/14747720) | 本页；自身推荐项，避免重复计作新节点。 |
| 24 | [Requirements for providing sign-in details for review](https://support.google.com/googleplay/android-developer/answer/15748846) | Play Console/审核流程专题已交叉引用；正文此前已打开。 |
| 25 | [How to declare a news and magazine app](https://support.google.com/googleplay/android-developer/answer/16189314) | [新闻与杂志](../news-and-magazines/news-and-magazines.zh-CN.md)；已纳入申报字段、实体类型、聚合应用和联系方式要求。 |
| 26 | [Cryptocurrency exchanges and software wallets policy](https://support.google.com/googleplay/android-developer/answer/16329703) | [加密资产](../crypto-assets-and-nfts/crypto-assets-and-nfts.zh-CN.md)；正文已纳入专题。 |
| 27 | [Flexibility for EEA app distribution](https://support.google.com/googleplay/android-developer/answer/16232690) | [付款与订阅](../payments/payments-and-subscriptions.zh-CN.md)；已区分 DMA 合同豁免与计费/站外分发计划。 |
| 28 | [Best Practices to Safeguard AI-Generated Content](https://support.google.com/googleplay/android-developer/answer/16353813) | [UGC 与审核](../user-generated-content/user-generated-content.zh-CN.md)；最佳实践正文及 10 个直接安全资源已整理。 |
| 29 | [Changes to the external offers program for users in the EEA](https://support.google.com/googleplay/android-developer/answer/16505463) | [付款与订阅](../payments/payments-and-subscriptions.zh-CN.md)及 [EEA 通用访问条件](../eea-general-conditions/eea-general-conditions.zh-CN.md)；公告是当前 External Offers 条款的短入口，费率/资格/操作以现行项目帮助页为准。 |
| 30 | [Changes to Google Play for upcoming app store bills in U.S. states](https://support.google.com/googleplay/android-developer/answer/16569691) | 本页下方新增美国州法/年龄信号快照；与 Google Play 通用年龄限制政策分开。 |
| 31 | [Apps with incidental dating or matchmaking features](https://support.google.com/googleplay/android-developer/answer/16838200) | [年龄限制与儿童安全](../age-restricted-child-safety/age-restricted-child-safety.zh-CN.md)；本轮已打开，未规定特定技术，但年龄门槛须有效、合理且不易绕过。 |
| 32 | [Preview: foreground service and full-screen intent requirements](https://support.google.com/googleplay/android-developer/answer/16965181) | 前台服务与地理围栏（快照：`foreground-services-and-geofencing.md`，未导入本仓库）；预览正文已交叉整理。 |

### 美国州级年龄保障立法与 Play 支持工具（截至 2026-10-22）

Google 的[州级应用商店法说明](https://support.google.com/googleplay/android-developer/answer/16569691?hl=en)介绍了年龄保障、家长批准和重大变更通知等州法要求，并将 Play Age Signals API、Play Console 通知和应用内商品年龄分级作为可供开发者评估的工具。Google 明确表示不会替每个开发者判断法律是否适用，也不要求开发者仅因该说明而采用这些工具；开发者仍须自行判断地域、产品和法律适用范围。

截至本次核对，Google 页面称 Texas SB 2420 已于 2026-01-01 生效；第五巡回上诉法院于 2026-06-04 暂停了此前的初步禁令，案件实体争议仍在上诉中。法院的 stay 是诉讼中的临时程序决定，不能解释为对法律实体问题的最终裁决。Texas 法条针对应用商店及应用开发者规定了账户年龄类别、家长关联/同意、每个应用与应用内购买的年龄分级、重大条款或隐私变化通知，以及年龄信号和同意状态的用途限制。年龄类别包括未满 13 岁、13–15 岁、16–17 岁和成年人。以下是 Texas 法与诉讼状态的摘要，不是所有州的统一 Play 政策。

| 直接或权威相关目标 | 关系与本地摘要 | 核验状态 |
| --- | --- | --- |
| [Google Play 州级法说明](https://support.google.com/googleplay/android-developer/answer/16569691?hl=en) | 年龄信号 beta、Console 重大变更通知/报告和应用内商品 SKU 年龄分级；说明家长可批准下载、购买及重大变更，拒绝重大变更不会自动撤销已安装应用的访问。 | 正文已打开；所列 API 版本 `0.0.4` 是该次核验时页面推荐的版本，需查当前 API 文档。 |
| [Google Blog 年龄保障立法提案](https://blog.google/company-news/outreach-and-initiatives/public-policy/google-legislative-proposal-for-keeping-kids-safe-online/) | Google 年龄保障立法提案的政策背景。 | Google 页面链接跳转后已打开；这是提案背景，不是生效法律。 |
| [LegiScan 上的 Texas SB 2420 文本](https://legiscan.com/TX/text/SB2420/id/3237346) | Google Help 页面直接链接的法案副本。 | 已打开；这是第三方托管副本，法律义务以 Texas Legislature 正式法案为准。 |
| [Texas SB 2420 最终法案](https://capitol.texas.gov/tlodocs/89R/billtext/html/SB02420F.htm) | Texas 法条原文；对商店年龄验证/家长关联和开发者分级、变更通知、年龄信号处理规定责任。 | Texas Legislature 正式法案全文已打开；州法义务与 Play 政策分开记录。 |
| [Texas SB 2420 立法历史](https://capitol.texas.gov/billlookup/History.aspx?Bill=SB2420&LegSess=89R) | 官方立法历史用于核对 2026-01-01 生效日期。 | 官方记录已检索；时间状态按本次核验日保存。 |
| [第五巡回法院 stay 命令](https://www.ca5.uscourts.gov/opinions/pub/26/26-50001-CV0.pdf) | 暂停普遍性初步禁令，等待上诉；不是实体判决。 | 2026-06-04 法院 PDF 已打开。 |
| [Age Signals API 概览](https://developer.android.com/google/play/age-signals/overview) | 说明应用如何请求 Play 提供的年龄/监督等信号；实现指南不是对州法适用性的法律判断。 | 官方 Android Developers 页面已打开；[与国家/地区分发专题](../country-specific-distribution/country-specific-distribution.zh-CN.md)技术说明互链。 |
| [年龄信号敏感数据要求](https://support.google.com/googleplay/android-developer/answer/16558241?hl=en) | 年龄保障相关 API 数据的访问、用途与声明限制。 | 当前 Help 页面已打开；旧链接重定向至此。 |
| [Family Link 监督说明](https://support.google.com/families/answer/9055704) | Google 账号监督和家长控制背景；不等同于 Texas 法定同意流程。 | Google Families 页面已打开。 |
| [创建应用内商品](https://support.google.com/googleplay/android-developer/answer/1153481) | Play Console 商品配置入口；Texas 可能要求对每个应用内商品单独分级，区别于应用整体内容分级。 | 正文已打开；具体商品字段应登录 Console 核查。 |
| [Google Play Developer API](https://developers.google.com/android-publisher) | 程序化管理 Play 应用/商品的 API 概览。 | 官方开发者页面已打开；API 方法与授权子项未穷尽。 |
| [Google Play 购买审批](https://support.google.com/googleplay/answer/7039872) | 家庭组购买审批的用户侧设置；只适用于通过 Google Play Billing 的购买。 | Google Play Help 页面已打开。 |
| Google 支持与 Play Console 年龄信号页面 | 正文链接中的支持和登录后 Console 路由未解析出可核实目标地址。 | 目标路由未公开解析；不推断账户功能或申报字段。 |

### Play Age Signals API：条款、共享流程与直接子链

API 概览页的专属条款（页面标注最后修改于 2025-10）把 API 用途限于依法提供适龄内容/体验；禁止广告、营销、用户画像和分析。API 仅供通过 Google Play 更新的应用调用，返回信息只能由发起请求的应用使用。违规可能导致 API 访问终止及应用暂停或下架。概览页称 Age Signals 客户端库本身不收集数据，但开发者仍须按自己的应用数据流判断 Data safety 回答；不能把“库本身不收集”解读为应用整体无需申报。

实现上先请求共享状态，再按状态处理：`SHARED` 才调用 `checkAgeSignals()`；`NOT_SHARED` 不返回年龄信号；`VERIFICATION_REQUIRED` 表示适用地区要求先在 Play 商店完成年龄验证/监督设置。其他地区按用户或家长的全球/单应用选择显示提示。Play 返回年龄区间而非生日；默认区间为 0–12、13–15、16–17、18+，自定义分段须在 Console 设置。显著变更审批仅适用于受监督用户；开发者要自行判断法律触发条件，并按审批状态限制相关内容/功能。

| Age Signals 直接子页面 | 页面内容与关系 / 核验状态 |
| --- | --- |
| [Play Age Signals 概览](https://developer.android.com/google/play/age-signals/overview) | SDK 0.0.4、API 适用范围、专属条款及 Data safety 说明。概览正文/条款页已打开；条款不是 DDA 或 Play 政策的替代。 |
| [Request age signals](https://developer.android.com/google/play/age-signals/request-age-signals) | 记录 `SHARED` / `NOT_SHARED` / `VERIFICATION_REQUIRED` 流程；美国适用州通过 Play 商店完成验证或监督设置，其他地区依据用户/家长分享设置处理。页面标注 2026-09-22 更新；Kotlin/Java 示例已核对。 |
| [About age range sharing on Google Play](https://support.google.com/googleplay/answer/17232873) → [Manage your child's Google Play apps](https://support.google.com/families/answer/7103028) | 面向用户的年龄分享设置说明：全球默认 “Ask before sharing”，可按全局或单应用调整；受监督账号由家长在 Family Link 控制。直接子页说明家长可在 Family Link → Google Play → Age sharing 中允许或禁止向所有应用分享，并会通知孩子设置变化。Google Play 分享年龄段和年龄来源，不提供确切生日。它解释用户控制流程，不授予开发者超范围使用权；Family Link 页内的其他设备管理侧栏不是 Play 开发者规则。 |
| [Understand age signals responses](https://developer.android.com/google/play/age-signals/understand-age-signals-responses) | 解释年龄来源 `TIER_A`–`TIER_D`、上下界、`significantChangeStatus`、批准日期及监督安装 ID；可选自定义年龄段最多 3 个最小年龄、相邻至少相差 2 岁且每年最多更改一次。关联的 [Age signals Console](https://play.google.com/console/developers/app/age-signals) 需开发者登录。该页建议可选使用 [Play Integrity API](https://developer.android.com/google/play/integrity/overview) 减少伪造/滥用，不是年龄信号资格要求。 |
| [Test your Play Age Signals API integration](https://developer.android.com/google/play/age-signals/test-age-signals-api) | 用 `FakeAgeSignalsManager` 模拟同意/拒绝、不同年龄来源和审批状态；License Tester 可测试通过 Play 发布检查的实时集成。页面最后更新 2026-10-06，并链接错误码表。 |
| [Play Age Signals API error codes](https://developer.android.com/google/play/age-signals/handle-errors) | 网络/服务暂时故障可有限重试；`APP_NOT_OWNED` 和 `SDK_VERSION_OUTDATED` 不应循环重试，应提示从 Play 安装或升级应用。错误表和建议已打开；页面的 [Developer support](https://support.google.com/googleplay/android-developer/gethelp) 链接跳转到账号专属 Console 支持，无法公开读取。 |
| [Notify Google Play of significant changes](https://developer.android.com/google/play/age-signals/notify-significant-changes) | 开发者负责判断适用法律是否要求通知。Console 提交未来生效日和面向家长的英文描述；最多提前 90 天登记 3 项，彼此至少间隔 2 天；审批请求仅发往法律要求的地区，且仅受监督用户有 API 审批状态。未批准时须由应用限制相关功能。 |
| [Review revoked app approvals](https://developer.android.com/google/play/age-signals/revoked-app-approval) | `installId` 用于依法需要时通知家长撤销安装批准；不能用于其他目的，设备重置后不保留。Console 撤销记录导出为 CSV 并保留 90 天；家长重新批准且设备未重置时 ID 可复用。页面与 [Age signals Console](https://play.google.com/console/developers/app/age-signals) 已打开/核验；账号内数据需开发者登录查看。 |
| [Play Integrity API overview](https://developer.android.com/google/play/integrity/overview) | Age Signals 响应指南把它作为可选防伪信号；其设备/应用完整性和服务端反滥用建议属于另一条 API 安全分支，不改变年龄信号政策用途限制。见Play Integrity API 双语专题（快照：`play-integrity-api.md`，未导入本仓库）；API 正文已打开，较深后代仍未穷尽。 |
| [Google APIs Terms of Service](https://developers.google.com/terms) | Age Signals 专属条款之外的 API 通用条款；适用法律、隐私、用户数据保护与 API 使用约束并行适用。正文已打开；Google APIs ToS 于 2021-11-09 修改，冲突时专属附加条款优先。 |
| Play 法律与数据声明交叉页面 | [Developer Distribution Agreement](https://play.google/developer-distribution-agreement.html)、[Developer Program Policies](https://play.google/developer-content-policy/)、[现行敏感权限/User Data 条款](https://support.google.com/googleplay/android-developer/answer/16558241?hl=en)、[Data safety 开发者帮助](https://support.google.com/googleplay/android-developer/answer/10787469?hl=en) 与 [Data safety 用户说明](https://support.google.com/googleplay/answer/11416267) | 这些页面分别约束开发者关系、Play 政策、Age Signals 数据用途和应用数据申报/用户透明度；overview 直接链接已打开或由各双语专题独立复核。消费端 [Google Play Terms](https://play.google.com/intl/en-US_us/about/play-terms/index.html) 也在 overview 的 Data safety 段落出现，但属于消费者服务条款，不替代开发者 DDA/政策。 |

这条技术链通过 Age Signals 政策、User Data、DDA 和 Data safety 页面交叉回链；登录后 Console 页、API reference 全量成员、Play Integrity 的完整技术后代和通用站点导航仍部分待核。可用的政策/实现主链已入双语知识库，但不声称外链网络无限闭合。

Google 的 2026-10-22 页面快照还称不会更改国家/地区定向，开发者可在应用内按地域限制功能。应将此与 Play 商店发现/下载控制、支付计划资格和各州法律分别核对；任何一个不自动替代其他义务。

UGC 的适用范围、服务条款、举报/屏蔽以及性内容过滤另见[用户生成内容与审核专题](../user-generated-content/user-generated-content.zh-CN.md)。对于匿名/随机聊天，年龄屏蔽和 Child Safety Standards 不能替代 UGC 审核要求。

## Families 与目标受众申报

- 新应用和更新都要准确填写 Target audience and content。选择多个年龄段，意味着应用已为其中每个年龄段设计并确认适龄；不得仅为扩大覆盖而勾选儿童。
- Google 会结合应用实际内容、营销图像和用语判断申报是否准确。应用定位不是唯一依据。
- 目标受众包含儿童时，SDK/API、数据处理、广告、社交功能、内容、商店分级和当地儿童隐私法规都可能触发额外要求。
- 混合受众应用需以中性年龄屏幕隔离不适合儿童的广告/SDK，并对儿童或未知年龄用户使用符合 Families 要求的广告 SDK；不得向儿童投放个性化广告。
- Families 政策禁止儿童独立使用不适龄社交功能；儿童交换自由文本、媒体或个人信息时有应用内安全提醒、成人操作控制等额外要求。匿名聊天应用不得选择儿童受众。

### Families 政策正文的直接子链接

2026-10-23 再次打开了 [Google Play Families policies](https://support.google.com/googleplay/android-developer/answer/9893335?hl=en) 英文正文；主要条款与 2026-10-22 的双语核验相比无实质变化，并复核其正文链接目标。帮助页说明摘要与图示只是概览，发生冲突时以完整政策为准。下表中的“政策”表示约束性要求；“操作/技术”页解释如何申报或实现；法律和培训资源各有自己的适用边界。

| 正文子链接 | 页面与本地专题 | 与 Families 规则的关系及核验状态 |
| --- | --- | --- |
| Target audience and content | [Play Console 目标受众设置](https://support.google.com/googleplay/android-developer/answer/9867159) · 本页 | 操作指南。儿童受众会触发 Families；要按实际设计选择年龄段，声明广告、审核访问方式和隐私政策后再完成受众表单。该页提供年龄段示例与适龄设计建议；它们帮助申报，不会替代政策判断。旧帮助地址 `9285070` 已跳转至当前 `9867159`。正文已打开。 |
| App update / release information | [发布流程](https://support.google.com/googleplay/android-developer/answer/9859350) · [发布流程专题](../publishing/play-release-workflow.zh-CN.md) | 操作指南。目标受众信息在提交应用更新后才会反映到商店，但 Google 可能在新版本提交前先审核 Play Console 字段变更；正文建议把年龄组、广告或 IAP 变化告知现有用户。旧地址跳转已核对。 |
| Limited regions | [Enforcement Process](https://support.google.com/googleplay/android-developer/answer/9899234) · [执行与申诉专题](../enforcement-and-appeals/enforcement-and-appeals.zh-CN.md) | 执法/可用性说明。因特定地区儿童适龄性而仅在该地区提供时，其他地区用户不能从 Play 下载；已安装用户可继续使用，但不再收到更新；区域限制本身不影响开发者账号 standing。正文已打开。 |
| Personal and sensitive information / data practices | [User Data](https://support.google.com/googleplay/android-developer/answer/10144311) · [用户数据专题](../user-data/user-data.zh-CN.md) | 政策交叉引用。儿童数据经 API/SDK 收集也要披露并按政策处理；儿童专用应用及混合受众应用对持久设备标识符有额外限制。旧 `9888076` 地址重定向到现行页面；正文已打开。 |
| Families 应用数据实践实施指南 | [Data practices in Families apps](https://support.google.com/googleplay/android-developer/answer/11043825) · 广告 ID / App Set ID 专题（快照：`advertising-id.md`，未导入本仓库） · [用户数据专题](../user-data/user-data.zh-CN.md) · 第三方 SDK 专题（快照：`sdk-requirements.md`，未导入本仓库） | Families 专项操作指南：儿童或未知年龄用户不得传输 AAID、SIM/Build Serial、BSSID、MAC、SSID、IMEI、IMSI；不得从 `TelephonyManager` 请求电话号码。儿童专用应用可通过不声明/禁用 `AD_ID`（API 33+）或配置 SDK 阻止传输；无法阻止的 SDK 应移除。混合受众应用须等确认用户为成人后才允许传输 AAID。页面建议分析场景考虑 App Set ID，但这不是 Families 政策强制指定的唯一方案。其 App Set ID、旧 Advertising ID、当前 Families SDK 清单、年龄屏幕和醒目披露链接已逐项跟进；App Set ID 的 API/Tasks 子页及与 AAID/Play 规则的边界见广告标识符专题（快照：`advertising-id.md`，未导入本仓库）。2026-10-24 复核该分支：Families 数据实践页称 target API 29 或以上“可以”帮助阻止传输所列标识符，这是技术建议，不是当前 Play target API 最低版本要求。规范目标受众页 `answer/9867159` 再次打开并复核 neutral-age-screen：让用户自由输入生日，不应预填达标年龄，也不应提示必须达到某年龄才能进入；混合受众应用须据此隔离儿童不适宜广告。旧 `answer/9285070` 目标跳转到该现行页面。平台 API 与其他 SDK 后代仍部分覆盖。 |
| Data safety answers | [Data safety](https://support.google.com/googleplay/android-developer/answer/10787469) · [Data safety 专题](../data-safety/data-safety.zh-CN.md) | Play Console 申报。Families 要求答案真实反映应用与 SDK 的数据实践；数据安全表单不能替代隐私政策或用户数据义务。正文已打开，长 FAQ/变更记录仍部分待核。 |
| Precise location and sensitive permissions | [Sensitive Permissions](https://support.google.com/googleplay/android-developer/answer/16558241) · [敏感权限专题](../sensitive-permissions/sensitive-permissions.zh-CN.md) | 政策/权限交叉引用。仅以儿童为目标的应用不得请求位置权限，也不得收集、使用或传输精确位置；该限制在 Families 正文直接写明。敏感权限现行综合页和相关专题已打开；旧单项页面归并及其全部技术后代仍不算闭合。 |
| Bluetooth pairing | [Companion Device Manager API reference](https://developer.android.com/reference/android/companion/CompanionDeviceManager) | Android 技术实现参考。Families 要求申请 Bluetooth 时使用 CDM，除非应用只面向不兼容 CDM 的 OS 版本；API 文档不是儿童隐私政策的替代品。2,885 行 API 参考页已打开；类成员与版本兼容性仍须按目标设备核对，未把整份平台 API 目录当成 Play 规则。 |
| Neutral age screen | [Target audience 设置中的年龄分屏指引](https://support.google.com/googleplay/android-developer/answer/9867159#neutral-age-screen) · 本页 | 操作/实现指导。混合受众若使用不适用于儿童的 API/SDK，需通过有效中性年龄屏幕隔离，或证明儿童数据不会被收集；年龄屏幕不得诱导儿童谎报年龄。目标受众规范页正文已全文打开并读到该小节；单独片段 URL 请求失败，不代表规范页正文缺失。 |
| Content rating questionnaire | [Content Ratings](https://support.google.com/googleplay/android-developer/answer/9859655) · [内容分级专题](../content-ratings/content-ratings.zh-CN.md) | Play Console 申报。社交/分享功能须如实反映在 IARC 问卷中；应用分级、目标年龄和 Restrict Minor Access 是不同控制。正文已打开，地区评级机构等后代仍部分待核。 |
| Families Self-Certified Ads SDK Program | [计划要求](https://support.google.com/googleplay/android-developer/answer/9900633)、[具体 SDK 政策](https://support.google.com/googleplay/android-developer/answer/12918983)、[现行 SDK/版本清单](https://support.google.com/googleplay/android-developer/answer/12955712)、[水印/测试 APK 要求](https://support.google.com/googleplay/android-developer/answer/9536665) · 第三方 SDK 专题（快照：`sdk-requirements.md`，未导入本仓库） | 正式政策及动态清单。儿童或未知年龄用户看到的广告须使用适用的自认证 SDK 版本；不得投放个性化/兴趣定向广告或再营销。2026-10-23 复核仍暂停新申请、既有参加者要求不变；14 个 Maven 条目（含两个 Ad Manager 项）链接至 13 个不同供应商目标。厂商状态、AdMob 支持与 Play Families 自认证须分层：Google 名单仍列 `com.adcolony:sdk` 4.8.0+；DT 于 2026-06-16 说明 legacy SDK 等资产出售给 Affle，且不再服务于 DT 的统一平台战略；AdMob Android/iOS mediation 指南分别于 2026-09-11 / 2026-10-16 标记 AdColony 弃用并建议移除。现有资料未证明 Play 名单已撤销该 artifact，也未证明其所有构建均无法运行。Vungle artifact 与厂商 v7.x Maven 坐标不一致，详见双语第三方 SDK 专题（快照：`sdk-requirements.md`，未导入本仓库）。四个政策/帮助正文均已打开。`9536665` 明确要求所有广告素材有可识别库存标记，测试 APK 使用完整或镜像库存、运行合规 SDK 并覆盖全部实时广告；混合受众须能区分儿童/全年龄库存。新版申请表和培训课件仍分别受抓取/登录限制。 |
| Ads and monetisation / ad walls | [Ads policy](https://support.google.com/googleplay/android-developer/answer/9857753) · 广告与推广专题（快照：`ads-and-advertising.md`，未导入本仓库） | Families 页中的链接实际打开现行 Ads 政策（`answer/9857753`），没有单独的“广告墙”文章。Families 以无清晰关闭方式的全屏广告为例，并额外限制面向儿童的广告素材、干扰性广告及商业化方式。Ads 正文已打开；基线要求见广告专题。 |
| AdMob child-directed ad implementation | [Comply with Google Play’s Families Policy using AdMob](https://support.google.com/admob/answer/6223431) · [AdMob 分级与年龄处理](../content-ratings/content-ratings.zh-CN.md) | AdMob 实现指南，不是 Play 分发政策。说明儿童专用/混合受众广告请求、儿童广告分级、自认证 SDK 与 mediation 配置；开发者仍负责第三方广告网络合规。示例仍用旧 `setTagForChildDirectedTreatment`，而当前 Android/iOS Targeting 文档称 TFCD/TFUA 已弃用，须按实际 SDK 产品线核验。正文、最大广告分级、TFAT 帮助及 Android/iOS Targeting 和 API 目标已打开；登录侧栏和更深 SDK/API 目标仍未审阅。 |
| AdMob linked implementation resources | [Android GMA Next-Gen SDK](https://developers.google.com/admob/android/next-gen/sdk)、[iOS Google Mobile Ads SDK](https://developers.google.com/admob/ios/download)、[Advertising ID Help](https://support.google.com/googleplay/android-developer/answer/6048248) | 这些是 AdMob 页的技术/标识符后代，不是 Families 条文。Android Next-Gen SDK 1.5.0 与 iOS GMA SDK 13.11.0 属于不同产品线；父页中的 20.6.0/7.67.0 版本标签不能直接与之比较。Advertising ID Help 的 2021/2022 时间点属历史说明；儿童标识符应以现行 Families/User Data/DPP 为准。三页均已打开。 |
| AdMob → TFAT 的 Android 实现与年龄保护 | [Android Targeting 指南](https://developers.google.com/admob/android/next-gen/targeting) · [`RequestConfiguration`](https://developers.google.com/admob/android/next-gen/reference/com/google/android/libraries/ads/mobile/sdk/common/RequestConfiguration) · [`RequestConfiguration.Builder`](https://developers.google.com/admob/android/next-gen/reference/com/google/android/libraries/ads/mobile/sdk/common/RequestConfiguration.Builder) · [`MobileAds`](https://developers.google.com/admob/android/next-gen/reference/com/google/android/libraries/ads/mobile/sdk/MobileAds) · [儿童广告保护](https://support.google.com/adspolicy/answer/14170968) · [青少年广告保护](https://support.google.com/adspolicy/answer/12205906) | Android Targeting 正文与三个 API 参考页已打开；儿童/青少年保护是 Google Ads 的广告投放规则，不是 Play 政策条款。详见下方 TFAT 小节；该指南更新快，须按实际 GMA SDK 产品线复核。 |
| AdMob → TFAT 的 iOS 实现与年龄保护 | [iOS Targeting 指南](https://developers.google.com/admob/ios/targeting) · [`GADRequestConfiguration`](https://developers.google.com/admob/ios/api/reference/Classes/GADRequestConfiguration) · [`GADMobileAds`](https://developers.google.com/admob/ios/api/reference/Classes/GADMobileAds) · [iOS 发布说明](https://developers.google.com/admob/ios/rel-notes) · [iOS mediation 总览](https://developers.google.com/admob/ios/mediation) | iOS Targeting 正文于 2026-10-21 更新；API、发布说明和 mediation 页面已打开，18 个 adapter 指南也已逐项打开并检查年龄信号变更记录。iOS 表与 Android Next-Gen 表属于不同 SDK 产品线的动态版本快照，不可混用。详见下方 iOS TFAT 小节；样例代码目标和更深技术后代仍部分未核。 |
| Developer Program Policies | [Developer Program Policy](https://support.google.com/googleplay/android-developer/answer/18258653) · [开发者计划政策全文](../developer-program-policy/developer-program-policy.zh-CN.md) | 上位/关联平台政策。Families 页面要求儿童可访问内容及其外链遵循开发者计划政策；政策正文已打开。 |
| COPPA / GDPR / local law | [FTC 儿童隐私资源](https://www.ftc.gov/business-guidance/privacy-security/childrens-privacy) · [EU GDPR 正文](https://eur-lex.europa.eu/eli/reg/2016/679/oj?locale=en) · [数据与儿童安全专题](../user-data/user-data.zh-CN.md) | 外部法律依据，不由 Play 帮助页概括取代。FTC 入口、两篇实务指引、FAQ、现行 eCFR 和 2025 Federal Register 修订已分别概括；一般合规日 2026-04-22 已过。旧 Safe Harbor URL 仍超时，但已另行打开 FTC 当前目录与 16 CFR §312.11；EUR-Lex 抓取受限，见下方 COPPA 子链和逐 URL 审计。Families 页面也提示“儿童”的年龄定义因地区和语境而异。 |
| Expert Approved / Teacher Approved | [Build Teacher Approved apps for Google Play](https://playacademy.exceedlms.com/sl/91535e27) · [Play Academy Families 课程目录](https://playacademy.exceedlms.com/student/catalog/list?category_ids=2558) · [广告与 IAP 标准课程](https://playacademy.exceedlms.com/student/path/22151/activity/32755) | 自愿教育/评级项目，不是政策豁免或审核保证。Families 正文用名为 “Expert Approved”，旧课程标题为 “Teacher Approved”；名称存在版本差异，不能据此断定当前评审标准相同。课程介绍可读，但启动课程需登录；另一个 5 分钟广告/IAP 课程公开目标涉及避免让 13 岁以下儿童感到困惑、分心、受操纵或过度商业化，课件需登录；Families 正文不保证应用获评。 |

#### Families 应用数据实践页：正文与直接子链接（英文 / 简体中文）

2026-10-24 分别打开 [英文正文](https://support.google.com/googleplay/android-developer/answer/11043825?hl=en)（131 行）和 [简体中文正文](https://support.google.com/googleplay/android-developer/answer/11043825?hl=zh-Hans)（141 行）。中文页提示内容可能由 AI 翻译，理解细微措辞时以英文现行正文和政策中心为准。两种语言的正文各有 6 个链接位置：5 个外部目标加一个跳到本页下方 AAID 说明的锚点。这里另列与政策理解直接相关的帮助导航和页脚链接；全站搜索、语言选择、反馈按钮等界面控件不计入政策后代。按源页面显示的不同外链 href（跳转前的原始地址）计数，并排除本段的两个源页面引用、仅供规则交叉核对的 DPP 链接、同页锚点和自链接；计入相关帮助导航和页脚后，英文与简体中文页分别有 11 个和 10 个不同外链。

| 正文链接 | 目标页内容及与本页规则的关系 | 访问与覆盖状态 |
| --- | --- | --- |
| 本页下方 AAID 小节（锚点） | 是同页跳转，不是新目标页；具体规则仍受 Families、User Data 与 Developer Program Policy 约束。 | 两种语言正文中均可见；按链接位置计数，不增加外部 URL 目标数。 |
| App Set ID（[旧 Android 路径](https://developer.android.com/training/articles/app-set-id)）→ [现行 App Set ID 指南](https://developer.android.com/identity/app-set-id) | Android 技术实现指南，介绍应用/开发者范围和读取方式；本页把它作为分析用途的可选方案，未规定必须使用 App Set ID，也不因此批准儿童数据流。 | 旧路径重定向至现行指南；正文及相关 API/Task 后代见递归链接图 §4.65（快照：`../google-play-policy-link-graph.md#465-families-data-practices-app-set-id-api-与异步任务后代`，未导入本仓库）和标识符专题（快照：`advertising-id.md`，未导入本仓库）。API 总目录仍部分覆盖。 |
| [Advertising ID 帮助页](https://support.google.com/googleplay/android-developer/answer/6048248?hl=en) | 解释 AAID 与 `AD_ID`。该旧帮助页含 2021/2022 年迁移日期等历史信息；当前规则应以现行 [Developer Program Policy](https://support.google.com/googleplay/android-developer/answer/18258653?hl=en) 为准：AAID 仅可用于广告和用户分析，访问时检查用户退出状态，不得为广告与持久设备标识符关联；PII 用于广告须有明确同意，分析数据不得与 PII 或持久标识符关联。DPP 是现行交叉核对来源，不是本页的直接链接。 | 英文帮助页正文已打开；其 11 个可解析正文目标已尝试，历史迁移语句与现行 DPP 分开处理。更深平台 API/侧栏后代仍部分覆盖。 |
| Families 自认证广告 SDK 清单（[旧入口 9283445](https://support.google.com/googleplay/android-developer/answer/9283445)）→ [现行清单](https://support.google.com/googleplay/android-developer/answer/12955712?hl=en) | 动态列出儿童广告适用的自认证 SDK/版本。2026-10-24 页面仍称暂停新申请、既有参与者要求不变；开发者须核对实际集成版本，不能只凭厂商或 SDK 名称推定合规。 | 旧地址跳到现行清单；正文已打开，14 行 Maven 项对应 13 个供应商目标。厂商、版本与 SDK 技术后代另见第三方 SDK 专题（快照：`sdk-requirements.md`，未导入本仓库），部分后代仍待核。 |
| 目标受众（[旧入口 9285070](https://support.google.com/googleplay/android-developer/answer/9285070)）→ [现行目标受众与内容设置](https://support.google.com/googleplay/android-developer/answer/9867159?hl=en) | Play Console 申报/实施指南，帮助声明目标年龄；中性年龄屏幕不得预填达标年龄或暗示用户必须达到某年龄才能进入。它不能覆盖 Families 的儿童数据和广告规则。 | 旧地址跳到现行页；正文及 neutral-age-screen 小节已打开。单独片段 URL 抓取失败，不影响对完整目标页的核验。 |
| [Families 政策](https://support.google.com/googleplay/android-developer/answer/9893335?hl=en) | 上位正式政策，涵盖儿童适龄内容、数据、SDK/API、广告、社交功能和申报；本数据实践页是其标识符限制的实施说明。 | 英文正文已打开；中文正文、5 个广告示例图目标及其访问限制见本专题上方。图片不可读，不据此推断画面。 |

**正文外的相关帮助链接：**

| 链接位置 / 目标 | 内容及访问状态 |
| --- | --- |
| 页首 Play Console Help → [developers/help-and-support](https://play.google.com/console/developers/help-and-support) | 账号内支持入口；本次点击跳转至 Google 登录，未形成可读的公开政策页。按非政策目标记录，不计入“政策子页面已读”分子。 |
| 相关帮助目录：[Data safety 主题目录](https://support.google.com/googleplay/android-developer/topic/12797379?hl=en)、[Data safety 表单说明](https://support.google.com/googleplay/android-developer/answer/10787469?hl=en) | 主题目录是导航入口。Data safety 正文英文与简体中文均已打开，要求申报准确反映应用及第三方 SDK 的数据实践；它是 Play Console 披露流程，不替代 User Data/Families 政策。目录英文入口已打开；精确 `zh-Hans` 目录请求 Cache miss，故不推断本地化目录正文。 |
| [Prominent disclosure 最佳实践](https://support.google.com/googleplay/android-developer/answer/11150561?hl=en) | 英文与简体中文正文均已打开。页面建议在收集或请求权限前及时、醒目、清楚地说明数据种类、用途及 SDK 行为，提供拒绝/稍后选择并妥善降级；可用视频演示交互。它是 UX 实践指南，不能替代隐私政策、Data safety 申报或 User Data 义务。 |
| 页脚 [Contact us](https://support.google.com/googleplay/android-developer/gethelp)；英文页另有 [Help Community](https://support.google.com/googleplay/android-developer/community?hl=en) | Contact 路由要求登录；英文社区是动态讨论/支持入口，不是规范性政策正文。简体中文正文页未显示 Community 链接。社区帖子、搜索和推荐项不纳入本页政策子链计数。 |
| 当前文章的自链接 | 相关链接区有指回本页的自链接；它不构成新的目标。 |

这组正文和帮助链接展示了政策、平台实现、Console 申报和 UX 指南的不同效力。已打开目标页的摘要及其与 Families 的关系均在上表说明；但 SDK 厂商后代、Android API 全目录和帮助站导航仍非穷尽递归。逐 URL 的访问、摘要及子链接状态见审计台账（快照：`../source-page-audit.csv`，未导入本仓库）。

#### Families 政策中儿童广告违规示例图片

2026-10-24 从现行 Families 正文逐一点击广告示例下方的 5 个图片链接。它们依正文顺序跟在“关闭按钮躲避手指”“5 秒后仍无法关闭”“占据大部分屏幕且无明显关闭方式”“一个横幅塞入多个广告优惠”“广告/自有 Play 商品推广伪装成应用内容”等示例旁。五个 `lh3.googleusercontent.com` 目标均返回 Cache miss，图片像素不可读；下表的对应关系只依据图片在官方正文中的顺序和相邻说明，不描述或推断图片实际画面。它们是违规示意素材，不是额外政策条款。

| 正文图片目标 | 相邻官方示例 | 图片访问状态 |
| --- | --- | --- |
| [Families 示例图 1](https://lh3.googleusercontent.com/mwrum9RyEI7fCKwsKySiw7QPrxyYnwJK5IZNe2bdzxW3Rk4HXM1Y1QDpa6VxTc_XHA%3Dw600) | 5 秒后仍无法关闭的广告示例之后 | 2026-10-24 点击返回 Cache miss；像素不可读。 |
| [Families 示例图 2](https://lh3.googleusercontent.com/x_00itIxYS9KEaMpKssADj_fX0dSUff6o6Nt04ASG4pey542vycDMIyFXX5clJE_fDSb%3Dw895-h503) | 占据大部分屏幕且没有明显关闭方式的广告示例之后 | 2026-10-24 点击返回 Cache miss；像素不可读。 |
| [Families 示例图 3](https://lh3.googleusercontent.com/FsWSkB1jUDZN6U3q53gxfYNee-Y5D1QeoVH3bdJ-2uuvIf9iZLM0mDV3fMZSdd18yxM%3Dw895-h503) | 同一广告位展示多个优惠的横幅示例之后 | 2026-10-24 点击返回 Cache miss；像素不可读。 |
| [Families 示例图 4](https://lh3.googleusercontent.com/JZk0x1JU5sP9YnXXMF4LJ8HDOfFJXJr1ssLSRxAD1UjHhvuGRmDBE2VhR3wzwgAJpg%3Dw895-h503) | 广告看起来像应用内容的示例之后 | 2026-10-24 点击返回 Cache miss；像素不可读。 |
| [Families 示例图 5](https://lh3.googleusercontent.com/RcNH80fh9w-1FFSzywqZ_GiXKlSPxzcua03TA_TdfQUqX42klFu0SmCw47j0Fd7onMex%3Dw895-h503) | 自有 Play 商品推广与应用内容无法区分的示例之后 | 2026-10-24 点击返回 Cache miss；像素不可读。 |

### Families 帮助目录与 Academy 课程后代

2026-10-23 重开 [Families 帮助目录](https://support.google.com/googleplay/android-developer/topic/9877766?hl=en)。它是入口页而非单独的政策条文：页面要求开发者在提交 Designed for Families 或面向儿童的应用前确认内容适龄并遵守适用法律。正文有两条正式政策链接、一条 Academy 课程入口、一个政策视频和图片资源；页脚另有社区与 Contact us。

| 目录直链/课程子页 | 状态与关系 |
| --- | --- |
| [Google Play Policy - Families 视频](https://www.youtube.com/watch?v=duPj0MW7A-U) | 视频抓取失败；未根据标题推断课程或政策内容。 |
| Families 目录图片资源（[原始图片](https://lh3.googleusercontent.com/84hS7ibvpGXLtjjXcJe_zgNsdFTa5x6ognj8r_miFzpJiVyRRfVfGNAUMvGko_hqp-8W%3Dh200)） | 图片目标 Cache miss；仅记录为页面资源，不推断图中文字或要求。 |
| [Google Play Families Policies](https://support.google.com/googleplay/android-developer/answer/9893335?hl=en) | 正式开发者政策正文，已全文复核；儿童目标受众的适龄内容、数据、SDK/API、广告、社交功能、AR 和申报要求见上表及本页其他小节。 |
| [Families Self-Certified Ads SDK Policy](https://support.google.com/googleplay/android-developer/answer/12918983?hl=en) | 正式 SDK 计划政策，已全文复核；它规定 SDK 提供商的创意、广告格式、无个性化/再营销、数据实践、mediation、自认证材料和法律合规要求。2026-10-23 页面仍称暂停新申请、既有参与者要求不变；应用方整合清单见第三方 SDK 专题（快照：`sdk-requirements.md`，未导入本仓库）。 |
| [Academy：Understand Google Play's Families policies](https://playacademy.exceedlms.com/student/path/19753-understanding-google-play-s-families-policies) | 公开目录发布于 2023-11-16，介绍如何遵守 Families 政策并选择匹配目标受众的 Play Console 设置；它是培训材料，不是新政策。目录列出以下五个活动： |
| [Families Play Policy Video](https://playacademy.exceedlms.com/student/path/19753/activity/58919) | 课程子页 Cache miss；未取得视频字幕或正文。 |
| [Select your target audience and content settings（15 分钟）](https://playacademy.exceedlms.com/student/path/19753/activity/28499) | 课程子页 Cache miss；仅保留目录公开的名称与时长。 |
| [Comply with Families policies and program requirements（12 分钟）](https://playacademy.exceedlms.com/student/path/19753/activity/28500) | 子页公开元数据可读：2023-04-05 发布、Beginner、12 分钟；课程启动需登录。公开简介只说明课程主题为儿童/家庭应用安全与政策要求，不含可核实的逐课件条款。 |
| [Comply with Families Ads and Monetization Requirements（15 分钟）](https://playacademy.exceedlms.com/student/path/19753/activity/983387) | 课程子页 Cache miss；未推断广告/商业化课程细节。 |
| [Comply with Families policies SDK requirements for your app（15 分钟）](https://playacademy.exceedlms.com/student/path/19753/activity/983388) | 课程子页 Cache miss；未推断 SDK 课程细节。 |
| [Google Play Developer Help Community](https://support.google.com/googleplay/android-developer/community?hl=en) | 公开动态社区，含帖子、课程指南与视频；不是权威政策来源，帖子和推荐内容未按政策正文递归扩展。 |
| [Contact us](https://support.google.com/googleplay/android-developer/gethelp) | 重定向至账号专属 Play Console 帮助与支持，需要登录；未提交请求。 |

课程目录和可见活动页面只提供公开课程元数据；内容播放/课件需要登录，故教学材料与约束性政策分开记录。逐目标状态见来源 URL 审计表（快照：`../source-page-audit.csv`，未导入本仓库）；平台导航、分享控件和动态社区内容不视为新增 Play 政策。

#### AdMob/GMA Next-Gen 的儿童年龄处理（TFAT）

2026-10-21 更新的 Android Targeting 指南改用 Tag for Age Treatment（TFAT）。AdMob 帮助页仍展示旧 `setTagForChildDirectedTreatment` 代码，但 TFAT 帮助页和当前 GMA Next-Gen 指南明确说 TFCD/TFUA 已弃用。实现时应以所集成 SDK 产品线的当前文档为准；这里是广告请求实现建议，不替代 Play 的目标受众申报、Families 政策、年龄核验或当地法律判断。

- 在发出广告请求前设置 `RequestConfiguration.Builder.setAgeRestrictedTreatment(CHILD | TEEN | UNSPECIFIED)`，并通过 `MobileAds.setRequestConfiguration()` 应用；这是全局配置，会覆盖原配置。若需从首次请求就生效，应把配置交给初始化流程。
- `CHILD` 表示儿童年龄处理：关闭个性化广告和再营销、阻止第三方广告测量像素/广告服务器请求、应用儿童广告保护，并且不传输 AAID/IDFA。`TEEN` 关闭个性化广告和再营销、应用青少年广告保护。`UNSPECIFIED` 是默认未指定状态，不表示已经完成用户年龄判定。
- 如多个年龄/隐私信号同时存在，按最严格信号处理。Google 的这些工具不免除开发者按适用辖区确定年龄处理方式和遵守法律的责任。
- AdMob/Play Families 政策另有自认证广告 SDK 资格要求。下表中的 mediation adapter 版本只说明该版本可向被调解 SDK 转发 TFAT 信号，**不代表该广告 SDK 已通过 Play Families 自认证**。自认证资格须另查[当前 Families SDK/版本清单](https://support.google.com/googleplay/android-developer/answer/12955712)。

Android Targeting 页的 mediation adapter 转发最低版本快照（页面最后更新 2026-10-21；发布前请检查实时文档）：

| Mediation adapter | 转发 TFAT 的最低版本 | Google 集成指南目标与访问状态 |
| --- | --- | --- |
| AppLovin | 13.6.3.0 | [指南](https://developers.google.com/admob/android/next-gen/mediation/applovin) 已打开；具体接入步骤未逐项审阅。 |
| BidMachine | 3.7.1.1 | [指南](https://developers.google.com/admob/android/next-gen/mediation/bidmachine) 已打开；具体接入步骤未逐项审阅。 |
| BIGO | 5.9.0.1 | [指南](https://developers.google.com/admob/android/next-gen/mediation/bigo) 已打开；具体接入步骤未逐项审阅。 |
| Chartboost | 9.12.1.1 | [指南](https://developers.google.com/admob/android/next-gen/mediation/chartboost) 已打开；具体接入步骤未逐项审阅。 |
| DT Exchange | 8.4.5.1 | [指南](https://developers.google.com/admob/android/next-gen/mediation/dt-exchange) 已打开；具体接入步骤未逐项审阅。 |
| i-mobile | 2.3.2.4 | [指南](https://developers.google.com/admob/android/next-gen/mediation/imobile) 已打开；具体接入步骤未逐项审阅。 |
| InMobi | 11.3.0.1 | [指南](https://developers.google.com/admob/android/next-gen/mediation/inmobi) 已打开；具体接入步骤未逐项审阅。 |
| ironSource | 9.4.3.0 | [指南](https://developers.google.com/admob/android/next-gen/mediation/ironsource) 已打开；具体接入步骤未逐项审阅。 |
| Liftoff Monetize | 7.7.4.2 | [指南](https://developers.google.com/admob/android/next-gen/mediation/liftoff-monetize) 已打开；具体接入步骤未逐项审阅。 |
| LY (Line) | 3.1.1.1 | [指南](https://developers.google.com/admob/android/next-gen/mediation/line) 已打开；具体接入步骤未逐项审阅。 |
| maio | 2.0.9.0 | [指南](https://developers.google.com/admob/android/next-gen/mediation/maio) 已打开；具体接入步骤未逐项审阅。 |
| Meta (Facebook) | 6.21.0.4 | [指南](https://developers.google.com/admob/android/next-gen/mediation/meta) 已打开；具体接入步骤未逐项审阅。 |
| Mintegral | 17.1.61.1 | [指南](https://developers.google.com/admob/android/next-gen/mediation/mintegral) 已打开；具体接入步骤未逐项审阅。 |
| Moloco | 4.10.0.0 | [指南](https://developers.google.com/admob/android/next-gen/mediation/moloco) 已打开；具体接入步骤未逐项审阅。 |
| myTarget | 5.47.1.1 | [指南](https://developers.google.com/admob/android/next-gen/mediation/mytarget) 已打开；具体接入步骤未逐项审阅。 |
| Pangle | 8.1.0.3.1 | [指南](https://developers.google.com/admob/android/next-gen/mediation/pangle) 已打开；具体接入步骤未逐项审阅。 |
| PubMatic OpenWrap（Beta） | 5.1.2.2 | [指南](https://developers.google.com/admob/android/next-gen/mediation/pubmatic) 已打开；具体接入步骤未逐项审阅。 |
| Verve | 3.9.0.0 | 链接点击返回 Internal Error，浏览器未暴露目标 URL；没有猜测或补造链接。 |

#### AdMob/GMA iOS 的儿童年龄处理与 mediation

[iOS Targeting 指南](https://developers.google.com/admob/ios/targeting)最后更新于 2026-10-21，使用 GADRequestConfiguration 的 ageRestrictedTreatment 设置 CHILD、TEEN 或 UNSPECIFIED，并要求在初始化 Google Mobile Ads SDK 前设置全局请求配置。该页的迁移表把旧 TFCD/TFUA 的 true 映射到 CHILD，把 false/未设置映射到 UNSPECIFIED；TEEN 没有旧信号等价项。旧代码示例仍出现在弃用说明之后，接入时应使用迁移后的属性和实际 SDK 版本文档。

- 同时存在多个年龄/隐私信号时，采用限制最严的处理；Family Link 管理的 Google 账号会自动把所有广告请求按儿童定向处理。年龄标签是广告服务请求信号，不是 Play Console 目标年龄申报或年龄核验的替代品。
- [iOS 发布说明](https://developers.google.com/admob/ios/rel-notes)记录 13.3.0 开始弃用 TFCD/TFUA 属性；页面当前列出 13.11.0（2026-09-29）。Targeting 页的 API Demo 链接当时落到 GitHub 示例 13.2.0，与发布说明的当前版本不同；Swift/Objective-C 年龄处理样例链接点击时返回 Internal Error、未暴露目标，因此这里不猜测其 URL。
- 下表是 iOS Targeting 页面所列的年龄信号最低 adapter 版本快照。它们与 Android GMA Next-Gen 页面上的版本数字不可互换；供应商发布说明中有的写“转发到 COPPA API”，有的写“过滤儿童年龄请求”，实际机制各有不同。每个版本均应以最新指南复核，也不代表 Play Families 自认证资格。

| iOS mediation adapter | 支持年龄信号的最低版本 | 该 adapter 指南中的年龄处理记录 |
| --- | --- | --- |
| AppLovin | 13.6.3.0 | [指南](https://developers.google.com/admob/ios/mediation/applovin)：CHILD 请求过滤；13.0.0.1 起，声明儿童/同意年龄以下处理时会自动禁用 AppLovin mediation。 |
| BidMachine | 3.6.1.1 | [指南](https://developers.google.com/admob/ios/mediation/bidmachine)：将 ageRestrictedTreatment 转发到 BidMachine COPPA API。 |
| BIGO | 5.2.1.0 | [指南](https://developers.google.com/admob/ios/mediation/bigo)：将年龄信号转发到 BIGO COPPA API。 |
| Chartboost | 9.12.0.1 | [指南](https://developers.google.com/admob/ios/mediation/chartboost)：将年龄信号转发到 Chartboost COPPA API。 |
| DT Exchange | 8.4.7.1 | [指南](https://developers.google.com/admob/ios/mediation/dt-exchange)：将年龄信号转发到 DT Exchange COPPA API。 |
| i-mobile | 2.3.4.7 | [指南](https://developers.google.com/admob/ios/mediation/imobile)：过滤 CHILD 年龄请求；较早版本说明其不能接收年龄信号。 |
| InMobi | 11.2.0.1 | [指南](https://developers.google.com/admob/ios/mediation/inmobi)：将年龄信号转发到 InMobi COPPA API。 |
| ironSource | 9.4.1.0.1 | [指南](https://developers.google.com/admob/ios/mediation/ironsource)：将年龄信号转发到 ironSource COPPA API。 |
| Liftoff Monetize | 7.7.2.1 | [指南](https://developers.google.com/admob/ios/mediation/liftoff-monetize)：将年龄信号转发到 Vungle COPPA API。 |
| LY Ads / Line | 3.0.1.1 | [指南](https://developers.google.com/admob/ios/mediation/line)：将年龄信号转发到 FiveAd COPPA API。 |
| maio | 2.2.1.2 | [指南](https://developers.google.com/admob/ios/mediation/maio)：过滤 CHILD 年龄请求；较早版本说明其不能接收年龄信号。 |
| Meta Audience Network | 6.21.1.1 | [指南](https://developers.google.com/admob/ios/mediation/meta)：将年龄信号转发到 Meta COPPA API。 |
| Mintegral | 8.1.3.1 | [指南](https://developers.google.com/admob/ios/mediation/mintegral)：将年龄信号转发到 Mintegral COPPA API。 |
| Moloco | 4.6.1.1 | [指南](https://developers.google.com/admob/ios/mediation/moloco)：将年龄信号转发到 Moloco COPPA API。 |
| myTarget | 5.43.0.0 | [指南](https://developers.google.com/admob/ios/mediation/mytarget)：将年龄信号转发到 myTarget COPPA API。 |
| Pangle | 7.9.1.1.1 | [指南](https://developers.google.com/admob/ios/mediation/pangle)：过滤 CHILD 年龄请求。 |
| PubMatic OpenWrap | 5.1.0.1 | [指南](https://developers.google.com/admob/ios/mediation/pubmatic)：将年龄信号转发到 PubMatic COPPA API。 |
| Verve / HyBid | 3.8.1.1 | [指南](https://developers.google.com/admob/ios/mediation/verve)：过滤 CHILD 年龄请求。 |

AppLovin 集成指南还说，其 iOS adapter 12.0.0.0 起可将 UMP 和符合 Google Additional Consent 规范的 GDPR 同意信号传给 AppLovin；必须在初始化 Google Mobile Ads SDK 前设置这些隐私选项。它同时提醒 Google 的受限数据处理设置不会自动应用到 mediation 链上的每个广告网络，开发者需逐网络核对。此类 vendor 接入说明不是 Play 政策，但揭示“Google 接受了信号”不等于每个被调解网络均正确处理。

[AdMob 最大广告内容分级帮助页](https://support.google.com/admob/answer/7562142)说明账号级、单应用级与 SDK 每请求级设置的覆盖顺序：应用设置覆盖账号设置，SDK 设置覆盖 AdMob 界面设置。Families 儿童专用应用的上限为 G；混合受众的 Families 应用上限为 PG。单次请求帮助页进一步说明每请求值会覆盖 app/account 上限，但 Families 应用的可选值仍受 G/PG 档位约束。旧 AdMob 示例为混合受众儿童请求设 G，较 PG 上限更严格，不能把示例误读为混合受众都可投放 G 以上广告。

[Publisher Privacy Treatment (PPT) Beta](https://support.google.com/admob/answer/14323214)是另一种可选请求信号：PPT=1 关闭该次请求的广告个性化，不等价于 TFAT 的年龄处理或 NPA/RDP。并存信号中最严格者生效。链接的[GDPR 发布者工具页](https://support.google.com/admob/answer/7666366)解释 Google 出版商产品中的控制者/处理者角色及出版商同意责任，属于 AdMob 操作说明；[COPPA 官方入口](https://www.ftc.gov/business-guidance/privacy-security/childrens-privacy)和 [GDPR 原文](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32016R0679)是外部法律来源，不由 Google 摘要代替。EUR-Lex 本次只返回有限正文。

本分支直接链接的 iOS Targeting、GADRequestConfiguration/GADMobileAds API、iOS Quick Start、发布说明、mediation 总览、上述 18 个 adapter 页面以及五个相关 AdMob Help 目标均已打开或记录状态；Quick Start、API 与 mediation 页面自身的其他后代尚未全部递归。Targeting 页的样例源码链接访问失败且未返回目标 URL，保留为未知，不据此补造链接。

已打开的 [儿童广告保护](https://support.google.com/adspolicy/answer/14170968)列出全球受限类别，包括酒精/烟草/毒品、赌博、年龄敏感媒体、危险品、复杂投机金融、健康/美容/减肥、药品补剂、抽奖、移动订阅、社交网络、间谍服务、成人虚拟世界、敏感议题、约会/浪漫及暴力/惊悚内容；页面说明该列表会更新，且覆盖 Google Ads 产品线。已打开的[青少年广告保护](https://support.google.com/adspolicy/answer/12205906)针对未满 18 岁账号，同样关闭广告个性化并限制敏感类别，列出成人内容、酒精/烟草/毒品、身体改造/减重、投机金融、抽奖、危险品、约会、赌博、药品补剂、惊悚内容、间谍服务和成人社交平台。两页是 Google Ads 广告投放限制，不等同于 Play 应用审核规则；Play Families 的应用与 SDK 义务仍以 Play 政策为准。

#### 从目标受众页核出的设计最佳实践

[目标受众操作页](https://support.google.com/googleplay/android-developer/answer/9867159)还给出分龄适龄性建议：面向 5 岁及以下儿童时，优先支持尚未识字/初读者、采用简单且一致的导航、让家长角色明确；6–8 岁可考虑积极反馈、适龄激励和早期教育主题。它也提醒评估内容、广告、IAP、奖励机制、敏感主题与儿童发展阶段是否相符。此类清单是设计指导，不是完整的内容审查规则；页面内年龄段锚点另有部分抓取缓存失效，故本段基于已打开的目标受众正文概括，不推断未读取的课程内容。

### Google Developers「Building for kids」最佳实践后代

AdMob 的 Families 页面继续链接到 [Google Play Families 计划概览](https://google.play/business/programs/families/)，该页的 “Learn More” 指向 [Building for kids](https://developers.google.com/building-for-kids)。这组 Google Developers 材料是儿童产品设计、安全和内容指导，不是新增的 Play 强制条文；具体准入仍以 Families、UGC、User Data 等政策为准。

| 子页 | 可复用的实践 | 核验边界 |
| --- | --- | --- |
| [Designing engaging apps](https://developers.google.com/building-for-kids/designing-engaging-apps) | 按目标年龄与较年幼用户的能力设计；用儿童和家长研究验证假设；保持导航简单一致、避免分心、扩大触控目标、提供清晰反馈和无障碍支持；让家长参与和管理设置。 | 全文已打开；辅助链接到 Material accessibility 页面需要 JavaScript，自动抓取只返回提示。 |
| [Developing thoughtful content](https://developers.google.com/building-for-kids/developing-thoughtful-content) | 结合年龄和发展阶段判断故事、图像、幽默与文本；避免刻板印象；5 岁及以下尽量少用文本并可用语音，6–8 岁使用有限文本，9–12 岁可采用更复杂的语言元素；向家长清楚说明重要披露、控制和体验。 | 全文已打开；年龄分段是设计建议，不是 Play 内容分级表或全球统一法定年龄。 |
| [Building safer apps](https://developers.google.com/building-for-kids/building-safer-apps) | 对聊天和 UGC 做滥用威胁评估；建议预审核、社区规则、举报/屏蔽、人工复核和家长控制。其聊天示例提出限制图片分享、预批准联系人/短语。 | 全文已打开；这些是建议，应与 Play UGC 和 Families 社交功能义务分别核对。页面的 Home app 家长控制 Intent 只适用于受监督账号平板，技术兼容性需另核。 |
| [Be Internet Awesome](https://beinternetawesome.withgoogle.com/en_us) 及其直接子链 | 主站涵盖谨慎分享、识别诈骗/钓鱼、保护密码与个人资料、善意交流、屏蔽霸凌并向可信成人求助。[AI Literacy guide](https://services.google.com/fh/files/misc/bia_ai-literacy-guide_en.pdf)（51 页，2–8 年级）含 AI 基础、数字公民与 AI、负责任使用三课，强调核验 AI 信息、数据/偏见意识、隐私和向成人求助；[Interland](https://beinternetawesome.withgoogle.com/en_us/interland) 用四个互动主题练习善意交流、识别虚假信息、谨慎分享和密码安全。它们是教育资源，不等于应用自身满足 Play 审核、举报或成人控制义务。 | 主站、AI 指南和 Interland 正文/可读内容已打开；主站链接的 [课程 PDF](https://www.gstatic.com/gumdrop/files/bia-curriculum-en-june-2023.pdf) 超过读取器 10 MiB 限制，未读取；[单页 pledge PDF](https://storage.googleapis.com/gweb-interland.appspot.com/en-us/hub/pdfs/Google_BeInternetAwesome_Pledge.pdf) 仅识别到文件，未提取正文。其它家长材料及外部合作方后代仍未穷尽。 |
| 外部辅助材料 | [FOSI 数字育儿建议](https://www.fosi.org/good-digital-parenting/seven-steps-good-digital-parenting/)；[Material accessibility](https://m2.material.io/design/usability/accessibility.html)。 | FOSI 目标返回 cache miss；Material 页面要求 JavaScript。未从标题推断未读取内容。 |

### COPPA 官方资料子链（美国法律，按适用条件判断）

Families 正文要求遵守 COPPA、GDPR 和其他适用法律，但 Google Play 的“儿童”口径与某项法律的适用年龄/范围不必相同。以下是 FTC 官方入口及关键后代的摘要，供定位原文，不是法律意见或对具体应用适用性的结论。**16 CFR Part 312 于 2025-06-23 生效；受监管主体的一般合规日期为 2026-04-22，已过。** Federal Register 说明 §312.11(d)(1)、(d)(4)、(g) 有单独过渡安排；具体主体应核对正式规则与适用日期。

| 页面 | 可用信息与关系 | 核验状态 |
| --- | --- | --- |
| [FTC Children's Privacy](https://www.ftc.gov/business-guidance/privacy-security/childrens-privacy) | FTC 商业合规入口链接规则、FAQ、家长可核实同意、Safe Harbor 和实务指引；页面还包含执法案、评论等其他材料，不能把每项都视为适用于 Play 应用。 | 正文已打开；关键 COPPA 子页按下列各行分别跟进。旧 Safe Harbor URL 超时；另行找到并打开 FTC 当前 [COPPA Safe Harbor Program](https://search.ftc.gov/enforcement/coppa-safe-harbor-program) 页面及其六个批准项目链接，动态案例/新闻等内容流未逐条递归。 |
| [Not Just for Kids' Sites](https://www.ftc.gov/business-guidance/resources/childrens-online-privacy-protection-rule-not-just-kids-sites) | FTC 指引说明 COPPA 也可能涵盖一般受众服务（运营者实际知道正在收集未满 13 岁儿童信息时）及满足条件的广告网络/插件；一般受众服务并非一概必须调查用户年龄，但询问并获知年龄、年级等信息可能形成 actual knowledge。 | 正文已打开；属于 FTC 解释材料，不是 Play 的年龄屏幕规则。 |
| [A Six-Step Compliance Plan](https://www.ftc.gov/business-guidance/resources/childrens-online-privacy-protection-rule-six-step-compliance-plan-your-business) | 将合规工作拆成：判断覆盖范围、发布隐私政策、向家长直接通知、取得可核实同意、兑现家长持续权利、建立安全/保留/删除流程；列出儿童应用、广告网络、插件等服务范围。适合作为流程检查表，不代替法规条文。 | 正文已打开；只提取与上位规则直接相关的六步，不把页面所有交叉引用视为已穷尽。 |
| [COPPA Rule (FTC)](https://www.ftc.gov/legal-library/browse/rules/childrens-online-privacy-protection-rule-coppa)、[16 CFR Part 312 (eCFR)](https://www.ecfr.gov/current/title-16/chapter-I/subchapter-C/part-312) 与 [2025 Federal Register 正式 PDF (GovInfo)](https://www.govinfo.gov/content/pkg/FR-2025-04-22/pdf/2025-05904.pdf) | 2025 修订新增 mixed audience 定义；把移动电话号码纳入 online contact information，并将政府签发识别码、可用于自动/半自动识别的生物特征标识纳入 personal information；细化 internal operations 与判断儿童定向受众的证据；更新家长通知、信息安全、保留/删除、同意方法与例外，以及 FTC Safe Harbor 年度评估/披露/报告要求。当前 eCFR 显示截至 2026-10-21 的 Part 312；eCFR 是权威但非正式法典版本。 | FTC 概览、现行 eCFR、Federal Register XML 与 GovInfo 66 页正式 PDF 均已打开。PDF 与 XML 对生效/一般合规日一致；FR XML 明确建议法律引用核对 GovInfo 正式 PDF。FTC 链接的 15 U.S.C. 目标此前返回 404，未据此推断法条。 |
| [COPPA FAQ](https://www.ftc.gov/business-guidance/resources/complying-coppa-frequently-asked-questions) | FTC FAQ 概述覆盖主体与核心义务：儿童隐私政策和直接通知、有限例外外先取得家长可核实同意、家长访问/删除和停止后续收集、合理安全、仅为既定目的保留并安全删除、不以不必要数据为参与条件。移动应用、SDK/广告网络、被动跟踪、照片/音视频和足以识别街道与城市的位置均有专门解释；运营者应查明可通过其应用收集的第三方及其做法。 | 正文已打开；页面明确其为 FTC staff 指引、并不约束委员会。535 行全文、全部锚点及历史引用没有逐条复录。 |
| [Verifiable Parental Consent](https://www.ftc.gov/business-guidance/privacy-security/verifiable-parental-consent-childrens-online-privacy-rule) | 说明规则要求在受覆盖情形下取得家长可核实同意，但不强制所有运营者使用同一种验证方法；FTC 列出若干已审查方法及提交流程。 | 正文已打开；历次申请与具体技术方法不是 Play 的统一年龄门槛。 |
| [FTC age-verification policy statement (2026-02-25)](https://www.ftc.gov/news-events/news/press-releases/2026/02/ftc-issues-coppa-policy-statement-incentivize-use-age-verification-technologies-protect-children) | FTC 声明在其规定条件下，不对一般受众/混合受众服务仅为判断用户年龄而收集、使用、披露个人信息采取 COPPA Rule 执法行动；条件包括不作次要用途、必要期限后及时删除、限制接收方、向家长/儿童清楚告知、合理安全保护、合理准确性。它是有条件的执法政策声明，不是 COPPA 一般豁免、Play 政策变更或各州法律豁免。 | 公告全文已打开；该声明有效性和规则后续修订需复查。 |
| [FTC COPPA Safe Harbor Program](https://search.ftc.gov/enforcement/coppa-safe-harbor-program) · [16 CFR §312.11 (eCFR)](https://www.ecfr.gov/current/title-16/chapter-I/subchapter-C/part-312/section-312.11) · [2025 Federal Register XML](https://www.federalregister.gov/documents/2025/04/22/2025-05904/childrens-online-privacy-protection-rule) / [GovInfo 正式 PDF](https://www.govinfo.gov/content/pkg/FR-2025-04-22/pdf/2025-05904.pdf) | FTC 当前目录列出六家经批准计划：CARU、ESRB、iKeepSafe、kidSAFE、PRIVO、TRUSTe；根据 16 CFR §312.11，申请须公开征求意见，FTC 在提交后 180 天内作出书面决定；获批计划至少每年独立评估成员，并履行纪律、投诉/评估记录、年度报告和公开成员清单义务。FTC 当前目录正文仍写 §312.10，而现行 eCFR 和 2025 Federal Register 规则文本列为 §312.11，存在编号差异，应以现行 eCFR/正式规则核准。2025-07-21 的公开成员清单期限和 2025-10-22 的年度报告/指南修订期限已过；技术能力评估报告首次期限为 2028-04-22。Safe Harbor 是 COPPA 监管框架内可选择的行业自律机制，不是 Google Play 要求所有开发者加入的认证，也不免除 Play 的 Families、数据安全、广告或其他适用政策。 | FTC 当前目录及 eCFR §312.11 已打开；目录所列六个官方项目文档均已点击：CARU、ESRB、iKeepSafe 三份大型 PDF 抓取超限；kidSAFE、PRIVO、TRUSTe 文档可读但属于较早版本/历史附件，不代表各计划现行条款。2025 Federal Register XML 和 66 页正式 PDF 已核对。旧 `ftc.gov/safe-harbor-program` 仍超时；FTC 页面上的其他 CMS 案例/新闻/博客等链接未全量递归。 |
| [GDPR 原文 (EUR-Lex)](https://eur-lex.europa.eu/eli/reg/2016/679/oj?locale=en) | Families 同时指向欧盟数据保护法律；Article 8 的儿童数字同意年龄为默认 16 岁、成员国可下调但不得低于 13 岁，且特别父母授权规则仅在“直接向儿童提供信息社会服务”并“以同意为法律依据”两项同时满足时触发。 | EUR-Lex 正文仍返回 JavaScript/机器人验证；这部分概括基于[欧盟委员会儿童保障页](https://commission.europa.eu/law/law-topic/data-protection/information-business-and-organisations/legal-grounds-processing-data/are-there-any-specific-safeguards-data-about-children_en)与[EDPB Consent 05/2020 第 7.1 节](https://www.edpb.europa.eu/system/files/documents/files/file1/edpb_guidelines_202005_consent_en.pdf)的选段，非直接读取 GDPR 全文。适用范围、年龄核验、最小化和 Play 边界见User Data 外部法律参考专题（快照：`user-data-policy-references.md`，未导入本仓库）。 |

#### FTC 六步指南：可执行内容与 Play 控制面

FTC 于 2026 年 5 月更新的 [A Six-Step Compliance Plan](https://www.ftc.gov/business-guidance/resources/childrens-online-privacy-protection-rule-six-step-compliance-plan-your-business)将 COPPA 工作拆成以下六步。它适用于符合美国 COPPA 覆盖条件的运营者，是实务指南而非法规正文；是否受覆盖须依现行 16 CFR Part 312 判断。

| FTC 步骤 | 实务要点摘要 | 与 Google Play 要求的关系 |
| --- | --- | --- |
| 1. 判断适用范围 | 评估服务是否面向 13 岁以下儿童并收集/允许第三方收集其个人信息；一般受众服务在实际知情直接收集儿童信息时也可能纳入。移动应用、联网游戏、位置服务、广告网络和插件均可能属于在线服务或参与收集的第三方。混合受众服务可选择只对识别为 13 岁以下的用户适用 COPPA 保护，但须在收集个人信息前以中立方式判定年龄。 | COPPA 覆盖判定不同于 Play 的目标年龄申报、Families 受众类别和年龄限制功能；一个结论不能替代另一个。 |
| 2. 发布合规隐私政策 | 清楚列出收集儿童信息的运营者及联系信息、数据类型/用途、接收方和披露目的、保留与删除安排，以及家长查看、删除和拒绝后续收集/使用的方式；相关页面要醒目易找。 | 与 Play 隐私政策及 Data safety 声明有关联，但 Play 的位置、内容和应用内可访问性要求仍按 User Data 与 Data safety 专题单独执行。 |
| 3. 直接通知家长 | 在收集前告知数据类型、目的、第三方披露、隐私政策和同意方式；处理做法发生重大变化时更新通知。非服务不可缺少的第三方披露须允许家长单独选择，不应把同意数据收集/使用与同意对外披露捆绑。 | 不能把 COPPA 邮件/通知流程当成 Play 的应用内醒目披露；Play 的披露和肯定同意须在具体应用场景中另行满足。 |
| 4. 取得可核实家长同意 | 除规则规定的有限例外外，在收集、使用或披露个人信息前取得能够合理确认家长身份的同意。FTC 不要求所有服务使用同一种验证技术；部分例外即使不需事先同意，仍可能要求家长通知。 | 该法律要求不等于 Play 的年龄屏幕、家长批准工具或 Play Console 声明。需分别检查年龄和数据政策。 |
| 5. 尊重家长持续权利 | 家长可查看儿童信息、撤回同意并停止后续收集/使用、要求删除。运营者应合理确认请求者是家长，同时避免把权利行使流程设计得过度繁琐。 | 与 Play 账户/数据删除和儿童控制要求相互补充；特定 Play 删除入口、期限和申报内容应按账户删除政策处理。 |
| 6. 安全、保留和删除 | 维护适合数据敏感度、运营规模和业务范围的书面信息安全计划；要求服务提供方书面承诺保护信息；另建书面保留/删除流程，最小化收集，在具体目的不再需要后安全删除。 | 与 Play User Data、Data safety、SDK 责任和安全政策重叠但不互相替代；第三方 SDK 数据流也须纳入 Play 申报。 |

FTC 六步指南的五个可见 HTTP 正文目标均已点击或由已审计规范页交叉核对：COPPA 规则入口、eCFR Part 312、FTC 儿童隐私入口、COPPA FAQ 和 SBA National Ombudsman。SBA 目标是小企业向联邦机构反映监管执行问题的反馈渠道，并非 COPPA 合规步骤；该链接经工具观察后跳转到 SBA 当前页面。FTC 规则目录自身的历史 Federal Register 通知清单很长，只核验了现行 eCFR 与 2025 最终修订规则，其他历史通知和后代仍部分覆盖。详情见递归链接图 §4.134 与 URL 审计表。

**与 Play 年龄屏幕的区别：** FTC 的 COPPA 年龄核验执法声明不等于 Google Play 的 neutral age screen，也不自动解决 Play 对数据披露、SDK、儿童广告、Data safety 或成人操作控制的要求。不要把美国法律下的执法政策外推到其他辖区。

### 欧盟 DSA 未成年人保护指南与透明度最佳实践

欧委会于 2025 年发布 DSA Article 28 未成年人保护指南，并在 2026 年继续维护公开说明。它与 Google Play 儿童安全标准、年龄限制、UGC、隐私和广告规则有关联，但适用范围与法律性质不同，不能作为 Play 政策的替代或自动新增条文。另有 Tech Coalition 的 Trust 自愿透明度框架、DSA 行业对照指南、ECPAT 术语译本及生成式 AI 报告材料。详见[儿童安全：DSA 指南与透明度实践](../child-safety-dsa-transparency/child-safety-dsa-transparency.zh-CN.md)，其中逐项区分法规、监管指南和非约束性最佳实践，并记录子链接与访问限制。

## 上线前核对清单

1. 画出真实用户流程，识别随机连接陌生人、匿名交流、约会/匹配、真钱参与及 UGC 的核心/附属关系。
2. 在 Console 对照应用功能准确填写目标年龄、内容分级和适用声明；不要用类别名称代替功能分析。
3. 如果属于必须限制未成年人的类别，确认仅选择 18+ 并启用 Restrict Minor Access；若仅约会为附属功能，验证年龄门槛确实覆盖进入和购买流程。
4. 如适用 Child Safety Standards，发布公开禁止 CSAE 的规则，部署应用内举报机制，制定 CSAM 处置/法定报告程序，并维护有效儿童安全联系人。
5. 若受众包含儿童，核查 SDK、数据安全/隐私政策、Families 广告 SDK、年龄屏幕、社交功能和儿童本地法规。
6. 对内容、功能、受众或广告 SDK 的每次变化重新检查申报；保留举报响应、升级、处置和培训记录。

## 来源与关联

- [Age-Restricted Content and Functionality](https://support.google.com/googleplay/android-developer/answer/16302250?hl=en)
- [Child Endangerment / Child Safety Standards](https://support.google.com/googleplay/android-developer/answer/9878809?hl=en)
- [Learning more about Child Safety Standards](https://support.google.com/googleplay/android-developer/answer/14747720?hl=en)
- [Tech Coalition developer good practices](https://technologycoalition.org/resources/developer-good-practices-combating-online-child-sexual-exploitation-and-abuse/)
- [欧盟 DSA 未成年人保护指南与透明度实践专题](../child-safety-dsa-transparency/child-safety-dsa-transparency.zh-CN.md)
- [Google Play Families Policies](https://support.google.com/googleplay/android-developer/answer/9893335?hl=en)
- [Manage target audience and app content settings](https://support.google.com/googleplay/android-developer/answer/9867159?hl=en)
- [2026-07-15 policy announcement](https://support.google.com/googleplay/android-developer/answer/17134731?hl=en)
- [Policy Deadlines](https://support.google.com/googleplay/android-developer/table/12921780?hl=en)
- 项目内关联：[用户数据](../user-data/user-data.zh-CN.md)、[Data safety](../data-safety/data-safety.zh-CN.md)、政策公告汇编（快照：`../google-play-policy-announcements.md`，未导入本仓库）。

本页为结构化改写。它不能替代 Console 当前功能、审核提示或各目标市场的法定义务；2026-08-26 是政策更新生效日，不代表某个应用已经通过年龄/儿童安全审核。
