---
id: google-play.data-safety.baseline
platform: google-play
language: en-US
authority: normative
status: current
kb_checked_at: 2026-11-26
review_due: 2027-02-26
regions: [global]
topics: [data-safety, privacy, sdk, disclosure]
---

# Google Play Data Safety Baseline

## Core principle

The Data Safety form must reflect the app's actual runtime collection, sharing, use, and deletion behavior, including every third-party SDK. It cannot be completed from static code guesses or the privacy policy alone.

## Review scope

- App, backend, analytics, advertising, authentication, payments, support, and external services.
- SDK data types, transmission timing, purposes, recipients, and encryption.
- Account creation, account deletion, backups, caches, logs, crash analytics, and device identifiers.
- Children, health, location, contacts, photo/video, SMS/call-log, and accessibility features.
- Deletion requests, retention exceptions, consent withdrawal, and regional differences.

## Submission workflow

Build the data-flow and SDK inventories first, answer the collection and sharing questions, then reconcile the form with the app, backend, and privacy policy. Unknown SDK behavior belongs in the risk register; it should not be assumed to be “no.”

## Policy boundaries

The Data Safety declaration does not replace the User Data policy, sensitive-permission requirements, Families policy, account-deletion requirements, or local law. Android implementation guidance does not automatically establish Play eligibility.

## Official sources

- [User Data policy](https://support.google.com/googleplay/android-developer/answer/10144311)
- [Data safety section](https://support.google.com/googleplay/android-developer/answer/10787469)
- [Google Play Policy Center](https://play.google.com/about/developer-content-policy/)

This is an operational summary. Verify the current Play Console form and official pages before release.
