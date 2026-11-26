---
id: google-play.user-ratings-reviews-installs
platform: google-play
language: en-US
authority: normative
status: current
kb_checked_at: 2026-10-22
review_due: 2027-01-22
regions: [global]
topics: [store-listing, ratings, reviews, installs, ranking, in-app-review]
snapshot_id: play.user-ratings-reviews-installs
snapshot_package: "GooglePlay-KnowledgeBase-2026-10-24-review.zip"
coverage_status: "detailed-summary"
source_url: "https://support.google.com/googleplay/android-developer/answer/9898684?hl=en"
source_url_zh_attempt: "https://support.google.com/googleplay/android-developer/answer/9898684?hl=zh-CN"
source_url_store_listing_topic: "https://support.google.com/googleplay/android-developer/topic/9877064?hl=en"
source_url_in_app_review_api: "https://developer.android.com/guide/playcore/in-app-review?hl=en"
source_url_in_app_review_kotlin_java: "https://developer.android.com/guide/playcore/in-app-review/kotlin-java?hl=en"
source_url_store_listing_topic_zh: "https://support.google.com/googleplay/android-developer/topic/9877064?hl=zh-CN"
source_url_in_app_review_api_zh: "https://developer.android.com/guide/playcore/in-app-review?hl=zh-cn"
source_url_in_app_review_kotlin_java_zh: "https://developer.android.com/guide/playcore/in-app-review/kotlin-java?hl=zh-cn"
effective_date: "current developer policy; Chinese Help cache miss; no 2027-01-27"
---

# Google Play Ratings, Reviews, and Installs Policy

> **Import note (Google batch 7).** The body is the paraphrased summary from the already separated 2026-10-24 Google Play knowledge-base snapshot (`play.user-ratings-reviews-installs`, reviewed 2026-10-22). It is not a verbatim copy of an official page. The English official source is the source of truth. `kb_checked_at` is the review date recorded in the snapshot source file; this import did not re-open the live official pages. Phrases such as “this knowledge base,” “this library,” and “local topic” describe coverage inside that snapshot, not the set of pages imported into this repository. Relative snapshot links to topics, link graphs, ledgers, or CSVs that are not in this repository are kept as text mentions. Relative links that target the Google batch 1–6 topics or these twelve batch 7 topics point at the hub files. Reviewed 2026-10-22. The English policy body and Key Considerations were opened. The Simplified Chinese Help URL returned a cache miss. The Chinese hub text is an editorial paraphrase and was not checked against a Chinese official body. That cache miss is not a policy change. The adjacent Content Ratings Chinese URL also returned a cache miss in this source; the Content Ratings topic records its own language gap. No 2027-01-27 date is recorded. This page is a `normative` developer policy. If an overview conflicts with the full policy, the full policy controls. The in-app review API is an implementation note and does not authorize rating prompts that the policy prohibits. The consumer posting policy is a separate topic.

**Reviewed: 2026-10-22.** This page summarizes the English Play Console Help policy body and Key Considerations. The Simplified Chinese Help URL returned a cache miss in this review, so the Chinese version is a bilingual paraphrase of the opened English page; it was not independently verified against a Chinese body. The Help Center states that the full policy controls if an overview conflicts with it.

## Core rule: do not manipulate Play placement

Developers must not attempt to influence an app's placement on Google Play through illegitimate means, including artificially inflating ratings, reviews, or install counts. The policy gives these examples:

- Offering discounts, rewards, or other benefits in exchange for a rating or review; do not imply that a user must give a high rating to receive an incentive.
- Repeatedly submitting ratings while posing as users to influence an app's placement.
- Submitting or encouraging reviews with promotional or inappropriate content, such as affiliate information, coupons, game codes, email addresses, or links to websites or other apps.
- Making incentivized installs of other apps the main functionality of the app.
- Using automated services to inflate ratings or installs; Key Considerations explicitly lists this as a prohibited practice.

The policy protects authenticity and ranking integrity. Ordinary user acquisition, genuine voluntary installs, honest reviews, and normal developer responses are not manipulation by themselves. The central risk is fabrication, pressure, incentives, or disguising unrelated promotion as user feedback.

## Review prompts and developer replies

The policy permits a clear, non-deceptive prompt for a rating. It encourages developers to earn positive feedback through a good experience and engage with their community. Do not use deceptive pop-ups to force users to rate, and do not reward users for ratings or reviews.

When replying to a review, focus on the issue raised and do not ask for a higher rating. A support address or FAQ can be useful. The reply should address the experience, not bargain for a different score.

## Android In-App Review API: technical best practices, not a separate policy clause

The [Google Play In-App Reviews API guide](https://developer.android.com/guide/playcore/in-app-review?hl=en) is Android technical documentation, not a direct link from the Play policy body above. It helps implement the no-pressure and reasonable-frequency principles:

- Wait until users have experienced enough of the app to give useful feedback; do not trigger prompts excessively.
- Do not ask users screening or predictive questions before or while showing the rating card, such as whether they like the app or how many stars they would give.
- Show the Google Play review card as provided. Do not change its size, opacity, shape, add overlays, or programmatically remove it after it appears.
- The API has a time-bound display quota. Its exact value is an implementation detail and can change. Do not assume each call displays a dialog or make a button's success depend on the dialog appearing; a direct Play Store link is an alternative when users explicitly want to leave a review.
- The API completion callback does not tell the app whether a review was submitted or whether the dialog appeared. Continue the normal app flow regardless of the result.

The [Kotlin/Java integration guide](https://developer.android.com/guide/playcore/in-app-review/kotlin-java?hl=en) describes the Play Core Review Library, `ReviewManager`, requesting `ReviewInfo`, and launching the flow. `ReviewInfo` is valid only for a limited time. If a call fails or the dialog is not shown, do not change the app's normal flow.

## Direct links and adjacent topics

The opened `9898684` body contains no substantive hyperlink to another policy, declaration form, or best-practice page. Illustrative images, the feedback survey, and generic Help Community/contact links are images or general feedback/support destinations, not policy descendants. Its sidebar shows five Store Listing and Promotion topic entries, including this page and four adjacent topics; keep these distinct from body links:

| Sidebar or supporting link | Relationship | Coverage in this review |
| --- | --- | --- |
| [Store Listing and Promotion topic index](https://support.google.com/googleplay/android-developer/topic/9877064?hl=en) | Index of adjacent store listing and promotion policies. | Opened; its topic links are recorded separately in the link graph. |
| [App Promotion](https://support.google.com/googleplay/android-developer/answer/9899004?hl=en) | Covers promotion, incentivized installs, and misleading presentation; adjacent to rewarded installs/ranking manipulation. | Covered by the bilingual Ads and Promotion topic and source summary. |
| [Metadata](https://support.google.com/googleplay/android-developer/answer/9898842?hl=en) | Governs titles, icons, descriptions, and other listing metadata; misleading claims about rankings/downloads are relevant. | Cross-referenced in the [Store Listing and Asset topic](../store-listing-best-practices/store-listing-best-practices.en-US.md). |
| This page | Ratings, reviews, and installs topic within Store Listing and Promotion. | English policy body opened in full; the Chinese Help page returned a cache miss. |
| [Content Ratings](https://support.google.com/googleplay/android-developer/answer/9859655?hl=en) | Adjacent requirements for content ratings, listing, and ad audiences; it does not determine review authenticity. | English body verified; the Simplified Chinese URL returned a cache miss. The bilingual [Content Ratings topic](../content-ratings/content-ratings.en-US.md) now summarizes questionnaire rules, ad suitability, regional labels, and linked descendants. |
| [News & Magazines](https://support.google.com/googleplay/android-developer/answer/9935326?hl=en) | Category-specific requirements for news/magazine apps; a sidebar destination, not an extension of the ratings rule. | Covered by a bilingual topic. |

Related local topics: [Store Listing and Asset Best Practices](../store-listing-best-practices/store-listing-best-practices.en-US.md) · [Content Ratings, Target Audience, and Ad Suitability](../content-ratings/content-ratings.en-US.md) · [Ads and Promotion](../ads-and-advertising/ads-and-advertising.en-US.md) · [News and Magazines](../news-and-magazines/news-and-magazines.en-US.md).

The Policy Center separately links to the [ratings and review posting policy for Play users](../play-store-review-posting/play-store-review-posting.en-US.md). It governs what reviewers may post, review visibility, and copyright restrictions. It is not a body link from this developer Help article, and it should not be conflated with developer rules for acquiring or manipulating reviews.

The Help Center policy page does not link from its body to the In-App Reviews API. The API and integration guide above were added as related official implementation guidance; they do not expand, replace, or redefine the policy obligations. The API page's Native, Unity, Unreal, testing, Play Core terms, and other technical descendants were not recursively captured in this topic. Check the official docs for implementation details.

## Release and operations checklist

1. Check whether rewards, discounts, contests, or in-app benefits are tied to ratings or reviews; remove that exchange.
2. Audit review-acquisition channels, agencies, and automation for fake accounts, repeated submissions, or purchased reviews/installs.
3. Ensure the app's main functionality is not incentivized installation of other apps; keep affiliate links and coupon codes out of user reviews.
4. Make prompts voluntary, clear, and non-deceptive. Do not reward or pressure users, or ask for their opinion/predicted rating before showing the review card.
5. Reply to the issue and provide useful support, without asking users to raise their score.
6. When using the In-App Review API, follow its display design, timing, changing-quota, and normal-flow guidance.

This is a bilingual paraphrase and link analysis of the English official page, not a mirror of the policy text. Ranking/review rules, API behavior, and Play Console enforcement may change; recheck the current official sources before release.
