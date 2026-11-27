---
id: regions.cn.apple-app-store-release
platform: apple
language: zh-CN
authority: operational
status: partial
kb_checked_at: 2026-11-27
review_due: 2027-02-27
regions: [CN]
topics: [china-mainland, icp-filing, distribution, app-store-connect]
source_url: https://developer.apple.com/help/app-store-connect/reference/app-information/app-and-compliance-information/
snapshot_id: apple.china-mainland.icp-community-record.2026-11-27
coverage_status: official requirement plus community-recorded exception workflow
---

# Apple 中国大陆上架：ICP 备案与无备案例外申请

> 本页只覆盖 Apple App Store 中国大陆店面。它把 Apple 官方要求和一篇社区经验记录分开维护；社区经验不是 Apple 官方豁免政策，也不是上架保证。

## 结论先行

- 先按 Apple 官方要求判断 App 是否需要提交 ICP 备案号及其他中国大陆许可或证明材料。
- 如果 App 没有自有网络服务、仅在支付时调用 Apple IAP，可以把“联系 Apple 申请个案处理”作为一个社区记录的支持路径；它不能替代正式 ICP 备案，也不能保证获批。
- 如果 App 有自建服务器、账号体系、第三方统计、广告或其他联网能力，应按正式备案和适用许可要求评估，不要把个案记录当成普遍捷径。

## 1. Apple 官方要求（规范性来源）

Apple 的中国大陆合规说明指出，中国大陆法律对部分 App 要求额外文件；工信部要求部分 App 具备有效的 Internet Content Provider（ICP）备案号。提交的 ICP 号码和 App Store Connect 中的 App 元数据应与工信部备案信息一致；匹配优先看简体中文本地化，未配置时看主要语言。

按 Apple 的状态说明：

- `ICP Filing Number Missing`：未提供有效 ICP 备案号，App 在中国大陆不可用。
- `ICP Filing Number Invalid`：提供的 ICP 备案号或元数据与工信部备案信息不匹配，App 在中国大陆不可用。
- 游戏、图书/杂志、宗教、新闻、AI 生成或合成内容，以及需要安全评估的功能，可能还有额外的批准号、出版/许可、备案或安全评估材料要求。

Apple 的 2026-11-16 App Store Connect 更新说明称，ICP、游戏许可和医疗器械声明等法规与许可已从 **App Information** 移到新的 **App Compliance** 页面。由于帮助页文字和控制台界面可能存在过渡期差异，实际发布时应以当前 App Store Connect 页面为准，并保存提交时的页面证据。

## 2. 无 ICP 备案号时联系 Apple：社区记录（非官方流程）

以下内容来自用户提供的社区文章《国区 App Store 无 icp 上架流程》（2026-11-26，Asia/Shanghai）。文章记录的是一个个案做法；Apple 官方帮助页没有公布一套通用的“无 ICP 豁免”流程。

### 适用前提（仅为文章记录）

文章所述案例是 App 没有自有联网功能，仅在支付时调用 Apple IAP，并希望在中国大陆 App Store 上架。是否适用于你的 App，应由 Apple 支持团队按个案判断。

### 文章记录的操作路径

1. 在 App Store Connect 页脚选择“联系我们”。
2. 选择“查看主题”，再选择“分发”。
3. 在联系表单中说明：App 没有自有网络功能，仅在支付时调用 IAP，并希望在中国大陆 App Store 上架。
4. 如果 Apple 通过邮件要求补充声明，准备该独立 App 的声明材料。文章记录的字段包括：Team ID、账户持有人的法定姓名、App ID、账户持有人签名和正楷法定姓名，以及确认这是为该独立 App 申请个案处理、已了解相关法规，并同意对虚假陈述承担法律责任。
5. 如果 Apple 从 `AppleSupport@email.apple.com` 发送安全上传链接，使用该链接上传材料，再回复原邮件，便于 Apple 继续处理案件。
6. 文章作者称该案例通常约 2 天收到审核结果；这不是 Apple 公布的服务时限，也不代表其他 App 会得到相同结果。

### 必须保留的边界

- 这不是 Apple 官方帮助页公布的豁免政策。
- 不应把社区记录写成“无 ICP 均可上架”或“只要发邮件就能通过”。
- 该路径不能代替游戏版号/批准号、出版许可、新闻许可、宗教信息许可、AI 备案或安全评估等其他要求。
- 不要在公开 issue、日志或知识库中提交 Team ID 以外的个人身份资料、签名、Apple 支持邮件内容或安全上传链接。

## 3. 发布前证据与决策记录

针对中国大陆店面，至少记录：

- App 是否有自建服务器、账号体系、第三方统计、广告、推送或其他联网能力；
- App 的 IAP 使用范围，以及是否存在支付以外的网络请求；
- App Store Connect 当前显示的合规字段和中国大陆可用性状态；
- ICP 备案号、元数据匹配结论及相关官方材料（如适用）；
- 若联系 Apple，记录 case ID、联系日期、Apple 回复结论和最终可用性状态；
- 适用的游戏、出版、新闻、宗教、AI 或安全评估材料。

## 来源分类

| 来源 | 类型 | 在知识库中的用途 |
| --- | --- | --- |
| [App and compliance information](https://developer.apple.com/help/app-store-connect/reference/app-information/app-and-compliance-information/) | Apple 官方规范性/操作性来源 | 识别中国大陆 ICP、许可和合规材料要求 |
| [App and submission statuses](https://developer.apple.com/help/app-store-connect/reference/app-information/app-and-submission-statuses/) | Apple 官方状态说明 | 解释 `ICP Filing Number Missing` 与 `ICP Filing Number Invalid` |
| [App Store Connect release notes](https://developer.apple.com/help/app-store-connect/release-notes/) | Apple 官方变更记录 | 记录 2026-11-16 的 App Compliance 页面迁移 |
| [国区 App Store 无 icp 上架流程](https://mp.weixin.qq.com/s/TYQ5fMpQNHeFp1YeaqoNxw) | 社区记录，用户提供，非官方 | 仅用于发现一个个案支持路径；不构成政策依据 |

## 覆盖边界

本页不是法律意见、备案代理或 Apple 审核承诺。正式备案、许可和安全评估应由项目的法务、隐私或合规负责人结合 App 的真实功能和中国大陆监管要求确认。
