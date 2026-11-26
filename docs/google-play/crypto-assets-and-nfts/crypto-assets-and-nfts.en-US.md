---
id: google-play.crypto-assets-and-nfts
platform: google-play
language: en-US
authority: normative
status: current
kb_checked_at: 2026-10-22
review_due: 2027-01-22
regions: [global]
topics: [crypto-assets, nft, blockchain, software-wallet, financial-features]
snapshot_id: play.crypto-assets-and-nfts
snapshot_package: "GooglePlay-KnowledgeBase-2026-10-24-review.zip"
coverage_status: "detailed-summary"
source_url_country_requirements: "https://support.google.com/googleplay/android-developer/answer/16329703?hl=en"
source_url_blockchain_policy: "https://support.google.com/googleplay/android-developer/answer/13607354?hl=en"
source_url_financial_declaration: "https://support.google.com/googleplay/android-developer/answer/13849271?hl=en"
source_url_gambling: "https://support.google.com/googleplay/android-developer/answer/9877032?hl=en"
source_url_gambling_pilots: "https://support.google.com/googleplay/android-developer/answer/12918670?hl=en"
source_url_one_time_products: "https://support.google.com/googleplay/android-developer/answer/16430488?hl=en"
source_url_metadata: "https://support.google.com/googleplay/android-developer/answer/9898842?hl=en"
source_url_country_distribution: "https://support.google.com/googleplay/android-developer/answer/7550024?hl=en"
source_url_country_requirements_zh: "https://support.google.com/googleplay/android-developer/answer/16329703?hl=zh-CN"
source_url_country_distribution_zh: "https://support.google.com/googleplay/android-developer/answer/7550024?hl=zh-CN"
effective_date: "current rules; Liechtenstein, Iceland, and Norway “Starting July 2026” has passed; no 2027-01-27 on this page"
---

# Crypto Exchanges, Software Wallets, and NFTs

> **Import note (Google batch 6).** The body is the paraphrased summary from the already separated 2026-10-24 Google Play knowledge-base snapshot (`play.crypto-assets-and-nfts`, reviewed 2026-10-22). It is not a verbatim copy of an official page. The English official source is the source of truth. `kb_checked_at` is the review date recorded in the snapshot source file; this import did not re-open the live official pages. Phrases such as “this knowledge base,” “this library,” and “local topic” describe coverage inside that snapshot, not the set of pages imported into this repository. Relative snapshot links to topics, link graphs, ledgers, or CSVs that are not in this repository are kept as text mentions. Relative links that target the Google batch 1–5 topics or these nine batch 6 topics point at the hub files. Reviewed 2026-10-22. The snapshot reopened the English exchange and software-wallet country page and the English country-distribution guide. The corresponding Simplified Chinese Help URLs were inaccessible. The Chinese summary is based on those English bodies and is not a line-by-line review of the Chinese pages. That access failure is not a policy change. The Chinese YAML still lists `hl=zh-CN` URLs for related policies; the bodies recorded as opened in the link table are English. The source labels Liechtenstein, Iceland, and Norway as included “Starting July 2026.” That date has passed as of the review. The real-money gaming pilot page’s effective date 2026-06-04 has passed, and that page said there were no active pilots. Those dates are not a 2027-01-27 preview. No 2027-01-27 date is recorded. Exchange and wallet eligibility, the financial-features declaration, and Blockchain-based Content are separate `normative` requirements. Non-custodial wallets are outside the special exchanges and wallets policy and are not exempt from the other rules. The country table lists credentials named by Play. It is not a complete statement of local law. Country targeting for testing tracks is operational guidance and does not replace a license.**

**Reviewed October 22, 2026.** Google Play treats crypto-exchange/software-wallet market eligibility, financial-feature declarations, blockchain-based assets, and NFT game mechanics as related but distinct requirements. The country table below summarizes credentials listed by Play; it is not a complete statement of local law and does not establish that a particular developer or app is licensed.

## Separate the product type from its obligations

| Product or feature | Main policy entry | Core actions |
| --- | --- | --- |
| Cryptocurrency exchange | Cryptocurrency Exchanges and Software Wallets; Blockchain-based Content | Declare financial features, confirm each target market's licenses/registrations, complete applicable location forms, and check local law |
| Custodial software wallet | Same | Declare the wallet feature; confirm target-market requirements and Play Console forms |
| Non-custodial wallet | Expressly out of scope of the special exchanges/software-wallets policy | This exclusion does not automatically waive the financial-features declaration, Blockchain-based Content, other Play rules, or local law |
| NFT/tokenized-asset sales, trading, or awards | Financial features declaration; Blockchain-based Content | Declare the feature and follow applicable game, real-money gambling, and metadata rules |
| On-device mining | Blockchain-based Content | Apps may not mine cryptocurrency on devices; remote mining-management apps are permitted, subject to other applicable rules |

Google Play expects cryptocurrency purchase, holding, or exchange to occur through certified services in regulated jurisdictions. Choosing a country in Play Console is an affirmative decision to make the app available there. A market not listed below is not automatically exempt: developers must comply with local law, and Google may request more evidence.

**Source verification:** This pass reopened the English [exchange/software-wallet country requirements](https://support.google.com/googleplay/android-developer/answer/16329703?hl=en) page and its direct [country-distribution guide](https://support.google.com/googleplay/android-developer/answer/7550024). The corresponding Simplified Chinese Help URLs were inaccessible to the fetcher; the Chinese summary is based on the English bodies and is not presented as an independent line-by-line review of the Chinese pages.

## Credentials listed by Google Play

The table follows the official “Cryptocurrency Exchanges and Software Wallets” Help page. In the captured page text, the cells for exchanges versus software wallets are not clearly separated except for Hong Kong and Thailand. The table therefore records the listed credential without inferring that a wallet type is exempt. Before release, confirm the exact product-type column in the live source table and the Play Console form.

| Country/region | License or registration listed by the Play page |
| --- | --- |
| Bahrain | Appropriate Crypto-Asset Services license from the Central Bank of Bahrain (CBB). |
| Canada | Registration with FINTRAC (CANAFE) as a money services business (MSB). |
| Hong Kong | **Exchange:** opt into the licensing regime and hold SFC Type 1 (dealing in securities) and Type 7 (automated trading services) licenses. **Software wallet:** the page says “Not required.” |
| Indonesia | Appropriate OJK license as a Digital Financial Asset Trading Provider. |
| Israel | A CMISA license as a financial-services provider, or a Bank of Israel license as a banking corporation. |
| Japan | Registration with Japan's Financial Services Agency (FSA) as a crypto-asset exchange service provider. |
| Philippines | Certificate of Authority as a Money Services Business from the Bangko Sentral ng Pilipinas (BSP). |
| South Africa | Registration with the Financial Sector Conduct Authority (FSCA). |
| South Korea | Successful filing of a virtual-asset-service-provider (VASP) report with the Commissioner of the Korea Financial Intelligence Unit (KoFIU). |
| Thailand | **Exchange:** relevant Digital Asset Business license from Thailand's Securities and Exchange Commission (SEC). **Software wallet:** the page says “Not required.” |
| United Arab Emirates | A license from one of FSRA, VARA, or DFSA. |
| United Kingdom | Registration with the Financial Conduct Authority (FCA). |
| United States | Registration with FinCEN as an MSB and with a state as a money transmitter; or status as a federally or state-chartered bank entity. |
| European Union, plus Liechtenstein, Iceland, and Norway as listed from July 2026 | Authorization as a crypto-asset service provider (CASP) under MiCA by a relevant national competent authority. Additional national and local requirements apply. |

EU Member States listed on the page: Austria, Belgium, Bulgaria, Croatia, Cyprus, Czechia, Denmark, Estonia, Finland, France, Germany, Greece, Hungary, Ireland, Italy, Latvia, Lithuania, Luxembourg, Malta, Netherlands, Poland, Portugal, Romania, Slovakia, Slovenia, Spain, and Sweden. The source labels Liechtenstein, Iceland, and Norway as included “Starting July 2026.” That date has passed as of this review, but the page retains that wording; confirm current Console forms and regulator status.

The source also says that from July 2026, developers located in Liechtenstein, Iceland, or Norway and authorized as MiCA CASPs by a relevant national authority may target EU Member States. Additional national requirements beyond MiCA still apply.

### Declaration and country-targeting workflow

1. In Play Console, open **App content → Financial features** and declare cryptocurrency wallet, exchange, and/or NFT/tokenized-asset sales, trading, and awards according to actual app functionality. The declaration Help page says all published apps must complete the declaration, including testing tracks; apps without financial features must declare that too. Its historical 2023 deadline has passed and should not be read as meaning that a current declaration is unnecessary.
2. Select only markets where the product is eligible and ready to operate. Complete location-specific forms for listed markets. If the required license or registration is missing, remove that market from the app's target countries/regions.
3. Separately review local requirements in markets not listed. “Not listed” does not mean “no license needed.” Keep evidence connecting license holders, the developer account, operating entities, partners, and the app's real functionality.
4. Recheck license validity, market availability, Console declarations, and store materials when a policy or market changes. Google may request additional documents.

### Country availability and testing tracks

The directly linked [Distribute app releases to specific countries](https://support.google.com/googleplay/android-developer/answer/7550024) guide distinguishes production **app availability** from **country targeting** for open and closed testing tracks. Selecting a country for production makes it available for current and future production releases. Testing tracks follow production countries by default, but can be unsynced and configured separately when the stated prerequisites are met. Internal testing is not subject to country targeting; internal testers can install from any location. Country targeting uses the user's **Google Play account country**, not their current GPS location.

Adding a country for a paid app automatically adds local prices. Subscription prices still need to be reviewed and set for each target market. This operational guide does not replace licensing, local-law, or Play country-form eligibility for crypto services; the target country must still meet the requirements in the table above.

## Blockchain content, NFTs, and game mechanics

Google Play defines blockchain-based content as tokenized digital assets secured on a blockchain. Apps that contain it must follow the policy.

- **Declaration and product details:** If an app sells or enables users to earn Tokenized Digital Assets, declare that in the Play Console Financial features declaration. When creating an in-app product, the product details must indicate that it represents a Tokenized Digital Asset. Product metadata must also accurately describe the product and not mislead users.
- **Earnings claims:** Do not promote or glamorize potential earnings from gameplay or trading. Avoid promises of price appreciation, investment returns, or guaranteed income as a game reward or progression outcome.
- **Mining:** Apps may not mine cryptocurrency on the device. Apps that remotely manage mining are permitted.
- **NFT chance mechanics:** Gambling apps that integrate tokenized assets such as NFTs must complete the gambling-application process and meet applicable licensing, location, and age requirements. Other apps that are ineligible as gambling apps and are not in an applicable pilot must not accept anything of monetary value in exchange for a chance to obtain an NFT of unknown value.
- **NFT use in games:** NFTs purchased by users should be consumed or used in the game to enhance the experience or help users progress. They must not be wagered or staked for a chance to win prizes of real-world monetary value, including other NFTs.
- **Examples of violations named by the policy:** NFT bundles sold without disclosing their specific contents and values; pay-to-play social casinos, such as slot-machine games, that reward NFTs.

Assess NFT mechanics together with [Real-Money Gambling, Games, and Contests](https://support.google.com/googleplay/android-developer/answer/9877032?hl=en): approved gambling apps must apply, hold valid licenses for each target location and product type, block minors and unlicensed locations, and meet requirements such as free installation, no Play Billing, AO/IARC-equivalent rating, and responsible-gambling information. The policy lists products such as online casinos, sports betting, horse racing, lotteries, and DFS. Other unapproved apps generally may not accept real money or money-purchased items for wagers that win real-world-value prizes, unless an applicable program/pilot permits it. That Help page also covers gambling ads, DFS, and gamified loyalty programs; this topic summarizes only the NFT overlap.

The real-money gaming pilots page opened on October 22, 2026 says there are currently no active pilots. This status can change. It records: the Japan online-crane pilot ended July 11, 2023; the India DFS/Rummy pilot ended September 28, 2023, with its grace period ending January 22, 2026 (former pilot apps can remain in India only after removing real-money functionality and complying with the gambling policy); and the Mexico DFS pilot ended June 4, 2026, after which real-money apps must comply with the gambling policy and be an allowed game type in Mexico. Do not treat the possibility of a pilot as a self-service exception; check the current pilot, territory, terms, and application eligibility.

## Page-by-page links and relationships

This table records body links from the policy pages above and key descendants opened to understand those obligations. Generic navigation, feedback, and image links are excluded; a page's navigation directory is not itself a policy requirement.

| Parent page | Child or descendant | Content and relationship / review status |
| --- | --- | --- |
| [Cryptocurrency Exchanges and Software Wallets country requirements](https://support.google.com/googleplay/android-developer/answer/16329703?hl=en) body (3 link occurrences) | [Blockchain-based Content policy](https://support.google.com/googleplay/android-developer/answer/13607354?hl=en) (twice) and [Distribute app releases to specific countries](https://support.google.com/googleplay/android-developer/answer/7550024) (once) | Full English body opened; three body-link occurrences deduplicate to two destinations. The Blockchain policy is open and summarized locally; the country-distribution guide is now also open. The Help sidebar separately lists 32 items including the current page. The `zh-CN` URL was inaccessible in this pass. |
| [Distribute app releases to specific countries](https://support.google.com/googleplay/android-developer/answer/7550024) | [Testing tracks](https://support.google.com/googleplay/android-developer/answer/9845334), [price setup](https://support.google.com/googleplay/android-developer/answer/6334373), [subscriptions](https://support.google.com/googleplay/android-developer/answer/140504), [staged rollouts](https://support.google.com/googleplay/android-developer/answer/6346149), and [release preparation](https://support.google.com/googleplay/android-developer/answer/9859348) | Full English body opened. Its nine body-link occurrences lead to eight unique targets: the five public Help destinations listed here were opened or verified in current topics; three Play Console track routes require sign-in. The page's 13-item Help sidebar, including the current page, is separate from its body links. Deeper descendants remain partial. |
| Same: track targeting | Play account country, production availability, and testing-track targeting | Production country selection affects current and future production releases. Testing defaults to production-country availability and can be unsynced when prerequisites are met. Internal testing has no country-targeting restriction. The target is based on the user's Play account country, not physical location. |
| Same: pricing and subscriptions | [Price setup](https://support.google.com/googleplay/android-developer/answer/6334373) · [Subscriptions](https://support.google.com/googleplay/android-developer/answer/140504) | Adding a country to a paid app automatically adds a local price; subscription prices must be checked/set separately. Country-distribution operations do not grant crypto licensing eligibility. |
| Blockchain-based Content | [Country/region crypto requirements](https://support.google.com/googleplay/android-developer/answer/16329703?hl=en) | Opened. Explains listed-market credentials, the Financial features declaration, location-specific forms, and removing markets where requirements are unmet. |
| Blockchain-based Content | Play Console Financial features form (referenced in the policy); [Financial features declaration Help](https://support.google.com/googleplay/android-developer/answer/13849271?hl=en) | The policy points to the App Content Console form; the separately opened Help article is related context, not mislabeled as a direct body link. It says all published apps must declare and lists crypto wallets, exchanges, and NFT sales/trading/awards. The form requires sign-in and the page retains a historical 2023 deadline. |
| Financial features declaration | [Financial Services policy](https://support.google.com/googleplay/android-developer/answer/9876821?hl=en) | Opened and summarized in the [Financial Services topic](../financial-services-and-loans/financial-services-and-loans.en-US.md). Its definition covers managing/investing money and cryptocurrencies and requires compliance with target-market law; binary-options trading is prohibited. |
| Blockchain-based Content | [Create an in-app product / one-time product](https://support.google.com/googleplay/android-developer/answer/1153481?hl=en), [Overview of one-time products](https://support.google.com/googleplay/android-developer/answer/16430488?hl=en) | Opened. Product details are where Play requires the Tokenized Digital Asset label. The newer catalog model separates a product, purchase option, and offer and supports regional availability. These product docs do not replace the tokenized-asset policy or authorize every NFT product. Some features are marked Early Access. |
| One-time products | [Metadata policy](https://support.google.com/googleplay/android-developer/answer/9898842?hl=en) | Opened. Titles, icons, and descriptions must be accurate, relevant, non-misleading, and suitable for audiences; Blockchain-based Content adds the specific tokenized-asset disclosure. |
| Blockchain-based Content | [Real-Money Gambling, Games, and Contests](https://support.google.com/googleplay/android-developer/answer/9877032?hl=en) | Opened. Eligible apps must apply, hold valid licenses for each location and product type, block minors/unlicensed locations, be free, avoid Play Billing, carry an AO/IARC-equivalent rating, and show responsible-gambling information. Other apps cannot facilitate cash/value-item wagers for real-world prizes; the policy also covers DFS, ads, and loyalty rewards. |
| Real-Money Gambling policy | [Gambling application form](https://support.google.com/googleplay/android-developer/contact/gambling) | The form link was opened. Developers must submit the application and license materials; public browsing cannot confirm approval for a particular account or app. |
| Real-Money Gambling policy | [Real-money gaming pilots](https://support.google.com/googleplay/android-developer/answer/12918670?hl=en) | Opened. Effective June 4, 2026; at review it said there were no active pilots. The India DFS/Rummy grace period ended January 22, 2026; the Mexico DFS pilot ended June 4, 2026. |
| Pilot page | [Online Crane Games](https://support.google.com/googleplay/android-developer/answer/12002615?hl=en) | Opened. The Japan pilot ended July 11, 2023. The current page requires submitting a declaration; a new app may be listed after acceptance, existing apps should check settings, and Google says it will notify developers within five business days. This pathway is not an NFT exemption. |
| Financial Services / developer identity | [Play Console Requirements](../play-console-requirements/play-console-requirements.en-US.md) | Existing bilingual notes cover the Organization account requirement for financial products/services businesses; verify the legal entity and actual business. |

## Pre-release checklist

1. Map exchange, custodial/non-custodial wallet, NFT sales/awards, mining management, and gameplay features to the relevant declaration categories.
2. For each target market, confirm licenses, registrations, location forms, legal entity, and permitted service scope. Do not target a market where a required credential is missing.
3. Check listing and product metadata and random-reward mechanics: label tokenized assets accurately, make no speculative earnings claims, and disclose the contents/value of NFT bundles.
4. Separately review wagers, staking, paid draws, and cash or valuable NFT prizes under the real-money gambling policy and local law. Do not extend a pilot or licensed-app pathway to ordinary NFT games.
5. Inspect device code, SDKs, and remote services to ensure the app does not mine on users' devices; remote management still needs accurate disclosure and compliance with other rules.
6. Sign in to Play Console to verify declaration status, country forms, review notices, and current eligibility. Public pages cannot establish an app's or account's approval status.

This is a paraphrased snapshot of official policy reviewed on October 22, 2026. Crypto licensing, MiCA/local implementation, Console fields, and gaming pilots can change; recheck official sources and regulators for each target market. This is not legal advice or a verbatim copy.
