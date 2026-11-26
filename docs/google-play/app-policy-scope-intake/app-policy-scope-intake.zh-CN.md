---
id: google-play.app-policy-scope-intake
platform: google-play
language: zh-CN
authority: operational
status: current
kb_checked_at: 2026-10-23
review_due: 2027-01-23
regions: [global]
topics: [scope-intake, release-checklist, navigation]
snapshot_id: play.app-policy-scope-intake
snapshot_package: "GooglePlay-KnowledgeBase-2026-10-24-review.zip"
coverage_status: "operational-router"
source_url: "https://play.google.com/about/developer-content-policy/"
source_url_zh: "https://support.google.com/googleplay/android-developer/answer/9859455?hl=zh-CN"
effective_date: "router only; 2027-01-27 kept separate from other deadlines"
---

> **导入说明（Google batch 9）。** 正文来自已经分开的 2026-10-24 Google Play 知识库快照（`play.app-policy-scope-intake`，核对日 2026-10-23）的改写发布分流页，不是官方页面的逐字副本，也不是对任何应用的合规结论。英文官方页面是效力来源。`kb_checked_at` 是快照源文件记录的核对日；本次导入没有重新打开线上官方页面。文中“本知识库”“本库”“本地专题”等说法描述的是该快照库的覆盖范围，不是本仓库已经导入的页面。指向本仓库没有收录的专题、链接图、台账或 CSV 的相对链接改为文字提及。指向 Google batch 1–8 或本批八个专题的相对链接改为本仓库文件。中文源文件把审核准备文章记为 `hl=zh-CN`，把期限表记为 `hl=en`。英文源文件的审核准备文章使用 `hl=en`。快照没有记录该 `hl=zh-CN` 审核文章的逐行对照，也没有记录抓取失败。中文正文是编辑分流。2027-01-27 是联系人、位置、SMS/通话记录和地理围栏前台服务的未来预告，与 2026-11-01 的延期、2026-12-01 的美国外部内容链接报告、2027-02-01 的 16 KB 兼容、2027-03-15 的印度商户 KYC，以及 2027-03-31 的日本外部支付分开。快照中的离线 Wiki 没有导入。证据等级：Operational。

# 按应用功能定位 Google Play 政策

**核对日期：2026-10-23。** 这是一份政策导航和发布准备问卷，不是对具体应用的合规结论。按实际功能、受众、数据流、分发地区和 SDK 回答；选“是”或“说不清”时，打开对应专题及当前官方原文。选“否”也要有代码、SDK 清单或产品事实支撑。没有触发导航条目，不代表无需遵守开发者计划政策、开发者分发协议、当地法律或 Play Console 要求。

## 1. 每个 Play 应用都要过一遍的基础项

| 自检项 | 要检查什么 | 知识库入口 |
| --- | --- | --- |
| 开发者与应用身份 | 开发者资料、身份验证、软件包名登记、签名和应用所有权是否正确；如计划继续分发，确认 Console 中没有未完成验证或包名登记事项。 | [Play Console 要求](../play-console-requirements/play-console-requirements.zh-CN.md)、[Android 开发者验证](../android-developer-verification/android-developer-verification.zh-CN.md)、[开发者分发协议](../developer-distribution-agreement/developer-distribution-agreement.zh-CN.md) |
| 政策与地区范围 | 用途、内容、目标市场、年龄组和变现方式是否真实；逐一查看适用政策、地区限制及法律要求。 | [开发者计划政策合并版](../developer-program-policy/developer-program-policy.zh-CN.md)、[政策中心目录](../google-play-developer-policy-center/google-play-developer-policy-center.zh-CN.md)、[国家/地区分发专题](../country-specific-distribution/country-specific-distribution.zh-CN.md) |
| App content 与审核访问 | 广告、隐私政策、数据安全、年龄组、内容分级、敏感权限/专项声明是否与实际产品一致；审核人员能否登录全部受限功能。 | [审核准备](../app-review-preparation/app-review-preparation.zh-CN.md)、[Console 声明](../play-console-requirements/play-console-requirements.zh-CN.md)、[测试与发布流程](../publishing/play-release-workflow.zh-CN.md) |
| 版本与设备兼容 | 新应用/更新是否满足当前目标 API、设备形态、64 位及 16 KB 内存页要求；不要把目标 API 与 16 KB 两个独立门槛混为一谈。 | [目标 API 与兼容期限](../target-api/target-api-level.zh-CN.md)、[设备形态质量指南](../app-quality-and-form-factor-guidelines/app-quality-and-form-factor-guidelines.zh-CN.md) |
| 权限、数据与 SDK | 核对最终合并 Manifest、运行时权限、后台任务、SDK/库的数据收集与网络行为；表单、隐私政策和实际行为相符。 | [Android 隐私清单](../android-privacy-checklist/android-privacy-checklist.zh-CN.md)、[用户数据](../user-data/user-data.zh-CN.md)、[数据安全](../data-safety/data-safety.zh-CN.md)、[第三方 SDK](../sdk-requirements/sdk-requirements.zh-CN.md) |
| 提交、发布和后续状态 | 保留可复现构建、测试结果、审核凭证和申报状态；每次功能、数据、SDK、受众、地区或价格变化后重查相关声明，并监控 Policy status 和官方期限。 | [发布流程](../publishing/play-release-workflow.zh-CN.md)、[执行控制总表](../google-play-policy-operations/google-play-policy-operations.zh-CN.md)、离线 Wiki 政策期限视图（快照：`google-play-policy-wiki.html`，未导入本仓库） |

## 2. 按产品特征分流到专题

回答“是”或“说不清”时，沿本行的本地链接检查政策、实施做法和申报要求。具体项目是否适用，以官方现行条款和 Console 中实际任务为准。

| 应用是否…… | 优先检查 | 建议准备的证据 |
| --- | --- | --- |
| 面向儿童，或儿童可能使用；包含社交、约会、匿名/随机聊天功能 | [年龄限制与儿童安全](../age-restricted-child-safety/age-restricted-child-safety.zh-CN.md)、[内容分级](../content-ratings/content-ratings.zh-CN.md)、[UGC 与内容审核](../user-generated-content/user-generated-content.zh-CN.md) | 年龄目标依据、年龄门槛/限制流程、儿童安全标准声明、举报/屏蔽与处理记录、适龄广告/SDK 清单 |
| 允许用户上传、发布、评论、私信、直播或分享内容 | [UGC 与内容审核](../user-generated-content/user-generated-content.zh-CN.md)、[儿童安全](../age-restricted-child-safety/age-restricted-child-safety.zh-CN.md)、[不当内容](../inappropriate-content/inappropriate-content.zh-CN.md) | 用户条款、内容规则、举报和屏蔽路径、审核值班与升级记录、违规处置样例 |
| 生成或编辑 AI 内容，或把 AI 输出展示给其他用户 | [AI 生成内容与安全实践](../ai-generated-content/ai-generated-content.zh-CN.md)、[UGC](../user-generated-content/user-generated-content.zh-CN.md)、[不当内容](../inappropriate-content/inappropriate-content.zh-CN.md) | 输出风险测试、过滤/审核规则、用户举报路径、误报/漏报处置和版本记录 |
| 收集、访问、共享或出售用户个人/敏感数据，或集成会这样做的 SDK | [用户数据](../user-data/user-data.zh-CN.md)、[数据安全](../data-safety/data-safety.zh-CN.md)、[Android 隐私清单](../android-privacy-checklist/android-privacy-checklist.zh-CN.md)、[第三方 SDK](../sdk-requirements/sdk-requirements.zh-CN.md) | 数据流与接收方清单、SDK 版本/用途、隐私政策、Data safety 答案、披露/同意界面、保留和删除记录 |
| 创建用户账号，或允许用户关联第三方账号 | [账号与关联数据删除](../account-deletion/account-deletion.zh-CN.md)、[数据安全](../data-safety/data-safety.zh-CN.md) | 在已卸载应用的浏览器中实测网页请求；记录应用内入口、关联数据/服务商删除、处理时限、保留依据/期限和 Data safety 答案 |
| 请求联系人、精确/后台位置、照片/视频、SMS/通话记录、所有文件、应用列表、无障碍、安装包或健康权限 | [敏感权限总览](../sensitive-permissions/sensitive-permissions.zh-CN.md)、[权限声明](../permissions-declaration/permissions-declaration.zh-CN.md)，以及[联系人/位置](../contacts-location-permissions/contacts-location-permissions.zh-CN.md)、[照片/视频](../photo-video-permissions/photo-video-permissions.zh-CN.md)、[SMS/Call Log](../sms-call-log/sms-call-log.zh-CN.md)、[后台位置](../background-location/background-location.zh-CN.md)、[健康/Health Connect](../health-apps-and-health-connect/health-apps-and-health-connect.zh-CN.md) | 合并 Manifest、功能必要性、系统替代 API 测试、权限触发时机、显著披露/同意、Console 声明及审核视频 |
| 使用前台服务、后台定位、地理围栏或长时间后台任务 | [前台服务与地理围栏](../foreground-services-and-geofencing/foreground-services-and-geofencing.zh-CN.md)、[后台位置](../background-location/background-location.zh-CN.md) | 服务类型/权限、用户可感知任务说明、停止方式、后台启动测试、位置披露与 Console 申报 |
| 显示广告、赞助内容、推广自家应用，或通过评分/评价/安装量获客 | [广告与推广](../ads-and-advertising/ads-and-advertising.zh-CN.md)、[评分/评价/安装量](../user-ratings-reviews-installs/user-ratings-reviews-installs.zh-CN.md)、[商店详情最佳实践](../store-listing-best-practices/store-listing-best-practices.zh-CN.md) | 广告 SDK 和版位清单、受众/分级适配、商店素材授权、推广文案、评价激励和安装来源审查 |
| 销售数字内容、订阅、随机虚拟物品，或引导用户去站外购买/下载 | [付款、计费与订阅](../payments/payments-and-subscriptions.zh-CN.md)、[国家/地区分发](../country-specific-distribution/country-specific-distribution.zh-CN.md) | Play Billing 使用范围、适用计划资格与批准、价格/续订/取消、交易上报、用户支持及地区规则 |
| 提供贷款、金融、加密资产/NFT、真钱博彩、健康/医疗或新闻功能 | [金融与贷款](../financial-services-and-loans/financial-services-and-loans.zh-CN.md)、[加密资产](../crypto-assets-and-nfts/crypto-assets-and-nfts.zh-CN.md)、[真钱博彩](../real-money-gambling/real-money-gambling.zh-CN.md)、[健康应用](../health-apps-and-health-connect/health-apps-and-health-connect.zh-CN.md)、[新闻/杂志](../news-and-magazines/news-and-magazines.zh-CN.md) | 具体功能与类别申报、许可/监管依据、市场资格、年龄/地区屏蔽、健康声明及支持材料 |
| 面向政府场景、引用第三方品牌/作品，或依赖外部内容和授权 | [知识产权](../intellectual-property/intellectual-property.zh-CN.md)、[冒充身份](../impersonation/impersonation.zh-CN.md)、[虚假陈述](../misrepresentation/misrepresentation.zh-CN.md)、[国家/地区专题](../country-specific-distribution/country-specific-distribution.zh-CN.md) | 权利链和书面授权、政府授权/信息来源说明、市场/地域/期限范围、商店资料一致性 |
| 以 Google Play Books Partner Center 发布电子书或有声书 | [Play Books 出版内容政策](../google-play-books-content-policies/google-play-books-content-policies.zh-CN.md) | 出版权利、格式/预览、成熟内容与销售地区设置、出版者账号和投诉处理记录。Books 出版者规则与 Android 应用政策分开评估。 |
| 包含原生 `.so` 库、游戏引擎或第三方二进制 SDK | [目标 API 与 16 KB 页面专题](../target-api/target-api-level.zh-CN.md)、[第三方 SDK](../sdk-requirements/sdk-requirements.zh-CN.md) | AAB/APK 中所有 ABI 的原生库清单、ZIP/ELF 对齐报告、供应商兼容确认、16 KB 环境测试结果 |
| 新建个人开发者账号，或使用认证设备/开源平台/第三方商店分发 | [测试与发布流程](../publishing/play-release-workflow.zh-CN.md)、[Play Console 要求](../play-console-requirements/play-console-requirements.zh-CN.md)、[Android 开发者验证](../android-developer-verification/android-developer-verification.zh-CN.md) | 账号创建日期/类型、闭测及测试者记录、设备验证、包名/签名所有权证明、目标分发渠道和安装流程 |

## 3. 按期限先排工作

以下是 **2026-10-23** 的时间快照。[官方 Policy Deadlines 页面](https://support.google.com/googleplay/android-developer/table/12921780?hl=en)于该日重新核对，页面列出 4 项于 2027-01-27 生效的政策变化；下表还汇集在各自官方专题中跟踪的计划期限。日期只用于排优先级，资格、延期、参与计划和应用状态仍须回到官方页面及账号内 Console 核实。

| 日期 | 适用时要做什么 | 入口 |
| --- | --- | --- |
| 2026-11-01 | 若应用收到符合条件的 Target API 或 Billing Library v7 警告，分别在各自的 Policy status/Console 任务中处理延期；两种申请相互独立。 | [目标 API](../target-api/target-api-level.zh-CN.md)、[付款与订阅](../payments/payments-and-subscriptions.zh-CN.md)、[期限总表](../google-play-policy-operations/google-play-policy-operations.zh-CN.md) |
| 2026-12-01 | 仅 External Content Links 计划参与者核对成功下载申报及适用服务费。 | [美国外部内容链接](../us-external-content-links/us-external-content-links.zh-CN.md)、[期限总表](../google-play-policy-operations/google-play-policy-operations.zh-CN.md) |
| 2027-01-27 | 如应用使用联系人、精确位置、电话账号验证、SMS/Call Log 或以 Geofencing 作为前台服务用例，按专题迁移/更新声明。 | [联系人/位置](../contacts-location-permissions/contacts-location-permissions.zh-CN.md)、[短信/通话记录](../sms-call-log/sms-call-log.zh-CN.md)、[前台服务](../foreground-services-and-geofencing/foreground-services-and-geofencing.zh-CN.md) |
| 2027-02-01 | 若 Play 应用目标 API 35+ 且含 64 位原生库，完成 16 KB 兼容检查；不兼容的更新将不能发布。 | [目标 API 与 16 KB](../target-api/target-api-level.zh-CN.md) |
| 2027-03-15 | 仅印度境内商户面向印度以外销售时，核对 Payments 专题记录的 BillDesk 商户 KYC 截止与账号要求。 | [付款与订阅](../payments/payments-and-subscriptions.zh-CN.md)、[期限总表](../google-play-policy-operations/google-play-policy-operations.zh-CN.md) |
| 2027-03-31 | 仅日本 External Payments 现有参与者、且要继续外链付款时，完成向 Billing Choice 的过渡。 | [付款与订阅](../payments/payments-and-subscriptions.zh-CN.md)、[期限总表](../google-play-policy-operations/google-play-policy-operations.zh-CN.md) |

期限会变化。完整历史/现行状态与适用范围见可筛选的离线 Wiki 期限视图（快照：`google-play-policy-wiki.html`，未导入本仓库）和[政策执行控制总表](../google-play-policy-operations/google-play-policy-operations.zh-CN.md)；每次发布前仍应在线核实官方页面。

## 4. 建议按此顺序完成一次发布自查

1. 记录应用包名、账号类型、目标用户、分发国家/地区、收费方式和所有实际功能；将“不确定”功能先纳入检查范围。
2. 从最终构建产物而非仅从源码核对权限、SDK、数据流、原生库、广告和支付实现。
3. 按上表打开所有命中的专题，并在专题的官方来源表中继续核查具体声明、例外和地区要求。
4. 对照 App content、Data safety、隐私政策、商店页、内容分级、审核登录凭证和 Console 的警告/期限；保持这些材料与当前产品一致。
5. 留存能解释判断的证据，修复后再测；上线后遇到功能、SDK、市场、受众或政策变化时重新走相关分支。

## 5. 用 Play Policy Insights 辅助代码审查

[Android Play Policy Insights skill](https://github.com/android/skills/tree/main/play/play-policy-insights) 是面向 Android 应用代码仓库的自动化审查工具，不是政策正文、Play 审核决定或合规认证。已安装副本的元数据标注最后更新于 2026-07-13；该 Skill 要求重点核查 Data safety、审核登录凭据和受限权限。其 `policies.json` 列出 16 个检查域及 31 个官方来源 URL；截至 2026-10-23，这 31 个 URL 都已进入本知识库来源台账，但登记目标不等于所有孙链接均已闭合。

该 Skill 应用于 Android 应用代码库，而不是本知识库目录。把它的发现映射到下表专题后，还要用最终构建产物、合并 Manifest、SDK 行为、Data safety/商店资料、审核凭据和账号内 Play Console 任务人工复核。静态代码信号不能单独证明实际运行时数据流、账号状态或 Play 审批。

| Skill 检查域 | 知识库对应专题 |
| --- | --- |
| Data safety section | [用户数据](../user-data/user-data.zh-CN.md)、[数据安全](../data-safety/data-safety.zh-CN.md) |
| Login credentials | [审核准备](../app-review-preparation/app-review-preparation.zh-CN.md)、[Play Console 要求](../play-console-requirements/play-console-requirements.zh-CN.md) |
| SMS and Call Log | [SMS 与通话记录](../sms-call-log/sms-call-log.zh-CN.md)、[敏感权限](../sensitive-permissions/sensitive-permissions.zh-CN.md) |
| Package visibility | [敏感权限](../sensitive-permissions/sensitive-permissions.zh-CN.md) |
| All files access | [敏感权限](../sensitive-permissions/sensitive-permissions.zh-CN.md)、[权限声明](../permissions-declaration/permissions-declaration.zh-CN.md) |
| Photo and video | [照片与视频权限](../photo-video-permissions/photo-video-permissions.zh-CN.md)、[敏感权限](../sensitive-permissions/sensitive-permissions.zh-CN.md) |
| Location | [联系人与前台位置](../contacts-location-permissions/contacts-location-permissions.zh-CN.md)、[后台位置](../background-location/background-location.zh-CN.md) |
| Contacts | [联系人与前台位置](../contacts-location-permissions/contacts-location-permissions.zh-CN.md) |
| Audio recording | [用户数据](../user-data/user-data.zh-CN.md)、[敏感权限](../sensitive-permissions/sensitive-permissions.zh-CN.md) |
| Files and docs | [敏感权限](../sensitive-permissions/sensitive-permissions.zh-CN.md)、[Android 隐私清单](../android-privacy-checklist/android-privacy-checklist.zh-CN.md) |
| Prominent disclosure | [用户数据](../user-data/user-data.zh-CN.md)、[Android 隐私清单](../android-privacy-checklist/android-privacy-checklist.zh-CN.md) |
| Account deletion | [账号与关联数据删除](../account-deletion/account-deletion.zh-CN.md) |
| Target API level | [目标 API 与兼容期限](../target-api/target-api-level.zh-CN.md) |
| Accessibility API | [敏感权限](../sensitive-permissions/sensitive-permissions.zh-CN.md)、[用户数据](../user-data/user-data.zh-CN.md) |
| Exact alarms | [敏感权限](../sensitive-permissions/sensitive-permissions.zh-CN.md)、[前台服务与地理围栏](../foreground-services-and-geofencing/foreground-services-and-geofencing.zh-CN.md) |
| Foreground services | [前台服务与地理围栏](../foreground-services-and-geofencing/foreground-services-and-geofencing.zh-CN.md)、[后台位置](../background-location/background-location.zh-CN.md) |

## 6. 边界与相关入口

本导航只帮助定位知识库已有的重点专题。政策中心和 Console 会更新，账号专属表单、地区法律、外部计划资格以及专题页中尚未展开的孙链接仍需在线逐项核实。该页的“说不清”不是违规结论，“未命中”也不是合规证明。

- [政策中心目录](../google-play-developer-policy-center/google-play-developer-policy-center.zh-CN.md) · 递归链接图（快照：`google-play-policy-link-graph.md`，未导入本仓库） · 逐 URL 来源台账（快照：`SOURCE_LEDGER.md`，未导入本仓库）
- [政策公告时间线](../google-play-policy-announcements/google-play-policy-announcements.zh-CN.md) · [公告子链接分析](../google-play-announcement-resources/google-play-announcement-resources.zh-CN.md)
- [英文版 / English version](../app-policy-scope-intake/app-policy-scope-intake.zh-CN.md)
