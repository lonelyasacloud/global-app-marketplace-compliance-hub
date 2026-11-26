---
id: google-play.app-version-codes-and-apk-distribution
platform: google-play
language: en-US
authority: operational
status: current
kb_checked_at: 2026-10-24
review_due: 2027-01-24
regions: [global]
topics: [version-code, app-bundle, apk, device-compatibility, publishing]
snapshot_id: play.version-codes-and-apk-distribution
snapshot_package: "GooglePlay-KnowledgeBase-2026-10-24-review.zip"
coverage_status: "detailed-summary"
source_url: "https://support.google.com/googleplay/android-developer/answer/17367361?hl=en"
effective_date: "current Play versionCode ceiling 2100000000; AAB dates August 2021 and June 2023 are historical format requirements; no 2027-01-27"
---

# Google Play Version Codes, App Bundles, and Device Filtering

> **Import note (Google batch 8).** The body is the paraphrased summary from the already separated 2026-10-24 Google Play knowledge-base snapshot (`play.version-codes-and-apk-distribution`, reviewed 2026-10-24). It is not a verbatim copy of an official page. The English official source is the source of truth. `kb_checked_at` is the review date recorded in the snapshot source file; this import did not re-open the live official pages. Phrases such as “this knowledge base,” “this library,” and “local topic” describe coverage inside that snapshot, not the set of pages imported into this repository. Relative snapshot links to topics, link graphs, ledgers, or CSVs that are not in this repository are kept as text mentions. Relative links that target the Google batch 1–7 topics or these thirteen batch 8 topics point at the hub files. Reviewed 2026-10-24. Both language files cite the English `hl=en` version-codes article. The snapshot does not record a checked Chinese official page for that article or a failed `hl=zh-CN` fetch. The Chinese hub text is an editorial paraphrase. The exact Android NDK tool page and the version-code illustration returned cache misses. Android compatibility returned Internal Error. Those failures are not policy changes. The Play ceiling of 2,100,000,000 is a current upload limit. August 2021 and June 2023 are historical App Bundle format dates. No 2027-01-27 date is recorded. Play Help supplies the version-code ceiling. Multiple-APK, manifest, filter, and App Bundle material is an implementation note and does not prove review approval. Evidence level: Operational for Play Help; Implementation note for Android publishing mechanics.

## Scope and evidence

This topic follows the review-preparation page's [Version codes](https://support.google.com/googleplay/android-developer/answer/17367361?hl=en) article through [Multiple APK support](https://developer.android.com/google/play/publishing/multiple-apks), [Filters on Google Play](https://developer.android.com/google/play/filters), and [Android App Bundles](https://developer.android.com/guide/app-bundle). On October 24, 2026, I reopened the version-code article, the two core Android guides, the App Bundle guide, and related manifest/licensing references. The tables deduplicate body links by destination; generic navigation and footer links are excluded. Per-URL states are in the source-page audit (snapshot: `../source-page-audit.csv`, not imported in this repository), and relationships are in link graph §4.125.

**Boundary:** The `versionCode` ceiling and upload consequence come from Play Help. APK/AAB, manifest, and filtering behavior are technical guidance in Android/Play developer documentation. They can help prevent configuration errors but do not establish Play policy approval or prove that an account has passed review.

## Play version-code rules

| Item | Verified information | Implementation check |
| --- | --- | --- |
| `versionCode` | A positive, 32-bit internal version number that must increase for each release and is used by Android and Play to order versions. Google Play's maximum is **2,100,000,000**. At or above the maximum, the app cannot upload new APKs or App Bundles. | Reserve room for long-term growth; check every product flavor, track, and automation script for duplicates, regressions, and out-of-range values. |
| `versionName` | A user-facing string such as `1.2.3`; it does not determine update ordering. | Keep the store description, in-app version display, and build artifact consistent. |
| Numbering strategy | Play recommends gradual, sustainable increases, monitoring remaining capacity, and automated warnings or blocks in build/release workflows. | Avoid timestamps or bit layouts that consume the range too quickly. CI should verify that the value exceeds the published maximum and stays below Play's ceiling. |

The Android manifest reference also defines `versionCode` as the update-order value and `versionName` as display text. Use Play Help for the Play-specific upper limit; do not infer it solely from the Android attribute's type.

## App Bundles and multiple APKs: choosing a path

- Android App Bundle (AAB) is the recommended Google Play publishing format. Play generates and serves optimized APKs for device configurations, so developers usually do not need to maintain device-specific APKs themselves.
- Android Developers documentation states that new apps have required AAB since August 2021 and new and existing TV apps since June 2023. Confirm transition eligibility for older apps against the current release flow, app type, and account-specific Console checks.
- The compressed total for APKs needed to install an App Bundle, and subsequent on-demand downloads, must meet the 4 GB limit. AAB does not support APK expansion (`.obb`) files. This is a publishing-format constraint, separate from the `versionCode` ceiling.
- Multiple APKs are an advanced, edge-case approach. Android guidance encourages most apps to publish one broadly compatible APK/AAB, using separate APKs only when a single artifact cannot meet real device-support or size constraints. APKs under one Play listing must share the package name and release signing key, and each APK needs a unique `versionCode`. Where device filters overlap, Play uses version ordering to select an applicable artifact. Higher-API variants and other overlapping upgrade paths need higher version codes so a system update does not strand users without an eligible app update.

### Filters that distinguish multiple APKs

[Filters on Google Play](https://developer.android.com/google/play/filters) lists four filter families that can distinguish APK variants for one application:

1. OpenGL texture-compression formats;
2. screen size, optionally with screen density;
3. API level; and
4. CPU architecture (ABI).

The Multiple APK Support page also gives device-feature-set and Android Go examples, while the Filters page says filters outside the four configurations above cannot distinguish APKs within one listing. These pages are in tension. This topic does not promote feature-only or Go examples into a universally available fifth or sixth split category; verify the current documentation and Play Console artifact validation before relying on them. For screen differences, adaptive layouts/resources are usually preferred to separate APKs. `<compatible-screens>` may exclude undeclared size/density combinations, so Android guidance normally advises against it.

## Visibility and implicit filtering

Google Play combines manifest metadata, required shared libraries, ABI, publication status, and Console distribution controls such as country/price targeting when deciding device compatibility. Filtering affects more than installation: an incompatible app can be hidden from search, category browsing, and even an app deep link; an update can also change whether an installed user sees an update.

- `minSdkVersion` sets minimum API compatibility. `targetSdkVersion` expresses platform-behavior compatibility; Play's annual target API submission floor is a separate rule in the [Target API topic](../target-api/target-api-level.en-US.md).
- Some hardware-related permissions can imply a device requirement. Consider explicitly declaring `android:required="false"` only when the feature is genuinely optional, to avoid unintentionally filtering devices without that hardware. This does not waive sensitive-permission eligibility, declarations, or review; see [Sensitive permissions](../sensitive-permissions/sensitive-permissions.en-US.md).
- `<uses-library android:required="true">` can filter devices lacking the shared library. With `false`, the app should check at runtime whether the library is available.
- Android guidance generally discourages `maxSdkVersion` as a way to exclude newer Android versions; public APIs should normally preserve forward compatibility.
- Play Licensing is an optional runtime licensing implementation, not a Play submission or policy requirement and not an APK device filter. The licensing documentation says authorized users in open/closed testing tracks count as licensed; unpublished draft testing is no longer supported.

## Direct body-link inventories for the two source pages

Counts cover visible external body links only; generic headers and footers are excluded. Repeated URLs and same-page anchors are deduplicated by destination. Deeper API/sample trees remain outside this bounded pass.

### Version codes → Multiple APK support

The Multiple APK article has 27 body-link references. Two are same-page section anchors; after grouping repeated destinations, there are 20 external page/resource targets. Repeated `<uses-sdk>` anchors are listed once.

| Direct target | Relationship and review status |
| --- | --- |
| [Android App Bundles](https://developer.android.com/guide/app-bundle) | Play generates optimized APKs by device configuration; AAB, the 4 GB compressed-download limit, and OBB boundary were rechecked. Full body opened; other delivery/API descendants remain open. |
| [Android NDK](https://developer.android.com/tools/sdk/ndk) | ABI/native-library context for multiple APKs. The exact target returned Cache miss; the separate ABI guide was only partially reviewed, so this is not treated as an NDK page read. |
| [Prepare & roll out releases (legacy URL)](https://support.google.com/googleplay/android-developer/answer/7159011) → [current release workflow](https://support.google.com/googleplay/android-developer/answer/9859348) | The legacy URL was observed redirecting to the current article. The bilingual [release workflow topic](../publishing/play-release-workflow.en-US.md) covers the main process. A current Help retry was blocked by fetch protection; no Console state is inferred. |
| [Filters on Google Play](https://developer.android.com/google/play/filters) | Core reference for multiple-APK variation and device visibility; body opened and summarized, with its 17 distinct body links listed below. |
| [`<supports-gl-texture>`](https://developer.android.com/guide/topics/manifest/supports-gl-texture-element) | OpenGL texture-compression filtering; body opened, reference descendants remain partial. |
| [`<supports-screens>`](https://developer.android.com/guide/topics/manifest/supports-screens-element) | Screen support declarations/defaults; relevant sections sampled, full reference descendants remain partial. |
| [`<compatible-screens>`](https://developer.android.com/guide/topics/manifest/compatible-screens-element) | Exact size/density enumeration can exclude undeclared configurations; relevant sections sampled, full reference descendants remain partial. |
| [Build Multiple APKs / APK splits (legacy path)](https://developer.android.com/studio/build/configure-apk-splits) → [current APK splits configuration](https://developer.android.com/build/configure-apk-splits) | The legacy Studio URL redirects to current Build documentation; related configuration sections sampled, other build/API descendants remain partial. |
| [Supporting Multiple Screens](https://developer.android.com/guide/practices/screens_support) | Single-APK adaptive screen/resource strategy; partially reviewed and not treated as Play policy. |
| [`<uses-sdk>`](https://developer.android.com/guide/topics/manifest/uses-sdk-element) | One destination linked from minimum/target/maximum SDK anchors; current technical reference opened in full. Annual Play target API rules are in a separate topic. |
| [Distributing to Specific Screens (legacy path)](https://developer.android.com/guide/practices/screens-distribution) → [current adaptive display-size guide](https://developer.android.com/develop/ui/compose/layouts/adaptive/support-different-display-sizes) | The legacy route redirects to current Compose adaptive-layout guidance. Relevant display-size/resizability sections were sampled; general Compose API descendants remain partial. |
| [`<uses-feature>`](https://developer.android.com/guide/topics/manifest/uses-feature-element) | Manifest feature declarations and device filtering; Play-related sections sampled, full reference descendants remain partial. |
| [Configure Product Flavors (legacy path)](https://developer.android.com/studio/build/build-variants) → [current Build variants guide](https://developer.android.com/build/build-variants) | The legacy Studio URL redirects to current Build documentation; only variant-related sections were checked. |
| [`<manifest>`](https://developer.android.com/guide/topics/manifest/manifest-element) | Checked the `versionCode`/`versionName` definitions; full page opened, general attribute descendants not closed in this pass. |
| [Android ABI guide](https://developer.android.com/ndk/guides/abis) | ABI/native-library packaging guidance; partially reviewed, NDK/API/sample trees remain open. |
| [`<uses-configuration>`](https://developer.android.com/guide/topics/manifest/uses-configuration-element) | Keyboard/navigation/touch configuration filters; relevant sections sampled, reference descendants remain partial. |
| [Android Studio projects (legacy path)](https://developer.android.com/tools/projects) → [current Studio projects](https://developer.android.com/studio/projects) | The legacy route redirects to the current Studio project overview; engineering guidance, not a new Play policy. |
| [Version-code illustration asset](https://developer.android.com/static/images/market/version-codes.png) | Image target returned Cache miss; the text article fully covers the readable version rules. |
| [Multiple APKs by API level](https://developer.android.com/training/multiple-apks/api) | Legacy API-splitting guide; partially reviewed. It recommends considering App Bundles first; deeper API descendants remain open. |
| [Android Developers Content License](https://developer.android.com/license) | License page opened: documentation/code and other site content have different terms, and linked content/trademarks have separate boundaries. This library uses summaries and links rather than copying full pages. |

### The 17 distinct body links from Filters on Google Play

The Filters page has 24 visible link references. Repeated anchors to `<uses-sdk>` and duplicate links are grouped into 17 distinct external targets. For generic Android references, only the Play-filtering sections were reviewed.

| Direct target | Relationship and status |
| --- | --- |
| [Google Play web app catalog](https://play.google.com/apps) | The web flow compares requirements with devices registered to the signed-in user; the link redirected to Google sign-in, so no account/device state could be checked. |
| [Android manifest overview](https://developer.android.com/guide/topics/manifest/manifest-intro) | Describes how the manifest declares components, permissions, and device features; full body opened, generic descendants remain partial. |
| [`<supports-screens>`](https://developer.android.com/guide/topics/manifest/supports-screens-element) | Screen-size filtering; relevant sections partially opened. |
| [`<uses-sdk>`](https://developer.android.com/guide/topics/manifest/uses-sdk-element) | `minSdkVersion`, `targetSdkVersion`, and `maxSdkVersion` anchors resolve to one reference. Minimum/target semantics were rechecked; the annual Play floor is a separate topic. |
| [Supporting Multiple Screens](https://developer.android.com/guide/practices/screens_support) | Adaptive layout/resources for broad support; partially reviewed, legacy-guide descendants remain open. |
| [`<uses-configuration>`](https://developer.android.com/guide/topics/manifest/uses-configuration-element) | Keyboard/navigation/touch hardware requirements; relevant sections checked. |
| [`<uses-feature>`](https://developer.android.com/guide/topics/manifest/uses-feature-element) | Declares hardware/software feature dependencies; optional features should match actual behavior; Play sections sampled. |
| [`<uses-permission>`](https://developer.android.com/guide/topics/manifest/uses-permission-element) | Play may infer hardware requirements from some permissions; exact target partially reviewed. Permission policy eligibility is a separate question. |
| [`<uses-library>`](https://developer.android.com/guide/topics/manifest/uses-library-element) | `required=true` can filter devices without a shared library; key requirement checked, other reference descendants partial. |
| [`<compatible-screens>`](https://developer.android.com/guide/topics/manifest/compatible-screens-element) | Undeclared size/density combinations may be excluded; key sections checked, Android generally advises avoiding it. |
| [`<supports-gl-texture>`](https://developer.android.com/guide/topics/manifest/supports-gl-texture-element) | Play filters based on supported texture-compression formats; page opened in full. |
| [Android NDK](https://developer.android.com/tools/sdk/ndk) | ABI/native-library background; exact page returned Cache miss. |
| [Application Licensing](https://developer.android.com/google/play/licensing) | Optional runtime licensing service; body opened in full, not a Play review/publishing requirement. |
| [Licensing Overview / Copy Protection replacement](https://developer.android.com/google/play/licensing/overview) | The Copy Protection replacement link lands here. Page opened; it describes purchase-record licensing, authorized open/closed test users, and the end of unpublished draft testing. |
| [Android compatibility](https://developer.android.com/guide/practices/compatibility) | General compatibility overview; clicking the target returned Internal Error, so its body was not verified. The Filters article remains the primary evidence for Play filtering. |
| [Multiple APK support](https://developer.android.com/google/play/publishing/multiple-apks) | Explains variants under one Play listing, package/signing requirements, and version ordering; reopened, with direct children itemized above. |
| [Android Developers Content License](https://developer.android.com/license) | License notice for documentation and code samples; opened and its scope recorded. |

## Pre-release checklist

1. Read the highest published `versionCode` from Play Console and enforce uniqueness, monotonic increase, and `≤ 2,100,000,000` for every variant/track.
2. Manage `versionName` separately from `versionCode`; changing the display string does not trigger an update.
3. Prefer an AAB and one broadly compatible app artifact. If using multiple APKs, record each variant's filters, signature, package name, and upgrade path.
4. Compare the merged manifest and Play's device-compatibility report for required features, implied permission requirements, shared libraries, ABI, screen declarations, and country/price controls.
5. Verify visibility, install, and upgrade behavior across Android versions, ABIs, screens, and hardware, especially after a system update that changes which APK a user qualifies for.
6. Review permissions such as `CAMERA` independently for device reach and Play sensitive-permission policy eligibility/declarations.

## Remaining scope

This pass attempted all 27 body-link references on Multiple APK support (20 distinct targets, including two same-page anchors) and all 24 visible links on Filters (17 distinct external targets). The version-code, App Bundle, Filters, manifest overview, Licensing, Licensing Overview, and Content License bodies were reviewed. The exact Android NDK tool page and version-code image returned Cache miss; Android compatibility returned Internal Error; legacy redirects and several manifest/build references were sampled only in relevant sections. General API, Gradle, NDK samples/libraries, and Android-version descendants remain partly unaudited. This topic does not claim infinite recursive closure.
