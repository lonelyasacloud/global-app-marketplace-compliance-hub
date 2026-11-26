---
id: google-play.android-emoji-support
platform: google-play
language: zh-CN
authority: normative
status: current
kb_checked_at: 2026-10-22
review_due: 2027-01-22
regions: [global]
topics: [emoji, unicode, android, accessibility, compatibility]
snapshot_id: play.android-emoji
snapshot_package: "GooglePlay-KnowledgeBase-2026-10-24-review.zip"
coverage_status: "detailed-summary"
source_url: "https://support.google.com/googleplay/android-developer/answer/11190644?hl=zh-CN"
source_url_unicode_index: "https://www.unicode.org/emoji/techindex.html"
source_url_unicode_charts: "https://www.unicode.org/emoji/charts/"
source_url_unicode_standard: "https://www.unicode.org/reports/tr51/"
source_url_android_guide: "https://developer.android.com/develop/ui/views/text-and-emoji/emoji2"
source_url_en: "https://support.google.com/googleplay/android-developer/answer/11190644?hl=en"
effective_date: "current Play emoji rule for Android 12+; derived four-month reminder around 2026-12-28 is not an account deadline and is not 2027-01-27"
---

# Google Play Android Emoji 支持政策

> **导入说明（Google batch 8）。** 正文来自已经分开的 2026-10-24 Google Play 知识库快照（`play.android-emoji`，核对日 2026-10-22）的改写摘要，不是官方页面的逐字副本。英文官方页面是效力来源。`kb_checked_at` 是快照源文件记录的核对日；本次导入没有重新打开线上官方页面。文中“本知识库”“本库”“本地专题”等说法描述的是该快照库的覆盖范围，不是本仓库已经导入的页面。指向本仓库没有收录的专题、链接图、台账或 CSV 的相对链接改为文字提及。指向 Google batch 1–7 或本批十三个专题的相对链接改为本仓库文件。核对日 2026-10-22。中文文件把政策 URL 记为 `hl=zh-CN`。快照没有记录对该中文官方页的逐行核对，也没有记录该路由抓取失败。中文是编辑改写。Unicode 图表和 UTS #51 以英文打开。Play 规则要求 Android 12+ 支持最新 Unicode Emoji；自定义实现须在新版本发布后四个月内完成。UTS #51 把 Unicode Emoji 18.0 标为 2026-08-28。由此推算的四个月窗口大约落在 2026-12-28。这是推导出的提醒，不是账号专属 Play 截止日，也不是 2027-01-27。Emoji2 指南标注 2026-10-16 更新，是实现说明。它的示例停在 Unicode 16.0，并不降低 Play 要求。证据等级：Play Emoji 政策为 Normative；Android Emoji2 为实现说明；Unicode 是“最新 Unicode Emoji”的标准来源。

**核对日期：2026-10-22。** Google Play 的 Android Emoji 政策要求所有运行 Android 12 或更高版本的应用支持最新 Unicode Emoji。采用 Android 默认 Emoji、没有自定义实现的应用，在 Android 12+ 上自动获得最新版本支持；使用自定义 Emoji 实现（包括第三方库）的应用，须在 Unicode 发布新 Emoji 后四个月内完整支持该版本。

## Play 政策要求

- **Android 12+：**所有应用都须支持最新 Unicode Emoji。使用平台默认字体/实现的应用通常已满足；自行替换或封装 Emoji 字体、渲染或输入实现的应用须评估兼容性。
- **自定义实现：**政策明确把第三方库也纳入自定义实现范围；应在每次 Unicode Emoji 新版发布后更新，并在四个月窗口内完成支持。不要把旧公告、旧 SDK 示例或设备系统版本误作永久豁免。
- **时间点推算：**Unicode Emoji 18.0 的 UTS #51 版本日期为 2026-08-28。若该日期适用于 Play 页面所说的“新版 Emoji 发布日”，四个月窗口约在 **2026-12-28** 到期；这是根据官方日期和政策文字推算的提醒日期，不是 Play 对某个应用的账号级截止通知。

## Android 实现与测试建议

Google 的 [Android Emoji2 指南](https://developer.android.com/develop/ui/views/text-and-emoji/emoji2)解释了系统 Emoji 字体、EmojiCompat 和兼容实现。Android 11（API 30）及更早版本无法通过系统字体更新自动获得新版 Emoji；使用 `androidx.emoji2`、AppCompat 或 Compose 的兼容路径，可以为旧系统提供更新的字形和序列支持。自定义文字控件也应检查组合字符是否由 EmojiCompat 处理。

发布前应在目标 Android 版本、Android 11 及更早系统上测试带肤色修饰符、ZWJ 组合序列、地区旗帜和新版本字符，确认没有出现方框（tofu）、拆分字形、错误顺序或不可输入情况。用 [Unicode Emoji 图表](https://www.unicode.org/emoji/charts/)和 [UTS #51](https://www.unicode.org/reports/tr51/)当前版本选取测试样本；技术页面的示例清单不一定随着 Unicode 最新版本同步更新。

## 直接子链接与关系

| 来源页 | 目标页 | 摘要/核验状态 |
| --- | --- | --- |
| Google Play Android Emoji Policy | [Unicode Emoji 技术索引](https://www.unicode.org/emoji/techindex.html) | 已打开。它将 Emoji 图表、UTS #51、数据文件、提案和常见问题作为规范资源入口。 |
| Unicode Emoji 技术索引 | [Unicode Emoji 图表](https://www.unicode.org/emoji/charts/) | 已打开；当前显示 Emoji v18.0，并列出字符/序列、版本、展示样式及排序图表。图表是动态页面，生产测试应查看对应的当前数据文件。 |
| Unicode Emoji 技术索引 | [UTS #51：Unicode Emoji](https://www.unicode.org/reports/tr51/) | 已打开；v18.0，日期 2026-08-28。定义 Emoji 字符/序列、呈现、修饰符及跨平台互操作指导，是解释“最新 Unicode Emoji”的标准来源。其大量章节表格和引用不属于 Play 义务，未逐条展开。 |
| Google Play Android Emoji Policy | [Android：Support modern emoji](https://developer.android.com/develop/ui/views/text-and-emoji/emoji2) | 已打开；说明 Emoji2、AppCompat、Compose、旧版 Android 回退、自定义视图及测试方法，页面最后更新 2026-10-16。该页列举的测试样例止于 Unicode 16.0，而 Unicode 标准页已更新至 18.0；应从最新 Unicode 图表/数据选取样例。 |

## 核对清单

1. 确认应用是否在 Android 12+ 使用自定义 Emoji 字体、渲染器、键盘或第三方 Emoji 库。
2. 在每个 Unicode Emoji 新版本发布后四个月内完成更新，并保留版本/测试记录。
3. 测试 Unicode 组合序列在旧版 Android、系统字体、输入法、自定义 View 和 UGC 场景中的显示与输入。
4. 使用当前 Unicode 版本的图表/数据文件更新回归样例；Android 指南中的示例字符是实现参考，不代表政策版本上限。

本专题整理 Google Play 政策与相关实现指南，不包含 Unicode 标准的逐字全文。Android Emoji 政策只有少量强制规则；Emoji2 指南提供的是实现路径，不是独立 Play 审核豁免。Android Emoji 技术文档的所有 API 孙链接尚未全部递归审核。

## 来源与关联知识库

- [Google Play：Android Emoji Policy](https://support.google.com/googleplay/android-developer/answer/11190644?hl=en)
- [Unicode Emoji 技术索引](https://www.unicode.org/emoji/techindex.html)
- [Unicode Emoji 图表](https://www.unicode.org/emoji/charts/)
- [UTS #51：Unicode Emoji](https://www.unicode.org/reports/tr51/)
- [Android：Support modern emoji](https://developer.android.com/develop/ui/views/text-and-emoji/emoji2)
- [Google Play 目标 API 与 Android 迁移](../target-api/target-api-level.zh-CN.md)
