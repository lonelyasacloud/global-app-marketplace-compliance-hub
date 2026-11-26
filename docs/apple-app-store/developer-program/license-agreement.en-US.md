---
id: apple.developer-program.license-agreement
platform: apple
language: en-US
authority: operational
status: current
kb_checked_at: 2026-11-09
review_due: 2027-02-09
snapshot_package: 2026-11-10
regions: [global, CN, EU, JP, BR, TW]
topics: [agreement, payments, distribution, certificates, regional]
editorial_note: "Snapshot checked 2026-11-09 (package 2026-11-10). No live re-check in this import. The supplied /cn/ license URL rendered English. The October 13, 2026 amendment notice said a translation would follow within one month. The paired Chinese page is an editorial summary, not Apple's published translation or legal advice. The separate App Review Guidelines gap (English 2026-10-16 vs Simplified Chinese 2026-06-08) is disclosed in the guidelines summary."
---

# Developer Program License Agreement Summary

## Version, language, and evidence level

This page is an **editorial summary** for product, engineering, and operations. It is not Apple’s official translation and it is not legal advice. For interpretation or a conflict, use the latest agreement, the applicable attachment, and qualified counsel.

The snapshot’s link contains `/cn/`: [Apple Developer Program License Agreement](https://developer.apple.com/cn/support/terms/apple-developer-program-license-agreement/). As of the check on **2026-11-09**, both the page title and the agreement text were in English. The October 13, 2026 update notice said a translation would be available within one month. Until then, use the English text on that page as the agreement source. This import did not reopen the live agreement and does not treat 2026-11-09 as a newer online verification. The package date is 2026-11-10.

The index of current agreements is [Apple Developer Agreements and Guidelines](https://developer.apple.com/support/terms/).

**Current versus historical:** This summary follows the live agreement opened on 2026-11-09, the [October 13, 2026 amendment notice](https://developer.apple.com/news/?id=17mwd36z), and the [October 29, 2026 Taiwan storefront notice](https://developer.apple.com/news/?id=w9mxlhek). The August 18, 2026 agreement notice is only an earlier point on the amendment timeline. It is not the current agreement text and cannot establish current obligations by itself. If this summary differs from the live agreement, a later notice, or terms waiting for acceptance in the account, use the latest official text and the applicable attachment, and confirm acceptance in the developer account.

The App Review Guidelines have a separate language gap: English page October 16, 2026; Simplified Chinese official page June 8, 2026. That gap belongs to the guidelines, not to a Chinese edition of this agreement. See the [guidelines summary](../app-review-guidelines/guidelines-summary.en-US.md).

## What the agreement does

The agreement grants a limited right to use Apple software, services, certificates, and related capabilities. It governs development, testing, signing, submission, distribution, payments, privacy, confidentiality, and liability. It applies together with the App Review Guidelines, App Store Connect documentation, entitlement terms, and local law. App Review does not transfer the developer’s responsibility for app safety, rights, data, taxes, support, or compliance.

The agreement itself is normative. The tables below are operational points, not the clause text.

## Main agreement

| Section | Summary | Operational meaning |
| --- | --- | --- |
| 1. Accepting this Agreement; Definitions | Confirms acceptance and defined terms. An individual must have legal capacity. A representative must have authority to bind the organization. Definitions cover Apple software, services, apps, data, certificates, authorized developers, and pre-release materials. | Check the contracting entity, the account holder, and team authority. Later interpretation should return to the definitions in the agreement. |
| 2. Internal Use License and Restrictions | The license is limited, nonexclusive, revocable, nontransferable, and nonsublicensable, for permitted development and testing. Software and services may be used only within the licensed purpose and terms. | Do not use Apple software, keys, services, or developer resources for an unlicensed purpose. Limit contractor access and remain responsible for contractor conduct. |
| 3. Your Obligations | Developers remain responsible for accurate account information, team and contractor conduct, law, privacy and consent, intellectual property, product safety, and use of APIs, frameworks, and services. Many APIs and data types have purpose-specific limits. | For each entitlement and API, record eligibility, purpose, data, user disclosure, and retention or deletion. Do not infer that a callable API is an approved purpose. |
| 4. Changes to Program Requirements or Terms | Apple may change program requirements or terms. Continued use requires acceptance. Refusal may suspend or terminate access. New requirements are not retroactive to apps already distributed, but Apple may remove a noncompliant app. | Name an owner for term changes and keep the acceptance record. Assess shipped versions, later updates, and whether each storefront needs action. |
| 5. Apple Certificates; Revocation | Apps, Wallet passes, Safari extensions, and other covered products must be signed for their permitted purposes. Developers must protect keys, limit sharing, and tell Apple about a compromise. Apple may revoke certificates or tickets in the security, breach, and other cases the agreement states. | Rotate keys. Do not place a distribution private key in an ordinary repository that third parties can reach. Keep a certificate owner and an incident-response path. |
| 6. Application Submission and Selection | Covers App Store and Custom App Distribution submission and selection, App Thinning, iOS and iPadOS app availability on macOS and visionOS, CarPlay and Apple HomeView widgets, TestFlight, and analytics. Developers may not hide features from review, must hold the rights, and remain responsible for cross-platform compatibility. | Keep the submission consistent with the real feature set. Check cross-platform rights, test coverage, material TestFlight changes, and permitted uses of analytics. |
| 7. Distribution of Applications and Libraries | Permitted routes include the App Store, Custom App Distribution, Ad Hoc, TestFlight, and libraries. Unauthorized third-party distribution is restricted. Developers remain responsible for the app, metadata, export compliance, and rights. | Record each build’s channel, audience, region, signature, and export compliance. Do not treat enterprise or in-house distribution as a substitute for public App Store distribution. |
| 8. Program Fees | Membership requires the applicable annual fee, generally nonrefundable, with applicable taxes. Auto-renewal and purchases through the Apple Developer app may add terms. | Keep renewal and payer details current. Purchases through the Developer app also implicate Attachment 9. |
| 9. Confidentiality | Pre-release software, services, hardware, and related materials are generally Apple Confidential Information. They cannot be disclosed or used outside the agreement before release unless an exception applies. | Put betas, unreleased features, and test materials under the confidentiality process. Check access and disclosure limits before offboarding, outsourcing, or external communication. |
| 10. Indemnification | To the extent allowed by law, developers must address and indemnify Apple for specified losses tied to breach, products, content, intellectual property, end-user claims, and development or distribution. | Include third-party content licenses, consumer complaints, child safety, privacy, and product liability in pre-release review and evidence retention. This row is not legal advice. |
| 11. Term and Termination | Membership renews annually. Serious or uncured breach, a confidentiality violation, or rejection of new terms may lead to termination or suspension. Use must stop after termination, and Apple software and confidential materials must be handled as required. Specified provisions survive. | Keep account continuity, renewal reminders, and a fallback for critical services. Note the post-termination state of data, certificates, and distribution. |
| 12. No Warranty | Apple software and services are provided under the agreement and may contain errors, become unavailable, or change. The agreement disclaims a general guarantee of availability, accuracy, or uninterrupted service. | Do not treat an Apple service as the only fail-safe. Design degradation, retry, and backup for critical features. This is an implementation note. |
| 13. Limitation of Liability | Specified Apple liabilities are limited or excluded. The full clause and mandatory local law control the scope. | Do not assume Apple bears the app’s operating losses when assessing the business, insurance, or service continuity. |
| 14. General Legal Terms | Covers third-party notices, independent development, notices, severability, waiver, export controls, government end users, dispute resolution and governing law, the entire agreement, and the governing language. | Check local export and sanctions duties and the applicable law. Do not treat marketing copy or an oral statement as an amendment. |

## Schedules

| Document | Scope | What to check |
| --- | --- | --- |
| Schedule 1, App Store distribution of free apps | Apple markets and delivers apps as agent or commissionaire. Covers submission, territory, metadata, the EULA, rights statements, withdrawal, legal responsibility, and App Store discoverability. | Distribution regions, product information, privacy policy, EULA, export, and intellectual-property rights. Exhibit D states that Apple does not guarantee featuring, placement, or rank. |
| Schedule 2, paid applications and IAP | Applies to paid apps and to goods or services sold through Apple In-App Purchase. Covers transactions, commission, refunds, tax, proceeds, and subscriptions. | Storefront, program eligibility, commission and tax, IAP delivery, and refund responsibility. The October 2026 revision covers multiseat Group Purchases. A November 2026 notice adds retention messages in the subscription cancellation flow: [retention messages](https://developer.apple.com/news/?id=fk9ps3gv). |
| Schedule 3, Custom App Distribution | Applies to apps distributed to identified institutional customers through Custom App Distribution. Covers customers, delivery, fees, tax, and responsibility. | Customer list and organization, private distribution, orders and payment, the EULA, and tax. The October 2026 revision covers volume purchasing of subscriptions for Apple Business Manager and Apple School Manager. |

## Attachments

The agreement page includes 14 attachments. An attachment applies when the developer uses that capability or enters that region or business model. Once it applies, it binds the developer together with the main agreement.

| Attachment | Topic | Control |
| --- | --- | --- |
| 1 | Apple Push Notification Service and local notifications | Push Application ID, user opt-in, notification-data use, and service limits. |
| 2 | In-App Purchase API | Receipt validation, delivery, refunds, group purchases, tax, and API limits. |
| 3 | Game Center | User content, player interaction, service security, and volume subscriptions for Apple School Manager and Apple Business Manager. |
| 4 | iCloud | Purpose, storage, and access limits for iCloud and CloudKit data. |
| 5 | Wallet passes | Pass content, signing, distribution method, and user-experience requirements. |
| 6 | Apple Maps, MapKit, and MapKit JS | Map-data use, display and attribution, and local law. |
| 7 | Safari extensions | Extension signing, distribution, functionality, and privacy requirements. |
| 8 | WeatherKit | Weather-data and API use, display, quota, and regional law. |
| 9 | Apple Developer app subscriptions | Extra purchase terms for membership or other subscriptions bought through the Developer app. |
| 10 | Mobile Device Management (MDM) | Authorized scenarios only. Configuration profiles, device management, and privacy responsibility. |
| 11 | EnergyKit | Eligible vehicle or thermostat developers only. Data must not be used for unrelated advertising, profiling, or model training. |
| 12 | iOS apps in Japan and Brazil | Alternative marketplaces, alternative payment, offers outside the app, and the related entitlement and regional constraints. **Region-sensitive.** |
| 13 | iOS and iPadOS apps in mainland China | Commission and payment terms for the mainland China storefront. The snapshot records a standard commission of 25%, with 12% for qualifying items. **Region-sensitive.** Use the current rate in the account. Do not generalize it. |
| 14 | Apps in the European Union | Alternative distribution, alternative payment, offers outside the app, and the EU business terms. The page states an effective date of October 1, 2026, or the signing date, whichever is later. **Region-sensitive.** |

## October 13, 2026 amendment

Apple’s [update notice](https://developer.apple.com/news/?id=17mwd36z) lists the following changes. This is an operational summary, not replacement wording. Chinese wording on the paired page is an editorial summary.

1. **Section 3.2, security:** Updates security and related requirements for use of Apple software and services. A security review should cover permissions, credentials, user data flows, malicious behavior, and platform protections.
2. **Sections 3.3.8(j) and 3.3.8(k):** States the terms for the Live Assistance API and the App Replacement Entitlement. Check eligibility, the API documentation, and the user-experience requirements before use.
3. **Sections 6.4–6.4.2, CarPlay and Apple HomeView:** iOS app widgets may be available in CarPlay and Apple HomeView. Decide whether a widget is appropriate while driving. Widgets that are not can be marked with `disfavoredLocations`. An app with the designated CarPlay entitlement may also be available in Apple HomeView on a paired device.
4. **Schedule 2, Group Purchases:** States the sales and service arrangement for providing multiple subscription seats through group purchase.
5. **Schedule 3, volume purchasing:** States the arrangement for offering multiseat subscriptions to Apple Business Manager and Apple School Manager organizations through volume purchase.
6. **Tax information in Schedules 2 and 3:** Apple may report information that the law requires to tax authorities. Customer tax information a developer receives may be used only for purposes the law allows.
7. **Acceptance:** The notice tells developers to sign in and accept the updated terms. Section 4 says that refusing new terms may suspend or terminate the related software, certificates, or services.

The product notice for business and school multiseat purchasing is the [October 22, 2026 announcement](https://developer.apple.com/news/?id=yfo21au).

## October 29, 2026 Taiwan storefront amendment

Apple’s [notice](https://developer.apple.com/news/?id=w9mxlhek) says that, effective **October 31, 2026**, the commission for standard In-App Purchases and paid-app transactions on the Taiwan iOS and iPadOS App Store storefront changed from **30% to 26%**. Apple also revised the Developer Program License Agreement. The notice says signing the updated terms by October 31 was not required in order to receive the rate change. **Region-sensitive.**

- [ ] If the product sells on the Taiwan storefront, recheck revenue forecasts, tax and settlement reporting, and the applicable schedules.
- [ ] Do not extend the Taiwan rate change to other regions or other transaction types. Use current App Store Connect account data and the latest agreement.

## High-priority checks

The items below are implementation notes.

- [ ] Confirm the contracting entity, the account holder, and App Store Connect roles. Give team members, contractors, and service providers only the access they need.
- [ ] Inventory every Apple API, entitlement, system data source, and service. Record eligibility, permitted purpose, disclosure, consent, and data lifecycle.
- [ ] Use documented APIs only, and process data for the permitted purpose. Health, location, communications, device identity, voice, AI or model, and Wi-Fi data may have extra limits.
- [ ] Keep reasonable safeguards for the Foundation Models Framework and follow its acceptable-use requirements.
- [ ] Protect signing certificates, private keys, provisioning profiles, App Store Connect API keys, and Push IDs. Maintain rotation and incident response.
- [ ] For each app, review applicable law, the privacy policy, intellectual property, export and encryption, age rating, and product support. Apple’s approval does not replace those duties.
- [ ] Map every distribution path. The App Store, Custom App Distribution, TestFlight, Ad Hoc, the web, and an alternative marketplace each have their own program terms, regional terms, and entitlements.
- [ ] For paid apps, IAP, subscriptions, group and multiseat purchases, alternative payments, and Custom Apps, check the correct schedule and attachment, plus commission, tax, refunds, and user support.
- [ ] **Region-sensitive:** For mainland China, verify Attachment 13 and the current App Store Connect rate. For the EU, Japan, and Brazil, verify the applicable regional attachment and entitlement.
- [ ] When a new agreement or Program Requirements arrive, log the effective date, the impact, who accepted and when, and the release actions.
- [ ] For the October 2026 revision, check whether the product uses the Live Assistance API, the App Replacement Entitlement, CarPlay or HomeView widgets, or multiseat subscriptions.
- [ ] **Region-sensitive:** If the app sells standard IAP or paid apps on the Taiwan iOS and iPadOS storefront, verify the 26% rate, tax and settlement records, and the current agreement status. Do not generalize the Taiwan adjustment.

## Scope of this summary

This summary focuses on App Store distribution, App Store Connect, IAP and subscriptions, certificates, privacy, and regional attachments. The agreement also covers Wallet, APNs, Game Center, iCloud, MapKit, WeatherKit, MDM, Safari extensions, EnergyKit, and other areas. Read the relevant attachment and API documentation when those capabilities are used.

The agreement lists discoverability factors such as text relevance, metadata, ratings and reviews, downloads, and launch date. Apple does not promise a particular placement or rank.

Submission checks: [pre-submission checklist](../pre-submission/submission-checklist.en-US.md). Age rating: [age-rating topic](../age-ratings/age-ratings.en-US.md).

This page does not replace the [current English agreement](https://developer.apple.com/cn/support/terms/apple-developer-program-license-agreement/) or terms waiting in the account. The snapshot records that this `/cn/` path displayed English text on 2026-11-09.
