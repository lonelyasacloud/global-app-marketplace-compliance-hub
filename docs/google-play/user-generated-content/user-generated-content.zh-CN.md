---
id: google-play.user-generated-content
platform: google-play
language: zh-CN
authority: normative
status: current
kb_checked_at: 2026-10-24
review_due: 2027-01-24
regions: [global]
topics: [ugc, moderation, social, child-safety, ai-content, content-rating]
snapshot_id: play.user-generated-content
snapshot_package: "GooglePlay-KnowledgeBase-2026-10-24-review.zip"
coverage_status: "detailed-summary"
source_url: "https://support.google.com/googleplay/android-developer/answer/9876937?hl=en"
source_url_zh: "https://support.google.com/googleplay/android-developer/answer/9876937?hl=zh-Hans"
effective_date: "current-policy"
---

# 用户生成内容（UGC）与内容审核

> **导入说明（Google batch 3）。** 本页正文取自 2026-10-24 Google Play 知识库快照里已经分开的对应语言改写（`play.user-generated-content`，核对日 2026-10-24），不是官方页面的逐字文本。英文官方来源是效力来源。`kb_checked_at` 使用快照源文件记录的核对日；本次导入没有重新打开线上官方页面。文中“本知识库”“本库”“本地专题”描述的是该快照知识库的覆盖范围，不是本仓库已经导入的页面清单。快照里指向尚未导入本仓库的专题、链接图、台账或 CSV 的相对链接，已改为文字提及；指向 Google batch 1、batch 2 或本批九个专题的相对链接已改到本仓库路径。2026-10-24 快照重读了英文和官方简体中文 `zh-Hans` 的 UGC 政策与审核指南正文。Google 提示中文可能由 AI 翻译且不准确，关键义务以英文现行政策交叉核对。精确 `hl=zh-CN` 路由不可读。该抓取失败不表示政策已经变更。本中文页是快照改写，不是 Google 已发布的中文页面文本。本 UGC 政策没有记录未来生效日。UGC 政策的证据等级是 `normative`。审核最佳实践是 operational 指南，不能豁免政策按交互形态给出的示例。AI 生成内容是相邻但独立的规则。本专题与不当内容、年龄限制和内容分级保持分开。

**核对日期：2026-10-24。** 本页按 Google Play 的 UGC 政策及审核最佳实践整理。2026-10-24 重读英文和官方简体中文 `zh-Hans` 正文；Google 页面提示中文可能由 AI 翻译且不准确，关键义务以英文现行政策和适用的 Play Console 规则交叉核对。UGC 不只包括社交网络帖子，也包括用户提交后可供至少一部分用户查看或访问的内容；把用户导向 UGC 平台的专用浏览器或客户端也在政策范围内。以下为双语改写摘要，不是政策全文镜像。

## 适用范围与责任

- 如果应用展示或链接到内容，政策覆盖应用能访问的内容，包括广告和应用托管或链接的 UGC；公开显示在 Play 上的开发者名称、开发者网站落地页等账户材料也须符合政策。
- UGC 应用必须持续实行有效、适度且与内容形态相称的审核。即使 UGC 只占应用一小部分，开发者仍需管理该功能带来的风险。
- 服务条款/用户规则与隐私政策是不同文件。用户发布前应能看到规则，并须先接受规则；规则要用符合 Google Play 政策的方式定义并禁止不当内容和行为。

## 举报、屏蔽与及时处置

政策要求按交互方式配置用户可用的审核工具，页面举例包括：

| UGC 形态 | 政策示例要求 |
| --- | --- |
| 通过验证或线下登记形成的固定群体 | 应能在应用内举报内容和用户。 |
| 一对一互动，例如私信、标记或提及 | 应能在应用内屏蔽用户。 |
| 可公开访问的 UGC | 应能在应用内举报内容与用户，并屏蔽用户。 |
| AR 中的 UGC | 举报和审核应覆盖有害 AR 内容及敏感锚点位置，例如限制区域或私人财产。 |

补充的审核说明建议让举报和屏蔽入口清楚、易找、标签明确，并对举报及时采取适当行动。不要把两个功能塞进含义不清的同一个按钮。实践上应按产品风险尽量同时支持“举报内容/用户”和“屏蔽用户/内容”；上表的政策示例用于判断最低场景要求，具体实现仍须结合交互形态核对。

应用还应防止付费功能、奖励或推荐机制鼓励骚扰、霸凌或其他不当行为。若应用持续忽视举报，或逐渐形成主要用于传播不当 UGC 的声誉，可能被移除。

## 附随性色情内容：非常有限的条件

这不是一般成人内容豁免。只有以非色情内容为主、且不主动推广或推荐色情内容的 UGC 应用，才可能在同时满足以下条件时包含“附随性”色情内容：

1. 内容默认隐藏在过滤器后；用户至少完成两次操作才能完全关闭过滤并看到内容。
2. 通过适当的年龄筛查阻止 Families 政策定义的儿童使用应用；年龄屏幕不能预设成年人生日，也不能提示用户填写特定年龄来绕过限制。
3. Play Console 的内容分级问卷如实反映应用中的 UGC。
4. 不包含适用法律认定为违法的色情内容或任何危害儿童内容；不主动推荐、推送或突出展示色情内容。

如果应用的主要目的就是展示不当 UGC，或应用形成供此类内容传播的声誉，可能被移除。Play 的 Inappropriate Content 与 Child Endangerment 规则仍然适用；“附随性”不能使违法、非自愿性内容或儿童性剥削内容变得可接受。

## 儿童安全、年龄与内容分级

- UGC 中的威胁、骚扰、霸凌，尤其针对未成年人的内容，需要有效防护和持续处置；开发者应评估用户年龄、社交功能、发现/推荐机制和举报响应能力。
- 匿名聊天、随机聊天、社交和约会应用还须核对 Child Safety Standards；这包括公开的儿童安全规则、应用内反馈机制、对已知 CSAM 的处置、依法报告流程和儿童安全联系人。参见[年龄限制与儿童安全专题](../age-restricted-child-safety/age-restricted-child-safety.zh-CN.md)。
- 目标受众包含儿童会触发 Families 额外要求，包括适龄内容、SDK/API、数据和广告规则；混合受众的年龄屏幕和儿童广告也须符合相应政策。
- 每个新应用和已上架应用都应有准确的 IARC 内容分级；UGC 或功能变化影响问卷答案时须重新提交。错误申报可能导致下架或暂停。

## AI 生成内容是相邻但独立的规则

生成式 AI 应用必须遵守 Google Play 的其他开发者政策，防止生成受限内容（包括危害儿童或欺骗用户的内容），并提供应用内举报/标记入口，让用户无需离开应用即可报告有害输出；开发者应把举报用于改进过滤和审核。Google 的最佳实践还建议采用过滤器/分类器，并参考安全测试框架。若 AI 输出被用户发布、分享或展示给其他用户，应结合真实功能进一步判断 UGC 政策是否同时适用。范围、违规示例和每个直接安全资源见独立的 AI 生成内容双语专题（快照：`ai-generated-content.md`，未导入本仓库） · English（快照：`ai-generated-content-en.md`，未导入本仓库）。

## 上线与运营核对清单

1. 列出所有用户可提交、分享、评论、私信、嵌入或浏览的内容类型，包括经第三方浏览器/客户端访问的 UGC。
2. 在用户发布前展示清楚的服务条款/社区规则并取得接受；规则须覆盖禁止内容、举报路径和处置方式。
3. 按产品形态提供清楚可见的举报与屏蔽工具，并测试举报是否进入有人负责、能及时处置的队列。
4. 评估搜索、推荐、通知、付费功能和奖励是否会放大有害内容或骚扰行为；对 AR 功能还检查锚点位置风险。
5. 若含可见的性内容，逐项核实是否满足附随性定义、默认过滤、至少两步关闭过滤、年龄筛查和准确分级；任何违法或儿童危害内容都不属于例外。
6. 对儿童受众、匿名/随机聊天、社交和约会功能分别核对 Families、Child Safety Standards、Restrict Minor Access 与当地法律要求。
7. 对生成式 AI 测试输入/输出安全，提供应用内举报入口，并根据新型滥用和用户举报更新防护。
8. 内容、受众、交互或变现方式变化后，重新检查政策适用、Console 申报与 IARC 问卷。

## 正文子链接与相关页面审计

| 父页面/分支 | 已打开的目标 | 关系与覆盖状态 |
| --- | --- | --- |
| User Generated Content policy | [Child Endangerment](https://support.google.com/googleplay/android-developer/answer/9878809?hl=en)、[Families Policies](https://support.google.com/googleplay/android-developer/answer/9893335?hl=en)、[Target audience and app content settings](https://support.google.com/googleplay/android-developer/answer/9867159?hl=en)、[Content Ratings](https://support.google.com/googleplay/android-developer/answer/9898843?hl=en) | 英文与 `zh-Hans` 正文均已完整读取，四个正文政策目标均已打开；中文页带 AI 翻译准确性提示，精确 `zh-CN` 路由不可读。年龄屏幕直链的带参数点击曾超时，但规范目标受众页已完整读取；三张中文正文图标作为媒体目标单独登记。 |
| UGC moderation best-practices article | [Understanding moderation requirements and incidental sexual content in UGC apps](https://support.google.com/googleplay/android-developer/answer/12923286?hl=en) · [简体中文 `zh-Hans`](https://support.google.com/googleplay/android-developer/answer/12923286?hl=zh-Hans) | 2026-10-24 重读两种语言正文。补充发布前接受条款、举报/屏蔽入口清楚易找、及时处置、默认隐藏和年龄筛查。该指南对 UGC 应用提出更广泛的应用内举报/屏蔽要求；基础政策按群组、1:1、公开和 AR 交互举例，不能将这些例子当成免除其他适用工具的豁免。两页的四个规范性直链均已打开。英文页 5 张示例图中 3 个超时、2 个 Cache miss；中文页 5 张示例图均 Cache miss。Community、Contact us 和 Policy education 标题入口点击失败且未暴露 href，未猜测目标。2026-10-23 已点击 32 个 Policy education 侧栏目标（含当前页），均有逐 URL 台账和本地双语专题映射；健康权限 FAQ 当时点击 Internal Error，保留既有全文记录。目标页正文后代仍未闭合。 |
| Policy Coverage | [Policy Coverage](https://support.google.com/googleplay/android-developer/answer/10146128?hl=en) | 已打开；确认政策覆盖应用显示或链接的 UGC/广告、公开开发者资料及内容分级。 |
| AI-generated content branch | [AI-Generated Content](https://support.google.com/googleplay/android-developer/answer/13985936?hl=en)、[Best Practices to Safeguard AI-Generated Content](https://support.google.com/googleplay/android-developer/answer/16353813?hl=en) | 两页已打开；AI 规则要求预防受限输出和应用内举报。最佳实践正文的 10 个安全框架/供应商直接链接均已打开并分类，见下表；它们不是 Play 强制政策，后续链接未继续扩展。 |
| 相关内容限制 | [Inappropriate Content](https://support.google.com/googleplay/android-developer/answer/9878810?hl=en)、[Learning more about Child Safety Standards](https://support.google.com/googleplay/android-developer/answer/14747720?hl=en) | Inappropriate Content 已打开。`14747720` 于 2026-10-22 重新打开全文，Child Safety Standards 的适用范围、公开标准、应用内反馈、CSAM 处置和指定联系人已补入[儿童安全专题](../age-restricted-child-safety/age-restricted-child-safety.zh-CN.md)；最佳实践后代见该专题 §“儿童安全标准的落地最佳实践与子链接”。 |

### UGC 政策与审核最佳实践正文直链清单（2026-10-24）

下面只列正文直接链接；侧栏目录另见上文。英文与 `zh-Hans` 审核指南的政策正文链接指向相同的规范目标。

| 父正文 | 直接目标 | 与 UGC 的关系及本次访问结果 |
| --- | --- | --- |
| 审核最佳实践 | [User Generated Content policy](https://support.google.com/googleplay/android-developer/answer/9876937?hl=en) | UGC 适用范围与按交互形态区分的政策；英文及 `zh-Hans` 正文均完整读取。 |
| 审核最佳实践 | [Child Endangerment](https://support.google.com/googleplay/android-developer/answer/9878809?hl=en) | 儿童伤害边界与保护要求；目标正文已打开。 |
| 审核最佳实践 | [Families Policies](https://support.google.com/googleplay/android-developer/answer/9893335?hl=en) | 儿童受众在内容、SDK、数据和广告方面的规则；目标正文已打开。 |
| 审核最佳实践 / UGC 政策 | [Target audience and app content settings](https://support.google.com/googleplay/android-developer/answer/9867159?hl=en) | 年龄筛查与受众指导；规范目标正文和中性年龄屏幕章节已完整读取。 |
| UGC 政策 | [Content Ratings](https://support.google.com/googleplay/android-developer/answer/9898843?hl=en) | UGC 变化可能影响内容分级问卷答案；目标正文已打开。 |
| 中文 UGC 政策正文中的中性年龄屏幕链接 | [带参数的直接目标](<https://support.google.com/googleplay/android-developer/answer/9867159?rd=1&visit_id=637661037575013539-1915084824>) | 该次点击返回 400 Timeout fetching；规范 `answer/9867159` 页面已完整读取。记录为原始入口失败、规范目标可读。 |
| 审核最佳实践英文示例图 1–5 | [图像 1](https://lh3.googleusercontent.com/yCNOQUtlNDBcHfFCCLYhwlyYxBy9wMY3wp8723a68Tmk3lLbkmb6GhAgC7Yh_2_RcCM%3Dw895), [图像 2](https://lh3.googleusercontent.com/mZYbxuII4CcE2PA_D4SE04EOPBwTX-n7lHwnVK1EDFiGGSC4ZGvIkrUZYesjbfByHA%3Dw895), [图像 3](https://lh3.googleusercontent.com/EoJEKqImBlKVH-GJbvLkm5AavKvF70LGsqBnkE0rs3ZjBAJvpzM7Svf3R5jDxLlEiJk%3Dw895), [图像 4](https://lh3.googleusercontent.com/eevd7uud5VWBvKFJNMgJ4q-h8JXBbGJlM5CEwZhnhDavQf0TcMP6ZlPnX97PCfHQkg%3Dw450), [图像 5](https://lh3.googleusercontent.com/bMyqO4IFDEBVX5j-Exfhyitc4i2VDjGYmPJyqX9RUTzVGylbYg3BKY1Sng7vmjSjSLne%3Dw450) | 3 个目标超时、2 个 Cache miss；无可核验像素或政策正文。 |
| 审核最佳实践 `zh-Hans` 示例图 1–5 | [图像 1](https://lh3.googleusercontent.com/VWOrs04dcRpwglePWv53fMPtnDm9RnZWHqtuDJ7BvyVYEZWlVNQhsWAEFKg7jM36PA%3Dw895), [图像 2](https://lh3.googleusercontent.com/eDCpoQsLe6QcZcz453PVD36N36bT1kWabv50_4f8rvB3V13U-8pPZtTiHbMLECj_L2g%3Dw895), [图像 3](https://lh3.googleusercontent.com/hQhEO3NpA1uiYAgdVJI2ZGhOUvSjS7aPQDuazw_Fa0x_gNIWIAPwpYYq9Y4ojk2llGC_%3Dw895), [图像 4](https://lh3.googleusercontent.com/AQ5dh5TlFwW4lJUrqcflaYCWdWR6ZZS6kizJ4W4F-RV7QfXtQKxusGuVhJui-BrgRw%3Dw895), [图像 5](https://lh3.googleusercontent.com/FMHts1Osfr_4huK-1MGmevdMk6UsUbjTEpdehQzvqyIxWayHXqyY9SosQ8GtnD7m9RQ%3Dw895) | 5 个目标均 Cache miss；无可核验像素或政策正文。 |
| UGC 政策 `zh-Hans` 正文图标 1–3 | [图标 1](https://lh3.googleusercontent.com/BPsAL28eke0gFbFJduiZupJyY6uR5X7_JHR_3vev1cApatT5KLrReyskdlNZXRGFsg%3Dw60-h60), [图标 2](https://lh3.googleusercontent.com/hnJIMKQ0lyssVbehdx4OCpjLHPBYy94NeG4dD-xZ40osbCjM8Lt3zS4P5JvA5Xsqig%3Dw30-h34), [图标 3](https://lh3.googleusercontent.com/IfJhh8qlFSuw1U7A2DSeKi0B3jBYMC5fU0pGMUG40oyCU3urkOu4yGg0D24TkbUvwRk%3Dw40) | 工具返回图像 endpoint，无可审阅像素；只作视觉资产记录。 |
| Community、Contact us、Policy education 标题入口；UGC 政策页 Contact us | 无可核验 href | 点击返回 Internal Error，未暴露目标 URL；不根据控件文字猜测地址。属于未解析的支持/导航入口，不是政策文本。 |

**两层政策措辞：**审核最佳实践页以较广措辞要求托管 UGC 的应用提供应用内举报和屏蔽能力；基础政策则按固定群组、一对一、公开 UGC、AR 等体验给出工具示例。应并列核对，不能把基础政策示例当成其他适用工具的豁免；应按实际交互为内容和用户提供适用的报告/屏蔽路径。

### UGC 政策页的“受限内容”侧栏（导航，不是正文义务）

政策页列出 10 个受限内容入口，其中 UGC 是当前页，其余 9 个现行目标本轮已逐页打开，并关联到已有双语专题。侧栏表示相邻政策目录，不等同于 UGC 正文新增加的要求；每个专题的更深子链接仍按各自来源审计状态处理。

| 侧栏条目 | 官方目标 | 本地双语专题与关系 |
| --- | --- | --- |
| Child Endangerment | [政策页面](https://support.google.com/googleplay/android-developer/answer/9878809?hl=en) | [年龄限制与儿童安全](../age-restricted-child-safety/age-restricted-child-safety.zh-CN.md) · 涉及儿童性剥削、危害儿童与相关保护要求。 |
| Inappropriate Content | [政策页面](https://support.google.com/googleplay/android-developer/answer/9878810?hl=en) | [不当内容](../inappropriate-content/inappropriate-content.zh-CN.md) · 解释禁止内容与 UGC 中“附随性色情内容”的边界。 |
| Financial Services | [政策页面](https://support.google.com/googleplay/android-developer/answer/9876821?hl=en) | [金融服务与贷款](../financial-services-and-loans/financial-services-and-loans.zh-CN.md) · 受监管金融功能、申报、贷款与地区要求。 |
| Real-Money Gambling, Games, and Contests | [政策页面](https://support.google.com/googleplay/android-developer/answer/9877032?hl=en) | [真钱赌博](../real-money-gambling/real-money-gambling.zh-CN.md) · 适用资格、许可、地域/年龄限制与责任博彩要求。 |
| Illegal Activities | [政策页面](https://support.google.com/googleplay/android-developer/answer/9878877?hl=en) | 非法活动（快照：`illegal-activities.md`，未导入本仓库） · 禁止促进非法行为，并须结合目标市场法律核验。 |
| User Generated Content | [当前政策页面](https://support.google.com/googleplay/android-developer/answer/9876937?hl=en) | 本页 · UGC 范围、审核、举报/屏蔽和附随性内容条件。 |
| Health Content and Services | [政策页面](https://support.google.com/googleplay/android-developer/answer/16679511?hl=en) | 健康应用与 Health Connect（快照：`health-apps-and-health-connect.md`，未导入本仓库） · 健康功能、医疗声明、健康数据与监管要求。 |
| Blockchain-based Content | [政策页面](https://support.google.com/googleplay/android-developer/answer/13607354?hl=en) | [加密资产与 NFT](../crypto-assets-and-nfts/crypto-assets-and-nfts.zh-CN.md) · 钱包、交易所、代币化资产与 NFT 游戏要求。 |
| AI-Generated Content | [政策页面](https://support.google.com/googleplay/android-developer/answer/13985936?hl=en) | AI 生成内容（快照：`ai-generated-content.md`，未导入本仓库） · 受限输出预防和应用内举报入口。 |
| Age-Restricted Content and Functionality | [政策页面](https://support.google.com/googleplay/android-developer/answer/16302250?hl=en) | [年龄限制与儿童安全](../age-restricted-child-safety/age-restricted-child-safety.zh-CN.md) · 需要阻止未成年人访问的核心功能类别。 |

### AI 安全最佳实践文章的直接外部链接

这些页面由 Google Play 的 AI 安全最佳实践文章直接推荐。记录它们是为了保留来源链；供应商功能与条款会变动，不能替代 Play 政策，也不应仅凭某个模型内置过滤器推断应用已符合 Play 要求。

| 类别 | 页面 | 与 UGC/AI 内容安全的关系及核验状态 |
| --- | --- | --- |
| 安全框架 | [Google Secure AI Framework（SAIF）](https://saif.google/secure-ai-framework) | 已打开；用数据、基础设施、模型和应用维度映射 AI 风险与控制。 |
| 安全测试 | [OWASP GenAI Red Teaming Guide](https://genai.owasp.org/resource/genai-red-teaming-guide/) | 已打开；把评测、实现测试、基础设施评估和运行时行为纳入红队测试。 |
| Google 开发者资源 | [Responsible Generative AI Toolkit](https://ai.google.dev/responsible) | 已打开；覆盖系统级安全规则、设计、模型评测、过滤器/分类器和相关工具。 |
| 模型/内容安全供应商资料 | [Microsoft AI Content Safety](https://azure.microsoft.com/en-us/products/ai-services/ai-content-safety)、[OpenAI Safety best practices](https://developers.openai.com/api/docs/guides/safety-best-practices)、[Anthropic Content moderation](https://platform.claude.com/docs/en/about-claude/use-case-guides/content-moderation)、[AWS Responsible content moderation](https://docs.aws.amazon.com/solutions/responsible-content-moderation-with-ai-services-on-aws/)、[Meta Responsible Use Guide](https://ai.meta.com/static-resource/responsible-use-guide/)、[Salesforce Trusted AI](https://www.salesforce.com/artificial-intelligence/trusted-ai/)、[Cohere Safety Modes](https://docs.cohere.com/docs/safety-modes) | 目标页面均已访问并列入台账；这里只记录来源类别，不把供应商说明汇总成 Play 规则，也未遍历这些站点的孙链接。 |

官方中文 UGC 政策入口：[简体中文](https://support.google.com/googleplay/android-developer/answer/9876937?hl=zh-Hans)；本轮英文和 `zh-Hans` 政策及审核指南正文均可读取，中文页面提示可能为 AI 翻译且不保证准确，精确 `zh-CN` 路由不可读。UGC 正文的三张中文图标、审核指南两种语言共十张示例图，以及无法解析 href 的 Community/Contact/Policy education 入口均在下方逐项标明；图像不是政策文本。10 项受限内容侧栏是导航目录，最佳实践页另有 32 项 Policy education 导航；两者与正文链接分开。各链接目标自己的子链和更深后代仍按台账状态处理，未声称递归闭合。

## 来源与关联专题

- [User Generated Content policy](https://support.google.com/googleplay/android-developer/answer/9876937?hl=en) · [官方简体中文页面](https://support.google.com/googleplay/android-developer/answer/9876937?hl=zh-Hans)
- [UGC moderation and incidental sexual content guidance](https://support.google.com/googleplay/android-developer/answer/12923286?hl=en) · [官方简体中文 `zh-Hans`](https://support.google.com/googleplay/android-developer/answer/12923286?hl=zh-Hans)
- [AI-Generated Content](https://support.google.com/googleplay/android-developer/answer/13985936?hl=en) · [AI safety best practices](https://support.google.com/googleplay/android-developer/answer/16353813?hl=en)
- [Policy Coverage](https://support.google.com/googleplay/android-developer/answer/10146128?hl=en) · [Inappropriate Content](https://support.google.com/googleplay/android-developer/answer/9878810?hl=en) · [Content Ratings](https://support.google.com/googleplay/android-developer/answer/9898843?hl=en)
- [年龄限制与儿童安全专题](../age-restricted-child-safety/age-restricted-child-safety.zh-CN.md) · 第三方 SDK 专题（快照：`sdk-requirements.md`，未导入本仓库） · [用户数据专题](../user-data/user-data.zh-CN.md)
