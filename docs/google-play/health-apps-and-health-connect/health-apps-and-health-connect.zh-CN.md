---
id: google-play.health-apps-and-health-connect
platform: google-play
language: zh-CN
authority: normative
status: current
kb_checked_at: 2026-10-24
review_due: 2027-01-24
regions: [global]
topics: [health, medical, health-connect, medical-device, research, sensitive-data]
snapshot_id: play.health-apps
snapshot_package: "GooglePlay-KnowledgeBase-2026-10-24-review.zip"
coverage_status: "detailed-summary"
source_url: "https://support.google.com/googleplay/android-developer/answer/16679511?hl=en"
source_url_zh: "https://support.google.com/googleplay/android-developer/answer/16679511?hl=zh-CN"
source_url_declaration: "https://support.google.com/googleplay/android-developer/answer/14738291?hl=en"
source_url_declaration_zh: "https://support.google.com/googleplay/android-developer/answer/14738291?hl=zh-Hans"
effective_date: "current-policy; consolidated policy 2026-09-30 already current; Medical Records Play policy still being developed"
---

# 健康应用、健康数据与 Health Connect

> **导入说明（Google batch 5）。** 正文来自已经分开的 2026-10-24 Google Play 知识库快照（`play.health-apps`，核对日 2026-10-24）的改写摘要，不是官方页面的逐字副本。英文官方页面是效力来源。`kb_checked_at` 是快照源文件记录的核对日；本次导入没有重新打开线上官方页面。文中“本知识库”“本库”“本地专题”等说法描述的是该快照库的覆盖范围，不是本仓库已经导入的页面。指向本仓库没有收录的专题、链接图、台账或 CSV 的相对链接改为文字提及。指向 Google batch 1–4 或本批八个专题的相对链接改为本仓库文件。 英文 Health Content and Services 正文已复核。简体中文根路由 `hl=zh-CN` 在快照的浏览器工具中仍不可读。健康应用分类页和 Android Health Permissions FAQ 打开的是英文正文；其中文目标不可用。健康应用声明帮助页的英文和 `hl=zh-Hans` 正文都已打开；中文页提示可能包含不准确的 AI 翻译。若干 Health Connect 界面指南（包括 Matchmaking）打开的是简体中文（`hl=zh-CN`）；快照记录英文 Matchmaking 变体缓存未命中。这些访问限制不是政策变更。本仓库中文正文是快照的编辑改写，除非源文件记录某一中文官方页面确已打开。合并版开发者计划政策的 2026-09-30 已经过去，是未批准物质规则的现行文本。快照没有记录 2027-01-27 的健康政策生效日。Android 医疗记录指南标注更新于 2026-10-19，称相关 API 仍在开发且为实验性，Google Play 对医疗记录访问的政策仍在制定。这项尚未完成的政策不是现行 Play 资格。Android 16 身体传感器迁移是 API 变化，不是新的 Play 生效日。Play 健康政策是 `normative`。Console 声明步骤是操作说明。Health Connect、Matchmaking 和身体传感器迁移是实现说明。本页不是医疗器械、隐私或临床研究方面的法律意见。

**核对日期：2026-10-24。** 本页综合 Google Play 的 Health Content and Services 政策、声明表单说明、健康权限 FAQ 与 Android Health Connect 发布指南。按政策结构改写并梳理主要要求，不是官网逐字镜像，也不替代国家/地区医疗器械、隐私或临床研究法规。

## 先判断哪些应用和数据在范围内

只要应用提供健康相关功能或信息，或者读取健康数据来支持非健康功能，就进入健康政策范围；应用自称“健身”“生活方式”“娱乐”或把采集交给 SDK，都不能据此排除。健康数据及 Health Connect 数据同时属于[个人和敏感用户数据](../user-data/user-data.zh-CN.md)，其数据安全申报、隐私政策、运行时权限、显著披露和肯定同意要求仍然适用。

Google Play 的健康声明分类包括：

| 类别 | 常见功能 |
| --- | --- |
| 健康与健身 | 活动/健身、营养/体重管理、月经周期、睡眠、压力/放松/认知健康 |
| 医疗 | 疾病管理、临床决策支持、疾病预防/公共卫生、急救、医疗服务/管理、心理/行为健康、医学参考/教育、用药/治疗、理疗/康复、生殖/性健康 |
| 医疗器械 | 受相关监管的诊断、治疗建议、临床监测、或与医疗器械硬件协同的软件 |
| 人体受试者研究 | 健康研究、临床试验、患者社群等研究参与功能 |

即使应用不提供健康功能，也必须按声明帮助页提交“没有健康功能”的确认；该要求覆盖 Google Play 上的应用，包括封闭式测试、开放式测试和正式版，以及通过 Play 更新的预装/预授权应用。系统服务和专用应用例外。功能发生变化时，要重新核对申报内容。

## Play Console、账号与商店页要求

- 在 Play Console 的 **政策 → 应用内容 → Health Apps** 完成健康应用声明。说明每类健康功能，以及相关权限或 Health Connect 数据类型如何直接支持具体的用户可见功能；不能只写“应用需要”之类泛化理由。
- 医疗、健康和人体受试者研究应用应使用**组织开发者账号**；组织账号登记通常需要 D‑U‑N‑S 编号。见[开发者账号类型说明](https://support.google.com/googleplay/android-developer/answer/13634885?hl=en)。
- 在 Play Console 指定字段和应用内提供隐私政策链接或文本。网页须有效、公开、无地域封锁且不是 PDF，并解释应用和第三方代码访问、收集、使用、保存、分享、保护与删除健康数据的方式。商店页的隐私政策应与 Health Connect 用户看到的政策一致。
- 不得请求核心功能不需要的健康权限；移除未使用权限。产品功能、商店说明、权限声明、Data safety、隐私政策和应用内披露应相互一致。
- 如健康功能依赖外接设备（例如血糖仪），须在商店说明清楚硬件要求，不能暗示没有设备也可独立工作。若通过摄像头等设备传感器提供功能，应说明兼容设备型号。

## 医疗功能、医疗器械与健康声明

不得提供误导或可能伤害用户的健康/医疗功能。若应用并非受监管的医疗器械，商店说明须包含清楚免责声明：**“不是医疗器械，不会诊断、治疗、治愈或预防任何疾病。”** 应用内也须提醒用户就医疗建议、诊断或治疗咨询医疗专业人员。

受监管的医疗器械应用须在 Health Apps 声明中按医疗器械申报；Google Play 可在商店中标记为医疗器械，并可要求开发者提供监管机构的批准、许可或认证证明。面向欧洲经济区和北爱尔兰、受 EU MDR 2017/745 或 IVDR 2017/746 监管的应用，还须公开：器械名称；制造商身份、注册地址和 SRN；用途说明；警告/注意事项；电子版使用说明 eIFU；UDI‑DI。视情况还可能要提供授权代表、公告机构/证书编号及运行、硬件、安全要求。

若应用声称帮助诊断、监测、改善或治疗疾病，应以容易理解的方式交代用途、声称收益及依据（证据、标准或最佳实践）、目标用户、风险和警告。不要夸大检测准确度或把普通健康建议包装成医疗诊断。

## 政府关联、公共卫生与人体研究

- 代表政府或获认可医疗机构开发/分发的关联健康应用，须通过 Advance Notice 流程提交由相关机构出具的授权证明；该表单只接受列明的特定情形，不能把它当成普通审核加急通道。
- 接触者追踪或健康状态应用，应在 Console 选择“疾病预防和公共卫生”并提交所需的 Advance Notice 材料。
- 人体受试者健康研究须遵守适用法规，取得参与者知情同意；未成年人须取得家长/监护人同意。通常还须由独立 IRB/伦理委员会审查批准，除非适用豁免；Google 要求时须提供批准证明。Health Connect 研究同意应说明研究性质、目的、时长、步骤、风险与收益、保密和第三方共享、联系人及退出方法。通过 Health Connect 获取研究数据可能还要填写专用研究表单。

## Health Connect：适用用例、边界和数据治理

Health Connect 可读取或写入活动、身体测量、周期追踪、营养、睡眠、生命体征、健康/心理状态以及医疗记录等类型。医疗记录可包含病史、诊断、治疗、药物和实验室结果，敏感级别尤其高。

Play 认可的用例包括健身/健康、奖励、健身教练、企业健康、医疗护理、健康研究和游戏。访问必须服务于真实、明确、用户可见的健康功能；获批用途不能扩展成未披露的二次用途。健康整合游戏的主要目的仍须是游戏，不能变成未受监管的医疗工具。

**禁止的用法**包括：

- 将健康/健身数据出售或转给广告平台、数据经纪商、信息转售商；用其投放个性化/兴趣广告；用于信用、保险资格、就业适合度或借贷判断。
- 未获明确、知情同意就把数据分享给第三方，或公开/社交发布敏感数据。
- 将数据用于未在应用界面呈现的功能、推荐或次要用途；超出获准的健康用途。
- 在应用无头运行时读取；将其用于仅面向儿童的应用/服务；或用于设备/平台互不兼容的数据同步。
- 在失败可能导致死亡、人身伤害、环境或财产损害的高风险/生命关键环境中使用，例如生命维持、航空管制等。

开发者须提供用户帮助说明，解释怎样查看、管理和删除应用数据，以及账号停用/删除后的处理；使用传输和静态加密、强访问控制、安全开发与漏洞管理保护数据。须自行判断 HIPAA、GDPR、医疗器械规则和本地健康隐私法律是否适用；可能还需与合作方签署 BAA/DPA，并在 Google 要求时提交遵循证明。Google 不保证 Health Connect 数据适合医疗、研究或诊断用途。

## 权限申请与技术实现的最佳实践

健康数据相关权限范围不限于 Health Connect：Play 的类别说明列举了位置、活动识别、蓝牙、身体传感器、相机、日历、短信、录音等可能收集或推断健康数据的权限；官方清单明示为**非穷尽**。无论数据来自 Health Connect、身体传感器还是其他权限，遵循同一原则：

官方 FAQ 当前列出的示例权限名包括：`ACCESS_BACKGROUND_LOCATION`、`ACCESS_COARSE_LOCATION`、`ACCESS_FINE_LOCATION`、`ACTIVITY_RECOGNITION`、`BLUETOOTH_ADVERTISE`、`BLUETOOTH_CONNECT`、`BLUETOOTH_SCAN`、`BODY_SENSORS`、`BODY_SENSORS_BACKGROUND`、`CAMERA`、`READ_CALENDAR`、`READ_SMS`、`RECORD_AUDIO`、`SEND_SMS`、`WRITE_CALENDAR`。该列举不是穷尽清单；具体应用仍须按代码、SDK、target API 与当前 Android/Play 规则核对权限。若权限可能接触健康相关敏感数据，须明确数据类型和用途，并先完成应用内显著披露与肯定同意。Android 16 身体传感器迁移见[目标 API 专题](../target-api/target-api-level.zh-CN.md)及[敏感权限专题](../sensitive-permissions/sensitive-permissions.zh-CN.md)。

1. 先把每个权限/数据类型映射到已实现、用户可见的功能、用户收益和商店描述；只请求最小必要数据，并在实际情境中说明用途、接收方和二次使用。更多系统 Picker、API 替代方案和披露示例见[Android 隐私清单](../android-privacy-checklist/android-privacy-checklist.zh-CN.md)。
2. 请求权限前给出符合[用户数据政策](../user-data/user-data.zh-CN.md)的显著披露和肯定同意；按 Android 运行时权限流程请求。用户拒绝或撤回后，不得继续访问未授权数据。
3. Play Console 为每个数据类型提供具体理由。健康权限 FAQ 的示例包括 `READ_MENSTRUAL_CYCLE_PHASE`、`READ_ALCOHOL_CONSUMPTION`、`READ_BLOOD_PRESSURE`、`READ_SKIN_TEMPERATURE` 和 `READ_SYMPTOM_COUGH`；症状权限按症状细分，不存在通用的 `ALL_SYMPTOMS` 权限。生殖健康、酒精/物质使用、临床生命体征、用户报告症状等高敏感字段会受到更严格审查；无功能需要不得申请。
4. 多用途或支持多个数据源的应用，尤其 AI agent，可参考 [Matchmaking API](https://developer.android.com/health-and-fitness/health-connect/ui/matchmaking?hl=zh-CN) 检查哪些应用/设备能够提供自己需要的数据源，减少一次性申请过多数据类型。
5. 确保 Data safety、隐私政策、应用内说明、Health Connect 权限声明和实际 SDK/服务端数据流一致；为数据提供用户管理/删除路径。若写入 UDI（Unique Device Identifier）来源元数据，必须保证准确、真实；若读取 UDI，开发者须自行对照相关监管数据库验证，并判断数据是否适合其临床功能。
6. Android 16 / API 36 起，身体传感器的相应访问应检查迁移到细粒度 `android.permission.health.*` 权限的要求。不要把 API 升级、Health Connect 运行时授权和 Play Console 数据访问审批混为一谈。

### Matchmaking API：缩小数据源请求范围，但不替代授权

Play 的健康权限 FAQ 特别提醒多用途应用（尤其 AI agent）先了解设备上的数据源，再决定是否显示权限请求。Android 的 [Matchmaking API 指南](https://developer.android.com/health-and-fitness/health-connect/ui/matchmaking?hl=zh-CN)把它实现为 Health Connect 提供的系统流程：以 `MatchmakingRequest.recordTypes` 指定类型，并可包含或排除数据来源；两种来源过滤不能同时设置。若类型集合为空，流程会针对调用应用已获读权限的全部类型。`checkIfMatchmakingIsPossible()` 可先检查是否有匹配来源；有来源时再启动系统 UI，由用户选择可写入相应记录的应用或设备。API 仍标注为实验性，应先检查设备的 `FEATURE_MATCHMAKING` 状态；来源匹配不是 Play 对数据类型的审批，也不代替用户授权。

**顺序边界待澄清：** Play FAQ 的简述说在权限提示前使用 Matchmaking API；Android 指南则明确说待匹配的记录类型必须已获调用应用读取授权。API reference 进一步说明，匹配对象是能够写入这些“调用应用可读取”记录的其他应用/设备，并可在系统界面授予来源端缺失的写入权限。因此不能把该 API 理解为在首次读取授权前探测任意健康类型，或绕过 Play Console 声明、审核和用户同意。实践上，只把已获授权的最小类型传给该流程；若审核结论依赖“首次读授权”和匹配的先后顺序，应向 Play 支持确认当前账号实际表单要求。Play FAQ 的概括措辞和实现指南之间的顺序并未被官方页面完全解释。

同一 Android 界面指南的[新用户引导](https://developer.android.com/health-and-fitness/health-connect/ui/onboard-users?hl=zh-CN)明确指出，Matchmaking API 不支持“授予权限后自动触发”的 onboarding 触发器；如需额外教程或同意步骤，可配置单独的导出 Activity，Android 14 前后使用相应 manifest 声明。Health Connect 可直接从自身应用发起连接，所以该 Activity 可能重复启动（例如用户撤权后重新连接），实现应可重复进入。

[推介 Health Connect](https://developer.android.com/health-and-fitness/health-connect/ui/promote?hl=zh-CN)建议用用户收益解释为何接入，而不是只介绍 Health Connect；按钮用“设置”“开始”或“选择要分享的数据”等清楚动作，避免含糊的“连接到 Health Connect”。请求新数据类型时只展示新权限，并在锻炼、睡眠等相关情境说明用途。[权限和数据访问指南](https://developer.android.com/health-and-fitness/health-connect/ui/permissions?hl=zh-CN)另建议提供同步开关和直接管理权限入口；关闭同步后停止读写，连续两次取消后引导用户到系统设置重新启用。若调用 `revokeAllPermissions()`，要说明系统变更可能要重启应用后才显示。数据来源说明见[数据展示和来源归因](https://developer.android.com/health-and-fitness/health-connect/ui/data?hl=zh-CN)：至少展示来源应用名称（可同时显示图标），在活动详情/报告/分析页提供权限页面入口；长时间同步时显示进度并使用低优先级通知。这些是 Android UX/实现指南，不能取代 Play 对用途、最小权限、披露、同意和申报的要求。

Health Connect 数据类型目录按活动、身体测量、周期追踪、营养、睡眠、生命体征和健康状态等类别列出数据结构及 Manifest 权限。[数据类型指南](https://developer.android.com/health-and-fitness/health-connect/data-types)还要求开发者在发布前于 Play Console 声明数据用途和计划访问的具体类型；权限须先在 Manifest 中声明。后台读取与读取首次授权前 30 天之外的数据，分别需要额外权限 `READ_HEALTH_DATA_IN_BACKGROUND` 和 `READ_HEALTH_DATA_HISTORY`。指南提醒，Health Connect 数据类型访问需要特别审批，未完成相应声明/审批时用户可能遇到访问错误。该页权限表标注适用于 Health Connect SDK 1.0.0-alpha10 及更高版本；完整字段和逐类型 API 子页尚未逐条整理。Health Connect UI 指南强调流程一致、透明说明 Health Connect 与应用的关系，并帮助用户从应用进入数据与权限管理。开发者发布流程为：核对政策 → 填 Data safety → 完成 Health Apps 声明 → 逐项说明所需数据类型。新增/不再使用数据类型时更新声明；每次提交新版本，声明也可能再次接受审核。实际可用数据类型、SDK 和申报结果须以当前技术文档与 Play Console 为准。

**医疗记录发布状态需单独核实：** Android 的 [Medical Records 技术文档](https://developer.android.com/health-and-fitness/health-connect/medical-records)于 2026-10-19 更新，明确指出 API 仍在开发中并标记为实验性，Google Play 对医疗记录访问的政策仍在制定，应用上架前可能需要额外条件。2026-10-23 复核时，读写指南仍说明 Medical Records API 可用版本为 Health Connect Jetpack 1.1.0-beta02 或更高；功能可用性指南展示的依赖示例则是 1.2.0-alpha06。请按目标 SDK/设备和当前正式文档核验版本，不能把 API 可用、用户授权或普通 Health Connect 声明获批当作医疗记录 Play 发布许可。

### Medical Records 读写指南、FHIR 数据与直接子链（2026-10-23 复核）

以下是 Android 实施文档的核对结果，**技术能力不等于 Play 政策批准**。Health Connect 的 Play 发布流程仍以健康政策、Data safety、Health Apps 声明及实际审核为准；医疗记录这一专门政策状态仍未定。

| 子页面 | 页面内容与实施要点 | 与 Play 政策的关系 |
| --- | --- | --- |
| [Write medical data](https://developer.android.com/health-and-fitness/health-connect/medical-records/write-data) | 写入前检查 `FEATURE_PERSONAL_HEALTH_RECORD`；申请 `android.permission.health.WRITE_MEDICAL_DATA`；Manifest 与 Play Console 都要声明，并在每次使用前重查授权，因为用户可随时撤回。先建用户可识别的 `MedicalDataSource`，再以 FHIR JSON 用 `upsertMedicalResources` 写入/更新。源内须避免同类型同 ID 冲突；删除数据源会连带删除其记录。 | 说明技术权限和数据模型，不表示 Play 医疗记录访问政策已完成或该用途已获批。只可删除本应用写入的记录。 |
| [Read medical data](https://developer.android.com/health-and-fitness/health-connect/medical-records/read-data) | 列出 12 类细粒度读取权限：过敏/不耐受、病症、实验室结果、药物、个人信息、医务人员信息、妊娠、医疗程序、社会史、疫苗、就诊、生命体征。读取可能包含其他应用写入的记录；须按类型过滤、分页、遵守限流，并可按数据源包名或 ID 查询。 | 只请求功能确实需要的具体类别；用户授予运行时权限仍不能替代 Play Console 申报、显著披露、Data safety、隐私政策和用途限制。 |
| [Medical Records data format](https://developer.android.com/health-and-fitness/health-connect/medical-records/data-format) | 当前列出 FHIR R4 4.0.1 与 R4B 4.3.0；定义 12 类 Medical Resource 与 FHIR resource/权限映射。Health Connect 目前面向单个个人的数据，所有写入资源应属于同一人；FHIR JSON、受支持的资源类型、ID 唯一性和字段结构会被验证；文档标注部分验证“Coming soon”，建议提前兼容。数据合并或转换时注意来源追溯（如 `meta.source`），并向用户说明写入更完整的未转换数据集。 | 这是格式互操作要求，不是 Google Play 的可上架资格清单。HL7 FHIR、IPS 和示例资源是外部技术标准/参考，不是 Play 政策。 |
| [Check for feature availability](https://developer.android.com/health-and-fitness/health-connect/features/availability) | 用 `getFeatureStatus()` 检查 `FEATURE_PERSONAL_HEALTH_RECORD`；不支持时须有合理降级/更新提示。页面说明 Android 13 及以下的 APK 模式无法使用仅适用于 Android 14+ 系统模块的功能。 | 设备支持情况不能证明用户资格、地区资格或 Play 审核通过。 |
| [Plan to avoid rate limiting](https://developer.android.com/health-and-fitness/health-connect/rate-limiting) | Health Connect 对读、变更日志、写入/更新/删除设置前台/后台请求与内存限制；后台限流更严格。最佳实践包括减少后台调用、从失败位置重试、避免整批清空重写，并优先用变更日志同步而不是反复全量读取。 | 这是平台稳定性/隐私实现指导。需注意 Medical Records 总览同时说明医疗记录的 changelog API 尚未开发；因此不要假定当前医疗记录读写已支持通用 changelog 流程。 |

#### FHIR 与 API 参考的继续链接

- 写入指南指向 [MedicalDataSource](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/MedicalDataSource) 与 [MedicalResource](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/MedicalResource) Kotlin API 参考。浏览器尝试均因正文超过 4 MiB 而失败；本专题仅采用可读的写入指南正文解释其数据模型，不推断 API 参考中的额外成员。
- 读写指南的 `getGrantedPermissions` 与 `createRequestPermissionResultContract` 链接指向 [PermissionController API 参考](https://developer.android.com/reference/kotlin/androidx/health/connect/client/PermissionController)，同样因超过 4 MiB 无法读取。
- [FHIR R4](https://hl7.org/fhir/R4/) 与 [FHIR R4B](https://hl7.org/fhir/R4B/)目录和 [FHIR Patient 示例](https://hl7.org/fhir/R4/patient-examples.html)已打开；[FHIR R4 HTTP 交互](https://hl7.org/fhir/R4/http.html)说明标准 REST 交互、安全和版本机制。Medical Records 格式页链接的 [International Patient Summary CI build](https://build.fhir.org/ig/HL7/fhir-ips/)会持续变化，并明确不是授权发布版本；不据此宣称 Health Connect 或 Google Play 已认可其临床适用性。FHIR 全标准条目树很大，本专题只汇总 Medical Records 直接采用的版本、类别、验证和来源追溯要点。
- [Create deep links](https://developer.android.com/training/app-links/create-deeplinks)是写入指南中 FHIR Base URI 示例所引的 Android 导航技术参考：它说明 custom scheme、web link 与 verified App Links 的差异。其用途只是解释 URI/应用链接实现，不增加 Play 健康政策要求。

| 目标页 | 访问与子链状态 |
| --- | --- |
| [Medical Records overview](https://developer.android.com/health-and-fitness/health-connect/medical-records) | 正文及主要正文链接已复核；Android 标注 2026-10-19 更新。写/读、FHIR 数据格式、功能可用性及关联关键指南已打开；媒体、导航/页脚和 Android Health Connect 的全部技术后代未穷尽。 |
| [Write medical data](https://developer.android.com/health-and-fitness/health-connect/medical-records/write-data) | 全文已读，Android 标注 2026-10-21 更新；MedicalDataSource/MedicalResource/PermissionController API 参考因超过 4 MiB 无法获取；FHIR 版本、类别、示例数据与 deep link 子页已打开。 |
| [Read medical data](https://developer.android.com/health-and-fitness/health-connect/medical-records/read-data) | 全文已读，Android 标注 2026-10-21 更新；MedicalResource/MedicalDataSource/PermissionController API 参考受 4 MiB 限制；限流指南已打开，完整 Android API 后代未穷尽。 |
| [Medical Records data format](https://developer.android.com/health-and-fitness/health-connect/medical-records/data-format) | 全文已读，Android 标注 2026-09-10 更新；R4/R4B、IPS CI build、FHIR Patient 示例和相关标准链接已审阅；FHIR 资源全集及每个标准引用未逐个穷尽。 |
| [Feature Availability API](https://developer.android.com/health-and-fitness/health-connect/features/availability) | 全文已读，Android 标注 2026-10-21 更新；医疗记录功能标志及降级边界已整理；其它 Health Connect 功能分支不属于本次医疗记录子树。 |
| [Health Connect rate limiting](https://developer.android.com/health-and-fitness/health-connect/rate-limiting) | 全文已读，Android 标注 2026-01-19 更新；通用限流实践与 Medical Records 尚无 changelog API 的限制已交叉分析。 |
| [MedicalDataSource](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/MedicalDataSource)、[MedicalResource](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/MedicalResource)、[PermissionController](https://developer.android.com/reference/kotlin/androidx/health/connect/client/PermissionController) API references | 已逐项尝试；浏览工具返回正文大于 4 MiB，状态记录为无法获取，未用搜索摘要替代正文。 |

本轮覆盖的是 Medical Records 相关政策与实现分支，不是整个 Android Health Connect 网站的闭包。官方页面链接数量随导航、API reference 与外部 FHIR 标准而大幅扩张；未打开/未穷尽的后代继续在逐 URL 台账中标记为部分或未知。

## 商品、药品和错误健康信息

- 不允许帮助用户在没有处方的情况下销售/购买处方药。
- **核心规则：**无论销售者声称产品在当地是否合法，都不允许应用推广或销售未经批准的物质。此规则在现行英文 [Health Content and Services](https://support.google.com/googleplay/android-developer/answer/16679511?hl=en) 正文和标注 2026-09-30 生效的合并版[开发者计划政策](https://support.google.com/googleplay/android-developer/answer/18258653?hl=en)“Unapproved Substances”部分均有体现。中文内容为对应摘要；本轮中文帮助页直达目标仍无法由浏览器工具读取。
- **常见违规示例（非穷尽）：**违禁药品/补充剂目录中的任何商品；含麻黄的产品；用于减重/体重控制的 hCG，或与合成代谢类固醇一起推广的 hCG；含活性药物成分或危险成分的草本/膳食补充剂；虚假或误导性地宣称产品等同处方药/受控物质；未经政府批准却暗示可安全、有效预防/治疗疾病的产品；曾受政府或监管机构措施/警告的产品；名称容易与未批准药品、补充剂或受控物质混淆的产品。
- [违禁药品和补充剂目录](https://support.google.com/googleplay/android-developer/answer/9217430?hl=en)是动态示例索引，不是政策全文或获准商品白名单。2026-10-24 从现行 Health Content and Services 正文链接 ID 20 打开该索引；同日也从合并版政策正文重开。索引完整正文为 540 行，分四组：未批准药品/补充剂、减重、麻黄、合成代谢类固醇。页面把这些名称列为示例，目录动态且非穷尽；不把名称表复制成稳定政策或白名单，发布前应核对现行目录及适用法律。
- **筛查要点：**逐项核对商品成分、名称/别名、商品页与推广文案、健康疗效声明和监管警告；检查应用是否推广、销售或帮助促成相关商品交易。对名单外商品也不能因未列入示例清单就推定获准；当地合法性主张不构成 Play 豁免。处方药无处方交易是相邻但独立的规则。
- Google 的健康政策建议参考 [LegitScript](https://www.legitscript.com/)了解其监测内容；该站是第三方信息来源，不是 Google Play 政策、商品白名单或审核批准证明。
- 旧的独立 [Unapproved Substances 政策章节目标](https://play.google.com/about/restricted-content/unapproved-substances/)仍无法通过本轮浏览器工具打开：2026-10-24 从可读目录点击其唯一政策正文链接（目标 ID 3）仍返回 Cache miss；此前 2026-10-23 直开为 Internal Error。上面的规则和示例依据可访问的现行 Health Help 与合并版政策；不把这些内容宣称为该目标页的抓取，也不推断 URL 重定向或页面等价；该目标正文及其后代仍未知。
- 不允许与既有医学共识矛盾或可能伤害用户的误导性健康主张，例如声称疫苗会改变 DNA、倡导有害未批准疗法或转换治疗。
- 受监管的临床服务交易不应使用 Google Play Billing；付款边界见[付款政策 FAQ](https://support.google.com/googleplay/android-developer/answer/10281818?hl=en)及[付款、计费与订阅专题](../payments/payments-and-subscriptions.zh-CN.md)。这不豁免服务本身的健康、隐私或当地法律要求。

## 上线前核对清单

- [ ] 完成 Health Apps 声明；若无健康功能也提交“无健康功能”。
- [ ] 核对组织账号、健康功能分类、医疗器械监管身份及所需凭证。
- [ ] 清点 Manifest、SDK、Health Connect 类型、传感器和推断数据；每项关联到具体功能与用户收益。
- [ ] 删除不必要权限；验证 Android 16 健康权限迁移和最小数据类型范围。
- [ ] 将隐私政策、Data safety、商店页、显著披露、同意、保留/删除和安全措施互相对齐。
- [ ] 核查广告/数据共享/二次用途、儿童定位、生命关键用途、研究伦理和医疗声明。
- [ ] 检查所售药品/补充剂、健康主张、处方药交易及临床服务计费路径。
- [ ] 若使用政府/医疗机构背书、公共卫生、医疗设备或研究功能，准备专门的授权、监管或伦理文件。

## 直接子链接覆盖记录

| 官方目标页 | 目标页内容与本页关系 | 状态 |
| --- | --- | --- |
| [Health Content and Services](https://support.google.com/googleplay/android-developer/answer/16679511?hl=en) | 健康/医疗、Health Connect、处方药、未批准物质和错误健康信息的根政策 | 英文正文及 Unapproved Substances 部分于 2026-10-24 复核；正文链接 ID 20 直达下方违禁商品目录；简体中文直达页仍不可读取 |
| [开发者计划政策合并版](https://support.google.com/googleplay/android-developer/answer/18258653?hl=en) | 同一合并政策中的 Health Content and Services / Unapproved Substances 正文；交叉核验现行规则与示例 | 2026-10-24 重新核对相关章节；仍直接链接违禁商品目录和 LegitScript。不可访问的旧 Play-about 页面未被当作此页的重定向目标 |
| [Health apps declaration form](https://support.google.com/googleplay/android-developer/answer/14738291?hl=en) | 所有应用声明义务、类别、医疗器械额外信息和提交流程 | 中英文帮助页已打开并整理；Play Console 实际表单需账号登录 |
| [Health app categories and additional information](https://support.google.com/googleplay/android-developer/answer/13996367?hl=en) | 健康应用分类、人体研究、权限范围和用户披露最佳实践 | 英文正文已打开并整理；中文目标暂不可读取 |
| [Android Health Permissions: Guidance and FAQs](https://support.google.com/googleplay/android-developer/answer/12991134?hl=en) | Health Connect/身体传感器用例、禁用用途、逐权限理由和高敏感字段审查 | 英文正文已打开并整理；中文目标暂不可读取 |
| [Permissions and APIs that Access Sensitive Information](https://support.google.com/googleplay/android-developer/answer/16558241?hl=en) | Health Connect 许可用例、限用、安全、禁止项 | 已整理在[敏感权限专题](../sensitive-permissions/sensitive-permissions.zh-CN.md)，本页交叉引用 |
| [Publish your health app on Google Play](https://developer.android.com/health-and-fitness/health-connect/publish) | 发布流程依次核对 Play 政策、Data safety 与 Health Apps 声明；新应用和现有应用新增/更换健康数据类型时都要完成相应申报。逐项说明用户可见健康功能及最小数据类型；无健康功能也须勾选确认；商店隐私政策须与 Health Connect 内展示的版本一致。 | 正文于 2026-10-22 打开，Android 标注 2026-03-10 更新。直接政策/申报链接已列出；技术导航、示例与 API 孙链接未全部扩展。2025-01-22 旧申请表截止日期只作为历史记录。 |
| [Health Connect overview](https://developer.android.com/health-and-fitness/health-connect) | Health Connect 的定位、兼容性和开发者入口 | 已打开并作入口级摘要；API、样例、视频和发布后代未全部展开 |
| [Health Connect data types](https://developer.android.com/health-and-fitness/health-connect/data-types) | 七类健康/健身数据、逐类型 Manifest 权限、Play Console 逐类型访问声明，以及后台/历史读取的额外权限 | 通过 Health Connect 概览页的官方链接打开规范地址并核对正文；记录 SDK 1.0.0-alpha10+ 表格范围及未申报时可能出现的访问错误。完整字段表未逐条复录，各类型 API 后代仍未穷尽 |
| [Get started with Health Connect](https://developer.android.com/health-and-fitness/health-connect/get-started) | 按 Android 版本安装/接入 Health Connect，检测功能可用性，并要求 Manifest 权限与 Play Console 申报匹配 | 正文关键段落已打开；版本和 SDK 依赖会变化，当前实现参数须回查官方版本页；示例及技术后代部分未审 |
| [Medical Records](https://developer.android.com/health-and-fitness/health-connect/medical-records) | FHIR 医疗记录读写、细粒度授权和 Health Connect 浏览界面；API 实验性，Play 医疗记录访问政策仍在制定 | 正文于 2026-10-23 复核，Android 标注更新至 2026-10-19；Write/Read、FHIR data format、feature availability 和 rate-limiting 子页已打开；API reference 因超过 4 MiB 受限，详见下文 |
| [Health Connect UI guidelines](https://developer.android.com/health-and-fitness/health-connect/ui/guidelines) | 一致性、透明度、清晰度和品牌素材使用 | 正文已完整打开，Android 标注 2026-09-22 更新；onboarding 与素材下载后代未深入审计 |
| [Matchmaking API](https://developer.android.com/health-and-fitness/health-connect/ui/matchmaking?hl=zh-CN) | 发现可为已获读权限的记录类型写入数据的其他应用/设备；可按类型及来源筛选 | 简体中文正文已打开；英文变体抓取缓存未命中。`HealthConnectClient`、实验性注解、功能探测与来源过滤已核对；先有读授权的要求与 Play FAQ“在权限提示前”简述存在顺序差异，见上文。Beta 注册和更深 API 参考未穷尽 |
| [为新用户制定计划](https://developer.android.com/health-and-fitness/health-connect/ui/onboard-users?hl=zh-CN) | Health Connect 可从系统界面启动连接；额外 onboarding Activity 的系统触发与重复启动条件 | 正文已打开并核对 Android 14 前后 manifest 路由；Matchmaking 不支持授权后自动 onboarding 触发器。下层 API/示例未穷尽 |
| [推介 Health Connect](https://developer.android.com/health-and-fitness/health-connect/ui/promote?hl=zh-CN) | 说明用户收益、清晰按钮措辞、入口位置和新数据类型的情境化权限提示 | 正文已打开，Android 标注 2026-09-23 更新；所列图片/设置子项未逐个抓取 |
| [权限和数据访问](https://developer.android.com/health-and-fitness/health-connect/ui/permissions?hl=zh-CN) | 同步开关、系统权限管理入口、连续拒绝后的提示和撤权后的同步停止 | 正文已打开，Android 标注 2026-09-23 更新；`revokeAllPermissions()` API 引用返回 Cache miss |
| [数据显示和提供方信息标注](https://developer.android.com/health-and-fitness/health-connect/ui/data?hl=zh-CN) | 来源名称/图标、权限管理入口、长时间同步状态 | 正文已打开，Android 标注 2026-09-23 更新；`DataOrigin.packageName` API 返回 Cache miss，官方 GitHub 示例已打开 |
| [MatchmakingRequest](https://developer.android.com/reference/androidx/health/connect/client/matchmaking/MatchmakingRequest) / [MatchmakingResponse](https://developer.android.com/reference/androidx/health/connect/client/matchmaking/MatchmakingResponse) | 匹配请求含记录类型及 include/exclude 数据源；响应说明是否存在可展示来源 | API 类的目标段已读取；页面带大型共享参考目录，未审每个类成员/跨链接。两类均标为 `@ExperimentalMatchmakingApi`，加入 connect-client 1.2.0-alpha06 |
| [HealthConnectClient API](https://developer.android.com/reference/kotlin/androidx/health/connect/client/HealthConnectClient) | Matchmaking 的 `checkIfMatchmakingIsPossible()` / `createMatchmakingIntent()` 与设备功能可用性 | 完整参考页超过读取器 4 MiB 限制；只用官方索引片段核对“调用应用须可读相应类型”、实验标注和系统流程范围，不能视为完整 API 正文已读 |
| [`DataOrigin` API](https://developer.android.com/reference/kotlin/androidx/health/connect/client/records/metadata/DataOrigin) | Android 指南用 `DataOrigin.packageName` 识别数据来源应用 | API 页返回 Cache miss；仅记录父页面明确给出的属性用途，不推断 API 细节 |
| [Jetpack `PermissionController` API](https://developer.android.com/reference/kotlin/androidx/health/connect/client/PermissionController) | 权限和数据访问指南引用的 `revokeAllPermissions()` | API 页返回 Cache miss；父页面关于撤权 UI 延迟的说明已摘要，方法其他行为仍未独立核验 |
| [Choose a developer account type](https://support.google.com/googleplay/android-developer/answer/13634885?hl=en) | 健康/医疗/研究服务通常须用组织账号，组织账号需 D‑U‑N‑S 编号 | 已打开并整理；账号验证细节见Play Console 要求[Play Console 要求](../play-console-requirements/play-console-requirements.zh-CN.md) |
| [Advance Notice](https://support.google.com/googleplay/android-developer/answer/6320428?hl=en) | 政府或认可医疗机构授权、公共卫生/接触者追踪等特定审查材料 | 帮助页已打开；提交入口和账号级处理状态不公开核验 |
| [Prohibited pharmaceuticals and supplements](https://support.google.com/googleplay/android-developer/answer/9217430?hl=en) | 动态、非穷尽的违禁商品示例目录；现行健康政策和合并版政策均将其作为违规示例来源 | 2026-10-24 从现行 Health Content and Services 正文链接 ID 20 及合并版政策正文链接重开完整 540 行页面，确认四个示例分组；不复制动态长名单。该目录唯一政策正文链接指向旧 [Unapproved Substances 政策章节](https://play.google.com/about/restricted-content/unapproved-substances/)；2026-10-24 重试仍 Cache miss，目标正文/后代不推断 |
| [LegitScript](https://www.legitscript.com/) | 主健康政策提供的第三方补充参考，用于了解其监测的未批准/误导性药品和补充剂 | 2026-10-22 打开首页：可见认证、监测和数据库查询服务；未深入其产品名录或认证条件。第三方信息不替代 Google Play 政策，也不能证明获 Play 批准。 |
| [Payments policy FAQ](https://support.google.com/googleplay/android-developer/answer/10281818?hl=en) | 受监管临床服务的计费例外 | 已打开；完整支付规则见[付款专题](../payments/payments-and-subscriptions.zh-CN.md) |
| [Health Permissions API reference](https://developer.android.com/reference/android/health/connect/HealthPermissions) | Android 平台 Health Connect 权限常量、数据类别和 API/Extension 版本 | 正文已打开；按审核相关类别、特殊权限流程和版本段作有边界摘要，未逐项抄录全部成员，见下文 |

### HealthPermissions API reference：有边界的实现摘要

**本分支复核：2026-10-23。**重新打开 Android API reference，并按类别抽查代表性权限、版本注记及权限用途界面关联；完整常量目录仍未逐项复制。

这是 Android 平台 `android.health.connect.HealthPermissions` 类的 API 实现参考，页面将其描述为访问 Health Connect API 的权限。类本身标注 **API level 34、U Extensions 7**；成员条目列出 `android.permission.health.*` 字符串、用途，以及适用时的 API level 和 U Extension；本摘要选取的权限均标注 `dangerous` protection level。页面还要求应用支持 `Intent.ACTION_VIEW_PERMISSION_USAGE` 与 `HealthConnectManager.CATEGORY_HEALTH_PERMISSIONS`，供 Health Connect 显示应用的权限理由/数据政策。这些信息说明 Android 端权限声明和系统交互如何实现，**不等于 Google Play 对该应用或权限用途的批准**。

| 参考范围 | 页面列出的成员/限制 | 版本提示（按 API reference 明示） |
| --- | --- | --- |
| 按数据类型读写 | 分别使用 `READ_*` / `WRITE_*`，例如 `READ_STEPS`、`WRITE_STEPS`、`READ_HEART_RATE`、`WRITE_HEART_RATE`；覆盖活动、身体测量、周期追踪、营养、睡眠、生命体征、健康状态等数据。具体记录与权限映射以数据类型表为准。 | 基础类与常见成员从 API 34 / U Extensions 7 起；例如皮肤温度读写权限为 API 35 / U Extensions 13。并非每个成员都同一版本加入。 |
| 后台、历史与路线 | `READ_HEALTH_DATA_IN_BACKGROUND` 用于后台读取；`READ_HEALTH_DATA_HISTORY` 用于读取全部历史数据。`READ_EXERCISE_ROUTES` 仅可由用户在 Health Connect 设置或路线请求界面手动授予，应用自行请求会被忽略。 | 后台/历史读取为 API 35 / U Extensions 13；路线权限为 API 35 / U Extensions 12。 |
| 医疗记录与正念 | `READ_MEDICAL_DATA_*` 将过敏/不耐受、病症、实验室结果、药物、个人和医务人员信息、妊娠、医疗程序、社会史、疫苗、就诊和生命体征分开；另有 `WRITE_MEDICAL_DATA`。正念读写权限单独列出。 | 医疗记录权限为 API 36 / U Extensions 16；正念读写为 API 36 / U Extensions 15。 |
| 症状与周期阶段 | 症状权限按具体症状分别列为 `READ_SYMPTOM_*` / `WRITE_SYMPTOM_*`，示例包括腹痛、咳嗽和发热；周期阶段有单独的读写权限。Play FAQ 也明确没有 `ALL_SYMPTOMS` 通配权限。 | 症状权限为 API 37 / U Extensions 21；周期阶段读权限为 API 37 / U Extensions 22，写权限为 API 37 / U Extensions 22。 |

本摘要选取了按类型读写、后台/历史读取、路线授权、医疗记录和症状/周期阶段等审核相关成员与版本限制；**未逐项复制所有 `READ_*` / `WRITE_*` 常量、每种记录字段、每个症状成员或 API 子项**。此类权限参考也不涵盖健康应用可能使用的所有 Android 权限（例如身体传感器、位置、相机或蓝牙）。Android 文档给出实现能力和平台版本条件；Play 规则仍要求在 Play Console 申报实际数据类型、逐项说明用户收益和功能关联、只申请最低必要范围，并接受相应政策审核。应将技术接入与 Play 政策资格分别核对。

| 直接子链/邻近权限指南 | 访问状态与本次核对范围 | 与 Play 规则的关系 |
| --- | --- | --- |
| [Intent API reference — `ACTION_VIEW_PERMISSION_USAGE`](https://developer.android.com/reference/android/content/Intent#ACTION_VIEW_PERMISSION_USAGE) | 已打开并核对该 action：Android API level 29 起；供应用展示权限用途说明，处理 Activity 需受 `START_VIEW_PERMISSION_USAGE` 保护。 | 系统交互实现要求；不是 Play Console 声明或权限用途批准。 |
| [HealthConnectManager API reference — `CATEGORY_HEALTH_PERMISSIONS`](https://developer.android.com/reference/android/health/connect/HealthConnectManager#CATEGORY_HEALTH_PERMISSIONS) | 已打开并核对该 category：Android API level 34 / U Extensions 7；与上述 action 配合显示 Health Connect 权限理由/数据政策。 | Android 平台实现细节；不能替代 Play 审核。 |
| [Health Connect data types](https://developer.android.com/health-and-fitness/health-connect/data-types) | 正文已打开；核对七类数据、Manifest 权限表、Play Console 数据用途/具体类型申报，以及后台读取和读取 30 天前数据所需的额外权限。权限表适用于 Health Connect SDK 1.0.0-alpha10+；未逐行复录各记录。 | 指导 Manifest 权限映射和 Play 数据类型申报；页面提示未完成所需声明/审批可能导致用户访问错误。它不等于 Play 已批准应用。 |
| [Get started with Health Connect](https://developer.android.com/health-and-fitness/health-connect/get-started) | 正文权限段已打开；核对了 Manifest 读写权限、`ACTION_VIEW_PERMISSION_USAGE`/权限理由 Activity、请求权限和每次使用前复查授权的要求。 | 指导接入；指南要求 Manifest 与 Play Console 所申报数据类型匹配。 |
| [Read data](https://developer.android.com/health-and-fitness/health-connect/read-data) | 正文权限相关段落已打开；核对后台读取需额外权限，以及默认可读首次授权前 30 天内数据、读取更早数据需历史读取权限。 | 技术读取范围；无论用户是否授权，Play 的已申报用途、最小权限和数据处理政策仍适用。 |
| [Jetpack `PermissionController` API reference（Java 路径）](https://developer.android.com/reference/androidx/health/connect/client/PermissionController) | 独立的官方 Java API 路径已打开（4,065 行）；核对 API 1.1.0 的三项公开方法：创建运行时请求 contract（provider package name 可选）、读取当前已获授权集合、撤销该应用全部已授 HealthPermission；页面标注 2026-06-24 更新。 | 实现请求、检查和撤销系统授权；它不判断 Play 用途是否合规或已批准。原 Kotlin 路径另列，未观察到重定向。 |
| [Jetpack `PermissionController` API reference（Kotlin 路径）](https://developer.android.com/reference/kotlin/androidx/health/connect/client/PermissionController) | 此精确目标返回 Cache miss；同名 Java 路径独立打开并核对，不把它声称为该 URL 的重定向或等价跳转。 | 精确 Kotlin 目标正文状态仍受限；后代状态见逐 URL 台账。 |
| [Jetpack `HealthPermission` API reference（Java 路径）](https://developer.android.com/reference/androidx/health/connect/client/permission/HealthPermission) | 独立官方路径已打开（4,715 行；标注 2026-06-24 更新）。`getReadPermission<T>()` / `getWritePermission<T>()` 把 Record 类型映射为权限字符串；KClass 重载从 connect-client 1.1.0 提供，非法 Record 类型抛 `IllegalArgumentException`。重点核对历史读取、后台读取、医疗记录与运动路线权限，未逐个复制整个成员表。 | 历史数据权限影响首次授权前 30 天以外的数据读取；后台读取需独立权限。医疗读权限按数据类型细分，写医疗数据由单一 `PERMISSION_WRITE_MEDICAL_DATA` 覆盖；请求前须检查功能可用性。技术能力不等于 Play 数据类型申报批准。 |
| [Jetpack `HealthPermission` API reference（Kotlin 路径）](https://developer.android.com/reference/kotlin/androidx/health/connect/client/permission/HealthPermission) | 此精确 Kotlin 页面仍因正文超过读取器 4 MiB 限制而不可读；上列 Java 类路径是另外打开的官方页面，不能据此声称观察到重定向。 | 搜索摘要不作为该精确页的正文证据；完整 API 及其成员树未穷尽。 |
| [Jetpack `HealthConnectFeatures` API reference](https://developer.android.com/reference/androidx/health/connect/client/HealthConnectFeatures) | 大型 API 页已打开（4,138 行；标注 2026-08-26 更新）；核对 `getFeatureStatus()` 及 AVAILABLE/UNAVAILABLE 状态，并抽查后台读取、历史读取、个人健康记录功能标志。相关成员从 connect-client 1.1.0 提供。 | Android 指南要求按设备上 Health Connect 版本检查功能可用性；功能缺失时，相关权限可能不会获授，相关 API 也不能运行。全量功能常量树未逐项审阅。 |
| [`Record` API reference](https://developer.android.com/reference/androidx/health/connect/client/records/Record) | 大型 API 页中检查其通用接口和 `getMetadata()`：可读/可写记录共用的元数据接口，成员自 1.1.0 提供；页面标注 2026-06-24 更新。 | 仅作 `HealthPermission` 类型参数背景；Record 子类集合庞大，未逐类审阅。 |
| [`ExerciseSessionRecord` API reference](https://developer.android.com/reference/androidx/health/connect/client/records/ExerciseSessionRecord) | 大型 API 页选读路线字段：`exerciseRouteResult` 的路线数据须落在父 session 时间范围内，且不能晚于 session 结束时间；页面标注 2026-08-26 更新。 | 运动路线属于位置敏感信息；页面的大量运动类型/聚合成员和更深链接未穷尽。 |
| [`ExerciseRoute` API reference](https://developer.android.com/reference/androidx/health/connect/client/records/ExerciseRoute) | 大型 API 页选读 `getRoute()`：返回由多个 `ExerciseRoute.Location` 点组成的运动路线；页面标注 2026-06-24 更新。 | 路线本身是时间序列位置数据；继续查看下面的 Location 子类字段，不代表 Play 允许任意收集。 |
| [`ExerciseRoute.Location` API reference](https://developer.android.com/reference/androidx/health/connect/client/records/ExerciseRoute.Location) | 大型 API 页已打开（3,952 行；标注 2026-06-24 更新）：每点必需时间、纬度和经度；海拔、水平/垂直精度为可选字段。 | 直接展示可识别路线和活动时间的精细位置数据；按用户可见功能最小化请求、披露和保留范围，仍须符合 Play/用户数据规则。 |
| [`ExerciseRouteResult` API reference](https://developer.android.com/reference/androidx/health/connect/client/records/ExerciseRouteResult) | 大型 API 页已检查三种返回状态：`Data`、`ConsentRequired`、`NoData`；标注 2026-06-24 更新。 | 区分已有路线、需用户同意以及没有可请求路线；三个直接嵌套类型另有下方逐 URL 审计。 |
| [`ExerciseRouteResult.ConsentRequired`](https://developer.android.com/reference/androidx/health/connect/client/records/ExerciseRouteResult.ConsentRequired) | 直接嵌套类型页已打开：表示没有授予权限，因此无法返回路线值；标注 2026-06-24 更新。 | 转入用户同意请求流程，不可把权限缺失当作空路线数据。 |
| [`ExerciseRouteResult.Data`](https://developer.android.com/reference/androidx/health/connect/client/records/ExerciseRouteResult.Data) | 直接嵌套类型页已打开：携带 `ExerciseRoute`，并通过 `getExerciseRoute()` 读取；标注 2026-06-24 更新。 | 路线数据只应在必要、已授权的功能中使用。 |
| [`ExerciseRouteResult.NoData`](https://developer.android.com/reference/androidx/health/connect/client/records/ExerciseRouteResult.NoData) | 直接嵌套类型页已打开：当前 session 没有可请求的路线数据；标注 2026-06-24 更新。 | 不应因 `NoData` 状态提示用户额外授权。 |
| [`ExerciseRouteRequestContract` API reference](https://developer.android.com/reference/androidx/health/connect/client/contracts/ExerciseRouteRequestContract) | 大型 API 页已打开（4,047 行；标注 2026-06-24 更新）；以 session ID 发起路线请求，得到路线时返回 ExerciseRoute；若用户未授权或该 session 没有路线，则返回 null。 | 应在用户触发的情境展示请求；该 contract 提供 Android 端路线同意流程，不替代 Play 的健康/位置用途审查。页面其他通用 ActivityResultContract 链接未纳入本政策分支。 |

对应的 Play 侧依据是 [Android Health Permissions FAQ](https://support.google.com/googleplay/android-developer/answer/12991134?hl=en)：它约束适用用例、逐项权限理由和用户收益、敏感数据类别审查与最小数据请求。API reference 与 Android 指南用于解释实现，FAQ/Health Content and Services 等 Play 政策页用于判断允许用途和审核要求。

### Health Connect 数据类型页的直接子链：体验指南与测试最佳实践

2026-10-22 逐项尝试了现行[数据类型页](https://developer.android.com/health-and-fitness/health-connect/data-types)编号 13–170 的 **158 个正文链接引用**（含重复/同一规范页链接；不含导航和页脚）。它们包括 Play 声明、快速开始、后台/历史读取、七类数据所用体验指南，以及大量数据记录、单位和聚合 API。主要流程指南已打开并概括；多数 Jetpack Kotlin 记录/API 参考目标返回超过 4 MiB 的抓取错误或超时，不能据此补写字段级实现。数据类型页面本身显示的类别、权限与 feature flag 仍可用于定位目标 API。

| 直接目标 | 关键内容及与 Play 的关系 | 核验状态 |
| --- | --- | --- |
| [Publish your health app on Google Play](https://developer.android.com/health-and-fitness/health-connect/publish) | 发布顺序为政策核对、Data safety、Health Apps 声明和逐项数据类型用途说明；新应用及数据类型发生变化的更新都要完成相应申报。只能申请支持具体用户可见健康功能的最低类型，并在 Play 商店页使用与 Health Connect 内相同的隐私政策。 | 正文已在上表展开；旧申请表的 2025-01-22 截止日仅是历史信息。 |
| [Sleep experience guide](https://developer.android.com/health-and-fitness/health-connect/experiences/sleep) | 用 `SleepSessionRecord` 记录完整睡眠会话，并按会话时段关联心率、血氧、呼吸频率和睡眠阶段。指南建议活跃跟踪最多每 15 分钟写入、后台延迟写入用 WorkManager、每批最多 1,000 条、为重试设置稳定唯一的 `clientRecordId`、避免会话时间重叠，并在睡眠结束后写完整会话。 | 正文 431 行；已核对权限、最佳实践和测试部分。它是 Android 实现指导，不是 Play 审核标准。 |
| [Vitals experience guide](https://developer.android.com/health-and-fitness/health-connect/experiences/vitals) | 血压、心率、体温等可逐项读写；建议批量写入（最多 1,000 条）、实时传感器批量间隔不超过 15 分钟、WorkManager 后台同步、唯一 `clientRecordId`、用 ChangeLogs 同步变化、校准单位/时间戳/生理范围，并在每次读取或写入前检查权限。 | 正文 393 行；已核对最佳实践、测试和错误处理章节。 |
| [Workout experience guide](https://developer.android.com/health-and-fitness/health-connect/experiences/workouts) | `ExerciseSessionRecord` 可关联运动路线、心率、速度和距离。除批量、后台同步和去重外，应支持暂停/继续，暂停期间停止采集；检查 GPS 精度与续航。跨应用读取运动路线须有用户主动操作；不能在后台读取其他应用创建的路线，即使已有持续授权。 | 正文 536 行；已核对路线权限/同意、最佳实践和测试章节。 |
| [Training plans](https://developer.android.com/health-and-fitness/health-connect/features/training-plans) | 训练计划是独立 `PlannedExerciseSessionRecord` 类型；先检查 `FEATURE_PLANNED_EXERCISE`。计划写入应用与训练读取应用所需权限不同，通常只申请角色实际需要的读/写权限；写权限可能已覆盖自己写入记录的读取。 | 正文已打开并核对权限矩阵；支持版本和 feature flag 需按当期 SDK 核对。 |
| [Add exercise routes](https://developer.android.com/health-and-fitness/health-connect/features/exercise-routes) | 路线要与运动会话关联；写权限 `WRITE_EXERCISE_ROUTE` 与读权限 `READ_EXERCISE_ROUTES` 名称不对称。读取第三方路线使用用户授权流程；指南明确建议在用户正在操作应用时申请，后台读取会需要额外同意。 | 正文已打开；Android 实现要求，不代表 Play 对精确位置/健康数据访问的批准。 |
| [Mindfulness](https://developer.android.com/health-and-fitness/health-connect/features/mindfulness) | 心理健康/福祉类型可记录冥想、呼吸、音乐、动作等；先检测 `FEATURE_MINDFULNESS_SESSION`，只申请 `READ_MINDFULNESS` / `WRITE_MINDFULNESS` 所需范围。 | 正文关键权限段已核对；支持版本会随 SDK 更新。 |
| [Skin temperature](https://developer.android.com/health-and-fitness/health-connect/features/skin-temperature) | `SkinTemperatureRecord` 表示指端、脚趾或手腕的外周皮温，**不可当作核心体温**；指南要求检测 `FEATURE_SKIN_TEMPERATURE`。 | 正文关键部分已核对；如产品表达疾病检测/医疗功效，另按健康内容和医疗器械政策审查。 |
| [Sleep sessions](https://developer.android.com/health-and-fitness/health-connect/features/sleep-sessions)；[Steps](https://developer.android.com/health-and-fitness/health-connect/features/steps)；[Native tracking](https://developer.android.com/health-and-fitness/health-connect/features/native-tracking) | 睡眠会话的子类型时间应连续且不重叠；步数提供区间计数及聚合。Native tracking 用设备传感器生成步数、距离、活动卡路里；至少一个应用获得某类型读取权限后才开始生成，用户可随时关闭跟踪而保留旧数据。它们补充实现，不替代每种数据类型的 Play 声明。 | Sleep sessions 与 Steps 的权限/会话段已核对；Native tracking 正文已打开并记录生成/用户控制逻辑，深层后代部分未审。 |
| [Test top use cases](https://developer.android.com/health-and-fitness/health-connect/test/test-cases)；[Health Connect Toolbox](https://developer.android.com/health-and-fitness/health-connect/test/health-connect-toolbox)；[Health Connect unit testing](https://developer.android.com/health-and-fitness/health-connect/test/unit-tests) | 官方用例覆盖首次接入、未安装 Health Connect、授权/拒绝、应用内解除关联并撤销所有权限、读/写/聚合/更新/删除。Toolbox 可对全部类型插入/读取测试记录；Fake client 支持内存记录、分页、聚合 stub、权限模拟和异常注入。应用需在拒绝/撤权时停止相应访问且不崩溃。 | 用例表正文已打开；Toolbox 与单测正文已打开。单测库目前标注 alpha；完整测试分支与其更深链接仍部分覆盖。 |
| [Legacy data types for Health Connect SDK 1.0.0-alpha09 and lower](https://developer.android.com/health-and-fitness/health-connect/data-types-legacy) | 旧 SDK 版本的历史数据类型/权限表；当前 SDK 应使用 alpha10+ 现行目录。 | 935 行页面已打开；只核对适用版本和迁移入口，未逐项转换旧权限。 |

**将最佳实践用于产品时的边界：** 这些实现指南主要为数据可靠性、互操作和用户体验提供建议。它们不是新的 Play 政策，也不能扩大 Play 批准的用例。上线前仍须按当前 Health Content and Services 与敏感权限规则，逐类型证明用户收益、披露真实数据流，并核对 Console 中的访问审批。记录 API 页面失败仅表示浏览工具无法提取大页面；不得把失败误读为页面不存在或政策豁免。

### 声明帮助页与分类页的后代

2026-10-22 重开[Health app categories and additional information](https://support.google.com/googleplay/android-developer/answer/13996367?hl=en)英文正文，并尝试页面返回的 9 个链接引用（正文链接、帮助社区与联系支持；重复锚点按规范目标归并）。页面区分健康/健身、医疗和人体受试者研究等应用类型。研究须获独立 IRB/伦理委员会批准，除非适用豁免；参与者同意应说明研究目的和时长、程序、风险/收益、保密和数据处理、联系人及退出方法。Google 要求时须提供审查批准证明。使用 Health Connect 研究数据还可能需要专门研究表单，本轮表单返回 401，字段无法核验。

#### 医疗器械资格 → Health Apps 表单分支（2026-10-23）

重新打开[Health Content and Services](https://support.google.com/googleplay/android-developer/answer/16679511?hl=en)英文正文（220 行）；简体中文根页面 `https://support.google.com/googleplay/android-developer/answer/16679511?hl=zh-CN` 本轮仍无法读取。根政策医疗功能条款中的“this article”（链接 13）指向[提供 Health apps 声明表单信息](https://support.google.com/googleplay/android-developer/answer/14738291?hl=en)，与前文 Console 声明说明链接指向同一帮助页。该帮助页英文正文（172 行）及简体中文版本（186 行）均已打开。

此分支说明：所有在 Play 发布的应用都须提交健康声明，包括测试轨道、通过 Play 更新的预装/预授权应用，以及确认没有健康功能的应用；若应用受医疗器械监管，应在声明中选择“Medical Device Apps”（中文帮助页译为“医疗设备配套应用”）。帮助页列出的例子包括诊断工具、治疗建议系统和连接医疗设备硬件的软件。对面向 EEA/北爱尔兰且受 EU MDR 2017/745 或 IVDR 2017/746 监管的应用，需公开器械/制造商身份、SRN、预期用途、警告或注意事项、eIFU 与 UDI-DI；视情况还可能需授权代表、指定机构/证书编号及运行或硬件要求。根 Play 政策另要求受监管器械应用按器械申报，可能标注为医疗器械，并在要求时提交主管机构的批准/许可/认证证明；其他健康/医疗应用须给出非医疗器械免责声明并提醒咨询医疗专业人员。这些是 Play 声明和商店展示义务，不是 Android/Health Connect 权限授权，也不替开发者或监管机构作器械分类结论。

| 本分支中的目标 | 访问状态（2026-10-23） | 与 Play 规则的关系/边界 |
| --- | --- | --- |
| 根政策：[Health Content and Services](https://support.google.com/googleplay/android-developer/answer/16679511?hl=en)；中文：[简体中文目标](https://support.google.com/googleplay/android-developer/answer/16679511?hl=zh-CN) | 英文正文已重新完整打开；中文目标返回工具不可访问错误。 | 英文正文确认医疗器械申报、可能的商店标记、按要求提供监管证明，以及非医疗器械应用的免责声明/专业人员提醒。 |
| 根政策链接 13 → [Health apps declaration 帮助页](https://support.google.com/googleplay/android-developer/answer/14738291?hl=en)；[简体中文版本](https://support.google.com/googleplay/android-developer/answer/14738291?hl=zh-Hans) | 英文和中文正文均已完整打开；中文帮助页标注可能包含 AI 翻译，可能不准确。 | 公开帮助页说明声明类别、适用应用范围和可能的补充问题；它没有给出当前账号实际看到的每一道医疗器械问题。 |
| 帮助页链接 3 → [Health apps declaration form](https://play.google.com/console/developers/app/app-content/health) | 已尝试打开；重定向至 Google 账号登录，浏览工具无法读取账号内表单。 | 仅能依据公开帮助页确认可能出现第二页和可展开补充问题；具体字段、要求上传的材料、当前表单状态均未核实。 |
| 帮助页链接 4 → [Play Console App content](https://play.google.com/console/app/app-content/summary) | 已尝试打开；重定向至 Google 账号登录，浏览工具无法读取账号内页面。 | 这是表单入口，不是公开政策正文；登录受限不表示公开帮助页或政策失效。 |

因此，本轮只核对到公开的分类说明、地区附加披露和表单提交流程；未读取登录后的医疗器械专属问题、当前材料上传控件或个案审核结果。不得据此推断任一应用已获得 Play 批准、监管许可或 Health Connect 数据访问资格。

健康主张最佳实践要求以易懂方式说明应用用途、声称收益及其依据（证据/标准/最佳实践）、目标用户、风险和必要警告/免责声明。披露示例把具体数据类型连到具体功能（例如活动数据用于估算消耗，或位置用于展示跑步路线），而不是笼统声称“应用需要权限”。这些是政策说明与申报辅助，不替代医疗器械审查或适用法律。

### 2025 年健康记录公告 → 权限 FAQ 的子链接

2025-03-05 公告要求健康记录访问具备合格用途、逐数据类型说明用户收益，并满足更严格的数据共享、用途和同意要求。公告正文有 **4 个链接锚点、3 个唯一目标**（Health Connect 政策、权限 FAQ、开发者互助社区）。其中 FAQ 于 2026-10-22 重新完整打开；其当前正文覆盖 Health Connect、身体传感器及其他可能采集或推断健康数据的权限，写明健康用例、禁止用途、逐权限理由及 Wear OS 适用性。

| FAQ 正文链接 | 页面作用及摘要 | 核验状态 |
| --- | --- | --- |
| [Health Connect developer guide](https://developer.android.com/health-and-fitness/health-connect) | Android 实现入口，包含接入、数据类型、读取/写入、医疗记录和 UI 指南；区分技术接入与 Play 政策批准 | 规范地址已打开；主要子文档见本页上表，全部 API/示例后代未闭合 |
| [HealthPermissions API reference](https://developer.android.com/reference/android/health/connect/HealthPermissions) | Android 实现参考；API level 34 / U Extensions 7 的类，以及按数据类型、后台/历史读取、医疗记录、症状等权限成员和版本段见上文摘要。FAQ 明确症状权限逐项授权，不存在 `ALL_SYMPTOMS` 通配权限 | 正文已打开并按审核相关成员作有限摘要；未逐项复制完整 `READ_*` / `WRITE_*` 列表、全部症状或所有 API 子项 |
| [Android 16 behavior changes](https://developer.android.com/about/versions/16/behavior-changes-16) | 目标 API 36 的身体传感器实现迁移背景；从 `BODY_SENSORS` 等旧权限转向细粒度 `android.permission.health.*` 权限 | 已打开并在[目标 API 专题](../target-api/target-api-level.zh-CN.md)概括；后代未全部展开 |
| [Health Content and Services policy](https://support.google.com/googleplay/android-developer/answer/16679511?hl=en) | 健康应用声明、隐私政策、敏感披露、最小权限、硬件兼容性、医疗器械与健康错误信息的正式 Play 政策 | 英文正文已完整打开；相关类别/声明子页见上表 |
| [User Data policy](https://support.google.com/googleplay/android-developer/answer/10144311) | 健康数据属于个人和敏感用户数据；要求按用户同意用途处理，适用显著披露、肯定同意、数据安全及第三方 SDK 责任 | 已打开并在[用户数据专题](../user-data/user-data.zh-CN.md)交叉摘要 |
| [Permissions and APIs that Access Sensitive Information](https://support.google.com/googleplay/android-developer/answer/16558241) | 所有敏感权限须与商店推广的核心功能相关；按需、分阶段申请，并尊重拒绝，优先满足最小范围替代方案 | 现行政策正文已打开并在[敏感权限专题](../sensitive-permissions/sensitive-permissions.zh-CN.md)整理 |
| [Health Connect UI guidelines](https://developer.android.com/health-and-fitness/health-connect/ui/guidelines) | 以一致、透明、清楚的界面说明数据读取用途及用户管理权限的路径 | 正文已完整打开；onboarding/素材等孙链接部分未审 |
| [Managing permissions in Health Connect video](https://youtu.be/C2I4OymO3S4) | 权限管理培训视频 | YouTube 页面可识别标题；正文/字幕未提取，未据此补写政策 |

FAQ 的通用侧栏另列 **32 个**政策教育/应用要求入口；它们不是公告正文的直接链接。知识库已有部分入口专题和摘要，但该侧栏的全部页面及各自后代尚未逐项复审。

健康声明说明页的主要后代包括：

| 后代目标 | 与声明的关系 | 本轮状态 |
| --- | --- | --- |
| [Health app categories and additional information](https://support.google.com/googleplay/android-developer/answer/13996367?hl=en) | 分类定义、人体研究同意/伦理审查、健康数据权限示例与披露最佳实践 | 正文已打开；见上表及本页权限实践部分 |
| [System services](https://support.google.com/googleplay/android-developer/answer/12085265) | OEM、运营商、SoC 等预装系统服务例外及核验入口 | 正文已打开；Partner Center 外部指南要求伙伴访问 |
| [Private Android apps](https://support.google.com/a/answer/2494992) → [Manage private Android apps in Google Play](https://knowledge.workspace.google.com/admin/devices/manage-private-android-apps-in-google-play) | 此声明帮助页中的旧 Workspace Help 链接现重定向到 Google Workspace 管理指南，说明组织内私有应用的发布和管理。声明帮助页本身明确私有应用免填 Health Apps 声明；Workspace 指南说明操作，不独立定义该健康政策豁免。 | 现行 293 行指南已打开；发布步骤受账号/版本影响，多数 Admin Console 深层链接仍部分覆盖。 |
| [Health Connect research consent form](https://docs.google.com/forms/d/1WFUG98j3kRU_muqcJB-JJBSEWdGiGqky1R75YC-rG4w/viewform?edit_requested=true) | Health Connect 研究用途的专用申报/同意流程 | 返回 401；表单字段不可读取 |
| [Play Console App content](https://play.google.com/console/app/app-content/summary) | 实际声明入口 | 重定向到账号登录；不代表公共页面失效 |

分类页进一步链接到[Android Manifest.permission 参考](https://developer.android.com/reference/android/Manifest.permission)（完整 API 权限目录已打开，但未逐项遍历）、当前[敏感权限政策](https://support.google.com/googleplay/android-developer/answer/16558241)（Health Connect 许可与限制），以及旧“Elevated Privilege Abuse”链接现指向的[恶意软件政策](https://support.google.com/googleplay/android-developer/answer/9888380)（权限滥用与恶意行为边界）。这些页面已与[敏感权限专题](../sensitive-permissions/sensitive-permissions.zh-CN.md)、[恶意软件与数据外传专题](../mobile-unwanted-software/mobile-unwanted-software.zh-CN.md)交叉关联；研究表单、Partner Center 和 Console 的动态/账号专属后代仍受访问限制。

此范围仅覆盖本专题政策相关的声明和分类分支，不表示 Health Connect 文档站中所有示例、视频、API reference 的孙链接都已穷举。疾病/医疗器械法规、账号资格、研究审批和 Console 实际表单须按应用分发地区及账号单独确认。

## 关联知识页

- [用户数据](../user-data/user-data.zh-CN.md) · [Data safety](../data-safety/data-safety.zh-CN.md) · [敏感权限与 API](../sensitive-permissions/sensitive-permissions.zh-CN.md)
- [Play Console 权限声明与审核](../permissions-declaration/permissions-declaration.zh-CN.md) · [家庭政策与儿童安全](../age-restricted-child-safety/age-restricted-child-safety.zh-CN.md)
- [付款、计费与订阅](../payments/payments-and-subscriptions.zh-CN.md) · [目标 API 与 Android 迁移](../target-api/target-api-level.zh-CN.md)
- 官方：[Health Content and Services](https://support.google.com/googleplay/android-developer/answer/16679511?hl=en) · [Android Health Permissions FAQ](https://support.google.com/googleplay/android-developer/answer/12991134?hl=en) · [Health Connect publish guide](https://developer.android.com/health-and-fitness/health-connect/publish)
