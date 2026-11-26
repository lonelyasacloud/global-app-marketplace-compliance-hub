---
id: google-play.real-money-gambling
platform: google-play
language: en-US
authority: normative
status: current
kb_checked_at: 2026-10-23
review_due: 2027-01-23
regions: [global]
topics: [gambling, licensing, age-rating, daily-fantasy-sports, contests]
snapshot_id: play.real-money-gambling
snapshot_package: "GooglePlay-KnowledgeBase-2026-10-24-review.zip"
coverage_status: "detailed-summary"
source_url: "https://support.google.com/googleplay/android-developer/answer/9877032?hl=en"
source_url_application: "https://support.google.com/googleplay/android-developer/contact/gambling"
source_url_dfs_application: "https://support.google.com/googleplay/android-developer/contact/dfsform"
source_url_country_allowances: "https://support.google.com/googleplay/android-developer/answer/12256011?hl=en"
source_url_common_violations: "https://support.google.com/googleplay/android-developer/answer/13381106?hl=en"
source_url_zh: "https://support.google.com/googleplay/android-developer/answer/9877032?hl=zh-CN"
effective_date: "current policy; ended pilots are historical; no 2027-01-27 on this page"
---

# Google Play Real-Money Gambling, Games, and Contests

> **Import note (Google batch 6).** The body is the paraphrased summary from the already separated 2026-10-24 Google Play knowledge-base snapshot (`play.real-money-gambling`, reviewed 2026-10-23). It is not a verbatim copy of an official page. The English official source is the source of truth. `kb_checked_at` is the review date recorded in the snapshot source file; this import did not re-open the live official pages. Phrases such as “this knowledge base,” “this library,” and “local topic” describe coverage inside that snapshot, not the set of pages imported into this repository. Relative snapshot links to topics, link graphs, ledgers, or CSVs that are not in this repository are kept as text mentions. Relative links that target the Google batch 1–5 topics or these nine batch 6 topics point at the hub files. The snapshot YAML `reviewed_on` is 2026-10-23. The policy-structure paragraph says reviewed October 22, 2026. The common-violations article was opened October 23, 2026. Those snapshot dates are not a policy change. The Chinese source file records the policy URL as `hl=zh-CN`. Its country-allowance and common-violations URLs are `hl=en`. The snapshot does not record a failed `hl=zh-CN` fetch or a line-by-line Chinese-versus-English check. The Chinese hub text is the snapshot’s editorial paraphrase. Ended pilots are historical and are not current listing exceptions: the India DFS/Rummy grace period ended 2026-01-22, the Mexico DFS pilot ended 2026-06-04, the real-money gaming pilot overview effective 2026-06-04 said there were no active pilots, and the Japan online-crane pilot ended 2023-07-11. No 2027-01-27 date is recorded. The gambling policy is `normative`. The common-violations article is an operational review checklist. Country allowances and a license are not worldwide Play permission. Prediction-market pilot enrollment is a separate program.**

## Policy structure

The official [Real-Money Gambling, Games, and Contests policy](https://support.google.com/googleplay/android-developer/answer/9877032) generally prohibits apps that facilitate real-money wagering or gambling. Exceptions are limited to eligible apps, product types, and markets supported by Google Play, after application and approval. Reviewed October 22, 2026. Supported countries, states, product categories, and programs change; this topic includes a dated October 22, 2026 market-scope snapshot, while actual eligibility still depends on current policy, the live form, and local licenses.

## Main conditions for approved gambling apps

| Area | Requirement |
| --- | --- |
| Product and market | Only eligible categories listed in the policy (such as online casino, sports betting, horse racing, lotteries, and Daily Fantasy Sports) in markets where local law permits and Google Play supports the product. |
| Play approval | Submit the applicable gambling application and receive approval. Follow the current form for each app, market/state, and category. Ownership, license, or distribution changes may require recertification. The form says certification and review can take at least a week or longer. |
| License | Hold a valid operating license for the relevant country/state/territory and product; do not exceed its scope. |
| Minors and geofencing | Prevent underage use and block access from territories outside the license. |
| Price and payment | Eligible real-money gambling apps must be free to download and install, not sold as paid Play apps, and must not use Google Play Billing for gambling services. |
| Rating and responsible-gambling information | Obtain an AO (Adults Only) or equivalent IARC rating and clearly display responsible-gambling information in the app and store listing. |
| Other rules | Follow applicable laws, industry standards, Developer Program Policies, and local advertising restrictions. Circumventing certification or serious/repeated violations may result in full app removal. |

Apps outside the exception may not let users wager/stake real money—including in-app items bought with money—or participate in games, contests, or tournaments for real-world monetary/value prizes. Navigation, WebViews, buttons, and calls to action such as “BET,” “REGISTER,” or “COMPETE” may also facilitate prohibited activity.

## Gambling ads, loyalty programs, and DFS

- **Gambling ads:** Only apps meeting every policy condition may show ads for gambling/real-money games. The app, advertiser, and ad location must comply with local law/licensing; ads cannot be shown to users known to be under 18, and the host app cannot be in Designed for Families or target minors. Simulated gambling, gambling companion/support functionality, and content that directs users to gambling services are also prohibited. Approved gambling and DFS apps have the policy's specified exceptions.
- **Gamified loyalty programs:** Rewards must remain secondary to a genuine, independent goods/services purchase; no part of the transaction may function as an entry fee or wager, and the purchase cannot be priced above its usual value to buy participation. Game apps may provide related rewards only on a fixed ratio/schedule, not amplified by game performance or chance. Non-game chance-based rewards must meet requirements for official rules, number of winners/deadlines/prize dates, and disclosure of odds or selection method.
- **Daily Fantasy Sports (DFS):** DFS has a separate application flow and different eligibility paths for the U.S. and other markets. Local authorization, underage protections, free installation, no Play Billing, AO/equivalent rating, and responsible-gaming information remain relevant requirements.
- **Pilots:** Google may run limited pilots in selected markets, but the current [pilot overview](https://support.google.com/googleplay/android-developer/answer/12918670) says there are **no active pilots** (effective June 4, 2026; rechecked October 23, 2026). Past-pilot dates and transitions are summarized below; they do not authorize new participation.
- **Prediction-market pilot:** This is separate from licensed real-money gambling/gaming; the current pilot page lists only U.S. financial or equivalent licenses. See the [prediction-market topic](../prediction-market-pilot/prediction-market-pilot.en-US.md) for the past deadline and live eligibility checks.

### Status of past real-money gaming pilots

| Pilot | Current official status | What it means now |
| --- | --- | --- |
| Japan online crane games | Pilot ended July 11, 2023. A separate declaration route began July 12, 2023. | The declaration page requires acceptance/submission of its form and Play account standing; it says new apps may publish only after the declaration is accepted. Local law and the current terms still apply. |
| India DFS/Rummy | Pilot ended September 28, 2023. The grace period ended January 22, 2026. | Former pilot apps can remain in India only after removing real-money functionality and complying with the [Real-Money Gambling policy](https://support.google.com/googleplay/android-developer/answer/9877032). The old pilot announcement is not a continuing listing exception. |
| Mexico DFS | Pilot concluded June 4, 2026. | The [country-allowance page](https://support.google.com/googleplay/android-developer/answer/12256011?hl=en) separately lists casino, sports betting, and lotteries for Mexico, subject to the general policy, local licenses, and Play approval. These normal-policy categories are not an active pilot. |

The current overview says there are no active pilots. Use the live overview and country table before making a market decision; a past-pilot record does not confer current eligibility.

### Common gambling-app review failures and best practices

The official [Common violations for gambling apps](https://support.google.com/googleplay/android-developer/answer/13381106?hl=en) Help article was opened in full on October 23, 2026. It is a review checklist, not an independent policy; the Real-Money Gambling policy, country/region allowances, and applicable law remain controlling. It lists ten common problems:

1. **Missing publishing prerequisites:** Hold a valid gambling license for every country/state/territory of distribution, complete the gambling application accurately, and obtain an AO or IARC-equivalent rating.
2. **License/product mismatch:** The actual gambling product must fall within the license's authorized scope.
3. **Insufficient geofencing:** Block both new sign-ups and existing-account access/use in unapproved territories.
4. **Insufficient age gating:** Prevent minors from registering and using the app.
5. **Missing responsible-gambling information:** Clearly display an in-app statement and provide an external help-resource link. The article's **best practice** is to put the statement in the app footer or a top-level menu so users can find it easily; localize the contact information for the relevant country/region.
6. **Wrong review track:** Submit the gambling app on the production track for review, not only on a test track.
7. **Nonfunctional or incomplete app:** It must load and provide the features advertised in its listing; fix incomplete, unstable, or broken builds before resubmission.
8. **Ratings, reviews, and installs violations:** Do not market monetary-equivalent installation incentives in the listing. Titles, icons, and developer names must not claim Play store performance/rankings or imply affiliation with existing Google Play programs.
9. **Payments violations:** Do not sell the gambling app as a paid Play app or use Google Play Billing.
10. **Repurposing an older app for real-money gambling:** An app previously released below AO must not gain real-money gambling through an update; submit it as a new app with a new package name. Users may still reinstall the old app, so renaming or hiding it is not a substitute.

| Direct body link from the checklist | Its role in the checklist | Destination and local status |
| --- | --- | --- |
| [Real-Money Gambling, Games, and Contests policy](https://support.google.com/googleplay/android-developer/answer/9877032) | Main rules for licenses, product scope, geofencing/age controls, distribution, and responsible-gambling information. | Full body opened and summarized in this topic. |
| [Country/region allowances for gambling apps](https://support.google.com/googleplay/android-developer/answer/12256011) | Check whether each market and product is allowed and identify regional exceptions. | English body opened; access records cover 45 markets and 53 body targets. The dynamic country/resources table is separately snapshotted above. |
| [Gambling Application Form](https://support.google.com/googleplay/android-developer/contact/gambling) | Application route for the app, markets, licenses, and eligibility details. | Dynamic form opened and fields/market scope reviewed; not filled or submitted. |
| [IARC ratings](https://www.globalratings.com/) | IARC-equivalent rating route; eligible gambling apps still need AO or equivalent. | External entry recorded; the Play [Content Ratings Help page](https://support.google.com/googleplay/android-developer/answer/9898843) has a separate summary. IARC's internal process was not recursively expanded. |
| [User ratings, reviews and installs](https://support.google.com/googleplay/android-developer/answer/9898684) | Supports review of installation incentives, store-performance/rank claims, and affiliation claims. | Full body opened and covered by a separate bilingual topic (snapshot: `user-ratings-reviews-installs-en.md`, not imported in this repository); this is the related policy link referenced by the article. |
| [Understanding Google Play’s Payments policy](https://support.google.com/googleplay/android-developer/answer/10281818) | Explains the paid-app and Play Billing prohibitions. | Full body opened and summarized in the [Payments topic](../payments/payments-and-subscriptions.en-US.md); the gambling-specific restriction remains controlling for gambling apps. |

The checklist's “helpful links” navigation also points back to the [Manage policy violations directory](https://support.google.com/googleplay/android-developer/topic/3453554?hl=en), plus community/contact routes. Its 11 destinations are mapped in the [enforcement topic](../enforcement-and-appeals/enforcement-and-appeals.en-US.md). These recommendations and account-specific support flows are not counted as policy body links.

## Direct links and important descendants

| Target | Relationship to the main policy | Status |
| --- | --- | --- |
| [Gambling Application Form](https://support.google.com/googleplay/android-developer/contact/gambling) | Play certification application; the current form lists 45 markets and requires an application for each app, market/state, and product category, with licensee details and evidence. | Form body opened; market table is dynamic; no application submitted. |
| [Daily Fantasy Sports Application Form](https://support.google.com/googleplay/android-developer/contact/dfsform) | Separate U.S. DFS certification; requires state/territory license or registration evidence, package name, licensee relationship, and license dates; one form allows up to 20 states. | Body and DFS terms opened; actual account eligibility/submission not verified. |
| [IARC content ratings](https://www.globalratings.com/) | An AO or equivalent rating is required before submission. | Target recorded; Play's [Content Ratings](https://support.google.com/googleplay/android-developer/answer/9898843) article was opened; IARC's external process was not explored in this review. |
| [Country/region allowances](https://support.google.com/googleplay/android-developer/answer/12256011?hl=en) | Product scope for 45 markets, state/province exceptions, and examples of local responsible-gambling resources; an October 22, 2026 offline snapshot is included below. | English body opened; all 53 body targets attempted; see link audit below; recheck live market table. |
| [Real-money gaming pilot overview](https://support.google.com/googleplay/android-developer/answer/12918670) | Current body says no pilots are active; India DFS/Rummy grace period ended January 22, 2026, and Mexico DFS ended June 4, 2026. | Full body and its three distinct policy targets opened; see the dated status table above. Sidebar is separate. |
| [Online Crane Games](https://support.google.com/googleplay/android-developer/answer/12002615) | Historical Japan online-claw-machine pilot information. | Opened; pilot ended July 11, 2023. |
| [Online Crane Games declaration form](https://support.google.com/googleplay/android-developer/contact/ocgform) | Declaration and eligibility flow for global distribution of online crane games, subject to local law. | Form body and key direct links opened; no fields were filled or submitted. See the next section for requirements and descendants. |
| [Ads policy](https://support.google.com/googleplay/android-developer/answer/9857753) and its deceptive-ad rules | Gambling ads remain subject to ad-content, age, and anti-deception rules. | Ads article read; the page anchor can change, see the [Ads topic](../ads-and-advertising/ads-and-advertising.en-US.md). |
| [Android WebView API](https://developer.android.com/reference/android/webkit/WebView) | Gambling policy lists WebView paths as a possible facilitation example. | Technical API reference opened; implementation context, not gambling eligibility policy. |
| Pilot details and the market/license tables | Determine product, market, and local-law exceptions. | Current license and market state can change; check the application form and relevant regulator. |

### Online Crane Games declaration and direct links

Google defines an online crane game (OCG) as an app-based entertainment service that lets users remotely operate, from a phone or PC, a physical crane machine installed at the operator's physical location. Japan's limited pilot has ended, but the declaration page still describes a declaration route for distribution subject to local law; ending the pilot does not mean the declaration requirement ended. Reopened the article and declaration on October 23, 2026; the current pilot overview also confirms there are no active real-money gaming pilots.

The declaration, effective July 12, 2023, must be completed and accepted by an authorized representative, and the developer account must remain in good standing. Google says it will generally notify the developer within five business days after receiving all required information. Required fields include the representative's name and email, Play developer account name, Console login email, package name, and app name; where applicable, the operator, company name/incorporation date, and Japanese corporate number are also requested. New apps may publish only after the declaration is accepted; existing apps may need updated Console settings. Missing or incomplete declarations can prevent distribution or lead to removal.

Core operating commitments include:

- Categorize the app as a Game in Play Console; maintain effective age verification and age-appropriate spending limits with warnings when limits are exceeded.
- Accept payment only for entertainment/gameplay, never as a wager, stake, or consideration to win a prize of real monetary value. Prizes must stay within local law and generally accepted local crane-game value limits, and must not be resold or made available for third-party resale.
- Provide effective redress and customer support; do not disadvantage users by secretly altering their chance to win; do not misrepresent gameplay or the likelihood of winning in ads.
- Comply with all Play policies (including Payments), the DDA, and the declaration terms. Keep submissions accurate and complete. Promptly notify Google in writing of changed information, relevant legal/regulatory investigations, or rulings.
- Google may suspend or terminate listings for breach, legal requirements, account status, or risk, and reserves the right to stop allowing OCG apps globally or in a particular market.

| Form link | Purpose and relationship | Access/status |
| --- | --- | --- |
| [Japan Corporate Number information (National Tax Agency)](https://www.houjin-bangou.nta.go.jp/en/setsumei/) | The form asks Japan distributors for a corporate number. The NTA says it is a 13-digit identifier and describes public lookup of organization names, addresses, and numbers, plus a Web API and bulk downloads. This explains a form field; it is not a Play approval rule. | Official information page opened. |
| [Google Play Developer Policy Center](https://play.google.com/developer-content-policy/) | Compliance with Developer Policies is a condition of eligibility; the center indexes content, user data, permissions, payments, ads, store listing, enforcement, and other policy areas. | Current policy center opened; individual requirements are checked on their topic pages. |
| [Developer Distribution Agreement](https://play.google/developer-distribution-agreement.html) | The declaration incorporates the DDA. Section 4.7 is especially relevant to support, accurate contact information, and response times for paid products/in-app transactions. | Current DDA has a bilingual topic; cross-checked here. |
| [Choose a category and tags](https://support.google.com/googleplay/android-developer/answer/9859673?hl=en) | The form requires the OCG app to be categorized as a Game. The Help page says categories/tags aid discovery, tags should be clearly relevant to a new user, the limit is five, and they should be revisited after significant changes. | Full body opened; covered by the store-listing topic. |
| [Play Developer Account](https://play.google.com/console/u/0/signup); [Google Play Store](https://play.google.com/store/games); [Developer Console](https://play.google.com/console/u/0/developers/app/app-dashboard) | Helps applicants create/sign in to a developer account and find the package name. The Store link opens a consumer listing surface; account and Console links require Google sign-in. | Store page opened; signup and Console are login-gated, so account-only content could not be checked. |
| [Google Privacy Policy](https://policies.google.com/privacy?hl=en); [Google Terms of Service](https://policies.google.com/terms?hl=en) | Footer links for the form's support/account-information notice. These are Google's general privacy and service terms, not OCG eligibility requirements or a substitute for an app privacy policy. | Both targets have separate URL-audit records; no form was submitted. |

The form also says account/system data and support communications may be used for support quality, training, technical troubleshooting, and product improvement, and that chats/emails may use translation services. The fetched form includes dynamic interface text saying “Your email has been sent,” but no fields were completed and no submit action was taken; that text is not evidence of a submission in this review.

## Market-allowance snapshot and direct-link audit (2026-10-22)

The official [country/region allowances article](https://support.google.com/googleplay/android-developer/answer/12256011?hl=en) lists 45 markets. The table below is an offline snapshot of product scope in the English Help article on that date. It does not mean a developer holds a local license or Play certification. State/province rules, licenses, and form options change; recheck the live application form before release.

**Every real-money gambling app must include a responsible-gambling statement both in the store-listing description and inside the app, with local contact information for third-party problem-gambling support resources.** Apps must also meet local requirements for those statements and licenses. The organizations listed by Google are examples, not Play certification or endorsement.

Codes: C = online casino; S = sports betting; H = horse racing; L = lotteries; DFS = daily fantasy sports. Unless noted, H is regulated separately from sports betting; DFS applies only where local law and Play eligibility allow it.

| Market | Products listed in the article (snapshot) | Local responsible-gambling resource examples and direct-fetch state |
| --- | --- | --- |
| Australia | S; DFS only where lawful; L | [Gambling Help Online](https://www.gamblinghelponline.org.au/) (HTTP 403); [Gamblers Anonymous Australia](https://gaaustralia.org.au/) (timeout) |
| Austria | C; S; H if separately regulated; L (government operators only) | [Federal Ministry of Finance: player protection](https://www.bmf.gv.at/themen/gluecksspiel-spielerschutz/spielerschutz-hilfsangebote.html) (destination page opened) |
| Belgium | C; S; L (government operators only) | [Gokhulp](https://gokhulp.be/begeleiding) (destination page opened); [Joueurs Aide-en-Ligne](https://joueurs.aide-en-ligne.be/) (destination page opened) |
| Brazil | H; L limited to approved apps published by Caixa Econômica Federal | [Gamblers Anonymous Brazil](https://www.gamblersanonymous.org/ga/addresses) (HTTP 404; target not found) |
| Bulgaria | C; S (DFS where lawful); H if separately regulated; L | [Solidarnost Association](https://www.solidarnost-bg.org/) (redirected and opened) |
| Canada | Outside Ontario/Alberta: C/S/L government operators only. Ontario: C/S; L government only. Alberta: C/S. | [National Problem Gambling Helpline](https://www.ncpgambling.org/help-treatment/about-the-national-problem-gambling-helpline/) (redirected and opened); [Canada Safety Council](https://canadasafetycouncil.org/gambling-addiction/) (destination page opened) |
| Colombia | C; S; L (government operators only) | [Jugadores Anónimos Colombia](https://jugadoresanonimoscolombia.org/) (destination page opened) |
| Croatia | C; S; L | [Andrija Štampar Public Health Institute](https://stampar.hr/hr/novosti/kada-zabava-prelazi-u-ovisnost-kockanje-i-kladenje) (destination page opened) |
| Czech Republic | C; S; H if separately regulated; L | [Anonymní Gambleři Česko](https://www.anonymnigambleri.cz/) (cache miss; body unavailable) |
| Denmark | C; S; L | [Spillemyndigheden treatment search](https://spillemyndigheden.dk/borgere-og-spillere/soeg-behandling) (redirected and opened) |
| Ethiopia | C; L | [Amanuel Mental Specialized Hospital](https://amsh.gov.et/) (page title only; no body retrieved) |
| Finland | C/S/L (government operators only) | [Peluuri](https://www.peluuri.fi/) (destination page opened) |
| France | C; S; H if separately regulated; L (government operators only) | [Joueurs Info Service](https://www.joueurs-info-service.fr/) (HTTP 503 Service Unavailable) |
| Germany | S; H if separately regulated; L (government or affiliated contracted operators only) | [FAGS Glücksspielsucht](https://www.gluecksspielsucht.de/) (destination page opened) |
| Ghana | C; S; L | [Gaming Commission of Ghana](https://gamingcommission.gov.gh/) (timeout) |
| Greece | C; S; DFS; L | [KETHEA Helpline 1114](https://www.kethea.gr/kethea/therapeftika-programmata/grammi-voitheias-1114/) (HTTP 502) |
| Hungary | C; L; S (DFS where lawful); H | [Szerencsejáték-függőség Megelőzési Segítő Központ](https://szmsk.hu/szolgaltatasaink/) (destination page opened) |
| Ireland | C; S; L (governmental or charitable operators only) | [GambleAware Ireland](https://www.gambleaware.ie/) (timeout) |
| Italy | L only | [Istituto Superiore di Sanità: Uscire dal Gioco](https://usciredalgioco.iss.it/) (HTTP 404) |
| Japan | Government-operated S only (horse, motorboat, bicycle, auto-bicycle racing, soccer lottery); government-operated L only | [Gambling Addiction Prevention and Recovery Support Center](https://www.gaprsc.or.jp/) (destination page opened) |
| Kenya | C; S; H if separately regulated; L | [Responsible Gambling Kenya](https://www.responsiblegambling.or.ke/) (redirected and opened) |
| Latvia | L only | [Spēles Brīvība](https://www.spelesbriviba.lv/) (destination page opened) |
| Lithuania | L only | [Nebenoriu lošti](https://nebenoriu-losti.lt/) (destination page opened) |
| Mexico | C; S; L | [Grupo Punto de Partida](https://grupopuntodepartida.com/en/) (redirected and opened) |
| Netherlands | C; L; S | [Open Over Gokken](https://www.loketkansspel.nl/index.html) (HTTP 502 Bad Gateway) |
| New Zealand | S/L (government operators only) | [Gambling Helpline Aotearoa](https://gamblinghelpline.co.nz/) (destination page opened); [Choice Not Chance](https://www.choicenotchance.org.nz/understand-gambling) (cache miss; body unavailable) |
| Nigeria | C; S (DFS where lawful); H if separately regulated; L, in selected states only | [Gamble Alert](https://gamblealert.org/) (destination page opened); [Gamble Pause](https://gamblepause.com/) (empty response) |
| Norway | C; S (government operators only); L | [Hjelpelinjen](https://hjelpelinjen.no/) (destination page opened); [Spillavhengighet Norge](https://spillavhengighet.no/) (redirected and opened) |
| Panama | C; S (DFS where lawful); H if separately regulated; L | Responsible-gambling contact listed by Play (email shown as plain text, no hyperlink) |
| Peru | L only | [Ministry of Health: Línea 113](https://www.gob.pe/555-linea-113-salud-recibir-orientacion-e-informacion-en-salud) (HTTP 418; body unavailable) |
| Philippines | L only | [PAGCOR Responsible Gaming](https://www.pagcor.ph/regulatory/responsible-gaming.php) (destination page opened) |
| Poland | L only | [Uzależnienia Behawioralne](https://uzaleznieniabehawioralne.pl/) (destination page opened) |
| Portugal | C; S; H if separately regulated; L only for approved apps published by Santa Casa da Misericórdia de Lisboa | [Serviço de Regulação e Inspeção de Jogos](https://www.srij.turismodeportugal.pt/pt/jogo-responsavel/politica-de-jogo-responsavel/) (cache miss; body unavailable) |
| Romania | C; S; L (government operators only) | [Clinica Aliat](https://www.clinica-aliat.ro/jocuri-de-noroc/) (cache miss; body unavailable) |
| Serbia | C; S (DFS where lawful); L (government operators only) | [Special Hospital for Addiction Diseases](https://www.drajzerova.org.rs/) (destination page opened) |
| Singapore | L only | [National Council on Problem Gambling](https://www.msf.gov.sg/ncpg) (redirected; only a short body was readable) |
| Slovakia | C; S (DFS where lawful); H if separately regulated; L | [Centrum pre liečbu drogových závislostí](https://cpldz.sk/) (timeout) |
| Spain | C; S (DFS where lawful); H if separately regulated; L (government operators only) | [FEJAR](https://fejar.org/) (destination page opened); [Clínicas CITA](https://www.clinicascita.com/tratamiento-ludopatia/) (cache miss; body unavailable) |
| Sweden | C; S; L (government operators only) | [Stödlinjen](https://stodlinjen.se/) (redirected and opened) |
| Switzerland | C; S; L | [SOS-Spielsucht](https://www.sos-spielsucht.ch/en/) (destination page opened) |
| Tanzania | C; S (DFS where lawful); L | [Gaming Board of Tanzania](https://www.gamingboard.go.tz/) (timeout) |
| Turkey | C; S; L | [Yeşilay gambling-addiction resource](https://www.yesilay.org.tr/bagimlilik/kumar-bagimliligi/) (redirected and opened) |
| Ukraine | L only | [State Agency PlayCity: gambling-addiction prevention](https://playcity.gov.ua/borotba-z-ihrovoiu-zalezhnistiu) (destination page opened) |
| United Kingdom | C; S (DFS where lawful); L | [GambleAware](https://www.gambleaware.org/) (redirected and opened) |
| United States | In legally permitted and appropriately licensed states: C; S; H if separately regulated; L (including lottery couriers). Also Class II tribal gaming under NIGC-approved tribal ordinances; the application form determines whether a state/product is supported. | [National Council on Problem Gambling: help by state](https://www.ncpgambling.org/help-treatment/help-by-state/) (redirected and opened) |

### Direct children: relationship and audit boundary

The body exposes 53 distinct targets, all individually attempted: one gambling application form, one current real-money gambling policy, and 51 market-specific third-party/regulatory help resources. Of the 51 resources, 33 returned readable text or a landing page (the Ethiopia target returned only its page title), 17 hit 403/404/418/502/503, timeout, cache-miss, or internal-fetch errors, and one returned an empty body. All 51 destination URLs are now recorded from the official page links or fetch output. The readable pages function as local support/regulatory examples, not Play certification, policy interpretation, or endorsement. The article’s footer Community/Contact routes were also attempted but did not load; its 32-item sidebar is a shared Help navigation index and is not part of the article body requirements. **Resource-site grandchildren are not crawled**, because they are not Google Play policy text.

| Target | Content and relationship | Status |
| --- | --- | --- |
| [Gambling Application Form](https://support.google.com/googleplay/android-developer/contact/gambling) | Lists 45 supported markets and includes U.S. state/product and Nigerian state/product matrices. Applications are scoped to app, market/state, and product; ownership or licensing changes require recertification. Fields identify the developer/authorized representative, package name, licensee/address/product/territory, and license evidence. Review can take at least a week or longer. | Form body opened; market options are dynamic; no application submitted. |
| [Daily Fantasy Sports Application Form](https://support.google.com/googleplay/android-developer/contact/dfsform) | Separate U.S. DFS certification. Requires U.S. state/territory license or registration evidence, developer-licensee relationship, package name, and license dates. One form can include up to 20 states. The terms prohibit third-party DFS aggregation and require timely notice/restriction when licenses change or end, regulators issue relevant rulings, or age/geofencing fails. | Body and terms opened; account eligibility/submission not verified. |
| [Content rating requirements](https://support.google.com/googleplay/android-developer/answer/9859655?hl=en) | The form requires an A/O or equivalent rating. The old Play rating link redirects to the current 9859655 Help article; see the bilingual [Content Ratings topic](../content-ratings/content-ratings.en-US.md). | Current Help page opened; external IARC process not recursively audited. |
| [Developer Policy Center](https://play.google.com/about/developer-content-policy/) | Gambling certification also incorporates the Developer Program Policies and DDA; current consolidated policy is maintained in this library. | Dynamic link fetch failed in this pass; local policy page remains available. |

## Review sequence

1. Determine whether the app involves real-value wagering/prizes, betting support, simulated gambling, or gambling ads; do not classify solely by Play Store category.
2. Confirm government authorization and Play eligibility for every target market and product type; record license holder, validity, territory, and scope.
3. Use the current Play application form. Separately verify market, age controls, IARC rating, responsible-gambling disclosures, and payment paths.
4. Review ads, DFS, loyalty rewards, and WebView/external links independently; an app can facilitate gambling through advertising or companion features even if users do not place bets in the primary UI.
5. Recheck market tables and approval status before release and after legal changes.

## Related topics

- [Ads and promotion](../ads-and-advertising/ads-and-advertising.en-US.md) · [Financial services and loans](../financial-services-and-loans/financial-services-and-loans.en-US.md)
- [Crypto assets and NFTs](../crypto-assets-and-nfts/crypto-assets-and-nfts.en-US.md) · [Payments and subscriptions](../payments/payments-and-subscriptions.en-US.md)
