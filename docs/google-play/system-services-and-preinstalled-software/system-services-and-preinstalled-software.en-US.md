---
id: google-play.system-services-and-preinstalled-software
platform: google-play
language: en-US
authority: operational
status: current
kb_checked_at: 2026-10-22
review_due: 2027-01-22
regions: [global]
topics: [system-services, preinstalled, OEM, carrier, SoC, exemption]
snapshot_id: play.system-services
snapshot_package: "GooglePlay-KnowledgeBase-2026-10-24-review.zip"
coverage_status: "detailed-summary"
source_url: "https://support.google.com/googleplay/android-developer/answer/12085265?hl=en"
source_url_partner_center: "https://docs.partner.android.com/partners/guides/system-services"
source_url_zh: "https://support.google.com/googleplay/android-developer/answer/12085265?hl=zh-CN"
effective_date: "public eligibility pointer only; Partner Center criteria were not readable; no 2027-01-27"
---

# Google Play System Services and Pre-installed Software Exemption

> **Import note (Google batch 8).** The body is the paraphrased summary from the already separated 2026-10-24 Google Play knowledge-base snapshot (`play.system-services`, reviewed 2026-10-22). It is not a verbatim copy of an official page. The English official source is the source of truth. `kb_checked_at` is the review date recorded in the snapshot source file; this import did not re-open the live official pages. Phrases such as “this knowledge base,” “this library,” and “local topic” describe coverage inside that snapshot, not the set of pages imported into this repository. Relative snapshot links to topics, link graphs, ledgers, or CSVs that are not in this repository are kept as text mentions. Relative links that target the Google batch 1–7 topics or these thirteen batch 8 topics point at the hub files. Reviewed 2026-10-22. The Chinese file records the Help URL as `hl=zh-CN`. The snapshot does not record a failed fetch of that route or a line-by-line comparison with English. The Chinese hub text is an editorial paraphrase of the short public page. The Partner Center guide returned a cache miss and requires partner access. No internal eligibility criteria are recorded. Help Community returned a cache miss. Contact support hit an anti-automation page. Those access limits are not an exemption. No 2027-01-27 date is recorded. The public page names carriers, SoC vendors, and OEMs with pre-installed or bundled software. It is not a general exemption for third-party apps, and it does not replace Managed Google Play private-app rules, Android developer verification, or target API requirements. Evidence level: Operational.

**Reviewed October 22, 2026.** The public Help article is short. This topic covers its entire public policy statement and records the linked Partner Center destination and its access limit; it does not reconstruct partner-only rules.

## Scope of the public statement

Google describes System services as **pre-installed software that supports core system functionality**. The public page names carriers, System-on-a-Chip (SoC) vendors, and original equipment manufacturers (OEMs) as potential applicants. If these parties have pre-installed or bundled apps, they can sign in to Partner Center, review the eligibility details, and determine whether their software qualifies as System services and may apply for an exemption.

| Confirmed by the public page | Do not infer |
| --- | --- |
| The category concerns pre-installed software that supports core system functionality. | A pre-install, OEM/carrier affiliation, or high install count automatically makes an app a system service. |
| Carriers, SoC vendors, and OEMs are named as parties who can check eligibility in Partner Center. | Ordinary third-party developers can use the same exemption path, or every bundled app will qualify. |
| The page says to check Partner Center for details and apply for an exemption. | Which exact Play rule is exempted, package/version scope, required evidence, renewal process, or approval period; the public body does not specify these details. |

**Operational boundary:** Treat this as a dedicated qualification path for eligible platform partners whose details must be checked in Partner Center, not as a general app-store exemption. The public page provides no eligibility checklist and does not describe the effects of approval on the Developer Program Policy, target API, Data safety, payments, or other policies. “Apply for an exemption” does not establish a blanket waiver of other rules.

## Keep related paths separate

| Path | What it covers | Difference from System services |
| --- | --- | --- |
| System services | Eligible carriers, SoC vendors, and OEMs check whether pre-installed/bundled software supporting core system functionality qualifies and may apply for a specific exemption. | Eligibility details are in Partner Center; the public Help article does not publish the criteria. |
| [Managed Google Play private apps](../play-console-requirements/play-console-requirements.en-US.md) | Publishing/distribution to specified organizations only. | Organization visibility or an EMM publishing method does not establish System services eligibility. |
| [Android developer verification](../android-developer-verification/android-developer-verification.en-US.md) | Developer identity and package-name verification. | Its managed-device/private-app scope and the target API exception for permanently private apps must be analyzed separately; neither replaces Partner Center's System services review. |
| [Target API requirements](../target-api/target-api-level.en-US.md) | Play target API submission/discoverability thresholds and exceptions. | Any exception must be confirmed through official eligibility/account state; it cannot be inferred from the System services definition. |

## Direct body links and review status

| Target | Role on the body | Review status |
| --- | --- | --- |
| [Partner Center: System services guide](https://docs.partner.android.com/partners/guides/system-services) | The public Help page directs authorized parties to sign in and read eligibility details. | The fetch returned a cache miss and the destination requires partner access; its body and descendants could not be publicly reviewed, so no internal criteria are recorded. |
| [Policy education and app requirements index](https://support.google.com/googleplay/android-developer/topic/12798386?hl=en) | A 32-item Help Center sidebar/navigation list. | All entries are registered in the recursive link graph (snapshot: `../google-play-policy-link-graph-en.md`, not imported in this repository); this is shared navigation, not 32 eligibility requirements stated in the System services article. |
| [Help Community](https://support.google.com/googleplay/android-developer/community?help_center_link=CJHQ4QUSD1N5c3RlbSBzZXJ2aWNlcw&hl=en) | Community discussion route. | Click returned a cache miss; community posts are not official eligibility criteria. |
| [Contact Play support](https://support.google.com/googleplay/android-developer/gethelp) | Support/account route. | Redirected to an anti-automation page; confirm the current contact path through an authorized Play Console or Partner Center account. |

## Eligibility review checklist

- [ ] Confirm the applicant is a carrier, SoC vendor, or OEM named by the public page and can access the relevant Partner Center.
- [ ] Check in Partner Center whether the software is pre-installed/bundled and supports core system functionality; the public Help page does not provide a substitute automated rule.
- [ ] Use the current Partner Center instructions to verify which policy clause, package names, versions, evidence, term, renewal, and appeal process the exemption covers.
- [ ] Preserve the official eligibility/approval status and review each other Play requirement that still applies. This page is not an exemption approval.

## Sources and related topics

- [Google Play System services Help](https://support.google.com/googleplay/android-developer/answer/12085265?hl=en)
- [Partner Center System services guide](https://docs.partner.android.com/partners/guides/system-services) (partner access)
- [Play Console Requirements](../play-console-requirements/play-console-requirements.en-US.md) · [Android developer verification](../android-developer-verification/android-developer-verification.en-US.md) · [Target API requirements](../target-api/target-api-level.en-US.md)
