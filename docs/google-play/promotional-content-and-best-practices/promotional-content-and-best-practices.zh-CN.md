---
id: google-play.promotional-content-and-best-practices
platform: google-play
language: zh-CN
authority: operational
status: current
kb_checked_at: 2026-10-23
review_due: 2027-01-23
regions: [global]
topics: [promotional-content, events, featuring, localization, deep-links, content-quality]
snapshot_id: play.promotional-content-and-best-practices
snapshot_package: "GooglePlay-KnowledgeBase-2026-10-24-review.zip"
coverage_status: "detailed-summary"
source_url_directory: "https://support.google.com/googleplay/android-developer/topic/12932623"
source_url_understand: "https://support.google.com/googleplay/android-developer/answer/12929029"
source_url_create: "https://support.google.com/googleplay/android-developer/answer/12932541"
source_url_quality: "https://support.google.com/googleplay/android-developer/answer/12929944"
source_url_review: "https://support.google.com/googleplay/android-developer/answer/12932123"
source_url_dates: "https://support.google.com/googleplay/android-developer/answer/12932229"
source_url_performance: "https://support.google.com/googleplay/android-developer/answer/12932124"
source_url_deep_links: "https://support.google.com/googleplay/android-developer/answer/15322603"
source_url_youtube: "https://support.google.com/googleplay/android-developer/answer/15501235"
source_url_animation: "https://support.google.com/googleplay/android-developer/answer/16009268"
source_url_dating: "https://support.google.com/googleplay/android-developer/answer/15678263"
source_url_pdf: "https://services.google.com/fh/files/helpcenter/google_play_promotional_content_guidelines.pdf"
effective_date: "operational promotional-content guidance; no 2027-01-27"
---

# Google Play Promotional Content 与活动素材最佳实践

> **导入说明（Google batch 7）。** 正文来自已经分开的 2026-10-24 Google Play 知识库快照（`play.promotional-content-and-best-practices`，核对日 2026-10-23）的改写摘要，不是官方页面的逐字副本。英文官方页面是效力来源。`kb_checked_at` 是快照源文件记录的核对日；本次导入没有重新打开线上官方页面。文中“本知识库”“本库”“本地专题”等说法描述的是该快照库的覆盖范围，不是本仓库已经导入的页面。指向本仓库没有收录的专题、链接图、台账或 CSV 的相对链接改为文字提及。指向 Google batch 1–6 或本批十二个专题的相对链接改为本仓库文件。核对日 2026-10-23。英文帮助正文可读，目录中的十篇文章都已打开。对应的 `zh-CN` 帮助页未能稳定取得。本仓库中文正文是编辑改写，不是已核验的 Google 中文译文。该读取限制不是政策变更。本页没有记录 2027-01-27。预览窗口、字符上限和报表区间是产品参数，不是政策生效日。本页是 operational 的推广内容说明。通过质量审核不保证出现在首页或搜索中。约会类标题质量指南是内容质量文章，不是真钱赌博政策。自定义受众仍是独立的 Console 工具，不是政策豁免。账号专属 Console 页面和部分 API 后代仍只是部分覆盖。

**核对日期：2026-10-23。** 本专题将 Google Play 帮助中心“Promotional content”目录中的 10 篇指南、创建流程、质量审查、深链、动画、YouTube 和效果评估资料汇总为可执行检查路径。它们主要是产品资格、提交流程和内容质量要求；是否能使用功能取决于应用/游戏类型、Premium growth tools 资格及账号权限。内容质量通过也不保证获得首页或搜索推荐。

英文帮助正文可读；相关 `zh-CN` 帮助页面在本次访问中未能稳定取得，因此中文是根据英文官方页面整理的双语改写，不代表核验了 Google 的中文译文。目录中的 10 篇正文均已打开；正文里的账号专属 Console 页面、支持入口及部分技术/API后代仍存在访问限制，不能据此声称递归链接闭合。

## 快速决策与期限

| 检查点 | 官方说明 | 实务含义 |
| --- | --- | --- |
| 可用资格 | Promotional Content 面向所有游戏；应用须满足 Premium growth tools 资格。Featuring、受众定向和 Promotional Content 深链另受相应资格限制。 | 先在 Play Console 确认账号实际入口与资格，不要把公开帮助页当作已获准使用。 |
| 最早提交 | 活动最早可在开始日前 60 天提交。 | 将准备和审核排期放在最早提交窗口内。 |
| 审核缓冲 | 创建页说最多可能需要 4 天；质量审查页说通常少于 24 小时，但建议开始前至少 4 天提交，以便修复问题。 | 按 4 天预留；被拒后重新提交至少还要 24 小时才可能上线。 |
| Featuring 申请 | 请求推荐的活动须至少在开始前 14 天提交。每季度名额重置；游戏面向广泛受众 4 次、特定受众 2 次；应用分别为最多 6 次和 2 次。 | 这是申请配额而非曝光保证。符合资格、审核通过也不保证被推荐。 |
| 预告展示 | 可在开始前最多 14 天预览；Offer 不可预览。 | 预览功能可让用户登记活动提醒。 |
| 事件长度 | 创建页正文写一般事件最长 4 周；同页 FAQ 又以限时活动说明“30 天内结束”。Major update 固定 28 天；预注册公告固定 1 周。 | “4 周”和“30 天”文本有边界差异，排期时采用更严格的 28 天或在 Console 核实，不自行认定二者等同。 |
| 国家/地区分组 | 同一活动可给不同国家设置不同起止时间；所有国家组的开始日期须在同一日历季度。跨季度要建不同活动；多国家组的推荐申请仍只消耗一个名额。 | 以每个地区的开始日期核对季度；把跨季度活动拆开。 |

创建页对“创建活动是否消耗配额”的表述需结合后文理解：**配额是 featuring request 配额**。不请求推荐而只创建活动，不消耗 featuring 次数；已提交的推荐申请仅在活动落入当前季度且非草稿时按规则计数。多国家日期组共用一次申请。对于失败后重新提交、取消等情形，原请求如何计数按来源页具体规则处理。

## 活动类型、受众和数据关系

Promotional Content 类型包括优惠、限时事件和重大更新。优惠可为折扣、增值组合、限时免费奖励或订阅试用；限时事件包括实时活动、竞赛/挑战和特殊事件；重大更新包括新功能/公告、新内容及预注册更新。错误分类会限制展示资格。

Play 可定向所有人、潜在用户、流失/沉睡用户、购买状态用户或自定义受众。官方定义中，流失用户已卸载；沉睡用户过去 28 天没有打开应用；沉睡买家过去 180 天没有购买。购买状态细分只适用于通过 Google Play Billing 处理的购买。自定义受众的 CSV 与 Grouping API 数据源、门槛和隐私边界见[自定义受众与 Grouping API](../custom-audiences-and-grouping-api/custom-audiences-and-grouping-api.zh-CN.md)。这些平台定向功能不代替开发者对实际数据处理做 User Data、Data safety 和适用法律核对。

## 内容质量：先让用户看懂“是什么、有什么好处、怎么参与”

### 文案与本地化

- Tagline 必填，最多 80 个字符；应直接说清活动/更新/优惠是什么，避免通用口号和按钮指令。优惠要明确用户获得的金额或折扣、商品范围、最低购买门槛、资格限制和关键账单条件；重要优惠值尽量放在前 40 个字符。
- Spotlight 格式的标题有更严格上限：单字节语言 48 字符，中文、日文、韩文等双字节语言 23 字符。符合此格式的预览仍不保证被选中。
- Description 必填，最多 500 字符；解释用户收益/卖点、参与方法、领取或兑换条件。官方建议至少 100 字符；不写与活动无关的通用应用介绍，不重复 tagline。以完整短段落表达，避免无意义 CTA、错误语言或低质量翻译。
- 每个目标国家需有适配的语言描述；Google Play 只会把活动展示给国家/语言与已提供本地化内容相匹配的用户。翻译应符合当地语言、文化、日期、时间和货币习惯。
- 文案需为新颖、具体、对用户可见的活动；常青服务介绍、日常例行活动、重复或非常相似的素材、同一时间提交多个重复活动可能被拒或限制曝光。活动须在应用内同步运行，并让用户打开应用后容易找到相关内容。
- 总则还写明活动应适用于所有用户；若只有满足最低等级的用户可参加，须在描述中说明，唯一明确写出的受众范围例外是“新用户”优惠。创建流程又提供流失/购买状态及自定义受众定向；两页没有解释这两条如何逐情形适用，因此不能推断任何“特定受众 + 活动”组合自动合规，应在 Console 核对适用条件并清楚披露参与资格。
- 质量页对标点、大小写、HTML、行距和说明要求较细；PDF 快速指南也建议文字本地化且避免项目符号。按帮助中心具体字段规则校对，而非只依赖摘要 PDF。

### 图片、动画、视频

| 素材 | 核心规格与限制 |
| --- | --- |
| 主图 | JPG 或 24-bit PNG；1920×1080、16:9；有视频时必须提供主图。关键主体放在安全区：上 15%、左右各 10%、下 20% 的裁切边界之外（主体保持在中心安全区域）；不要边框、文字、品牌 Logo、商店徽章或仿按钮/开关元素。Spotlight 主图建议不超过 1 MB。 |
| 方图 | 创建页要求方图，用于部分 Play 展示面；具体尺寸以创建表单当前校验为准。 |
| 动画 | Lottie JSON；≤200 KB、60 FPS、≤6 秒、16:9；须无缝循环。关键元素安全区：上 15%、左右 20%、下 20%。不要文字、Logo、折扣文案、仿 UI、商店排名/奖项；需同时提交静态图，建议提供无动画时的替代图及屏幕阅读器描述。 |
| 活动视频 | 内容须与活动具体相关，横屏、可嵌入，并设为公开或不公开列出；关闭变现。若版权声明仍会带广告，需换成无相关变现声明的视频；本地化画面、字幕和音频。通常仅前 30 秒自动播放。 |
| YouTube 展示功能 | 这是 Premium growth tools 下的单独频道/播放列表展示功能，要求与“活动视频”字段区分：YouTube 展示页要求视频公开（不能私密或不公开列出）、由应用/游戏所有、无变现、无无授权版权内容、非直播且可嵌入。游戏还受不同展示面的上传新鲜度窗口约束。 |

所有素材需和文案中的优惠/活动一致且专属于该活动。Google Play 质量页指出不遵守要求可能减少展示范围；内容仍须遵守开发者计划政策的受限内容要求。促销内容不得呈现令人震惊/恶心或露骨性内容；赌博/受监管类别的展示可能受限，且不得混淆娱乐玩法与现实经济活动。该功能当前排除某些金融建议、投资、借贷、信贷修复、加密货币及二元期权主题。约会应用促销文案须包容、不歧视，不应按年龄、宗教、性取向、种族/残障等群体作排斥式宣传。

### 优惠资格

优惠须提供货币折扣或原本购买/使用之外的增量商品/服务；质量指南说建议折扣或增量价值至少 10%，属于“建议”而不是本文明确写出的硬性最低门槛。须具体说明商品/SKU或类别、价值、运行机制及适用人群。通常不得限制为“前 500 名”等极少量；应能在 Android 应用内兑换；返现应在购物篮/结账时体现，不能要求邮寄或邮件返现。不得把日常低价包装成临时折扣；新用户专属的常青优惠是文档列出的例外。优惠还须遵守当地/国家法律，不能用作付费应用/游戏本体降价，后者应使用 Play Console 的付费应用促销功能。

## 深层链接：让活动卡片落到对应体验

深链为可选项，但如使用，应与活动标题、描述、优惠或更新一致，落到可理解且容易参与的应用内页面。Play 支持 Android App Links 与自定义 scheme，不支持经过重定向或第三方深链服务跳转的方案；提交时会检查链接是否出现在应用 Manifest 且 URL 未损坏。每个活动只能配置一个深链；不同地区要去不同目的地时应创建不同活动。深链只在已安装用户从活动卡点“Open”时工作；新用户点击“Install”并安装后不会保留该深链。修改既有深链结构/intent filter 可能要求重新提交活动。详见[Promotional Content 深链指南](https://support.google.com/googleplay/android-developer/answer/15322603)及[Android App Links 官方开发指南](https://developer.android.com/training/app-links)。

## 审核、修复和监测

每次提交都会按多个语言做内容质量审查。未通过质量指南但符合政策的内容仍可能出现在应用详情页，但不具备在更多 Play 展示面的资格。常见失败包括素材或文案不符合要求、本地化不足、优惠资格不符、内容不清楚或互相矛盾、政策问题，以及活动类型选错。Console 会指出失败的语言和状态；对排定或已上线的活动可编辑并重新提交，原活动会取消并被新版本替换，新版本最早在提交 24 小时后上线。重新提交不额外消耗一笔 featuring quota，但原请求/新版本按页面说明处理。

报告区分独立用户数与展示次数：独立浏览者和转化者按用户统计；Open、Update、Install 是转换行为。图表提供每日和 28 天滚动视图；多个活动可比较，达到 10 个或以上时只提供汇总表现。活动卡片带来的互动提升看 active days，并以卡片留出组对照，评估其后 28 天；Featuring uplift 衡量更高店面展示带来的额外获客，通常比较 7–14 天推荐期的处理组和留出组。两种 uplift 含义不同，不能把相关性或总转化直接当成因果效果；结论按官方的 95% 置信规则显示为明确、不明确或数据不足。

## 官方目录的 10 篇子页面与关系

| 目录子页 | 本专题所用内容 | 核验状态（2026-10-23） |
| --- | --- | --- |
| [Understand promotional content](https://support.google.com/googleplay/android-developer/answer/12929029) | 功能用途、展示面、优惠/限时事件/重大更新的类型边界。 | 英文正文完整打开；正文和目录链接已尝试；登录专属支持入口不可读。 |
| [Content quality guidelines](https://support.google.com/googleplay/android-developer/answer/12929944) | 文案、语言、主图、动画、视频、优惠、受限内容与金融主题限制。 | 英文正文完整打开；重要规范被摘要。内嵌图像和账号侧栏资源并非全部可读取。 |
| [Dating-title quality guidance](https://support.google.com/googleplay/android-developer/answer/15678263) | 约会类文案需包容，避免按受保护/敏感人群作排斥式营销。 | 英文正文完整打开；其余为重复目录/支持入口。 |
| [Create promotional content](https://support.google.com/googleplay/android-developer/answer/12932541) | 提交时点、活动类型、国家/日期、受众、推荐配额、素材、CSV、不可编辑规则。 | 英文正文完整打开；正文可见链接已逐项核验或与下表目标交叉核对；Console 需登录。 |
| [Track and fix quality issues](https://support.google.com/googleplay/android-developer/answer/12932123) | 审查、失败原因、修复/重新提交、图文视频本地化和常见错误。 | 英文正文完整打开；5 页[官方 PDF 检查指南](https://services.google.com/fh/files/helpcenter/google_play_promotional_content_guidelines.pdf)已读；Console/支持登录限制，Developer Program Policies 直链本次超时。 |
| [View your events](https://support.google.com/googleplay/android-developer/answer/12932229) | 草稿、排定、上线、已停止/过期状态；查看、复制、预览、停止。 | 英文正文完整打开；绩效及质量页面链接已打开；Console 操作需账号权限。 |
| [Evaluate promotional-content performance](https://support.google.com/googleplay/android-developer/answer/12932124) | 活动指标、获客和互动 uplift、报表筛选/导出。 | 英文正文完整打开；Console/Cloud Storage 导出需账号/项目权限；开发者指南等后代未全部展开。 |
| [Add deep links](https://support.google.com/googleplay/android-developer/answer/15322603) | 支持类型、重定向限制、安装后行为、单活动限制和验证。 | 英文正文完整打开；Android App Links 和 custom scheme 目标可读；Play Console 的深链管理需登录。 |
| [Showcase YouTube videos](https://support.google.com/googleplay/android-developer/answer/15501235) | 单独的 YouTube 频道/播放列表展示、许可、公开/嵌入、变现/版权与效果指标。 | 英文正文完整打开；YouTube Analytics 目标已识别；Play Console 提交和账号绩效面板需登录。 |
| [Animated asset guidelines](https://support.google.com/googleplay/android-developer/answer/16009268) | Lottie 技术规格、安全区、文案禁限、无障碍与视觉建议。 | 英文正文完整打开；受限内容和总质量指南已打开/交叉核对；社区及支持目标失败或登录受限。 |

## 页面链接的审计边界

Help 目录已打开并且 10/10 子页正文均被打开。创建页的 Premium growth tools、自定义受众、深链、商店详情、内容质量/素材要求和 Console 入口与本库主题交叉链接；内容质量、追踪修复、效果报表、YouTube 与动画页的重复侧栏均视为目录导航，不再将每次重复计为新目标。高价值新增孙页面（PDF、约会类规范、效果衡量、YouTube 展示）已摘要。Play Console、支持、云存储和账号设置需登录；外部 API、YouTube/云导出技术树、帮助侧栏之外的通用导航、所有图像附件及其下游链接没有全部递归审阅。原始 HTML 抽取的可见正文 URL 与图片/脚本链接并非同一范围。

功能开放资格、推荐展示、国家/语言可见性和账号权限均需在开发者自身 Console 中复核。此专题不是政策合规审查或推荐保证。
