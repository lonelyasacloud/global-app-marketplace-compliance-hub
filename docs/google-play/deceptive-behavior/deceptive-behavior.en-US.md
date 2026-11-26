---
id: google-play.deceptive-behavior
platform: google-play
language: en-US
authority: normative
status: current
kb_checked_at: 2026-10-22
review_due: 2027-01-22
regions: [global]
topics: [deceptive-behavior, truthful-metadata, manipulated-media, review-evasion, device-settings]
snapshot_id: play.deceptive-behavior
snapshot_package: "GooglePlay-KnowledgeBase-2026-10-24-review.zip"
coverage_status: "detailed-summary"
source_url: "https://support.google.com/googleplay/android-developer/answer/17006354?hl=en"
effective_date: "current-policy"
---

# Google Play Deceptive Behavior Policy

> **Import note (Google batch 3).** The body is the paraphrased summary from the already separated 2026-10-24 Google Play knowledge-base snapshot (`play.deceptive-behavior`, reviewed 2026-10-22). It is not a verbatim copy of an official page. The English official source is the source of truth. `kb_checked_at` is the review date recorded in the snapshot source file; this import did not re-open the live official pages. Phrases such as “this knowledge base,” “this library,” and “local topic” describe coverage inside that snapshot, not the set of pages imported into this repository. Relative snapshot links to topics, link graphs, ledgers, or CSVs that are not in this repository are kept as text mentions. Relative links that target the Google batch 1 and 2 topics or these nine batch 3 topics point at the hub files. The snapshot records the current English Help article, reviewed 2026-10-22. It does not record a checked Chinese official Deceptive Behavior page. The Chinese hub text is the snapshot’s editorial paraphrase of that English article, not Google’s published Chinese page text. The April 10, 2025 announcement cited in the source says its manipulated-media clarifications are not new or updated policy. The linked April 2026 permissions preview schedules Contacts and Location changes for 2027-01-27; that preview is not current Deceptive Behavior text, and the dates stay separate. This policy is `normative`. Misrepresentation, User Data, sensitive permissions, device abuse, and target API remain separate topics.

## Scope

The current English Help article is [Deceptive Behavior](https://support.google.com/googleplay/android-developer/answer/17006354?hl=en). The older [answer/16680223 URL](https://support.google.com/googleplay/android-developer/answer/16680223?hl=en) redirects to the current article. The page has five sections: misleading claims, deceptive device-setting changes, enabling dishonest behavior, manipulated media, and behavior transparency. The app, third-party SDKs, ads, and services must all comply.

**Distinction from Misrepresentation:** Deceptive Behavior covers the actual product experience, device settings, dishonest tools, manipulated media, hidden features, and review evasion. Misrepresentation (snapshot: `misrepresentation-en.md`, not imported in this repository) is a separate sibling policy with its own store-listing and developer/government-identity rules; check both.

## Five policy areas and practical checks

| Policy area | Main requirements |
| --- | --- |
| Misleading claims | Titles, icons, descriptions, screenshots, video, category, and rating must accurately reflect actual functionality. Do not claim impossible features, miscategorize the app, claim “official” status without rights, falsely claim government affiliation, or publish demonstrably false content that could interfere with elections. |
| Deceptive device-setting changes | Get the user's explicit knowledge and consent before changing device or browser settings, bookmarks, shortcuts, widgets, or home-screen presentation outside the app; make changes easy to reverse. Do not modify settings for advertising or third parties, or mislead/incentivize users to remove or disable other apps. The verifiable-security-service exception is limited by policy conditions. |
| Enabling dishonest behavior | Do not generate fake IDs, passports, diplomas, Social Security numbers, credit cards, bank accounts, or driver's licenses; mimic apps/sites to steal credentials; expose private information without consent; conceal material geographic/device differences; or make major version changes without notifying users. Prompt users and disclose download size before downloading additional assets. |
| Manipulated media | Do not create, distribute, or enable demonstrably misleading images, audio, video, or text that could cause harm in sensitive-event, political, social, or public-concern contexts. Public interest, clearly artificial media, clear user-facing disclaimers/watermarks, satire, or parody may qualify for exceptions, but the content must still comply with [Restricted Content policies](../inappropriate-content/inappropriate-content.en-US.md). |
| Behavior transparency | Do not hide dormant, undocumented, or review-only features; detect the review environment; remotely download and execute new functionality absent during review; or obfuscate code to evade review. App behavior must match its listing, and the developer must be able to explain app functionality and code, including SDKs, when requested. |

## Direct links and target analysis

On October 22, 2026, the current body was checked across **11 anchor occurrences and 10 unique destinations**. The “Restricted Content” index appears twice in the body. Linked images are recorded as targets. The Help Center's related-policy category is inventoried separately below and is not counted in the body total.

| Direct body target | Relationship and review status |
| --- | --- |
| [Two-minute policy feedback survey](https://google.qualtrics.com/jfe/form/SV_9YPSYrwjw03d7cG/?Source=9888077) | Returned a cache miss; survey questions could not be read. It is feedback, not a policy obligation. |
| Three policy display icons: [Policy Summary](https://lh3.googleusercontent.com/BPsAL28eke0gFbFJduiZupJyY6uR5X7_JHR_3vev1cApatT5KLrReyskdlNZXRGFsg%3Dw60-h60), [Full Policy](https://lh3.googleusercontent.com/hnJIMKQ0lyssVbehdx4OCpjLHPBYy94NeG4dD-xZ40osbCjM8Lt3zS4P5JvA5Xsqig%3Dw30-h34), and [Key Considerations](https://lh3.googleusercontent.com/IfJhh8qlFSuw1U7A2DSeKi0B3jBYMC5fU0pGMUG40oyCU3urkOu4yGg0D24TkbUvwRk%3Dw40) | Visual assets only; they add no independent policy requirement. |
| Example image: [impossible breathalyzer functionality](https://x20web.corp.google.com/teams/play-kmt/no_crawl/arhc/images/quebec_deceptive_example1.png) | Google-internal SSO-protected image; public access was blocked. The textual example remains readable. |
| Example image: [misleading news-video edit without a watermark](https://lh3.googleusercontent.com/mRVacICnbXaC5GPY0SNdp9hKiBxYK0tHUsrSCZ70WK2i2F5kd5g65CD_1-cFFO00w2k%3Dw311) | Image asset opened; illustrates the risk of imitating a real news broadcast without a clear disclaimer or watermark. |
| [What's new section / Prepare and roll out a release](https://support.google.com/googleplay/android-developer/answer/7159011?hl=en) | The legacy destination redirects to the current release-notes Help page. The policy cites major unannounced functionality changes and stale store listings as misleading; the release guide explains release notes. See the [release workflow topic](../publishing/play-release-workflow.en-US.md). |
| [Restricted Content category index](https://support.google.com/googleplay/android-developer/topic/9877466) | Two body anchors resolve to the same index. It lists ten restricted-content policies; each target was opened and is indexed below. |
| [Google Play Developer Help Community](https://support.google.com/googleplay/android-developer/community?help_center_link=CJL-jQgSEkRlY2VwdGl2ZSBCZWhhdmlvcg&hl=en) | Public community page opened; it shows current featured posts, discussions, and training videos. Community replies can be case-specific or stale and do not replace formal policy. |
| [Contact us](https://support.google.com/googleplay/android-developer/gethelp) | Redirects to signed-in Play Console Help; account-specific support content cannot be inspected publicly. |

### Legacy URL and the April 10, 2025 announcement

The former [Manipulated Media article](https://support.google.com/googleplay/android-developer/answer/9888077?hl=en) now redirects to the current Deceptive Behavior policy; the old [answer/14584985 target](https://support.google.com/googleplay/android-developer/answer/14584985) linked from the April 3, 2024 announcement was also verified to resolve here. That 2024 announcement says audio was added as another example of covered media; current section 4.1 expressly names imagery, audio, video, and text. Google's [April 10, 2025 policy announcement](https://support.google.com/googleplay/android-developer/answer/15899442?hl=en) describes its changes as clarifying allowed exceptions and violation examples; it explicitly says these are not new or updated policy and enforcement standards/practices remain the same. The history and current terms remain traceable in the Manipulated media branch below and the announcement child-link inventory (snapshot: `../google-play-announcement-resources-en.md`, not imported in this repository).

## Ten descendant policies in the Restricted Content directory

The directory and its listed policy targets were opened. Each is a separate policy with its own scope; the category index is not one unified rule.

| Directory child policy | Topic |
| --- | --- |
| [Child Endangerment](https://support.google.com/googleplay/android-developer/answer/9878809) | [Age restrictions and child safety](../age-restricted-child-safety/age-restricted-child-safety.en-US.md) |
| [Inappropriate Content](https://support.google.com/googleplay/android-developer/answer/9878810) | [Inappropriate Content](../inappropriate-content/inappropriate-content.en-US.md) |
| [Financial Services](https://support.google.com/googleplay/android-developer/answer/9876821) | [Financial services and loans](../financial-services-and-loans/financial-services-and-loans.en-US.md) |
| [Real-Money Gambling, Games, and Contests](https://support.google.com/googleplay/android-developer/answer/9877032) | [Real-Money Gambling](../real-money-gambling/real-money-gambling.en-US.md) · [Prediction-market pilot](../prediction-market-pilot/prediction-market-pilot.en-US.md) |
| [Illegal Activities](https://support.google.com/googleplay/android-developer/answer/9878877) | Illegal Activities (snapshot: `illegal-activities-en.md`, not imported in this repository) |
| [User Generated Content](https://support.google.com/googleplay/android-developer/answer/9876937) | [User-generated content](../user-generated-content/user-generated-content.en-US.md) |
| [Health Content and Services](https://support.google.com/googleplay/android-developer/answer/16679511) | Health apps and Health Connect (snapshot: `health-apps-and-health-connect-en.md`, not imported in this repository) |
| [Blockchain-based Content](https://support.google.com/googleplay/android-developer/answer/13607354) | [Crypto assets and NFTs](../crypto-assets-and-nfts/crypto-assets-and-nfts.en-US.md) |
| [AI-Generated Content](https://support.google.com/googleplay/android-developer/answer/13985936) | [Age restrictions and child safety](../age-restricted-child-safety/age-restricted-child-safety.en-US.md) (includes AI-generated content requirements) |
| [Age-Restricted Content and Functionality](https://support.google.com/googleplay/android-developer/answer/16302250) | [Age restrictions and child safety](../age-restricted-child-safety/age-restricted-child-safety.en-US.md) |

## Privacy, Deception and Device Abuse descendants

The Help article's related-policy index was opened on October 22, 2026. It is navigation among sibling rules, not additional Deceptive Behavior text. User Data, sensitive permissions, device/network abuse, Misrepresentation, and Target API each have separate topics. The index video fetch failed; its Contact us link requires Play Console sign-in.

| Related policy link | Relationship |
| --- | --- |
| [User Data](https://support.google.com/googleplay/android-developer/answer/10144311) | Data disclosure, consent, security, deletion, and SDK responsibility; see [User Data](../user-data/user-data.en-US.md). |
| [Permissions and APIs that Access Sensitive Information](https://support.google.com/googleplay/android-developer/answer/16558241) | Permissions must match advertised core functionality, use minimum scope, and respect denial; see [Sensitive Permissions](../sensitive-permissions/sensitive-permissions.en-US.md). |
| [Device and Network Abuse](https://support.google.com/googleplay/android-developer/answer/16559646) | Prohibits unauthorized device/network interference, sandbox bypass, and off-Play executable downloads; see Mobile Unwanted Software/device abuse (snapshot: `mobile-unwanted-software-en.md`, not imported in this repository). |
| [Deceptive Behavior](https://support.google.com/googleplay/android-developer/answer/17006354) | This topic. |
| [Misrepresentation](https://support.google.com/googleplay/android-developer/answer/9888689) | Separate, related policy; see Misrepresentation (snapshot: `misrepresentation-en.md`, not imported in this repository). |
| [Google Play Target API Level Policy](https://support.google.com/googleplay/android-developer/answer/16561298) | Specialized target API policy; see [Target API requirements](../target-api/target-api-level.en-US.md). |
| [Preview: Permissions and APIs that Access Sensitive Information](https://support.google.com/googleplay/android-developer/answer/16909972?hl=en) | April 2026 policy preview; Contacts and Location changes are scheduled for January 27, 2027. A preview is not current effective text. |

## Review workflow

1. Compare the running APK/AAB, server configuration, ads, and third-party SDK behavior with the title, description, screenshots, video, category, and rating. Look for impossible or undisclosed location/device-dependent functionality.
2. Check for fake login pages, OS-warning impersonation, unauthorized government/brand claims, remote feature toggles, and review-only behavior. Reviewers should see the same functionality as users.
3. Audit device-setting changes, background downloads, remote scripts/code, and automated modification: are they core to the app, explicitly consented, reversible, and preceded by a download-size disclosure where needed?
4. For generated/edited/shared images, audio, video, and text, review sensitive-event context, visible watermarks/disclaimers, satire context, and Restricted Content rules.
5. Review alongside Misrepresentation (snapshot: `misrepresentation-en.md`, not imported in this repository), Mobile Unwanted Software/device abuse (snapshot: `mobile-unwanted-software-en.md`, not imported in this repository), [User Data](../user-data/user-data.en-US.md), and Store Listing Best Practices (snapshot: `store-listing-best-practices-en.md`, not imported in this repository).

## Coverage limits

The current policy article and its direct policy directories were opened. The survey returned a cache miss, one Google-internal illustration is SSO-protected, and the community/Console routes are supporting destinations rather than evidence of app approval. The ten Restricted Content topics and the Privacy/Deception sibling topics have local entries, while their deeper APIs, local laws, dynamic forms, and sidebar branches remain on the source-ledger work queue.
