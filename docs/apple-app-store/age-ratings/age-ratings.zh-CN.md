---
id: apple.age-ratings.values-and-definitions
platform: apple
language: zh-CN
authority: operational
status: current
kb_checked_at: 2026-11-09
review_due: 2027-02-09
snapshot_package: 2026-11-10
regions: [global, AU, BR, KR, VN]
topics: [age-rating, kids, regional, ugc]
editorial_note: "Snapshot checked 2026-11-09 (package 2026-11-10). No live re-check in this import. Age-rating help pages are cited in English and Simplified Chinese; the snapshot does not record a date lag between those two help pages. Shared Location and Dating and Relationships deadlines come from the English news notice of 2026-11-02. Chinese wording of that notice is an editorial summary, not a claim that Apple published this Chinese text. The separate App Review Guidelines language gap (English 2026-10-16 vs Simplified Chinese 2026-06-08) is disclosed in the guidelines summary."
---

# 年龄分级值与内容定义 / Age Rating Values and Definitions

## 这页解决什么问题

年龄分级是 App Store Connect 里必填的 App 信息。开发者按问卷说明各类内容、功能和控件是否出现，以及出现频率。Apple 根据回答生成分级。它不是开发者自行挑选的营销标签。分级帮助家长和监护人用家长控制管理儿童体验，也帮助用户理解 App 内容。

本页是官方定义页的操作性摘要，不是年龄评级法律意见。最终以 App Store Connect 当前问卷和各地主管机关要求为准。知识库核查日为 2026-11-09（包日期 2026-11-10）。本次导入没有重新打开实时帮助页。

官方定义页：

- [Age ratings values and definitions（英文）](https://developer.apple.com/help/app-store-connect/reference/app-information/age-ratings-values-and-definitions)
- [年龄分级值与定义（简体中文）](https://developer.apple.com/cn/help/app-store-connect/reference/app-information/age-ratings-values-and-definitions)

快照没有记录这两个帮助页之间的更新日期差。不要把《App 审核指南》的中英文滞后（英文 2026-10-16，简体中文官方页 2026-06-08）写成这两页也滞后。指南差异见[审核指南摘要](../app-review-guidelines/guidelines-summary.zh-CN.md)。

## 问卷覆盖的内容与功能

下表是内容信号摘要。最终等级由完整问卷和 Apple 的计算决定，不是“出现某一项就等于某一级”。

| 类别 | 需要识别的内容 |
| --- | --- |
| App 内控件 | 家长控制、年龄保证机制。年龄保证包括声明年龄范围、年龄估测，以及证件或其他验证手段。 |
| 功能 | 不受限网页访问、UGC、社交媒体、未满 13 岁不能使用的社交媒体、信息与聊天、广告。社交媒体不只指发帖，也包括对 UGC 的推荐、转发、点赞、评论和发现。 |
| 成人主题 | 低俗笑话、恐怖或惊悚题材、烟酒或毒品的使用与提及。 |
| 医疗或保健 | 医疗或治疗信息与指导；健康或保健生活方式主题，例如饮食、运动或卡路里追踪。 |
| 性或裸体 | 成人或暗示性主题、色情内容或裸体、露骨色情内容及裸体。 |
| 暴力 | 卡通或幻想暴力、现实暴力、大量露骨或残暴的现实暴力、枪支或其他武器。 |
| 基于概率的活动 | 赌博、模拟赌博、竞赛、抽奖箱。赌博指用真钱或可兑换真钱的游戏内货币下注。模拟赌博不涉及真钱。抽奖箱是可购买并随机给出虚拟物品的容器。 |
| 共享位置 | 与另一名真实用户或群组分享现实世界位置。 |
| 约会与恋爱关系 | 真实用户之间的约会或恋爱连接，或与会参与性或恋爱内容的虚拟伴侣建立此类连接。 |

## 2026 年 11 月新增内容描述符

以下日期和分级效果概括 Apple 的英文公告 [Upcoming: New age rating content descriptors](https://developer.apple.com/news/?id=yxkh08us)（2026-11-02）。**本节中文是该英文公告的编辑摘要，不是 Apple 已发布的中文公告正文。**

App Store Connect 将于 **2026-11-16** 在年龄分级问卷中新增“共享位置”和“约会与恋爱关系”声明。提交 App 更新或修改年龄分级问卷时必须填写。所有 App 必须在 **2027-01-12** 前完成。

- **约会与恋爱关系：** 触发最低 **18+**。
- **共享位置：** 最低分级按地区而异。在巴西，Apple 规定共享位置为 **A16**，约会与恋爱关系为 **A18**。**地区敏感。**
- 若巴西 App 有合理理由需要更低分级（例如面向家长与儿童的定位共享），开发者可向巴西司法与公共安全部（MJSP）申请官方评级。核验后，Apple 会在巴西 App Store 展示官方评级。MJSP 页面：[Classificação](https://www.gov.br/mj/pt-br/assuntos/seus-direitos/classificacao-1)。这是监管来源，不是 Apple 规则正文。

执行时先盘点：

- [ ] 所有向他人或群组共享实时或精确现实位置的功能。
- [ ] 真人约会或恋爱匹配，以及会与用户进行性或恋爱内容互动的虚拟伴侣。
- [ ] 下次提交前写下问卷答案、预期全球分级、巴西分级，以及任何监管证明。

这些勾选项是执行提示。

## 当前分级值

快照记录的当前常规年龄分级为 **4+、9+、13+、16+、18+ 和未评级**，用于运行 iOS 26 等系统的设备。下表只汇总页面列出的典型信号。

| 分级 | 页面给出的典型信号 |
| --- | --- |
| 4+ | 无令人反感内容。仍可能包含家长控制、年龄保证、UGC、聊天、广告、偶尔竞赛等功能。 |
| 9+ | 偶尔低俗笑话或惊悚内容、健康或保健主题、偶尔成人暗示、卡通或幻想暴力、武器，或抽奖箱。 |
| 13+ | 社交媒体或未满 13 岁限制功能；频繁低俗笑话、惊悚题材或烟酒毒品提及；偶尔医疗信息、色情内容或裸体、现实暴力、模拟赌博；频繁卡通暴力、武器或竞赛。 |
| 16+ | 不受限网页访问、频繁医疗或治疗信息、频繁成人或暗示性主题。 |
| 18+ | 频繁烟酒毒品相关内容、色情内容或裸体、现实暴力；赌博或频繁模拟赌博。 |
| 未评级 | 露骨色情内容或裸体，或大量露骨、残暴的现实暴力。此类内容不能发布到 App Store。 |

## 地区分级

地区规则可以在 Apple 全球分级之外增加本地标识、条件或审核材料。不要把同一个全球分级当成每个店面的完整答案。**地区敏感。**

| 地区 | 摘要 | 执行要点 |
| --- | --- | --- |
| 澳大利亚 | 该页分别给出当前和旧系统的展示条件。澳大利亚分级机关可能要求修正或补充地区分级。当前页面还把部分社交媒体、抽奖箱、模拟赌博内容映射到地区分级。 | 发行包含抽奖箱或模拟赌博的游戏时，核对当地分类规则和 App Review 提醒，按提醒补充资料并重新提交。 |
| 巴西 | Apple 自评与司法和公共安全部（MJSP）官方评级使用不同标识。存在官方评级时按官方地区评级展示。固定赔率博彩须持有 SPA 有效许可，并在 App Review 信息中填写和上传证明。 | 赌博类 App 上架前核实许可是否有效、范围是否匹配、审核附件是否齐全。自评不能代替合法经营资格。 |
| 韩国 | 当前年龄问卷分级包括与 All、12+、15+、19+ 相关的映射。GRAC 官方等级与 Apple 问卷结果不同时，可能要求提交 RCN 或覆盖韩国分级。 | 游戏、娱乐，以及含频繁或强烈模拟赌博的 App，应核对 GRAC 分类编号和 App Store Connect 的提交要求。 |
| 越南 | 页面列出 00+、12+、16+、18+，并按功能、成人主题、医疗、性或裸体、暴力和概率活动映射。 | 对越南店面复核当地法令和问卷映射。不要直接复制 Apple 全球分级。 |

## 旧系统分级

仅在仍需支持会显示旧分级体系的系统时查阅本节。新系统使用上一节的当前分级，并以提交时的 App Store Connect 问卷为准。

旧版全球年龄分级为 **4+、9+、12+、17+、未评级**。澳大利亚、巴西、法国和韩国还可能显示地区标识。不要把旧系统的 12+ / 17+ 与当前的 13+ / 16+ / 18+ 当成同一套数字。

## 与公告的关系

本页用来填写问卷并解释答案含义。

- 2026-11-02 的[新增内容描述符公告](https://developer.apple.com/news/?id=yxkh08us)补充了共享位置、约会与恋爱关系，以及 2027-01-12 完成期限。上文中文是编辑摘要。
- 快照记录：2026-09-09“现已接受最新版操作系统提交”公告链到 2026-07-09 的[年龄分级问卷与社交媒体公告](https://developer.apple.com/cn/news/?id=tlur8uvi)。该公告说明社交媒体能力如何影响问卷、产品页描述符和“时间额度”分类。本页对社交媒体、UGC、年龄保证、年龄限制和聊天的定义，用于判断答案范围。快照没有单列 9 月 9 日那则公告的 URL，这里不补写。
- 快照记录：2026-08-12 韩国分级公告也指向本定义页，并补充韩国 GRAC RCN 覆盖流程。快照的年龄分级稿没有给出该公告 URL，这里不补写。

## 上架前核查

- [ ] 盘点公开 UGC、推荐与发现、点赞评论、私信与群聊、广告、嵌入浏览器、年龄保证和家长控制。
- [ ] 按实际内容和频率填写问卷，不要只依据 App 主类别、目标用户或商店营销文案。
- [ ] 核对成人主题、医疗指导、性内容、暴力、武器、赌博与模拟赌博、竞赛和抽奖箱。
- [ ] 新字段上线后填写共享位置、约会与恋爱关系；在 2027-01-12 前完成所有 App，并保留巴西 A16/A18 或 MJSP 官方评级路径的证据。
- [ ] 按目标系统分别检查当前分级和旧分级，并按每个目标店面复核地区分级。
- [ ] 适用时准备 GRAC RCN、巴西 SPA 博彩许可、监管评级证明，以及 App Review 备注和附件。
- [ ] 保留问卷答案、内容盘点、地区材料和审核提醒。功能或内容变化后重新评估。

这些勾选项是执行提示。可与[上架前检查清单](../pre-submission/submission-checklist.zh-CN.md)一起使用。

本页不代替 [英文定义页](https://developer.apple.com/help/app-store-connect/reference/app-information/age-ratings-values-and-definitions) 或账户内的实时问卷。
