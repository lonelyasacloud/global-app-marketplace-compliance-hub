---
id: google-play.play-policy-insights-skill
platform: google-play
language: en-US
authority: implementation note
status: current
kb_checked_at: 2026-10-23
review_due: 2027-01-23
regions: [global]
topics: [play-policy-insights, developer-tool, static-analysis]
snapshot_id: android.play-policy-insights-skill
snapshot_package: "GooglePlay-KnowledgeBase-2026-10-24-review.zip"
coverage_status: "detailed-reference-summary"
source_url: "https://github.com/android/skills/tree/main/play/play-policy-insights"
effective_date: "official developer tool updated 2026-07-13; not Play policy text"
---

> **Import note (Google batch 9).** The body is the paraphrased tool summary from the already separated 2026-10-24 Google Play knowledge-base snapshot (`android.play-policy-insights-skill`, reviewed 2026-10-23). It is not a verbatim copy of the repository and it is not Play policy text. The English files in Google's android/skills repository are the source of truth for what the tool contained on the review date. `kb_checked_at` is the review date recorded in the snapshot source file; this import did not re-open the live repository. Phrases such as “this knowledge base,” “this library,” and “local topic” describe coverage inside that snapshot, not the set of pages imported into this repository. Relative snapshot links to topics, link graphs, ledgers, or CSVs that are not in this repository are kept as text mentions. Relative links that target Google batch 1–8 topics or these eight batch 9 topics point at the hub files. **This page describes an official Android/Play developer tool. The skill metadata names Google LLC as author and lists July 13, 2026 as its update date. GitHub `main` is mutable. The tool is not Google Play policy text, not a Play review result, and not a compliance certification.** The reviewed repository content is English. The snapshot does not record a Chinese official skill page. The Chinese hub text is an editorial paraphrase. The configuration links to the Contacts policy preview. That preview’s 2027-01-27 date lives on the contacts topic and is not a rule stated by this tool. Evidence level: Implementation note.

**Official Android/Play developer tool.** This page describes the Play Policy Insights skill in Google's [android/skills](https://github.com/android/skills/tree/main/play/play-policy-insights) repository. It is not Play policy text.

# Android Play Policy Insights Skill: Code-Review Aid, Resources, and Scope

## Purpose and review basis

This page summarizes the Play Policy Insights skill in Google's [android/skills repository](https://github.com/android/skills/tree/main/play/play-policy-insights). The directory contains a coding-agent workflow, not Google Play policy text. The skill metadata names Google LLC as author and lists July 13, 2026 as its update date; GitHub's main branch is mutable. On October 23, 2026, we opened the skill text, repository directory, and its resource/script child pages, and cross-checked the installed local copy at the module level.

The stated purpose is to compare static code clues with developer-provided or publicly readable Play information and produce an evidence-based pre-submission report. It covers three domains: Permissions and APIs Hygiene, User Account and Identity, and Data Safety and Privacy. It explicitly requires checking Data safety, demo login credentials for review, and restricted permissions. That scope is not a complete Developer Program Policy audit and does not represent a Google Play review result.

## Workflow and key constraints

1. **Initialize and triage:** The orchestrator's init flow scans relevant source/configuration files, summarizes modules, permissions, and data-source clues, then activates goals and writes prompts. Its temporary directory is created under the workspace root with a play_policy_insights prefix and unique identifier.
2. **Targeted analysis:** Activated goals cover permission/API use, data collection and transmission, prominent disclosure/consent, and account/identity or deletion concerns. Resource prompts direct the reviewer to use scanner-provided file/line evidence, avoid unbounded searches, cite direct evidence for severe findings, and lower the finding level when context is abstract or missing.
3. **Cross-review and report:** Findings are aggregated, a critic stage checks for false positives, exaggerated claims, or weak evidence, and a report script produces Markdown. The skill defines delegation and sequential modes according to the available environment. If initial orchestration fails, it says to stop rather than present a manual audit as a successful automated scan.
4. **File containment:** Intermediate files, logs, and final machine outputs must remain within the scratch directory. Missing required inputs trigger fail-fast behavior. The report template says output is informational/advisory only, not legal advice, a compliance guarantee, or approval to publish.

## Repository contents and direct child pages

At review time, the skill directory's direct listing showed SKILL.md, resources/, and scripts/. Those folders list eight resource files and five Python scripts. Each is recorded below. The code was reviewed by module purpose; this is not a line-by-line source-code security audit.

| Child page | Content and role |
| --- | --- |
| [SKILL.md](https://github.com/android/skills/blob/main/play/play-policy-insights/SKILL.md) | Defines the three-domain scope, path resolution, two-phase workflow, initialization/aggregation/review/report commands, fail-fast rules, and output containment. |
| [common_mandates.md](https://github.com/android/skills/blob/main/play/play-policy-insights/resources/common_mandates.md) | Requires absolute paths, targeted searches inside the app directory, and exclusions for build/cache/test folders; findings need direct evidence, ambiguity lowers severity, and empty results remain empty arrays. |
| [goal_data_safety.md](https://github.com/android/skills/blob/main/play/play-policy-insights/resources/goal_data_safety.md) | Reviews data sources, network transmission, SDKs, Data safety declarations, prominent disclosure, and consent cues. |
| [goal_user_account.md](https://github.com/android/skills/blob/main/play/play-policy-insights/resources/goal_user_account.md) | Infers account functionality from sign-in, account-management, and profile clues, then checks review credentials and account deletion. |
| [goal_permissions_and_apis.md](https://github.com/android/skills/blob/main/play/play-policy-insights/resources/goal_permissions_and_apis.md) | Checks permission/API signals for SMS/Call Log, media, location, contacts, audio, files, app visibility, accessibility, exact alarms, and foreground services. |
| [critic.md](https://github.com/android/skills/blob/main/play/play-policy-insights/resources/critic.md) | Rechecks findings and separates code-supported violations, ambiguous cases needing human review, and informational suggestions. |
| [compliance_report_template.md](https://github.com/android/skills/blob/main/play/play-policy-insights/resources/compliance_report_template.md) | Defines the report's status, evidence, manual-review items, and disclaimer; it says issues may be missed and developers retain responsibility. |
| [policies.json](https://github.com/android/skills/blob/main/play/play-policy-insights/resources/policies.json) | Provides structured module names, categories, policy links, and data-taxonomy terms for report context. Its 16 modules are mapped in the next section. |
| [scanner_config.json](https://github.com/android/skills/blob/main/play/play-policy-insights/resources/scanner_config.json) | Configures signal categories, file-name patterns, permission groups, ignored directories, and extensions; it is a static-detection configuration, not a complete policy catalog. |
| [orchestrator.py](https://github.com/android/skills/blob/main/play/play-policy-insights/scripts/orchestrator.py) | Parses app modules, Gradle/version catalogs, and manifests; organizes identity/permission/data-source clues; invokes the scanner and creates stage prompts and aggregate results. |
| [scanner.py](https://github.com/android/skills/blob/main/play/play-policy-insights/scripts/scanner.py) | Collects supported source/configuration files and uses bounded patterns to find data-source, transmission, permission, and disclosure clues. |
| [play_store_scraper.py](https://github.com/android/skills/blob/main/play/play-policy-insights/scripts/play_store_scraper.py) | Reads public Play Store detail and Data safety display pages. It constructs requests to play.google.com/store/apps/details and /store/apps/datasafety using a package name and English/US parameters. This reads public listing information, not private Console forms or account state. |
| [template_engine.py](https://github.com/android/skills/blob/main/play/play-policy-insights/scripts/template_engine.py) | Renders variables, conditionals, and loops in resource prompts. |
| [generate_report.py](https://github.com/android/skills/blob/main/play/play-policy-insights/scripts/generate_report.py) | Merges scanner, scraper, and critic JSON, formats severities and finding cards, and creates the final Markdown report. |

## Official policy and implementation sources in policies.json

The configuration contains **31 URL references and 18 normalized unique destinations** across 16 review modules. The pages below are linked in the Knowledge Base's per-URL audit. Android implementation documents provide technical context; they do not grant Play permission eligibility.

| Config module | Official pages it references | Knowledge Base entry |
| --- | --- | --- |
| Data safety section | [User Data: Data safety section](https://support.google.com/googleplay/android-developer/answer/10144311#safetysection), [Android declare data use](https://developer.android.com/privacy-and-security/declare-data-use), [Data safety form instructions](https://support.google.com/googleplay/android-developer/answer/10787469) | [User Data](../user-data/user-data.en-US.md), [Data safety](../data-safety/data-safety.en-US.md) |
| Login credentials | [Sign-in details for review](https://support.google.com/googleplay/android-developer/answer/15748846) | [App review preparation](../app-review-preparation/app-review-preparation.en-US.md) |
| SMS and Call Log | [Sensitive permissions: SMS/Call Log section](https://support.google.com/googleplay/android-developer/answer/16558241#sms-call-permissions), [SMS and Call Log permissions Help](https://support.google.com/googleplay/android-developer/answer/10208820) | [SMS and Call Log](../sms-call-log/sms-call-log.en-US.md), [Permission declaration](../permissions-declaration/permissions-declaration.en-US.md) |
| Package Visibility | [Sensitive permissions: package visibility section](https://support.google.com/googleplay/android-developer/answer/16558241#package-vis), [Package visibility](https://support.google.com/googleplay/android-developer/answer/10158779) | [Sensitive Permissions](../sensitive-permissions/sensitive-permissions.en-US.md) |
| All Files Access | [Sensitive permissions: all-files-access section](https://support.google.com/googleplay/android-developer/answer/16558241#all-files-access), [Manage all files Android guide](https://developer.android.com/training/data-storage/manage-all-files), [File access permission declaration](https://support.google.com/googleplay/android-developer/answer/10467955) | [Sensitive Permissions](../sensitive-permissions/sensitive-permissions.en-US.md), [Android privacy checklist](../android-privacy-checklist/android-privacy-checklist.en-US.md) |
| Photo and Video Permissions | [Sensitive permissions: photo/video section](https://support.google.com/googleplay/android-developer/answer/16558241#photo-and-video-permissions), [Minimum-scope alternatives](https://support.google.com/googleplay/android-developer/answer/16935362), [Android shared media storage](https://developer.android.com/training/data-storage/shared/media) | [Photo and Video Permissions](../photo-video-permissions/photo-video-permissions.en-US.md) |
| Location Permissions | [Sensitive permissions](https://support.google.com/googleplay/android-developer/answer/16558241), [Location permission declaration](https://support.google.com/googleplay/android-developer/answer/9799150) | [Contacts and location: minimum scope](../contacts-location-permissions/contacts-location-permissions.en-US.md), [Background location](../background-location/background-location.en-US.md) |
| Contacts Permissions | [Contacts policy preview](https://support.google.com/googleplay/android-developer/answer/16909972#contacts-permissions), [Minimum-scope alternatives](https://support.google.com/googleplay/android-developer/answer/16935362) | [Contacts and location: minimum scope](../contacts-location-permissions/contacts-location-permissions.en-US.md) |
| Audio Recording | [User Data](https://support.google.com/googleplay/android-developer/answer/10144311), [Sensitive permissions](https://support.google.com/googleplay/android-developer/answer/16558241) | [User Data](../user-data/user-data.en-US.md), [Sensitive Permissions](../sensitive-permissions/sensitive-permissions.en-US.md) |
| Files and Docs Access | [File access permission declaration](https://support.google.com/googleplay/android-developer/answer/10467955), [Sensitive permissions](https://support.google.com/googleplay/android-developer/answer/16558241) | [Sensitive Permissions](../sensitive-permissions/sensitive-permissions.en-US.md), [Android privacy checklist](../android-privacy-checklist/android-privacy-checklist.en-US.md) |
| Prominent Disclosure | [User Data](https://support.google.com/googleplay/android-developer/answer/10144311) | [User Data](../user-data/user-data.en-US.md) |
| Account Deletion | [User Data: account deletion section](https://support.google.com/googleplay/android-developer/answer/10144311#account_deletion), [Account deletion requirements](https://support.google.com/googleplay/android-developer/answer/13327111) | [Account deletion](../account-deletion/account-deletion.en-US.md) |
| Target API Level | [Target API policy](https://support.google.com/googleplay/android-developer/answer/16561298), [Target API requirements Help](https://support.google.com/googleplay/android-developer/answer/11926878) | [Target API requirements](../target-api/target-api-level.en-US.md) |
| Accessibility API | [Sensitive permissions: Accessibility API section](https://support.google.com/googleplay/android-developer/answer/16558241#accessibility) | [Sensitive Permissions](../sensitive-permissions/sensitive-permissions.en-US.md) |
| Exact Alarm | [Sensitive permissions: exact-alarm section](https://support.google.com/googleplay/android-developer/answer/16558241#exact_alarm) | [Sensitive Permissions](../sensitive-permissions/sensitive-permissions.en-US.md) |
| Foreground Services | [Foreground service declaration](https://support.google.com/googleplay/android-developer/answer/13392821), [Sensitive permissions: foreground service section](https://support.google.com/googleplay/android-developer/answer/16559646#foreground_service) | [Foreground services and geofencing](../foreground-services-and-geofencing/foreground-services-and-geofencing.en-US.md), [Permission declaration](../permissions-declaration/permissions-declaration.en-US.md) |

## Relationship to the July 15, 2026 announcement and limits

The announcement lists this skill as an optional engineering tool for developers. It turns some policy topics from the announcement into code-review signals, especially obvious mismatches among Manifest permissions, call sites, Data safety, and review login information. It cannot replace the policy text, Play Console declarations, runtime testing, account verification, or human judgment. A static hit does not by itself establish a violation; no hit does not prove compliance.

The configuration is finite: its 16 modules and URLs do not cover every Google Play policy, regional requirement, exception, or runtime path. The scanner is bounded by its supported extensions, patterns, inputs, and visibility into static code. The Android shared-media-storage page remains partial in this pass; the other 17 unique policy/implementation destinations have full-body access classifications in the URL ledger. Account-specific Console status for signing, login, or Data safety cannot be inferred from a public store listing.

This pass reviewed the skill and its public resources for the policy library; it did not run the workflow against an Android app.

## License pointer and open scope

The skill metadata names a LICENSE.txt file; the [relative LICENSE.txt path inside the skill directory](https://github.com/android/skills/blob/main/play/play-policy-insights/LICENSE.txt) returned 404; the repository-root [LICENSE.txt](https://github.com/android/skills/blob/main/LICENSE.txt) contains the Apache License 2.0 text. The root license includes conditions on redistribution, notices, marking modified files, and disclaimers. This entry records the license text supplied by the repository; verify its scope, any NOTICE file, and file-level headers before copying or redistributing a specific script or resource.

GitHub's main branch is mutable; the directory and page inventory here is the October 23, 2026 snapshot. Scripts were reviewed at module level, not through a line-by-line security audit. GitHub's generic navigation and unrelated skills elsewhere in the repository were not enumerated. This is engineering reference material and is not part of the policy-text catalog.
