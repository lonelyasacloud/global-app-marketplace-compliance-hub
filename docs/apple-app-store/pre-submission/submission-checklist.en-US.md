---
id: apple.pre-submission.checklist
platform: apple
language: en-US
authority: operational
status: current
kb_checked_at: 2026-11-09
review_due: 2027-02-09
snapshot_package: 2026-11-10
regions: [global]
topics: [review, metadata, privacy, payments, age-rating, submission]
editorial_note: "Imported from the snapshot checked 2026-11-09 (package 2026-11-10). No live re-check in this import. Checklist items are implementation notes derived from Apple guidelines and Help. Chinese wording for post-2026-06-08 English guideline changes is an editorial translation. The shorter cross-platform gate remains docs/operations/pre-submission/quick-check."
---

# Pre-submission Checklist

Check each item and record the evidence, owner, or review note in the team workflow. This checklist is an **implementation note**. It is not an Apple approval guarantee and it does not add Apple rules.

It is more detailed than the cross-platform [pre-submission quick check](../../operations/pre-submission/quick-check.en-US.md). Keep both. The rule summary is the [guidelines summary](../app-review-guidelines/guidelines-summary.en-US.md). The short readiness page is [review readiness](../app-review-guidelines/review-readiness.en-US.md). In the snapshot, the English App Review Guidelines were updated on October 16, 2026, and the Simplified Chinese official page still shows June 8, 2026. Chinese wording on the paired page for later English changes is an editorial translation, not Apple’s published Chinese text. This import did not reopen live pages. The knowledge-base check date is 2026-11-09 (package dated 2026-11-10).

## A. Build and runtime

- [ ] Test the submitted build on real supported devices and OS versions. No crashes, blocking defects, placeholders, or empty screens.
- [ ] Sign-in, core flows, paid content, and required backend services stay available during review.
- [ ] The build matches its metadata. New features and material changes are located in the review notes.
- [ ] Provide reproducible steps and evidence for required hardware, regions, accounts, QR codes, networks, or configurations.
- [ ] No hidden, dormant, undocumented, or post-review-only features. The reviewed build matches the release experience. The hidden-functionality control includes English guideline 2.5.19. Paired Chinese wording for that clarification is an editorial translation.

## B. Store metadata

- [ ] Name, subtitle, keywords, description, and developer identity are accurate. No keyword stuffing, impersonation, unauthorized marks, or unverifiable claims.
- [ ] Icons, screenshots, previews, creative assets, and in-app events show real functionality, suit all audiences, and are rights-cleared. Creative-asset limits include English guideline 2.3.14. Paired Chinese wording is an editorial translation.
- [ ] Age-rating answers are accurate. Child-audience claims, Kids Category selection, and children’s privacy handling agree with each other. See [age-rating values and definitions](../age-ratings/age-ratings.en-US.md).
- [ ] **New in November 2026. Region-sensitive:** Complete the Shared Location and Dating and Relationships declarations in App Store Connect. Finish every app by 2027-01-12. If Dating and Relationships applies, confirm the minimum 18+ rating. For Brazil, review A16/A18 and the MJSP official-rating path where it is needed. See the [age-rating topic](../age-ratings/age-ratings.en-US.md) and the [announcement](https://developer.apple.com/news/?id=yxkh08us). Chinese wording of this item is an editorial summary of the English notice.
- [ ] Support, privacy-policy, marketing, and in-app URLs work. Contact information is current.
- [ ] Paid features, subscriptions, trials, virtual items, and additional purchases are clearly disclosed on the product page and in the app.

## C. Privacy and accounts

- [ ] App Privacy answers match the real data flows of the app, backend, analytics or ad SDKs, and other third parties.
- [ ] The privacy policy covers collection, use, sharing, retention, deletion, and consent withdrawal, and is easy to reach in the app.
- [ ] Permission prompts and purpose strings describe the data use specifically. Ask in context, and leave a reasonable experience after denial or withdrawal.
- [ ] Tracking happens only with the required ATT consent. Third-party AI and SDK data sharing is disclosed and authorized.
- [ ] **Conditional:** If the app integrates the Siri AI Developer Preview, test it separately for beta OS versions, supported regions and languages, the under-13 restriction, Apple Intelligence terms, and privacy disclosures. Do not treat preview behavior as a stable release commitment. The source is the 2026-11-03 announcement, not a universal review clause: [Siri AI Developer Preview](https://developer.apple.com/news/?id=gdk2umrf). **Region-sensitive.**
- [ ] If users can create accounts, they can start deletion in the app. The flow deletes associated data or explains lawful retention.
- [ ] Restrictions for children, health, location, contacts and photos, calls and SMS, and other sensitive areas are checked one by one.

## D. Payments and business model

- [ ] Each transaction is classified as digital content, physical goods or services, real-time person-to-person services, enterprise, reader, or another applicable category.
- [ ] Digital unlocks, subscriptions, virtual currency, and randomized items follow the current IAP rules. Restore and refund behavior works.
- [ ] **Region-sensitive:** External payments, links, and alternative distribution are enabled only for eligible storefronts, platforms, and entitlements. Required agreements are accepted.
- [ ] Subscription screens show price, duration, trial, renewal, benefits, and cancellation. Paid benefits do not depend on an unrelated task.
- [ ] **Region-sensitive:** If the app sells standard IAP or paid apps on the Taiwan iOS/iPadOS storefront, reconcile revenue, tax, and settlement records at the 26% rate effective 2026-10-31. Do not apply that rate to other storefronts. See the [Taiwan storefront notice](https://developer.apple.com/news/?id=w9mxlhek) and the [license summary](../developer-program/license-agreement.en-US.md).
- [ ] If the app offers auto-renewable subscriptions, verify multiseat availability in App Store Connect, organization purchases in Apple Business Manager and Apple School Manager, group seat assignment and removal, and Sandbox testing. If the app does not offer this, check whether those channels should be off. See the [business and school subscription notice](https://developer.apple.com/news/?id=yfo21au).
- [ ] **Only if enabled:** Retention-message copy is accurate, relevant, and suitable for all audiences. Do not include a specific price or discount, or a coercive or unverifiable outcome. Images and offers match subscription eligibility and storefront settings, and are submitted for review. See the [retention-message notice](https://developer.apple.com/news/?id=fk9ps3gv).
- [ ] **Region-sensitive:** Regulated financial, medical, VPN, gambling, crypto, and fundraising services have the required provider eligibility, licenses, geographic limits, and documents.

## E. UGC, children, and safety

- [ ] UGC has filtering, reporting, a timely response, user blocking, reachable contact information, and a working removal process.
- [ ] Moderation responsibility is clear for UGC, AI-generated content, creator content, and mini apps. Content above the age rating is labeled and age-restricted. Treating AI content creation as part of the UGC risk area restates the English 1.2 clarification. Paired Chinese wording is an editorial translation.
- [ ] Purchases and external links in the Kids Category sit behind a parental gate. Children’s data is not sent to third parties without a permitted reason.
- [ ] Medical, health, safety, dangerous-activity, and real-world-harm features have an accuracy and risk review, with the evidence kept.

## F. Intellectual property, design, and system integration

- [ ] Rights are cleared for assets, music, video, marks, likenesses, third-party services, and external content.
- [ ] The app is not confusingly similar to a competitor, an Apple product, an ad, or a popular app. Bundle IDs are not being used to create repetitive listings.
- [ ] APIs, background modes, extensions, widgets, notifications, WebKit or other browser engines, and device permissions are used as intended.
- [ ] Mini apps, chatbots, plug-ins, and emulators have been checked for indexing, universal links, moderation, permission isolation, and payment rules.

## G. Agreement, certificates, and regional terms

- [ ] The Program account has accepted the latest agreement. Record who accepted it, when, and which version. See the [license summary](../developer-program/license-agreement.en-US.md).
- [ ] Certificates, private keys, and App Store Connect API keys are access-controlled, with rotation and incident-response plans.
- [ ] The relevant attachment and restrictions are checked for every API, entitlement, Apple service, and data type in use.
- [ ] **Region-sensitive:** Regional attachments and business terms are checked for the storefronts you ship, especially payments, distribution, commissions, and taxes in mainland China, the EU, Japan, and Brazil.

## H. Suggested review-note fields

These fields are an implementation note to help a reviewer reproduce the app. They are not a fixed form quoted from the guidelines.

| Field | What to record |
| --- | --- |
| Purpose and model | Core purpose, intended audience, business model |
| New features | Entry points and reproduction steps |
| Accounts | Demo credentials or demo mode, and permissions |
| Environment | Tested devices, OS versions, and regional differences |
| Third parties | SDKs, AI services, authentication, payments, and content providers |
| Evidence | Licenses, regulatory approvals, IP permissions, or security documentation |
| IAP | How to open, test, and restore items |

## I. Complete-review evidence

- [ ] The app concept, business model, intended audience, and restricted regions are in App Review Information.
- [ ] Each account role has working demo credentials, sample data, and permissions. Codes, MFA, invitations, region limits, and reset steps are documented.
- [ ] Backend, login, payments, content services, and third-party dependencies stay reachable during review, without internal-only access or a temporary setup.
- [ ] If hardware pairing is required, a physical-device video includes the device, OS, pairing, and reproduction steps.
- [ ] Regulated features have licenses, partnership evidence, or other documents Apple asks for.
- [ ] IAP and subscription product IDs, navigation paths, Sandbox testing, restore, and regional differences can be reproduced.

## J. Privacy supply chain and metadata assets

- [ ] The final app bundle has been inspected for `PrivacyInfo.xcprivacy`, Required Reason APIs, SDK signatures, and the third-party SDK inventory.
- [ ] App Privacy Details match the app, backend, and every SDK. Answers are updated when practices change.
- [ ] Screenshots and previews for every localization, device size, and Media Manager entry match the current version. No stale asset remains.
- [ ] For each device type, most screenshots show the app in use rather than a login screen, splash screen, or marketing art alone. See the [guideline 2.3.3 screenshot reference](https://developer.apple.com/help/app-review/guideline-reference/2-3-3-screenshots/).

## K. Submission objects, statuses, and time

- [ ] The submission lists every object it includes: app version, IAP, subscriptions, In-App Events, custom product pages, product-page optimization tests, asset packs, or Game Center items. See the [review-workflow topic](../review-workflow/review-workflow.en-US.md).
- [ ] Each platform is checked on its own. An approved app version does not mean every attached item is approved.
- [ ] The current status, editable fields, response path, and resubmission method are recorded.
- [ ] Effective dates, mandatory deadlines, case-specific notice deadlines, internal due dates, and the next review date are recorded separately. An Apple deadline is not the same date as this page’s `review_due` (knowledge-base recheck on 2027-02-09).

## Official workflow references

- [Provide information for a complete review](https://developer.apple.com/help/app-review/before-submitting-for-review/complete-review/)
- [Test your app on compatible devices](https://developer.apple.com/help/app-review/before-submitting-for-review/test-compatible-devices)
- [Configure In-App Purchases for review](https://developer.apple.com/help/app-review/before-submitting-for-review/configure-in-app-purchases)
- [Track a submission's review status](https://developer.apple.com/help/app-review/after-submitting-for-review/review-status)
- [Contact App Review for help with a submission](https://developer.apple.com/help/app-review/after-submitting-for-review/contact-app-review)
- [App Review Guidelines (English baseline)](https://developer.apple.com/app-store/review/guidelines/)
- [App Privacy Details](https://developer.apple.com/app-store/app-privacy-details/), [Privacy Manifest](https://developer.apple.com/documentation/bundleresources/adding-a-privacy-manifest-to-your-app-or-third-party-sdk), and [Required Reason API](https://developer.apple.com/documentation/bundleresources/describing-use-of-required-reason-api)

This checklist does not replace those official pages or the current App Store Connect configuration.
