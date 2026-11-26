---
id: google-play.play-console-user-permissions
platform: google-play
language: en-US
authority: operational
status: current
kb_checked_at: 2026-10-22
review_due: 2027-01-22
regions: [global]
topics: [play-console, users, permissions, account-access, audit]
snapshot_id: play.console-user-permissions
snapshot_package: "GooglePlay-KnowledgeBase-2026-10-24-review.zip"
coverage_status: "detailed-summary"
source_url: "https://support.google.com/googleplay/android-developer/answer/9844686?hl=en"
source_url_zh: "https://support.google.com/googleplay/android-developer/answer/9844686?hl=zh-CN"
effective_date: "current-as-reviewed on 2026-10-22; no 2027-01-27"
---

# Play Console Users, Permissions, and Access Auditing

> **Import note (Google batch 7).** The body is the paraphrased summary from the already separated 2026-10-24 Google Play knowledge-base snapshot (`play.console-user-permissions`, reviewed 2026-10-22). It is not a verbatim copy of an official page. The English official source is the source of truth. `kb_checked_at` is the review date recorded in the snapshot source file; this import did not re-open the live official pages. Phrases such as “this knowledge base,” “this library,” and “local topic” describe coverage inside that snapshot, not the set of pages imported into this repository. Relative snapshot links to topics, link graphs, ledgers, or CSVs that are not in this repository are kept as text mentions. Relative links that target the Google batch 1–6 topics or these twelve batch 7 topics point at the hub files. Reviewed 2026-10-22. The English Help article was opened. The `hl=zh-CN` URL could not be accessed, so the Chinese hub text is an editorial paraphrase and is not a line-by-line check of a Chinese official page. That access failure is not a policy change. The source records `effective_date: current-as-reviewed`. No 2027-01-27 date is recorded. An organization-verification PDF is offered in Simplified Chinese, English, Japanese, Korean, and Brazilian Portuguese. The snapshot opened the entry and did not reproduce the PDF’s internal steps. The developer-account settings directory page fetch failed. This page is operational Console access guidance. It is not a Developer Program Policy and it does not prove an account’s live grants. Play app permissions declarations remain a separate topic.

**Reviewed: October 22, 2026.** The full English [Add developer account users and manage permissions](https://support.google.com/googleplay/android-developer/answer/9844686?hl=en) Help article was opened and summarized. The Simplified Chinese URL could not be accessed in this review, so the Chinese page is a bilingual paraphrase of the English source, not a claim of line-by-line translation parity. This is an operational Play Console access guide, not a standalone Developer Program Policy or proof of any account's live grants.

## Access levels and scope

| Level | What the Help article says | Important boundary |
| --- | --- | --- |
| Account owner | The first account registered in Play Console; full access; can invite/remove users and manage permissions. | Only the owner can link the sales Payments profile and access/edit Play Console Payments settings. |
| Admin | Holds Admin (all permissions), with access at account or selected-app scope; can invite/remove users and manage permissions. | A global Admin can manage access expirations and review the Activity log. An app-level Admin cannot remove users with global access. Some account-level actions remain owner-only. |
| User | Can receive different account-level or app-level grants. | Cannot invite users or edit other users' permissions. |

Account permissions apply to all apps in the developer account, usually including apps added later. App permissions apply only to selected apps. Some grants exist only at one scope; do not infer scope from the label alone.

## Key permissions and their boundaries

| Permission | What it allows | Important boundary |
| --- | --- | --- |
| Admin (all permissions) | Invite/remove users, manage permissions, and receive all other permissions. | Treat as a high-privilege grant and limit it to people who administer the account. An app-level Admin remains limited by app scope. |
| View app information (read-only) | Read app information and associated Play Games Services projects. | Does not include financial data; this is an app-level grant. The account-level equivalent includes all-app information and bulk reports. |
| View app quality information (read-only) | Read Android vitals, pre-launch reports, and basic artifact, track, and release information. | Read-only; it does not let users change information. |
| View app information and download bulk reports (read-only) | Read information about all apps and download bulk reports. | Account-level; financial data is separate. Creating a new app also requires this grant together with the draft-app creation grant. |
| Edit/delete draft apps; create/edit/delete draft apps | Edit or delete draft apps; the account-level version can also create drafts. | Draft grants do not publish apps or start a release rollout. Creating apps at account level also requires read-only app information access. |
| Manage policy declarations | Edit and submit declarations such as Data safety and permission declarations, and view related notifications. | This access does not waive the underlying policies or guarantee approval. |
| View financial data; view financial data, orders, and cancellation survey responses | View financial/sales reports, the Purchases API, and associated Play Games Services revenue; the account version also covers orders and written cancellation-survey responses. | Financial access is separate from ordinary read-only app information. Reports and survey responses require the corresponding financial grant at the right scope. |
| Manage orders and subscriptions | View orders, issue refunds, and cancel subscriptions. | Does not grant access to aggregate financial reports; that separately requires View financial data. |
| Release to production, exclude devices, and use Play App Signing | Create/edit/roll out production releases; unpublish/republish; exclude devices; use Play App Signing. | This is the permission that explicitly includes production publishing. |
| Release apps to testing tracks | Upload drafts, create/roll out test releases, modify OBB files, edit release notes for apps not active in production, and upload Internal App Sharing APKs. | Does not allow production publishing. |
| Manage testing tracks and edit tester lists | Change internal/open/closed testing configuration and manage tester lists. | Does not allow production publishing; tester management and release rollout are distinct grants. |
| Manage store presence | Edit store listings and experiments, pricing, in-app products, distribution/content ratings, promotions, and related settings. | Does not allow device exclusions in the device catalog. |
| Reply to reviews | Reply to Google Play reviews and change the contact information used in suggested replies. | Users can still view ratings/reviews without this grant, but cannot reply. |
| Managed Google Play private apps | Create, edit, and publish private apps for an organization. | Does not include internal testing-track management or public-app publishing. |
| Google Play Games Services | Edit or publish Play Games Services projects. | Account-level only. The user also needs separate access to the Google Developers Console project. Some game-financial-data access requires both the account-level and linked app-level financial grants. |

## Invitations, permission groups, expiration, and removal

- Invitees must sign in with the same email address entered by the Admin/owner. To change the address, the inviter must resend the invitation.
- Invitations expire if not accepted and used to sign in within 30 days; the Admin must resend them.
- Individual users and permission groups can have an expiration date. An individual grant without one remains active; a group grant without one does not expire until the user or group is removed.
- Owners/Admins can grant account-level or app-level access individually or through permission groups. A single user can hold grants at both scopes.
- Before removing access or shortening its duration, confirm that the account will retain the people needed for publishing, review, support, and financial tasks.

## Exporting users and reviewing account changes

An account owner can export a user CSV from Users and permissions. The table can be filtered by permission, app, invitation status, email domain, or name. The CSV includes email, invitation/access status, invitation and expiration times, app permissions, and account permissions. Admins see only the app data in their scope. The official [user-list export article](https://support.google.com/googleplay/android-developer/answer/10019561?hl=en) maps CSV permission codes to Console labels.

Use this CSV as an access-review aid: check Admin, production-release, financial, order, and policy-declaration grants first; then check expirations for temporary collaborators. Review account-level and app-level columns separately. This is an operational recommendation, not a new Google Play policy obligation.

The [Activity log article](https://support.google.com/googleplay/android-developer/answer/9859273?hl=en) says account owners can view changes over the lifetime of the developer account. The page displays up to 200 changes by default and supports filtering by app and changed item; entries show the app, changed item, change details, user email, and date/time in the local time zone. The link redirects to legacy URL `answer/6053184`; the redirect is recorded in the source ledger.

## Direct links in the article: destination and relationship

| Article link | Destination and relation to this page | Access/coverage |
| --- | --- | --- |
| [Link a Google Play developer account to a Payments profile](https://support.google.com/googleplay/android-developer/answer/9875344) | Merchant setup for paid apps/IAP. A Play Console account and Payments profile can only be linked once; changes generally require a new Payments profile/developer account and an app transfer. | Opened; redirects to `answer/3092739`. See [Play Console Requirements](../play-console-requirements/play-console-requirements.en-US.md). |
| [Activity log](https://support.google.com/googleplay/android-developer/answer/9859273?hl=en) | Account-change auditing, complementing the owner/global Admin access notes above. | Opened; redirects to `answer/6053184`; its filters and record fields are summarized above. |
| [Publish private apps](https://support.google.com/googleplay/android-developer/answer/9874937) | Managed Google Play private-app publishing, Organization IDs, organization visibility, and limits on changing private apps to public. | Full body opened; see [Play Console Requirements](../play-console-requirements/play-console-requirements.en-US.md). |
| [Play Console home](https://play.google.com/console) / [Users and permissions](https://play.google.com/console/developers/users-and-permissions) | Account-only pages for inviting users and setting permissions. | The home link redirects to the Play business landing page; Users and permissions redirects to sign-in. A public page fetch cannot verify live account grants. |
| [Google Developers Console](https://console.developers.google.com/) | Separate access control for Play Games Services projects. | Click redirected to sign-in; access must also be granted by the project administrator. |
| [Google Payments Center](https://payments.google.com/payments/) | Report access must be granted separately in Payments Center; it is separate from Play Console permissions. | Redirects to an account page with no public Help body to archive. |
| [Play Academy account basics course](https://playacademy.exceedlms.com/student/path/6420) | Supplementary account-management training. | Entry opened; lesson content requires sign-in and could not be confirmed from the public page. |
| [Help community](https://support.google.com/googleplay/android-developer/community?hl=en), [Contact us](https://support.google.com/googleplay/android-developer/gethelp), images, and in-page anchors | Support/feedback, interface illustration, and navigation within the article. | Community returned Cache miss; Contact us redirects to account support; in-page anchors are not new policy pages. |

## “Set up your developer account” Help sidebar (15 items, including this article)

This is the [Set up your developer account directory](https://support.google.com/googleplay/android-developer/topic/7072535), separate from the article's permission requirements. The directory itself could not be fetched, but the other 14 targets were clicked and mapped to account-profile/identity topics in this library. Opening the sibling pages does not mean all their descendants have been recursively closed.

| Sidebar target | Relation to user permissions | Local reading path / status |
| --- | --- | --- |
| [Developer account registration payment methods and receipts](https://support.google.com/googleplay/android-developer/answer/9875040) | Registration-fee payment methods, receipts, and transaction history. | Opened; account-registration/payment context is in [Play Console Requirements](../play-console-requirements/play-console-requirements.en-US.md). |
| [Choose a developer account type](https://support.google.com/googleplay/android-developer/answer/13634885) | Personal/Organization choice; financial, health, approved VPN, and government cases should use an Organization account. | Opened; see [Play Console Requirements](../play-console-requirements/play-console-requirements.en-US.md). |
| [Contact information requirements](https://support.google.com/googleplay/android-developer/answer/10840893) | Public developer details and verified private Google contact email/phone. | Opened; see [Play Console Requirements](../play-console-requirements/play-console-requirements.en-US.md). |
| [View and manage account information for verified accounts](https://support.google.com/googleplay/android-developer/answer/13634081) | Applies only to accounts verified under Play Console Requirements; only the owner can change developer-account information. | Opened; cross-linked to [Play Console Requirements](../play-console-requirements/play-console-requirements.en-US.md) and Developer verification (snapshot: `android-developer-verification-en.md`, not imported in this repository). |
| [Verify accounts created before September 2023](https://support.google.com/googleplay/android-developer/answer/14177239) | Legacy verification workflow and historical rollout deadlines. | Opened; the historical timeline is not an account's current personal deadline. Check Console; see Developer verification (snapshot: `android-developer-verification-en.md`, not imported in this repository). |
| [Verify developer identity information](https://support.google.com/googleplay/android-developer/answer/10841920) | Identity/contact details, Payments profile, and verification sequence. | English article opened; see Developer verification (snapshot: `android-developer-verification-en.md`, not imported in this repository) and [Play Console Requirements](../play-console-requirements/play-console-requirements.en-US.md). |
| [Organization verification guide](https://support.google.com/googleplay/android-developer/answer/15574489) | PDF guide to legacy verification for organizations, offered in Simplified Chinese, English, Japanese, Korean, and Brazilian Portuguese. | Entry opened; language/purpose recorded; PDF internal links and steps were not reproduced individually. |
| [Create and manage an Account Group](https://support.google.com/googleplay/android-developer/answer/10627869) | Associated account groups and program eligibility; group membership does not transfer app or financial permissions. | Opened; see [Play Console Requirements](../play-console-requirements/play-console-requirements.en-US.md). |
| [Export a list of users with account access](https://support.google.com/googleplay/android-developer/answer/10019561) | CSV user/permission auditing. | Opened and summarized; see the “Exporting users and reviewing account changes” section above. |
| [Create or update your developer profile](https://support.google.com/googleplay/android-developer/answer/9873827) | Optional public developer-brand page; at least one app must be published. | Opened; it does not grant account permissions. Check the official page for current asset specs and propagation times. |
| [Required information to create a developer account](https://support.google.com/googleplay/android-developer/answer/13628312) | Identity, contact, and payment details required for Personal/Organization registration. | Full body opened; see Developer verification (snapshot: `android-developer-verification-en.md`, not imported in this repository). |
| [Keeping developer account information up to date](https://support.google.com/googleplay/android-developer/answer/13634888) | Maintain legal identity, public profile, and contact data to avoid account restrictions. | Full body opened; see [Play Console Requirements](../play-console-requirements/play-console-requirements.en-US.md). |
| [Manage email recipients](https://support.google.com/googleplay/android-developer/answer/15771712) | Admins can send policy, payments/tax, tips, and survey emails to organization contacts without granting Play Console sign-in access. | Opened; recipients are not Play Console users. Do not grant broader account access just to deliver notifications. |
| [Update identity details managed by a Payments profile](https://support.google.com/googleplay/android-developer/answer/16260648) | Owners can update legal name/address in the Payments profile; country, account type, and D-U-N-S changes generally require a new verified profile. | Opened; related to the payment-profile and identity sections in [Play Console Requirements](../play-console-requirements/play-console-requirements.en-US.md). |

## Operational review suggestions (not standalone policy clauses)

1. Grant the narrowest account or app scope for each job; consider app-level access for collaborators working on only one app.
2. Review Admin, production release, financial data, order/refund, and policy-declaration access separately. Read-only app access does not include financial data.
3. Set expirations for temporary access; revisit users, permission groups, and notification recipients when people leave or change roles.
4. Check for accidental account-level access when a user should only see app-specific data. Review Payments Center and Google Developers Console access separately.
5. Verify testing-release and production-release grants independently; draft-app, test-track, tester-management, and production permissions are distinct.

## Related topics

| Topic | Relationship |
| --- | --- |
| [Play Console Requirements](../play-console-requirements/play-console-requirements.en-US.md) | Developer accounts, payments profiles, verification, and pre-release requirements. |
| [Testing, Review, and Release Workflow](../publishing/play-release-workflow.en-US.md) | Testing tracks, production release, review status, and permissions needed for these actions. |
| [Play Console permissions declaration and review](../permissions-declaration/permissions-declaration.en-US.md) | Manage policy declarations enables editing declarations; it does not change restricted-permission review rules. |
| [Payments and Subscriptions](../payments/payments-and-subscriptions.en-US.md) | Financial-report, order, and cancellation-survey access in its commercial context. |

## Coverage limits

The current English permissions article, its parseable body links, and the 15-item Help sidebar were checked. Console, Payments, and Developers Console workflows still require sign-in. Play Academy lessons, internal links in the PDF guide, and every descendant of the 14 sibling pages were not recursively exhausted here. Permission labels, account state, and Console UI can change; check the current official article and target account before acting.
