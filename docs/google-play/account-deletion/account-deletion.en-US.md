---
id: google-play.account-deletion
platform: google-play
language: en-US
authority: normative
status: current
kb_checked_at: 2026-10-24
review_due: 2027-01-24
regions: [global]
topics: [account-deletion, data-deletion, data-safety, user-data, retention, privacy]
snapshot_id: play.account-deletion
snapshot_package: "GooglePlay-KnowledgeBase-2026-10-24-review.zip"
coverage_status: "detailed-summary"
source_url: "https://support.google.com/googleplay/android-developer/answer/13327111?hl=en"
source_url_zh: "https://support.google.com/googleplay/android-developer/answer/13327111?hl=zh-CN"
---

# App account and associated data deletion

> **Import note (Google batch 2).** The body is the paraphrased summary from the already separated 2026-10-24 Google Play knowledge-base snapshot (`play.account-deletion`, reviewed 2026-10-24). It is not a verbatim copy of a Google page. The English official page is the source of truth. `kb_checked_at` is the review date recorded in the snapshot source file; this import did not re-open the live official pages. Phrases such as “this knowledge base,” “this library,” and “local topic” describe coverage inside that snapshot, not the set of pages imported into this repository. Relative snapshot links to topics, link graphs, ledgers, or CSVs that are not in this repository are kept as text mentions. Relative links that target the Google batch 1 topics or these seven batch 2 topics point at the hub files. The snapshot reopened the English Help article and the Simplified Chinese `hl=zh-Hans` body and records that they agree on scope, in-app and external paths, associated-data deletion, processors, timing, and exceptions. The exact `hl=zh-CN` route was inaccessible in that pass; the Chinese content check used the opened `zh-Hans` page, and the two locale outcomes stay separate. That fetch failure is not a content change. The Chinese hub text is the snapshot paraphrase, not Google’s published Chinese page text. December 7, 2023 and May 31, 2024 remain expired migration dates. The account-deletion requirement is `normative`. Data safety form answers and Play Console fields described here are operational and do not replace the User Data requirement. This topic stays separate from the User Data and Data safety pages.

**Reviewed October 24, 2026.** If any part of an app lets users create an app account—including a registration flow the app sends them to outside the app—the Google Play User Data policy requires a way to request account deletion. Mobile apps need initiation paths both in and outside the app. Developers must also accurately answer the deletion questions in the Play Console Data safety form. Logging out, deactivating, or freezing an account is not deletion.

## Scope and exceptions

- An app account is a user-facing identity/login mechanism provided by the developer for use across one or more apps or devices. Account creation can happen in the app or through an external flow the app directs users to. The requirement still applies if some features work without an account, as long as any part of the experience enables account creation.
- Accounts created and operated only offline, without an online app account, are outside this policy definition. Permanently private apps and enterprise device-management apps may qualify for an exemption; verify the app's actual category instead of extending the exception to ordinary enterprise tools or apps with only some private features.
- Non-mobile surfaces (such as web, Android TV, or Wear OS) do not need an in-app deletion entry, but still need a readily discoverable external initiation path and a URL entered in Console. A mobile app may link to an external deletion resource; a fully native end-to-end flow is not the only allowed implementation.

## Required deletion paths

| Location | Requirement |
| --- | --- |
| In the app (mobile apps) | Provide an intuitive, prominent, easily found entry—typically in account settings or a similar area. It can complete deletion or link to the external web resource. |
| Outside the app | Provide a working, discoverable web resource where a user can actually initiate the request. A user who uninstalled the app must not have to reinstall it. |
| Play Console | All developers must answer the Data safety deletion questions. In-scope account-deletion apps must disclose whether they support account deletion and provide the web link. Some answers appear in the store listing's Data safety/deletion area. |
| Service providers | Delete associated data from your own systems and ask providers processing data for you to delete their copies as well. |

The external resource must load, prominently explain the deletion path, and identify the app or developer name as shown on the Play store listing. It can be a dedicated page, request form, or support email. If users must take additional steps, such as canceling a subscription, clearly explain them and provide a support flow that can complete the request. A privacy-policy paragraph without an actual request path is insufficient.

## What to delete, timing, and permissible retention

When a user requests app-account deletion, delete the user data associated with that account, including data declared as collected in Data safety. It may include personal identifiers, payment/financial and authentication information, contacts, location, SMS/call data, health/Health Connect, microphone/camera, installed-app inventory, and other sensitive device or usage data.

- Fulfill requests within a reasonably short time and tell users what to expect. Deletion and retention deadlines vary by jurisdiction; a generic estimate does not replace local-law review.
- Data may be retained when genuinely needed for security, fraud prevention, or regulatory compliance, subject to applicable rules. Clearly explain the data, reason, and retention practice (for example, in the privacy policy). Highly regulated industries may need additional steps to complete a request.
- The Data safety deletion-mechanism question is related but distinct from account deletion. A discoverable request channel—such as an in-app entry, form, or dedicated email—can support the Data safety declaration. If there is no request mechanism, the official FAQ permits selecting that mechanism badge when data is automatically deleted or anonymized within 90 days of collection. This 90-day option does not exempt an account-creating app from its in-app and external account-deletion paths.

## Data safety and user-visible information

The Data safety form must accurately reflect practices across all versions, regions, and age audiences currently distributed through Play. Keep deletion answers and the external link consistent with the privacy policy; a form approval or store badge does not replace actually deleting data. Google Play may show a deletion mechanism/data-deletion area on the store listing so users can review or initiate a request.

The **December 7, 2023** form deadline and **May 31, 2024** extension endpoint shown in the older Help article are historical and have passed. They are not future deadlines; keep the current form and link accurate and functional.

## Official experience-design best practices

The Android Developers Blog's five recommendations map to the current Help requirements as follows. This crosswalk separates UX advice from mandatory controls so that automation, account recovery, or surveys are not mistaken for universal approval conditions:

| UX recommendation | Current Play control it supports | Evidence to verify |
| --- | --- | --- |
| **Make it seamless:** reduce navigation and offer a direct route from account settings or another prominent place. | The in-app path for a mobile app must be intuitive and prominent. It may link to the external deletion resource; an end-to-end native flow is not required. Play does not prescribe a fixed number of taps. | Test the route from the normal account entry point; record screens/steps and confirm that back, denial, or re-authentication does not hide the option. |
| **Prefer automatic handling:** if automation is not available, use a request form or dedicated support path. | The requirement is a real way to initiate a request and completion within a reasonably quick period. A web link, support email, or form can provide that path; deletion does not have to be instant or fully automated. | Submit through signed-in and signed-out states; retain receipt, owner, service target, and escalation path. Confirm that “contact support” does not lead to a dead end. |
| **Explain implications early:** explain steps such as subscriptions or data export; a Help Center can describe the process. The blog also suggests considering account recovery within a reasonable period. | If extra steps are genuinely needed before deletion (for example, subscription cancellation), current Help requires them to be clearly explained and a support flow to be available. Recovery or export reminders are UX suggestions, not universal Play deletion requirements. | Keep the deletion copy, prerequisites, and support route; review real subscription, paid-content, and export scenarios so unrelated steps do not delay deletion. |
| **Confirm progress and outcome:** clarify when the account and cloud data are handled, and why some data may remain. | A request to delete an account also covers associated user data, including copies held by service providers. Developers should set expectations and complete requests in a reasonably quick period. Any security, anti-fraud, or regulatory retention must be transparent; local law may set specific limits, while Play Help gives no single number of days for all apps. | Retain request status/completion records, processor deletion requests or confirmations, a justified retention list, applicable basis/period, and user notices. |
| **Support users who uninstalled:** let them initiate deletion on the web; feedback can be invited. | For apps that allow account creation, the external web resource is required and must initiate account and associated-data deletion without requiring reinstallation. It must work, be easy to find, identify the app/developer as shown on the Play listing, and be entered in Data safety. Surveys or feedback must be optional and cannot block deletion. | Open the store-listing link in a browser where the app is not installed; verify the name, discoverability, successful submission, and no forced reinstall. Confirm a survey can be skipped. |

The **“new account deletion policy”** link in the 2024 UX post resolves to the [2023 policy-launch announcement](https://android-developers.googleblog.com/2023/04/giving-people-more-control-over-their-data.html), not to the current Help text. The current [Account Deletion Help article](https://support.google.com/googleplay/android-developer/answer/13327111?hl=en) links back to the 2024 blog as best-practice guidance. The 2023 announcement says account deletion also covers associated data, permits separate deletion of other data where applicable, and requires a web request path for users who uninstalled. Its December 7, 2023 and May 31, 2024 Data safety migration dates have passed; current obligations come from the live User Data and Account Deletion Help pages.

### Direct body links and assets in the 2024 UX post

| Body destination | Access and relationship |
| --- | --- |
| [“new account deletion policy”](https://android-developers.googleblog.com/2023/04/giving-people-more-control-over-their-data.html) | Rechecked on October 24 and confirmed as the 2023 policy-launch announcement. All 13 of that post's body destinations were attempted previously and are recorded in the announcement child-link audit ([announcement resources](../google-play-announcement-resources/google-play-announcement-resources.en-US.md)). The rollout dates in that post are historical. |
| [Header case-study image](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhljLTe4e3m2lCTVHZukvwtt3N5A34tfp3uQ9kITH8m5EM-9FI-7752LR4HofGCVBUzc9aaTXmUEC_xrKJnNW1R4pzx9YCZMFxWDxF64PWv8Zg6Yai3XKNlDvRv_PjR8QE8gikqfChslevvcNF8SzPET1WNH-_thMq-svIuGSTQ5t_KrFoE-SUWok28Xhc/s1600/social-Account-Deletion-Case-Study-Blog.png) | Cache miss. Recorded as a visual example only; no requirements are inferred from the unavailable image. |
| [Canva flow example](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhSmgP5HlDbudibibZxpVwLrzDcBnt2rg_ITmTLc2t_OFMIDPyLBzQJxeBfmyyp_nk1OL0Yd-pkQKiPFUqH0WyUbcDloblVhUOv6HcW-I0iNeTOghSLQjcQnVyqEFBEpXjqT5zDcIJUFnrcAEyh_-8Y2HxwW3sRCsP4glQPy03pBG40xhwC6G9qOClzmugk/s1600/Account-Deletion-Google-Play-inline%20%281%29.png) | The URL was attempted and returned a binary asset without extractable text. The parent-page alt text identifies it as a Canva in-app deletion-flow example, not a policy clause. |
| [SYBO Games web-flow example](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi59KSA_oGI24P30Um9abe7fLhiYoTWKn5q8oJ2lDsKScf30Jq6GyC_ZAWCfCAYfwiGRD4jdN4n5KCCXFH7L-zdCY7efdN96HhsuTmOFvQNUw5l75QoLBa43i_LPo5ph1-W64y3fTSKRXFMLIy8TeFWa-pY-qjpX-0j9Tg0mroJcxc56ZFAmRjH06kvKCE/s1600/Account-Deletion-Google-Play-inline-2.png) | The URL was attempted and returned a binary asset without extractable text. The parent-page alt text identifies it as a SYBO Games web deletion-flow example, not a policy clause. |

The Android Developers header/footer navigation, blog categories, previous/next posts, and general privacy/license/brand links are site-shell or general resources, not Play deletion obligations stated in the article body. This audit covers the body's policy link and three image destinations; it does not claim recursive review of the whole site navigation.

All 13 body links in the 2023 launch post have now been attempted: Data safety, account-deletion Help, and the April 5, 2023 Play policy notice are represented in the bilingual topics/announcement link table; PolicyBytes has no readable full transcript, the global webinar requires sign-in, several regional webinar short links were unreadable, and the community is dynamic peer support. See the announcement child-link audit ([announcement resources](../google-play-announcement-resources/google-play-announcement-resources.en-US.md)) for individual statuses and policy relationships. This records the direct-link layer; it does not claim closure of infinitely deep external descendants.

### Current Account Deletion Help body links and shared sidebar (October 24, 2026)

Reopened both the [English account-deletion Help article](https://support.google.com/googleplay/android-developer/answer/13327111?hl=en) and its Simplified Chinese `zh-Hans` body: 251 rendered lines in English and 268 in Chinese. The exact `hl=zh-CN` route was inaccessible in this pass, so the Chinese content check uses the successfully opened `zh-Hans` page; the two locale-route outcomes are kept separate. Both bodies agree on scope, in-app/external request paths, associated-data deletion, processors, reasonably quick fulfillment, and exceptions. The still-displayed December 7, 2023 and May 31, 2024 dates are expired migration deadlines, not future dates. The previously inventoried policy body has **7 link anchors/5 normalized destinations**; the footer adds two support routes (**9 anchors/7 normalized destinations** total). The shared 32-item “Policy education and app requirements” sidebar is navigation, not additional account-deletion requirements.

| Destination type | Access and policy relationship |
| --- | --- |
| [Current User Data policy](https://support.google.com/googleplay/android-developer/answer/10144311?hl=en) | The Help body's legacy `answer/13316080` link timed out again in this pass; that alias was previously recorded as redirecting to current `answer/10144311`. Opened the canonical 329-line body directly today and confirmed its separate Account Deletion Requirement; see the [User Data topic](../user-data/user-data.en-US.md). The alias timeout does not mean the canonical policy body is unavailable. |
| [2024 Android Developers UX post](https://android-developers.googleblog.com/2024/03/designing-your-account-deletion-experience-google-play.html) | Successfully reopened the full 82-line English article today (published March 6, 2024). The five recommendations and their crosswalk to current mandatory controls appear above. They are UX practices, not separate approval clauses. |
| Play Console App content | The article points to an account-specific form. This retry redirected to Google sign-in, so no app-specific answers, status, or form fields are inferred. |
| Store-listing example image | The current target returned a GIF image type that the browser tool cannot preview. It illustrates the data-deletion badge/store listing and is not policy text. |
| [Data safety Help article](https://support.google.com/googleplay/android-developer/answer/10787469?hl=en) | Reopened from the FAQ link today and rechecked lines 546–559: the form requires a deletion-mechanism answer; no mechanism type is prescribed, and the mechanism badge may be selected when collected data is automatically deleted or anonymized within 90 days. The FAQ's anonymization example links to Google's [anonymization explainer](https://policies.google.com/technologies/anonymization?hl=en); both locale bodies were reopened, with k-anonymity, l-diversity, differential privacy, and the embedded-video fetch failure summarized in the [Data safety topic](../data-safety/data-safety.en-US.md). That Google page is not a Play algorithm/threshold standard, and the form option does not exempt account-creating apps from the in-app/external account-deletion paths. |
| Help Community and Contact us | Neither footer link returned readable policy text in this pass. Community discussions are dynamic peer support; Contact us is an account-specific support route, recorded separately in the URL ledger. |

The article also links to the shared [Policy education and app requirements index](https://support.google.com/googleplay/android-developer/topic/12798386?hl=en). On October 23, I confirmed that its 32 items match the shared sidebar inventory ([Age restrictions, anonymous chat, and child safety](../age-restricted-child-safety/age-restricted-child-safety.en-US.md)), then attempted each target directly from this article: 31 returned page bodies; the Android Health Permissions FAQ timed out, and its prior full-body audit remains. The final foreground-service preview is summarized separately in the foreground-services topic ([Foreground services and geofencing migration](../foreground-services-and-geofencing/foreground-services-and-geofencing.en-US.md)). These entries are Help navigation/recommendations, not account-deletion clauses. Their own grandchildren have mixed coverage; this does not claim infinite recursion.

These are design recommendations. Formal requirements remain discoverable request paths, actual deletion, reasonable handling, accurate declarations, and transparent retention.

## Pre-release checklist

1. Inspect app and external registration flows, account systems, and client surfaces to determine whether any path creates an online app account.
2. Verify the mobile entry in account settings and test the external link from a browser after uninstall; confirm users can submit a request without reinstalling.
3. Trace requests through app databases, backups/deletion queues, cloud providers, support tools, analytics/ad SDKs, and other processors; document a reasonable fulfillment time.
4. List data retained by law, the basis, retention period, and user notice. Verify support can complete any required extra steps such as identity checks or subscription cancellation.
5. Update Play Console Data safety deletion answers and the external URL; align them with the privacy policy, store name, and in-app flow, then retest the link.
6. Keep evidence for offline accounts, permanently private/enterprise device-management apps, or non-mobile surfaces; do not extend an exception to other features by assumption.

## Sources, descendants, and related pages

- [Understanding Google Play’s app account deletion requirements](https://support.google.com/googleplay/android-developer/answer/13327111?hl=en)
- [User Data policy — Account Deletion Requirement](https://support.google.com/googleplay/android-developer/answer/10144311?hl=en#account-deletion-requirement)
- [Provide information for Google Play’s Data safety section — deletion-mechanism FAQ](https://support.google.com/googleplay/android-developer/answer/10787469?hl=en)
- [Android Developers Blog: Designing your account deletion experience with users in mind](https://android-developers.googleblog.com/2024/03/designing-your-account-deletion-experience-google-play.html)
- [Android Developers Blog: Giving Users More Transparency and Control Over Account Data (2023 policy launch)](https://android-developers.googleblog.com/2023/04/giving-people-more-control-over-their-data.html)
- Related topics: [User Data](../user-data/user-data.en-US.md), [Data safety](../data-safety/data-safety.en-US.md), [Permissions declaration and review](../permissions-declaration/permissions-declaration.en-US.md), and Age restrictions and child safety ([Age restrictions, anonymous chat, and child safety](../age-restricted-child-safety/age-restricted-child-safety.en-US.md)).

This is a structured paraphrase. Actual deletion requests must also follow applicable privacy law, consumer/subscription rules, and processor contracts; verify current Console forms and account-review status in the developer account.
