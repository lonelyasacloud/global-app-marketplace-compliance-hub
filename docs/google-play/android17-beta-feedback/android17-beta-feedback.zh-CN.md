---
id: google-play.android17-beta-feedback
platform: google-play
language: zh-CN
authority: operational
status: current
kb_checked_at: 2026-10-23
review_due: 2027-01-23
regions: [global]
topics: [android-17, location, privacy, beta, issue-tracker, engineering-feedback]
snapshot_id: reference.android17-beta-feedback
snapshot_package: "GooglePlay-KnowledgeBase-2026-10-24-review.zip"
coverage_status: "detailed-reference-summary;direct-links-partially-reviewed;descendants-open"
source_url_location_blog: "https://android-developers.googleblog.com/2026/03/location-privacy.html"
source_url_android17_feedback: "https://developer.android.com/about/versions/17/feedback"
source_url_android17_release_notes: "https://developer.android.com/about/versions/17/release-notes"
source_url_issue_tracker: "https://developers.google.com/issue-tracker/"
source_url_issue_tracker_subscribe: "https://developers.google.com/issue-tracker/guides/subscribe"
source_url_issue_tracker_edit: "https://developers.google.com/issue-tracker/guides/edit-issue-ui"
source_url_android_security_updates: "https://source.android.com/docs/security/overview/updates-resources"
effective_date: "Android 17 platform preview and feedback path; not a Play permission rule; the 2027-01-27 contacts and location preview stays on the contacts topic"
---

# Android 17 位置隐私与测试反馈链

> **导入说明（Google batch 8）。** 正文来自已经分开的 2026-10-24 Google Play 知识库快照（`reference.android17-beta-feedback`，核对日 2026-10-23）的改写摘要，不是官方页面的逐字副本。英文官方页面是效力来源。`kb_checked_at` 是快照源文件记录的核对日；本次导入没有重新打开线上官方页面。文中“本知识库”“本库”“本地专题”等说法描述的是该快照库的覆盖范围，不是本仓库已经导入的页面。指向本仓库没有收录的专题、链接图、台账或 CSV 的相对链接改为文字提及。指向 Google batch 1–7 或本批十三个专题的相对链接改为本仓库文件。核对日 2026-10-23。两种语言文件使用不带语言参数的 Android 和博客地址。快照没有记录已核对的中文官方反馈页，也没有记录该主页面 `hl=zh-CN` 抓取失败。中文是编辑改写。2026-04-15 Play 公告和公告资源索引未导入本仓库。反馈页有 4 个链接返回 Internal Error 且没有暴露 URL，没有据此推断目标。本页是 Android 17 平台实现和 Beta 反馈路径，不新增 Play 权限资格、声明或申诉渠道。2027-01-27 的联系人与前台位置预告留在联系人专题。版本说明上的 Beta 日期是平台预览日期，不是该项 Play 预告。证据等级：位置变更为实现说明；反馈流程为 Operational。

**核对日期：2026-10-23。** 本页追踪 2026-04-15 Play 公告引用的 Android 17 位置隐私博客，再到博客正文中的官方反馈入口。这里记录的是 Android 平台实现和 Beta 测试流程；它不新增 Google Play 权限资格、声明或审核规则。Play 义务仍以[联系人与前台位置政策专题](../contacts-location-permissions/contacts-location-permissions.zh-CN.md)和当前 Play Console 为准。

## 来源链与 Android 实现要点

链路为：2026-04-15 Play 公告（[公告子链接目录](../google-play-announcement-resources/google-play-announcement-resources.zh-CN.md#announcement-2)） → [Android 17 位置隐私博客](https://android-developers.googleblog.com/2026/03/location-privacy.html) → 博客唯一实质正文链接 [Official Tracker](https://developer.android.com/about/versions/17/feedback) → Android 17 反馈与问题页。博客于 2026-03-26 发布，称 Location Button 可在 Android 17 Beta 3 测试。

博客概述了五项平台改进：一次用户操作触发的会话级精确位置按钮；Jetpack 在 Android 16 及以下回退到既有位置权限提示；持续的位置访问指示器和“Recent app use”管理入口；按人口密度调整的粗略位置范围；区分更清楚的“精确/大致”运行时对话框。按钮外观可有限定制，但位置图标不可移除，字体大小由系统控制。它们解释实现和用户体验方向，不代表 Play 对持续定位或广泛权限的豁免。

## Android 17 反馈页的正文直链

反馈页于 2026-10-23 打开，页脚标注最后更新 2026-10-16。排除同页锚点、图像、页眉和页脚后，正文有 **10 个外部目标**；其中 **6 个目标页面可读，4 个链接打开时报内部错误且浏览器未暴露目标 URL**。

| 正文链接 | 目标页内容与覆盖状态 |
| --- | --- |
| [Android 17 发行说明](https://developer.android.com/about/versions/17/release-notes) | 页面列出 Beta 4.1（2026-06-01）、Beta 4（2026-04-16）、Beta 3（2026-03-26）等版本和已修复问题；Beta 4 说明应做最终兼容性测试。发行说明含大量 issue/API 引用，本轮没有逐个打开所有编号链接，故目标页已读不等于该页孙链接已闭合。 |
| Top open issues | 目标尝试打开后返回 Internal Error；浏览器没有给出目标 URL。只记录链接标签和错误，不猜测地址或列表内容。 |
| Recently created issues | 目标尝试打开后返回 Internal Error；浏览器没有给出目标 URL。只记录链接标签和错误，不猜测地址或列表内容。 |
| [Subscribe to an Issue](https://developers.google.com/issue-tracker/guides/subscribe) | 指南说明可通过 CC、评论时勾选 CC Me 或 star 订阅；star 不向其他用户显示邮箱，同时也投票。向 CC 字段添加他人需对该组件有 Edit Issues 权限。该页的“What's next”链接继续指向下方的 View and Edit Issues 页面。 |
| [Google Issue Tracker 文档首页](https://developers.google.com/issue-tracker/) | 说明 Issue Tracker 是 Google 内部缺陷/功能请求工具，也向特定公开项目用户及合作方开放；按项目控制读写权限，不是通用缺陷平台或 Google 产品通用反馈入口。 |
| Platform 问题模板 | 目标尝试打开后返回 Internal Error，精确 URL 未暴露。父页只说明此模板用于 Android 系统/API、NDK、设备硬件或 ART 问题。 |
| App compatibility 问题模板 | 目标尝试打开后返回 Internal Error，精确 URL 未暴露。父页只说明此模板用于应用在最新 Beta 上的兼容性问题。 |
| [Security issue tracker：Security updates and resources](https://source.android.com/docs/security/overview/updates-resources) | Android 安全团队页面说明可通过漏洞表单报告潜在 Android 平台安全问题，报告可能在评估/修复前不公开。它是安全漏洞通道，不是 Play 政策申诉。漏洞表单点击跳到 Google Bug Hunters 安全奖励规则页，但该目标未返回可读正文。 |
| [Android Studio：Report a bug](https://developer.android.com/studio/report-bugs) | 建议用完整复现步骤、工具/系统版本和必要诊断信息报告 Android Studio、Gradle、模拟器问题；该页明确 Issue Tracker 不是使用帮助论坛。提交前应检查附件，避免夹带敏感数据。技术支持子链接未全部递归审阅。 |
| [Android Developers Content License](https://developer.android.com/license) | 已打开。知识库对官方内容采用摘要和链接，不以该许可为由逐字复制政策或帮助全文。 |

反馈页还指出：先查发行说明和问题列表，避免重复报告；按系统/平台问题与应用兼容性问题选择模板；报告可能没有回复，也可能在下一构建时关闭。若最新构建仍复现，应复查已知问题；尚无对应条目再重新提交。Pixel 预览版内的 Android Beta Feedback app 入口和正文的 Issue tracker 指向同页锚点；Beta app 新报告在核实前与 Issue Tracker 报告分开。这些是测试工作流说明，不是 Google Play 审核 SLA 或申诉流程。

## 已打开的孙链接及数据边界

- [Issue Tracker：View and Edit Issues](https://developers.google.com/issue-tracker/guides/edit-issue-ui) 已打开。查看/编辑需要登录；编辑字段需要该组件的 Edit Issues 或 Admin Issues 权限，只有 Comment on Issues 时可以查看和评论。其更多组件、搜索和通知指南仍未全部追踪。
- Issue Tracker 文档页的[服务专属条款](https://issuetracker.google.com/terms)已打开，页面标注 2016-11-08 更新。条款说明提交内容可能向获准访问该 issue 的用户显示，且授予 Google 为协作、处理提交、运营和改进服务等目的使用提交内容的许可；明确禁止提交高度敏感个人信息。通用 [Google Terms of Service](https://www.google.com/intl/en/policies/terms) 链接跳转到带尾斜杠的目标后未返回正文；[Google Privacy Policy](https://policies.google.com/privacy)已在另一分支读过，但它是 Google 服务隐私声明，不是 Play 开发者政策或应用隐私政策模板。
- Android 安全更新页的漏洞表单点击后重定向到 [Android and Google Devices Security Reward Program Rules](https://bughunters.google.com/about/rules/android-friends/android-and-google-devices-security-reward-program-rules)；浏览器未返回正文。未把奖励计划条款推断为漏洞提交的完整流程。
- Android Studio 报错页、Android 17 发行说明和安全资源页各自仍含大量技术、API、issue、站点导航链接；本轮只摘要与这条位置隐私测试路径直接相关的内容。问题模板和动态 issue 列表的目标 URL 仍待工具可读时补查。

## 应用团队的实际用法

1. 在 Android 17 Beta 上测试 Location Button、会话范围、拒绝/撤销路径与粗略位置行为；Play 权限声明仍单独按正式政策判断。
2. 报告前先看当前发行说明和可见问题列表；平台行为用 Platform 模板，应用兼容性问题用 App compatibility 模板。
3. 不要把 Play Console 的权限声明、政策警告或审核决定送到 Android 平台 Issue Tracker；它不是 Play 审核申诉入口。
4. Issue Tracker 条款禁止提交高度敏感个人资料。复现日志、截图、堆转储或测试账号中如包含用户数据、令牌、个人身份信息，应先脱敏或删去。

## 递归审计边界

本分支已读博客、反馈页及六个可读直链目标，并打开 Issue Tracker 的订阅、编辑指南和服务条款；四个反馈页直链仍因 Internal Error 未获得 URL。Android 17 发行说明中的 API/issue 目标、反馈页外的动态问题列表、安全奖励页正文、Android Studio 的全部技术后代尚未全量审核。逐 URL 状态见 source-page-audit.csv；本页不声称这棵技术文档树已经无限递归穷尽。
