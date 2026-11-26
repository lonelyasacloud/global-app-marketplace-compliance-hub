---
id: google-play.google-play-shorts-creative-guidelines
platform: google-play
language: en-US
authority: operational
status: current
kb_checked_at: 2026-10-24
review_due: 2027-01-24
regions: [global]
topics: [play-shorts, promotional-content, creative-assets, app-discovery]
snapshot_id: play.google-play-shorts
snapshot_package: "GooglePlay-KnowledgeBase-2026-10-24-review.zip"
coverage_status: "detailed-summary"
source_url: "https://support.google.com/googleplay/android-developer/answer/18611720?hl=en"
source_url_2: "https://support.google.com/googleplay/android-developer/answer/17165227?hl=en"
effective_date: "creative and review guidance; built-in captions planned for the end of 2026; manage-guide display was US-only on the review date; no 2027-01-27"
---

# Google Play Shorts Creative, Content Review, and Technical Guide

> **Import note (Google batch 8).** The body is the paraphrased summary from the already separated 2026-10-24 Google Play knowledge-base snapshot (`play.google-play-shorts`, reviewed 2026-10-24). It is not a verbatim copy of an official page. The English official source is the source of truth. `kb_checked_at` is the review date recorded in the snapshot source file; this import did not re-open the live official pages. Phrases such as “this knowledge base,” “this library,” and “local topic” describe coverage inside that snapshot, not the set of pages imported into this repository. Relative snapshot links to topics, link graphs, ledgers, or CSVs that are not in this repository are kept as text mentions. Relative links that target the Google batch 1–7 topics or these thirteen batch 8 topics point at the hub files. Reviewed 2026-10-24. The English article was reopened from the unnumbered link on the Target API Help page. The `?hl=zh-CN` variant was inaccessible, so the Chinese hub text is an editorial paraphrase of the English body. That access failure is not a policy change. The safe-zones document and the third-party pitch presentation returned cache misses on 2026-10-23. Their contents are unknown. Built-in captions are described as planned for the end of 2026. That plan is not 2027-01-27. The separate manage guide, read 2026-10-23, said access was limited to selected partners and display was US-only. A 30–90 second story mention does not override the 60-second upload cap. This is operational creative and review guidance. It does not replace the Developer Program Policy, store-listing rules, or content ratings, and it is not a Target API requirement. Evidence level: Operational.

## Scope and availability

Google's [getting-started guide](https://support.google.com/googleplay/android-developer/answer/18611720?hl=en) describes Play Shorts as a swipeable vertical-video discovery feed in Google Play, initially including Apps Home. It supports two broad creative purposes: showing real app interfaces and workflows for functional discovery, and previewing catalog content such as episodic video, comics/webtoons, audiobooks, or wellness audio. The guide's install and retention uplift statements are Google's product claims, not guarantees.

This is a feature-specific creative, content-review, and asset-specification guide. It does not replace the Developer Program Policies, store-listing asset requirements, content ratings, or review of the app itself. Use it with [App review preparation](../app-review-preparation/app-review-preparation.en-US.md), [Content ratings](../content-ratings/content-ratings.en-US.md), [store-listing assets](../store-listing-best-practices/store-listing-best-practices.en-US.md), and [Ads policy](../ads-and-advertising/ads-and-advertising.en-US.md).

The separate [Manage Play Shorts guide](https://support.google.com/googleplay/android-developer/answer/17165227?hl=en)—not a direct body link from the creative guide—said on October 23, 2026 that access is limited to selected partners and display is currently US-only. The upload/management workflow moved into Play Console starting June 2026. Do not read the creative guide as a promise that every developer can submit or that assets display worldwide.

## Creative best practices

- **Show value early:** Put a clear visual or audio hook in the first 3–5 seconds. Avoid slow fades, static logo intros, and blank opening frames. Comics can open on the cover.
- **Work with sound off:** Align narration, visuals, and text/captions so the idea remains understandable when muted. Keep captions readable and on screen long enough. The article says built-in captions are planned for the end of 2026 and may overlap embedded captions; recheck this planned feature before submission.
- **Keep pacing readable:** Use smooth transitions, allow time to read text, and use subtle tap cues or zooms only when they help direct attention.
- **App/function previews:** Favor practical tutorials, feature walkthroughs, real app usage, or major updates. Show the actual UI and avoid generic brand advertising that does not explain the app.
- **Drama, webtoons, and comics:** Establish characters, conflict, or a turn quickly. Preserve comic reading order, full panels, and legible dialogue; avoid borders, headers, footers, or letterboxing that shrink the content. The guide mentions a 30–90 second story format for episodic drama, while its technical table sets a 60-second maximum upload length. Follow the hard technical cap; do not treat 90 seconds as an allowed upload duration.
- **Audiobooks/wellness audio:** Choose representative catalog audio with no silent lead-in or abrupt cut. Pair it with a clear, undistorted poster that matches the track.
- **Authenticity and metadata:** Show genuine app workflows or catalog content. Titles, subtitles, episode descriptions, warnings, and poster imagery must accurately match the submitted asset; do not imply unavailable features or misleading outcomes.

## Four content-review dimensions

| Dimension | Guide focus | Pre-submission check |
| --- | --- | --- |
| Useful, authentic, and accurate | Show real app functionality or catalog content, communicate its value, align audio posters with tracks, and match metadata to the creative. | Record a released build and verify the demonstrated feature, item, episode, chapter, track, and warnings. |
| Craft and production quality | At least 720p, clear/stable footage, full vertical framing, intelligible synchronized audio, and readable captions/text. More than three flashes per second is listed as disqualifying. Listen posters should be crisp, undistorted JPG/PNG; avoid rounded borders and competing store logos. | Check small screens, muted playback, low brightness, and crops. Keep UI and key information within safe zones. The article describes top 15%, bottom 20%, and 10% on each side as cutoff/overlap areas. The linked safe-zone file was inaccessible in this review, so these percentages are not a complete coordinate specification. |
| Platform safety and integrity | All assets must still follow Google Play Developer Program Policies. The guide names hate/harassment, child exploitation/endangerment, extreme gore, self-harm promotion, illegal/extremist acts, non-consensual sexual content/severe abuse, animal cruelty, and unauthorized IP as risks. | Check the [Developer Program Policy](../developer-program-policy/developer-program-policy.en-US.md), [inappropriate content](../inappropriate-content/inappropriate-content.en-US.md), [child safety](../age-restricted-child-safety/age-restricted-child-safety.en-US.md), and IP rules for visuals, dialogue, music, and artwork. |
| Discovery-surface suitability | Shorts/homepage discovery is for general audiences and is held to a stricter appropriateness standard than an individual app detail page. Avoid shocking/grotesque imagery, real-world tragedies/mass casualties/active conflicts/elections, and promotion of sensitive services such as crypto trading, payday loans, compensated dating, or real-money gambling. | Review “app can be listed” and “creative is eligible for homepage featuring” separately. Ineligibility for a discovery surface does not automatically mean the app itself violates policy. |

For fictional stories, the guide says not to sexualize or gratuitously focus on intimate body parts, and to respect a clearly expressed refusal. Limited stylized conflict serving the story can be acceptable, but avoid realistic severe injury, gore, or self-harm/illegal-drug instructions. Severe profanity, sexual insults, and identity-based slurs are incompatible with general-audience discovery; occasional mild language is contextual. Promotional assets should avoid third-party watermarks/social handles, external ad or sponsorship overlays, unauthorized Google Play logos, competitor devices/operating systems, and unverifiable ranking or award badges.

## Technical specifications shown in the article

| Item | Stated requirement/recommendation | Implementation note |
| --- | --- | --- |
| Duration | Required: 10–60 seconds. Recommended: 15–45 seconds, with about 30 seconds as a guide and the first 3–5 seconds as critical. | The 60-second technical maximum takes precedence over the drama example's 30–90-second narrative format. |
| Aspect ratio/resolution | Required 9:16 portrait; minimum 720p (720×1280); recommended 1080p (1080×1920). | Fill the screen without static header/footer bars or letterboxing. |
| Format/size | MP4, MPG, or MOV; the table lists a 1 GB maximum per file. | Recheck current Console encoding, size, and validation errors before upload. |
| Language | The article currently states `en-US` and English-only for launch; choose audio and subtitle languages in Play Console. | This launch-state statement can change; do not treat it as a permanent language policy. |
| File/brand rules | No third-party watermarks; ASCII-only filenames. | Check video, audio, poster, cover, and export filenames. |

## Direct links, sidebar, and access states

The English article body was reopened on October 24, 2026, through its unnumbered link on the Target API Help page. Its `?hl=zh-CN` variant was inaccessible in the prior review, so the Chinese summary remains based on the English body. All three visible asset-link occurrences were attempted:

| Target | Relationship | Status |
| --- | --- | --- |
| [Safe Zones document](https://docs.google.com/document/d/1gPLEQVwEn_PL8pPd5K4u4jxrNFQA79ELAKn-2F6vyzI/edit?resourcekey=0-Bw8Oxm3UBlegUqcCL0R9ww&tab=t.91in98cpanba) | Safe-zone illustrations/details. | Click returned Cache miss on October 23; content is unknown and is not inferred from the title. |
| [Play Shorts 3P Pitch presentation](https://docs.google.com/presentation/d/1U6hbvB966tQiurvRTGKJoApTbZ2uGeqbrtxWkMsaVUA/edit?resourcekey=0-oYMruFHsnIawdzbcDOjZvQ&slide=id.g3df62c6cf7e_0_0) | Labeled “MAKE A COPY” beside the safe-zone section. | Click returned Cache miss on October 23; presentation content is unknown. |
| Inline image target | A guide illustration. | Click returned Internal Error and the tool did not expose its URL; neither address nor image contents are inferred. |
| Play Console Help navigation | The page shows 30 numbered entries (including Help Center home and Version codes as item 30), followed by a separate unnumbered link to this Shorts guide. These navigation links are separate from the creative/review body and are not policy clauses. | The numbered entries are listed in [App review preparation](../app-review-preparation/app-review-preparation.en-US.md); the Shorts guide link is an extra target outside that numbered list. Descendants of the numbered entries were not reopened item-by-item from this page. |

For upload navigation, language metadata, file verification, and policy-ingestion states, see [Manage Play Shorts in Play Console](https://support.google.com/googleplay/android-developer/answer/17165227?hl=en). It separates file-processing states (`Processing` / `Processing failed`) from content/policy review states (`In review` / `Rejected` / `Live` / `Unpublished`). Unpublishing may take 2–3 days to propagate. Confirm the actual controls and app eligibility in an authorized Play Console account.

## Pre-submission workflow

1. Confirm the account/app has the Shorts entry and that the target market is eligible.
2. Choose the asset type and build the first 3–5 seconds around real functionality or real content.
3. Review for general-audience safety, rights, metadata, captions, audio, and safe-zone placement.
4. Export within the 10–60 second, 9:16, resolution, format/size, language, and filename constraints.
5. Upload directly in Play Console; check file processing separately from content/policy ingestion review.
6. If unpublishing, allow for a 2–3 day propagation delay and monitor status.

## Coverage limits

This topic summarizes the English Help body, visible technical table, creative recommendations, and content-review sections. The unavailable safe-zone document, pitch presentation, and internal image remain unresolved. Eligibility, geography, language, and Console workflow are changeable; this is not a universal store-listing requirement and does not establish that a creative or app was approved. Deeper descendants of the linked materials and Help sidebar have not all been recursively closed.
