---
id: google-play.developer-program-policy
platform: google-play
language: en-US
authority: normative
status: current
kb_checked_at: 2026-10-24
review_due: 2027-01-24
regions: [global]
topics: [developer-program-policy, consolidated-policy]
snapshot_id: play.developer-program-policy
snapshot_package: "GooglePlay-KnowledgeBase-2026-10-24-review.zip"
coverage_status: "detailed-summary"
source_url: "https://support.google.com/googleplay/android-developer/answer/18258653?hl=en"
source_url_zh: "https://support.google.com/googleplay/android-developer/answer/18258653?hl=zh-Hans"
effective_on: 2026-09-30
---

# Google Play Developer Program Policy (Consolidated)

> **Import note (Google batch 1).** The body is the paraphrased summary from the already separated 2026-10-24 Google Play knowledge-base snapshot. It is not a verbatim copy of a Google page. The English official page is the source of truth. `kb_checked_at` is the review date recorded in the snapshot source file; this import did not re-open the live official pages. Phrases such as “this knowledge base,” “this library,” and “local topic” describe coverage inside that snapshot, not the set of pages imported into this repository. Relative snapshot links to topics, link graphs, ledgers, or CSVs that are not in this repository are kept as text mentions. Relative links that target the six topics in this batch now point at the hub files. The consolidated Developer Program Policy is effective **September 30, 2026** unless the official page says otherwise. Do not treat older wording as current. The snapshot records that the English body and the readable `hl=zh-Hans` Simplified Chinese body were opened on 2026-10-24, and that the `hl=zh-CN` route returned a fetch error. Evidence level: `normative`.

## Source, effect, and scope

- Current consolidated policy: [Developer Program Policy (English)](https://support.google.com/googleplay/android-developer/answer/18258653?hl=en); [Readable Simplified Chinese body (`zh-Hans` route)](https://support.google.com/googleplay/android-developer/answer/18258653?hl=zh-Hans); the `zh-CN` route could not be read in this pass.
- The page states that it is effective **September 30, 2026**, unless otherwise noted.
- Reviewed 2026-10-24. The English and `zh-Hans` Simplified Chinese bodies were reopened; the Chinese `zh-CN` route returned a fetch error.
- The policy and the [Developer Distribution Agreement](https://play.google.com/about/developer-distribution-agreement.html) form the main rules framework. Developers must also follow local law, Play Console declaration requirements, and terms for applicable programs.
- This is a navigation and operational summary, not a full verbatim translation. If requirements conflict, use the applicable official policy, agreement, and current Console requirements.

## Policy domains covered

The consolidated page brings together rules previously spread across the policy center. The original **51 topic entries** and their individual entry-level summaries remain in the Developer Policy Center and the policy link graph.

| Domain | Main requirements and policies to check | Common related material |
| --- | --- | --- |
| Restricted content and safety | Child safety; inappropriate sexual, hateful, or violent content; age restrictions; financial services; real-money gambling; illegal activity; UGC; health; blockchain; and AI-generated content. Check local law, geographic availability, and audience fit. | Age restrictions and child safety, Inappropriate Content, Illegal Activities, [Financial Services and Loans](../financial-services-and-loans/financial-services-and-loans.en-US.md), [Real-Money Gambling](../real-money-gambling/real-money-gambling.en-US.md), User-Generated Content, Health Apps and Health Connect, [Crypto Assets and NFTs](../crypto-assets-and-nfts/crypto-assets-and-nfts.en-US.md) |
| Identity, rights, and accuracy | Do not impersonate or mislead. Store information, app functionality, ratings/reviews/installs, and developer-affiliation claims must be accurate. You must hold rights to distribute included intellectual property. | Impersonation, Misrepresentation, Intellectual Property, Store Listing Best Practices, Ratings, Reviews, and Installs |
| User data, privacy, and permissions | Developers remain responsible for data accessed, used, or shared by the app, SDKs, and third-party AI components. Apply data minimization, purpose limits, security, a privacy policy, Data safety, and, when required, prominent disclosure and consent and account/data deletion. Sensitive permissions/APIs also have eligibility, use-case, runtime permission, and Console declaration rules. | [User Data](../user-data/user-data.en-US.md), [Data safety form](../data-safety/data-safety.en-US.md), Sensitive Permissions and APIs, Permissions Declaration, SMS and Call Log Permissions, Photo and Video Permissions, Contacts and Foreground Location, Background Location, Account Deletion, Third-Party SDK Requirements, Health Data and Health Connect |
| Device, network, and malware | Malware, mobile unwanted software, ad fraud, social engineering, and device/network abuse are prohibited. APIs and system features must be used for permitted purposes; apps and SDKs may not hide, bypass, or perform harmful actions without consent. | Malware, Spyware and Data Exfiltration, Mobile Unwanted Software, Deceptive Behavior, Device and Network Abuse, Third-Party SDK Requirements |
| Monetization, payments, and ads | Digital goods/services generally use Google Play Billing under the Payments rules; verify applicable exceptions and regional programs. Subscriptions must clearly disclose price, period, renewal, and cancellation. Ads and landing pages are also subject to content, age, privacy, and UX rules. | [Payments, Billing, and Subscriptions](../payments/payments-and-subscriptions.en-US.md), Ads and Promotion, Child Safety and Age Restrictions, Third-Party SDK Requirements |
| Store presence, promotion, and distribution | Metadata, graphics, events, promotion, and app marketing must be accurate and must not manipulate rankings/reviews. Complete accurate ratings, News/Magazine declarations, and target API requirements. | Store Listing and Asset Best Practices, Ratings, Reviews, and Installs, Content Ratings and Target Audiences, [News and Magazines](../news-and-magazines/news-and-magazines.en-US.md), Target API Requirements |
| Spam, functionality, and UX | Apps need stable, responsive functionality and original user value. Restrictions cover repetitive/low-quality or nonfunctional apps, unauthorized WebViews/traffic-driving, message spam, and disruptive behavior toward Play or devices. | Spam, Functionality, and User Experience, App Quality and Form-Factor Guidelines, App Review Preparation, [Testing and Release Workflow](../publishing/play-release-workflow.en-US.md) |
| Form factors, audiences, and programs | Android Auto/Automotive, Android TV, Wear OS, Instant Apps, emoji, and Families have additional requirements. Real-money gambling, health, ad SDK, and regional pilot programs have separate eligibility and declaration conditions. | App Quality and Form-Factor Guidelines, Child Safety and Age Restrictions, Health Apps and Health Connect, [Real-Money Gambling](../real-money-gambling/real-money-gambling.en-US.md), [Prediction Market Pilot](../prediction-market-pilot/prediction-market-pilot.en-US.md), Policy Course Index |
| Enforcement and appeals | Google may reject, remove, suspend, or restrict apps/accounts. Check Policy status in Console, fix issues described in notices, and use the formal appeal path. Repeated/serious violations, account associations, and incomplete review materials create additional risks. | Enforcement and Appeals, Play Console Requirements, App Review Preparation, Google Play Policy Operations Control Register |

These internal links connect the consolidated policy domains to existing bilingual topics for offline navigation. The topic summaries and child-link audit states remain documented in each topic and the recursive policy link graph.

## Common lifecycle checks

| Stage | Minimum areas to review |
| --- | --- |
| Account setup | Choose Personal/Organization; complete identity/contact and applicable device/website verification. Certain financial, health, VPN, and government apps must use Organization accounts. New personal accounts also face closed-testing and production-access requirements. |
| Before submission | App functionality, content, store listing, target audience, and ratings must agree. Provide an accessible privacy policy, Data safety, and applicable declarations; give reviewers working credentials and special access steps; review app and SDK permissions, data, and security. |
| Each release/update | Recheck target API, permissions/API declarations, changes to content and age experience, subscriptions/billing/ads, and third-party SDK changes. Update affected declarations and monitor Policy Deadlines. |
| After launch | Maintain account/developer details and privacy/Data safety disclosures; handle data deletion, user reports, refunds/support, and policy notices; monitor Policy status and resolve or appeal promptly. |
| Program/market-specific distribution | Add country/market and form-factor rules for finance, loans, gambling, health, children, and device programs, as well as local law. Program approval or pilot enrollment does not satisfy other policies automatically. |

## Related knowledge-base entries

- The 51 original policy topics and unexpanded descendant-link status: recursive policy link graph.
- Actionable pre-release and operational checks for privacy, permissions, billing, audiences, content, safety, and declarations: Google Play Policy Operations Control Register (中文).
- App content declarations, identity, and release gates: Play Console Requirements.
- Dynamic dates: use [Policy Deadlines](https://support.google.com/googleplay/android-developer/table/12921780). As of this review, the 2026 target API deadline has passed; eligible extensions run to November 1, 2026. See the Play Console Requirements entry.
- Historical notices: announcement index. Historical wording does not override the current consolidated policy.
- Contract duties: [Developer Distribution Agreement](../developer-distribution-agreement/developer-distribution-agreement.en-US.md). Verification status and regional rollout: Android Developer Verification.
- The “User Data” and “SDK Requirements” sections were cross-checked against the standalone [User Data topic](../user-data/user-data.en-US.md). Core duties align; the consolidated SDK section adds examples about ad/analytics sharing, installed-package disclosure, and a two-week evidence response. See the scope and failed User Data retry in that topic and recursive link graph §4.123.

## Coverage gaps and audit conclusion

This knowledge base can be described as a bilingual navigation and summary library for **major public Google Play policies and release requirements**, but **not an exhaustive collection of every Google Play rule**. Remaining boundaries include:

1. All 51 direct targets in the current Chinese Policy Center and all 52 in the English directory (which adds Android XR) have a full-body-open status and manual summary record in the URL ledger. The local library stores bilingual summaries and official source links, not copies of the complete policy text. Inline links, grandchildren, and deeper descendants on these separate articles have not yet been exhausted. The link graph and operations control register describe the coverage and status.
2. Country-specific finance, lending, gambling, privacy, tax, consumer-protection, and industry licensing rules have not been compiled jurisdiction by jurisdiction. Laws change, and Play policy does not replace legal review.
3. The 56 Policy Archive PDFs are registered as a version index, not reproduced in full. Open a specific dated version when reconstructing historical requirements.
4. Signed-in Play Console forms/account state, closed program terms, Play Academy courses, videos, and community cases are not treated as fully verifiable policy text.
5. General Android API documentation, Google service terms, payment/ad/game program terms, and third-party SDK terms are included only where directly relevant to Play policy; this is not a recursive crawl of all Google/Android properties.

This library helps locate rules, dates, and implementation guidance. It cannot establish that a particular app is compliant or approved. Use the account-specific Console notices and current official text for final decisions.
