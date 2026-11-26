---
id: google-play.android-app-security-improvement-campaigns
platform: google-play
language: zh-CN
authority: historical
status: current
kb_checked_at: 2026-10-23
review_due: 2027-01-23
regions: [global]
topics: [android-security, security-campaigns, remediation, app-integrity]
snapshot_id: play.android-app-security-improvement-campaigns
snapshot_package: "GooglePlay-KnowledgeBase-2026-10-24-review.zip"
coverage_status: "partial-recursive-summary"
source_url: "https://developer.android.com/privacy-and-security/googleplay-asi"
effective_date: "campaign table dates are historical start dates, not current universal deadlines; no 2027-01-27"
---

# Google Play App Security Improvement 安全改进活动与整改指南

> **导入说明（Google batch 8）。** 正文来自已经分开的 2026-10-24 Google Play 知识库快照（`play.android-app-security-improvement-campaigns`，核对日 2026-10-23）的改写摘要，不是官方页面的逐字副本。英文官方页面是效力来源。`kb_checked_at` 是快照源文件记录的核对日；本次导入没有重新打开线上官方页面。文中“本知识库”“本库”“本地专题”等说法描述的是该快照库的覆盖范围，不是本仓库已经导入的页面。指向本仓库没有收录的专题、链接图、台账或 CSV 的相对链接改为文字提及。指向 Google batch 1–7 或本批十三个专题的相对链接改为本仓库文件。核对日 2026-10-23。35 个不同的活动支持目标中，21 个正文已打开，12 个只读到官方索引片段，2 个仍未读：SQL Injection 和 Vungle SDK。SQL Injection 的英文、简体中文和西班牙语直开都未取回正文。Vungle 停在 Google 验证页。未读页面不推断漏洞或修复。活动表日期是历史启动日，不是当前统一截止日。没有 2027-01-27。该计划仍可能通知开发者；某个应用的期限以该账号的 Console 告警为准。证据等级：活动门槛为 Historical；现行通知计划为 Operational。

## 适用范围与期限判断

[Android App Security Improvement Program](https://developer.android.com/privacy-and-security/googleplay-asi) 是 Google Play 面向开发者提供的应用安全改进服务。官方页说明，应用在获准进入 Play 前会接受安全扫描，之后也会持续复扫；发现潜在问题时，Google 通过邮件和 Play Console 告警，并链接到对应修复说明。通知通常给出整改时间；某些问题可能阻止应用继续发布更新。开发者上传修复版本并递增版本号后，可在数小时后检查告警是否消失。

**不要把活动表中的 Started 日期当成现行截止日期。** 页面列出的活动始于 2014–2022 年；它们是历史活动启动日期。具体受影响应用、修复时限、发布限制和告警是否清除，应以该应用 Play Console 中的通知为准。历史 SDK 版本门槛也不是当前推荐使用的最新版本。

官方目录分为“有整改期限的警告活动”和“仅警告、无整改期限的活动”。例如，Implicit PendingIntent 页面明确写明修复“建议但非强制”，且不会影响应用发布状态；不能把所有安全活动都描述成统一的下架倒计时。

## 活动目录与目标页复核

官方目录有 **38 行活动记录**、**36 次支持页链接引用**、**35 个不同的链接目标**；Apache Cordova 目标重复引用一次，Embedded Keystore files 和 Amazon Web Services embedded credentials 两行没有支持页链接。目标页访问状态以 2026-10-23 的本地审计为准。下表对取回正文的目标概括可见内容；对于抓取失败或仅有搜索索引片段的页面，明确标出边界，不从标题补写修复细节。

| # | 活动（启动日期） | 官方支持页 | 风险/修复要点 | 正文访问状态 |
| --- | --- | --- | --- | --- |
| 1 | Exposed Firebase Cloud Messaging Server Keys（2021-10-12） | [FCM Server Keys](https://support.google.com/faqs/topic/11015404) | 客户端暴露的旧 FCM 密钥可能被滥用向用户推送恶意通知。优先迁移 FCM HTTP v1 并停用旧 API；轮换暴露密钥，将新密钥仅放在受控服务器，撤销/删除旧密钥，并检查所有受影响轨道及旧版本。 | 正文已打开 |
| 2 | Intent Redirection（2019-05-16） | [Intent Redirection](https://support.google.com/faqs/answer/9267555) | 不可信嵌套 Intent 可能访问私有组件/文件或携带恶意参数。将无需外部访问的组件设为非导出，验证来源、目标组件与 URI 授权标记；不要把未验证 Intent 直接交给 `startActivity`、服务、广播或 `setResult`。 | 官方搜索索引读取正文；直接抓取遇到 Google 验证页 |
| 3 | JavaScript Interface Injection（2018-12-04） | [JavaScript Interface Injection](https://support.google.com/faqs/answer/9095419) | 不可信 Web 内容可调用 WebView 暴露的 `@JavascriptInterface` 方法。移除桥接对象，或确保 WebView 不加载不可信内容；限制明文 HTTP 和未经校验的 Intent URL。 | 正文已打开 |
| 4 | Scheme Hijacking（2018-11-15） | [Intent Scheme Hijacking](https://support.google.com/faqs/answer/9101196) | 不可信 WebView 内容可能构造 `intent://` 导向私有组件。限制解析后的 Intent 为预期的隐式 BROWSABLE 目标，清除显式 component/selector，并校验 URL/来源。 | 正文已打开 |
| 5 | Cross App Scripting（2018-10-30） | [Cross App Scripting](https://support.google.com/faqs/answer/9084685) | 外部应用构造的数据进入启用 JavaScript 的 WebView，可能窃取 Cookie/应用数据。优先将受影响 Activity 设为非导出；必须导出时验证输入与来源，收紧文件访问和 Cookie 数据库访问。 | 正文已打开 |
| 6 | File-based Cross-Site Scripting（2018-06-05） | [File-based XSS](https://support.google.com/faqs/answer/7668153) | WebView 同时启用文件 URL 跨域访问设置并加载不可信内容（包括经 HTTP 传输的可信域名内容），可能让注入脚本跳转到恶意本地文件并读取私有文件或 Cookie。应关闭危险设置、禁止本地文件/JavaScript，或确保此类 WebView 只加载可信内容；旧文举出的 API 16 target 阈值是历史修复说明，当前 WebSettings 已将相关方法标为 API 30 弃用并建议用 `WebViewAssetLoader`。 | 正文已打开；当前 Android 子页已抽查 |
| 7 | SQL Injection（2018-06-04） | [SQL Injection](https://support.google.com/faqs/answer/7668308) | 目标 URL 已解析；英文、简体中文和西班牙语直开均未取回正文。本页不据活动标题补写数据库 API、漏洞条件或修复代码。 | 多语言直开仍 Cache miss / 不可访问，正文未读 |
| 8 | Path Traversal（2017-09-22） | [Path Traversal](https://support.google.com/faqs/answer/7496913) | 导出的 `ContentProvider` 若未校验 `openFile`/`openAssetFile` 收到的 URI，可被编码的 `../` 诱导返回预期目录之外的文件描述符。无须对外开放时设 `android:exported="false"`；需开放时用签名级权限或严格校验规范路径。文章特别警告：`getLastPathSegment()` 会解码输入，`UriMatcher` 的 `*` 匹配也不是路径净化。 | 正文与 Android Manifest/API 相关章节已打开 |
| 9 | Insecure Hostname Verification（2016-11-29） | [Hostname Verification](https://support.google.com/faqs/answer/7188426) | 自定义验证器若接受任意主机名，会使 HTTPS 易受中间人攻击。错误主机名应验证失败；不要吞掉校验异常或使用 `AllowAllHostnameVerifier`。 | 正文已打开 |
| 10 | Fragment Injection（2016-11-29） | [Fragment Injection](https://support.google.com/faqs/answer/7188427) | 不安全导出的 `PreferenceActivity` 可能加载本应私有的 Fragment。优先设 `exported=false`；确需导出时对 Fragment 类名做严格白名单校验。页面提到的旧 target API 阈值是历史修复背景，不是现行 target API 要求。 | 正文已打开 |
| 11 | Supersonic Ad SDK（2016-09-28） | [Supersonic SDK](https://support.google.com/faqs/answer/7126517) | 官方索引内容指向旧 SDK 通过 JavaScript/HTTP 暴露功能；页面列有历史版本修复门槛。应以当前 SDK 维护方和 Play Console 告警为准，不能把旧门槛当作当前版本建议。 | 官方搜索索引部分读取；直开受限 |
| 12 | Libpng（2016-06-16） | [Libpng](https://support.google.com/faqs/answer/7011127) | 正文确认 CVE-2015-8540 造成越界内存访问，可能导致代码执行；列出的 1.0.66、1.2.56、1.4.19、1.5.26 是 2016 年活动修复门槛。当前上游页（2026-04-15 更新）列出 libpng 1.6.58；旧主版本支线不再更新，不能把历史门槛当作当前升级建议。 | 正文与上游版本页已打开；CVE 页仅显示 JavaScript 壳 |
| 13 | Libjpeg-turbo（2016-06-16） | [Libjpeg-turbo](https://support.google.com/faqs/answer/7008337) | 官方索引指出旧于 1.4.2 的版本存在 Huffman 解码器缓冲区越界风险；此处版本号仅记录历史活动，不是最新版本建议。 | 官方搜索索引部分读取；直开 Cache miss |
| 14 | Vpon Ad SDK（2016-06-16） | [Vpon SDK](https://support.google.com/faqs/answer/7012047) | 索引内容指出旧 SDK 的 WebView 文件访问配置可能让恶意广告脚本访问本地资源；官方页给出历史修复版本。直开 Cache miss。 | 官方搜索索引部分读取 |
| 15 | Airpush Ad SDK（2016-03-31） | [Airpush SDK](https://support.google.com/faqs/answer/6376737) | 索引内容指向旧版本 WebView 默认配置过宽和相应升级分支；需核查应用实际打包的广告 SDK/传递依赖，而不只看顶层依赖。通告是 2016 年历史活动。 | 官方搜索索引部分读取；直开受限 |
| 16 | MoPub Ad SDK（2016-03-31） | [MoPub SDK](https://support.google.com/faqs/answer/6345928) | 可读索引片段显示历史修复版本为 4.4.0；本次未取回英文正文，具体漏洞机制仍待复核，不据此补写技术细节。 | 官方搜索索引片段；直开受限 |
| 17 | OpenSSL（Logjam、CVE-2015-3194、CVE-2014-0224；2016-03-31） | [OpenSSL campaign](https://support.google.com/faqs/answer/6376725) | 活动链接目标在直开时遇到限流；官方索引命中旧 OpenSSL 漏洞与历史版本修复信息。避免将旧版号解释成今天可用版本；实际依赖和系统 TLS provider 需单独盘点。 | 官方搜索索引部分读取；直开限流 |
| 18 | TrustManager（2016-02-17） | [TrustManager](https://support.google.com/faqs/answer/6346016) | 自定义 `X509TrustManager` 若忽略证书错误会被中间人攻击。证书不满足预期时从 `checkServerTrusted` 抛出异常，不要吞掉异常；`checkValidity` 只检查有效期，不能证明证书可信。 | 正文已打开 |
| 19 | AdMarvel（2016-02-08） | [AdMarvel](https://support.google.com/faqs/answer/6345881) | 官方索引说明旧于 2.5.4 的 SDK 有 WebView 文件访问风险，并指出相关危险产品/DDA 历史条款。核实应用和封装 SDK 实际携带版本；2.5.4 是当年修复门槛，不是当前版本建议。 | 官方搜索索引部分读取；直开 Cache miss |
| 20 | Libupup（父目录标签；2016-02-08） | [活动表链接目标](https://support.google.com/faqs/answer/6346109) | 点击目标的页面标题和正文实际写的是 Portable SDK for UPnP Devices（libupnp），称 1.6.18 以前版本存在可导致任意代码执行的栈缓冲区溢出，并给出 2016 年升级门槛。父活动表标注 “Libupup / CVE-2015-8540”，但目标正文没有显示该 CVE 号；保留为来源标签与目标正文的对应差异，不把两者自行校正成同一表述。 | 完整正文与 SourceForge 项目/文件页已打开；Vitamio 帮助与 Trend Micro 子页访问失败 |
| 21 | Apache Cordova（CVE-2015-5256、CVE-2015-1835；2015-12-14） | [Apache Cordova](https://support.google.com/faqs/answer/6325474) | 官方索引确认当年要求从低于 4.1.1 的版本升级，并处理其安全漏洞；正文还关联多个历史 CVE。外部封装 SDK 应由其维护方升级。该版本门槛不能替代对当前维护版本和已修复依赖的核查。 | 官方搜索索引部分读取；直开 Cache miss |
| 22 | Vitamio Ad SDK（2015-12-14） | [Vitamio SDK](https://support.google.com/faqs/answer/6365106) | 正文确认 5.0 以前的 Vitamio 含 world-writable code；可通过 SDK 中的 `libs/armeabi-v7a/libvinit.so` 或 `libs/armeabi/libvinit.so` 识别旧包。若由封装库带入，须升级到包含 5.0+ 的版本。该版本号和 2016 发布拦截日期属于历史活动门槛，不代表当前维护状态。 | 正文已打开；Vitamio 官网/帮助与 NowSecure 子页访问失败 |
| 23 | GnuTLS（2015-10-13） | [GnuTLS](https://support.google.com/faqs/answer/6344084) | 官方索引列出历史缓冲区漏洞和当年修复分支版本（3.1.25、3.2.15、3.3.4）；这些是历史修复信息。 | 官方搜索索引部分读取；直开 Cache miss |
| 24 | WebView SSLErrorHandler（2015-07-17） | [WebView SSL Error Handler](https://support.google.com/faqs/answer/7071387) | 对可信证书按应用预期继续，否则取消；不能因单个 `getPrimaryError()` 值就忽略其它证书错误。第三方 SDK 引发的问题需与供应方修复；页面还提及危险产品政策与 DDA §4.4 的风险联系。 | 正文已打开 |
| 25 | Vungle Ad SDK（2015-06-29） | [Vungle SDK](https://support.google.com/faqs/answer/6313713) | 目标 URL 已由活动表识别；抓取遇到 Google 验证页，正文未取回，不推断漏洞或 SDK 版本。 | 抓取受限，正文未读 |
| 26 | Apache Cordova（CVE-2014-3500、CVE-2014-3501、CVE-2014-3502；2015-06-29） | [Apache Cordova（同一支持页）](https://support.google.com/faqs/answer/6325474) | 同一支持页链接再次用于另一组历史 CVE；不要把重复行计作第二个 URL。 | 与 #21 相同目标；索引部分读取 |
| 27 | Implicit PendingIntent（2022-02-22；仅警告） | [Implicit PendingIntent](https://support.google.com/faqs/answer/10437428) | 页面明示修复建议但非强制且不会影响发布。将基础 Intent 的 action/package/component 限定到预期范围，只交给可信接收方，并在适用平台使用 `FLAG_IMMUTABLE`。 | 正文已打开 |
| 28 | Implicit Internal Intent（2021-06-22；仅警告） | [Implicit Internal Intent](https://support.google.com/faqs/answer/10399926) | 发送到本应用内部组件的隐式 Intent 可被拦截、读取或替换。优先用 `setComponent`、`setClass`、`setClassName`，或至少用 `setPackage` 限定接收方。 | 正文已打开 |
| 29 | Unsafe Encryption Mode（2020-10-13；仅警告） | [Unsafe Encryption Mode](https://support.google.com/faqs/answer/10046138) | 正文将 AES/ECB 视为较弱模式；`Cipher.getInstance("AES")` 只写算法名时会采用 provider 默认模式，Google 建议使用 `AES/GCM/NoPadding`。正文还说明动态加载模块、SDK 或 packer 可能是告警代码位置；修复版本提交后会进入待审核发布状态。实际告警位置与期限仍看该应用的 Console 通知。 | 正文、Cipher API、Play Feature Delivery 与相关安全指南已打开 |
| 30 | Unsafe Encryption（2019-09-17；仅警告） | [Unsafe Cryptographic Encryption](https://support.google.com/faqs/answer/9450925) | 静态、可预测或重复的密钥/IV/salt 会削弱加密。优先使用 AndroidX Security/Tink 等成熟库、随机不可预测参数和 Android Keystore；传输保护另用 TLS。 | 正文已打开 |
| 31 | Zipfile Path Traversal（2019-05-21；仅警告） | [Zip Path Traversal](https://support.google.com/faqs/answer/9294009) | 解压时校验规范化后的目标路径仍位于预期目录内，防止恶意条目写出目标目录。 | 正文已打开 |
| 32 | Embedded Foursquare OAuth Token（2016-09-28；仅警告） | [Foursquare OAuth secret](https://support.google.com/faqs/answer/7050471) | 客户端内嵌 OAuth `client_secret` 可使攻击者访问应用获准的用户数据。将需要机密的请求移至自己控制的服务端并轮换/撤销暴露凭据。父页目标已识别；官方搜索可读内容，目标正文直开曾 Cache miss。 | 官方搜索索引部分读取 |
| 33 | Embedded Facebook OAuth Token（2016-09-28；仅警告） | [Facebook OAuth secret](https://support.google.com/faqs/answer/7126515) | 客户端内嵌 OAuth 密钥不能视为秘密；迁移机密操作到受控服务器，并按供应方流程处理已暴露凭据。 | 正文已打开 |
| 34 | Google Play Billing interception（2016-07-28；仅警告） | [In-app Billing vulnerability](https://support.google.com/faqs/answer/7054270) | 活动针对旧版应用内结算集成的拦截/篡改风险；将本地客户端判断、服务端验证和历史库修复说明分开核对，具体版本要求按原页面/当前 Billing 文档复核。 | 正文已打开 |
| 35 | Embedded Google Refresh Token OAuth（2016-07-28；仅警告） | [Google OAuth refresh token](https://support.google.com/faqs/answer/7052200) | 客户端包中泄露 refresh token 会暴露对应账户/授权能力；不要把长期凭据打包进 APK，需处理已暴露 token 并迁移受保护流程。 | 正文已打开 |
| 36 | Developer URL Leaked Credentials（2016-06-16；仅警告） | [URL credentials](https://support.google.com/faqs/answer/7026406) | 搜索索引页面建议排查 URL 内嵌的 Basic Authentication 用户名/密码；真实秘密应立即轮换，并重构应用避免打包凭据。父页此链接的 href 未从浏览器响应中恢复，因此与活动行的对应关系仍标为待确认。 | 官方搜索索引部分读取；父子映射未确认 |
| 37 | Embedded Keystore files（2014-10-02；仅警告） | 无支持页链接 | 活动表有标题和启动日期，但未提供支持页目标；没有正文可供摘要。 | 官方目录未提供链接 |
| 38 | Amazon Web Services embedded credentials（2014-06-12；仅警告） | 无支持页链接 | 活动表有标题和启动日期，但未提供支持页目标；没有正文可供摘要。 | 官方目录未提供链接 |

## 本轮补读页面及直接子链接

2026-10-23 以各帮助页正文链接为入口重新打开此前未读的 5 个目标，并补读先前只有官方搜索索引摘要的 Libpng 页。35 个不同活动支持目标现在为 **21 个正文完整打开、12 个官方索引部分读取、2 个正文仍无法取得**。未读目标是 [SQL Injection](https://support.google.com/faqs/answer/7668308) 与 [Vungle SDK](https://support.google.com/faqs/answer/6313713)：前者英文、简体中文和西班牙语直开都未取回，后者点击进入 Google 验证页。没有根据非官方论坛猜测这两页内容。

| 目标页 | 页面内容及与活动的关系 | 正文直接子链接及核验状态 |
| --- | --- | --- |
| [File-based XSS](https://support.google.com/faqs/answer/7668153) | 告警针对 WebView 危险文件 URL 设置与不可信内容组合的风险；修复建议分别为关闭危险设置、禁止本地文件/JavaScript，或确保此类 WebView 不加载不可信内容。Android API 现将两个 file-URL 跨域方法标为 API 30 弃用，并推荐 [WebViewAssetLoader](https://developer.android.com/reference/androidx/webkit/WebViewAssetLoader) 以 http(s) URL 在同源模型中提供本地资源。 | Play Console 直链[点击后转到公开业务落地页](https://play.google.com/console/)；[Play Feature Delivery](https://developer.android.com/guide/playcore/feature-delivery)、[Android Security Checklist](https://developer.android.com/privacy-and-security/security-tips)、[Device and Network Abuse](https://support.google.com/googleplay/android-developer/answer/16559646?hl=en)、[WebView API](https://developer.android.com/reference/android/webkit/WebView.html)、[WebSettings API](https://developer.android.com/reference/android/webkit/WebSettings.html)、[`uses-sdk`](https://developer.android.com/guide/topics/manifest/uses-sdk-element.html)、[Manifest overview](https://developer.android.com/guide/topics/manifest/manifest-intro.html)、[`<application>`](https://developer.android.com/guide/topics/manifest/application-element.html) 和 [Network Security Configuration](https://developer.android.com/privacy-and-security/security-config) 已打开或抽查相关章节。Stack Overflow 只到[通用问题首页](https://stackoverflow.com/questions)；[开发者安全支持](https://support.google.com/googleplay/android-developer/contact/app_vuln)转至账号登录流程。 |
| [Path Traversal](https://support.google.com/faqs/answer/7496913) | 页面说明导出 ContentProvider 的文件读取入口如何因 URI 校验不足而暴露预期目录之外的文件。 | 其 [ContentProvider API](https://developer.android.com/reference/android/content/ContentProvider.html)、[`<provider>`](https://developer.android.com/guide/topics/manifest/provider-element.html)、[`<permission>`](https://developer.android.com/guide/topics/manifest/permission-element.html)、[`Uri`](https://developer.android.com/reference/android/net/Uri.html) 与 [`UriMatcher`](https://developer.android.com/reference/android/content/UriMatcher) 目标均已打开；核对了 `openFile`/`openAssetFile`、`android:exported`、签名保护级别、解码后的 `getLastPathSegment()` 和通配符匹配说明。[Play Console](https://play.google.com/console/) 已尝试；Stack Overflow 到[通用问题首页](https://stackoverflow.com/questions)；开发者支持目标返回内部错误。 |
| [Unsafe Encryption Mode](https://support.google.com/faqs/answer/10046138) | 目标页说明 AES/ECB 及算法名默认模式，并建议 AES-GCM；这是历史安全告警的修复说明。 | [Play Console](https://play.google.com/console/) 路由转到公开落地页；[Play Feature Delivery](https://developer.android.com/guide/playcore/feature-delivery)、[Android Security Checklist](https://developer.android.com/privacy-and-security/security-tips)、[Device and Network Abuse](https://support.google.com/googleplay/android-developer/answer/16559646?hl=en)、[Cipher API](https://developer.android.com/reference/javax/crypto/Cipher) 和当前[应用发布流程](https://support.google.com/googleplay/android-developer/answer/9859751?hl=en)已打开或交叉核对。Stack Overflow 到[通用问题首页](https://stackoverflow.com/questions)。 |
| [Portable SDK for UPnP / libupnp](https://support.google.com/faqs/answer/6346109) 与 [Vitamio](https://support.google.com/faqs/answer/6365106) | 两页分别描述 libupnp 栈缓冲区溢出和 Vitamio world-writable code，也提醒第三方封装库会传递携带问题库。版本门槛保留为历史活动信息。 | libupnp 链接的 [SourceForge 当前文件页](https://sourceforge.net/projects/pupnp/files/)显示 2026-09 发布的 22.1.0；[项目首页](https://pupnp.sourceforge.io/)说明 Portable SDK 的用途，并链接许可和开发文档。Google Play Dangerous Products、[开发者分发协议](https://play.google/developer-distribution-agreement.html)与[开发者计划政策](https://play.google/developer-content-policy/)已打开并与现有专题交叉核对。Vitamio 官网/帮助、Trend Micro 和 NowSecure 子页抓取失败；[Play Console](https://play.google.com/apps/publish)/Help 路由只到公开落地页、登录流程或内部错误；Stack Overflow 到[通用问题首页](https://stackoverflow.com/questions)。 |
| [Libpng](https://support.google.com/faqs/answer/7011127) | 正文确认 CVE-2015-8540 和越界内存访问；历史版本门槛不能与当前上游版本混用。 | [上游 libpng 页面](https://libpng.sourceforge.io/index.html)记录 2026-04-15 版本状态：1.6.58 是最新发布版本，1.0/1.2/1.4/1.5 分支不再更新。CVE 页面目前只显示 JavaScript 壳；Malicious Behavior 链接转到政策目录，DDA 和 Developer Policy Center 已打开，[Play Console](https://play.google.com/apps/publish)到公开落地页，Stack Overflow 为[通用问题首页](https://stackoverflow.com/questions)，开发者支持打开失败。 |

## 共通整改步骤与发布核验

1. 从 Play Console 告警确定受影响应用、代码位置、轨道、实际期限和适用修复说明；不要只凭活动名称判断。
2. 盘点应用自身代码、动态加载代码、打包/混淆产物、广告/分析 SDK 及传递依赖。移除当前源码中的密钥并不足以处理已发布旧版本；密钥泄露还需轮换或撤销。
3. 修复后递增版本号，并确保所有受影响轨道/版本都提交符合要求的 APK 或 App Bundle。等待审核并回到 Console 确认原告警状态；失败时按邮件/Console 信息继续修复。
4. 把技术安全整改与正式 Play 政策判断分开：Play 的 User Data、Data safety、Malware/危险产品和 DDA 义务须按应用真实行为独立核对。

## 本次递归覆盖边界

2026-10-23 复核了活动目录和其 35 个不同的支持目标：21 个目标直接打开正文，12 个目标通过 Google 官方搜索索引读取到部分正文，2 个目标因验证页或 Cache miss 未读。一个“URL 凭据”目标正文可由官方搜索识别，但活动表对应 href 未能恢复；另有两行没有支持页链接。访问、摘要和子链接状态逐 URL 记录在来源审计表（快照：`../source-page-audit.csv`，未导入本仓库）。

已打开的修复页还链接 Android API/指南、Play Console 操作、开发者支持、政策条款和第三方站点。它们的孙级链接并未全部逐个打开或摘要；与 Android 安全最佳实践直接相关的 Intent、WebView、TLS、存储和依赖页面，另见[Android 隐私与安全专题](../android-privacy-checklist/android-privacy-checklist.zh-CN.md)及递归链接图 §4.111（快照：`../google-play-policy-link-graph.md`，未导入本仓库）。此页是活动通知和技术修复的整理，不是 Google Play 当前政策全文，也不声称这条外部链接树已无限递归闭合。
