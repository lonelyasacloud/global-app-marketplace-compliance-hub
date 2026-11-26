---
id: google-play.spyware-and-data-exfiltration
platform: google-play
language: zh-CN
authority: normative
status: current
kb_checked_at: 2026-10-22
review_due: 2027-01-22
regions: [global]
topics: [spyware, data-exfiltration, sdk, monitoring, privacy]
snapshot_id: play.spyware-and-data-exfiltration
snapshot_package: "GooglePlay-KnowledgeBase-2026-10-24-review.zip"
coverage_status: "detailed-summary"
source_url: "https://support.google.com/googleplay/android-developer/answer/14745000?hl=en"
effective_date: "current-policy"
---

# 间谍软件、数据外传与监控类应用

> **导入说明（Google batch 4）。** 本页正文取自 2026-10-24 Google Play 知识库快照里已经分开的中文改写（`play.spyware-and-data-exfiltration`，核对日 2026-10-22）。它不是官方页面的逐字文本。英文官方来源是效力来源。`kb_checked_at` 使用快照源文件记录的核对日；本次导入没有重新打开线上官方页面。文中“本知识库”“本库”“本地专题”描述的是该快照知识库的覆盖范围，不是本仓库已经导入的页面清单。快照里指向尚未导入本仓库的专题、链接图、台账或 CSV 的相对链接，已改为文字提及；指向 Google batch 1–3 或本批十二个专题的相对链接已改到本仓库路径。中文源文件的 Spyware 解释页地址是 `hl=zh-CN`。链接审计表记录已打开的是英文解释页全文。快照没有记录该主文的 `hl=zh-CN` 抓取失败，也没有记录已逐行核对的中文官方页面与英文页面的差异。本中文页是快照的编辑改写，不是 Google 已发布中文页面的逐字文本。本专题没有记录未来生效日。Play Academy MUwS 课程页显示 2020-07-08，且视频没有可读字幕；培训材料不替代现行政策。Spyware 解释页上的数据限制是 `normative`，但本页不是完整 Malware 分类。醒目披露文章是操作建议，不能只靠隐私政策代替应用内披露。监控类应用的窄范围例外不是对配偶或其他成年人跟踪的许可。

**核对日期：2026-10-22。** Google Play 的间谍软件解释页把风险核心表述为：应用、代码或行为收集、窃取、外传或分享与合规功能无关的用户/设备数据，或在用户没有充分通知与同意时监视用户。用户同意并不会把与合规功能无关或有害的数据处理自动变成允许行为。此专题总结的是 Spyware 分支，不等于完整 Malware 分类清单。

## 明确列出的高风险行为

- SDK 将与应用合规功能无关的录音或通话录音发送到设备外。
- 从其他应用通知中窃取信息。
- 在用户没有使用应用时，于后台意外传输联系人、非应用自有照片/SD 卡文件、邮件内容、通话记录、SMS 记录，或其他应用 `/data/` 目录的信息。
- 个人贷款或预算应用外传、分享非金融或个人短信历史。
- 第三方代码以用户未预期或未充分获知/同意的方式传输设备数据。

该列表是非穷尽示例。数据访问、收集、使用和分享都应限制在用户预期/同意、且符合政策的应用功能范围内。所有集成 SDK 与库均纳入审查；“行为来自 SDK”不免除开发者责任。应把权限声明、隐私政策、Data safety、应用内披露、服务端接收方和 SDK 实际网络行为互相核对。

## 监控类应用的窄范围

Play 的 Malware/Stalkerware 规则只允许专为家长监护孩子或企业管理监控员工而设计并营销的监控应用，并要求满足严格控制。不得把应用用于跟踪配偶或其他成年人，即使对方知情或同意也不行。此类应用须使用 Manifest `isMonitoringTool` 元数据、持续显示可识别通知和独特图标、在商店详情页披露监控功能、不得隐藏/伪装跟踪行为，也不得链接到 Play 外不合规 APK；开发者还须自行遵守当地法律。

`isMonitoringTool` 可用值包括 `child_monitoring`、`enterprise_management` 和 `other`；`other` 由 Google Play 审核是否属于有效例外。跨所有轨道的有效版本都应正确声明该标记。Play Protect 会向用户提示设备上存在监控应用。

## 落地核查

1. 从 Manifest、SDK/SBOM、初始化代码、后台任务、网络端点和服务端日志逐项追踪敏感字段流向。
2. 对每类数据写明对应功能、用户触发点、预期、披露位置、接收方、保留/删除规则及 Data safety 答案。
3. 检查 SDK 是否在应用未交互时传输信息；对于无法停用或修复的违规 SDK，移除或替换。
4. 特别复核短信/通话、联系人、麦克风、通知、应用清单、其他应用私有数据和贷款/预算类短信处理。
5. 若属于监控应用，核对唯一用途、目标人群、标记、持续通知、商店披露、所有发布轨道和 Play Protect 提示。

## 直接子链接与用途

| 目标页 | 本次核验与关联 |
| --- | --- |
| [Understanding Google Play's Spyware policy](https://support.google.com/googleplay/android-developer/answer/14745000?hl=en) | 全文已打开；列出数据限制、SDK 责任、录音/通知/后台数据/贷款短信等非穷尽例子及相关资源。 |
| [Malware policy](https://support.google.com/googleplay/android-developer/answer/9888380?hl=en) | 全文相关章节已打开。Spyware 是 Malware/潜在有害应用的一类；通用 Malware 还包括后门、计费欺诈、Stalkerware、DoS、恶意下载器、钓鱼、权限提升滥用、勒索软件、Rooting、垃圾信息、木马、风险软件等。代码即使不是故意恶意，只要在某些 Android 设备/版本上产生明显风险也可能被标记。 |
| [User Data policy](https://support.google.com/googleplay/android-developer/answer/10144311?hl=en) | 全文已打开。要求透明披露处理方式、数据用途符合披露、SDK 数据实践合规、安全处理并遵守当地隐私法；它为 Spyware 提供跨应用的数据处理底线。 |
| [Mobile Unwanted Software (MUwS)](https://developers.google.com/android/play-protect/mobile-unwanted-software) | 全文已打开。补充透明功能、明确系统变更、用户同意、加密传输、不诱使用户关闭 Play Protect，以及未经同意收集数据、社会工程、破坏体验广告、滥用系统功能和广告欺诈等分类。MUwS 与 Malware 分开维护，但可与 Spyware/权限滥用重叠。 |
| [Sensitive Permissions policy](https://support.google.com/googleplay/android-developer/answer/16558241?hl=en) | 正文已打开并在[敏感权限专题](../sensitive-permissions/sensitive-permissions.zh-CN.md)中摘要；用于核对权限/接口是否为核心功能所必需，以及最小范围、申报和披露同意。旧链接 `answer/9888170` 已重定向到当前政策页。 |
| [SDK Requirements](https://support.google.com/googleplay/android-developer/answer/13323374?hl=en) 与 [Using SDKs safely and securely](https://support.google.com/googleplay/android-developer/answer/13326895?hl=en) | 两个目标均已打开。前者是 SDK 要求页，后者为安全集成说明；两者都说明开发者须对集成代码和 SDK 数据处理承担责任，详见第三方 SDK 专题（快照：`sdk-requirements.md`，未导入本仓库）。 |
| [Prominent disclosure and consent best practices](https://support.google.com/googleplay/android-developer/answer/11150561?hl=en) | 全文已打开。补充披露应在应用内、清楚说明数据/用途/共享、展示在正常使用情境并取得明确肯定同意的界面实践；不能只放在隐私政策或条款。 |
| [Use of the isMonitoringTool Flag](https://support.google.com/googleplay/android-developer/answer/12955211?hl=en) | 全文已打开。三个标记值为 child_monitoring、enterprise_management、other；Google Play 根据类别与商店描述审核，并通过 Play Protect 提醒用户。 |
| [Google Play Protect Malware categories](https://developers.google.com/android/play-protect/phacategories) | 全文已打开，展示 Malware 分类与 Play Protect 说明；它解释检测分类，不另行建立开发者上传/申报流程。 |
| Google Play Academy [Malware](https://playacademy.exceedlms.com/student/path/261439/activity/345726) 与 [MUwS](https://playacademy.exceedlms.com/student/path/261439/activity/345727) 课程 | Malware 课程正文未能提取；MUwS 课程页显示 2020-07-08 发布但视频无可读字幕。培训页可作学习入口，不能替代现行政策。 |
| [Google Play Data safety 用户说明](https://support.google.com/googleplay/answer/11416267) | 页面已打开，解释消费者如何阅读开发者提交的数据安全信息；这是用户教育材料，不是开发者申报规则本身。开发者规则见 [Data safety 专题](../data-safety/data-safety.zh-CN.md)。 |

## 关联专题

- [敏感权限与 API](../sensitive-permissions/sensitive-permissions.zh-CN.md) · [用户数据](../user-data/user-data.zh-CN.md) · [Data safety](../data-safety/data-safety.zh-CN.md)
- [SMS 与通话记录](../sms-call-log/sms-call-log.zh-CN.md) · 第三方 SDK 要求（快照：`sdk-requirements.md`，未导入本仓库） · [广告与推广](../ads-and-advertising/ads-and-advertising.zh-CN.md)

已覆盖所选 Spyware 解释页的正文及直接政策/学习目标；帮助页侧栏推荐、SDK 的所有技术后代、不同地区监控法律、视频字幕与 Play Console 私有申报状态仍未全部读取。外链出现在目录中不代表所有后代都已审计。
