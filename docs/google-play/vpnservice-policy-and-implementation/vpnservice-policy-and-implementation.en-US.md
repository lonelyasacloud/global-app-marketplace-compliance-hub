---
id: google-play.vpnservice-policy-and-implementation
platform: google-play
language: en-US
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

# Google Play VpnService Policy and Android VPN Implementation

> **Import note (Google batch 5).** The body is the paraphrased summary from the already separated 2026-10-24 Google Play knowledge-base snapshot (`play.vpnservice-policy`, reviewed 2026-10-24). It is not a verbatim copy of an official page. The English official source is the source of truth. `kb_checked_at` is the review date recorded in the snapshot source file; this import did not re-open the live official pages. Phrases such as “this knowledge base,” “this library,” and “local topic” describe coverage inside that snapshot, not the set of pages imported into this repository. Relative snapshot links to topics, link graphs, ledgers, or CSVs that are not in this repository are kept as text mentions. Relative links that target the Google batch 1–4 topics or these eight batch 5 topics point at the hub files. Both language files record the English Play explainer `hl=en` and the Android VPN guide. The snapshot calls the page a bilingual paraphrase and does not record a checked Chinese official VpnService Help page or a failed `hl=zh-CN` fetch of that primary article. The Chinese hub text is the snapshot’s editorial paraphrase, not Google’s published Chinese page text. The explainer’s August 31, 2023 declaration date is historical and has passed; it does not waive the current declaration. No future-effective Play date is recorded. The body link labeled Permissions returned Internal Error without exposing a destination; the imported sensitive-permissions topic is related context, not a confirmed redirect. That access limit is not a policy change. Play eligibility, listing, encryption, disclosure, consent, and the Console declaration are `normative`. `VpnService`, always-on VPN, per-app routing, and ToyVpn are Android implementation notes. A technically correct tunnel is not Play approval.

> **Keep the two rule sets separate:** Google Play determines eligibility, declarations, and disclosures. Android Developers documents system APIs, routing, and service lifecycle. A technically correct Android implementation does not establish Play-policy approval.

## 1. Play eligibility and mandatory requirements

Google Play says an app may use `VpnService` to create a device-level tunnel only when VPN is the app's core functionality or its core functionality genuinely requires a remote server. Listed categories include:

- parental control and enterprise management;
- app-usage tracking;
- device-security apps such as antivirus, mobile-device management, and firewalls;
- network tools such as remote access;
- web browsers; and
- carrier apps that need VPN functionality for telephony or connectivity services.

The category must match the app's actual core purpose; appearing in the list does not guarantee approval. The Play explainer says every app using `VpnService` must submit the Play Console declaration. Its **August 31, 2023** date is historical and has passed; it does not waive the current declaration requirement.

Apps using the service must:

1. document its use in the Google Play listing;
2. encrypt data between the device and the VPN tunnel endpoint; and
3. comply with the Developer Program Policies, including Ad Fraud, Permissions, and Malware.

Apps may not collect personal or sensitive data without prominent disclosure and consent, or redirect/manipulate traffic from other apps for monetization. The explainer gives changing the geographic route of ad traffic as an example and warns that ad manipulation affecting monetization leads to rejection.

If the app's core purpose is outside the listed categories, the declaration asks the developer to explain why the use still meets the criteria; otherwise, remove VpnService from all active artifacts across all release tracks. Do not check only the production track while leaving another active artifact or testing track behind.

## 2. Prominent disclosure, consent, and declaration videos

When an app accesses or collects personal or sensitive data through `VpnService`, the Play User Data policy requires prominent disclosure and affirmative consent. The disclosure should:

- appear in the app during normal use, without requiring navigation to a menu or Settings;
- describe data accessed or collected through `VpnService` and how it is used or shared;
- separately explain why the app needs `VpnService` and its potential uses; and
- require a clear affirmative user action. A privacy policy, terms, store listing, or website alone is not enough.

The declaration preview distinguishes two video materials: one video, no longer than 90 seconds, showing the app opening and VPN use; and a data-disclosure video showing the full disclosure, the consent path and VPN authorization, and the decline/return path including how to reopen the disclosure. Add narration or captions when the VPN use is not obvious. The form also asks what data is collected or shared through `VpnService` and whether traffic from other apps is manipulated for monetization.

If API usage changes, submit an updated and accurate declaration. The explainer warns that deceptive or undeclared use may suspend the app and can lead to developer-account termination. Submission is not approval; check the current account-specific state in Play Console.

## 3. Android implementation and user controls

An Android VPN service should extend `VpnService`. In the manifest, protect it with `android.permission.BIND_VPN_SERVICE` and declare the `android.net.VpnService` intent filter. The system guide's connection sequence is:

1. When the user requests a connection, call `VpnService.prepare()`. If Android returns a consent Intent, complete the system confirmation first. Recheck before each connection because the user may have granted VPN control to another app; only one app is prepared at a time.
2. After creating the tunnel socket to the gateway, call `VpnService.protect()` so the socket is not routed back into the app's own TUN interface; then connect the socket to the gateway.
3. Configure the local TUN address, routes, and DNS with `VpnService.Builder`, then call `establish()`. Read outgoing IP packets from the device interface, encrypt them for the gateway, and write decrypted incoming packets back to the interface.
4. If `protect()` fails, stop the connection flow. It fails when the app is not prepared or its authorization was revoked, and it does not close the socket for the app.

Android requires strong encryption between the app and VPN gateway. The app should also provide visible start/stop controls and a non-dismissible notification while the service is active; system Settings, Quick Settings, and the status-bar VPN icon help people identify an active connection. Only one VPN service can run for each user or work profile at a time; starting another stops the existing service.

When `onRevoke()` runs, the system has already deactivated the VPN interface; the callback may run off the main thread. Close the tunnel socket and `ParcelFileDescriptor`, stop the service, and clean up state gracefully. On Android 8.0/API 26 and higher, when the system starts the service in the background, the guide says to move it promptly to the foreground with `Service.startForeground()`. Always-on VPN is available from Android 7/API 24. Lockdown can block every connection that does not use the VPN. Android recommends explaining the network consequences when enabling allow/disallow lists or lockdown.

## 4. Always-on, per-app routing, and Builder details

- Per-app VPN can use an allowed-app list **or** a disallowed-app list, not both. With neither list, all app traffic goes through the VPN by default. Set the list before `establish()`; changing it requires a new VPN connection. Listed apps must already be installed.
- Always-on VPN is started and controlled by the system. Lockdown blocks non-VPN traffic while the VPN is disconnected; test connection loss, unreachable gateways, configuration updates, and user disconnection in system Settings.
- If the app does not support always-on VPN, the Android VPN guide describes opting out on Android 8.1/API 27 and higher by setting the service metadata `android.net.VpnService.SUPPORTS_ALWAYS_ON` to `false`. This is an Android configuration option, not a Play-policy exemption.
- `VpnService.Builder.addAddress()` and `addRoute()` allow the corresponding IPv4/IPv6 address family. The current Builder reference says the longest matching route prefix takes precedence. From API 33, `excludeRoute()` can exclude a route; a later `addRoute()` for the same destination overrides the exclusion.
- Without an address, route, or DNS server for an address family, outgoing traffic of that family is blocked by default. `allowFamily()` can allow IPv4 or IPv6 without adding a route. `allowBypass()` lets apps bypass the VPN and changes the default boundary in which all app traffic goes through it; disclose and test that product behavior deliberately.
- Android Enterprise managed configurations let an IT administrator configure a VPN remotely. Personal and work profiles are subject to their own administrator policies, app availability, and cross-profile boundaries.

These are Android platform behaviors and engineering guidance. They do not change Play's eligibility, listing, strong-encryption, disclosure/consent, or Console-declaration requirements.

## 5. Direct body links from the Play explainer

The article has **7 body-link occurrences across 6 distinct link targets**. Its 32 numbered Help sidebar entries are navigation and are tracked separately from body links. Clicking the body link labeled `Permissions` returned Internal Error without exposing its destination URL. The current [Sensitive Permissions topic](../sensitive-permissions/sensitive-permissions.en-US.md) is an independently reviewed related page; this does not establish that the failed link redirects there.

| Body target | Relationship to VpnService | Access and coverage |
| --- | --- | --- |
| [Android `VpnService` API](https://developer.android.com/reference/android/net/VpnService) | Authorization, service binding, tunnel-socket protection, revocation, and lifecycle; see the Android-link inventory below. | API body opened; relevant methods sampled, general members remain partial. |
| [Policy Center Help directory](https://support.google.com/googleplay/android-developer/topic/9858052?hl=en) | The destination labeled “Developer Program Policies”; this is a policy directory, not the VPN clause itself. | Directory opened; this branch does not claim all directory descendants are closed. |
| [Ad Fraud](https://support.google.com/googleplay/android-developer/answer/9969955?hl=en) | Applies to ad-traffic redirection, click/impression manipulation, and monetization risk. | Page opened and indexed; generic deeper Help descendants remain tracked individually. |
| Permissions | The explainer's body reference to the Permissions policy. | Click returned Internal Error and exposed no URL; related rules are summarized in [Sensitive Permissions](../sensitive-permissions/sensitive-permissions.en-US.md), but the exact link/redirect relationship is unconfirmed. |
| [Malware](https://support.google.com/googleplay/android-developer/answer/9888380?hl=en) | Applies in parallel to malicious or harmful device/data behavior. | Current page opened and indexed; generic deeper descendants remain partial. |
| [User Data](https://support.google.com/googleplay/android-developer/answer/10144311?hl=en) (two body occurrences) | Governs disclosure, consent, use, and sharing when personal or sensitive data is accessed or collected through the VPN. | Body opened and summarized bilingually; deeper API, course, and Console descendants remain partial. |

## 6. Direct body links from Android's VPN guide

The current Android guide's link IDs 9–46 contain **38 occurrences**: five same-page section anchors (Always-on, Per-app, service lifecycle, allowed list, and disallowed list) and 33 external occurrences resolving to **18 distinct targets**, including one diagram asset. All 17 external URLs were opened or attempted. The diagram click returned Internal Error without exposing its URL, so it cannot receive a URL-level audit row. Repeated API-member links are grouped by destination page; this does not mean every API member has been reviewed.

| Direct target (body link IDs) | Destination and relevance | Access state and boundary |
| --- | --- | --- |
| [Work profiles](https://developer.android.com/work/managed-profiles) (11) | Enterprise profile control, app availability, cross-profile intents, and file sharing; relevant to enterprise VPN/profile isolation. | Body opened; its own testing, Intent, notification, and FileProvider descendants are not exhaustive. |
| [`VpnService` API](https://developer.android.com/reference/android/net/VpnService) (12, 17, 19, 31, 39) | `prepare()`, `protect()`, `onRevoke()`, service binding, and always-on metadata. | 2,769-line API body opened; relevant methods inspected, other members not exhausted. |
| [`VpnService.Builder` API](https://developer.android.com/reference/android/net/VpnService.Builder) (13, 22–24, 40–42) | `establish()`, addresses/routes, per-app lists, bypass, and address-family configuration. | 2,411-line API body opened; those members sampled; other members and version compatibility remain partial. |
| VPN architecture diagram (14, image) | Shows the local TUN interface and gateway data path. | Click returned Internal Error; exact asset URL was not exposed. No additional policy duty is inferred from the image. |
| [Manifest `<service>` element](https://developer.android.com/guide/topics/manifest/service-element) (15) | Manifest service structure, permissions, and intent filters. | Page opened; generic properties, component security, and descendants remain partial. |
| [`Manifest.permission`](https://developer.android.com/reference/android/Manifest.permission) (16) | `BIND_VPN_SERVICE` constant and protected-permission context. | 6,738-line API catalog; relevant permission context sampled, not a full-catalog review. |
| [`DatagramSocket`](https://developer.android.com/reference/java/net/DatagramSocket) (20, 32) | Connect and close calls for the example tunnel socket. | 2,751-line API reference opened; the VPN guide supplies the lifecycle context; other members not exhausted. |
| [TUN/TAP reference](https://en.wikipedia.org/wiki/TUN/TAP) (21) | Background definition for the TUN virtual network interface. | Page opened; this third-party encyclopedia is not authoritative for Play policy or Android platform rules. |
| [`ParcelFileDescriptor`](https://developer.android.com/reference/android/os/ParcelFileDescriptor) (25, 33) | File descriptor returned from `Builder.establish()` and its close lifecycle. | Large API reference opened; relevant close flow cross-checked against the VPN guide, other members partial. |
| [`Context`](https://developer.android.com/reference/android/content/Context) (26) | `startService()` service-launch entry point. | 8,206-line API reference opened; this branch records the VPN-service launch relation only, not a full member review. |
| [Services overview](https://developer.android.com/guide/components/services) (27, 30) | Service startup, lifecycle, and foreground-service context. Both legacy routes redirect to current `/develop/background-work/services`. | Current destination opened and redirect observed in the URL ledger; general service types and descendants remain partial. |
| [`Service` API](https://developer.android.com/reference/android/app/Service) (28, 29) | `onStartCommand()` and `startForeground()` lifecycle/API references. | 3,571-line API reference opened; call context recorded, other members not exhausted. |
| [Managed configurations](https://developer.android.com/work/managed-configurations) (34) | Lets enterprise IT administrators remotely configure a VPN. | Page opened; configuration fields, Console, and enterprise-management descendants remain partial. |
| [`Intent` API](https://developer.android.com/reference/android/content/Intent) (35, 36) | Starts the service and carries the “started by this app” marker. | 9,795-line API reference opened; only this guide's relevant usage is captured, other members partial. |
| [`ConnectivityManager`](https://developer.android.com/reference/android/net/ConnectivityManager) (43) | When `allowBypass()` is used, a process can select the underlying or another network. | 3,223-line API reference opened; the targeted call and API-level implications need member-level follow-up. |
| [`Network`](https://developer.android.com/reference/android/net/Network) (44) | Explicit network binding and socket-routing APIs. | 2,282-line API reference opened; members and compatibility are not exhaustive. |
| [ToyVpn sample source directory](https://android.googlesource.com/platform/development/+/master/samples/ToyVpn) (45) | Platform-repository example VPN client. | The root and key source files were followed; see the descendant inventory below. The mutable `main` branch is not a pinned version. |
| [Android Developers Content License](https://developer.android.com/license) (46) | Content-licensing context for the guide and sample. | Page opened; its full linked-license descendants are not exhausted. |

### ToyVpn sample descendants and production-security boundary (2026-10-24)

The VPN guide links to the ToyVpn repository directory. From that directory, the current `refs/heads/main` README, manifest, build file, Java client/service/connection code, and Linux server were followed. Directory links redirect to these current source paths; this is a mutable-branch snapshot, not an immutable commit.

| Direct child | Read result and compliance relationship |
| --- | --- |
| [Sample `_index.html`](https://android.googlesource.com/platform/development/+/refs/heads/main/samples/ToyVpn/_index.html) | Describes an API 14-era example client and Linux server that tunnel IP over UDP and demonstrate handover when the same VPN parameters are received; its linked [VPN consent illustration](https://android.googlesource.com/platform/development/+/refs/heads/main/samples/images/vpn-confirmation.png) was unreadable. This does not establish current Play compliance. |
| [Android.bp](https://android.googlesource.com/platform/development/+/refs/heads/main/samples/ToyVpn/Android.bp) | Uses `sdk_version: current`, compiles `src/**/*.java`, and points to the Android Apache-2.0 license. |
| [AndroidManifest.xml](https://android.googlesource.com/platform/development/+/refs/heads/main/samples/ToyVpn/AndroidManifest.xml) | `minSdkVersion=14`; declares `FOREGROUND_SERVICE`, `FOREGROUND_SERVICE_SPECIAL_USE`, and `INTERNET`; the VPN service uses `BIND_VPN_SERVICE` and the `android.net.VpnService` intent filter, with `foregroundServiceType="specialUse"` and subtype value `vpn`. This sample configuration does not show that a target app has completed Play VPN or foreground-service declarations. |
| [`src/` entry](https://android.googlesource.com/platform/development/+/refs/heads/main/samples/ToyVpn/src/) → [current Java package directory](https://android.googlesource.com/platform/development/+/refs/heads/main/samples/ToyVpn/src/com/example/android/toyvpn) | The entry resolves to the sample package directory, which lists the three Java files below. |
| [ToyVpnClient.java](https://android.googlesource.com/platform/development/+/refs/heads/main/samples/ToyVpn/src/com/example/android/toyvpn/ToyVpnClient.java) | Reads/writes server, port, shared-secret, proxy, and per-app-list settings; calls `VpnService.prepare()` first and starts the service only after a successful system-consent result. |
| [ToyVpnConnection.java](https://android.googlesource.com/platform/development/+/refs/heads/main/samples/ToyVpn/src/com/example/android/toyvpn/ToyVpnConnection.java) | Calls `protect()` on the tunnel `DatagramChannel` before connecting to the server, forwards TUN packets, and configures addresses, routes, DNS, MTU, and allowed/disallowed application lists. Its handshake comment explicitly says the demo sends the shared secret in plaintext and does not implement mutual authentication or session-key encryption. |
| [ToyVpnService.java](https://android.googlesource.com/platform/development/+/refs/heads/main/samples/ToyVpn/src/com/example/android/toyvpn/ToyVpnService.java) | Creates a foreground notification, starts/stops the connection thread, and closes a previous `ParcelFileDescriptor`; no explicit `onRevoke()` override appears in the file. A production app still needs correct revocation, tunnel-close, and reconnect handling. |
| [Server entry](https://android.googlesource.com/platform/development/+/refs/heads/main/samples/ToyVpn/server/) → [current Linux server directory](https://android.googlesource.com/platform/development/+/refs/heads/main/samples/ToyVpn/server/linux), [directory index](https://android.googlesource.com/platform/development/+/refs/heads/main/samples/ToyVpn/server/linux/_index.html), [Makefile](https://android.googlesource.com/platform/development/+/refs/heads/main/samples/ToyVpn/server/linux/Makefile), [ToyVpnServer.cpp](https://android.googlesource.com/platform/development/+/refs/heads/main/samples/ToyVpn/server/linux/ToyVpnServer.cpp) | Linux/TUN-only server implementation, one session at a time. The index returned no readable body; the C++ source explicitly says it has neither strong authentication nor encryption and says “DO NOT USE IT IN PRODUCTION.” This does not meet Play's device-to-VPN-endpoint encryption requirement and is not a store-ready protocol example. |
| [`res/` resource directory](https://android.googlesource.com/platform/development/+/refs/heads/main/samples/ToyVpn/res/) and [drawable](https://android.googlesource.com/platform/development/+/refs/heads/main/samples/ToyVpn/res/drawable/), [layout](https://android.googlesource.com/platform/development/+/refs/heads/main/samples/ToyVpn/res/layout/), [values](https://android.googlesource.com/platform/development/+/refs/heads/main/samples/ToyVpn/res/values/) | The root resource directory opened and exposed three subdirectories; the browser tool rejected all three child URLs, so their file contents are not inferred. |
| [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0) | Opened the license text referenced by source-file headers; this is source licensing, not Play policy. |

We also checked the current [Android foreground-service types guide](https://developer.android.com/develop/background-work/services/fgs/service-types). For apps targeting Android 14/API 34 or higher, an appropriate type and permission are required, and the type must be declared in Play Console App content. `specialUse` is for valid use cases not covered by other types, with the manifest subtype reviewed in Play Console. The same guide separately lists VPN apps configured in system Settings among `systemExempted` criteria. ToyVpn's manifest uses `specialUse` with subtype `vpn`; that classification boundary must be checked against the target app, target SDK, and current Console form. The knowledge base does not infer which type a developer should choose or treat the AOSP sample as approval evidence.

**Security conclusion:** ToyVpn is useful for understanding the `VpnService`/TUN data path and lifecycle handoffs. Its own client handshake and Linux server explicitly lack strong authentication and encryption, so they do not satisfy Play's VPN-tunnel encryption requirement. A production app needs a separately designed and reviewed secure tunneling protocol, plus independent compliance with VPN eligibility, disclosure, consent, declaration, and foreground-service requirements. Resource subdirectories, generic API members used by the sample, and the rest of the repository's descendants remain incomplete; exact states are in the per-URL audit (snapshot: `../source-page-audit.csv`, not imported in this repository).

## 7. Pre-release review checklist

- [ ] Compare the manifest, merged SDK manifests, runtime features, and Play Console declaration. Verify the actual core purpose fits the current permitted category.
- [ ] Inspect all active artifacts and release tracks; align the Play listing, device-to-endpoint encryption, and declaration state.
- [ ] Maintain an inventory of data types, recipients, uses, and sharing purposes for VPN traffic; prepare a separate in-app disclosure and affirmative consent when required.
- [ ] Record declaration videos showing app launch, VPN use, the full disclosure, consent/decline paths, and how to reopen the disclosure.
- [ ] Verify renewed `prepare()` authorization, `protect()` failure, tunnel establishment/revocation, descriptor/socket closure, foreground notification, and always-on behavior.
- [ ] Test IPv4/IPv6, route lists, lockdown, VPN loss, work profiles, and per-app VPN. Android system consent is not a substitute for Play eligibility.

## Coverage and remaining gaps

The Play explainer's body links are inventoried; five accessible targets were opened or cross-checked against existing bilingual topics. The exact URL for its `Permissions` link could not be extracted because the click returned Internal Error. The Android guide's 38 body-link occurrences are classified, with five in-page anchors separated from 33 external occurrences; 17 external URL targets were opened or attempted, and the diagram URL was not exposed. General descendants of Android API classes, the ToyVpn source directory, enterprise configurations, and service/network APIs were sampled only where relevant and are not recursively closed. See the per-URL source audit (snapshot: `../source-page-audit.csv`, not imported in this repository) and recursive link graph (snapshot: `../google-play-policy-link-graph-en.md`, not imported in this repository).

**Sources:** [Google Play VpnService policy](https://support.google.com/googleplay/android-developer/answer/12564964?hl=en) and the [Android VPN developer guide](https://developer.android.com/develop/connectivity/vpn). This page is a bilingual paraphrase and relationship analysis, not official full text or a review guarantee; check current official pages and Play Console before release.
