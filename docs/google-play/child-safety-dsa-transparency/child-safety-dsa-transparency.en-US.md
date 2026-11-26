---
id: google-play.child-safety-dsa-transparency
platform: google-play
language: en-US
authority: regulatory
status: current
kb_checked_at: 2026-10-22
review_due: 2027-01-22
regions: [EU, EEA, UK]
topics: [child-safety, dsa, transparency-reporting, age-appropriate-design, external-guidance]
snapshot_id: external.child-safety-dsa-transparency
snapshot_package: "GooglePlay-KnowledgeBase-2026-10-24-review.zip"
coverage_status: "source-backed-summary"
source_url: "https://digital-strategy.ec.europa.eu/en/library/commission-publishes-guidelines-protection-minors"
---

# Child Safety: DSA Guidance and Transparency Practices

> **Import note (Google batch 3).** The body is the paraphrased summary from the already separated 2026-10-24 Google Play knowledge-base snapshot (`external.child-safety-dsa-transparency`, reviewed 2026-10-22). It is not a verbatim copy of an official page. The English official source is the source of truth. `kb_checked_at` is the review date recorded in the snapshot source file; this import did not re-open the live official pages. Phrases such as “this knowledge base,” “this library,” and “local topic” describe coverage inside that snapshot, not the set of pages imported into this repository. Relative snapshot links to topics, link graphs, ledgers, or CSVs that are not in this repository are kept as text mentions. Relative links that target the Google batch 1 and 2 topics or these nine batch 3 topics point at the hub files. This page records EU and industry child-safety transparency material. It does not create Google Play policy requirements. The Commission published the Article 28 guidelines on 2025-07-14; the Official Journal text is C/2025/5519 dated 2025-10-10; the Commission explainer cited in the snapshot was updated 2026-04-22. Those are source dates, not future Play effective dates. The snapshot does not record a checked Chinese official page for these external sources. The Chinese hub text is the snapshot’s editorial paraphrase. EUR-Lex automated-fetch limits recorded in the source are access limits, not changes to the law. Evidence level: `regulatory` for the DSA text and Commission guidelines; the Tech Coalition materials are industry guidance and are not Play rules, EU law, or Commission guidance.

**Reviewed October 22, 2026.** This page separates the EU legal and industry resources adjacent to Google Play's child-safety rules. They can inform cross-border product risk reviews, but **they do not automatically create new Google Play policy requirements**. Use current Google Play rules for Play submissions and assess the EU Digital Services Act (DSA), the UK Children's Code, and other local requirements according to the service's role, location, and scope.

## Distinguish the four source types

| Source | Nature | Relationship to Play child safety |
| --- | --- | --- |
| [Google Play Child Safety Standards explainer](https://support.google.com/googleplay/android-developer/answer/14747720?hl=en) | Play policy explanation and Play Console self-certification requirements for in-scope developers. | Direct basis for Play review; see the [bilingual age-restriction and child-safety topic](../age-restricted-child-safety/age-restricted-child-safety.zh-CN.md). |
| [DSA Regulation (EU) 2022/2065](https://eur-lex.europa.eu/eli/reg/2022/2065/oj/eng) and Article 28 minor-protection guidelines | EU law and Commission guidance/recommendations. The Commission published the guidelines on July 14, 2025; the Official Journal text is C/2025/5519 (October 10, 2025). The Commission says following the guidelines is voluntary, but it will use them as a reference when assessing Article 28(1); following them does not by itself guarantee compliance. | Applicability depends on DSA service category, territory, and exceptions. It is not interchangeable with Play policy. The Commission page describes the guidelines as applying to online platforms accessible to minors, with an exception for micro and small enterprises. |
| [Tech Coalition Trust framework](https://technologycoalition.org/resources/trust-voluntary-framework-for-industry-transparency/) | A voluntary industry transparency framework. Its overview describes a 2024 update; the currently downloadable full framework PDF is the 2025 version. | Useful for organizing governance, processes, and outcome data; it does not replace law, Play self-certification, or service-specific risk review. |
| [Tech Coalition × Tremau DSA transparency guide](https://technologycoalition.org/resources/dsa-transparency-compliance-guide/) | Industry interpretation published in 2024; the PDF was revised in December 2024. It is not EU law or official Commission guidance. | Useful for understanding how Trust overlaps with DSA transparency, but its reporting-template and minors-guidance sections need to be checked against later official sources. |

## EU DSA minor-protection guidelines: current official reference

The Commission published its Article 28 minor-protection guidelines on July 14, 2025. The Official Journal communication dated October 10, 2025 is **C/2025/5519**. The Commission's explainer, updated April 22, 2026, summarizes a risk-based approach tailored to the platform's nature, size, purpose, and user base, grounded in children's rights and privacy and safety by design. Measures should not disproportionately restrict children's rights.

The Commission highlights private-by-default minor accounts; changes to recommender systems to reduce harmful-content exposure and rabbit holes; blocking, muting, and consent-based group controls; restrictions on downloading or capturing minors' posts; disabling certain engagement features by default; safeguards against exploiting children's limited commercial literacy; and better moderation, reporting, feedback, and parental-control tools. Age-assurance methods should be accurate, reliable, robust, non-intrusive, and non-discriminatory. Stronger age verification may be appropriate for adult content or where national rules set an age threshold.

The Commission also links to the [Age Verification Blueprint technical portal](https://ageverification.dev/). It describes a design based primarily on zero-knowledge proofs that reveals whether a user meets an age threshold without sharing identity or date of birth with the service. In August 2026, the portal updated its architecture and threat model. This is technical reference material, not a Play mandate to adopt a particular API; its setup, architecture, and verifier documents have not all been added to this topic.

**Use the right authority:** The Commission guidelines are a non-exhaustive set of recommendations; they do not replace the DSA text or national regulator interpretation. Cross-border services should check official guidance and the competent authority rather than rely only on the 2024 Tech Coalition guide.

### Relevant direct links from the Commission page

| Direct child link | Content and relationship | Review status |
| --- | --- | --- |
| [Official DSA minors-guidelines page](https://digital-strategy.ec.europa.eu/en/library/commission-publishes-guidelines-protection-minors) · [Official Journal text on EUR-Lex](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX%3A52025XC05519) | The official text is organized around general principles, risk review, service design, reporting/user support/guardian tools, and governance. | Commission page fully opened and summarized. EUR-Lex PDF extraction was blocked by bot verification; logged using the readable Commission summary and document metadata. |
| [Family-friendly DSA minors booklet](https://digital-strategy.ec.europa.eu/en/library/digital-service-act-dsa-explained-what-online-platforms-should-do-keep-kids-and-teens-safe-online) | Plain-language explanation of child rights, privacy and safety by design, age checks, private settings, moderation, reporting, and support for parents. | Page opened; download files and all language editions were not expanded. |
| [DSA user-rights fact page](https://digital-strategy.ec.europa.eu/en/factpages/user-rights-under-digital-services-act) | Explains reporting illegal content, understanding moderation decisions, internal complaints, and external redress. | Page opened. Developer implementation duties should be checked in the DSA text and guidance. |
| [Commission DSA guidelines index](https://digital-strategy.ec.europa.eu/en/policies/dsa-guidelines) | Explains that Commission guidelines are non-binding recommendations that can be a reference for regulatory assessment. | Page reviewed; useful for finding updates. |
| [EU Age Verification Blueprint](https://ageverification.dev/) | Commission technical portal with the blueprint, open reference implementation, and developer/verifier guides. | Overview opened; deeper installation, protocol, trust-list, and threat-model documents remain to be reviewed. |

### DSA transparency reporting: distinguish official templates from industry frameworks

The Tech Coalition DSA guide groups transparency into three areas: terms that explain permitted and prohibited conduct; explanations to users affected by moderation decisions; and public reporting of moderation activity. It also maps obligations by provider/service tier and compares them with Trust's three reporting areas: policies and practices, processes and systems, and outcomes.

**Check the legal instrument's name:** Some passages in the Tech Coalition PDF call the Commission instrument a “Delegated act.” The EU's official transparency-reporting template instrument is [Commission Implementing Regulation (EU) 2024/2835](https://eur-lex.europa.eu/eli/reg_impl/2024/2835/oj/eng), an **implementing regulation**. The Commission says the harmonized format has applied since July 1, 2025. Use the Regulation, DSA text, and current Commission page rather than repeating shorthand or transition-period descriptions in the 2024 industry PDF.

### Trust framework and operational resources

The downloadable [full Trust framework PDF](https://technologycoalition.org/wp-content/uploads/tech-coalition-trust-framework-2025.pdf) is voluntary industry guidance. It says reporting should be tailored to the service's risk and maturity, not used for simplistic cross-service rankings. Its five principles can be summarized as: support trust and accountability; reflect the nature of the service; match company maturity; report regularly and evolve (aim at least annually); and protect privacy and safety so reporting does not help offenders bypass safeguards.

The framework groups report content into **policies and practices, processes and systems, and outcomes**. Useful starting metrics include CSEA identified and actioned, accounts identified and actioned, and reports to external authorities. Define each metric, scope, period, counting method, and limitation. Avoid double counting and do not present a platform's moderation volume as a measure of societal prevalence.

In June 2026, the Tech Coalition published [Transparency reporting for generative AI](https://technologycoalition.org/resources/trust-transparency-reporting-for-generative-ai/) and a [nine-page PDF](https://technologycoalition.org/wp-content/uploads/transparency-reporting-for-generative-ai.pdf). It applies the Trust structure to model policies, training-data governance, safety evaluation/red teaming, detection and mitigation, moderation and enforcement, and outcome data. It recommends defining metrics while avoiding disclosure of safety details that could be abused. This is child-safety industry guidance, not a substitute for Google Play's AI-generated-content policy; see the AI-generated content topic ([Google Play AI-Generated Content Policy and Safety Practices](../ai-generated-content/ai-generated-content.en-US.md)).

### Descendant pages, best practices, and access records

| Parent → direct target | Summary / Play relationship | Access status |
| --- | --- | --- |
| [Trust Framework updates and New DSA Resource (July 23, 2024)](https://technologycoalition.org/news/updates-to-trust-framework-and-new-dsa-resource/) → [Trust launch article](https://technologycoalition.org/news/tech-coalition-launches-trust-voluntary-framework-for-industry-transparency/), [Microsoft interview](https://technologycoalition.org/blog/one-on-one-with-liz-thomas/), [2023 Annual Report / action plan PDF](https://paragonn-cdn.nyc3.cdn.digitaloceanspaces.com/technologycoalition.org/uploads/Tech_Coalition_Annual-Report-2023.pdf), and the [DSA guide](https://technologycoalition.org/resources/dsa-transparency-compliance-guide/) | The announcement says Trust was updated in 2024 and adds DSA support material. The 2022 launch article and interview explain its voluntary industry background; the 2023 report is a historical progress record, not a current policy requirement. | Announcement, launch article, and interview opened; the 29-page report is readable and was sampled as historical material, not used as a current obligation source. |
| Trust update page → [full Trust framework PDF](https://technologycoalition.org/wp-content/uploads/tech-coalition-trust-framework-2025.pdf) | Voluntary framework covering proportionality, metric definitions, reporting boundaries, and privacy/safety protections. | Full 16-page PDF opened; this library uses paraphrased summary only. |
| Trust update page → [Transparency reporting implementation guide](https://technologycoalition.org/resources/trust-transparency-reporting-implementation-guide/) · [2024 PDF](https://technologycoalition.org/wp-content/uploads/Tech_Coalition_Trust_Implementation_Guide_2024_FINAL.pdf) | Covers audiences, metric-tracking systems, staged reporting, executive support, publication communications, and the risk of data exposure or evasion. Early-stage teams can start with a spreadsheet and mature the process over time. | Page and full 14-page PDF opened; this is Tech Coalition guidance, not a mandatory Play process. |
| Trust guide → [Transparency Reporting Template](https://technologycoalition.org/resources/transparency-reporting-template/) · [Google Docs template](https://docs.google.com/document/d/1FiBI3rRC1D9UytXUrRSOZasWbfnEgesAA4EpIdUqL0w/edit?tab=t.0) | The template separates policies/practices, processes/systems, and outcomes, and distinguishes expected from optional or aspirational items. | Template landing page opened; Google Docs returned a cache miss, so its fields could not be read. |
| [Trust transparency resource index](https://technologycoalition.org/resources/transparency/) → [Transparency reporting for generative AI](https://technologycoalition.org/resources/trust-transparency-reporting-for-generative-ai/) | Applies Trust to model policy, training/red teaming, and handling outputs; cross-reference the Google Play AI-generated-content and child-safety topics. | Resource index, landing page, and full nine-page PDF opened; the GenAI resource was published June 17, 2026. |
| DSA guide landing page → [28-page guide PDF](https://technologycoalition.org/wp-content/uploads/Tech-Coalition-Guide-to-Transparency-under-the-EU-DSA-Final.pdf) | The PDF separates DSA transparency into user terms, explanations to users affected by moderation, and public reporting, with tiers by service type. It is industry interpretation, not the regulation. | Landing page and PDF opened; the PDF is marked revised December 2024. |
| DSA guide → [EU Regulation 2024/2835](https://eur-lex.europa.eu/eli/reg_impl/2024/2835/oj/eng) · [Commission transparency page](https://digital-strategy.ec.europa.eu/en/policies/dsa-brings-transparency) | Official implementing regulation defines standardized reporting templates; required fields and periods vary by service category. | EUR-Lex body extraction was limited; instrument title/number/date were checked against EUR-Lex search output and Commission guidance. |
| DSA guide → [IEEE 2089-2021](https://standards.ieee.org/ieee/2089/7633/) · [CEN-CENELEC CWA 18016:2023 PDF](https://www.cencenelec.eu/media/CEN-CENELEC/CWAs/ICT/cwa18016_2023.pdf) | Process guidance for recognizing child users, evaluating age-appropriate design risks, and validating decisions across a service lifecycle, grounded in children's rights. | IEEE standards page opened; full text requires subscription/access program. Full 54-page CWA opened. CWA explicitly says it is not an official CEN/CENELEC standard. |
| DSA guide → [5Rights 2024 best-practice baseline PDF](https://5rightsfoundation.com/wp-content/uploads/2024/10/241001_Note-on-the-EC-Art.-28-DSA-guidelines-protection-of-minors_SIGNATURES.pdf) | Civil-society recommendations for Article 28 guidance: child-rights assessments, privacy-preserving age assurance, safe defaults, data minimization, reporting/redress, and governance. | Full three-page PDF opened; advocacy recommendations, not final law. |
| DSA guide → [UK ICO Age Appropriate Design Code](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/childrens-information/childrens-code-guidance-and-resources/age-appropriate-design-a-code-of-practice-for-online-services/) | UK child-data design code addressing best interests, DPIAs, transparency, default settings, minimization, location, parental controls, profiling, and nudge techniques. | ICO page opened; UK data-protection context does not automatically apply to every developer or territory. |
| Trust 2025 framework → [ECPAT Luxembourg Guidelines](https://ecpat.org/luxembourg-guidelines/) | Multi-stakeholder terminology guide for clearer language across organizations and research; it is not a source of binding legal definitions. | Landing and download pages opened. Metadata for nine translations recorded, but translations were not compared page by page. |

#### ECPAT terminology guide download descendants

The Trust PDF directly links to the ECPAT Luxembourg Guidelines. The ECPAT page also offers nine language editions and a translation/adaptation handbook. The English and Traditional Chinese PDFs checked here show a **CC BY-NC-ND 4.0** license; check each other translation's own license before reuse. This library links to them and paraphrases their purpose; it does not copy or adapt their text.

| File | Source PDF / pages | Review note |
| --- | --- | --- |
| English | [PDF](https://ecpat.org/wp-content/uploads/2021/05/Terminology-guidelines-396922-EN-1.pdf), 114 pages | Main reference edition; file metadata and license identified. |
| French | [PDF](https://ecpat.org/wp-content/uploads/2021/05/Terminology-guidelines-396922-FR.pdf), 122 pages | French translation. |
| Spanish | [PDF](https://ecpat.org/wp-content/uploads/2021/05/Terminology-guidelines_Spanish_version-electronica_FINAL.pdf), 126 pages | Spanish translation. |
| Turkish | [PDF](https://ecpat.org/wp-content/uploads/2021/05/Terminology-Guidelines-sexual-exploitation-of-children-Turkish-2019.pdf), 124 pages | Turkish translation. |
| German | [PDF](https://ecpat.org/wp-content/uploads/2021/05/ECPAT-Terminologischer-Leitfaden-DE.pdf), 131 pages | German translation. |
| Bosnian | [PDF](https://ecpat.org/wp-content/uploads/2021/05/Zastita-djece-od-seksualnog-iskoristavanja-i-zlostavljanja-ZA-WEB-SPREAD.pdf), 58 pages | Bosnian translation. |
| Traditional Chinese | [PDF](https://ecpat.org/wp-content/uploads/2022/01/%E5%B0%8D%E5%A4%96%E5%85%AC%E9%96%8B%E7%89%88%E6%9C%AC%E4%BF%9D%E8%AD%B7%E5%85%92%E7%AB%A5%E5%B0%88%E6%9C%89%E5%90%8D%E8%A9%9ETraditional-Chinese_The-Terminology-Guidelines.pdf), 120 pages | Traditional Chinese translation; PDF identifies the same license. |
| Dutch | [PDF](https://ecpat.org/wp-content/uploads/2022/02/20220202_DC_Terminologiegids_web-2.pdf), 133 pages | Dutch translation. |
| Polish | [PDF](https://ecpat.org/wp-content/uploads/2022/11/WYTYCZNE_TERMINOLOGICZNE_ECPAT_FDDS_FINAL.pdf), 126 pages | Polish translation. |
| Translation/adaptation handbook | [PDF](https://ecpat.org/wp-content/uploads/2021/05/Handbook-for-the-translation-and-adaption-of-the-Terminology-Guidelines-for-the-protection-of-children-from-sexual-exploitation-and-sexual-abuse.pdf), 32 pages | 2017 methodology guide for adapting translations; not an additional policy. |

## A practical review workflow

1. **Label the source of each obligation:** Separate Play rules, local law, regulator guidance, and industry recommendations in internal checklists; retain source URLs and review dates.
2. **Review risk by product and audience:** Check stranger communication, UGC, recommendations, search, direct messages, groups, AI chat, ads, and purchasing. Record intended users and evidence that children may access the service.
3. **Translate risk into controls:** Consider default privacy, age-appropriate design, reporting/blocking, moderation escalation, parental tools, and age assurance accuracy/data minimization. Do not collect more data for age checks than the purpose requires.
4. **Keep metrics interpretable:** Define the numerator, denominator, reporting period, deduplication rules, external reporting routes, and known limitations. Before publication, check for identity exposure or information that could help offenders evade detection.
5. **Recheck on change:** Update risk records when features, SDKs, audience, law, Play policy, or regulator guidance changes. An annual transparency report does not replace Console declarations or timely incident response.

## Coverage and remaining gaps

This pass covers the child-safety/transparency links in the DSA guide, the Trust framework and its implementation materials, the generative-AI reporting resource, ECPAT translations, and current Commission DSA references. It does not recursively treat headers/footers, every linked Tech Coalition member report, every news citation, or every implementation document in the Age Verification Blueprint as child-safety policy nodes. The Google Docs template and two EUR-Lex bodies remain blocked by automated fetching and should be reviewed in an interactive or authorized environment. Source edges, access states, and follow-up targets are in the source-link ledger (snapshot: `../SOURCE_LEDGER-en.md`, not imported in this repository).

## Related topics

- [Age restrictions, anonymous chat, and child safety](../age-restricted-child-safety/age-restricted-child-safety.en-US.md)
- AI-generated content policy and safety practices ([Google Play AI-Generated Content Policy and Safety Practices](../ai-generated-content/ai-generated-content.en-US.md))
- [User-generated content and moderation](../user-generated-content/user-generated-content.en-US.md)
- [User data and privacy](../user-data/user-data.en-US.md)
