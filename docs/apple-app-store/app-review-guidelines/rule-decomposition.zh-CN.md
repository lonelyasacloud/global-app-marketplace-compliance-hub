---
id: apple.app-review.rule-decomposition
platform: apple
language: zh-CN
authority: implementation-note
status: current
kb_checked_at: 2026-11-09
review_due: 2027-02-09
snapshot_package: 2026-11-10
regions: [global]
topics: [review, evidence, safety, performance, business, design, legal]
editorial_note: "Editorial and analytical model from the snapshot checked 2026-11-09 (package 2026-11-10). It is not Apple source text and does not add Apple policy. This import did not re-check live pages. English App Review Guidelines in the snapshot are dated 2026-10-16; the Simplified Chinese official page shows 2026-06-08. Chinese titles that are not Apple's published translation must be marked editorial translation."
---

# 审核规则拆解模型 / App Review Rule Decomposition Model

## 这页是什么

本页定义知识库的规则单元模型。证据等级是**执行说明 / implementation note**。它不是新的 Apple 规则，也不代替[审核指南摘要](guidelines-summary.zh-CN.md)或实时官方页面。它把 Apple 规则、App Store Connect 操作要求、时间要求、审核证据和内部动作拆成可以执行的字段。

知识库核查日为 2026-11-09（包日期 2026-11-10）。本次导入没有重新打开实时官方页面。

## 规则单元

每一条规则至少保留以下字段：

| 字段 | 说明 |
| --- | --- |
| `rule_id` | Apple 条款号、App Store Connect 页面标识或内部稳定编号。 |
| `domain` | Safety、Performance、Business、Design、Legal，或协议、年龄分级、平台专项。 |
| `title_zh` / `title_en` | 双语标题。中文不是 Apple 官方译文时，标为 editorial translation。 |
| `authority` | Apple rule、Apple operational guidance、community experience、internal recommendation。社区经验和内部建议不能写成 Apple 规则。 |
| `source_url` | 当前来源原文。旧页面不能覆盖当前页面。 |
| `source_updated_at` | 来源页面更新时间或公告日期。 |
| `effective_at` | 规则、功能或费率开始适用的时间。 |
| `deadline_at` | 必须完成的截止日期。没有统一截止日时留空。 |
| `scope` | 受影响的平台、店面、地区、App 类型、用户类型或商业模式。 |
| `triggers` | 何种 App 功能、数据、配置或提交行为会触发此规则。 |
| `must` | 必须做什么。 |
| `must_not` | 禁止做什么。 |
| `exceptions` | 资格、地区、平台或业务模式的例外。 |
| `review_evidence` | 审核员需要看到的账号、文档、视频、资质、路径或截图。 |
| `test_cases` | 产品、研发、测试和发布应执行的验证。 |
| `failure_signals` | 可能触发拒审、下架、协议风险或延迟的表现。 |
| `remediation` | 发现问题后的暂停、修复、披露、重新提交或申诉动作。 |
| `owner` | 产品、研发、测试、发布、法务、财务或 App Owner。 |
| `status` | Current、Upcoming、Effective、Conditional、Historical、Background。 |

## 五大审核域

下列清单是模型里的条款地图，用来给规则单元选择 `domain` 和 `rule_id`。它不是指南正文。现行措辞以英文指南为准。简体中文官方页在快照中仍显示 2026-06-08，见[审核指南摘要](guidelines-summary.zh-CN.md)。

### 1. 安全 / Safety

- 1.1 有害、令人反感、色情、暴力、误导内容
- 1.2 UGC、AI 生成内容、创作者内容、过滤、举报、屏蔽和通知后整改
- 1.3 Kids Category、儿童隐私、家长控制
- 1.4 医疗、健康、危险活动和人身伤害
- 1.5–1.7 开发者信息、安全和犯罪举报

### 2. 性能 / Performance

- 2.1 App 完整性、崩溃、URL、登录、后端、IAP 可审查性
- 2.2 Beta、试用和演示版本使用 TestFlight
- 2.3 元数据、截图、预览、创意素材、年龄分级和 What’s New
- 2.4 硬件兼容、功耗和设备影响
- 2.5 公共 API、后台服务、权限、WebKit、扩展、广告和 2.5.19 隐藏功能

### 3. 业务 / Business

- 3.1 IAP、订阅、退款、随机虚拟物品、外部购买链接和地区授权
- 3.2 其他商业模式、金融、医疗、VPN、赌博、募款、加密资产和企业服务

付款、订阅、外部购买和地区条款还没有单独成篇。相关义务先回指南摘要和[许可协议摘要](../developer-program/license-agreement.zh-CN.md)。

### 4. 设计 / Design

- 4.1–4.3 抄袭、冒充、重复 App、模板化和垃圾提交
- 4.4–4.6 扩展、Apple 服务、通知、营销和用户体验
- 4.7 Mini Apps、小游戏、聊天机器人、插件和模拟器
- 4.8 登录、Apple Pay、系统能力和 Apple 服务的商业化限制

### 5. 法律 / Legal

- 5.1 隐私、权限、账户删除、ATT、第三方 SDK 和数据生命周期
- 5.2 知识产权和内容授权
- 5.3 游戏、赌博、彩票和抽奖
- 5.4 VPN、MDM、受监管业务和许可
- 5.5 其他法律义务
- 5.6 Developer Code of Conduct 和开发者行为

## 示例：2.5.19 隐藏、休眠或未披露功能

这个例子拆的是快照所记录的英文指南 2.5.19 方向：禁止隐藏、休眠或未文档化功能。下面的触发条件、必须项、禁止项和关闭条件是**编辑模型中的执行拆解**，不是 Apple 条款原文，也不能代替审核备注里对当前英文指南的核对。

### 触发条件

- 远程配置、Feature Flag、A/B 测试或服务端动态下发
- 不同地区、语言、用户身份、广告入口或账号权限返回不同功能
- WebView、第三方域名、动态网页或远程资源改变用户体验
- 审核期间与上线后使用不同配置

### 必须满足

- 提交版本和实际发布体验保持一致
- 在 App Review Information 中说明重要差异和复现路径
- 提供可用审核账号、测试数据、配置快照和回滚方式
- 审核期间冻结关键远程配置

### 禁止

- 审核时隐藏、审核后打开
- 把审核账号放到看不到问题的分组
- 用代码混淆、入口差异或动态网页隐藏功能
- 用“以前审核通过过”替代当前版本的披露和验证

### 证据与关闭条件

- Feature Flag 和后台配置清单
- 账号、地区、语言、设备、用户状态测试矩阵
- 审核备注、演示账号和复现视频
- 配置冻结与回滚记录
- 法务和 App Owner 的放行结论

提交材料的官方操作说明见[审核流程](../review-workflow/review-workflow.zh-CN.md)。

## 来源层与经验层

使用规则单元时按这个顺序取证。低层不能覆盖高层。

1. **规范层 / Normative。** 当前英文指南、当前 App Store Connect Help、当前协议及适用附件。英文指南：[App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/)（快照中的页面日期 2026-10-16）。简体中文官方页：[App 审核指南](https://developer.apple.com/cn/app-store/review/guidelines/)（快照中仍显示 2026-06-08，只作历史译文）。协议入口以许可协议主题记录的页面为准；快照中提供的 [`/cn/` 协议链接](https://developer.apple.com/cn/support/terms/apple-developer-program-license-agreement/) 在 2026-11-09 显示英文正文。
2. **操作层 / Operational。** Apple 官方审核材料、提交状态、帮助页和 API 文档。入口包括 [App Store Connect Help](https://developer.apple.com/help/app-store-connect/)。
3. **变更层 / Change。** Apple Developer News、RSS、公告正文直链及目标页。见[新闻索引](../news/news-rss-index.zh-CN.md)。新闻不是政策规则。
4. **经验层 / Experience。** Apple Developer Forums、Reddit、CSDN 等社区内容只用于发现测试场景，不改变规则优先级。见[社区经验](../community-evidence/community-evidence.zh-CN.md)。
5. **历史层 / Historical。** 旧版中文指南、旧协议公告、旧新闻和已失效要求。只用于追溯，不得作为当前条款依据。
