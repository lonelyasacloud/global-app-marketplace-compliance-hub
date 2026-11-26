---
id: google-play.account-deletion
platform: google-play
language: zh-CN
authority: normative
status: current
kb_checked_at: 2026-10-24
review_due: 2027-01-24
regions: [global]
topics: [account-deletion, data-deletion, data-safety, user-data, retention, privacy]
snapshot_id: play.account-deletion
snapshot_package: "GooglePlay-KnowledgeBase-2026-10-24-review.zip"
coverage_status: "detailed-summary"
source_url: "https://support.google.com/googleplay/android-developer/answer/13327111?hl=en"
source_url_zh: "https://support.google.com/googleplay/android-developer/answer/13327111?hl=zh-CN"
---

# 应用账号与关联数据删除

> **导入说明（Google batch 2）。** 本页正文取自 2026-10-24 Google Play 知识库快照里已经分开的中文改写（`play.account-deletion`，核对日 2026-10-24），不是 Google 已发布中文页面的逐字文本。英文官方页面是效力来源。`kb_checked_at` 使用快照源文件记录的核对日；本次导入没有重新打开线上官方页面。文中“本知识库”“本库”“本地专题”描述的是该快照知识库的覆盖范围，不是本仓库已经导入的页面清单。快照里指向尚未导入本仓库的专题、链接图、台账或 CSV 的相对链接，已改为文字提及；指向 Google batch 1 或本批七个专题的相对链接已改到本仓库路径。快照重开了英文帮助页和简体中文 `hl=zh-Hans` 正文，并记录两者在适用范围、应用内与站外路径、关联数据删除、第三方处理者、处理时间和例外上一致。精确 `hl=zh-CN` 路由该轮无法读取；中文内容核对使用已打开的 `zh-Hans` 页面，两种 locale 结果分开保留。抓取失败不表示正文已经变更。本中文页是快照改写，不是 Google 已发布的中文页面文本。2023-12-07 与 2024-05-31 仍是已过期的迁移日期。账号删除要求的证据等级是 `normative`。文中的 Data safety 表单答案和 Play Console 字段是 operational，不替代 User Data 中的删除要求。本专题与用户数据、Data safety 页面保持分开。

**核对日期：2026-10-24。** 只要应用体验的任何部分允许用户创建应用账号（包括跳转到应用外完成注册），Google Play《User Data》政策要求提供账号删除请求路径。移动应用必须在应用内和应用外均能发起删除；Play Console 的 Data safety 表单还需准确回答删除实践并填写外部网页链接。注销、停用或冻结账号本身不等于删除。

## 适用范围和例外

- “应用账号”是开发者提供给用户、可用于一个或多个应用/设备的身份和登录机制；账号创建可直接发生在应用里，也可由应用引导到站外流程完成。即使部分功能无需登录，只要应用任一部分允许创建账号，就须提供删除途径。
- 仅在离线创建和运行、没有在线应用账号的账户不属于该政策定义的 app account。永久私有应用和企业设备管理应用可适用政策例外；须按应用类别核验，不应泛化至普通企业工具或只有部分功能私有的应用。
- 非移动表面（例如 Web、Android TV、Wear OS）可不在设备端提供删除入口，但仍须提供易发现的站外发起方式，并在 Console 填入网址。移动应用可在应用内提供直达网页删除资源的链接；完整的原生删除流程不是唯一允许实现。

## 必须提供的删除路径

| 位置 | 要求 |
| --- | --- |
| 应用内（移动应用） | 在账号设置或相近位置放置直观、显著、容易找到的发起入口；可直接完成删除，也可链接到站外网页。 |
| 应用外 | 提供有效、易发现并能让用户真正发起请求的网页资源；用户卸载应用后无需重新安装也能使用。 |
| Play Console | 所有开发者都须回答 Data safety 删除问题；适用账号删除要求的应用须说明是否支持账号删除，并填入网页链接。部分答案会展示在商店详情页的数据安全/删除区域。 |
| 服务提供商 | 删除自有系统中的账号关联数据，并要求代表应用处理数据的服务提供商也删除其副本。 |

站外资源须可正常加载，页面应突出删除路径，并准确显示与 Play 商店详情页一致的应用或开发者名称。可采用专门删除页面、请求表单或客服邮箱等方式。若用户还须先取消订阅等步骤，需清楚说明前置条件，并提供可实际发起处理的客服流程；不能只给一段隐私政策文字却没有请求入口。

## 删除什么、何时删除与允许保留

用户请求删除应用账号时，也要删除与该账号关联的用户数据；包括已在 Data safety 中申报收集的数据。范围可能涵盖个人身份、支付/财务、认证信息、通讯录、位置、短信/通话记录、健康/Health Connect、麦克风/相机、已安装应用清单及其他敏感设备或使用数据。

- 完成请求应在合理较短时间内进行，并提前告诉用户预计流程/时长；各司法辖区的数据删除和保留时限可能不同，不能用统一估计替代当地法律审查。
- 安全、欺诈预防或监管合规确需保留的少量数据可按适用规则处理，但必须清楚披露保留内容、理由与保留实践（例如隐私政策中的 retention/deletion 说明）；高度监管行业可设置完成删除所需的额外流程。
- Data safety 删除请求机制问题与账号删除要求相关，但范围不同：Data safety 可将易发现的请求机制（如应用内入口、表单、专用邮箱）作为申报依据；若没有请求机制，官方 FAQ 允许在收集后 90 天内自动删除或匿名化时选择该机制标记。这个 90 天选项不等于创建账号的应用可以免除应用内/站外账号删除请求路径。

## Data safety 与用户可见信息

Data safety 表单必须真实反映当前在 Play 分发的所有版本、地区和年龄受众的数据实践。账号删除字段、外部链接和隐私政策应相互一致；表单审批或商店展示标记不能替代实际删除操作。Play 商店可据表单展示删除机制/数据删除区域，帮助用户查看和发起请求。

旧帮助页中的 **2023-12-07** 表单提交截止日和 **2024-05-31** 延期终点均已过期，是历史迁移时间线，不是未来截止日期。当前应保持表单和删除链接准确、有效。

## 官方最佳实践（建议，不是单独的准入条款）

Android Developers Blog 的五项建议与现行帮助页要求对照如下。此表刻意区分 UX 建议与强制控制，避免把“自动化”“账号恢复”或“问卷”误写成普遍准入条件：

| UX 建议 | 对应的现行 Play 控制 | 可验证证据 |
| --- | --- | --- |
| **入口顺手**：减少绕行，在账号设置或醒目位置直达删除流程。 | 移动应用内的入口须直观、醒目；可以链接到站外删除网页，不要求所有应用都在原生界面完成端到端删除。Play 没有规定统一的点击层数。 | 从常用账号入口实测路径；记录页面/步骤，并验证返回、拒绝或重新登录不会把删除入口隐藏。 |
| **优先自动处理**：若暂不能自动化，可用请求表单或专用客服入口。 | 强制要求是让用户真正能发起请求并在合理较短时间内完成处理；站外可用能启动删除的链接、客服邮箱或表单，不等于必须即时、全自动完成。 | 用真实的未登录/已登录状态提交请求，留存回执、处理负责人、服务时限和升级路径；确认“联系支持”不是无响应的死链。 |
| **提前说明影响**：解释订阅、资料导出等前置步骤，帮助中心可说明流程；博文还建议可考虑合理期限内恢复账号。 | 若删除前确需额外步骤（例如取消订阅），现行帮助页要求清楚说明并提供可发起处理的支持流程。账号恢复、导出提醒等是 UX 建议，不是所有应用的通用 Play 删除条件。 | 保存删除页文案、前置步骤及客服入口；按订阅、付费内容、资料导出等真实场景检查，避免无关步骤拖延删除。 |
| **确认进度与结果**：说清账号和云端数据何时处理，以及依法保留部分数据的原因。 | 用户请求删除账号时，须删除关联用户数据，并要求服务提供商处理其副本；应告知预期并在合理较短时间内完成。安全、反欺诈或监管留存须透明说明；各地法律可能另有时限，Play 帮助页没有给所有应用设一个统一天数。 | 保留请求状态/完成记录、服务商删除请求或确认、例外数据清单、依据与期限，以及给用户的完成/保留通知。 |
| **照顾已卸载用户**：让用户在网页上发起请求；可邀请反馈。 | 对允许创建账号的应用，站外网页资源是强制项，必须能在无需重新安装应用的情况下发起账号及关联数据删除；链接须可用、易发现、指明商店详情页所示应用/开发者，并填写到 Data safety。问卷或挽留反馈只能自愿，不能成为删除前置条件。 | 从未安装应用的浏览器打开商店详情页链接，核对应用名称、可发现性、请求提交成功和无强制重装；测试问卷可跳过。 |

这篇 2024 UX 博文正文中的 **“new account deletion policy”** 链接实际指向[2023 年政策发布公告](https://android-developers.googleblog.com/2023/04/giving-people-more-control-over-their-data.html)，不是当前 Help 条文。当前 [Account Deletion 帮助页](https://support.google.com/googleplay/android-developer/answer/13327111?hl=en)则反向把 2024 博文列作最佳实践。该发布公告说明账号删除同时要处理关联数据、可用时支持单独删除其他数据，并在 Data safety 中提供卸载后网页请求路径；公告中的 2023-12-07 和 2024-05-31 表单迁移日期均已过期，现行义务以当前 User Data 与 Account Deletion 帮助页为准。

### 2024 UX 博文正文直链与资产核查

| 正文目标 | 访问与关系 |
| --- | --- |
| [“new account deletion policy”](https://android-developers.googleblog.com/2023/04/giving-people-more-control-over-their-data.html) | 2026-10-24 再次确认该链接指向 2023 年政策发布公告；其 13 个正文目标此前均已尝试并在公告子链接审计（[公告子链接目录](../google-play-announcement-resources/google-play-announcement-resources.zh-CN.md)）记录。公告中的迁移日期仅属历史时间线。 |
| [页首案例图](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhljLTe4e3m2lCTVHZukvwtt3N5A34tfp3uQ9kITH8m5EM-9FI-7752LR4HofGCVBUzc9aaTXmUEC_xrKJnNW1R4pzx9YCZMFxWDxF64PWv8Zg6Yai3XKNlDvRv_PjR8QE8gikqfChslevvcNF8SzPET1WNH-_thMq-svIuGSTQ5t_KrFoE-SUWok28Xhc/s1600/social-Account-Deletion-Case-Study-Blog.png) | 图片目标返回 Cache miss；只记录为视觉示例，不从不可读图片推断要求。 |
| [Canva 流程示例图](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhSmgP5HlDbudibibZxpVwLrzDcBnt2rg_ITmTLc2t_OFMIDPyLBzQJxeBfmyyp_nk1OL0Yd-pkQKiPFUqH0WyUbcDloblVhUOv6HcW-I0iNeTOghSLQjcQnVyqEFBEpXjqT5zDcIJUFnrcAEyh_-8Y2HxwW3sRCsP4glQPy03pBG40xhwC6G9qOClzmugk/s1600/Account-Deletion-Google-Play-inline%20%281%29.png) | 图片目标已尝试，返回二进制资源而无可提取正文；父页 alt 文本将其标为 Canva 应用内删除流程示例，不是政策条款。 |
| [SYBO Games 网页流程示例图](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi59KSA_oGI24P30Um9abe7fLhiYoTWKn5q8oJ2lDsKScf30Jq6GyC_ZAWCfCAYfwiGRD4jdN4n5KCCXFH7L-zdCY7efdN96HhsuTmOFvQNUw5l75QoLBa43i_LPo5ph1-W64y3fTSKRXFMLIy8TeFWa-pY-qjpX-0j9Tg0mroJcxc56ZFAmRjH06kvKCE/s1600/Account-Deletion-Google-Play-inline-2.png) | 图片目标已尝试，返回二进制资源而无可提取正文；父页 alt 文本将其标为 SYBO Games 网页删除流程示例，不是政策条款。 |

页首/页尾 Android Developers 导航、博客分类、前后篇、隐私/许可/品牌链接属于网站外壳或通用法律/导航资源，不是这篇博文正文提出的 Play 删除义务；本次闭合的是正文政策链接及三项正文图片目标，不声称递归审查整站导航。

这篇 2023 发布博文的 13 个正文直链已逐项尝试打开：Data safety、账号删除帮助和 2023-04-05 Play 政策公告已分别并入双语专题/公告逐链接表；PolicyBytes 无可读完整字幕，全球 webinar 需登录，多个地区 webinar 短链无法读取，社区为动态互助内容。逐项访问状态及它们与政策的关系见公告子链接审计（[公告子链接目录](../google-play-announcement-resources/google-play-announcement-resources.zh-CN.md)）。这表示直接链接层有审计记录，不表示外部页面的无限后代全部闭合。

### 现行 Account Deletion Help 正文直链与共享侧栏（2026-10-24）

分别重开[英文账号删除帮助页](https://support.google.com/googleplay/android-developer/answer/13327111?hl=en)与简体中文 `zh-Hans` 正文；英文渲染 251 行，中文渲染 268 行。精确 `hl=zh-CN` 路由本轮无法读取，因此中文内容以成功打开的 `zh-Hans` 页面为核验对象，不把两种 locale 路由状态混为一谈。两种正文对适用范围、应用内/站外请求路径、关联数据删除、第三方服务商、合理处理时间和例外的核心要求一致；两页仍显示的 2023-12-07 与 2024-05-31 是已过期迁移日期，不是未来截止日。此前枚举的政策正文链接为 **7 个链接锚点/5 个规范目标**，页脚另有 2 个支持入口（合计 **9 个锚点/7 个规范目标**）；32 项共享“Policy education and app requirements”侧栏是导航，不是账号删除新增义务。

| 目标类别 | 本轮访问与政策关系 |
| --- | --- |
| [现行 User Data 政策](https://support.google.com/googleplay/android-developer/answer/10144311?hl=en) | Help 正文中的旧入口 `answer/13316080` 本轮再次点击超时；该别名此前已记录为跳转至现行 `answer/10144311`。今天直接打开规范目标的 329 行正文，确认其中仍有独立的 Account Deletion Requirement；详见[用户数据专题](../user-data/user-data.zh-CN.md)。不把本轮旧别名超时写成规范正文不可用。 |
| [2024 Android Developers UX 博文](https://android-developers.googleblog.com/2024/03/designing-your-account-deletion-experience-google-play.html) | 今天成功重开 82 行英文全文（发布日期 2024-03-06）；五项建议及与现行强制控制的逐项对照见上文。建议是 UX 实践，不是独立准入条款。 |
| Play Console App content | 页面链接指向开发者账号内的表单；本轮重试仍转到 Google 登录页，无法核对具体应用答案、状态或表单字段。账号特定内容不作推断。 |
| 商店展示示例图片 | 当前目标返回 GIF 图像类型，浏览工具不支持预览；它只是数据删除徽章/商店展示示例，不是政策正文。 |
| [Data safety 帮助页](https://support.google.com/googleplay/android-developer/answer/10787469?hl=en) | 今天从 FAQ 直链打开现行正文，并重核第 546–559 行：表单要求回答是否提供删除请求机制；机制类型不限，且在符合“收集后 90 天内自动启动删除或匿名化”条件时可选择该机制标记。FAQ 的“匿名化”示例又链接到 Google 的[匿名化方法说明](https://policies.google.com/technologies/anonymization?hl=zh-CN)，本轮双语全文重开，摘要 K 匿名、L 多样性、差分隐私及正文视频抓取失败状态见[Data safety 专题](../data-safety/data-safety.zh-CN.md)。该 Google 页面不是 Play 的算法/阈值标准；90 天填报条件不豁免账号创建应用的应用内/站外账号删除义务。 |
| Help Community 与 Contact us | 两个页脚链接本轮均未返回可读政策正文；社区内容是动态互助讨论，Contact us 属账号专属支持路径，另见逐 URL 台账。 |

本页还链接至共享的[Policy education and app requirements 索引](https://support.google.com/googleplay/android-developer/topic/12798386?hl=en)。2026-10-23 核对账号删除页显示的 32 项与共享侧栏逐项清单（快照：`age-restricted-child-safety.md`，未导入本仓库）相同，并从本页逐项尝试：31 个目标返回页面正文；Android Health Permissions FAQ 当时超时，保留此前的全文核验。最后一项前台服务预览已在前台服务专题（快照：`foreground-services-and-geofencing.md`，未导入本仓库）单独整理。32 项属于帮助导航/推荐，目标页自身的孙链接覆盖程度不一；此处关闭的是当前页面到这批直接目标的核验，不声称递归穷尽。

这些是设计建议；正式政策仍以可发现的请求路径、实际删除、合理处理、准确申报和透明保留为准。

## 发布前核对清单

1. 检查应用、站外跳转注册、账号体系和各客户端表面，确认是否任何路径能创建在线 app account。
2. 在移动端的账号设置等处验证删除入口；从已卸载应用的浏览器环境验证站外链接可用、无需重装且能提交删除请求。
3. 跟踪请求贯穿应用数据库、备份/删除队列、云服务商、客服工具、分析/广告 SDK 和其他处理者；记录合理完成时限。
4. 单独列出依法保留的数据、法律依据、保留期限和对用户的说明；确认客服流程确实能完成额外核验/取消订阅等步骤。
5. 更新 Play Console Data safety 删除问题和外部链接；与隐私政策、商店名称、应用内流程逐项对齐，并复测链接。
6. 对仅离线账号、永久私有/企业设备管理或非移动表面等例外保留适用依据，不把例外自动扩展到其他功能。

## 来源、子链接与关联

- [Understanding Google Play’s app account deletion requirements](https://support.google.com/googleplay/android-developer/answer/13327111?hl=en)
- [User Data policy — Account Deletion Requirement](https://support.google.com/googleplay/android-developer/answer/10144311?hl=en#account-deletion-requirement)
- [Provide information for Google Play’s Data safety section — deletion request mechanism FAQ](https://support.google.com/googleplay/android-developer/answer/10787469?hl=en)
- [Android Developers Blog: Designing your account deletion experience with users in mind](https://android-developers.googleblog.com/2024/03/designing-your-account-deletion-experience-google-play.html)
- [Android Developers Blog: Giving Users More Transparency and Control Over Account Data (2023 policy launch)](https://android-developers.googleblog.com/2023/04/giving-people-more-control-over-their-data.html)
- 关联专题：[用户数据](../user-data/user-data.zh-CN.md)、[Data safety](../data-safety/data-safety.zh-CN.md)、[权限声明与审核](../permissions-declaration/permissions-declaration.zh-CN.md)、年龄限制与儿童安全（快照：`age-restricted-child-safety.md`，未导入本仓库）。

本页是结构化改写摘要。真实删除请求还须满足适用隐私法、消费者保护/订阅规则和服务提供商合同；Console 当前表单及账号审核状态需在相应开发者账号中确认。
