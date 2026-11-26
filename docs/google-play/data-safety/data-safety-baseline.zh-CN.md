---
id: google-play.data-safety.baseline
platform: google-play
language: zh-CN
authority: normative
status: current
kb_checked_at: 2026-11-26
review_due: 2027-02-26
regions: [global]
topics: [data-safety, privacy, sdk, disclosure]
---

# Google Play Data Safety 基线

## 核心原则

Data Safety 表单必须反映 App 和全部第三方 SDK 在运行时真实收集、共享、使用和删除数据的情况。它不是只根据代码静态猜测，也不能只看隐私政策。

## 检查范围

- App、后端、分析、广告、登录、支付、客服和外部服务。
- SDK 的数据类型、传输时机、处理目的、共享对象和是否加密。
- 账户创建、账户删除、备份、缓存、日志、崩溃分析和设备标识符。
- 儿童、健康、位置、通讯录、照片/视频、短信/通话记录和无障碍功能。
- 数据删除请求、保留例外、撤回同意后的行为和地区差异。

## 提交流程

先建立数据流和 SDK 清单，再逐项回答收集/共享问题，最后将表单结果与 App、后端和隐私政策做一致性复核。任何无法确认的 SDK 行为都应进入风险清单，不应默认回答“否”。

## 相关政策边界

Data Safety 申报不替代 User Data policy、敏感权限政策、儿童政策、账户删除要求或当地法律。Android 实现指南也不自动赋予 Play 资格。

## 官方来源

- [User Data policy](https://support.google.com/googleplay/android-developer/answer/10144311)
- [Data safety section](https://support.google.com/googleplay/android-developer/answer/10787469)
- [Google Play Policy Center](https://play.google.com/about/developer-content-policy/)

## 同目录详细专题

[Data safety 表单详解](data-safety.zh-CN.md) 来自 2026-10-24 快照，核对日为 2026-10-24。它覆盖表单分类、FAQ 和来源审计。本基线不替换该详解，两页的核对日也不同。政策义务见[用户数据](../user-data/user-data.zh-CN.md)。表单申报不替代该政策。

本页是执行摘要，发布前必须核对当前 Play Console 表单和官方页面。
