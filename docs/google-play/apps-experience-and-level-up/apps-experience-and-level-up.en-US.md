---
id: google-play.apps-experience-and-level-up
platform: google-play
language: en-US
authority: operational
status: current
kb_checked_at: 2026-10-23
review_due: 2027-01-23
regions: [global]
topics: [apps-experience, level-up, voluntary-program, rate-card, app-quality, form-factors]
snapshot_id: play.apps-experience-level-up
snapshot_package: "GooglePlay-KnowledgeBase-2026-10-24-review.zip"
coverage_status: "detailed-summary"
source_url_enrollment: "https://support.google.com/googleplay/android-developer/answer/18018581?hl=en"
source_url_aep_overview: "https://developer.android.com/distribute/aep/aep-guidelines-overview"
source_url_aep_planner: "https://developer.android.com/distribute/aep/aep-integration-planner"
source_url_aep_program: "https://google.play/business/programs/appsexperience/"
source_url_level_up_program: "https://google.play/business/levelup/"
source_url_level_up_guidelines: "https://developer.android.com/games/guidelines"
source_url_aep_form_factor: "https://developer.android.com/distribute/aep/aep-req-form-factor-support"
source_url_aep_stability: "https://developer.android.com/distribute/aep/aep-req-stability"
source_url_aep_android_mcp: "https://developer.android.com/distribute/aep/aep-req-android-mcp"
source_url_credential_manager: "https://developer.android.com/identity/credential-manager"
source_url_sign_in_google: "https://developer.android.com/identity/sign-in/credential-manager-siwg"
source_url_legacy_sign_in_migration: "https://developer.android.com/identity/sign-in/legacy-gsi-migration"
source_url_restore_credentials: "https://developer.android.com/identity/sign-in/restore-credentials"
source_url_block_store: "https://developer.android.com/identity/block-store"
source_url_engage_sdk_guide: "https://developer.android.com/guide/playcore/engage"
source_url_premium_growth_tools: "https://google.play/business/guides/premium-growth-tools/"
source_url_youtube_play_videos: "https://support.google.com/googleplay/android-developer/answer/15501235"
source_url_promotional_content: "https://support.google.com/googleplay/android-developer/topic/12932623"
effective_date: "voluntary program dates include 2026-09-30, 2027-03-01, February 2027, and 2027-09-30; none of these is the 2027-01-27 permissions preview"
---

# Apps Experience and revamped Level Up voluntary programs

> **Import note (Google batch 8).** The body is the paraphrased summary from the already separated 2026-10-24 Google Play knowledge-base snapshot (`play.apps-experience-level-up`, reviewed 2026-10-23). It is not a verbatim copy of an official page. The English official source is the source of truth. `kb_checked_at` is the review date recorded in the snapshot source file; this import did not re-open the live official pages. Phrases such as “this knowledge base,” “this library,” and “local topic” describe coverage inside that snapshot, not the set of pages imported into this repository. Relative snapshot links to topics, link graphs, ledgers, or CSVs that are not in this repository are kept as text mentions. Relative links that target the Google batch 1–7 topics or these thirteen batch 8 topics point at the hub files. Reviewed 2026-10-23. Both language files cite the English `hl=en` enrollment article. The snapshot does not record a checked Chinese official enrollment page or a failed `hl=zh-CN` fetch. The Chinese hub text is an editorial paraphrase. Three help, community, or support targets returned internal errors in the enrollment-article pass. Their signed-in contents were not inferred. Program dates kept separate from the 2027-01-27 permissions preview include 2026-09-30, Googlebook by 2027-03-01 for Apps Experience form-factor support, dynamic-memory enforcement expected from February 2027, Android MCP enforcement deferred until 2027-03-01 or three months after self-service registration, Level Up rewards from 2027-03-01, and Level Up XR, TV, Googlebook, and Auto distribution from 2027-09-30. The older March 1, 2027 Googlebook date is not carried forward onto the current Level Up device-distribution row. These are voluntary programs. They do not replace the Developer Program Policy or the Payments policy, and a program rate card is not baseline Play policy. Evidence level: Operational.

**Reviewed October 23, 2026.** This topic summarizes Google's Apps Experience Program (AEP) and revamped Google Play Games Level Up. Both are voluntary programs. Eligible apps or games can receive a program rate card after Google review; the programs are not baseline requirements for every Google Play developer and do not replace the Developer Program Policy, Payments policy, local law, or Play Console review.

## 1. Separate program guidelines from baseline policy

| Program | Audience | Main goal | Boundary |
| --- | --- | --- | --- |
| Apps Experience Program (AEP) | Apps | Consistent, rich, stable experiences across Android form factors | Meet applicable AEP guidelines and pass an app-specific review |
| Revamped Level Up | Games | Game experience, cross-screen availability, player engagement, and stability | Meet applicable Level Up guidelines and pass a game-specific review |
| Google Play baseline policy | All applicable apps/developers | Content, data, permissions, payments, security, store presence, enforcement, and more | Participation in either program is optional; baseline policies still apply |

Enrollment in AEP or Level Up **does not improve Play Store ranking**. The published benefit is a rate card for eligible transactions. Good quality may have general product value, but program qualification is not a ranking promise. Guidelines and benefits can change; use the terms and app-specific review status shown in Play Console.

## 2. Enrollment eligibility, review, and continued qualification

The current enrollment Help page describes these main steps:

1. **Launch and account threshold:** Enrollment opened in Play Console on September 1, 2026. It is currently open only to developer-account groups that earned at least USD $1 million over the prior 12 months. The applicant needs Admin or account-owner permission.
2. **App/game threshold:** The app or game must be in production on Google Play and have remained in good standing, including compliance with applicable Play policies, for at least six months. Qualification is reviewed per app or game, not for the developer account as a whole.
3. **Preparation:** Provide review login credentials that unlock all functionality; check the applicable program guidelines; submit any eligible exemption requests before enrollment.
4. **Review and rate-card start:** Program rates apply only after Google verifies that all applicable guidelines are met. Review may take up to 14 days or longer in exceptional cases. Rates begin on the eligible market's program date or within 24 hours of enrollment, whichever is later, subject to Google's verification/approval.
5. **Rejection and resubmission:** Fix all identified issues, then submit a review request describing a full fix, an appeal, or a combination. The requester must hold an allowed Play Console role.
6. **Maintaining status:** Continue to meet program guidelines and remain in good Play policy standing. Console warnings provide remediation deadlines; missing one can remove the app/game from the program and its rate card. After returning to good standing, a six-month wait generally applies before program-rate eligibility can be restored.

The enrollment planner only produces a **preliminary** estimate of applicable guidelines and exemptions. It is not Google's final determination. Use the official guideline pages and the app-specific Console review result.

## 3. Program rate card and regional availability

This is a summary of the public rate card reviewed on the date above. Actual fees depend on the buyer's location, transaction type, new versus existing install, annual earnings tier, and approved program status. Applicable Billing fees may be additional. Do not use the developer's registration address as a proxy for buyer location, and do not treat the program rate as an automatic global fee.

| Earnings/qualification tier | Auto-renewing subscriptions | Other transactions: new installs | Other transactions: existing installs | External web-link transactions |
| --- | ---: | ---: | ---: | ---: |
| First USD $1 million of annual earnings | 10% | 10% | 10% | Check applicable program terms |
| Standard tier above USD $1 million annual earnings | 10% | 20% | 25% | 20% |
| Qualified for AEP or Level Up rate | 10% | 15% | 20% | 15% |

Program rate-card eligibility rolls out by buyer location:

| Market | Published availability date |
| --- | --- |
| United States, United Kingdom, Japan, European Economic Area, Australia | September 30, 2026 |
| South Korea | December 31, 2026 |
| Rest of world | September 30, 2027 |

Voluntary enrollment, earnings tiers, Play Billing applicability, taxes, and external-link programs are separate determinations. Use Play Console financial reports and order details to verify actual fees.

## 4. Apps Experience Program: 26 guidelines in three groups

The AEP overview groups its requirements into consistent/rich experiences, form-factor reach, and stable/modern experiences. **Not every guideline applies to every app**; applicability depends on core use cases, sign-in needs, comparable cross-platform experiences, and supported form factors. All 26 direct guideline destinations were clicked and registered; the table follows the overview, with key targets separately checked against their full text.

### Consistent and rich user experiences

| Guideline | Implementation focus and applicability |
| --- | --- |
| [Phishing Resistant Authentication](https://developer.android.com/distribute/aep/aep-req-phishing-resistant-auth) | Apps requiring sign-in offer a passkey or accepted SSO at comparable prominence; use Credential Manager for passkeys/Sign in with Google. Applies to phone, tablet, foldable, XR, Wear, and Auto. Apps without a signed-in state are out of scope; the accepted SSO list can change. |
| [Restore Credentials](https://developer.android.com/distribute/aep/aep-req-restore-credentials) | Integrate Restore Credentials for signed-in apps on phone, tablet, and foldable. The guideline lists exemptions for no-account apps, high-security/regulatory constraints, and apps already using Block Store for restoration as of September 30, 2026. |
| [Engage SDK](https://developer.android.com/distribute/aep/aep-req-engage-sdk) | Eligible media, social, health, travel, shopping, food, books/comics, and education apps on phones/tablets surface personalized recommendations and continuation content on Google surfaces. Update continuation within 10 minutes of a triggering action, refresh recommendations at least every three days, and delete surfaced content on logout/account deletion. Use-case and no-sign-in/native-content exemptions are listed. |
| [Play Content](https://developer.android.com/distribute/aep/aep-req-play-content) | Phone, tablet, foldable, and desktop apps meet one content-discovery path: allow Play access to an existing feed, or submit at least two quality-approved items per quarter across programs such as Promo Content and Play Shorts. Tools/utilities, chat/communications, and live-streaming apps may be out of scope. |
| [Title Availability](https://developer.android.com/distribute/aep/aep-req-new-title-availability) | Launch new titles on comparable Android form factors at the same time as non-Android platforms; missing the timing can cause a six-month wait for rate-card eligibility. Hardware/technical mismatch, launch grace, and EEA rules are separate. |
| [Feature Availability](https://developer.android.com/distribute/aep/aep-req-feature-availability) | Fully launch a feature on Android within three weeks of its full launch on a comparable non-Android platform in the same country, with functional parity. Technical infeasibility or an accepted production regression can qualify for an exemption. |
| [Material UX](https://developer.android.com/distribute/aep/aep-req-material-ux) | Apps with comparable cross-platform design systems use Compose Material 3; Wear OS uses Wear Compose Material 3. The guideline lists no exemptions. |
| [System Emoji](https://developer.android.com/distribute/aep/aep-req-system-emojis) | For apps that render user emoji, keep emoji in inputs, comments, messages, reactions, and text-on-image consistent with the system keyboard/surfaces; use the highest available font resolution where emoji can be enlarged. |
| [Dark Theme Support](https://developer.android.com/distribute/aep/aep-req-dark-theme) | Apps with a comparable dark experience support the system dark preference across all screens, overlays, and system components; text/icons maintain at least 4.5:1 contrast and respond to system uiMode changes. |
| [Themed App Icons](https://developer.android.com/distribute/aep/aep-req-theme-app-icons) | Provide an adaptive app icon that can be tinted to match the user's system theme; check the linked guideline for its resources and exemption conditions. |
| [Physics Based Motion](https://developer.android.com/distribute/aep/aep-req-physics-based-motion) | Apps with comparable cross-platform motion avoid zero-millisecond primary-navigation/state changes and use interruptible transitions that preserve context and gesture momentum. |
| [Share Sheet](https://developer.android.com/distribute/aep/aep-req-share-sheet) | Apps with comparable external sharing use the Android Sharesheet/system chooser for external shares. In-app forwarding is outside the external-share requirement. |

### Reach across Android form factors

| Guideline | Implementation focus and applicability |
| --- | --- |
| [Form Factor Support](https://developer.android.com/distribute/aep/aep-req-form-factor-support) | Every app must reach Adaptive App Tier 2: phone, tablet, foldable, and XR at enrollment; **Googlebook by March 1, 2027**. TV, Wear, and Auto add quality requirements for relevant app use cases. Updated form-factor quality specifications generally allow a 12-month migration grace period. Exemptions cover hardware/technical constraints, no logical use case, or regional device unavailability. This requirement does not itself require distribution on Play on those devices. |

### Stable, modern, and use-case-specific experiences

| Guideline | Implementation focus and applicability |
| --- | --- |
| [Stability](https://developer.android.com/distribute/aep/aep-req-stability) | AEP thresholds: average crash rate below 1% on reference devices and 2% on 4GB+ devices; ANR below 2%/3%; excessive slow frames below 2% on reference devices. Calculated over trailing 28 days for the approved device set with at least 1,500 sessions. These differ from general Play bad-behaviour thresholds. Dynamic-memory thresholds are expected to be enforced from February 2027; check the live technical-quality page. |
| [Quality — Jetpack Compose](https://developer.android.com/distribute/aep/aep-req-jetpack-compose) | Guideline for modern, scalable, high-quality UI; check its source for the accepted Compose and equivalent-implementation criteria. |
| [Predictive Back](https://developer.android.com/distribute/aep/aep-req-predictive-background) | Use Android predictive-back behavior to preview the destination and reduce accidental exits. |
| [Edge to Edge](https://developer.android.com/distribute/aep/aep-req-edge-to-edge) | Adopt modern edge-to-edge window behavior, use screen space fully, and correctly handle system bars and safe areas. |
| [Android MCP](https://developer.android.com/distribute/aep/aep-req-android-mcp) | For listed messaging, notes, calendar, tasks, health, shopping, travel, creativity, media, and system-tool use cases, use AppFunctions to expose at least one relevant capability and pass integration tests. It is optional during Early Access. Enforcement is deferred until **March 1, 2027 or three months after self-service Android MCP registration launches, whichever is later**; current participants will receive advance notice. |
| [Media3](https://developer.android.com/distribute/aep/aep-req-media-3) | Check Media3 playback and session guidance for relevant media-playback use cases. |
| [CameraX](https://developer.android.com/distribute/aep/aep-req-camera-x) | Check CameraX capture guidance for camera-centric use cases. |
| [Cast Support](https://developer.android.com/distribute/aep/aep-req-cast-support) | Check Cast guidance for casting and large-screen experiences. |
| [Photo Picker](https://developer.android.com/distribute/aep/aep-req-photo-picker) | Check the system Photo Picker and minimum-scope media selection guidance for photo/video selection use cases. |
| [Preload Caching](https://developer.android.com/distribute/aep/aep-req-preload-caching) | Check preloading/caching requirements for scrollable media feeds, especially playback-start latency. |
| [Night Mode](https://developer.android.com/distribute/aep/aep-req-night-mode) | Check hardware-accelerated low-light still-capture guidance for night-photography use cases. |
| [Android Telecom Framework](https://developer.android.com/distribute/aep/aep-req-telecom-api) | Check Telecom Framework registration and system integration for VoIP-call use cases. |
| [Picture in Picture Support (PiP)](https://developer.android.com/distribute/aep/aep-req-picture-in-picture) | Check PiP guidance for applicable video playback, calling, navigation, and similar experiences. |

The eight use-case-specific criteria are conditional. Android Developers says a compatible alternative framework can be considered if it offers comparable quality, user capability, stability, and ecosystem compatibility. These technical program criteria do not replace Google Play baseline policy.

## 5. Revamped Level Up: game experience requirements

The Level Up page groups the game requirements into three themes; games need all applicable new guidelines to qualify for the rate card. The current page has changed over time, so do not carry the former March 1, 2027 Googlebook date forward to the overall Level Up device-distribution row.

| Theme | Main checks | Exceptions/date notes |
| --- | --- | --- |
| Consistent gamer experience | Initialize Play Games Services v2 at startup; enable Sidekick as the guideline requires; provide at least 10 lifetime achievements, including four reasonably achievable in the first hour for Quests; integrate Game Stats, Rewards, and cloud saves/conflict resolution. PGS v2 platform identity does not require Google identity or an in-game account. | Games primarily targeting children under 13 can be exempt from many items in this section. Paid games and other use cases have guideline-specific Rewards/cloud-save exemptions. |
| Reach across screens | Support large-screen layouts/configuration changes and precision input; meet Google Play Games on PC, form-factor distribution, and title-availability criteria. | Mobile/foldable/tablet from September 30, 2026; the current page lists XR, TV, Googlebook, and Auto from September 30, 2027. Play distribution on every device is not automatically required. Location/sensor dependencies, insufficient hardware, regional device availability, and IP licensing may qualify for exemptions. |
| Stable, smoother gameplay | Check stability, performance, memory, Vulkan/graphics APIs, and reference-device testing against the current guideline. | Reference devices and exemptions change; assess the current criteria against the game's engine, device capabilities, and enrollment status. |

Dates: the Rewards guideline requires at least two single-use Play Games Reward offers from September 30, 2026. From **March 1, 2027**, it also requires at least one repeatable reward for completed social challenges, capped at one reward per player per week. Games primarily targeting under-13 players and paid games have stated exemptions. The current form-factor distribution date is **September 30, 2027**, as above. A missed comparable title/feature launch can trigger a six-month program-rate wait; qualifying legacy launch dates or approved exemptions may change the result.

## 6. Practical review sequence

1. Decide whether to pursue AEP or Level Up. If not, continue to meet baseline Play policies.
2. Inventory use cases: sign-in, content/recommendations, media/camera/communications, cross-platform launches, device form factors, child-directed audience, and monetization.
3. Use the [AEP Guidelines Planner](https://developer.android.com/distribute/aep/aep-integration-planner) as an initial screen, then open each applicable official guide listed here for applicability, exemptions, deadlines, and testing criteria.
4. For enrollment, prepare the production app, six months of good standing, reviewer credentials, evidence for each guideline, and exemption materials. Keep a per-guideline acceptance record.
5. After approval, reconcile fees by buyer location, transaction type, install status, earnings tier, and monthly order reports; track Console warnings to maintain eligibility.

## 7. October 13, 2026 official product update: discovery, deep links, and game engagement

The [Android Developers Blog](https://android-developers.googleblog.com/2026/10/new-tools-for-discovery-and-engagement.html) published a developer-facing product checklist covering Ask Play app comparisons, Game Finder, Gemini/Play discovery, Sprints, Playbacks, Quests, and quality programs. It is a product/tool update, not a new Developer Program Policy announcement. The table records the article's direct body-link targets and their relationship to this topic.

| Direct blog link | Target-page content and relationship | Boundary |
| --- | --- | --- |
| [“More than a store” product update](https://blog.google/products-and-platforms/platforms/google-play/google-play-updates-october-2026/) | Covers Ask Play, Game Finder, cross-device discovery, 48-hour Sprints, and personal AI apps. Personal apps are initially limited to the user's own device, selected markets, and users 18+; public distribution still requires a professional developer account and the same Trust & Safety reviews and quality standards. | This describes product scope; it does not exempt public releases from review. Check current rollout notes for availability and dates. |
| [I/O 2026 Google Play update](https://android-developers.googleblog.com/2026/05/io-2026-whats-new-in-google-play.html) | Provides context on Gemini discovery, Engage SDK, Play Shorts, Sidekick, Play Console AI/business tools, and subscription recovery. | The blog describes roadmap, features, and examples; it does not replace payment, subscription, data, or user-experience policies. Its other product links are separate branches and are not exhausted here. |
| [Verify and maintain deep links](https://support.google.com/googleplay/android-developer/answer/12463044) | Play Console's Deep links page can inspect website URL/app-version mappings and intent filters, preview links, and patch configurations. Console patches do not carry into future app versions, so recheck the Manifest and released build. | This pass opened the article and Android App Links child. Account-specific Console data requires developer access; Ads data is visible only when a Google Ads account is linked. The article's 15-item generic sidebar was not exhausted. |
| [Engage SDK program page](https://google.play/business/programs/EngageSDK/) | Describes Apps Home, You tab, store listings, Collections, tablets, and Google TV; nine content categories require eligibility and an expression of interest in the developer preview. It recommends continue journeys, timely personalized recommendations, and featured content clusters; the FAQ links to eligibility, the interest form, and vertical integration guides. | SDK integration is a discovery/engagement option, not a universal obligation or ranking guarantee. Check AEP criteria, preview eligibility, and technical integration separately. |
| [Game Stats guideline anchor](https://developer.android.com/games/guidelines) and [Play Games Rewards guideline anchor](https://developer.android.com/games/guidelines) | Both blog links land on different sections of the revamped Level Up guidelines. They concern eligibility for games voluntarily participating in Level Up, not a universal Play policy for every game. See the next section for conditions, exemptions, and implementation. | The links resolve to the same page; the graph distinguishes their section relationships without counting two URLs. |
| [Apps Experience Program](https://google.play/business/programs/appsexperience/) and [Level Up program overview](https://google.play/business/levelup/) | Both programs offer rate-card benefits for apps/games meeting program criteria. The overview pages describe availability, enrollment, and eligibility; the Level Up guidelines provide the experience checks. | Enrollment is voluntary. Do not describe program fee conditions as baseline policy for every developer, or marketing case studies as guaranteed outcomes. |
| [Play Console home and navigation changes](https://support.google.com/googleplay/android-developer/answer/18742903) | Explains homepage filters, app switching, and the location of account-level pages, helping developers find release/policy tasks and management controls. | This is Console navigation guidance, not a new policy requirement; account-visible content can vary by permission. |

The blog recommends keeping store listings, tags, and promotional events current; using high-resolution media that works across screens; previewing/testing deep links with the Play Console emulator; and integrating Engage when eligible. For games, it describes Sprints as 48-hour challenges matching two to five similarly skilled players, plus Game Stats and Play Games Rewards as paths for challenges and rewards. These are product best practices and tool recommendations; label them separately from formal policy, program eligibility, and account-specific review.

## 8. Game Stats and Play Games Rewards: Level Up descendants and implementation checks

### Game Stats

The current [Level Up guidelines](https://developer.android.com/games/guidelines) ask enrolled games to provide at least five repetitive stats representing common core gameplay, with at least one usable for competitive engagement. If a game has a primary progression mechanic, it also needs at least one progression stat. Games primarily targeting children under 13 do not have the feature enabled; games without a clear progression mechanic and qualifying Native PC Early Access titles should be assessed against their specific exemptions.

The [Game Stats guide](https://developer.android.com/games/pgs/gamestats) places stats on the player's Gamer profile and requires that they do not depend on purchases or ad views, are not generic app use such as opening settings, contain no personal/sensitive data or offensive/sexual/violent/hateful content, and are available to all players. A game can configure at most 50 stats. Send discrete per-event values and aggregate with `SUM` or `COUNT`; use `MAX` only for a single-occurrence peak. Do not send a precomputed lifetime total with `MAX`: it may appear on the profile but cannot power features such as Leagues, Quests, and Sprints.

### Play Games Rewards

The current Level Up guideline requires at least two single-use offers from **September 30, 2026**, and at least one repeatable offer from **March 1, 2027**, capped at one per player per week. Rewards need to be meaningful and available to every player in the game's published regions. Games primarily targeting under-13 players and paid games have stated exemptions. Assess whether a title qualifies for an exception; do not apply these dates to every game's baseline Play policy.

The [Rewards implementation guide](https://developer.android.com/games/rewards) further requires selecting/creating SKUs in Play Console and using the Play Billing Library's out-of-app purchase flow to grant rewards provided by Play. **This does not require developers to switch their own paid transactions to Play Billing**; developers using alternative billing still need the SKU and PBL integration for reward delivery. On game start/resume, check for unacknowledged rewards and verify/grant them promptly. Players have three days to claim. If the game supports multiple in-game identities, prompt the player to choose where the reward goes; the PGS ID and Play Billing account must match.

### Implementation sequence and irreversible steps

| Resource | Reviewed content in this pass | Practical check |
| --- | --- | --- |
| [Integrate Game Stats](https://developer.android.com/games/pgs/integrate-gamestats) | Play Console event/stat configuration, CSV/ZIP imports, internal testing, logs, and publishing; fields such as event names, stat IDs, progression direction, units, and associated events have editing limits. Published stats cannot be deleted; draft/test events and stats can be removed. | Define the event schema and calculation/display logic first, check privacy and the 50-stat cap, then use internal tests and validation logs. Review the schema before publishing because published stats cannot be deleted. |
| [Game Stats for Android](https://developer.android.com/games/pgs/android/gamestats) | Covers client/server event submission paths, event fields, and progress updates; the large implementation page also links to PGS API constraints and examples. | This is a selected review of the main model and API direction, not every SDK, API field, or game-engine example. Check personal/sensitive-data exclusions against Play User Data. |
| [Rewards / Play Billing integration](https://developer.android.com/google/play/billing/integrate) | The Rewards page connects verification, granting entitlements, notifying users, and acknowledging processing to the Play Billing Library's out-of-app purchase flow. Developers also need to handle purchase state and duplicate grants. | This is a reward-delivery integration, not an alternative-billing payment route; validate Console SKU setup and in-game identity mapping separately. |
| [Internal testing track](https://support.google.com/googleplay/android-developer/answer/9845334) | Tests event/stat visibility and PGS sign-in with a limited group before release. | Play Console and tester accounts require account permissions; passing internal tests is not a policy approval or program qualification decision. |

The Game Stats guide still says the You-tab UI “will be available in September 2026,” although the page shows a last-updated date of October 22, 2026. That date has passed. This pass does not infer whether the UI has launched; verify current Console/player visibility. Install/spend uplifts quoted by Google are specific partner cases and measurement windows, not a guaranteed causal result of integration.

## 9. Selected second-level implementation resources reviewed

These are grandchildren of the AEP overview. They explain how some program checks translate into Android implementation or Play Console preparation.

| Parent guideline | Linked resource | What it adds to the program summary |
| --- | --- | --- |
| Phishing Resistant Authentication | [Credential Manager](https://developer.android.com/identity/credential-manager), [Sign in with Google](https://developer.android.com/identity/sign-in/credential-manager-siwg), and [migration from legacy Google Sign-In](https://developer.android.com/identity/sign-in/legacy-gsi-migration) | Credential Manager is the recommended unified Android API for passkeys, passwords, and federated sign-in. Google Sign-In migration separates authentication from later authorization; it does not change the AEP requirement for an accepted phishing-resistant method. |
| Restore Credentials | [Restore Credentials guide](https://developer.android.com/identity/sign-in/restore-credentials) and [Block Store](https://developer.android.com/identity/block-store) | The restore key is generated after authentication and can move through cloud backup or device-to-device transfer. Cloud restore depends on Google Account, Android backup, and device lock settings. Block Store stores session data/tokens and is a legacy option; current Android guidance recommends considering passkeys and Credential Manager. |
| Engage SDK | [Engage SDK guide](https://developer.android.com/guide/playcore/engage) | Adds personalized recommendations and continuation content to Google surfaces, with vertical-specific integration guides. The guide points to eligibility, reach, and interest-form routes; those routes remain a separate program/Console check. |
| Play Content | [Premium growth tools](https://google.play/business/guides/premium-growth-tools/), [YouTube videos on Google Play](https://support.google.com/googleplay/android-developer/answer/15501235), and [promotional content index](https://support.google.com/googleplay/android-developer/topic/12932623) | Premium growth tools require good standing plus metric and category eligibility. The public baseline examples include 1.6 million daily active users and installs over a three-month period, or qualifying monthly spend; partner and dating thresholds differ. YouTube submissions should be owned, public, embeddable, non-monetized, non-live, copyright-cleared, and recent enough for the target surface. Promotional content covers events and featured in-app products, with separate content-quality and submission checks. |

The seven destinations above were opened and their relationship summarized. Their own code samples, vertical integration pages, forms, and linked quality resources are not all recursively audited yet. See graph §4.93 for the remaining branch boundary.

## 10. Sources and descendant-link coverage

| Source | Role in this topic | Reviewed / unresolved boundary |
| --- | --- | --- |
| [Enrollment and maintenance Help page](https://support.google.com/googleplay/android-developer/answer/18018581?hl=en) | Eligibility, enrollment, exemptions, review, appeals, continued status, rate-card timing, and financial reports | 19 body-link occurrences normalize to approximately 16 destinations; readable targets were followed. Three Help/community/support routes returned internal errors in that pass; signed-in content was not inferred. |
| [AEP guidelines overview](https://developer.android.com/distribute/aep/aep-guidelines-overview) | Classification and applicability overview for the 26 direct AEP guideline targets | All 26 destinations were clicked and registered. Key eligibility/threshold pages were read in full. Deeper code/API/best-practice links on each technical guide are not all closed; see recursive link graph §4.93 (snapshot: `../google-play-policy-link-graph-en.md`, not imported in this repository). |
| [AEP Guidelines Planner](https://developer.android.com/distribute/aep/aep-integration-planner) | Use-case questionnaire and preliminary exemption identification | Explicitly not a final/official determination; the official guides and Play review control applicability. |
| [AEP program description and rate card](https://google.play/business/programs/appsexperience/) | Regional rate table, availability, and ranking clarification | Program overview/marketing page; actual eligibility still depends on Console enrollment and official guidelines. |
| [Level Up program page](https://google.play/business/levelup/) and [revamped guidelines](https://developer.android.com/games/guidelines) | Game rate card, three guideline themes, dates, and exemptions | The guide has many same-page anchors and technical descendants. This topic covers key program branches but does not claim to recursively capture every Android API, game-engine guide, or reference-device page. |
| [October 13, 2026 Android Developers product update](https://android-developers.googleblog.com/2026/10/new-tools-for-discovery-and-engagement.html) | Entry point for Ask Play, Game Finder, Engage, Sprints, Game Stats/Rewards, and Console visual changes | Every external page linked in the article body was opened by target. Game Stats, Rewards, and Engage are summarized here and in graph §4.98. Deeper product links in the I/O and Google blogs, all nine Engage vertical guides, every Game Stats SDK/API member, and all Reward descendants remain open. |

This is a bilingual paraphrase, not a full-text mirror. Revisit official sources and Play Console whenever a guideline, exception, date, or account-specific approval changes. Continue through [Payments and subscriptions](../payments/payments-and-subscriptions.en-US.md), [app quality and form-factor guidelines](../app-quality-and-form-factor-guidelines/app-quality-and-form-factor-guidelines.en-US.md), and the deadline register (snapshot: `../google-play-policy-operations-en.md`, not imported in this repository).
