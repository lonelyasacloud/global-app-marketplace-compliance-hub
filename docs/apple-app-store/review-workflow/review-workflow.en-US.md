---
id: apple.review.workflow
platform: apple
language: en-US
authority: operational
status: current
kb_checked_at: 2026-11-09
review_due: 2027-02-09
snapshot_package: 2026-11-10
regions: [global]
topics: [review, submission, status, deadlines]
editorial_note: "Imported from the snapshot checked 2026-11-09 (package 2026-11-10). No live re-check in this import. Dates below are the snapshot's recorded deadlines, not a new verification. review_due is the hub recheck date and is separate from Apple deadlines."
---

# Review Materials, Submission Objects, and Timing

This page summarizes official Help material on submission objects, statuses, and kinds of dates. Its evidence level is **operational**. It does not replace the current App Store Connect UI and does not guarantee a review duration.

The knowledge-base check date is 2026-11-09 (package dated 2026-11-10). This import did not reopen these Help pages. In the same snapshot, the English App Review Guidelines were updated on October 16, 2026, and the Simplified Chinese official guidelines page still shows June 8, 2026. This page’s workflow notes come from Help. When a step also restates a guideline duty, the English guidelines remain the policy baseline. The language gap is recorded in the [guidelines summary](../app-review-guidelines/guidelines-summary.en-US.md).

## Complete review information

Prepare the submission so a reviewer can examine it completely, stably, and reproducibly. A username and password alone are not enough.

| Area | Preparation | Common failure signal |
| --- | --- | --- |
| App concept | Explain the purpose, business model, audience, and restricted regions | The reviewer cannot tell what the app does or how it makes money |
| Accounts | Active demo credentials, one account per role, and any code, MFA, or invitation steps | Sign-in fails, the account is expired, sample data is missing, or the role is too limited |
| Backend | Keep the production or review environment reachable during review, without a VPN or an internal-only network | Empty screens, failed requests, or a build that works only in development |
| Hardware | When pairing is required, provide a physical-device video and the reproduction steps | A screen recording cannot show the device interaction |
| Qualifications | Provide licenses or partnership evidence for finance, medical, crime-reporting, and similar features. **Region-sensitive** | Review asks for more documents, or the provider cannot be verified |
| New features | Explain the change, entry points, accounts, test devices, and regional differences | Guideline 2.1 information is needed, or the feature cannot be found |
| IAP and subscriptions | Explain product IDs, the navigation path, Sandbox testing, restore, and any special configuration | The reviewer cannot find the product or complete the purchase |

The checkbox list is the [pre-submission checklist](../pre-submission/submission-checklist.en-US.md).

## Submission objects

App Review can examine these objects separately:

- App version
- In-App Purchase
- Auto-renewable subscription and subscription group
- In-App Event
- Custom Product Page
- Product page optimization test
- Apple-hosted asset pack
- Game Center leaderboard, achievement, challenge, and activity

Submit the app version for each platform separately. A platform generally has at most one submission that includes an app version and one submission that contains only other items at the same time. An approved app does not mean every attached item is approved.

Source: [Overview of submitting for review](https://developer.apple.com/help/app-store-connect/manage-submissions-to-app-review/overview-of-submitting-for-review).

## Review statuses

```text
Ready for Review
  ↓
Waiting for Review
  ↓
In Review
  ├─ Accepted
  ├─ Rejected
  └─ Unresolved Issues
       ↓
    Reply / Fix / Resubmit
```

The status changes what can still be edited. After Waiting for Review, some screenshots, previews, or In-App Event metadata may be locked. A rejected attached item can be fixed on its own or removed from the submission.

Status definitions: [App and submission statuses](https://developer.apple.com/help/app-store-connect/reference/app-information/app-and-submission-statuses/). Evidence and appeal handling after a rejection: [rejection and appeals](../../operations/rejection-and-appeals/README.md). That page is a hub procedure, not Apple’s appeal text.

## Kinds of dates

Record each time requirement on its own. Do not collapse them into one date:

- Announcement date
- Source-page update date
- Effective date
- Date the App Store Connect field becomes available
- Mandatory completion deadline
- Case-specific notice deadline
- Internal due date
- Next knowledge-base review date (2027-02-09 on this page)

Dates already recorded in the snapshot:

| Item | Date | Status | Source recorded in the snapshot |
| --- | --- | --- | --- |
| New age-rating fields become available | From 2026-11-16 | Upcoming | [Age-rating descriptor notice](https://developer.apple.com/news/?id=yxkh08us) |
| Every app completes the new age-rating declarations | 2027-01-12 | Mandatory deadline | Same notice |
| Taiwan iOS/iPadOS storefront commission for standard IAP and paid apps changes to 26% | Effective 2026-10-31 | In effect, **that storefront only** | [Taiwan storefront notice](https://developer.apple.com/news/?id=w9mxlhek) |
| iOS and iPadOS SDK 27, and the iOS 15 deployment target | From April 2027 | Upcoming requirement | [Submit your apps and games](https://developer.apple.com/app-store/submitting/) and [Upcoming Requirements](https://developer.apple.com/news/upcoming-requirements/) |
| Review queue time | The snapshot does not record a day count. Apple publishes an average reference, not a guarantee | Planning signal | No separate day-count page was recorded |
| 14-day compliance notice | Applies only when that app receives the notice | Case-specific | The snapshot does not treat one public page as a universal 14-day rule |

Re-open the official pages in this table before a release. A snapshot date is not the acceptance state or field toggle in the current account.

## After submission

Available paths include:

- Reply in App Review Resolution Center
- Add review materials
- Change metadata without a new binary, when that path is available
- Bug Fix Submission
- Expedited Review
- Appeal
- A one-on-one App Review appointment

A one-on-one appointment can help explain an issue. It does not pre-approve an app or a feature. Each submission is still judged under the guidelines in effect at review time. The policy baseline is the [English App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/).

## Official sources

- [Overview of submitting for review](https://developer.apple.com/help/app-store-connect/manage-submissions-to-app-review/overview-of-submitting-for-review)
- [Provide information for a complete review](https://developer.apple.com/help/app-review/before-submitting-for-review/complete-review/)
- [App and submission statuses](https://developer.apple.com/help/app-store-connect/reference/app-information/app-and-submission-statuses/)
- [Submit your apps and games](https://developer.apple.com/app-store/submitting/)
- [Upcoming Requirements](https://developer.apple.com/news/upcoming-requirements/)

This page is an operational summary of those Help pages.
