---
id: apple.pre-submission.checklist
platform: apple
language: zh-CN
authority: operational
status: current
kb_checked_at: 2026-11-09
review_due: 2027-02-09
snapshot_package: 2026-11-10
regions: [global]
topics: [review, metadata, privacy, payments, age-rating, submission]
editorial_note: "Imported from the snapshot checked 2026-11-09 (package 2026-11-10). No live re-check in this import. Checklist items are implementation notes derived from Apple guidelines and Help. Chinese wording for post-2026-06-08 English guideline changes is an editorial translation. The shorter cross-platform gate remains docs/operations/pre-submission/quick-check."
---

# 上架前检查清单 / Pre-submission Checklist

对每一项勾选，并把证据、负责人或审核备注记在团队流程里。本清单是**执行提示**，不是 Apple 的批准保证，也不是新增的 Apple 规则。

它比跨平台的[提交前快速检查](../../operations/pre-submission/quick-check.zh-CN.md)更细，两者都保留。规则摘要见[审核指南摘要](../app-review-guidelines/guidelines-summary.zh-CN.md)，简表见[审核准备](../app-review-guidelines/review-readiness.zh-CN.md)。英文《App 审核指南》在快照中的更新日期是 2026-10-16；简体中文官方页仍显示 2026-06-08。涉及此后英文变更的中文条目是编辑译文，不是 Apple 已发布的中文指南正文。本次导入未重新打开实时页面。知识库核查日为 2026-11-09（包日期 2026-11-10）。

## A. 包体与运行

- [ ] 当前构建在目标设备和系统版本上完成真实设备测试；无崩溃、阻塞缺陷、占位内容或空页面。
- [ ] 登录、核心流程、付费内容和必要后端服务在审核期间均可用。
- [ ] 提交的构建与元数据对应；新功能和重大变化已在审核备注中写明位置和步骤。
- [ ] 若需要特定硬件、区域、账号、二维码、网络或配置，提供可复现方式和必要证据。
- [ ] 无隐藏、休眠、未披露或仅在审核后启用的功能；审核版本与实际发布体验一致。关于隐藏功能的中文表述包含对英文 2.5.19 的编辑译文。

## B. App Store 元数据

- [ ] 名称、副标题、关键词、描述和开发者身份准确；没有关键词堆砌、冒充、未授权商标或不可验证承诺。
- [ ] 图标、截图、预览、创意素材和 App 内活动展示真实功能，适合所有受众，并已取得使用权。创意素材限制包含对英文 2.3.14 的编辑译文。
- [ ] 年龄分级问卷准确；儿童受众声明、Kids Category 与儿童隐私处理一致。见[年龄分级值与定义](../age-ratings/age-ratings.zh-CN.md)。
- [ ] **2026-11 新增，地区敏感：** 在 App Store Connect 填写“共享位置”和“约会与恋爱关系”声明；所有 App 在 2027-01-12 前完成。若选择约会与恋爱关系，确认最低 18+。若发行巴西，复核 A16/A18，并在需要时向 MJSP 申请官方评级。中文依据英文公告的编辑摘要，见[年龄分级主题](../age-ratings/age-ratings.zh-CN.md)与[公告](https://developer.apple.com/news/?id=yxkh08us)。
- [ ] Support URL、隐私政策 URL、营销 URL 及 App 内链接可用；联系信息是最新的。
- [ ] 付费功能、订阅、试用、虚拟物品以及可能的额外购买在产品页和 App 中清楚说明。

## C. 隐私与账户

- [ ] App 隐私标签与实际 App、后端、分析或广告 SDK、第三方服务的数据流一致。
- [ ] 隐私政策覆盖收集、用途、共享、保留、删除和撤回同意，并在 App 内易于访问。
- [ ] 权限提示和 purpose strings 具体说明数据用途；在合适时机请求权限，并提供拒绝或撤回后的合理体验。
- [ ] 跟踪仅在满足 ATT 同意要求后进行；第三方 AI 与 SDK 的数据共享已清楚披露并获得必要许可。
- [ ] **有条件：** 若接入 Siri AI Developer Preview，按 Beta 系统、支持地区与语言、13 岁以下限制、Apple Intelligence 条款和隐私披露做隔离测试。不要把预览能力写成稳定发布承诺。来源是 2026-11-03 公告，不是一条普遍适用的审核条款：[Siri AI Developer Preview](https://developer.apple.com/news/?id=gdk2umrf)。**地区敏感。**
- [ ] 若能创建账户，可在 App 内发起删除；删除流程覆盖相关数据，或说明合法保留部分。
- [ ] 儿童、健康、位置、通讯录与照片、通话与短信等敏感领域的限制已逐项核对。

## D. 付款与业务模式

- [ ] 每项交易已按数字内容、实体商品或服务、人与人实时服务、企业或阅读器等类别判定支付规则。
- [ ] App 内数字解锁、订阅、虚拟货币和随机虚拟物品遵循当前 IAP 规则；恢复和退款行为可用。
- [ ] **地区敏感：** 外部支付、外链和替代分发只在适用店面、平台和授权范围启用；对应协议已接受。
- [ ] 订阅页清楚列出价格、周期、试用、自动续订、权益和取消方式；获得已付费权益不需要额外无关任务。
- [ ] **地区敏感：** 若在台湾 iOS/iPadOS 店面销售标准 IAP 或付费 App，按 2026-10-31 起 26% 的费率复核收入、税务和结算记录。不要把该调整外推到其他店面。见[台湾店面公告](https://developer.apple.com/news/?id=w9mxlhek)和[许可协议摘要](../developer-program/license-agreement.zh-CN.md)。
- [ ] 若提供自动续期订阅，确认 App Store Connect 的多席位购买、Apple Business Manager 与 Apple School Manager 组织购买、群组席位分配和移除，以及沙盒测试。不提供时，核对是否应关闭对应渠道。见[企业与学校订阅公告](https://developer.apple.com/news/?id=yfo21au)。
- [ ] **仅在启用时：** 订阅挽留信息的文案准确、相关且适合所有受众；不得写具体价格或折扣、强迫性或无法验证的结果。图片和优惠与订阅资格、地区设置一致，并提交审核。见[挽留信息公告](https://developer.apple.com/news/?id=fk9ps3gv)。
- [ ] **地区敏感：** 金融、医疗、VPN、赌博、加密资产、募款等受监管业务具备相应主体资格、许可、地理限制和证明文件。

## E. UGC、儿童与安全

- [ ] UGC 具备内容过滤、举报、及时响应、屏蔽用户、有效联系方式和可执行的移除流程。
- [ ] UGC、AI 生成内容、创作者内容和 mini apps 的审核责任明确；高于年龄分级的内容有标注和年龄限制。AI 内容创作属于 UGC 风险范围的说法是对英文 1.2 澄清的编辑译文。
- [ ] 儿童类别的购买与外链位于家长监控之后；儿童数据不被不必要地传给第三方。
- [ ] 医疗与健康、安全、危险活动或现实伤害相关功能经过准确性和风险审查，并保留证据。

## F. 知识产权、设计与系统集成

- [ ] 素材、音乐、视频、商标、人物肖像、第三方服务和外部内容均有适当授权。
- [ ] App 不与竞品、Apple 产品、广告素材或热门 App 混淆；Bundle ID 结构不是重复上架。
- [ ] API、后台模式、扩展、小组件、通知、WebKit 或浏览器引擎，以及设备权限，均按预期用途使用。
- [ ] 若提供 mini apps、聊天机器人、插件或模拟器，已检查索引、通用链接、审核、权限隔离和付费规则。

## G. 协议、证书与地区附件

- [ ] 计划账户已接受最新协议；记录接受人、日期和版本。见[许可协议摘要](../developer-program/license-agreement.zh-CN.md)。
- [ ] 证书、私钥和 App Store Connect API 密钥受访问控制，并有轮换和泄露响应方案。
- [ ] 已按实际使用的 API、entitlement、Apple 服务和数据类型检查相应附件与限制。
- [ ] **地区敏感：** 已按发行地区核对附件和商业条款，特别是中国大陆、欧盟、日本和巴西的付款、分发、佣金与税务。

## H. 审核备注建议字段

这些字段是执行提示，帮助审核员复现，不是指南里的固定表单原文。

| 字段 | 写什么 |
| --- | --- |
| 用途与模式 | App 核心用途、目标用户、商业模式 |
| 新功能 | 入口与可复现步骤 |
| 账号 | 演示账户或演示模式，以及权限 |
| 环境 | 测试设备、系统版本和地区差异 |
| 第三方 | SDK、AI 服务、登录、支付和内容提供方 |
| 证明 | 许可证、监管批准、知识产权授权或安全文档 |
| IAP | 如何进入、测试和恢复 |

## I. 完整审核材料

- [ ] App 概念、商业模式、目标用户和受限地区已写入 App Review Information。
- [ ] 每种账号角色都有可用演示账号、样例数据和权限；验证码、MFA、邀请、地区限制和重置方式已说明。
- [ ] 后端、登录、支付、内容服务和第三方依赖在审核期间可访问，不依赖内部网络或临时配置。
- [ ] 需要硬件配对时已上传真机视频，并写明设备、系统、配对和复现步骤。
- [ ] 受监管功能已准备许可证、机构合作证明或其他 Apple 要求的支持文件。
- [ ] IAP 与订阅的商品 ID、进入路径、Sandbox 测试、恢复和地区差异可复现。

## J. 隐私供应链与元数据资产

- [ ] 已检查最终 App bundle 中的 `PrivacyInfo.xcprivacy`、Required Reason API、SDK 签名和第三方 SDK 清单。
- [ ] App Privacy Details 与 App、后端和全部 SDK 的数据流一致；数据实践变化时已同步更新。
- [ ] 所有本地化、设备尺寸和 Media Manager 中的截图与预览都是当前版本；没有遗留旧资源。
- [ ] 每种设备的多数截图展示 App 实际使用，不以登录页、启动页或纯营销图代替主功能。见[指南 2.3.3 截图说明](https://developer.apple.com/help/app-review/guideline-reference/2-3-3-screenshots/)。

## K. 提交对象、状态与时间

- [ ] 明确本次提交包含哪些对象：App version、IAP、订阅、In-App Event、Custom Product Page、产品页优化测试、asset pack 或 Game Center 项目。见[审核流程主题](../review-workflow/review-workflow.zh-CN.md)。
- [ ] 每个平台单独检查。不要把“App 已通过”当成附属项目也已通过。
- [ ] 记录当前状态、可修改字段、回复路径和下次提交方式。
- [ ] 把生效日、强制截止日、个案通知期限、内部完成日和下一次复查日分开记录。Apple 截止日期与本页 `review_due`（知识库复核日 2027-02-09）不是同一个日期。

## 官方操作说明

- [提交前准备完整审核信息](https://developer.apple.com/help/app-review/before-submitting-for-review/complete-review/)
- [在兼容设备上测试](https://developer.apple.com/help/app-review/before-submitting-for-review/test-compatible-devices)
- [为审核配置 App 内购买项目](https://developer.apple.com/help/app-review/before-submitting-for-review/configure-in-app-purchases)
- [跟踪提交的审核状态](https://developer.apple.com/help/app-review/after-submitting-for-review/review-status)
- [就提交联系 App Review](https://developer.apple.com/help/app-review/after-submitting-for-review/contact-app-review)
- [App Review Guidelines（英文基准）](https://developer.apple.com/app-store/review/guidelines/)
- [App 隐私详情](https://developer.apple.com/app-store/app-privacy-details/)、[Privacy Manifest](https://developer.apple.com/documentation/bundleresources/adding-a-privacy-manifest-to-your-app-or-third-party-sdk)、[Required Reason API](https://developer.apple.com/documentation/bundleresources/describing-use-of-required-reason-api)

本清单不替代上述官方页面，也不替代 App Store Connect 里的当前配置。
