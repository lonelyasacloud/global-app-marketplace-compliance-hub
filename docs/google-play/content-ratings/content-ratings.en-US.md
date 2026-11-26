---
id: google-play.content-ratings
platform: google-play
language: en-US
authority: operational
status: current
kb_checked_at: 2026-10-23
review_due: 2027-01-23
regions: [global]
topics: [content-ratings, target-audience, ads, iarc, families, store-listing]
snapshot_id: play.content-ratings
snapshot_package: "GooglePlay-KnowledgeBase-2026-10-24-review.zip"
coverage_status: "detailed-summary"
source_url: "https://support.google.com/googleplay/android-developer/answer/9859655?hl=en"
source_url_zh: "https://support.google.com/googleplay/android-developer/answer/9859655?hl=zh-CN"
---

# Google Play Content Ratings, Target Audience, and Ad Suitability

> **Import note (Google batch 3).** The body is the paraphrased summary from the already separated 2026-10-24 Google Play knowledge-base snapshot (`play.content-ratings`, reviewed 2026-10-23). It is not a verbatim copy of an official page. The English official source is the source of truth. `kb_checked_at` is the review date recorded in the snapshot source file; this import did not re-open the live official pages. Phrases such as “this knowledge base,” “this library,” and “local topic” describe coverage inside that snapshot, not the set of pages imported into this repository. Relative snapshot links to topics, link graphs, ledgers, or CSVs that are not in this repository are kept as text mentions. Relative links that target the Google batch 1 and 2 topics or these nine batch 3 topics point at the hub files. The snapshot YAML `reviewed_on` is 2026-10-23. The English opening line says reviewed 2026-10-22, and the Chinese opening line says 2026-10-23. Those two snapshot dates are not treated as a policy change. The Simplified Chinese page was inaccessible in that review; the Chinese hub text is a paraphrase of the English source, not a checked Chinese official page. That access failure is not a policy change. No future-effective Play date is recorded for the rating rules. The IARC requirement on the policy-summary page is `normative`. The questionnaire, target-audience, and Console steps are operational and do not replace Families rules, age restriction, or ad suitability.

**Reviewed: 2026-10-22.** This topic summarizes the English Play Console Help requirements for content ratings and their main policy/operational links. The Simplified Chinese page was inaccessible in this review; the Chinese topic is a paraphrase of the English source. Regional rating authorities independently assign ratings from the developer's questionnaire. One market's label cannot stand in for every territory, and a content rating does not replace a target-audience declaration or age restriction.

The August 2017 announcement's “Content rating guidelines” link currently opens the [Content Ratings policy-summary page](https://support.google.com/googleplay/android-developer/answer/9898843?hl=en). It states that every app must have an IARC content rating; developers must accurately complete the Play Console questionnaire for each new and existing app and resubmit it when content/features change; unrated apps may be removed; and ads must not be significantly more mature than the app's main content. It links to the [Ads policy, including its inappropriate-ad requirements](https://support.google.com/googleplay/android-developer/answer/9857753?hl=en) and the [detailed content-ratings Help article](https://support.google.com/googleplay/android-developer/answer/9859655?hl=en). These pages serve as a policy overview and an operational guide; the full policy takes precedence in case of conflict. The current `answer/9878810` URL is Inappropriate Content, not the ad-policy destination linked from this summary.

## Distinguish three declarations and controls

| Item | Purpose | Does not replace |
| --- | --- | --- |
| Content-rating questionnaire | Produces familiar local age/content labels from the app's actual content; ratings help with search/browse filtering, minor access controls, and some program eligibility checks. | Target-age declarations, Families requirements, ad suitability, or local law. |
| Target audience and app content | Declares the age groups the app was actually designed for. Selecting children triggers additional Families, child-ad SDK, and neutral-age-screen requirements. | A broad reach strategy; do not select age groups the app was not designed and made suitable for. |
| Restrict Minor Access / age restriction | Limits users identified as minors from finding, downloading, or purchasing apps designed only for adults or required to be age-restricted. Existing installers may still use the app but cannot renew subscriptions or make new purchases. | A high content-rating label by itself; developers must enable the control in Console and follow the related policy. |

## When to complete or update the questionnaire

Play requires a content-rating questionnaire for new submissions, existing apps on Play that lack a rating, and updates whose changed content or features affect answers. Describe the app accurately and completely; misrepresentation can lead to rejection or suspension. Multiple rating authorities assign results using their own methods and regional standards.

Basic workflow:

1. In Play Console, open **Policy → App content**, then start the content-rating questionnaire under “Target audience and content.”
2. Enter an email for IARC correspondence, select a category, and answer each content question accurately. You can save a draft while completing sections; only one questionnaire draft can exist per app at a time.
3. Review the calculated regional ratings on the Summary page and submit. Edit answers or start a new questionnaire if needed.
4. Review the submitted questionnaire and ratings under App content. Reassess the answers after changing app content or features.
5. To challenge a rating authority's decision, use the appeal link in its rating-certificate email. Use IARC's contact channel for other inquiries.

The calculated Summary rating may differ from the rating shown to Play users. Authorities may override a result after review. Local law may require a market-specific rating. Rating icons are trademarks of their respective authorities and must follow the authority's usage guidelines.

A July 2025 policy announcement clarified that the rating questionnaire evaluates the app's content, not ads, additional user agreements, or privacy practices. Ad suitability remains a separate Ads-policy check. See the [July 10, 2025 announcement](https://support.google.com/googleplay/android-developer/answer/16296680?hl=en) and the announcement KB summary (snapshot: `../google-play-announcement-resources-en.md`, not imported in this repository).

## Ads and associated offers must match the app rating

Ads and related offers shown in an app are treated as part of that app. They must match its content rating even if the app itself complies with policy. For example, an offer that promotes the download of a mature-rated app may still be inappropriate for an app with a lower rating.

- Confirm with the ad provider that campaigns show creatives suitable for the app's rating. For AdMob, configure the maximum ad content rating and blocking controls.
- AdMob supports account-level and per-app maximum ratings. A per-app setting overrides the account default, while an SDK setting on an ad request may override the interface configuration. Rating levels are cumulative: selecting T also allows lower levels.
- Families apps have stricter ceilings: the system sets G for primarily child-directed apps and at most PG for mixed-audience apps. Interface settings may be overridden, and ads to children still need to come from an applicable self-certified SDK.
- For real-time bidding, review/rate ad creatives before delivery or use only approved self-certified sources.

Related topics: Ads and Promotion (snapshot: `ads-and-advertising-en.md`, not imported in this repository), [Age Restrictions and Child Safety](../age-restricted-child-safety/age-restricted-child-safety.en-US.md), and [Ratings, Reviews, and Installs](../user-ratings-reviews-installs/user-ratings-reviews-installs.en-US.md).

## Regional rating systems: one app can receive different results

Google Play lists rating authorities, their territories, and the separate systems used for games and apps. Authorities apply their own standards; the mapping below reflects the Help page checked on this date and may change with local law and policy.

| Rating authority/system | Territories and scope listed by Play Help | Common labels/boundaries on the page |
| --- | --- | --- |
| ESRB | A group of markets in the Americas, including the US, Canada, Mexico, and many Central/South American markets. | E, E10+, T, M, AO; rating categories may be accompanied by content descriptors and interactive elements. |
| PEGI | A listed group of countries in Europe and the Middle East. | PEGI 3, 7, 12, 16, 18; variable-content portals may also show “Parental Guidance Recommended.” |
| USK | Germany. | USK 0, 6, 12, 16, 18. |
| Australian Classification Board (ACB) | Australia; the Help page says ACB ratings apply to games, while other apps use the “Other countries” category. | G, PG, M, MA15+, R18+; advisory ages and legally restricted classes are different. |
| ClassInd | Brazil. | Livre/All ages, 6, 10, 12, 14, 16, 18. |
| GRAC | Games in South Korea; the page says apps use Google Play Rating instead. | All, 12, 15, 19. |
| Generic IARC | Other territories not represented by a participating authority. | 3+, 7+, 12+, 16+, 18+. |
| Google Play Rating | Apps (excluding games) in South Korea, plus a separate rating table for Russia. | Korea apps: 3+, 7+, 12+, 16+, 19+; Russia: 3+, 7+, 12+, 16+, 18+. |

Google Play's page also lists the ESRB and PEGI country groups. ESRB includes Antigua and Barbuda, Argentina, Bahamas, Barbados, Belize, Bolivia, Canada, Chile, Colombia, Costa Rica, Cuba, Dominica, Dominican Republic, Ecuador, El Salvador, Greenland, Grenada, Guatemala, Guyana, Haiti, Honduras, Jamaica, Mexico, Nicaragua, Panama, Paraguay, Peru, Saint Kitts and Nevis, Saint Lucia, Saint Vincent and the Grenadines, Suriname, Trinidad and Tobago, the United States, Uruguay, and Venezuela. PEGI includes Albania, Andorra, Austria, Belgium, Bosnia and Herzegovina, Bulgaria, Croatia, Cyprus, Czech Republic, Denmark, Estonia, Finland, France, Greece, Hungary, Iceland, Ireland, Israel, Italy, Kosovo, Latvia, Liechtenstein, Lithuania, Luxembourg, North Macedonia, Malta, Moldova, Monaco, Montenegro, the Netherlands, Norway, Poland, Portugal, Romania, San Marino, Serbia, Slovakia, Slovenia, Spain, Sweden, Switzerland, Turkey, the United Arab Emirates, the United Kingdom, and Vatican City.

If an authority refuses classification in a territory, the app/game cannot be distributed there. Play Console displays “Refused Classification,” and Google Play removes the item only in that territory. Appeal through the link in the IARC email.

## Direct links and destination relationships

The ten links in the Help article's opening contents list are in-page anchors to sections of the same article. Other policy and operational destinations are grouped below. Illustrative rating images, questionnaire mockups, generic feedback forms, global site navigation, and account sign-in controls are not policy clauses.

| Direct destination | Content and relationship | Review status |
| --- | --- | --- |
| [Content Ratings policy summary](https://support.google.com/googleplay/android-developer/answer/9898843?hl=en) | Direct target of the August 2017 announcement. Requires an IARC rating for each app, accurate questionnaire answers updated after relevant content changes, and ads no more mature than app content. | Full body opened; IARC, ad-policy, and detailed procedure destinations cross-checked. Five Help sidebar topics are treated as navigation. |
| [Target audience and app content settings](https://support.google.com/googleplay/android-developer/answer/9867159?hl=en) | Target age selection, age suitability, Families triggers, neutral age screens, personal data, ad SDKs, and adult-access restrictions. | Body opened; also covered in the [Age Restrictions and Child Safety topic](../age-restricted-child-safety/age-restricted-child-safety.en-US.md). |
| [Families policy topic](https://support.google.com/googleplay/android-developer/topic/9877766?hl=en) | Families requirements when children are included in the target audience. | Help request timed out; cross-reference the existing Families/child-safety summaries. |
| [Families Self-Certified Ads SDK program](https://support.google.com/googleplay/android-developer/answer/12955712?hl=en) | Lists self-certified SDKs/versions for child-directed ads and explains mixed audiences, neutral age screens, developer responsibility, and list changes. | Body opened; it says new applications are paused and existing participant requirements are unchanged. Recheck the live SDK version list before release. |
| [Ads policy](https://support.google.com/googleplay/android-developer/answer/9857753?hl=en) and [AdMob maximum ad content rating](https://support.google.com/admob/answer/7562142?hl=en) | The former covers ad content/rating and disruptive or deceptive ads; the latter explains account/app/ad-request setting precedence, estimated impact, and Families overrides. | Both opened; see the Ads topic (snapshot: `ads-and-advertising-en.md`, not imported in this repository) for Play requirements. |
| [Developer Program Policy](https://play.google/developer-content-policy/) and [Developer Distribution Agreement](https://play.google/developer-distribution-agreement.html) | General policy constraints and contractual terms; content ratings also need to match local law. | Both already have bilingual entries in the knowledge base. |
| Ad and privacy declarations described in [Prepare your app for review](https://support.google.com/googleplay/android-developer/answer/9859455?hl=en), [App access instructions](https://support.google.com/googleplay/android-developer/answer/9815348?hl=en), and [Play Console App content](https://play.google.com/console/app/app-content/summary) | Before declaring the target audience and content, developers need to address ad presence, app-access instructions, and a privacy policy; Console is the actual submission surface. | Prepare body opened and summarized; App access target was blocked by the automated fetch; Console route redirected to sign-in. |
| [IARC homepage](https://www.globalratings.com/), [Ratings Definitions](https://www.globalratings.com/ratings-definitions/), and [contact page](https://www.globalratings.com/contact-us/) | The homepage routes developers to process, participants, storefronts, FAQ, and institutional information; Definitions explains regional labels; Contact provides general inquiries and rating-authority contact routes. | Reopened October 23, 2026. The homepage has six primary navigation pages plus Definitions and Contact; its headline totals use different scopes from the About page and are excluded from compliance conclusions. The Contact form says submitted personal data is transferred to the United States. Its nine authority destinations and the Taiwan legal branch are mapped below. |
| [Rating authority sites](https://www.esrb.org/), [Australian Classification](https://www.classification.gov.au/), [PEGI](https://www.pegi.info/), [USK](https://www.usk.de/iarc/), [ClassInd](https://www.justica.gov.br/seus-direitos/classificacao), and [GRAC](https://www.grac.or.kr/english/) | Local rating systems and official classification explanations. | Direct Help-page clicks: ESRB and ACB opened; PEGI returned 503, USK a cache miss, the legacy ClassInd URL 502, and GRAC was firewall-blocked. Current/related authority links from IARC definitions are tracked below. These are external references, not additional Play rules. |
| [Legacy IARC display-guidelines URL](https://www.globalratings.com/display.aspx) | Linked guidance for displaying rating icons. | Returned 404. Do not treat the legacy address as a valid icon license; confirm the current authority specification. |
| Play Academy video link on the page | Policy education/training. | The click did not resolve to a readable destination; it does not change questionnaire, rating, or ad-policy duties. |

### IARC Ratings Definitions: one layer below the Help article

The IARC definitions page links to nine rating-authority sites. This table records the destinations and the extent to which their content was readable; their own menus, news, legal pages, and unrelated resources have not been recursively mirrored.

| IARC destination | Review status and relationship |
| --- | --- |
| [Australian Classification Board](https://www.classification.gov.au/) | Official homepage opened; the “What do the ratings mean?” child page was also opened. Play Help says this system applies to games in Australia. |
| [ClassInd — current Brazilian Ministry portal](https://www.gov.br/mj/pt-br/assuntos/seus-direitos/classificacao-1) | Official government portal opened; its rating criteria were not extracted in this pass. The old `justica.gov.br` link in Play Help returned 502. |
| [Taiwan DGSC](https://www.gamerating.org.tw/) | Reopened October 23, 2026; the current body exposes Taiwan’s five local game-rating levels and links to regulations, a rating-assessment tool, and public game lookup. These descendants are local references, not Google Play global policy. |
| [ESRB Ratings Guide](https://www.esrb.org/ratings-guide/) | Full guide opened: rating categories, content descriptors, interactive elements, and rating summaries. It explains ESRB labels but adds no Play-specific duty. |
| [Saudi Gmedia](https://gmedia.gov.sa/ar) | IARC Definitions lists five Gmedia age labels with brief content descriptions and links “Read More” here; the official Arabic homepage returned zero readable lines. The English [homepage](https://gmedia.gov.sa/en) exposed only a title, as did [Age Classification](https://gmedia.gov.sa/en/age-classification). The table below summarizes IARC's labels; it is not a verified copy of Gmedia's full rules. |
| [Korea GRAC](https://www.grac.or.kr/english/) | Destination was reached but its firewall blocked readable content; labels are summarized from IARC/Play Help. |
| [Indonesia IGRS](https://igrs.id/) | Target returned a page title but no readable body; labels are summarized from IARC definitions only. |
| [PEGI](https://pegi.info/) | Current site opened, with readable age categories and content descriptors; the separate `www.pegi.info` click from Play Help returned 503 in the same review. |
| [Germany USK](https://www.usk.de/iarc/) | The Help `/iarc/` route remains unreadable; IARC Contact separately links to `www.usk.de/`, whose canonical host homepage and [USK IARC page](https://usk.de/fuer-unternehmen/spiele-und-apps-pruefen-lassen/spiele-und-apps-im-iarc-system/) are now readable. The IARC page describes Germany's local classification context and lists Google Play as a participating storefront; it does not add a global Play rule. Descendants are summarized below. |

### Saudi Gmedia age labels: the readable source is IARC's summary

The [IARC Ratings Definitions](https://www.globalratings.com/ratings-definitions/) page displays five Gmedia labels with short content examples. Its “Read More” link opens the [official Gmedia Arabic homepage](https://gmedia.gov.sa/ar), which returned no readable body in this review; the English [Age Classification page](https://gmedia.gov.sa/en/age-classification) also exposed only a title. The table therefore paraphrases the Arabic descriptions on IARC's page, not a verified copy of Gmedia's complete, current regulations or rating criteria.

| Label listed by IARC | IARC's content summary |
| --- | --- |
| 3+ | Suitable for all ages, with sports games as an example; cartoon-context violence suitable for children may appear. |
| 7+ | May include frightening scenes or sounds, implied violence, or unrealistic consequences of violence (for example, characters disappearing after death). |
| 12+ | May include frightening sound or visual effects and minor injury detail. |
| 16+ | May include realistic violence against people or human-like creatures, positively portrayed crime or crime without negative consequences, and inappropriate language. |
| 18+ | May include extreme violence, such as detailed torture or dismemberment, and depictions of drug, tobacco, or alcohol use. |

**Interpretation boundary:** This helps explain the Saudi labels shown by IARC. It is not a legal conclusion about local age restrictions, distribution duties, or Gmedia's rating workflow. Do not substitute it for Gmedia's current official rules or treat a local standard as a Google Play rule that applies globally. Recheck readable Gmedia rules and applicable law before making a market-launch decision.

### Direct child pages of the IARC website

The Content Ratings Help article also links to the IARC homepage. On October 23, 2026, we reopened its six primary navigation destinations (How IARC Works, Participants, Storefronts, FAQ, About, and Milestones) plus the separate Ratings Definitions and Contact pages: eight substantive page links. The homepage also links to a video; the click returned Internal Error without exposing a verifiable destination URL. Storefronts uses an image-based regional display matrix that was unreadable in text. Global privacy/cookie/terms footer links are site chrome, not Google Play rating policy. These eight pages explain IARC operations and do not add Play policy duties.

| IARC child page | Summary and descendant status |
| --- | --- |
| [How IARC Works](https://globalratings.com/how-iarc-works/) | One questionnaire generates regional age ratings, content descriptors, and interactive elements; authorities may correct ratings after release, and developers can reuse an IARC certificate ID on other participating storefronts. Its cross-site navigation points to the FAQ, Participants, Storefronts, Definitions, and Contact targets already inventoried. |
| [Participants](https://globalratings.com/participants/) | Lists nine participating authorities and their websites; these were cross-checked against the nine destinations from IARC Definitions above. Its Brazil ClassInd link points to [classindportal.mj.gov.br](https://classindportal.mj.gov.br/home), which returned only a title with no body in this review. |
| [Storefronts](https://globalratings.com/storefronts/) | Lists participating platforms and a regional-rating display matrix, but the matrix is image-based and the text fetch did not expose its storefront/territory cells; no values were inferred. |
| [IARC FAQ](https://globalratings.com/faq/) | Reopened October 23, 2026: the questionnaire is available only through participating storefronts, is currently free for developers, and issues ratings immediately after submission. Authorities may revise ratings after release. Developers may request a “rating check,” give a reason, and may be asked for evidence; a certificate code can usually be reused at another participating storefront. FAQ links return to nodes already mapped in this topic. |
| [About IARC](https://globalratings.com/about/) | Explains collaborative questionnaire logic, localized rating outcomes, and content descriptors/interactive elements; it adds no separate developer workflow. |
| [IARC Milestones](https://globalratings.com/milestones/) | The timeline says Google Play began IARC adoption in North America in 2015, records Taiwan DGSC, Indonesia IGRS, and Saudi Gmedia joining in 2023–2024, and says Gmedia began assigning ratings in 2026. This is institutional history, not a new Play deadline. |

**Distinguish the appeal routes:** Play Help directs developers to appeal to the relevant IARC authority using the link in the rating-certificate email. IARC FAQ calls a review request a “rating check” and says a reason or supporting evidence may be required. Both point to authority review, but the sources do not prove that every formal appeal and general rating check are identical; follow the certificate email and the relevant authority’s instructions. The general IARC Contact form requests a name, email, and comments and says submitted personal data will be transferred to the United States. No form was submitted.

**IARC metrics:** The homepage and About page show aggregate audience/developer/rating figures with different scopes. These promotional totals are not used as policy facts.

### IARC Contact → Taiwan local rating law and assessment tools

IARC Contact lists nine regional rating-authority destinations. All nine were opened or their access limits recorded. Taiwan’s DGSC site is readable and exposes descendants for local rules and a rating-assessment tool. This is Taiwan-specific game-classification law and process, not Google Play global policy, and does not replace the IARC/Play Console questionnaire.

| Taiwan descendant | Content, access, and scope |
| --- | --- |
| [Taiwan Digital Entertainment Software Rating site](https://www.gamerating.org.tw/) | Reopened October 23, 2026. The site describes the local system overseen by Taiwan’s Ministry of Digital Affairs and shows five levels: General, Protected, Guidance 12, Guidance 15, and Restricted. Keep this local classification separate from an IARC regional rating displayed on Google Play. |
| [About the site](https://www.gamerating.org.tw/Page?itemid=10&mid=5) | Explains the local legal basis and that publishers/importers register ratings and content; the public can search or report classification problems. Immersive-experience venues are also in local scope. |
| [Regulations and notices index](https://www.gamerating.org.tw/Message?itemid=1&mid=6) | The index reports 502 items and includes the 2019 Game Software Rating Management Regulations and 2026 notices. The other items were not individually reviewed. |
| [Rating-level assessment overview](https://www.gamerating.org.tw/Assess?itemid=2&mid=21) and [interactive assessment form](https://www.gamerating.org.tw/Assess/Type?itemid=2&mid=21) | The tool is presented as a reference that suggests a level after users select involved content categories: sex, violence, horror, tobacco/alcohol, drugs, inappropriate language, antisocial content, strategy games, card/puzzle games, and romance/dating. The public form was opened but not answered or submitted; it does not prove registration or an official decision. |
| [Taiwan Game Software Rating Management Regulations](https://www.gamerating.org.tw/Message/MessageView?GroupName=%E6%B3%95%E4%BB%A4%E8%A6%8F%E7%AB%A0&itemid=1936&mid=6&page=0) | The site-hosted text is dated May 23, 2019. It lists five statutory age levels and requires pre-release classification/registration, visible rating/content/warning labels, rating labels in ads, and safeguards for restricted games. This is Taiwan local law, not a global Play rule; verify current legal status locally. |
| [Game Software Rating Reference Table short link](https://reurl.cc/024E6A) | The click exposed only a short-link interstitial, not the final URL or readable table; no table content was inferred. |

The nine authority links and access limits appear in the IARC authority table and `source-page-audit.csv`.

### IARC Contact → USK's IARC process, ratings, and local legal context

The USK destination on the IARC Contact page leads to the USK homepage. Its business section distinguishes physical retail, general online distribution, and storefronts connected to IARC. The USK IARC page says developers complete the questionnaire during submission to a participating storefront, which generates regional ratings; it names Google Play as one such storefront. It also describes a German platform-labeling duty following the 2021 Youth Protection Act amendment and says state youth ministries legally recognized the USK IARC ratings in April 2025. These are USK's descriptions of German law and should not be generalized into global Google Play requirements.

| USK descendant | Summary, relationship, and access limits |
| --- | --- |
| [USK IARC process for games and apps](https://usk.de/fuer-unternehmen/spiele-und-apps-pruefen-lassen/spiele-und-apps-im-iarc-system/) | Full body opened. The process is to submit through a participating storefront, complete the IARC questionnaire, and receive regional ratings from the matrix. It also describes online-risk notices such as chat and purchases. This explains Germany's USK participation in IARC; it does not replace the Play questionnaire. The page distinguishes the JMStV basis for online games/apps from the JuSchG process for physical retail games. |
| [USK age ratings and content/use notices](https://usk.de/die-usk-alterskennzeichen/) | Full body opened. It explains rating levels, classification reasons, and use notices. Use notices cover purchases/random items, chat, location sharing, and internet access; content notices include violence, horror, sex, language, substances, advertising, and purchase pressure. These can help identify Play topics to review, but USK labels do not map directly to Play questionnaire answers or policy findings. |
| [USK principles and legal-materials index](https://usk.de/die-usk/grundlagen-und-struktur/grundlagen/) | Body opened. It separates USK review principles, the JuSchG process, and supplemental JMStV principles for online games/apps, with legal/rule PDFs. The two law PDFs returned an unsupported binary content type, so their text was not read or paraphrased. |
| [USK rating-label glossary index](https://usk.de/alle-lexikonbegriffe/category/usk-alterskennzeichen/) | Readable directory listing the local USK 0, 6, 12, 16, and 18 labels and links to individual entries. Only the directory was checked; each glossary entry was not downloaded. |
| [USK application page for games and apps](https://usk.de/fuer-unternehmen/spiele-und-apps-pruefen-lassen/) | Full body opened. The business page links to standard review, IARC review, other online releases, fees, application forms, and label artwork. The full fee, application, and artwork descendants were not expanded in this pass. |

**Boundary:** USK's explanation of German online-platform duties and Taiwan's local classification rules are stored as separate regional legal context; neither is an IARC or global Play rule. The two legal PDFs, all USK label glossary entries, and business application/fee/artwork descendants remain open and are individually tracked in the source audit.

## Help Center sidebar: store-listing navigation

The content-rating page sidebar has seven topic entries including the current page (six related entries), plus a parent [Manage your store listings](https://support.google.com/googleplay/android-developer/topic/3450987?hl=en) topic index. The six neighboring pages are [Choose a category and tags](https://support.google.com/googleplay/android-developer/answer/9859673?hl=en), [Add preview assets](https://support.google.com/googleplay/android-developer/answer/9866151?hl=en), [Create custom store listings](https://support.google.com/googleplay/android-developer/answer/9867158?hl=en), [Best practices for your store listing](https://support.google.com/googleplay/android-developer/answer/13393723?hl=en), [Manage target audience](https://support.google.com/googleplay/android-developer/answer/9867159?hl=en), and [Manage Play Shorts in Play Console](https://support.google.com/googleplay/android-developer/answer/17165227?hl=en). The first five already have knowledge-base summaries. The Play Shorts page was opened: since June 2026, uploads are managed in Play Console; access is limited to selected partners and US display; asset processing and policy/quality review have separate status fields; unpublishing may take 2–3 days. Play Shorts is an operational/asset workflow, not a content-rating rule.

The AdMob maximum-rating article also links from its body to [Comply with Families using AdMob](https://support.google.com/admob/answer/6223431) and [Tag an ad request for age treatment](https://support.google.com/admob/answer/6219315). Both were opened: the first contains child-directed and mixed-audience request examples, but its older TFCD code should be checked against the current TFAT guide; the second says TFCD/TFUA are deprecated and describes CHILD, TEEN, and UNSPECIFIED treatments. These are implementation resources. AdMob's “More about apps” sidebar has six items including the current page; related entries include these two guides and Content mapping. Other AdMob Help descendants are not fully inventoried.

Related local topics: [Store Listing and Asset Best Practices](../store-listing-best-practices/store-listing-best-practices.en-US.md) · [Ratings, Reviews, and Installs](../user-ratings-reviews-installs/user-ratings-reviews-installs.en-US.md) · Ads and Promotion (snapshot: `ads-and-advertising-en.md`, not imported in this repository) · [Age Restrictions and Child Safety](../age-restricted-child-safety/age-restricted-child-safety.en-US.md).

This is a bilingual paraphrase of the official pages, not a verbatim copy of every regional rating description. Before release, confirm the current territory mapping, rating-icon rules, target-audience answers, and ad compliance in the official pages and Play Console.
