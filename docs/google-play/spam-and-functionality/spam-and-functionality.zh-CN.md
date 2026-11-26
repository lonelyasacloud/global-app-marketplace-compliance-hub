---
id: google-play.spam-and-functionality
platform: google-play
language: zh-CN
authority: normative
status: current
kb_checked_at: 2026-10-22
review_due: 2027-01-22
regions: [global]
topics: [spam, webview, repetitive-content, functionality, user-experience]
snapshot_id: play.spam-and-functionality
snapshot_package: "GooglePlay-KnowledgeBase-2026-10-24-review.zip"
coverage_status: "detailed-summary"
source_url: "https://support.google.com/googleplay/android-developer/answer/9899034?hl=en"
effective_date: "current-policy"
---

# Google Play 垃圾信息、功能性与用户体验政策

> **导入说明（Google batch 4）。** 本页正文取自 2026-10-24 Google Play 知识库快照里已经分开的中文改写（`play.spam-and-functionality`，核对日 2026-10-22）。它不是官方页面的逐字文本。英文官方来源是效力来源。`kb_checked_at` 使用快照源文件记录的核对日；本次导入没有重新打开线上官方页面。文中“本知识库”“本库”“本地专题”描述的是该快照知识库的覆盖范围，不是本仓库已经导入的页面清单。快照里指向尚未导入本仓库的专题、链接图、台账或 CSV 的相对链接，已改为文字提及；指向 Google batch 1–3 或本批十二个专题的相对链接已改到本仓库路径。快照记录的 Spam、Functionality 和帮助目录地址都是英文。快照没有记录已核对的中文官方 Spam 或 Functionality 页面。本中文页是快照的编辑改写，不是 Google 已发布中文页面的逐字文本。本政策没有记录未来生效日。正文里的“1 / 2”编号只用于定位当前帮助页，不表示其他政策采用同一套永久全局编号。发布前测试清单是落实稳定性要求的操作建议，不是政策页列出的穷尽测试清单。Play Academy 课程是培训，不替代政策条文。Spam 与 Functionality 是两项独立的 `normative` 帮助页，与 MUwS、恶意软件、欺骗性行为和广告欺诈分开核对。

**核对日期：2026-10-22。** Google Play 把 Spam 与 Functionality、Content and User Experience 放在同一政策目录组内，但它们是两个独立 Help 页面。本专题合并归纳其规则：应用不能以垃圾互动或重复低价值内容充斥 Play，也必须能稳定运行并给用户提供有意义的功能和内容。

## 垃圾信息（Spam）

| 风险类别 | 政策边界 | 上线前检查 |
| --- | --- | --- |
| 代用户发送消息 | 未先让用户确认消息内容和目标收件人，不得代用户发送 SMS、电子邮件或其他消息。仅有“分享”按钮不等于用户已确认具体内容和收件人。 | 在发出前展示完整内容和接收对象；明确的用户确认必须发生在实际发送之前。 |
| WebView 与联盟导流 | 主要目的若是把用户导向网站赚取注册/购买等联盟佣金，或未经网站所有者/管理员许可，仅把网站包成 WebView，属于常见违规类型。 | 确认应用有独立、实际的用户功能；对嵌入第三方网站取得并留存许可，不能只靠导流或网页外壳构成产品。 |
| 重复内容 | 不能只复制 Play 上现有应用的体验。应用应通过原创内容或服务给用户带来独特价值；复制内容而未增加价值，或用多款内容量很少、功能高度相似的应用填充目录，均是常见问题。 | 评估相似应用是否应合并为一个有足够内容的应用；证明内容、服务或体验有真实增量。 |

## 功能、内容与用户体验

应用应具备基本、稳定、响应良好的移动应用功能，并提供足够且有意义的内容。Google 的政策页列举的低功能示例包括：只有静态文字或 PDF 文件、内容很少且体验不完整的单一壁纸应用、没有实际功能的应用。崩溃、强制关闭、冻结、不安装、安装后无法载入或无法响应用户，也与可用体验要求冲突。

### 官方正文编号（2026-10-22 页面核对）

当前 Help 正文将条款分为 **1. Limited Functionality and Content**（有限功能与内容）和 **2. Broken Functionality**（功能损坏）。前者涵盖静态文字/PDF、内容过少和没有实际功能等例子；后者涵盖无法安装、启动后无法载入、无响应、崩溃、强制关闭或冻结。公告所说的标准化编号正逐步出现在部分政策页；本页的“1/2”用于定位当前正文，不据此推定其他政策也采用同一套全局编号或编号永久不变。

Help 页面还明确说明，Policy Summary 与 Key Considerations 只是概览；若概览与完整政策不一致，以完整政策为准。因此审核时应记录政策标题、来源 URL、核对日和正文标题，不只抄录摘要或编号。

**操作建议：** 发布前在目标设备、系统版本和主要用户路径上测试安装、首次启动、核心功能、网络错误与恢复；审核产品内容量、交互完成度和失败路径。此处测试项目是落实稳定性/功能要求的实践建议，不是政策页面列出的穷尽式测试清单。

## 与其他政策的关系

- 垃圾/低价值应用与[移动垃圾软件（MUwS）和欺骗性行为](../mobile-unwanted-software/mobile-unwanted-software.zh-CN.md)有关联，但垃圾、恶意软件、欺骗性行为和广告欺诈不是同一个政策类别；应按具体行为分别核对。
- 如果问题导致 Play 执法，先在[执行处置与申诉专题](../enforcement-and-appeals/enforcement-and-appeals.zh-CN.md)区分拒绝、下架、暂停和警告，并按通知修复。重复发布未经修复的版本可能让处置升级。
- Help 页面顶部声明：摘要和 Key Considerations 仅作概览，若其与完整政策冲突，以完整政策为准。Play Academy 课程用于培训，不取代政策条文。

## 页面与直接链接核验

Spam 和 Functionality 页面正文的主要政策条目已分别打开。两页的图像超链接是示例/政策插图，不是额外规则文本；以下逐条登记访问结果，图像页面内容无法通过文本提取稳定读取。

| 来源页 | 正文直链目标 | 与政策的关系和访问结果 |
| --- | --- | --- |
| [Spam](https://support.google.com/googleplay/android-developer/answer/9899034?hl=en) | [消息垃圾示例图](https://lh3.googleusercontent.com/ba4qjNQZ7-IgV4QhGps-OVgNA7cQpgWRb348SxYlgw05cv3tZqFvrNrNlYuzku88Z788%3Dh839)、[WebView/联盟示例图](https://lh3.googleusercontent.com/AZr3T8GiGN_g2AS76qWQ622zQNReHU4GKoKjbhrZGWNazx15FhZTOEomNI9z2o2pEps%3Dh1100)、[重复内容示例图](https://lh3.googleusercontent.com/6viGjA--lsmMb74UZL8pAO9YY34hHWCDtxkfQAHlK_pbBAmLd9kq8P39lckZh2ayv8LY%3Dw895) | 三个目标均已打开为图像地址；图像说明未能以文本可靠提取，因此摘要只依赖正文可读规则，不臆测图中细节。 |
| [Functionality, Content, and User Experience](https://support.google.com/googleplay/android-developer/answer/9898783?hl=en) | [政策摘要图](https://lh3.googleusercontent.com/BPsAL28eke0gFbFJduiZupJyY6uR5X7_JHR_3vev1cApatT5KLrReyskdlNZXRGFsg%3Dw60-h60)、[完整政策图](https://lh3.googleusercontent.com/hnJIMKQ0lyssVbehdx4OCpjLHPBYy94NeG4dD-xZ40osbCjM8Lt3zS4P5JvA5Xsqig%3Dw30-h34)、[有限功能示例图](https://play-kmt.teams.x20web.corp.google.com/no_crawl/arhc/images/minimum_funct1.png)、[无法载入示例图](https://lh3.googleusercontent.com/8Stc92Uebx_6XLNG0-cE6IlFertNFab0nNjhdKrihRS3teDiGk1ePWnAcC5w6W_qIg%3Dh839)、[无响应示例图](https://lh3.googleusercontent.com/VG3exQhozTq3qrIuen3HBMeLGDWBtedEkseSlyBMVtuYGJQ-OD3gruKvXogAozuDA%3Dh839)、[Key Considerations 图](https://lh3.googleusercontent.com/IfJhh8qlFSuw1U7A2DSeKi0B3jBYMC5fU0pGMUG40oyCU3urkOu4yGg0D24TkbUvwRk%3Dw40) | 六个目标均被尝试打开：四个公开图像地址返回目标、一个内部示例跳转至企业登录、一个图像缓存未命中。插图不增加独立政策义务。 |
| 两个 Help 页面 | 反馈/支持链接 | Qualtrics 调查和 Help Community 返回缓存未命中；Contact us 最终转到需登录的 Play Console 支持页。它们是反馈/支持入口，不是政策要求。 |
| [Spam, Functionality, and User Experience Help 目录](https://support.google.com/googleplay/android-developer/topic/9876964?hl=en) | [Spam](https://support.google.com/googleplay/android-developer/answer/9899034?hl=en)、[Functionality](https://support.google.com/googleplay/android-developer/answer/9898783?hl=en)、[Play Academy 课程](https://playacademy.exceedlms.com/student/path/65190-comply-with-google-play-s-spam-and-minimum-functionality-policies) | Help 目录正文称这组规则旨在防止垃圾目录并确保基本功能；两项政策已分别核验。目录链接的课程页可公开读取到章节名，但课程正文/互动需登录。 |
| Play Academy 课程 | [培训视频](https://www.youtube.com/watch?v=0PGBqQWgBEA) | 视频抓取失败。课程页面显示 Affiliate Spam、Made for Ads、Messaging Spam、Functionality、Repetitive Content、Webview Spam 等模块名；仅作培训目录，不把未访问课程正文写成已核验政策。 |

两篇 Help 页各有 Help Community、Contact us 等页面操作入口，已尝试访问并如上记录；其相关内容侧栏只用于政策导航，不等同于正文链接。Help 页面并未给出 Spam 的专用申诉方式；个案状态和执法结果以开发者账号通知与 Console 为准。

## 发布前核对

- [ ] 任何代发送消息的流程都让用户在发送前核对并确认内容及收件人。
- [ ] 应用没有以联盟导流或未经许可的第三方 WebView 作为主要产品功能。
- [ ] 多款同质应用有清楚的差异化用户价值；低内容量条目评估合并。
- [ ] 新用户可安装、启动、理解并完成应用宣传的核心功能；关键失败路径有可恢复体验。
- [ ] 商店描述、截图和实际功能一致，未用夸大或虚假互动制造应用价值。

## 来源

- [Spam](https://support.google.com/googleplay/android-developer/answer/9899034?hl=en)
- [Functionality, Content, and User Experience](https://support.google.com/googleplay/android-developer/answer/9898783?hl=en)
- [Spam, Functionality, and User Experience Help topic](https://support.google.com/googleplay/android-developer/topic/9876964?hl=en)
- [Play Academy course](https://playacademy.exceedlms.com/student/path/65190-comply-with-google-play-s-spam-and-minimum-functionality-policies)

本页是双语改写摘要，不是政策全文镜像。政策页的插图、交互式支持入口和课程可能需要联网或登录。
