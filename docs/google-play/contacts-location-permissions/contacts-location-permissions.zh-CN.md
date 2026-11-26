---
id: google-play.contacts-location-permissions
platform: google-play
language: zh-CN
authority: normative
status: current
kb_checked_at: 2026-10-24
review_due: 2027-01-24
regions: [global]
topics: [contacts, foreground-location, contact-picker, location-button, read-contacts, manage-contacts]
snapshot_id: play.contacts-location-minimum-scope
snapshot_package: "GooglePlay-KnowledgeBase-2026-10-24-review.zip"
coverage_status: "detailed-summary"
source_url: "https://support.google.com/googleplay/android-developer/answer/16909972?hl=en"
source_url_minimum_scope: "https://support.google.com/googleplay/android-developer/answer/16935362?hl=en"
source_url_location: "https://support.google.com/googleplay/android-developer/answer/17033915?hl=en"
effective_date: "preview-2027-01-27; newsletter 2026-10-28 kept separate; MANAGE_CONTACTS date is 2027 with no exact day"
---

# 联系人与前台位置权限：最小范围和替代方案

> **导入说明（Google batch 5）。** 正文来自已经分开的 2026-10-24 Google Play 知识库快照（`play.contacts-location-minimum-scope`，核对日 2026-10-24）的改写摘要，不是官方页面的逐字副本。英文官方页面是效力来源。`kb_checked_at` 是快照源文件记录的核对日；本次导入没有重新打开线上官方页面。文中“本知识库”“本库”“本地专题”等说法描述的是该快照库的覆盖范围，不是本仓库已经导入的页面。指向本仓库没有收录的专题、链接图、台账或 CSV 的相对链接改为文字提及。指向 Google batch 1–4 或本批八个专题的相对链接改为本仓库文件。 中文源文件写明，简体中文是基于英文官方政策和 Android 开发者文档的结构化翻译与改写。两种语言文件记录的 Play 帮助政策地址都是英文 `hl=en`。快照没有记录已逐项核对的中文官方联系人或前台位置政策页面。本仓库中文正文是该快照改写，不是 Google 已发布的中文页面文本。如果中文预览页面措辞不同，快照要求以生效时的正式政策及 Console 要求为准。联系人与前台位置的最小范围规则是预定生效的政策预告，在快照核对日还不是已经生效的现行规则。正式政策预览和 Policy Deadlines 表都列 2027-01-27。2026 年 4、6、7 月 Play Developers Newsletter 另写 2026-10-28，快照称 Google 没有解释这两个日期的关系。精确位置的 Play Console 声明在快照中预计于 2026 年 11 月开放。最小范围帮助页 FAQ 另预计 2027 年 1 月下旬执行，并称时间线可能按开发者反馈再确定；该预期与精确的 2027-01-27 分开。写入联系人和 `MANAGE_CONTACTS` 是另一条分支：博客把 Play 声明和政策合规日期写成“2027 年，不早于即将发布的 Android 版本”，没有给出具体日历日，并把这项特殊访问权限安排在 Android 17 QPR2（2026 年第四季度）。不要把这些日期并入现行 `READ_CONTACTS` 或位置规则，也不要把抓取失败或未完成的抓取当成政策变更。Play 政策文本是 `normative`。Contact Picker、Location Button 和 People Directory 是 Android 实现说明。Manifest 声明或系统选择器不等于 Play 批准。

**核对日期：2026-10-24。** 本页归纳 2026 年 4 月公告涉及的联系人和前台位置新规则、官方替代 API 及实施时间。正式政策预览和 Policy Deadlines 表均列 **2027-01-27**；但 2026 年 4、6、7 月 Play Developers Newsletter 另写 **2026-10-28**，官方资料尚未解释两日期的关系。定位声明预计于 2026 年 11 月在 Play Console 开放。最小范围 Help 页 FAQ 另称预计在 2027 年 1 月下旬执行，并表示会根据开发者反馈进一步明确时间线；这是执行预期，不替代期限表中精确列出的 **2027-01-27**。日期差异和应对见下方时间线；还须查看账号内 Console 通知。

简体中文为基于英文官方政策和 Android 开发者文档的结构化翻译/改写；如果中文页面的预览措辞不同，以生效时的正式政策及 Console 要求为准。

## 先判断访问范围

| 场景 | 首选做法 | 何时可能申请广泛权限 |
| --- | --- | --- |
| 用户挑选一位/若干联系人来分享、邀请、发送短信或填写信息 | 使用 Android Contact Picker，仅请求该流程要用的字段 | Contact Picker 无法支持应用商品详情所宣传的核心功能，且能在声明中说明数据需求和替代方案不足时，才考虑 `READ_CONTACTS` |
| 用户临时搜索附近地点、分享当前坐标、给内容加位置或填写地址 | 目标 Android 17 / API 37+ 的一次性精确定位使用系统 Location Button；只需城市/区域时用粗略位置 | 常规、持续的 `ACCESS_FINE_LOCATION` 仅在粗略位置和 Location Button 都无法支持核心功能时考虑。注意：按钮专用 Manifest 仍可能声明 `ACCESS_FINE_LOCATION`（加 `onlyForLocationButton`）；现行 Play 帮助页要求所有申请该权限的应用完成 Console 声明 |

联系人和位置数据都是个人及敏感数据。即使访问通过系统选择器或按钮发生，数据收集、用途、共享、安全和删除仍须符合 [User Data](../user-data/user-data.zh-CN.md) 与 [Data safety](../data-safety/data-safety.zh-CN.md) 要求。更广泛的 Android 权限替代方案、用户披露/同意和标识符最佳实践见[Android 隐私清单](../android-privacy-checklist/android-privacy-checklist.zh-CN.md)。

## Contacts Permissions：联系人权限

- **适用门槛：** 目标 Android 17 / API 37 及以上的应用，只有在 Android Contact Picker 不足以支撑核心功能时才可申请 `READ_CONTACTS`。
- **Play Console：** 仍申请 `READ_CONTACTS` 的应用须提交联系人权限声明，说明需要哪些联系人字段、对应哪项核心功能，以及为何 Contact Picker 在技术上不够。官方帮助页称 2026 年 9 月起，带有 `READ_CONTACTS` 的开发者会在 Console 收到声明提示。
- **披露边界：** 不得披露或公开非公开联系人信息，除非获得联系人数据主体本人的授权。通讯录内容不能因为用户授予访问就默认可上传、公开或用于其他目的。
- **时间：** 这是 2026 年新增政策，正式生效日为 2027-01-27。

### 联系人声明的用途和边界

Play 的用途选项包括联系人管理、拨号或短信、通话记录、CRM、来电筛选、无障碍、个人助理、好友匹配/搜索、备份恢复/设备迁移、自动更正/自动补全、用户主动选择联系人，以及“其他”。这些是申报分类和示例，不是自动获批名单。声明还须解释为什么 Contact Picker 不足以支撑对应核心功能。

如果功能只是分享文件、协作、邀请/推荐他人加入服务，或选择一个联系人进行交易，帮助页通常认为不应申请完整 `READ_CONTACTS`；自制联系人选择界面也不构成保留宽泛访问的理由。私人应用和企业设备管理应用获该项 Contacts 政策要求的豁免；应用是否属于豁免类别应按官方定义确认。

### Contact Picker 的实现要点

Android 17/API 37 的系统 Picker 让应用先声明需要的数据字段，再由用户选择联系人或具体数据项。推荐 API action 为 `ContactsPickerSessionContract.ACTION_PICK_CONTACTS`；该 Contract 及其 `Session` 类从 API 37 加入。结果为一次性的 session URI，只能读取用户选中的字段，不需要 `READ_CONTACTS`。该 Picker 不回移到更早 Android 版本。

- 必须设置 `EXTRA_PICK_CONTACTS_REQUESTED_DATA_FIELDS`，且只列出功能实际使用的 MIME 类型。当前 Android API 允许结构化姓名、邮箱、电话、邮寄地址、组织、关系、事件、照片、群组成员、网站和昵称；传入未支持的类型会触发 `IllegalArgumentException`。短信邀请只需请求电话字段。
- 默认情况下，联系人只要有任一请求字段就会显示。仅当每个字段都必不可少时，才将 `EXTRA_PICK_CONTACTS_MATCH_ALL_DATA_FIELDS` 设为 `true`；默认 `false` 会保留更多可选联系人。
- 默认单选。添加 `Intent.EXTRA_ALLOW_MULTIPLE` 才开放多选；`EXTRA_PICK_CONTACTS_SELECTION_LIMIT` 默认上限为 50，最高可设为 100。若功能只需较少接收人，应设更小上限。
- 只查询选择完成后返回的 session URI；不能直接查询 `Session.CONTENT_URI` 基础集合，也不能传自定义 `selection` 或 `selectionArgs`，官方 API 说明这些参数不受支持。指南示例将游标读取放在后台线程处理。
- 一个联系人可能有多个邮箱或电话号码。可用 `ContactsContract.Contacts.LOOKUP_KEY` 聚合同一联系人数据，并在界面需要区分时展示“工作/个人”等字段标签。返回结果会剥离账号专属元数据。
- Session 权限是临时的。若用户功能确实需要在进程退出后继续使用已选字段，只保存必要值，并限于已披露的用途；一次选择不构成保留整本通讯录的理由。
- 目标 Android 17/API 37 的旧 `ACTION_PICK` 会自动升级到系统 Picker；如需多字段和 session 结果，应使用 `ContactsPickerSessionContract.ACTION_PICK_CONTACTS` 及对应 extra。Play 帮助预览写作 `Intent.ACTION_PICK_CONTACTS`，实现时按当前 Android API 参考中的符号核对，不要照抄预览名称。在目标 SDK 较低的 Android 17 设备上，可按指南添加系统 Picker extra 测试新界面。

官方 Contact Picker 指南正文的三处示例链接都指向同一个[固定 GitHub 源码提交](https://github.com/android/snippets/blob/e72c9d1fdc9658b16537b8b137ba517e229b02ab/contacts/src/main/java/com/example/contacts/ContactPickerActivity.kt)。2026-10-23 通过 Android 官方仓库的 GitHub 文件页直接读取该固定 `e72c9d1f…` 提交（288 行、265 行代码）；同日尝试的 raw 镜像仍缓存未命中，但这不再影响固定版本源码的核验。样例显式请求系统 Picker，分别演示邮箱/电话字段单选、最多 5 人的多选，以及只请求电话号码并选择具体号码；用户取消或系统 Picker 不可用时不继续处理，并显示不可用提示。成功结果仅使用本次 Picker 返回的 Session URI，在 `Dispatchers.IO` 上投影 `LOOKUP_KEY`、显示名、MIME 类型和数据列，再按 `LOOKUP_KEY` 合并同一联系人的多行；查询不传自定义 `selection`/`selectionArgs`。源码文件头声明 Apache 2.0。知识库另留有[仓库 `main` 分支同路径文件](https://github.com/android/snippets/blob/main/contacts/src/main/java/com/example/contacts/ContactPickerActivity.kt)作为可变分支的旁证；它不是指南正文的直接链接，也不用于替代固定提交。该代码示例不证明应用的 Manifest、Play Console 声明或 `READ_CONTACTS` 资格。2026-10-22 已通过官方 [ContactsPickerSessionContract API 参考](https://developer.android.com/reference/android/provider/ContactsPickerSessionContract) 及其嵌套 [Session API 参考](https://developer.android.com/reference/android/provider/ContactsPickerSessionContract.Session)复核相关成员；大型 API 页只按本专题相关成员审阅，未穷尽全部常量和通用导航。

**API 符号注意：** Android Developers 指南当前正文将请求字段 extra 写作 `EXTRA_REQUESTED_DATA_FIELDS`，但同页 Kotlin 示例和 API 参考使用 `EXTRA_PICK_CONTACTS_REQUESTED_DATA_FIELDS`。实现应以 API 参考符号为准；这是指南正文与示例/API 名称不一致，需留意后续文档更新。

### 新增：写入联系人与 `MANAGE_CONTACTS`（2026-10-21）

Android 官方于 2026-10-21 公布下一版 Android 联系人写入方式调整。它与上文 `READ_CONTACTS` 最小化政策是**不同的权限分支**：旧政策管读取整本通讯录，新变化管直接创建、修改联系人以及调用通讯录目录的方式。

- **普通的、由用户发起的单条新增或编辑：** 使用 `ACTION_INSERT`、`ACTION_EDIT` 或 `ACTION_INSERT_OR_EDIT` 打开系统联系人编辑器，并通过标准 extras 预填数据。Android 官方指南把 Intent 作为单条联系人修改的首选方案；用户可检查并保存，无须应用直接写入权限。
- **系统版本与目标 SDK：** 新版联系人编辑器预计随 2027 年 Android 版本标准化。目标该版本及更高版本的应用若仍通过 `WRITE_CONTACTS`、`ContactsContract` 直接写入，写入将被拒绝并可能抛 `SecurityException` 或权限拒绝。博客称旧目标版本保留现有行为，但新系统的标准 Intent 编辑器可供设备上的应用使用。
- **`MANAGE_CONTACTS`：** Android 17 QPR2（2026 年第四季度）计划提供的特殊应用访问权限，适用于核心用途确实需要批量或后台管理联系人、且联系人 Intent 无法满足的少数应用。官方列举专用联系人管理器/拨号器替代、批量来电识别/垃圾电话更新、企业或云端双向同步、批量备份恢复/设备迁移、联系人专属铃声等可能场景。仅为保留自有品牌编辑 UI 不构成资格。它涵盖读取、添加、编辑、删除联系人、账号及 People Directory 数据，因此无需再同时请求 `READ_CONTACTS`；用户在系统“特殊应用访问权限”设置中启用，不是运行时弹窗。 Android API 37.2 的 [Settings.ACTION_MANAGE_CONTACTS](https://developer.android.com/reference/android/provider/Settings#ACTION_MANAGE_CONTACTS) 会打开“管理联系人”特殊应用访问设置页；部分设备可能没有可处理该 Intent 的 Activity。这是系统设置入口，不代表 Play 批准，也不替代 Play Console 声明。
- **Play 声明：** 博客称使用 `MANAGE_CONTACTS` 上架 Google Play 需要在 Play Console 说明为何联系人 Intent 不足以支撑核心功能。博客写明声明和政策合规时间为“2027 年，且不早于下一版 Android 发布”，没有给出具体日。不要将其误认为现有 `READ_CONTACTS` 政策的 **2027-01-27** 日期。
- **People Directory：** VoIP/消息应用若此前向用户通讯录注入“使用某应用通话/发消息”条目，官方建议改用系统 People Directory。博客称功能随 Android 17 QPR2（2026 年第四季度）推出。当前 `PeopleContract` API 参考说明目录由应用提供者登记、系统聚合/查询，并用受系统保护的 `PendingIntent` 启动交互；参考页同时写明读取 People Provider 需要 `MANAGE_CONTACTS`。这属于 Android 平台 API 说明，不应推断成 Play 的独立政策豁免。
- **迁移注意：** 搜索 manifest 和代码中的 `WRITE_CONTACTS`、`RawContacts.CONTENT_URI`、`Data.CONTENT_URI`、`applyBatch(ContactsContract.AUTHORITY, …)`；按用户动作改用系统 Intent，People Directory 用标准字段/协议，并在没有剩余代码路径后移除 `WRITE_CONTACTS`。系统编辑器不支持自定义 MIME 类型；`SHOW_OR_CREATE_CONTACT` 跨设备行为不一致，宜改为 `ACTION_INSERT_OR_EDIT`。先在 Android 17 QPR2 和目标新版上验证真实设备与目标 SDK 组合。博客还介绍即将新增的 `EXTRA_PHOTO_URI` 预填照片能力。2026-10-23 成功打开的 `ContactsContract.Intents.Insert` API 参考未列出该符号；2026-10-24 对同一大型 API 页的重试超时，定向查找也返回 Internal Error，因此本次无法确认参考页是否已更新。不要把未发布的预览当作当前 API 保证；待新版正式 SDK/参考页可访问后再核验。

#### 官方发布时间与 Play 帮助页的状态差异

| 日期/来源 | 当前可确认内容 | 使用边界 |
| --- | --- | --- |
| 2026-10-21 Android Developers 博客 | 宣布 Android 联系人写入迁移、`MANAGE_CONTACTS` 和 People Directory；QPR2 预计 2026 Q4，下一版 Android 预计在 2027 年；Play 声明/合规不早于该版本发布。 | 平台路线图，没有精确 Play 截止日；版本时间仍应按后续正式发布信息复核。 |
| Play 敏感权限政策预览与 Policy Deadlines 表（2026-10-24 重开） | 预览页仍说明的是面向 Android 17/API 37+ 的 `READ_CONTACTS`、Contact Picker 和 2027-01-27 生效日；Policy Deadlines 表也只有 2027-01-27 的联系人读取政策行，没有 `MANAGE_CONTACTS` 独立条目。现行帮助页提示后续将更新；本次在当前帮助正文和政策预览中均未找到 `MANAGE_CONTACTS`，期限表也没有该权限的独立条目。 | 博客称 Google Play 当日发布更新指引，但当前公开帮助页尚未展示 `MANAGE_CONTACTS` 条款。本知识库据此登记“正式帮助页待复核”，不把 Android 博客中的资格示例扩写成完整 Play 条文或推定具体申报流程。 |

#### Android 联系人写入博客的直接子链接

以下仅统计公告正文中与规则/实现相关的链接；图片、作者简介、标签、站点页脚不计作政策要求。完整目标状态见逐 URL 来源审计（快照：`../source-page-audit.csv`，未导入本仓库）与递归链接图 §4.96（快照：`../google-play-policy-link-graph.md`，未导入本仓库）。

| 公告直接链接 | 页面内容与公告关系 |
| --- | --- |
| [`ACTION_INSERT`](https://developer.android.com/reference/android/content/Intent#ACTION_INSERT)、[`ACTION_EDIT`](https://developer.android.com/reference/android/content/Intent#ACTION_EDIT)、[`ACTION_INSERT_OR_EDIT`](https://developer.android.com/reference/android/content/Intent#ACTION_INSERT_OR_EDIT) → [Intent API](https://developer.android.com/reference/android/content/Intent) | 三个成员均位于同一大型 API 页面并已按成员复核。新增、编辑、二选一的输入/输出语义支持博客推荐的用户确认式编辑器流程；API 页面其余 Intent 成员未穷尽。 |
| [Modify contacts using intents](https://developer.android.com/identity/providers/contacts-provider/modify-data) | 完整打开。推荐把单条联系人新增/修改委托给联系人应用；提供 Kotlin/Java 示例、标准 extras、`LOOKUP_KEY`、账户选择、用户取消路径，并说明 `ACTION_INSERT_OR_EDIT` 的 MIME 类型。该指南最后更新于 2024-05-22，仍是 Android 一般 Intent 实现指导；下一版 Android 对 extras/体验的统一支持以新博客为准。 |
| [Android Contact Picker](https://developer.android.com/about/versions/17/features/contact-picker) | 已作为上文 `READ_CONTACTS` 替代 API 单独审阅；负责读取用户挑选的联系人，不负责写入联系人，也不能替代符合资格的批量管理权限。 |
| [PeopleContract API](https://developer.android.com/reference/android/provider/PeopleContract) | 已打开当前 API 37.2 参考。登记目录的 ContentProvider、查询 Person/Group、变化通知、能力字段，以及由 People Provider 创建受保护 PendingIntent 发起交互；读取 People Provider 要求 `MANAGE_CONTACTS`。API 其他类/成员与 Android 17 QPR2 行为尚未全量核验。 |

#### 公告代码样例中的 Android Settings API（非 HTML 子链接）

博客代码示例提到 `Settings.ACTION_MANAGE_CONTACTS`，但它不是公告正文里的可点击超链接，因此不计入直接子链接数量。2026-10-24 打开了 [Settings API 参考](https://developer.android.com/reference/android/provider/Settings#ACTION_MANAGE_CONTACTS)并核对该成员：API 37.2，该 Intent 打开用户可管理哪些应用可管理联系人的系统设置页；设备上可能没有匹配 Activity，且该动作不带数据 URI、没有输出。此处只抽查一个成员，大型 Settings API 页的其他成员未穷尽。与之相关的 [Manifest.permission.MANAGE_CONTACTS](https://developer.android.com/reference/android/Manifest.permission#MANAGE_CONTACTS) 元数据将其列为 `signature|preinstalled|appop` 保护级别；这是平台 API 元数据，应与博客描述的特殊应用访问流程及 Play 声明一并理解，不能单独据此推导资格。

#### PeopleContract 参考页的重点后代

博客的 People Directory 目标继续链接到下列 API 类型。2026-10-24 已复核这些当前标为 API 37.2 的页面，并针对目录接入和用户通信操作抽样核对：

| PeopleContract 后代 | 页面与公告的关系 |
| --- | --- |
| [Directory](https://developer.android.com/reference/android/provider/PeopleContract.Directory) | 服务通过 Manifest 中 `Directory.DIRECTORY_PROPERTY` 注册 ContentProvider；联系人/群组变化时通知系统 Provider 更新缓存。API 文档建议只允许系统搜索权限访问 Provider，并提示每个应用最多登记一个目录。 |
| [Persons](https://developer.android.com/reference/android/provider/PeopleContract.Persons) 与 [Persons.Query.Builder](https://developer.android.com/reference/android/provider/PeopleContract.Persons.Query.Builder) | 供系统按结构化查询聚合目录人物；实现端返回稳定的目录内 `LOOKUP_KEY`、显示名、照片、能力位和匹配依据。客户端用 builder 表示电话号码、邮箱或 lookup key 查询，不能用传统 SQL `selection`。`
| [Groups](https://developer.android.com/reference/android/provider/PeopleContract.Groups) 与 [Groups.Query.Builder](https://developer.android.com/reference/android/provider/PeopleContract.Groups.Query.Builder) | 对群组提供对应的 URI、字段与结构化查询；通过 lookup key 定位群组，不直接查询持久 lookup URI。 |
| [Intents](https://developer.android.com/reference/android/provider/PeopleContract.Intents)、[Capability](https://developer.android.com/reference/android/provider/PeopleContract.Capability) 与 [PendingIntent](https://developer.android.com/reference/android/app/PendingIntent) | API 37.2 的 `TEXT_REACHABILITY`、`VOICE_REACHABILITY`、`VIDEO_REACHABILITY` 分别为 `4`、`1`、`2`；目录端根据身份实际支持的方式按位或后写入整型 `Persons.CAPABILITY` 列，客户端读取后再展示相应消息/语音/视频入口。客户端用 `Persons.Query.Builder` 构造**恰好一个**指向单一 People Directory 的目标子查询（联系人 lookup key、电话、邮箱，或群组 lookup key），调用 `PeopleContract.createPeopleInteractionRequest()` 取得由 People Provider 身份签发的 `PendingIntent`。目录应用须声明处理 `ACTION_START_PEOPLE_INTERACTION` 的 exported Activity，并读取交互类型及目标查询参数 extras；客户端不应直接发送该 action。通用 `PendingIntent` API 的其余安全成员未穷尽。 |
| [`MANAGE_CONTACTS` Manifest 权限定义](https://developer.android.com/reference/android/Manifest.permission#MANAGE_CONTACTS) | API 37.2 定义该权限用于完整联系人管理，面向少数需要此能力的应用；参考页列出的保护级别为 `signature\|preinstalled\|appop`。这是平台权限元数据，须与公告中的特殊应用访问设置、Play 声明和正式发布版行为一并核验，不应当作普通运行时 `READ_CONTACTS` 权限。 |

这些页面解释的是 People Directory/Android 权限的技术契约，不会自动让应用满足 Play 的核心用途或声明要求。被点开的类型和 `Persons`/`Groups` 查询 builder 已入逐 URL 台账；它们各自剩余成员、版本后代、样例工程和系统端细节仍未穷尽。

2026-10-24 对照 [Capability API 参考](https://developer.android.com/reference/android/provider/PeopleContract.Capability)、其 `Persons.CAPABILITY` 列和父级 `createPeopleInteractionRequest()` 方法后，已补齐三种 API 37.2 通信能力位的名称、值、组合方式，以及客户端到目录应用的安全交接约束。这些位只描述身份可达的通信类型，不代表应用获得联系人读取权限，也不构成 Google Play 的权限批准或额外政策例外。

#### 公告正文中的图像和导航链接

公告中还直接链接了一个文章题图、四张明确标作“UX not Final”的联系人编辑器示意图、作者档案及 `#Android` 主题目录。它们可帮助辨认用户流程，但图片稿不是最终系统承诺，也不是政策要求。作者档案只列两篇文章，其中 Contact Picker 文章已在本专题单独覆盖；主题目录混有无关 Android 新闻。作者头像链接在 2026-10-23 返回 Cache miss。

| 直接链接资产/导航 | 审阅记录 |
| --- | --- |
| [文章题图](https://developer.android.com/static/blog/assets/1009_ABL_142_A_more_reliable_way_to_add_and_edit_contacts_on_Android_Strapi_b510ec4fc0_ZXfljU.webp) | 作为图片资源目标已尝试打开；只记录其为公告配图，不从无法读取的图像提取政策。 |
| [新建联系人半屏示意图](https://developer.android.com/static/blog/assets/Figure01_01_Quick_Insert_Half_Sheet_Prefilled_47cedd26cb_Dw4kb.webp)、[新建联系人全页示意图](https://developer.android.com/static/blog/assets/Figure01_02_Full_Page_Editor_Default_Top_35707ebba8_4OBIj.webp) | 公告标为尚未定稿；说明 Intent 可预填资料并由用户核对，不构成未来 UI 的保证。 |
| [添加到已有联系人的半屏示意图](https://developer.android.com/static/blog/assets/Figure02_01_Add_To_Existing_0_Search_State_Half_Sheet_7543788ec9_Z1HMcPH.webp)、[编辑已有联系人全页示意图](https://developer.android.com/static/blog/assets/Figure02_02_Edit_Existing_Contact_Prefilled_Full_Page_7e796e7fb5_ZYSROB.webp) | 公告标为尚未定稿；只是交互模型图，无额外权限或 Play 审核规则。 |
| [作者档案](https://developer.android.com/blog/authors/roxanna-walker) 与 [`#Android` 文章目录](https://developer.android.com/blog/topics/android) | 档案页列出 Contact Picker 与 Embedded Photo Picker 两篇文章；前者已覆盖，后者与联系人写入无直接关系。主题页是动态文章目录，不是规范性政策。 |
| [作者头像资源](https://developer.android.com/static/blog/assets/roxana_02dc1d3afc_1Q1ceg.webp) | 直接尝试返回 Cache miss；仅记录访问失败，不推断资源内容。 |

#### “Modify contacts using intents”指南的直接子链接与深度边界

2026-10-23 已打开指南正文并逐项尝试其 22 个正文链接出现项：去重后涉及 Intent、Activity、ContactsContract.RawContacts、联系人提供者指南、ContactsContract.Intents.Insert、ContactsContract.Contacts、Content License 等 API/指南页面；其中 `startActivity()` 的链接目标本轮返回 Internal Error，抓取器未暴露目标 URL。相关 API 页面已打开并按 Intent 动作、URI/MIME 类型、联系人行/账户和隐私声明关系抽样核对；大型 API 类的全部成员、每个成员的后续引用和通用站点导航没有穷尽。详细状态见审计表，不据此声称技术后代递归闭合。

## Location Permissions：前台精确位置

### 一次性或会话级位置

目标 Android 17 / API 37 及以上，若功能只在某次操作中短暂需要精确位置，必须使用 Android Location Button。这类事务性场景包括“搜索附近”、一次性发当前位置、用户主动给照片/帖子添加位置、配送地址填写。

Location Button 将精确位置授权限定在当前会话，用户点击时才触发，并在会话结束后失效。系统按钮可调整颜色、轮廓、尺寸/形状及预先批准的文案，但位置图标不可定制，字号由系统管理以遵守无障碍设置。官方实现文档说明可使用 Jetpack 库；该库目前标注为实验性，实施时应复核其最新兼容状态。

实现还需要 `android.permission.USE_LOCATION_BUTTON`，供系统远程渲染 Location Button；只通过按钮访问精确位置时，给 `ACCESS_FINE_LOCATION` 使用 `onlyForLocationButton` 标志，可阻止应用改走较宽泛的常规精确权限路径。Android 16 及更低版本上，Jetpack 库会回退为本地绘制按钮并触发标准位置权限提示，因此这些版本不会呈现 Android 17 的系统会话级授权体验。

Android 文档给出的 Manifest 形态如下；若应用有其它经核准的持续定位场景，应按实际用途调整标志和权限，不能照抄按钮专用配置：

```xml
<uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />
<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION"
    android:usesPermissionFlags="onlyForLocationButton" />
<uses-permission android:name="android.permission.USE_LOCATION_BUTTON" />
```

### 粗略位置何时足够

Google Play 的最小范围帮助页列出无需精确街道级位置的设计例子：按城市展示本地新闻、活动和天气；让社区应用显示“同城”或按大致距离筛选，而不暴露实时坐标；用粗略位置查找附近门店；按国家/地区设置语言、货币或本地促销。这些例子提示先评估粗略位置是否能完成用户功能，不是对任何应用的自动豁免或审批清单。来源页还要求用户应能合理预期功能需要所申请的精度。

### `ACCESS_FINE_LOCATION` 声明与持续精确访问

Google Play 的[最小范围前台位置帮助页](https://support.google.com/googleplay/android-developer/answer/17033915?hl=en)明确要求所有申请 `ACCESS_FINE_LOCATION` 的应用完成 Play Console 声明；预计 2026 年 11 月开放，期限表目前列出的强制执行日为 2027-01-27。帮助页称届时 Console 会提供 30 天自行延期选项，实际资格应查看账号状态。FAQ 另将执行时间描述为预计在 2027 年 1 月下旬，并称时间线可能根据开发者反馈进一步明确；应将此预期与期限表的精确日期分开记录。

**Location Button 不是 `ACCESS_FINE_LOCATION` 的申报豁免。** Android [按钮实现指南](https://developer.android.com/guide/topics/permissions/private-alternatives/location-button)给出的按钮专用 Manifest 仍声明 `ACCESS_FINE_LOCATION`，并以 `onlyForLocationButton` 将它限制为只能通过按钮使用，同时声明 `USE_LOCATION_BUTTON`。该标志缩小 Android 访问路径；现行 Play 帮助页没有说明它可以免除 Play Console 声明。上线前应按实际 Manifest 和 Console 表单核验，不要把会话级授权误读成无权限/无申报路径。

声明应精确对应面向用户的功能。常规或持续精确访问须解释为什么粗略位置和 Location Button 均不足，以及该访问为何是商品详情所宣传核心功能的必要部分。页面列举搜索附近、一次性分享、实时追踪、用户/自动位置标签、个性化、导航、区域触发、附近设备、浏览器位置和网络诊断等场景；这些类别不是自动批准名单。

持续精确位置仅在其对商品详情宣传的核心功能不可或缺时才可能合理。不得仅为广告或分析申请位置权限，且不得出售设备位置数据。若应用在用户看不到时访问位置，属于后台位置范畴，应另外核对[后台位置政策](https://support.google.com/googleplay/android-developer/answer/9799150?hl=zh-CN)和相关声明；Location Button 不会替代后台位置审核。

## 发布前核对清单

1. 从 manifest、依赖 SDK、代码调用和运行时流程列出 `READ_CONTACTS`、`ACCESS_FINE_LOCATION` 及实际访问点。
2. 为每个访问点写清楚对应商品详情中的核心功能、触发时机、数据字段、留存和接收方。
3. 联系人：先证明 Picker 不足，再判断是否需要完整联系人访问；如果需要，准备 Play Console 声明材料和数据主体授权流程。
4. 位置：先区分粗略/精确、一次性/持续、前台/后台；一次性会话精确位置改用 Location Button；持续精确位置准备技术理由和声明。
5. 设计权限被拒绝、撤回或暂时不可用时的合理替代路径，不施压用户授权。
6. 同步更新隐私政策、Data safety、应用内显著披露和 SDK 供应商核对结果。
7. 在 2026 年 11 月和 2027-01-27 前再次查看政策截止日期及 Console 表单，因为预览页、申报字段和执行状态可能变更。

## 来源与关联

- [敏感权限政策预览：Contacts Permissions / Location Permissions](https://support.google.com/googleplay/android-developer/answer/16909972?hl=en)
- [Understanding Restricted Permissions with minimum scope alternatives](https://support.google.com/googleplay/android-developer/answer/16935362?hl=en)：同时说明联系人、照片和视频权限及 Console 时间线；当前正文和所列相关帮助主题已登记在递归链接图（快照：`../google-play-policy-link-graph.md`，未导入本仓库）。
- [前台位置与 Location Button 政策帮助](https://support.google.com/googleplay/android-developer/answer/17033915?hl=en)
- [Android Contact Picker：API 与最佳实践](https://developer.android.com/about/versions/17/features/contact-picker)
- [Android Location Button：用户流程与实现](https://developer.android.com/guide/topics/permissions/private-alternatives/location-button)
- [Google Play Policy Deadlines](https://support.google.com/googleplay/android-developer/table/12921780?hl=en)
- 项目内关联：[敏感权限与 API](../sensitive-permissions/sensitive-permissions.zh-CN.md)、[权限声明与审核](../permissions-declaration/permissions-declaration.zh-CN.md)、[User Data](../user-data/user-data.zh-CN.md)、[后台位置政策](https://support.google.com/googleplay/android-developer/answer/9799150?hl=zh-CN)。

## 时间线：预审检查、申报提示和政策生效

2026-04-15 的 [Google Play 政策更新博客](https://developer.android.com/blog/posts/boosting-user-privacy-and-business-protection-with-updated-play-policies)是实施准备说明，不取代正式政策。旧 Android Developers Blogger 链接仍返回 HTTP 429；当前 Android Developers 同名、同日文章可读取，但本次未观察到旧 URL 的重定向。博客同时提到 Contact Picker/Sharesheet、Location Button、Play Console 权限声明以及新的预审检查；这些是不同流程，不能把预审检查的计划日期当成申报表开放日。

| 事项 | 当前官方页面所述时间 | 应如何解读 |
| --- | --- | --- |
| `READ_CONTACTS` 声明提示 | [最小范围权限帮助页](https://support.google.com/googleplay/android-developer/answer/16935362?hl=en)称 Play Console 自 **2026 年 9 月**开始提示含该权限的开发者提交声明或移除权限。 | 这是联系人声明提示；实际应用是否收到提示仍须在账号中核实。联系人政策对 Android 17/API 37+ 应用的强制生效日为 2027-01-27。 |
| 联系人申报的操作提醒 | Play 官方开发者社区 2026-10-05 的[合规提醒](https://support.google.com/googleplay/android-developer/thread/471472559/mandatory-steps-for-contacts-permissions-policy-compliance-by-january-27-2027?hl=en-GB)称联系人声明现已开放，并列出申报、申请 30 天自动自行延期，或删除 `READ_CONTACTS` 并改用 Contact Picker 三种操作。 | 目标为 Android 17/API 37+ 且带 `READ_CONTACTS` 的应用须在 2027-01-27 前完成处理。提醒给出的 Console 路径为 Monitor and improve → Policy and programs → App content → Contacts Permission；移除权限时应检查本次提交中的所有版本代码，包括生产和测试轨道。社区帖是操作提醒；适用范围和日期仍以正式帮助页及期限表为准。该帖直开正文未能读取，细节来自官方搜索索引摘录，目标页链接及其后代尚未审计。 |
| 联系人/位置政策公告中的 10 月 28 日 | Google 官方 Play Developers Newsletter 的 2026 年 4、6、7 月版本都写：从 **2026-10-28** 起，不需要广泛联系人访问的应用必须使用 Android Contact Picker。 | 这句没有说明 API 37+ 范围，也没有解释它和专门政策预览/期限表所列 **2027-01-27** 的关系。两者均为 Google 官方来源，不能擅自把其中一个改写成另一个的生效日。对仅需偶尔或选择性访问的应用，建议尽早迁移并以 10 月 28 日作为保守的准备节点；广泛访问仍须准备声明，正式 Help 页目前列出的强制期限为 2027-01-27。此项准备建议是基于两种官方措辞的风险控制推断，不是新增政策条款；发版前核对当前 Console。 |
| `ACCESS_FINE_LOCATION` 声明 | [前台位置政策帮助页](https://support.google.com/googleplay/android-developer/answer/17033915?hl=en)目前称精确位置声明预计于 **2026 年 11 月**开放。 | 这是位置权限申报表单，不等于预审检查。政策计划于 2027-01-27 强制执行；资格和可用的 30 天自行延期须看 Console。 |
| 联系人/位置预审检查 | 4 月博客称新的 Play Console 预审检查计划从 **2026-10-27** 开始提供。2026-10-23 重开通用[预审检查帮助页](https://support.google.com/googleplay/android-developer/answer/14807773?hl=en)：检查在有未送审变更时自动运行，关键问题须先解决，部分其他问题可选择继续；通过预检不保证通过正式审核。帮助页没有列举或确认联系人/位置专属检查。 | 10 月 27 日是工具计划上线日，不是政策生效/申报截止日。通用流程说明不能证明专属检查已上线；截至 2026-10-23，计划日期尚未来到，且未读取账号内 Console 状态。应在 10 月 27 日后由开发者账号实查。 |

博客较早写称联系人和位置声明表单将在“10 月前”开放。现行联系人帮助页已称联系人声明提示自 9 月开始；现行精确位置帮助页仍称位置表单预计 11 月。2026-10-24 另行打开 [Android Developers 的 Google Play 政策期限页](https://developer.android.com/distribute/play-policies)：当前日期清单也把联系人、位置、短信/通话记录和前台服务地理围栏变化列在 **2027-01-27**，并链接到政策与 Contact Picker 资料；它与 Play Help 期限表一致，但没有解释 Newsletter 所写 10 月 28 日。位置表单时间存在公告与现行帮助页之间的表述差异，按现行帮助页准备，并以账号实际 Console 状态为准。这里的 **10 月 27 日是独立的预审检查计划日期**，不能用来消解或替代表单时间差异。

### 2026-10-05 联系人合规提醒：直接子链核对

Google 官方搜索索引本轮显示了该社区提醒的完整正文，但网页直开仍只返回 Help Center 外壳，没有暴露正文里的实际 URL、链接锚点或链接总数。因此下表将正文语义所指向的帮助页作为“已核对的相关目标”，不声称已验证它们就是原帖的每一条直接链接。

| 提醒正文所指向的页面/流程 | 页面内容及与提醒的关系 | 读取与边界 |
| --- | --- | --- |
| [Request more time to complete a policy declaration](https://support.google.com/googleplay/android-developer/answer/15644220?hl=en) | 说明如何从 Play Console 的 App content 找到声明、选择 Request additional time、选择原因并提交；获批后会在声明 Timeline 显示新期限和 `Extension granted`。并非所有政策都能延期；各政策有固定时长，已完成或不在适用范围的声明通常不会提供该选项。 | 本轮重新打开全文。联系人政策的 30 天时长来自联系人专项 Help 页；通用延期页只说明具体政策决定时长。App content 需登录帐号；相关的 [Prepare your app for review](https://support.google.com/googleplay/android-developer/answer/9859455) 已另行审阅。 |
| [Understanding Restricted Permissions with minimum scope alternatives](https://support.google.com/googleplay/android-developer/answer/16935362?hl=en) | 正式说明目标 API 37+ 的 `READ_CONTACTS` 规则、申报用例和技术理由、2026 年 9 月 Console 提示，以及 2027-01-27 强制期限和 30 天自行延期。 | 正文已打开；这是范围、资格和期限的主要 Help 来源。 |
| [Android Contact Picker](https://developer.android.com/about/versions/17/features/contact-picker) | 说明用 `ACTION_PICK_CONTACTS` 让用户选择要分享的联系人和字段；Session URI 只授予对用户所选数据的临时读取权限。最佳实践包括只请求必要字段、按 `LOOKUP_KEY` 合并同一联系人的多项数据、及时保存后续仍需使用的已选数据，以及不依赖账户元数据。 | 2026-10-24 打开并核对。Android 实施指南，不是 `READ_CONTACTS` 资格豁免。 |
| Play Console 的 Contacts Permission 声明页 | 社区提醒给出 Monitor and improve → Policy and programs → App content → Contacts Permission，以及保存/送审后到 Publishing overview 发布的路径。 | 帐号内路径来自官方搜索索引；登录后页面、具体声明字段和该账号的延期状态不能公开核验。 |

### 延期流程帮助页的正文子链接

2026-10-24 重新打开[延期流程帮助页](https://support.google.com/googleplay/android-developer/answer/15644220?hl=en)，并跟随可见正文链接。此页说明的是通用声明延期流程，不能单独证明某应用符合联系人权限资格。

| 延期页子链接 | 目标页与状态 |
| --- | --- |
| [Play Console App content](https://play.google.com/console/developers/app/app-content/overview) | 点击后跳转至 Google 帐号登录；声明与提交状态按开发者帐号显示，无法匿名核验。 |
| [Prepare your app for review](https://support.google.com/googleplay/android-developer/answer/9859455) | 已打开并纳入[应用审核准备](../app-review-preparation/app-review-preparation.zh-CN.md)。该页解释 App content 用于提交隐私政策、广告、登录说明、权限声明、目标受众、内容分级等资料，并区分 `Needs attention` 与 `Actioned` 两个声明标签。 |
| [Google Play Developer Help Community](https://support.google.com/googleplay/android-developer/community?help_center_link=CLzsugcSMlJlcXVlc3QgbW9yZSB0aW1lIHRvIGNvbXBsZXRlIGEgcG9saWN5IGRlY2xhcmF0aW9u&hl=en) | 点击返回 Cache miss；没有读取到讨论正文。社区入口不是正式权限规则来源。 |
| [Contact us](https://support.google.com/googleplay/android-developer/gethelp) | 点击后跳转/重定向到帐户登录门槛；无公开帮助正文。没有提交支持请求。 |
| [延期步骤截图一](https://lh3.googleusercontent.com/l8AyzHZdpBYBUMJXKkPcAMaFuw0nJAih2wFU6qF8PrVA2nSap1U4wN-mMNrxLaWZTMk%3Dw895) · [截图二](https://lh3.googleusercontent.com/MrAtdGaOOfr9oKysrQfaGjArfbiXL6n6Mbz7h4EWEBCt553Rw1Vv4GNIl0FE4CrUSTei%3Dw895) | 两个图片目标已点开到 Googleusercontent 地址，但工具未返回可读像素；按页面上下文是 Play Console 操作示意图，不把图像内容推断为政策条款。 |

延期页还有独立的帮助中心侧边栏导航，已在逐 URL 审计中单独计数；侧边栏目标不改变联系人权限条件。

**递归状态：** 上述政策、延期流程和 Picker 指南页面均有独立正文摘要，延期流程页的 App content/Prepare for review 相关目标亦已登记。社区提醒原帖的链接 URL 及精确锚点仍未从可读取页面中取得；原帖后代的直接父子关系尚未闭合。逐 URL 状态见来源审计表（快照：`../source-page-audit.csv`，未导入本仓库）及递归链接图 §4.133（快照：`../google-play-policy-link-graph.md`，未导入本仓库）。


Android 官方 [Android 17 Location Privacy 博客](https://android-developers.googleblog.com/2026/03/location-privacy.html)补充了实现背景：Location Button 让用户在动作发生时授予会话级位置访问，Jetpack 库在 Android 16 及以下回退到标准定位提示；按钮外观可以有限定制，但位置图标保持系统可识别、字号受系统无障碍设置控制。Android 17 还增加持续位置访问提示、最近访问应用与权限控制入口，粗略位置精度按人口密度调整，定位运行时对话框更清楚地区分精确/大致位置。这些平台行为和 UI 是技术背景，不改变 Play 的必要性、声明或审核要求。

| 公告关联页面 | 本专题提取内容与访问状态 |
| --- | --- |
| [Android Developers Blog: Redefining Location Privacy](https://android-developers.googleblog.com/2026/03/location-privacy.html) | 正文已打开；已整理 Location Button、Android 16 及以下回退、位置使用指示器、人口密度感知粗略位置和新版精确/大致定位对话框。技术功能在原文发布时为 Android 17 Beta 3 可测试；实际版本状态应查看当前 Android 文档。 |
| [Android Developers Blog: Contact Picker privacy-first contact access](https://android-developers.googleblog.com/2026/03/contact-picker-privacy-first-contact.html) | 2026-10-23 已重开完整正文。`ACTION_PICK_CONTACTS` 可限定字段、单/多选和数量；返回 Session URI 只提供临时读取权限，应用应尽快持久化用户选择的数据。Android 17 会把带联系人数据类型的旧 `ACTION_PICK` 升级到新界面；要使用多选/字段等完整能力应显式迁移。其唯一实质正文子链接是[完整 Contact Picker 指南](https://developer.android.com/about/versions/17/features/contact-picker)，已另行打开并核对示例、API 与最佳实践。此博客是 Android 实现建议，不决定 Play 对广泛联系人访问的资格。 |

### Contact Picker 实现页的直接子链接

Android 17 Contact Picker 指南最后更新于 2026-10-16。正文三处示例链接都指向同一份固定版官方 `ContactPickerActivity.kt`。2026-10-23 通过 GitHub 文件页成功读取精确 `e72c9d1f…` 提交；此前 raw 镜像缓存未命中不再代表目标正文未读。页面另链接 Android 内容许可说明。代码样例用于实现，不能替代 Play 对访问必要性的判定。

| 实现页子链接 | 内容与核验状态 |
| --- | --- |
| [Android snippets: ContactPickerActivity.kt（固定 e72 提交）](https://github.com/android/snippets/blob/e72c9d1fdc9658b16537b8b137ba517e229b02ab/contacts/src/main/java/com/example/contacts/ContactPickerActivity.kt) | 指南正文三处重复链接的唯一目标。2026-10-23 从官方 GitHub 文件页读取精确提交（288 行、265 行代码）：`EXTRA_USE_SYSTEM_CONTACTS_PICKER=true`；单选示例只请求 email/phone 字段；多选设 5 人上限并令 match-all 为 false；电话专用流程只请求电话 MIME 类型；成功时只查询返回的 Session URI，在 IO dispatcher 读取 `LOOKUP_KEY`、显示名、MIME 类型与 `DATA1` 并合并同一联系人的多行；不传自定义 selection 参数；捕获 `ActivityNotFoundException` 并提示 Picker 不可用。文件头声明 Apache 2.0。该代码文件不说明应用 Manifest 或 Play 声明。 |
| [Android snippets: ContactPickerActivity.kt（main 分支补充，非正文直链）](https://github.com/android/snippets/blob/main/contacts/src/main/java/com/example/contacts/ContactPickerActivity.kt) | 可变分支文件作为单独比较来源保留；目前已直接核实固定 e72 提交，因而不再用 `main` 推断固定版内容。该行不是 Android Contact Picker 指南正文的直接链接。 |
| [Android Developers Content License](https://developer.android.com/license) | 页面许可说明已打开；代码样例受 Android Developers 内容许可约束。此链接不是 Play 政策要求。 |

### Contact Picker API 参考交叉核对

实现指南提到 `ContactsPickerSessionContract.ACTION_PICK_CONTACTS`，但正文抽取结果没有把该类显示为可点击链接；因此以下 API 参考作为相关技术交叉核对，不计作实现指南正文的直接子链接。该参考及其 `Session` 子页提供具体的 API 37 接口与 URI 授权语义：

| 相关 API 页面 | 内容与访问状态 |
| --- | --- |
| [ContactsPickerSessionContract API reference](https://developer.android.com/reference/android/provider/ContactsPickerSessionContract) | API 37 参考页相关成员已打开；页面最后更新 2026-08-03。必须提供允许的请求字段 MIME 列表；默认只需匹配任一字段，设置 match-all 才要求全匹配。默认单选；选择上限默认 50、最高 100；不支持的 MIME 类型会抛 `IllegalArgumentException`。该大型 API 页仍有其他成员未逐项核对。 |
| [ContactsPickerSessionContract.Session](https://developer.android.com/reference/android/provider/ContactsPickerSessionContract.Session) | 此前直接抓取超时；2026-10-22 已通过官方 API 正文复核相关段落。每个 Session URI 指向一次用户选择，仅发起该次选择的应用可凭返回 URI 读取用户所选字段，授权由 `FLAG_GRANT_READ_URI_PERMISSION` 限定；可投影 `ContactsContract.Data` 列。不能直接查询基础 `Session.CONTENT_URI`，应查询 Picker 返回的唯一 session URI。传入自定义 `selection` 或 `selectionArgs` 会抛 `UnsupportedOperationException`。其余成员仍未逐项核对。 |

这强化了最小权限结论：Picker 把联系人选择动作与字段范围交给用户；若只需选联系人发短信，申请 `READ_CONTACTS` 会扩大读取范围，且超出该交互所需。该技术 API 不改变 Play 对核心功能必要性、豁免类别和 Console 声明的判断。

实施要点：只请求功能需要的数据字段；要发送短信时只请求电话号码字段；同一联系人有多个号码/邮箱时用 `LOOKUP_KEY` 分组并让用户选择具体条目；Session URI 的读取权限是临时的，进程结束后仍需使用的数据应在授权期间妥善保存；不要依赖结果中被移除的账号元数据。Android 17 目标应用的旧 `ACTION_PICK` 会自动升级为新 Picker UI；若需要多字段、单 URI 或个人/工作资料切换等能力，应迁移到新的 session contract/intent extras。Session URI 不支持自定义 `selection`/`selectionArgs`。

### Sharesheet 与安全文件分享：Android 实现子链（不是 Play 政策）

4 月 15 日博客正文的精确 [Sharesheet 旧链接](https://developer.android.com/develop/ui/views/components/share)于 2026-10-23 再次返回 Internal Error。通过 Android 官方文档搜索另行打开了现行的 [Send data to other apps 指南](https://developer.android.com/develop/ui/compose/sharing/send?hl=en)，页面标注最后更新于 2026-10-19；没有观察到旧链接跳转到此页，因此两者只记录为“博客链接不可读、现行相关指南独立找到”，不宣称它们是同一 URL 或已验证重定向。

对现行指南正文可见的 58 个链接引用（含同页锚点、插图、API、代码样例和文档许可）逐项尝试。API 参考大多可打开，但因页面很长只抽查相关成员；`FileProvider` API 的该次点击和 `ShareBroadcastReceiver.kt` 样例点击返回 Internal Error，后者没有暴露目标 URL。各链接及访问状态已登记在递归图与逐 URL 台账。

| Android 指南与子页 | 已核实的实现建议及边界 |
| --- | --- |
| [Send data to other apps](https://developer.android.com/develop/ui/compose/sharing/send?hl=en) | 面向向应用外或其他用户发送内容时使用系统 Sharesheet：以 `ACTION_SEND`、准确 MIME 类型及内容 URI 构造 Intent，再调用 `Intent.createChooser()`。对于定义明确的应用间任务，才用 Intent Resolver；分享时不要自建一套目标列表或自定义 Sharesheet。多项内容使用 `ACTION_SEND_MULTIPLE`；混合多种媒体会让接收者难以判断内容。 |
| [Photo Picker](https://developer.android.com/training/data-storage/shared/photo-picker?hl=en) | 这是用户从媒体库向本应用导入照片/视频时的系统选择器，不是把内容发送给他人的 Sharesheet。系统只向应用开放用户选中的 URI，替代读取整个媒体库；长时间后台上传时才考虑持久化 URI 读取授权。指南 2026-10-16 更新；Android 13+ HDR 转码是显式选择功能，需注意耗时、缓存及一分钟视频限制。 |
| [Restrict interactions with other apps](https://developer.android.com/training/permissions/restrict-interactions?hl=en) 与 [Sharing files](https://developer.android.com/training/secure-file-sharing?hl=en) | 对外分享文件优先使用 `content://` URI、`FileProvider` 和按 URI 授予的临时读取权限；避免 `file://` / `Uri.fromFile()`。FileProvider 的 Manifest 示例将 Provider 设为 `android:exported="false"`、启用 `grantUriPermissions`，并只列出确需分享的目录。不要把 MediaStore 当作私有文件通道：写入系统 MediaStore 的内容可被设备上的其他应用访问。 |
| [Setting up file sharing](https://developer.android.com/training/secure-file-sharing/setup-sharing?hl=en)、[Sharing a file](https://developer.android.com/training/secure-file-sharing/share-file?hl=en)、[Requesting a shared file](https://developer.android.com/training/secure-file-sharing/request-file?hl=en)、[Retrieving file information](https://developer.android.com/training/secure-file-sharing/retrieve-info?hl=en) | 四个文件分享教程正文均已打开。发送端用 `FileProvider` 仅为配置路径生成 URI，并在结果 Intent 上授予临时读取权限；不要依赖长期或宽泛授权。接收端只按用途读取，校验收到的 URI 不会通过路径穿越越出允许目录；用 `ContentResolver` 读取 MIME 类型/文件元数据。教程更新日期为 2025-02-10；其中旧式 `startActivityForResult()` 示例是平台教程快照，接入新项目时应核对当前 Activity Result API。 |
| [Provide Direct Share targets](https://developer.android.com/develop/ui/compose/sharing/direct-share-targets?hl=en) | Direct Share 是接收应用向 Sharesheet 提供可直达会话/联系人等具体操作的快捷目标。Android 11/API 30 起应使用 Sharing Shortcuts；避免陈旧或不相关目标（示例将 30 天无活动对话视为过期），联系人删除后移除长期快捷方式，MIME 类别应与目标实际能力匹配，点击后直接进入对应操作而非再显示无关选择页。指南称快捷方式数据保存在设备加密分区，并仅对系统服务和发布它的应用开放。 |
| [Receive data from other apps](https://developer.android.com/develop/ui/compose/sharing/receive?hl=en) 与 [Intents and intent filters](https://developer.android.com/guide/components/intents-filters?hl=en) | 接收端要在 Manifest 声明实际支持的 Action/MIME 类型，将 Intent 路由到对应界面，并提取 `EXTRA_TEXT`/`EXTRA_STREAM`。Android 接收指南建议在使用用户分享的文本前先让用户确认或编辑；不要用 `*/*` 接收器却无法处理所有内容。 |
| Sharesheet API 参考与代码样例 | 正文所链的 `Intent`、`Uri`、`ContentProvider`、`FileProvider`、`MediaStore`、`MediaScannerConnection`、`ContentResolver`、`MimeTypeMap`、`DocumentFile`、`ChooserAction`、`ChooserTarget`、`ShortcutManagerCompat` 等参考页已逐项尝试；大型 API 的成员树仍部分覆盖。Android `snippets` 固定提交中的 Sharesheet 示例页可读；`platform-samples` 分享示例目录可读，但其全部源码与深层成员未逐一核对。内容许可已打开。 |

**Play 政策关系：** 以上是 Android 平台实现和最小授权建议，不是 Play 对联系人、媒体或文件权限的批准。Sharesheet 选择回调可返回接收应用的 `ComponentName`；若产品将该接收方记录、发送到服务器或用于画像，应单独评估 User Data、Data safety、显著披露/同意、用途限制和保存期限。Contact Picker 负责从用户联系人中选择数据；Sharesheet 负责把应用已有内容交给用户选择的目标，两者不可互相替代。

## 前台位置页的直接子链接与状态

| 来源链接 | 关系与核验状态 |
| --- | --- |
| [Understanding location in the background](https://support.google.com/googleplay/android-developer/answer/9799150?hl=en) | 正文已打开并有[后台位置专题](../background-location/background-location.zh-CN.md)；只在核心功能有显著用户价值时才可申请，需提供一项关键功能、声明、视频、应用内披露和隐私政策。其表单、视频和违规处理后代未完全递归。 |
| [Declare permissions for your app](https://support.google.com/googleplay/android-developer/answer/9214102?hl=en) | 正文已打开并有[权限声明专题](../permissions-declaration/permissions-declaration.zh-CN.md)；未声明权限可能阻止所有商店资料/应用变更，审查可能持续数周；已记录 API 用户需先走 Play Console 网页流程。 |
| [Android Location Button implementation](https://developer.android.com/guide/topics/permissions/private-alternatives/location-button) | 正文已打开，页面于 2026-09-08 更新。已纳入 `USE_LOCATION_BUTTON`、`onlyForLocationButton`、实验性 Jetpack 库及 Android 16 及以下的回退行为；发行记录和官方 Manifest/Compose 样例已打开。API 参考超过读取上限、Issue Tracker 缓存未命中；其他技术后代仍未穷尽。 |
| [Android 17 Location Button design guidelines](https://developer.android.com/about/versions/17/features/location-button) | 这是前台位置政策正文直接给出的设计指南链接。2026-10-23 再次用官方网页搜索并直开精确 URL，目标仍无法访问；搜索结果只指向另外的实现指南和 Java API 参考。它们的样式/尺寸约束已按各自来源另行摘要，但不能据此认定本设计页已读取或内容等同。 |
| [Android：Request location permissions](https://developer.android.com/develop/sensors-and-location/location/permissions) | 正文于 2026-10-22 打开，Android 文档标注 2026-10-16 更新：区分前台/后台与精确/粗略授权；列出 FGS 中的位置访问、用户只需单次位置时使用 Location Button，并明确目标 Android 17/API 37+ 且仅含会话级位置功能的应用须使用 Location Button。此处是实现指南，Play 的必要性、声明和审核仍依政策页；代码、精度和 API 后代未穷举。 |
| [Build location-aware apps 旧地址](https://developer.android.com/training/location) → [现行位置开发总览](https://developer.android.com/develop/sensors-and-location/location) | 旧地址跳转至现行页面并已打开；入口链接到位置权限、Fused Location Provider、电量优化、Maps、代码实验和样例。这里只记录入口页与导航关系，Android 技术后代没有全量递归。 |
| [Android permissions overview 旧地址](https://developer.android.com/training/basics/permissions) → [现行 Android permissions overview](https://developer.android.com/guide/topics/permissions/overview) | 旧地址跳转至现行页面并已打开；涵盖 Android 权限声明、运行时请求和用户选择的一般流程。具体 API 示例及版本分支未全量递归。 |
| [Access location in the background](https://support.google.com/googleplay/android-developer/answer/9799150?hl=en)、[敏感权限政策旧地址](https://support.google.com/googleplay/android-developer/answer/9888170) → [现行合并政策](https://support.google.com/googleplay/android-developer/answer/16558241?hl=en#location-permissions)、[Foreground Services policy](https://support.google.com/googleplay/android-developer/answer/16559646?hl=en) | 后台位置和现行合并政策正文已打开并在对应专题中关联；旧敏感权限地址已确认跳转到现行页。本轮从前台位置页点击 FGS 政策返回 HTTP 500，但该现行规范目标已有独立正文审计。后台位置、位置前台服务与会话级前台精确位置是不同审查路径；Location Button 不替代后台位置申报。 |
| [Android privacy checklist 旧地址](https://developer.android.com/privacy/best-practices) → [现行 Android privacy checklist](https://developer.android.com/privacy-and-security/about)、[User Data 原始地址](https://support.google.com/googleplay/android-developer/answer/9888076) → [现行 User Data policy](https://support.google.com/googleplay/android-developer/answer/10144311?hl=en) | 两组旧链接均重定向并规范化到现行正文；技术隐私清单与 Play 数据处理政策补充位置用途、披露、SDK 共享和安全义务。 |
| [Play Console location declaration](https://support.google.com/googleplay/android-developer/answer/17033915?hl=en) | 正文指出 2026 年 11 月预计开放，2027-01-27 生效并提供 30 天自行延期。此类 Console 声明和延期状态须登录后按账号验证。 |
| [Play Academy：Declare your use of device location data](https://playacademy.exceedlms.com/student/path/64266/activity/88785) | 公开课程页显示 2023-04-11 发布、11 分钟、中级；介绍 Google Play 如何结合应用功能与商店资料核验位置用途及政策合规，并提示需登录才能启动课程。正文课件不可见，不能据此推断额外规则。 |
| [Play Academy：Understand Google Play's location permissions policies](https://playacademy.exceedlms.com/student/path/64266) | 已解析并打开公开学习路径。介绍其课程帮助开发者遵守位置政策、最小化权限并正确回应申报；列出 4 门课：位置数据最小化（10 分钟）、位置数据申报（11 分钟）、后台位置审核（4 分钟）、已申报权限与应用内披露（2 分钟）。四个课页均已尝试：申报课的公开简介可读（2023-04-11 发布、中级，说明审核会结合应用功能和商店详情），其余三页返回 Cache miss；课程启动/课件须登录。属于培训材料，不新增政策条款。 |
| Play Academy 相关课程：[Minimize your use of location data to protect user privacy](https://playacademy.exceedlms.com/student/path/64266/activity/85882) | 课程页点击返回缓存未命中；只登记标题与关联关系，不推断课件内容。 |
| Play Academy 相关课程：[Understand the location background permissions review process](https://playacademy.exceedlms.com/student/path/64266/activity/1157005) | 课程页点击返回缓存未命中；后台定位审核要求以正式政策页及[后台位置专题](../background-location/background-location.zh-CN.md)为准。 |
| Play Academy 相关课程：[Declared permissions and in-app disclosures](https://playacademy.exceedlms.com/student/path/64266/activity/89576) | 课程页点击返回缓存未命中；权限声明和应用内披露要求以正式政策页为准。 |

英文前台位置帮助页正文包含 19 次链接出现、15 个不同的链接目标引用（按页面链接 ID 统计；重定向后的规范目标另行合并）。本轮重开正文并核对了目标页及对应专题；Android 17 design-guideline 目标经 Android Developers 直接访问和网页链接均仍不可读。此前未解析的 Academy 入口现已定位到上方学习路径，四门课均已尝试，其中三门 Cache miss、课件需登录。Help Community / Contact 是支持控件，没有作为政策内容链接扩展。当前页的 12 项权限帮助导航另行核对并映射到现有专题/来源记录，不与正文链接混计；这些导航目标自己的深层后代仍部分待核。课程及其相关课程不替代正式政策，也不代表课程正文已收录。

### Location Button 实现页的直接子链接与最佳实践

2026-10-22 继续沿 Android Location Button 实现指南检查到 Jetpack 发布记录、Android 官方代码样例、依赖配置、API 参考和 Issue Tracker。它们解释如何落地按钮，不会改变 Play 对权限必要性、Console 声明或审核的要求。

| 实现页子链接 | 内容与核验状态 |
| --- | --- |
| [Core Locationbutton release notes](https://developer.android.com/jetpack/androidx/releases/core-locationbutton) | 正文已打开：截至页面显示的 2026-06-17 更新，列出 `1.0.0-alpha01`，包括 View、Compose 和 testing 工件；发布说明称 Android 16/API 36 及以下会回退到标准定位权限提示。页面未列出 stable、RC 或 beta 版本。使用前应回查现行版本和兼容要求。 |
| [LocationButton AndroidManifest.xml sample](https://github.com/android/snippets/blob/334a3fd83e91998063db65445f8528c9a8dacdf1/misc/src/main/java/com/example/snippets/location/AndroidManifest.xml) | 官方 Android snippets 文件已打开。示例声明 coarse/fine 位置权限及 `USE_LOCATION_BUTTON`；仅由按钮取得精确位置时，可把 `onlyForLocationButton` 加到 `ACCESS_FINE_LOCATION`，限制应用绕过按钮走宽泛精确定位权限。 |
| [LocationButton.kt Compose sample](https://github.com/android/snippets/blob/334a3fd83e91998063db65445f8528c9a8dacdf1/misc/src/main/java/com/example/snippets/location/LocationButton.kt) | 官方代码文件已打开。示例在用户点击系统信任的按钮并作出权限选择后分别处理获准/拒绝回调；按钮可有限调整颜色、轮廓、形状和系统提供的文字，位置图标与系统管理的字体大小不可自定义。 |
| [AndroidX Locationbutton API reference](https://developer.android.com/reference/kotlin/androidx/core/locationbutton/package-summary) | 已尝试打开；文档响应超过读取器大小限制（4 MiB），无法检查 API 成员。实现细节不从截断响应推断。 |
| [Add build dependencies](https://developer.android.com/build/dependencies) | 已打开。通用 Android 构建指南建议依赖校验、固定版本并避免动态版本号；它不是 Play 权限规则。 |
| [Locationbutton issue tracker](https://issuetracker.google.com/components/2162367) | 已点击，返回缓存未命中；不推断具体缺陷或支持状态。 |

#### 可读取的 AndroidX Java API 页面与直接成员链接

2026-10-23 另行打开官方 [AndroidX Location Button Java package summary](https://developer.android.com/reference/androidx/core/locationbutton/package-summary)，页面标注 2026-06-24 更新。它是上表 Kotlin 路径之外的另一个 URL；本轮没有观察到两者之间的重定向，因此新页面可读不代表旧 URL 已恢复。API 正文说明：Android 17/API 37+ 的按钮通过 `SurfaceView` 显示远程 SystemUI 组件；Android 16/API 36 及以下使用本地按钮并触发标准权限对话框。XML `LocationButton` 不支持子 View；padding 会限制在 4–8 dp；宽和高至少 48 dp，否则禁用点击，高度最多 136 dp；建议对比度至少 4.5:1。按钮必须完整无遮挡：覆盖其上的视图会触发防 tapjacking 保护并让点击被系统静默丢弃。API 示例还要求 Android 16 及以下由 Activity/Fragment 手动处理标准权限回调，并可处理获准/拒绝与远程会话错误。这些是 Android 实现约束，不改变 Play 对“是否有资格请求权限”的判定。

| package summary 中的直接 API 链接 | 阅读结果与关系 |
| --- | --- |
| [OnErrorListener](https://developer.android.com/reference/androidx/core/locationbutton/OnErrorListener) | 已打开；API 37+ 建立或维持远程会话发生严重错误时回调，并携带底层 `Throwable`。 |
| [Build.VERSION_CODES.CINNAMON_BUN](https://developer.android.com/reference/android/os/Build.VERSION_CODES.html#CINNAMON_BUN) | 已打开；常量对应 API 37，与 Android 17 Location Button 的平台分界一致。 |
| [OnPermissionResultListener](https://developer.android.com/reference/androidx/core/locationbutton/OnPermissionResultListener) | 已打开；用户与系统按钮交互并作出选择后回调，布尔值表示是否授予精确位置权限。 |
| [OnRequestPermissionsListener](https://developer.android.com/reference/androidx/core/locationbutton/OnRequestPermissionsListener) | 直链仍返回缓存未命中，但 2026-10-23 官方搜索索引提供了该 API 页面摘录：这是 `CINNAMON_BUN` / API 37 之前的回调；`onRequestPermissions()` 可由应用自定义权限请求流程，例如请求权限或先解释用途。完整类页仍未直开。 |
| [LocationButton](https://developer.android.com/reference/androidx/core/locationbutton/LocationButton) | 直链仍失败；官方搜索索引摘录确认它是会话级精确位置按钮，API 37+ 由系统远程渲染、较低版本使用本地回退。摘录还称默认旧版权限流由库自动请求，若要接收回调，宿主 Activity 需实现 `ActivityResultRegistryOwner` 且 View 需有 `android:id`。完整 Java 类页仍未直开；参见单独的 [Kotlin 类参考](https://developer.android.com/reference/kotlin/androidx/core/locationbutton/LocationButton) 摘录。 |
| [LocationButtonCompat](https://developer.android.com/reference/androidx/core/locationbutton/LocationButtonCompat) | 已打开；`setLocationButtonProvider` 标为 `@RequiresApi(37)`，页面记载其自 `1.0.0-alpha01` 添加。 |

六个成员链接均已逐项尝试：4 个目标正文完整打开，另 2 个直链失败，但官方搜索索引为 `LocationButton` 和 `OnRequestPermissionsListener` 提供了相关页面摘录，故仅算部分读取。Java package summary 的 Android 16/API 36 及以下示例要求宿主 Activity/Fragment 手动接收标准权限回调，并展示 request code 1001；Kotlin `LocationButton` 类参考的摘录则说明默认流程由库请求权限，宿主 Activity 需实现 `ActivityResultRegistryOwner` 且 View 带 `android:id` 才能把结果传给 listener。两种官方文档呈现的旧版回调接入方式不完全一致；应按实际 AndroidX 版本复核并测试，不把其中一种表述推断为另一种的替代。Java package summary 的完整正文（页面标注 2026-06-24）还记录 XML 控件不支持子 View、padding 限制 4–8 dp、至少 48 dp 可点击尺寸、高度上限 136 dp、建议对比度 4.5:1，以及遮挡时防 tapjacking 会丢弃点击。API 通用类型、注解、源码和站点导航后代仍未全部展开；逐 URL 状态见来源台账。Android 17 [release notes](https://developer.android.com/about/versions/17/release-notes)也确认系统按钮授予当次会话精确位置且需 `USE_LOCATION_BUTTON`；[Manifest.permission 参考](https://developer.android.com/reference/android/Manifest.permission#USE_LOCATION_BUTTON)将该权限列为 API 37、`normal` protection level。平台元数据与 Play Console 声明/审查要求是两层不同判断。

### Android 官方指南复核：Location Button 适用场景与设计限制

2026-10-22 重开 Android Developers 的[使用位置按钮申请会话级位置访问](https://developer.android.com/guide/topics/permissions/private-alternatives/location-button)；页面标注更新于 2026-09-08。它建议将按钮用于用户主动触发、只需会话级精确位置的任务，例如附近搜索、一次性位置分享、签到/位置标签和地址自动填充。对于目标 Android 17/API 37+ 且所有位置功能只需会话级访问的应用，按钮是 Play 政策要求。

页面允许有限样式调整（背景/图标颜色、轮廓、尺寸、形状和预设文案）；位置图标必须保留，不能自定义，字体大小由系统管理以支持无障碍。Manifest 需按功能声明 coarse/fine 权限和 `USE_LOCATION_BUTTON`；若所有精确位置都只经按钮取得，可用 `onlyForLocationButton` 限制宽泛的精确位置路径。Jetpack 库仍属实验性；当前发布页只列出 `1.0.0-alpha01`，Android 16/API 36 及以下回退到标准位置权限提示。上线前应重查库版本和状态。

该指南的正文链接及发布说明后代（包括抓取失败的图片和文档导航）见递归链接图（快照：`../google-play-policy-link-graph.md`，未导入本仓库）第 4.51 节。相邻 Android 页面[解释敏感信息访问](https://developer.android.com/training/permissions/explaining-access)属于工程指导：在用户触发功能时申请位置、先获前台授权再申请后台位置，并在适当位置提供访问理由；它不替代 Play 声明或政策审核。Android 的[应用权限最佳实践](https://developer.android.com/training/permissions/usage-notes)已覆盖最小权限、SDK 权限审查、拒绝处理和测试。

#### 实施检查

1. 只需一次定位的功能使用用户主动点击的 Location Button；目标 Android 17/API 37+ 且全部位置功能都只需会话级访问时，这是 Play 政策要求，不是可选的 UX 建议。
2. 按实际功能声明 coarse/fine 和 `USE_LOCATION_BUTTON`。如果应用只能通过按钮获得精确位置，考虑 `onlyForLocationButton`，避免同时保留不需要的宽泛精确定位通路。
3. 在 Android 17+ 验证系统按钮、授权回调和拒绝路径；在 Android 16 及以下验证 Jetpack 回退到标准权限提示后的体验。检查 alpha 库现行版本，不把页面上的旧版本号当作固定推荐。
4. Location Button 仅解决会话级前台精确位置。若功能在后台持续取位置、使用 Geofencing，或以位置前台服务持续运行，仍分别适用[后台位置](../background-location/background-location.zh-CN.md)和[前台服务/Geofencing](../foreground-services-and-geofencing/foreground-services-and-geofencing.zh-CN.md)政策及声明。

短信/通话政策预览 [answer/17225965](https://support.google.com/googleplay/android-developer/answer/17225965) 的直接目标页、替代 API 与状态见[SMS/通话权限专题](../sms-call-log/sms-call-log.zh-CN.md)和递归链接图（快照：`../google-play-policy-link-graph.md`，未导入本仓库）第 4.1 节；预览页、现行政策和 2027-01-27 生效差异均已分别登记。帮助页侧栏另有 Use of app permissions and APIs 主题 12 项导航；它们与正文直接链接分开记录，不能把侧栏数当作正文子链接数。

本页是政策结构化改写，不是政策逐字副本。作为 Android 17/API 37 新规，执行日期前应再次核对官方页面，特别是 Console 声明开放时间、30 天延期资格和 Location Button Jetpack 库的稳定性。
