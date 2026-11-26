---
id: google-play.permissions-declaration
platform: google-play
language: en-US
authority: operational
status: current
kb_checked_at: 2026-10-22
review_due: 2027-01-22
regions: [global]
topics: [play-console, permissions, declaration, review, release]
snapshot_id: play.permissions-declaration
snapshot_package: "GooglePlay-KnowledgeBase-2026-10-24-review.zip"
coverage_status: "detailed-summary"
source_url: "https://support.google.com/googleplay/android-developer/answer/9214102?hl=en"
source_url_zh: "https://support.google.com/googleplay/android-developer/answer/9214102?hl=zh-CN"
effective_date: "current-as-reviewed"
---

# Play Console permissions declaration and review

> **Import note (Google batch 2).** The body is the paraphrased summary from the already separated 2026-10-24 Google Play knowledge-base snapshot (`play.permissions-declaration`, reviewed 2026-10-22). It is not a verbatim copy of a Google page. The English official page is the source of truth. `kb_checked_at` is the review date recorded in the snapshot source file; this import did not re-open the live official pages. Phrases such as “this knowledge base,” “this library,” and “local topic” describe coverage inside that snapshot, not the set of pages imported into this repository. Relative snapshot links to topics, link graphs, ledgers, or CSVs that are not in this repository are kept as text mentions. Relative links that target the Google batch 1 topics or these seven batch 2 topics point at the hub files. The snapshot records that the English Help body and the Simplified Chinese page were both opened, and that the substantive body links match. It does not record a failed fetch of this primary article. The linked Sensitive Permissions page announces location and contacts changes effective 2027-01-27; those future changes are not current declaration-form rules and stay dated separately. The Play Academy course link returned Cache miss, and the snapshot does not infer course content from the title. This page describes Play Console declaration and review steps. Evidence level: `operational`. It does not replace the applicable permission policies.

**Reviewed: 2026-10-22.** High-risk or sensitive permissions (such as SMS, Call Log, and background location) are reviewed in the release workflow. Technical eligibility does not mean approval; submit materials required by the current Console form and the applicable permission policy.

## When the declaration form appears

Uploading an App Bundle that requests a restricted permission not previously declared to Google Play can trigger the Permissions Declaration Form in the release flow. If any active bundle in an Open, Closed, or Internal testing track requires a declaration, Play Console shows an App content alert. You cannot publish any app changes, including store listing, price, or distribution changes, until you create a release with the declaration or remove the permissions.

Consider deactivating unused, noncompliant test tracks. If the newly requested permissions list contains permissions you do not plan to use, remove the affected Bundle/APK and upload a new package with the correct permission set instead of submitting an inaccurate declaration.

## Form steps

1. **Review the permission inventory:** Compare previously declared and newly requested permissions with manifests, all active tracks, and actual code behavior. New permissions enter review.
2. **Select core functionality:** Choose the supported use cases that match the app's real core features and the features prominently described on the store listing.
3. **Give review instructions:** Explain how reviewers can reach and verify the permission-dependent feature.
4. **Provide a video:** Demonstrate core functionality and permission use through YouTube (the Help page's preferred format) or an accessible cloud video file.
5. **Explain access to restricted content:** If sign-in or special access is required, provide a valid test-only account/number, password, and steps. Never provide production-user credentials. If no special access is needed, say that all functionality is available without it.
6. **Request a legacy APK exception only when applicable:** The SMS/Call Log exception field appears only for a multi-APK configuration where a variant requests those permissions. Check the conditions in the [SMS/Call Log policy](../sms-call-log/sms-call-log.en-US.md) or the [background location policy](https://support.google.com/googleplay/android-developer/answer/9799150), enter qualifying version codes, and deactivate APKs that do not qualify.
7. **Confirm the declaration:** Attest that the information is accurate and agree to use the permissions as declared.

After submitting the form, continue with app review preparation and release rollout. A declaration is review material, not a standalone policy exemption.

## Review period and release impact

- After form submission and rollout, the app receives an extended review. The Help page says it may take several weeks; the app/update can remain in Pending publication.
- Replacing a pending release can cause additional review delays.
- For an urgent release, the documented path is to remove high-risk/sensitive permissions from the App Bundle and roll out a new release. That release receives standard policy review; the Help page says it may publish within several hours, which is not a guaranteed SLA.
- If the app is noncompliant, Play sends the result to the developer account's Account Owner and contact email. If the declaration and the overall app are approved, the release is automatically published.

## Special flow for Publishing API users

Releasing through the Google Play Developer Publishing API can return an error if the permission request has not yet been approved. The developer must either:

1. Remove the high-risk/sensitive permissions and upload a compliant Bundle; or
2. Use the Play Console web UI to upload the Bundle, complete the Permissions Declaration Form, and roll out that release.

Use the Publishing API again after the declaration and policy review are approved. Any newly requested permission requires a revised declaration through the Console UI.

## Pre-submission checklist

- [ ] Inventory every active production, Open, Closed, and Internal test Bundle/APK.
- [ ] Map each permission to an allowed policy use, implemented core feature, store listing text, and actual data flow.
- [ ] Remove accidental or unnecessary permissions and deactivate unused noncompliant test tracks.
- [ ] Ensure the video, reproduction steps, and test-only credentials let reviewers reach restricted functionality.
- [ ] Align the privacy policy, in-app prominent disclosure/consent, Data safety declaration, and SDK behavior with the declared use.
- [ ] Allow time for extended review; a submitted form or test-track status is not permission approval.

## Related pages

| Page | Relationship to the declaration |
| --- | --- |
| [SMS and Call Log permissions](../sms-call-log/sms-call-log.en-US.md) | Lists permitted handlers, temporary exceptions, disallowed uses, alternative APIs, and legacy APK exception criteria. |
| [Sensitive permissions overview](../sensitive-permissions/sensitive-permissions.en-US.md) | Explains core functionality, minimum scope, disclosure/consent, and requirements for other restricted permissions. |
| [User Data policy](../user-data/user-data.en-US.md) and [Data safety form](../data-safety/data-safety.en-US.md) | User disclosure, privacy policy, Data safety declaration, and SDK review still apply outside the declaration form. |
| [Background location permissions](https://support.google.com/googleplay/android-developer/answer/9799150) | Another sensitive-permission use case requiring a declaration and review evidence. |
| [Prepare your app for review](https://support.google.com/googleplay/android-developer/answer/9859455) and [Prepare and roll out a release](https://support.google.com/googleplay/android-developer/answer/9859348) | Review preparation and release actions after the declaration; follow the current Play Console flow. |
| [Developer Program Policy](../developer-program-policy/developer-program-policy.en-US.md) | The broader program rules that apply beyond the permission declaration. |

## Direct body links, audited individually

The English body has 14 link occurrences, deduplicated to 11 external targets and one same-page anchor. The Publishing API and “prepare and roll out your release” links each appear twice. The Simplified Chinese page was opened separately; its substantive body links match. This table counts body links, not the Help Center navigation rail.

| Body link target | Access result and relationship |
| --- | --- |
| [Android App Bundle (legacy body URL)](https://developer.android.com/platform/technology/app-bundle/index.html) → [current guide](https://developer.android.com/guide/app-bundle) | The old Android Developers route redirects to the current App Bundle guide. It explains the upload format and how Play generates device-specific APKs; this is release-technology context, not permission approval. See [app setup](../play-console-app-setup/play-console-app-setup.en-US.md) and the [release workflow](../publishing/play-release-workflow.en-US.md). The guide's technical descendants are not fully traversed. |
| [High-risk or sensitive permissions](https://play.google.com/about/privacy-security-deception/permissions/) → [current Sensitive Permissions policy](https://support.google.com/googleplay/android-developer/answer/16558241?hl=en) | The legacy policy entry first redirects to `answer/16324062`, then to the consolidated current policy at `answer/16558241`. The current page also announces location and contacts changes effective **January 27, 2027**; current rules and future-effective changes must be distinguished by date. See [Sensitive Permissions](../sensitive-permissions/sensitive-permissions.en-US.md). |
| [Google Play Developer Publishing API](https://developers.google.com/android-publisher/) | The API overview describes uploading/publishing apps, managing tracks and store listings, and transactional edits. The permission rule is an additional release gate: initial or newly requested restricted permissions still require Console declaration/review; API references do not create a policy exemption. See the [release workflow](../publishing/play-release-workflow.en-US.md). |
| This page's [special instructions for Publishing API users](https://support.google.com/googleplay/android-developer/answer/9214102?hl=en) | The same-page link returns to this article's API instructions; it is not a separate destination. Its anchor may change with the Help Center structure. |
| [Published guidelines (legacy Help page)](https://support.google.com/googleplay/android-developer/answer/9888170) → [current Sensitive Permissions policy](https://support.google.com/googleplay/android-developer/answer/16558241?hl=en) | Legacy `answer/9888170` redirects to the current Sensitive Permissions page, converging with the policy link above; do not count it as a separate current rule. |
| [SMS or Call Log permission groups (legacy Help page)](https://support.google.com/googleplay/android-developer/answer/9047303) → [current SMS/Call Log policy](https://support.google.com/googleplay/android-developer/answer/10208820?hl=en) | Legacy `answer/9047303` redirects to `answer/10208820`. Default-handler eligibility, allowed uses, alternative APIs, declarations, and denial examples are summarized in the [SMS/Call Log topic](../sms-call-log/sms-call-log.en-US.md). |
| [Background location permissions](https://support.google.com/googleplay/android-developer/answer/9799150?hl=en) | The article cites this as an additional rule for legacy APK exceptions and sensitive permissions. It was opened and summarized in the [background-location topic](../background-location/background-location.en-US.md); form, video, and disclosure descendants remain partly open. |
| [Prepare your app for review (legacy Help page)](https://support.google.com/googleplay/android-developer/answer/9815348) → [current review-preparation article](https://support.google.com/googleplay/android-developer/answer/9859455?hl=en) | Legacy `answer/9815348` redirects to current `answer/9859455`. Reviewer credentials, App content, and policy/store prerequisites are covered in [app review preparation](../app-review-preparation/app-review-preparation.en-US.md). |
| [Prepare and roll out a release (legacy Help page)](https://support.google.com/googleplay/android-developer/answer/7159011) → [current release workflow](https://support.google.com/googleplay/android-developer/answer/9859348?hl=en) | Legacy `answer/7159011` redirects to current `answer/9859348`. The steps after permission approval are cross-linked to the [release workflow](../publishing/play-release-workflow.en-US.md). |
| [Pending publication (legacy Help page)](https://support.google.com/googleplay/android-developer/answer/6334282) → [current Publish your app Help page](https://support.google.com/googleplay/android-developer/answer/9859751?hl=en) | Legacy `answer/6334282` redirects to the current status page, which explains app, update, and item statuses. These statuses do not indicate that the permission declaration itself has been approved. See the [release workflow](../publishing/play-release-workflow.en-US.md). |
| [Google Play policies (legacy entry)](https://play.google.com/policy) → [Developer Policy Center](https://play.google/developer-content-policy/) | The old entry redirects to the policy directory. The directory is not the consolidated Developer Program Policy body; see the [Developer Program Policy topic](../developer-program-policy/developer-program-policy.en-US.md). |
| [Play Academy: Play Console permissions course](https://playacademy.exceedlms.com/student/path/264896) | The body course link was attempted and returned Cache miss; its lesson text and descendants could not be read, so no course content is inferred from its title. |

## Help Center sidebar destinations (separate from body links)

The page shows 29 navigation items including itself; all 28 other destinations were clicked or have independent page-audit records. The sidebar is a publishing/account/product-help navigation rail, not part of the policy body. Existing bilingual summaries and access states are cross-referenced below; a few generic support directories or technical pages have only an entry-level or limited summary.

| Sidebar destination | Local relationship and audit status |
| --- | --- |
| [Create and set up your app](https://support.google.com/googleplay/android-developer/answer/9859152?hl=en) | [App setup](../play-console-app-setup/play-console-app-setup.en-US.md); the sidebar click timed out, but this target has an independent full-body audit. |
| [App testing requirements for new Personal developer accounts](https://support.google.com/googleplay/android-developer/answer/14151465?hl=en) | The [release workflow](../publishing/play-release-workflow.en-US.md) covers account scope, 12 testers/14 days, production access, and 14 body targets. |
| [Device verification requirements for new developer accounts](https://support.google.com/googleplay/android-developer/answer/14316361?hl=en) | Cross-referenced in [Play Console Requirements](../play-console-requirements/play-console-requirements.en-US.md) and Developer Verification (snapshot: `../android-developer-verification-en.md`, not imported in this repository); account/device actions require sign-in. |
| [Set up your app on the app dashboard](https://support.google.com/googleplay/android-developer/answer/9859454?hl=en) | Covered by [app setup](../play-console-app-setup/play-console-app-setup.en-US.md); Console tasks vary by account and app. |
| [Inspect app versions](https://support.google.com/googleplay/android-developer/answer/9844279?hl=en) | [App setup](../play-console-app-setup/play-console-app-setup.en-US.md) summarizes App Bundle Explorer/version details; actual app data requires sign-in. |
| [Prepare and roll out a release](https://support.google.com/googleplay/android-developer/answer/9859348?hl=en) | The [release workflow](../publishing/play-release-workflow.en-US.md) covers testing tracks, versions, signing, staged rollout, and submission. |
| [About your submission activity](https://support.google.com/googleplay/android-developer/answer/17118609?hl=en) | The [release workflow](../publishing/play-release-workflow.en-US.md) records submission IDs, source, and status history; Google says up to one year of records is retained from May 1, 2026. |
| [Halting a fully rolled-out release](https://support.google.com/googleplay/android-developer/answer/16285429?hl=en) | The [release workflow](../publishing/play-release-workflow.en-US.md) says a 100% rollout can be halted on tracks other than Internal testing; fallback eligibility is limited. |
| [Detect app issues early with pre-review checks](https://support.google.com/googleplay/android-developer/answer/14807773?hl=en) | The [release workflow](../publishing/play-release-workflow.en-US.md) summarizes the pre-review entry point, scope, and limits; a pre-check pass is not final policy approval. |
| [Publish your app](https://support.google.com/googleplay/android-developer/answer/9859751?hl=en) | The [release workflow](../publishing/play-release-workflow.en-US.md) covers app/update/item states, rejection, and managed publishing. |
| [Helpful tips to get your app published](https://support.google.com/googleplay/android-developer/answer/15191715?hl=en) | Opened and all 13 body links were attempted; store listing, reviewer access, testing, and rejection remediation are linked to the [release workflow](../publishing/play-release-workflow.en-US.md). |
| [Best Practices for White Label Developers](https://support.google.com/googleplay/android-developer/answer/15884185?hl=en) | Opened and all 11 body links were attempted; recommends decentralized client accounts, unique listings, and pre-submission quality checks. See the white-label announcement resources (snapshot: `../google-play-announcement-resources-en.md`, not imported in this repository). |
| [Update or unpublish your app](https://support.google.com/googleplay/android-developer/answer/9859350?hl=en) | The [Target API topic](../target-api/target-api-level.en-US.md) and [release workflow](../publishing/play-release-workflow.en-US.md) distinguish unpublishing from reduced visibility on newer Android versions. |
| [Control when app changes are reviewed and published](https://support.google.com/googleplay/android-developer/answer/9859654?hl=en) | The [release workflow](../publishing/play-release-workflow.en-US.md) distinguishes sending changes for review from managed publishing; the sidebar click errored, but this target has an independent full-body audit. |
| [Release app updates with staged rollouts](https://support.google.com/googleplay/android-developer/answer/6346149?hl=en) | The [release workflow](../publishing/play-release-workflow.en-US.md) covers staged rollout, halting, and increasing percentages; descendants remain partial. |
| [Prompt users to update to your latest app version](https://support.google.com/googleplay/android-developer/answer/13812041?hl=en) | The [release workflow](../publishing/play-release-workflow.en-US.md) covers Recovery eligibility, scope, and Wear OS/TV/Automotive exclusions. |
| [Manage your store listings](https://support.google.com/googleplay/android-developer/topic/3450987?hl=en) | Opened as a store-listing navigation directory; topic descendants are covered in [Store Listing and Asset Best Practices](../store-listing-best-practices/store-listing-best-practices.en-US.md), not expanded again here. |
| [Distribute your instant experience](https://support.google.com/googleplay/android-developer/answer/7381861?hl=en) | This is a historical Instant Apps workflow; current retirement and migration information are in the Android Instant Apps history topic (snapshot: `android-instant-apps-en.md`, not imported in this repository). |
| [Manage different form-factor releases](https://support.google.com/googleplay/android-developer/answer/13295490?hl=en) | [App review preparation](../app-review-preparation/app-review-preparation.en-US.md) and app quality/form factors (snapshot: `app-quality-and-form-factor-guidelines-en.md`, not imported in this repository) distinguish release tracks from quality requirements. |
| [Add or test APK expansion files](https://support.google.com/googleplay/android-developer/answer/2481797?hl=en) | The legacy APK expansion Help page opened; the AAB/OBB boundary is summarized in [app setup](../play-console-app-setup/play-console-app-setup.en-US.md). Check applicability for the specific legacy app/upload path. |
| [Google Play game services](https://support.google.com/googleplay/android-developer/topic/7071327?hl=en) | Only the Help Center directory was opened; its game-services descendants are outside this permission declaration topic and are not claimed as traversed. |
| [Using third-party SDKs in your app](https://support.google.com/googleplay/android-developer/answer/10358880?hl=en) | SDK warnings and developer responsibility are covered in Third-Party SDK Requirements (snapshot: `sdk-requirements-en.md`, not imported in this repository); app-specific Console alerts require sign-in. |
| [Target API level requirements](https://support.google.com/googleplay/android-developer/answer/11926878?hl=en) | The [Target API topic](../target-api/target-api-level.en-US.md) records the matrix and extension as of October 22, 2026; recheck the annual threshold before release. |
| [Create and distribute a watch face](https://support.google.com/googleplay/android-developer/answer/13560201?hl=en) | [App review preparation](../app-review-preparation/app-review-preparation.en-US.md) covers Wear OS tracks, assets, format, and review; the category/tags target timed out. |
| [Prepare your app for review](https://support.google.com/googleplay/android-developer/answer/9859455?hl=en) | [App review preparation](../app-review-preparation/app-review-preparation.en-US.md) covers reviewer access, policy declarations, and store-content prerequisites; deeper account routes remain limited. |
| [Request more time to complete a policy declaration](https://support.google.com/googleplay/android-developer/answer/15644220?hl=en) | Extension forms must be opened from a specific Console warning; eligibility and submitted state cannot be verified publicly. See [Play Console Requirements](../play-console-requirements/play-console-requirements.en-US.md). |
| [Manage your store listing, experiment, and event graphics with the Asset Library](https://support.google.com/googleplay/android-developer/answer/16386748?hl=en) | [App review preparation](../app-review-preparation/app-review-preparation.en-US.md) and [store listing and asset best practices](../store-listing-best-practices/store-listing-best-practices.en-US.md) cover Asset Library operations, asset policy, and DDA context. |
| [Version codes](https://support.google.com/googleplay/android-developer/answer/17367361?hl=en) | [App review preparation](../app-review-preparation/app-review-preparation.en-US.md) covers version ordering/limits and links the Android multi-APK technical guide. |

## Coverage

This page organizes the Chinese and English source articles' form trigger, all seven steps, testing-track effects, review timing, urgent-release path, and Publishing API flow. It also records the 11 unique external body targets, one same-page anchor, and 28 peer destinations in the sidebar. Body targets were opened, redirect-checked, or explicitly marked as a course cache miss. Four sidebar clicks errored, but those targets have independent full-body audit records. **Descendant links are not infinitely closed**: remaining priorities include the background-location form/best-practice branch, Android App Bundle technical descendants, and the Play Games directory. Sign-in-only pages, courses, and deeper API examples retain explicit access limits.

This is a structured bilingual paraphrase, not a verbatim copy. The official source and current Console form control.
