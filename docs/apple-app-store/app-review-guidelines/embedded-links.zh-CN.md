---
id: apple.app-review.embedded-links
platform: apple
language: zh-CN
authority: operational
status: partial
kb_checked_at: 2026-11-09
review_due: 2027-02-09
snapshot_package: 2026-11-10
regions: [global]
topics: [review, sources, guidelines]
editorial_note: "Operational link catalog, not a policy rule. The catalog crawl inside the snapshot is dated 2026-10-21. kb_checked_at is the package check 2026-11-09. This import did not re-crawl the links. English guidelines in the snapshot are dated 2026-10-16; the Simplified Chinese official page shows 2026-06-08. Some form URLs did not resolve, and some design links returned a crawler 404. The supplied /cn/ license URL rendered English on 2026-11-09; that later fact is noted below and does not rewrite the 2026-10-21 catalog row."
---

# 指南正文嵌入链接目录 / Embedded Links Index

## 这页是什么

本页是操作性链接目录，不是审核规则。它收录两页指南**正文以及“提交前 / 提交后”内容中的直接链接**，重复目标已合并。页眉、页脚、全站菜单、同页章节锚点和链接目标页里的二级链接不算正文嵌入链接。

英文链接是便于核对的规范来源。快照确认过的中文页面一并列出。列出某个资源，不表示该功能适用于每个 App 或每个店面。

目录自身的抓取日期是 **2026-10-21**。知识库核查日 `kb_checked_at` 用快照包的核对日 **2026-11-09**（包日期 2026-11-10）。本次导入没有重新抓取这些链接。

来源页：

- [App Review Guidelines（英文）](https://developer.apple.com/app-store/review/guidelines/)，快照中的页面日期 2026-10-16
- [App 审核指南（简体中文）](https://developer.apple.com/cn/app-store/review/guidelines/)，快照中仍显示 2026-06-08

英文页是当前政策基准。中文官方页是较旧译文。指南 2.3.14 的创意素材链接在本次抓取中只出现在英文指南；中文指南当时尚未更新。规则摘要见[审核指南摘要](guidelines-summary.zh-CN.md)。

## 1. 分发、公证与上架资格

| 主题 | 英文来源 | 中文来源 | 指南位置 |
| --- | --- | --- | --- |
| 替代 App 市场 | [Apple Developer Documentation](https://developer.apple.com/documentation/marketplacekit/participating-in-alternative-distribution-for-specific-regions) | 该中文指南页链接到同一英文文档 | 简介 |
| 网站分发 | [Apple Developer Documentation](https://developer.apple.com/documentation/marketplacekit/distributing-your-app-from-your-website) | 该中文指南页链接到同一英文文档 | 简介 |
| iOS/iPadOS App 公证提交 | [App Store Connect Help](https://developer.apple.com/help/app-store-connect/managing-alternative-distribution/submit-for-notarization) | [提交至公证审核](https://developer.apple.com/cn/help/app-store-connect/managing-alternative-distribution/submit-for-notarization) | 简介；适用公证的规则 |
| Entitlements | [Entitlements documentation](https://developer.apple.com/documentation/bundleresources/entitlements) | 页面指向同一英文文档 | 简介；WebKit 替代引擎 |
| App Store Improvements | [App Review Help](https://developer.apple.com/help/app-review/safe-and-trusted-store/app-store-improvements) | [中文版帮助页](https://developer.apple.com/cn/help/app-review/safe-and-trusted-store/app-store-improvements) | 提交前；App 持续维护 |
| 欧盟 App 规则 | [Apple Developer Support](https://developer.apple.com/support/apps-in-the-eu) | [Apple Developer 支持（中文）](https://developer.apple.com/cn/support/apps-in-the-eu) | 分发、付款与地区适用规则 |
| 欧盟/日本替代浏览器引擎授权 | [Using alternative browser engines in the EU](https://developer.apple.com/support/alternative-browser-engines/) | [欧盟替代浏览器引擎（中文）](https://developer.apple.com/cn/support/alternative-browser-engines/) | 2.5.6 Web 浏览器引擎 |

## 2. 提交前、审核材料与开发文档

| 主题 | 英文来源 | 中文来源 | 指南位置 |
| --- | --- | --- | --- |
| 兼容设备测试 | [App Review Help](https://developer.apple.com/help/app-review/before-submitting-for-review/test-compatible-devices) | — | Before You Submit |
| 为审核配置 App 内购买 | [App Review Help](https://developer.apple.com/help/app-review/before-submitting-for-review/configure-in-app-purchases) | — | Before You Submit |
| 完整审核所需信息与监管文件 | [App Review Help](https://developer.apple.com/help/app-review/before-submitting-for-review/complete-review) | — | Before You Submit；所需文件链接解析到此帮助主题 |
| SwiftUI | [Apple Developer Documentation](https://developer.apple.com/documentation/swiftui) | 页面指向同一英文文档 | Developer documentation |
| 公共 API 文档入口 | [Documentation](https://developer.apple.com/documentation/) | 中文指南指向同一文档入口 | 2.5.1 Public APIs |
| UIKit | [Apple Developer Documentation](https://developer.apple.com/documentation/uikit) | 页面指向同一英文文档 | Developer documentation |
| AppKit | [Apple Developer Documentation](https://developer.apple.com/documentation/appkit) | 页面指向同一英文文档 | Developer documentation |
| App 扩展 | [Apple Developer Documentation](https://developer.apple.com/documentation/technologyoverviews/app-extensions) | 页面指向同一英文文档 | Developer documentation；扩展 |
| iCloud 备份数据优化 | [Apple Developer Documentation](https://developer.apple.com/documentation/foundation/optimizing-your-app-s-data-for-icloud-backup) | 页面指向同一英文文档 | Developer documentation |
| Apple 文件系统 | [Apple Developer Documentation](https://developer.apple.com/documentation/foundation/about-apple-file-system) | 页面指向同一英文文档 | Developer documentation；macOS sandbox |
| App Store Connect 帮助 | [Help center](https://developer.apple.com/help/app-store-connect/) | [App Store Connect 帮助（中文）](https://developer.apple.com/cn/help/app-store-connect/) | Before You Submit |
| App Review 帮助 | [Help center](https://developer.apple.com/help/app-review/) | [App 审核帮助（中文）](https://developer.apple.com/cn/help/app-review/) | 提交前 / 提交后 |
| 开发者账户帮助 | [Help center](https://developer.apple.com/help/account/) | [开发者账户帮助（中文）](https://developer.apple.com/cn/help/account/) | Before You Submit |
| 人机界面指南 | [Apple Design](https://developer.apple.com/design/human-interface-guidelines/) | [中文指南入口](https://developer.apple.com/cn/design/human-interface-guidelines/) | Before You Submit；Apple Pay；位置；Apple 产品 |
| App Store 营销资源和识别标志 | [Apple Developer](https://developer.apple.com/app-store/marketing/guidelines/) | [中文指南](https://developer.apple.com/cn/app-store/marketing/guidelines/) | Before You Submit |
| Apple Pay 营销指南 | [Apple Developer](https://developer.apple.com/apple-pay/marketing/) | [中文指南](https://developer.apple.com/cn/apple-pay/marketing/) | Before You Submit；Apple Pay |
| “添加到 Apple 钱包”徽章指南 | [Apple Developer](https://developer.apple.com/wallet/add-to-apple-wallet-guidelines/) | [中文指南](https://developer.apple.com/cn/wallet/add-to-apple-wallet-guidelines/) | Before You Submit；Wallet passes |
| Apple 商标与版权使用指南 | [Apple Legal](https://www.apple.com/legal/intellectual-property/guidelinesfor3rdparties.html) | [Apple 法律（中文）](https://www.apple.com.cn/legal/intellectual-property/guidelinesfor3rdparties.html) | Before You Submit；知识产权 |
| 儿童安全与适龄体验 | [Apple Developer](https://developer.apple.com/kids/) | [Apple 开发者（中文）](https://developer.apple.com/cn/kids/) | 1.3 Kids Category；家长门 |

## 3. 商店展示、元数据与发现

| 主题 | 英文来源 | 中文来源 | 指南位置 |
| --- | --- | --- | --- |
| 推广 App 内购买项目 | [Apple Developer](https://developer.apple.com/app-store/promoting-in-app-purchases/) | [中文指南](https://developer.apple.com/cn/app-store/promoting-in-app-purchases/) | 2.3.2 |
| StoreKit 交易处理 | [Apple Developer Documentation](https://developer.apple.com/documentation/storekit/skpaymenttransactionobserver/paymentqueue(_:shouldaddstorepayment:for:)) | 页面指向同一英文文档 | 2.3.2 |
| 截图展示实际使用 | [App Review Help](https://developer.apple.com/help/app-review/guideline-reference/2-3-3-screenshots) | — | 2.3.3 |
| App Store 类别 | [Apple Developer](https://developer.apple.com/app-store/categories/) | [中文页面](https://developer.apple.com/cn/app-store/categories/) | 2.3.5 |
| App 内活动 | [Apple Developer](https://developer.apple.com/app-store/in-app-events/) | [中文页面](https://developer.apple.com/cn/app-store/in-app-events/) | 2.3.13 |
| App Store 创意素材最佳实践 | [Apple Developer](https://developer.apple.com/app-store/asset-best-practices/) | —（英文指南 2026-10 新增 2.3.14；本次抓取的中文指南仍待更新，正文没有对应中文链接） | 2.3.14 |
| 设备兼容与多平台 App | [Xcode documentation](https://developer.apple.com/documentation/xcode/configuring-a-multiplatform-app-target) | 页面指向同一英文文档 | 2.4.1 |
| macOS 文件与目录 | [File System Programming Guide（存档）](https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/FileSystemProgrammingGuide/Introduction/Introduction.html) | 页面指向同一英文存档 | 2.4.5 |

## 4. 付款、订阅与商业模式

本节只登记指南正文里的直接链接。它不是 IAP、订阅、外部购买或地区条款专题。那些专题不在本次快照包中。

| 主题 | 英文来源 | 中文来源 | 指南位置 |
| --- | --- | --- | --- |
| 收据验证 | [Apple Developer Documentation](https://developer.apple.com/documentation/storekit/choosing-a-receipt-validation-technique) | 页面指向同一英文文档 | 3.1.1 试用 / 访问管理 |
| DeviceCheck | [Apple Developer Documentation](https://developer.apple.com/documentation/devicecheck) | 页面指向同一英文文档 | 3.1.1 试用 / 访问管理 |
| External Purchase API | [Apple Developer Documentation](https://developer.apple.com/documentation/storekit/external-purchase) | 页面指向同一英文文档 | 3.1.1(a) |
| 跨多个 App 提供订阅 | [Apple Developer Documentation](https://developer.apple.com/documentation/storekit/offering-a-subscription-across-multiple-apps) | 页面指向同一英文文档 | 3.1.2 |
| 自动续期订阅 | [Apple Developer](https://developer.apple.com/app-store/subscriptions/) | [中文页面](https://developer.apple.com/cn/app-store/subscriptions/) | 3.1.2 |
| Apple Developer Program 许可协议 | [Current agreement](https://developer.apple.com/support/terms/apple-developer-program-license-agreement/) | [快照所记中文路径](https://developer.apple.com/cn/support/terms/apple-developer-program-license-agreement/) | 3.1.2(c)；隐私；费用与条款 |
| 阅读器 App 外链账户授权 | [Apple Developer Support](https://developer.apple.com/support/reader-apps/) | [中文支持页](https://developer.apple.com/cn/support/reader-apps/) | 3.1.3(a) |
| 非营利组织 Apple Pay 捐赠 | [Apple Developer](https://developer.apple.com/apple-pay/nonprofits/) | — | 3.2.1 |

2026-10-21 的目录把 `/cn/` 协议路径记为中文来源列。随后在 2026-11-09 核对许可协议时，该 URL 显示的是英文正文。中文列因此不能当成 Apple 已发布的中文协议。详见[许可协议摘要](../developer-program/license-agreement.zh-CN.md)。

## 5. 设计、第三方服务与平台 API

| 主题 | 英文来源 | 中文来源 | 指南位置 |
| --- | --- | --- | --- |
| 防止仿冒 / 抄袭拒审 | [App Review Help](https://developer.apple.com/help/app-review/guideline-reference/4-1-prevent-copycat-rejection) | — | 4.1 |
| App Extension Programming Guide | [Apple Developer Archive](https://developer.apple.com/library/archive/documentation/General/Conceptual/ExtensibilityPG/index.html) | — | 4.4 |
| Safari App Extensions | [Apple Developer Documentation](https://developer.apple.com/documentation/safariservices/safari-app-extensions) | 页面指向同一英文文档 | 4.4 |
| Safari Web Extensions | [Apple Developer Documentation](https://developer.apple.com/documentation/safariservices/safari-web-extensions) | 页面指向同一英文文档 | 4.4 |
| MusicKit | [Apple Developer](https://developer.apple.com/musickit/) | [MusicKit 中文](https://developer.apple.com/cn/musickit/) | 4.5.2 |
| Apple Music Identity Guidelines | [Apple Marketing](https://marketing.services.apple/apple-music-identity-guidelines) | — | 4.5.2 |
| 保护用户隐私 | [UIKit documentation](https://developer.apple.com/documentation/uikit/protecting-the-user-s-privacy) | 页面指向同一英文文档 | 5.1 隐私 |
| HIG 隐私 / 位置设计参考 | [指南中的 HIG 路径](https://developer.apple.com/design/human-interface-guidelines/patterns/accessing-private-data/) | [中文隐私指南入口](https://developer.apple.com/cn/design/human-interface-guidelines/privacy) | 5.1.5 位置；所链接路径在本次抓取返回 crawler 404 |
| HIG 健身圆环设计参考 | [指南中的 HIG 路径](https://developer.apple.com/design/human-interface-guidelines/patterns/workouts/) | —（未确认中文目标） | 5.2.5 Apple 产品；所链接路径在本次抓取返回 crawler 404 |
| 清楚撰写用途字符串 | [App Review Help](https://developer.apple.com/help/app-review/guideline-reference/5-1-1-purpose-strings) | — | 5.1.1(ii) |
| App 内提供账户删除 | [App Review Help](https://developer.apple.com/help/app-review/guideline-reference/5-1-1-account-deletion) | [中文帮助页](https://developer.apple.com/cn/help/app-review/guideline-reference/5-1-1-account-deletion) | 5.1.1(v) |
| 用户隐私和数据使用 | [Apple Developer](https://developer.apple.com/app-store/user-privacy-and-data-use/) | [中文页面](https://developer.apple.com/cn/app-store/user-privacy-and-data-use/) | 5.1.2 与隐私 |
| CallKit | [Apple Developer Documentation](https://developer.apple.com/documentation/callkit) | 页面指向同一英文文档 | 2.5.12 |
| HealthKit | [Apple Developer Documentation](https://developer.apple.com/documentation/healthkit) | 页面指向同一英文文档 | 5.1 健康数据 |
| ClassKit | [Apple Developer Documentation](https://developer.apple.com/documentation/classkit) | 页面指向同一英文文档 | 2.5.18 广告定向 |
| ARKit | [Apple Developer Documentation](https://developer.apple.com/documentation/arkit) | [ARKit 中文](https://developer.apple.com/cn/documentation/arkit) | 2.5.13 面容认证 |
| WeatherKit | [Apple Developer](https://developer.apple.com/weatherkit/) | [WeatherKit 中文](https://developer.apple.com/cn/weatherkit/) | 5.2.5 Apple 天气署名 |
| NEVPNManager | [Apple Developer Documentation](https://developer.apple.com/documentation/networkextension/nevpnmanager) | 页面指向同一英文文档 | 5.4 VPN |
| Apple 知识产权争议表单 | [Apple Legal](https://www.apple.com/legal/intellectual-property/dispute-forms/index.html) | [Apple 法律（中文）](https://www.apple.com.cn/legal/intellectual-property/dispute-forms/) | 5.2 知识产权投诉 |
| Matter 认证机构 | [CSA-IoT](https://csa-iot.org/) | [CSA-IoT 中文](https://csa-iot.org/zh-CN/) | 2.5.17 Matter |

## 6. 审核后沟通与申诉

| 主题 | 英文来源 | 中文来源 | 指南位置 |
| --- | --- | --- | --- |
| App Review 概览 | [Apple Developer](https://developer.apple.com/distribute/app-review/) | [中文版概览](https://developer.apple.com/cn/distribute/app-review/) | After You Submit |
| 跟踪审核状态 | [App Review Help](https://developer.apple.com/help/app-review/after-submitting-for-review/review-status) | — | After You Submit |
| 申请加急审核 | [App Review Help](https://developer.apple.com/help/app-review/after-submitting-for-review/request-expedited-review) | — | After You Submit |
| 联系 App Review | [App Review Help](https://developer.apple.com/help/app-review/after-submitting-for-review/contact-app-review) | — | After You Submit |
| 向 App Review Board 申诉 | [App Review Help](https://developer.apple.com/help/app-review/after-submitting-for-review/appeal-to-the-app-review-board) | — | After You Submit |
| 建议修改审核指南 | [App Review Help](https://developer.apple.com/help/app-review/after-submitting-for-review/improve-guidelines) | — | After You Submit |
| 接受错误修复提交 | [App Review Help](https://developer.apple.com/help/app-review/after-submitting-for-review/bug-fix-submissions) | — | After You Submit |
| 2026-10 更新公告 | [Apple Developer News](https://developer.apple.com/news/?id=92th7e5i) | — | Last Updated；当时记录的最新规则变更 |
| 2026-06 中文更新公告 | [英文公告](https://developer.apple.com/news/?id=a233fmpw) | [中文版更新公告](https://developer.apple.com/cn/news/?id=a233fmpw) | 中文指南页的“最后更新”链接 |

本次抓取没有解析出下列表单或入口的 URL，因此不记录猜测地址：

| 主题 | 抓取结果 | 当前可核对的帮助页 |
| --- | --- | --- |
| 加急审核申请表 | 英文和中文指南里的表单链接都未能解析 | [申请加急审核](https://developer.apple.com/help/app-review/after-submitting-for-review/request-expedited-review) |
| 申诉入口 | 英文和中文指南里的入口链接都未能解析 | [向 App Review Board 申诉](https://developer.apple.com/help/app-review/after-submitting-for-review/appeal-to-the-app-review-board) |
| 指南修改建议表单 | 英文和中文指南里的表单链接都未能解析 | [建议修改审核指南](https://developer.apple.com/help/app-review/after-submitting-for-review/improve-guidelines) |

申诉流程的知识库说明见[拒审与申诉](../../operations/rejection-and-appeals/README.md)。那一页是内部流程，不是 Apple 申诉正文。

## 链接核对备注

- 部分 Apple Developer Documentation 页面在普通浏览器里需要 JavaScript。抓取工具可能只看到壳页面，即使链接本身可以解析。
- 本次核对中，少数指南里的设计或文档链接返回 crawler 404，或只返回需要 JavaScript 的壳。目标 URL 在指南正文中可见时，目录仍保留该 URL。投入使用前应在浏览器里再核对。
- 付款、替代分发、订阅、隐私和地区资源可以独立于指南正文变化。把某条规则用于一次发布时，重新核对链接页和协议。
- 公告正文里的另一套链接在[新闻目标页分析](../news/news-link-targets.zh-CN.md)，不要和本目录混成同一份清单。
