---
id: google-play.spyware-and-data-exfiltration
platform: google-play
language: en-US
authority: normative
status: current
kb_checked_at: 2026-10-22
review_due: 2027-01-22
regions: [global]
topics: [spyware, data-exfiltration, sdk, monitoring, privacy]
snapshot_id: play.spyware-and-data-exfiltration
snapshot_package: "GooglePlay-KnowledgeBase-2026-10-24-review.zip"
coverage_status: "detailed-summary"
source_url: "https://support.google.com/googleplay/android-developer/answer/14745000?hl=en"
effective_date: "current-policy"
---

# Spyware, Data Exfiltration, and Monitoring Apps

> **Import note (Google batch 4).** The body is the paraphrased summary from the already separated 2026-10-24 Google Play knowledge-base snapshot (`play.spyware-and-data-exfiltration`, reviewed 2026-10-22). It is not a verbatim copy of an official page. The English official source is the source of truth. `kb_checked_at` is the review date recorded in the snapshot source file; this import did not re-open the live official pages. Phrases such as “this knowledge base,” “this library,” and “local topic” describe coverage inside that snapshot, not the set of pages imported into this repository. Relative snapshot links to topics, link graphs, ledgers, or CSVs that are not in this repository are kept as text mentions. Relative links that target the Google batch 1–3 topics or these twelve batch 4 topics point at the hub files. The Chinese source file’s Spyware explainer URL is `hl=zh-CN`. The link-audit table records the English explainer as opened in full. The snapshot does not record a failed `hl=zh-CN` fetch of that primary article, and it does not record a line-by-line check of a Chinese official page against English. The Chinese hub text is the snapshot’s editorial paraphrase, not Google’s published Chinese page text. No future-effective date is recorded. The Play Academy MUwS course page is dated 2020-07-08, and its video has no readable transcript. Training material does not replace current policy. The data limits on the Spyware explainer are `normative`, and this page is not the full Malware taxonomy. The prominent-disclosure article is operational guidance; a privacy policy alone does not replace an in-app disclosure. The narrow monitoring-app exception is not permission to track a spouse or another adult.

**Reviewed October 22, 2026.** Google Play's Spyware explainer defines the central risk as apps, code, or behavior collecting, stealing, exfiltrating, or sharing user/device data unrelated to policy-compliant functionality, or spying without adequate user notice and consent. User consent does not automatically legitimize harmful or unrelated data processing. This topic covers the Spyware branch, not the complete Malware taxonomy.

## Explicit high-risk examples

- An SDK transmits audio or call recordings unrelated to the app's policy-compliant functionality.
- An app steals information from other apps' notifications.
- The app unexpectedly transfers data in the background while the user is not engaging with it: contacts, photos/files not owned by the app, email contents, call logs, SMS logs, or data from other apps' `/data/` directories.
- A personal-loan or budgeting app exfiltrates or shares non-financial or personal SMS history.
- Third-party code transmits device data in a way the user did not expect or was not adequately told about/asked to consent to.

This list is non-exhaustive. Access, collection, use, and sharing should be limited to functionality users expect or consent to and that complies with policy. All integrated SDKs and libraries are in scope; attributing behavior to an SDK does not remove developer responsibility. Reconcile permission declarations, privacy policy, Data safety, in-app disclosures, server recipients, and observed SDK network behavior.

## Narrow exception for monitoring apps

Play's Malware/Stalkerware rules permit only apps designed and marketed exclusively for parents monitoring their children or enterprises monitoring employees, subject to strict controls. Do not track a spouse or another adult, even with their knowledge or consent. These apps must use the Manifest `isMonitoringTool` metadata, show a persistent identifying notification and unique icon, disclose monitoring functionality on the store listing, avoid hiding or cloaking tracking, and not link to non-compliant APKs outside Play. Developers remain responsible for local law.

`isMonitoringTool` values include `child_monitoring`, `enterprise_management`, and `other`; Google Play reviews whether `other` qualifies for a valid exception. Every active version across all tracks should carry the correct flag. Play Protect warns users when a monitoring app is present.

## Implementation review

1. Trace sensitive fields through the manifest, SDK/SBOM, initialization code, background jobs, network endpoints, and server logs.
2. For each data type, record the feature, user trigger, expectation, disclosure surface, recipients, retention/deletion rule, and Data safety answer.
3. Check whether SDKs transmit information when the app is not being used; remove or replace SDKs that cannot be disabled or fixed.
4. Pay particular attention to SMS/calls, contacts, microphone, notifications, app inventories, other apps' private data, and loan/budget app SMS handling.
5. For monitoring apps, verify the exclusive use and audience, flag, persistent notification, listing disclosure, all release tracks, and Play Protect warning.

## Direct children and their roles

| Target | Review and relationship |
| --- | --- |
| [Understanding Google Play's Spyware policy](https://support.google.com/googleplay/android-developer/answer/14745000?hl=en) | Full body opened. Lists data limits, SDK responsibility, audio/notification/background-data/loan-SMS examples, and supporting resources. |
| [Malware policy](https://support.google.com/googleplay/android-developer/answer/9888380?hl=en) | Relevant sections opened in full. Spyware is a Malware/PHA category; Malware also covers backdoors, billing fraud, stalkerware, DoS, hostile downloaders, phishing, privilege abuse, ransomware, rooting, spam, trojans, riskware, and others. Code can be flagged even without malicious intent if it poses a clear risk to some Android devices/versions. |
| [User Data policy](https://support.google.com/googleplay/android-developer/answer/10144311?hl=en) | Full body opened. Requires transparent handling, policy-compliant disclosed purposes, secure processing, SDK compliance, and compliance with local privacy law; it is the cross-app data baseline for Spyware. |
| [Mobile Unwanted Software (MUwS)](https://developers.google.com/android/play-protect/mobile-unwanted-software) | Full body opened. Adds transparent functionality, clear system-change disclosure, user consent, secure transmission, not inducing users to disable Play Protect, and categories including unconsented collection, social engineering, disruptive ads, system-function abuse, and ad fraud. MUwS is tracked separately from Malware but can overlap with Spyware/permission abuse. |
| [Sensitive Permissions policy](https://support.google.com/googleplay/android-developer/answer/16558241?hl=en) | Body opened and summarized in the [sensitive permissions topic](../sensitive-permissions/sensitive-permissions.en-US.md); use it to verify core-function need, minimum scope, declarations, and disclosure/consent. The older `answer/9888170` link redirects to the current policy. |
| [SDK Requirements](https://support.google.com/googleplay/android-developer/answer/13323374?hl=en) and [Using SDKs safely and securely](https://support.google.com/googleplay/android-developer/answer/13326895?hl=en) | Both targets opened. One is the SDK Requirements page and the other a safe-integration explainer; both reinforce developer responsibility for included code and SDK data practices. See the third-party SDK topic ([Google Play third-party SDK requirements and safe integration](../sdk-requirements/sdk-requirements.en-US.md)). |
| [Prominent disclosure and consent best practices](https://support.google.com/googleplay/android-developer/answer/11150561?hl=en) | Full body opened. Adds practical guidance for an in-app disclosure that explains data/use/sharing in the normal usage flow and requires affirmative consent; a privacy policy or terms page alone is insufficient. |
| [Use of the isMonitoringTool Flag](https://support.google.com/googleplay/android-developer/answer/12955211?hl=en) | Full body opened. Defines `child_monitoring`, `enterprise_management`, and `other`; Google Play reviews consistency with the category/listing and Play Protect warns users. |
| [Google Play Protect Malware categories](https://developers.google.com/android/play-protect/phacategories) | Full body opened. Describes Malware categories and Play Protect; it does not create a separate developer upload/declaration process. |
| Google Play Academy [Malware](https://playacademy.exceedlms.com/student/path/261439/activity/345726) and [MUwS](https://playacademy.exceedlms.com/student/path/261439/activity/345727) courses | Malware course text could not be extracted. The MUwS course page is dated July 8, 2020, but the video has no readable transcript. Training is supplemental and does not replace current policy. |
| [Google Play Data safety consumer article](https://support.google.com/googleplay/answer/11416267) | Page opened; explains how consumers read developer-provided Data safety information. This is user education, not the developer declaration rule itself; see the [Data safety topic](../data-safety/data-safety.en-US.md) for developer requirements. |

## Related topics

- [Sensitive permissions and APIs](../sensitive-permissions/sensitive-permissions.en-US.md) · [User Data](../user-data/user-data.en-US.md) · [Data safety](../data-safety/data-safety.en-US.md)
- [SMS and Call Log](../sms-call-log/sms-call-log.en-US.md) · Third-party SDK requirements ([Google Play third-party SDK requirements and safe integration](../sdk-requirements/sdk-requirements.en-US.md)) · [Ads and promotion](../ads-and-advertising/ads-and-advertising.en-US.md)

The selected Spyware explainer's body and direct policy/training destinations are covered. Help-sidebar recommendations, all SDK technical descendants, jurisdiction-specific monitoring laws, video transcripts, and private Play Console declarations remain incomplete. A link appearing in the inventory does not mean all of its descendants have been audited.
