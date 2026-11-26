# Global App Marketplace Compliance Hub

A bilingual, source-backed knowledge hub for Apple App Store and Google Play compliance.

本项目面向产品、研发、测试、法务、隐私和发布团队，整理 Apple App Store 与 Google Play 的平台规则、地区要求、提交流程、隐私与数据安全、上架检查、拒审整改和政策变更。

> This repository provides operational summaries and source navigation. It does not replace the current Apple, Google, regulator, or legal source, and it does not guarantee approval.

## Start here

| 你的场景 / Your situation | 从这里开始 / Start here |
| --- | --- |
| 第一次了解项目 / New to the hub | [知识库导航 / Knowledge-base map](docs/README.md) |
| 准备提交 App / Preparing a submission | [提交前快速检查 / Pre-submission quick check](docs/operations/pre-submission/quick-check.zh-CN.md) |
| 需要 Apple 规则 / Apple requirements | [Apple App Store](docs/apple-app-store/README.md) |
| 需要 Google Play 规则 / Google Play requirements | [Google Play](docs/google-play/README.md) |
| 需要共性隐私与数据规则 / Shared privacy topics | [Shared controls](docs/shared/README.md) |
| App 被拒审 / App was rejected | [拒审与申诉 / Rejection and appeals](docs/operations/rejection-and-appeals/README.md) |
| 查看来源与维护约定 / Sources and maintenance | [来源与编辑政策 / Source and editorial policy](docs/governance/source-and-editorial-policy.md) |

## Repository map

- `docs/shared/`: rules and controls that commonly apply across both platforms.
- `docs/apple-app-store/`: Apple App Review, App Store Connect, privacy manifest, payments, and review materials.
- `docs/google-play/`: Google Play policies, Data Safety, permissions, Play Console, billing, content, child safety, and enforcement.
- `docs/regions/`: jurisdiction-specific requirements and regional launch notes.
- `docs/operations/`: pre-submission checks, rejection response, appeals, and deadlines.
- `data/sources/`: source registry and evidence metadata.
- `scripts/`: lightweight knowledge-base validation tools.

## Bilingual policy

A topic should have one stable ID and two language files:

```text
topic.zh-CN.md
topic.en-US.md
```

The Chinese and English versions may differ when the platform publishes different language versions or update dates. Such differences must be disclosed in the document metadata and maintenance notes.

## Evidence levels

- `Normative`: current official platform rule or agreement.
- `Operational`: official help, submission, or console workflow.
- `Regulatory`: official law, regulator, or government source.
- `Implementation note`: practical advice derived from a source.
- `Community evidence`: useful for test cases, not for overriding official rules.
- `Historical`: superseded or archived material kept for change history.

## Current baseline

The first content import is based on the supplied Apple Store Compliance KB snapshot dated 2026-11-10 and Google Play Knowledge Base snapshot dated 2026-10-24. Google batch 1 adds six topics from that Google snapshot: the Developer Distribution Agreement, the consolidated Developer Program Policy, User Data, the detailed Data Safety form, payments and subscriptions, and the Play release workflow. Google batch 2 adds seven further topics from the same snapshot: sensitive permissions, the permissions declaration workflow, background location, SMS and Call Log, photo and video permissions, account deletion, and target API level requirements. Google batch 3 adds nine further topics from the same snapshot: user-generated content, inappropriate content, content ratings, deceptive behavior, age restrictions and child safety, the Families Self-Certified Ads SDK program, child-safety DSA transparency, the child-safety regional reporting directory, and enforcement and appeals. Check dates on those pages are the review dates recorded in the snapshot. Always re-check the live official source before making a release decision.

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) before adding or updating content.
