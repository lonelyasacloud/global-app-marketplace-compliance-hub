---
id: google-play.families-self-certified-ads-program
platform: google-play
language: en-US
authority: operational
status: current
kb_checked_at: 2026-10-24
review_due: 2027-01-24
regions: [global]
topics: [families, child-directed-ads, self-certified-sdk, mediation, sdk]
snapshot_id: play.families-self-certified-ads-program
snapshot_package: "GooglePlay-KnowledgeBase-2026-10-24-review.zip"
coverage_status: "detailed-summary"
source_url: "https://support.google.com/googleplay/android-developer/answer/9900633?hl=en"
source_url_zh: "https://support.google.com/googleplay/android-developer/answer/9900633?hl=zh-Hans"
effective_date: "current-snapshot"
---

# Google Play Families Self-Certified Ads SDK Program

> **Import note (Google batch 3).** The body is the paraphrased summary from the already separated 2026-10-24 Google Play knowledge-base snapshot (`play.families-self-certified-ads-program`, reviewed 2026-10-24). It is not a verbatim copy of an official page. The English official source is the source of truth. `kb_checked_at` is the review date recorded in the snapshot source file; this import did not re-open the live official pages. Phrases such as “this knowledge base,” “this library,” and “local topic” describe coverage inside that snapshot, not the set of pages imported into this repository. Relative snapshot links to topics, link graphs, ledgers, or CSVs that are not in this repository are kept as text mentions. Relative links that target the Google batch 1 and 2 topics or these nine batch 3 topics point at the hub files. On 2026-10-24 the snapshot reopened the English and `zh-Hans` program pages. The Chinese direct fetch of the watermark and test-app article returned Internal Error; the English body of that article was opened. That failure is not a policy change. The program page says new applications are paused and that the reopen time will be announced on that page. The snapshot records no reopen date, and the pause is not a prediction that applications will reopen. Current participants’ requirements are recorded as unchanged. Older wording about reapplying after three months is not evidence that an application window is open. These program requirements are `operational` and apply when an ads SDK serves ads to children. They do not replace the Families policy, User Data, or the publisher’s own responsibility. Vendor and SDK version tables stay in the unimported third-party SDK snapshot topic and are not copied here.

**Reviewed October 24, 2026.** This topic brings together the program overview, applicability, SDK-provider duties, publisher checks, and every body link on the overview page. It is a bilingual paraphrase and navigation aid, not Google's full text. It links to the existing vendor/version audit instead of duplicating it. On October 24, reopened the English and `zh-Hans` program pages, the English SDK policy, the current version list, and the Policy Deadlines table: new applications remain paused, current participants' requirements remain unchanged, and the live list still has 14 Maven rows across 13 distinct vendor destinations. The October 23 offline version table showed no change; it is not proof of release-time eligibility.

## Current status and applicability

The program overview currently says **new applications are paused; Google will announce when the application window reopens and publish updated guidance there. Existing participants remain subject to the current program requirements.** This is a snapshot verified October 23, 2026, not a forecast or a known reopening date.

The current self-certified SDK/version requirement applies when an app uses an ads SDK to serve ads **to children**. If the app targets both children and older users, ads shown to children must come exclusively from a self-certified SDK version; the overview gives neutral age screening as an example. The declared audience, actual content, SDK initialization, and ad-request paths should agree.

The page lists two cases that do not require the ads SDK's self-certification:

1. In-house advertising: an SDK manages cross-promotion of the developer's apps, other owned media, or merchandising.
2. A direct advertiser deal in which an SDK is used only for inventory management.

These exceptions cover **SDK self-certification only**. Developers remain responsible for ad content and data collection, and must still follow the [User Data policy](https://support.google.com/googleplay/android-developer/answer/10144311?hl=en), [Families policy](https://support.google.com/googleplay/android-developer/answer/9893335?hl=en), and applicable law. Google says it does not represent or guarantee the accuracy of information SDK providers submit during self-certification; certification does not transfer responsibility away from the app developer.

## Requirements for SDK providers

| Area | Verifiable program requirement | Publisher/integrator check |
| --- | --- | --- |
| Prohibited content and terms | Define and prohibit objectionable ad content and behavior in the SDK's terms or policies; definitions should align with Play Developer Program policies. | Review the SDK's content rules and contract boundary; a vendor statement does not replace app-level review. |
| Creative ratings | Provide age-appropriate creative ratings with at least Everyone and Mature groups, aligned with Google's method for applicants. | Check the selected ad slot, creative ratings, and child/all-age inventory configuration. |
| Child-directed treatment | Let publishers request child-directed treatment per request or app, consistent with law; treatment must disable personalized ads, interest-based advertising, and remarketing. | Pass consistent child-treatment signals through every child ad request, mediation path, and bidding path. |
| Ad formats | Offer formats that comply with the [Families Ads and Monetization rules](https://support.google.com/googleplay/android-developer/answer/9893335?hl=en) and Teacher Approved standards. | Review what children actually see, timing, dismissibility, accidental-tap risk, and commercial prompts. |
| Real-time bidding | For ads served to children through real-time bidding, review creatives and propagate privacy indicators to bidders. | Verify each hop in the bidding chain receives and preserves rating/privacy signals. |
| Evidence and version governance | Provide enough information and a test app; respond promptly to later requests; self-certify every new release against the latest policies. | Do not treat historic review of an older release as proof that a newer version is currently certified. |
| Applicable law | Support compliance with child-related laws and regulations that may apply to publishers. | Assess law by market, audience, data, and transaction; the Help page's examples are not an exhaustive legal list. |

### Separate policy for SDK and mediation providers

The [Families Self-Certified Ads SDK Policy](https://support.google.com/googleplay/android-developer/answer/12918983?hl=en) is a separate formal policy page from the program overview. It makes the SDK/mediation provider duties explicit: disclose access to, collection, use, and sharing of children's personal/sensitive data, and limit use to disclosed purposes; do not transmit AAID, SIM Serial, Build Serial, BSSID, MAC, SSID, IMEI, or IMSI from children or users of unknown age; and disable personalized, interest-based, and remarketing ads for child-directed requests. Real-time-bidding creatives must be reviewed, with privacy indicators passed to bidders. Ads must be age-appropriate, distinguishable from app content, and must not deceive, induce accidental clicks, or manipulate children; ads that interrupt normal app/game use must be dismissible after five seconds. Violations can lead to removal or suspension from the program.

SDK providers must also submit English terms of service, privacy policy, and publisher integration guide, plus a test APK using the latest compliant version and full live inventory; respond to later information requests and self-certify new versions against current policy. The third-party SDK requirements topic ([Google Play third-party SDK requirements and safe integration](../sdk-requirements/sdk-requirements.en-US.md)) and graph §4.114 contain the full clauses, direct-link map, and access limits. Certification does not transfer the app publisher's separate data, audience, or ads responsibilities under [User Data](../user-data/user-data.en-US.md) and the [Families policy](../age-restricted-child-safety/age-restricted-child-safety.en-US.md).

### Mediation platforms

For ads to children, a mediation platform must use Families self-certified SDKs **or** implement safeguards sufficient to ensure every mediated ad meets these requirements. It must also pass the ad-content rating and applicable child-directed treatment to mediation platforms. This is not a blanket exemption for every mediation layer merely because one certified SDK is present.

## Certification evidence, watermarks, and test apps

The live [Families Self-Certified Ads SDK list](https://support.google.com/googleplay/android-developer/answer/12955712?hl=en) has 14 Maven rows and 13 distinct vendor destinations. The bilingual third-party SDK topic ([Google Play third-party SDK requirements and safe integration](../sdk-requirements/sdk-requirements.en-US.md)) contains the vendor/version snapshot and discrepancies. The list can change; check the live page before every release or upgrade. An offline snapshot does not prove that a newly released version remains certified.

The [watermark and test-app guide](https://support.google.com/googleplay/android-developer/answer/9536665?hl=en) says:

- A self-certified SDK must use a recognizable mark—such as text, an image, a third-party icon, URL, or redirect page—on **every creative** in its inventory.
- The test app should use the same inventory as the live app or a mirror of it, and be a fully built, executable Android APK for phones.
- Testing should use the latest released or soon-to-be-released policy-compliant SDK and exercise ad retrieval and display.
- The test app should access all live/serving network inventory without geolocation restrictions. For mixed audiences it must distinguish full inventory from child/all-age inventory; it should not restrict testing to selected ads unless a valid neutral age screen controls that selection.
- Providers using only an in-house ads solution are outside this certification process.

The watermark page also retains wording about not reapplying for three months after rejection. The program overview, however, currently says new applications are paused. Do not read the older page's process wording as proof that an application window is open. The form fields are not publicly readable in this review; see the link audit below.

## Every body link on the program overview

The table records the 11 visible body-link occurrences in page order (IDs 3–13). Help Community, Contact, and the Help sidebar are separate navigation chrome and are not counted among these 11. Some old routes redirect; policy meaning below follows the current readable destination.

| Body link | Destination and relationship | Access and boundary |
| --- | --- | --- |
| [Families Policy](https://support.google.com/googleplay/android-developer/answer/9893335) | Parent policy for audience declarations, children's data, SDKs, ads, and app functionality. | Full body opened; cross-reference the [child-safety topic](../age-restricted-child-safety/age-restricted-child-safety.en-US.md). |
| [User Data Policy](https://support.google.com/googleplay/android-developer/answer/9888076) | The overview says developers must still meet User Data disclosure, use, and handling duties. This old URL redirects to the [current article](https://support.google.com/googleplay/android-developer/answer/10144311). | Destination body opened; both old route and current destination are in the URL ledger. |
| [U.S. COPPA](https://www.ftc.gov/tips-advice/business-center/privacy-and-security/children%27s-privacy) | U.S. children's privacy law resource; the program uses it as an example of child-related laws to consider. | Old URL redirects to the FTC's current [Children's Privacy](https://www.ftc.gov/business-guidance/privacy-security/childrens-privacy) portal; applicability depends on the market and processing. |
| [GDPR](https://gdpr.eu/) | GDPR background. The site states it is operated by Proton AG, is not an official EU Commission/Government resource, and is not legal advice. | Followed its official EU link to the [European Commission business guide](https://commission.europa.eu/law/law-topic/data-protection/information-business-and-organisations_en) and six child topics; Article 8 child-data rules, digital-consent age, verification boundaries, and EDPB guidance are now added to External law and reference materials for User Data ([External law and reference materials for User Data](../user-data-policy-references/user-data-policy-references.en-US.md)) and graph §4.120. The EUR-Lex body, national DPA sites, and other statutory/EDPB descendants remain open. |
| [Families Ads and Monetization](https://play.google.com/about/families/ads-monetization/) | Older Google Play Families advertising route; the current readable policy text is in the Families Help article. | When reopened from the SDK policy article on October 23, 2026, this legacy route was observed redirecting to the [current Families policy](https://support.google.com/googleplay/android-developer/answer/9893335), but the fetch tool returned an error while following the redirect. The current target body was opened separately. The old route is not a separate rule. |
| [Teacher Approved course](https://playacademy.exceedlms.com/sl/044a202e) | Play Academy training on ad/IAP standards and avoiding confusing, distracting, manipulative, or excessive commercial behavior for children under 13. | Short link redirects to the [course page](https://playacademy.exceedlms.com/student/path/22151/activity/32755); outline is public, lesson requires sign-in. Training is not policy text. |
| [Legacy interest form](https://docs.google.com/forms/d/e/1FAIpQLSc8msikGDxjTHHFmIECoitMnpudaCbtrb_hhgzpUOznPhDoBw/viewform?p=adnet) | The form says it is deprecated and points to a newer form. | The closed page and new URL were confirmed; new-form fields are inaccessible, and the program is paused, so current eligibility is not inferred. |
| [Self-certify](https://support.google.com/googleplay/android-developer/answer/12253906) | Current click resolves to the [Policy Deadlines table](https://support.google.com/googleplay/android-developer/table/12921780). | Table body opened. Its August 26, 2026 Families row concerns the anonymous-chat age-targeting expansion; it is not an ads SDK certification or reapplication deadline. |
| [Watermark and test-app requirements](https://support.google.com/googleplay/android-developer/answer/9536665) | Creative identification and test APK requirements for SDK self-certification. | English body opened and summarized above. The Chinese direct fetch returned Internal Error. |
| [Families SDK list](https://support.google.com/googleplay/android-developer/answer/9283445) | Older route to the current SDK/version list. | Redirects to the [current list](https://support.google.com/googleplay/android-developer/answer/12955712); the 14 Maven rows and 13 vendor destinations are in the SDK topic. |
| [Share the interest form](https://support.google.com/googleplay/android-developer/?p=adnet) | Help route leads to the same new application form. | Public fetch did not reveal its contents; no fields were inferred from an empty/error response. |

## Practical review sequence

1. Set the target audience accurately in Play Console and make sure the app's actual content fits that audience.
2. Trace every ad request to the final user and identify which SDKs, mediation layers, and bidders serve children, unknown-age users, and older users.
3. For child-directed requests, check the SDK and exact version against the [live list](https://support.google.com/googleplay/android-developer/answer/12955712?hl=en). Verify child-directed treatment, disabled personalized/interest-based/remarketing ads, creative ratings, and mediation signals.
4. Review every child-visible creative, ad format, accidental-tap/obstruction risk, commercial pressure, and IAP prompt. Check the provider's terms, content rating, creative review, and version-notice process.
5. Reconcile SDK data collection, use, and sharing with [User Data](../user-data/user-data.en-US.md), [Data safety](../data-safety/data-safety.en-US.md), the privacy policy, prominent disclosure/consent, and law applicable to the actual distribution markets.
6. Before release, recheck the live list, policy, and account-specific Play Console notices. Repeat the review after an SDK upgrade, vendor change, audience change, or ad-path change.

## Related topics in this library

- Third-party SDK requirements ([Google Play third-party SDK requirements and safe integration](../sdk-requirements/sdk-requirements.en-US.md)): vendors, version coordinates, announcements, and deeper SDK/vendor descendants. This page avoids copying the full vendor table.
- [Age restrictions and child safety](../age-restricted-child-safety/age-restricted-child-safety.en-US.md): parent Families policy, child-visible content, audience, and social-safety rules.
- [User Data](../user-data/user-data.en-US.md) and external legal references ([External law and reference materials for User Data](../user-data-policy-references/user-data-policy-references.en-US.md)): Play data obligations and the distinction between official GDPR guidance and external sources.
- [Payments and subscriptions](../payments/payments-and-subscriptions.en-US.md): the Monetization and Ads Help navigation relationship; this ads program does not change Play Billing or subscription requirements.

Per-URL access states, redirects, and descendant boundaries are in the URL source ledger (snapshot: `../SOURCE_LEDGER-en.md`, not imported in this repository) and bilingual recursive link graph §4.114 (snapshot: `../google-play-policy-link-graph-en.md`, not imported in this repository). This pass covers the readable program body and its important direct targets; it does not claim recursive closure of Help sidebars, the course, forms, vendor pages, GDPR articles, or all external descendants.
