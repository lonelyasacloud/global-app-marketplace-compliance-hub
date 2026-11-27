---
id: operations.pre-submission.quick-check
platform: shared
language: en-US
authority: operational
status: current
kb_checked_at: 2026-11-26
review_due: 2027-02-26
regions: [global]
topics: [pre-submission, quick-check]
---

# Pre-submission Quick Check

This is a release gate, not an approval guarantee. Record a reason for every not-applicable item.

## P0: Check first

- [ ] The app launches and completes core flows on real devices, the minimum supported OS, and the latest supported OS.
- [ ] Demo accounts, MFA, invitations, backend services, and review credentials work during the review window.
- [ ] The in-app privacy policy is reachable and matches the real data flows.
- [ ] Apple App Privacy Details or Google Play Data Safety matches the app, backend, and every third-party SDK.
- [ ] Paid features, subscriptions, restore, refunds, and regional pricing are reproducible.
- [ ] The build, store metadata, screenshots, previews, and released experience match.
- [ ] No hidden, dormant, post-review-only, or undocumented functionality exists.
- [ ] Every sensitive permission has a visible core use case, minimum scope, and supporting evidence.

## Apple focus

- [ ] App Review Information includes purpose, demo credentials, hardware, region differences, and reproduction steps.
- [ ] Privacy Manifest, Required Reason APIs, and the third-party SDK inventory are checked.
- [ ] ATT, sign-in, account deletion, IAP, subscriptions, and external-purchase rules are checked for each applicable storefront.
- [ ] Age rating, Kids, UGC, health, finance, VPN, gambling, and other regulated capabilities have evidence.
- [ ] Screenshots, previews, assets, name, description, and prices match the current build.
- [ ] If China mainland distribution is selected, ICP filing and permit applicability and the current App Store Connect compliance status are checked; the community-recorded IAP-only support path is case-specific and does not replace formal filing.

## Google Play focus

- [ ] The Data Safety form matches runtime collection, sharing, deletion, and SDK behavior.
- [ ] SMS, call log, contacts, location, photo/video, accessibility, and other sensitive permissions have eligibility and declaration evidence.
- [ ] Target API, Play Billing, content rating, target audience, and Families requirements are checked.
- [ ] New personal developer-account testing requirements have been verified.
- [ ] Play Console App content, policy declarations, and release-track status are recorded.

## Evidence record

For each check, record the source URL, review date, owner, test environment, evidence location, and the reason for any not-applicable item.

## Official sources

- [Apple App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/)
- [Apple App Store Connect Help](https://developer.apple.com/help/app-store-connect/)
- [Google Play Policy Center](https://play.google.com/about/developer-content-policy/)
- [Google Play Console Help](https://support.google.com/googleplay/android-developer/)

## Related pages

This page remains the cross-platform quick gate. The detailed Apple list is the [pre-submission checklist](../../apple-app-store/pre-submission/submission-checklist.en-US.md). The short Apple brief is [review readiness](../../apple-app-store/app-review-guidelines/review-readiness.en-US.md). For the China mainland storefront, also use [ICP filing and the community-recorded support path](../../regions/china/apple-app-store-release.en-US.md). Use the lists together.

Google Play detail lives on [Data safety](../../google-play/data-safety/data-safety.en-US.md), [User Data](../../google-play/user-data/user-data.en-US.md), [sensitive permissions](../../google-play/sensitive-permissions/sensitive-permissions.en-US.md), [target API](../../google-play/target-api/target-api-level.en-US.md), [payments](../../google-play/payments/payments-and-subscriptions.en-US.md), and the [release workflow](../../google-play/publishing/play-release-workflow.en-US.md).
