---
id: google-play.android-xr-app-quality-and-policies
platform: google-play
language: en-US
authority: normative
status: current
kb_checked_at: 2026-10-22
review_due: 2027-01-22
regions: [global]
topics: [android-xr, app-quality, privacy, camera, microphone, wearable-devices]
snapshot_id: play.android-xr-policy
snapshot_package: "GooglePlay-KnowledgeBase-2026-10-24-review.zip"
coverage_status: "detailed-summary"
source_url: "https://developer.android.com/docs/quality-guidelines/android-xr"
source_url_chinese: "https://developer.android.com/docs/quality-guidelines/android-xr?hl=zh-cn"
source_url_immersive: "https://developer.android.com/docs/quality-guidelines/android-xr/immersive"
source_url_immersive_chinese: "https://developer.android.com/docs/quality-guidelines/android-xr/immersive?hl=zh-cn"
source_url_augmented: "https://developer.android.com/docs/quality-guidelines/android-xr/augmented"
source_url_devices: "https://developer.android.com/develop/xr/devices"
source_url_zh: "https://developer.android.com/docs/quality-guidelines/android-xr?hl=zh-cn"
source_url_english_zh: "https://developer.android.com/docs/quality-guidelines/android-xr"
source_url_immersive_zh_zh: "https://developer.android.com/docs/quality-guidelines/android-xr/immersive?hl=zh-cn"
source_url_immersive_en_zh: "https://developer.android.com/docs/quality-guidelines/android-xr/immersive"
source_url_augmented_en_zh: "https://developer.android.com/docs/quality-guidelines/android-xr/augmented"
effective_date: "Android XR app policies alongside general Play policy; pages last updated 2026-10-20 UTC; no separate effective date and no 2027-01-27"
---

# Android XR app quality and policy requirements

> **Import note (Google batch 8).** The body is the paraphrased summary from the already separated 2026-10-24 Google Play knowledge-base snapshot (`play.android-xr-policy`, reviewed 2026-10-22). It is not a verbatim copy of an official page. The English official source is the source of truth. `kb_checked_at` is the review date recorded in the snapshot source file; this import did not re-open the live official pages. Phrases such as “this knowledge base,” “this library,” and “local topic” describe coverage inside that snapshot, not the set of pages imported into this repository. Relative snapshot links to topics, link graphs, ledgers, or CSVs that are not in this repository are kept as text mentions. Relative links that target the Google batch 1–7 topics or these thirteen batch 8 topics point at the hub files. YAML `reviewed_on` is 2026-10-22. The opening line says 2026-10-24. Those snapshot dates are not a policy change. The English Developer Policy Center lists Android XR. The Simplified Chinese policy-center directory in this snapshot has no corresponding entry. English and Simplified Chinese immersive guides were opened. The Chinese augmented-guide target returned a cache miss, so that Chinese summary follows the English official page. That cache miss is not a policy change. The pages show a last-updated date of 2026-10-20 UTC and do not state a separate effective deadline. No 2027-01-27 date is recorded. Android XR App Policies apply alongside general Play policies. Quality checklists are operational guidance and implementation notes, not a new article inside the consolidated Developer Program Policy. Evidence level: Normative for the XR app policies; Operational and Implementation note for quality and emulator guidance.

**Reviewed 2026-10-24.** The English [Google Play Developer Policy Center](https://play.google/developer-content-policy/) lists Android XR under “Other Programs” and links to Android Developers quality guidance. The current Simplified Chinese directory has no corresponding entry. The XR guidance combines form-factor quality checklists with explicit “Android XR App Policies.” It is a platform-specific requirement set linked by the Play policy directory, not a new standalone article in the consolidated Developer Program Policy.

## Applicable devices and experiences

| Device/experience | Official guidance | Directory relationship |
| --- | --- | --- |
| Fully or semi-immersive experiences on XR headsets and wired XR glasses | [Immersive app quality and policies](https://developer.android.com/docs/quality-guidelines/android-xr/immersive) | English and Simplified Chinese bodies opened. Wired devices leave the physical world visible, so bystander privacy and spatial safety matter. |
| Lightweight augmented experiences on audio and display glasses | [Augmented app quality and policies](https://developer.android.com/docs/quality-guidelines/android-xr/augmented) | English body opened. The Chinese localized target returned Cache miss in the browser, so the Chinese summary here is translated from the English official source. |
| Capability differences among headsets, wired XR glasses, and audio/display glasses | [Android XR device types](https://developer.android.com/develop/xr/devices) | Headsets are primarily immersive; audio/display glasses are wearable intelligent eyewear that may include a camera, microphone, and touchpad. This is a platform overview, not a Play eligibility policy. |

## Play rules that apply across XR experiences

The immersive guide explicitly says apps distributed through Google Play must comply with all [Google Play Developer Policies](https://play.google/developer-content-policy/). XR-specific safety requirements further prohibit apps from facilitating or promoting:

- Doxxing; facial recognition or biometric identification; surveillance; and creation or dissemination of non-consensual intimate imagery (NCII).
- Using a camera to identify bystanders and surface their personally identifiable information, such as a name, address, phone number, or employer; using a camera to facilitate NCII or other illegal content, including CSAM.
- Persistent background audio recording or transcription when the wearer is not actively engaged in a user-initiated task; using the microphone to identify non-wearer voices or bystanders.
- Changing, dimming, or disabling system-enforced user-facing/world-facing LEDs, or instructing users to do so; bypassing or interfering with the tamper detection that stops recording if an outward-facing LED is covered or damaged.

## Camera boundaries for intelligent-eyewear audio experiences

The augmented-experience page is more specific about allowed and prohibited wearable-camera uses:

| Allowed | Prohibited |
| --- | --- |
| Video calls; ambient sensing and scene understanding. | Real-time, one-to-many public live streaming, public broadcasting, or casting to public feeds/open channels; real-time identification of bystanders to reveal personal information; creating NCII or illegal content. |

Microphone arrays must not persistently eavesdrop in the background or identify bystanders. Apps must not change or disable system audio denoisers or direct users to do so. The public-broadcast restriction is stated for intelligent-eyewear augmented experiences; do not generalize it into a universal ban on every XR headset or every video call.

## Gestures and exits for audio glasses

These rules apply to audio-only experiences on intelligent eyewear. They should not be applied automatically to every XR headset control scheme.

| Input | Required/allowed behavior | Prohibited behavior |
| --- | --- | --- |
| Single touchpad tap | Play a prompt relevant to the user's current context, repeat the last audible message, pause/stop playback, or provide clear microphone mute-state feedback. | Ads or irrelevant information; using it as a high-frequency game controller; triggering instructions that facilitate crime, violence, or self-harm. |
| Quick double-press of the camera button | Actually start the camera and provide sensor data to the app. Explain the intended use before initial permission/setup; use the feed only for the purpose the user agreed to. | Remapping to a non-camera function; intercepting the button while discarding/suppressing the feed; undisclosed or deceptive camera use. |
| Single-finger back swipe | Always call `onBack()` to exit or return to the previous state; stop or suspend primary sensor use after exit. | Hijacking the exit command, launching ads/media, or simulating an exit while secretly listening or surveilling. |

## Device eligibility, experience quality, and release decisions

- Existing mobile apps can be automatically compatible with XR if they do not require unsupported hardware/software features. An app whose required feature is unsupported cannot be installed through the Play Store. Play uses manifest feature declarations for device filtering; see Android's [`<uses-feature>`](https://developer.android.com/guide/topics/manifest/uses-feature-element) guide.
- Apps that meet the Tier 2 / Tier 1 adaptive quality level for tablets, desktop, or foldables can qualify as XR-compatible adaptive apps. An XR-differentiated app must implement at least one XR-specific feature/content item and meet the applicable quality metrics; qualifying apps automatically receive the “Made for XR” Play Store badge.
- The immersive checklist gives reference values: under 11.1 ms per frame at 90 Hz or 13.8 ms at 72 Hz; mean cold start under 2 seconds and warm start under 1 second; fewer than one ANR in 99.5% of daily sessions; and roughly 1% crash rate. These are metrics/goals in the XR quality guidance, not universal numeric policy thresholds for every Play app.
- Spatial experiences should avoid abrupt viewpoint motion that can cause discomfort, respect real-world boundaries, keep central vision clear, use appropriately sized targets, and provide a clear exit. Intelligent-eyewear experiences should be user initiated, minimize distraction during movement/public use, use the lowest camera frame rate/resolution that meets the use case, and avoid unnecessary high-drain sensors.
- Request glasses camera/microphone access through the [XR hardware-permission API](https://developer.android.com/develop/xr/jetpack-xr-sdk/request-hardware-permissions). Glasses hardware needs its own runtime request and system consent flow on the paired phone/host even when the phone already has the corresponding permission. Implementation must still comply with the [User Data policy](../user-data/user-data.en-US.md) and applicable sensitive-permission rules.
- Compatible apps should use standard `NotificationManager` and Live Updates so timely information can be presented as a glanceable visual cue or spoken notification. Differentiated experiences should also test audio focus, alternative inputs, varied environments, and sensor lifecycle behavior.

## Direct links in the source pages: targets and relationships

The table below records direct body links relevant to device selection, policy duties, or actionable XR implementation. In-page anchors such as compatibility tiers, checklists, and audio-only policies are sections, not separate target pages. Android Developers pages also include many test cases, API references, and general navigation descendants that have not all been expanded.

| Parent → direct link | Target content and relationship to Play/XR | Review status |
| --- | --- | --- |
| [Android XR overview](https://developer.android.com/docs/quality-guidelines/android-xr) → [device types](https://developer.android.com/develop/xr/devices), [immersive guide](https://developer.android.com/docs/quality-guidelines/android-xr/immersive), [augmented guide](https://developer.android.com/docs/quality-guidelines/android-xr/augmented) | Select requirements based on device and experience type; these are the main descendants of the English Policy Center's Android XR entry. | All three English bodies opened; Simplified Chinese overview and immersive guide also opened. |
| Immersive guide → [Core app quality](https://developer.android.com/docs/quality-guidelines/core-app-quality), [Adaptive app quality](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality) | XR quality inherits the Android core baseline; adaptive tiers determine compatible-adaptive status. These are Android quality references, not substitutes for Play policy. | Both pages opened. Core app quality has a large test/API tree; only policy-relevant sections were summarized. |
| Immersive guide → [`<uses-feature>`](https://developer.android.com/guide/topics/manifest/uses-feature-element) | Play may filter devices based on manifest features; an unsupported required feature can prevent installation on XR. | Direct body target opened; Android implementation guidance. |
| Immersive guide → [XR design](https://developer.android.com/design/ui/xr/guides/get-started), [accessibility](https://developer.android.com/guide/topics/ui/accessibility), [startup time](https://developer.android.com/topic/performance/issues/launch-time), [crash handling](https://developer.android.com/topic/performance/issues/crash), [Play pre-launch reports](https://google.play/business/pre-launchreports/) | Spatial comfort/interactions, basic accessibility, performance diagnosis, and pre-release testing; none guarantees policy approval. | Targets opened; this topic summarizes their relevance to XR quality. Their deeper technical/API branches were not exhausted. |
| Augmented guide → [Compose Glimmer](https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer), [Jetpack Projected hardware access](https://developer.android.com/develop/xr/jetpack-xr-sdk/access-hardware), [hardware permissions](https://developer.android.com/develop/xr/jetpack-xr-sdk/request-hardware-permissions), [ARCore for Jetpack XR](https://developer.android.com/develop/xr/jetpack-xr-sdk/arcore) | Low-distraction display-glasses UI, phone/glasses projection, host-side permission consent, and environmental perception. API availability does not mean Play has approved the data use. | Direct body targets opened; cross-check data and permission policies. |
| Augmented guide → [NotificationManager](https://developer.android.com/reference/kotlin/android/app/NotificationManager), [Live Updates](https://developer.android.com/develop/ui/compose/notifications/live-update), [background tasks](https://developer.android.com/develop/background-work/background-tasks), [audio focus](https://developer.android.com/media/optimize/audio-focus) | Standard notifications/ongoing-activity presentation, background task scheduling, and audio focus help avoid confusing alerts, excess battery use, and background-sensor misuse. | Pages opened as implementation references; deeper API members were not individually summarized. |
| Augmented guide → [glasses emulator](https://developer.android.com/develop/xr/jetpack-xr-sdk/run/create-avds/glasses), [Glimmer composable previews](https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/preview) | Test glasses displays/interactions across scenarios and lighting. | Pages opened; emulator images and tooling will evolve. |
| Augmented guide → [Google Play Developer Policies](https://play.google/developer-content-policy/), [User Data](https://support.google.com/googleplay/android-developer/answer/10144311), [Bullying and Harassment](https://support.google.com/googleplay/android-developer/answer/9878810) | XR camera/glasses behavior must satisfy general Play rules, data handling, and anti-bullying/harassment requirements; bystander identification and public exposure intersect with these rules. | Policy Center and User Data opened and have bilingual summaries. The Bullying target failed on this click, but the current policy is covered in the [Inappropriate Content topic](../inappropriate-content/inappropriate-content.en-US.md). |

### Descendants of glasses permission requests and projected contexts (October 24, 2026)

Reopened [Request hardware permissions](https://developer.android.com/develop/xr/jetpack-xr-sdk/request-hardware-permissions) (updated October 19) and followed its device, manifest, runtime-permission, API, sample, and neighboring hardware-guide links. The table records the destinations most relevant to camera/microphone access. Android implementation documentation does not approve a use under Play policy.

| Link / destination | Content and relationship | Review status |
| --- | --- | --- |
| Permission guide → [`ProjectedActivityCompat`](https://developer.android.com/reference/androidx/xr/projected/ProjectedActivityCompat) → [XR Projected release notes](https://developer.android.com/jetpack/androidx/releases/xr-projected) | From a projected-glasses Activity, use `ProjectedActivityCompat.requestPermissions`; the system sends the user from the glasses prompt to host-phone consent and returns the result to the initiating Activity. The API reference marks it API 35+, worker-thread, and lists failure conditions such as an unavailable projected service or a non-projected Activity. The release page lists `1.0.0-alpha14` as current on October 21, still an alpha; `ProjectedPermissionsResultContract` is deprecated and the old `androidx.xr.projected.permissions.*` APIs were removed. | Targeted API reference opened; release page opened. The API reference and release history do not agree on the first-added version annotation; use the current release and reference, and do not label the alpha as stable. |
| Permission guide → [Declare app permissions](https://developer.android.com/training/permissions/declaring) → [`<uses-permission>`](https://developer.android.com/guide/topics/manifest/uses-permission-element) → [Request runtime permissions](https://developer.android.com/training/permissions/requesting) | Declare only permissions the feature needs; request in response to the user's action, check before each operation, explain when appropriate, and degrade gracefully after denial/revocation. Hardware permissions can affect Play device filtering: if camera hardware is optional, declare the camera feature explicitly as optional and check device availability. | Declaration, manifest, and runtime-permission bodies opened or cross-checked. These Android minimum-permission/compatibility practices are tracked separately from Play XR privacy rules. |
| Permission guide → [`Activity.requestPermissions(..., deviceId)`](https://developer.android.com/reference/android/app/Activity); [Android XR device types](https://developer.android.com/develop/xr/devices) | A request from a phone Activity must include the projected device ID; use the device-aware result callback. Do not treat the host phone's camera/microphone grant as the glasses hardware grant. | Targeted method lookup in the large Activity API reference; device-types body opened. The two GitHub code-sample clicks returned Internal Error, and the reader did not expose verifiable hrefs. |
| [Access hardware](https://developer.android.com/develop/xr/jetpack-xr-sdk/access-hardware) → [Use a projected context](https://developer.android.com/develop/xr/jetpack-xr-sdk/access-hardware-projected-context) → [`ProjectedContext`](https://developer.android.com/reference/androidx/xr/projected/ProjectedContext) | A projected Activity context can access glasses hardware. A phone Activity/service should create a projected context while the glasses are connected, release camera/system resources on disconnect, then create a new context after reconnect. The official API search excerpt also warns that application Context's device ID can shift with the most recently foregrounded Activity; prefer Activity Context. | Relevant hardware-guide sections opened; direct ProjectedContext API access failed, so its members are summarized from the official Android Developers search excerpt only. The sample href was not exposed. |
| Projected context → [AudioManager](https://developer.android.com/reference/kotlin/android/media/AudioManager), [AudioDeviceInfo](https://developer.android.com/reference/kotlin/android/media/AudioDeviceInfo), [Bluetooth overview](https://developer.android.com/develop/connectivity/bluetooth), [CameraX overview](https://developer.android.com/media/camera/camerax) | The hardware guide points to CameraX for glasses-camera access and recommends checking availability. Bluetooth HFP recording uses host-phone `RECORD_AUDIO` / `BLUETOOTH_CONNECT` runtime permission and `AudioManager` routing. HFP is a standard Bluetooth audio path; it does not replace the glasses-specific camera permission. | Target pages opened or checked at the relevant sections; large APIs, CameraX use cases, and Bluetooth permission descendants remain partial. |

**Open boundary:** The two GitHub sample targets could not be read and their hrefs were not exposed. Large Activity/ProjectedContext/AudioManager API references were sampled only for relevant members; sample-repository, CameraX, Bluetooth, and navigation descendants are not exhausted. The current Jetpack XR API is still alpha. These platform flows do not change Play requirements for necessity, disclosure, user consent, background collection, or bystander privacy.

## Coverage boundary

This topic summarizes the Android XR policy core and important direct descendants in both languages, linking high-impact policy targets to existing topics. It does not expand every Android Developers test case, footnote, navigation link, or SDK/API descendant. The Chinese-localized augmented page failed to fetch. The pages show a last-updated date of October 20, 2026 UTC and do not state a separate effective deadline. Before release, recheck the current sources, target device types, Play Console device filtering, and account-specific policy status.
