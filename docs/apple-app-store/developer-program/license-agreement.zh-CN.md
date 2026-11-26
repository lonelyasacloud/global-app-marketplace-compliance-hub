---
id: apple.developer-program.license-agreement
platform: apple
language: zh-CN
authority: operational
status: current
kb_checked_at: 2026-11-09
review_due: 2027-02-09
snapshot_package: 2026-11-10
regions: [global, CN, EU, JP, BR, TW]
topics: [agreement, payments, distribution, certificates, regional]
editorial_note: "Snapshot checked 2026-11-09 (package 2026-11-10). No live re-check in this import. The supplied /cn/ license URL rendered English. The October 13, 2026 amendment notice said a translation would follow within one month. This Chinese page is an editorial summary, not Apple's published translation or legal advice. The separate App Review Guidelines gap (English 2026-10-16 vs Simplified Chinese 2026-06-08) is disclosed in the guidelines summary."
---

# Developer Program 许可协议摘要 / License Agreement Summary

## 版本、语言与证据等级

本页是便于产品、工程和运营使用的**编辑摘要**。它不是 Apple 的正式中文译文，也不构成法律意见。出现解释或条款冲突时，回到最新协议、对应附件和合格的法律意见。

快照使用的链接含有 `/cn/`：[Apple Developer Program License Agreement](https://developer.apple.com/cn/support/terms/apple-developer-program-license-agreement/)。截至核对日 **2026-11-09**，该页标题和协议正文均为英文。2026-10-13 更新公告称翻译版将在一个月内提供。在此之前，以该页英文文本作为协议原文。本次导入没有重新打开实时协议页，也不把 2026-11-09 写成新的在线复核。包日期为 2026-11-10。

当前协议的入口索引见 [Apple Developer Agreements and Guidelines](https://developer.apple.com/support/terms/)。

**当前与历史：** 本摘要按 2026-11-09 打开的实时协议、[2026-10-13 修订公告](https://developer.apple.com/news/?id=17mwd36z) 和 [2026-10-29 台湾店面公告](https://developer.apple.com/news/?id=w9mxlhek) 整理。2026-08-18 的协议公告只保留为较早修订的时间线，不是现行协议文本，也不能单独用来确认当前义务。若本摘要与实时协议、后续公告或账户内待接受条款不同，以最新官方文本和适用附件为准，并在开发者账户中确认接受状态。

《App 审核指南》另有语言差：英文页 2026-10-16，简体中文官方页 2026-06-08。那是指南页的差异，不是本协议页的中文译本。说明见[审核指南摘要](../app-review-guidelines/guidelines-summary.zh-CN.md)。

## 协议的作用

协议授予开发者有限的 Apple 软件、服务、证书和相关能力使用许可，并约束开发、测试、签名、提交、分发、付款、隐私、保密和责任。它与《App 审核指南》、App Store Connect 文档、各项授权条款及当地法律同时适用。通过审核不转移开发者对 App 安全、权利、数据、税务、支持和合规的责任。

协议本身是规范性文件。下表是操作性要点，不是条款原文。

## 主协议索引

| 条款 | 要点 | 操作意义 |
| --- | --- | --- |
| 1. 接受协议；定义 | 确认接受条款。个人签约者须具备法定行为能力，代表组织签约者须有权约束该组织。定义覆盖 Apple 软件、服务、App、数据、证书、授权开发者和预发布资料等。 | 核对签约实体、账户持有人和团队授权。后续解释应回到协议中的定义。 |
| 2. 内部使用许可与限制 | 许可是有限、非独占、可撤销、不可转让且不可再许可的，用于允许的开发与测试。软件和服务只能在许可目的和条款范围内使用。 | 不把 Apple 软件、密钥、服务或开发资源挪作未授权用途。限制承包商访问，并对其行为负责。 |
| 3. 开发者义务 | 开发者负责账户信息准确、团队和承包商行为、适用法律、隐私与用户同意、知识产权、产品安全，以及按规定使用 API、框架和服务。不同 API 和数据有专用目的限制。 | 为每个 entitlement 和 API 建立“资格、用途、数据、用户披露、保留与删除”记录。不要仅因 API 能调用就推断用途已获准。 |
| 4. 计划要求或条款变更 | Apple 可更新计划要求和协议。继续使用软件、证书或服务必须接受新要求。拒绝可能导致暂停或终止。新要求不追溯适用于已分发的 App，但 Apple 仍可下架不合规 App。 | 指定条款变更负责人和接受记录。评估已有版本、后续更新，以及各店面是否需要行动。 |
| 5. Apple 证书；撤销 | App、Wallet Pass、Safari 扩展等须按用途签名。开发者须保护证书和私钥并限制共享。发现泄露应及时通知 Apple。Apple 可在安全、违约或其他约定情况下撤销证书或票据。 | 管理密钥并轮换。不要把分发私钥放进第三方可访问的普通仓库。保留证书负责人和泄露响应流程。 |
| 6. App 提交与选择 | 涵盖 App Store 与 Custom App Distribution 的提交和选择、App Thinning、iOS/iPadOS App 在 macOS/visionOS 上的可用性、CarPlay 与 Apple HomeView 小组件、TestFlight 和分析数据。开发者不得对审核隐藏功能，必须拥有权利，并对跨平台兼容负责。 | 提交内容与实际功能保持一致。核对跨平台权利、测试覆盖、TestFlight 重大变更，以及分析数据的允许用途。 |
| 7. App 与 Library 分发 | 允许的路径包括 App Store、Custom App Distribution、Ad Hoc、TestFlight 和 Library，并限制未获准的第三方分发。提交的 App、元数据、出口合规和知识产权声明仍由开发者负责。 | 写明每个 build 的分发渠道、用户范围、区域、签名和出口合规。不要把企业或自用分发当成公开 App Store 分发的替代。 |
| 8. 计划费用 | 参加计划须支付适用年费，通常不退款，相关税费按协议承担。自动续费和通过 Apple Developer App 购买可能触发附加条款。 | 维护续费和支付主体。通过 Developer App 购买时关注 Attachment 9。 |
| 9. 保密 | 预发布软件、服务、硬件和相关材料通常属于 Apple 机密信息。公开前不得未经授权披露或用于协议外目的，除非条款规定的例外适用。 | 把 Beta、未发布功能和测试材料纳入保密流程。离职、外包和对外沟通前核对访问与披露限制。 |
| 10. 赔偿 | 在法律允许范围内，开发者需处理并赔偿因违约、产品、内容、知识产权、用户索赔、开发与分发等引起的特定损失。 | 把第三方素材授权、消费者投诉、未成年人安全、隐私和产品责任纳入发布前审核和证据留存。本行不是法律意见。 |
| 11. 期限与终止 | 计划按年度续期。严重或未补救的违约、保密违规、未接受新条款等可能导致终止或暂停。终止后须停止使用并处理 Apple 软件和机密材料。部分条款继续有效。 | 维持账号连续性、到期提醒和关键服务的替代方案。注意终止后的数据、证书和分发状态。 |
| 12. 无保证 | Apple 软件和服务按协议提供，可能有错误、不可用或变更。协议不对可用性、准确性和不中断作一般保证。 | 不把 Apple 服务当作唯一的故障安全机制。关键功能需要降级、重试和备份。这是执行提示。 |
| 13. 责任限制 | 对 Apple 的损失责任设有限制和排除。具体范围必须读完整条文和当地强制性法律。 | 业务、保险和服务连续性评估不要假设 Apple 承担 App 运营损失。 |
| 14. 一般法律条款 | 涵盖第三方声明、独立开发、通知、可分割性、弃权、出口管制、政府终端用户、争议解决与准据法、完整协议和管辖语言等。 | 检查本地出口和制裁义务以及适用法律。不要把营销说明或口头沟通当成协议修订。 |

## 附表

| 文件 | 作用 | 需核查事项 |
| --- | --- | --- |
| Schedule 1，App Store 免费 App 分发 | Apple 作为代理或佣金商营销和交付 App。涵盖提交、地区、元数据、EULA、权利声明、撤回、法律责任和 App Store 可发现性。 | 发行区域、产品信息、隐私政策、EULA、出口与知识产权。Exhibit D 写明 Apple 不保证展示、精选或排名。 |
| Schedule 2，付费 App 与 IAP | 适用于收费 App 和通过 Apple In-App Purchase 销售的商品或服务。规定交易、佣金、退款、税务、收入结算和订阅。 | 店面、程序资格、佣金与税费、IAP 交付和退款责任。2026-10 修订涉及 Group Purchases 多席位。2026-11 公告新增订阅取消流程中的挽留信息，见[挽留信息公告](https://developer.apple.com/news/?id=fk9ps3gv)。 |
| Schedule 3，Custom App Distribution | 适用于通过 Custom App Distribution 向指定机构客户分发的 App。规定客户、交付、收费、税务和责任。 | 客户名单与组织、私有分发、订单与付款、EULA、税务。2026-10 修订涉及 Apple Business Manager 与 Apple School Manager 的批量购买订阅。 |

## 附件

协议页面包含 14 个附件。它们在使用相应能力或进入对应地区、商业模式时适用，被引用后与主协议一起约束开发者。

| 附件 | 主题 | 执行重点 |
| --- | --- | --- |
| 1 | Apple 推送通知服务与本地通知 | Push Application ID、用户选择加入、通知数据用途和服务限制。 |
| 2 | In-App Purchase API | 收据验证、商品交付、退款、群组购买、税务和 API 限制。 |
| 3 | Game Center | 用户内容、玩家交互、服务安全，以及 Apple School Manager 与 Business Manager 批量订阅。 |
| 4 | iCloud | iCloud 与 CloudKit 的数据用途、存储和访问限制。 |
| 5 | Wallet Passes | Pass 内容、签名、分发方式和用户体验要求。 |
| 6 | Apple 地图、MapKit、MapKit JS | 地图数据用途、展示与归属要求，以及当地法律。 |
| 7 | Safari 扩展 | 扩展签名、分发、功能与隐私要求。 |
| 8 | WeatherKit | 天气数据和 API 的用途、展示、配额与地区法律。 |
| 9 | Apple Developer App 订阅 | 通过 Developer App 购买会员或其他订阅时的附加购买条款。 |
| 10 | 移动设备管理（MDM） | 仅可在授权场景使用。配置描述文件、设备管理和隐私责任。 |
| 11 | EnergyKit | 仅限符合条件的汽车或恒温器开发者。数据不得用于无关广告、画像或模型训练。 |
| 12 | 日本、巴西 iOS App | 替代市场、替代付款、站外优惠，以及相应 entitlement 和地区约束。**地区敏感。** |
| 13 | 中国大陆 iOS/iPadOS App | 中国大陆店面佣金与付款条款。快照记录标准佣金 25%，符合条件的项目适用 12%。**地区敏感。** 以账户内当前费率为准，不要外推。 |
| 14 | 欧盟 App | 替代分发、替代付款、站外优惠和 EU business terms。页面写明 2026-10-01 或签署日（以较晚者为准）生效。**地区敏感。** |

## 2026-10-13 修订

[更新公告](https://developer.apple.com/news/?id=17mwd36z)列出下列变化。这里是工作摘要，不代替条款原文。中文是编辑摘要。

1. **第 3.2 节，安全：** 更新使用 Apple 软件和服务的安全及相关要求。安全评审应检查权限、凭证、用户数据流、恶意行为和平台防护。
2. **第 3.3.8(j)/(k) 节：** 明确 Live Assistance API 和 App Replacement Entitlement 的使用条款。使用前核对实际资格、API 文档和用户体验要求。
3. **第 6.4–6.4.2 节，CarPlay 与 Apple HomeView：** iOS App 小组件可能出现在 CarPlay 和 Apple HomeView。开发者要判断小组件是否适合驾驶场景；不适合的可通过 `disfavoredLocations` 标注。具备指定 CarPlay entitlement 的 App 也可能出现在配对设备的 Apple HomeView 中。
4. **Schedule 2，Group Purchases：** 明确通过群组购买为订阅提供多个席位的销售与服务安排。
5. **Schedule 3，批量购买：** 明确通过批量购买向 Apple Business Manager 和 Apple School Manager 组织提供多席位订阅。
6. **Schedule 2 与 Schedule 3 的税务信息：** Apple 可向税务机关报告法律要求的信息。开发者收到的顾客税务信息只能用于法律规定的用途。
7. **接受：** 公告要求开发者登录账户接受更新条款。第 4 节说明，不接受新条款可能导致相关软件、证书或服务被暂停或终止。

企业与学校多席位购买的产品公告见[2026-10-22 公告](https://developer.apple.com/news/?id=yfo21au)。

## 2026-10-29 台湾店面修订

[Apple 公告](https://developer.apple.com/news/?id=w9mxlhek)说明：自 **2026-10-31** 起，台湾 iOS/iPadOS App Store 店面中，标准 App 内购买和付费 App 交易的佣金由 **30% 调整为 26%**。Apple 同时修订了开发者计划许可协议。公告写明，不必在 10 月 31 日前签署更新条款才能获得该费率调整。**地区敏感。**

- [ ] 若产品在台湾店面销售，复核收入预测、税务与结算报表，以及适用的协议附表。
- [ ] 不把台湾店面费率变化外推到其他地区或其他交易类型。以 App Store Connect 当前账户数据和最新协议为准。

## 高优先级检查

下列各项是执行提示。

- [ ] 确认签约主体、账户持有人和 App Store Connect 角色正确。团队成员、外包和服务商只获得必要权限。
- [ ] 盘点所有 Apple API、entitlement、系统数据与服务。为每项记录准入条件、用途限制、用户披露、同意方式和数据生命周期。
- [ ] 只使用文档化 API，并按规定用途处理数据。健康、位置、通信、设备识别、语音、AI 或模型、Wi-Fi 等数据可能有额外约束。
- [ ] 对 Foundation Models Framework 保留合理安全防护，并遵循其可接受使用要求。
- [ ] 保护签名证书、私钥、Provisioning Profile、App Store Connect API 密钥和 Push ID。建立轮换与泄露响应。
- [ ] 每个 App 都完成适用法律、隐私政策、知识产权、出口与加密、年龄分级和产品支持检查。Apple 审核通过不能替代这些责任。
- [ ] 核对全部分发路径。App Store、Custom App Distribution、TestFlight、Ad Hoc、网页或替代市场分别对应不同的计划条款、地区条款和 entitlement。
- [ ] 对收费 App、IAP、订阅、团购与多席位、替代支付和 Custom Apps，检查正确的 Schedule、附件、佣金、税务、退款和用户支持安排。
- [ ] **地区敏感：** 中国大陆发行时核对 Attachment 13 与 App Store Connect 当前费率。欧盟、日本、巴西发行时核对适用的地区附件和授权。
- [ ] 收到新协议或 Program Requirements 时，记录生效日、影响面、接受人、接受时间和上线所需动作。
- [ ] 对 2026 年 10 月修订，检查产品是否使用 Live Assistance API、App Replacement Entitlement、CarPlay 或 HomeView 小组件，以及多席位订阅。
- [ ] **地区敏感：** 若在台湾 iOS/iPadOS 店面销售标准 IAP 或付费 App，核对 26% 费率、税务与结算记录，以及当前协议状态。不要把台湾调整外推到其他店面。

## 适用范围

本摘要侧重 App Store 上架、App Store Connect、IAP 与订阅、证书、隐私和地区附件。协议还覆盖 Wallet、APNs、Game Center、iCloud、MapKit、WeatherKit、MDM、Safari 扩展、EnergyKit 等主题。使用这些能力时应直接阅读相应附件和 API 文档。

协议页列出的 App Store 可发现性因素包括文本相关性、元数据、评分与评论、下载和上架时间等。Apple 不承诺特定展示或排名。

上架勾选见[上架前检查清单](../pre-submission/submission-checklist.zh-CN.md)。年龄分级见[年龄分级主题](../age-ratings/age-ratings.zh-CN.md)。

本页不代替[当前英文协议](https://developer.apple.com/cn/support/terms/apple-developer-program-license-agreement/)或账户中的待接受条款。快照记录该 `/cn/` 路径在 2026-11-09 显示的是英文正文。
