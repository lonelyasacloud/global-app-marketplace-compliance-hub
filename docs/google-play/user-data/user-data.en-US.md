---
id: google-play.user-data
platform: google-play
language: en-US
authority: normative
status: current
kb_checked_at: 2026-10-24
review_due: 2027-01-24
regions: [global]
topics: [user-data, privacy, sdk, consent, data-safety, account-deletion]
snapshot_id: play.user-data
snapshot_package: "GooglePlay-KnowledgeBase-2026-10-24-review.zip"
coverage_status: "detailed-summary"
source_url: "https://support.google.com/googleplay/android-developer/answer/10144311?hl=en"
source_url_zh: "https://support.google.com/googleplay/android-developer/answer/10144311?hl=zh-Hans"
effective_date: "current-policy"
---

# User Data

> **Import note (Google batch 1).** The body is the paraphrased summary from the already separated 2026-10-24 Google Play knowledge-base snapshot. It is not a verbatim copy of a Google page. The English official page is the source of truth. `kb_checked_at` is the review date recorded in the snapshot source file; this import did not re-open the live official pages. Phrases such as “this knowledge base,” “this library,” and “local topic” describe coverage inside that snapshot, not the set of pages imported into this repository. Relative snapshot links to topics, link graphs, ledgers, or CSVs that are not in this repository are kept as text mentions. Relative links that target the six topics in this batch now point at the hub files. The readable Simplified Chinese official route recorded in the snapshot is `hl=zh-Hans`. A retry on 2026-10-24 returned HTTP 429 for English and HTTP 500 for the Chinese route; the snapshot did not treat that failure as a content change, because an earlier full read the same day had succeeded. The prominent-disclosure best-practices child is labelled as guidance in the snapshot; the binding rules remain the User Data policy. Evidence level: `normative` for the policy. That best-practices child is operational guidance.

**Reviewed: 2026-10-24.** This page paraphrases the main sections of the current official article. It is not a replacement for the full policy. Technical links and deeper article descendants are still being added to the link inventory.

## Scope and responsibility

“User data” covers information obtained from or about a user, including device information. Developers must disclose how their app accesses, collects, uses, handles, and shares user data, and limit use to disclosed, policy-compliant purposes. Developers must also comply with privacy and data-protection laws in the jurisdictions where their products or services are offered.

Responsibility includes third-party code integrated into the app, including SDKs, services, and AI integrations. The developer must review their practices, ensure disclosures and consent are sufficient, and prevent impermissible sales or expanded uses. If Google Play requests evidence that third-party code designed to collect sensitive data by default satisfies prominent disclosure and consent requirements, provide sufficient evidence within two weeks unless the request specifies a longer period.

## Persistent device identifiers

Do not associate persistent identifiers such as IMEI, IMSI, or SIM serial number with personal or sensitive data or resettable device identifiers. Narrow exceptions include telephony associated with SIM identity and enterprise device-management apps operating in device-owner mode. Prominently disclose permitted exception use. Remove SDKs that cannot be brought into compliance.

## Personal and sensitive user data

Examples include identity, financial and payment, authentication, phonebook/contact, location, SMS/call, health and Health Connect, installed-app inventory, microphone, camera, and other sensitive device or usage data.

When handling this data, developers must:

- Limit access, collection, use, and sharing to app/service functionality and policy-compliant purposes reasonably expected by users. Advertising use must also comply with the Ads policy.
- Transfer data only in permitted situations such as providing a service, legal obligations, valid government requests, or a merger/acquisition with adequate notice.
- Use security measures, including modern encryption in transit.
- Use Android runtime permissions where available before accessing permission-gated data.
- Never sell personal and sensitive user data. The current [User Data policy](https://support.google.com/googleplay/android-developer/answer/10144311?hl=en) defines a sale as an exchange or transfer of this data to a third party for monetary consideration. A user-initiated transfer (for example, using an app feature to send a file to a third party) is not treated as a sale under this definition. This answers only the sale classification; separately assess purposes, disclosure, affirmative consent, security, and Data safety reporting.

## Prominent disclosure and affirmative consent

When access, collection, use, or sharing is outside a user’s reasonable expectation for the feature (for example, background collection while the app is not being used), show a prominent in-app disclosure. It must appear in normal app use without requiring the user to find a menu or settings screen. It must identify the data and its use or recipients. A privacy policy, website, or terms page alone is insufficient; unrelated disclosures must not obscure it.

Immediately before consent or a runtime permission request, show a clear consent step. The user must take an affirmative action. Leaving the screen, tapping away, or pressing Back or Home is not consent. A message that auto-dismisses or expires cannot collect consent. Do not begin collection or access until the user has granted permission. Another legal basis for processing does not remove the in-app disclosure obligation under this policy.

Describe which data is collected, transmitted, synced, or stored, for which feature, and in what context. State whether processing occurs in the background, who receives data, and any secondary use. Common violations include requesting a system permission before explaining its purpose; treating app inventory, screen recordings, contacts, or phone data as non-sensitive; and ignoring collection by an SDK.

If Google Play asks for evidence about an SDK designed to collect sensitive data by default, provide it within two weeks unless a longer deadline is specified.

### Best-practices child: make disclosure an understandable user choice

On October 24, 2026, I reopened the official [best-practices article for prominent disclosure and consent](https://support.google.com/googleplay/android-developer/answer/11150561?hl=en). The article labels the following as recommendations; the binding requirements remain the User Data clauses above.

| Stage | Guidance and implementation notes |
| --- | --- |
| Timing and flow | Show the disclosure in the app immediately before the permission/capability request, ideally in the flow that leads to Android Settings. An app description or website does not replace in-app disclosure. The prompt can be a dialog or part of a normal or conversational feature flow. |
| User choice | Offer a clear, friendly way to agree and a way to decline or decide later; preserve a cancel path. Keep unaffected app functionality usable after denial/revocation and gracefully disable the dependent feature. Repeated prompts can cause fatigue; respect the user's choice after repeated refusals. |
| Visual design and language | Do not imitate Android system permission UI. The guide suggests using the app's own visual style so users know the explanation comes from the app. Use clear language understandable to a reader around age 13; clarity matters more than brevity. |
| Why / What / How | Why: explain why the core function needs the capability; this should be the disclosure's main point. What: list all data types involved. How: explain how the data supports the core feature. If an SDK collects/transmits data, identify the data, why it is needed, and the third-party recipient rather than saying only that an SDK processes it. |
| Declaration video | The declaration flow lets developers provide a video link; YouTube is preferred, and a Google Drive link to a common video format is also supported. If supplied, show the app opening, the complete path to the disclosure (slowly scroll if needed to expose all text), consent, refusal plus the flow to show the prompt again, and a core feature using the capability. Add narration/captions if the use is not obvious. This is review evidence guidance; “you can provide” is not rewritten as a universal submission requirement. |

The best-practices article still says the Data safety form was due by July 20, 2022; that is a past rollout date. Use the [current Data safety Help article](https://support.google.com/googleplay/android-developer/answer/10787469?hl=en) for current form scope and exceptions; do not treat the old date as a new deadline.

## Specific data restrictions

| Scenario | Requirement |
| --- | --- |
| Financial, payment, or government-issued ID data | Do not publicly disclose the relevant personal or sensitive data. |
| Non-public phonebook or contact details | Do not publish or disclose another person’s non-public contact information without authorization. |
| Antivirus or security apps | Explain collected/transmitted data, purposes, and recipient categories in the privacy policy and in-app disclosures. |
| Apps for children | Use SDKs approved for child-directed services and comply with Families requirements. |
| Persistent device identifiers | Use only the specified telephony or enterprise-management exceptions and prominently disclose them; do not associate identifiers arbitrarily. |

## Data safety section

Maintain a clear and accurate Data safety declaration for every app in Play Console, covering data collected, used, or shared by the app and its SDKs/third-party code. It appears on the store listing, should agree with the privacy policy, and must be updated when data practices change. See the [Data safety form guide](../data-safety/data-safety.en-US.md) for classification and form logic.

Assess “collection” and “sharing” separately in the form. Data safety treats off-device transmission as collection, including data an integrated SDK/library sends directly to a third-party server. The service-provider exclusion applies only to the “sharing” classification when the recipient processes data on the developer’s behalf and under the developer’s instructions. It does not make an SDK transmission “not collected,” or remove the developer’s User Data disclosure, applicable consent, security, and accurate-reporting responsibilities. An SDK that builds advertising profiles across customers does not qualify for this service-provider exception and must be disclosed as sharing. Base the decision on actual data flows, purposes, recipients, and processing instructions—not the vendor label or server ownership alone. See the [Data safety form topic](../data-safety/data-safety.en-US.md).

## Privacy policy

Every app must provide a privacy policy link in the designated Play Console field and a link or text in the app, even if it does not access personal or sensitive data. Together with in-app disclosures, the policy should describe:

- Developer identity and a privacy contact mechanism.
- Personal and sensitive data accessed, collected, used, and shared, including recipients.
- Security practices.
- Data retention and deletion.
- A clear privacy-policy title and identification of the app/developer.

The link must be active, public, globally accessible, and not a PDF; the page must be non-editable. The company/developer named in the store listing or the app name must be identifiable in the policy.

## Account deletion

An app that lets users create an account must provide a readily discoverable in-app deletion option and an external web resource. Enter the external link in the designated Play Console field. After a request, delete data associated with that account. Freezing, disabling, or temporarily deactivating the account is not deletion. If specific data must be retained for security, fraud prevention, or legal compliance, disclose the retention clearly. The standalone summary is [Account deletion](../account-deletion/account-deletion.en-US.md).

## App Set ID

App Set ID may support essential non-advertising uses such as analytics or fraud prevention. Do not use it for ad personalization or measurement, or associate it with Android identifiers, identity information, or sensitive data for advertising. Disclose its use in a legally adequate privacy notice, including the privacy policy, and obtain legally valid consent where required.

## EEA, UK, and Swiss personal information

For personal information made available by Google that can directly or indirectly identify someone and originated in the EEA, UK, or Switzerland, developers must comply with applicable privacy/data-protection laws, process it only for purposes consistent with the individual’s consent, implement appropriate organizational and technical safeguards, and provide protections required by the applicable transfer mechanism. Monitor compliance regularly. If unable or at significant risk of being unable to meet the requirements, the policy says to immediately email `data-protection-office@google.com` to notify Google and immediately stop processing or take reasonable, appropriate steps to restore adequate protection.

## Operational checklist

- Inventory data flows across the app, backend, SDKs, and AI services; compare them against the store listing, Data safety section, and privacy policy.
- For unexpected or background processing, show a specific in-app disclosure, obtain affirmative consent, and only then request permissions or start processing.
- Review behavior after refusal, revocation, and deletion; do not label optional data as required or substitute account freezing for deletion.
- Review identifier associations, child-directed SDKs, advertising use of sensitive data, and local-law obligations.
- Recheck disclosures, the Data safety section, and the privacy policy whenever features, SDKs, recipients, or purposes change.

## Direct body links and descendants

The table groups policy-relevant links in the current User Data article body. Repeated anchors remain separate source occurrences; generic Help sidebars and footer controls are tracked separately. Check the per-URL source ledger for exact access states and failure details.

| Direct body link / destination | Relationship to User Data and descendant status |
| --- | --- |
| [CNIL mobile-app recommendations (original English link in User Data)](https://www.cnil.fr/en/mobile-applications-cnil-publishes-its-recommendations-better-privacy-protection) | On October 24, 2026, checked all 13 body links and seven “Read more”/tag/related targets; child summaries, failures, and relationships are in the external references topic. The news page links to the 2025 English courtesy translation; the [French revision notice](https://www.cnil.fr/fr/recommandations-applications-mobiles-modifiee) lists the current French PDF and annotated revision. The French-version route still reaches the 2024 original. The external topic adds developer/SDK permission and network-audit prompts and distinguishes CNIL guidance, Google Play rules, and related site content. |
| [Android location overview (legacy body URL)](https://developer.android.com/training/location) | Redirects to the current location documentation. Location-permission, background-location, and foreground-location topics are cross-linked. See the recursive link graph §4.107 for itemized summaries and audit scope for continuous-update APIs, lifecycle, sample code, and storage descendants; large API references and deeper descendants remain partial. |
| [Health data (legacy Help article)](https://support.google.com/googleplay/android-developer/answer/12261419) | Redirects to current [Health Content and Services](https://support.google.com/googleplay/android-developer/answer/16679511), whose current body and major related children have bilingual summaries. |
| [Health Connect / legacy Sensitive Permissions entry](https://support.google.com/googleplay/android-developer/answer/9888170) | Redirects to the current [Sensitive Permissions policy](https://support.google.com/googleplay/android-developer/answer/16558241). Health Connect data remains subject to User Data and the applicable Sensitive Permissions/Health topics. |
| [Ads policy](https://support.google.com/googleplay/android-developer/answer/9857753) and [Families policy](https://support.google.com/googleplay/android-developer/answer/9893335) | These cover advertising uses of sensitive data and data/SDK rules for child-directed apps. Bilingual topics exist; deeper SDK-vendor, legal, and course descendants remain partly covered. |
| [Service-provider / third-party definitions and Data safety form guidance](https://support.google.com/googleplay/android-developer/answer/10787469) | The same target defines service-provider and third-party concepts and explains collection, sharing, and form completion. The Data safety body, FAQ, and change log are summarized separately. The crosswalk above clarifies that off-device SDK transmissions may still count as collection while a qualifying service-provider transfer is excluded only from “sharing”; cross-customer ad profiling does not qualify. A wording difference between the general ephemeral-processing rule and one FAQ example remains preserved; deeper API/course/Console pages are partly unreadable or sign-in gated. |
| [Android permissions overview](https://developer.android.com/guide/topics/permissions/overview) | Covers alternatives, declaration, runtime requests, and checking access before each use. The permissions sample README, single/multiple/Compose code, and Activity/Fragment/Accompanist descendants have been individually analyzed. Samples are implementation references, not Play approval for a use case; the remaining dynamic tree and large API members are partial. See the Android Privacy Checklist and recursive link graph §4.101. |
| [Prominent disclosure and consent best practices](https://support.google.com/googleplay/android-developer/answer/11150561?hl=en) | Reopened October 24, 2026. Its body has eight anchor occurrences resolving to six distinct URLs. The article supplies recommended practices for timing, choice/decline paths, graceful degradation, Why/What/How copy, third-party SDK disclosure, and declaration-video evidence; it is not a separate binding policy. It still carries a historical July 20, 2022 Data safety date; current form scope is in [Data safety Help](https://support.google.com/googleplay/android-developer/answer/10787469?hl=en). The “Privacy policy” anchor actually opens [Prepare your app for review](https://support.google.com/googleplay/android-developer/answer/9859455), an App content workflow article, not privacy-policy text. The legacy Sensitive Permissions target redirects to the current [Sensitive Permissions article](https://support.google.com/googleplay/android-developer/answer/16558241?hl=en); the App content Console route remains sign-in gated. The linked [Play Academy course](https://playacademy.exceedlms.com/student/activity/66910-declared-permissions-and-in-app-disclosures) is summarized from its public description, but its lesson requires sign-in. The path continues through the Play Academy Policy Hub, course paths, and public course targets; see the Play Academy policy-courses topic and recursive link graph §4.63. |
| [Alternative unique identifiers guide (legacy body URL)](https://developer.android.com/training/articles/user-data-ids) → [current best practices for unique identifiers](https://developer.android.com/identity/user-data-ids) | Android implementation guidance: choose the narrowest, resettable ID for each use case and distinguish AAID, FID/GUID/App Set ID, carrier/SIM, sign-in, crash/performance, abuse-detection, and DRM needs. The bilingual AAID topic includes the full use-case matrix and all 31 body-link anchors. The new [Play Integrity API](../play-integrity-api/play-integrity-api.en-US.md) topic adds the no-fingerprinting/tracking terms, API data-handling statement, and server-side verification practices. The Android guide updated October 16, 2026 is not an additional binding Play clause. General APIs and deeper technical descendants remain partial. |
| [App account deletion requirements](https://support.google.com/googleplay/android-developer/answer/13327111) | Explains in-app and web deletion paths, associated data, and retention exceptions. Major FAQs and the Android UX best-practices blog were reviewed; rollout dates are historical, and sidebar descendants remain partial. |
| [Data Privacy Framework Principles](https://www.dataprivacyframework.gov/program-articles/Participation-Requirements-Data-Privacy-Framework-%28DPF%29-Principles) and [Google Controller-Controller Terms](https://business.safety.google/controllerterms/) | Direct retrieval of the DPF body remains JavaScript-limited, but the official index exposes seven principles, 16 supplemental principles, and an arbitral annex. It is a transfer mechanism for covered data from participating organizations, not GDPR-wide compliance. Google Controller Terms are currently Version 11 (May 7, 2026) and apply only to Controller Services incorporated into/accepted under the relevant agreement. Google Play and Managed Google Play have different service classifications. See the bilingual external references topic for scope, regional appendices, historical versions, and access status. |
| [User Data feedback survey](https://google.qualtrics.com/jfe/form/SV_9YPSYrwjw03d7cG?Source=10144311) | Requires JavaScript and did not expose survey questions. It is page feedback, not a policy obligation or declaration step. |

### Policy sidebar and parent category index

The User Data Help page also has a seven-item policy navigation rail. Its parent [Privacy, Deception and Device Abuse category index](https://support.google.com/googleplay/android-developer/topic/9877467?hl=en) lists the same destinations. These navigation links are separate from the body links above; each target article has been opened and cross-linked to its local topic.

| Navigation target | Relationship to User Data and local topic | Target/descendant review |
| --- | --- | --- |
| [User Data (current page)](https://support.google.com/googleplay/android-developer/answer/10144311?hl=en) | This topic; current policy entry in the parent index. | Full body reviewed and summarized bilingually; body links are listed above. |
| [Permissions and APIs that Access Sensitive Information](https://support.google.com/googleplay/android-developer/answer/16558241?hl=en) | Governs sensitive-permission access to user data; see [Sensitive Permissions](../sensitive-permissions/sensitive-permissions.en-US.md). | English body opened in full; the Contacts/Location preview and high-impact descendants are cross-linked. Other direct links and Android technical descendants remain partial. |
| [Device and Network Abuse](https://support.google.com/googleplay/android-developer/answer/16559646?hl=en) | Adds device, network, and data-abuse boundaries; see Device and Network Abuse. | Full body reviewed and 17 direct policy/technical targets inventoried; deeper Android implementation descendants remain partial. |
| [Deceptive Behavior](https://support.google.com/googleplay/android-developer/answer/17006354?hl=en) | Covers deceptive interfaces, functionality, and data-use claims; see Deceptive Behavior. | Full body opened; 11 anchor occurrences/10 distinct targets inventoried. Descendants remain partial. |
| [Misrepresentation](https://support.google.com/googleplay/android-developer/answer/9888689?hl=en) | Covers false claims about identity, functionality, origin, and relationships; see Misrepresentation. | Full body opened; no independent policy-body links were found, and its navigation rail is tracked separately. |
| [Google Play's Target API Level Policy](https://support.google.com/googleplay/android-developer/answer/16561298?hl=en) | Platform API thresholds affect implementation under sensitive-permission rules; see [Target API requirements](../target-api/target-api-level.en-US.md). | English body and navigation reviewed. The Simplified Chinese endpoint was unreadable; API/form-factor descendants remain partial. |
| [Preview: Permissions and APIs that Access Sensitive Information](https://support.google.com/googleplay/android-developer/answer/16909972?hl=en) | April 2026 policy preview; it marks Contacts and Location changes effective January 27, 2027, and should not be merged with current clauses; see Contacts and Location. | Preview body opened and summarized; Contact Picker, Location Button, and declaration/review relationships reviewed. Android API/sample descendants remain partial. |

The parent index's other direct links were also checked: its [Google Play Policy video](https://www.youtube.com/watch?v=zMHv1yH7C4E) could not be fetched and no usable transcript was available; [Help Community](https://support.google.com/googleplay/android-developer/community?hl=en) opened as a dynamic community landing page whose posts change and are not authoritative policy; [Contact us](https://support.google.com/googleplay/android-developer/gethelp) redirects to account-only Play Console support and requires sign-in. These navigation/support routes are kept separate from policy text. Technical, course, dynamic legal-directory, and account-specific Console descendants continue to be checked within access limits; this does not claim infinite recursive closure.

## Cross-check against the consolidated Developer Program Policy

On October 24, 2026, I compared the “User Data” and “SDK Requirements” portions of the current [consolidated Developer Program Policy](../developer-program-policy/developer-program-policy.en-US.md). The consolidated page says it is effective September 30, 2026. Its English body and Simplified Chinese `hl=zh-Hans` body were opened. The `hl=zh-CN` route could not be read in this pass, so the readable `zh-Hans` version was used for the Chinese comparison.

The core duties match across the two official pages: disclose access, collection, use, handling, and sharing, and limit use to disclosed policy-compliant purposes; remain responsible for SDK/third-party code and its data practices; meet the reasonable-expectation, purpose, security, permission, applicable disclosure/affirmative-consent, Data safety, and privacy-policy requirements for personal and sensitive data; and do not sell such data. A user-initiated transfer is outside the policy's definition of a sale. The consolidated page's User Data section also expressly includes third-party AI integrations.

The consolidated policy has a separate “SDK Requirements” section with additional examples: an SDK claimed to be used only for anti-fraud but sharing data for ads/analytics, or an SDK transmitting installed-package information without prominent disclosure. If an SDK is designed to collect personal and sensitive user data by default, sufficient evidence is generally due within two weeks after a Google Play request unless that request provides a longer period. These examples help assess SDK integration risk; they do not replace the other User Data duties.

The standalone [User Data Help article](https://support.google.com/googleplay/android-developer/answer/10144311?hl=en) keeps its own full explanation, focused sections, and body-link network. The consolidated policy presents the wider policy set and cross-references User Data and prominent-disclosure guidance from its SDK section. Keep their source records and descendant audits separate; overlapping text does not make them the same page or establish that one replaces the other. This comparison covers only those two relevant sections of the consolidated page; **it does not mean every link or descendant in the full consolidated policy has been exhausted**.

Access note: the English and Simplified Chinese User Data bodies had been fully read earlier on October 24, 2026. A retry in this pass returned HTTP 429 for English and HTTP 500 for the Chinese route, so no content change was inferred from the failed retry. The URL audit retains the prior full-body status and records this fetch failure.

## Related pages

- [Data safety form](../data-safety/data-safety.en-US.md)
- Third-party SDK requirements and safe integration
- [Sensitive permissions and APIs](../sensitive-permissions/sensitive-permissions.en-US.md)
- Health apps, health data, and Health Connect
- [Account deletion](../account-deletion/account-deletion.en-US.md) · [Account deletion requirements](https://support.google.com/googleplay/android-developer/answer/13327111?hl=en)
- External law and reference materials for User Data: prominent-disclosure practices, CNIL mobile-app recommendations, and the relationship/access limits of DPF and Google Controller Terms
- [Consolidated Developer Program Policy](../developer-program-policy/developer-program-policy.en-US.md)
- Official: [User Data (English)](https://support.google.com/googleplay/android-developer/answer/10144311?hl=en) · [用户数据（简体中文）](https://support.google.com/googleplay/android-developer/answer/10144311?hl=zh-Hans)

## Coverage note

The main policy sections and high-relevance direct references are summarized; see the external references topic. General Android APIs, all non-policy details in the 98-page CNIL guide, the DPF JavaScript pages and participant verification, failed historical Controller Terms PDF targets, legal descendants, and deeper site links remain partly uncovered and are tracked in the URL ledger. Unread pages are not inferred from their titles.
