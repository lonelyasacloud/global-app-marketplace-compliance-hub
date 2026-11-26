---
id: google-play.play-policy-insights-skill
platform: google-play
language: zh-CN
authority: implementation-note
status: current
kb_checked_at: 2026-10-23
review_due: 2027-01-23
regions: [global]
topics: [play-policy-insights, developer-tool, static-analysis]
snapshot_id: android.play-policy-insights-skill
snapshot_package: "GooglePlay-KnowledgeBase-2026-10-24-review.zip"
coverage_status: "detailed-reference-summary"
source_url: "https://github.com/android/skills/tree/main/play/play-policy-insights"
effective_date: "official developer tool updated 2026-07-13; not Play policy text"
---

# Android Play Policy Insights 技能：代码审查辅助、资源清单与范围边界

> **导入说明（Google batch 9）。** 正文来自已经分开的 2026-10-24 Google Play 知识库快照（`android.play-policy-insights-skill`，核对日 2026-10-23）的改写工具摘要，不是仓库文件的逐字副本，也不是 Play 政策正文。核对日 Google android/skills 仓库中的英文文件是该工具内容的效力来源。`kb_checked_at` 是快照源文件记录的核对日；本次导入没有重新打开线上仓库。文中“本知识库”“本库”“本地专题”等说法描述的是该快照库的覆盖范围，不是本仓库已经导入的页面。指向本仓库没有收录的专题、链接图、台账或 CSV 的相对链接改为文字提及。指向 Google batch 1–8 或本批八个专题的相对链接改为本仓库文件。**本页描述的是官方 Android/Play 开发者工具。技能元数据把作者标为 Google LLC，更新日期为 2026-07-13。GitHub 的 `main` 分支会变化。该工具不是 Google Play 政策正文，不是 Play 审核结果，也不是合规认证。** 所核对的仓库内容是英文。快照没有记录中文官方技能页。中文正文是编辑改写。配置链接到联系人政策预览。该预览的 2027-01-27 日期留在联系人专题，不是本工具陈述的规则。证据等级：Implementation note。

**官方 Android/Play 开发者工具。** 本页描述 Google [android/skills](https://github.com/android/skills/tree/main/play/play-policy-insights) 仓库中的 Play Policy Insights 技能。它不是 Play 政策正文。

## 定位与核对口径

本页整理 Android 官方 [android/skills 仓库中的 Play Policy Insights 技能](https://github.com/android/skills/tree/main/play/play-policy-insights)。该目录不是 Google Play 政策正文，而是供编程助手使用的应用代码审查工作流。技能元数据署名 Google LLC，标注更新日为 2026-07-13；GitHub 的 main 分支会变化。本次于 2026-10-23 打开技能原文、仓库目录及其资源/脚本子页，并对同名本地安装副本作结构核对。

核心用途是把静态代码线索与开发者提供或公开可读的 Play 信息对照，生成带证据的预提交检查报告。它要求覆盖三个审查域：权限与 API 卫生、用户账号与身份、数据安全与隐私；并明确要求检查 Data safety、审核演示登录凭证及受限权限。这个覆盖范围不等于完整的 Developer Program Policy 审核，也不代表 Google Play 审核结论。

## 工作流及关键约束

1. **初始化与分流：** 运行 orchestrator 的 init 流程，扫描应用目录中的相关源码/配置，汇总模块、权限和数据源线索，并按线索激活审查目标、生成工作提示。临时目录在工作区根目录下创建，名称带有 play_policy_insights 前缀和唯一标识。
2. **定向分析：** 对激活目标检查权限/API、数据采集和传输、显著披露/同意、账号/身份及删除等问题。资源提示要求优先使用扫描器提供的文件与行号，避免无边界搜索；严重发现须指出直接证据，不得把缺少上下文当作违规。
3. **交叉复核与报告：** 汇总结果后由 critic 阶段复查误报、夸大和证据不足，再由 report 脚本生成报告。技能按环境区分委派和顺序执行两种方式，并规定初始 orchestrator 失败时停止，不能用手工审查冒充自动扫描成功。
4. **文件隔离：** 中间文件、日志和最终机器结果都须写在上述 scratch 目录；所需输入缺失时按 fail-fast 处理。报告模板声明它仅供信息和建议用途，不构成法律意见、合规保证或上架批准。

## 仓库正文及直接子页

检查时，技能目录的直接清单显示 SKILL.md、resources/、scripts/ 三项。两个目录分别列出 8 个资源文件和 5 个 Python 脚本；以下逐项记录其用途。代码按模块用途阅读，不将本页误作逐行源码安全审计。

| 子页 | 内容和作用 |
| --- | --- |
| [SKILL.md](https://github.com/android/skills/blob/main/play/play-policy-insights/SKILL.md) | 定义三域范围、路径解析、两阶段流程、初始化/聚合/复核/报告命令、失败停止规则与输出隔离。 |
| [common_mandates.md](https://github.com/android/skills/blob/main/play/play-policy-insights/resources/common_mandates.md) | 要求绝对路径、只在目标应用目录内做定向检索、排除构建/缓存/测试目录；发现须有直接证据，抽象或缺失上下文时降低结论级别，空结果保持空数组。 |
| [goal_data_safety.md](https://github.com/android/skills/blob/main/play/play-policy-insights/resources/goal_data_safety.md) | 检查数据来源、网络传输、SDK、Data safety 声明、显著披露与同意等隐私线索。 |
| [goal_user_account.md](https://github.com/android/skills/blob/main/play/play-policy-insights/resources/goal_user_account.md) | 从登录界面、账号管理和用户档案线索识别账号功能，再检查审核登录凭证、账号删除等事项。 |
| [goal_permissions_and_apis.md](https://github.com/android/skills/blob/main/play/play-policy-insights/resources/goal_permissions_and_apis.md) | 按权限和数据源线索检查短信/通话记录、媒体、位置、联系人、音频、文件、设备应用可见性、无障碍、精确闹钟及前台服务等情形。 |
| [critic.md](https://github.com/android/skills/blob/main/play/play-policy-insights/resources/critic.md) | 对发现逐项核验，区分可由代码证实的违规、需要人工判断的模糊情形及信息性建议，抑制无根据的严重结论。 |
| [compliance_report_template.md](https://github.com/android/skills/blob/main/play/play-policy-insights/resources/compliance_report_template.md) | 规定最终报告的状态、证据、待人工核验事项和免责声明；明确扫描可能遗漏问题，最终责任仍由开发者承担。 |
| [policies.json](https://github.com/android/skills/blob/main/play/play-policy-insights/resources/policies.json) | 用结构化模块名称、类别、政策链接和数据分类词表为报告提供政策提示。下节逐项映射其 16 个模块。 |
| [scanner_config.json](https://github.com/android/skills/blob/main/play/play-policy-insights/resources/scanner_config.json) | 配置扫描器识别的信号类别、文件名模式、权限组、忽略目录和扩展名；这是静态检测配置，不是完整政策目录。 |
| [orchestrator.py](https://github.com/android/skills/blob/main/play/play-policy-insights/scripts/orchestrator.py) | 解析应用模块、Gradle/版本目录和 Manifest，整理身份/权限/数据源线索，调用扫描器并生成阶段提示、聚合结果。 |
| [scanner.py](https://github.com/android/skills/blob/main/play/play-policy-insights/scripts/scanner.py) | 按配置收集受支持的源码/配置文件，并用限定模式寻找数据源、传输、权限和披露相关线索。 |
| [play_store_scraper.py](https://github.com/android/skills/blob/main/play/play-policy-insights/scripts/play_store_scraper.py) | 读取公开 Play 商店详情和 Data safety 展示页。代码按包名构造 play.google.com/store/apps/details 与 /store/apps/datasafety 请求，并使用英语/美国区域参数。它读公开商店页面，不等同于读取开发者账号里的 Console 表单或私有状态。 |
| [template_engine.py](https://github.com/android/skills/blob/main/play/play-policy-insights/scripts/template_engine.py) | 渲染资源提示中的变量、条件和循环模板。 |
| [generate_report.py](https://github.com/android/skills/blob/main/play/play-policy-insights/scripts/generate_report.py) | 合并扫描、抓取和复核 JSON，格式化严重级别、发现卡片和最终 Markdown 报告。 |

## policies.json 引用的官方政策与实现资料

配置中有 **31 次 URL 引用、18 个规范化唯一目标**，分属 16 个审查模块。逐项目标如下；这些页面在本知识库已有逐页审计记录。Android 实现文档只是技术背景，不自动产生 Play 权限资格。

| 配置模块 | 它关联的官方页面 | 知识库入口 |
| --- | --- | --- |
| Data safety section | [User Data：Data safety 章节](https://support.google.com/googleplay/android-developer/answer/10144311#safetysection)、[Android 声明数据用途](https://developer.android.com/privacy-and-security/declare-data-use)、[Data safety 表单说明](https://support.google.com/googleplay/android-developer/answer/10787469) | [User Data](../user-data/user-data.zh-CN.md)、[Data safety](../data-safety/data-safety.zh-CN.md) |
| Login credentials | [审核登录详情要求](https://support.google.com/googleplay/android-developer/answer/15748846) | [应用审核准备](../app-review-preparation/app-review-preparation.zh-CN.md) |
| SMS and Call Log | [敏感权限政策：短信/通话章节](https://support.google.com/googleplay/android-developer/answer/16558241#sms-call-permissions)、[短信和通话记录权限帮助页](https://support.google.com/googleplay/android-developer/answer/10208820) | [短信和通话记录](../sms-call-log/sms-call-log.zh-CN.md)、[权限申报](../permissions-declaration/permissions-declaration.zh-CN.md) |
| Package Visibility | [敏感权限政策：应用可见性章节](https://support.google.com/googleplay/android-developer/answer/16558241#package-vis)、[应用包可见性](https://support.google.com/googleplay/android-developer/answer/10158779) | [敏感权限](../sensitive-permissions/sensitive-permissions.zh-CN.md) |
| All Files Access | [敏感权限政策：全部文件访问章节](https://support.google.com/googleplay/android-developer/answer/16558241#all-files-access)、[Manage all files Android 指南](https://developer.android.com/training/data-storage/manage-all-files)、[文件访问权限申报](https://support.google.com/googleplay/android-developer/answer/10467955) | [敏感权限](../sensitive-permissions/sensitive-permissions.zh-CN.md)、[Android 隐私清单](../android-privacy-checklist/android-privacy-checklist.zh-CN.md) |
| Photo and Video Permissions | [敏感权限政策：照片/视频章节](https://support.google.com/googleplay/android-developer/answer/16558241#photo-and-video-permissions)、[权限最小化替代方案](https://support.google.com/googleplay/android-developer/answer/16935362)、[Android 共享媒体存储](https://developer.android.com/training/data-storage/shared/media) | [照片和视频权限](../photo-video-permissions/photo-video-permissions.zh-CN.md) |
| Location Permissions | [敏感权限政策](https://support.google.com/googleplay/android-developer/answer/16558241)、[位置权限声明](https://support.google.com/googleplay/android-developer/answer/9799150) | [联系人与位置最小范围](../contacts-location-permissions/contacts-location-permissions.zh-CN.md)、[后台位置](../background-location/background-location.zh-CN.md) |
| Contacts Permissions | [联系人权限政策预览](https://support.google.com/googleplay/android-developer/answer/16909972#contacts-permissions)、[权限最小化替代方案](https://support.google.com/googleplay/android-developer/answer/16935362) | [联系人与位置最小范围](../contacts-location-permissions/contacts-location-permissions.zh-CN.md) |
| Audio Recording | [User Data](https://support.google.com/googleplay/android-developer/answer/10144311)、[敏感权限政策](https://support.google.com/googleplay/android-developer/answer/16558241) | [User Data](../user-data/user-data.zh-CN.md)、[敏感权限](../sensitive-permissions/sensitive-permissions.zh-CN.md) |
| Files and Docs Access | [文件访问权限申报](https://support.google.com/googleplay/android-developer/answer/10467955)、[敏感权限政策](https://support.google.com/googleplay/android-developer/answer/16558241) | [敏感权限](../sensitive-permissions/sensitive-permissions.zh-CN.md)、[Android 隐私清单](../android-privacy-checklist/android-privacy-checklist.zh-CN.md) |
| Prominent Disclosure | [User Data](https://support.google.com/googleplay/android-developer/answer/10144311) | [User Data](../user-data/user-data.zh-CN.md) |
| Account Deletion | [User Data：账号删除章节](https://support.google.com/googleplay/android-developer/answer/10144311#account_deletion)、[账号删除要求](https://support.google.com/googleplay/android-developer/answer/13327111) | [账号删除](../account-deletion/account-deletion.zh-CN.md) |
| Target API Level | [Target API 政策](https://support.google.com/googleplay/android-developer/answer/16561298)、[Target API 要求帮助页](https://support.google.com/googleplay/android-developer/answer/11926878) | [Target API 要求](../target-api/target-api-level.zh-CN.md) |
| Accessibility API | [敏感权限政策：无障碍 API 章节](https://support.google.com/googleplay/android-developer/answer/16558241#accessibility) | [敏感权限](../sensitive-permissions/sensitive-permissions.zh-CN.md) |
| Exact Alarm | [敏感权限政策：精确闹钟章节](https://support.google.com/googleplay/android-developer/answer/16558241#exact_alarm) | [敏感权限](../sensitive-permissions/sensitive-permissions.zh-CN.md) |
| Foreground Services | [前台服务声明](https://support.google.com/googleplay/android-developer/answer/13392821)、[敏感权限政策：前台服务章节](https://support.google.com/googleplay/android-developer/answer/16559646#foreground_service) | [前台服务与地理围栏](../foreground-services-and-geofencing/foreground-services-and-geofencing.zh-CN.md)、[权限申报](../permissions-declaration/permissions-declaration.zh-CN.md) |

## 与 2026-07-15 公告的关系及审查边界

公告把该技能列作开发者可选的工程工具；它把公告所列政策转成源码审查线索，尤其适合提早发现 Manifest 权限、调用点、Data safety 与审核登录信息之间的明显不一致。它不能替代政策原文、Play Console 申报、运行时测试、账号核验或人工判断；静态扫描的命中也不等于违规，未命中更不证明合规。

policies.json 是有限提示集合：上面 16 个模块及其 URL 不覆盖全部 Google Play 政策、地区要求、例外或所有应用运行路径。扫描器受支持扩展名、配置模式、输入材料和静态代码可见性约束。来源链接中的 Android 共享媒体存储页本轮仍为部分读取；其余 17 个唯一政策/实现目标在逐 URL 台账中为完整打开状态。有关签名、登录和 Data safety 的账号专属 Console 状态不能从公开商店页反推。

本次只审阅技能及其公开资源以建设政策知识库，没有对某个 Android 应用运行该自动审查工作流。

## 许可指向与未闭合范围

技能元数据写明许可文件名 LICENSE.txt；[技能目录内的相对 LICENSE.txt 路径](https://github.com/android/skills/blob/main/play/play-policy-insights/LICENSE.txt) 返回 404；仓库根目录的 [LICENSE.txt](https://github.com/android/skills/blob/main/LICENSE.txt) 则是 Apache License 2.0 全文。根许可证包含复制许可、保留声明、标记修改和免责声明等条件，但本次记录的是该仓库提供的许可文本；如需复制/再分发某个具体脚本或资源，应核对该文件适用范围、NOTICE 及文件头声明。

GitHub main 是可变分支；此页核验到的目录清单和正文是 2026-10-23 快照。代码脚本仅作模块级梳理，未进行逐行安全审计，也未穷举 GitHub 页面通用导航或整仓库其他 Skills。此技能属于工程辅助资料，不列入政策全文目录。
