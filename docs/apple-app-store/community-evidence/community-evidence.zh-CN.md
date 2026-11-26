---
id: apple.community.evidence
platform: apple
language: zh-CN
authority: community
status: current
kb_checked_at: 2026-11-09
review_due: 2027-02-09
snapshot_package: 2026-11-10
regions: [global]
topics: [community, review, testing]
editorial_note: "Community-evidence layer from the snapshot checked 2026-11-09 (package 2026-11-10). Not an Apple official rule. Quora was blocked by robots.txt in that pass and is excluded. This import did not re-check forums or live official pages. English guidelines in the snapshot are dated 2026-10-16; the Simplified Chinese official guidelines page shows 2026-06-08."
---

# 社区经验与故障模式 / Community Evidence and Failure Patterns

## 证据等级

本页是**社区经验**。它不是 Apple 官方规则，不能单独支持合规结论，也不能覆盖[审核指南摘要](../app-review-guidelines/guidelines-summary.zh-CN.md)或实时官方页面。社区报告只用来发现测试场景和排错线索。先回到官方条款核验，再决定是否写成测试用例。

知识库核查日为 2026-11-09（包日期 2026-11-10）。本次导入没有重新打开论坛或实时官方页面。

| 等级 | 用法 |
| --- | --- |
| A | Apple Guidelines、App Store Connect Help、协议和 Apple 官方公告。可以进入规范层。这些材料不在本页展开，回到对应官方页面和已导入的主题。 |
| B | Apple Developer Forums 上的 Apple 员工提示或官方技术回复。可以进入操作建议层。仍然不是指南正文。 |
| C | Reddit、CSDN、开发者论坛中的重复经验。只能转成测试场景或排错线索。 |
| D | 绕过审核、隐藏功能、机审规避、套壳过审一类内容。禁止纳入执行方案。本知识库不记录做法。 |

## 可转成测试用例的经验

下面每条都是社区里反复出现的故障形态。它们是 C 级线索。测试通过不能代替官方规则。

### 1. 账号和审核可访问性

社区经常报告 Guideline 2.1 拒审并不是 App 崩溃，而是审核员无法走完流程。可用来设计测试，不能单独写成规则：

- 演示账号是否需要邮箱验证、邀请、MFA 或地区权限
- 是否已有足够样例数据
- 是否有多个账号角色
- 后端是否依赖 VPN、内网、IP 白名单或时间窗口
- 账号是否会过期、锁定或触发频率限制

这些线索要回指 Apple 的[完整审核材料要求](https://developer.apple.com/help/app-review/before-submitting-for-review/complete-review/)。官方操作摘要在[审核流程](../review-workflow/review-workflow.zh-CN.md)。

### 2. 元数据和素材

常见经验包括旧本地化截图、遗漏的设备尺寸资源、旧版 App Preview、IAP promotion image，以及截图和实际状态不一致。可测试：

- 所有本地化版本
- 所有设备尺寸和 View All Sizes
- 截图、预览、What’s New 与当前 binary
- IAP 的 Display Name、Description、Review Screenshot 和 Promotion image
- 是否包含价格、第三方平台、旧 UI 或无法验证的宣传语

素材是否符合现行规则，回到英文[App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/)。快照中的简体中文官方页仍显示 2026-06-08，不能用它覆盖更新的英文规则。

### 3. UGC 和 AI

社区常见的重复拒审点是没有举报、屏蔽、过滤、内容移除、未成年人限制或通知后整改流程。把它们回指指南 1.2、1.3、5.1 和年龄分级规则，见[审核指南摘要](../app-review-guidelines/guidelines-summary.zh-CN.md)和[年龄分级](../age-ratings/age-ratings.zh-CN.md)。不要把某一次拒审信写成普遍规则。

### 4. 隐私供应链

论坛中经常出现 ITMS-91061、缺少 privacy manifest、Required Reason API 未声明、第三方 SDK 触发权限字符串等问题。这是社区报告的排错线索，不是本快照里的 Privacy Manifest 或 Required Reason API 专题，也没有把这些代码或报错写成已复核的 Apple 规则。

线索应回指：

- [Privacy manifest](https://developer.apple.com/documentation/bundleresources/adding-a-privacy-manifest-to-your-app-or-third-party-sdk)
- [Required Reason API](https://developer.apple.com/documentation/bundleresources/describing-use-of-required-reason-api)
- [User Privacy and Data Use](https://developer.apple.com/app-store/user-privacy-and-data-use/)

Privacy Manifest 和 Required Reason API 的详细主题不在本次快照包中，仍未导入。

## Reddit 和 CSDN 的使用规则

- 只用来发现“可能会发生什么”
- 不把个案拒审原因扩大为 Apple 的普遍规则
- 先回到官方条款核验，再转成测试用例
- 保留来源、发布日期、App 类型和不确定性
- 含有“绕过审核”“隐藏功能”“机审规避”“套壳过审”的内容直接降级或排除，不写入执行方案

## Quora

本轮 Quora 页面受 robots.txt 限制，无法可靠读取和核验。当前不把 Quora 内容纳入知识库。如果以后提供具体链接，只作为待验证线索，在读到正文并回指官方来源之前不能使用。
