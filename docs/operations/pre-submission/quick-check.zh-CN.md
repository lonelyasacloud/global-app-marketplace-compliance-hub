---
id: operations.pre-submission.quick-check
platform: shared
language: zh-CN
authority: operational
status: current
kb_checked_at: 2026-11-26
review_due: 2027-02-26
regions: [global]
---

# 提交前快速检查 / Pre-submission Quick Check

这是一个快速门禁，不是完整审核保证。任何不适用项都要写明原因。

## P0：先检查

- [ ] App 在真实设备、最低支持系统和最新支持系统上可启动、可登录、可完成核心流程。
- [ ] 审核账号、演示账号、验证码/MFA、邀请流程和后端服务在审核期间可用。
- [ ] App 内隐私政策链接可访问，并且与实际数据流一致。
- [ ] Apple App Privacy Details 或 Google Play Data Safety 与 App、后端和全部第三方 SDK 一致。
- [ ] 付费功能、订阅、恢复购买、退款入口和地区价格可复现。
- [ ] 版本、商店元数据、截图、预览和实际发布体验一致。
- [ ] 没有隐藏、休眠、审核后才打开或未披露的功能。
- [ ] 所有敏感权限都有明确的核心功能、最小范围和必要证据。

## Apple 重点

- [ ] App Review Information 包含核心用途、测试账号、特殊硬件、地区和复现步骤。
- [ ] Privacy Manifest、Required Reason API、第三方 SDK 清单已检查。
- [ ] ATT、登录、账户删除、IAP、订阅和外部购买规则按适用店面核对。
- [ ] 年龄分级、儿童、UGC、健康、金融、VPN、赌博和其他受监管能力有证明材料。
- [ ] 截图、预览、素材、名称、描述和价格与当前版本一致。

## Google Play 重点

- [ ] Data Safety 表单与运行时收集、共享、删除和 SDK 行为一致。
- [ ] SMS、通话记录、联系人、位置、照片/视频、无障碍和其他敏感权限已完成资格与申报核对。
- [ ] Target API、Play Billing、内容分级、目标受众和 Families 要求已核对。
- [ ] 新个人开发者账号的测试轨道和持续时间要求已核验。
- [ ] Play Console 中的 App content、政策声明和发布轨道状态已记录。

## 证据记录

对每个勾选项记录：来源 URL、核查日期、负责人、测试环境、截图或日志位置，以及不适用时的理由。

## 官方来源

- [Apple App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/)
- [Apple App Store Connect Help](https://developer.apple.com/help/app-store-connect/)
- [Google Play Policy Center](https://play.google.com/about/developer-content-policy/)
- [Google Play Console Help](https://support.google.com/googleplay/android-developer/)

## 相关页面

本页仍是跨平台快速门禁。Apple 的详细清单另见[上架前检查清单](../../apple-app-store/pre-submission/submission-checklist.zh-CN.md)，审核准备短表见[审核准备](../../apple-app-store/app-review-guidelines/review-readiness.zh-CN.md)。两份清单一起使用。
