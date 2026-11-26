---
id: apple.review.workflow
platform: apple
language: zh-CN
authority: operational
status: current
kb_checked_at: 2026-11-09
review_due: 2027-02-09
snapshot_package: 2026-11-10
regions: [global]
topics: [review, submission, status, deadlines]
editorial_note: "Imported from the snapshot checked 2026-11-09 (package 2026-11-10). No live re-check in this import. Dates below are the snapshot's recorded deadlines, not a new verification. review_due is the hub recheck date and is separate from Apple deadlines."
---

# 审核材料、提交对象与时间 / Review Materials, Submission Objects, and Timing

本页整理官方帮助文档中的提交对象、状态和时间类型，供发布执行使用。证据等级是**操作性说明**。它不代替 App Store Connect 的当前界面，也不保证审核时长。

知识库核查日为 2026-11-09（包日期 2026-11-10）。本次导入没有重新打开这些帮助页。英文《App 审核指南》在同一快照中更新于 2026-10-16，简体中文官方指南页仍显示 2026-06-08。本页的流程说明来自帮助文档；若与指南义务一起使用，指南仍以英文页为基准。中文指南滞后说明见[审核指南摘要](../app-review-guidelines/guidelines-summary.zh-CN.md)。

## 完整审核材料

提交前要让审核员能够完整、稳定、可复现地审查，而不是只填写账号和密码。

| 材料 | 需要准备 | 失败时的常见表现 |
| --- | --- | --- |
| App 概念 | 说明用途、商业模式、目标用户和受限地区 | 审核员无法判断真实用途或商业模式 |
| 账号 | 有效演示账号、每种角色的账号，以及验证码、MFA 或邀请说明 | 登录失败、账号过期、没有样例数据、权限不足 |
| 后端 | 审核期间保持生产或审核环境可访问，不依赖 VPN 或内部网络 | 空页面、请求失败、只在开发环境可用 |
| 硬件 | 需要配对硬件时提供真机视频和复现步骤 | 只有屏幕录制，无法验证设备互动 |
| 资质 | 金融、医疗、犯罪举报等场景提供许可证或合作证明。**地区敏感** | 审核要求补件，或无法验证主体资格 |
| 新功能 | 说明变化、入口、账号、测试设备和地区差异 | 2.1 需要补充信息，或功能无法定位 |
| IAP 与订阅 | 说明商品 ID、进入路径、Sandbox 测试、恢复和特殊配置 | 审核员找不到商品或无法完成购买 |

勾选清单见[上架前检查清单](../pre-submission/submission-checklist.zh-CN.md)。

## 提交对象

App Review 可能分别审查：

- App version
- In-App Purchase
- 自动续期订阅和订阅群组
- In-App Event
- Custom Product Page
- 产品页优化测试
- Apple 托管的 asset pack
- Game Center 排行榜、成就、挑战和活动

不同平台的 App version 要分别提交。一个平台通常最多同时存在一个包含 App version 的提交，以及一个只包含其他项目的提交。“App 已通过”不代表所有附属项目都已通过。

来源：[提交审核概述](https://developer.apple.com/help/app-store-connect/manage-submissions-to-app-review/overview-of-submitting-for-review)。

## 审核状态

```text
Ready for Review
  ↓
Waiting for Review
  ↓
In Review
  ├─ Accepted
  ├─ Rejected
  └─ Unresolved Issues
       ↓
    回复 / 修复 / 重新提交
```

状态会影响还能修改什么。进入 Waiting for Review 之后，部分截图、预览或 In-App Event 元数据可能不能再改。被拒绝的附属项目可以单独修复，或从提交中移除。

状态定义见[App 与提交状态](https://developer.apple.com/help/app-store-connect/reference/app-information/app-and-submission-statuses/)。拒审后的证据和申诉路径见[拒审与申诉](../../operations/rejection-and-appeals/README.md)。该页是仓库里的执行说明，不是 Apple 申诉规则原文。

## 时间类型

每条时间要求分开记录，不要合成一个日期：

- 公告日期
- 页面更新时间
- 开始适用日期
- App Store Connect 字段启用日期
- 强制完成截止日期
- 个案通知期限
- 内部完成日期
- 下一次知识库复核日期（本页为 2027-02-09）

快照已登记的时间要求：

| 项目 | 日期 | 状态 | 快照中的来源 |
| --- | --- | --- | --- |
| 年龄分级新字段可见 | 2026-11-16 起 | 即将适用 | [年龄分级描述符公告](https://developer.apple.com/news/?id=yxkh08us) |
| 所有 App 完成年龄分级新声明 | 2027-01-12 | 强制截止日期 | 同上 |
| 台湾 iOS/iPadOS 店面标准 IAP 与付费 App 交易费率改为 26% | 2026-10-31 起生效 | 已生效，**仅该店面** | [台湾店面公告](https://developer.apple.com/news/?id=w9mxlhek) |
| iOS 与 iPadOS SDK 27，以及 iOS 15 部署目标 | 2027 年 4 月起 | 即将适用的要求 | [提交 App 与游戏](https://developer.apple.com/app-store/submitting/) 与 [Upcoming Requirements](https://developer.apple.com/news/upcoming-requirements/) |
| 审核排队时间 | 快照未记录具体天数。Apple 只提供平均参考，不是保证 | 排期信号 | 快照未单列天数页面 |
| 14 天合规通知 | 只在具体 App 收到通知时适用 | 个案期限 | 快照未把某一公开页写成普遍的 14 天规则 |

发布前必须重新打开上表中的官方页面。快照日期不是当前账户里的接受状态或字段开关。

## 提交之后

可用路径包括：

- 在 App Review Resolution Center 回复
- 补充审核材料
- 在适用时只改元数据、不上传新的 binary
- Bug Fix Submission
- Expedited Review
- Appeal
- 一对一 App Review appointment

一对一沟通可以帮助解释问题，不能预先批准某个 App 或功能。每次提交仍按审核当时的指南评估。指南基准是[英文 App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/)。

## 官方来源

- [提交审核概述](https://developer.apple.com/help/app-store-connect/manage-submissions-to-app-review/overview-of-submitting-for-review)
- [提交前提供完整审核信息](https://developer.apple.com/help/app-review/before-submitting-for-review/complete-review/)
- [App 与提交状态](https://developer.apple.com/help/app-store-connect/reference/app-information/app-and-submission-statuses/)
- [提交 App 与游戏](https://developer.apple.com/app-store/submitting/)
- [Upcoming Requirements](https://developer.apple.com/news/upcoming-requirements/)

本页是这些帮助页的操作摘要。
