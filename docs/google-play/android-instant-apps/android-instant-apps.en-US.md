---
id: google-play.android-instant-apps
platform: google-play
language: en-US
authority: historical
status: historical
kb_checked_at: 2026-10-22
review_due: 2027-01-22
regions: [global]
topics: [instant-apps, retired-program, deep-links, credential-manager, historical-policy]
snapshot_id: play.android-instant-apps
snapshot_package: "GooglePlay-KnowledgeBase-2026-10-24-review.zip"
coverage_status: "detailed-summary"
source_url_policy: "https://support.google.com/googleplay/android-developer/answer/9900182?hl=en"
source_url_technical_requirements: "https://developer.android.com/topic/google-play-instant/tech-requirements"
source_url_ux_best_practices: "https://developer.android.com/topic/google-play-instant/best-practices/apps"
source_url_smart_lock: "https://developers.google.com/identity/smartlock-passwords/android/overview"
source_url_credential_manager: "https://developer.android.com/training/sign-in/passkeys/"
source_url_deep_links_console: "https://support.google.com/googleplay/android-developer/answer/12463044"
source_url_android_app_links: "https://developer.android.com/training/app-links"
effective_date: "retired December 2025; checklist pages updated 2026-06-24 do not revive the program; no 2027-01-27"
---

# Android Instant Apps (retired): policy and historical implementation guide

> **Import note (Google batch 8).** The body is the paraphrased summary from the already separated 2026-10-24 Google Play knowledge-base snapshot (`play.android-instant-apps`, reviewed 2026-10-22). It is not a verbatim copy of an official page. The English official source is the source of truth. `kb_checked_at` is the review date recorded in the snapshot source file; this import did not re-open the live official pages. Phrases such as “this knowledge base,” “this library,” and “local topic” describe coverage inside that snapshot, not the set of pages imported into this repository. Relative snapshot links to topics, link graphs, ledgers, or CSVs that are not in this repository are kept as text mentions. Relative links that target the Google batch 1–7 topics or these thirteen batch 8 topics point at the hub files. Reviewed 2026-10-22. Both language files cite the English `hl=en` Instant Apps Help article. The snapshot does not record a checked Chinese official policy page or a failed `hl=zh-CN` fetch. The Chinese hub text is an editorial paraphrase. The program ended in December 2025. Instant Apps can no longer be published through Google Play, Instant APIs no longer work, and Play no longer serves Instant Apps. Technical and UX pages updated 2026-06-24 still carry the retirement notice. Those update dates do not revive the program. No 2027-01-27 date is recorded. Historical Instant clauses are not current publishing requirements. Current Developer Program Policy, user-data, and permission rules still apply to installed apps. Evidence level: Historical.

**Reviewed: 2026-10-22.** The Google Play Android Instant Apps policy Help page remains accessible, but the program it describes has been discontinued. The current Android Developers technical checklist states that **starting in December 2025, Instant Apps can no longer be published through Google Play; Google Play services Instant APIs no longer work; and Play no longer serves Instant Apps by any mechanism.** This topic preserves `answer/9900182` as a historical policy and legacy-implementation reference; its Instant-specific rules are not current publishing requirements for new apps.

## Current status and migration direction

- The Instant Apps program is retired. If an app or game still contains an Instant App module or Google Play services Instant API calls, check for and remove disabled dependencies.
- Android Developers encourages developers to direct users to the regular installed app and, where useful, use deep links to open a relevant feature. For website URLs, Android App Links are one official recommended approach.
- If a legacy implementation uses Smart Lock for Passwords, its linked Google Identity documentation now marks Smart Lock deprecated and recommends Credential Manager. That is guidance for migrating ordinary Android sign-in, not evidence that Instant Apps remain publishable.
- Current development still follows the general Developer Program Policy, data/permission rules, deceptive-behavior requirements, and applicable Android technical rules. The retired Instant Apps clauses do not replace those current requirements.

## Historical contents of `answer/9900182`

The Help page lists the following Instant Apps-specific rules. Since the program has ended, these are retained only to explain legacy code, historical review material, and migration decisions:

| Historical topic | What the old Help page said | Current interpretation |
| --- | --- | --- |
| Identity | Instant Apps with login functionality should integrate Smart Lock for Passwords. | The linked Smart Lock documentation now marks it deprecated; evaluate Credential Manager for new sign-in work. The old policy page has not been synchronized. |
| Link support | If a link could resolve to an Instant App, route it there instead of capturing it in a WebView. | Instant App destinations no longer exist. Migrate web-to-installed-app routing to current deep-link/App Links approaches and test browser/Play fallbacks. |
| Installation prompts | Installing the full app must not be the Instant App's main purpose; use “install” and the designated icon; allow no more than 2–3 implicit install prompts; do not use ad-like banners. | Historical UX requirements only, not current Play Instant publishing controls. |
| Device state and visibility | Do not leave persistent device changes after the Instant App session; keep the running Instant App visible to the user. | Product-specific rules for the retired experience. Installed apps remain subject to applicable user-data, permission, and transparency requirements. |
| Device identifiers | Do not access identifiers that persist beyond the session and cannot be reset by the user, such as build serial, MAC, IMEI/IMSI; do not fingerprint users by other means. Phone number access was allowed only with runtime permission. | Historical privacy review signals. Check current User Data, sensitive-permission, and Android platform rules for any live identifier use. |
| Network traffic | Encrypt Instant App network traffic with TLS, such as HTTPS. | An explicit requirement in the historical page; current apps still need secure transmission under applicable security and data-protection requirements. |

## Direct body links and descendants

`answer/9900182` also links to Developer Program Policies, Smart Lock, WebView, the Instant technical checklist, the Material “get app” icon, and UX best practices. The table separates body links, technical resources, and access boundaries:

| Destination | Content, relationship to parent, and access status |
| --- | --- |
| [Google Play Developer Program Policies (old link)](https://support.google.com/googleplay/android-developer/answer/9904549) | Clicking from the Instant Apps page returned HTTP 404. Use the project's bilingual [consolidated Developer Program Policy](../developer-program-policy/developer-program-policy.en-US.md) for a current summary and check the official policy center for current source text. |
| [Smart Lock for Passwords: Android integration flow](https://developers.google.com/identity/smartlock-passwords/android/overview) | The old URL redirects to the integration-flow page. It marks Smart Lock deprecated and recommends migration to [Credential Manager](https://developer.android.com/training/sign-in/passkeys/). It describes legacy credential retrieval, saving, hints, and sign-out; do not treat its API calls as new-project guidance. |
| [Credential Manager: sign in users](https://developer.android.com/training/sign-in/passkeys/) | The migration destination linked from the Smart Lock page; it covers Credential Manager guidance for passwords, passkeys, and federated sign-in. This records its relationship as the replacement technology rather than copying the Android identity API documentation into the Play policy library. |
| [Android `WebView` API reference](https://developer.android.com/reference/android/webkit/WebView.html) | The Instant Apps policy uses WebView as an example of what not to use to capture links that should resolve to an Instant App. This is a very large general API reference, not an Instant Apps review guide; its API members and descendants are not exhaustively summarized. |
| [Google Play Instant technical requirements checklist](https://developer.android.com/topic/google-play-instant/tech-requirements) | The page begins by stating the program ended in December 2025. It labels checklist items Required, Best practice, or Good to have. Historical examples include a 15 MB download cap, 150 MB device-storage cap, a recommended uncached load time, back/exit behavior, ad format, purchase rules, and state transfer to the installed app. These values and UX items are archival context, not current Play publishing gates. The page was updated June 24, 2026; its retirement notice takes precedence over the later historical checklist. |
| [Material Design icons (old “get app” destination)](https://m2.material.io/icons/) | Redirected to a general Material icons catalog with little extractable body; the old icon/button-label requirement is preserved as historical. |
| [Google Play Instant UX best practices](https://developer.android.com/topic/google-play-instant/best-practices/apps) | The page carries the same December 2025 retirement notice and shows an update date of June 24, 2026. Historic guidance includes a meaningful landing screen, letting users finish tasks before asking them to install, delaying sign-in, preserving state after install, avoiding extra splash screens, keeping instant/installed UI consistent, clear install buttons, removing nonfunctional sections, and distinguishing first-party from external offers. Kept as a legacy UX summary only. |
| [Verify and maintain deep links](https://support.google.com/googleplay/android-developer/answer/12463044) | A descendant of the UX guide's deep-link resource. The current Play Console page checks domain association, manifest intent filters, and web-URL coverage, and can publish link patches for existing versions. Patches do not automatically carry to future versions; manifest changes still require a new release. Account data requires sign-in. |
| [Android App Links guide](https://developer.android.com/training/app-links) | A child of the deep-link page. It explains general deep links versus verified Android App Links and recommends App Links for URLs on a developer's website. Updated October 16, 2026; a current technical starting point for migrating retired Instant links. |
| [Google Play services Instant API reference](https://developers.google.com/android/reference/com/google/android/gms/instantapps/package-summary) | The technical checklist also links to this Instant API package summary. The reference remains accessible, but the retirement notice says Instant APIs no longer work; an available reference page does not mean the service is still functional. The full package tree is not recursively audited. |

The Help page also has an Other Programs sidebar and Help Community/Contact us footer links; they are separate from the Instant Apps policy body. Account-only Console content, all sidebar descendants, the entire WebView API member tree, and all UX-guide outbound links were not exhaustively followed; per-URL status is in the source ledger.

## Migration checks for legacy projects

These are engineering migration suggestions, not new Google Play policy clauses:

1. Search modules, Gradle dependencies, manifests, and runtime code for Instant App/Instant API references and ensure the app no longer calls disabled services.
2. Replace instant-experience entry points with installed-app routing, a web fallback, or ordinary Android App Links. Verify `assetlinks.json`, intent filters, Play Console deep-link diagnostics, and browser outcomes.
3. If Smart Lock is still used, migrate sign-in using current Credential Manager guidance and verify credential save, user sign-out, and account switching.
4. Recheck the current Developer Program Policy, data/permission requirements, and the app's actual features; do not use the historical Instant Apps checklist as a substitute for a current policy review.

This topic is a bilingual historical summary of the retired policy page, official technical checklist, and UX guide. It is not a full-text mirror and does not imply that legacy Instant Apps can still be published or run.
