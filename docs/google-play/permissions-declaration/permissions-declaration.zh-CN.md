---
id: google-play.permissions-declaration
platform: google-play
language: zh-CN
authority: operational
status: current
kb_checked_at: 2026-10-22
review_due: 2027-01-22
regions: [global]
topics: [play-console, permissions, declaration, review, release]
snapshot_id: play.permissions-declaration
snapshot_package: "GooglePlay-KnowledgeBase-2026-10-24-review.zip"
coverage_status: "detailed-summary"
source_url: "https://support.google.com/googleplay/android-developer/answer/9214102?hl=en"
source_url_zh: "https://support.google.com/googleplay/android-developer/answer/9214102?hl=zh-CN"
effective_date: "current-as-reviewed"
---

# Play Console 权限声明与审核

> **导入说明（Google batch 2）。** 本页正文取自 2026-10-24 Google Play 知识库快照里已经分开的中文改写（`play.permissions-declaration`，核对日 2026-10-22），不是 Google 已发布中文页面的逐字文本。英文官方页面是效力来源。`kb_checked_at` 使用快照源文件记录的核对日；本次导入没有重新打开线上官方页面。文中“本知识库”“本库”“本地专题”描述的是该快照知识库的覆盖范围，不是本仓库已经导入的页面清单。快照里指向尚未导入本仓库的专题、链接图、台账或 CSV 的相对链接，已改为文字提及；指向 Google batch 1 或本批七个专题的相对链接已改到本仓库路径。快照记录英文帮助页正文和简体中文页都已打开，主体链接一致；没有把这篇主帮助页记为抓取失败。所链的敏感权限页面预告位置与联系人变更于 2027-01-27 生效；这些是未来变更，不是当前申报表规则，日期必须分开。Play Academy 课程直链返回 Cache miss，快照不根据标题推断课程内容。本页描述 Play Console 的权限声明与审核步骤。证据等级：`operational`。它不替代相应的权限政策。

**核对日期：2026-10-22。** 高风险或敏感权限（例如 SMS、通话记录、后台位置等）的申请会在发布流程中审核。符合技术条件不等于获批；按 Console 当前表单和适用专项政策提交材料。

## 何时会出现声明表单

上传包含尚未向 Google Play 声明的受限权限的 App Bundle 后，发布流程会要求填写 Permissions Declaration Form。只要 Open、Closed 或 Internal testing 轨道仍有一个需要声明的活跃 App Bundle，Play Console 就会在 App content 下提示待处理事项；在通过含有权限声明的新版本或移除相关权限解决前，无法发布应用的任何更改，包括商店详情、价格或分发设置。

不再使用且不合规的测试轨道应考虑停用。若新权限列表中出现并非计划使用的权限，先移除对应 Bundle/APK，再上传权限集合正确的新包，不要用不准确的声明继续提交。

## 声明表单步骤

1. **核对权限清单：** 查看此前已声明权限和新增权限；新增权限会进入审核。将它们与 Manifest、所有轨道包及实际代码行为核对。
2. **选择核心功能：** 从表单支持的用途类别中选择适用于应用的核心功能，并确保与商店页醒目展示的实际功能一致。
3. **提供审核说明：** 说明审核人员如何进入并验证需要权限的功能。
4. **提供演示视频：** 通过 YouTube（官方优先）或可访问的云端视频文件展示核心功能和权限使用流程。
5. **提供受限内容访问方式：** 若功能要求登录或特殊访问，提交有效的测试账号/号码、密码和操作步骤。只能提供专供审核的测试凭据，不能给真实用户账号。无需特殊访问时，明确选择功能均可直接访问。
6. **仅多 APK 情形申请旧包例外：** SMS/通话记录旧 APK 例外字段只在多 APK 配置且某变体请求这些权限时出现。按 [SMS/通话记录政策](../sms-call-log/sms-call-log.zh-CN.md)或[后台位置政策](https://support.google.com/googleplay/android-developer/answer/9799150)核对条件，填写符合条件的 version code；不符合条件的 APK 必须停用。
7. **确认声明：** 确认材料准确，并同意按声明用途使用权限。

完成表单后继续准备应用审核并发布版本。声明只是审核输入，不是独立的政策豁免。

## 审核期间与发布影响

- 提交表单并推出版本后会进入扩展审核；官方说明可能需要数周。等待期间，新应用或更新可能显示为 Pending publication。
- 如果覆盖/替换待发布版本，可能增加审核延迟。
- 如需紧急发布，官方指引是从 App Bundle 移除高风险/敏感权限后重新推出版本。该版本只进入标准合规审核；帮助页称可能在数小时内发布，但不构成时限保证。
- 不合规时，Play 会向开发者账号的 Account Owner 和联系邮箱发送审核结果；获批且整体符合 Developer Program Policy 后，版本会自动发布。

## Publishing API 特殊流程

若通过 Google Play Developer Publishing API 发布，而权限尚未获得审核批准，接口会返回错误。开发者需要：

1. 删除高风险/敏感权限并重新上传合规 Bundle；或
2. 改用 Play Console 网页界面上传 Bundle、完成 Permissions Declaration Form 并推出该版本。

声明及政策审核通过后，才可继续用 Publishing API 管理后续发布。每当新增权限，都必须在 Console 网页界面填写针对新权限的修订声明。

## 提交前核对清单

- [ ] 统计生产、开放测试、封闭测试和内部测试中的全部活跃 Bundle/APK。
- [ ] 将每项权限映射到政策允许用途、已实现的核心功能、商店页描述和实际数据流。
- [ ] 移除误带入或不再需要的权限；停用不再使用的违规测试轨道。
- [ ] 视频、逐步复现说明、账号/测试凭据能让审核人员访问受限功能。
- [ ] 隐私政策、应用内显著披露/同意和 Data safety 声明与权限用途、SDK 行为一致。
- [ ] 留出扩展审核时间，不把表单提交或测试轨道状态当成权限批准。

## 关联页面

| 页面 | 与权限声明的关系 |
| --- | --- |
| [SMS 与通话记录权限](../sms-call-log/sms-call-log.zh-CN.md) | 给出允许处理器、临时例外、禁止用途、替代 API 和旧 APK 例外条件。 |
| [敏感信息权限总则](../sensitive-permissions/sensitive-permissions.zh-CN.md) | 说明核心功能、最小范围、披露/同意和不同受限权限的专项要求。 |
| [用户数据政策](../user-data/user-data.zh-CN.md) 与 [Data safety 表单](../data-safety/data-safety.zh-CN.md) | 表单之外仍须完成用户披露、隐私政策、数据安全声明及 SDK 核查。 |
| [后台位置权限政策](https://support.google.com/googleplay/android-developer/answer/9799150) | 另一种需要声明、演示和审核材料的敏感权限场景。 |
| [Prepare your app for review](https://support.google.com/googleplay/android-developer/answer/9859455) 与 [Prepare and roll out a release](https://support.google.com/googleplay/android-developer/answer/9859348) | 声明完成后的审核准备与发布操作；发布流程变动以 Play Console 当前界面为准。 |
| [Developer Program Policy](../developer-program-policy/developer-program-policy.zh-CN.md) | 适用于权限申报之外的整体开发者政策。 |

## 正文直链逐项核验

英文正文有 14 次链接出现，去重后为 11 个外部目标和 1 个页内锚点；Publishing API 与“准备和发布版本”各重复出现一次。简体中文页也已单独打开，主体链接一致。下表按正文链接而非 Help Center 导航栏统计。

| 正文链接目标 | 访问结果与关系 |
| --- | --- |
| [Android App Bundle（正文旧地址）](https://developer.android.com/platform/technology/app-bundle/index.html) → [现行指南](https://developer.android.com/guide/app-bundle) | 旧 Android Developers 地址重定向到现行 App Bundle 指南。它说明上传包格式及 Play 如何按设备生成 APK；是发布技术背景，不等于敏感权限获批。AAB 发布流程另见应用设置专题（快照：`../play-console-app-setup.md`，未导入本仓库）和[发布流程专题](../publishing/play-release-workflow.zh-CN.md)。该指南的技术后代仍未全部递归展开。 |
| [高风险或敏感权限](https://play.google.com/about/privacy-security-deception/permissions/) → [现行敏感权限政策](https://support.google.com/googleplay/android-developer/answer/16558241?hl=en) | 旧政策入口先跳到 `answer/16324062`，再跳到现行合并政策 `answer/16558241`。当前页面还预告位置权限及联系人权限变更于 **2027-01-27** 生效；现行规则与未来生效变更应按日期区分。详见[敏感权限专题](../sensitive-permissions/sensitive-permissions.zh-CN.md)。 |
| [Google Play Developer Publishing API](https://developers.google.com/android-publisher/) | API 总览说明发布 API 可上传/发布应用、管理轨道和商店详情，并采用事务式 edits。本文中的权限要求是额外的发布准入条件：首次或新增受限权限仍须先走 Console 声明/审核；API 参考不构成政策豁免。发布流程另见[发布流程专题](../publishing/play-release-workflow.zh-CN.md)。 |
| 本页[Publishing API 特别说明](https://support.google.com/googleplay/android-developer/answer/9214102?hl=en) | 页内链接回到本页的 API 特别流程，没有独立子页面。具体链接锚点会随 Help Center 页面结构变化。 |
| [Published guidelines（旧帮助页）](https://support.google.com/googleplay/android-developer/answer/9888170) → [现行敏感权限政策](https://support.google.com/googleplay/android-developer/answer/16558241?hl=en) | 旧 `answer/9888170` 已重定向到现行敏感权限页，与上方政策入口汇合；不应重复算作独立现行规则。 |
| [SMS 或通话记录权限组（旧帮助页）](https://support.google.com/googleplay/android-developer/answer/9047303) → [现行 SMS/Call Log 政策](https://support.google.com/googleplay/android-developer/answer/10208820?hl=en) | 旧 `answer/9047303` 重定向到 `answer/10208820`。默认处理器资格、允许用途、替代 API、声明与拒绝示例见[SMS/通话记录专题](../sms-call-log/sms-call-log.zh-CN.md)。 |
| [后台位置权限](https://support.google.com/googleplay/android-developer/answer/9799150?hl=en) | 正文将其作为旧 APK 例外/敏感权限的补充规则。已打开并在[后台位置专题](../background-location/background-location.zh-CN.md)摘要；视频、显著披露和表单后代仍有未闭合项。 |
| [Prepare your app for review（旧帮助页）](https://support.google.com/googleplay/android-developer/answer/9815348) → [现行审核准备页](https://support.google.com/googleplay/android-developer/answer/9859455?hl=en) | 旧 `answer/9815348` 跳转到现行 `answer/9859455`。审核凭据、App content 和政策/商店信息前置条件见审核准备专题（快照：`app-review-preparation.md`，未导入本仓库）。 |
| [Prepare and roll out a release（旧帮助页）](https://support.google.com/googleplay/android-developer/answer/7159011) → [现行发布流程](https://support.google.com/googleplay/android-developer/answer/9859348?hl=en) | 旧 `answer/7159011` 跳转到现行 `answer/9859348`。本文的审核通过后发布步骤与[发布流程专题](../publishing/play-release-workflow.zh-CN.md)交叉引用。 |
| [Pending publication（旧帮助页）](https://support.google.com/googleplay/android-developer/answer/6334282) → [现行 Publish your app 帮助页](https://support.google.com/googleplay/android-developer/answer/9859751?hl=en) | 旧 `answer/6334282` 跳转到现行发布状态页；它说明应用、更新和单项状态，不代表权限申报本身已批准。见[发布流程专题](../publishing/play-release-workflow.zh-CN.md)。 |
| [Google Play policies（旧入口）](https://play.google.com/policy) → [Developer Policy Center](https://play.google/developer-content-policy/) | 旧入口重定向到政策目录。目录页不等于单一的 Developer Program Policy 正文；合并版政策见[Developer Program Policy 专题](../developer-program-policy/developer-program-policy.zh-CN.md)。 |
| [Play Academy：Play Console 权限课程](https://playacademy.exceedlms.com/student/path/264896) | 正文课程直链已尝试打开，返回 Cache miss；无法读取课程正文或其子链接，不据标题推断课程内容。 |

## Help Center 侧栏目标（与正文链接分开）

页面显示 29 个导航项，其中包含本页；其余 28 个目标均已点击或有独立的逐页审计记录。侧栏是发布/账号/产品帮助导航，不应与正文政策条款混为一谈。已存在的双语摘要和具体状态按页面主题交叉列出；少数通用支持目录或技术页仍只记录入口/有限摘要。

| 侧栏目标 | 本地关系与审计状态 |
| --- | --- |
| [Create and set up your app](https://support.google.com/googleplay/android-developer/answer/9859152?hl=en) | 应用设置专题（快照：`../play-console-app-setup.md`，未导入本仓库）；侧栏点击超时，但该目标已有独立完整正文审计。 |
| [App testing requirements for new personal developer accounts](https://support.google.com/googleplay/android-developer/answer/14151465?hl=en) | [发布流程专题](../publishing/play-release-workflow.zh-CN.md)已整理适用账号、12 名测试者/14 天、生产权限申请与 14 个正文目标。 |
| [Device verification requirements for new developer accounts](https://support.google.com/googleplay/android-developer/answer/14316361?hl=en) | Play Console 要求专题（快照：`../play-console-requirements.md`，未导入本仓库）与开发者验证专题（快照：`../android-developer-verification.md`，未导入本仓库）交叉整理；账号/设备操作仍须登录。 |
| [Set up your app on the app dashboard](https://support.google.com/googleplay/android-developer/answer/9859454?hl=en) | 应用设置专题（快照：`../play-console-app-setup.md`，未导入本仓库）；Console 任务清单依账号和应用而变。 |
| [Inspect app versions](https://support.google.com/googleplay/android-developer/answer/9844279?hl=en) | 应用设置专题（快照：`../play-console-app-setup.md`，未导入本仓库）记录 App Bundle Explorer 与版本信息；实际应用数据需登录。 |
| [Prepare and roll out a release](https://support.google.com/googleplay/android-developer/answer/9859348?hl=en) | [发布流程专题](../publishing/play-release-workflow.zh-CN.md)；含测试轨道、版本、签名、分阶段发布和提交步骤。 |
| [About your submission activity](https://support.google.com/googleplay/android-developer/answer/17118609?hl=en) | [发布流程专题](../publishing/play-release-workflow.zh-CN.md)记录 submission ID、来源和状态历史；自 2026-05-01 起保留最多一年记录。 |
| [Halting a fully rolled-out release](https://support.google.com/googleplay/android-developer/answer/16285429?hl=en) | [发布流程专题](../publishing/play-release-workflow.zh-CN.md)说明可停止非 Internal 轨道的 100% rollout；旧版本回退受资格限制。 |
| [Detect app issues early with pre-review checks](https://support.google.com/googleplay/android-developer/answer/14807773?hl=en) | [发布流程专题](../publishing/play-release-workflow.zh-CN.md)总结预检入口、适用范围和限制；预检通过不代表正式政策审核通过。 |
| [Publish your app](https://support.google.com/googleplay/android-developer/answer/9859751?hl=en) | [发布流程专题](../publishing/play-release-workflow.zh-CN.md)整理应用/更新/项目状态、拒绝和托管发布。 |
| [Helpful tips to get your app published](https://support.google.com/googleplay/android-developer/answer/15191715?hl=en) | 已打开并逐项尝试 13 个正文链接；商店资料、审核凭据、测试轨道及拒绝修复与[发布流程专题](../publishing/play-release-workflow.zh-CN.md)关联。 |
| [Best Practices for White Label Developers](https://support.google.com/googleplay/android-developer/answer/15884185?hl=en) | 已打开并尝试 11 个正文链接；建议按客户分散账号、每个应用提供独特资料、提交前质量检查，详见白标公告资源（快照：`../google-play-announcement-resources.md`，未导入本仓库）。 |
| [Update or unpublish your app](https://support.google.com/googleplay/android-developer/answer/9859350?hl=en) | [目标 API 专题](../target-api/target-api-level.zh-CN.md)及[发布流程专题](../publishing/play-release-workflow.zh-CN.md)说明下架与旧系统用户可见性不同。 |
| [Control when app changes are reviewed and published](https://support.google.com/googleplay/android-developer/answer/9859654?hl=en) | [发布流程专题](../publishing/play-release-workflow.zh-CN.md)区分“发送审核”与“托管发布”；侧栏点击报错但该目标有独立完整正文审计。 |
| [Release app updates with staged rollouts](https://support.google.com/googleplay/android-developer/answer/6346149?hl=en) | [发布流程专题](../publishing/play-release-workflow.zh-CN.md)整理分阶段发布、暂停和扩大比例；子链接仍为部分覆盖。 |
| [Prompt users to update to your latest app version](https://support.google.com/googleplay/android-developer/answer/13812041?hl=en) | [发布流程专题](../publishing/play-release-workflow.zh-CN.md)整理 Recovery 资格、范围及 Wear OS/TV/Automotive 等排除项。 |
| [Manage your store listings](https://support.google.com/googleplay/android-developer/topic/3450987?hl=en) | 已作为商店详情导航目录打开；主题页后代见商店详情与素材专题（快照：`store-listing-best-practices.md`，未导入本仓库），目录的深层子页不在此重复展开。 |
| [Distribute your instant experience](https://support.google.com/googleplay/android-developer/answer/7381861?hl=en) | 这是历史 Instant Apps 操作页；当前停用状态及迁移资料见Android Instant Apps 历史专题（快照：`android-instant-apps.md`，未导入本仓库）。 |
| [Manage different form-factor releases](https://support.google.com/googleplay/android-developer/answer/13295490?hl=en) | 审核准备专题（快照：`app-review-preparation.md`，未导入本仓库）和应用质量/设备形态专题（快照：`app-quality-and-form-factor-guidelines.md`，未导入本仓库）区分各设备轨道与质量要求。 |
| [Add or test APK expansion files](https://support.google.com/googleplay/android-developer/answer/2481797?hl=en) | 已打开的旧 APK 扩展文件操作帮助；App Bundle 不支持 OBB 的边界见应用设置专题（快照：`../play-console-app-setup.md`，未导入本仓库）。该旧页的当前适用性仍需按实际旧应用/上传形式核对。 |
| [Google Play game services](https://support.google.com/googleplay/android-developer/topic/7071327?hl=en) | 仅打开了 Help Center 主题目录；其游戏服务子页不是权限申报政策，本库未声称遍历目录全部后代。 |
| [Using third-party SDKs in your app](https://support.google.com/googleplay/android-developer/answer/10358880?hl=en) | SDK 风险提示及开发者责任见第三方 SDK 专题（快照：`sdk-requirements.md`，未导入本仓库）；Console 中应用专属警告需登录。 |
| [Target API level requirements](https://support.google.com/googleplay/android-developer/answer/11926878?hl=en) | [目标 API 专题](../target-api/target-api-level.zh-CN.md)整理截至 2026-10-22 的版本矩阵和延期；动态年度门槛发布前应再核对。 |
| [Create and distribute a watch face](https://support.google.com/googleplay/android-developer/answer/13560201?hl=en) | 审核准备专题（快照：`app-review-preparation.md`，未导入本仓库）整理 Wear OS 轨道、素材、格式和审核；category/tags 目标曾超时。 |
| [Prepare your app for review](https://support.google.com/googleplay/android-developer/answer/9859455?hl=en) | 审核准备专题（快照：`app-review-preparation.md`，未导入本仓库）含审核访问凭据、政策声明和商店内容前置项；深层账号路由仍受限。 |
| [Request more time to complete a policy declaration](https://support.google.com/googleplay/android-developer/answer/15644220?hl=en) | 延期表单需从特定 Console 警告进入；其资格和已提交状态无法公开验证，见Play Console 要求专题（快照：`../play-console-requirements.md`，未导入本仓库）。 |
| [Manage your store listing, experiment, and event graphics with the Asset Library](https://support.google.com/googleplay/android-developer/answer/16386748?hl=en) | 审核准备专题（快照：`app-review-preparation.md`，未导入本仓库）与商店详情专题（快照：`store-listing-best-practices.md`，未导入本仓库）整理素材库操作、政策素材要求和 DDA 关系。 |
| [Version codes](https://support.google.com/googleplay/android-developer/answer/17367361?hl=en) | 审核准备专题（快照：`app-review-preparation.md`，未导入本仓库）整理递增规则/上限，并链接 Android 多 APK 技术指南。 |

## 覆盖状态

本文按官方中英文帮助页正文整理触发表单的条件、全部七步、测试轨道影响、审核时间、紧急发布路径和 Publishing API 用户流程，并逐项记录了正文的 11 个外部目标、1 个页内锚点及 28 个侧栏同级目标。正文目标均已打开、重定向核实或明确标记为课程缓存不可读；侧栏中有四个本次点击遇到抓取错误的页面，均有独立完整正文审计。**后代链接并未无限递归闭合**：优先补充仍部分覆盖的后台位置表单/最佳实践、Android App Bundle 技术分支及游戏服务目录；账号登录页、课程和更深 API 示例须保留访问边界。

此文为结构化双语改写，不逐字镜像官方原文；以官方来源和 Console 实际表单为准。
