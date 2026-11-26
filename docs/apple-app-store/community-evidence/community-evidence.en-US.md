---
id: apple.community.evidence
platform: apple
language: en-US
authority: community
status: current
kb_checked_at: 2026-11-09
review_due: 2027-02-09
snapshot_package: 2026-11-10
regions: [global]
topics: [community, review, testing]
editorial_note: "Community-evidence layer from the snapshot checked 2026-11-09 (package 2026-11-10). Not an Apple official rule. Quora was blocked by robots.txt in that pass and is excluded. This import did not re-check forums or live official pages. English guidelines in the snapshot are dated 2026-10-16; the Simplified Chinese official guidelines page shows 2026-06-08."
---

# Community Evidence and Failure Patterns

## Evidence level

This page is **community evidence**. It is not an Apple official rule. It cannot support a compliance conclusion on its own, and it cannot override the [guidelines summary](../app-review-guidelines/guidelines-summary.en-US.md) or the live official page. Community reports are used only to discover test scenarios and troubleshooting clues. Check the official clause first, then decide whether to turn the clue into a test case.

The knowledge-base check date is 2026-11-09 (package dated 2026-11-10). This import did not reopen forums or the live official pages.

| Tier | Use |
| --- | --- |
| A | Apple Guidelines, App Store Connect Help, the agreement, and Apple’s official announcements. These may enter the normative layer. They are not restated here; use the official page and the imported topic. |
| B | Apple-employee tips or official technical replies on Apple Developer Forums. These may inform operational suggestions. They are still not guideline text. |
| C | Repeated experience on Reddit, CSDN, or developer forums. Convert only into test scenarios or troubleshooting clues. |
| D | Material about bypassing review, hiding functionality, evading automated review, or wrapper apps aimed at passing review. Do not turn it into an execution plan. This knowledge base does not record those methods. |

## Experience that can become test cases

Each item below is a failure pattern the snapshot describes as recurring in community reports. Treat it as tier C. A passing test does not replace the official rule.

### 1. Accounts and review access

Community reports often describe a Guideline 2.1 rejection where the app did not crash and the reviewer could not complete the flow. Use that to design tests. Do not treat it as a rule by itself:

- Whether the demo account needs email verification, an invitation, MFA, or a region permission
- Whether enough sample data already exists
- Whether more than one account role is available
- Whether the backend depends on a VPN, an internal network, an IP allowlist, or a time window
- Whether the account can expire, lock, or hit a rate limit

Point these clues back to Apple’s [complete-review requirements](https://developer.apple.com/help/app-review/before-submitting-for-review/complete-review/). The operational summary is the [review workflow](../review-workflow/review-workflow.en-US.md).

### 2. Metadata and assets

Recurring reports include stale localized screenshots, missing device-size assets, an old App Preview, an IAP promotion image, and screenshots that do not match the current app. Tests to consider:

- Every localization
- Every device size, including View All Sizes
- Screenshots, previews, and What’s New against the current binary
- IAP Display Name, Description, Review Screenshot, and Promotion image
- Prices, third-party platforms, old UI, or claims that cannot be verified

Whether an asset meets the current rule is decided on the English [App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/). In this snapshot the Simplified Chinese official page still shows June 8, 2026, and does not override a later English rule.

### 3. UGC and AI

A recurring rejection pattern in community reports is a missing report, block, filter, content-removal, minor-restriction, or post-notice remediation flow. Map those clues back to guidelines 1.2, 1.3, and 5.1 and to the age-rating rules. See the [guidelines summary](../app-review-guidelines/guidelines-summary.en-US.md) and [age ratings](../age-ratings/age-ratings.en-US.md). Do not generalize one rejection letter into a universal Apple rule.

### 4. Privacy supply chain

Forum reports often mention ITMS-91061, a missing privacy manifest, an undeclared Required Reason API, or a third-party SDK that triggers a permission string. Those are community troubleshooting clues. This snapshot does not contain a Privacy Manifest or Required Reason API topic, and this page does not treat those codes or reports as a re-checked Apple rule.

Point the clues back to:

- [Privacy manifest](https://developer.apple.com/documentation/bundleresources/adding-a-privacy-manifest-to-your-app-or-third-party-sdk)
- [Required Reason API](https://developer.apple.com/documentation/bundleresources/describing-use-of-required-reason-api)
- [User Privacy and Data Use](https://developer.apple.com/app-store/user-privacy-and-data-use/)

Detailed Privacy Manifest and Required Reason API topics are not in this snapshot package and are not imported.

## How to use Reddit and CSDN

- Use them only to learn what might happen
- Do not expand one app’s rejection reason into a general Apple rule
- Verify the official clause before turning a report into a test case
- Keep the source, publication date, app type, and remaining uncertainty
- Drop or downgrade anything about bypassing review, hiding functionality, evading automated review, or wrapper apps aimed at passing review. Do not write it into an execution plan

## Quora

In this pass, Quora pages were blocked by robots.txt and could not be read or checked reliably. Quora content is not in the knowledge base. A specific link supplied later is only an unverified clue until its text is read and mapped back to an official source.
