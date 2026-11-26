# Google Play / Google Play 应用商店

本目录整理 Google Play Developer Distribution Agreement、Developer Program Policies、Play Console 操作、User Data、Data Safety、敏感权限、账号删除、目标 API、计费和发布要求。

## Priority reading path / 推荐阅读顺序

1. [Developer Distribution Agreement / 开发者分发协议](developer-distribution-agreement/developer-distribution-agreement.zh-CN.md)。英文协议文本控制译文。
2. [Consolidated Developer Program Policy / 合并版开发者计划政策](developer-program-policy/developer-program-policy.zh-CN.md)。快照记录除另有说明外自 2026-09-30 起生效。协议、政策和 Console 申报保持分开。
3. [User Data / 用户数据](user-data/user-data.zh-CN.md)
4. Data Safety：[baseline / 基线](data-safety/data-safety-baseline.zh-CN.md) 与 [form detail / 表单详解](data-safety/data-safety.zh-CN.md)。表单申报不替代 User Data 政策。
5. [Payments, subscriptions, and billing programs / 付款、订阅与计费项目](payments/payments-and-subscriptions.zh-CN.md)
6. [Testing, review, and release / 测试、审核与发布](publishing/play-release-workflow.zh-CN.md)
7. 敏感权限 / Sensitive permissions，与 User Data 和 Data Safety 分开：[Sensitive permissions and APIs](sensitive-permissions/sensitive-permissions.zh-CN.md)、[权限声明 / Permissions declaration](permissions-declaration/permissions-declaration.zh-CN.md)、[后台位置 / Background location](background-location/background-location.zh-CN.md)、[SMS 与通话记录 / SMS and Call Log](sms-call-log/sms-call-log.zh-CN.md)、[照片与视频权限 / Photo and video permissions](photo-video-permissions/photo-video-permissions.zh-CN.md)。敏感权限页和 SMS/通话记录页上的现行规则与 2027-01-27 生效预告按日期分开。
8. [账号删除 / Account deletion](account-deletion/account-deletion.zh-CN.md)。User Data 页仍保留简短摘要并链接到这里。内容、UGC、儿童安全与年龄限制仍是后续导入。
9. [目标 API / Target API level requirements](target-api/target-api-level.zh-CN.md)。执行、申诉和地区期限仍是后续导入。

## Topics in this directory / 本目录专题

| Topic | Chinese | English | Evidence | Snapshot review |
| --- | --- | --- | --- | --- |
| Developer Distribution Agreement | [zh-CN](developer-distribution-agreement/developer-distribution-agreement.zh-CN.md) | [en-US](developer-distribution-agreement/developer-distribution-agreement.en-US.md) | Normative | 2026-10-24 |
| Developer Program Policy | [zh-CN](developer-program-policy/developer-program-policy.zh-CN.md) | [en-US](developer-program-policy/developer-program-policy.en-US.md) | Normative | 2026-10-24 |
| User Data | [zh-CN](user-data/user-data.zh-CN.md) | [en-US](user-data/user-data.en-US.md) | Normative | 2026-10-24 |
| Data Safety baseline | [zh-CN](data-safety/data-safety-baseline.zh-CN.md) | [en-US](data-safety/data-safety-baseline.en-US.md) | Normative | Phase 1 page, checked 2026-11-26 |
| Data safety form | [zh-CN](data-safety/data-safety.zh-CN.md) | [en-US](data-safety/data-safety.en-US.md) | Operational | 2026-10-24; partial descendant coverage |
| Payments and subscriptions | [zh-CN](payments/payments-and-subscriptions.zh-CN.md) | [en-US](payments/payments-and-subscriptions.en-US.md) | Normative policy; operational and implementation notes are labelled in the page | 2026-10-24 |
| Release workflow | [zh-CN](publishing/play-release-workflow.zh-CN.md) | [en-US](publishing/play-release-workflow.en-US.md) | Operational | 2026-10-22 |
| Sensitive permissions and APIs | [zh-CN](sensitive-permissions/sensitive-permissions.zh-CN.md) | [en-US](sensitive-permissions/sensitive-permissions.en-US.md) | Normative policy; Android API material is labelled as an implementation note | 2026-10-24; current rules and 2027-01-27 preview kept separate |
| Permissions declaration | [zh-CN](permissions-declaration/permissions-declaration.zh-CN.md) | [en-US](permissions-declaration/permissions-declaration.en-US.md) | Operational | 2026-10-22 |
| Background location | [zh-CN](background-location/background-location.zh-CN.md) | [en-US](background-location/background-location.en-US.md) | Normative policy; Android location guidance is labelled as an implementation note | 2026-10-23 |
| SMS and Call Log | [zh-CN](sms-call-log/sms-call-log.zh-CN.md) | [en-US](sms-call-log/sms-call-log.en-US.md) | Normative policy; Android and Play services alternatives are implementation notes | 2026-10-24; current rules and 2027-01-27 preview kept separate |
| Photo and video permissions | [zh-CN](photo-video-permissions/photo-video-permissions.zh-CN.md) | [en-US](photo-video-permissions/photo-video-permissions.en-US.md) | Normative policy; Photo Picker guidance is an implementation note | 2026-10-23 |
| Account deletion | [zh-CN](account-deletion/account-deletion.zh-CN.md) | [en-US](account-deletion/account-deletion.en-US.md) | Normative requirement; Data safety and Console steps are operational | 2026-10-24 |
| Target API level | [zh-CN](target-api/target-api-level.zh-CN.md) | [en-US](target-api/target-api-level.en-US.md) | Normative Play requirements; Android migration guides are implementation notes | 2026-10-24 |

## Source hierarchy / 来源层级

以当前 Google Play Policy Center、Android Developers 和 Play Console Help 为准。Android API 或开发指南不自动等于 Play eligibility；文档必须区分平台政策义务与工程实现建议。

[Google Play Policy Center](https://play.google.com/about/developer-content-policy/)
[Google Play Console Help](https://support.google.com/googleplay/android-developer/)
[Android Developers](https://developer.android.com/)

## Snapshot note / 快照说明

Google batch 1 从 2026-10-24 Google Play Knowledge Base 快照导入开发者分发协议、合并版开发者计划政策、User Data、Data safety 表单、付款与发布流程这六个专题。表中的 Data Safety baseline 仍是 Phase 1 页面。Google batch 2 从同一快照再导入敏感权限、权限声明、后台位置、SMS 与通话记录、照片与视频权限、账号删除和目标 API。这些页面的 `kb_checked_at` 是快照源文件记录的核对日，不是本次导入时对线上页面的重新复核。英文官方页面是效力来源。中文专题正文是编辑改写，不是 Google 已发布中文页面的逐字文本。

语言差异（读不到的 `zh-CN` 路由、AI 翻译提示、分发协议中文日期格式异常，以及第 16.1 条英文控制译文）写在各页导入说明和[快照清单](../../data/sources/google-play-kb-snapshot-2026-10-24.md)中。Batch 2 里，敏感权限和目标 API 的 Play Help `zh-CN` 路由在快照中未能读取。SMS/通话记录的中文页无法稳定抓取，中文稿依据英文正文；同时 `hl=zh-Hans` 页仍显示旧例外表，这不表示 2027-01-27 的日期被取消。账号删除的精确 `hl=zh-CN` 路由未能读取，核对使用的是已打开的 `hl=zh-Hans` 页面。权限声明的简体中文页已打开。后台位置和照片/视频主文没有记录 `hl=zh-CN` 抓取失败。敏感权限和 SMS/通话记录同时保留现行规则与 2027-01-27 生效的预告，两类日期不合并。抓取失败不表示政策已经变更。

合并版 Developer Program Policy 在该快照中的生效日是 2026-09-30。更早政策措辞不作为现行规则。

开发者分发协议、开发者计划政策、Play Console 发布步骤和 Data Safety 申报保持为不同专题。敏感权限、权限声明、后台位置、SMS 与通话记录、照片与视频权限、账号删除和目标 API 也各自独立，不并入 User Data 或 Data Safety。
