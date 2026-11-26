---
id: google-play.photo-video-permissions
platform: google-play
language: en-US
authority: normative
status: current
kb_checked_at: 2026-10-23
review_due: 2027-01-23
regions: [global]
topics: [photo-picker, media-permissions, minimum-scope, privacy]
snapshot_id: play.photo-video-permissions
snapshot_package: "GooglePlay-KnowledgeBase-2026-10-24-review.zip"
coverage_status: "detailed-summary"
source_url: "https://support.google.com/googleplay/android-developer/answer/16935362?hl=en"
source_url_zh: "https://support.google.com/googleplay/android-developer/answer/16935362?hl=zh-CN"
---

# Photo and video permissions, Photo Picker, and minimum-scope access

> **Import note (Google batch 2).** The body is the paraphrased summary from the already separated 2026-10-24 Google Play knowledge-base snapshot (`play.photo-video-permissions`, reviewed 2026-10-23). It is not a verbatim copy of a Google page. The English official page is the source of truth. `kb_checked_at` is the snapshot YAML `reviewed_on` of 2026-10-23; this import did not re-open the live official pages. The body keeps the source’s October 22, 2026 note for when the shared parent Help page was opened in full, and the closing line dates the paraphrase to pages available on October 23, 2026. Those two snapshot dates are not treated as a policy change. Phrases such as “this knowledge base,” “this library,” and “local topic” describe coverage inside that snapshot, not the set of pages imported into this repository. Relative snapshot links to topics, link graphs, ledgers, or CSVs that are not in this repository are kept as text mentions. Relative links that target the Google batch 1 topics or these seven batch 2 topics point at the hub files. The snapshot calls this a bilingual paraphrase of official pages available on that date. It does not record a failed `hl=zh-CN` fetch for this primary article. The shared parent page also states Contacts rules effective 2027-01-27; the photo and video full-compliance date in the same source is May 28, 2025, which the snapshot says has passed. Those dates stay separate. Play photo and video permission rules are `normative`. Photo Picker and other Android storage guidance is an implementation note and does not by itself establish Play eligibility.

**Reviewed October 22, 2026.** Google Play treats user photos as personal and sensitive data. Apps targeting Android 13 (API 33) or later may request `READ_MEDIA_IMAGES` or `READ_MEDIA_VIDEO` only when system pickers such as Android Photo Picker are insufficient for core functionality. Apps that keep these permissions must submit a Play Console declaration explaining their photo/video access needs and why Photo Picker or other alternatives are insufficient; Google Play reviews the use case. The full-compliance deadline of May 28, 2025 has passed.

## Decision rules

| App need | Recommended or required action |
| --- | --- |
| Occasional selection such as a profile image, one upload, or a check image | Use Android Photo Picker or another suitable system picker and pass only the URI selected by the user to the feature. Do not keep broad library permission for occasional selection. |
| A core feature needs persistent or frequent access to many photos/videos in shared storage | Determine whether a system picker truly cannot support the core feature. If keeping `READ_MEDIA_IMAGES` / `READ_MEDIA_VIDEO`, submit a declaration explaining the core feature, access frequency/scope, and technical limits of alternatives, then await Play review. |
| The app has a custom media-selection UI | A custom UI alone does not qualify the app for broad permission. Use narrower access if Photo Picker or another option supports the core feature; otherwise explain the specific technical limitation in the declaration. |
| The user declines broad access | Make a reasonable effort to support the user with transactional system-picker access or a gracefully reduced experience. Do not block all functionality because a non-critical permission was declined. |

Play's Help page gives gallery/media management and core functionality that cannot be served by system-picker features as examples, but eligibility is determined by the actual app and review. A general “upload media” button or preference for custom UI does not by itself show a need to read the entire library.

Private apps and enterprise device-management apps are exempt from this particular policy requirement; verify that the app actually fits the category.

## Photo Picker implementation and scope

Android Photo Picker lets users browse local media and grants the app a read URI only for selected items; the app does not need broad media-storage permission first. Android recommends launching it through the `PickVisualMedia` or `PickMultipleVisualMedia` contracts in `androidx.activity`. If Photo Picker is unavailable on a device, the library falls back to `ACTION_OPEN_DOCUMENT`. Apps can restrict media type and selection count. Eligible cloud media providers may also contribute content to the picker.

- Compatibility: Photo Picker is available on Android 11/API 30+ devices receiving Google System Updates; some older Android 4.4–10 and Android Go devices can receive a backported version through Google Play services. Check the current device and library support before integration.
- URI lifetime: the selected media is exposed through a URI grant with a limited default lifetime. Long-running background work such as a large upload may need `takePersistableUriPermission()` to extend read access; clean up access state when the workflow no longer needs it.
- User experience: open the picker in response to the feature the user chose, limit media types and selection count, and support cancellation, reselection, and partial completion. A selected URI represents only media the user chose. Any upload or sharing still needs secure handling, disclosure, and Data safety accuracy under the User Data policy.

### Multi-select fallback, persisted grants, and HDR video

The Android Photo Picker guide was updated on **October 16, 2026**. `PickMultipleVisualMedia` uses the system Photo Picker when available and can fall back to `ACTION_OPEN_DOCUMENT` on older devices; the fallback does not enforce the requested maximum number of items. Do not treat `maxItems` as a cross-device hard limit. If a product or safety rule requires a cap, validate the returned items and explain any rejected selection. The system multi-select limit is exposed through [`MediaStore.getPickImagesMaxLimit()`](https://developer.android.com/reference/android/provider/MediaStore#getPickImagesMaxLimit%28%29), available from Android 13/API 33 or R Extensions 2 for `ACTION_PICK_IMAGES`; this does not establish that document pickers enforce the same cap.

To check device availability, use [`isPhotoPickerAvailable(context)`](https://developer.android.com/reference/androidx/activity/result/contract/ActivityResultContracts.PickVisualMedia). It checks the Android version, SDK extension, and whether a system app handles the fallback-picker action. The old no-argument check does not detect a system-app fallback and is deprecated.

Picker URI grants normally expire when the app stops or the device restarts. An app can call [`ContentResolver.takePersistableUriPermission()`](https://developer.android.com/reference/android/content/ContentResolver#takePersistableUriPermission%28android.net.Uri%2Cint%29) only when the returned URI grant permits persistence. Android's picker supports up to 5,000 persisted media grants; after that, the oldest grant is removed. Long-running uploads should handle expired or unavailable URIs and offer reselection. Persisted grants are not permanent library-wide access.

HDR video transcoding by Photo Picker is **optional and off by default**. On Android 13/API 33+, AndroidX Activity's `MediaCapabilities` lets an app state the formats it supports so the picker can transcode when appropriate. The API is included in stable `androidx.activity` **1.11.0**. Transcoding takes time and storage, and the guide sets a one-minute video limit; declare capabilities accurately and test both original and transcoded URIs. This is media-compatibility guidance, not an additional Google Play permission criterion. The Activity page also lists 1.7.0 as the minimum for picker contracts; check the current stable dependency and target devices before implementation.

### Android 14 Selected Photos Access

Android 14/API 34 introduced `READ_MEDIA_VISUAL_USER_SELECTED` and Selected Photos Access so apps maintaining their own gallery UI can handle partial access. Implement Android's permission-state, reselection, and UI-refresh guidance; do not assume that previously selected media remains accessible indefinitely. This platform runtime option **does not replace** Google Play's core-functionality test or Console declaration review for broad `READ_MEDIA_IMAGES` / `READ_MEDIA_VIDEO` access. If the product only needs the user to choose particular files, prefer Photo Picker.

## Declaration, review, and release-track audit

If the app keeps broad media permissions:

1. Map each permission to a core feature clearly described in the store listing, and explain why that feature needs frequent or persistent library-wide access.
2. Explain the specific technical requirement that Photo Picker, `ACTION_OPEN_DOCUMENT`, or another system option cannot meet. Having a custom picker is not enough.
3. Complete the photo/video permissions declaration in Play Console and submit review materials. The declaration should match the manifest, runtime behavior, privacy policy, and Data safety answers.
4. Inspect merged manifests from the app and all SDKs, dynamic feature modules, build variants, and Play production/testing tracks. If the use is not eligible, remove broad permissions from every version still distributed, not just one APK or one track.
5. Record the review status and rejection reasons. Reassess the declaration when code or SDK behavior changes; an old approval does not automatically cover a new use.

The 2025 reminder asked developers to submit a declaration or remove the permissions by January 22, 2025 and allowed extensions through May 28, 2025. Both dates have passed. As of this review, the current consolidated policy still requires a Console declaration for qualifying apps that retain broad access. The actual submission and review outcome for an app can only be confirmed in its developer account.

## Page links and coverage

The shared parent page, [Understanding Restricted Permissions with minimum scope alternatives](https://support.google.com/googleplay/android-developer/answer/16935362?hl=en), was opened in full on October 22, 2026. It combines Contacts (API 37+) and Photo/Video (API 33+) rules: Console prompts for Contacts declarations began in September 2026, the Contacts policy takes effect January 27, 2027 with a stated 30-day self-extension, and the media-permission full-compliance deadline was May 28, 2025. Its 12 related-permission Help sidebar links are tracked separately from body links in sections 4.1/4.2 of the recursive link graph (snapshot: `../google-play-policy-link-graph-en.md`, not imported in this repository).

| Parent page/source | Linked target | Relationship and status |
| --- | --- | --- |
| Current Restricted Permissions minimum-scope Help | [User Data policy — Personal and Sensitive User Data](https://support.google.com/googleplay/android-developer/answer/10144311?hl=en) | Read. Photos fall under personal/sensitive-data handling: limit access and use to expected functionality, use Android permissions, protect data, and meet prominent disclosure/consent rules when the access or collection is unexpected. SDK data behavior remains the developer's responsibility. |
| Current Restricted Permissions minimum-scope Help | [Android Sharesheet — Send data to other apps](https://developer.android.com/develop/ui/compose/sharing/send) | Body opened and added as a minimum-permission alternative. The Sharesheet lets users send content to another app/person; when the task is selecting or importing photos/videos from the library, use Photo Picker instead of treating Sharesheet as a media picker. |
| Current Restricted Permissions minimum-scope Help | [Android Photo Picker](https://developer.android.com/training/data-storage/shared/photo-picker), [AndroidX Activity release notes](https://developer.android.com/jetpack/androidx/releases/activity) | Both opened. Photo Picker uses `PickVisualMedia`/`PickMultipleVisualMedia` for user-selected media; Activity release notes track picker contracts and dependency versions. The large, changing release log is not mirrored beyond picker-relevant entries. |
| Photo Picker compatibility descendants | [Mainline / Modular System Components](https://source.android.com/docs/core/ota/modular-system), [Google System Updates release notes](https://support.google.com/product-documentation/answer/11412553) | Both opened and checked for Photo Picker backport/system-update context: Mainline lets selected system components update independently; Google System Updates records Photo Picker backport releases. These explain compatibility and do not create Play eligibility criteria. |
| Current consolidated Developer Program Policy | [Photo and Video Permissions](https://support.google.com/googleplay/android-developer/answer/18258653?hl=en#restricted-permissions-with-minimum-scope-alternatives) | Read. Confirms the Android 13/API 33+ permission boundary, the core-functionality test for system-picker insufficiency, and the declaration requirement for retained broad access. |
| Legacy Photo/Video target in the April 10, 2025 announcement | [Announcement](https://support.google.com/googleplay/android-developer/answer/15899442?hl=en) → [original answer/13986130 target](https://support.google.com/googleplay/android-developer/answer/13986130) → [current consolidated Sensitive Permissions policy](https://support.google.com/googleplay/android-developer/answer/16558241?hl=en) | Reopened October 23, 2026: the old route redirects to the current consolidated article. Its photo/video section retains the Android 13/API 33+ core-functionality and declaration rule. The separate minimum-scope Help article records May 28, 2025 as the passed full-compliance date and lists private/enterprise device-management exceptions; the announcement date is not a current grace period. |
| October 25, 2023 policy announcement | [Android Photo Picker](https://developer.android.com/training/data-storage/shared/photo-picker), [`READ_MEDIA_IMAGES`](https://developer.android.com/reference/android/Manifest.permission#READ_MEDIA_IMAGES), and [`READ_MEDIA_VIDEO`](https://developer.android.com/reference/android/Manifest.permission#READ_MEDIA_VIDEO) | Read. The announcement says media access must relate directly to app functionality and recommends a system picker for one-time/infrequent needs. It is historical context; current Help and the consolidated policy govern. |
| Android Photo Picker implementation guide | [Android Privacy Codelab](https://developer.android.com/codelabs/android-privacy-codelab), [Cloud media providers](https://developer.android.com/guide/topics/providers/cloud-media-provider), [AndroidX Activity release notes](https://developer.android.com/jetpack/androidx/releases/activity), [Modular System Components](https://source.android.com/docs/core/ota/modular-system), and [Google System Updates](https://support.google.com/product-documentation/answer/11412553) | Reopened the guide and relevant sections of these targets on October 23. The codelab covers in-context permission requests, reducing location scope, Photo Picker, and data-access auditing; its “Learn more” link now redirects to the [Android Privacy & Security](https://developer.android.com/quality/privacy-and-security) overview. Cloud media providers are currently an OEM-nomination pilot: each OEM may nominate up to three apps, approved providers must meet technical and quality requirements, and only one provider can be active per Android profile. Implementing the API does not itself establish eligibility. If a service is not the user’s primary cloud-photo backup/retrieval source, consider a [Document Provider](https://developer.android.com/guide/topics/providers/create-document-provider). The Activity release page confirms that stable 1.11.0 includes HDR `MediaCapabilities`; system-component/update pages explain picker compatibility and do not create Play eligibility criteria. |
| Photo Picker → picker, availability, multi-select, URI, and transcoding APIs | [`PickVisualMedia`](https://developer.android.com/reference/androidx/activity/result/contract/ActivityResultContracts.PickVisualMedia), [`PickMultipleVisualMedia`](https://developer.android.com/reference/androidx/activity/result/contract/ActivityResultContracts.PickMultipleVisualMedia), [`MediaStore.getPickImagesMaxLimit()`](https://developer.android.com/reference/android/provider/MediaStore#getPickImagesMaxLimit%28%29), [`ContentResolver.takePersistableUriPermission()`](https://developer.android.com/reference/android/content/ContentResolver#takePersistableUriPermission%28android.net.Uri%2Cint%29), [`MediaCapabilities`](https://developer.android.com/reference/androidx/activity/result/contract/ActivityResultContracts.PickVisualMedia.MediaCapabilities) | Both `ActivityResultContracts` targets were opened as large API references and the relevant contract, availability, and fallback sections were checked. The no-argument `isPhotoPickerAvailable()` was deprecated in 1.7; the Context overload also checks for the OEM system-app fallback. Relevant `MediaStore` and `ContentResolver` sections were opened; `MediaCapabilities` confirms availability in stable Activity 1.11.0. The multi-select limit is the smaller of the contract and request values, but the final `ACTION_OPEN_DOCUMENT` fallback does not enforce a maximum. The picker guide also caps persisted grants at 5,000 and removes the oldest when exceeded. Other API members and samples remain partly unreviewed. |
| Android 14 runtime branch | [Grant partial access to photos and videos](https://developer.android.com/about/versions/14/changes/partial-photo-video-access) | Read. Covers `READ_MEDIA_VISUAL_USER_SELECTED`, partial access/reselection, and UI refresh. It does not replace Play's declaration review for broad media permission. |
| Historical deadline reminder | [Required actions by January 22, 2025](https://support.google.com/googleplay/android-developer/answer/15800983?hl=en) | Read. Declaration/removal, all testing and production tracks, and the May 28, 2025 extension endpoint are historical migration dates that have passed. |
| Play Console | [App content / permissions declaration](https://play.google.com/console/) | Sign-in required to see an individual app's form and review state; public pages cannot confirm approval for a package. |

These links cover policy descendants and the most relevant Android implementation branch found for this topic. The parent Help Community fetch failed, and the “Contact us” click did not return a verifiable destination URL; both are recorded as access limits. The AndroidX, cloud-provider, and system-component pages have further general API/navigation links; those are not expanded as new Google Play policy branches.

## Pre-release checks

1. Search the manifest, merged manifest, Gradle dependencies, SDKs, dynamic features, and all release tracks for `READ_MEDIA_IMAGES`, `READ_MEDIA_VIDEO`, `READ_MEDIA_VISUAL_USER_SELECTED`, and legacy storage permissions.
2. Map each permission to an actual user-facing feature; move occasional selection to Photo Picker or a document picker.
3. If broad access remains, prepare evidence for the core feature and a technical explanation of why alternatives fail, then submit the Console declaration. Do not confuse technical ability to request the permission with Play approval.
4. Test URI behavior under grant, denial, partial selection, revocation, app restart, and background upload.
5. Compare the privacy policy, in-app prominent disclosure, Data safety form, and SDK data flows; state whether media is uploaded, shared, retained, or deleted.

## Sources

- [Understanding Restricted Permissions with minimum scope alternatives](https://support.google.com/googleplay/android-developer/answer/16935362?hl=en)
- [Consolidated Developer Program Policy](https://support.google.com/googleplay/android-developer/answer/18258653?hl=en)
- [Policy announcement: October 25, 2023](https://support.google.com/googleplay/android-developer/answer/14016515?hl=en)
- [Android Photo Picker](https://developer.android.com/training/data-storage/shared/photo-picker)
- [Android 14 partial photo/video access](https://developer.android.com/about/versions/14/changes/partial-photo-video-access)
- [Google Play User Data](https://support.google.com/googleplay/android-developer/answer/10144311?hl=en)

This is a bilingual paraphrase based on official pages available on October 23, 2026, not a full policy copy. Confirm the actual Console declaration and review status in the developer account for each app.
