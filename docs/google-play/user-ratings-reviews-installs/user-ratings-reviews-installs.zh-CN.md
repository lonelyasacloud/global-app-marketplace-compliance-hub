---
id: google-play.user-ratings-reviews-installs
platform: google-play
language: zh-CN
authority: normative
status: current
kb_checked_at: 2026-10-22
review_due: 2027-01-22
regions: [global]
topics: [store-listing, ratings, reviews, installs, ranking, in-app-review]
snapshot_id: play.user-ratings-reviews-installs
snapshot_package: "GooglePlay-KnowledgeBase-2026-10-24-review.zip"
coverage_status: "detailed-summary"
source_url: "https://support.google.com/googleplay/android-developer/answer/9898684?hl=en"
source_url_zh_attempt: "https://support.google.com/googleplay/android-developer/answer/9898684?hl=zh-CN"
source_url_store_listing_topic: "https://support.google.com/googleplay/android-developer/topic/9877064?hl=en"
source_url_in_app_review_api: "https://developer.android.com/guide/playcore/in-app-review?hl=en"
source_url_in_app_review_kotlin_java: "https://developer.android.com/guide/playcore/in-app-review/kotlin-java?hl=en"
source_url_store_listing_topic_zh: "https://support.google.com/googleplay/android-developer/topic/9877064?hl=zh-CN"
source_url_in_app_review_api_zh: "https://developer.android.com/guide/playcore/in-app-review?hl=zh-cn"
source_url_in_app_review_kotlin_java_zh: "https://developer.android.com/guide/playcore/in-app-review/kotlin-java?hl=zh-cn"
effective_date: "current developer policy; Chinese Help cache miss; no 2027-01-27"
---

# Google Play 评分、评价与安装量政策

> **导入说明（Google batch 7）。** 正文来自已经分开的 2026-10-24 Google Play 知识库快照（`play.user-ratings-reviews-installs`，核对日 2026-10-22）的改写摘要，不是官方页面的逐字副本。英文官方页面是效力来源。`kb_checked_at` 是快照源文件记录的核对日；本次导入没有重新打开线上官方页面。文中“本知识库”“本库”“本地专题”等说法描述的是该快照库的覆盖范围，不是本仓库已经导入的页面。指向本仓库没有收录的专题、链接图、台账或 CSV 的相对链接改为文字提及。指向 Google batch 1–6 或本批十二个专题的相对链接改为本仓库文件。核对日 2026-10-22。英文政策正文和 Key Considerations 已打开。简体中文帮助 URL 返回缓存未命中。本仓库中文正文是编辑改写，没有对照中文官方正文核对。该缓存未命中不是政策变更。本源文件还记录相邻的内容分级中文 URL 缓存未命中；内容分级专题自己记录了语言差异。本页没有记录 2027-01-27。本页是面向开发者的 `normative` 政策。概述与完整政策冲突时，以完整政策为准。应用内评价 API 是 implementation note，不能授权本政策禁止的评分提示。消费者评价发布政策是独立专题。

**核对日期：2026-10-22。** 本页逐段整理了 Play Console Help 的英文政策正文和 Key Considerations。简体中文帮助页 URL 在本次抓取中返回缓存未命中，因此中文内容是对已打开英文页面的双语改写，不代表中文页面也已逐字核验。政策摘要页面声明：发生冲突时以完整政策为准。

## 核心规则：不得操纵 Play 排名

开发者不得以不正当方式影响应用在 Google Play 上的展示位置，包括人为抬高评分、评价或安装量。政策明确举例：

- 以优惠、折扣或其他利益换取评分/评价；不应暗示用户必须给高分才可获得奖励。
- 冒充普通用户反复提交评分，以影响应用排名。
- 提交或鼓励用户发布带有推广性质或不适当内容的评价，例如 affiliate 信息、优惠券、游戏兑换码、电子邮件地址，或指向网站/其他应用的链接。
- 把奖励用户安装其他应用作为本应用的主要功能。
- 使用自动化服务虚增评分或安装量；Key Considerations 将其列为明确的禁止做法。

这项政策关注真实性和排名操纵。正常获客、真实用户自主安装、诚实评价以及对评价的正常回应不等同于操纵；关键在于是否造假、施压、奖励或把无关推广伪装成真实用户反馈。

## 邀请评价与回复评价

政策允许以清晰、非欺骗的方式邀请用户评分，并鼓励开发者通过优秀体验赢得正面反馈、倾听社区意见。不得使用欺骗性弹窗强迫用户评分，也不得用奖励换取评分/评价。

开发者回复评价时，应聚焦用户实际提出的问题，不要索要更高评分；可以提供有帮助的支持邮箱或 FAQ。评价回复的目标是解决体验问题，而非改变评价分数。

## Android 应用内评价 API：技术最佳实践（不是独立政策条款）

[Google Play In-App Reviews API 指南](https://developer.android.com/guide/playcore/in-app-review?hl=zh-cn)是 Android 技术资料，不是上述 Play 政策正文的直接链接。它帮助落实不施压、不过度请求的原则：

- 等用户充分体验应用、能够给出有用反馈后再展示请求；不要过度频繁触发。
- 展示评分卡之前或期间，不先问用户是否喜欢应用、会给几星等筛选性或预测性问题。
- 将 Google Play 提供的评分卡原样展示；不要改尺寸、透明度、形状，不加覆盖层，也不要在展示后以代码移除。
- API 有按时间变化的展示配额，具体数值属于实现细节且可能改变。不要假定每次调用都会显示，也不要把“点击按钮必然弹出评分卡”作为流程前提；若用户明确要求前往评价，可改为打开 Play 商店页面。
- API 完成回调不表示用户是否提交了评价，也不表示评分对话框是否出现；无论结果如何，都应继续应用原有流程。

[Kotlin/Java 集成指南](https://developer.android.com/guide/playcore/in-app-review/kotlin-java?hl=zh-cn)进一步说明 Play Core Review Library 的集成、`ReviewManager`、请求 `ReviewInfo` 及启动流程。ReviewInfo 只在有限时间内有效；调用失败或对话框未显示时，不要改变正常应用流程。

## 直接链接与相邻主题清单

本次打开的 `9898684` 页面正文没有指向其他政策正文、申报表或最佳实践页的实质性超链接；示例图片、反馈问卷、帮助社区/联系支持属于图片或通用反馈/支持入口，不作为政策后代。页面侧栏显示 5 个 Store Listing and Promotion 主题项（含本页；另有 4 个相邻主题），需与正文链接分开看待：

| 侧栏/辅助链接 | 页面关系 | 本次覆盖状态 |
| --- | --- | --- |
| [Store Listing and Promotion 主题索引](https://support.google.com/googleplay/android-developer/topic/9877064?hl=zh-CN) | 汇总商店展示与推广的相邻政策主题。 | 页面已打开；侧栏主题在链接图中单独登记。 |
| [App Promotion](https://support.google.com/googleplay/android-developer/answer/9899004?hl=zh-CN) | 处理推广、诱导安装、误导展示等；与奖励式安装/排名操纵相邻。 | 已有双语广告与推广专题和来源摘要。 |
| [Metadata](https://support.google.com/googleplay/android-developer/answer/9898842?hl=zh-CN) | 规范标题、图标、说明等商店元数据；不得用排名、下载量等误导宣传。 | 已在[商店详情与素材专题](../store-listing-best-practices/store-listing-best-practices.zh-CN.md)交叉整理。 |
| 本页自身 | Store Listing and Promotion 的评分/评价/安装量主题。 | 英文政策正文已完整打开；中文帮助页本次缓存未命中。 |
| [Content Ratings](https://support.google.com/googleplay/android-developer/answer/9859655?hl=zh-CN) | 内容分级与商店页面、广告受众相邻，但不决定评价真实性。 | 英文正文已核验，简体中文 URL 本次缓存未命中；已新增双语[内容分级专题](../content-ratings/content-ratings.zh-CN.md)，整理问卷、广告适配、地区标签及链接后代。 |
| [News & Magazines](https://support.google.com/googleplay/android-developer/answer/9935326?hl=zh-CN) | 新闻/杂志应用类别专属要求；属于侧栏导航，不是评分规则的扩展。 | 已有双语专题。 |

政策中心另链接到面向 Play 用户的[评分与评价发布政策](../play-store-review-posting/play-store-review-posting.zh-CN.md)。它规定评论者可发布什么内容、评价可见性和版权限制；这不是本 Help Center 开发者政策正文的链接，也不能与开发者的评价获取/操纵规则合并理解。

本地关联专题：[商店详情与素材最佳实践](../store-listing-best-practices/store-listing-best-practices.zh-CN.md) · [内容分级、目标受众与广告适配](../content-ratings/content-ratings.zh-CN.md) · [广告与推广](../ads-and-advertising/ads-and-advertising.zh-CN.md) · [新闻与杂志](../news-and-magazines/news-and-magazines.zh-CN.md)。

Help Center 页面里没有从评分政策正文指向 In-App Reviews API 的链接。上文 API 及其集成指南是为了提供可操作的官方技术最佳实践而补充的关联资料；它们不能扩大、替代或重新定义政策义务。API 页的 Native、Unity、Unreal、测试、Play Core 条款等技术后代没有在本专题内递归收录，具体集成应继续按官方文档核对。

## 发布/运营核对清单

1. 检查激励、优惠、抽奖、游戏内奖励是否与评分/评价挂钩；如有，应移除该交换关系。
2. 检查评价采集渠道、代理商和自动化流程，确认没有虚假账号、重复提交或批量购买评价/安装。
3. 检查应用主要功能是否变成奖励用户安装其他应用；推广链接、affiliate 和优惠码不要塞入用户评价。
4. 评分提示需自愿、清晰、不欺骗；不要奖励或施压，也不要在评分卡出现前询问用户的态度或预期星级。
5. 评价回复聚焦问题并提供有效支持入口，不要求用户提高分数。
6. 使用 In-App Review API 时遵守原样展示、适时触发、配额会变化和继续正常流程等实现约束。

本专题是英文官方页面的双语摘要和链接分析，不是政策原文镜像。排名和评价规则、API 行为及 Play Console 处置可能更新；提交前请复查官方当前页面。
