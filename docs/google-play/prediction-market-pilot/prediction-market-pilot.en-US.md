---
id: google-play.prediction-market-pilot
platform: google-play
language: en-US
authority: operational
status: current
kb_checked_at: 2026-10-22
review_due: 2027-01-22
regions: [global]
topics: [prediction-markets, real-money, licensing, pilot, financial-features]
snapshot_id: play.prediction-market-pilot
snapshot_package: "GooglePlay-KnowledgeBase-2026-10-24-review.zip"
coverage_status: "detailed-summary"
source_url: "https://support.google.com/googleplay/android-developer/answer/16902027?hl=en"
source_url_application: "https://support.google.com/googleplay/android-developer/contact/Application_Pilot_Program_for_Prediction_Market_Apps"
effective_date: "pilot; 2026-06-01 deadline for apps already on Play has passed; no recorded end date; no 2027-01-27"
---

# Google Play Prediction Market Real-Money Pilot

> **Import note (Google batch 6).** The body is the paraphrased summary from the already separated 2026-10-24 Google Play knowledge-base snapshot (`play.prediction-market-pilot`, reviewed 2026-10-22). It is not a verbatim copy of an official page. The English official source is the source of truth. `kb_checked_at` is the review date recorded in the snapshot source file; this import did not re-open the live official pages. Phrases such as “this knowledge base,” “this library,” and “local topic” describe coverage inside that snapshot, not the set of pages imported into this repository. Relative snapshot links to topics, link graphs, ledgers, or CSVs that are not in this repository are kept as text mentions. Relative links that target the Google batch 1–5 topics or these nine batch 6 topics point at the hub files. Reviewed 2026-10-22. Both language files cite the English Help page `hl=en`. The snapshot does not record a Chinese official URL or a checked Chinese official pilot page. The Chinese hub text is an editorial paraphrase of the English source. The 2026-06-01 deadline for apps already on Play has passed. The Help page does not state the pilot’s end date. Google may modify, suspend, or terminate it. No 2027-01-27 date is recorded. This pilot is operational program guidance. It does not replace the Real-Money Gambling policy. Apps offered under a gambling or gaming license are excluded from this pilot and follow that policy. A global announcement is not current eligibility for every market. As of this review, the Help page accepted only U.S. financial or equivalent licenses for apps targeting the United States.**

## Current status

The official [prediction-market pilot Help page](https://support.google.com/googleplay/android-developer/answer/16902027?hl=en) was reviewed on October 22, 2026. The April 15, 2026 announcement required apps already on Play that offered real-money prediction-market functions to join and meet the pilot requirements by **June 1, 2026**; that deadline has passed. The current Help page says applications are assessed on a rolling basis during the pilot but does not specify the pilot's duration. Google may modify, suspend, or terminate it. Check the live form and the app's Play Console status before relying on availability.

The announcement described a global pilot. The current Help page narrows the presently accepted scope: as of this review, the program accepts **only U.S. financial or equivalent licenses for apps targeting the United States**; additional countries may be assessed during the pilot. “Global pilot” does not mean every market is currently eligible.

## Scope and routing

| App pattern | Treatment |
| --- | --- |
| Accepts money, cryptocurrency, or another real-world-value asset and offers an exchange or transaction based on an event occurring or not occurring | In scope; real-money prediction-market functionality may be offered on Play only after pilot enrollment. |
| Displays prediction-market information without real-world-value transactions | Outside this pilot's enrollment scope; other Play policies still apply. |
| Uses buttons, navigation, or another call to action to direct users to off-app real-money transactions | Still subject to pilot rules and restrictions; moving the transaction off-app does not by itself create an exemption. |
| Offers prediction markets under a real-money gambling or gaming license | Excluded from this pilot; follow the [Real-Money Gambling, Games, and Contests policy](../real-money-gambling/real-money-gambling.en-US.md) and its separate approval path. |
| Accepts cryptocurrency | Also comply with the [Blockchain-based Content policy](../crypto-assets-and-nfts/crypto-assets-and-nfts.en-US.md) and financial-feature declaration requirements. |

## Enrollment requirements

- **Developer and application:** Use a verified Organization developer account; personal accounts are ineligible. Select “Prediction markets” in the Play Console financial-features declaration, submit the pilot application and license/registration materials, and provide reviewer sign-in details.
- **Licensing and markets:** Submit a valid financial, commodities, or equivalent regulatory license/registration for each target market. U.S. examples include a CFTC-registered Designated Contract Market, an NFA-registered Introducing Broker, or an NFA-registered Futures Commission Merchant. A CFTC No-Action letter addressed to the specific developer/app may serve as certification if it is publicly available in the CFTC database. Target only pilot markets where the app holds a valid license and local law allows it.
- **Age and rating:** Obtain an Adults Only (AO) or equivalent IARC 18+ rating and effectively prevent underage users from using the app. A mixed-content app may need to adjust its overall rating or put prediction-market functions in a separate AO-rated app.
- **Price and responsible use:** The app must be free to download. Show a responsible-use disclaimer in both the app and store listing, and let users set account limits such as deposit, gain, or loss caps, or self-exclusion.
- **Transaction transparency:** The application terms require all fees, contract terms, and settlement rules to be clearly shown before execution. Google Play may immediately remove an app if its license becomes invalid, age/rating controls fail, or it otherwise stops meeting pilot terms.
- **Cross-compliance:** Follow all Developer Program Policies, the Developer Distribution Agreement, applicable law, and the pilot terms. Pilot acceptance does not replace local financial or gambling-law review.

## Announcement body links and target-page relationships

On October 22, 2026, all **11 body-link occurrences across 9 unique targets** on the pilot Help page were handled. The application-form anchor appears twice, as does the Blockchain policy anchor. Generic footer community/contact controls are excluded from this body-link count.

| Direct body target | Relationship, review result, and descendants |
| --- | --- |
| [Prediction Market pilot application form](https://support.google.com/googleplay/android-developer/contact/Application_Pilot_Program_for_Prediction_Market_Apps) | Public fields request an authorized representative, organization/license name, target countries, license type, developer account, package name, and app name. Its terms require limiting real-money features to licensed markets, disclosing fees/terms/settlement before execution, and permit immediate removal for an invalid license, age/rating failures, or other non-compliance. The form says participation becomes binding only after Google accepts the application. It links to Google's [Privacy Policy](https://policies.google.com/privacy?hl=en) and [Terms of Service](https://policies.google.com/terms?hl=en); these are general form terms, not additional Play pilot eligibility rules. The “account and system information” control returned the same form URL in this capture, so no separate target was resolved. |
| [Play Console Financial features declaration](https://play.google.com/console/developers/app/app-content/financial-features) | Pilot declaration entry point. It redirects to sign-in; app-specific declarations and available options are not publicly verifiable. |
| [Requirements for providing sign-in details for review](https://support.google.com/googleplay/android-developer/answer/15748846) | Reviewer credentials must remain reusable, valid, and accessible regardless of user location. Supply them in English; account for reusable OTP/two-step verification access or a static access URL. See [Prepare your app for review](https://support.google.com/googleplay/android-developer/answer/9859455). Maintain the credentials in the Play Console account. |
| [Real-Money Gambling, Games, and Contests](https://support.google.com/googleplay/android-developer/answer/9877032) | Apps using the licensed gambling route must follow that policy and its separate application process; the pilot page explicitly distinguishes the two. See the [gambling topic](../real-money-gambling/real-money-gambling.en-US.md). |
| [Google Play Developer Policy Center](https://play.google/developer-content-policy/) | Directory of 51 policy-topic entry points, inventoried in the policy link graph (snapshot: `../google-play-policy-link-graph-en.md`, not imported in this repository). Descendant status is tracked in the individual topics and source ledger. |
| [Inappropriate Content](https://support.google.com/googleplay/android-developer/answer/9878810) | General policy incorporated by reference in the pilot terms; see the [Inappropriate Content topic](../inappropriate-content/inappropriate-content.en-US.md). |
| [Blockchain-based Content](https://support.google.com/googleplay/android-developer/answer/13607354) | Additional requirements when cryptocurrency is accepted, including financial-feature declarations, tokenized-asset identification, licensing, and NFT gambling limits; see [Crypto assets and NFTs](../crypto-assets-and-nfts/crypto-assets-and-nfts.en-US.md). This anchor appears twice in the source body; both occurrences are counted. |
| [Google Play Developer Distribution Agreement](https://play.google/developer-distribution-agreement.html) | Developer agreement incorporated into the application; see the [bilingual DDA topic](../developer-distribution-agreement/developer-distribution-agreement.en-US.md). |
| [CFTC Staff Letters database](https://www.cftc.gov/LawRegulation/CFTCStaffLetters/letters.htm?field_csl_letter_types_target_id%5B%5D=636) | Dynamic official No-Action letter directory. On October 22, 2026, the filtered list's first visible entry concerned perpetual futures, not prediction-market licensing. Check the exact letter for the named developer/app; a letter merely appearing in the directory does not establish pilot approval. |

## Coverage limits and review reminders

- The Play Console financial-features form requires sign-in. The pilot duration is unspecified and program scope can change.
- The pilot application form links to Google's general Privacy Policy and Terms of Service. Their broad descendants are outside the Play pilot policy tree.
- The 51 Developer Policy Center topics and direct policy targets are represented elsewhere in this library; deep API docs, jurisdictional laws, forms, and sidebar recommendations are not all recursively closed.
- The CFTC No-Action directory changes over time. Each letter has its own scope and conditions; confirm that it specifically covers the developer/app.

## Related topics

- [Real-Money Gambling, Games, and Contests](../real-money-gambling/real-money-gambling.en-US.md) · [Financial services and loans](../financial-services-and-loans/financial-services-and-loans.en-US.md)
- [Crypto assets and NFTs](../crypto-assets-and-nfts/crypto-assets-and-nfts.en-US.md) · [Age restrictions and child safety](../age-restricted-child-safety/age-restricted-child-safety.en-US.md)
- [Play Console requirements](../play-console-requirements/play-console-requirements.en-US.md) · April 15, 2026 announcement and direct links (snapshot: `../google-play-announcement-resources-en.md`, not imported in this repository)
