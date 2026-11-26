---
id: google-play.user-data
platform: google-play
language: zh-CN
authority: normative
status: current
kb_checked_at: 2026-10-24
review_due: 2027-01-24
regions: [global]
topics: [user-data, privacy, sdk, consent, data-safety, account-deletion]
snapshot_id: play.user-data
snapshot_package: "GooglePlay-KnowledgeBase-2026-10-24-review.zip"
coverage_status: "detailed-summary"
source_url: "https://support.google.com/googleplay/android-developer/answer/10144311?hl=en"
source_url_zh: "https://support.google.com/googleplay/android-developer/answer/10144311?hl=zh-Hans"
effective_date: "current-policy"
---

# 用户数据（User Data）

> **导入说明（Google batch 1）。** 本页正文取自 2026-10-24 Google Play 知识库快照里已经分开的中文改写摘要，不是 Google 已发布中文页面的逐字文本。英文官方页面是效力来源。`kb_checked_at` 使用快照源文件记录的核对日；本次导入没有重新打开线上官方页面。文中“本知识库”“本库”“本地专题”描述的是该快照知识库的覆盖范围，不是本仓库已经导入的页面清单。快照里指向尚未导入本仓库的专题、链接图、台账或 CSV 的相对链接，已改为文字提及；指向本批六个专题的相对链接已改到本仓库路径。 快照记录可读的简体中文官方入口为 `hl=zh-Hans`。本页中文是编辑改写，不是该官方中文页的逐字文本。2026-10-24 再次请求时，英文返回 HTTP 429、中文路由返回 HTTP 500；快照没有把这次失败推断为正文变更，因为同日更早一次完整读取已经完成。醒目披露最佳实践子页在快照中被标为建议，强制要求仍以 User Data 政策为准。证据等级：`normative`；该最佳实践子页为 operational 建议。

**核对日期：2026-10-24。** 本页覆盖官方页面的主要政策章节，采用中文改写；不替代官方全文。页面中的技术实现链接和帮助页后代仍在递归清单中持续补录。

## 适用范围与责任

“用户数据”包含从用户取得或与用户有关的信息，也包括设备信息。开发者必须说明应用如何访问、收集、使用、处理和分享用户数据，并把数据用途限制在已经披露且符合政策的目的内。政策也要求持续遵守应用提供地区适用的隐私和数据保护法律。

责任覆盖应用内集成的第三方代码，包括 SDK、服务和 AI 集成。即使数据由第三方 SDK 直接采集或传输，应用开发者仍须核查其做法、确保披露与同意充分，并避免不合规的数据出售或扩展用途。若 Google Play 要求证明某个默认收集敏感数据的第三方代码符合醒目披露和同意要求，通常须在收到请求后两周内提供充分证据；请求若给出更长期限则按其期限办理。

## 永久性设备标识符

不得把 IMEI、IMSI、SIM 卡序列号等永久标识符与个人/敏感数据或可重置设备标识符关联。政策列出的有限例外包括与 SIM 身份相关的电话服务，以及以设备所有者模式运行的企业设备管理应用。适用例外时仍须醒目披露。不能调整到合规状态的 SDK 应移除。

## 个人数据和敏感用户数据

类别包括但不限于身份、财务和支付、认证、电话簿/联系人、位置、短信和通话、健康与 Health Connect、已安装应用清单、麦克风、摄像头，以及敏感设备或使用数据。

处理这些数据时，开发者须：

- 将访问、收集、使用和分享限制为应用/服务功能所需、用户合理预期且符合政策的目的；广告使用还须符合广告政策。
- 只在服务提供、法定义务、政府有效要求或有适当通知的并购等允许情形下传输数据。
- 采取安全措施，包括使用现代加密保护传输。
- 在适用时，先使用 Android 运行时权限，再访问受权限控制的数据。
- 不出售个人和敏感用户数据。现行 [User Data 正文](https://support.google.com/googleplay/android-developer/answer/10144311?hl=en)将“出售”定义为向第三方以货币对价交换或转让这类数据；用户主动发起的转移（例如使用应用功能向第三方传送文件）不按该政策定义视为出售。这个定义只回答“出售”分类，不替代对用途、披露、肯定同意、安全处理和 Data safety 申报的分别判断。

## 醒目披露与肯定同意

当访问、收集、使用或分享超出用户对相应功能的合理预期（例如应用未在前台使用时仍于后台收集）时，必须在应用内提供醒目披露。披露须在正常使用流程中可见，不应要求用户先进入菜单或设置；需说明数据类型以及用途/接收方，不能只放在隐私政策、网站或服务条款，也不能与无关披露混在一起。

披露之后、取得同意或请求运行时权限之前，必须紧接清楚的同意步骤。用户须主动确认；离开页面、点按其他区域、返回或回到主屏幕不构成同意。自动消失或限时消息不能代替同意。应用必须在用户授权之后才开始访问或收集相关数据。法律上的其他处理依据不会免除本政策要求的应用内披露。

建议把披露写成“应用在何种情境下收集/传输/同步/保存何种数据，以支持何种功能”，并准确说明后台处理、分享对象和次要用途。常见问题包括：先弹系统权限、后解释用途；把已安装应用、屏幕录制、联系人或电话数据当作非敏感信息；忽略 SDK 的采集。

如果 Google Play 要求证明默认收集敏感数据的 SDK 符合要求，须在两周内提供证据，除非请求明确给出更长期限。

### 最佳实践子页：把披露设计成用户可理解的选择

2026-10-24 重读官方[醒目披露与同意最佳实践](https://support.google.com/googleplay/android-developer/answer/11150561?hl=en)。该页明确把以下做法称为建议；真正的强制要求仍以本专题上方的 User Data 条文为准。

| 环节 | 官方建议及实施要点 |
| --- | --- |
| 时机和路径 | 在应用内、紧靠权限/能力请求之前展示；最好置于用户即将前往 Android 设置授予权限的流程中。应用说明或网站不能替代应用内披露。可用窗口提示，也可嵌入普通或对话式功能流程。 |
| 用户选择 | 给出清楚、友善的同意选项，同时允许拒绝或稍后再决定；保留取消路径。拒绝或撤回时让其余功能继续工作，并优雅关闭依赖该数据的功能。反复请求会造成疲劳；多次拒绝后应尊重选择。 |
| 视觉和措辞 | 不要仿造 Android 系统权限弹窗；可使用应用自己的视觉主题，让用户知道这是应用的说明。建议用清楚、易懂的语言，按约 13 岁读者可理解的水平解释；清晰度比简短更重要。 |
| Why / What / How | Why：说明核心功能为何需要该能力，应是披露的主要信息。What：列出涉及的数据类型。How：说明数据如何用于核心功能。若由 SDK 收集/传输，还要说明具体数据、必要性和第三方接收方，不能只写“由 SDK 处理”。 |
| 申报视频 | 填写权限声明时可附视频链接，YouTube 为首选，也支持指向常见格式文件的 Google Drive 链接。若提交，视频应展示应用打开、完整进入披露页（如需滚动，应慢速展示全部文字）、用户同意流程、拒绝并再次触发披露的流程，以及使用该能力的核心功能；若用途不直观，可加旁白或字幕。视频示例是审查辅助，不把“可提供”改写成所有应用必须提交。 |

该最佳实践页仍写有 Data safety 表单应在 2022-07-20 前完成；这是已过的历史上线日期。当前哪些应用须填表及例外条件，应以[现行 Data safety 帮助页](https://support.google.com/googleplay/android-developer/answer/10787469?hl=en)为准，不要把旧日期当作新申报期限。

## 专项数据限制

| 场景 | 要求 |
| --- | --- |
| 财务、支付、政府签发身份证号 | 不得公开披露相关个人或敏感数据。 |
| 非公开电话簿/联系人 | 未获授权不得发布或披露他人的非公开联系信息。 |
| 防病毒/安全类应用 | 隐私政策与应用内披露须说明收集/传输哪些数据、用途和分享对象类别。 |
| 面向儿童的应用 | 使用获准用于儿童场景的 SDK，并遵守 Families 政策。 |
| 永久设备标识符 | 仅适用规定的电话或企业设备管理例外，并醒目披露；不得任意关联。 |

## Data safety 部分

Play Console 中每个应用都须维护清晰、准确的 Data safety 申报，覆盖应用以及 SDK/第三方代码的数据收集、使用和分享。该申报显示在商品详情中，应与隐私政策中的数据披露一致，并随数据处理行为变化及时更新。具体数据分类和填表边界见[数据安全表单详解](../data-safety/data-safety.zh-CN.md)。

填表时须分别判断“收集”和“分享”。Data safety 将从设备向外传输的数据视为收集，包括应用内 SDK/库直接把数据送到第三方服务器的情形。服务提供方例外只适用于“分享”分类：接收方须代表开发者并按开发者指示处理数据；这不会把 SDK 传输变成“未收集”，也不会免除开发者的 User Data 披露、适用同意、安全处理和准确申报责任。若 SDK 跨多个客户建立广告画像，则不属于该服务提供方例外，须按分享申报。应依据实际数据流、处理目的、接收方和处理指示判断，不因“供应商”称呼或服务器归属直接套用例外。详见[Data safety 表单专题](../data-safety/data-safety.zh-CN.md)。

## 隐私政策

所有应用都须在 Play Console 指定字段填写隐私政策链接，并在应用内提供链接或文本；即使应用不访问个人或敏感数据也须提交。隐私政策及应用内披露应共同说明：

- 开发者身份和隐私联系渠道；
- 各类个人/敏感数据的访问、收集、使用、分享及相关接收方；
- 安全处理措施；
- 数据保存和删除做法；
- 清晰的隐私政策标题与对应应用/开发者身份。

链接必须有效、公开访问、没有地域限制，且不是 PDF；页面应不可随意编辑。应用商店资料上的公司/开发者实体或应用名称，应能在隐私政策中识别。

## 账号删除

只要应用允许用户创建账号，就必须提供易于发现的应用内删除入口和应用外删除网页资源；外部链接须填写在 Play Console 指定字段。收到请求后删除该账号相关用户数据。冻结、停用或临时禁用不等同于删除。若基于安全、欺诈防范或法规义务保留特定数据，应明确告知保留范围和依据。

## App Set ID

App Set ID 可用于分析或防欺诈等必要、非广告用途；不得用于广告个性化或广告衡量，也不得为了广告把它与 Android 标识符、身份信息或敏感数据关联。应在符合法律要求的隐私声明（包括隐私政策）中说明使用，并在法律要求时取得有效同意。

## EEA、英国和瑞士个人信息

若处理的是由 Google 提供、可直接或间接识别个人且来源于欧洲经济区、英国或瑞士的个人信息，开发者须遵守适用隐私/数据保护法律，只按相关个人同意的用途处理，部署适当组织和技术保护，并提供适用数据传输机制要求的保护水平。须定期监控合规；若无法或有重大风险无法满足要求，官方条文要求立即发邮件至 `data-protection-office@google.com` 通知 Google，并立即停止处理或采取合理、适当措施恢复充分保护。

## 执行核对清单

- 建立应用、服务端、SDK 和 AI 服务的数据流清单，并与商品详情、Data safety 和隐私政策逐项比对。
- 对非预期或后台数据处理，先展示独立、具体的应用内披露，再取得肯定同意，最后请求权限/开始处理。
- 检查用户拒绝、撤回和删除时的产品行为；避免把可选数据标为必需或将冻结账号当作删除。
- 审核永久标识符关联、儿童 SDK、敏感数据广告用途和地区法律要求。
- 每次功能、SDK、数据接收方或处理目的变化时，重新检查披露、Data safety 和隐私政策。

## 正文直链与后代核验

以下按当前 User Data 正文中的政策相关直链归类。重复锚点仍按来源边保留；通用 Help 侧栏和页脚控件不混入正文。访问状态、精确 URL 与受限原因以逐 URL 来源台账为准。

| 正文直链 / 目标页 | 与 User Data 的关系及后代状态 |
| --- | --- |
| [CNIL 移动应用建议（User Data 正文原始英文链接）](https://www.cnil.fr/en/mobile-applications-cnil-publishes-its-recommendations-better-privacy-protection) | 2026-10-24 逐项检查英文新闻页 13 个正文链接与 7 个“Read more”/标签/相关文章目标；目标页摘要、访问失败及父子关系见外部参考专题。英文页链接到 2025 年礼貌译本；[法文修订公告](https://www.cnil.fr/fr/recommandations-applications-mobiles-modifiee)列出现行法文 PDF 与标注版。英文页 French version 仍落到 2024 原始 PDF。外部专题补充开发者/SDK 权限和网络审计提示，并区分 CNIL 建议、Play 规则及相关文章。 |
| [Android location overview（正文旧链接）](https://developer.android.com/training/location) | 重定向至当前 location 文档；位置权限、后台位置和前台位置专题已互链。持续定位 API、生命周期、样例及存储后代的逐项摘要与审计范围见递归链接图 §4.107；大型 API 和更深后代仍部分覆盖。 |
| [Health data（正文旧帮助页）](https://support.google.com/googleplay/android-developer/answer/12261419) | 重定向至现行[Health Content and Services](https://support.google.com/googleplay/android-developer/answer/16679511)；当前健康政策和主要相关子页有独立双语摘要。 |
| [Health Connect / 敏感权限旧入口](https://support.google.com/googleplay/android-developer/answer/9888170) | 重定向至现行[敏感权限政策](https://support.google.com/googleplay/android-developer/answer/16558241)；Health Connect 数据仍同时受 User Data 与敏感权限/健康专题约束。 |
| [Ads policy](https://support.google.com/googleplay/android-developer/answer/9857753) 与 [Families policy](https://support.google.com/googleplay/android-developer/answer/9893335) | 分别规定敏感数据广告用途和儿童应用数据/SDK要求；本库已有双语专题，儿童 SDK 供应商、法律和课程等更深后代仍部分覆盖。 |
| [Service-provider / third-party 定义与 Data safety 表单说明](https://support.google.com/googleplay/android-developer/answer/10787469) | 同一目标承接服务提供方、第三方、数据收集/分享与表单定义；Data safety 正文、FAQ 和变更记录已独立摘要。跨设备 SDK 传输仍可能属于“收集”，服务提供方例外只影响“分享”分类；跨客户广告画像不属于仅代表开发者处理。短暂处理的一般规则与 FAQ 示例措辞差异仍原样标注，深层 API/课程/Console 页面部分不可读或需登录。 |
| [Android permissions overview](https://developer.android.com/guide/topics/permissions/overview) | 说明权限替代方案、声明、运行时请求和逐次核验；权限样例仓库 README、单项/多项/Compose 代码以及 Activity/Fragment/Accompanist 子页已逐项分析。样例仅供实现参考，不构成 Play 用途批准；其余动态文件树和大 API 成员仍部分覆盖。详见 Android 隐私清单与递归链接图 §4.101。 |
| [Prominent disclosure and consent best practices](https://support.google.com/googleplay/android-developer/answer/11150561?hl=en) | 于 2026-10-24 重开；正文 8 次锚点对应 6 个不同 URL。该页为披露时机、用户允许/拒绝选择、拒绝后的降级、Why/What/How 文案、SDK 第三方披露和申报视频提供推荐性实现示例，不另立强制政策。它仍保留 2022-07-20 的历史 Data safety 日期；现行表单范围见[Data safety 帮助页](https://support.google.com/googleplay/android-developer/answer/10787469?hl=en)。“Privacy policy”锚点实际跳转到 [Prepare your app for review](https://support.google.com/googleplay/android-developer/answer/9859455)，属于 App content 操作指南，不是隐私政策原文。旧敏感权限目标跳转到现行[敏感权限页](https://support.google.com/googleplay/android-developer/answer/16558241?hl=en)；App content Console 入口需登录。正文链接的 [Play Academy 课程](https://playacademy.exceedlms.com/student/activity/66910-declared-permissions-and-in-app-disclosures)公开简介已摘要，课件需登录。继续沿 Play Academy 课程追踪到 Policy Hub、课程目录及公开目标页，见 Play Academy 政策课程专题和递归链接图 §4.63。 |
| [Alternative unique identifiers guide（正文旧链接）](https://developer.android.com/training/articles/user-data-ids) → [现行唯一标识符最佳实践](https://developer.android.com/identity/user-data-ids) | Android 实现建议：按用途选最窄范围、可重置的 ID；将 AAID 用途、FID/GUID/App Set ID、运营商/SIM、登录、崩溃/性能、反滥用和 DRM 区分。中英AAID 专题现含完整用途矩阵及 31 个正文直链的目标分析；Play Integrity API 专题补充其不得用于用户/设备指纹识别或跟踪、API 数据处理说明和服务端验证最佳实践。2026-10-16 更新的 Android 指南不是额外的 Play 强制条款。通用 API 与更深技术后代仍部分覆盖。 |
| [App account deletion requirements](https://support.google.com/googleplay/android-developer/answer/13327111) | 解释应用内和网页删除入口、关联数据及保留例外；主要 FAQ 和 Android UX 最佳实践博客已核对，旧 rollout 日期按历史信息处理，侧栏后代仍部分覆盖。 |
| [Data Privacy Framework Principles](https://www.dataprivacyframework.gov/program-articles/Participation-Requirements-Data-Privacy-Framework-%28DPF%29-Principles) 与 [Google Controller-Controller Terms](https://business.safety.google/controllerterms/) | DPF 正文直接读取仍受 JavaScript 限制，但官方索引显示七项原则、16 项补充原则和仲裁附件；它只为参与组织提供特定传输机制，不是 GDPR 整体合规机制。Google Controller Terms 当前为 Version 11（2026-05-07），只适用于协议纳入/实际接受的 Controller Services；Google Play 与 Managed Google Play 的服务角色不同。详细适用边界、地区附录、历史版本和访问状态见双语外部参考专题。 |
| [User Data 正文反馈问卷](https://google.qualtrics.com/jfe/form/SV_9YPSYrwjw03d7cG?Source=10144311) | 需要 JavaScript，未显示问卷问题；这是页面反馈，不是政策义务或申报步骤。 |

### 政策侧栏与父级分类目录

User Data 帮助页还有 7 项政策导航。父级[Privacy, Deception and Device Abuse 分类目录](https://support.google.com/googleplay/android-developer/topic/9877467?hl=en)列出同一组目标；这些导航不计入上表的正文直链，但每个目标页都单独打开并与本地专题互链。

| 导航目标 | 与 User Data 的关系和本地入口 | 目标页/后代核验 |
| --- | --- | --- |
| [User Data（当前页）](https://support.google.com/googleplay/android-developer/answer/10144311?hl=en) | 本专题；父目录中的当前政策入口。 | 正文已完整核对并有双语摘要；正文链接另见上表。 |
| [Permissions and APIs that Access Sensitive Information](https://support.google.com/googleplay/android-developer/answer/16558241?hl=en) | 规定受限权限如何访问用户数据；见敏感权限专题。 | 英文正文已完整打开；联系人/位置预览及重点后代已互链，其他直接链接和 Android 技术后代仍部分覆盖。 |
| [Device and Network Abuse](https://support.google.com/googleplay/android-developer/answer/16559646?hl=en) | 补充设备、网络与数据滥用边界；见设备与网络滥用专题。 | 正文已完整核对，17 个直接政策/技术目标已登记；更深 Android 实现后代仍部分覆盖。 |
| [Deceptive Behavior](https://support.google.com/googleplay/android-developer/answer/17006354?hl=en) | 覆盖误导性界面、功能和数据处理表述；见欺骗性行为专题。 | 正文已完整打开，11 次锚点/10 个不同目标已登记；目标页后代仍部分覆盖。 |
| [Misrepresentation](https://support.google.com/googleplay/android-developer/answer/9888689?hl=en) | 涉及身份、功能、来源和关系的虚假陈述；见虚假陈述专题。 | 正文已完整打开；未发现独立政策正文外链，侧栏另行记录。 |
| [Google Play's Target API Level Policy](https://support.google.com/googleplay/android-developer/answer/16561298?hl=en) | 版本门槛影响敏感权限政策/实现所依赖的平台 API；见目标 API 专题。 | 英文正文及侧栏已核对；简体中文官方入口不可读，API/设备形态后代仍部分覆盖。 |
| [Preview: Permissions and APIs that Access Sensitive Information](https://support.google.com/googleplay/android-developer/answer/16909972?hl=en) | 2026 年 4 月政策预览；将联系人和位置变化标为 2027-01-27 生效，不能与当前条文混为一谈；见联系人与位置专题。 | 预览正文已完整打开并摘要；联系人选择器、Location Button 和申报/审核关系已核对，Android API/样例后代仍部分覆盖。 |

父级目录的其他直接链接也逐项核对：它的 [Google Play Policy 视频](https://www.youtube.com/watch?v=zMHv1yH7C4E)抓取失败，未取得可用字幕；[Help Community](https://support.google.com/googleplay/android-developer/community?hl=en)已打开为动态社区首页，帖子会变化且不是权威政策文本；[Contact us](https://support.google.com/googleplay/android-developer/gethelp)会跳转到 Play Console 账号内支持页，需登录，未提交请求。上述导航和支持入口与政策正文分开标注。直接目标页中的技术、课程、动态法律目录和账号专属 Console 后代仍按可访问范围递进核验，不声称无限递归闭合。

## 与合并版开发者计划政策交叉核对

2026-10-24 对照了现行[开发者计划政策合并版](../developer-program-policy/developer-program-policy.zh-CN.md)的“用户数据”和“SDK 要求”部分。合并版标注自 2026-09-30 生效；英文正文和简体中文 `hl=zh-Hans` 正文均已打开。`hl=zh-CN` 入口本轮未能读取，中文核对使用可读的 `zh-Hans` 版本。

两份官方页面的核心义务一致：说明应用如何访问、收集、使用、处理和分享数据并限制在已披露的合规目的；开发者要对集成的 SDK/第三方代码及其数据做法负责；敏感数据须满足合理预期、用途限制、安全、权限、适用时披露与肯定同意、Data safety 和隐私政策要求；不得出售个人/敏感数据，而用户主动发起的传输不属于该政策对“出售”的定义。合并版的“用户数据”段还明确覆盖第三方 AI 集成。

合并版另有独立的“SDK 要求”段，补充了 SDK 违规示例：SDK 声称只用于反欺诈，却把数据用于广告/分析分享；或在没有醒目披露的情况下传输已安装软件包清单。若 SDK 默认收集个人数据和敏感用户数据，Google Play 要求提供证据时，通常须在两周内提交充分证明，除非请求另给更长期限。这些例子帮助检查集成风险，不改变 User Data 正文中的其他义务。

单独的 [User Data 帮助页](https://support.google.com/googleplay/android-developer/answer/10144311?hl=en)仍有自己的完整解释、专项章节和正文链接；合并版则集中呈现整套政策，并在 SDK 部分交叉引用 User Data、显著披露最佳实践等条目。两页应分别保留来源和后代审计，不因内容重合而视为同一页面或推定某一页替代另一页。本轮只对照合并版中这两个相关部分，**不表示合并版全部正文链接和后代已穷尽**。

访问记录：User Data 英文及简体中文正文在 2026-10-24 的先前核对中已完整读取；本轮再次请求时英文返回 HTTP 429，中文路由返回 HTTP 500，因此没有把重试失败当作正文变更。逐 URL 台账保留先前完整读取状态并记录本次失败。

## 关联页面

- [Data safety 表单](../data-safety/data-safety.zh-CN.md)
- 第三方 SDK 要求与安全集成
- 敏感权限与 API
- 健康应用、健康数据与 Health Connect
- [账号删除要求](https://support.google.com/googleplay/android-developer/answer/13327111?hl=zh-CN)
- 用户数据政策的外部法律与参考资源：醒目披露最佳实践、CNIL 移动应用建议、DPF 和 Google Controller Terms 的关系与访问边界
- [开发者计划合并政策](../developer-program-policy/developer-program-policy.zh-CN.md)
- 官方：[用户数据（简体中文）](https://support.google.com/googleplay/android-developer/answer/10144311?hl=zh-Hans) · [User Data (English)](https://support.google.com/googleplay/android-developer/answer/10144311?hl=en)

## 覆盖说明

主要政策章节和高相关直接参考页已整理；参见用户数据外部参考专题。Android 通用 API、CNIL 98 页指南的全部非政策细节、DPF 动态页面及参与者核验、Controller Terms 历史 PDF 中的失败目标、法律后代和更深层站点链接仍部分未覆盖，按逐 URL 台账标注；不据未读页面标题推断内容。
