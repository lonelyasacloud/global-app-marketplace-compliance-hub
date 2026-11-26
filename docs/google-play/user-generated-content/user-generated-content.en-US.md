---
id: google-play.user-generated-content
platform: google-play
language: en-US
authority: normative
status: current
kb_checked_at: 2026-10-24
review_due: 2027-01-24
regions: [global]
topics: [ugc, moderation, social, child-safety, ai-content, content-rating]
snapshot_id: play.user-generated-content
snapshot_package: "GooglePlay-KnowledgeBase-2026-10-24-review.zip"
coverage_status: "detailed-summary"
source_url: "https://support.google.com/googleplay/android-developer/answer/9876937?hl=en"
source_url_zh: "https://support.google.com/googleplay/android-developer/answer/9876937?hl=zh-Hans"
effective_date: "current-policy"
---

# User-Generated Content (UGC) and Moderation

> **Import note (Google batch 3).** The body is the paraphrased summary from the already separated 2026-10-24 Google Play knowledge-base snapshot (`play.user-generated-content`, reviewed 2026-10-24). It is not a verbatim copy of an official page. The English official source is the source of truth. `kb_checked_at` is the review date recorded in the snapshot source file; this import did not re-open the live official pages. Phrases such as “this knowledge base,” “this library,” and “local topic” describe coverage inside that snapshot, not the set of pages imported into this repository. Relative snapshot links to topics, link graphs, ledgers, or CSVs that are not in this repository are kept as text mentions. Relative links that target the Google batch 1 and 2 topics or these nine batch 3 topics point at the hub files. On 2026-10-24 the snapshot reread the English and official Simplified Chinese (`zh-Hans`) UGC policy and moderation-guidance bodies. Google warns that the Chinese text may be AI-translated and inaccurate, so material requirements were cross-checked against the current English policy. The exact `hl=zh-CN` route was inaccessible. That failure is not a policy change. The Chinese hub text is the snapshot paraphrase, not Google’s published Chinese page text. No future-effective date is recorded for this UGC policy. The UGC policy is `normative`. The moderation best-practices article is operational guidance and does not waive the policy’s interaction examples. AI-generated content is a related but separate rule. This topic stays separate from Inappropriate Content, age restrictions, and content ratings.

**Reviewed: 2026-10-24.** This page summarizes Google Play's UGC policy and moderation best practices. On October 24, the English and official Simplified Chinese (`zh-Hans`) bodies were reread. Google warns that the Chinese text may be AI-translated and inaccurate, so material requirements were cross-checked against the current English policy and applicable Play Console rules. UGC is content users contribute that is visible or accessible to at least some app users. The policy also covers specialized browsers or clients that direct users to a UGC platform. This is a bilingual paraphrase, not a verbatim mirror of the policy.

## Scope and responsibility

- Policies cover content an app displays or links to, including ads and UGC hosted or linked by the app. Public developer-account materials shown on Play, such as the developer name and listed website landing page, are also in scope.
- UGC apps must maintain effective, ongoing moderation that is reasonable for the type of content and interaction. UGC does not need to be the app's primary feature to create moderation duties.
- Terms of Use/user rules and a Privacy Policy serve different purposes. Users must be able to read and accept the posting rules before creating or uploading UGC. The rules must define and prohibit objectionable content and behavior consistently with Google Play policies.

## Reporting, blocking, and timely action

The policy describes moderation tools that depend on the interaction model:

| UGC experience | Policy example |
| --- | --- |
| A defined group formed through verification or offline registration | Provide in-app functionality to report content and users. |
| One-to-one interactions, such as direct messaging, tagging, or mentions | Provide in-app functionality to block users. |
| Publicly accessible UGC | Provide in-app functionality to report content and users, and to block users. |
| UGC in augmented reality | Include objectionable AR content and sensitive anchoring locations, such as restricted areas or private property, in moderation and reporting. |

Supplementary guidance recommends that report and block controls be clear, easy to find, and clearly labeled, and that developers take appropriate action promptly. Avoid a single ambiguous control that users cannot distinguish as “report” or “block.” As a practical baseline, support both reporting content/users and blocking users/content where the product experience calls for it; use the policy's examples to assess the minimum required for each interaction pattern.

Apps must also prevent paid features, rewards, and recommendations from encouraging objectionable behavior. Repeatedly ignoring reports, or developing a reputation for primarily hosting objectionable UGC, can lead to removal.

## Incidental sexual content: a narrow set of conditions

This is not a general adult-content exception. Sexual content may be considered “incidental” only in a UGC app that primarily provides non-sexual content and does not actively promote or recommend sexual content. All applicable conditions must be met:

1. Content is hidden by default behind a filter that takes at least two user actions to disable completely.
2. An appropriate age-screening system prevents children, as defined by the Families policy, from accessing the app. Do not prefill an adult birth date or instruct users to enter a particular age to bypass the restriction.
3. Play Console content-rating answers accurately reflect the app's UGC.
4. The app does not provide sexual content that is illegal under applicable law or any child-endangerment content. It does not promote, recommend, push, or prominently feature sexual content.

An app whose primary purpose is objectionable UGC, or that develops a reputation as a place where such content thrives, may be removed. Inappropriate Content and Child Endangerment rules still apply. “Incidental” does not make illegal, non-consensual, or child-exploitation content acceptable.

## Child safety, age, and content ratings

- Threats, harassment, and bullying in UGC—especially toward minors—require effective safeguards and ongoing action. Assess age, social features, discovery/recommendation, and report-response capacity.
- Anonymous-chat, random-chat, social, and dating apps must also check Child Safety Standards. Requirements include published child-safety rules, in-app feedback, action on known CSAM, legally required reporting, and a child-safety point of contact. See the [Age restrictions and child safety topic](../age-restricted-child-safety/age-restricted-child-safety.en-US.md).
- A child-inclusive target audience triggers additional Families requirements for content, SDKs/APIs, data, and ads. Mixed-audience age screens and ads shown to children must follow the relevant Families rules.
- Each new and active app needs an accurate IARC content rating. Submit a new questionnaire when UGC or feature changes affect the answers. Misrepresentation can lead to removal or suspension.

## AI-generated content is a related but separate rule

Generative AI apps must follow other Google Play policies, prevent restricted output (including content that harms children or enables deception), and provide an in-app reporting/flagging feature so users can report offensive output without leaving the app. Developers should use reports to improve filtering and moderation. Google's best-practices article also recommends filters/classifiers and references safety-testing frameworks. If AI output is posted, shared, or shown to other users, assess the real feature flow to determine whether UGC requirements also apply. See the standalone AI-Generated Content topic (snapshot: `ai-generated-content-en.md`, not imported in this repository) and its Chinese edition (snapshot: `ai-generated-content.md`, not imported in this repository) for scope, examples, and direct safety resources.

## Release and operations checklist

1. Inventory every type of content users can submit, share, comment on, message, embed, or browse, including UGC accessed through a third-party browser/client.
2. Show clear Terms of Use/community rules before posting and obtain acceptance. Cover prohibited content, reporting, and moderation actions.
3. Provide clear reporting and blocking controls appropriate to the product, then test that reports reach an accountable team and are handled promptly.
4. Assess whether search, recommendations, notifications, paid features, or rewards amplify harmful content or harassment. For AR, review anchoring-location risks too.
5. If sexual content is visible, check the incidental-content definition, default filtering, two-action opt-in, age screening, and accurate ratings. Illegal or child-endangerment content is never covered by this exception.
6. For child audiences, anonymous/random chat, social, and dating features, separately verify Families, Child Safety Standards, Restrict Minor Access, and applicable local law.
7. For generative AI, test input/output safety, provide in-app reporting, and update safeguards as abuse patterns and reports change.
8. Reassess policy scope, Console declarations, and IARC answers whenever content, audience, interaction, or monetization changes.

## Direct child links and related-page audit

| Parent page/branch | Opened targets | Relationship and coverage |
| --- | --- | --- |
| User Generated Content policy | [Child Endangerment](https://support.google.com/googleplay/android-developer/answer/9878809?hl=en), [Families Policies](https://support.google.com/googleplay/android-developer/answer/9893335?hl=en), [Target audience and app content settings](https://support.google.com/googleplay/android-developer/answer/9867159?hl=en), [Content Ratings](https://support.google.com/googleplay/android-developer/answer/9898843?hl=en) | English and `zh-Hans` bodies were fully read; all four policy destinations opened. The Chinese page carries an AI-translation accuracy warning, and the exact `zh-CN` route was inaccessible. A tracked age-screen click timed out, but the canonical target-audience body was read in full; three Chinese-page body icons are separately logged as media. |
| UGC moderation best-practices article | [Understanding moderation requirements and incidental sexual content in UGC apps](https://support.google.com/googleplay/android-developer/answer/12923286?hl=en) · [Simplified Chinese `zh-Hans`](https://support.google.com/googleplay/android-developer/answer/12923286?hl=zh-Hans) | Both bodies reread on October 24. They add pre-posting terms acceptance, discoverable/clearly labeled reporting and blocking, timely action, default hiding, and age screening. The article states broader in-app reporting/blocking expectations for UGC apps; the base policy gives examples for group, 1:1, public, and AR interactions. Do not treat those examples as an exemption from other applicable tools. All four normative direct targets opened. Of five English illustrative images, three timed out and two returned Cache miss; all five `zh-Hans` images returned Cache miss. Community, Contact us, and the Policy education heading click failed without exposing hrefs, so no target was guessed. On October 23, all 32 Policy education sidebar targets were clicked and mapped to URL audits and local bilingual topics; the Health Permissions FAQ returned Internal Error while its prior full-body audit remains. Target pages' own body links and deeper descendants are not recursively closed. |
| Policy Coverage | [Policy Coverage](https://support.google.com/googleplay/android-developer/answer/10146128?hl=en) | Opened; confirms scope over UGC/ads shown or linked by an app, public developer materials, and content ratings. |
| AI-generated content branch | [AI-Generated Content](https://support.google.com/googleplay/android-developer/answer/13985936?hl=en), [Best Practices to Safeguard AI-Generated Content](https://support.google.com/googleplay/android-developer/answer/16353813?hl=en) | Both bodies opened. AI policy requires restricted-output prevention and in-app reporting. All 10 direct safety-framework/provider links in the best-practices article were opened and classified below; they are not mandatory Play policies, and their descendants were not expanded. |
| Related content restrictions | [Inappropriate Content](https://support.google.com/googleplay/android-developer/answer/9878810?hl=en), [Learning more about Child Safety Standards](https://support.google.com/googleplay/android-developer/answer/14747720?hl=en) | Inappropriate Content opened. `14747720` was reopened in full on October 22, 2026; its scope, public standards, in-app feedback, CSAM response, and point-of-contact requirements are in the [child-safety topic](../age-restricted-child-safety/age-restricted-child-safety.en-US.md), with descendants under “Implementation guidance and child links.” |

### Direct body-link inventory for the UGC policy and moderation guidance (October 24, 2026)

The inventory below covers direct body links separately from sidebars. The English and `zh-Hans` moderation articles point to the same canonical policy destinations.

| Parent body | Direct target | UGC relationship and access result |
| --- | --- | --- |
| Moderation guidance | [User Generated Content policy](https://support.google.com/googleplay/android-developer/answer/9876937?hl=en) | Scope and interaction-dependent policy; full English and zh-Hans bodies read. |
| Moderation guidance | [Child Endangerment](https://support.google.com/googleplay/android-developer/answer/9878809?hl=en) | Child-harm boundary and safeguards; destination opened. |
| Moderation guidance | [Families Policies](https://support.google.com/googleplay/android-developer/answer/9893335?hl=en) | Child-audience rules for content, SDKs, data, and ads; destination opened. |
| Moderation guidance / UGC policy | [Target audience and app content settings](https://support.google.com/googleplay/android-developer/answer/9867159?hl=en) | Age-screening and audience guidance; canonical body and neutral-age-screen section read in full. |
| UGC policy | [Content Ratings](https://support.google.com/googleplay/android-developer/answer/9898843?hl=en) | UGC changes may affect rating answers; destination body opened. |
| Neutral-age-screen link in Chinese UGC policy body | [Tracked direct route](<https://support.google.com/googleplay/android-developer/answer/9867159?rd=1&visit_id=637661037575013539-1915084824>) | That click returned 400 Timeout fetching; the canonical `answer/9867159` body was fully read. The raw-route failure is distinct from canonical access. |
| English moderation-article illustrations 1–5 | [Image 1](https://lh3.googleusercontent.com/yCNOQUtlNDBcHfFCCLYhwlyYxBy9wMY3wp8723a68Tmk3lLbkmb6GhAgC7Yh_2_RcCM%3Dw895), [Image 2](https://lh3.googleusercontent.com/mZYbxuII4CcE2PA_D4SE04EOPBwTX-n7lHwnVK1EDFiGGSC4ZGvIkrUZYesjbfByHA%3Dw895), [Image 3](https://lh3.googleusercontent.com/EoJEKqImBlKVH-GJbvLkm5AavKvF70LGsqBnkE0rs3ZjBAJvpzM7Svf3R5jDxLlEiJk%3Dw895), [Image 4](https://lh3.googleusercontent.com/eevd7uud5VWBvKFJNMgJ4q-h8JXBbGJlM5CEwZhnhDavQf0TcMP6ZlPnX97PCfHQkg%3Dw450), [Image 5](https://lh3.googleusercontent.com/bMyqO4IFDEBVX5j-Exfhyitc4i2VDjGYmPJyqX9RUTzVGylbYg3BKY1Sng7vmjSjSLne%3Dw450) | Three targets timed out and two returned Cache miss; no pixels or policy text could be reviewed. |
| `zh-Hans` moderation-article illustrations 1–5 | [Image 1](https://lh3.googleusercontent.com/VWOrs04dcRpwglePWv53fMPtnDm9RnZWHqtuDJ7BvyVYEZWlVNQhsWAEFKg7jM36PA%3Dw895), [Image 2](https://lh3.googleusercontent.com/eDCpoQsLe6QcZcz453PVD36N36bT1kWabv50_4f8rvB3V13U-8pPZtTiHbMLECj_L2g%3Dw895), [Image 3](https://lh3.googleusercontent.com/hQhEO3NpA1uiYAgdVJI2ZGhOUvSjS7aPQDuazw_Fa0x_gNIWIAPwpYYq9Y4ojk2llGC_%3Dw895), [Image 4](https://lh3.googleusercontent.com/AQ5dh5TlFwW4lJUrqcflaYCWdWR6ZZS6kizJ4W4F-RV7QfXtQKxusGuVhJui-BrgRw%3Dw895), [Image 5](https://lh3.googleusercontent.com/FMHts1Osfr_4huK-1MGmevdMk6UsUbjTEpdehQzvqyIxWayHXqyY9SosQ8GtnD7m9RQ%3Dw895) | All five returned Cache miss; no pixels or policy text could be reviewed. |
| `zh-Hans` UGC-policy body icons 1–3 | [Icon 1](https://lh3.googleusercontent.com/BPsAL28eke0gFbFJduiZupJyY6uR5X7_JHR_3vev1cApatT5KLrReyskdlNZXRGFsg%3Dw60-h60), [Icon 2](https://lh3.googleusercontent.com/hnJIMKQ0lyssVbehdx4OCpjLHPBYy94NeG4dD-xZ40osbCjM8Lt3zS4P5JvA5Xsqig%3Dw30-h34), [Icon 3](https://lh3.googleusercontent.com/IfJhh8qlFSuw1U7A2DSeKi0B3jBYMC5fU0pGMUG40oyCU3urkOu4yGg0D24TkbUvwRk%3Dw40) | Tool returned image endpoints without reviewable pixels; recorded as visual assets only. |
| Community, Contact us, and Policy education heading controls; UGC-policy Contact us | No verifiable href exposed | Clicks returned Internal Error without target URLs; no URL was inferred from a control label. These are unresolved support/navigation entries, not policy text. |

**How the two policy layers fit:** The moderation article uses broader language requiring in-app reporting and blocking for UGC apps. The base policy gives examples by fixed-group, one-to-one, public-UGC, and AR experience. Read both together; do not treat those examples as a waiver for other applicable tools. Provide suitable reporting/blocking paths for content and users based on the actual interaction model.

### “Restricted Content” sidebar on the UGC policy page (navigation, not body requirements)

The page lists ten restricted-content entries. UGC is the current page; the other nine current policy targets were opened individually in this pass and mapped to existing bilingual topics. This sidebar is an adjacent-policy directory, not a set of additional requirements introduced by the UGC body. Deeper descendants remain governed by each topic's own source-audit status.

| Sidebar entry | Official target | Local bilingual topic and relationship |
| --- | --- | --- |
| Child Endangerment | [Policy page](https://support.google.com/googleplay/android-developer/answer/9878809?hl=en) | [Age restrictions and child safety](../age-restricted-child-safety/age-restricted-child-safety.en-US.md) · Child sexual exploitation, endangerment, and related safeguards. |
| Inappropriate Content | [Policy page](https://support.google.com/googleplay/android-developer/answer/9878810?hl=en) | [Inappropriate Content](../inappropriate-content/inappropriate-content.en-US.md) · Prohibited content and the narrow incidental-sexual-content conditions for UGC. |
| Financial Services | [Policy page](https://support.google.com/googleplay/android-developer/answer/9876821?hl=en) | Financial services and loans (snapshot: `financial-services-and-loans-en.md`, not imported in this repository) · Regulated features, declarations, lending, and regional requirements. |
| Real-Money Gambling, Games, and Contests | [Policy page](https://support.google.com/googleplay/android-developer/answer/9877032?hl=en) | Real-money gambling (snapshot: `real-money-gambling-en.md`, not imported in this repository) · Eligibility, licensing, geo/age limits, and responsible-gambling rules. |
| Illegal Activities | [Policy page](https://support.google.com/googleplay/android-developer/answer/9878877?hl=en) | Illegal activities (snapshot: `illegal-activities-en.md`, not imported in this repository) · Prohibits facilitating illegal conduct and requires market-law review. |
| User Generated Content | [Current policy page](https://support.google.com/googleplay/android-developer/answer/9876937?hl=en) | This topic · UGC scope, moderation, report/block tools, and incidental-content conditions. |
| Health Content and Services | [Policy page](https://support.google.com/googleplay/android-developer/answer/16679511?hl=en) | Health apps and Health Connect (snapshot: `health-apps-and-health-connect-en.md`, not imported in this repository) · Health features, medical claims, health data, and regulatory requirements. |
| Blockchain-based Content | [Policy page](https://support.google.com/googleplay/android-developer/answer/13607354?hl=en) | Crypto assets and NFTs (snapshot: `crypto-assets-and-nfts-en.md`, not imported in this repository) · Wallets, exchanges, tokenized assets, and NFT-game requirements. |
| AI-Generated Content | [Policy page](https://support.google.com/googleplay/android-developer/answer/13985936?hl=en) | AI-generated content (snapshot: `ai-generated-content-en.md`, not imported in this repository) · Restricted-output prevention and in-app reporting. |
| Age-Restricted Content and Functionality | [Policy page](https://support.google.com/googleplay/android-developer/answer/16302250?hl=en) | [Age restrictions and child safety](../age-restricted-child-safety/age-restricted-child-safety.en-US.md) · Core functions that must block minors. |

### Direct external links from the AI safety best-practices article

Google Play's AI safety article directly recommends the resources below. They are recorded to preserve the source chain; provider features and terms can change. They do not replace Play policy, and an SDK's built-in filtering alone does not establish Play compliance.

| Category | Page | Relationship to UGC/AI safety and audit status |
| --- | --- | --- |
| Safety framework | [Google Secure AI Framework (SAIF)](https://saif.google/secure-ai-framework) | Opened; maps AI risks and controls across data, infrastructure, model, and application components. |
| Safety testing | [OWASP GenAI Red Teaming Guide](https://genai.owasp.org/resource/genai-red-teaming-guide/) | Opened; organizes testing around evaluation, implementation, infrastructure, and runtime behavior. |
| Google developer resource | [Responsible Generative AI Toolkit](https://ai.google.dev/responsible) | Opened; covers system-level safety rules, design, model evaluation, filters/classifiers, and related tools. |
| Model/content-safety provider resources | [Microsoft AI Content Safety](https://azure.microsoft.com/en-us/products/ai-services/ai-content-safety), [OpenAI Safety best practices](https://developers.openai.com/api/docs/guides/safety-best-practices), [Anthropic Content moderation](https://platform.claude.com/docs/en/about-claude/use-case-guides/content-moderation), [AWS Responsible content moderation](https://docs.aws.amazon.com/solutions/responsible-content-moderation-with-ai-services-on-aws/), [Meta Responsible Use Guide](https://ai.meta.com/static-resource/responsible-use-guide/), [Salesforce Trusted AI](https://www.salesforce.com/artificial-intelligence/trusted-ai/), [Cohere Safety Modes](https://docs.cohere.com/docs/safety-modes) | All target pages were reached and recorded in the ledger. This table classifies the sources without turning provider guidance into Play requirements; their grandchildren were not traversed. |

Official Chinese UGC entry: [Simplified Chinese](https://support.google.com/googleplay/android-developer/answer/9876937?hl=zh-Hans). Both English and `zh-Hans` UGC-policy and moderation-guidance bodies were readable in this pass. Google flags the Chinese pages as potentially AI-translated and inaccurate; the exact `zh-CN` route was inaccessible. Three policy-page icons and ten moderation-article images across the two locales are itemized below; they are media, not policy text. The ten Restricted Content entries and 32 Policy education recommendations are navigation, separate from body links. Their destination pages' own links and deeper descendants retain their individual partial-coverage statuses; no recursive closure is claimed.

## Sources and related topics

- [User Generated Content policy](https://support.google.com/googleplay/android-developer/answer/9876937?hl=en) · [official Simplified Chinese page](https://support.google.com/googleplay/android-developer/answer/9876937?hl=zh-Hans)
- [UGC moderation and incidental sexual content guidance](https://support.google.com/googleplay/android-developer/answer/12923286?hl=en) · [official Simplified Chinese `zh-Hans`](https://support.google.com/googleplay/android-developer/answer/12923286?hl=zh-Hans)
- [AI-Generated Content](https://support.google.com/googleplay/android-developer/answer/13985936?hl=en) · [AI safety best practices](https://support.google.com/googleplay/android-developer/answer/16353813?hl=en)
- [Policy Coverage](https://support.google.com/googleplay/android-developer/answer/10146128?hl=en) · [Inappropriate Content](https://support.google.com/googleplay/android-developer/answer/9878810?hl=en) · [Content Ratings](https://support.google.com/googleplay/android-developer/answer/9898843?hl=en)
- [Age restrictions and child safety](../age-restricted-child-safety/age-restricted-child-safety.en-US.md) · Third-party SDK requirements (snapshot: `sdk-requirements-en.md`, not imported in this repository) · [User Data](../user-data/user-data.en-US.md)
