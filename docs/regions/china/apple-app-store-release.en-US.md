---
id: regions.cn.apple-app-store-release
platform: apple
language: en-US
authority: operational
status: partial
kb_checked_at: 2026-11-27
review_due: 2027-02-27
regions: [CN]
topics: [china-mainland, icp-filing, distribution, app-store-connect]
source_url: https://developer.apple.com/help/app-store-connect/reference/app-information/app-and-compliance-information/
snapshot_id: apple.china-mainland.icp-community-record.2026-11-27
coverage_status: official requirement plus community-recorded exception workflow
---

# Apple China Mainland Distribution: ICP Filing and a No-Filing Support Request

> Scope: the China mainland storefront on the Apple App Store. This page separates Apple’s published requirements from a community-recorded experience. The community path is not an Apple-published exemption policy and is not a release guarantee.

## Executive summary

- Start by determining whether the app must provide an ICP Filing Number and any other China mainland permits or supporting documents under Apple’s published requirements.
- If the app has no self-operated network service and uses Apple IAP only for payment, contacting Apple for case-specific handling can be tracked as a community-recorded support path. It does not replace a formal ICP filing and does not guarantee approval.
- If the app has its own servers, accounts, third-party analytics, advertising, or other network capabilities, assess formal filing and applicable permits. Do not treat a single case record as a general shortcut.

## 1. Apple’s published requirements (normative source)

Apple’s China mainland compliance description says that Chinese law requires additional documentation for some apps, and that MIIT requires some apps to have a valid Internet Content Provider (ICP) Filing Number. The submitted ICP number and App Store Connect app metadata should match the information filed with MIIT. The match is checked against the Simplified Chinese localization, or the primary language if Simplified Chinese is not configured.

Apple’s availability-status page defines:

- `ICP Filing Number Missing`: the app is not available in China mainland because a valid ICP Filing Number was not provided.
- `ICP Filing Number Invalid`: the ICP number or submitted metadata does not match the MIIT filing information, so the app is not available in China mainland.
- Games, books or magazine content, religious content, news content, AI-generated or synthetic content, and features requiring a security assessment may trigger additional approval numbers, permits, filings, or assessment evidence.

Apple’s November 16, 2026 App Store Connect release note says that regulations and permits, including ICP, game licenses, and medical device declarations, moved from **App Information** to the new **App Compliance** page. Because help-page wording and console navigation may be in transition, follow the current App Store Connect interface at release time and retain page evidence.

## 2. Contacting Apple without an ICP filing: community record, not an official workflow

The following is based on the user-provided community article, “China mainland App Store listing without ICP” (November 26, 2026, Asia/Shanghai). It describes one case. Apple’s official help pages do not publish a general “no-ICP exemption” workflow.

### Case conditions described by the article

The reported case involved an app with no self-operated online functionality that called Apple IAP only at payment time, and sought distribution on the China mainland App Store. Apple Support must decide whether any similar request is acceptable for a particular app.

### Steps recorded by the article

1. In App Store Connect, use the footer link “Contact Us.”
2. Select “View Topics,” then choose “Distribution.”
3. Explain in the contact form that the app has no self-operated network functionality, calls IAP only for payment, and is intended for China mainland distribution.
4. If Apple requests a declaration by email, prepare materials for that standalone app. The article records fields including the Team ID, the account holder’s legal name, App ID, the account holder’s signature and printed legal name, and confirmation that the request concerns this standalone app, that applicable regulations are understood, and that false statements may create legal responsibility.
5. If Apple sends a secure upload link from `AppleSupport@email.apple.com`, use that link to upload the requested materials and reply to the original email so the case can continue.
6. The author reports that the case result often arrived in about two days. This is not an Apple-published SLA and does not predict another app’s outcome.

### Boundaries that must remain visible

- This is not an exemption policy published in Apple Help.
- Do not rewrite the record as “any app without ICP can list” or “emailing Apple always works.”
- It does not replace game approval numbers, publishing permits, news permits, Internet Religious Information Permits, AI filings, or security-assessment evidence.
- Do not put personal identity documents, signatures, Apple support correspondence, or secure upload links into public issues, logs, or this knowledge base.

## 3. Release evidence and decision record

For the China mainland storefront, record at least:

- whether the app has self-operated servers, accounts, third-party analytics, advertising, push services, or other network capabilities;
- the scope of IAP and whether any network request occurs outside payment;
- the current App Store Connect compliance fields and China mainland availability status;
- the ICP filing number, metadata match conclusion, and supporting official documents, when applicable;
- if Apple is contacted, the case ID, contact date, Apple’s response, and final availability status;
- any applicable game, publishing, news, religious, AI, or security-assessment evidence.

## Source classification

| Source | Type | Use in this knowledge base |
| --- | --- | --- |
| [App and compliance information](https://developer.apple.com/help/app-store-connect/reference/app-information/app-and-compliance-information/) | Apple official normative/operational source | Identify China mainland ICP, permit, and compliance-document requirements |
| [App and submission statuses](https://developer.apple.com/help/app-store-connect/reference/app-information/app-and-submission-statuses/) | Apple official status reference | Explain `ICP Filing Number Missing` and `ICP Filing Number Invalid` |
| [App Store Connect release notes](https://developer.apple.com/help/app-store-connect/release-notes/) | Apple official change log | Record the November 16, 2026 move to App Compliance |
| [China mainland App Store listing without ICP](https://mp.weixin.qq.com/s/TYQ5fMpQNHeFp1YeaqoNxw) | Community record supplied by the user; not official | Discover one case-specific support path; not policy authority |

## Coverage boundary

This page is not legal advice, a filing service, or an Apple approval promise. Formal filing, permits, and security assessments should be confirmed by the project’s legal, privacy, or compliance owner against the app’s actual functionality and China mainland requirements.
