---
id: shared.privacy-data-protection.baseline
platform: shared
language: en-US
authority: normative
status: current
kb_checked_at: 2026-11-26
review_due: 2027-02-26
regions: [global]
topics: [privacy, sdk, consent, deletion]
---

# Privacy and Data Protection Baseline

## Scope

This is a cross-platform control baseline. Apple App Store, Google Play, and local law may impose different fields, declarations, exemptions, and deadlines; verify them separately.

## Core conclusion

Privacy disclosures must describe the app's actual runtime collection, use, sharing, retention, and deletion behavior, including the backend, analytics, advertising, authentication, payment, and third-party SDK supply chain.

## Required controls

- Maintain a data-flow inventory covering the app, backend, SDKs, third parties, and cross-border transfers.
- For every data type, record purpose, legal basis, collection timing, necessity, recipients, retention, and deletion method.
- Keep the privacy policy reachable in-app and consistent with store declarations.
- Obtain valid consent before tracking, sensitive-data processing, or third-party transfer when required.
- Test denial, withdrawal, account deletion, and post-deletion behavior.
- Recheck the final build for SDKs, permissions, Privacy Manifest, Data Safety, and store privacy fields before release.

## Platform differences

- Apple: review App Privacy Details, Privacy Manifest, Required Reason APIs, ATT, account deletion, and App Review Information.
- Google Play: review Data Safety, User Data policy, sensitive-permission declarations, prominent disclosure and consent, account deletion, and SDK behavior.
- Regional law may add requirements for children, health, location, cross-border transfer, automated decisions, retention, and data-subject requests.

## Evidence and testing

Retain the data-flow diagram, SDK inventory, permission matrix, consent and withdrawal tests, deletion tests, privacy-policy version, store-form evidence, and final-build verification record.

## Sources

- [Apple App Privacy Details](https://developer.apple.com/app-store/app-privacy-details/)
- [Apple Privacy Manifest](https://developer.apple.com/documentation/bundleresources/adding-a-privacy-manifest-to-your-app-or-third-party-sdk)
- [Google Play User Data policy](https://support.google.com/googleplay/android-developer/answer/10144311)
- [Google Play Data safety](https://support.google.com/googleplay/android-developer/answer/10787469)

This page is an operational summary, not a privacy policy or legal advice.
