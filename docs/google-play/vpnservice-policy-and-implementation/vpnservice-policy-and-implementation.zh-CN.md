---
id: google-play.vpnservice-policy-and-implementation
platform: google-play
language: zh-CN
authority: normative
status: current
kb_checked_at: 2026-10-24
review_due: 2027-01-24
regions: [global]
topics: [vpnservice, vpn, permissions, user-data, networking]
snapshot_id: play.vpnservice-policy
snapshot_package: "GooglePlay-KnowledgeBase-2026-10-24-review.zip"
coverage_status: "detailed-summary"
source_url: "https://support.google.com/googleplay/android-developer/answer/12564964?hl=en"
source_url_android_guide: "https://developer.android.com/develop/connectivity/vpn"
effective_date: "current-policy; 2023-08-31 declaration date is historical"
---

# Google Play VpnService 政策与 Android VPN 实现

> **导入说明（Google batch 5）。** 正文来自已经分开的 2026-10-24 Google Play 知识库快照（`play.vpnservice-policy`，核对日 2026-10-24）的改写摘要，不是官方页面的逐字副本。英文官方页面是效力来源。`kb_checked_at` 是快照源文件记录的核对日；本次导入没有重新打开线上官方页面。文中“本知识库”“本库”“本地专题”等说法描述的是该快照库的覆盖范围，不是本仓库已经导入的页面。指向本仓库没有收录的专题、链接图、台账或 CSV 的相对链接改为文字提及。指向 Google batch 1–4 或本批八个专题的相对链接改为本仓库文件。 两种语言文件记录的都是英文 Play 说明页 `hl=en` 和 Android VPN 指南。快照称本页为双语改写，没有记录已核对的中文官方 VpnService 帮助页，也没有记录该主文章 `hl=zh-CN` 抓取失败。本仓库中文正文是快照的编辑改写，不是 Google 已发布的中文页面文本。说明页上的 2023-08-31 申报日期是已经过去的历史日期，不免除现行申报。快照没有记录未来生效的 Play 日期。标注为 Permissions 的正文链接返回 Internal Error，且没有暴露目标地址；已导入的敏感权限专题只是相关背景，不是已证实的重定向。该访问限制不是政策变更。Play 的资格、商品详情、加密、披露、同意和 Console 申报是 `normative`。`VpnService`、始终开启 VPN、按应用路由和 ToyVpn 是 Android 实现说明。技术上正确的隧道不是 Play 批准。

> **先区分两条规则线：** Google Play 页面决定应用能否使用 `VpnService`、需要怎样申报和披露；Android Developers 页面说明系统 API、网络路由和服务生命周期。实现符合 Android 指南，不等于通过 Play 政策审核。

## 1. Play 的用途资格与强制要求

Google Play 说明页称，只有 VPN 是应用核心功能，或应用的核心功能确实需要远程服务器，才可使用 `VpnService` 创建设备级隧道。页面列出的用途类别包括：

- 家长控制与企业设备管理；
- 应用使用情况跟踪；
- 设备安全，例如防病毒、移动设备管理和防火墙；
- 网络工具，例如远程访问；
- 网页浏览器；
- 为电话或网络连接提供服务、且确实需要 VPN 功能的运营商应用。

类别必须与实际核心用途相符；落在列表里本身不代表自动获批。Play 页面要求所有使用 `VpnService` 的应用提交 Play Console 声明。说明页里的 **2023-08-31** 是已经过去的历史期限，不代表现在可免申报。

所有使用应用都必须：

1. 在 Google Play 商品详情中说明 `VpnService` 的用途；
2. 加密设备到 VPN 隧道端点之间的数据；
3. 遵守开发者计划政策，包括广告欺诈、权限和恶意软件规则。

不得在没有醒目披露和同意的情况下收集个人或敏感数据；不得为变现目的重定向或操纵设备上其他应用的用户流量。页面举例说明，改变广告流量的地域路由或以其他方式影响广告变现会导致拒绝。

若核心用途不属于列出的类别，声明表要求解释为何仍符合标准；否则应从所有有效发布制品和所有发布轨道移除 VPN 服务。不要仅从当前生产轨道删除而遗漏测试轨道或其他仍有效的制品。

## 2. 醒目披露、同意与申报视频

当应用通过 `VpnService` 访问或收集个人/敏感数据时，Play 的 User Data 要求醒目披露和肯定式同意。披露应：

- 在应用内、正常使用流程中出现，不要求用户先进入菜单或设置；
- 说明通过 `VpnService` API 访问或收集的数据，以及数据如何使用或分享；
- 单独解释应用为何需要 `VpnService` 及可能的使用方式，不与其他敏感数据披露合并；
- 让用户采取明确的肯定动作同意；隐私政策、服务条款、商品详情或网站不能代替应用内披露。

声明预览区分了两类视频材料：一段不超过 90 秒的视频展示打开应用并实际使用 VPN；数据披露视频应展示完整披露内容、同意后授予 VPN 权限的流程，以及不同意后退出/返回并再次查看披露的流程。若 VPN 用途不容易从画面看懂，应添加旁白或字幕。表单还会询问使用 `VpnService` 收集/分享的数据类别，以及是否为变现而操纵其他应用流量。

如果 API 的实际用途发生变化，必须重新提交准确的声明。说明页指出，欺骗性或未申报使用可能导致应用暂停，严重时终止开发者账号。提交声明不代表已经获批；应在 Console 确认账号内的当前状态。

## 3. Android 实现与用户控制

Android 的 VPN 服务应继承 `VpnService`，并在 Manifest 中以 `android.permission.BIND_VPN_SERVICE` 保护服务，声明 `android.net.VpnService` intent filter。连接流程按系统指南组织：

1. 用户主动请求连接时调用 `VpnService.prepare()`；若系统返回授权 Intent，先完成系统确认流程。每次连接前都重新检查，因为用户可能已将授权交给另一 VPN 应用；同一时刻只有一个已准备的 VPN 应用。
2. 创建通往 VPN 网关的隧道 socket 后调用 `VpnService.protect()`，避免隧道 socket 被送回自身 TUN 接口形成循环；再将 socket 连接到网关。
3. 用 `VpnService.Builder` 配置本地 TUN 地址、路由和 DNS，再调用 `establish()` 建立接口。应用读取从设备发出的 IP 包、加密后送往网关，并把从网关收到且解密的包写回接口。
4. `protect()` 失败时应停止连接流程；该调用在应用尚未获授权或授权被撤销时会失败，也不会替应用关闭 socket。

Android 指南要求 VPN 网关之间使用强加密。应用还应提供可见的手动启动/停止控制，并在服务活动期间显示不可划除通知；系统设置、Quick Settings 与状态栏 VPN 图标也会帮助用户识别当前连接。每个用户或工作资料同一时刻只有一个活动 VPN 服务，启动另一个服务会停止已有服务。

`onRevoke()` 调用时系统已经停用 VPN 接口；回调可能不在主线程。应用应安全关闭隧道 socket 和 `ParcelFileDescriptor`，停止服务并有序清理状态。Android 8.0/API 26 及以上，系统从后台启动服务时，指南要求服务及时调用 `Service.startForeground()`。始终开启 VPN 可从 Android 7/API 24 起用；锁定模式可阻断所有不经 VPN 的连接。Android 指南建议在启用允许/排除应用名单或锁定模式时，向用户解释名单外应用可能失去网络连接。

## 4. 始终开启、分应用路由与 Builder 细节

- 分应用 VPN 只能配置允许名单或排除名单之一，不能同时设置；未配置任何名单时，默认所有应用流量都进入 VPN。名单必须在 `establish()` 前设置；要更改名单，需要建立新的 VPN 连接；加入名单的应用必须已安装。
- 始终开启 VPN 由系统启动和控制。锁定模式会在 VPN 未连接时阻断非 VPN 流量；测试时要覆盖断网、网关不可达、配置更新及用户从系统设置断开的情形。
- 若应用暂不支持始终开启，Android VPN 指南给出的退出方式是在 Android 8.1/API 27 及以上将服务元数据 `android.net.VpnService.SUPPORTS_ALWAYS_ON` 设为 `false`。这只是 Android 功能配置，不是 Play 政策豁免。
- `VpnService.Builder.addAddress()`、`addRoute()` 会开放对应 IPv4/IPv6 地址族；当前 Builder 文档说明路由最长前缀优先。API 33 起 `excludeRoute()` 可排除路由；对同一目的地后续添加的 `addRoute()` 会覆盖排除路由。
- 未配置某一地址族的地址、路由或 DNS 时，该地址族的出站流量默认被阻断；`allowFamily()` 可在无路由时单独开放 IPv4 或 IPv6。`allowBypass()` 允许应用绕过 VPN，改变默认“所有应用均经 VPN”的网络边界；需要将它作为产品行为明确说明并测试。
- 企业部署可通过 Android Enterprise managed configurations 远程配置 VPN。个人资料和工作资料各自受管理员策略、可用应用和跨资料边界影响。

以上均为 Android 平台行为与工程建议。它们不改变 Play 对用途资格、商品详情说明、强加密、数据披露/同意和 Console 声明的要求。

## 5. Play 说明页的正文直链

该页的正文有 **7 次链接引用、6 个不同链接目标**。编号侧栏的 32 个 Help 页面是导航项，单独记录，不计入正文直链数。点击 `Permissions` 正文链接时抓取器返回 Internal Error，且没有暴露目标 URL；下面不猜测其确切跳转地址。当前汇总的[敏感权限专题](../sensitive-permissions/sensitive-permissions.zh-CN.md)是独立核验的相关现行页面，不把它声称为该失败链接已证实的重定向目标。

| 正文目标 | 与 VpnService 规则的关系 | 访问与覆盖 |
| --- | --- | --- |
| [Android `VpnService` API](https://developer.android.com/reference/android/net/VpnService) | API 授权、服务绑定、隧道 socket 保护、撤销和生命周期；见下方 Android 直链表。 | API 正文已打开；重点方法已抽查，通用 API 成员仍部分覆盖。 |
| [Policy Center Help 目录](https://support.google.com/googleplay/android-developer/topic/9858052?hl=en) | 页面称“Developer Program Policies”的导航目标；它是政策目录，不是 VPN 条款本身。 | 目录页已打开；目录内所有政策后代不由此分支宣称已闭合。 |
| [Ad Fraud](https://support.google.com/googleplay/android-developer/answer/9969955?hl=en) | 约束广告流量重定向、点击/展示操纵及广告变现风险。 | 页面已打开并入库；更深通用帮助页仍按逐 URL 台账跟踪。 |
| Permissions | VpnService 说明页正文中的权限政策引用。 | 本次点击返回 Internal Error，没有目标 URL；相关规则见[敏感权限专题](../sensitive-permissions/sensitive-permissions.zh-CN.md)，但两者之间的精确跳转关系未确认。 |
| [Malware](https://support.google.com/googleplay/android-developer/answer/9888380?hl=en) | 约束恶意或有害设备/数据行为，与 VPN 流量处理并行适用。 | 现行页面已打开并入库；更深一般性后代仍部分覆盖。 |
| [User Data](https://support.google.com/googleplay/android-developer/answer/10144311?hl=en)（正文含两次引用） | 决定 VPN 访问/收集个人和敏感数据时的披露、同意、数据使用及分享要求。 | 正文已打开并有双语专题；更深 API、课程和 Console 后代仍部分覆盖。 |

## 6. Android VPN 指南的正文直链

当前 Android 指南正文链接 ID 9–46 共 **38 次引用**：5 个指向本页段落的锚点（Always-on、Per-app、服务生命周期、允许名单、排除名单），另外 33 次外部引用归并为 **18 个不同目标**，其中含一个图示资源。17 个外部 URL 均已打开或尝试；图示点击返回 Internal Error，没有暴露 URL，因此无法为它建立 URL 级审计记录。重复的 API 方法链接按其目标 API 页合并；各方法成员并未因此视为全部审核完成。

| 直接目标（正文链接 ID） | 目标页说明与本分支用途 | 访问状态与边界 |
| --- | --- | --- |
| [Work profiles](https://developer.android.com/work/managed-profiles)（11） | 企业资料由 IT 管理；应用可用性、Intent 跨资料行为和文件分享边界可能变化。与企业 VPN/工作资料隔离相关。 | 正文已打开；该页面自身的测试、Intent、通知和 FileProvider 后代未全部展开。 |
| [`VpnService` API](https://developer.android.com/reference/android/net/VpnService)（12、17、19、31、39） | `prepare()`、`protect()`、`onRevoke()`、服务绑定和始终开启元数据。 | 2,769 行 API 正文已打开；相关方法已查看，其他成员未穷尽。 |
| [`VpnService.Builder` API](https://developer.android.com/reference/android/net/VpnService.Builder)（13、22–24、40–42） | `establish()`、地址/路由、分应用名单、绕过 VPN 及地址族设置。 | 2,411 行 API 正文已打开；上述成员已抽查；其他成员和版本兼容性未穷尽。 |
| VPN 架构图（14，图片） | 展示本地 TUN 接口与网关之间的数据路径。 | 点击返回 Internal Error，确切资产 URL 未暴露；未推断图像内容以外的政策义务。 |
| [Manifest `<service>` 元素](https://developer.android.com/guide/topics/manifest/service-element)（15） | 服务声明、权限和 Intent filter 的 Manifest 结构。 | 页面已打开；通用属性、组件安全性和跨页后代仍部分覆盖。 |
| [`Manifest.permission`](https://developer.android.com/reference/android/Manifest.permission)（16） | `BIND_VPN_SERVICE` 常量和保护权限背景。 | 6,738 行大型 API 目录；仅对相关权限上下文抽查，不能视作全目录已读。 |
| [`DatagramSocket`](https://developer.android.com/reference/java/net/DatagramSocket)（20、32） | 示例隧道 socket 的连接与关闭 API。 | 2,751 行大型 API 页已打开；socket 生命周期以 VPN 指南为主，其他成员未穷尽。 |
| [TUN/TAP 参考页](https://en.wikipedia.org/wiki/TUN/TAP)（21） | 对 TUN 这一虚拟网络接口术语作背景说明。 | 页面已打开；这是第三方百科资料，不作为 Play 政策或 Android 平台规则的权威依据。 |
| [`ParcelFileDescriptor`](https://developer.android.com/reference/android/os/ParcelFileDescriptor)（25、33） | `Builder.establish()` 返回的文件描述符及关闭生命周期。 | 大型 API 参考页已打开；相关关闭流程已从 VPN 指南核对，其他成员部分覆盖。 |
| [`Context`](https://developer.android.com/reference/android/content/Context)（26） | `startService()` 服务启动入口。 | 8,206 行大型 API 参考页已打开；本分支仅记录 VPN 服务启动关系，通用成员未穷尽。 |
| [Services overview](https://developer.android.com/guide/components/services)（27、30） | 服务启动、生命周期及前台服务背景；两次旧入口都重定向至当前 `/develop/background-work/services`。 | 当前目标页已打开，重定向已观察并记入 URL 台账；通用服务类型和后代仍部分覆盖。 |
| [`Service` API](https://developer.android.com/reference/android/app/Service)（28、29） | `onStartCommand()` 与 `startForeground()` 生命周期/API 引用。 | 3,571 行大型 API 页已打开；目标成员语境已记录，其他成员未穷尽。 |
| [Managed configurations](https://developer.android.com/work/managed-configurations)（34） | 企业 IT 管理员为应用远程配置 VPN。 | 页面已打开；配置字段、控制台和企业管理后代仍部分覆盖。 |
| [`Intent` API](https://developer.android.com/reference/android/content/Intent)（35、36） | 启动服务并携带“由应用发起”标记的 Intent。 | 9,795 行大型 API 页已打开；只记录本指南相关调用，其他成员未穷尽。 |
| [`ConnectivityManager`](https://developer.android.com/reference/android/net/ConnectivityManager)（43） | 结合 `allowBypass()` 时，允许进程选择底层或其他网络。 | 3,223 行大型 API 页已打开；目标调用和 API 级别关系仍需逐成员核对。 |
| [`Network`](https://developer.android.com/reference/android/net/Network)（44） | 显式网络绑定与 socket 路由相关 API。 | 2,282 行大型 API 页已打开；未穷尽其成员及兼容性。 |
| [ToyVpn 示例源码目录](https://android.googlesource.com/platform/development/+/master/samples/ToyVpn)（45） | 平台仓库中的示例 VPN 客户端。 | 根目录和主要源文件已跟进；见下方子页清单。可变 `main` 分支不是固定版本。 |
| [Android Developers Content License](https://developer.android.com/license)（46） | 指南与示例相关的内容授权边界。 | 页面已打开；许可证本身的全部链接后代未穷尽。 |

### ToyVpn 示例子页与生产安全边界（2026-10-24）

VPN 指南链接到 ToyVpn 仓库目录。沿该目录的当前 `refs/heads/main` 继续跟进了 README、Manifest、构建文件、Java 客户端/服务/连接代码及 Linux 服务端。目录链接会重定向到下列当前源文件路径；这是一份可变分支快照，不是不可变提交。

| 直接子页 | 读取结果及合规关系 |
| --- | --- |
| [样例说明 `_index.html`](https://android.googlesource.com/platform/development/+/refs/heads/main/samples/ToyVpn/_index.html) | 说明其 API 14 起的示例客户端与 Linux 服务端用 IP-over-UDP 建隧道，并示意相同 VPN 参数下跨网络切换；引用的 [VPN 授权示意图](https://android.googlesource.com/platform/development/+/refs/heads/main/samples/images/vpn-confirmation.png)不可读；不表示样例已满足当前 Play 要求。 |
| [Android.bp](https://android.googlesource.com/platform/development/+/refs/heads/main/samples/ToyVpn/Android.bp) | 使用 `sdk_version: current`，编译 `src/**/*.java`，并指向 Android Apache-2.0 许可。 |
| [AndroidManifest.xml](https://android.googlesource.com/platform/development/+/refs/heads/main/samples/ToyVpn/AndroidManifest.xml) | `minSdkVersion=14`；声明 `FOREGROUND_SERVICE`、`FOREGROUND_SERVICE_SPECIAL_USE`、`INTERNET`；VPN service 使用 `BIND_VPN_SERVICE` 和 `android.net.VpnService` intent filter，且标记 `foregroundServiceType="specialUse"`、子类型值 `vpn`。这是样例配置，不等于目标应用已完成 Play VPN 或前台服务申报。 |
| [`src/` 入口](https://android.googlesource.com/platform/development/+/refs/heads/main/samples/ToyVpn/src/) → [当前 Java 包目录](https://android.googlesource.com/platform/development/+/refs/heads/main/samples/ToyVpn/src/com/example/android/toyvpn) | 入口重定向至示例包目录；该目录列出下方三份 Java 文件。 |
| [ToyVpnClient.java](https://android.googlesource.com/platform/development/+/refs/heads/main/samples/ToyVpn/src/com/example/android/toyvpn/ToyVpnClient.java) | 读写服务端、端口、共享秘密、代理及分应用名单设置；先调用 `VpnService.prepare()`，仅在系统授权结果为成功后启动服务。 |
| [ToyVpnConnection.java](https://android.googlesource.com/platform/development/+/refs/heads/main/samples/ToyVpn/src/com/example/android/toyvpn/ToyVpnConnection.java) | 先 `protect()` 隧道 `DatagramChannel` 再连服务端，收发 TUN 包，并按服务端参数设置地址、路由、DNS、MTU 和允许/排除应用名单。其握手注释明确说该演示把共享秘密以明文发送，未实现相互认证或会话密钥加密。 |
| [ToyVpnService.java](https://android.googlesource.com/platform/development/+/refs/heads/main/samples/ToyVpn/src/com/example/android/toyvpn/ToyVpnService.java) | 创建前台通知、启动/停止连接线程并关闭旧 `ParcelFileDescriptor`；文件中未见显式 `onRevoke()` 覆写。真实应用仍要按 VPN 生命周期正确处理撤销、隧道关闭和重连。 |
| [服务端入口](https://android.googlesource.com/platform/development/+/refs/heads/main/samples/ToyVpn/server/) → [当前 Linux 服务端目录](https://android.googlesource.com/platform/development/+/refs/heads/main/samples/ToyVpn/server/linux)、[目录索引](https://android.googlesource.com/platform/development/+/refs/heads/main/samples/ToyVpn/server/linux/_index.html)、[Makefile](https://android.googlesource.com/platform/development/+/refs/heads/main/samples/ToyVpn/server/linux/Makefile)、[ToyVpnServer.cpp](https://android.googlesource.com/platform/development/+/refs/heads/main/samples/ToyVpn/server/linux/ToyVpnServer.cpp) | 服务端仅提供 Linux/TUN 实现，一次处理一个会话。索引页无可读正文；C++ 源码明确声明它没有强认证或加密，并写明“DO NOT USE IT IN PRODUCTION”。这与 Play 对设备到 VPN 端点之间加密的要求不符，不能把该协议当作上架实现范本。 |
| [`res/` 资源目录](https://android.googlesource.com/platform/development/+/refs/heads/main/samples/ToyVpn/res/) 与 [drawable](https://android.googlesource.com/platform/development/+/refs/heads/main/samples/ToyVpn/res/drawable/)、[layout](https://android.googlesource.com/platform/development/+/refs/heads/main/samples/ToyVpn/res/layout/)、[values](https://android.googlesource.com/platform/development/+/refs/heads/main/samples/ToyVpn/res/values/) | 根资源目录可读并显示三个子目录；三个子目录 URL 均被浏览器工具拒绝，未推测其文件内容。 |
| [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0) | 源文件头部引用的许可证正文已打开；这是源代码许可，不是 Play 政策。 |

另核对了当前 [Android 前台服务类型指南](https://developer.android.com/develop/background-work/services/fgs/service-types)：target Android 14/API 34 及以上时，应用需要声明合适的服务类型及权限，并在 Play Console 的 App content 声明前台服务类型；`specialUse` 面向未被其他类型覆盖的有效用途，Manifest 子类型说明会进入 Play Console 审核。该指南的 `systemExempted` 条件另列出在系统 Settings 中配置的 VPN 应用。ToyVpn 的 Manifest 用 `specialUse`、子类型 `vpn`，与此处分类条件形成需要结合目标应用、目标 SDK 和当前 Console 表单核对的边界；知识库不替开发者推断应改用哪个类型，也不把 AOSP 样例视作审批依据。

**安全结论：** ToyVpn 的价值是演示 `VpnService`/TUN 数据流和生命周期连接点；它自己的客户端握手及 Linux 服务端明确没有强认证、没有加密，不能满足 Play 的 VPN 隧道加密要求。生产应用须另用经设计与审查的安全隧道协议，并单独满足 VPN 用途、披露、同意、声明与前台服务要求。资源子目录、样例引用的通用 API 成员及整个 Git 仓库的其他后代仍未穷尽；精确状态见逐 URL 审计（快照：`../source-page-audit.csv`，未导入本仓库）。

## 7. 上架前复核清单

- [ ] 把 Manifest、合并后的 SDK Manifest、运行时功能与 Play Console 声明逐项比对；确认实际核心用途落在当前允许类别内。
- [ ] 从所有有效 artifact 和所有发布轨道检查 `VpnService`，确认商品详情用途描述、设备到端点加密和声明状态一致。
- [ ] 为每种通过 VPN 的数据类型、数据接收方、用途与分享目的维护清单；在适用时准备单独的应用内醒目披露和肯定式同意。
- [ ] 录制申报视频，覆盖打开应用、VPN 实际功能、完整披露、同意/拒绝两条路径以及如何重新打开披露。
- [ ] 验证 `prepare()` 重新授权、`protect()` 失败、建立/撤销隧道、文件描述符和 socket 关闭、前台通知及始终开启行为。
- [ ] 分别测试 IPv4/IPv6、路由名单、锁定模式、VPN 断开、企业工作资料和分应用 VPN；不得用 Android 系统授权替代 Play 资格判断。

## 覆盖范围与仍待补齐项

Play 说明页的正文直链已逐项记录；5 个可访问目标已打开或与现有双语主题交叉核对，`Permissions` 链接的精确 URL 仍因 Internal Error 未能提取。Android 指南正文的 38 个链接引用已分类，5 个页内锚点与 33 个外部引用分开统计，17 个外部 URL 目标逐一打开或尝试；图示 URL 未暴露。Android API 类库、ToyVpn 源码目录、企业配置、服务/网络 API 的通用后代仍只是相关段落抽查，并未无限递归闭合。逐 URL 状态见来源审计表（快照：`../source-page-audit.csv`，未导入本仓库）；关系和递归分支见链接图（快照：`../google-play-policy-link-graph.md`，未导入本仓库）。

**来源范围：** [Google Play VpnService policy](https://support.google.com/googleplay/android-developer/answer/12564964?hl=en) 与 [Android VPN developer guide](https://developer.android.com/develop/connectivity/vpn)。页面为双语改写和关联分析，不是官方全文或审核保证；提交前请在 Play Console 和官方页面复核当前要求。
