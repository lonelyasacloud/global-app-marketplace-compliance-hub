---
id: google-play.account-ownership-transfer
platform: google-play
language: en-US
authority: operational
status: current
kb_checked_at: 2026-10-24
review_due: 2027-01-24
regions: [global]
topics: [account-transfer, developer-account, ownership, identity-verification, play-console]
snapshot_id: play.account-ownership-transfer
snapshot_package: "GooglePlay-KnowledgeBase-2026-10-24-review.zip"
coverage_status: "detailed-summary"
source_url: "https://support.google.com/googleplay/android-developer/answer/10788890?hl=en"
source_url_announcement: "https://support.google.com/googleplay/android-developer/answer/16926792?hl=en"
source_url_announcement_alias: "https://support.google.com/googleplay/android-developer/answer/16911971?hl=en"
source_url_owner_transfer: "https://support.google.com/googleplay/android-developer/answer/16909862?hl=en"
source_url_identity_verification: "https://support.google.com/googleplay/android-developer/answer/10841920?hl=en"
source_url_app_transfer: "https://support.google.com/googleplay/android-developer/answer/6230247?hl=en"
source_url_policy_blog: "https://android-developers.googleblog.com/2026/04/giving-users-clearer-choice-and-everyone-a-safer-more-trusted-app-ecosystem.html"
source_url_transfer_form: "https://support.google.com/googleplay/android-developer/contact/general_contact"
effective_date: "official feature required from 2026-05-27, which has passed; announcement 30-day wording kept separate; no 2027-01-27"
---

# Google Play developer account ownership transfer

> **Import note (Google batch 7).** The body is the paraphrased summary from the already separated 2026-10-24 Google Play knowledge-base snapshot (`play.account-ownership-transfer`, reviewed 2026-10-24). It is not a verbatim copy of an official page. The English official source is the source of truth. `kb_checked_at` is the review date recorded in the snapshot source file; this import did not re-open the live official pages. Phrases such as “this knowledge base,” “this library,” and “local topic” describe coverage inside that snapshot, not the set of pages imported into this repository. Relative snapshot links to topics, link graphs, ledgers, or CSVs that are not in this repository are kept as text mentions. Relative links that target the Google batch 1–6 topics or these twelve batch 7 topics point at the hub files. Reviewed 2026-10-24. Both language files cite English `hl=en` Help URLs. The snapshot says the Simplified Chinese Help route was inaccessible. The Chinese hub text is an editorial paraphrase. That access failure is not a policy change. The policy was announced on 2026-04-15. The official blog says ownership changes must use the official feature starting 2026-05-27. That date has passed. The announcement’s “at least 30 days” wording and the blog’s feature-switch date stay separate. The announcement’s original target `answer/16911971` redirects to Play Console Requirements. It is not a separate policy. No 2027-01-27 date is recorded. This page is an operational ownership workflow. It does not replace single-app transfer. A monetizing Personal account that cannot use this flow is directed to app transfer instead. Signed-in eligibility cannot be verified from the public Help page.

**Reviewed October 24, 2026.** This page summarizes the policy boundary and current public workflow for changing account ownership. It is a standalone navigation topic within [Play Console Requirements](../play-console-requirements/play-console-requirements.en-US.md), based on the English official text; the Simplified Chinese Help route was inaccessible in this review. It is not an application form and cannot verify eligibility, verification progress, or an individual case in the signed-in Play Console.

## First distinguish the two transfer types

| Goal | Use this process | Main boundary |
| --- | --- | --- |
| Transfer ownership of the entire developer account | Play Console **Users and permissions → Manage → Make account owner** | Only the current account owner can initiate it. The recipient is an existing account user and must meet eligibility and identity-verification requirements. |
| Move one or more apps only | [App transfer process](https://support.google.com/googleplay/android-developer/answer/6230247?hl=en) | This is a separate app-migration request involving active source/target accounts, a registration transaction ID, signing, payments, and integrations. See [Play Console Requirements](../play-console-requirements/play-console-requirements.en-US.md#app-transfer-prerequisites-and-effects). |

Do not hand over the entire developer account just to migrate an app. If a business change truly requires transferring account control, moving only an app does not substitute for the account-ownership process.

## Policy and date

Google Play requires transparent and accountable ownership of developer accounts. Legitimate business reasons such as acquisitions, organizational restructuring, and personnel changes may require a formal transfer. Both the transferor and transferee remain responsible for account actions during the transfer, including the transition period. Developers must use the official Play Console flow.

- **Prohibited conduct:** Buying, selling, or leasing developer accounts through third-party marketplaces or other illegitimate means is prohibited. Informal transfers through shared login credentials are also not allowed.
- **Effective/workflow date:** The policy was announced on April 15, 2026. Google's official blog says account ownership changes must use the official feature starting **May 27, 2026**. That date has passed. The announcement's “at least 30 days” and the blog's feature-switch date describe different timing statements; use the current policy and account-specific notices for execution.
- **Announcement link today:** The announcement's original Account Transfer destination, [answer/16911971](https://support.google.com/googleplay/android-developer/answer/16911971), now redirects to [Play Console Requirements](https://support.google.com/googleplay/android-developer/answer/10788890). The current policy text is in that Help page's **Account Transfers** section. The [ownership-transfer Help article](https://support.google.com/googleplay/android-developer/answer/16909862?hl=en) describes the steps.

## Eligibility and common blocks

| Situation | Current Help-page explanation |
| --- | --- |
| Direct ownership switch is available | Organization accounts and Personal accounts that do not monetize apps may transfer ownership after required information and applicable identity checks are complete. |
| Direct switch is unavailable | A Personal developer account that monetizes apps is currently ineligible for this direct process. Create another developer account and transfer the apps separately. |
| Account/process may be blocked | Outstanding verification or good-standing issues; a pending Payments Profile change or account-type switch; an upload-key reset or app transfer in progress; or a prospective owner who already owns another Play Console developer account. Console gives account-specific eligibility feedback. |
| Current owner cannot be reached | Self-service is currently unavailable. Contact Support through Play Console Help. Without Console access, use the [public issue form](https://support.google.com/googleplay/android-developer/contact/general_contact); it can be read publicly, but filing and case handling require account information. |

## Stages of an ownership change

1. **The current owner initiates.** The owner signs in to Play Console, opens **Users and permissions**, then chooses **Make account owner** on the recipient's **Manage** page. The recipient must already be a user on the account; Console checks owner eligibility.
2. **Choose the account-type relationship.** An Organization account must specify whether the recipient belongs to the same organization or a new entity. A same-organization transfer can reuse existing account details, but the recipient needs admin access to the required Google Payments profiles. A different entity selects a payments profile for identity verification. For a Personal account, the recipient selects or creates a profile used only for identity verification.
3. **Submit and enter the seven-day security hold.** The current owner and admins with access to all apps receive email; team members receive a Console notification. Any account user can cancel during the hold, which is intended to surface mistakes or unauthorized takeovers.
4. **The recipient completes the final setup.** After seven days, the recipient receives an invitation to finish. Once the recipient starts the final transfer, other account users can no longer cancel it. The setup wizard may request a payments profile; organization type, size, and phone (website is optional); contact name; OTP-verified contact email and phone; and the developer phone and email shown to users.
5. **Complete any additional identity check.** Google may ask the recipient to submit identity documents and send follow-up instructions for uploading them. Unsupported documents are rejected. The Help page does not promise one review outcome or timeline for every country and account.

### Responsibility and security during the seven-day hold

The hold is an account-security measure; it is not Google's approval of an account sale or business transaction. The transferor and transferee remain responsible for following Play policies and for account actions throughout the transition. Before finalization, confirm the recipient's identity, organizational relationship, payments-profile access, and pending verification tasks. If the request is unauthorized, cancel it during the hold and contact Support.

## Direct sources and child-link relationships

| Page/target | Role in this topic and review status |
| --- | --- |
| [Account Transfer announcement](https://support.google.com/googleplay/android-developer/answer/16926792?hl=en) → [original policy link answer/16911971](https://support.google.com/googleplay/android-developer/answer/16911971) → [current Play Console Requirements](https://support.google.com/googleplay/android-developer/answer/10788890?hl=en) | The announcement introduces the change. Its original target now redirects to the current requirements page, whose `Account Transfers` text covers ownership transparency, the required formal process, transition responsibility, prohibited informal marketplace transfers, and the separate app-migration route. |
| [Transferring ownership of a Play Console developer account](https://support.google.com/googleplay/android-developer/answer/16909862?hl=en) | Full body reopened October 24, 2026. It expands the UI steps, organization/personal profile branches, seven-day hold, final wizard, eligibility, and blocks. The account form and status still require sign-in. |
| [Verify your developer identity information](https://support.google.com/googleplay/android-developer/answer/10841920) | Direct target for the transfer wizard's data and verification requirements. This target has a separate identity/contact-information topic; regional document selectors and some support descendants remain incomplete. |
| [Transfer apps to a different developer account](https://support.google.com/googleplay/android-developer/answer/6230247?hl=en) | The alternative when a monetizing Personal account cannot transfer ownership directly, and the route when only apps need to move. Its body and 18 exposed article-level targets have URL access states; deeper API/service descendants remain partial. |
| [Report an Issue form](https://support.google.com/googleplay/android-developer/contact/general_contact) | Publicly lists an account/support route. The project read its visible fields and instructions but did not submit it. The Help article's separate “contact support” click returned Internal Error without exposing a verifiable destination URL. |

The ownership article's ten generic sidebar entries are tracked separately from body links. This page follows the high-impact policy, identity-verification, and app-transfer children, but does not recursively expand every regional identity document, Console form, and external descendant. Current per-URL results are in the source audit (snapshot: `source-page-audit.csv`, not imported in this repository).

## Related local topics

- [Play Console Requirements: account eligibility, identity information, and app migration](../play-console-requirements/play-console-requirements.en-US.md)
- Android Developer Verification [Android developer verification](../android-developer-verification/android-developer-verification.en-US.md)
- [Google Play Developer Program Policy](../developer-program-policy/developer-program-policy.en-US.md)
