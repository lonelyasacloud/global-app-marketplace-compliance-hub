---
id: google-play.policy-announcements
platform: google-play
language: zh-CN
authority: historical
status: current
kb_checked_at: 2026-10-24
review_due: 2027-01-24
regions: [global]
topics: [announcements, policy-history, deadlines]
snapshot_id: play.policy-announcements
snapshot_package: "GooglePlay-KnowledgeBase-2026-10-24-review.zip"
coverage_status: "announcement-digest"
source_url: "https://support.google.com/googleplay/android-developer/announcements/13412212?hl=en"
effective_date: "historical notices 2016-03 through 2026-07-15; four deadline rows effective 2027-01-27 are upcoming"
---

> **导入说明（Google batch 9）。** 正文来自已经分开的 2026-10-24 Google Play 知识库快照（`play.policy-announcements`，目录于 2026-10-24 复核）的改写公告汇编，不是官方公告的逐字副本。英文官方页面是效力来源。`kb_checked_at` 是快照记录的核对日；本次导入没有重新打开线上官方页面。文中“本知识库”“本库”“本地专题”等说法描述的是该快照库的覆盖范围，不是本仓库已经导入的页面。指向本仓库没有收录的专题、链接图、台账或 CSV 的相对链接改为文字提及。指向 Google batch 1–8 或本批八个专题的相对链接改为本仓库文件。Help 公告目录在 `hl=en` 复核，列出 1–58 项。公告 52 的英文路由仍返回 HTTP 429，其官方 `zh-Hans` 正文可读。快照没有记录公告 52 的完整 `hl=zh-CN` 正文，也没有记录每条公告中文路由的逐行对照。中文汇编是编辑改写。这些公告是历史材料。期限快照里于 2027-01-27 生效的四行是尚未生效的预告，不是现行规则。证据等级：公告为 Historical。期限行是指向现行期限页的 Operational 指针，不是第二份政策。

# Google Play 政策公告汇编

**公告目录复核日期：2026-10-24**  
**覆盖范围：** Google Play Developer Help「Announcements」当前目录正文编号为 1–58，本地索引收录 58/58 条；逐 URL 台账还记录 58/58 个对应公告页面正文已在至少一个官方语言路由完整打开并有人工摘要。公告 52 的英文路由仍返回 HTTP 429，但其官方 `zh-Hans` 正文可读。此项正文统计不表示所有正文子链接目标及其后代均已完整覆盖；本地保存改写摘要和来源链接，不是官方全文副本，也不涵盖 Play 可能存在的其他公告渠道。关联政策、帮助中心文章、课程和资源的子链状态见[公告子链接清单](../google-play-announcement-resources/google-play-announcement-resources.zh-CN.md)及递归链接图（快照：`google-play-policy-link-graph.md`，未导入本仓库）。最新一条公告为 2026-07-15，最早一条为 2016 年 3 月。

> **时效说明：** 这是历史公告索引。公告中的生效日、宽限期、试点资格、地区范围和政策措辞可能已变更；部分历史日期已经过去，部分要求可能有新的延长日期。判断当前是否合规时，请从 [Google Play 政策中心](https://play.google.com/about/developer-content-policy/) 和 [政策截止日期](https://support.google.com/googleplay/android-developer/table/12921780) 核实当前原文和日期。

逐条公告的正文子链接、用途分析和去重后的最佳实践汇总见[《政策公告子链接清单与分析》](../google-play-announcement-resources/google-play-announcement-resources.zh-CN.md)（[English](../google-play-announcement-resources/google-play-announcement-resources.zh-CN.md)）。

## 全部公告（新到旧）

1. **2026-07-15 — [Policy announcement](https://support.google.com/googleplay/android-developer/answer/17134731)**：针对未成年人收紧匿名/随机聊天要求，并禁止面向儿童的匿名聊天应用；READ_CALL_LOG 不再可用于电话验证，公告建议采用 Digital Credentials API、SMS Retriever 等替代方式；Play 应用须完成开发者验证注册。另澄清 EWA 贷款、第三方 AI 数据处理、内容分级和 Data safety 位置信息，并宣布部分政策开始逐步采用标准化编号。公告中“policies”直链实际指向功能/内容/体验政策页；该页当前有第 1、2 节编号，但没有提供跨政策统一编号目录。关联资源包括开发者验证与 Play Console 要求、PolicyBytes、Play Academy 隐私政策最佳实践和 Android Skills。
2. **2026-04-15 — [Policy announcement](https://support.google.com/googleplay/android-developer/answer/16926792)**：新增联系人权限和账户转移政策；低频/有限联系人访问应使用 Android Contact Picker，账户转移走 Play Console 官方流程；精确位置建议采用 location button，围栏场景改用 Geofence API；另澄清照片/视频权限、健康数据和约会功能的未成年人访问限制。关联资源包括 Health Connect 指南、新闻/杂志申报、预测市场试点（公告所列 2026-06-01 截止日已过）、PolicyBytes 与社区。
3. **2026-01-28 — [Policy announcement](https://support.google.com/googleplay/android-developer/answer/16797260)**：泰国个人贷款应用的商店页须披露服务提供方、最高利率和全部费用；同时在年龄限制政策中补充 matchmaking/dating 交叉链接。原文给出的存量应用截止日为 2026-03-04，现已过去。
4. **2025-12-09 — [Policy announcement](https://support.google.com/googleplay/android-developer/answer/16671517)**：美国合规调整，涉及 Payments 政策链接、符合条件开发者的替代计费计划，以及外部内容链接计划；公告中的 2026-01-28 截止日已过去。办理资格及流程应查看原文所链的计划条款。
5. **2025-11-19 — [Policy announcement](https://support.google.com/googleplay/android-developer/answer/16706838)**：Age Signals API 返回的数据仅可用于接收该数据的同一应用内的适龄体验；公告所述起始日期为 2026-01-01。
6. **2025-10-30 — [Policy announcement](https://support.google.com/googleplay/android-developer/answer/16550159)**：约会/配对及真钱博彩类功能须使用 Play Console 功能屏蔽未成年人；印度贷款应用须符合政府认可数字贷款应用名单；更新欧盟医疗器械应用指导、Accessibility API 禁止自主启动/规划/执行操作，以及订阅重要条款披露。另涉及 180 天账号终止申诉期、金融功能申报、开发者验证、Play Policy Insights 和政策「Do/Don't」摘要。
7. **2025-07-10 — [Policy announcement](https://support.google.com/googleplay/android-developer/answer/16296680)**：个人贷款短期例外限于巴基斯坦且须遵守当地法规；补充加密货币交易所/软件钱包地区要求、Android 16 健康权限说明、AI 生成内容安全实践、内容分级与广告年龄适配、冒充政策 FAQ。附有 Android SDK Upgrade Assistant、Policy Insights Canary 版及新闻/杂志、Target API 的当年截止日（均已过）。
8. **2025-06-24 — [PolicyBytes: Your video guide to Google Play policies](https://support.google.com/googleplay/android-developer/answer/16321613)**：介绍由 Google Play 团队成员讲解近期政策的 PolicyBytes 视频系列及 PolicyBytes Hub；作为详细书面政策的学习补充，并列出 2024、2025 集数。
9. **2025-04-10 — [Policy announcement](https://support.google.com/googleplay/android-developer/answer/15899442)**：News 政策覆盖新闻与杂志应用并更新申报，Personal Loans 纳入信用额度应用；澄清 manipulated media、联系人默认处理器、Data safety「分享」定义、EWA 与个人贷款区分、Android ID、数据保护框架及金融应用短信权限。重申照片/视频访问须与功能直接相关；社交/约会应用需完成儿童安全标准自我认证，并推荐 Tech Coalition CSEA 最佳实践。公告中的 2025-05-28 等日期已过。
10. **2025-03-05 — [Policy announcement](https://support.google.com/googleplay/android-developer/answer/15931464)**：加强 Health Connect 敏感健康记录保护；访问资格须有正当用途，申请时要说明具体数据类型及用户收益，并遵守更严格的数据共享、使用和同意要求。原文链接到 Health Connect 常见问题。
11. **2025-02-10 — [Helpful tips for white label developers](https://support.google.com/googleplay/android-developer/answer/15931448)**：面向白标/模板应用发布者，重点推荐分散式账号管理以隔离单应用违规风险；各应用须有独特、准确的商店资料；提交前做基本质量和政策检查；准备可用审核凭证、审查期间冻结改动、关注 Policy status、预留审核时间并考虑 Managed Publishing。2026-10-23 重核目标指南的 11 个正文文本链接和 4 个示例图片目标；逐项状态见[公告子链表](../google-play-announcement-resources/google-play-announcement-resources.zh-CN.md)及递归图 §4.122（快照：`google-play-policy-link-graph.md`，未导入本仓库）。
12. **2025-01-22 — [Required actions for Photo & Video Permissions](https://support.google.com/googleplay/android-developer/answer/15800983)**：提醒持有 READ_MEDIA_IMAGES/READ_MEDIA_VIDEO 的应用按核心功能申报确有必要的广泛访问，或移除权限并使用系统照片选择器；也曾提供延期选项。原文截止日已过，应按当前权限政策复核。
13. **2024-12-19 — [Google Play Developer Help Community](https://support.google.com/googleplay/android-developer/answer/15750244)**：介绍开发者帮助社区，可咨询发布、技术和政策问题，获取 Google 产品专家及开发者建议、最佳实践和政策动态；原文说明可订阅精选帖子通知。
14. **2024-10-30 — [Policy announcement](https://support.google.com/googleplay/android-developer/answer/15444680)**：扩展医疗功能政策并归并健康相关政策；澄清第三方 SDK 责任、健康数据隐私和 Health Connect 受监管设备同意要求。社交/约会应用儿童安全自我认证和照片/视频权限节点曾有 2025 截止日；附 Tech Coalition 儿童性剥削与虐待防治实践资源。
15. **2024-08-28 — [Helpful tips to get your app published on Google Play](https://support.google.com/googleplay/android-developer/answer/15327688)**：发布指南索引。下方汇总该帮助文档的核心实操：清楚准确地描述应用、让实际功能兑现商店承诺、提供审核登录凭证、全面测试并利用测试轨道，拒审后修复问题再提交。
16. **2024-07-17 — [Policy announcement](https://support.google.com/googleplay/android-developer/answer/14993590)**：金融、健康、VPN 和政府服务开发者账号需采用 Organization 类型；另更新 Spam 与 Minimum Functionality 等政策。新账号先行，既有账号随后迁移；具体主体及时间以原文/当前 Play Console 提示为准。
17. **2024-04-03 — [Policy announcement](https://support.google.com/googleplay/android-developer/answer/14594990)**：新增社交/约会应用儿童安全标准自我认证及健康应用申报；更新书籍/视频目录性内容、被操纵媒体（纳入音频）、贷款期限、Play Asset Delivery 的 dataSync 前台服务例外和 Health Connect 申报。并澄清暴力极端主义、间谍软件、贷款敏感权限、QUERY_ALL_PACKAGES、Play Protect 和 Maskware。包含账户删除、照片/视频权限历史截止日期。
18. **2024-03-06 — [Policy announcement](https://support.google.com/googleplay/android-developer/answer/14631918)**：依欧盟《数字市场法》更新 EEA 付款政策，允许符合条件的外部优惠链接并扩大替代计费范围；附 EEA 一般访问条件、项目加入要求与法规说明。
19. **2023-10-25 — [Policy announcement](https://support.google.com/googleplay/android-developer/answer/14016515)**：生成式 AI 应用须遵守全部 Play 政策，部分应用需提供举报/标记功能；引入照片/视频广泛权限限制、Android 14 全屏意图权限要求和健康应用政策；并更新儿童广告识别、UGC 审核、泰国贷款证明等。提醒 Play Billing Library 5 的历史迁移节点。
20. **2023-07-12 — [Policy announcement](https://support.google.com/googleplay/android-developer/answer/13678785)**：设备端 Android 容器须遵循 REQUIRE_SECURE_ENV；区块链数字内容应用要申报，NFT 游戏化须满足透明度/安全要求；明确禁止非透明行为及规避审核；还涉及开发者验证、金融功能申报、儿童 SDK、安装包权限、VPN 广告欺诈和日本线上抓娃娃试点结束。
21. **2023-06-29 — [Keeping Google Play safe for users and developers](https://support.google.com/googleplay/android-developer/answer/13721042)**：介绍 Play 结合机器学习检测、人工审核、违规移除和开发者教育维护生态安全，并链接 PolicyBytes、网络研讨会、博客及政策更新。
22. **2023-04-05 — [Policy announcement](https://support.google.com/googleplay/android-developer/answer/13411745)**：允许创建账号的应用提供应用内和网页端账号删除请求，并更新 Data safety 表单；Android 14 前台服务和 JobScheduler 数据传输要求；还涉及 Families、巴基斯坦个人贷款、激励安装、SDK 安全（含 Play Academy SDK Best Practices）、色情内容、Target API 和 VPN 等。
23. **2023-02-22 — [Policy announcement](https://support.google.com/googleplay/android-developer/answer/14551113)**：因印度监管发展，开发者可在 Play 分发的手机/平板应用内购买中，于 Play Billing 旁提供替代计费。2026-10-22 重开公告并追到现行 Payments policy、印度地区要求及新费率时间表。印度专属路径与全球 Billing choice 入组范围不同；手工报告迁移状态要以 Console 当前条款核对，详见[公告子链接分析](../google-play-announcement-resources/google-play-announcement-resources.zh-CN.md)。
24. **2022-12-14 — [Policy announcement](https://support.google.com/googleplay/android-developer/answer/14552018)**：说明 Target API Level 政策例外，包括永久私有应用，以及与汽车/穿戴形态打包的应用；公告称这是澄清而非新执法标准。
25. **2022-11-16 — [Policy announcement](https://support.google.com/googleplay/android-developer/answer/14550832)**：肯尼亚和尼日利亚个人贷款应用需提交申报和证明文件；禁止广告模拟应用界面；儿童广告只能使用 Families 自认证 SDK 版本；强调开发者对端到端用户数据处理负责。
26. **2022-11-02 — [Policy announcement](https://support.google.com/googleplay/android-developer/answer/14554246)**：真钱游戏试点细节从主政策移至帮助中心。现行试点概览（2026-06-04 生效）称无活跃试点；印度 DFS/Rummy 过渡期 2026-01-22 到期、墨西哥 DFS 试点 2026-06-04 结束。见[公告子链接分析](../google-play-announcement-resources/google-play-announcement-resources.zh-CN.md)。
27. **2022-09-07 — [Policy announcement](https://support.google.com/googleplay/android-developer/answer/14554741)**：公告启动印度注册公司开发者参与的 DFS 与 Rummy 限时试点。试点 2023-09-28 结束，过渡期于 2026-01-22 到期；该历史公告不再授权印度真钱功能。
28. **2022-07-27 — [Policy announcement](https://support.google.com/googleplay/android-developer/answer/14554661)**：更新插屏广告体验（参考 Better Ads Standards）、FLAG_SECURE、VpnService 核心用途、精确闹钟权限；并澄清健康误导信息、订阅取消、stalkerware 标识、儿童广告、广告 ID、重复广告、隐私政策可访问性和敏感事件等。
29. **2022-05-11 — [Policy announcement](https://support.google.com/googleplay/android-developer/answer/14554740)**：新增 Health Connect 权限政策，并将 Health Connect 数据纳入 User Data 中的个人及敏感数据类别；另有 Android 开发者健康数据接入说明。
30. **2022-04-06 — [Policy announcement](https://support.google.com/googleplay/android-developer/answer/14554743)**：更新 Families 区域可用性；启动日本线上抓娃娃试点；引入 Request Install Packages 权限政策并扩展 Target API 规则至未更新的既有应用；另含菲律宾、印度、印尼贷款、仇恨言论、血氧仪、儿童广告 SDK、Accessibility API、新闻与 UGC 等更新。
31. **2021-12-15 — [Policy announcement](https://support.google.com/googleplay/android-developer/answer/14555045)**：澄清订阅须在整个订阅期持续或周期性提供价值，不能将一次性权益伪装成订阅。
32. **2021-11-18 — [Policy announcement](https://support.google.com/googleplay/android-developer/answer/14554574)**：为响应韩国法规，允许符合条件的韩国手机和平板应用购买使用替代应用内计费系统。
33. **2021-10-27 — [Policy announcement](https://support.google.com/googleplay/android-developer/answer/14554575)**：禁止与针对平民暴力有关的危险组织应用；增加地区性执法/内容适用范围；新增 hostile downloader、儿童社交应用安全要求及 Android Emoji 政策；并澄清儿童广告和诱导购买等。
34. **2021-07-28 — [Policy announcement](https://support.google.com/googleplay/android-developer/answer/14554513)**：预告 App Set ID 的受限用途、儿童标识符限制、长期不活跃开发者账号关闭、运行时解释代码和 Accessibility API 规则；同时涉及 Data safety/隐私政策、贷款、商店元数据、广告 ID、新闻和审核登录资料。
35. **2021-03-31 — [Policy announcement](https://support.google.com/googleplay/android-developer/answer/14554804)**：更新 Android 11 全文件访问权限、真钱博彩地区与忠诚度计划、性内容、Families 功能、新闻、恶意软件/stalkerware、误导性声明、支付政策常见问题、COVID-19 状态应用、Families 广告和 QUERY_ALL_PACKAGES。
36. **2020-11-11 — [Policy announcement](https://support.google.com/googleplay/android-developer/answer/14554899)**：补充 CRM 与默认处理器对 SMS/通话记录数据的可接受用途、高风险应用覆盖和欧盟/英国数据传输条款；亦涉及新闻、社交工程、敏感事件、垃圾内容及后台位置权限申报。
37. **2020-09-28 — [Policy announcement](https://support.google.com/googleplay/android-developer/answer/14555207)**：澄清何时须使用 Google Play 计费系统；公告曾设新应用和既有替代计费应用不同过渡期，这些日期已过。当前支付方案以现行政策和计划资格为准。
38. **2020-09-16 — [Policy announcement](https://support.google.com/googleplay/android-developer/answer/14554576)**：澄清协同行为不得隐瞒应用/内容来源；允许巴西政府发布的真钱博彩应用，并修正 stalkerware 政策文字。
39. **2020-07-08 — [Policy announcement](https://support.google.com/googleplay/android-developer/answer/14555135)**：新增 Android R 应用广泛存储访问和申报审查要求，推出新闻应用政策，并更新儿童广告、个人贷款、订阅、恶意软件、权限/数据和地区博彩等内容。
40. **2020-04-16 — [Policy announcement](https://support.google.com/googleplay/android-developer/answer/14554577)**：更新功能欺骗与准确披露、下载大资源文件前通知、被操纵媒体、恶意软件、订阅、Families 和儿童广告等政策；附 Google Play Protect 恶意软件说明。
41. **2020-01-28 — [Policy announcement](https://support.google.com/googleplay/android-developer/answer/14555134)**：扩大允许发布持牌真钱博彩应用的国家，并新增 gamified loyalty 计划要求及示例；地区牌照和当前国家名单需以现行政策为准。
42. **2019-11 — [Policy announcement](https://support.google.com/googleplay/android-developer/answer/14554806)**：更新医疗、健康和政府服务应用的误导性声明政策、准确元数据、广告 SDK/网络认证、虚拟货币、垃圾内容及最低功能要求。
43. **2019-08 — [Policy announcement](https://support.google.com/googleplay/android-developer/answer/14555136)**：补充第三方代理服务、个人贷款剥削性条款及可能干扰选举的欺骗性内容示例。
44. **2019-05 — [Policy announcement](https://support.google.com/googleplay/android-developer/answer/14554978)**：新增 Families 与儿童广告网络认证政策；更新性内容、仇恨言论、大麻/烟草/酒精、盲盒赔率、博彩、UGC 变现、最低功能和假冒商品政策。
45. **2019-01 — [Policy announcement](https://support.google.com/googleplay/android-developer/answer/14555047)**：禁止推广/销售未获批准物质，并为敏感事件、欺凌与骚扰政策补充示例。
46. **2018-10 — [Policy announcement](https://support.google.com/googleplay/android-developer/answer/14554578)**：澄清监控/商业间谍软件、Designed for Families 及儿童定向声明；更新 User Data、Permissions、SMS/通话记录、联系人数据和执法说明。
47. **2018-07 — [Policy announcement](https://support.google.com/googleplay/android-developer/answer/14554516)**：强调儿童应用成人主题限制；新增危险产品销售和加密货币挖矿政策；禁止重复内容、以广告为主要用途的应用，并更新暴力和误导政策。
48. **2018-04 — [Policy announcement](https://support.google.com/googleplay/android-developer/answer/14554517)**：澄清儿童安全、仇恨言论、暴力及 UGC；新增二元期权和每日梦幻体育要求，并更新不诚实行为、恶意行为、元数据和 Families 资格。
49. **2017-11 — [Policy announcement](https://support.google.com/googleplay/android-developer/answer/14554746)**：更新锁屏变现、不评级应用的内容分级，以及 Designed for Families 要求。
50. **2017-10 — [Policy announcement](https://support.google.com/googleplay/android-developer/answer/14554518)**：澄清博彩地域限制、应用最低功能、导览类应用限制，以及权限请求的时机和方式。
51. **2017-08 — [Policy announcement](https://support.google.com/googleplay/android-developer/answer/14554663)**：新增博彩应用政策；扩展 User Data 突出披露指导；调整 Android Instant Apps 与内容分级的政策目录位置。Instant Apps 项目已于 2025-12 停用，旧要求见[历史专题](../android-instant-apps/android-instant-apps.zh-CN.md)。
52. **2017-06 — [Policy announcement](https://support.google.com/googleplay/android-developer/answer/14554580)**：公告称新增 EU–U.S. Privacy Shield 数据保护指引。本轮从 `zh-Hans` 路由读取到完整短正文，唯一政策链接指向旧 User Data 路由；英文路由仍为 HTTP 429。Privacy Shield 后来失效；见[公告子链接分析](../google-play-announcement-resources/google-play-announcement-resources.zh-CN.md)和[用户数据外部参考专题](../user-data-policy-references/user-data-policy-references.zh-CN.md)。
53. **2017-05 — [Policy announcement](https://support.google.com/googleplay/android-developer/answer/14555048)**：澄清恶意行为/下载可执行代码、激励安装和 Android Instant Apps 历史要求；另附「10 tips to help you stay on the right side of Google Play policy」视频。Instant Apps 已于 2025-12 停用，见[历史专题](../android-instant-apps/android-instant-apps.zh-CN.md)。
54. **2017-04 — [Policy announcement](https://support.google.com/googleplay/android-developer/answer/14554664)**：澄清 Designed for Families 项目资格，新增 AR/VR 资格标准及 Play Console 儿童定向声明要求。
55. **2016-10 — [Policy announcement](https://support.google.com/googleplay/android-developer/answer/14554809)**：更新 Metadata 政策示例以提高说明清晰度。
56. **2016-07 — [Policy announcement](https://support.google.com/googleplay/android-developer/answer/14554665)**：建立 Families 政策目录入口；澄清隐私披露位置、露骨性服务、博彩广告、UGC 最低安全功能、欺骗行为和暴力示例。
57. **2016-05 — [Policy announcement](https://support.google.com/googleplay/android-developer/answer/14555208)**：在 Payments 政策部分加入 Android Pay 相关信息。
58. **2016-03 — [Policy announcement](https://support.google.com/googleplay/android-developer/answer/14554666)**：更新不当广告、Doze/App Standby、干扰系统功能的广告和用户数据政策，并上线 Developer Policy Center。

## 当前截止日期快照（2026-10-23）

根据 [Policy Deadlines](https://support.google.com/googleplay/android-developer/table/12921780) 于 2026-10-23 显示的信息：仍有 8 行，其中 4 行已过期、4 行集中于 2027-01-27。

| 截止日期 | 状态 / 要求 |
| --- | --- |
| 2026-08-26 | **已过：** 匿名/随机聊天应用的年龄限制、儿童安全标准和 Families 政策更新。 |
| 2026-09-30 | **已过：** 为符合 Android 开发者验证要求，在 Play Console 注册 Play 应用包名。 |
| 2027-01-27 | **尚未到期：** Contacts Permissions、Location Permissions、SMS/Call Log Permissions，以及从前台服务地理围栏用例转用 Geofence API。 |

截止日期页会持续更新，旧于三个月的项目还可能移入 Policy Archive；实施前务必重新查看页面与 Play Console 提示。

## 公告中的最佳实践与实操子链接

以下资料在公告中被明确推荐，或是公告链接链路中的直接操作指南。应按各自适用范围使用；政策条文本身优先于指南摘要。

### 发布、白标和商店资料

- [Best Practices for White Label Developers](https://support.google.com/googleplay/android-developer/answer/15884185)：Google 强烈推荐按客户或客户组分散账号（managed 或 unmanaged），但不是所有应用的普遍账号硬性要求；各模板应用应有独特商店资料、准确可复现的功能说明、合适截图及目标受众披露。审核通常在 7 天内完成但可能更久；Managed publishing 可控制已上架应用更新的获批发布时间，不适用于首次发布。见[完整 11 个正文文本链接与 4 个图片资产清单](../google-play-announcement-resources/google-play-announcement-resources.zh-CN.md)。
- [Helpful tips to get your app published on Google Play](https://support.google.com/googleplay/android-developer/answer/15191715)：描述应用的价值和实际功能；确保标题、说明、截图与应用相符；给审核人员提供有效登录凭证；检查安装、加载、稳定性并通过测试轨道收集反馈；拒审后修复根因、充分测试再重新提交。
- [Best practices for your store listing](https://support.google.com/googleplay/android-developer/answer/13393723)：元数据应简洁、准确、原创，避免关键词堆砌、无来源用户评价、误导排名/折扣/关系声明；图标、截图、视频需反映实际功能，适配各设备与支持语言。页面还链接到应用说明、商店图像和 Play Academy 课程。
- [Play Console Requirements](https://support.google.com/googleplay/android-developer/answer/10788890)：公告及白标指南均指向此处，尤其是审核受登录墙保护的功能时，需提供可用账号、访问说明及审核所需资源。实操细节见 [Requirements for providing sign in details for review](https://support.google.com/googleplay/android-developer/answer/15748846)。

### AI、儿童安全、隐私和 SDK

- [Best Practices to Safeguard AI-Generated Content](https://support.google.com/googleplay/android-developer/answer/16353813)：生成式 AI 开发者仍对输出负责；应防止违规/有害内容，可采用输入输出过滤器与分类器，并按行业标准做安全测试和红队测试。指南链接 Google Secure AI Framework (SAIF)、OWASP GenAI Red Teaming Guide 及多家模型提供方安全资源。
- [Developer good practices: Combating online child sexual exploitation and abuse](https://technologycoalition.org/resources/developer-good-practices-combating-online-child-sexual-exploitation-and-abuse/)：Tech Coalition 提供的儿童性剥削与虐待防治实践，覆盖公开服务条款/社区准则、内部识别与处置流程等。与 Play Child Safety Standards 自我认证一并阅读。
- [Build user trust with an accurate privacy policy](https://playacademy.exceedlms.com/student/activity/1961002-build-user-trust-with-an-accurate-privacy-policy)：公告引用的 Play Academy 视频课程；公开简介指向 Data safety 表单提交前的核对，课程页标注 2026-06-18、2 分钟、Beginner。视频需登录；政策义务仍以 User Data 和 Data safety 正文为准。
- [Play Academy: SDK Best Practices](https://g.co/playacademy/sdkbestpractices)：2023 公告推荐的 SDK 安全学习课程；同时阅读 [SDK Requirements](https://support.google.com/googleplay/android-developer/answer/13323374)，应用开发者仍须对整合的第三方 SDK 数据行为负责。

### 政策学习和开发期检查

- [PolicyBytes Hub](https://support.google.com/googleplay/android-developer/answer/16373081)：Google Play 团队成员讲解政策更新的视频索引，用于快速理解公告背景；最终核对政策正文和日期。
- [Google Play Developer Help Community](https://support.google.com/googleplay/android-developer/community)：提问、查找常见政策/发布问题，并与其他开发者和产品专家交流经验。
- [Android Skills — Google Play policy skill](https://github.com/android/skills)：2026 年 7 月公告推荐的开源工具，可将 Google Play 政策作为上下文，在 IDE/CLI 中辅助审查代码；自动化结果是预检，不能替代政策原文或 Play 审核决定。
- [Play Policy Insights](https://developer.android.com/studio/publish/insights)：Android Studio 中的政策提示工具；可显示政策概览、常见注意事项和政策链接，适合提交前发现潜在问题。它不覆盖所有政策，也不代替正式审核决定。
- [Google Play Developer Policy Center](https://play.google.com/about/developer-content-policy/) 与 [Policy Deadlines](https://support.google.com/googleplay/android-developer/table/12921780)：用于最终检查现行政策和截止日期；公告摘要、视频或课程不应作为唯一合规依据。

## 维护记录

- 目录来源：[Google Play Developer Help — Announcements](https://support.google.com/googleplay/android-developer/announcements/13412212?hl=en)。2026-10-24 重开后，页面列出 1–58 共 58 项，最早为 2016-03、最新为 2026-07-15；本地索引条目数与目录项数相符。此为清单覆盖核对，正文/后代覆盖仍按逐页审计状态判断。
- 为避免历史信息被误作当前规则，固定日期、区域计划和试点仅按公告原意记录；每次实际发布前应重新打开对应政策、帮助文章和 Play Console 表单确认。
- 后续维护时重新计数目录条目，补齐新增公告，并同步更新英文版 [google-play-policy-announcements-en.md](../google-play-policy-announcements/google-play-policy-announcements.zh-CN.md)。
- 本项目的相关条目：[Google Play 开发者政策中心](../google-play-developer-policy-center/google-play-developer-policy-center.zh-CN.md)、[Play Console 要求](../play-console-requirements/play-console-requirements.zh-CN.md) 和 [Android 开发者验证](../android-developer-verification/android-developer-verification.zh-CN.md)。
