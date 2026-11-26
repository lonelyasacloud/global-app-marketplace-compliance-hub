---
id: google-play.android-developer-console-accounts
platform: google-play
language: zh-CN
authority: operational
status: current
kb_checked_at: 2026-10-24
review_due: 2027-01-24
regions: [global]
topics: [android-developer-console, developer-identity, package-registration, duns, terms-of-service]
snapshot_id: android.developer-console-accounts
snapshot_package: "GooglePlay-KnowledgeBase-2026-10-24-review.zip"
coverage_status: "detailed-summary"
source_url: "https://support.google.com/android-developer-console/answer/16641416"
source_url_account_type: "https://support.google.com/android-developer-console/answer/16641046"
source_url_required_information: "https://support.google.com/android-developer-console/answer/16640818"
source_url_required_documents: "https://support.google.com/android-developer-console/answer/16501669"
source_url_distribution: "https://support.google.com/android-developer-console/answer/16640817"
source_url_limited_distribution: "https://support.google.com/android-developer-console/answer/17131204"
source_url_package_registration: "https://support.google.com/android-developer-console/answer/16640821"
source_url_identity_updates: "https://support.google.com/android-developer-console/answer/16641334"
source_url_add_users: "https://support.google.com/android-developer-console/answer/16642750"
source_url_verification_overview: "https://support.google.com/android-developer-console/answer/16561738"
source_url_get_started: "https://support.google.com/android-developer-console/answer/16604405"
source_url_contact_form: "https://support.google.com/android-developer-console/contact/developer_verification_issue"
source_url_console_terms: "https://developer.android.com/developer-verification/console/terms"
source_url_search_console_associations: "https://support.google.com/webmasters/answer/9419894"
source_url_search_console_add_property: "https://support.google.com/webmasters/answer/34592"
source_url_payments_settings: "https://payments.google.com/gp/w/home/settings"
source_url_adc_entry: "https://get.google.com/adc-early-access"
source_url_phone_format: "https://en.wikipedia.org/wiki/E.164"
source_url_google_terms: "https://policies.google.com/terms"
source_url_dnb_lookup: "https://my.dnb.com/lookup"
source_url_dnb_expedited: "https://www.dnb.com/en-us/marketing/dunsfile.html"
effective_date: "ADC ToS effective 2025-11-11, last updated 2026-03-27 UTC; 20-device and 50-device texts kept separate; no 2027-01-27"
---

# Android Developer Console 账号、身份核验与服务条款

> **导入说明（Google batch 7）。** 正文来自已经分开的 2026-10-24 Google Play 知识库快照（`android.developer-console-accounts`，核对日 2026-10-24）的改写摘要，不是官方页面的逐字副本。英文官方页面是效力来源。`kb_checked_at` 是快照源文件记录的核对日；本次导入没有重新打开线上官方页面。文中“本知识库”“本库”“本地专题”等说法描述的是该快照库的覆盖范围，不是本仓库已经导入的页面。指向本仓库没有收录的专题、链接图、台账或 CSV 的相对链接改为文字提及。指向 Google batch 1–6 或本批十二个专题的相对链接改为本仓库文件。核对日 2026-10-24。两种语言文件引用的 Android Developer Console 帮助 URL 都不带语言参数。快照没有记录已核对的中文官方 ADC 帮助页，也没有记录这些帮助文章的 `hl=zh-CN` 抓取失败。本仓库中文正文是编辑改写。中文本地化的有限分发指南（`hl=zh-cn`，2026-09-30 更新）、指南总览和验证 FAQ 仍写 20 台设备。2026-10-23 更新的英文专用有限分发指南写 50 台。快照中的公开来源没有解释这一冲突。两个数字保持分开，也不能确认某个账号的实际上限。ADC 服务条款自 2025-11-11 起生效，最后更新于 2026-03-27 UTC。两个日期都已过去。本页没有记录 2027-01-27。早期访问入口当时无法公开读取。ADC 帮助是 operational。ADC 条款是使用 ADC 的合同。ADC 用于 Google Play 以外的分发。它不替代 Play Console 要求、Play 开发者分发协议、Play Console 条款或开发者计划政策。Android 开发者验证仍是快照中的独立专题，未导入本仓库。

**核对日期：2026-10-24。** 本专题整理 Android Developer Console（ADC）的建号、身份验证、包名登记和账号条款。它是 Android 开发者验证体系的一部分，和 Google Play 开发者账号及 Play 政策相关，但不是同一套制度。

## 适用边界：Play Console 与 Android Developer Console

- Android Developer Console 面向**只在 Google Play 之外分发**应用的开发者，用于验证开发者身份和登记包名。
- 已使用或准备使用 Play Console 的开发者，可在 Play Console 完成 Android developer verification 的相关步骤，也包括 Play 之外分发的应用；不应仅因 Play 外分发就重复创建 ADC 账号。
- Android developer verification 核验开发者身份及包名/签名密钥关系；它不审查应用内容、源代码或 Play 政策合规性。Play 上架与分发仍须分别满足[Play Console 要求](../play-console-requirements/play-console-requirements.zh-CN.md)、[开发者计划政策](../developer-program-policy/developer-program-policy.zh-CN.md)和适用合同。
- Android Developer Console 的服务条款（ADC ToS）是使用 ADC 的合同，不是 [Google Play Developer Distribution Agreement](../developer-distribution-agreement/developer-distribution-agreement.zh-CN.md)，也不是 Play Console 服务条款。

## 建号前先选两件不同的事

| 选择维度 | 选项 | 适用与后果 |
| --- | --- | --- |
| **身份/所有权类型** | Personal / Organization | 决定法律所有人、付款资料和核验材料。创建后不可把个人账号直接改成组织账号，反之亦然。 |
| **分发计划** | Limited / Full | 决定可分发设备范围与注册费。计划创建后不能直接转换；要换计划，官方要求创建新账号并转移包名。 |

两组选择互相关联，但不是同一字段：Limited 仅提供给 Personal；Full 可按个人或组织路径创建。

| 计划 | 官方描述 | 核验及限制 |
| --- | --- | --- |
| **Limited distribution** | 免费，最多向 20 台已授权设备分发。 | 需要 Google 账号、两步验证、Google Payments profile 和仅供 Google 联系的邮箱；不要求政府身份证件。只能登记此前未在 Android 出现过的新包名。 |
| **Full distribution** | 一次性 25 美元注册费；不限制安装设备数量。 | 按个人/组织类型完成身份核验；接受的银行卡种类可能因地区不同。不能把预付卡当作默认可用付款方式。 |

Full 计划收费、Limited 的设备上限和可选计划以官方注册流程为准；这不是 Google Play 的 25 美元开发者账号注册费。

**来源口径提示（2026-10-24）：**本专题的 20 台数字忠实记录 Android Developer Console Help 当前页面；但 Android 官方[专用有限分发指南](https://developer.android.com/developer-verification/guides/limited-distribution)于 2026-10-23 更新后称上限为 50 台，而[中文本地化专页](https://developer.android.com/developer-verification/guides/limited-distribution?hl=zh-cn)（2026-09-30 更新）、[指南总览](https://developer.android.com/developer-verification/guides)和[验证 FAQ](https://developer.android.com/developer-verification/guides/faq)也仍保留 20 台。公开资料未解释冲突，因此不可把此处的 Help 原文或专用指南单独当作已确认的实际账户上限；超过 20 台前应核对账户当前页面并取得 Google 支持书面答复。

## 身份资料与建号检查清单

### 付款资料与法定身份

建号时须选择或建立 Google Payments profile。ADC 用其中的法定姓名/组织名称和地址核验现实身份；资料必须准确并保持更新。开发者名称可以不同于法定名称，但在包名转移等部分账号操作中可能向其他 ADC 用户显示。

个人资料可能需要政府身份证件。组织资料一般需要：

1. D-U-N-S 编号；  
2. 有权代表组织的人士所持的政府签发照片证件；  
3. 可信政府或公共机构出具的组织登记文件。文件中的组织名称须与 Dun & Bradstreet（D&B）资料相符。

可接受组织文件取决于地区。提交不受支持的文件是 Google 所列的常见验证失败原因。政府组织若无法提供普通登记材料，可按页面要求使用官方抬头文件；D-U-N-S 例外要先联系支持，不应把政府例外扩大成一般组织豁免。

### D-U-N-S：免费申请、先核对主体、提前准备

- D-U-N-S 是 D&B 分配的九位组织识别码。组织可能已有编号；大型机构也可能有多个不同实体的编号，应先查找并选取与本次账号主体名称、地址相符的编号。
- Google 页面说明向 D&B 申请编号免费，并提醒不要向第三方中介支付所谓必需的高额申请费。
- Google 的“Required information”页面写申请可能最多 **30 天**；“Understanding Android developer verification”页面写最多 **28 天**；D&B 当前公开申请页写通常最长 **30 个工作日**，并另提供收费的 8 个工作日加急服务。三者口径不同；应尽早申请，并以当前地区的 D&B 实际流程为准。收费加急是 D&B 的可选服务，不是 Google 的强制费用。
- D&B 对企业一般经营并不要求持有 D-U-N-S；但 Google 对 ADC 组织账号提出自己的 D-U-N-S 要求。不要把 D&B 的一般说明当作 Google 账号的豁免。
- D&B 不支持的地区及政府实体可在建号前向 Google 支持申请替代核验。政府组织可能要提供官方邮箱域名或关联官网。Google 表示不接受不完整请求，也不会因普通组织未提供 D-U-N-S 而给予豁免或延期。

可查阅 [Google 的组织账号资料要求](https://support.google.com/android-developer-console/answer/16640818)、[D&B 官方服务查询入口](https://service.dnb.com/)、[D-U-N-S 在线查询](https://my.dnb.com/lookup)和 [D&B 免费申请说明](https://www.dnb.com/duns/get-a-duns.html)。查询入口分别显示浏览器兼容性提示或要求 JavaScript；申请页可读，未启动或提交申请。D&B 还单独提供[加急服务](https://www.dnb.com/en-us/marketing/dunsfile.html)，当前页面列价 US$229；这是可选的供应商服务，不是 Google 要求。

### 组织官网必须做 Search Console 关联

所有新建组织账号都要验证组织网站所有权：先在 [Google Search Console](https://support.google.com/webmasters/answer/34592) 添加并验证网站，再从 ADC 身份页发起关联请求。用同一个 Google 账号拥有网站并创建 ADC 时，关联可自动批准；否则 Search Console 已登记的站点所有者要批准请求。拒绝、输错网址或使用社交媒体个人主页都会导致失败；更正官网 URL 后可重新申请。

这是官网归属核验，不等于商店详情、Play 开发者资料或应用内容审核。Search Console 的“所有权验证”会授予该账号很高的站点权限；先确认网站、Google 账号和令牌管理责任人，再批准关联。

### 联系方式与隐私

ADC 的验证联系邮箱和电话供 Google 联系开发者，不展示给 Android 用户。邮箱和电话都需通过一次性验证码核验；电话采用 [E.164 国际格式](https://en.wikipedia.org/wiki/E.164)，可选短信或语音，修改电话后须重新核验。短信/电话费用可能由运营商计费；短信收不到时可改用语音。

组织团队建议使用组织域名邮箱和可持续管理的团队收件箱，保持联系人可以接收验证码及账号通知。不要把 ADC 私密联系资料与 Play 商店公开开发者联系方式或每个应用的客服邮箱混为一谈；后两者在 Play Console 中另行维护。

### 付款资料共享与账号权限

个人付款资料不能在团队成员间共享，且身份资料页称个人账号资料绑定最初创建该 ADC 账号的人。组织付款资料可由组织管理员共享；同一组织的多个开发者账号可考虑复用资料，但每位 ADC 账号所有者都必须先被加为付款资料管理员并接受邀请，之后才可在 ADC 选择该资料。操作入口是 [Google Payments Center 设置](https://payments.google.com/gp/w/home/settings)，需要登录。付款资料管理员可能可以使用资料中的付款信息，因此应先核对所选资料与权限。

ADC 的“Users”邀请和 Payments profile 的管理员授权是两套权限。新增或移除 ADC 用户不会自动授予/撤销 Payments profile 权限，反之亦然。

### 更改账号资料

- 法定姓名或地址通过关联的 Payments profile 更新；只有该付款资料管理员可修改。组织付款资料可有多名管理员。
- 国家/地区变化时，Google 要求建立新的 ADC 账号并转移已登记包名。
- Personal/Organization 类型创建后固定。需改变时要新建相应账号并重新登记包名。
- 联系邮箱或电话在 ADC Identity > Contact details 更新；更新后的邮箱/电话须重新通过六位验证码。
- 未保持身份和联系信息有效，可能导致 ADC 身份受限，并阻止应用在经过认证的 Android 设备上分发。

## 包名登记与 Limited 计划实操

身份核验完成前，ADC 会阻止包名登记。新包名提交签名证书的公开 SHA-256 指纹；已有包名则按 Android 已知安装量决定哪些签名密钥可直接登记。若密钥不符合资格，开发者可向 Google 说明使用理由并请求，但可能被拒。

证明现有包名的密钥控制权时，按官方引导把 ADC 生成的片段放到 APK 的 assets/adi-registration.properties 文件中，再用对应私钥签名并上传 APK。若第三方商店会重签应用，应从该商店取得最终签名的 APK 作为证明。**只提交公钥证书指纹；不要把私钥或密钥库密码交给 Google 支持、D&B 或不可信第三方。**

Limited 计划额外要求：

- 此帮助页称一个账号最多有 20 台当前授权设备；未经授权的设备不能安装或接收更新。上限冲突见上方来源提示。
- 只能登记此前从未在 Android 出现过的包名；已存在的包名会被拒绝。
- 邀请链接七天后过期，接收人须在实体设备上生成验证码并确认认识、信任开发者。
- 删除设备后，该设备无法安装或更新账号的已登记应用；若要恢复，必须重新授权。

参见 [注册 Android 包名](https://support.google.com/android-developer-console/answer/16640821)和[获取应用 SHA-256 证书指纹](https://support.google.com/android-developer-console/answer/16641489)。包名资格、现有应用密钥和多商店重签都可能涉及特殊步骤；上架/迁移前以账号内 Console 的包名状态为准。

## Android Developer Console 服务条款

[Android Developer Console Terms of Service](https://developer.android.com/developer-verification/console/terms)自 **2025-11-11** 起生效，页面标注最后更新于 **2026-03-27 UTC**。使用 ADC 的个人用户必须接受；条款说明 ADC 用于开发者身份核验及应用包登记，未完成验证/登记可能导致应用无法安装。Limited 账号可能适用额外或不同条款，应以创建该账号时展示的版本为准。

条款要求仅按 ADC 预期功能使用；禁止非法或滥用行为、干扰或逆向工程服务，以及违反其他 Google 产品条款的使用。Google 可更改或停止 ADC；现有用户对普通条款变更通常至少提前 30 天获通知，但新功能或法律要求变更可立即生效。继续使用视为接受修改；违反条款或分发恶意/有害应用可能导致访问被终止。条款指定英文版本控制、加州法律及 Santa Clara 郡法院管辖；美国政府实体有专门例外。

ADC ToS 是账号/平台使用合同，不决定某个应用是否符合 Google Play 的内容政策。相关原文链接包括 [Google 隐私权政策](https://policies.google.com/privacy)、[Google 服务条款](https://policies.google.com/terms)、[Android Developers 内容许可](https://developer.android.com/license)和条款中的 [ADC 入口](https://get.google.com/adc-early-access)；ADC 入口本次无法公开读取。不要把 Android Developers 内容许可推定为 Google Play Help 或合同全文可自由复制的授权。

## 地区材料抽查

下表是 Android Developer Console Help 的五个英文地区视图抽查，并非全球地区清单。各账号最终适用的文件以付款资料地区与 Console 动态任务为准。

| 地区 | 组织/代表材料（摘要） | 个人材料及特殊点 |
| --- | --- | --- |
| [澳大利亚](https://support.google.com/android-developer-console/answer/16501669?co=GENIE.CountryCode%3DAU&hl=en) | 注册/成立证件；部分单位信托可用成立契据；也可提供 ABN。政府机构在缺少商业文件时可交官方抬头材料。 | 澳大利亚政府照片证件，加姓名地址一致且近 90 天的地址证明；要求也适用于 Norfolk Island。 |
| [美国](https://support.google.com/android-developer-console/answer/16501669?co=GENIE.CountryCode%3DUS&hl=en) | IRS 组织文件、州注册证、SEC 申报或商业信用报告等；代表提交政府照片证件。 | 美国政府照片证件；地址证明姓名和地址精确匹配，且近 90 天签发。 |
| [印度](https://support.google.com/android-developer-console/answer/16501669?co=GENIE.CountryCode%3DIN&hl=en) | 可接受公司章程、注册、GST、合伙/信托/社团等文件及 CIN；代表提交政府照片证件。 | 印度护照、驾照、选民证或 PAN，加地址证明。此视图未写统一 90 天有效期，不从其他地区规则推断。 |
| [法国](https://support.google.com/android-developer-console/answer/16501669?co=GENIE.CountryCode%3DFR&hl=en) | 注册证明、商业登记摘录或 VAT 文件；原文意外写成 “advertiser verification”，与 Android developer verification 标题不一致，须以 Console 当前任务确认。 | 个人证件须由 EEA 国家或瑞士签发；要求也适用于法属圭亚那、瓜德罗普、马提尼克、马约特和留尼汪。页面未明确列出 90 天地址时限。 |
| [韩国](https://support.google.com/android-developer-console/answer/16501669?co=GENIE.CountryCode%3DKR&hl=en) | 公司注册证明；政府部门可用含全名、地址和日期的官方信函。 | 个人及组织代表需通过移动运营商核验；个人地址证明与付款资料精确匹配且近 90 天签发。 |

Play Console 的[身份文件地区页](https://support.google.com/googleplay/android-developer/answer/15633622)是另一项核验工作流。虽然有相似文件规则，不要把某个 ADC 地区页缺少的日期要求从 Play 页面自动补入，也不要用一个工作流的政府例外推导另一项例外。

## 子链接与覆盖状态

本专题已分别记录身份页、账号类型、所需信息、地区文件、Full/Limited 计划、包名注册、身份证明指纹、账号资料更新、用户权限、账号入门、验证 FAQ、公开支持表单及 ADC ToS。Help Center 侧栏与正文链接分开审计。组织网站验证的 Search Console 后代重点核对了[Associations](https://support.google.com/webmasters/answer/9419894)、[添加站点](https://support.google.com/webmasters/answer/34592)、[网站所有权验证](https://support.google.com/webmasters/answer/9008080)和[站点所有者与权限](https://support.google.com/webmasters/answer/7687615)。

Search Console 技术方法、帮助侧栏、Google 登录/Console 账号内页面、D&B 交互查询和更深技术示例仍未做无限递归。公开的身份支持表单已读取字段和英语回复限制，**未填写或提交**。各页访问状态和可读范围记录在 来源审计台账（快照：`source-page-audit.csv`，未导入本仓库）及递归链接图（快照：`google-play-policy-link-graph.md`，未导入本仓库）。

## 来源链接

- [验证 Android 开发者身份信息](https://support.google.com/android-developer-console/answer/16641416)
- [创建 Android Developer Console 账号所需信息](https://support.google.com/android-developer-console/answer/16640818)
- [选择账号类型](https://support.google.com/android-developer-console/answer/16641046) · [选择分发计划](https://support.google.com/android-developer-console/answer/16640817) · [Limited distribution](https://support.google.com/android-developer-console/answer/17131204)
- [开始使用 ADC](https://support.google.com/android-developer-console/answer/16604405) · [更新身份资料](https://support.google.com/android-developer-console/answer/16641334) · [添加用户](https://support.google.com/android-developer-console/answer/16642750)
- [Android developer verification FAQ](https://support.google.com/android-developer-console/answer/16561738) · [地区文件页](https://support.google.com/android-developer-console/answer/16501669)
- [ADC Terms of Service](https://developer.android.com/developer-verification/console/terms)
