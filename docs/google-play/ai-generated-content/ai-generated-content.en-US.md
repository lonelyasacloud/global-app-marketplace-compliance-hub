---
id: google-play.ai-generated-content
platform: google-play
language: en-US
authority: normative
status: current
kb_checked_at: 2026-10-24
review_due: 2027-01-24
regions: [global]
topics: [ai, generative-ai, content-safety, restricted-content, moderation]
snapshot_id: play.ai-generated-content
snapshot_package: "GooglePlay-KnowledgeBase-2026-10-24-review.zip"
coverage_status: "detailed-summary"
source_url: "https://support.google.com/googleplay/android-developer/answer/13985936?hl=en"
effective_date: "current-policy"
---

# Google Play AI-Generated Content Policy and Safety Practices

> **Import note (Google batch 4).** The body is the paraphrased summary from the already separated 2026-10-24 Google Play knowledge-base snapshot (`play.ai-generated-content`, reviewed 2026-10-24). It is not a verbatim copy of an official page. The English official source is the source of truth. `kb_checked_at` is the review date recorded in the snapshot source file; this import did not re-open the live official pages. Phrases such as “this knowledge base,” “this library,” and “local topic” describe coverage inside that snapshot, not the set of pages imported into this repository. Relative snapshot links to topics, link graphs, ledgers, or CSVs that are not in this repository are kept as text mentions. Relative links that target the Google batch 1–3 topics or these twelve batch 4 topics point at the hub files. The policy, scope explainer, best-practices article, and August 25, 2026 safety post recorded in the snapshot are English official URLs. The snapshot does not record a checked Chinese official AI-generated-content page. The Chinese hub text is the snapshot’s editorial paraphrase, not Google’s published Chinese page text. No future-effective date is recorded for this policy. The blog restates current prohibitions and adds no compliance date or fixed review SLA. The October 20, 2026 date on OWASP GenAI Red Teaming Manual v1.0 is a source date, not a Play deadline. The blog’s older policy route `answer/13823020` returned 404. The snapshot uses the accessible current page `answer/13985936` and does not treat matching subject matter as proof the routes are equivalent. That failed fetch is not a policy change. In-app reporting, restricted-output prevention, and compliance with other Play policies are `normative`. SAIF, OWASP, model-provider documentation, and the Android prompt-injection guide are implementation or industry references, not Play obligations or certifications. The OWASP manual section keeps the snapshot’s CC BY-SA 4.0 paraphrase notice. That license note covers only the snapshot’s paraphrase of that manual.

**Reviewed: 2026-10-24.** This topic summarizes Google Play's AI-generated content policy, its scope explainer, and safety best practices. It separates Play obligations from implementation references. This is a bilingual paraphrase, not a full-text mirror.

## Core requirements

| Type | Requirement |
| --- | --- |
| Policy obligation | Generative AI apps must comply with all applicable Google Play Developer Policies and prevent restricted content, including content that exploits or harms children or enables deceptive behavior. |
| Policy obligation | Apps must provide an in-app reporting or flagging feature so users can report offensive output without leaving the app. |
| Policy obligation | Developers should use user reports to inform content filtering and moderation. |
| Best practice | Google Play recommends safety testing and security practices aligned with industry standards. Filters and classifiers can help block harmful input and output. |
| Best-practice references | Google recommends the SAIF and OWASP GenAI Red Teaming Guide as references. Provider documentation is implementation material, not a Google Play endorsement or mandate. |

## Scope

AI-generated content is content created by generative AI models based on user prompts. The current scope explainer covers combinations of text, voice, and image prompts. Examples include:

- Text-to-text AI chatbot apps where chatbot interaction is a central feature.
- Apps that generate images or video from text, image, or voice prompts.
- Apps that use AI to create voice or video recordings of real-life individuals.

The current explainer says the policy is not intended to cover these limited-scope apps at this time:

- Apps that only host AI-generated content and cannot create it with AI. If such an app hosts UGC, it must still check the [User Generated Content policy](../user-generated-content/user-generated-content.en-US.md).
- Apps whose only feature is summarizing non-AI-generated content, such as search results or books.
- Productivity apps that use AI to improve an existing feature, such as email-draft suggestions.

These are examples in the scope explainer as reviewed on the date above. “Not intended to cover at this time” does not waive other policies. Reassess when an app adds generation, sharing, recommendation, or monetization features.

## Examples of violative output

Google's examples are non-exhaustive: non-consensual sexual deepfakes; voice or video of real people used to facilitate scams; content encouraging dangerous activities or self-harm; demonstrably deceptive or false election content; bullying or harassment; generative AI apps primarily intended for sexual gratification; fake official documents that enable dishonest behavior; and malicious-code creation.

Apply these examples together with [Inappropriate Content](../inappropriate-content/inappropriate-content.en-US.md), the [Age Restrictions and Child Safety topic](../age-restricted-child-safety/age-restricted-child-safety.en-US.md), [Deceptive Behavior](../deceptive-behavior/deceptive-behavior.en-US.md), and any other relevant policy. Examples do not replace a review of the actual output, prompts, and app features.

## Release and ongoing operations checklist

1. Inventory models, prompt entry points, and output types, including text, voice, images, and video; identify generation involving real people.
2. Design safeguards for restricted input and output, then test them against abuse scenarios. This is an engineering recommendation for implementing safety responsibilities, not a Google-specified model or threshold.
3. Place an easy-to-find in-app report/flag control by generated content; verify that users can submit a report without leaving the app.
4. Route reports to an accountable moderation process. Track categories, decisions, and recurrence, and use findings to improve filters and moderation.
5. Cover model, implementation, infrastructure, and runtime behavior in safety assessments. Retest when model or prompt flows change.
6. If other users can view, share, comment on, or receive recommendations for outputs, also assess the [UGC and Moderation topic](../user-generated-content/user-generated-content.en-US.md) and applicable child-safety, privacy, and ratings requirements.
7. Recheck the Developer Policy Center and relevant Play Console declarations when features, models, target users, or distribution change.

## Policy page, scope explainer, and direct-link audit

### AI-Generated Content policy

| Direct body link | Relationship to this policy |
| --- | --- |
| [Policy Coverage](https://support.google.com/googleplay/android-developer/answer/10146128?hl=en) | Explains that Play policies cover content an app displays or links to, ads, UGC, and public developer materials. |
| [Restricted Content](https://support.google.com/googleplay/android-developer/topic/9877467?hl=en) | Restricted-content policy collection; the linked topics are listed below. |
| [Child Endangerment](https://support.google.com/googleplay/android-developer/answer/9878809?hl=en) | Applies to AI output involving child exploitation or abuse; see the [child-safety topic](../age-restricted-child-safety/age-restricted-child-safety.en-US.md). |
| [Deceptive Behavior](https://support.google.com/googleplay/android-developer/answer/17006354?hl=en) | Applies to output that enables deceptive or dishonest behavior; see the [local topic](../deceptive-behavior/deceptive-behavior.en-US.md). |
| [Best Practices to Safeguard AI-Generated Content](https://support.google.com/googleplay/android-developer/answer/16353813?hl=en) | Google Play's AI safety guidance; direct external resources are listed below. |

The policy page's Restricted Content navigation lists these 10 topics. They are policy-directory links; an AI safety review should identify the topics relevant to its actual content and features.

| Policy topic | Official page | Local topic |
| --- | --- | --- |
| Child Endangerment | [Official page](https://support.google.com/googleplay/android-developer/answer/9878809?hl=en) | [Age restrictions and child safety](../age-restricted-child-safety/age-restricted-child-safety.en-US.md) |
| Inappropriate Content | [Official page](https://support.google.com/googleplay/android-developer/answer/9878810?hl=en) | [Inappropriate Content](../inappropriate-content/inappropriate-content.en-US.md) |
| Financial Services | [Official page](https://support.google.com/googleplay/android-developer/answer/9876821?hl=en) | [Financial services and loans](../financial-services-and-loans/financial-services-and-loans.en-US.md) |
| Real-Money Gambling, Games, and Contests | [Official page](https://support.google.com/googleplay/android-developer/answer/9877032?hl=en) | [Real-Money Gambling](../real-money-gambling/real-money-gambling.en-US.md) |
| Illegal Activities | [Official page](https://support.google.com/googleplay/android-developer/answer/9878877?hl=en) | [Illegal Activities](../illegal-activities/illegal-activities.en-US.md) |
| User Generated Content | [Official page](https://support.google.com/googleplay/android-developer/answer/9876937?hl=en) | [UGC and Moderation](../user-generated-content/user-generated-content.en-US.md) |
| Health Content and Services | [Official page](https://support.google.com/googleplay/android-developer/answer/16679511?hl=en) | Health apps and Health Connect (snapshot: `health-apps-and-health-connect-en.md`, not imported in this repository) |
| Blockchain-based Content | [Official page](https://support.google.com/googleplay/android-developer/answer/13607354?hl=en) | [Crypto assets and NFTs](../crypto-assets-and-nfts/crypto-assets-and-nfts.en-US.md) |
| AI-Generated Content | [Official page](https://support.google.com/googleplay/android-developer/answer/13985936?hl=en) | This topic |
| Age-Restricted Content and Functionality | [Official page](https://support.google.com/googleplay/android-developer/answer/16302250?hl=en) | [Age restrictions and child safety](../age-restricted-child-safety/age-restricted-child-safety.en-US.md) |

### Scope explainer

[Understanding Google Play's AI-Generated Content policy](https://support.google.com/googleplay/android-developer/answer/14094294?hl=en) directly links to Inappropriate Content, child exploitation/abuse content, Deceptive Behavior, and the Developer Policy Center. It also points to [User Generated Content](https://support.google.com/googleplay/android-developer/answer/9876937?hl=en) when an app only hosts AI-generated UGC. Related Content navigation lists the AI policy, Restricted Content, Deceptive Behavior, and Families Policies. The key local topics are cross-linked here; the Help Center's generic 32-item learning sidebar is not treated as body-linked content.

### Direct safety resources from the best-practices page

[Best Practices to Safeguard AI-Generated Content](https://support.google.com/googleplay/android-developer/answer/16353813?hl=en) directly lists SAIF, OWASP, and resources from eight providers. Google Play presents them as safety references. Third-party material must not be described as a Google Play obligation.

| Resource | Page | Relationship to Play requirements |
| --- | --- | --- |
| Google Secure AI Framework (SAIF) | [Framework overview](https://saif.google/secure-ai-framework) | Organizes AI risks and controls across data, infrastructure, model, and application areas. Opened the [map tour](https://saif.google/secure-ai-framework/saif-map), [components](https://saif.google/secure-ai-framework/components), [risks](https://saif.google/secure-ai-framework/risks), [controls](https://saif.google/secure-ai-framework/controls), [AI development primer](https://saif.google/ai-development-primer), and [risk self-assessment](https://saif.google/risk-self-assessment). The page also links to the [CoSAI Risk Map repository](https://github.com/cosai-oasis/secure-ai-tooling/tree/main/risk-map), which was opened; the [agent-specific diagram](https://gweb-saif-stg.appspot.com/focus-on-agents) redirects to Google sign-in and could not be read. SAIF says its material is for industry information/inspiration and does not reflect Google's current technical implementations. |
| OWASP GenAI Red Teaming Guide | [Guide overview](https://genai.owasp.org/resource/genai-red-teaming-guide/) · [Guide PDF](https://genai.owasp.org/download/44859/) | The overview covers model evaluation, implementation testing, infrastructure assessment, and runtime behavior; the 2025 PDF was opened earlier, but a current retry timed out. The resource also links to the [GenAI Red Teaming Manual v1.0 (October 20, 2026)](https://genai.owasp.org/resource/genai-red-teaming-manual-version-1-0/) and its [144-page PDF](https://genai.owasp.org/download/58204/), which was opened and summarized for AI application/content-safety relevance below. It also lists the [Agent Control Standard](https://genai.owasp.org/resource/agent-control-standard-acs/) and [GenAI Security Industry Framework Crosswalk](https://genai.owasp.org/resource/genai-security-industry-framework-crosswalk/). These are OWASP references, not Play obligations or certifications. |
| Google Responsible GenAI Toolkit | [Resource](https://ai.google.dev/responsible) | Google developer material on responsible AI design, evaluation, and safeguards; implementation reference. |
| Microsoft AI Content Safety | [Product information](https://azure.microsoft.com/en-us/products/ai-services/ai-content-safety) | Vendor content-filtering material; not a Play certification. |
| OpenAI Safety best practices | [Developer guide](https://developers.openai.com/api/docs/guides/safety-best-practices) | API implementation guidance; not Play policy. |
| Anthropic Content Moderation | [Use-case guide](https://platform.claude.com/docs/en/about-claude/use-case-guides/content-moderation) | Vendor moderation guidance; not Play policy. |
| AWS Responsible Content Moderation | [Solution information](https://docs.aws.amazon.com/solutions/responsible-content-moderation-with-ai-services-on-aws/) | AWS solution reference; not Play policy. |
| Meta Responsible Use Guide | [Guide PDF](https://ai.meta.com/static-resource/responsible-use-guide/) | Meta responsible-use reference; not Play policy. |
| Salesforce Trusted AI | [Resource](https://www.salesforce.com/artificial-intelligence/trusted-ai/) | Salesforce trust and safety material; not Play policy. |
| Cohere Safety Modes | [Documentation](https://docs.cohere.com/docs/safety-modes) | Cohere model-specific safety-mode documentation; not Play policy. |

### OWASP GenAI Red Teaming Manual v1.0 (October 2026)

The [OWASP resource page](https://genai.owasp.org/resource/genai-red-teaming-manual-version-1-0/) is dated October 20, 2026. Its [144-page PDF](https://genai.owasp.org/download/58204/) is Version 1.0, October 2026. The table of contents, license, and sections relevant to AI application/content safety were reviewed; this is not a page-by-page transcription of all 144 pages. The manual does not set Google Play rules. It extends the Play best-practices article's reference to OWASP safety testing; it is not a Play review standard, certification, or additional compliance obligation.

The manual organizes red teaming into eight phases:

1. **Planning & Scoping:** Agree on systems, models, data, identity and access, objectives, success criteria, rules of engagement, and stop conditions; record external services outside scope.
2. **Reconnaissance & Fingerprinting:** Gather public artifacts, dependency, and supply-chain context, and label unverified assumptions.
3. **Surface Mapping:** Map orchestration, retrieval/RAG, tools, trust boundaries, and data flows into a threat model.
4. **Exploitation & Impact:** Test direct model weaknesses, application pathways, multimodal inputs, agent actions, resource exhaustion, and evasion of input/output guardrails and safety classifiers.
5. **Persistence & Escalation:** Examine data exfiltration, agent privilege escalation, and persistence across turns or state.
6. **Post-Exploitation:** Validate attacker capability, blast radius, business and safety impact, severity, and containment options.
7. **Evaluation & Reporting:** Define pass/fail/needs-review criteria in advance; preserve reproducible evidence, coverage, budgets, and limitations. Missing logs or telemetry are not a defensive pass.
8. **Post-Engagement & Remediation:** Fix guardrail and architectural gaps, retest the fix, turn confirmed attacks into regression cases, and update monitoring and response procedures.

**Application to Google Play AI apps:** Design tests around the app's actual input, output, retrieval, and tool paths. Use Play's prohibited restricted-content categories as test-scope references, and verify the required in-app report/flag flow for offensive output and the developer's follow-up moderation process. Run regression checks before release, after onboarding a model or feature, and after changing the model, guardrails, retrieval, or agent tools. Prefer isolated environments, dedicated test accounts, synthetic data, and mock tools so testing cannot reach real user data or production actions. These are implementation suggestions derived from OWASP; Play's reporting and content-policy obligations remain defined by Google's official policies.

**Source license:** The original manual is licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/legalcode). This section is a paraphrased summary based on the OWASP GenAI Security Project's *GenAI Red Teaming Manual v1.0* (October 2026), not the official text; this summary follows the same license. Other parts of the knowledge base have their own source and license terms.

The best-practices article's Related Content also links AI-Generated Content, Restricted Content, Deceptive Behavior, and [Google Play Families Policies](https://support.google.com/googleplay/android-developer/answer/9893335?hl=en). The SAIF/OWASP pages and provider material contain deeper site links; this topic lists key descendants that were opened and does not claim recursive closure across those external sites. The generic 32-item Help Center sidebar is not counted as body links.

### Official AI safety blog: NCII and review readiness (August 25, 2026)

[Ensuring Safety in the Generative AI Ecosystem: Protecting Users from Non-Consensual Intimate Content](https://developer.android.com/blog/posts/ensuring-safety-in-the-generative-ai-ecosystem-protecting-users-from-non-consensual-intimate-content) is an official Android Developers post about Google Play safety. It sits outside the 58-item Help Center announcement directory. It reiterates Play's prohibition on facilitating, creating, or distributing non-consensual sexual content, then addresses NCII, “nudify/undress” features, deepfakes, and explicit-image editing in review readiness and safety practice. It adds no compliance date or fixed review SLA.

| Direct body link | Target content and relationship | Access and scope |
| --- | --- | --- |
| [Priority Flagger Program](https://transparency.google/intl/en_uk/tools-programs/partner-programs/) | A voluntary partner program for qualified organizations, with a dedicated reporting channel and policy discussions. Reports receive priority review, but are not automatically removed and do not receive different policy treatment. | Body target opened; its DSA, copyright, and child-safety-toolkit descendants are mapped in recursive graph §4.142 (snapshot: `../google-play-policy-link-graph-en.md`, not imported in this repository). |
| [Sexual Content and Profanity / Inappropriate Content](https://support.google.com/googleplay/android-developer/answer/9878810?hl=en) | The formal Play policy prohibits non-consensual sexual content, apps that claim to undress people or see through clothing, and non-consensual sexual deepfakes. See the [Inappropriate Content topic](../inappropriate-content/inappropriate-content.en-US.md). | Current policy body and examples opened and cross-checked against the blog. |
| [AI-Generated Content policy (blog target answer/13823020)](https://support.google.com/googleplay/android-developer/answer/13823020) | The blog cites the AI policy, but this exact target returned 404. The KB separately covers the accessible current [AI-Generated Content page, answer/13985936](https://support.google.com/googleplay/android-developer/answer/13985936?hl=en); matching subject matter alone does not prove the two routes are equivalent. | Original target unreadable; use the accessible current policy and retain the old route as unresolved. |
| [Best Practices to Safeguard AI-Generated Content](https://support.google.com/googleplay/android-developer/answer/16353813?hl=en) | Play recommends industry-aligned safety testing, filters/classifiers, and references such as SAIF, OWASP, and model-provider resources; developers remain responsible for app outputs. | The full target and its ten direct safety resources are already summarized in this topic and §4.142. |
| [App Promotion policy](https://support.google.com/googleplay/android-developer/answer/9899004?hl=en) | Advertising “nudify” capabilities outside the store may violate App Promotion policy even when the app lacks that functionality; promotional content must accurately represent the app. | Bilingual policy summary already exists; apply the current text to the actual promotion. |
| [Google Ads: Inappropriate content](https://support.google.com/adspolicy/answer/6015406?hl=en) | Google Ads separately prohibits promotion of synthetic explicit/nude content; the page says serious violations can lead to Ads account suspension. The blog also reminds developers that they remain responsible for ads for their apps, including ads made by authorized third parties. | Ads page opened. This is Ads serving policy and enforcement, distinct from Play app-distribution policy. |
| [Android core practices (actual target: Mitigate prompt injection attacks)](https://developer.android.com/privacy-and-security/risks/ai-risks/prompt-injection) | Android guidance recommends limiting model permissions, isolating untrusted input, validating output, requiring human approval for risky actions, and running regular adversarial tests. | Six reference-link occurrences reduce to five target slots; four hrefs are verifiable, while the Vertex AI anchor did not expose a URL. This is Android implementation guidance, not a new Play obligation. See §4.142. |
| [Report a Policy Violation](https://support.google.com/googleplay/android-developer/contact/policy_violation_report?rd=1) | A reporting form for alleged violations in apps published on Google Play; it asks for a category, package name, and a good-faith, supportable report. | Form opened. It is a reporting channel, not policy text or an adjudication. |

**Operational review checklist from the post:** Ensure review accounts can use all AI features, including paid or geo-fenced functions, without a subscription wall blocking review. Keep evidence of tested adversarial prompts, edge cases, and model refusals, especially for nudify/undress, deepfake, and explicit-image editing or generation. Do not rely only on the underlying model's native filters; add app-level input/output controls and keep monitoring user feedback and failed prompts. The post says complex AI-safety evaluations and appeals may sometimes take longer, but sets no specific duration. Treat these as review-readiness and engineering checks, not a new deadline or policy clause.

**Recursive boundary:** This pass covers the post's eight unique body destinations, six reference-link occurrences on the Android prompt-injection guide (five target slots after deduplicating the two SAIF anchors, of which four hrefs are verifiable), four body targets on the Priority Flagger page, and one “Continue reading” related article. The old AI-policy route returned 404, and the DSA Trusted Flagger onboarding destination requires an approved identity and could not be read. OWASP research references, all external descendants of the engineering resources, and generic navigation are not exhausted. Per-target states are in the source-page audit (snapshot: `../source-page-audit.csv`, not imported in this repository).

## Sources and related topics

- [AI-Generated Content policy](https://support.google.com/googleplay/android-developer/answer/13985936?hl=en) · [Scope explainer](https://support.google.com/googleplay/android-developer/answer/14094294?hl=en) · [Safety best practices](https://support.google.com/googleplay/android-developer/answer/16353813?hl=en)
- [Policy Coverage](https://support.google.com/googleplay/android-developer/answer/10146128?hl=en) · [Restricted Content](https://support.google.com/googleplay/android-developer/topic/9877467?hl=en) · [Developer Policy Center](https://play.google.com/about/developer-content-policy/)
- [UGC and Moderation](../user-generated-content/user-generated-content.en-US.md) · [Inappropriate Content](../inappropriate-content/inappropriate-content.en-US.md) · [Deceptive Behavior](../deceptive-behavior/deceptive-behavior.en-US.md) · [Age restrictions and child safety](../age-restricted-child-safety/age-restricted-child-safety.en-US.md)
