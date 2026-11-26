---
id: google-play.android-developer-verification
platform: google-play
language: zh-CN
authority: operational
status: current
kb_checked_at: 2026-10-24
review_due: 2027-01-24
regions: [global]
topics: [android-developer-verification, package-registration, app-signing, developer-identity, sideloading]
snapshot_id: android.developer-verification
snapshot_package: "GooglePlay-KnowledgeBase-2026-10-24-review.zip"
coverage_status: "detailed-summary"
source_url: "https://developer.android.com/developer-verification?hl=zh-cn"
source_url_android_console: "https://developer.android.com/developer-verification/guides/android-developer-console?hl=zh-cn"
source_url_full_distribution: "https://developer.android.com/developer-verification/guides/full-distribution?hl=zh-cn"
source_url_limited_distribution: "https://developer.android.com/developer-verification/guides/limited-distribution?hl=zh-cn"
source_url_limited_distribution_en: "https://developer.android.com/developer-verification/guides/limited-distribution?hl=en"
source_url_play_console: "https://developer.android.com/developer-verification/guides/google-play-console?hl=zh-cn"
source_url_faq: "https://developer.android.com/developer-verification/guides/faq?hl=zh-cn"
source_url_android_studio_panda_4: "https://developer.android.com/studio/releases/past-releases/as-panda-4-release-notes"
source_url_security_announcement: "https://android-developers.googleblog.com/2025/08/elevating-android-security.html"
source_url_play_identity_announcement: "https://android-developers.googleblog.com/2023/07/boosting-trust-and-transparency-in-google-play.html"
source_url_open_source_registration: "https://developer.android.com/developer-verification/guides/open-source-app-registration"
source_url_developer_console_api: "https://developer.android.com/developer-verification/guides/developer-console-api"
source_url_june_2026_update: "https://android-developers.googleblog.com/2026/06/android-developer-verification.html"
source_url_march_2026_rollout: "https://android-developers.googleblog.com/2026/03/android-developer-verification-rolling-out-to-all-developers.html"
source_url_private_apps_verification: "https://support.google.com/work/android/answer/17266330?hl=en"
source_url_enterprise_terminology: "https://developers.google.com/android/work/terminology"
source_url_certified_devices: "https://www.android.com/certified/"
source_url_enterprise_management: "https://www.android.com/enterprise/management/"
source_url_en: "https://developer.android.com/developer-verification?hl=en"
source_url_android_console_en: "https://developer.android.com/developer-verification/guides/android-developer-console?hl=en"
source_url_full_distribution_en: "https://developer.android.com/developer-verification/guides/full-distribution?hl=en"
source_url_play_console_en: "https://developer.android.com/developer-verification/guides/google-play-console?hl=en"
source_url_faq_en: "https://developer.android.com/developer-verification/guides/faq?hl=en"
effective_date: "device enforcement began 2026-09-30 in Brazil, Indonesia, Singapore, and Thailand; global expansion is 2027 and beyond, not 2027-01-27"
---

# Android 开发者验证与应用包注册

> **导入说明（Google batch 8）。** 正文来自已经分开的 2026-10-24 Google Play 知识库快照（`android.developer-verification`，核对日 2026-10-24）的改写摘要，不是官方页面的逐字副本。英文官方页面是效力来源。`kb_checked_at` 是快照源文件记录的核对日；本次导入没有重新打开线上官方页面。文中“本知识库”“本库”“本地专题”等说法描述的是该快照库的覆盖范围，不是本仓库已经导入的页面。指向本仓库没有收录的专题、链接图、台账或 CSV 的相对链接改为文字提及。指向 Google batch 1–7 或本批十三个专题的相对链接改为本仓库文件。核对日 2026-10-24。设备侧执行自 2026-09-30 起适用于巴西、印度尼西亚、新加坡和泰国的已认证 Android 7+ 设备。后续全球扩展写的是 2027 年及以后。这不是 2027-01-27 的联系人、位置或地理围栏预告。快照记录的重开结果是：英文有限分发指南（标注 2026-10-23 更新）和简体中文专页（标注 2026-09-30 更新）都写最多 20 台经最终用户授权的设备。较早观察到的英文“50 台”未能复现，在本专题标为过时。另外的 Android Developer Console 账号专题仍记录中文本地化有限分发指南、指南总览和 FAQ 为 20 台，而 2026-10-23 更新的英文专用指南为 50 台。两份快照记录保持分开，不合并成一个数字。中国证件的简体中文视图提示译文可能由 AI 翻译，以英文为准。组织核验 PDF 抓取失败。Play Console 和总览页的 YouTube 目标缓存未命中。旧 Android Developer Console 预览 URL 返回 404。这些访问限制不是登记规则变更。快照 URL 中的 Play Console 数字开发者 ID 不写入本公开页面。这是已认证 Android 设备的操作登记说明，不替代开发者分发协议或开发者计划政策。制裁说明和 ITU-T E.164 是监管或标准背景，不是 Play 条款。证据等级：Operational。

**核对日期：2026-10-24。** Android 开发者验证把开发者的真实身份与应用包名/签名密钥关联起来。它与 Google Play 开发者账号验证、Play 政策审核相关，但不是同一项检查：Play 管理中心账号状态、包名注册和经过认证设备上的安装验证应分别核对。

Android Developer Console 的开户、身份联系资料、付款资料权限和服务条款已单独整理在[Android Developer Console 账号专题](../android-developer-console-accounts/android-developer-console-accounts.zh-CN.md)。该专题与本页的 Android 系统级包名验证互相引用；不要将其与 Google Play Developer Distribution Agreement 或 Play Console 要求合并。

## 适用范围与当前时间线

Android 官方指南要求开发者注册应用包名，才能让应用在受保护的已认证 Android 设备上安装。系统级执行措施于 **2026-09-30** 起在巴西、印度尼西亚、新加坡和泰国面向 Android 7+ 已认证设备推出；初始参与商店包括 Google Play、Honor、OPlus/OPPO、Samsung Galaxy Store、Transsion/Palm Store、vivo 和 Xiaomi。官方计划在 **2027 年及以后**扩展到全球已认证设备和更多第三方商店。

这项设备侧分阶段保护不等于 Play 分发豁免：Google Play 的 [Play Console 要求](../play-console-requirements/play-console-requirements.zh-CN.md)另要求注册希望继续分发的 Play 应用包名。官方称 99% 的 Play 应用已自动注册，但开发者仍需检查 Console 首页及应用状态，并处理未注册包名。Play 外分发则使用对应注册路径。

## 选择账号和分发路径

| 路径 | 适用对象和能力 | 身份/费用要点 |
| --- | --- | --- |
| **全面分发账号** | 组织或专业开发者；可以不限数量/时长地广泛分发 | 需验证身份。个人通常提交政府签发带照片证件和地址证明；组织还需 D-U-N-S、经 Search Console 验证的网站及地区要求的组织文件。FAQ 当前称 Android Developer Console 全面分发账号收费 25 美元；以注册页面显示的实际费用/付款方式为准。 |
| **有限范围分发账号** | 学生、业余爱好者及其他小范围/个人用途；当前英文和简体中文专页均称最多分享给 20 台经用户明确授权的设备 | 免费且不需政府证件，但需 Google 账号、两步验证、关联 Google Payments Profile 和联系邮箱。设备分享需经链接/二维码、接收端确认和管理中心注册的握手流程。 |
| **未验证开发者旁加载** | 用户仍可安装，但需在设备端完成高级流程；ADB 开发/测试安装保持原样 | FAQ 描述的高级流程包含安全提示、设备重启/重新验证和 24 小时保护等待；完成后用户可选择 7 天或无限期允许安装，并仍会看到警告。具体开放状态以 Android 版本/设备为准。 |

**有限范围分发上限复核（2026-10-24）：**本轮重开[英文专用指南](https://developer.android.com/developer-verification/guides/limited-distribution)（页面标注 2026-10-23 更新）和[简体中文专页](https://developer.android.com/developer-verification/guides/limited-distribution?hl=zh-cn)，两者现均写最多 20 台经最终用户明确授权的设备。英文专页上次知识库记录为 50 台；本轮当前正文中已无法复现该数字，因此将旧观察标为过时，不再据此宣称存在 20/50 官方口径冲突。指南总览、FAQ 和两篇 Android Developer Console Help 当前也都写 20 台；其中[分发计划帮助](https://support.google.com/android-developer-console/answer/16640817)说明超过 20 台应选 Full。若账号页面显示不同的实际设备上限，以该账号当前状态为准。开源指南里的“安装达到 50 次”是已有包名密钥所有权证明门槛，与可分享设备数无关。

**适用范围补充：**FAQ 说明，Google Play 分发的应用需在所有外形规格登记；Play 外分发建议各外形规格都登记以面向未来，但当前选定地区的设备侧执行只覆盖手机和平板。FAQ 还称，全面受制裁地区的开发者可能无法完成验证，但验证检查不会在实体位于此类地区的认证设备上运行；这不等于开发者在其他地区或其他设备上获得豁免。FAQ 中不同问答的更新时间和 rollout 文字不一致，应以更新的现行总览、专页和账户页面分别确认。

## 包名注册和签名密钥

### 仅在 Google Play 之外分发

使用 Android 开发者管理中心创建账号并验证身份。包名注册通常要提交唯一包名和应用签名密钥的 SHA-256 证书指纹。对于已由其他开发者使用的包名，注册者可能需要用自己的私钥签署 APK，并将管理中心提供的验证代码放入 APK 资源后上传，以证明控制权。若现有密钥不符合条件，可申请共享/例外，但需提供使用理由并接受审核。

重复包名的优先权按已知安装量计算：一个密钥占总安装量超过 50% 时，该开发者优先；若没有多数密钥，安装量至少 50 次的密钥持有者可注册；如果没有达到该规模的密钥，则由已有密钥者先到先得。失去签名私钥可能导致无法注册；官方建议安全管理密钥。一个包名可添加并验证多个密钥。

### 在 Google Play 上分发

使用 Play 管理中心统一管理 Play 内外分发的应用包。符合条件且使用 Play App Signing 的应用可自动识别/注册；新建 Play 应用时包名会自动关联账号。如果包名已被其他开发者使用，Console 会要求选择其他包名。Play 开发者还应在 Console 的 Android 开发者验证页面查看逐应用状态；Android Studio Panda 4+ 也会显示注册状态。

### Managed Google Play 私有应用：不要把两种豁免混为一谈

从 **2026-09-30** 起，部署到未受管理的 Play Protect 认证 Android 设备上的私有应用，必须关联已验证的开发者身份并登记包名，才能继续安装或更新。该规则的“受管理”指通过 EMM/MDM 纳入 Android Enterprise 管理，包括全托管设备或工作资料；个人或未注册设备属于未受管理设备。仅分发到受管理设备或工作资料的私有应用无需完成这项设备侧登记。

可按分发和设备路径选择：

1. **Play Console：**Google Play 分发的主要管理入口。开发者可以在此验证身份；使用 Play Console 时，无需再通过 Android Developer Console 重复登记同一应用包名。FAQ 还说，Play Console 可统一管理 Play 内外分发应用的验证要求。
2. **Android Developer Console：**供 Play 外分发的开发者验证身份并登记包名；它不是应用发布平台。私有应用需要覆盖未受管理设备、且尚未在 Play Console 完成身份验证时，可用该路径。当前帮助页要求全面分发组织账号、企业域名邮箱、名称/地址/D-U-N-S 匹配的 Google Payments Profile、联系人邮箱验证以及 25 美元注册费。登记现有包名须提交 SHA-256 签名证书指纹，并用生产私钥完成加密挑战：把 nonce 放入临时 APK 的 assets，签名后上传以证明密钥控制权。若签名密钥由 Google Play 管理，帮助页称后续会提供具体步骤。
3. **纳入 Android Enterprise 管理：**把设备注册到 EMM/MDM 后，私有应用适用设备侧验证豁免；范围包括全托管设备和工作资料。
4. **用户高级流程：**用户可在 Android 开发者选项中开启高级流程，手动允许未登记的私有应用在未受管理设备安装。它是用户主动承担风险的安装通道，不等同于开发者身份验证或 Play 政策审核通过。

不要把 Play 目标 API 要求中“永久私有、只供特定组织内部使用”的例外，推导成设备侧开发者验证豁免。身份注册、Play 上架/政策审核、设备管理状态是不同检查。发布前应按目标设备实际 EMM 注册状态判断覆盖面，并在对应 Console 查看账号和包名状态。详见[Android Enterprise 私有应用开发者验证帮助](https://support.google.com/work/android/answer/17266330?hl=en)、[Android Enterprise 设备术语](https://developers.google.com/android/work/terminology)和[Play 私有应用发布专题](../play-console-requirements/play-console-requirements.zh-CN.md)。

### API 和状态查询

- **Android Developer ID Status API**：查询包名注册状态和资格。
- **Android Developer Console API**：在开发环境或 CI/CD 中注册包名、管理密钥；支持 OAuth 委托。
- FAQ 指出 Play Console、Android 开发者管理中心和 Android Studio 都可显示状态；实际包名所有权/自动注册仍须在团队自己的账号中确认。
- FAQ 的状态查询答案直接链接到 [Android Studio Panda 4 发行说明](https://developer.android.com/studio/releases/past-releases/as-panda-4-release-notes)：生成签名 App Bundle 或 APK 时显示登记状态。这是构建时检查/提示，不会替开发者登记包名、验证身份或证明 Play 政策审核通过。

## 开源商店登记、Play 手工登记与自动化最佳实践

### 开源分发平台

Android 官方的[开源平台登记指南](https://developer.android.com/developer-verification/guides/open-source-app-registration)说明：登记并不是继续在开源平台分发的前置条件；但未登记应用的用户需要在设备上完成高级流程，登记后用户可保持熟悉的安装体验。已集成 Android Developer Console API 的商店可以代开发者处理包名和密钥登记，但开发者仍须有经过验证的 Android Developer Console 或 Play Console 身份，并把应用关联到该身份。

- **新应用、商店沿用开发者密钥：**登记包名并添加该密钥的 SHA-256 证书指纹。
- **商店重新签名：**在原签名外添加商店签名证书的指纹。若应用在商店登记前已达到 50 次或更多 Android 安装，可能要走现有应用的密钥所有权证明。
- **已有应用由商店重新签名：**从商店取得最终签名 APK，选择符合条件的证书；在应用 `assets/adi-registration.properties` 写入控制台生成的验证片段，发布含文件的版本，再从商店下载最终 APK 并上传以证明密钥所有权。
- **Play Console 的通用登记帮助页**同样要求现有包名提交对应私钥签署的 APK；若密钥委托给第三方商店，上传该商店最终签名的 APK。不要用本地未经过商店重签的构建物代替。

### API 集成最佳实践

[Android Developer Console API 指南](https://developer.android.com/developer-verification/guides/developer-console-api)面向第三方商店和个人开发者，支持程序化登记包名、管理密钥和证明密钥所有权。调用需要 OAuth 2.0 Web Server 流和 `androiddeveloperconsole` scope；由于账号数据属于 Google 账号，文档不支持用 API key、Service Account 或 Workload Identity Federation 代替用户授权。

面向开发者的集成界面应在打开 OAuth 同意页前说明为何需要账户访问；列出已授权账号并清楚显示账户名称/验证状态、包名登记状态和密钥指纹/状态；未验证账号应提示先完成验证。品牌规范要求按钮使用“Continue with Google”或“Sign in with Google”，产品名称写全 Android Developer Console，称“package name”并说“register a package name”，不能把它简写为 ADC 或“claim a package”。这些是 API 集成界面的官方建议/品牌要求，不是所有开发者都必须使用该 API 的政策。

不要混淆两套 API：只读的 [Android Developer ID Status API](https://developer.android.com/developer-verification/guides/check-registration-status) 可查询包名是否已登记，也可核对“包名 + SHA-256 指纹”是否与已登记密钥匹配；它使用 Google Cloud API key，默认配额为每项目每天 1,000 次。响应状态区分 `REGISTERED`、`NOT_REGISTERED` 和 `REGISTERED_WITH_ANOTHER_CERTIFICATE_FINGERPRINT`。该 API 只能查状态，不能替开发者完成登记；会改变包名/密钥状态的 Android Developer Console API 才需要 Google 账号 OAuth 授权。

#### Android Developer Console API 的登记方法链

Android 的 API 集成指南把 REST 方法嵌入操作流程中，而不是提供可逐项核对的完整请求/响应参考：

| 阶段 | 指南列出的 API 方法 | 用途与分支 |
| --- | --- | --- |
| 选择账户 | `ListDeveloperAccounts` | 列出当前 OAuth 授权涵盖的开发者账号；界面应显示 `displayName` 和 `verificationState`。`NOT_VERIFIED` 账号须先完成身份验证，不能继续登记。 |
| 读取包名与密钥 | `ListAndroidPackages`、`ListAndroidPackageKeys` | 展示账号下的包名、登记状态、SHA-256 指纹及密钥状态，供用户核对目标包名和签名密钥。 |
| 判断登记路径 | `CreateAndroidPackage`、`GetAndroidPackageRegistrationPolicy` | 新包名以签名公钥登记；已有包名先取得已知密钥和 `keySelectionStrategy`。`SELECT_KEY_FROM_LIST` 要从 `knownKeys` 选择并证明密钥所有权；`USE_ANY_KEY` 允许提交密钥，不要求该所有权证明。 |
| 添加密钥 | `CreateAndroidPackageKey` | 将所选或新增公钥密钥关联到包名；不能把创建密钥记录与完成登记/审核混为一谈。 |
| 证明密钥所有权 | `VerifyAndroidPackageKeyOwnership` | 在需要证明的路径中取得 `verificationToken`，写入 `assets/adi-registration.properties`，用对应私钥签署 APK 后提交验证。由商店托管密钥时，集成方须按指南自动处理该证明并告知开发者。 |
| 提交业务理由 | `JustifyAndroidPackageKeyRegistration` | 仅当已知密钥的 `justificationRequired` 为 `REQUIRED` 时提交详细理由；官方页面称审核可能需要最多 24 小时。 |

**状态字段边界：**同一指南的术语表把密钥状态写为 `DRAFT`、`OWNERSHIP_VERIFIED`、`IN_REVIEW`、`REGISTERED`、`PENDING_TRANSFER`，而界面建议一节列出 `REGISTERED_ACTIVE`。这里保留为来源页内部的状态标签差异；本轮没有取得可读的 machine-readable API schema，因此不把两个值自行合并，也不推断完整状态机、HTTP 请求体、错误码或重试语义。集成应按当前 API 响应和可用参考文档实现。

以上是 API 集成工作流与界面建议，不要求所有 Play 开发者接入该 API；Play 的包名登记义务、身份验证和 Console 操作仍以对应正式政策/账号状态为准。

### Play Console 手工登记与排查

Play Console 的[包名登记说明](https://support.google.com/googleplay/android-developer/answer/16984799)称，**2026-09-30 起所有 Play 包名都须登记**；截至本页核对日该日期已过。Console 会自动登记符合条件的应用，但应在首页及逐应用的 Android developer verification 页面核对结果。未自动登记时，按提示选择可用指纹、把验证片段放入 `assets/adi-registration.properties`、签署并上传证明 APK；帮助页说明这不是提交实际应用 APK。若指纹不符合登记资格，需提交业务理由且可能被拒；只有合理的包名共用理由才应申请，否则可评估改用新包名。新增密钥通常需要数分钟传播。

#### Play Console 包名登记帮助的正文与 8 项侧栏子页

2026-10-23 逐项重开包名登记帮助分支。`answer/16761053` 的帮助中心侧栏共有 8 个登记相关入口（含其自身和父级登记帮助）；下表逐项记录正文、页面关系及访问结果，不把侧栏导航误称为父文正文链接。

| 帮助侧栏目标 | 内容及其在登记流程中的作用 | 核验状态 |
| --- | --- | --- |
| [取得 SHA-256 证书指纹](https://support.google.com/googleplay/android-developer/answer/16641489) | 用 `apksigner` 从已签名 APK 或用 `keytool` 从 keystore 读取公钥证书指纹，为选择/核验登记密钥提供输入。 | Play Console 与 Android Developer Console 两个帮助版本均已打开；分享公钥指纹不等于泄露私钥或密码。 |
| [Play Console 包名登记帮助](https://support.google.com/googleplay/android-developer/answer/16984799) | 说明 2026-09-30 起所有 Play 包名须登记、自动登记资格、身份状态、手动登记和不合格密钥申请。 | 正文已完整打开；本页中的操作需结合账号内实际状态。 |
| [Registering Android package names](https://support.google.com/googleplay/android-developer/answer/16761053) | 区分新包名与已存在包名；列出签名密钥安装量资格、私钥控制证明、第三方商店最终签名及附加密钥流程。 | 正文已完整打开；其 8 项相关侧栏逐项复核。 |
| [Select a key for an existing package name](https://support.google.com/googleplay/android-developer/answer/16762143) | 为已有包名选择满足自动登记资格的签名密钥；不符合资格时需走申请并提供理由。 | 正文已打开；指纹指南和登记步骤已交叉核对；页面支持表单已查看但未提交。 |
| [Sign and upload an APK](https://support.google.com/googleplay/android-developer/answer/16761055) | 将 Console 提供的 `adi-registration.properties` 验证文件放入 APK assets，并用与所选公钥匹配的私钥签署后上传；若由第三方商店持有密钥，应使用其最终签名 APK。 | 正文已打开；GitHub 官方示例 README 与 `app/src/main/assets/adi-registration.properties` 路径已核对；支持表单已查看但未提交。 |
| [Add additional keys](https://support.google.com/googleplay/android-developer/answer/16762301) | 为已登记包名添加其他签名密钥；变更通常需数分钟传播，某些情形需要再次证明私钥控制权。 | 正文已打开并摘要；与主登记步骤交叉核对。 |
| [How Android developer verification uses Play identity data](https://support.google.com/googleplay/android-developer/answer/16762390?hl=en) | Play 中已验证且保持准确的身份资料会用于 Android 开发者身份；法定名称/地址来自付款资料，可在开发者账号 About 页维护，在身份页只读查看。 | 英文正文已打开并摘要；这是身份来源说明，不构成登记豁免。 |
| [Play Console developer-verification walkthrough videos](https://support.google.com/googleplay/android-developer/answer/17216631) | 视频索引列出自动登记、新建应用和手动登记三类演示。 | 索引页已打开；三个 YouTube 目标均缓存未命中，未从标题推断视频内容。 |

签名帮助页另链到 [Android 官方 APK 签名示例](https://github.com/android/security-samples/tree/main/AndroidDeveloperVerificationAPKSigningExample)。README 说明 `adi-registration.properties` 的放置结构，仓库中的 `app/src/main/assets/adi-registration.properties` 示例文件也已打开；示例值只是占位内容，不能拿来证明真实应用的密钥控制权。示例仓库其余 Gradle、Manifest、源代码和资源文件未逐一审计。两个帮助页链接的[包名登记支持表单](https://support.google.com/googleplay/android-developer/contact/package_registration_issue)仅查看字段，未提交；表单要求账号/应用资料、问题类别及证据材料，不代表个案已受理或获批。

用户端帮助页[了解 Android developer verification](https://support.google.com/android/answer/17065026)写明保护适用于认证 Android 设备，AOSP/未认证设备不在范围内，并列出受制裁地区及不支持 Google Mobile Services 的地区限制；其中写 Android 8+，而开发者总览的 2026-09-30 条目写 Android 7+。官方页面对系统版本存在表述差异，本专题保留两者，不据此推断设备资格；发布前以实际目标设备和最新 Android 官方指南为准。

## 2026 年新增指南与公告

[2026-06-18 公告](https://android-developers.googleblog.com/2026/06/android-developer-verification.html)记录 2026-07-15 Play Console 要求更新，提示开发者在 2026-09-30 前检查未自动登记应用、并宣布 Android Developer ID Status API、Android Developer Console API 与有限分发账号的阶段计划。日期已过，阶段计划应由现行指南核验；该公告也明确开源平台不登记仍可分发，但用户安装会走高级流程。

[2026-03-30 全面开放公告](https://android-developers.googleblog.com/2026/03/android-developer-verification-rolling-out-to-all-developers.html)表示 Play 与 Android Developer Console 开始向开发者开放验证；页面于 2026-09-29 增补更正，当前地区与全球时间线应以更正后的总览页为准。它是 rollout 公告，不改变现行注册帮助页中的提交步骤。

Android 普通用户帮助页另解释 Android Developer Verifier 系统服务及一次性高级旁加载流程。Play Console 的[三段操作视频索引](https://support.google.com/googleplay/android-developer/answer/17216631)分别介绍自动登记、新建应用流程和手动登记；本次三个 YouTube 目标均因缓存未命中而无法读取，视频不作为政策条款证据。

## 关键子页及链接关系

### 总览页正文直链核对

2026-10-23 重开 [Android developer verification 总览](https://developer.android.com/developer-verification?hl=en)，逐项检查其正文 17 次链接出现，去重后为 16 个目标。当前页面仍称 99% 的 Play 应用已自动登记，并要求开发者检查应用状态、手动登记剩余包名。下表包含正文中的政策/操作链接；页眉、社交媒体、页脚的通用站点导航不计作政策正文子页。链接目标的内容、访问限制及与当前要求的关系分别记录如下。

| 总览页直接链接目标 | 目标页内容及其与总览的关系 | 访问/核对结果 |
| --- | --- | --- |
| [参与商店名单 / Guides hub](https://developer.android.com/developer-verification/guides)（正文出现两次） | 指南中心列出初期 7 个参与渠道：Google Play、HONOR App Market、OPPO App Market、Galaxy Store、Palm Store、V-Appstore、GetApps；其比较表称有限分发最多 20 台。 | 英文总览页面标注更新于 2026-08-18，中文总览为 2026-09-11；两者的 20 台上限与本轮重开的中英文专页、FAQ 和两篇 Console Help 一致。 |
| [认证 Android 设备说明](https://www.android.com/certified/) | 面向消费者说明 Android 设备认证及 Google 服务；支持“认证设备”这一范围术语，不定义开发者验证流程或例外。 | 页面部分打开；仅作设备范围背景，不从营销说明推导额外政策。 |
| [Android Developer Console 指南](https://developer.android.com/developer-verification/guides/android-developer-console?hl=en) | 仅在 Play 外分发时使用；介绍身份验证和包名/签名密钥登记步骤。 | 正文已打开并在本专题摘要；API、协议和技术后代仍部分覆盖。 |
| [Android Developer Console 注册入口](https://android.google.com/developerconsole) | 登录/创建 Play 外分发所用的开发者管理中心账号。 | 目标要求 Google 账号登录；浏览工具未取得账号内注册流程，不能据此核验账号状态。 |
| [Play Console 指南](https://developer.android.com/developer-verification/guides/google-play-console?hl=en) | Play 分发或 Play 内外并行分发时，使用现有 Play Console 管理身份和包名登记。 | 正文已打开并在本专题摘要；相关手工登记帮助子页另有记录。 |
| [Play Console 注册入口](https://play.google.com/console/signup) | Play Console 账号入口。 | 点击后转至 Google 登录；账号创建及具体任务需登录后查看。 |
| [Android developer verification FAQ](https://developer.android.com/developer-verification/guides/faq?hl=en) | 展开身份、费用、区域执行、企业/ADB、密钥、API 和高级流程等问答；Play 应用需覆盖所有外形规格登记，Play 外当前设备侧执行限手机和平板；设有全面受制裁地区的设备侧检查例外。 | 页面标注 2026-09-30 更新；有限分发条目（2026-06-18 更新）仍写最多 20 台，但“8 月推出”是过时 rollout 措辞，不改变本轮核实的 20 台上限。 |
| [Android Developer Console Help Center](https://support.google.com/android-developer-console) | Console 的账户和使用支持入口。 | 帮助中心入口已打开；账号工单和登录后支持内容不能匿名读取。 |
| [Play Console Help Center](https://support.google.com/googleplay/android-developer) | Play Console 的账户及操作支持目录，链接到现有包名登记帮助等具体文章。 | 目录已打开；将其视为支持导航，不把目录本身当作新增政策条款。 |
| [高级流程：保障侧载选择与反胁迫设计](https://android-developers.googleblog.com/2026/03/android-developer-verification.html) | 说明用户安装未验证开发者应用的一次性安全流程。该用户侧选择机制与开发者身份/包名登记是不同控制层。 | 公告全文及其正文直链已另行核对，见下节；现行操作以当前指南和 FAQ 为准。 |
| [开源应用登记指南](https://developer.android.com/developer-verification/guides/open-source-app-registration) | 说明开源平台是否必须登记、平台重签密钥和证明现有包名控制权的流程。 | 全文已打开并摘要；技术/平台后代状态见本专题表格。 |
| [有限范围分发账号指南](https://developer.android.com/developer-verification/guides/limited-distribution) | 英文版标注 2026-10-23 更新、中文版标注 2026-09-30 更新；本轮重开后两者均称免费分享至最多 20 台用户授权设备。均列出 Google 账号、两步验证、付款资料和联系邮箱要求，不需要政府证件。 | 中英文专页正文现在对上限一致；较早知识库记录的英文“50 台”已被本轮正文复核取代。 |
| [2026-06-18 更新公告](https://android-developers.googleblog.com/2026/06/android-developer-verification.html) | 回顾 7 月 Play 要求、9 月期限、API 与有限分发计划。 | 全文已打开；已过的计划日期由当前指南核对，不以旧公告替代当前要求。 |
| [2026-03-30 开放注册公告](https://android-developers.googleblog.com/2026/03/android-developer-verification-rolling-out-to-all-developers.html) | 记载 Play Console 与 Android Developer Console 面向开发者开放验证；正文后来更正地区和全球 rollout 时间。 | 全文已打开；当前区域执行范围以现行总览为准。 |
| [高级流程预览视频](https://www.youtube.com/shorts/WcPElxbOeXY) | 总览页引用的用户侧视频。 | 视频正文抓取失败/缓存未命中；不从标题推断视频内容。 |
| [Android developer verification 简介视频](https://www.youtube.com/watch?v=A7DEhW-mjdc) | 总览页引用的计划简介视频。 | 视频正文抓取失败/缓存未命中；不从标题推断视频内容。 |

### FAQ → Android Studio Panda 4 登记状态子链

2026-10-23 重开 [Android 开发者验证 FAQ](https://developer.android.com/developer-verification/guides/faq?hl=en)：其“Where can I check the status of my package registration?”答案把 Android Studio 列为第三个状态查询位置，并直接链接到 [Android Studio Panda 4 发行说明](https://developer.android.com/studio/releases/past-releases/as-panda-4-release-notes)。发行说明的“Developer verification support”段称，生成签名 App Bundle 或 APK 时会显示应用登记状态，便于在构建时发现问题；页面最后更新时间为 **2026-06-02 UTC**。这只是读取/展示包名登记状态的构建期检查，不是登记操作、身份验证或 Play 政策审核结论。该段的 [verification requirement](https://developer.android.com/developer-verification) 回到本专题已审阅的现行总览；页面页脚的 [Android 内容许可](https://developer.android.com/license)已有独立访问记录。Panda 4 页面其余 Gemini、AI 编辑器和 IDE 功能链接不属于开发者验证政策范围，未继续展开。

**范围解读：** 指南中心称认证设备上的应用需由已验证开发者登记；现行总览明确这是分阶段执行：2026-09-30 起，巴西、印度尼西亚、新加坡和泰国的认证 Android 7+ 设备，仅对 7 个参与商店开始设备侧保护；2027 年及以后继续全球扩展。FAQ 另写 Play 开发者应登记各外形规格应用，而初期 Play 外强制执行只涉及选定地区的手机和平板。不要把长期要求、Play Console 的账号/包名工作和初期设备侧拦截混为一谈。

### 高级流程公告的正文链接与作用

[2026-03-19 高级流程公告](https://android-developers.googleblog.com/2026/03/android-developer-verification.html)说明：用户先打开开发者选项，通过反胁迫确认，重启设备并重新验证；等待一天后用生物识别或设备 PIN 确认，之后可选择允许 7 天或无限期安装未验证开发者应用，但仍会看到风险警告。有限分发路径则面向小范围分享。公告是设计/解释材料；当前生效范围和实际可用状态以开发者验证总览、指南和 FAQ 为准。

| 高级流程公告的正文链接 | 目标及关系 | 核对状态 |
| --- | --- | --- |
| [2025-08 首次公告：认证设备的新安全层](https://android-developers.googleblog.com/2025/08/elevating-android-security.html) | 说明开发者身份核验与应用内容审核/下载来源无关，并给出分阶段计划；旧日期已被后续公告更新。 | 全文已打开；当前日期与范围以现行总览为准。 |
| [2025-11 社区反馈与早期体验公告](https://android-developers.googleblog.com/2025/11/android-developer-verification-early.html) | 汇总学生/爱好者需要有限分发、资深用户希望保留侧载选择等反馈；介绍有限分发账号及高级流程的设计方向。 | 全文已打开；“early access”阶段已结束，不能当作现行注册入口。 |
| [GASA 2025 全球诈骗报告说明](https://gasa.org/knowledge-base/blog/global-scams-on-the-rise-over-half-of-adults-worldwide-report-scam-encounters) | 为公告解释反胁迫设计提供背景调查；该研究并非 Google Play 要求。页面称 57% 受访成年人过去一年遇到诈骗、23% 损失金钱；具体统计口径应以该报告为准。 | 文章已打开。其下载按钮跳转到 GASA 知识库列表，没有取得 PDF；Google 公告中的其他总损失估算不据此单独背书。 |
| [GASA 网站](https://gasa.org/) | 报告发布组织主页，不产生 Play 开发者义务。 | 主页已打开；仅作为来源背景。 |
| [Android 开发者选项开启说明](https://www.android.com/intl/en_uk/articles/enable-android-developer-settings/) | 消费者说明如何在设备设置中开启开发者选项；具体菜单随设备而异。 | 正文已打开；它是高级流程的前置操作说明，不等于验证豁免。 |
| [现行 Android developer verification 总览](https://developer.android.com/developer-verification) | 指向当前范围、Console 路径和时间线。 | 全文已打开并在本节上文逐项核对。 |

公告页通用导航、分享、隐私/许可页不属于高级流程的政策性正文子链接；官方政策和帮助页面之间的关系见上表及下方总览子页清单。

| 页面 | 摘要及与主指南的关系 | 核对状态 |
| --- | --- | --- |
| [Android 开发者验证总览](https://developer.android.com/developer-verification?hl=zh-cn) | 解释适用范围、区域/全球时间线、分发路径和包名注册步骤。 | 正文已打开并纳入本页。 |
| [Android 开发者管理中心注册](https://developer.android.com/developer-verification/guides/android-developer-console?hl=zh-cn) | 仅 Play 外分发：验证后注册包名、SHA-256 指纹；已用包名通过签名 APK 资源挑战证明所有权；说明重复包名的安装量分配规则和注册 API。 | 正文已打开并摘要。 |
| [全面分发账号](https://developer.android.com/developer-verification/guides/full-distribution?hl=zh-cn) | 组织/专业分发、无限制分发、个人身份证件和地址证明；组织需 D-U-N-S、验证网站和法定组织文件。 | 正文已打开并摘要；证件清单依国家/地区变化。 |
| [有限范围分发账号](https://developer.android.com/developer-verification/guides/limited-distribution?hl=zh-cn) | 中文本地化正文称免费分享至最多 20 台用户授权设备，标注 2026-09-30 更新；与本轮重开的英文现行正文一致。 | 中英文现行正文均写 20 台；逐 URL 审计保留本轮英文专页复核及先前 50 台观察被取代的记录。
| [Play 管理中心注册指南](https://developer.android.com/developer-verification/guides/google-play-console?hl=zh-cn) | 已有 Play 身份多可复用；检查自动登记状态，Play 新应用自动关联包名，已在 Play 外使用的包名可继续使用。 | 正文已打开并摘要。 |
| [开源应用登记指南](https://developer.android.com/developer-verification/guides/open-source-app-registration) | 开源平台可以继续分发未登记应用，但用户需使用高级流程；平台重签时要登记其签名密钥，并可能对已有包名证明所有权。 | 正文已打开；密钥 SHA-256、现有包名证明和 Android Developer Console API 后代已打开并整理。 |
| [Android Developer Console API 指南](https://developer.android.com/developer-verification/guides/developer-console-api) | OAuth 2.0 下程序化注册包名与密钥；含账户、包名、密钥状态显示及 OAuth 授权界面的最佳实践和品牌要求。 | 2026-10-23 复核：正文 16 次链接引用、13 个唯一外部目标及 2 个页内锚点均逐项处理；命名方法与登记流程已按当前正文映射到上文。完整请求/响应 schema、错误码、代码示例和更深技术后代仍部分覆盖；来源页的 `REGISTERED` / `REGISTERED_ACTIVE` 标签差异单独标注。 |
| [Android Developer ID Status API 指南](https://developer.android.com/developer-verification/guides/check-registration-status) | 只读检查包名登记状态，或检查包名与签名证书指纹是否匹配；使用 Cloud API key，默认每天每项目 1,000 次。 | 2026-10-23 复核：已读状态值、API key 设置和 Cloud 项目步骤；示例代码及 Cloud 配额/安全配置后代未全部展开。不可与需 OAuth 的 Console 登记 API 混为一谈。 |
| [Play Console 包名登记帮助](https://support.google.com/googleplay/android-developer/answer/16984799) | 2026-09-30 起所有 Play 包名须登记；解释自动登记、手动登记、身份状态检查、不合格密钥申请和证明 APK。 | 正文已打开；相关 8 项 Help 侧栏及直接操作子页均已逐项打开，见上方登记分支表。 |
| [Registering Android package names](https://support.google.com/googleplay/android-developer/answer/16761053) | 新旧包名登记差异、>50%/50 次安装资格、现有密钥证明、第三方商店委托签名和附加密钥。 | 正文和 8 项相关侧栏已逐项打开；官方示例已核到 README 与 `app/src/main/assets/adi-registration.properties`，仓库其余文件树未穷尽。 |
| [取得 SHA-256 证书指纹](https://support.google.com/googleplay/android-developer/answer/16641489) · [Android Developer Console Help 版](https://support.google.com/android-developer-console/answer/16641489) | 介绍使用 apksigner/keytool 从签名 APK 或 keystore 读取公钥证书指纹。 | 两个帮助页版本均已打开；公开指纹可用，不应分享私钥或密码。 |
| [添加其他密钥](https://support.google.com/googleplay/android-developer/answer/16762301) | 已登记包名可添加签名密钥；传播需要数分钟，部分情形仍要提交 APK 验证私钥控制权。 | 正文已打开并摘要。 |
| [Android 验证如何使用 Play 开发者身份数据](https://support.google.com/googleplay/android-developer/answer/16762390?hl=zh-CN) | Play 账号已验证且维护准确的信息会成为 Android 开发者身份；法定名称/地址来自付款资料，可在开发者账号 About 页面修改，并在身份页只读查看。 | 英文正文已打开并摘要；帮助中心子导航部分与登记流程重复。 |
| [Android Developer Verifier 用户说明](https://support.google.com/android/answer/17065026) | 说明用户端安装阻止、高级流程、区域/认证设备范围和系统服务；Android 版本口径与开发者总览有差异。 | 正文已打开；记录为用户说明而非开发者注册步骤。 |
| [Play Console 开发者验证操作视频](https://support.google.com/googleplay/android-developer/answer/17216631) | 三段视频覆盖自动登记、新建应用和手动登记。 | 视频索引正文已打开；三个 YouTube 页面均缓存未命中。 |
| [Android 开发者验证总览的用户侧视频](https://www.youtube.com/shorts/WcPElxbOeXY) · [Android developer verification 简介](https://www.youtube.com/watch?v=A7DEhW-mjdc) | 面向用户介绍侧载高级流程和验证计划。 | 两个 YouTube 目标均缓存未命中；不从标题推断视频细节。 |
| [2026-06-18 更新公告](https://android-developers.googleblog.com/2026/06/android-developer-verification.html) | 记录 7 月 Play 要求更新、9 月登记截止日、API 推出和有限分发账号计划。 | 公告全文已打开；计划/期限用现行总览核验，公告不替代现行 Console 步骤。 |
| [2026-03-30 面向所有开发者开放公告](https://android-developers.googleblog.com/2026/03/android-developer-verification-rolling-out-to-all-developers.html) | 记载 Play 与 Android Developer Console 分阶段开放验证；页面在 2026-09-29 更正地区和全球时间线。 | 公告全文已打开；当前范围以更正后的开发者验证总览为准。 |
| [Android 开发者内容许可](https://developer.android.com/license) | Android 文档/代码样例有 Apache 2.0 等许可，其他网站内容通常为 CC BY 2.5；商标不包含在许可内，外链内容也不自动受同一许可覆盖。 | 正文已打开；本知识库使用改写摘要和来源链接，不复制整篇政策正文。 |
| [Android Enterprise 私有应用开发者验证](https://support.google.com/work/android/answer/17266330?hl=en) | 自 2026-09-30 起，未受管理的 Play Protect 认证设备上的私有应用须关联已验证身份并登记包名；全托管设备、工作资料适用豁免。说明 Play Console、Android Developer Console、企业设备管理和用户高级流程四种路径。 | 英文正文已打开；组织账号资料、25 美元费用、SHA-256 与 nonce APK 密钥挑战均已摘要。 |
| [Android Enterprise 术语](https://developers.google.com/android/work/terminology) · [认证设备说明](https://www.android.com/certified/) · [Android Enterprise 管理概览](https://www.android.com/enterprise/management/) | 解释全托管、工作资料、EMM 与 Play Protect 认证设备的范围。前两类技术/消费者说明用于界定适用设备；不增加 Google Play 政策义务。 | 页面已打开；设备认证页与管理概览仅作背景资料。 |
| [私有应用开发者验证 FAQ](https://developer.android.com/developer-verification/guides/faq) | 覆盖账号类型、费用、Android 版本/地区 rollout、企业应用、ADB、签名密钥、包名状态、CI/CD API 和高级旁加载流程。 | FAQ 正文已打开；部分条目有各自更新时间，子链接和 Console 具体状态仍须按适用情形核实。 |
| [开发者验证 FAQ](https://developer.android.com/developer-verification/guides/faq?hl=zh-cn) | 说明账号/费用、受制裁地区、ADB/企业例外、密钥、自动注册、CI/CD API 和高级流程；高级流程包括 24 小时等待与 7 天/无限期启用选项。 | 主要章节已打开并整理；FAQ 部分条目可能滞后于时间线，账号与设备可用性需实时核实。 |
| [安全公告：认证 Android 设备新增保护层](https://android-developers.googleblog.com/2025/08/elevating-android-security.html) | 2025 年公告把开发者验证解释为身份问责层，并预告 2026 年从受影响地区开始执行。原文现已更新：早期访问于 2026-04-21 关闭、面向所有开发者开放；现行指南确认保护自 2026-09-30 起在巴西、印度尼西亚、新加坡和泰国生效，并计划 2027 年后继续全球扩展。 | 公告全文已打开；现代指南优先于历史时间措辞。其旧 Android Developer Console 预览链接返回 404；[认证设备合作厂商目录](https://www.android.com/certified/partners/)只说明受保护设备范围，不是开发者政策。 |
| [2023 开发者身份与 Play 透明度公告](https://android-developers.googleblog.com/2023/07/boosting-trust-and-transparency-in-google-play.html) | 历史背景：组织账号 D-U-N-S、账户资料核验，以及商店页展示已验证开发者身份信息。它是当时变更公告，不能代替 2026 年现行包名注册和设备侧保护规则。 | 公告全文已打开；当前账号资料子页见下两行；旧版 Play Console Requirements URL 抓取被 Google 反机器人页阻断，现行规则见本库当前要求专题。 |
| [创建 Play Console 开发者账号所需信息](https://support.google.com/googleplay/android-developer/answer/13628312) | 区分个人/组织开户资料、公开开发者资料与 Google 联系信息；列出组织 D-U-N-S、付款资料对齐、验证联系方式和收款方式，强调 D-U-N-S 免费申请及避免付费代办。 | 正文已打开并摘要；后代涉及账号类型、身份、付款和联系最佳实践，部分需登录或按地区变化。 |
| [验证开发者身份信息](https://support.google.com/googleplay/android-developer/answer/10841920?hl=en) | 说明法定身份、公开开发者资料与仅供 Google 使用的联系方式的验证顺序；涵盖身份证件、组织 D-U-N-S、网站/设备核验、付款资料匹配、账户资料最佳实践和验证失败后果。 | 英文正文已完整打开；正文中的账号类型、地区文件、韩国分发、网站/设备验证等目标已分别打开或链接到现有摘要；其中两个“最佳实践”入口是页内锚点，实际建议已归纳于下文。 |
| [保持开发者账号信息最新](https://support.google.com/googleplay/android-developer/answer/13634888) | 说明新账号需持续维护法定名称/地址、D-U-N-S 对齐、联系与公开开发者信息；资料失效可能导致商店开发者资料和应用移除。组织名称/地址须先更新 D&B，再在 Console 完成重新验证；商家还须验证收款方式。 | 正文已打开并摘要；页面另有国家/地区 D-U-N-S 代理商目录、表单和 Help Center 子链，本轮未把各市场供应商条目逐一展开。 |
| [已通过 Play Console Requirements 验证的账号：查看和管理开发者账号信息](https://support.google.com/googleplay/android-developer/answer/13634081) | 仅适用于已完成 Play Console Requirements 验证的账号；所有者才能修改资料。正文区分商店联系资料、Google 私下联系资料、公开开发者联系资料和付款资料中的法定身份信息，并说明通知、迁移和删除账号的后果。 | 英文正文已完整打开；23 个正文链接出现、20 个唯一目标；15 项账号设置侧栏已逐项映射。账号专属操作入口需登录；字段摘要见下文及[Play Console 用户权限专题](../play-console-user-permissions/play-console-user-permissions.zh-CN.md)。 |
| [更新由 Google 付款资料管理的开发者身份信息](https://support.google.com/googleplay/android-developer/answer/16260648) | 说明在同一国家更新姓名/地址、切换国家或 D-U-N-S 时改用新付款资料，以及个人账号转组织账号的前置条件和步骤；组织账号转个人账号不支持。 | 英文正文已完整打开；6 个正文目标已逐项映射。身份核验、网站验证和应用转移页已打开；Play Console 与账号内支持入口需登录；公开支持表单已检查但未提交。15 项设置账号侧栏与正文链接分别统计。 |
| [2023 公告所链的 Play Console Requirements 旧入口](https://support.google.com/googleplay/android-developer/answer/13583557) | 历史公告所引用的政策入口。 | 公开抓取跳转 Google 反机器人页面（HTTP 500）；当前版本见[Play Console 要求专题](../play-console-requirements/play-console-requirements.zh-CN.md)。 |
| [Android Developer Console 预览说明旧链接](https://support.google.com/android-developer-console/answer/16450960) | 2025 安全公告中的早期预览链接。 | 当前返回 404；不用于判断现行注册规则。 |
| [Play Console 要求](https://support.google.com/googleplay/android-developer/answer/10788890?hl=zh-CN) | 自 2026-09-30 起要求登记希望继续分发的 Play 应用包名；另含账号身份、开发者信息及审核资源要求。 | 正文已读，细则另见[Play Console 要求专题](../play-console-requirements/play-console-requirements.zh-CN.md)。 |
| FAQ 指向的高级流程视频/博客、Android Developer Console/Play Console 帮助中心及身份验证专用帮助文章 | 分别用于设备操作演示、控制台操作和账号专属支持。 | 部分视频/帮助中心需登录或因访问限制未逐页展开；本页不将主指南的摘要误当作这些子页面已全部审阅。 |

### Android Developer Console API 指南：正文子链接逐项核对

2026-10-23 重开[Android Developer Console API 指南](https://developer.android.com/developer-verification/guides/developer-console-api)，按正文逐项处理 16 次链接引用：去重后 13 个外部目标，以及指向本页“密钥资格规则”和“验证密钥所有权”的 2 个页内锚点；重复的 Google Cloud Console 链接只计一个目标。插图和网站页眉/页脚导航不是独立政策页面。此表覆盖目标页与开发者验证流程的关系；通用 Cloud/OAuth 文档、API 方法代码示例和链接目标自身的所有后代不因此视为递归闭合。

| API 指南正文链接 | 目标内容及与验证流程的关系 | 访问与边界 |
| --- | --- | --- |
| [REST API basics](https://cloud.google.com/discover/what-is-rest-api) | 解释以资源、URI、HTTP 方法和 JSON 表示交互的 REST 架构；这是理解 Console API 调用的通用背景，不是 Play 政策。 | 正文已打开；仅记录与 API 接口有关的内容，不扩展 Cloud 产品推荐或其无关后代。 |
| [APK structure](https://developer.android.com/topic/performance/reduce-apk-size) | API 指南用 APK 结构作为密钥所有权证明的背景；目标页面是更广泛的 APK 体积优化指南。登记挑战关注在应用 `assets` 中放入验证材料并使用目标私钥签署 APK。 | 页面已打开并核对相关结构段；无关的性能优化章节不属于开发者验证要求。 |
| [Sign your app](https://developer.android.com/studio/publish/app-signing) | 区分应用签名密钥与上传密钥：Play App Signing 由 Google 管理分发签名密钥，开发者以上传密钥提交版本；公开证书/指纹可用于识别密钥，私钥和密码必须保密。 | 正文已打开并复核密钥/指纹相关章节；这是签名实现说明，不等于某个包名已完成 Android 开发者验证。 |
| [取得 SHA-256 证书指纹](https://support.google.com/android-developer-console/answer/16641489) | 展示从签名 APK 或 keystore 读取公钥证书指纹的 `apksigner` 与 `keytool` 方法，用于对照包名注册记录。 | 帮助正文已打开；可分享的是公钥证书指纹，不应提交私钥或 keystore 密码。 |
| [创建 Google Cloud 账号](https://console.cloud.google.com/freetrial) | Cloud 项目/启用 API 的账号前置步骤；不是 Android Developer Console 身份验证本身。 | 点击后发生 400 重定向循环，未取得账号创建页；按不可公开核验记录。 |
| [Google Cloud Console](https://console.cloud.google.com/) | 用于选项目并启用 Android Developer Console API。 | 跳转 Google 登录，无法公开读取账号内项目或 API 状态。 |
| [创建 Cloud 项目](https://cloud.google.com/resource-manager/docs/creating-managing-projects) | 说明项目是启用 Cloud API 与分配 IAM/资源的边界；此 Cloud 项目不取代 Android Developer Console 开发者账号。 | 目标重定向至 `docs.cloud.google.com` 后正文已打开；记录项目 ID 创建和资源用途。 |
| [OAuth 2.0 Web Server flow](https://developers.google.com/identity/protocols/oauth2/web-server) | Google 通用用户授权流程；官方建议使用客户端库、安全保存客户端凭据，并按场景管理授权码/令牌。Console API 本身要求 `androiddeveloperconsole` 用户授权 scope，且不接受 API key、Service Account 或 Workload Identity Federation 代替用户授权。 | 相关 OAuth 授权、安全和 scope 章节已打开；全篇 1,905 行及各语言库代码并未逐行摘要。 |
| [密钥资格规则](https://developer.android.com/developer-verification/guides/developer-console-api#key-eligibility-rules)（本页锚点） | 多密钥情况下，安装量超过 50% 的密钥优先；无单一多数时，达到 50 次安装的密钥符合直接登记条件；没有密钥达到门槛时先到先得。其他情形可能要求业务理由并经审核。 | 页内章节已阅读；需以注册 API 返回的当前资格和 Console 结果为准。 |
| [验证密钥所有权](https://developer.android.com/developer-verification/guides/developer-console-api#verify-key-ownership)（本页锚点） | 对需要证明控制权的已有包名，把 API 生成的验证 token 写入 `assets/adi-registration.properties`，再用对应私钥签署并提交 APK；平台代管密钥时可由集成 API 自动完成。 | 页内章节已阅读；只证明对相应签名密钥的控制，不代替身份验证或政策审查。 |
| [Sign in with Google 品牌指南](https://developers.google.com/identity/branding-guidelines) | API 集成界面要使用规定的 Google 登录按钮文字，并清楚说明授权用途；品牌页面说明登录按钮需至少与其他第三方登录选项同等醒目。 | 相关摘要与按钮要求已打开；完整图标素材和自定义按钮设计子项未逐个复核。 |
| [Android Developer ID Status API](https://developer.android.com/developer-verification/guides/check-registration-status) | 只读查询包名/证书指纹登记状态；用 Cloud API key。它可帮助发布工具发现未登记包名，但不能创建登记或证明调用者身份。 | 正文、API 状态值和项目启用步骤已打开；请求示例、配额与密钥防滥用设置的所有后代仍部分覆盖。 |
| [Register on Android Developer Console](https://developer.android.com/developer-verification/guides/android-developer-console) | Play 外分发的身份验证和包名/密钥登记指南；与 API 自动化操作互为人工/自动流程。 | 正文已打开并纳入本专题。 |
| [Register on Google Play Console](https://developer.android.com/developer-verification/guides/google-play-console) | Play 分发路径的身份与包名登记说明；Play Console 自动登记/手工核对适用流程见上文和 Play Console Requirements 专题。 | 正文已打开并纳入本专题。 |
| [Android Developers 内容许可](https://developer.android.com/license) | 说明 Android 文档、代码样例和其他网站内容可能适用不同许可；商标不包含在通用许可中。 | 正文已打开；本知识库保留来源链接并写摘要，不复制整篇外部内容。 |

### Play Console 开发者身份信息核验

[验证开发者身份信息](https://support.google.com/googleplay/android-developer/answer/10841920?hl=en)把身份核验、联系方式核验、设备/网站核验和包名登记分成不同事项。正文称开发者可以在个人账号期限前 60 天开始验证；实际期限仍以该账号 Play Console 待办为准。身份或联系信息未通过核验时，开发者可能被移除商店展示和应用，并且在补齐验证前不能重新发布。

身份资料与公开资料依账号类型不同：个人账号使用关联 Payments profile 的法定姓名/地址，先提交政府签发身份证件；组织账号还需组织法定文件和 D-U-N-S（已知政府机构可能例外）。组织名称/地址须与 D&B 档案匹配；同一企业可能有多个 D-U-N-S，须选与目标法律实体一致的编号。D-U-N-S 可向 Dun & Bradstreet 免费申请，帮助页称可能需最多 30 天；受支持国家/地区以外、无法取得 D-U-N-S 的组织应在开户前联系支持，且不能把一般组织缺号当作默认豁免。

**核验顺序与最佳实践：**开发者邮箱（用户可见）须通过 6 位验证码验证；组织公开电话也须通过验证码，个人账号电话的适用范围受地区规则影响。Google 使用的私下联系邮箱/电话同样须验证，但不会显示给用户。核验电话前，组织账号须完成身份与网站核验，个人账号须完成身份与设备核验。组织应使用长期可用、属于组织且非通用/个人邮箱的联系地址；团队账号可设置共享通知。公开的开发者邮箱/电话也必须可联系，失效可能导致应用被移除。更新邮箱或电话号码后，通常要重新验证。对于新个人账号，Play Console 移动应用的设备核验要求使用账号所有者、非 Root 的实体 Android 10+ 设备；这项账号开户核验不同于 Android 开发者包名注册，也不同于用户侧设备安装验证。

组织网站核验通常通过 Search Console 将网站与开发者账号关联：同一 Google 账号登记网站时可自动批准；否则网站所有者需批准请求。社交媒体主页不能代替可验证的网站。身份文件须与关联 Payments profile 的法定姓名、组织名和地址完全匹配。照片身份证件须有效、清晰、彩色，不能是复印件；本轮核对的 16 个地区均要求个人地址证明的姓名和地址准确匹配，并规定近 90 天签发期限。英国及 EEA 身份证件不得遮挡任何字段。帮助页地区选择器会改变材料清单，因此下表只是 16 个已核对地区的快照，不是全球清单。

### 2023 年 9 月前账号：历史验证时间线、操作流程与直接子链接

重开官方 [Verifying your Play Console developer account (for accounts created before September, 2023)](https://support.google.com/googleplay/android-developer/answer/14177239?hl=en) 全文。它服务于旧账号的分批验证，不应把其中 2023–2025 年的 rollout 日期当作当前截止日；具体账号期限、延期按钮和待办状态以 Play Console 为准。该页当前仍描述：个人期限前 60 天可开始，符合条件的账号可在 Console 申请一次 90 天延期；逾期可能导致开发者资料和应用从 Play 移除。

| 流程环节 | 官方帮助页说明 | 使用边界 |
| --- | --- | --- |
| 准备并开始 | 账号所有者在 Console 首页、个人截止日前 60 天内开始；先确认账号类型、关联身份核验 Payments profile、填写账号信息和联系方式。该文称选定账号类型后不能在此流程中更改。 | rollout 时间线属于历史信息；以当前 Console 任务和[账号类型转换帮助](https://support.google.com/googleplay/android-developer/answer/16260648)核对适用流程。 |
| 组织资料 | 组织账号需要 D-U-N-S；官方帮助称申请免费、可能需 30 天以上，输入次数有限。名称与地址须与 D&B/付款资料一致。已识别的政府组织可能可不提供 D-U-N-S；若 Console 没有该选项，使用账号内支持或公开表单。 | 一般组织缺少 D-U-N-S 不等于豁免；政府例外按账号是否被识别及 Console 是否提供路径判断。 |
| 联系信息与提交 | 分开填写供 Google 私下联系的邮箱/电话和展示给 Play 用户的公开联系资料；检查并确认付款资料，保存资料后可能还需上传有效身份证件及组织文件。提交后由账号所有者收完成邮件，审核可能需要数日。 | 公开联系方式、Google 联系方式及每个应用的客服邮箱不是同一个字段。核验照片须清晰、彩色、有效且非复印件。 |
| 商家收款核验 | 若使用 Google Play Billing 营收，还需单独验证 merchant payment details/银行账户；未验证收款银行资料也可能导致开发者资料和应用移除。 | 这是商家收款资料流程，不等同于验证开发者身份的 Payments profile。 |
| 多账号共用组织付款资料 | 组织付款资料可在多个开发者账号间复用；每个账号所有者需成为付款资料管理员，接受邀请后才能在 Console 选择该资料。增加管理员意味着对付款资料拥有完整权限。 | 先确认目标资料和访问范围，再授予管理员权限；不要把付款资料共享误解为转移开发者账号所有权。 |

该旧账号帮助页的直接正文目标按政策关系核对如下。Console 首页、Account details、Activity log、Store settings 和付款资料选择步骤会显示账号专属状态，公开页面不能代替登录核验。

| 页面关系 | 目标与本地关系 | 访问/内容状态 |
| --- | --- | --- |
| 旧账号验证 → 当前 Play Console Requirements、账号类型、开户资料 | [Play Console Requirements](https://support.google.com/googleplay/android-developer/answer/10788890)、[账号类型](https://support.google.com/googleplay/android-developer/answer/13634885)、[创建开发者账号所需信息](https://support.google.com/googleplay/android-developer/answer/13628312) | 公共正文已打开并纳入本库双语专题；当前政策优先于旧 rollout 日期。 |
| 旧账号验证 → 国家/地区证件 | [按国家/地区查看所需文件](https://support.google.com/googleplay/android-developer/answer/15633622) | 16 个英文地区及中国简体中文视图已核对；其余选择项仍未穷尽。 |
| 旧账号验证 → 组织核验指南 | [指南下载页](https://support.google.com/googleplay/android-developer/answer/15574489)：[简体中文](https://goo.gle/409YfEE)、[英文（美国）](https://goo.gle/3Yp3FLa)、[日文](https://goo.gle/3WbDDKO)、[韩文](https://goo.gle/4apTH1L)、[葡萄牙文（巴西）](https://goo.gle/3Wyk287) | 下载页已打开。五个链接都重定向到 Google 静态 PDF，但抓取返回错误；英文静态目标独立请求为 HTTP 404。PDF 正文及其内部链接未读取，不能依据文件名或第三方镜像推断。 |
| 旧账号验证 → Payments profile 与收款 | [创建开发者付款资料](https://support.google.com/googleplay/android-developer/answer/7161426)、[商家银行账户资料](https://support.google.com/googleplay/android-developer/answer/7161440)、[验证银行账户](https://support.google.com/googleplay/android-developer/answer/7161378) | 银行账户资料与验证页已全文打开，并补入下方 EFT/电汇流程摘要；创建/选择付款资料的账号专属目标仍需登录。银行核验不是身份 profile 的同一事项。 |
| 旧账号验证 → 身份文件、联系人与地区披露 | [开发者身份核验](https://support.google.com/googleplay/android-developer/answer/10841920)、[联系方式要求](https://support.google.com/googleplay/android-developer/answer/10840893)、[地区分发要求](https://support.google.com/googleplay/android-developer/answer/6223646) | 三个公共帮助页已打开并有双语摘要；页面中的国家/账号差异按对应专题记录。 |
| 旧账号验证 → Console 中的期限、资料和支持 | [Play Console 首页](https://play.google.com/console/)、账户详情、Activity log、付款资料设置、账号内支持；[无 Console 访问时的公开表单](https://support.google.com/googleplay/android-developer/contact/general_contact) | Console/Payments 操作需要账号登录；公开表单已打开但未提交。旧页中的具体账号截止日和延期资格必须在账号内核对。 |

### 地区身份材料对照（2026-10-22 核对）

下表按官方帮助页选定国家/地区后的英文视图整理；中国另核对了简体中文视图。组织登记材料、代表身份证件和个人账号材料是不同类别，不要用某一类别的文件替代另一类别。所有材料仍须服从付款资料国家/地区、账号类型及 Console 当前任务。

| 国家/地区及官方视图 | 组织登记材料（节选） | 组织代表身份证件 | 个人账号身份证件及地址证明 |
| --- | --- | --- | --- |
| [美国](https://support.google.com/googleplay/android-developer/answer/15633622) | IRS 出具/盖章并列明组织名称的文件（如符合条件的 IRS 表格）、州公司注册证明、最新 SEC 申报、商业信用报告；政府部门可用载明名称、地址和日期的官方信函。 | 护照、州身份证、驾照或永久居民卡；可由任何国家签发。 | 美国政府签发的带照片身份证件；地址证明须匹配姓名和地址，类别包括带地址的政府身份证件、水电账单、保险、信用卡或银行对账单等，通常须为近 90 天内签发。 |
| [中国](https://support.google.com/googleplay/android-developer/answer/15633622?co=GENIE.CountryCode%3DCN) · [简体中文视图](https://support.google.com/googleplay/android-developer/answer/15633622?co=GENIE.CountryCode%3DCN&hl=zh-Hans) | 营业执照、组织机构代码证；政府部门/机构可用载有完整名称、地址和日期的官方信函。 | 护照、身份证、驾照或永久居留卡；代表身份证件可由任何国家签发。 | 中国政府签发的带照片身份证件，如护照、居民身份证、驾照或居留许可；地址证明可为含地址身份证件、水电账单、保险、信用卡或银行对账单等，姓名/地址须匹配，通常限近 90 天。 |
| [印度](https://support.google.com/googleplay/android-developer/answer/15633622?co=GENIE.CountryCode%3DIN) | 公司章程、注册证书、GST 证书、组织备忘录、合伙企业登记文件、社团登记、信托契据、VAT 证书或 Udyam MSME 证书；公司 CIN 可接受。 | 护照、身份证、驾照或永久居留卡；可由任何国家签发。 | 印度护照、驾照、选民身份证或 PAN；另需姓名/地址完全匹配的地址证明，通常限近 90 天。 |
| [英国（含根西岛）](https://support.google.com/googleplay/android-developer/answer/15633622?co=GENIE.CountryCode%3DGB) | 公司注册证、VAT 注册证、慈善机构注册证；政府部门可用官方信函。 | 护照、身份证、驾照或永久居留卡；可由任何国家签发。 | 英国政府签发的驾照、护照或永久居留卡；另需匹配的近期地址证明，通常限近 90 天。EEA/英国身份证件不得遮挡字段。 |
| [日本](https://support.google.com/googleplay/android-developer/answer/15633622?co=GENIE.CountryCode%3DJP) | 公司注册/登记证明、税务机关登记摘录、纳税证明；政府部门可用官方信函。个体经营者可用“个人事业开业/歇业申报书”按组织路径核验。 | 护照、身份证、驾照或永久居留卡；可由任何国家签发。 | 日本政府签发的护照、驾照或在留卡；另需匹配的近期地址证明，通常限近 90 天。 |
| [巴西](https://support.google.com/googleplay/android-developer/answer/15633622?co=GENIE.CountryCode%3DBR) | 营业执照、CNPJ 登记摘录、MEI 证书；政府部门可用官方信函。 | 护照、身份证、驾照或永久居留卡；可由任何国家签发。 | 护照、RG、驾照、工作证或 RNE；另需匹配的近期地址证明，通常限近 90 天。 |
| [加拿大](https://support.google.com/googleplay/android-developer/answer/15633622?co=GENIE.CountryCode%3DCA) | 公司注册证、良好存续/状态证明、合规证书；政府部门可用官方信函。 | 护照、身份证、驾照或永久居民卡；可由任何国家签发。 | 加拿大政府签发的护照、身份证、驾照或永久居民卡；地址证明可为带地址政府证件、水电/网络/有线电视账单、保险、信用卡或银行对账单；近 90 天内签发。 |
| [澳大利亚（含诺福克岛）](https://support.google.com/googleplay/android-developer/answer/15633622?co=GENIE.CountryCode%3DAU) | 公司注册/成立证明；特定公司受托单位信托可交成立契据；政府部门可用官方信函；也可提交 ABN。 | 护照、身份证、驾照或永久居民卡；可由任何国家签发。 | 澳大利亚政府签发的护照、驾照或照片身份证；地址证明可为带地址政府证件、水电/网络/有线电视账单、保险、信用卡或银行对账单；近 90 天内签发。 |
| [德国](https://support.google.com/googleplay/android-developer/answer/15633622?co=GENIE.CountryCode%3DDE) | 商业登记簿摘录（Handelsregisterauszug）、营业许可、VAT 注册证；政府部门可用官方信函。 | 护照、身份证、驾照或永久居留卡；可由任何国家签发。 | 身份证件须由 EEA 国家或瑞士签发，可用护照、国民身份证、驾照或居留许可；另需匹配的近期地址证明，限近 90 天。 |
| [韩国](https://support.google.com/googleplay/android-developer/answer/15633622?co=GENIE.CountryCode%3DKR) | 营业登记证；政府部门可用载明全名、地址和日期的官方信函。 | 页面没有列出通常的代表照片证件清单；个人及授权代表须通过移动运营商完成手机核验。 | 个人须提交地址证明（带地址政府照片证件、水电/网络/有线电视账单、保险、信用卡或银行对账单等），姓名/地址精确匹配且 90 天内签发；另须通过运营商手机核验。 |
| [印度尼西亚](https://support.google.com/googleplay/android-developer/answer/15633622?co=GENIE.CountryCode%3DID) | 公司注册证、公司章程、公司契据、营业执照、税务登记证；政府部门可用官方信函。 | 护照、身份证、驾照或永久居留卡；可由任何国家签发。 | 印度尼西亚政府签发的护照、国民身份证、驾照或居留许可；地址证明可为带地址政府证件、水电/网络/有线电视账单、保险、信用卡或银行对账单；近 90 天内签发。 |
| [墨西哥](https://support.google.com/googleplay/android-developer/answer/15633622?co=GENIE.CountryCode%3DMX) | 公司注册/成立证明、税务识别卡（Cédula de Identificación fiscal）；政府部门可用官方信函。 | 护照、身份证、驾照或永久居留卡；可由任何国家签发。 | 墨西哥政府签发的护照、驾照、领事身份证或选民身份证（Credencial para votar）；地址证明可为带地址政府证件、水电/网络/有线电视账单、保险、信用卡或银行对账单；近 90 天内签发。 |
| [以色列](https://support.google.com/googleplay/android-developer/answer/15633622?co=GENIE.CountryCode%3DIL&hl=en) | 公司注册/成立证明、商业登记摘录或增值税登记证明；政府部门/机构可用含全名、地址和日期的官方信函。 | 授权代表须提交政府签发的护照、身份证、驾照或永久居留卡，可由任何国家签发。 | 个人须提交以色列政府签发的护照、国民身份证或驾照；地址证明姓名和完整地址须与付款资料精确匹配，并在 90 天内签发；可用含地址政府证件、水电/网络账单、保险或银行/信用卡对账单。 |
| [新加坡](https://support.google.com/googleplay/android-developer/answer/15633622?co=GENIE.CountryCode%3DSG&hl=en) | 公司注册/成立证明、商业登记摘录、营业执照或税务证明；政府部门/机构可用含全名、地址和日期的官方信函。 | 授权代表须提交政府签发的护照、身份证、驾照或永久居留卡，可由任何国家签发。 | 个人须提交新加坡政府签发的护照、身份证、驾照或居留证；地址证明姓名和完整地址须与付款资料精确匹配，并在 90 天内签发；可用含地址政府证件、水电/网络账单、保险或银行/信用卡对账单。 |
| [泰国](https://support.google.com/googleplay/android-developer/answer/15633622?co=GENIE.CountryCode%3DTH&hl=en) | 公司注册/成立证明或商业登记摘录；政府部门/机构可用载明全名、地址和日期的官方信函。 | 授权代表可提交护照、身份证、驾照或永久居留卡，可由任何国家签发。 | 个人须提交泰国政府签发的护照、国民身份证、驾照或居留许可；地址证明可为带地址的政府证件、水电/燃气/网络/有线电视账单、保险或信用卡/银行对账单；姓名和完整地址须与付款资料精确匹配，且文件须在 90 天内签发。 |
| [法国](https://support.google.com/googleplay/android-developer/answer/15633622?co=GENIE.CountryCode%3DFR&hl=en) | 公司注册/成立证明、商业登记摘录（示例：extrait Kbis、avis SIRENE）或增值税登记证明；政府部门/机构可用含全名、地址和日期的官方信函。原文组织材料段写“advertiser verification”，与页面开发者验证标题不一致，须以 Console 当前任务确认。 | 授权代表须提交政府签发的护照、身份证、驾照或永久居留卡，可由任何国家签发。 | 个人须提交由 EEA 国家或瑞士签发的政府身份证件（护照、国民身份证、驾照或居留许可）；地址证明姓名和完整地址须与付款资料精确匹配，并在 90 天内签发；要求也适用于法属圭亚那、瓜德罗普、马提尼克、马约特和留尼汪。 |
| [南非](https://support.google.com/googleplay/android-developer/answer/15633622?co=GENIE.CountryCode%3DZA&hl=en) | 公司与知识产权委员会（CIPC）登记摘录或增值税登记证明；政府部门/机构可用含全名、地址和日期的官方信函。 | 授权代表须提交政府签发的护照、身份证、驾照或永久居留卡，可由任何国家签发。 | 个人可用南非政府签发的护照、驾照、身份证簿或 Smart ID；地址证明姓名和完整地址须与付款资料精确匹配，并在 90 天内签发；可用含地址政府证件、水电/网络账单、保险或银行/信用卡对账单。 |

**共通核验要点：**除韩国视图另列运营商手机核验且未单独列出通常的代表照片证件清单外，组织账号一般需组织登记材料和授权代表政府照片证件；个人账号按地区要求提交政府证件与地址证明。官方页将不受支持的材料列为身份核验失败的常见原因，并警告伪造或修改文件可能立即导致应用或账号被移除。中国视图提示译文可能由 AI 翻译，执法口径以英文版为准；法国视图出现“advertiser verification”广告商用语异常，已标记待按 Console 当前任务确认。本库中文表格是便于阅读的转述，不代替账号内材料清单。

营收付款方式核验与开发者身份 Payments profile 是两套资料。Play Billing 商家账号可能需要验证所有活动收款方式；按地区通过小额入账挑战或上传银行文件，官方帮助页称可能需要最多 5 天。组织资料不匹配时，Play Console 会显示账号专属修复期限；应在该期限内由所有者更正并确认相关付款资料。**来源局限：**身份帮助页的“60 天前开始”和新账号流程文本与账号内动态期限/任务不同步时，以账号待办及现行 Play Console Requirements 为准；地区文件页已抽查 17 个英文地区选项（含美国），另核对中国简体中文视图；选择器尚未穷尽。

### 商户收款银行：验证方式、付款门槛与地区差异

[商户银行账户资料页](https://support.google.com/paymentscenter/answer/7161440)要求收款账户能够接收 EFT 或电汇，通常须与商户付款账号位于同一国家/地区；EFT 使用当地币种，电汇使用美元。EEA 商户可经支持流程指定任一 EEA 国家/地区的 SEPA 可达账户。开户时，账户持有人姓名须与银行记录一致；Google 声明不会通过电子邮件索要银行账号信息。该页包含按银行所在地列出的账户字段和格式，字段表可能变化，应按官方地区选择器填写，本库不复制静态国家字段大全。

[银行账户验证说明](https://support.google.com/paymentscenter/answer/7161378)指出验证方式取决于支付路径：银行账户验证适用于 EFT 国家；美国 EFT 商户可能即时验证，其他适用地区通常等待 Google 小额测试入账（不到 1 美元，最多约 3 个工作日）后在付款资料中输入金额。电汇付款不会收到测试入账。验证后还须把拟收款账户设为主要账户；国家/币种不同，最低打款金额也不同。该页的故障排查链接目前转到[Google Payments Center 帮助目录](https://support.google.com/paymentscenter)，而不是一个具体错误码文章；Google Play 开发者付款问题则转到[Play Console 支持说明](https://support.google.com/paymentscenter/answer/16144127)。

付款操作页还要按路径区分实际最低付款额与可配置门槛：[电汇说明](https://support.google.com/googleplay/android-developer/answer/2700656)称电汇最低余额为 100 美元、以美元打款，银行费用可能为 0 至 50 美元以上；阿根廷商户可能须向银行出示当地支持材料。[订单处理与付款](https://support.google.com/googleplay/android-developer/answer/137997)称通常在下月 15 日左右支付上月订单，银行入账还可能需数日；该页也称买家购买应用或游戏后有两小时取消时间，之后 Google 才自动扣款。当地币种付款和电汇的最低付款额不同。[付款门槛设置页](https://support.google.com/paymentscenter/answer/7163445)则列出按币种变化的门槛，并说明可暂缓最多一年的付款，若要影响当月周期应在当月 21 日前修改。上述帮助页属于收款/订单操作说明，不是新的 Developer Program Policy 义务；实际资格、账户状态和付款时间应以当前付款资料及银行为准。

| 正文直接链接目标 | 与身份核验的关系 | 核对状态 |
| --- | --- | --- |
| [开户所需信息](https://support.google.com/googleplay/android-developer/answer/13628312) · [账号类型](https://support.google.com/googleplay/android-developer/answer/13634885) | 规定个人/组织账号字段及需选择组织账号的业务类型；决定身份文件、公开资料与 D-U-N-S 要求。 | 两个正文已打开并有双语摘要。 |
| [按国家/地区查看所需文件](https://support.google.com/googleplay/android-developer/answer/15633622) | 文件由付款资料国家/地区和账号类型决定；要求材料与付款资料一致，提交不受支持或伪造文件可能导致账号和应用移除。 | 美国、中国、印度、英国、日本、巴西、加拿大、澳大利亚、德国、韩国、印度尼西亚、墨西哥、以色列、新加坡、泰国、法国、南非英文视图已逐项打开；中国简体中文视图也已打开并确认其 AI 翻译提示。地区选择器内其余选项未穷尽，17 地抽查不代表全球覆盖。 |
| [韩国分发要求](https://support.google.com/googleplay/android-developer/answer/6223646) | 说明个人韩国开发者的公开电话等当地分发字段，与身份页的地区例外相连。 | 正文及主要相关子页已在[地区分发专题](../country-specific-distribution/country-specific-distribution.zh-CN.md)中摘要；国家级后代仍分层标记。 |
| [验证组织网站](https://support.google.com/googleplay/android-developer/answer/13205715) | Search Console 关联网站和 Play Console 开发者账号；列出所有者批准流程，并排除社交主页。 | 正文已打开并摘要；Search Console 操作页为技术子链，Play Console 入口需登录。 |
| [新开发者账号设备核验](https://support.google.com/googleplay/android-developer/answer/14316361) | 新个人账号在应用公开前证明账号所有者可使用实体 Android 设备；非 Root、Android 10+，通过 Play Console 移动应用完成。 | 正文已打开；29 项帮助侧栏与正文分开登记。 |
| [历史账号验证流程](https://support.google.com/googleplay/android-developer/answer/14177239) | 解释 2023 年 9 月前账号历史分批验证和延期说明。 | 正文已打开；历史日期不代表现行期限，个人账号截止日须查 Play Console。 |
| [开发者联系信息要求](https://support.google.com/googleplay/android-developer/answer/10840893) | 细分 Google 私下联系方式与商店页公开联系方式，并列出个人/组织差异。 | 正文已打开并摘要；与本页最佳实践及下文“已验证 Play 开发者账号资料维护”一节交叉阅读。 |
| [创建和管理付款资料（Google Payments）](https://support.google.com/paymentscenter/answer/9028746) · [创建开发者付款资料](https://support.google.com/googleplay/android-developer/answer/7161426) | 通用 Payments 帮助说明资料字段和成员管理；Play 帮助说明创建开发者付款资料及地区信息。两者不等于 Play 的开发者身份政策。 | 两页正文已打开；通用付款中心页 9 项侧栏后代没有全部展开。 |
| [旧版账号资料帮助入口](https://support.google.com/googleplay/android-developer/answer/139626) | 历史链接落到当前开户资料页 answer/13628312。 | 已打开并确认重定向；当前内容以新目标页为准。 |
| [E.164 电话号码格式参考](https://en.wikipedia.org/wiki/E.164) | 仅解释国际电话号码格式，不增加 Google Play 政策义务；Wikipedia 页面列出的版本日期为 2020 年。 | 页面已打开；继续追到当前 ITU-T 官方版本，见下一行。 |
| [ITU-T E.164 官方目录（现行版）](https://www.itu.int/rec/T-REC-E.164/) · [英文 PDF（2026-02）](https://www.itu.int/rec/dologin_pub.asp?id=T-REC-E.164-202602-I%21%21PDF-E&lang=e&type=items) · [中文 PDF（2026-02）](https://www.itu.int/rec/dologin_pub.asp?id=T-REC-E.164-202602-I%21%21PDF-C&lang=e&type=items) | ITU 目录列出 2026-02 版为现行生效版本；它规范八类国际电信号码结构，地理区域国际号码最多 15 位，并建议用“+”表示国际前缀。它是电话号码技术标准，不是 Play 政策。 | 目录及中英 36 页 PDF 均已打开并摘要关键结构；未逐项复录全部分配/路由表。ITU 表示建议书原则上自愿遵循。 |
| [账号内身份支持入口](https://support.google.com/googleplay/android-developer/contact/kyd) · [无法登录时的问题报告表单](https://support.google.com/googleplay/android-developer/contact/general_contact) | 政府组织缺少 D-U-N-S、无法登录或需要帮助时可用的支持路径。 | Console 内支持目标转向登录后工单并无法公开读取；公开表单已打开，但本次未提交。 |
正文还包含两个同页“联系信息最佳实践”“开发者公开信息最佳实践”锚点；其建议已归纳在上文，不是额外独立页面。重复的旧入口 answer/139626 已与新开户资料页合并记录。

### 按国家/地区查看所需文件：正文链接审计

`answer/15633622` 的正文链接数会随地区视图变化。美国默认视图有 **8 次链接出现**：同页选择器、5 个共用外链和 2 个仅美国视图出现的 IRS 查询链接。其余 16 个非美国英文视图各有 **6 次链接出现**：同页选择器和 5 个共用外链；未观察到地区专属外部链接。Help 导航和页脚链接不计入正文链接数。

| 正文目标 | 与所需文件页的关系 | 核对状态 |
| --- | --- | --- |
| [2023 年开发者身份公告](https://goo.gle/3NLnFma) | 历史验证 rollout 背景，不改变当前材料清单。 | 短链接已打开并转至既有公告专题。 |
| [Play Console 要求](https://support.google.com/googleplay/android-developer/answer/10788890) | 与身份验证相邻的账号及应用包名现行要求。 | 正文已打开并有双语专题。 |
| [国家/地区选择器（同页）](https://support.google.com/googleplay/android-developer/answer/15633622) | 切换付款资料国家/地区对应的材料清单；下方已核对 17 个英文地区，并另看中国简体中文视图。 | 已逐项打开美国、中国、印度、英国、日本、巴西、加拿大、澳大利亚、德国、韩国、印度尼西亚、墨西哥、以色列、新加坡、泰国、法国和南非英文视图；另打开中国简体中文视图。美国默认视图的 IRS 查询链接不出现在非美国视图；其余选择项仍未穷尽。 |
| [Google 安全与隐私入口](https://safety.google/security-privacy/) · [当前目标页](https://safety.google/safety/) | 通用安全/隐私背景，不新增身份文件类别或豁免条件。 | 原链接已打开并重定向到当前安全中心。 |
| [Google 隐私权政策](https://policies.google.com/privacy) | Google 对个人信息的通用处理说明，不决定 Play 接受哪些身份证明。 | 当前政策页已打开；作为背景说明。 |
| [通过 Google 销售的客户服务条款目录](https://support.google.com/paymentscenter/answer/7188707) | 国家/地区销售者付款条款目录，可能解释商家付款资料核验；不替代 Play 身份文件要求。 | 目录正文已打开；国家/地区条款是更深层子链，未全部展开。 |
| [IRS 政治组织检索](https://forms.irs.gov/app/pod/basicSearch/search) | 帮助核验美国组织文件示例中提及的部分 IRS 记录。 | 官方检索入口已打开；动态表单未提交查询。 |
| [IRS 免税组织检索](https://apps.irs.gov/app/eos/) | 帮助核验美国组织文件示例中提及的部分免税组织记录。 | 官方检索入口已打开；动态表单未提交查询。 |

## 已验证 Play 开发者账号资料维护

[查看和管理已验证账号资料](https://support.google.com/googleplay/android-developer/answer/13634081)只适用于已按 Play Console Requirements 完成验证的账号；未验证账号应从[开户所需信息](https://support.google.com/googleplay/android-developer/answer/13628312)页进入。只有账号所有者能修改开发者账号资料。Google 要求资料保持准确；身份或联系资料过期可能导致账号受限并移除应用。

核对时要分清四类字段：

- **商店页联系信息**：邮箱为发布或更新应用的必填项；这里填写的联系资料会展示在应用商店页。
- **Google 私下联系信息**：联系人姓名、联系邮箱、电话和邮件语言仅供 Google 联系；邮箱和电话须经一次性验证码验证。组织联系邮箱应代表组织、使用组织网站域名，并与 Google 账号邮箱区分；可使用团队邮件列表。
- **用户公开联系信息**：开发者邮箱，以及适用时的开发者电话须验证后展示。开发者名称经 Google 审核批准后才会在 Play 显示。韩国开发者还要提交营业登记号、电商许可号和许可机构；这些字段会向韩国地区用户显示。
- **法定身份/商家地址**：组织名称、地址和 D-U-N-S 取自关联的 Google Payments profile；通过 Play 商店销售付费应用或应用内商品的商家账号，商店页须展示该付款资料中的完整地址。更改同一国家内的名称/地址，通常可更新原付款资料；更换国家或组织 D-U-N-S 则需创建并验证新的付款资料。

**通知和账号生命周期：**“政策”“付款与税务”邮件不能关闭；关闭可选提示邮件后，强制服务公告仍会发送到开发者资料邮箱。转移已发布或未发布应用时须使用[应用转移清单](https://support.google.com/googleplay/android-developer/answer/6230247)。若要删除已发布应用所在的开发者账号，先备份资料、转移应用，再回复转移确认；Google 账号删除不会自动删除 Play 开发者账号，开发者名称也不能与另一账号相同。

此帮助页正文有 **23 次链接出现、20 个唯一目标**，包括政策要求、身份/账号资料帮助、地区规则、应用转移，以及需要登录的 Play Console、Payments、Google Account 和支持流程。另有 **15 项“设置开发者账号”帮助侧栏**（含当前页）；14 个同级目标的摘要与访问状态列在[Play Console 用户权限专题](../play-console-user-permissions/play-console-user-permissions.zh-CN.md)。账号专属表单、动态 Console 页面及支付/登录流程不是可据公开帮助页推断的政策正文；相关条目按抓取状态单独标记在来源台账。

## 付款资料身份变更与账号类型转换

[更新由 Google 付款资料管理的开发者身份信息](https://support.google.com/googleplay/android-developer/answer/16260648?hl=en)规定，只有账号所有者能在 Play Console 的 **Developer account → About you** 发起身份资料更新。先区分用于身份验证的付款资料与用于收款的商家付款资料；有些开发者共用同一资料，有些则分开。

- **同一国家内改姓名或地址：**更新现有关联付款资料；Google 可能要求补交身份证明或组织文件。
- **改国家或组织 D-U-N-S：**在 Console 创建或选择一份新付款资料，提交并验证所需信息，再由所有者将已验证资料关联到开发者账号并确认保存。D-U-N-S 可免费申请；帮助页提示警惕收费代办。组织通常必须填写 D-U-N-S；政府组织/机构可能可不填。若 Console 未显示该选项且确实无法提供 D-U-N-S，可使用账号内支持入口，无法访问 Console 时再使用公开表单。
- **个人账号转组织账号：**个人账号必须已完成验证且没有待处理警告；先提交并验证组织官网，再选择组织付款资料，填写组织类型、规模、电话以及分别供 Google 使用和展示给用户的已验证联系方式；完成身份资料验证、关联资料并确认转换。转换完成后至少等待 **72 小时**再提交新应用，以便账号资料同步并降低重复拒审风险。
- **组织账号转个人账号：**现有账号类型不能反向转换。需要新建并验证个人开发者账号，再按[应用转移清单](https://support.google.com/googleplay/android-developer/answer/6230247)迁移应用。

| 正文直接链接 | 页面用途及与本指南的关系 | 核对状态 |
| --- | --- | --- |
| [Play Console 账号入口（账号应用列表）](https://play.google.com/console/) | 发起资料更新、创建/选择付款资料、查看验证任务并关联已验证资料。 | 正文链接已点击；该账号专属应用列表跳转至 Google 登录，无法检查具体账号状态。快照 URL 中的数字开发者 ID 不写入本公开页面。 |
| [Play Console 身份支持](https://support.google.com/googleplay/android-developer/contact/kyd) | 在 Console 内为政府组织 D-U-N-S 例外等问题联系支持。 | 已点击；跳转至需登录的 Play Console 支持工单。 |
| [无 Console 访问权限时使用的公开问题表单](https://support.google.com/googleplay/android-developer/contact/general_contact) | 当开发者无法创建或访问 Console 账号时提供问题报告入口；终止账号或执法申诉应优先使用执法通知邮件中的渠道。 | 表单页面已打开并核对字段、支持语言及隐私信息提示；未提交。 |
| [验证开发者身份信息](https://support.google.com/googleplay/android-developer/answer/10841920?hl=en) | 承接新付款资料的身份/组织文件核验、联系方式和验证期限。 | 正文已打开并汇总于本页上文。 |
| [验证组织网站](https://support.google.com/googleplay/android-developer/answer/13205715) | 个人转组织前的组织官网验证前置步骤；通过 Search Console 将网站与 Play Console 账号关联。 | 正文已打开并摘要；Console 操作需要登录，Search Console 实现文档属于技术子链。 |
| [转移应用到其他开发者账号](https://support.google.com/googleplay/android-developer/answer/6230247) | 组织转个人需新建账号后的应用迁移清单；账号类型不能直接反向切换。 | 正文已打开；详细条件见应用转移专题。 |

此帮助页的 6 个正文链接目标已逐一核对；Play Console 设置侧栏另有 15 项（含当前页），不与正文目标混算。表单和 Console 账号操作不代表可公开核实账号的实际验证状态；更深的帮助侧栏后代继续按逐 URL 台账标注。

## 发布与迁移核对清单

1. 按 Google Play、其他商店、官网/企业渠道、测试和个人分享分别列出分发渠道及目标国家/设备。
2. 在 Play Console 和适用的 Android Developer Console 中逐应用检查包名注册状态、签名证书和密钥持有人；不要仅依赖“99% 自动注册”的总体比例。
3. 提前确认开发者账号路径、身份/地址证明、D-U-N-S、网站验证和费用；组织材料处理可能需要等待。
4. 对重复包名准备签名密钥/安装量证据；备份并限制签名私钥访问。
5. 若走有限分发，当前中英文官方指南和 Android Developer Console Help 均写最多 20 台；计划超过该数量前核对具体账号的 Console 上限。若测试安装使用 ADB，记录其与消费者旁加载流程不同。
6. 若分发 Managed Google Play 私有应用，逐项确认目标设备属于完整受管理/工作资料还是未受管理认证设备，并按对应路径完成包名注册。
7. 为 2027 年全球扩展持续关注 Android 开发者验证时间线；区域执行、合作商店范围及 Console 字段以官方最新页面为准。

本页是双语改写摘要，不是官方网页全文或账号合规证明。关联政策：[Play Console 要求](../play-console-requirements/play-console-requirements.zh-CN.md)、[Android 开发者身份信息验证](https://support.google.com/googleplay/android-developer/answer/10841920?hl=zh-CN)、[开发者分发协议](../developer-distribution-agreement/developer-distribution-agreement.zh-CN.md)。10841920 英文正文已打开并摘要；验证字段与截止日可能因国家、账号类型及账号状态而异，应按 Play Console 实际待办核对。
