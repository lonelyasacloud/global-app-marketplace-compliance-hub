---
id: shared.privacy-data-protection.baseline
platform: shared
language: zh-CN
authority: normative
status: current
kb_checked_at: 2026-11-26
review_due: 2027-02-26
regions: [global]
topics: [privacy, sdk, consent, deletion]
---

# 隐私与数据保护基线 / Privacy and Data Protection Baseline

## 适用范围

这是一份跨平台控制基线。Apple App Store、Google Play 和当地法律的具体字段、申报方式、豁免和期限必须分别核对。

## 核心结论

应用的隐私声明必须能够解释真实运行时的数据收集、使用、共享、保留和删除行为，并覆盖后端、分析、广告、登录、支付和第三方 SDK。

## 必须做什么

- 建立数据流清单，覆盖 App、后端、SDK、第三方服务和跨境传输。
- 为每个数据类型记录目的、法律依据、收集时机、是否必需、共享对象、保留期限和删除方式。
- 让隐私政策在 App 内可访问，并与商店表单保持一致。
- 在需要时先取得有效同意，再进行跟踪、敏感数据处理或向第三方传输。
- 设计拒绝、撤回、账户删除和数据删除后的可用体验。
- 在发布前重新核对最终构建中实际包含的 SDK、权限、Privacy Manifest、Data Safety 和商店隐私字段。

## 平台差异

- Apple：重点核对 App Privacy Details、Privacy Manifest、Required Reason API、ATT、账户删除和 App Review Information。
- Google Play：重点核对 Data Safety、用户数据政策、敏感权限申报、显著披露与同意、账户删除和 SDK 行为。
- 地区法律：可能增加未成年人、健康、位置、跨境传输、自动决策、保留期限和数据主体请求要求。

## 证据与测试

至少保留数据流图、SDK 清单、权限矩阵、同意/撤回测试记录、删除测试记录、隐私政策版本、商店表单截图和最终构建核验记录。

## 来源

- [Apple App Privacy Details](https://developer.apple.com/app-store/app-privacy-details/)
- [Apple Privacy Manifest](https://developer.apple.com/documentation/bundleresources/adding-a-privacy-manifest-to-your-app-or-third-party-sdk)
- [Google Play User Data policy](https://support.google.com/googleplay/android-developer/answer/10144311)
- [Google Play Data safety](https://support.google.com/googleplay/android-developer/answer/10787469)

## 相关专题

- Google Play：[用户数据](../../google-play/user-data/user-data.zh-CN.md)、[Data safety 表单](../../google-play/data-safety/data-safety.zh-CN.md)、[Data Safety 基线](../../google-play/data-safety/data-safety-baseline.zh-CN.md)、[账号删除](../../google-play/account-deletion/account-deletion.zh-CN.md)。
- Apple：[审核指南摘要](../../apple-app-store/app-review-guidelines/guidelines-summary.zh-CN.md)。Privacy Manifest、Required Reason API、App Privacy Details 和 ATT 还没有专题页。2026-11-10 快照包没有这些全文。在成篇之前，以上官方链接是入口。

本页是执行摘要，不是隐私政策或法律意见。
