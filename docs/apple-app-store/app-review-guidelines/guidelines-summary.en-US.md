---
id: apple.app-review.guidelines-summary
platform: apple
language: en-US
authority: operational
status: current
kb_checked_at: 2026-11-09
review_due: 2027-02-09
snapshot_package: 2026-11-10
regions: [global]
topics: [review, safety, privacy, payments, metadata, ugc, kids]
editorial_note: "English App Review Guidelines page updated 2026-10-16; Simplified Chinese official page in the snapshot shows 2026-06-08. Chinese wording for newer English rules is an editorial translation, not Apple's published Chinese text. Snapshot checked 2026-11-09; package dated 2026-11-10. Guideline-page comparison inside the snapshot is dated 2026-10-21. This import did not re-check live pages."
---

# App Review Guidelines Summary

## Sources and evidence level

This page is an operational summary of the App Review Guidelines. It is not Apple’s source text and does not replace the live page used at submission. Completing the summary does not guarantee approval.

| Material | Evidence level | Date recorded in the snapshot |
| --- | --- | --- |
| [App Review Guidelines (English)](https://developer.apple.com/app-store/review/guidelines/) | Normative source. The English page is the current policy baseline | Page updated October 16, 2026. In-snapshot comparison dated 2026-10-21 |
| [App Review Guidelines (Simplified Chinese)](https://developer.apple.com/cn/app-store/review/guidelines/) | Historical translation / comparison page | Page shows June 8, 2026 |
| [October 16, 2026 guidelines update](https://developer.apple.com/news/?id=92th7e5i) | Change notice | 2026-10-16 |
| [Nonconsensual intimate imagery and bait-and-switch enforcement note](https://developer.apple.com/news/?id=vvzx6cul) | Companion enforcement notice | 2026-10-16 |

`kb_checked_at` is the snapshot check date **2026-11-09** (package dated 2026-11-10). This import did not reopen the live pages and does not record a newer online verification.

## English / Simplified Chinese official-page gap

As of the snapshot check, the English guidelines are dated **October 16, 2026**. The Simplified Chinese official page still shows **June 8, 2026**. Apple’s October 16 update notice says translations will be published within one month. Until that localized page is updated:

- Use the English page as the current policy baseline.
- Keep the Chinese official page as an older translation and comparison source. Do not use it to override a later English rule.
- Chinese wording in the paired page for rules added or clarified after June 8, 2026 is an **editorial translation**, not Apple’s published Simplified Chinese guideline text.

## October 16, 2026 English changes

The table is the snapshot maintenance paraphrase of Apple’s [October 16 announcement](https://developer.apple.com/news/?id=92th7e5i), not a full guideline translation. The paired Chinese page labels the same items as editorial translation. The same maintenance note also lists the November 2026 age-rating descriptors beside these rows. Those dates and rating effects come from the [November 2 English notice](https://developer.apple.com/news/?id=yxkh08us) and are kept in the [age-rating topic](../age-ratings/age-ratings.en-US.md), not in this table.

| Guideline | Change summary |
| --- | --- |
| 1.2 | Clarifies which apps and content fall under UGC moderation, including AI content-creation apps. Failure to implement safeguards, or to remediate noticed violations, may also implicate the Developer Code of Conduct. |
| 2.3.14 | Creative assets used across the App Store must accurately relate to app content, functionality, or brand; follow metadata rules; be suitable for all audiences; and avoid misleading references, unverifiable claims, or specific or discounted pricing. |
| 2.5.19 | Explicitly prohibits hidden, dormant, or undocumented functionality. Obfuscation or other concealment can lead to removal and developer-account termination. |
| 3.1.1(a) | Approved entitlements may link to a permitted destination. The music-streaming entitlement is described within the StoreKit External Purchase Link entitlement provision. Scope still depends on storefront, platform, and entitlement terms. |
| 5 | Apps found to facilitate human trafficking or child exploitation will be removed and blocked from alternative distribution, with authorities notified in extreme cases. |

## Scope

- App Review covers apps, updates, in-app purchases, events, metadata, and submitted content. Developers remain responsible for ad networks, analytics services, and third-party SDKs.
- The guidelines change over time. Some rules apply only to alternative distribution and notarization on iOS/iPadOS. Do not treat that scope as a universal App Store obligation.
- Local law in each distribution region also applies. Apple policy and legal obligations run together; neither replaces the other.

## 1. Safety

### 1.1 Objectionable or harmful content

Do not publish defamatory, discriminatory, malicious, overtly sexual, violence- or danger-promoting, misleading religious, false-device-data or prank, or exploitative current-event content. “For entertainment only” does not cure a deceptive feature. Treat pornography, trafficking, and exploitation risks carefully.

The latest English update explicitly highlights nonconsensual intimate imagery and “nudification” functionality. The paired Chinese wording for that point is an editorial translation.

### 1.2 User-generated and creator content

- Filter objectionable material before or at publication, provide reporting and a timely response, let users block abusive accounts, and publish reachable contact information.
- Developers must remove content that violates the guidelines, terms, or community standards. Egregious or repeated failures can lead to removal or account-level consequences.
- UGC services primarily used for pornography, random or anonymous chat, objectification, threats, or bullying do not belong on the App Store.
- AI content-creation services are within the UGC risk area under the newer English clarification. Creator content cannot change the native app’s core functionality. Disclose content that requires extra payment.
- Creator apps need to identify content above the app’s age rating and restrict minors using verified or declared age.

### 1.3 Kids Category

Kids Category apps should be designed for children. External links, purchases, and other distractions need to sit behind a parental gate. Leaving the category does not automatically remove expectations created by earlier distribution. Follow children’s privacy laws. Third-party ads and analytics are generally restricted, as is sending children’s personal or device information to third parties. Any limited exception must meet Apple’s stated conditions.

### 1.4 Physical harm

Health, medical, and diagnostic features may receive heightened scrutiny. Accuracy claims need verifiable methods and evidence. Unsupported sensor-only claims for blood pressure, glucose, oxygen, temperature, or X-rays are not acceptable. Remind users to consult clinicians where appropriate, and submit regulatory clearance when it applies. Drug dosage calculators must come from qualified entities or hold the required approval. Do not encourage minors to use tobacco, vapes, illegal drugs, or excess alcohol. Provide required licenses for regulated services. Do not encourage dangerous challenges or impaired driving.

### 1.5–1.7 Developer information, security, and crime reporting

Provide accurate, working support contacts. Protect data collected under law or agreement. Apps for reporting alleged criminal activity must involve local law enforcement and be offered only where that involvement is active. **Region-sensitive.**

## 2. Performance

| Guideline | Summary |
| --- | --- |
| 2.1 App Completeness | Submit a complete, release-ready build with valid metadata and URLs. Remove placeholders and crashes. Provide working demo credentials for login-based apps and keep backend services available during review. A full demo mode instead of credentials requires Apple’s prior approval. IAP must be configured, visible, and reviewable. |
| 2.2 Beta testing | Use TestFlight for betas, trials, and demos rather than an App Store release. TestFlight builds remain subject to review and cannot be distributed to testers for compensation. |
| 2.3 Accurate metadata | Names, descriptions, privacy information, icons, screenshots, previews, and events must represent the real experience. Describe new features in review notes and make them reachable. Names are limited to 30 characters. Do not stuff keywords or misuse trademarks. Screenshots should show the app in use. Assets must suit all audiences. See the October 16 table for guideline 2.3.14. |
| 2.4 Hardware compatibility | Support iPad where practical. Avoid excessive battery use, heat, or device damage. Do not run unrelated background tasks. Mac App Store apps also have sandboxing, packaging, startup, code-download, privilege, update, and localization requirements. |
| 2.5 Software requirements | Use public APIs as intended. Respect sandbox and container boundaries. Do not download code that changes app functionality, aside from the narrow educational-coding exception. Use background modes only for their intended purposes. Support IPv6-only networks. Use WebKit unless the app is eligible and authorized for an alternative engine. Call blocking, face authentication, recording, component ads, Matter, and ad presentation have specific constraints. Guideline 2.5.19 explicitly prohibits hidden, dormant, or undocumented functionality. |

## 3. Business

### 3.1 Payments and In-App Purchase

- Digital features, content, subscriptions, and virtual currency generally use In-App Purchase. Do not bypass that with custom unlock mechanisms. Provide restore for restorable purchases. Purchased credits cannot expire. Disclose randomized-item odds before purchase.
- Digital goods and services, physical goods and services, real-time person-to-person services, enterprise services, multiplatform services, and reader apps have different rules and exceptions. Classify by the underlying transaction, not only by the checkout screen or the merchant.
- **Region-sensitive:** External purchase links, alternative payments, and alternative distribution depend on storefront, platform, entitlement eligibility, and the current agreement. The U.S. storefront and selected regions may differ. Do not generalize a regional exception. See the October 16 table for guideline 3.1.1(a).
- Subscriptions must provide ongoing value, last at least seven days, and work across the user’s devices. Clearly disclose price, benefits, duration, trials, renewal, and cancellation. Do not trick users into subscribing or remove core functionality that existing customers already purchased.

See [auto-renewable subscriptions](https://developer.apple.com/app-store/subscriptions/), the [Developer Program License Agreement](https://developer.apple.com/support/terms/apple-developer-program-license-agreement/), [reader apps](https://developer.apple.com/support/reader-apps/), and [External Purchase](https://developer.apple.com/documentation/storekit/external-purchase). Agreement-level summary: [license topic](../developer-program/license-agreement.en-US.md).

### 3.2 Other business models

Apps that resemble catalogs, inflate ad impressions or clicks, restrict users without a reasonable basis, manipulate rankings on other services, or fundraise without authorization may be rejected. Financial, lending, crypto, exchange, donation, insurance, and virtual-asset services need checks of provider eligibility, licensing, regional limits, disclosures, and payment flows. **Region-sensitive.** Explain a business model that is not obvious in the metadata and review notes. That explanation step is an implementation note, not an additional Apple rule.

## 4. Design

| Guideline | Summary |
| --- | --- |
| 4.1–4.3 | Do not copy or impersonate apps. Avoid many near-identical Bundle IDs. Established, low-differentiation categories need a meaningful improvement. Do not submit placeholders, volume-manipulation builds, or repetitive variants. |
| 4.4–4.6 | Extensions should be useful and accurately disclosed. Do not put marketing, ads, or IAP inside extensions. Do not use Apple services for spam, phishing, or unsolicited marketing. Notifications cannot be required in order to use the app. |
| 4.7 | The host developer is responsible for mini apps, mini games, streaming games, chatbots, plug-ins, and emulators. Requirements include privacy safeguards, moderation, reporting, blocking, compliant payments, an index and universal links, age restrictions, and no sharing of native APIs or privacy permissions without consent. |
| 4.8–4.10 | When a third-party or social login creates the primary account, an equivalent qualifying login option is generally required, including private-email capability. Exceptions are listed in the guidelines. Disclose material purchase information before an Apple Pay transaction. Do not monetize built-in hardware or system capabilities, or Apple services themselves. |

## 5. Legal

### 5.1 Privacy

- Provide an easily accessible privacy policy in the app and in App Store Connect metadata. Explain what is collected, how, for what purpose, which third parties receive it, retention and deletion, how consent is withdrawn, and how users request deletion.
- Obtain appropriate consent before collection. Purpose strings must be specific and complete. Do not make unrelated data access a condition of paid functionality.
- Do not share personal data with third parties, including third-party AI, without explicit disclosure and permission. Do not repurpose data, reidentify anonymous users, or build contact or photo databases for internal use or sale. Tracking requires ATT permission.
- If the app supports account creation, provide in-app account deletion and actually complete deletion, or disclose a lawful retention exception. Deletion is not deactivation, sign-out, or hiding the account.
- Children’s data, health-research data, location, call and SMS data, and device permissions have additional constraints. Developers are responsible for third-party SDK behavior.

See [User Privacy and Data Use](https://developer.apple.com/app-store/user-privacy-and-data-use/), [account deletion](https://developer.apple.com/help/app-review/guideline-reference/5-1-1-account-deletion), and [purpose strings](https://developer.apple.com/help/app-review/guideline-reference/5-1-1-purpose-strings).

### 5.2–5.6 Intellectual property, regulated categories, and conduct

- **Intellectual property:** Use only content you own or are licensed to use. Third-party services, content, and media downloads need authorization. Do not imply Apple’s endorsement or imitate Apple products.
- **Games, gambling, and lotteries:** Developer-sponsored contests need official rules. Real-money gambling and lotteries need licensing, geographic restriction, and free App Store availability. Follow real-money gaming limits. **Region-sensitive.**
- **VPN and MDM:** Use the required APIs and meet provider eligibility and regional licensing rules. Disclose data collection and use before purchase or use. Follow the strict limits on sale, use, and sharing. **Region-sensitive.**
- **Developer Code of Conduct:** Be truthful about the developer and the product. Do not harass or defraud. Do not manipulate reviews, rankings, search, referrals, or purchase and refund flows.
- **After approval:** The app must keep working, maintain quality, and adapt when policy changes. Serious safety or legal issues can affect availability and the account.
- Apps found to facilitate human trafficking or child exploitation will be removed and blocked from alternative distribution, with authorities notified in extreme cases. The paired Chinese sentence for this October 16 clarification is an editorial translation.

## Before and after submission (implementation notes)

These steps operationalize the requirement for a complete, reproducible review. They are not a second set of Apple rules.

**Before submission:** Test stability. Keep metadata accurate, screenshots representative, and support links working. Prepare review credentials, demo paths, regional and device differences, third-party services, and authorization evidence. Keep backend services available. Explain non-obvious features and the business model in the review notes.

**After submission:** Track status in App Store Connect. Answer a rejection with facts, reproduction steps, and the relevant guideline. Request expedited review only for a genuine critical need. Use the formal appeal path when you disagree. Ask about Bug Fix Submission for an eligible bug-fix update to an app already on the store.

Executable checks, submission objects, and statuses:

- [Pre-submission checklist](../pre-submission/submission-checklist.en-US.md)
- [Review readiness](review-readiness.en-US.md)
- [Review materials, submission objects, and timing](../review-workflow/review-workflow.en-US.md)
- Cross-platform short gate: [pre-submission quick check](../../operations/pre-submission/quick-check.en-US.md)

This page does not replace the [current English guidelines](https://developer.apple.com/app-store/review/guidelines/) or the live App Store Connect configuration.
