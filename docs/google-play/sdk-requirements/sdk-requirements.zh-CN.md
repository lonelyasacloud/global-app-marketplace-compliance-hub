---
id: google-play.sdk-requirements
platform: google-play
language: zh-CN
authority: normative
status: current
kb_checked_at: 2026-10-23
review_due: 2027-01-23
regions: [global]
topics: [sdk, third-party-code, families-ads-sdk, sdk-index, privacy]
snapshot_id: play.sdk-requirements
snapshot_package: "GooglePlay-KnowledgeBase-2026-10-24-review.zip"
coverage_status: "detailed-summary"
source_url: "https://support.google.com/googleplay/android-developer/answer/13323374?hl=en"
source_url_safe_use: "https://support.google.com/googleplay/android-developer/answer/13326895?hl=en"
source_url_families_ads_sdk: "https://support.google.com/googleplay/android-developer/answer/12918983?hl=en"
effective_date: "current-policy; Families new applications paused; no SDK-certification effective date"
---

# Google Play 第三方 SDK 要求与安全集成

> **导入说明（Google batch 5）。** 正文来自已经分开的 2026-10-24 Google Play 知识库快照（`play.sdk-requirements`，核对日 2026-10-23）的改写摘要，不是官方页面的逐字副本。英文官方页面是效力来源。`kb_checked_at` 是快照源文件记录的核对日；本次导入没有重新打开线上官方页面。文中“本知识库”“本库”“本地专题”等说法描述的是该快照库的覆盖范围，不是本仓库已经导入的页面。指向本仓库没有收录的专题、链接图、台账或 CSV 的相对链接改为文字提及。指向 Google batch 1–4 或本批八个专题的相对链接改为本仓库文件。 YAML 的 `reviewed_on` 是 2026-10-23。两种语言文件记录的主要 SDK 帮助地址都是英文。快照没有记录这些主要 SDK 要求文章的已核对中文官方页面。2026-10-24，源文件再核对了英文和 `zh-Hans` 的 Families 自认证广告 SDK 计划概览与政策、当前 SDK 版本清单和 Policy Deadlines 表。新申请仍然暂停。期限表中的 Families 一行是匿名聊天受众扩展，不是 SDK 认证或重新申请的截止日期。新版申请表返回 401，字段没有读到。水印与测试应用文章打开的是英文正文。这些访问限制不是政策变更。本仓库中文正文是快照的编辑改写，不是 Google 已发布的中文页面文本；源文件记录已经打开 `zh-Hans` 页面的 Families 计划材料除外。快照没有记录未来的 SDK 认证生效日。严重 SDK 问题的 90 天窗口是帮助页在临时发布之后的整改窗口，不是新的政策生效日。开发者对 SDK 行为仍负责任，这是 `normative` 的 Play 规则。Families 广告 SDK 计划是操作层面的计划要求，不替代 Families 政策。SDK Index、AGP 元数据和供应商集成指南是实现说明。Index 徽章或供应商声明不是 Play 批准。

**核对日期：2026-10-23。** Google Play 将集成到应用中的 SDK/第三方代码视为应用合规责任的一部分。SDK 供应商的说明、SDK Index 的信号或自动扫描结果都不能替开发者核对最终 APK/AAB 中的版本、权限、数据流、用途和用户同意。

## 核心责任

- 开发者须确认每个直接和传递依赖 SDK 实际使用的权限、访问的数据、传输对象和用途；SDK 在后台默认收集的数据也要计入应用的数据披露，即使应用没有调用对应功能。
- SDK 获取的用户数据必须符合 Play 的用户数据、敏感权限、恶意软件、设备与网络滥用、家庭广告、广告和误导行为等规则。第三方直接收集或将数据传给供应商，不会转移应用开发者的责任。
- 只在实现用户已知并合理预期的应用功能所需时向第三方分享数据。SDK 供应商应公开说明数据处理；应用应验证该资料与集成的实际版本相符。
- SDK 若默认收集个人或敏感用户数据，应用必须满足适用的醒目披露与同意要求，并使 SDK 按用户选择停用或限制收集。Google Play 要求提供证据时，通常须在请求后 **两周内**提供；若请求给予更长期限，则按该期限。
- 不得出售个人或敏感用户数据；须用现代加密保护传输，且不得把持久设备标识符任意关联到敏感或可重置标识符。

## 重点禁止行为

| 风险 | 检查与处置要点 |
| --- | --- |
| 未披露或不合规的数据收集 | 盘点 SDK 的权限、数据类型、接收方、用途、保留和共享；同步更新 Data safety 与隐私政策。SDK 未提供清晰资料时，向供应商确认或移除。 |
| 儿童应用中的 SDK | 面向儿童的应用只能集成符合 Families 要求的 SDK；儿童广告、数据处理及广告定向有专门限制。截至 2026-10-23，Families Self-Certified Ads SDK 页面显示暂停接收新申请，现有参与者仍受现有项目要求约束；每次集成前核对当前清单与规则。 |
| 恶意软件、间谍软件或不透明行为 | SDK 不得盗取凭据、规避 Android 权限、隐蔽收集/外传与功能无关的数据、阻止卸载、关闭 SELinux，或利用隐藏功能逃避审核。 |
| 任意下载或自我更新 | 不得由 SDK 从 Google Play 以外来源下载可执行代码、安装未知来源应用或自行更新 APK。运行时加载的解释型代码不得引入政策违规或安全漏洞。 |
| 不安全 WebView/网络代码 | 不得让带 JavaScript Interface 的 WebView 加载不可信内容/URL；不得通过不安全连接下载文件或暴露安全漏洞。 |
| 未申报的前台服务 | 若 SDK 使用前台服务，必须具有合适用途并在合并后的应用 Manifest 中正确声明；SDK 用途本身也须符合 Play 政策。 |
| 欺骗和审核规避 | SDK 不得模拟系统界面、隐藏或休眠功能、误导用户，也不得按审核状态改变行为或规避审核。 |

## SDK 风险信号与处理期限

Google Play 会在 Play Console 中提示部分热门 SDK 的已知问题；提示可能出现在 Production 或 Release overview。针对导致违反政策的 SDK 版本，新版本可能被拒绝。若 SDK 版本被报告为“过时/有明显问题”，一般是警告并建议遵循供应商指引；如被报告存在 **critical issue**，帮助页允许暂时发布另一版本，但要求在该次发布后的 **90 天内**升级到较新版本。期限过后，将不能继续发布仍使用该问题 SDK 版本的应用版本。收到通知后应以账号里的实际警告、日期和修复说明为准。

[Google Play SDK Index](https://developer.android.com/distribute/sdk-index) 为常见商业 SDK 提供使用率、版本采用、权限请求、保留率和数据安全资料等信号；官方文档称覆盖 100 多个常用商业 SDK。其帮助页说明，目录资格限于通过 Maven 分发的商业 SDK、既有分类且达到使用门槛（被 100 个应用使用、至少 1 亿次应用安装）；统计仅来自与 Google Play 共享依赖数据、安装量超过 1,000 的应用，安装量按过去 30 天内至少启动过一次的设备计算。因此未列入目录不代表没有依赖或已获豁免。

目录条目可展示供应商登记徽标、Maven artifact、最新版本/API 要求、安装量分布、五个最常用版本、最近一年 SDK 版本使用的 Android 权限、留存概率、供应商版本消息及可选 Data safety 指引。artifact 清单可能不完整，Google Play 也明确说不一定能检测出 SDK 使用的所有权限；登记徽标仅代表供应商已在 SDK Console 登记，不是政策合规认证。权限信号可帮助发现受限访问、披露/同意要求，但仍要检查应用实际合并 Manifest、SDK 版本和数据流。互动目录 [play.google.com/sdks](https://play.google.com/sdks) 本次只返回嵌入式框架壳，离线知识库不包含逐 SDK 实时目录。

Android 构建文档补充了此索引如何进入发布流程：[AGP 会在构建产物中加入依赖元数据](https://developer.android.com/build/dependencies)，Play Console 可检查该元数据并对已知 SDK/依赖问题发出提示；Android Studio 也会对索引中标记为过时、违反 Play 政策、有已知漏洞或已弃用的 SDK 显示 lint 警告。元数据默认有助于诊断；构建配置允许选择不将其写入 APK/AAB，但官方建议保留。该文是 Android 构建实现指南，不创造新的 Play 政策义务；实际处置仍应以 Play Console 对应用/版本发出的通知和期限为准。

## 集成与版本更新清单

1. 导出直接和传递依赖清单，记录 SDK 名称、准确版本、来源、负责人、升级路径和已知问题；审核 AAB/APK 实际依赖文件，而不只看源码声明。
2. 在集成前阅读该版本公开的数据安全/权限文档，核对 SDK 初始化默认值、网络端点、持久标识符、日志、广告与后台行为。用 SDK Index 和供应商公告辅助判断，不把供应商自述当作唯一证据。
3. 将 SDK 权限与合并后的 Manifest、Play 商店宣传功能、Play Console 权限声明逐项对应；移除没有正当功能用途的权限或 SDK。
4. 让用户选择先于 SDK 读取敏感数据或联网收集：SDK 应读取应用偏好，或由应用在同意后初始化并传递同意状态。拒绝/撤回时验证 SDK 不继续处理不允许的数据。
5. 将 SDK 收集/分享、目的、安全方式和删除方式纳入 Data safety；让隐私政策及适用的应用内醒目披露覆盖第三方接收方、数据类型和用途。
6. 若面向儿童，检查 SDK 及版本是否仍符合 Families，自我认证广告 SDK 名单是否适用；不得仅因“SDK 支持儿童模式”就略过广告素材、数据和 mediation 配置核验。
7. 每次升级 SDK、改变初始化配置、调整数据流或切换广告/分析供应商时，重做权限、网络、披露、Data safety 和审核路径检查；上线后监控 Console 警告，收到证据请求或违规通知后按其期限处理。

## Families 儿童广告 SDK 分支

计划整体状态、适用边界、SDK 提供商义务和 9900633 正文所有直接链接另见[Families 自认证广告 SDK 计划专题](../families-self-certified-ads-program/families-self-certified-ads-program.zh-CN.md)。本页继续保留逐厂商、逐 Maven 坐标和版本后代，避免把动态名单复制成第二份。

截至 **2026-10-23**，Families 自我认证广告 SDK 计划暂不接收新申请，现有参加者继续按当前要求执行。仅当第三方广告 SDK 向儿童投放广告时，才需要按项目使用当前列出的自我认证 SDK/版本；混合受众应用可用中性年龄筛查把非认证 SDK 限于非儿童用户。名单与具体认证版本会变化，应用方须在每次发布/更新前查[实时 SDK 版本名单](https://support.google.com/googleplay/android-developer/answer/12955712?hl=en)。Google 明确不保证 SDK 自报认证资料的准确性，认证也不转移应用开发者责任。

### 水印与自我认证测试应用

官方[水印与测试应用要求](https://support.google.com/googleplay/android-developer/answer/9536665?hl=en)已打开全文。若 SDK 仅使用自有广告方案，该认证要求不适用；申请 Families 自我认证的广告 SDK 则须为自己的广告库存提供可识别的视觉标记（例如文字、图像、第三方图标、URL 或跳转页），并将标记放在该库存的**所有广告素材**上，方便审核者确认素材来源。测试应用应使用与线上相同或镜像的广告库存。

测试应用须为可运行的手机形态完整 Android APK，使用符合政策的最新已发布或即将发布 SDK 版本，调用 SDK 获取并展示广告，并能访问网络的全部实时投放库存，不得按地理位置限制。混合受众库存还须能区分完整库存与适合儿童/全年龄的库存；除非由有效中性年龄屏幕控制，否则不得把测试素材限制成库存中的少数广告。

页面内[旧版申请表](https://docs.google.com/forms/d/e/1FAIpQLSc8msikGDxjTHHFmIECoitMnpudaCbtrb_hhgzpUOznPhDoBw/viewform?p=adnet)已关闭并指向[新版 Families Ads Program 表单](https://docs.google.com/forms/d/e/1FAIpQLSesXeSKHTl55o1c0JsCgrDOcJJuGdpYBDgv1c8nSY_Rhz9_Gg/viewform)，但本次抓取工具无法读取新版表单字段；且计划页目前说明暂停接受新申请，因此不能据旧表单链接推断当前可申请。相关[广告与 IAP 课程](https://playacademy.exceedlms.com/student/path/22151/activity/32755)公开页只显示课程目标，启动课件需登录；其介绍指出课程涵盖儿童广告/IAP 标准，以及避免让 13 岁以下儿童感到困惑、分心、受操纵或过度商业化的实践，不能替代政策。

### Families SDK 政策正文直链逐项核验（2026-10-24）

重新打开[Families Self-Certified Ads SDK Policy](https://support.google.com/googleplay/android-developer/answer/12918983?hl=en)全文，并将正文内政策、操作、表单和法律目标逐项归类；重复引用合并显示。2026-10-24 再核对英文/`zh-Hans` 计划页、政策页、版本清单和 Policy Deadlines 表：仍暂停新申请、现有参加者要求不变；清单仍为 14 个 Maven 行/13 个不同供应商目标。期限表的 Families 日期对应匿名聊天受众扩展，不是 SDK 认证或重新申请期限。Help 社区、Contact 与侧栏是页面导航，不计作正文政策链接。

| 正文目标 | 页面与本地关系 | 访问与边界 |
| --- | --- | --- |
| [Developer Policy Center](https://play.google.com/about/developer-content-policy/) | 上位政策目录；当前规范入口是 [`play.google.com/developer-content-policy/`](https://play.google/developer-content-policy/)，含政策类别与直接入口。 | 正文链接观察到重定向；规范目录页已打开并纳入政策目录专题。目录不是单独的 Families 条款。 |
| [Google Play Families Policies](https://support.google.com/googleplay/android-developer/answer/9893335?hl=en) | 应用侧儿童受众、数据、SDK、广告、社交和功能要求；见[儿童安全专题](../age-restricted-child-safety/age-restricted-child-safety.zh-CN.md)。 | 目标正文已完整打开；Families 链接中旧的 Ads and Monetization 路由也重定向回此页。 |
| [Families Self-Certified Ads SDK Program Requirements](https://support.google.com/googleplay/android-developer/answer/9900633?hl=en) | 计划状态、SDK/中介提供商条件、应用方边界及正文其他链接；见[计划专题](../families-self-certified-ads-program/families-self-certified-ads-program.zh-CN.md)。 | 正文已打开；新申请暂停，现有参与者要求不变。 |
| [新版 interest form](https://docs.google.com/forms/d/e/1FAIpQLSesXeSKHTl55o1c0JsCgrDOcJJuGdpYBDgv1c8nSY_Rhz9_Gg/viewform) 与[旧版 self-certify form](https://docs.google.com/forms/d/e/1FAIpQLSc8msikGDxjTHHFmIECoitMnpudaCbtrb_hhgzpUOznPhDoBw/viewform?p=adnet) | 计划申请/提供商版本自我认证所用表单入口。 | 新表单直链返回 401，字段不可读；旧表单显示已弃用并引向新表单。结合暂停公告，不推断当前开放资格或未读字段。 |
| [Watermark and test app requirements](https://support.google.com/googleplay/android-developer/answer/9536665?hl=en) | 创意标识、测试 APK、完整实时广告库存及混合受众分流条件；上文已摘要。 | 英文正文已打开；测试要求不等于名单已认证，也不证明某供应商当前仍合格。 |
| [Families Ads and Monetization](https://play.google.com/about/families/ads-monetization/) | 旧广告规则路径；现行正文在 Families Help 页面。 | 从本政策点击时观察到跳转至 `answer/9893335`，抓取工具跟随失败；目标正文已单独打开。旧链接不是独立条文。 |
| [Ad walls / Ads policy](https://support.google.com/googleplay/android-developer/answer/9857753?hl=en) | 广告墙、不当/干扰性广告与误触规则；见[广告与推广专题](../ads-and-advertising/ads-and-advertising.zh-CN.md)。 | 当前 Ads 正文已完整打开；Families 对儿童广告还附加适龄素材和格式要求。 |
| [Personal and sensitive information / User Data](https://support.google.com/googleplay/android-developer/answer/10144311?hl=en) | 通过 SDK 收集儿童数据时的披露、用途、共享和标识符控制；见[用户数据专题](../user-data/user-data.zh-CN.md)。 | 旧链接跳转到现行正文；当前正文已打开。 |
| [U.S. COPPA resource](https://www.ftc.gov/business-guidance/privacy-security/childrens-privacy) | 美国儿童隐私法律入口；不是 Google Play 条款。 | FTC 当前入口正文已打开；具体适用和法律后代按[外部法律参考](../user-data-policy-references/user-data-policy-references.zh-CN.md)分别分析。 |
| [EU GDPR text](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32016R0679) | 欧盟法规原文；不是由 Families Help 替代的 Play 规则。 | 从 SDK 政策直链打开仅返回三行，不能称已读法规全文；儿童同意年龄、Article 8 和 GDPR 后代状态见[外部法律参考](../user-data-policy-references/user-data-policy-references.zh-CN.md)。 |

该表闭合了正文直接目标的页面映射，但表单字段、EUR-Lex 正文和法律/技术目标的更深后代仍部分覆盖；不得把“已登记直链”说成无限递归闭合。

下表是官方清单在 **2026-10-23** 的版本快照，供离线检索；清单可增删/撤销，不应将该快照当作当前批准证明。

| 广告 SDK | Maven 坐标 | 页面列出的自我认证版本 |
| --- | --- | --- |
| AdColony | `com.adcolony:sdk` | 4.8.0 或更高版本 |
| AddApptr | `com.intentsoftware.addapptr:AATKit-family-safe` | 3.8.3 或更高版本 |
| Chartboost | `com.chartboost:chartboost-sdk` | 9.1.1 或更高版本 |
| DT Exchange SDK | `com.fyber:marketplace-sdk` | 8.2.1 或更高版本 |
| Google Ad Manager | `com.google.ads.interactivemedia.v3:interactivemedia` | 3.19.0 或更高版本 |
| Google Ad Manager | `com.google.android.gms:play-services-pal` | 18.0.0 或更高版本 |
| Google AdMob | `com.google.android.gms:play-services-ads` | 19.0.0 或更高版本 |
| HyprMX | `com.hyprmx.android:HyprMX-SDK` | 6.0.3 或更高版本 |
| InMobi | `com.inmobi.monetization:inmobi-ads` | 10.5.5 或更高版本 |
| ironSource | `com.ironsource.sdk:mediationsdk` | 7.2.1 或更高版本 |
| Kidoz | `net.kidoz.sdk:kidoz-android-native` | 8.9.4 或更高版本 |
| SuperAwesome | `tv.superawesome.sdk.publisher:superawesome` | 8.4.3 或更高版本 |
| Unity Ads | `com.unity3d.ads:unity-ads` | 4.0.1 或更高版本 |
| Vungle | `com.vungle:publisher-sdk-android` | 6.10.4 或更高版本 |

名单页同时说明 AppLovin 已退出该计划；该页面给出的旧迁移日期为 2023-05-31。依赖核验应检查完整 Maven artifact 和实际集成版本，而不能只匹配供应商品牌名。

### 官方清单供应商直链审计（2026-10-23）

重新打开官方[Families SDK/版本清单](https://support.google.com/googleplay/android-developer/answer/12955712?hl=en)：当日仍显示 14 个 Maven 条目（Google Ad Manager 占两项）及 13 个不同供应商目标。官方页面是认证状态和精确 Maven 坐标的控制来源；供应商主页、营销说法或隐私承诺不能代替清单。表中“已读”仅指目标页面的访问/正文状态，不代表供应商的其他网页均已递归遍历。

| 清单供应商 | 官方直链及本次目标状态 | 与 Play 认证判断的关系 |
| --- | --- | --- |
| AdColony | [AdColony/Affle 品牌页](https://www.adcolony.com/)称 AdColony 已成为 Affle 的一部分，但没有可读 SDK 指南。Affle 于 2026-06-15 宣布与 DT 签订资产购买协议，范围包括 Android/iOS SDK；DT 于 2026-06-16 表示双方前一日宣布出售，并称 legacy SDK、部分集成、技术平台和域名不再属于 DT 的统一平台战略。 | Google 当前清单仍列 `com.adcolony:sdk` 4.8.0+。Google AdMob 的 [Android](https://developers.google.com/admob/android/mediation/adcolony)（2026-09-11 更新）和 [iOS](https://developers.google.com/admob/ios/mediation/adcolony)（2026-10-16 更新）mediation 指南均标为 deprecated 并建议移除 AdColony SDK/adapter 和 mediation source。这是 AdMob 集成支持状态，不等于 Google Play Families 名单已撤销该 artifact；也不能据此断言所有 AdColony SDK 构建均无法运行。资产移交后的维护方、发版计划及 Play 自认证延续情况仍须向 Affle/Google 核实。 |
| AddApptr | [Gravite（原清单目标）](https://gravite.net/) → Gravite 营销页，页脚仍显示 AddApptr GmbH；其 API 文档入口 [dashboard.gravite.net/apiDocumentation](https://dashboard.gravite.net/apiDocumentation) 未能读取正文。 | Google 清单坐标是 `com.intentsoftware.addapptr:AATKit-family-safe` 3.8.3+。厂商主页不是 Families 认证证据；API 页面状态单独记录为受限。 |
| Chartboost | [Chartboost](https://www.chartboost.com/) → 当前跳转到 LoopMe 的 Chartboost 页面。 | 现行产品/公司关系说明，不证明特定 SDK 版本通过 Families 自认证；以官方 Maven 条目 `com.chartboost:chartboost-sdk` 9.1.1+ 为准。 |
| DT Exchange SDK | [旧入口](https://developer.digitalturbine.com/hc/en-us/articles/360010814637-Getting-Started-with-DT-Exchange) → [当前 DT Exchange 入门页](https://docs.digitalturbine.com/dt-exchange/publishers/getting-started-with-dt-exchange)；页内另有 [DT Console 应用/广告位设置](https://docs.digitalturbine.com/dt-console/offer-wall/setting-up-an-existing-app)、[注册](https://docs.digitalturbine.com/dt-console/authorization/signing-up-for-dt-console)、[Android SDK guide](https://docs.digitalturbine.com/dt-exchange/sdk-configuration/integrating-the-android-sdk.md)、[Privacy](https://docs.digitalturbine.com/dt-exchange/publishers/getting-started-with-dt-exchange/privacy)。 | 当前入门页介绍程序化变现并列出 SDK 接入步骤；Android 正文/Privacy 子页当前抓取受限，Console 设置页落到 Offer Wall 指引，注册流程可读。它是另一个供应商产品分支。DT 关于 AdColony 资产出售/战略的公告并不表示现行 DT Exchange SDK 停运；该产品须按自己的 Maven 坐标 `com.fyber:marketplace-sdk` 8.2.1+ 和 Android 实现文档状态核验。 |
| Google Ad Manager | [Google Ad Manager](https://admanager.google.com/home/) → 通用产品入口；清单中的两个 Maven 条目共用此直链。 | 官方认证表仍分别列 IMA `com.google.ads.interactivemedia.v3:interactivemedia` 3.19.0+ 与 PAL `com.google.android.gms:play-services-pal` 18.0.0+；主页不替代精确 artifact 核验。 |
| Google AdMob | [AdMob Families 实现帮助](https://support.google.com/admob/answer/6223431) 已全文审阅，并已在[儿童安全专题](../age-restricted-child-safety/age-restricted-child-safety.zh-CN.md)记录其实现建议与过时代码差异。 | 清单坐标 `com.google.android.gms:play-services-ads` 19.0.0+；AdMob 实现帮助与 Google Play 的认证/政策规则分层处理。 |
| HyprMX | [清单所链 SDK 文档入口](https://documentation.hyprmx.com/sdk/) 当前为旧路径/404；改从官方文档导航打开[Android/Amazon 集成指南](https://documentation.hyprmx.com/sdk-integration-guides/android-amazon)。 | 清单坐标 `com.hyprmx.android:HyprMX-SDK` 6.0.3+；当前指南显示同坐标 6.4.7，并称可选的 Ads Identifier 依赖由应用方负责满足所有 Play 政策（含 Families）。坐标一致且版本高于门槛，但具体发版仍须核对实时清单和最终依赖。 |
| InMobi | [InMobi](https://www.inmobi.com/) → 通用企业/广告平台主页。 | 本次入口未提供可核验的 SDK 版本或 Families 处理细节；不由主页推定认证。按清单 `com.inmobi.monetization:inmobi-ads` 10.5.5+ 核对。 |
| ironSource | [ironSource](https://www.ironsrc.com/) → 当前跳转到 Unity Grow，产品导航包括 LevelPlay/Unity Ads。 | 公司/产品品牌变更不等于 Play 认证转移证明；清单仍以精确 `com.ironsource.sdk:mediationsdk` 7.2.1+ 条目为准。 |
| Kidoz | [Kidoz](https://kidoz.net/) → 当前 `www.kidoz.net` 入口，浏览器未返回可读正文。另见厂商的[隐私政策索引](https://www.kidoz.net/privacy-policies)和[Publisher Agreement](https://www.kidoz.net/publisher-agreement)，但目标页正文同样不可读。 | 搜索索引可见厂商的 Website/SDK Privacy Policy、Safe Ad Policy、PRIVO 会员等自述；这些不是对精确 `net.kidoz.sdk:kidoz-android-native` 8.9.4+ artifact 的 Play 认证证明。 |
| SuperAwesome | [SuperAwesome](https://www.superawesome.com/) → youth advertising 产品页；另打开[广告标准](https://www.superawesome.com/superawesome-ad-standards/)及 [Awesome Ads Marketplace 隐私政策](https://www.superawesome.com/privacy-hub/awesomeads-privacy-policy/)。 | 厂商标准涵盖年龄适配、广告可识别和 SAFE AD 水印；隐私政策称其 Awesome Ads 以情境信息投放、默认按儿童实施数据最小化。它们是厂商承诺/做法，不能替代 Play Families、User Data、Data safety 或自认证名单。 |
| Unity Ads | [Unity](https://unity.com/) → 通用企业入口；ironSource 链路另显示 Unity Grow 产品。 | 不从品牌主页推定 Families 状态；以清单 `com.unity3d.ads:unity-ads` 4.0.1+ 为准。 |
| Vungle | [Google 清单指向的 Vungle SDK 下载入口](https://publisher.vungle.com/sdk/sdks/android/) → [Android/Amazon 下载页](https://support.vungle.com/hc/en-us/articles/15722228922395-Download-Vungle-SDK-for-Android-Amazon)。 | 截至 2026-10-23，Google Families 当前名单仍列 `com.vungle:publisher-sdk-android` 6.10.4+。厂商 2024-09-17 的 [v6 Android/Amazon 指南](https://support.vungle.com/hc/en-us/articles/18092084187931-Integrate-Vungle-SDK-v-6-for-Android-or-Amazon)给出同坐标 6.12.1，并对 Family apps 建议 6.10.4+；Sonatype 的 [v6 artifact 页面](https://central.sonatype.com/artifact/com.vungle/publisher-sdk-android)也列 6.12.1。这一坐标/版本与名单条目一致。旧 [Android-SDK 仓库](https://github.com/Vungle/Android-SDK)现明确标为 deprecated / 不再维护，并要求新集成不要使用其示例、7.x 转到另一个 [VungleAds-SDK 仓库](https://github.com/Vungle/VungleAds-SDK)。2026-09-30 的 [v7 指南](https://support.vungle.com/hc/en-us/articles/360002922871-Integrate-Vungle-SDK-for-Android-or-Amazon)和 [Android changelog](https://github.com/Vungle/VungleAds-SDK/blob/master/CHANGELOG-Android.md)均给出 `com.vungle:vungle-ads:7.7.9`；changelog 记载 7.0.0 从 6.x 静态 API 改为实例 API并按广告格式分类。Sonatype [v7 artifact 页面](https://central.sonatype.com/artifact/com.vungle/vungle-ads)当次显示 7.7.8，与厂商指南/changelog 的 7.7.9 不同，版本快照以较新的厂商说明为准。当前 Play 名单没有列 `vungle-ads`，所以 7.x 的 Families 自认证状态仍未确认；不得由品牌相同、仓库链接或 API 关系推断认证转移。Vungle Help Center 将 SDK 品牌仍称 Vungle，并把 Liftoff Monetize 描述为变现套件品牌；品牌说明本身也不证明 artifact 或认证映射。 |

### 供应商直链下的政策相关后代

| 分支 | 已打开的直接目标 | 分析与覆盖边界 |
| --- | --- | --- |
| AdColony → Affle 资产与 AdMob mediation 弃用 | [Affle 资产购买公告](https://affle.com/affle_news/affle-announces-strategic-acquisition-of-adcolony-technology-assets-and-trademark-from-dt)、[DT 战略说明](https://digitalturbine.com/blog/one-platform-full-focus)、Google AdMob [Android](https://developers.google.com/admob/android/mediation/adcolony) / [iOS](https://developers.google.com/admob/ios/mediation/adcolony) AdColony mediation 页、[从 mediation group 编辑/移除广告源](https://support.google.com/admob/answer/9850777) | Affle 公告称协议拟取得 AdColony Android/iOS SDK 等资产；DT 公告称双方前一日宣布出售，并称 legacy SDK 等资产不再服务于 DT 的统一平台战略，但没有说 SDK 一律无法运行。Google AdMob 两平台页建议移除 SDK/adapter；AdMob Help 说明移除操作按 mediation group 执行，改动不会自动传播至其他 group。此为 AdMob 产品/技术状态，不是 Play Families 自认证决定。Google Play 名单仍列 `com.adcolony:sdk` 4.8.0+；它与 AdMob adapter `com.google.ads.mediation:adcolony` 不是同一 Maven artifact。各页品牌/导航后代未全量审阅。 |
| DT Exchange → Android 集成 | [旧入门入口](https://developer.digitalturbine.com/hc/en-us/articles/360010814637-Getting-Started-with-DT-Exchange)、[当前入门页](https://docs.digitalturbine.com/dt-exchange/publishers/getting-started-with-dt-exchange)、[DT Console 应用/广告位设置](https://docs.digitalturbine.com/dt-console/offer-wall/setting-up-an-existing-app)、[注册流程](https://docs.digitalturbine.com/dt-console/authorization/signing-up-for-dt-console)、[Android SDK guide](https://docs.digitalturbine.com/dt-exchange/sdk-configuration/integrating-the-android-sdk.md)、[Privacy](https://docs.digitalturbine.com/dt-exchange/publishers/getting-started-with-dt-exchange/privacy) | 当前入门页说明程序化广告变现并链接 Console、Android/iOS 接入及隐私页。注册流程已读；设置页跳到 Offer Wall 页面；Android 子页返回旧路径不存在并建议 `.md` 目标，抓取仍失败；Privacy 页返回 400 content-type 错误。它们均是厂商操作/技术页，不是 Play 认证凭证；DT 的 AdColony 资产出售/战略公告不证明现行 DT Exchange SDK 已停运；两条厂商产品线须分别核验。 |
| HyprMX → Android/Amazon guide | [Google Play services Ads Identifier 设置](https://developers.google.com/android/guides/setup#list-dependencies)、[Families program](https://play.google.com/console/about/families/)、[6.4+ migration guide](https://documentation.hyprmx.com/sdk-integration-guides/android-amazon/migrate-to-version-6.4%2B)、[Data safety questionnaire](https://documentation.hyprmx.com/sdk-integration-guides/android-amazon/googles-data-safety-questionnaire)、[Privacy](https://documentation.hyprmx.com/sdk-integration-guides/android-amazon/privacy)、[Rewarded Ads](https://documentation.hyprmx.com/sdk-integration-guides/android-amazon/ad-formats/rewarded-ads)、[Interstitial Ads](https://documentation.hyprmx.com/sdk-integration-guides/android-amazon/ad-formats/interstitial-ads)、[Banner/MREC Ads](https://documentation.hyprmx.com/sdk-integration-guides/android-amazon/ad-formats/banner-mrec-ads)、Kotlin [suspending functions](https://kotlinlang.org/docs/composing-suspending-functions.html) / [higher-order functions](https://kotlinlang.org/docs/lambdas.html#higher-order-functions)、[UID2](https://unifiedid.com/)、[ID5](https://id5.io/)、[LiveIntent ID](https://www.liveintent.com/identity-solutions/)、[厂商 Privacy Policy](https://www.hyprmx.com/privacy-policy.html)、[EULA](https://hyprmx.com/eula.html) | 集成指南正文及 migration、Data safety、Privacy、Rewarded、Banner/MREC 页面已读取；Interstitial 页面本次抓取失败。指南要求有条件时由开发者自行确保包括 Families 在内的 Play 合规；可选 Ads Identifier、替代身份标识符与隐私披露需要纳入数据流/同意评估。UID2 落地页描述以加密邮箱/电话号码建立可定向的广告身份；ID5 与 LiveIntent 页面是身份广告产品介绍。均未说明可用于儿童流量，需按实际数据类型、目的、同意和 Families 标识符限制独立审查。HyprMX 隐私政策标注生效于 2020-09-16，提到 GAID、设备/活动和可能经同意的位置等；EULA 另指向其隐私政策。Kotlin 两页仅解释语言语法，均非 Play 政策。广告格式页是工程说明，不是认证。 |
| Kidoz → 厂商隐私/出版商条款 | [Privacy Policies](https://www.kidoz.net/privacy-policies)、[Publisher Agreement](https://www.kidoz.net/publisher-agreement) | 两个官方目标都没有可读正文；搜索索引显示其有 SDK 隐私和 Safe Ad Policy，并写有出版商自行负责平台规则/法律合规的合同条款。未读到条款全文；不将厂商 COPPA/PRIVO 自述等同于 Play 自认证。 |
| SuperAwesome → youth advertising standards | [SuperAwesome Ad Standards](https://www.superawesome.com/superawesome-ad-standards/)、[Awesome Ads Marketplace Privacy Policy](https://www.superawesome.com/privacy-hub/awesomeads-privacy-policy/) | 标准覆盖儿童/青少年广告类别、年龄适配、清晰标示、不得误导/利用脆弱性；厂商称 Marketplace 创意带 SAFE AD 水印且按情境而非行为追踪投放。政策明确它不是法律意见；隐私政策只适用于 Awesome Ads。审核来源为 2026-10-23，政策最近更新标记为 2026-02-17 / 2026-04-22。 |
| Vungle → v6 / v7 版本与政策相关后代 | [Google Families 政策](https://support.google.com/googleplay/android-developer/answer/9893335)、[Families 当前 SDK 名单](https://support.google.com/googleplay/android-developer/answer/12955712?hl=en)、[Vungle v6 指南](https://support.vungle.com/hc/en-us/articles/18092084187931-Integrate-Vungle-SDK-v-6-for-Android-or-Amazon)、[v7 指南](https://support.vungle.com/hc/en-us/articles/360002922871-Integrate-Vungle-SDK-for-Android-or-Amazon)、[Android/Amazon 下载页](https://support.vungle.com/hc/en-us/articles/15722228922395-Download-Vungle-SDK-for-Android-Amazon)、[v6 Maven artifact](https://central.sonatype.com/artifact/com.vungle/publisher-sdk-android)、[v6 POM 源码仓库](https://github.com/Vungle/vungle-android-sdk)、[v7 Maven artifact](https://central.sonatype.com/artifact/com.vungle/vungle-ads)、[v6 Android-SDK 样例仓库](https://github.com/Vungle/Android-SDK)、[v6 README](https://github.com/Vungle/Android-SDK/blob/master/README.md)、[v6 changelog](https://github.com/Vungle/Android-SDK/blob/master/CHANGELOG.md)、[v7 VungleAds-SDK 仓库](https://github.com/Vungle/VungleAds-SDK)、[v7 README 路由](https://github.com/Vungle/VungleAds-SDK/blob/master/README.md)、[v7 Samples 目录](https://github.com/Vungle/VungleAds-SDK/tree/master/Samples)、[Android Samples 目录](https://github.com/Vungle/VungleAds-SDK/tree/master/Samples/android)、[Java Samples 目录](https://github.com/Vungle/VungleAds-SDK/tree/master/Samples/android/Java)、[Kotlin Samples 目录](https://github.com/Vungle/VungleAds-SDK/tree/master/Samples/android/Kotlin)及[Android changelog](https://github.com/Vungle/VungleAds-SDK/blob/master/CHANGELOG-Android.md)、[旧版 JavaDoc](https://vungle.github.io/vungle-android-sdk/javadoc)、[Publisher Dashboard 指南](https://support.vungle.com/hc/en-us/articles/360021968731-Using-the-Publisher-Dashboard)、[SDK Help Center 目录](https://support.vungle.com/hc/en-us/categories/200269670-Vungle-SDK)、[支持表单](https://support.vungle.com/hc/en-us/requests/new)、[广告格式页](https://support.vungle.com/hc/en-us/articles/360047788532-Integrate-Interstitial-Ads)、[横幅页](https://support.vungle.com/hc/en-us/articles/360048256211-Integrate-Banner-Ads)、[激励广告页](https://support.vungle.com/hc/en-us/articles/360048262131-Integrate-Rewarded-Ads)、[高级设置](https://support.vungle.com/hc/en-us/articles/360047780372-Advanced-Settings)、[下载入口](https://dashboard.vungle.com/sdk)、[变现帮助目录](https://support.vungle.com/hc/en-us/categories/200269670-Monetization)、[发布商报表页](https://support.vungle.com/hc/en-us/articles/211025797-Publisher-Application-Reports) | v6 指南正文称 mixed-audience app 应在适用时使用 COPPA API，并建议 Family apps 使用 v6.10.4+；它的同坐标例子是 6.12.1。v6 README 再次明确该仓库不再维护、仅供历史参考，并禁止新集成使用其代码，转而指向 v7 仓库；v6 changelog 将 6.12.1 标为 2023-01-10，并记载 6.10.4 加入 COPPA API GA、符合当时的 Google Privacy Policies。v7 仓库列出 Samples 与 Android changelog；Samples/android 目录列出 Java/Kotlin 子目录，但两者抓取 Cache miss；单独的 v7 README 路由返回 404。changelog 显示 7.7.9（2026-09-30），以及 7.0.0 从 6.x 静态 API 改为实例 API、按格式拆分类和增加无缓存竞价支持。这些是 SDK 版本/实现证据，不是 Play 对 v7 的自认证证据。v6 指南的 Google Families、Advanced Settings 与广告格式目标已纳入相应专题；旧 Maven POM 的源码仓库链接 Cache miss，旧 JavaDoc 跳到 GitHub 登录，Publisher Dashboard 是账号/应用/广告位运维指南，不是政策。Dashboard 的直接后代中，SDK 下载返回 502、变现目录 Cache miss、报表页 404；支持表单可读，询问账号、包名、SDK/adapter 版本、placement、广告素材与复现信息。其余仓库 Samples、一般帮助中心侧栏、页脚链接和更深依赖未全部递归打开。Sonatype 的 v7 页面显示 7.7.8，而同日厂商指南与 changelog 是 7.7.9，审计保留此版本差异。|

**本分支状态：** 已逐项尝试官方清单的 13 个供应商直链，并打开若干政策相关直接后代；Generic/营销入口不代表已审核所有 SDK 子页。Gravite API、DT Android 集成目标、Kidoz 两个政策文档和 HyprMX Interstitial 页面受抓取限制；HyprMX 的三个替代标识符站点及完整厂商隐私/合同后代未遍历。Families 名单、供应商运营状态、artifact/版本及 SDK 数据流均须在具体发布前实时复核。 

儿童广告实现至少核对：广告素材适龄并按 Everyone/Mature 等年龄层评级；实时竞价素材已审核且把隐私信号传给竞价方；广告清楚可辨，不得诱导误触、遮挡正常使用或以情绪操纵儿童。会干扰正常使用/游戏的广告须可在 5 秒后关闭；儿童请求须关闭个性化、兴趣定向和再营销，并不得传输 AAID、SIM Serial、Build Serial、BSSID、MAC、SSID、IMEI 或 IMSI 等列明标识符。中介平台要么只调用 Families 自我认证 SDK，要么能证明所有广告都受同等保护，并传递儿童定向状态和内容评级。应用方须把广告 SDK 的数据访问、收集、使用和共享同步到隐私披露及 Data safety。

政策允许特定自有媒体交叉推广和仅用于库存管理的直接广告协议不经第三方 SDK 认证；但应用开发者仍须保证广告适龄、数据处理符合 User Data/Families，并满足当地法律。详见[Families 广告 SDK 专题要求](https://support.google.com/googleplay/android-developer/answer/12918983?hl=en)和[计划说明](https://support.google.com/googleplay/android-developer/answer/9900633?hl=en)；SDK 提供商还须提交测试 APK、条款/隐私政策/集成指南、创意审核和可视识别（如 watermark）机制等材料。

## 子链接与递归范围

| 来源/关系 | 目标页 | 摘要和状态 |
| --- | --- | --- |
| SDK Requirements 正文及其关联政策 | [User Data](../user-data/user-data.zh-CN.md)、[Sensitive permissions](../sensitive-permissions/sensitive-permissions.zh-CN.md)、[Device and Network Abuse](https://support.google.com/googleplay/android-developer/answer/16559646?hl=en)、[Malware](https://support.google.com/googleplay/android-developer/answer/9888380?hl=en)、[Mobile Unwanted Software](https://support.google.com/googleplay/android-developer/answer/9970222?hl=en)、[Families Self-Certified Ads SDK](https://support.google.com/googleplay/android-developer/answer/12918983?hl=en)、[Ads](../ads-and-advertising/ads-and-advertising.zh-CN.md)、[Deceptive Behavior](https://support.google.com/googleplay/android-developer/answer/17006354?hl=en)、[Policy Center / Developer Program Policies](https://support.google.com/googleplay/android-developer/topic/9858052) | 安全集成帮助页把前八项列为 SDK 违规的常见关联政策，并链接到 Policy Center 目录。旧敏感权限、设备与网络滥用、欺骗行为链接分别重定向到现行政策页；Policy Center 是政策目录，不是新增的 SDK 专项义务。 |
| 安全集成页的政策、工具与处理帮助直链 | [SDK Requirements](https://support.google.com/googleplay/android-developer/answer/13323374)、[Make informed choices with Google Play SDK Index](https://support.google.com/googleplay/android-developer/answer/12034434)、[My app has been removed from Google Play](https://support.google.com/googleplay/android-developer/answer/2477981)、[Google Play Data safety 说明](https://support.google.com/googleplay/android-developer/answer/10787469)、[Using third-party SDKs in your app](https://support.google.com/googleplay/android-developer/answer/10358880) | 正文的 20 个链接引用对应 19 个去重目标，均已尝试；移除应用帮助被两个锚点重复引用。开发者对第三方代码和 SDK 数据处理负责，SDK 数据视同应用收集；须最小化共享、了解权限/数据/用途、传递用户同意，并移除或替换违规版本。SDK Index 与 Play Console 提供诊断信号，不构成合规认证。**90 天 critical-issue 升级期限来自第三方 SDK 帮助页**：在使用存在 critical issue 的版本暂时发布后，须在该次发布起 90 天内升级；期限后不得继续发布仍含该版本的应用版本。 |
| 安全集成页的最佳实践、用户说明与学习资源 | [Android SDK user-safety best practices](https://developer.android.com/guide/practices/sdk-best-practices)、[Google Play Academy SDK best-practices course](https://g.co/playacademy/sdkbestpractices)、[面向用户的 Data safety 说明](https://support.google.com/googleplay/answer/11416267)、[Android SDK Index 概览](https://developer.android.com/distribute/sdk-index)、[醒目披露与同意最佳实践](https://support.google.com/googleplay/android-developer/answer/11150561) | 五个目标均已尝试；Academy 课程链接返回 Cache miss，未推断课程内容。其余正文已打开。Data safety 消费者说明帮助解释用户看到什么，不是开发者政策；Android/Play Academy 内容属于辅助材料，不能替代政策正文。 |
| Using third-party SDKs 帮助页 → Android 构建与 Privacy by design 课程 | [App Bundle 旧入口](https://developer.android.com/platform/technology/app-bundle)、[Android Studio releases 页面（AGP 4.0 锚点的当前目标）](https://developer.android.com/studio/releases/)、[Privacy by design Academy 路径](https://playacademy.exceedlms.com/student/path/264896-privacy-by-design) | App Bundle 旧入口重定向到已审阅的现行指南，是上传/分发技术说明。帮助页中名为 Android Gradle Plugin 4.0 的链接目前打开的是 Android Studio Rabbit 1（2026.2.1）发布页，不能当作 AGP 4.0 历史说明。Privacy by design 路径的公开课程大纲和活动见下行；该页还展示了登录与启动入口，但课程正文无法读取。 |
| Privacy by design Academy 课程 → 七个活动目标 | [Build privacy-friendly apps · 13 分钟](https://playacademy.exceedlms.com/student/path/264896/activity/348012)、[Declared permissions and in-app disclosures · 2 分钟](https://playacademy.exceedlms.com/student/path/264896/activity/348013)、[Showcase your app’s safety practices with the Data safety section · 9 分钟](https://playacademy.exceedlms.com/student/path/264896/activity/538644)、[Security development lifecycle · 7 分钟](https://playacademy.exceedlms.com/student/path/264896/activity/347557)、[Threat modeling basics · 7 分钟](https://playacademy.exceedlms.com/student/path/264896/activity/347558)、[Introduction to app security best practices · 6 分钟](https://playacademy.exceedlms.com/student/path/264896/activity/347559)、[Vulnerability Disclosure Program（选修）](https://playacademy.exceedlms.com/student/path/264896/activity/347561) | 课程页标注 2021-04-21 发布，公开列出 3 个隐私与 3 个安全活动，以及一个选修 VDP。七个活动直链均返回 Cache miss；Get Started 路由也未能读取。以上只保存可见课程元数据，不推断课件内容或政策义务。 |
| 安全集成页的共享政策侧栏 | [Policy education and app requirements 目录](https://support.google.com/googleplay/android-developer/topic/12798386?hl=en)、[前台服务与全屏 intent 预览](https://support.google.com/googleplay/android-developer/answer/16965181?hl=en) | 目录及其 31 个帮助文章目标、另列的 FGS 预览均逐项尝试；31 个文章目标中 30 个可读，Android Health Permissions FAQ 本次超时，但其 2026-10-23 既有全文审阅记录保留。共享侧栏是导航，不代表这些专题都由 SDK 页面新增；每个目标的后代状态按逐 URL 台账分别记录，仍有部分未递归完成。 |
| 安全集成页页脚支持入口 | Help Community、Contact us | 两个入口均已尝试；Community 返回 Cache miss，Contact us 跳转到需账号/Play Console 的支持流程。它们是支持渠道，不是政策正文。 |
| Device and Network Abuse 子孙页 | [App Security Improvement Program](https://developer.android.com/privacy-and-security/googleplay-asi) | 用于解释 Play Console 可能发送的安全修复通知及历史漏洞活动；历史活动日期不应当作当前新期限。 |
| 在线交互式索引 | [Google Play SDK Index](https://play.google.com/sdks) | 目标站由动态嵌入内容组成，本次未能提取完整 SDK 目录；Android Developers 的说明页已读取。逐 SDK 的最新版本/安全状态须在线核查。 |
| Families 儿童广告 SDK | [Families Self-Certified Ads SDK Program](https://support.google.com/googleplay/android-developer/answer/9900633?hl=en)、[Families SDK policy](https://support.google.com/googleplay/android-developer/answer/12918983?hl=en)、[current SDK/version list](https://support.google.com/googleplay/android-developer/answer/12955712?hl=en)、[watermark/test-app requirements](https://support.google.com/googleplay/android-developer/answer/9536665?hl=en)、[closed legacy form](https://docs.google.com/forms/d/e/1FAIpQLSc8msikGDxjTHHFmIECoitMnpudaCbtrb_hhgzpUOznPhDoBw/viewform?p=adnet)、[new interest form](https://docs.google.com/forms/d/e/1FAIpQLSesXeSKHTl55o1c0JsCgrDOcJJuGdpYBDgv1c8nSY_Rhz9_Gg/viewform)、[Teacher Approved ads/IAP course](https://playacademy.exceedlms.com/student/path/22151/activity/32755) | 四个政策/帮助正文页已打开；水印/测试 APK 页面完整列出创意标记、手机 APK、最新 SDK、全量库存、混合受众区分等条件。旧表单重定向到新版，但新版字段不可读；课程公开简介可读、课件需登录。计划当前暂停新申请，清单为动态状态。 |

本页为结构化双语改写，不保存政策全文。SDK 产品与版本、Families 名单、账号告警和实际数据流会变化；发布前应回到官方现行页面和 Play Console 核对。

## 关联条目

- [用户数据与隐私政策](../user-data/user-data.zh-CN.md)
- [Data safety 表单](../data-safety/data-safety.zh-CN.md)
- [敏感信息权限与 API](../sensitive-permissions/sensitive-permissions.zh-CN.md)
- [儿童安全与 Families](../age-restricted-child-safety/age-restricted-child-safety.zh-CN.md)
- [广告与推广](../ads-and-advertising/ads-and-advertising.zh-CN.md)
- [权限声明与审核](../permissions-declaration/permissions-declaration.zh-CN.md)
- [官方 SDK Requirements](https://support.google.com/googleplay/android-developer/answer/13323374?hl=en)
