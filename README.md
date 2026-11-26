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
- `docs/apple-app-store/`: Apple App Review summaries, the license-agreement summary, age ratings, news indexes, and review materials. Privacy Manifest, Required Reason API, App Privacy Details, ATT, IAP, subscriptions, and external purchase are not topic pages yet.
- `docs/google-play/`: Google Play policies, Data Safety, permissions, Play Console, billing, and the other topics imported from the 2026-10-24 snapshot. The [platform map](docs/google-play/README.md) is the index.
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

The imported pages come from the supplied Apple Store Compliance KB snapshot dated 2026-11-10 and the Google Play Knowledge Base snapshot dated 2026-10-24. Check dates on those pages are the review dates recorded in the snapshots. This import did not re-open the live official pages. Always re-check the live official source before making a release decision.

Apple pages from that snapshot: the guidelines summary, pre-submission checklist, review workflow, age ratings, and the license-agreement summary, plus the rule-decomposition model, the embedded-link catalog, the news index, the news target-page index, and community evidence. The second group is an editorial model or an operational or historical index, not additional Apple rules. In that snapshot the English App Review Guidelines page is dated October 16, 2026, and the Simplified Chinese guidelines page shows June 8, 2026. The news RSS boundary was not verified. Privacy Manifest, Required Reason API, App Privacy Details, ATT, IAP, subscriptions, external purchase, and regional-terms topics are not in this snapshot package and are not topic pages.

Google batches 1–9 cover the topic pages in that Google snapshot. The [Google Play map](docs/google-play/README.md) and the [snapshot inventory](data/sources/google-play-kb-snapshot-2026-10-24.md) list them. Play Policy Insights is an official Android/Play developer tool, not Play policy text. The announcement catalog does not reproduce the snapshot's per-target child-page tables. Current Play rules stay distinct from future-dated previews, including 2027-01-27 items. Offline wiki HTML, recursive link graphs, and URL-audit CSVs are not in this repository.

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) before adding or updating content.
