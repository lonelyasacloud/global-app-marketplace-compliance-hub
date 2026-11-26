---
id: google-play.us-external-content-links
platform: google-play
language: en-US
authority: operational
status: current
kb_checked_at: 2026-10-22
review_due: 2027-01-22
regions: [US]
topics: [us, external-content-links, billing, transaction-reporting, service-fees]
snapshot_id: play.us-external-content-links
snapshot_package: "GooglePlay-KnowledgeBase-2026-10-24-review.zip"
coverage_status: "detailed-summary"
source_url: "https://support.google.com/googleplay/android-developer/answer/16470497?hl=en"
source_url_zh: "https://support.google.com/googleplay/android-developer/answer/16470497?hl=zh-CN"
source_url_us_policy_update: "https://support.google.com/googleplay/android-developer/answer/15582165?hl=en"
source_url_play_policy_center: "https://play.google/developer-content-policy/"
source_url_alternative_billing_apis: "https://developer.android.com/google/play/billing/alternative"
source_url_api_overview: "https://developer.android.com/google/play/billing/externalcontentlinks"
source_url_billing_release_notes: "https://developer.android.com/google/play/billing/release-notes"
source_url_in_app_integration: "https://developer.android.com/google/play/billing/externalcontentlinks/integration"
source_url_backend_integration: "https://developer.android.com/google/play/billing/outside-gpb-backend"
source_url_external_transactions_api: "https://developers.google.com/android-publisher/api-ref/rest/v3/externaltransactions"
source_url_external_links_form: "https://support.google.com/googleplay/android-developer/contact/external_content_links"
source_url_program_terms: "https://support.google.com/googleplay/android-developer/answer/16471405"
source_url_external_offers_eea: "https://support.google.com/googleplay/android-developer/answer/14372887?hl=en"
effective_date: "ECL terms effective 2025-12-09; other qualifying transactions from 2026-10-01; successful-download reporting deadline 2026-12-01 kept separate from 2027-01-27"
---

# Google Play External Content Links program for the US

> **Import note (Google batch 6).** The body is the paraphrased summary from the already separated 2026-10-24 Google Play knowledge-base snapshot (`play.us-external-content-links`, reviewed 2026-10-22). It is not a verbatim copy of an official page. The English official source is the source of truth. `kb_checked_at` is the review date recorded in the snapshot source file; this import did not re-open the live official pages. Phrases such as “this knowledge base,” “this library,” and “local topic” describe coverage inside that snapshot, not the set of pages imported into this repository. Relative snapshot links to topics, link graphs, ledgers, or CSVs that are not in this repository are kept as text mentions. Relative links that target the Google batch 1–5 topics or these nine batch 6 topics point at the hub files. Reviewed 2026-10-22. The Chinese source file records `hl=zh-CN` as `source_url` and also records the English URL. The English file records both. The Chinese closing line cites the English ECL page as the official source and calls the Chinese text a structured summary. The snapshot does not record a line-by-line check of the `hl=zh-CN` page and does not record a failed fetch of that route. The ECL Developer Terms took effect on 2025-12-09. The English version controls, and translations are for reference only. Reporting and fees for qualifying transactions other than successful downloads began 2026-10-01. The deadline to report successful app-download events and pay the related fees is 2026-12-01. That download-reporting extension does not defer the 2026-10-01 start for other qualifying transactions. Neither date is a 2027-01-27 preview. No 2027-01-27 date is recorded. The March 4, 2026 settlement request does not, on this snapshot, replace current program terms. This page is operational program guidance. Android billing APIs are implementation notes. US ECL, US alternative billing, and EEA External Offers stay separate. The captured fee table did not reliably align three column headings with two extracted percentages, so this page does not infer which percentage belongs to which column.**

**Reviewed October 22, 2026.** This page separates the US External Content Links (ECL) program terms from Android/Play Billing implementation guidance. ECL is an optional program for eligible, approved Play apps serving users in the US and its territories. It allows links to off-app digital-content purchases or app downloads not managed by Google Play; it is not a worldwide permission for off-Play links and does not replace regional program eligibility elsewhere.

## 1. Scope, markets, and legal context

- Eligibility is limited to **mobile or tablet apps and games serving users in the US and its territories**. Developers may be based elsewhere, but ECL links may only serve US and territorial users. Both games and other apps may apply; no enrollment is needed if the developer does not use external content links.
- Links may lead to off-app purchases of in-app digital goods or services, or to app downloads whose installation and updates are not managed by Google Play. Purchase links may be used alongside Play Billing or in lieu of it, subject to the program terms.
- Before use, developers must complete enrollment and obtain approval for the Play app and any linked external apps. If Play Billing is offered alongside ECL, **all users must continue to have consistent and reliable access to Play Billing**.
- The program is connected to a US court order, and Google reserves the right to modify or terminate it if the order changes or ends. Google's [US policy update](https://support.google.com/googleplay/android-developer/answer/15582165?hl=en) records that Google and Epic reached a new settlement on March 4, 2026 and asked the court to approve a revised injunction. As of this review, Google says current policies and programs remain in effect. Check both the latest court status and program terms.
- US ECL and US alternative billing may be used together if each program's eligibility, enrollment, and implementation requirements are independently met. EEA External Offers is a separate program; do not carry US eligibility, rates, or API assumptions into the EEA.

### ECL has separate Developer Terms of Service

The [External Content Links Developer Terms of Service](https://support.google.com/googleplay/android-developer/answer/16471405) took effect on **December 9, 2025**. It supplements, but does not replace, the [Developer Distribution Agreement](https://play.google.com/about/developer-distribution-agreement.html); if the two conflict regarding ECL participation, the ECL-specific terms prevail. The English version controls, and translations are for reference only. The terms say that their reporting, service-fee, payment, and audit sections apply when Google applies a service fee under the program; the program is now charging the relevant fees.

- The developer contracts directly with users for external transactions and is responsible for required disclosures, receipts/invoices, transaction taxes, product delivery, and support. Google is not the merchant of record, does not process the user's payment, and does not manage distribution of the external app.
- Google invoices monthly service fees and taxes, using commercially reasonable efforts to issue the invoice within 15 calendar days after month-end. Payment is due on the 30th calendar day from the invoice date. Late amounts may bear 1.5% monthly interest (or a lower legal maximum); the terms also allow offsets where applicable.
- The developer is responsible for taxes on external transactions and required tax documents. The terms also cover audit rights, representations and warranties, termination for breach, notice of term changes, and program exit. Continued participation can constitute acceptance of a change; the terms state that ceasing participation is the remedy if the developer does not agree.
- The terms define ECL external transactions, linked external apps, and each party's role. They make the developer responsible for user complaints, unauthorized-transaction disputes, refunds, and local-law obligations, alongside the program Help page's reporting and user-protection rules.

## 2. Destinations and user safeguards

### Digital-content purchase links

- A purchase destination may open in a browser, WebView, or another app store already installed on the user's device.
- Before linking out, the app must explain the destination and its purpose. The actual landing page must match the destination presented to the user; it must not mislead or use false information to induce a linkout.
- External URLs must not expose personally identifiable information without sufficient security or encryption.

### App-download links

Download links may open a browser or another app store already installed on the device. The destination may offer only apps approved for ECL. It must also:

1. Have distribution rights and clearly display the app name, icon, description, version number, download size, and developer information.
2. Install each app only with the user's knowledge and explicit action through a clearly labeled, visible UI control.
3. Provide direct, public, easy-to-find customer support and a user-data policy.
4. Comply with applicable local laws, regulations, and ordinances.

The program also requires Play apps and linked external apps to follow applicable Play Developer Policies; only policies that do not apply to a linked app (for example, some payment policies) are excepted. The app must use the API to surface Play's information screen and enable parental controls. Developers must provide customer support for off-Play transactions/downloads, a process for unauthorized-transaction disputes, and refund methods unless non-refundability was clearly disclosed before purchase.

## 3. Enrollment and review of external app downloads

Complete these steps before showing a link:

1. Check eligibility and destination requirements, submit the [External Content Links declaration form](https://support.google.com/googleplay/android-developer/contact/external_content_links), and complete any onboarding required by Google's support team.
2. Integrate the external links APIs in the app.
3. Select the Play apps participating in the program in Play Console under **Settings → External content links**.
4. If linking to app downloads, register all versions of each external app in Console under **Settings → Register external apps**. Review may take up to 7 days or longer in exceptional cases.
5. In **Monitor and improve → Policy and programs → App content → External apps declaration**, enter the successfully registered package name, every user-facing landing-page URL, and every APK download URL. All external apps available on the destination page must be registered.
6. After every external-app or APK update, submit the updated versions and wait for approval before linking users to them.

The declaration form, Console settings, external-app registration, Publishing overview, and Policy status expose account-specific state. Public pages cannot confirm whether a particular package is enrolled, approved, or awaiting action.

## 4. Reporting dates and fees

### Deadline scope

- Transaction reporting and the relevant Play service fees for US ECL participants start **October 1, 2026**.
- The deadline to report successful app-download events and pay the related fees has been extended to **December 1, 2026**. This extension specifically covers successful downloads; it does not defer reporting and fees for other qualifying transactions from October 1, 2026.
- The program FAQ requires reporting all transactions completed after an external link, including $0 free trials, new purchases, rentals, renewals, top-ups, upgrades, and downgrades.

### 24-hour attribution window and fee snapshot

Fees apply when a qualifying transaction or app install outside the app occurs within 24 hours after a user follows an ECL link. A US user's install is “new” if their first Play install or first Play update of the app occurred on or after June 30, 2026; an earlier date is an “existing install.”

The official Help body shows three fee-column headings for in-app digital offers—“Recurring subscriptions / All other offers (new installs) / All other offers (existing installs)”—but the text extraction returns only two percentages per row. The three-column mapping cannot be established reliably from the extracted text, so this page preserves the visible values without assigning them to columns. For account-level calculations, open the [official ECL fee table](https://support.google.com/googleplay/android-developer/answer/16470497?hl=en) and the developer Console.

| Official table row | Percentages visible in extracted text | Column mapping |
| --- | --- | --- |
| First $1M in annual earnings | 10%, 10% | One of the three column values is not explicit in the extracted text; check the live table and account terms |
| Standard service fees | 10%, 20% | Same limitation |
| Play Games Level Up or Apps Experience participants | 10%, 15% | Same limitation |

App downloads have a separate fixed per-install fee, subject to periodic adjustment. On October 22, 2026, the official page listed **$3.65 per game install** and **$2.85 per app install**; the installed app category must also be declared in reporting.

**Do not double-charge the download and later purchase path:** when the initial Play-app linkout is for an external app download, only the fixed download fee applies. Purchases resulting from that initial download link do not incur a transaction service fee even within 24 hours. A later, independent purchase linkout from a Play app is assessed separately.

## 5. Android client integration

The current [in-app integration guide](https://developer.android.com/google/play/billing/externalcontentlinks/integration) requires Play Billing Library **8.2.1 or higher**. This is a technical prerequisite, not a grant of program eligibility or enrollment approval.

| Step | Client implementation | Compliance significance / common mistake |
| --- | --- | --- |
| Initialize | Call `enableBillingProgram()` with `BillingProgram.EXTERNAL_CONTENT_LINK`; this flow does not need a `PurchasesUpdatedListener`. | Do not treat the ordinary Play Billing purchase listener as the ECL flow. |
| Check availability | After connecting to Play, call `isBillingProgramAvailableAsync()`; proceed only when it returns `BillingResponseCode.OK`. | If country, enrollment, or device eligibility fails, do not bypass Play and open the external page directly. |
| Generate a token | Call `createBillingProgramReportingDetailsAsync()` immediately before each linkout to get a new `externalTransactionToken`; never cache or reuse it. | The token ties the linkout to transaction reporting; every linkout needs a new token. |
| Launch the link | Call `launchExternalLink()` with the registered/approved URI, link type, `BillingProgram.EXTERNAL_CONTENT_LINK`, and launch mode. App downloads must use `LAUNCH_IN_EXTERNAL_BROWSER_OR_APP`. | Link only to the destination already shown to the user; download URLs need Console approval. |
| Handle responses | `OK` means Play directed the user outside the app; it **does not mean a purchase occurred**. Handle `BILLING_UNAVAILABLE`, `FEATURE_NOT_SUPPORTED`, `DEVELOPER_ERROR`, `USER_CANCELED`, and retryable network/connection errors appropriately. | Do not infer or fabricate a transaction from a successful redirect callback; the external transaction system must confirm and report it. |
| Test | Use license testers; the guide says test-account transactions are not invoiced to the developer. | Also cover country/device eligibility, cancellation, network retry, and destination-version approval. |

## 6. Backend transaction reporting and refunds

The [Play backend integration guide](https://developer.android.com/google/play/billing/outside-gpb-backend) describes reporting qualifying off-Play transactions through the Google Play Developer API's [`externaltransactions` resource](https://developers.google.com/android-publisher/api-ref/rest/v3/externaltransactions). The guide serves several regional billing/link programs, so eligibility and timing remain controlled by the US ECL terms.

- Report all qualifying transactions under the applicable program, including zero-value free trials, initial purchases, renewals, top-ups, upgrades/downgrades, and app-download events. Reporting is accepted only for eligible program/country combinations; otherwise the API rejects the request.
- Initial purchases, one-time purchases, and app downloads require the client-provided `externalTransactionToken`. Each report uses a developer-generated unique `externalTransactionId`; do not include personal, proprietary, or confidential data in the ID.
- Later renewals/top-ups use a new transaction ID and reference the initial one with `initialExternalTransactionId`. A product change, or a repurchase after cancellation/expiration, starts a new transaction chain.
- Report refunds against the exact previously reported transaction ID. A subscription refund must identify the specific recurrence; partial refunds require the pre-tax refunded amount.
- `createexternaltransaction` and `refundexternaltransaction` have an additional limit of 1,200 calls per minute; `getexternaltransaction` does not count against that additional limit. General Developer API quotas also apply.
- The backend guide's `ExternalOfferDetails` and `appDownloadEventExternalTransactionId` examples are for EEA External Offers. This pass checked the Developer API schema: US ECL uses the mutually exclusive `externalContentLinkDetails`; an app download uses `LINK_TO_APP_DOWNLOAD` and requires the external app package/category. The EEA `appDownloadEventExternalTransactionId` field is not part of the US ECL object. No end-to-end US download amount example was found, so the EEA sample is not used to infer one.

### US ECL ExternalTransaction API fields (reviewed October 24, 2026)

The Google Play Developer API [`externaltransactions` REST resource](https://developers.google.com/android-publisher/api-ref/rest/v3/externaltransactions), marked updated September 28, 2026, models ECL and EEA External Offers as different, mutually exclusive detail objects: an ExternalTransaction can set at most one of `externalContentLinkDetails` or `externalOfferDetails`.

- US ECL uses `externalContentLinkDetails`. Its `linkType` is required and can be `LINK_TO_DIGITAL_CONTENT_OFFER` or `LINK_TO_APP_DOWNLOAD`. For an app install, `installedAppPackage` and `externalAppCategory` are also required. The category is `APP` or `GAME` and must match the category submitted during external-app verification in Play Console.
- EEA External Offers uses the separate `externalOfferDetails`, `ExternalOfferLinkType`, and `installedAppCategory` fields. `appDownloadEventExternalTransactionId` belongs to EEA `ExternalOfferDetails`; it is not part of US ECL's `ExternalContentLinkDetails`. Do not copy an EEA backend example into a US request.
- The create method requires an `externalTransactionId` unique within the app, 1–63 characters, using ASCII letters, digits, underscores, or hyphens; it must not contain PII. Requests use the `androidpublisher` OAuth scope. Common required transaction fields include original pre-tax amount, original tax amount, transaction time, user tax address, and a one-time or recurring transaction object. The one-time transaction token comes from the client external-link flow.
- The get method retrieves a transaction by `applications/{packageName}/externalTransactions/{externalTransactionId}` and has no request body. The refund method POSTs to the transaction resource name and requires `refundTime` plus exactly one of `fullRefund` or `partialRefund`; a partial refund requires a per-transaction unique `refundId` and an amount below the remaining pre-tax amount.
- US ECL Help requires qualifying app installs to be tracked and says the app-download category is reported. The deadline for successful-download reporting and related fees is **December 1, 2026**; reporting/fees for other qualifying transactions began **October 1, 2026**. The API resource lists the fields but has no end-to-end US download example that establishes how to populate the monetary amount. This topic therefore does not infer a zero amount from the EEA example or infer a US ECL field for linking later transactions inside the downloaded app.

Method pages opened individually: [createexternaltransaction](https://developers.google.com/android-publisher/api-ref/rest/v3/externaltransactions/createexternaltransaction) · [getexternaltransaction](https://developers.google.com/android-publisher/api-ref/rest/v3/externaltransactions/getexternaltransaction) · [refundexternaltransaction](https://developers.google.com/android-publisher/api-ref/rest/v3/externaltransactions/refundexternaltransaction). The methods and key ECL types were reviewed; Price, all other API type members, complete request samples, and account-specific requirements have not all been traversed.

## 7. Direct policy links and their child pages

“Direct body links” means pages linked from the ECL article body, such as policy, implementation, and enrollment pages. The Help Center's “Tax, compliance & regional requirements” rail is site navigation and is tracked separately from ECL requirements. For account entry points, only public instructions were reviewed; no developer-specific state can be inferred.

| Source page / direct target | Relationship to ECL and review status |
| --- | --- |
| The “US policy update” and “District Court order” links in the ECL Help body → the same [US policy update](https://support.google.com/googleplay/android-developer/answer/15582165?hl=en) → [2024 permanent-injunction PDF](https://storage.googleapis.com/gweb-uniblog-publish-prod/documents/2024.10.07_Dkt._1017_Permanent_Injunction.pdf) | Both ECL Help anchors resolve to the same update page; the PDF is one level below that page, not a direct ECL Help link. Both pages were opened and summarized in the US policy branch. The update records the March 4, 2026 request for a revised injunction, the July 22 fee/reporting start notice, and the September 17 download-deadline update. The order and program terms may change. |
| [Developer Policy Center](https://play.google/developer-content-policy/); [Payments policy](https://support.google.com/googleplay/android-developer/answer/9858738?hl=en) | The Policy Center body was opened; individual policies are covered in other bilingual topics. Play apps and linked external apps must comply with applicable policies. The exception for policies that do not apply to a linked app does not create a general payment exemption for the main Play app. Payments is summarized separately. |
| [External Content Links API overview](https://developer.android.com/google/play/billing/externalcontentlinks) → [Play Billing Library release notes](https://developer.android.com/google/play/billing/release-notes) → [in-app integration guide](https://developer.android.com/google/play/billing/externalcontentlinks/integration) → [backend guide](https://developer.android.com/google/play/billing/outside-gpb-backend) | All bodies opened. Release notes show that PBL 8.2.0 introduced ECL APIs and 8.2.1 fixed availability/token-method bugs; the current release-notes page also lists 9.1.0. The ECL-specific guide sets the minimum at 8.2.1+. The overview confirms US scope and Console approval for external downloads; the client guide covers eligibility, tokens, linkouts, and errors; backend guidance covers IDs, zero-value events, renewals/refunds, and quotas. API method types and all sample descendants remain incomplete. |
| [External Content Links declaration form](https://support.google.com/googleplay/android-developer/contact/external_content_links) → [ECL Developer Terms of Service](https://support.google.com/googleplay/android-developer/answer/16471405) → [DDA](https://play.google.com/about/developer-distribution-agreement.html) | Form and full ECL terms opened. The form asks for developer-account ID, registered entity/address, package names, billing address/company-domain invoice email, contact, working user-support details, PCI DSS or non-card-handling confirmation, an unauthorized-transaction dispute path, and authority to sign for the entity. The ECL terms took effect December 9, 2025 and supplement the DDA; monthly invoicing, 30-day payment, transaction taxes, direct developer-user responsibility, audit, and exit terms are summarized above. |
| ECL terms → [Enforcement Process](https://support.google.com/googleplay/android-developer/answer/9899234), [exit/billing-and-link-program support form](https://support.google.com/googleplay/android-developer/contact/billing_and_linkouts_program_q) | The Enforcement Process click timed out; enforcement has a separate topic. The exit form opened but redirected to the general alternative-billing/link-out support form; account ID, package name, and issue details are requested, and submitting requires account access. |
| [How Google Play Works](https://google.play/howplayworks/), linked as fee context; FAQ and destination requirements | Overview opened. Fee table and FAQ are within the main ECL Help page; this topic summarizes its 24-hour window, install fee, and post-download transaction rule. |
| ECL Help → [Alternative billing APIs](https://developer.android.com/google/play/billing/alternative) | Opened; it describes User Choice/alternative billing APIs and information/choice screens. Its PBL 5.2/6.2.1 version requirements apply to alternative billing, not ECL. Use the [dedicated ECL integration guide](https://developer.android.com/google/play/billing/externalcontentlinks/integration) for ECL's current PBL 8.2.1+ minimum. |
| ECL Help → [Play Console](https://play.google.com/console/developers) | Clicking it redirects to a public Google Play for business landing page and reveals no developer account state; the Settings/App content steps still require Console sign-in. |
| ECL Help → Help Community and [Contact us](https://support.google.com/googleplay/android-developer/contact/billing_and_linkouts_program_q) | The Help Community click returned an internal error without a stable target URL. Contact us resolves to a multi-program support form whose submission requires account details. |
| [EEA External Offers](https://support.google.com/googleplay/android-developer/answer/14372887?hl=en) | Opened and summarized separately in [Payments, billing, and subscriptions](../payments/payments-and-subscriptions.en-US.md); it is a regional comparison only, not a source for US rules. |
| API descendants: Play Billing 8 migration, `BillingClient`, `LaunchExternalLinkParams`, license testing, the [`externaltransactions` resource](https://developers.google.com/android-publisher/api-ref/rest/v3/externaltransactions), and its [create](https://developers.google.com/android-publisher/api-ref/rest/v3/externaltransactions/createexternaltransaction), [get](https://developers.google.com/android-publisher/api-ref/rest/v3/externaltransactions/getexternaltransaction), and [refund](https://developers.google.com/android-publisher/api-ref/rest/v3/externaltransactions/refundexternaltransaction) methods | The resource and all three method pages were opened. Added the mutually exclusive US `externalContentLinkDetails` / EEA `externalOfferDetails` distinction, app-download package/category conditions, create ID/OAuth constraints, and get/refund request shapes. Other API type members, all code samples, and generated-client descendants remain unreviewed page by page; see the source-link audit register (snapshot: `../source-page-audit.csv`, not imported in this repository). |
| Release notes → [Android skills overview](https://developer.android.com/tools/agents/android-skills) and [Android CLI overview](https://developer.android.com/tools/agents/android-cli) | Both opened. They describe optional Android developer tooling and skill installation, not additional Play ECL requirements. The release notes' Billing upgrade skill may help maintain a client implementation if the team chooses to use it. |
| The ECL Help page's 16 regional/tax sidebar links and Android Developers header/footer links | These are navigation, not ECL body requirements. The ledger retains their URLs and access states, but this pass did not open every sidebar target and its descendants. |

**Recursive boundary:** The ECL terms, API overview, core client/backend guides, declaration form, US update, and API resource were opened. Pages that affect eligibility, user flow, reporting, refunds, and fees are summarized above. Play Billing types, every code sample, every Developer API schema field, and all descendants of the 16 regional sidebar links are not fully closed; the source ledger records per-URL access state, so this does not claim to exhaust the entire Google Play link graph.

## 8. Related knowledge-base pages

- [Payments, billing, and subscriptions](../payments/payments-and-subscriptions.en-US.md) · [中文](../payments/payments-and-subscriptions.zh-CN.md)
- Recursive policy-link graph (snapshot: `../google-play-policy-link-graph-en.md`, not imported in this repository)
- Policy deadlines register ([policy operations register](../google-play-policy-operations/google-play-policy-operations.en-US.md))

Official sources: [US ECL program terms](https://support.google.com/googleplay/android-developer/answer/16470497?hl=en) · [in-app integration](https://developer.android.com/google/play/billing/externalcontentlinks/integration) · [backend reporting](https://developer.android.com/google/play/billing/outside-gpb-backend). This is a structured summary, not a verbatim copy of the official material. Recheck the live official pages before launch or fee calculations; fees, account eligibility, court status, and Console enrollment can change.
