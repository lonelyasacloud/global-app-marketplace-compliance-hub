---
id: apple.age-ratings.values-and-definitions
platform: apple
language: en-US
authority: operational
status: current
kb_checked_at: 2026-11-09
review_due: 2027-02-09
snapshot_package: 2026-11-10
regions: [global, AU, BR, KR, VN]
topics: [age-rating, kids, regional, ugc]
editorial_note: "Snapshot checked 2026-11-09 (package 2026-11-10). No live re-check in this import. Age-rating help pages are cited in English and Simplified Chinese; the snapshot does not record a date lag between those two help pages. Shared Location and Dating and Relationships deadlines come from the English news notice of 2026-11-02. Chinese wording of that notice is an editorial summary, not a claim that Apple published this Chinese text. The separate App Review Guidelines language gap (English 2026-10-16 vs Simplified Chinese 2026-06-08) is disclosed in the guidelines summary."
---

# Age Rating Values and Definitions

## What this page is for

Age rating is required App information in App Store Connect. Developers answer whether content, features, and controls are present and how often they appear. Apple generates the rating from those answers. It is not a marketing label the developer chooses freely. Ratings help parents and guardians manage children’s experiences through parental controls, and help users understand app content.

This page is an operational summary of the official definitions. It is not legal advice on age rating. Follow the live App Store Connect questionnaire and the competent authority in each region. The knowledge-base check date is 2026-11-09 (package dated 2026-11-10). This import did not reopen the live Help pages.

Official definitions:

- [Age ratings values and definitions (English)](https://developer.apple.com/help/app-store-connect/reference/app-information/age-ratings-values-and-definitions)
- [Age ratings values and definitions (Simplified Chinese)](https://developer.apple.com/cn/help/app-store-connect/reference/app-information/age-ratings-values-and-definitions)

The snapshot does not record an update-date gap between these two Help pages. Do not copy the App Review Guidelines lag (English October 16, 2026; Simplified Chinese official page June 8, 2026) onto these Help pages. That guidelines gap is in the [guidelines summary](../app-review-guidelines/guidelines-summary.en-US.md).

## Questionnaire topics

The table summarizes content signals. The final rating comes from the full questionnaire and Apple’s calculation. One item does not map mechanically to one rating.

| Category | What to identify |
| --- | --- |
| In-app controls | Parental controls and age-assurance mechanisms, including a declared age range, age estimation, and document or other verification. |
| Features | Unrestricted web access, UGC, social media, social media unavailable to people under 13, messaging and chat, and advertising. Social media includes discovery, promotion, reposting, likes, and comments on UGC, not only posting. |
| Mature themes | Crude humor, horror or fear themes, and use of or references to tobacco, alcohol, or drugs. |
| Medical or wellness | Medical or treatment information and guidance. Health and wellness topics such as diet, exercise, or calorie tracking. |
| Sexual content or nudity | Mature or suggestive themes, sexual content or nudity, and explicit sexual content and nudity. |
| Violence | Cartoon or fantasy violence, realistic violence, graphic or sadistic realistic violence, and guns or other weapons. |
| Chance-based activities | Gambling, simulated gambling, contests, and loot boxes. Gambling uses real money or in-game currency convertible to real money. Simulated gambling does not. A loot box is a purchasable container that awards random virtual items. |
| Shared Location | Sharing a person’s real-world location with another person or group. |
| Dating and Relationships | Dating or relationship connections between real people, or with a virtual companion that engages the user in sexual or romantic content. |

## November 2026 content descriptors

The dates and rating effects below summarize Apple’s English notice [Upcoming: New age rating content descriptors](https://developer.apple.com/news/?id=yxkh08us) (November 2, 2026). **Chinese wording of this section on the paired page is an editorial summary of that English notice, not a claim that Apple published this Chinese text.**

App Store Connect adds **Shared Location** and **Dating and Relationships** to the age-rating questionnaire on **November 16, 2026**. The declarations are required when submitting an app update or changing the age-rating questionnaire. Every app must complete them by **January 12, 2027**.

- **Dating and Relationships** triggers a minimum **18+** rating.
- **Shared Location** has a region-dependent minimum. In Brazil, Apple states **A16** for Shared Location and **A18** for Dating and Relationships. **Region-sensitive.**
- If a Brazil app has a legitimate reason for a lower rating, for example location sharing designed for parents and children, the developer can request an official rating from Brazil’s Ministry of Justice and Public Security (MJSP). After verification, Apple displays that official Brazil rating on the App Store. MJSP page: [Classificação](https://www.gov.br/mj/pt-br/assuntos/seus-direitos/classificacao-1). That page is a regulatory source, not Apple rule text.

Inventory before you answer:

- [ ] Every feature that shares live or precise real-world location with another person or group.
- [ ] Real-person dating or relationship matching, and any virtual companion that engages users in sexual or romantic content.
- [ ] The questionnaire answer, expected global rating, Brazil rating, and any regulator evidence, recorded before the next submission.

These checks are implementation notes.

## Ratings on current OS versions

The snapshot records the current ordinary scale as **4+, 9+, 13+, 16+, 18+, and Unrated**, for devices running OS 26 or later. The table only collects typical signals listed on the page.

| Rating | Typical signals listed |
| --- | --- |
| 4+ | No objectionable content. The app may still include parental controls, age assurance, UGC, chat, ads, and occasional contests. |
| 9+ | Occasional crude humor or horror, health or wellness themes, occasional suggestive themes, cartoon or fantasy violence, weapons, or loot boxes. |
| 13+ | Social-media features or features unavailable under 13. Frequent crude humor, horror, or substance references. Occasional medical information, sexual content or nudity, realistic violence, or simulated gambling. Frequent cartoon violence, weapons, or contests. |
| 16+ | Unrestricted web access, frequent medical or treatment information, or frequent mature or suggestive themes. |
| 18+ | Frequent substance-related content, sexual content or nudity, or realistic violence. Gambling or frequent simulated gambling. |
| Unrated | Explicit sexual content or nudity, or graphic and sadistic realistic violence. That content cannot be published on the App Store. |

## Regional ratings

Regional rules can add local labels, conditions, or review materials on top of Apple’s global rating. One global rating is not a complete answer for every storefront. **Region-sensitive.**

| Region | Summary | What to do |
| --- | --- | --- |
| Australia | The page distinguishes display rules for the current system and older systems. The Australian classification authority may require a correction or a regional rating. Current-page mappings include some social-media, loot-box, and simulated-gambling content. | For games with loot boxes or simulated gambling, check local classification rules and App Review notices, then provide the requested materials and resubmit. |
| Brazil | Apple’s self-rating is distinct from an official Ministry of Justice and Public Security (MJSP) rating. When an official rating exists, the storefront shows that regional rating. Fixed-odds gambling requires a valid SPA license, entered and documented in App Review information. | Before release of a gambling app, verify that the license is valid, the scope matches, and the review attachments are complete. A self-rating does not establish authorization to operate. |
| Korea | Current questionnaire mappings include All, 12+, 15+, and 19+. If the GRAC rating and the Apple questionnaire result differ, an RCN or a Korean rating override may be required. | For games, entertainment apps, and apps with frequent or intense simulated gambling, check the GRAC number and the App Store Connect submission requirements. |
| Vietnam | The page lists 00+, 12+, 16+, and 18+, mapped from features, mature themes, medical content, sexual content or nudity, violence, and chance-based activities. | Recheck the local decree and the questionnaire mapping for the Vietnam storefront. Do not copy the Apple global rating across unchanged. |

## Historical ratings on older systems

Use this section only when you still support OS versions that display the older scale. Newer systems use the current scale above and the live questionnaire at submission time.

The legacy global scale is **4+, 9+, 12+, 17+, and Unrated**. Australia, Brazil, France, and Korea may also show regional labels. Do not treat legacy 12+ / 17+ as the same numbers as the current 13+ / 16+ / 18+ scale.

## Relation to announcements

This page is for answering the questionnaire and for the meaning of each answer.

- The November 2, 2026 [content-descriptor notice](https://developer.apple.com/news/?id=yxkh08us) adds Shared Location, Dating and Relationships, and the January 12, 2027 completion deadline. Chinese wording of that notice in this hub is an editorial summary.
- The snapshot records that the September 9, 2026 notice on accepting submissions built with the latest OS links to the July 9, 2026 [age-rating questionnaire and social-media notice](https://developer.apple.com/cn/news/?id=tlur8uvi). That notice explains how social-media capabilities affect the questionnaire, the product-page descriptor, and the Time Allowances category. The definitions of social media, UGC, age assurance, under-age restrictions, and chat on this page are the terms used for that decision. The snapshot does not give a separate URL for the September 9 notice, so none is added here.
- The snapshot records that the August 12, 2026 Korea-rating announcement also points at this definitions page and adds the GRAC RCN override flow. The age-rating source does not include that announcement’s URL, so none is added here.

## Pre-submission checks

- [ ] Inventory public UGC, discovery and recommendation, likes and comments, direct and group messaging, ads, embedded browsers, age assurance, and parental controls.
- [ ] Answer from actual content and frequency, not only from the primary category, the intended audience, or store marketing copy.
- [ ] Review mature themes, medical guidance, sexual content, violence, weapons, gambling and simulated gambling, contests, and loot boxes.
- [ ] After the new fields go live, complete Shared Location and Dating and Relationships. Finish every app by 2027-01-12, and keep evidence for Brazil A16/A18 or the MJSP official-rating path.
- [ ] Check the current scale and the legacy scale against the target OS versions, and check regional rules for each target storefront.
- [ ] Where they apply, prepare the GRAC RCN, the Brazil SPA gambling license, regulator ratings, and App Review notes or attachments.
- [ ] Keep the questionnaire answers, content inventory, regional documents, and review notices. Reassess after features or content change.

These checks are implementation notes. Use them with the [pre-submission checklist](../pre-submission/submission-checklist.en-US.md).

This page does not replace the [English definitions](https://developer.apple.com/help/app-store-connect/reference/app-information/age-ratings-values-and-definitions) or the live questionnaire in the account.
