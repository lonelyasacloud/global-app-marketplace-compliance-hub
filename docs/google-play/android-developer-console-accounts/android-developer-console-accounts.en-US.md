---
id: google-play.android-developer-console-accounts
platform: google-play
language: en-US
authority: operational
status: current
kb_checked_at: 2026-10-24
review_due: 2027-01-24
regions: [global]
topics: [android-developer-console, developer-identity, package-registration, duns, terms-of-service]
snapshot_id: android.developer-console-accounts
snapshot_package: "GooglePlay-KnowledgeBase-2026-10-24-review.zip"
coverage_status: "detailed-summary"
source_url: "https://support.google.com/android-developer-console/answer/16641416"
source_url_account_type: "https://support.google.com/android-developer-console/answer/16641046"
source_url_required_information: "https://support.google.com/android-developer-console/answer/16640818"
source_url_required_documents: "https://support.google.com/android-developer-console/answer/16501669"
source_url_distribution: "https://support.google.com/android-developer-console/answer/16640817"
source_url_limited_distribution: "https://support.google.com/android-developer-console/answer/17131204"
source_url_package_registration: "https://support.google.com/android-developer-console/answer/16640821"
source_url_identity_updates: "https://support.google.com/android-developer-console/answer/16641334"
source_url_add_users: "https://support.google.com/android-developer-console/answer/16642750"
source_url_verification_overview: "https://support.google.com/android-developer-console/answer/16561738"
source_url_get_started: "https://support.google.com/android-developer-console/answer/16604405"
source_url_contact_form: "https://support.google.com/android-developer-console/contact/developer_verification_issue"
source_url_console_terms: "https://developer.android.com/developer-verification/console/terms"
source_url_search_console_associations: "https://support.google.com/webmasters/answer/9419894"
source_url_search_console_add_property: "https://support.google.com/webmasters/answer/34592"
source_url_payments_settings: "https://payments.google.com/gp/w/home/settings"
source_url_adc_entry: "https://get.google.com/adc-early-access"
source_url_phone_format: "https://en.wikipedia.org/wiki/E.164"
source_url_google_terms: "https://policies.google.com/terms"
source_url_dnb_lookup: "https://my.dnb.com/lookup"
source_url_dnb_expedited: "https://www.dnb.com/en-us/marketing/dunsfile.html"
effective_date: "ADC ToS effective 2025-11-11, last updated 2026-03-27 UTC; 20-device and 50-device texts kept separate; no 2027-01-27"
---

# Android Developer Console Accounts, Identity Verification, and Terms

> **Import note (Google batch 7).** The body is the paraphrased summary from the already separated 2026-10-24 Google Play knowledge-base snapshot (`android.developer-console-accounts`, reviewed 2026-10-24). It is not a verbatim copy of an official page. The English official source is the source of truth. `kb_checked_at` is the review date recorded in the snapshot source file; this import did not re-open the live official pages. Phrases such as “this knowledge base,” “this library,” and “local topic” describe coverage inside that snapshot, not the set of pages imported into this repository. Relative snapshot links to topics, link graphs, ledgers, or CSVs that are not in this repository are kept as text mentions. Relative links that target the Google batch 1–6 topics or these twelve batch 7 topics point at the hub files. Reviewed 2026-10-24. Both files cite Android Developer Console Help URLs without a language parameter. The snapshot does not record a checked Chinese official ADC Help page or a failed `hl=zh-CN` fetch of those Help articles. The Chinese hub text is an editorial paraphrase. The Chinese-localized limited-distribution guide (`hl=zh-cn`, updated 2026-09-30), the guides hub, and the verification FAQ still say 20 devices. The English dedicated limited-distribution guide, updated 2026-10-23, says 50. Public sources in the snapshot do not explain the conflict. Those figures stay separate and do not confirm an account’s live cap. The ADC Terms of Service are effective 2025-11-11 and were last updated 2026-03-27 UTC. Both dates have passed. No 2027-01-27 date is recorded. The early-access entry was not publicly readable. ADC Help is operational. The ADC Terms are a contract for ADC use. ADC is for distribution outside Google Play. It does not replace Play Console requirements, the Play Developer Distribution Agreement, Play Console Terms, or Developer Program Policies. Android developer verification remains a separate snapshot topic and is not imported here.

**Reviewed: 2026-10-24.** This topic summarizes Android Developer Console (ADC) onboarding, identity verification, package registration, and account terms. ADC is part of Android developer verification and relates to Google Play developer accounts, but it is a separate system.

## Scope: Play Console and Android Developer Console

- Android Developer Console is for developers who distribute apps **only outside Google Play**. It is used to verify developer identity and register package names.
- Developers who use or plan to use Play Console can complete the Android developer verification steps in Play Console, including for apps distributed outside Play. Do not create an ADC account just because an app also ships outside Play.
- Android developer verification checks developer identity and the relationship between package names and signing keys. It does not review app content, source code, or compliance with Play policy. Play distribution still has separate [Play Console requirements](../play-console-requirements/play-console-requirements.en-US.md), [Developer Program Policies](../developer-program-policy/developer-program-policy.en-US.md), and applicable contracts.
- The Android Developer Console Terms of Service (ADC ToS) govern use of ADC. They are not the [Google Play Developer Distribution Agreement](../developer-distribution-agreement/developer-distribution-agreement.en-US.md) or the Play Console Terms of Service.

## Make two different account choices before signup

| Choice | Options | What it affects |
| --- | --- | --- |
| **Identity and ownership type** | Personal / Organization | Determines legal ownership, payment profile, and verification documents. A Personal account cannot be directly converted to Organization after creation, or vice versa. |
| **Distribution plan** | Limited / Full | Determines distribution reach and registration fee. The plan cannot be directly changed after creation; Google says to create another account and transfer package names. |

These choices are related but are not the same field. Limited distribution is available only for Personal accounts; Full distribution can follow either the Personal or Organization path.

| Plan | Official description | Verification and limits |
| --- | --- | --- |
| **Limited distribution** | Free; distribute to up to 20 authorized devices. | Requires a Google Account, 2-Step Verification, a Google Payments profile, and a contact email used by Google. No government ID is required. Only package names never previously seen on Android can be registered. |
| **Full distribution** | One-time US$25 registration fee; no install-device limit. | Complete verification for the selected Personal or Organization type. Accepted cards may vary by region. Prepaid cards are not a safe default. |

The Full plan fee and Limited device cap are from ADC registration guidance; they are not the Google Play developer-account registration fee.

**Source-specific cap note (October 24, 2026):** The 20-device figure in this topic faithfully reflects the current Android Developer Console Help pages. However, Android's dedicated [Limited Distribution guide](https://developer.android.com/developer-verification/guides/limited-distribution), updated October 23, now says 50, while the Chinese-localized [dedicated guide](https://developer.android.com/developer-verification/guides/limited-distribution?hl=zh-cn), the [guides hub](https://developer.android.com/developer-verification/guides), and the [verification FAQ](https://developer.android.com/developer-verification/guides/faq) still say 20. Public sources do not explain the conflict. Neither this Help text nor the dedicated guide alone confirms the cap currently active for a particular account; check the account page and obtain written Google Support guidance before planning for more than 20 devices.

## Identity and signup checklist

### Payments profile and legal identity

At signup, select or create a Google Payments profile. ADC uses its legal name/organization name and address to verify the real-world identity. Keep those details accurate and current. A developer name may differ from the legal name, but it can be shown to other ADC users in some account operations, such as a package transfer.

A Personal profile may require a government identity document. An Organization profile generally requires:

1. A D-U-N-S number;
2. Government photo ID for a person authorized to act for the organization; and
3. An organization registration document from a trusted government or public authority. The organization name must match the Dun & Bradstreet (D&B) profile.

Accepted organization documents depend on region. Google lists unsupported documents as a common cause of verification failure. A government organization that lacks ordinary registration documents may use official letterhead as directed by the page. Contact support before seeking a D-U-N-S exception; do not extend a government exception to ordinary organizations.

### D-U-N-S: apply for free, identify the right entity, and plan ahead

- D-U-N-S is a nine-digit organization identifier assigned by D&B. An organization may already have one; a large organization may have different numbers for different legal entities. Search first and select the number whose entity details match the account.
- Google says applying through D&B is free and warns developers about third parties charging high fees for this free application.
- Google's “Required information” article says an application may take up to **30 days**; its “Understanding Android developer verification” article says up to **28 days**; D&B's current public application page says normal processing can take up to **30 business days**, with an optional paid eight-business-day expedited service. These estimates differ. Apply early and check the current D&B process for your region. Paid expedited processing is a D&B option, not a Google-required fee.
- D&B says businesses generally do not need a D-U-N-S number to operate; Google sets its own D-U-N-S requirement for ADC Organization accounts. Do not treat D&B's general statement as a Google account exemption.
- Developers in regions unsupported by D&B and government entities can ask Google support for an alternative before signup. A government organization may need to provide an official email domain or associated official website. Google says incomplete requests are not considered and ordinary organizations will not receive an exemption or extension for failing to provide D-U-N-S.

See Google's [Organization account requirements](https://support.google.com/android-developer-console/answer/16640818), the [D&B business lookup](https://service.dnb.com/), the [D-U-N-S number lookup](https://my.dnb.com/lookup), and [D&B application guidance](https://www.dnb.com/duns/get-a-duns.html). D&B's interactive lookup showed a browser-compatibility notice or required JavaScript in this review; the application page was readable, and no application was started or submitted. D&B also lists an [optional expedited service](https://www.dnb.com/en-us/marketing/dunsfile.html), currently priced at US$229; this is a vendor option, not a Google requirement.

### Organization websites must be associated through Search Console

Every new Organization account must verify ownership of its website: first add and verify the site in [Google Search Console](https://support.google.com/webmasters/answer/34592), then request an association from the ADC Identity page. If the same Google Account owns the site and creates the ADC account, approval can be automatic. Otherwise, a registered Search Console owner must approve the request. Denial, an incorrect URL, or using a social-media profile URL can cause failure; correct the official website URL and try again.

This verifies control of the organization website. It does not verify a Play Store listing, a public Play developer profile, or app content. Search Console ownership verification grants high site permissions; check the site, Google Account, and token owners before approving an association.

### Contact details and privacy

ADC identity contact email and phone are used by Google to contact the developer and are not shown to Android users. Both are verified with one-time codes. Phone numbers use [E.164 international format](https://en.wikipedia.org/wiki/E.164); verification supports SMS or voice, and the carrier may charge for a call or message. If SMS does not arrive, try voice. Manage the linked profile in [Google Payments settings](https://payments.google.com/gp/w/home/settings); this route required sign-in during review.

For an organization, use an organization-domain address and a team inbox that will remain monitored for verification codes and account notices. Do not confuse private ADC contact details with public Google Play developer contact information or the app-specific support email; those are maintained separately in Play Console.

### Sharing a payments profile and account access

Personal payment profiles cannot be shared with team members; ADC's identity article says a Personal profile is tied to the person who originally created the ADC account. An Organization profile can be shared by its administrators. For multiple developer accounts with the same organization identity, Google says the same profile may be reused, but each ADC account owner must first be added as a payment-profile administrator and accept the invitation before selecting it in ADC. A payment-profile administrator may be able to use payment details stored in that profile, so check the profile and permissions.

ADC “Users” invitations and Payments profile administrator access are separate permission systems. Adding or removing an ADC user does not automatically grant or revoke Payments profile access, and the reverse is also true.

### Updating account details

- Update legal name or address through the linked Payments profile. Only a profile administrator can edit it. Organization profiles can have multiple administrators.
- To change country/region, Google requires a new ADC account and transfer of registered package names.
- Personal/Organization type is permanent. To change it, create another account and register the package names there.
- Update contact email or phone under ADC Identity > Contact details; the new value must pass a six-digit verification code.
- If identity and contact details are not kept valid, ADC identity may be restricted, preventing app distribution to certified Android devices.

## Package registration and Limited plan operations

ADC blocks package registration until identity verification is complete. A new package name requires the public SHA-256 signing-certificate fingerprint. For an existing package, Android's known install counts determine which signing keys can register directly. If a key is not eligible, a developer can ask Google to use the package name with a rationale, but the request may be denied.

To prove control of the signing key for an existing package, follow the Console flow: put the ADC-generated snippet in the APK's assets/adi-registration.properties file, sign the APK with the corresponding private key, and upload it. If a third-party store re-signs the app, use the final signed APK from that store as the proof. **Submit the public certificate fingerprint only; never disclose a private key or keystore password to Google support, D&B, or an untrusted third party.**

Limited plan details:

- This Help page says an account can have up to 20 devices authorized at one time. An unauthorized device cannot install or receive updates. See the source-specific cap note above.
- Only package names never previously seen on Android can be registered; an existing package name is rejected.
- A device-authorization link expires after seven days. The recipient must generate a code on the physical device and confirm they know and trust the developer.
- Removing a device prevents it from installing or updating the account's registered apps. Re-enable it by authorizing the device again.

See [Registering Android package names](https://support.google.com/android-developer-console/answer/16640821) and [Obtaining the app's SHA-256 certificate fingerprint](https://support.google.com/android-developer-console/answer/16641489). Package eligibility, existing signing keys, and multi-store re-signing can require special steps; check the account's current Console state before release or migration.

## Android Developer Console Terms of Service

The [Android Developer Console Terms of Service](https://developer.android.com/developer-verification/console/terms) are effective **November 11, 2025** and marked last updated **March 27, 2026 UTC**. Individual users must accept them to use ADC. The Terms say ADC enables developer identity verification and package registration; incomplete verification or registration may prevent app installation. Limited accounts may have additional or different terms, so use the version shown during that account's signup.

The Terms restrict use to ADC's intended functionality and prohibit illegal or abusive behavior, interference with or reverse engineering of the service, and use that violates terms for other Google products. Google may change or discontinue ADC; existing users generally receive at least 30 days' notice for ordinary Terms changes, with exceptions for new functions or legal requirements. Continued use indicates acceptance. Violations or distributing malware/harmful apps may result in termination of access. The English version controls, with California law and Santa Clara County venue; U.S. government entities have a specific exception.

The ADC ToS is an account/platform-use contract. It does not determine whether an app complies with Google Play content policy. Related official links include the [Google Privacy Policy](https://policies.google.com/privacy), [Google Terms of Service](https://policies.google.com/terms), [Android Developers Content License](https://developer.android.com/license), and the [ADC entry point](https://get.google.com/adc-early-access) named in the Terms; the entry point could not be publicly read in this review. The Android Developers Content License does not establish permission to copy Google Play Help or contract text in full.

## Regional document sample

The table summarizes five English regional views of Android Developer Console Help. It is not a global list; the applicable documents depend on the payment-profile region and current Console task.

| Region | Organization/representative documents (summary) | Individual documents and special notes |
| --- | --- | --- |
| [Australia](https://support.google.com/android-developer-console/answer/16501669?co=GENIE.CountryCode%3DAU&hl=en) | Registration/incorporation document; certain unit trusts may use a deed of incorporation; ABN is also listed. Government bodies may use official letterhead when business documents are unavailable. | Australian government photo ID plus matching name/address proof issued within 90 days; also applies to Norfolk Island. |
| [United States](https://support.google.com/android-developer-console/answer/16501669?co=GENIE.CountryCode%3DUS&hl=en) | IRS organization documents, state incorporation, SEC filings, or business credit reports; representative submits government photo ID. | U.S. government photo ID; address proof must match name and address and be issued within 90 days. |
| [India](https://support.google.com/android-developer-console/answer/16501669?co=GENIE.CountryCode%3DIN&hl=en) | Articles, incorporation, GST, partnership/trust/society documents, and CIN are listed; representative submits government photo ID. | Indian passport, driving licence, voter ID, or PAN plus address proof. This view does not state a general 90-day window; do not infer one from other regions. |
| [France](https://support.google.com/android-developer-console/answer/16501669?co=GENIE.CountryCode%3DFR&hl=en) | Registration, commercial-register extract, or VAT document; the source unexpectedly says “advertiser verification,” inconsistent with its Android developer-verification heading. Confirm against the current Console task. | Individual ID must be issued in an EEA country or Switzerland. The rules also cover French Guiana, Guadeloupe, Martinique, Mayotte, and Réunion. The page does not state a 90-day address-proof limit. |
| [South Korea](https://support.google.com/android-developer-console/answer/16501669?co=GENIE.CountryCode%3DKR&hl=en) | Business registration; government departments may submit an official letter with full name, address, and date. | Individuals and organization representatives verify through a mobile carrier; individual address proof must match the payments profile and be issued within 90 days. |

The [Play Console identity-document page](https://support.google.com/googleplay/android-developer/answer/15633622) describes a separate verification workflow. Although some document rules are similar, do not import an age-of-document rule omitted from an ADC region page or infer that a government exception in one workflow applies to the other.

## Child links and coverage status

This topic separately records the identity article, account type, required information, country documents, Full/Limited plans, package registration, certificate fingerprints, identity updates, user access, onboarding, verification FAQ, public support form, and ADC ToS. Help Center sidebars are audited separately from article-body links. For organization website verification, the relevant Search Console descendants reviewed were [Associations](https://support.google.com/webmasters/answer/9419894), [adding a site](https://support.google.com/webmasters/answer/34592), [site ownership verification](https://support.google.com/webmasters/answer/9008080), and [owners and permissions](https://support.google.com/webmasters/answer/7687615).

Search Console technical methods, Help sidebars, sign-in/Console-only pages, interactive D&B lookup, and deeper technical examples have not been recursively exhausted. The public identity-support form was reviewed for fields and its English-only response note but **was not filled out or submitted**. Access and coverage status for each URL is in the source audit ledger (snapshot: `source-page-audit.csv`, not imported in this repository) and recursive link graph (snapshot: `google-play-policy-link-graph-en.md`, not imported in this repository).

## Source links

- [Verify your Android developer identity information](https://support.google.com/android-developer-console/answer/16641416)
- [Required information to create an Android Developer Console account](https://support.google.com/android-developer-console/answer/16640818)
- [Choose an account type](https://support.google.com/android-developer-console/answer/16641046) · [Choose a distribution plan](https://support.google.com/android-developer-console/answer/16640817) · [Limited distribution](https://support.google.com/android-developer-console/answer/17131204)
- [Get started with ADC](https://support.google.com/android-developer-console/answer/16604405) · [Update identity details](https://support.google.com/android-developer-console/answer/16641334) · [Add users](https://support.google.com/android-developer-console/answer/16642750)
- [Android developer verification FAQ](https://support.google.com/android-developer-console/answer/16561738) · [Regional documents](https://support.google.com/android-developer-console/answer/16501669)
- [ADC Terms of Service](https://developer.android.com/developer-verification/console/terms)
