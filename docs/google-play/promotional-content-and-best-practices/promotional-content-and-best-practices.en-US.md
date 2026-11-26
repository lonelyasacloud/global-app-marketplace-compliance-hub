---
id: google-play.promotional-content-and-best-practices
platform: google-play
language: en-US
authority: operational
status: current
kb_checked_at: 2026-10-23
review_due: 2027-01-23
regions: [global]
topics: [promotional-content, events, featuring, localization, deep-links, content-quality]
snapshot_id: play.promotional-content-and-best-practices
snapshot_package: "GooglePlay-KnowledgeBase-2026-10-24-review.zip"
coverage_status: "detailed-summary"
source_url_directory: "https://support.google.com/googleplay/android-developer/topic/12932623"
source_url_understand: "https://support.google.com/googleplay/android-developer/answer/12929029"
source_url_create: "https://support.google.com/googleplay/android-developer/answer/12932541"
source_url_quality: "https://support.google.com/googleplay/android-developer/answer/12929944"
source_url_review: "https://support.google.com/googleplay/android-developer/answer/12932123"
source_url_dates: "https://support.google.com/googleplay/android-developer/answer/12932229"
source_url_performance: "https://support.google.com/googleplay/android-developer/answer/12932124"
source_url_deep_links: "https://support.google.com/googleplay/android-developer/answer/15322603"
source_url_youtube: "https://support.google.com/googleplay/android-developer/answer/15501235"
source_url_animation: "https://support.google.com/googleplay/android-developer/answer/16009268"
source_url_dating: "https://support.google.com/googleplay/android-developer/answer/15678263"
source_url_pdf: "https://services.google.com/fh/files/helpcenter/google_play_promotional_content_guidelines.pdf"
effective_date: "operational promotional-content guidance; no 2027-01-27"
---

# Google Play Promotional Content and Event Asset Best Practices

> **Import note (Google batch 7).** The body is the paraphrased summary from the already separated 2026-10-24 Google Play knowledge-base snapshot (`play.promotional-content-and-best-practices`, reviewed 2026-10-23). It is not a verbatim copy of an official page. The English official source is the source of truth. `kb_checked_at` is the review date recorded in the snapshot source file; this import did not re-open the live official pages. Phrases such as “this knowledge base,” “this library,” and “local topic” describe coverage inside that snapshot, not the set of pages imported into this repository. Relative snapshot links to topics, link graphs, ledgers, or CSVs that are not in this repository are kept as text mentions. Relative links that target the Google batch 1–6 topics or these twelve batch 7 topics point at the hub files. Reviewed 2026-10-23. The English Help bodies were readable, and all ten directory articles were opened. The corresponding `zh-CN` Help pages were not reliably retrievable. The Chinese hub text is an editorial paraphrase, not a verified Google Chinese translation. That retrieval limit is not a policy change. No 2027-01-27 date is recorded. Preview windows, character limits, and reporting ranges are product parameters, not policy effective dates. This page is operational promotional-content guidance. Passing a quality review does not guarantee homepage or search placement. Dating-title quality guidance is a content-quality article, not the real-money gambling policy. Custom audiences remain a separate Console tool and are not a policy exemption. Account-specific Console pages and some API descendants stay partial.

**Reviewed: 2026-10-23.** This topic brings together the ten guides in the Google Play Console Help “Promotional content” directory, the creation workflow, quality review, deep links, animation, YouTube, and performance reporting. These materials primarily describe product eligibility, submission workflows, and content quality. Feature availability depends on app/game type, Premium growth tools eligibility, and account permissions. Passing a quality review does not guarantee placement on the Play homepage or in search.

The English Help bodies were readable. The corresponding `zh-CN` Help pages were not reliably retrievable in this pass, so the Chinese topic is a bilingual paraphrase of the English originals, not a verified Google Chinese translation. All ten directory articles were opened. Account-specific Console pages, support destinations, and some technical/API descendants remain restricted or partial; recursive closure is not claimed.

## Decision points and timing

| Checkpoint | Official guidance | Practical reading |
| --- | --- | --- |
| Availability | Promotional content is available to all games and to apps meeting Premium growth tools eligibility. Featuring, audience targeting, and Promotional Content deep links have their own eligibility restrictions. | Confirm the actual Console access and account eligibility; a public Help page does not prove access has been granted. |
| Earliest submission | Events can be created at any time but may be submitted no earlier than 60 days before their start. | Schedule production and review inside the submission window. |
| Review buffer | The creation page says approval can take up to four days. The quality-review page says review typically takes under 24 hours but recommends submission at least four days before start to allow fixes. | Reserve four days. After an edit/resubmission, the replacement cannot go live earlier than 24 hours after submission. |
| Featuring request | Submit a featuring request at least 14 days before start. Quarterly allocations reset each quarter: games get 4 requests for broad audiences and 2 for specific audiences; apps get up to 6 and 2, respectively. | These are request allocations, not guaranteed placement. Eligibility and approval do not guarantee featuring. |
| Preview | Preview can begin up to 14 days before start; Offers cannot be previewed. | Preview can let users sign up for a launch notification. |
| Event duration | The creation page body says a maximum of four weeks; its FAQ separately says time-limited events must end within 30 days. Major updates are fixed at 28 days; preregistration announcements at one week. | The source has a four-week/30-day boundary discrepancy. Use the more conservative 28-day schedule or confirm the current Console validation instead of treating the values as equivalent. |
| Country/region groups | One event may use different start/end dates for different country groups, but all start dates must fall in the same calendar quarter. Use separate events across quarters; one multi-country event uses one featuring request. | Check each country group's start quarter and split cross-quarter campaigns. |

Read the creation page's quota wording together with its later explanation: **the quota is for featuring requests**. Creating an event without requesting featuring does not use a featuring allocation. A submitted request counts under the stated conditions; multiple country groups share one request. Drafts, cancellations, and failed-quality resubmissions are covered by the page's more specific rules.

## Event types, audiences, and data context

Promotional content types are Offers, time-limited events, and major updates. Offers may be discounts, value-add bundles, limited-time free rewards, or subscription trials. Time-limited events include real-time events, competitions/challenges, and special events. Major updates include new features/announcements, new content, and preregistration updates. Choosing the wrong type can limit eligibility.

Play targeting options include everyone, potential users, churned or lapsed users, buyer-state groups, and custom audiences. Google's definitions say churned users uninstalled the app; lapsed users have not opened it in the last 28 days; lapsed buyers have not purchased in the last 180 days. Buyer-state targeting only supports purchases made through Google Play Billing. For CSV and Grouping API audiences, eligibility, data-source thresholds, and privacy boundaries, see [Custom Audiences and Grouping API](../custom-audiences-and-grouping-api/custom-audiences-and-grouping-api.en-US.md). These targeting tools do not replace the developer's review of actual processing under User Data, Data safety, and applicable law.

## Content quality: make clear what it is, why it matters, and how to participate

### Text and localization

- The required tagline is limited to 80 characters. It should clearly identify the event, update, or offer, without generic slogans or button instructions. For offers, disclose the amount/discount, product scope, minimum purchase threshold, eligibility, and material billing conditions; put the key offer value in the first 40 characters where possible.
- Spotlight has a stricter tagline limit: 48 characters for single-byte languages and 23 for double-byte languages such as Chinese, Japanese, and Korean. A preview does not guarantee placement.
- The required description is limited to 500 characters. Explain the user benefit or selling points, participation, and claim/redemption conditions. Google recommends at least 100 characters. Avoid generic app descriptions and repeated tagline text; use a concise paragraph instead of an ad-like CTA or low-information copy.
- Localize descriptions for the languages of the countries being targeted. Google Play shows events to users whose country/language matches the localization provided. Adapt punctuation, grammar, culture, dates, times, and currency.
- Content should be new, noteworthy, and user-facing. Evergreen service descriptions, routine events, duplicate or very similar assets, or multiple duplicate submissions at the same time may be rejected or receive limited visibility. Events must run in-app at the scheduled time and be easy to find after opening the app.
- The general section also says events must be applicable to all users; if participation is limited by a minimum level, describe it, and the only explicit audience-scope exception named there is a new-user offer. The creation workflow also offers churn/buyer-state and custom-audience targeting. The two pages do not explain how these rules interact in every case, so do not infer that every “specific audience + event” combination is automatically eligible. Check the in-Console eligibility and state participation limits clearly.
- The detailed Help page includes field-specific punctuation, capitalization, HTML, and description rules. A short PDF checklist also advises proper localization and avoiding bullets. Check the current field-specific Help requirements rather than relying only on the summary PDF.

### Images, animation, and video

| Asset | Main specifications and restrictions |
| --- | --- |
| Primary image | JPG or 24-bit PNG; 1920 × 1080, 16:9; required when a video is included. Keep critical subjects in the center safe area: cropping margins are 15% top, 10% on each side, and 20% bottom. No border frame, text, brand logo, store badge, or fake button/toggle. Spotlight primary image should be 1 MB or less. |
| Square image | The creation page requires a square image for some Play surfaces; use the dimensions validated by the current submission form. |
| Animation | Lottie JSON; ≤200 KB, 60 FPS, ≤6 seconds, 16:9; loop seamlessly. Safe-zone margins: 15% top, 20% on each side, 20% bottom. No text, logo, offer copy, fake UI, or Play ranking/award claim. A static image is also required; a fallback image and screen-reader description are recommended. |
| Promotional-event video | Make it specific to the event, landscape, embeddable, and public or unlisted; disable monetization. If a copyright claim can still cause ads, use a different video. Localize visuals, text, and audio. Usually only the first 30 seconds autoplay. |
| YouTube showcase feature | This is a separate Premium growth tools feature for channel/playlist placement, distinct from the event video field. Its Help page requires videos to be public (not private or unlisted), owned by the app/game, non-monetized, copyright-cleared, non-live, and embeddable. Games also have surface-specific recency windows. |

Assets should match the offer/event described in the text and be unique to the submission. Google says missing quality requirements may reduce exposure. All promotional content must also comply with Developer Program Policies on restricted content. It must not contain shocking/gross or sexually explicit material. Featuring may be limited for gambling or other regulated categories, and entertainment gameplay must remain distinct from real-world economic activity. Some finance themes are currently excluded, including investment advice, lending/credit, credit repair, cryptocurrency, and binary options. Dating-app promotional messaging must be inclusive and non-discriminatory rather than excluding groups by age, religion, sexual orientation, ethnicity, race, disability, or similar demographics.

### Offer eligibility

An offer must add value through a monetary discount or incremental goods/services beyond normal purchase/use. The quality guide says an offer **should** represent a discount or incremental value of at least 10%; this is a recommendation, not an explicit hard minimum in the wording reviewed here. State the SKU/category, value, mechanics, and eligible user group. Offers should not be limited to a tiny quantity such as the first 500 buyers; they must be redeemable in the Android app. Cashback must appear in the basket/checkout rather than requiring mail-in or email rebate. Everyday low prices are not genuine time-limited discounts; new-user-only evergreen offers are the stated exception. Offers must comply with local/national law and cannot discount the paid app/game title itself; use Play Console paid-app sales for that.

## Deep links: route the event card to the matching experience

Deep links are optional. If used, the destination should match the event name, description, offer, or update and make participation intuitive. Play supports Android App Links and custom schemes, but not redirect-based or third-party deep-link solutions. On submission, Play checks whether the link is in the app Manifest and whether the URL is broken. An event can have only one deep link; use separate events for different regional destinations. The deep link works when an installed user taps **Open** from the event card; it is not preserved for a new user who taps **Install** and then installs. Significant changes to the existing deep-link structure or intent filters may require event resubmission. See [Promotional Content deep-link guidance](https://support.google.com/googleplay/android-developer/answer/15322603) and the [Android App Links developer guide](https://developer.android.com/training/app-links).

## Review, remediation, and measurement

Each submission receives a multi-language quality review. Content that meets policy but fails quality review may still appear on the app details page, but is not eligible for wider Play surfaces. Common failures include non-compliant or inconsistent copy/assets, poor localization, ineligible offers, unclear event details, policy violations, and the wrong event type. Console shows affected languages and issue status. Scheduled or live events can be edited and resubmitted; the original is canceled and replaced, and the replacement cannot go live sooner than 24 hours after submission. The guidance says resubmission does not consume an additional featuring quota; the original/new request behavior is described in the review page.

Reporting distinguishes unique users from impressions: unique viewers and converters are user counts; conversion actions include Open, Update, and Install. Charts include daily and 28-day rolling views. Multiple events can be compared; at 10 or more events the report only provides aggregated performance. Event-card engagement uplift measures active days over the following 28 days against a holdback group. Featuring uplift measures extra acquisitions from increased store visibility and typically compares a 7–14 day featuring period with a holdback group. These are different outcomes; do not treat correlation or total conversions as causal lift. The official report labels results conclusive, inconclusive, or insufficient under a 95% confidence rule.

## Ten child pages in the official directory

| Directory article | Coverage used here | Review status (2026-10-23) |
| --- | --- | --- |
| [Understand promotional content](https://support.google.com/googleplay/android-developer/answer/12929029) | Feature purpose, surfaces, and boundaries among offers, time-limited events, and major updates. | Full English body opened; body and directory links attempted; account-specific support destination inaccessible. |
| [Content quality guidelines](https://support.google.com/googleplay/android-developer/answer/12929944) | Text, language, image, animation, video, offer, restricted-content, and finance rules. | Full English body opened and key requirements summarized; embedded images and account-only side resources not all retrievable. |
| [Dating-title quality guidance](https://support.google.com/googleplay/android-developer/answer/15678263) | Inclusive, non-discriminatory promotional messaging for dating apps. | Full English body opened; remaining links are repeated directory/support links. |
| [Create promotional content](https://support.google.com/googleplay/android-developer/answer/12932541) | Submission timing, type, country/date, audiences, featuring allocation, assets, CSV, and no-edit-after-submit rule. | Full English body opened; visible body links checked individually or cross-referenced below; Console requires sign-in. |
| [Track and fix quality issues](https://support.google.com/googleplay/android-developer/answer/12932123) | Review, failure causes, edit/resubmit, localization, and common fixes. | Full English body opened; the five-page [official PDF checklist](https://services.google.com/fh/files/helpcenter/google_play_promotional_content_guidelines.pdf) was read. Console/support are gated; the Developer Program Policy target timed out. |
| [View your events](https://support.google.com/googleplay/android-developer/answer/12932229) | Draft, scheduled, live, stopped, and expired states; view, copy, preview, stop. | Full English body opened; performance and quality pages opened; Console actions require account access. |
| [Evaluate performance](https://support.google.com/googleplay/android-developer/answer/12932124) | Event metrics, acquisition and engagement uplift, report filters/exports. | Full English body opened; Console/Cloud Storage exports require account/project access; developer-guide descendants are not all expanded. |
| [Add deep links](https://support.google.com/googleplay/android-developer/answer/15322603) | Supported types, redirect limits, install behavior, one-link limit, validation. | Full English body opened; Android App Links and custom-scheme targets are readable; Console deep-link management is gated. |
| [Showcase YouTube videos](https://support.google.com/googleplay/android-developer/answer/15501235) | Separate channel/playlist showcase, permission, visibility, monetization/copyright, and metrics. | Full English body opened; YouTube Analytics target identified; Console submission and account metrics are gated. |
| [Animated asset guidelines](https://support.google.com/googleplay/android-developer/answer/16009268) | Lottie specifications, safe zones, text limits, accessibility, and visual recommendations. | Full English body opened; restricted-content and general quality guidance opened/cross-checked; community/support routes failed or are gated. |

## Link-audit boundary

The Help directory is open and all 10/10 child article bodies have been opened. The creation page's Premium growth tools, custom-audience, deep-link, store-listing, content-quality/asset, and Console links are cross-referenced to this KB. Repeated Help sidebars on the review, performance, YouTube, and animation pages are directory navigation and are not counted as new unique targets on each occurrence. High-value grandchildren (the PDF, dating-specific guidance, performance measurement, and YouTube showcase) are summarized. Play Console, support, Cloud Storage, and account settings require sign-in; external API, YouTube/cloud-export technical trees, generic navigation outside the Help sidebar, all image attachments, and their descendants were not fully traversed. Extracted visible body URLs and image/script resources are not the same audit scope.

Feature access, featuring, country/language visibility, and account permissions must be checked in the developer's own Console. This topic is not a compliance verdict or a guarantee of featuring.
