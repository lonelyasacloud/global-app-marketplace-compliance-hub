---
id: google-play.sms-call-log
platform: google-play
language: zh-CN
authority: normative
status: current
kb_checked_at: 2026-10-24
review_due: 2027-01-24
regions: [global]
topics: [sms, call-log, permissions, verification, privacy, policy-declaration]
snapshot_id: play.sms-call-log
snapshot_package: "GooglePlay-KnowledgeBase-2026-10-24-review.zip"
coverage_status: "detailed-summary"
source_url: "https://support.google.com/googleplay/android-developer/answer/10208820?hl=en"
source_url_zh: "https://support.google.com/googleplay/android-developer/answer/10208820?hl=zh-CN"
effective_date: "mixed-current-and-2027-01-27"
---

# SMS 与通话记录权限

> **导入说明（Google batch 2）。** 本页正文取自 2026-10-24 Google Play 知识库快照里已经分开的中文改写（`play.sms-call-log`，核对日 2026-10-24），不是 Google 已发布中文页面的逐字文本。英文官方页面是效力来源。`kb_checked_at` 使用快照源文件记录的核对日；本次导入没有重新打开线上官方页面。文中“本知识库”“本库”“本地专题”描述的是该快照知识库的覆盖范围，不是本仓库已经导入的页面清单。快照里指向尚未导入本仓库的专题、链接图、台账或 CSV 的相对链接，已改为文字提及；指向 Google batch 1 或本批七个专题的相对链接已改到本仓库路径。快照写明简体中文同页该次无法稳定抓取，因此本中文页是基于官方英文正文的整理翻译，不是对已发布中文页的逐段校验。另外，`hl=zh-Hans` 页面仍显示旧例外表，且没有呈现英文页顶部的更新提示，也没有数字凭证和 Incoming Call Retriever 的较新替代说明。不能据此认为已宣布的日期被取消。现行政策仍列出通用的电话来电账号验证。预览将该 `READ_CALL_LOG` 例外的删除日定为 2027-01-27。2026-07-15 通告里“至少 30 天”的总体适配期不替代这一条目日期。银行和证券经纪应用的电话认证在来源中仍是单独用途。中文页抓取失败或不完整不表示政策已经变更。本页 Play 权限规则的证据等级是 `normative`。Android 与 Google Play 服务替代方案是 implementation note，不构成受限权限例外。

**核对日期：2026-10-24。** 本文按官方政策各章节整理现行要求、例外、替代方案和申报步骤。政策页面同时展示 2027-01-27 生效的变更，文中按生效时间区分。

## 一页判断

- 如果应用不是默认短信、电话或 Assistant 处理器，也不符合政策列出的临时例外，应从所有发布轨道的 App Bundle/Manifest 中移除 SMS 与通话记录权限。
- 即使属于允许用途或申请例外，也必须对应商店页醒目展示的核心功能；没有该功能时应用会损坏或不可用。须在 Play Console 申报并取得审核批准。
- 默认处理器必须先完成系统默认角色注册，再请求权限；失去默认角色后立即停止访问。
- 2027-01-27 起，通用的“通过电话来电验证账号”不再是 READ_CALL_LOG 的允许例外。优先评估 Digital Credentials API；短信验证可使用 SMS Retriever 或 SMS User Consent，来电验证可评估 Incoming Call Retriever 的号码范围匹配方案。
- SMS、通话记录及其推导数据不能用于广告、跨用户画像、出售或与核心功能无关的目的；也不能通过其他权限、API 或第三方数据源绕过限制。

## 适用权限与核心功能标准

| 权限组 | 页面列出的示例权限 |
| --- | --- |
| SMS | READ_SMS、SEND_SMS、WRITE_SMS、RECEIVE_SMS、RECEIVE_WAP_PUSH、RECEIVE_MMS |
| 通话记录 | READ_CALL_LOG、WRITE_CALL_LOG、PROCESS_OUTGOING_CALLS |

“核心功能”是应用的主要用途，可以是一项或一组功能。缺少它会使应用损坏或不可用；商店详情必须醒目说明并推广这些功能。权限只可用于经批准的核心功能，不得为未实现、未披露或不允许的用途申请。Google Play 审查和批准是单独条件，技术上可用不代表政策批准。

## 默认处理器允许范围

应用必须先被系统积极注册为相应默认处理器，才能提示用户接受相关权限；不再是默认处理器时必须立即停止使用权限。

| 处理器角色 | 政策列出的权限 | 使用边界 |
| --- | --- | --- |
| 默认 SMS | READ_SMS、RECEIVE_MMS、RECEIVE_SMS、RECEIVE_WAP_PUSH、SEND_SMS、WRITE_SMS | 用于核心短信收发体验。 |
| 默认 Phone | SEND_SMS、PROCESS_OUTGOING_CALLS、READ_CALL_LOG、WRITE_CALL_LOG | 用于核心拨号/电话体验。 |
| 默认 Assistant | READ_SMS、RECEIVE_MMS、RECEIVE_SMS、RECEIVE_WAP_PUSH、SEND_SMS、WRITE_SMS、READ_CALL_LOG | 用于 Assistant 核心交互，例如实时理解并回复短信。 |

对已注册的默认处理器，政策允许以用户本人最近联系频率、联系时长等信息，帮助用户优先显示重要联系人或识别姓名，但用途须服务于该用户主动发起的通话、短信或操作。不得把某个用户的数据用于直接影响另一个用户的产品体验。表中用途仍须经 Play 审查批准。

## 非默认处理器的临时例外

只有当权限确实启用下列核心功能，且目前没有替代方式时，Google Play 才可能给予例外。下表概括官方页面列出的 17 类用途及权限；例外不是自动授权，也不免除其他政策义务。

| 用途 | 页面列出的权限 |
| --- | --- |
| 电话来电账号验证（仅现行版本，2027-01-27 删除） | READ_CALL_LOG |
| 反短信钓鱼/短信诈骗防护 | READ_SMS、RECEIVE_MMS、RECEIVE_SMS、RECEIVE_WAP_PUSH、WRITE_SMS。须能以分析报告、基准测试、行业出版物等可信材料证明长期且显著的用户保护记录。 |
| 用户内容备份、恢复和云存储 | READ_SMS、RECEIVE_MMS、RECEIVE_SMS、RECEIVE_WAP_PUSH、WRITE_SMS；READ_CALL_LOG、WRITE_CALL_LOG |
| 来电识别、垃圾信息检测或拦截 | READ_SMS、RECEIVE_MMS、RECEIVE_SMS、RECEIVE_WAP_PUSH、SEND_SMS；READ_CALL_LOG、PROCESS_OUTGOING_CALLS |
| 手机与手表、车载或智能家居等连接设备配套，收发短信或电话 | READ_SMS、RECEIVE_MMS、RECEIVE_SMS、RECEIVE_WAP_PUSH、SEND_SMS、WRITE_SMS；PROCESS_OUTGOING_CALLS、READ_CALL_LOG、WRITE_CALL_LOG |
| 在手机与电脑等设备间同步或迁移短信/通话 | READ_SMS、RECEIVE_MMS、RECEIVE_SMS、RECEIVE_WAP_PUSH、SEND_SMS；READ_CALL_LOG |
| 由用户设置触发条件、跨系统区域自动执行重复操作 | READ_SMS、RECEIVE_MMS、RECEIVE_SMS、RECEIVE_WAP_PUSH、SEND_SMS、WRITE_SMS；READ_CALL_LOG、WRITE_CALL_LOG、PROCESS_OUTGOING_CALLS |
| 企业归档、企业 CRM 或企业设备管理（须企业登录） | SMS：READ_SMS、RECEIVE_MMS、RECEIVE_SMS、RECEIVE_WAP_PUSH、WRITE_SMS；电话：READ_CALL_LOG、PROCESS_OUTGOING_CALLS、WRITE_CALL_LOG。CRM 仅允许带星号的 READ_CALL_LOG 和 PROCESS_OUTGOING_CALLS。 |
| 车载免提或投屏，且核心功能直接关联驾驶/出行 | RECEIVE_SMS、SEND_SMS、RECEIVE_MMS、RECEIVE_WAP_PUSH、WRITE_SMS；PROCESS_OUTGOING_CALLS、WRITE_CALL_LOG、READ_CALL_LOG |
| 人身安全/紧急情况发送短信警报 | SEND_SMS |
| 代理号码中转用户电话或短信 | PROCESS_OUTGOING_CALLS、READ_CALL_LOG、WRITE_CALL_LOG |
| SMS Cell Broadcast 客户通信 | RECEIVE_SMS |
| 基于短信的金融交易，例如 UPI 或金融交易验证 | READ_SMS、RECEIVE_MMS、RECEIVE_SMS、RECEIVE_WAP_PUSH、SEND_SMS |
| 银行或证券经纪应用的电话验证/授权 | READ_CALL_LOG、PROCESS_OUTGOING_CALLS |
| 基于短信的个人资金管理/预算 | READ_SMS、RECEIVE_MMS、RECEIVE_SMS、RECEIVE_WAP_PUSH |
| 在默认拨号器中写入并显示通话历史 | WRITE_CALL_LOG |
| 积极持有 SYSTEM_UI_INTELLIGENCE 角色的系统服务 | READ_SMS、READ_CALL_LOG |

**日期核对：** 当前政策正文仍列通用电话来电账号验证这一例外；更新预览说明该条目将于 **2027-01-27** 移除。政策表中单独列出的银行/证券经纪应用电话认证与授权是不同用途，预览版仍保留该行。不能把通用例外的变更误读成对所有电话认证的统一结论；仍须逐项核对更新后的政策和应用资格。

**中英文版本与通告核对（2026-10-24）：** 英文现行帮助页顶部新增“Changes are coming to this article”提示，并链到[通告目录](https://support.google.com/googleplay/android-developer/announcements/13412212)；目录中的[2026-07-15 政策通告](https://support.google.com/googleplay/android-developer/answer/17134731)给出该批变更至少 30 天的总体适配期，而[短信/通话权限预览](https://support.google.com/googleplay/android-developer/answer/17225965)明确电话验证例外的具体生效日为 2027-01-27。两种日期并不冲突：通告的“至少 30 天”不是该条目的替代生效日。此次 `zh-Hans` 页面仍显示旧例外表，也没有呈现英文页顶部的更新提示及数字凭证/来电 Retriever 新替代说明；故不能从中文页未展示提示推断期限取消，具体实施日期以预览页及对应通告交叉核对。该政策子链及通告目标页的覆盖状态见递归链接图 §4.1（快照：`../google-play-policy-link-graph.md`，未导入本仓库）。

**`SYSTEM_UI_INTELLIGENCE` 的系统服务边界（AOSP 源码核对：2026-10-23）：** 政策把“积极持有 `SYSTEM_UI_INTELLIGENCE` 角色的系统服务”单列为 SMS/Call Log 用例。官方 AOSP [`roles.xml` 当前 main 分支](https://android.googlesource.com/platform/packages/modules/Permission/%2B/refs/heads/main/PermissionController/res/xml/roles.xml)和 [Android 16 QPR2 分支](https://android.googlesource.com/platform/packages/modules/Permission/%2B/refs/heads/android16-qpr2-release/PermissionController/res/xml/roles.xml)均将该角色标为 `systemOnly="true"`；角色清单中的 `READ_SMS` 和 `READ_CALL_LOG` 从 Android 13 / API 33 起适用。因此这不是普通第三方应用可以申请或通过改 manifest 获得的通用例外。Play 页面另列 system services 的资格说明；具体应用仍须满足适用的 Play 条款与审核要求。该系统角色源码注释链接到 [Android 11 CDD §9.8.6 Content Capture](https://source.android.com/docs/compatibility/11/android-11-cdd#9_8_6_content_capture)：该 CDD 面向设备实现者，要求对其定义的系统内容捕获数据加密、禁止备份、限制为隐私保护的聚合传输，并提供用户同意/删除/关闭与权限管理能力；这些设备层要求不能替代普通 Play 应用的 User Data、披露同意或权限政策。

## 旧 APK 例外

无法再修改代码的旧 APK 可在 Permissions Declaration Form 的 APK Exceptions 栏申请个案例外，但必须同时满足：

1. 申报具体 APK/version code。
2. APK 发布于 2019-01-01 之前。
3. 为 Android Oreo（API 26）及以上用户提供符合 Permissions policy 的替代 APK。
4. 申请例外的 APK 只占总安装基数极低的个位数比例。

Google Play 逐案审核；另一条合规路径是取消发布不符合要求的 APK。例外字段仅在符合条件的多 APK 发布设置中出现。

## 明确不允许的常见用途

以下是政策列举的常见不允许用途，列表并非穷尽：

- 通过广泛读取 SMS/通话记录进行账号或设备验证；内容分享或邀请。
- 不是默认处理器或系统级默认联系人处理器时进行联系人优先级排序。
- 社交关系图谱、人格画像、通话录音。
- 设备性能加速、存储/数据管理、家庭或设备定位。
- 智能/预测键盘；在壁纸、启动器或其他工具中展示短信/通话。
- 非默认处理器进行短信翻译；不符合角色/例外条件的文字转语音、语音转文字。
- 不符合默认处理器、系统级联系人处理器或例外条件的短信/联系人管理。
- 不符合默认处理器或例外条件的短信/电话通知增强。
- 根据 SMS 做市场调研、远程控制用户手机/其他设备。
- 出售 SMS/通话数据，或通过 SDK 转售/变现此类数据。

存在更安全替代方案时，不得以方便为由读取完整短信或通话记录。

## 替代方案

| 需求 | 政策认可的较窄方案 | 含义 |
| --- | --- | --- |
| 短信 OTP / 账号验证 | [SMS Retriever API 总览](https://developers.google.com/identity/sms-retriever/overview) · [Android 客户端指南](https://developer.android.com/identity/sms-retriever)；无法使用时让用户手动输入验证码。若应用不能控制验证码短信格式，可评估 Android 最小权限指南中的 [SMS User Consent API](https://developers.google.com/identity/sms-retriever/user-consent/overview)，让用户同意仅向应用提供一条短信。 | SMS Retriever 可自动接收匹配本应用的一次性验证码而不申请短信读取权限；User Consent 只提供单条短信并经过用户同意。 |
| 电话来电验证号码 | [Digital Credentials API](https://developer.android.com/identity/digital-credentials/phone-number-verification)；更新预览也链接 [Incoming Call Retriever API](https://developers.google.com/android/reference/com/google/android/gms/auth/api/phone/IncomingCallRetrieverClient)。 | Incoming Call Retriever 在用户同意后，只匹配开发者提供号码范围内的特定来电，并拒接该验证来电、回传验证状态；不需要广泛 READ_CALL_LOG。API 文档标注 Android 10/API 29+，访问可能需要提交申请，且要处理设备/API 不可用情况。 |
| 获取用户本机号码 | [Phone Number Hint](https://developer.android.com/identity/phone-number-hint) | 在兼容设备上让用户选择本机号码，不需要 READ_PHONE_STATE；号码提示本身不等于号码已验证。 |
| 识别/筛选来电 | [CallScreeningService](https://developer.android.com/reference/android/telecom/CallScreeningService) | 用来实现来电筛选而不声明 READ_PHONE_STATE；应与短信/通话记录的广泛读取权限区分。 |
| 发起短信/MMS | Android [Common intents](https://developer.android.com/guide/components/intents-common) 的短信 Intent | 让系统短信应用处理发送动作。 |
| 分享内容或邀请 | [Android Sharesheet](https://developer.android.com/develop/ui/compose/sharing) | 由用户选择接收应用，应用无需读取短信/联系人历史。 |
| 发起电话 | Android [Common intents](https://developer.android.com/guide/components/intents-common) 中的 Dial Intent | 打开拨号器并预填号码，由用户明确发起呼叫；不需要 CALL_PHONE。 |
| 逐步减少权限 | Android [最小权限指南](https://developer.android.com/privacy-and-security/minimize-permission-requests#manage-phone-calls-and-text-messages) | 优先无权限 API、系统 Picker、Intent、低精度/短时数据；尊重拒绝并提供合理降级体验。 |

### Digital Credentials / TS.43 的端到端实现链

[Android 官方电话号码验证指南](https://developer.android.com/identity/digital-credentials/phone-number-verification)（页面标注 2026-07-29 更新）把号码验证分成客户端取凭证、后端兑换号码两部分。它适用于 Android 10/API 29 及以上；实现前需要与运营商或聚合服务建立关系，后者通常提供收费的云 API。指南示例当时使用 `androidx.credentials` 与 `credentials-play-services-auth` `1.7.0-alpha03`；这是页面里的示例版本，不应视为当前稳定版本要求，实施时应重新核对依赖和运营商覆盖。

| 步骤 | 技术要求与核对点 |
| --- | --- |
| 1. 后端请求凭证参数 | 后端向聚合服务请求 DCQL 凭证对象，并传入请求 ID 与 nonce。取设备号码使用 `number-verification/device-phone-number/ts43`；验证既有号码使用 `number-verification/verify/ts43`。 |
| 2. 后端建立 OpenID4VP 请求 | 将聚合服务返回的凭证对象放入 `dcql_query`，使用 `openid4vp-v1-unsigned`、`response_type=vp_token`、`response_mode=dc_api`。每次请求生成唯一 nonce，且必须与聚合服务返回参数中的 nonce 一致。 |
| 3. 客户端向系统请求凭证 | 把后端生成的请求交给 Credential Manager，并使用 `GetDigitalCredentialOption`。用户可取消；设备/ SIM 不支持时也会失败，应用应保留手动输入或其他验证回退。 |
| 4. 后端验证响应 | 客户端将 OpenID4VP 响应送回后端。指南要求校验请求与凭证 nonce 一致、凭证由可信的 Android Telephony 签发，并检查签发时间、到期时间等有效性；具体校验由应用还是聚合服务完成，需与服务商确认。错误可包括格式错误的 `invalid_request` 与处理失败的 `server_error`。 |
| 5. 后端兑换号码 | 将验证后的加密 TS.43 Digital Credential 发送给聚合服务。聚合服务验证并解密后返回已验证号码。 |

指南列出的直接子链接与边界：

| 页面关系 | 目标页 | 核验结果 |
| --- | --- | --- |
| Digital Credentials 指南 → 凭证返回类型 API 参考 | [`DigitalCredential` Kotlin API 参考](https://developer.android.com/reference/kotlin/androidx/credentials/DigitalCredential) · [Java API 参考](https://developer.android.com/reference/androidx/credentials/DigitalCredential) | Kotlin 路径仍因响应超过 4 MiB 无法读取；Java 路径已全文打开。该类型继承 `Credential`，自 `androidx.credentials` 1.5.0 提供，并标注 `@ExperimentalDigitalCredentialApi`。详见下表；平台 API 说明不构成 Play 权限资格。 |
| Digital Credentials 指南 → 服务商集成方案 | [Firebase Phone Number Verification](https://firebase.google.com/docs/phone-number-verification) | 该分支已在下节单独核对；它是服务商实现方案，不改变 Play 的权限、数据披露或用户同意义务。 |
| Digital Credentials 指南 → 同页实现锚点 | DCQL 参数、OpenID4VP 请求、Credential Manager 调用、响应校验、号码兑换 | 这些是同一指南中的章节锚点，不是额外独立网页；以上流程表逐项概括。 |
| Digital Credentials 指南 → 流程图图片 | [TS.43 验证流程 SVG](https://developer.android.com/static/identity/digital-credentials/images/pnv_verifier_diagram.svg) | 图片目标已点击，但当前抓取器不支持 `image/svg+xml`；父页正文已分步描述相同的后端、客户端、聚合服务流程，不推测图中的额外信息。 |
| Digital Credentials 指南 → 内容许可 | [Android Developers Content License](https://developer.android.com/license) | 已打开：Android 文档与代码示例通常按 Apache 2.0 提供（页面声明的例外除外），站点其他内容通常按 CC BY 2.5；外链内容不自动受该许可覆盖。不能将此许可外推到 Play Help 或 Developer Program Policy。 |

#### `DigitalCredential` Java API 参考 → 正文直接链接及关键结论

官方 Java API 页面（2026-08-06 更新）可读。它将 `DigitalCredential` 定义为常用于验证/登录的凭证类型，但特别提醒 `credentialJson` **可能是协议错误响应，不代表验证成功**。应用必须按请求使用的协议解析结果；多凭证请求可能由一个或多个 provider 返回多个 `DigitalCredential`，须逐项判断。系统基础设施、provider 崩溃或通用 Credential Manager 异常属于非协议错误，会中止事务且不返回部分凭证。构造器只检查 JSON 格式有效；JSON 合法不等同于凭证/号码已验证。

| API 页正文链接 | 已读目标与关系 |
| --- | --- |
| Artifact / “Added in 1.5.0” | [AndroidX credentials release notes](https://developer.android.com/jetpack/androidx/releases/credentials)：1.5.0 稳定版于 2025-03-12 发布；`DigitalCredential` 类型在 1.5.0-alpha05（2024-09-04）加入。PNV 指南中的 `1.7.0-alpha03` 是示例依赖，不应照抄成当前生产版本。 |
| [View Source](https://cs.android.com/search?q=file:androidx/credentials/DigitalCredential.kt+class:androidx.credentials.DigitalCredential) | 点击后只返回 JavaScript 搜索壳，没有可审阅的源码正文；API 摘要依据可读的 reference 页面，不从搜索壳推断实现。 |
| [`Credential` 父类](https://developer.android.com/reference/androidx/credentials/Credential) | 抽象凭证基类；API 列出 `DigitalCredential` 等直接子类。它解释类型层级，不规定 Play 权限审批。 |
| [`ExperimentalDigitalCredentialApi` 注解](https://developer.android.com/reference/androidx/credentials/ExperimentalDigitalCredentialApi) | 注解使用 Kotlin `RequiresOptIn`，页面称该 Credential Manager API 仍属实验性，可能变化或移除。集成前应显式处理 opt-in，并在升级时重新核对 API。 |
| [OpenID4VP 1.0 错误响应规范](https://openid.net/specs/openid-4-verifiable-presentations-1_0.html) | 规范正文已打开：协议定义 `invalid_request`、`access_denied` 等错误及 VP Token 校验。Android API 的 `credentialJson` 可能承载协议错误；服务端仍须按其请求配置和 TS.43/聚合服务约定验证，不能把收到 JSON 当作成功。 |
| [`GetCredentialResponse`](https://developer.android.com/reference/androidx/credentials/GetCredentialResponse) | 页面说明一次数字凭证请求可返回多项凭证；`getCredential()` 多项时只取第一项，`getCredentials()` 才列出全部（该列表 API 标注 1.7.0-alpha03）。应遍历全部结果并独立解析/验证，避免漏查其他 provider 的错误。 |
| [WICG Digital Credentials 接口规范](https://wicg.github.io/digital-credentials/#the-digitalcredential-interface) | 目标页直接抓取返回空正文；官方搜索索引可见其为 2026-10-20 的 W3C Editor’s Draft，描述凭证交互需用户中介/明确参与。它是 Web API 草案，不能替代 Android Credential Manager 行为或 Play 政策；正文访问状态按索引摘录记录。 |
| [`credentialJson` 同页锚点](https://developer.android.com/reference/androidx/credentials/DigitalCredential#getCredentialJson()) | 指向同一 API 页的 JSON getter；构造参数和返回值均为 JSON 字符串，格式不合法时构造器抛 `IllegalArgumentException`。 |
| [Android Developers Content License](https://developer.android.com/license) | 同上：许可只适用于其覆盖的 Android Developers 内容，不可据此复用 Play Help/政策全文。 |

**政策关系：** TS.43/数字凭证链可以避免应用广泛读取短信或通话记录，但技术上能取号不等于 Play 批准受限权限用途。尤其是 2027-01-27 起取消通用电话来电账号验证 `READ_CALL_LOG` 例外后，不应继续以该用途申报；数据仍须遵守最小化、安全、隐私披露和 Data safety 要求。API 的“experimental”标记、协议返回成功与否以及 Play 权限审批是三件不同的事。

### 已核对的替代方案直接子页与 SMS Retriever 后代

下表记录政策页“Alternatives to common uses”中最相关的直接目标及继续打开的 SMS Retriever 技术页。技术页面帮助实现窄范围方案，但不扩大 Play 权限例外。

| 页面关系 | 已打开的目标 | 与政策的关系及核对结果 |
| --- | --- | --- |
| SMS/Call Log 政策 → 短信 OTP 替代方案 | [SMS Retriever 总览](https://developers.google.com/identity/sms-retriever/overview) | 服务端短信包含一次性验证码和应用哈希；Play services 只把匹配短信交给应用，不需额外 SMS 权限。页面直接链接 Android 客户端指南与服务端指南。 |
| SMS Retriever 总览 → Android 客户端指南 | [Request SMS Verification in an Android App](https://developer.android.com/identity/sms-retriever)（原链接路径 [`/request`](https://developers.google.com/identity/sms-retriever/request) 重定向到此） | 应用先向服务端请求验证并开始监听；Retriever 最多等待 5 分钟接收一条匹配短信，随后把验证码回传服务端验证。 |
| SMS Retriever 总览 → 服务端指南 | [Perform SMS Verification on a Server](https://developers.google.com/identity/sms-retriever/verify) | 短信最多 140 bytes，包含一次性验证码和 11 字符应用哈希；验证码由服务端生成并校验，须不可猜测、有期限且只能使用一次。指南特别要求不要通过其他渠道返回 OTP 或验证短信，包括不要把 OTP 放进发起验证请求的 API 响应。 |
| 服务端指南 → Play App Signing | [Use Play App Signing](https://support.google.com/googleplay/android-developer/answer/7384423)（当前目标重定向到[现行签名帮助页](https://support.google.com/googleplay/android-developer/answer/9842756)） | 为计算短信应用哈希，服务器需使用实际应用签名证书；Play App Signing 用户应取用 Play 管理的 app signing certificate，不能把 upload key 与 app signing key 混淆。 |
| 服务端指南 → 示例代码 | [AppSignatureHelper.java](https://github.com/googlearchive/android-credentials/blob/master/sms-verification/android/app/src/main/java/com/google/samples/smartlock/sms_verify/AppSignatureHelper.java) | 链接仓库已于 2019-09-19 归档为只读；官方指南仅建议临时取哈希后移除 helper，不应在生产验证消息中动态使用客户端计算的哈希。该代码是历史示例，不是当前实现规范。 |
| 服务端指南 → 短信供应商示例 | [Twilio App Verification with SMS](https://www.twilio.com/docs/verify/app-verification) | 这是第三方传输/集成示例，不是 Google Play 政策；其文档和服务可用性需由采用该供应商的项目另行核对。 |
| SMS/Call Log 政策 → 短信与拨号 Intent | [Common intents](https://developer.android.com/guide/components/intents-common) | 将短信发送和拨号交给可处理的系统应用；页面还链接 Intent、startActivity 等平台参考，技术实现不替代 Play 政策审查。 |
| SMS/Call Log 政策 → Sharesheet 直接子页 | [发送数据](https://developer.android.com/develop/ui/compose/sharing/send) · [接收数据](https://developer.android.com/develop/ui/compose/sharing/receive) · [Direct Share targets](https://developer.android.com/develop/ui/compose/sharing/direct-share-targets) | 发送页把用户主动选择的内容交给 Sharesheet；接收页说明如何接收其他应用分享给本应用的数据；Direct Share 页说明如何发布分享快捷目标。后两者是 Sharesheet 的实现指南，不是读取 SMS/Call Log 的政策许可。 |

**服务端安全边界（技术实现指导，不是新的 Play 权限例外）：** 服务端应把 OTP 绑定到对应用户/号码和验证流程，生成并在服务端验证验证码，设置有效期且成功使用后立即作废。不要在 API 响应或其他非短信渠道中回传 OTP；SMS Retriever 只负责把符合应用哈希的短信交给客户端，验证码仍须回到服务端验证。客户端和服务端指南的语言版本更新时间不同（英文客户端 2026-10-21、中文客户端 2026-10-17；服务端英文 2024-10-31、中文 2025-07-25），实施时应查看当前文档。该安全要求来自 Android 技术指南，不构成额外的 Play 政策条款或权限资格。

SMS Retriever 技术指南还会链接代码样例、服务商和 Android 平台参考。这里已登记政策相关的直接目标及关键后代；通用 Android 文档站导航、API 的全部引用和第三方供应商子树仍按来源台账标为未穷尽。

### SMS/MMS 与电话拨号的 Android 直链实现细节

从 Play [SMS/Call Log 政策](https://support.google.com/googleplay/android-developer/answer/10208820)链接到 [Android Common intents](https://developer.android.com/guide/components/intents-common) 后，我重开了其 SMS/MMS、Phone 两段及相关 Intent 解析说明，并点击了 21 个相关正文链接，合并为 9 个直接目标 URL。页面整体另含大量与权限替代无关的闹钟、地图、相机等通用 Intent；本节只覆盖 SMS/Phone 用例及其实现依赖，不宣称扫描了 Common intents 的全部站点链接。该页标注最后更新 2026-10-16。

| 链接目标 | 目标页内容与本政策的关系 |
| --- | --- |
| [Android Common intents：Phone / Text messaging](https://developer.android.com/guide/components/intents-common) | Play 将 SMS Intent 与 Dial Intent 列为替代方案。发短信可调用系统消息应用编辑/确认；<code>ACTION_DIAL</code> 打开拨号器，用户点击呼叫；<code>ACTION_CALL</code> 会直接拨出并要求 <code>CALL_PHONE</code>。因此普通发起呼叫优先采用用户确认的 Dial 路径，不要把直接呼叫误写成不需要权限的替代方案。 |
| [Intent API](https://developer.android.com/reference/android/content/Intent) | 对 <code>ACTION_DIAL</code> 的 API 描述要求显示号码并让用户明确发起；API 还说大多数应用应使用该 Intent，并限制特定应用的直接呼叫。<code>ACTION_SENDTO</code> 将消息发送给 data 指定的目标；<code>ACTION_SEND</code>/<code>ACTION_SEND_MULTIPLE</code> 用于发送单项/多项内容。Intent 定义解释平台行为，不证明 Play 受限权限资格。 |
| [Common intents 的短信示例](https://developer.android.com/guide/components/intents-common#ComposeAnSmsMessageWithAttachment) | 该节先写“若要确保只由短信应用处理，应使用 <code>ACTION_SENDTO</code> 并设置 <code>smsto:</code>”，但紧接着 Kotlin/Java 示例实例化的是 <code>ACTION_SEND</code>。这是页面文字与示例之间的可见不一致；实现时应核实当前推荐代码，并在目标 Android 版本/消息应用上测试路由，不能无说明地照抄冲突示例。 |
| [Android <code>Uri</code> API](https://developer.android.com/reference/android/net/Uri) | 本页的 <code>Uri.parse()</code> 说明其输入是已编码 URI 字符串；<code>Uri.fromParts()</code> 会对 scheme-specific part 编码并创建不透明 URI，不能构造分层 URI。Android 示例展示 <code>tel:</code> 用法，但 API 方法本身不等于号码验证器；按电话 URI 规范验证/编码输入。旧的 <code>Uri.html</code> 链接已在另一分支确认重定向到此无扩展名地址。 |
| [RFC 3966：tel URI](https://www.rfc-editor.org/rfc/rfc3966)（Android 页面原链接为 [旧 IETF URL](https://tools.ietf.org/html/rfc3966)，现跳至 [RFC Editor 页面](https://www.rfc-editor.org/info/rfc3966/)） | 规范将 <code>tel:</code> 定义为电话号码标识符，不表达拨号步骤或拨号语义；全球号码以 <code>+</code> 标示并建议优先使用，不能用全球号码表示时，本地号码必须带 <code>phone-context</code>。该参数不是把本地号补成 E.164 的国家码前缀。可有视觉分隔符但其不影响 URI 比较/拨号，<code>tel:</code> URI 中不能用空格作视觉分隔符。Android 的 <code>ACTION_DIAL</code> 才负责打开拨号 UI 并交由用户确认。 |
| RFC 3966 所引及更新文档：[RFC 5341](https://www.rfc-editor.org/info/rfc5341/) · [已被取代的 RFC 2806](https://www.rfc-editor.org/info/rfc2806/) · [已废止的 URI 通用语法 RFC 2396](https://www.rfc-editor.org/info/rfc2396/) → [现行通用语法 RFC 3986](https://www.rfc-editor.org/info/rfc3986/) | RFC 5341 更新 RFC 3966 并建立 tel 参数注册表；RFC 2806 已被 RFC 3966 取代。RFC 3966 与 Android API 文档仍会引用 RFC 2396，但 RFC Editor 标明该 URI 通用语法已由 RFC 3986 取代。不要把旧引用误报成 Play 要求，也不要仅凭通用 URI 解析推断 <code>tel:</code> 号码有效。 |
| [ITU-T E.123](https://www.itu.int/rec/T-REC-E.123) 与 [ITU-T E.164 (02/26)](https://www.itu.int/rec/T-REC-E.164-202602-I/en) | RFC 3966 用它们作为电话表示/国际号码结构依据。E.123 目录列 2001 版及后续勘误/修正仍为 in-force；E.164 02/2026 于 2026-02-13 批准并标记 in force，页面提供免费 PDF。此处只核对官方目录元数据，未逐页审读 PDF；这两份 ITU 建议不是 Play 审核政策。 |
| [Intents and intent filters](https://developer.android.com/guide/components/intents-filters) | 隐式 Intent 通过 action、data、category 与目标应用 filter 匹配；调用 <code>startActivity()</code> 时系统按隐式 Intent 处理 <code>CATEGORY_DEFAULT</code>。Common intents 建议先用 <code>resolveActivity()</code> 检查是否有可处理应用，再启动以免无接收者时崩溃。对外发送 SMS/Dial Intent 是发起跨应用操作；不要把接收侧 Manifest filter 的要求混同为发送侧权限例外。 |
| [Context API](https://developer.android.com/reference/android/content/Context) · [Activity API](https://developer.android.com/reference/android/app/Activity) · [ArrayList API](https://developer.android.com/reference/java/util/ArrayList) | Common intents 链到 Activity 启动方法、Intent 解析方法以及多附件示例中的 URI 列表类型。相关入口已打开，但这些大型参考页其余成员、示例和后代未穷尽；ArrayList 只解释多附件集合类型。 |
| [Telephony API](https://developer.android.com/reference/android/provider/Telephony) | 该页说明只有用户选为默认 SMS 应用者可写 SMS Provider、接收 SMS/MMS delivery 广播；默认应用还需声明相应 SMS/MMS action/filter。其“Creating an SMS app”小节有 9 次链接出现、去重为 5 个直接目标，见下文。它解释平台默认处理器角色的技术能力，不代表其他应用可读短信，也不扩大 Play SMS/Call Log 例外。 |
| [Android Developers Content License](https://developer.android.com/license) | Common intents 页标注的许可仅说明 Android Developers 页面/示例适用的许可范围；它不授权将 Play Help、Developer Program Policy 或 DDA 全文复制到离线包。离线许可边界另见上方“离线资料与来源许可边界”。 |

### 默认短信处理器：投递广播、角色 API 与历史 KitKat 指南

[Telephony API](https://developer.android.com/reference/android/provider/Telephony) 的“Creating an SMS app”小节共链接 9 次，去重后为 5 个目标：[`Telephony.Sms.Intents`](https://developer.android.com/reference/android/provider/Telephony.Sms.Intents)、[`Manifest.permission`](https://developer.android.com/reference/android/Manifest.permission)、[`Intent`](https://developer.android.com/reference/android/content/Intent)、[`TelephonyManager`](https://developer.android.com/reference/android/telephony/TelephonyManager)，以及 2013 年的[“Getting Your SMS Apps Ready for KitKat”指南](https://android-developers.googleblog.com/2013/10/getting-your-sms-apps-ready-for-kitkat.html)。父页引用的旧 Blogspot 链接 [原始地址](https://android-developers.blogspot.com/2013/10/getting-your-sms-apps-ready-for-kitkat.html)会转到该现行博客地址。

当前 API 参考给出的平台行为是：

- `SMS_DELIVER_ACTION` 和 `WAP_PUSH_DELIVER_ACTION` 只投递给用户选定的默认短信应用；该应用负责把收到的消息写入 SMS Provider 并通知用户。对应 receiver filter 使用 `BROADCAST_SMS` 和 `BROADCAST_WAP_PUSH`。
- `SMS_RECEIVED_ACTION` 是发给已注册 receiver 的通知广播；这些观察者不应写入消息或自行通知用户。API 说明接收该广播需要 `RECEIVE_SMS`。这是 Android 平台行为，不等于 Play 允许广泛访问 SMS。
- 默认 SMS 应用还需通过 `ACTION_SENDTO` 处理 SMS/MMS scheme，并提供 `RESPOND_VIA_MESSAGE` service。`ACTION_RESPOND_VIA_MESSAGE` 的 URI 用 `sms:`、`smsto:`、`mms:` 或 `mmsto:` 携带收件人，可包含短信正文/主题。`SEND_RESPOND_VIA_MESSAGE` 容易被误读：`Manifest.permission` 将其标注为不可供第三方应用使用，而 `TelephonyManager` 和 SMS 角色示例把它放在 service 的 `android:permission` 属性中，以限制可调用该 service 的调用方。不要把它作为应用自身的 `<uses-permission>`，也不要据此推断 Play 权限例外。

链接的[2013 年 KitKat 指南](https://android-developers.googleblog.com/2013/10/getting-your-sms-apps-ready-for-kitkat.html)正文有 7 次链接出现、去重为 6 个 API 目标：`Intent.ACTION_SENDTO`、`TelephonyManager.ACTION_RESPOND_VIA_MESSAGE`、共用的 `Manifest.permission` 页面、`PackageManager.setComponentEnabledSetting()`、`SmsManager` 和 `Context.startActivity()`。这些目标页均已打开，并抽查相关成员。`SmsManager.sendTextMessage()` 需要 `SEND_SMS`；当前平台参考将该权限列为 dangerous 且 hard-restricted。直接发送因此仍有平台权限和 Play 资格审核要求；它不能替代无权限收件/读取方案。`PackageManager.setComponentEnabledSetting()` 可改变 receiver 是否启用，旧指南将其用于 Android 4.4 下的 `SMS_RECEIVED_ACTION` 示例。该建议是历史平台迁移资料，不是现行 Play 政策。

历史指南还用 `Telephony.Sms.Intents.ACTION_CHANGE_DEFAULT` 请求用户切换默认短信应用。当前 API 明确说明该 action 自 Android Q 起不再受支持，并指向 [`RoleManager`](https://developer.android.com/reference/android/app/role/RoleManager)：先检查系统是否提供 `ROLE_SMS`，再使用 `createRequestRoleIntent()` 返回的 Intent 请求用户同意。RoleManager 页面又链接到 [AndroidX Role 包](https://developer.android.com/reference/androidx/core/role/package-summary)及其 [`RoleManagerCompat`](https://developer.android.com/reference/androidx/core/role/RoleManagerCompat)；该兼容参考列出 SMS 角色所需的 Manifest 组件和 `Intent.CATEGORY_APP_MESSAGING`。这些组件描述 Android 平台角色资格，不是 Play 批准。Play 仍要求用途符合核心功能标准、完成适用申报并经审核批准，之后才可使用受限权限。

**该分支的递归边界：**本次覆盖 Common intents 的 SMS/Phone 政策相关段落、Telephony SMS-app 小节的全部 5 个唯一直接目标、历史指南的全部 6 个唯一直接 API 目标，以及 RoleManager → AndroidX Role API 链。大型 API 页面仅抽查直接相关成员；其他成员、继承 API 和更深文档/站点导航未穷尽。2013 年指南明确标为 Android 4.4 历史资料。整棵外部技术链接树仍未声称闭合。逐 URL 访问级别和子链状态见来源页审计（快照：`../source-page-audit.csv`，未导入本仓库）及来源链接台账（快照：`../source-targets.csv`，未导入本仓库）。

### Phone Number Hint 实现链：选填号码不等于验证号码

SMS Retriever 客户端指南提到用 hint picker 减少手动输入，但其代码示例使用旧的 `HintRequest` / `Auth.CredentialsApi.getHintPickerIntent` 流程。单独的 [Phone Number Hint 当前指南](https://developer.android.com/identity/phone-number-hint)（2026-10-21 更新）改用 `GetPhoneNumberHintIntentRequest`、`Identity.getSignInClient(activity)` 和 `SignInClient.getPhoneNumberHintIntent()`；用户从 SIM 卡可用号码中选择或取消，应用不需要额外权限或 Google 账号。两个页面的示例 API 不应混为同一套当前实现；落地前应按当前指南和项目依赖核对。

号码提示只提供用户选定的号码字符串，**不证明用户控制该号码或已完成验证**。要验证号码，仍需 SMS Retriever、SMS User Consent、手动验证码或适合的其他验证流程；验证码应由服务端生成和校验，限制有效期并防止重复使用。若应用把号码发送、保存或用于其他目的，仍要分别核对 User Data、Data safety、隐私披露、安全和同意义务；系统提示框本身不会替代这些要求。

当前指南的主流程为：创建 `GetPhoneNumberHintIntentRequest` → 通过 `Identity.getSignInClient(activity).getPhoneNumberHintIntent(request)` 获取 `PendingIntent` → 由 Activity Result 流程启动 → 把结果 `Intent` 传给 `getPhoneNumberFromIntent()`。公开的 `SignInClient` API 参考将这两个 Phone Number Hint 方法列为可用方法；同一页另把若干传统登录方法标为弃用并建议 Credential Manager，不能把该弃用标记扩大到 Phone Number Hint 方法。

| 页面关系 | 直接目标及核验 | 与政策/实现的关系 |
| --- | --- | --- |
| SMS Retriever 客户端指南 → 号码输入建议 | [Phone Number Hint](https://developer.android.com/identity/phone-number-hint) | 当前指南列明无需额外权限、无需 Google 账号、显示 SIM 可用号码供用户选择；页面最后更新于 2026-10-21。它是号码输入便利功能，不是号码所有权证明。 |
| Phone Number Hint → 请求对象及构造器 | [`GetPhoneNumberHintIntentRequest`](https://developers.google.com/android/reference/com/google/android/gms/auth/api/identity/GetPhoneNumberHintIntentRequest) · [Builder](https://developers.google.com/android/reference/com/google/android/gms/auth/api/identity/GetPhoneNumberHintIntentRequest.Builder) | 两个大型 API 参考均已打开；核对 `builder()` / `build()` 请求构造入口。类成员与全部 API 后代未逐项穷尽。 |
| Phone Number Hint → `SignInClient` | [Google Play services `SignInClient`](https://developers.google.com/android/reference/com/google/android/gms/auth/api/identity/SignInClient) | 该页承载 `getPhoneNumberHintIntent()` 和 `getPhoneNumberFromIntent()` 两个指南调用；已核对方法用途与返回/异常边界。页面的传统登录方法另有弃用标记，不代表这两个号码提示方法也弃用。 |
| Phone Number Hint → 平台交互对象 | [PendingIntent](https://developer.android.com/reference/android/app/PendingIntent) · [Intent](https://developer.android.com/reference/android/content/Intent) | 前者包装启动提示流程的待执行操作；后者承载用户成功选择后的号码结果。两页是大型平台 API 参考，只核对本流程相关成员。 |
| Phone Number Hint / SMS Retriever 客户端 → Google Play services / 构建说明 | [Google Play services 入口](https://developers.google.com/android) · [Android 构建配置](https://developer.android.com/build) · [依赖项指南](https://developer.android.com/build/dependencies) | 前者是 API 产品目录，不是权限政策；后两者是模块级依赖配置说明。页面中的依赖版本仅是文档示例，不是政策要求。 |
| 两篇 Android 指南 → Maven 仓库与图片 | [Google Maven Repository](https://maven.google.com/web/index.html) · [Maven Central](https://search.maven.org/artifact) · [Phone Number Hint UI 示意图](https://developer.android.com/static/identity/phone-number-hint/images/phone_number_hint_ui.png) | Maven 仓库页面依赖交互选择器/JavaScript，未从本次读取中确认某个具体 artifact 的全部版本；示意图只是 UI 视觉资源，不是政策要求。 |
| SMS Retriever 客户端 → `SmsRetrieverClient` API | [`SmsRetrieverClient`](https://developers.google.com/android/reference/com/google/android/gms/auth/api/phone/SmsRetrieverClient) | 大型 Google Play services API 页已打开：`startSmsRetriever()` 等待最多 5 分钟的一条匹配短信；`startSmsUserConsent(senderAddress)` 等待一条 OTP 短信并通过同意 Activity 返回。该参考页列出 `startSmsRetriever()` 的两种排错原因：`DEVELOPER_ERROR` 表示调用应用的签名证书数量不正确（仅允许一个）；`ERROR` 表示 AppCode 与设备上其他已安装应用冲突。这是 API 运行时诊断，不是 Play 权限资格或政策条款。 |
| `SmsRetrieverClient` → 关键状态/接收器参考 | [`Status`](https://developers.google.com/android/reference/com/google/android/gms/common/api/Status) · [`CommonStatusCodes`](https://developers.google.com/android/reference/com/google/android/gms/common/api/CommonStatusCodes) · [`Context.registerReceiver`](https://developer.android.com/reference/android/content/Context#registerReceiver(android.content.BroadcastReceiver,android.content.IntentFilter)) · [`OnCompleteListener`](https://developers.google.com/android/reference/com/google/android/gms/tasks/OnCompleteListener) · [`Task`](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task) | 已打开 API 页面并核对必要的结果/监听边界。`SmsRetriever` 常量页请求超时；常量在 `SmsRetrieverClient` 参考中可读。其他继承成员和参考页链接尚未全量审计。 |

Android 客户端指南还要求把 `com.google.android.gms.auth.api.phone.permission.SEND` 设置为广播接收器的 `android:permission`，用于识别 Google Play services 发来的 Retriever 广播；不要把它作为应用自身的 `<uses-permission>`。该识别方式要求 Google Play services 19.8.31 或更高版本。Retriever 广播含短信正文，应用应只提取 OTP、尽量不记录或留存整条短信，并继续在服务端验证 OTP。以上实现参考不改变 SMS/Call Log 的 Play 资格、申报或审核标准。

### SMS User Consent 直接子页与 Smart Lock 迁移链

[SMS User Consent 总览](https://developers.google.com/identity/sms-retriever/user-consent/overview) 是 SMS Retriever 不适用时的窄范围回退：当应用无法控制验证码短信格式时，用户可批准应用读取一条短信。获批后 SDK 会把整条短信交给应用，因此仍应只解析验证码、避免记录或留存无关正文；用户拒绝、短信到达另一台设备或流程超时，都应保留手动输入。先启动监听，再让服务端发送短信；指南的示例等待窗口为 5 分钟，并可选用发送方号码过滤。验证码最后仍须交给服务端验证。

总览直接链接 SMS Retriever 总览和[单次短信同意实现指南](https://developers.google.com/identity/sms-retriever/user-consent/request)。后者列出 4–10 个字母数字字符且至少包含一位数字的 OTP 匹配条件；允许时可限定发送方。该页面最后更新于 2024-10-31，示例依赖版本较旧，应按项目当前 Google Play services / AndroidX 依赖重新核对；不要把旧示例版本当作 Play 要求。若应用可以控制短信格式，优先用不需短信读取权限的 SMS Retriever。

实现指南还链接到已弃用的 [Smart Lock 密码登录提示](https://developers.google.com/identity/smartlock-passwords/android/retrieve-hints)，其登录提示功能应迁移到 [Credential Manager](https://developer.android.com/training/sign-in/passkeys/)。该迁移页覆盖 passkeys、密码和联合登录，范围远大于 OTP 自动填充；其示例依赖也有较旧版本，不应直接复制为当前配置。Smart Lock 迁移仅是实现参考，不改变 Play 的受限权限、披露或同意规则。SMS Retriever 当前 Android 客户端页（2026-10-21 核对）展示 `play-services-auth:22.0.0` 与 `play-services-auth-api-phone:18.3.1` 示例；这是该页示例版本，发布前仍应检查最新兼容版本。

### 离线资料与来源许可边界

[Android Developers 内容许可](https://developer.android.com/license) 和 [Google Developers 站点政策](https://developers.google.com/terms/site-policies) 说明的是各自开发者文档、代码样例和网站内容的不同许可类别，并排除部分商标、媒体和第三方链接内容。这些通用许可页面**不能证明 Google Play Help、开发者计划政策或开发者分发协议正文可按相同条件全文复制**。因此本库以双语改写摘要、原始链接、核对时间和链接审计为主；离线 HTML 可离线查看已收录摘要，但并不等于离线保存所有官方全文。若要增加可再分发的完整原文，应先逐个确认该具体来源页面的许可或取得授权。

### 技术集成参考：Firebase Phone Number Verification

Firebase PNV 是基于设备 SIM 和运营商确认号码的另一条技术流程：应用先检查设备/运营商是否支持，再经 Android Credential Manager 取得用户同意，随后由运营商返回本机已验证号码及签名令牌；若不支持，应保留 SMS 等回退路线。它不是 SMS Retriever，也不读取短信/通话记录；它不构成 Google Play 权限或用途豁免，仍须核对 User Data、Data safety、SDK 行为、披露和同意要求。

| 直接目标 | 核验重点与边界 |
| --- | --- |
| [Firebase PNV 总览](https://firebase.google.com/docs/phone-number-verification) · [Android 快速开始](https://firebase.google.com/docs/phone-number-verification/android/get-started) | 快速开始用 SIM-less 测试令牌完成 UI/流程验证；正式运行前先检查每张 SIM 的支持状态，不支持则回退。系统凭据流程会请求用户同意分享号码。 |
| [生产模式](https://firebase.google.com/docs/phone-number-verification/android/production-mode) · [地区价格与运营商覆盖](https://firebase.google.com/docs/phone-number-verification/pricing) | 生产接入涉及 Blaze 计费、API 限制、SHA-256、OAuth 品牌验证和公开隐私政策审查；价格及运营商清单按地区动态更新，不把当前报价复制成固定规则。 |
| [服务端 Token 验证](https://firebase.google.com/docs/phone-number-verification/verify-tokens) | 号码在客户端外使用时传递签名令牌；服务端核验 JWT 类型、ES256/JWKS 签名、项目 issuer/audience 和有效期。 |
| [Firebase Auth 自定义登录](https://firebase.google.com/docs/phone-number-verification/android/sign-in) · [自定义 Credential Manager 流程](https://firebase.google.com/docs/phone-number-verification/android/custom-flow) | Firebase 文档将 Auth 直接接受 PNV token 标为 Beta/未支持；当前示例需先验证 PNV token，再由服务端签发 Firebase custom-auth token。自定义流程还需维护 nonce 与 Credential Manager 交互。 |

以上是服务商集成与平台实现资料，不是 Google Play 政策文本；提交前复查运营商覆盖、计费、Firebase Auth 支持状态及 Play Console 当前表单。

### Firebase PNV 直接子链与开发/隐私最佳实践

2026-10-24 重新打开 [Firebase PNV 概览](https://firebase.google.com/docs/phone-number-verification) 及其实现后代。概览标注 2026-10-20 更新，直接正文链接包括 `DigitalCredential` API 参考、PNV 实现步骤、Firebase PNV 服务页、流程图和许可说明。Kotlin API 路径仍超 4 MiB；Java 等价页面及其直接正文链接已打开并摘要于上表。流程图为抓取器不支持的 SVG；实现步骤中的五个链接是同页章节锚点，已按 DCQL、OpenID4VP、Credential Manager、后端校验和号码兑换分别概括。

| 直接子链 | 核对结果与使用边界 |
| --- | --- |
| [PNV 运营商覆盖与价格](https://firebase.google.com/docs/phone-number-verification/pricing) | 2026-10-22 更新的页面列出 12 个地区、17 家运营商以及动态覆盖/分层计费表；订户覆盖估算依据运营商最近公开数据（页面称截至 2026-06-30，另有标记例外）。生产必须绑定计费账号；只有应用成功收到电话号码时计费。SIM-less 测试模式无需计费账号。地区、运营商覆盖、设备覆盖和价格会变，本库不把报价或列表当成固定政策。 |
| [Android PNV 快速开始](https://firebase.google.com/docs/phone-number-verification/android/get-started) | 页面标注 2026-10-21 更新。测试令牌映射到假号码，7 天过期；测试可在实体设备或模拟器运行，不需真实 SIM 或生产计费。正式界面前建议无同意地预检每张 SIM 支持状态；不支持时回退到 SMS。测试模式要求设备加入 Google system services public beta；测试令牌需项目内的 PNV 管理角色。 |
| [Firebase Android BoM](https://firebase.google.com/docs/android/learn-more) | 官方建议用 BoM 统一并协调 Firebase SDK 版本；页面示例为 BoM 35.0.2，快速开始示例的 PNV 库为 17.0.0，均是页面当时的版本，不是 Play 要求或长期版本建议。KTX 库自 BoM 34.0.0（2025-07）移出 BoM；新版本建议使用主模块中的 KTX API。实施时按当前发布说明核对版本。 |
| [Firebase Android 项目设置](https://firebase.google.com/docs/android/setup) → [Firebase 项目通用最佳实践](https://firebase.google.com/docs/projects/dev-workflows/general-best-practices) | 重要设计原则是每个开发/测试/生产环境使用不同 Firebase 项目；同一项目中的注册应用共享后端、资源和数据。一个产品的 Android/iOS/web 平台变体可在同一环境项目共享；debug 与 release 应分开，避免测试数据污染或覆盖生产数据。彼此独立的白标应用通常应分项目，以避免跨应用数据和配置混用。 |
| [环境概览](https://firebase.google.com/docs/projects/dev-workflows/overview-environments) · [各环境安全指南](https://firebase.google.com/docs/projects/dev-workflows/general-security-guidelines) · [Firebase 安全清单](https://firebase.google.com/support/guides/security-checklist) | 至少建立与生产资源/数据隔离的预生产环境；测试/暂存环境不使用真实用户数据并限制访问。适用时使用 Local Emulator Suite；Firestore、Realtime Database、Cloud Storage 采用安全规则并在模拟器/CI 测试；生产对支持的 Firebase 服务启用 App Check。Firebase 提供的 API key 是项目/应用标识，不是授权边界；授权仍依赖 IAM、安全规则和 App Check，且 API key 应限制到所需 API。 |
| [Firebase 上线清单](https://firebase.google.com/support/guides/launch-checklist) 与 [PNV 管理角色](https://docs.cloud.google.com/iam/docs/roles-permissions/fpnv) | 上线清单建议生产与预生产项目隔离、多个项目所有者/群组化成员、按需授予访问、启用 App Check 并先在模拟器测试；预算提醒只是通知，不是消费上限。快速开始所链接的 `roles/fpnv.admin` 页面将该角色标为 Beta、说明其拥有 FPNV 全部权限（获取数字凭证、生成测试号码令牌、签发号码令牌）；这是很宽的项目角色，分配前应核实需要的权限。测试标签页要求 Google 账号和项目访问；另一个 IAM 控制台链接本轮返回 Internal Error。 |

**关系与限制：**这些是 Firebase/Android 产品的安全和接入建议，不是 Play 政策条文、权限例外或审核通过证明。Firebase 上线清单中的 SMS region policy 指的是 Identity Platform 短信验证服务，不应误记成 PNV 的条件。Firebase 系统同意、App Check 或测试账号访问控制也不能替代 Play User Data 的醒目披露、同意、Data safety 申报或受限权限审核。

### Firebase PNV 服务合同、隐私审查与 Codelab 边界

**核对日期：2026-10-23。** Firebase 的[服务条款目录](https://firebase.google.com/terms)把 Phone Number Verification (PNV) 列在 Google Cloud Platform Terms 一组；该组进一步受[Google Cloud Service Specific Terms](https://cloud.google.com/terms/service-terms)约束。第 45 节是 PNV 的服务专属合同要求，不能把它误写成 Google Play 权限例外。

第 45 节要求在 PNV API 启用期间持续维护、公开发布并遵守隐私政策。政策至少要准确说明开发者/联系信息、收集的数据类型与方式、处理目的、第三方接收者、安全措施、用户权利、保存期限和政策更新通知方式。安全措施须达到或超过行业标准；发生个人数据泄露时，按适用法律通知受影响用户并及时减害。Google 可以审计；发现违反这些要求时可能暂停 PNV，整改并重新核验后才恢复。

最关键的用途限制：**通过 PNV 收到的用户数据不视为合同定义的 Customer Data；授权用途仅为账号安全与身份验证。** 营销、短信/电话联系或其他联系用户的用途，需要用户同意或隐私政策所述的其他法律依据。这个合同定义不消除个人信息保护法义务，也不免除 Play User Data、Data safety、SDK 数据流、应用内醒目披露和同意要求。应按实际数据流而非“使用了 Firebase”来填写政策与 Data safety；不能仅凭 PNV token 推定某个 Data safety 分类。

| 服务链页面 | 已核对的要求与实际关系 |
| --- | --- |
| [Firebase PNV 隐私与接入说明](https://firebase.google.com/docs/phone-number-verification/carrier_specs/privacy) | 生产接入前需完成品牌验证和公开隐私政策审查；通过前只可本地测试，不产生运营商流量。Firebase 会定期复查隐私政策，若政策不再说明号码用途，可暂停 PNV。Android 聚合服务流程在每次请求号码时展示同意界面，界面链接到接入审查时提交的隐私政策。 |
| [Google API Services User Data Policy](https://developers.google.com/terms/api-services-user-data-policy) | Service Specific Terms 第 45 节明确交叉引用此政策。用于交叉核对透明度、安全、负责任的数据处理；该政策中面向 OAuth 敏感/受限 scope 的验证条款不能不加区分地当成 PNV 的 OAuth scope 规则。 |
| [Google Cloud Data Processing Addendum](https://cloud.google.com/terms/data-processing-addendum) · [Firebase Data Processing and Security Terms](https://firebase.google.com/terms/data-processing-terms) | 这类附加条款以 Customer Data 的处理和安全为主题；Firebase PNV 第 45 节却明确称 PNV 收到的用户数据不属于 Customer Data。本库不据此断言通用 DPA 自动覆盖 PNV 数据，也不推断这会排除其他隐私法义务；应以适用的服务合同、产品条款和法律审查为准。Firebase [Paid Services Terms](https://firebase.google.com/terms/billing) 也不是 PNV 第 45 节的替代文本。 |

#### Codelab 是样例，不是 Play 审批或完整生产清单

[Firebase PNV Android Codelab](https://firebase.google.com/codelabs/firebase-pnv-android) 的样例是餐厅预约 AI 语音代理，不是一般电话号码验证或 Play 合规证明。测试模式无需真实 SIM 或生产计费，测试令牌 7 天过期；正式启用需要 Blaze 计费、添加 SHA-256 指纹、品牌验证及隐私政策审查，并在生产包中删除测试会话代码。Codelab 链接的[生产模式指南](https://firebase.google.com/docs/phone-number-verification/android/production-mode)、[自定义流程](https://firebase.google.com/docs/phone-number-verification/android/custom-flow)、[Token 验证](https://firebase.google.com/docs/phone-number-verification/verify-tokens)、[价格与配额](https://firebase.google.com/docs/phone-number-verification/pricing)均有各自摘要；运营商覆盖和计费随地区变化，应以实时页面为准。

Codelab 还说明 Firebase AI Logic 设置过程会自动启用 App Check，但该 Codelab 尚未补上相应配置步骤。它建议开发时自行配置 [App Check debug provider](https://firebase.google.com/docs/app-check/android/debug-provider)或暂时关闭 AI Logic enforcement；这是样例的 App Check 阻塞说明，不是正式环境绕过建议。Debug 文档明确要求保护 debug token 和 debug build：不得提交到公开仓库，也不得带入生产包；令牌泄露后应立即撤销。开发者还应按 AI Logic/App Check 当前控制台要求配置生产环境，不能照抄 Codelab 的暂时关闭步骤。

Codelab 正文的 19 个不同目标均尝试打开；Firebase Console/项目设置和生产配置入口受登录或项目权限限制，Google Play system-services 测试邀请及 OAuth 品牌验证链接出现抓取错误，示例 GitHub 目录返回 Cache miss。具体已读、重定向、账号门槛和未解析链接见递归链接图 §4.72（快照：`../google-play-policy-link-graph.md#472-smscall-log-firebase-pnv-隐私合同与示例链接链`，未导入本仓库）及逐 URL 台账；未解析的目标不按链接标题推断内容。Codelab、Firebase/Android 实现文档均不构成 Google Play 审核批准。

### Incoming Call Retriever：来电号码验证的最小权限实现

[Incoming Call Retriever API 参考](https://developers.google.com/android/reference/com/google/android/gms/auth/api/phone/IncomingCallRetrieverClient) 将它定位为无需广泛 `READ_CALL_LOG` 的来电号码验证方案：应用给出预期号码范围，用户同意后，API 在限定时间内拦截第一个匹配来电、拒接该电话，并通过广播回传验证结果。该接口要求 Android 10 / API 29 及以上；不支持电话服务、设备/SIM 不兼容或客户端未获 API 授权时，可能返回 `API_UNAVAILABLE`。

Google 的 API 参考明确要求先填写[Incoming Call Retriever 接入申请表](https://docs.google.com/forms/d/e/1FAIpQLSezoJZPt6L-J-httaMiSJnHFUIF0oR1n0Xvvpoxco9LB42LMg/viewform)。2026-10-23 重开公开表单，页面说明仅对有效用例开放、每个应用单独申请；必填项包括联系人邮箱、公司/组织、商店链接、准确包名、详细用例与用户流程，以及现有电话验证流程 PDF 或 UI 样图等支持材料。本轮页面可读，未提交表单。**API 接入申请不是 Play 权限声明或政策豁免申请，也不保证获批。** API 页面把 Digital Credentials 列为推荐方案，Firebase Phone Number Verification 是其供应商路线；SMS Retriever 是短信 OTP 的另一种无敏感权限方案。来电验证若采用 Incoming Call Retriever，应确认应用确有接入资格和服务覆盖，再决定是否采用。

| 步骤 | 实现与失败处理 |
| --- | --- |
| 1. 检查设备能力 | 在启动前检查 `Context.TELEPHONY_SERVICE` 是否可用。该 API 标注 `@RequiresApi(29)`；无电话服务、无适用 SIM、设备/API 不可用或客户端未授权时应走备用验证，不能退回未经批准的广泛 `READ_CALL_LOG`。 |
| 2. 请求并展示同意 | 调用 `startIncomingCallRetriever(request)` 开始验证（必要时同时请求同意），或先调用 `startUserConsent()`；成功返回的 `Task<PendingIntent>` 应由 Activity 启动系统同意界面。只在用户授予同意或近期同意可复用后继续。 |
| 3. 匹配验证来电 | 请求对象限定后端发起验证电话时可用的号码范围；后端须在用户同意后的 API 时间窗口内呼叫符合范围的号码。API 只拦截首个匹配来电并拒接它，然后通过状态广播通知成功、失败或超时。不要把它描述为通用来电筛选、通话记录访问或可任意读取号码的接口。 |
| 4. 处理结果 | Activity 应先核对 `requestCode`，再检查 `resultCode` 与状态码；用户拒绝、取消或触发频率限制均应停止验证并提供替代路径。对异步失败处理 `ApiException` 和其他 `Exception`，特别处理 `IncomingCallRetrieverStatusCodes.API_UNAVAILABLE`。 |
| 5. 保护结果接收器 | 按 API 指南在 Manifest 中注册 `BroadcastReceiver`，过滤 `PHONE_VERIFICATION_STATUS_INTENT_ACTION`，并将 `android:permission` 设为 `com.google.android.gms.auth.api.phone.permission.SEND`，以限制为 Google Play services 发送的广播；**不要**为此加入该权限的 `<uses-permission>`。官方建议静态注册接收器以提高应用不在运行时收到结果的可靠性。 |

#### 孙级 API 参考：号码范围、同意结果与失败状态

2026-10-24 继续打开 [IncomingCallRetrieverRequest](https://developers.google.com/android/reference/com/google/android/gms/auth/api/phone/IncomingCallRetrieverRequest)、[IncomingCallRetriever](https://developers.google.com/android/reference/com/google/android/gms/auth/api/phone/IncomingCallRetriever) 和 [IncomingCallRetrieverStatusCodes](https://developers.google.com/android/reference/com/google/android/gms/auth/api/phone/IncomingCallRetrieverStatusCodes)，把先前只记录“API_UNAVAILABLE”的状态审计扩展到完整公开状态常量。它们是 Android/Play services 实现参考，不是 Play 权限资格或政策例外。

| API 目标 | 参考页明示的约束 | 实施含义/待确认点 |
| --- | --- | --- |
| [`IncomingCallRetrieverRequest`](https://developers.google.com/android/reference/com/google/android/gms/auth/api/phone/IncomingCallRetrieverRequest) | 请求含国家代码（不带 `+`）、号码前缀、包含端点的 `startRange` 和 `endRange`。前缀在国家代码后的号码部分达到 10 位或更多时为必填；上下界必须同位数且 `startRange ≤ endRange`。待匹配来电的后缀须落在该范围内。 | 服务端号码池和客户端范围必须一致；只允许预期验证呼叫落入窄范围。文档写明总位数应为国家代码位数 + 前缀位数 + 范围位数，但同页示例又展示短于该位数的后缀（如 `12`）及带前导零范围（如 `000000`），与该位数说明存在表面张力。不要据示例自行推断可变长度/前导零匹配规则；上线前用真实号码格式向 API 支持确认。 |
| [`IncomingCallRetriever`](https://developers.google.com/android/reference/com/google/android/gms/auth/api/phone/IncomingCallRetriever) | 同意 Activity 结果由 `ACTIVITY_RESULT_INTENT_EXTRA_STATUS_CODE` 和说明性 `ACTIVITY_RESULT_INTENT_EXTRA_MESSAGE` 承载；验证完成后以 `PHONE_VERIFICATION_STATUS_INTENT_ACTION` 广播，并由 `PHONE_VERIFICATION_STATUS_INTENT_EXTRA` 携带结果。需要启动同意 UI 的调用应使用 Activity context；仅有 Application context 会在尝试启动 UI 时出错。 | `SUCCESS_CACHE` 表示近期同意可复用，不等于本次刚展示并点击了新同意框；`RESULT_CANCELED` 应按拒绝、取消或限流处理，不能继续验证。结果广播接收器仍须用 API 指定权限保护。 |
| [`IncomingCallRetrieverStatusCodes`](https://developers.google.com/android/reference/com/google/android/gms/auth/api/phone/IncomingCallRetrieverStatusCodes) | 官方常量包括 `CONCURRENT_REQUESTS`、`IN_EMERGENCY_CALL`、`API_UNAVAILABLE`、`RATE_LIMIT_REACHED`、`TELEPHONY_FEATURE_UNAVAILABLE`、`INVALID_PHONE_NUMBER_RANGE`、`USER_CONSENT_DENIED` 与 `FAILURE_OTHER`。 | 这是公开状态枚举；可据其类别停止并发请求、修正非法号码范围、对紧急通话/限流/用户拒绝暂停本次流程，对设备/电话能力不可用切换替代验证。它不授予任何受限权限资格，也不改变 2027-01-27 后的 Play 用途限制。 |

参考页状态说明很简短（例如 `API_UNAVAILABLE` 为“API 当前不可用”）；客户端页另外说明可能原因包括设备/API 不支持、调用方未获授权或设备不支持 SIM。其他状态的枚举名可帮助分类，但文档没有为每个错误规定重试间隔或业务处置方案；上表的回退建议是实现层的稳健处理，不冒充官方政策。API 方法参考最后更新于 2026-07-07；应在具体集成时再核对最新版本。

此技术链与 2027-01-27 政策变更的关系：它可用作号码验证的窄范围实现，但不会改变 Play 对受限权限用途的判断。通用电话来电账号验证例外到期后，应迁移为不读取 `READ_CALL_LOG` 的方案；银行/证券经纪的电话认证是政策中单独列出的用途，仍需按该用途的适用条件、核心功能、申报和审核逐项判断。

## Play Console 申报和审核

1. 检查所有已上传 App Bundle/APK，包括 Open、Closed、Internal 测试轨道；确认实际权限与计划用途一致。
2. 在 App content 的 Permissions Declaration Form 中选择受支持的核心用途，解释权限如何支撑商店页明确展示的核心功能。
3. 提供审核步骤和视频；需要登录时提供专用于测试的账号/号码与访问说明，不得提供真实用户凭据。
4. 如申请旧 APK 例外，填写符合条件的 version code 并停用不合规 APK/测试轨道。
5. 确认声明真实、完整；使用权限方式发生变化时重新提交更新后的声明。
6. 为延长审核留出时间。官方说明可能需要数周；紧急发布时可移除高风险权限后提交新版本，走标准审核。

未声明、用途不合规或材料不足可能导致应用下架或发布受阻。发布 API 用户仍需按 Console 流程完成首次声明/审核及新增权限声明。

## 子链接与知识库关系

本页正文锚点、相关主题链接和重复链接的逐项登记见政策递归链接图（快照：`../google-play-policy-link-graph.md`，未导入本仓库）中 SMS/通话权限章节。以下列出最重要的目标页及其与本政策的关系：

| 目标页面 | 关系与要点 |
| --- | --- |
| [Permissions Declaration Form 详解](../permissions-declaration/permissions-declaration.zh-CN.md) · [官方表单帮助](https://support.google.com/googleplay/android-developer/answer/9214102) | 申报、测试轨道阻塞、视频和测试账号、延长审核及旧 APK 例外步骤。 |
| [敏感信息权限总则](../sensitive-permissions/sensitive-permissions.zh-CN.md) | SMS/通话记录属于个人和敏感数据；核心功能、最小范围、替代方案及其他敏感权限的横向规则。 |
| [用户数据政策](../user-data/user-data.zh-CN.md) 与 [Data safety 表单](../data-safety/data-safety.zh-CN.md) | 规定披露、同意、隐私政策和 Console 数据声明；SMS 例外仍须遵守。 |
| [Malware 总政策](https://support.google.com/googleplay/android-developer/answer/9888380)（短信页该锚点显示 “Spyware Policy”） | 本次点击实际打开 Malware 总政策，覆盖恶意代码及 SDK，spyware 是其风险类别之一；完整分类见双语专题（[Google Play 恶意软件（Malware）与 Play Protect 威胁分类](../malware/malware.zh-CN.md)）。它与下一行的独立 Spyware 说明页分开记录。 |
| [Spyware policy 说明](https://support.google.com/googleplay/android-developer/answer/14745000) | 禁止与合规功能无关的数据外传；个人贷款/预算应用不得外传非金融或个人短信历史；SDK 同样需要核查。 |
| [Digital Credentials 电话号码验证](https://developer.android.com/identity/digital-credentials/phone-number-verification) | Android 10/API 29+ 支持的号码验证链：客户端请求临时 TS.43 凭证，后端通过运营商/聚合服务换取已验证号码。 |
| [Incoming Call Retriever API](https://developers.google.com/android/reference/com/google/android/gms/auth/api/phone/IncomingCallRetrieverClient) 与[逐应用接入申请表](https://docs.google.com/forms/d/e/1FAIpQLSezoJZPt6L-J-httaMiSJnHFUIF0oR1n0Xvvpoxco9LB42LMg/viewform) | 用户同意后仅匹配开发者提供号码范围内的验证来电，拒接首个匹配来电并回传状态；Android API 29+。接口申请与 Play 权限声明分开。完整流程、失败回退、Manifest 接收器安全要求见上文。 |
| [SMS Retriever](https://developer.android.com/identity/sms-retriever) | 客户端与服务器协作接收包含应用哈希的一次性短信验证码，不需额外短信读取权限；服务端验证回传验证码。 |
| [权限最小化指南](https://developer.android.com/privacy-and-security/minimize-permission-requests) | 优先系统选择器、无权限 API、Intent 和最少数据；拒绝权限后优雅降级。 |
| [`SmsManager`](https://developer.android.com/reference/android/telephony/SmsManager) | `sendTextMessage()` 用于主动发送 SMS，要求 `SEND_SMS`；它不是读取验证码或接收短信的无权限替代 API，且发送权限仍受 Play 规则约束。 |
| [SMS User Consent API](https://developers.google.com/identity/sms-retriever/user-consent/overview) | 当应用不能控制短信格式时，先由用户同意，再把一条短信内容交给应用用于提取验证码；用户拒绝或短信在另一台设备时，应保留手动输入路径。 |
| [Phone Number Hint API](https://developer.android.com/identity/phone-number-hint) | 让用户从设备可用号码中选择并自动填入，减少手动输入；它不是号码验证结果。 |
| [CallScreeningService](https://developer.android.com/reference/android/telecom/CallScreeningService) | 由用户选择的单一 `ROLE_CALL_SCREENING` 应用处理来电筛选；来电到达后应在 5 秒内响应。它是平台角色/API，不自动授予 Play 政策例外。 |
| [SMS 和通话验证的最小权限实现建议](https://developer.android.com/privacy-and-security/minimize-permission-requests#manage-phone-calls-and-text-messages) | 该指南还列出 appSpecificSmsToken、SMS User Consent、Phone Number Hint、CallScreeningService 和 ACTION_DIAL；这些分别解决验证码、填号、筛选来电或发起通话，不代表可读取完整历史。 |
| [Android 角色说明](https://source.android.com/docs/core/permissions/android-roles) | 解释默认处理器/系统角色；系统角色定义不是普通应用自行宣称政策豁免的依据。 |
| [System Services 说明页](https://support.google.com/googleplay/android-developer/answer/12085265) · [Partner Center 系统服务指南](https://docs.partner.android.com/partners/guides/system-services) | 说明页将 System services 定义为预装且支持核心系统功能的软件；只有运营商、SoC 厂商或 OEM 对预装/捆绑应用可到 Partner Center 核查资格并申请例外。这不是普通第三方应用的通用豁免。Partner Center 目标本次返回缓存未命中，正文受合作伙伴访问限制，未推断其内部要求。 |
| [Android 通用 Intent](https://developer.android.com/guide/components/intents-common)、[Android Sharesheet](https://developer.android.com/develop/ui/compose/sharing) | 具体实现短信、拨号和用户主动分享的最小权限路径。 |
| [短信/通话政策预览](https://support.google.com/googleplay/android-developer/answer/17225965) | 记录 2027-01-27 删除电话验证 READ_CALL_LOG 例外及替代路线。 |
| [2026-07-15 政策通告](https://support.google.com/googleplay/android-developer/answer/17134731) · [通告目录](https://support.google.com/googleplay/android-developer/announcements/13412212) | 英文现行页的更新提示链到通告目录；该通告说明至少 30 天的总体更新期。具体 SMS/Call Log 变更仍以预览页标注的 2027-01-27 为准，勿将总体适配期当作专项生效日期。 |

## 覆盖状态与注意事项

- 本文覆盖可访问的英文官方政策页主要正文：通用规则、默认处理器、全部例外、旧 APK、禁止用途、替代方案和申报审核；简体中文同页本次无法稳定抓取，故中文稿为基于官方英文正文的整理翻译。
- 主要政策目标页已在上方逐项概述；所有已发现的正文锚点、帮助主题及重复链接仍以递归链接图为链接清单。Incoming Call Retriever API 的实质性直接子链接已按其接入表单、替代方案、调用/同意流程、结果类型和接收器参考分组；大型 Android/Google Play services API 目录成员、通用导航和第三方供应商的全部后代仍未穷尽。
- Android API 实现文档仍会变化。涉及 SDK 版本、服务可用性和具体实现时，以官方开发者文档和审核时 Play Console 要求为准。
- 本文是结构化改写，不是逐字镜像；官方来源链接保留，便于离线知识库核对原文与更新。
