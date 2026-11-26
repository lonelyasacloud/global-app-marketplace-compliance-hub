---
id: google-play.custom-audiences-and-grouping-api
platform: google-play
language: zh-CN
authority: operational
status: current
kb_checked_at: 2026-10-23
review_due: 2027-01-23
regions: [global]
topics: [custom-audiences, grouping-api, store-listing, promotional-content, privacy]
snapshot_id: play.custom-audiences-and-grouping-api
snapshot_package: "GooglePlay-KnowledgeBase-2026-10-24-review.zip"
coverage_status: "detailed-summary"
source_url: "https://support.google.com/googleplay/android-developer/answer/15854918?hl=en"
source_url_custom_listings: "https://support.google.com/googleplay/android-developer/answer/9867158?hl=en"
source_url_grouping_api: "https://support.google.com/googleplay/android-developer/answer/14840298?hl=en"
effective_date: "operational-help; no future Play policy date"
---

# Google Play 自定义受众与 Grouping API

> **导入说明（Google batch 5）。** 正文来自已经分开的 2026-10-24 Google Play 知识库快照（`play.custom-audiences-and-grouping-api`，核对日 2026-10-23）的改写摘要，不是官方页面的逐字副本。英文官方页面是效力来源。`kb_checked_at` 是快照源文件记录的核对日；本次导入没有重新打开线上官方页面。文中“本知识库”“本库”“本地专题”等说法描述的是该快照库的覆盖范围，不是本仓库已经导入的页面。指向本仓库没有收录的专题、链接图、台账或 CSV 的相对链接改为文字提及。指向 Google batch 1–4 或本批八个专题的相对链接改为本仓库文件。 快照采用可读的英文帮助正文。相应的 `?hl=zh-CN` 页面在该次抓取中不可访问。本仓库中文正文是英文来源的改写，不是已经核验的 Google 中文译文，也不是已核对的中文官方页面。该访问失败不是政策变更。快照没有记录未来生效的 Play 政策日期。5,000 个地址门槛、约 24 小时匹配、受众 90 天过期、令牌 30 天 TTL 和标签 90 天 TTL 是帮助文章记录的产品参数；集成指南称这些数值可能变化。它们不是 Play 政策生效日，CSV 门槛也不是收集或上传电子邮箱的法律依据。这些页面描述的是符合资格的开发者可用的增长工具，属于操作层面的 Console 说明，不是开发者计划政策的豁免，也不保证每个账号都能使用该功能。User Data 和 Data safety 义务留在各自页面，在那些页面仍是 `normative`。

**核对日期：2026-10-23。** 本页汇总自定义商店详情页和 Play Console 自定义受众帮助文档。它们介绍的是有资格的开发者可使用的增长工具和配置流程，不是对所有应用普遍适用的独立政策豁免或保证。

本专题以可读的英文帮助正文为依据；相应 `?hl=zh-CN` 页面在本次抓取中不可访问，因此中文部分是基于英文原文的双语改写，不代表已验证 Google 的中文译文。

## 先区分两种受众来源

自定义商店详情页可按国家/地区、预注册状态、搜索关键词、广告流量或特定用户群体显示不同文案和素材；页面最多可创建 50 个自定义详情页。自定义详情仍须准确反映应用及其功能，并遵守 Metadata 等政策。它们不会自动翻译；开发者需为目标语言提供翻译。联系信息、隐私政策和应用类别在不同详情页之间共用。更多详情见商店详情与素材最佳实践[商店详情与素材最佳实践](../store-listing-best-practices/store-listing-best-practices.zh-CN.md)。

Play Console 的自定义受众有两类来源：

1. **CSV 邮箱列表：**帮助页要求原始文件至少 5,000 个邮箱。匹配通常约需 24 小时；受众 90 天后过期，需要上传新的、超过 5,000 个地址的文件续期。匹配数低于门槛或受众过期时，正在使用该受众的活动可能暂停。此门槛是产品功能条件，不代表开发者因此获得收集、上传或营销使用邮箱的法律依据。
2. **Google Play Grouping API：**开发者以标签描述用户特征或行为，再在 Console 中用标签规则建受众并面向 Play 商店内容做定向。文档目前把标签定向用于 Promotional Content；功能只对符合条件的部分合作伙伴开放。

## Grouping API 的隐私和安全约束

- 首次使用时，Play 会向用户显示数据交换通知；Google 提供退出控制，文档将其链接到 [My Activity](https://myactivity.google.com/myactivity)。这不代表应用可跳过自身适用的数据披露、同意或 Data safety 评估。
- App 使用自己的用户/档案标识生成 persona 时，persona 必须是不含敏感或个人身份信息的加密或哈希不透明字符串。写入用户标签时，也不得把姓名、护照号、健康信息、族裔等敏感或可识别个人的信息放入标签。
- App 端生成的 token 必须由服务器验证后才能用于写标签；验证是强制的安全步骤。SDK 调用要求应用位于前台，并通过系统通知用户首次数据交换。游戏和普通应用的 token 获取流程不同。
- 文档给出的 token TTL 为 30 天、tag TTL 为 90 天；persona、tag 字段大小及标签键数量也有上限。具体值可能调整，应以当前集成文档为准。
- 邮箱列表和 Grouping API 都是将受众/用户标签与 Play 商店内容定向关联。应从实际数据流出发复核[用户数据政策](../user-data/user-data.zh-CN.md)和[数据安全表单](../data-safety/data-safety.zh-CN.md)：如果应用或其中的 SDK 收集/传输邮箱、用户标识或标签，应核实透明披露、目的限制、适用时的醒目披露/同意，以及隐私政策和 Data safety 申报。Data safety 将 email address 列为个人信息，并提供 advertising/marketing、personalization 等用途；但开发者在 Console 单独上传外部 CSV 是否属于特定应用表单的申报范围，不能只凭本功能页推断，需按应用实际处理和表单定义判定。

## 与 Promotional Content 和资格门槛的关系

Promotional Content 可在商店详情页及其他 Play 界面展示优惠、限时活动、新内容和重大更新；自定义受众可用于面向符合条件的人群定向活动。详细的活动类型、定向、提交流程和素材最佳实践见[推广内容](../promotional-content-and-best-practices/promotional-content-and-best-practices.zh-CN.md)。此项与用户群体无关的常规商店详情素材不是同一功能。

[Premium growth tools 资格页](https://google.play/business/guides/premium-growth-tools/)另列开发者账号良好状态、应用类别、活跃安装、MAU 和消费指标等门槛，并说明某些新游戏有阶段性资格。指标与受支持类别可能变动；不得把“有自定义受众帮助页”理解为自己的 Console 账号已开放功能。开发者账号权限页和 Console 内受众状态需要账号授权才能核验。

## 已追踪的直接链接

| 来源页面的链接 | 与本专题的关系 | 核验状态 |
| --- | --- | --- |
| [自定义商店详情页](https://support.google.com/googleplay/android-developer/answer/9867158?hl=en) | 用户/地区定向商店资料；指出自定义页不自动翻译、最多 50 页及共用的资料字段。 | 英文正文完整打开；10 个正文链接目标均已尝试，预注册、广告、翻译、素材、自定义受众和资格相关目标已打开或由已有专题交叉核对；Console、社区与支持路线分别受账号登录、抓取错误限制。 |
| [定义自定义受众](https://support.google.com/googleplay/android-developer/answer/15854918?hl=en) | CSV 邮箱列表和 Grouping API 两种受众数据源；包含 5,000 地址门槛、约 24 小时匹配和 90 天续期规则。 | 英文正文完整打开；正文目标均尝试；Console 目标要求账号登录，社区返回 Cache miss，支持页转入账号专属流程。 |
| [Play Grouping API 概览](https://support.google.com/googleplay/android-developer/answer/14840298?hl=en) | 说明定向用途、首次用户通知、My Activity 退出控制、资格和 app/game 集成差异。 | 正文完整打开；核心资格、隐私控制、集成说明和权限目标已尝试；Play Console 配置需登录。 |
| [Grouping API 集成指南](https://support.google.com/googleplay/android-developer/answer/15239759?hl=en) | 详细说明 token、persona、服务器验证、标签写入、过期、SDK 与游戏流程。 | 523 行正文已打开；本专题提取与隐私/安全直接相关的规则。云端 API、SDK、Play Games Services、代码示例和技术参考的全部后代尚未穷尽；共享 Drive 代码库及动态 API 文档不作为政策义务。 |
| [Premium growth tools](https://google.play/business/guides/premium-growth-tools/)；[Promotional content](https://google.play/business/programs/promotionalcontent/) | 确认功能的适用资格和其在 Play 商店中的促销用途。 | 两个公开页面均已打开；其培训、营销和站点导航链接不等同于开发者计划政策。 |
| [My Activity](https://myactivity.google.com/myactivity) | Grouping API 页面提供的用户控制入口。 | 目标打开后要求用户登录以管理个人设置；只据公开页面记录其用途，不推断个人账号状态。 |
| 政策交叉核对：[User Data](https://support.google.com/googleplay/android-developer/answer/10144311?hl=en) 与 [Data safety](https://support.google.com/googleplay/android-developer/answer/10787469?hl=en) | User Data 规定 app/SDK 数据处理须透明、限于合规且合理预期的用途，并在不符合用户合理预期时满足醒目披露/同意要求；Data safety 把 email address 列为 Personal info，并列有 Advertising or marketing、Personalization 等用途。 | 两篇英文现行正文在本次重开；`answer/10144311` 通过 Data safety 正文的政策链接打开。该交叉核对不是对外部 CSV 上传应填哪一项的结论。 |

### 自定义商店详情页的正文子链接

| 直接目标 | 内容及与父页的关系 | 核验状态 |
| --- | --- | --- |
| [预注册帮助页](https://support.google.com/googleplay/android-developer/answer/9859047?hl=en) | 介绍上架前预注册活动；正文写明单个活动最长 90 天、最多同时运行两个预注册应用/游戏，并链接审核准备、素材翻译、广告声明和付款/奖励配置。 | 正文已打开；摘要和发布流程见[测试与发布专题](../publishing/play-release-workflow.zh-CN.md)，其大量 Console 操作和技术后代仍未全部展开。 |
| [Google Ads：创建广告系列](https://support.google.com/google-ads/answer/6324971) | 说明广告目标和不同广告系列设置；自定义商店页可与广告活动素材保持一致。它是 Google Ads 的实施帮助，不是 Play 政策。 | 正文已打开；广告系统后代不纳入 Play 政策条款。 |
| [翻译与本地化](https://support.google.com/googleplay/android-developer/answer/9844778?hl=en) | 说明商店资料、应用内商品和字符串翻译；与自定义页不自动翻译的限制互补。 | 正文已打开，已有[应用设置与发布专题](../play-console-app-setup/play-console-app-setup.zh-CN.md)摘要。 |
| Google Ads App Campaign 链接 | 自定义详情页可按广告组关联；点击后返回 Internal Error，未暴露可核实的目标地址。 | 目标链接无法读取；未推断其内容或精确 URL。 |
| [AdMob](https://admob.google.com/home/resources/what-is-admob/) | 广告平台说明；父页指出广告目标的自定义商店详情可能因流量来源而显示。 | 页面已打开；产品概览不是 Play 适用性规则。 |
| [自定义受众帮助页](https://support.google.com/googleplay/android-developer/answer/15854918?hl=en)；[图形素材帮助页](https://support.google.com/googleplay/android-developer/answer/9866151?hl=en) | 分别扩展用户群体定向和素材规格；自定义商店页自身还链接到同页“创建详情页/详情组”步骤。 | 两个目标均已打开；素材要点见本地商店详情专题；同页锚点已归并。 |
| [Play Console](https://play.google.com/console) | 创建/发布详情页的操作入口。 | 此通用入口重定向到 Google Play for business 公开页；实际应用配置需登录 Console。 |
| 帮助社区与[联系支持](https://support.google.com/googleplay/android-developer/gethelp) | 求助渠道，不是政策依据。 | 社区点击超时；支持页转入账号专属 Console 求助流程。 |

### 自定义受众与 Grouping API 的正文后代

| 直接目标 | 关系 | 核验状态 |
| --- | --- | --- |
| [Premium growth tools 资格页](https://google.play/business/guides/premium-growth-tools/) 与 [Promotional Content](https://google.play/business/programs/promotionalcontent/) | 前者解释账号状态、应用类别和活跃安装/MAU/消费指标等功能资格；后者说明 Play 上优惠、限时活动、新内容和重大更新的展示用途。 | 两页正文已打开；门槛、受支持类别和产品页面会调整，采取行动前应复查。 |
| [Grouping API 概览](https://support.google.com/googleplay/android-developer/answer/14840298?hl=en) 与[集成指南](https://support.google.com/googleplay/android-developer/answer/15239759?hl=en) | 解释标签受众如何用于 Promotional Content，以及 app/game 的 token、persona、服务端和 SDK 流程。 | 两篇 Help 正文均已打开；集成指南的政策相关隐私/安全部分已摘要。 |
| [Play 帐号权限说明](https://support.google.com/googleplay/android-developer/answer/9844686?hl=en)；[查看应用统计](https://support.google.com/googleplay/android-developer/answer/139628?hl=en) | 管理受众需要相应 Play Console 用户权限；统计页可按受众查看活动表现。 | 两篇正文已打开；账号内权限和真实匹配数需由获授权的 Console 用户查看。 |
| [My Activity](https://myactivity.google.com/myactivity) | Grouping API 向用户提供的退出控制入口。 | 页面打开并显示登录要求；无法读取任何个人设置或账户状态。 |
| 云端 API/游戏实现： [Google Cloud Console](https://console.cloud.google.com/)、[API Keys 概览](https://docs.cloud.google.com/api-keys/docs/overview)、[Play Games Services 入门](https://developer.android.com/games/pgs/start)、[服务器访问](https://developer.android.com/games/pgs/android/server-access)、[Recall 集成](https://developer.android.com/games/pgs/recall/recall-setup)、[Console 配置](https://developer.android.com/games/pgs/console/setup)、[发布游戏改动](https://developer.android.com/games/pgs/console/publish) | 这些后代指导 OAuth、服务器登录、Recall、API key 与发布流程；它们不改变 Play 用户数据规则。 | 页面均已打开；Google Cloud Console 要求登录。共享 Drive 代码示例返回 Internal Error；其内容未推断。 |
| [Grouping token API 参考](https://developer.android.com/games/services/web/api/rest/v1/accesstokens/generatePlayGroupingApiToken) 与 [Recall token API 参考](https://developer.android.com/games/services/web/api/rest/v1/accesstokens/generateRecallPlayGroupingApiToken)；[Google APIs 公共定义库](https://github.com/googleapis/googleapis) | 描述游戏端 token 生成接口及公共 API 定义代码库。 | API 页面与 GitHub 仓库均打开；属于技术后代，未复制其整套 API/源码。Help 指向的共享 Drive 代码附件仍不可读。 |
| Play Console 配置、报表、帮助社区和联系支持 | 配置项目关联/权限、查看报告或请求帮助。 | Console 路由要求登录；部分动态报表链接未返回可读取正文；社区/支持目标抓取失败。 |

**范围边界：**本专题覆盖被审阅来源页的政策相关正文链接，以及 Grouping API 的隐私/安全关键后代；不递归收录共享页脚、站点导航、全部 Google Cloud/Play Games API 参考和账户内页面。现有或受限目标的逐 URL 状态见来源页审计表（快照：`../source-page-audit.csv`，未导入本仓库）和递归链接图（快照：`../google-play-policy-link-graph.md`，未导入本仓库）。
