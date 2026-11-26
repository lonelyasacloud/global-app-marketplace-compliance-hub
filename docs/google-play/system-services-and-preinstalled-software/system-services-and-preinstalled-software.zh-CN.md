---
id: google-play.system-services-and-preinstalled-software
platform: google-play
language: zh-CN
authority: operational
status: current
kb_checked_at: 2026-10-22
review_due: 2027-01-22
regions: [global]
topics: [system-services, preinstalled, OEM, carrier, SoC, exemption]
snapshot_id: play.system-services
snapshot_package: "GooglePlay-KnowledgeBase-2026-10-24-review.zip"
coverage_status: "detailed-summary"
source_url: "https://support.google.com/googleplay/android-developer/answer/12085265?hl=zh-CN"
source_url_partner_center: "https://docs.partner.android.com/partners/guides/system-services"
source_url_en: "https://support.google.com/googleplay/android-developer/answer/12085265?hl=en"
effective_date: "public eligibility pointer only; Partner Center criteria were not readable; no 2027-01-27"
---

# Google Play 系统服务与预装软件豁免入口

> **导入说明（Google batch 8）。** 正文来自已经分开的 2026-10-24 Google Play 知识库快照（`play.system-services`，核对日 2026-10-22）的改写摘要，不是官方页面的逐字副本。英文官方页面是效力来源。`kb_checked_at` 是快照源文件记录的核对日；本次导入没有重新打开线上官方页面。文中“本知识库”“本库”“本地专题”等说法描述的是该快照库的覆盖范围，不是本仓库已经导入的页面。指向本仓库没有收录的专题、链接图、台账或 CSV 的相对链接改为文字提及。指向 Google batch 1–7 或本批十三个专题的相对链接改为本仓库文件。核对日 2026-10-22。中文文件把帮助 URL 记为 `hl=zh-CN`。快照没有记录该路由抓取失败，也没有记录与英文的逐行对照。中文是对这篇短公开页面的编辑改写。Partner Center 指南返回缓存未命中并需要合作伙伴访问，因此不记录内部资格条件。帮助社区返回缓存未命中。联系支持遇到反自动化页面。这些访问限制不是一项豁免。没有 2027-01-27。公开页点名的是有预装或捆绑软件的运营商、SoC 供应商和 OEM。它不是普通第三方应用的通用豁免，也不替代 Managed Google Play 私有应用、Android 开发者验证或目标 API 要求。证据等级：Operational。

**核对日期：2026-10-22。** 公开帮助页正文很短，本专题覆盖其全部公开政策说明，并记录它链接到的 Partner Center 页面及其访问边界；不把不可见的合作伙伴规则补写成公开要求。

## 公开说明的范围

Google 将 System services 描述为**支持系统核心功能的预装软件**。公开页点名的潜在申请主体是运营商、System on a Chip（SoC）供应商和原始设备制造商（OEM）；这些主体若有预装或捆绑应用，可以登录 Partner Center 查看资格细节，并判断软件是否符合 System services 条件、是否可申请豁免。

| 可从公开页面确认 | 不应据此推定 |
| --- | --- |
| 该分类针对预装软件，且须支持系统核心功能。 | 仅因应用出厂预装、由运营商/OEM提供或安装量高，就自动成为系统服务。 |
| 公开页面列出运营商、SoC 供应商、OEM 作为可登录 Partner Center 核验资格的角色。 | 普通第三方开发者可以直接使用同一豁免，或任何预装应用都会获批。 |
| 页面说明可通过 Partner Center 查看细节并申请豁免。 | 豁免适用哪条具体 Play 规则、包名/版本范围、审批材料、续期方式或批准期限；公开正文没有说明这些细节。 |

**实务边界：** 把它视为需由合格平台伙伴在 Partner Center 核验的专门资格路径，而不是应用商店一般豁免。公开页面没有列出资格测试清单，也没有说明获批后对开发者计划政策、目标 API、数据安全、付款或其他政策的整体影响；不能从“申请豁免”推导为免除其他规则。

## 相关路径不可混为一谈

| 路径 | 作用范围 | 与 System services 的区别 |
| --- | --- | --- |
| System services | 运营商、SoC 供应商、OEM 核验预装/捆绑软件是否属于支持核心系统功能的软件，并在适用时申请特定豁免。 | 资格规则在 Partner Center；公开 Help 页未公开申请条件。 |
| [Managed Google Play 私有应用](../play-console-requirements/play-console-requirements.zh-CN.md) | 仅向指定组织提供应用的发布和分发方式。 | 组织可见性或 EMM 发布方式不等于系统服务资格。 |
| [Android 开发者验证](../android-developer-verification/android-developer-verification.zh-CN.md) | 开发者身份及包名验证要求。 | 其受管理设备/私有应用范围与目标 API 的永久私有应用例外也应分别判断，不替代 Partner Center 的系统服务审核。 |
| [目标 API 要求](../target-api/target-api-level.zh-CN.md) | Play 对新应用、更新和旧应用可发现性的 target API 门槛及例外。 | 即使可能存在某项豁免，须由官方资格/账号状态确认；不能从系统服务定义推导出目标 API 豁免。 |

## 正文直接链接与核验状态

| 目标 | 正文中的作用 | 核验状态 |
| --- | --- | --- |
| [Partner Center：System services 指南](https://docs.partner.android.com/partners/guides/system-services) | 公开 Help 页要求有相应权限的主体登录并查阅资格细节。 | 本轮请求返回 cache miss，且目标提示合作伙伴访问；正文和后代无法公开核验，因此不记录其内部条件。 |
| [Policy education and app requirements 索引](https://support.google.com/googleplay/android-developer/topic/12798386?hl=en) | Help Center 侧栏展示的 32 项关联学习/政策入口。 | 已在递归链接图（快照：`../google-play-policy-link-graph.md`，未导入本仓库）逐项登记；这是共享导航，不是 System services 正文列出的 32 项资格义务。 |
| [Help Community](https://support.google.com/googleplay/android-developer/community?help_center_link=CJHQ4QUSD1N5c3RlbSBzZXJ2aWNlcw&hl=en) | 社区讨论入口。 | 点击后 cache miss；社区帖子不是官方资格规则。 |
| [联系 Play 支持](https://support.google.com/googleplay/android-developer/gethelp) | 支持/账号入口。 | 重定向到反自动化验证页；须从有权限的 Play Console 或 Partner Center 账户确认当前联系路径。 |

## 资格核验清单

- [ ] 确认申请方是公开页面列出的运营商、SoC 供应商或 OEM，并能使用相应 Partner Center 权限。
- [ ] 在 Partner Center 核对软件是否预装/捆绑，以及是否支持系统核心功能；公开 Help 页没有提供可代替该核验的自动规则。
- [ ] 由 Partner Center 当前说明确认豁免针对的政策条款、应用包名、版本、材料、有效期和更新/申诉流程。
- [ ] 保存官方资格判断/批准状态，并逐项核对其他仍适用于应用的 Play 要求；本页面不构成豁免批准。

## 来源与相关专题

- [Google Play System services Help](https://support.google.com/googleplay/android-developer/answer/12085265?hl=en)
- [Partner Center system-services guide](https://docs.partner.android.com/partners/guides/system-services)（合作伙伴访问）
- [Play Console 要求](../play-console-requirements/play-console-requirements.zh-CN.md) · [Android 开发者验证](../android-developer-verification/android-developer-verification.zh-CN.md) · [目标 API 要求](../target-api/target-api-level.zh-CN.md)
