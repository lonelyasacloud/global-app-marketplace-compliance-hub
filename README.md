# Global App Marketplace Compliance Hub

[![Validate knowledge base](https://github.com/lonelyasacloud/global-app-marketplace-compliance-hub/actions/workflows/validate-docs.yml/badge.svg)](https://github.com/lonelyasacloud/global-app-marketplace-compliance-hub/actions/workflows/validate-docs.yml)
[![Build documentation site](https://github.com/lonelyasacloud/global-app-marketplace-compliance-hub/actions/workflows/docs-site.yml/badge.svg)](https://github.com/lonelyasacloud/global-app-marketplace-compliance-hub/actions/workflows/docs-site.yml)

A bilingual, source-backed knowledge base for global mobile app marketplace compliance across Apple App Store and Google Play.

面向产品、研发、测试、法务、隐私和发布团队，集中整理 Apple App Store 与 Google Play 的平台政策、地区要求、隐私与数据安全、提交流程、发布检查、拒审整改和政策变更。

> This repository provides original operational summaries and source navigation. It does not replace current Apple, Google, regulatory, or legal sources, and it does not guarantee approval.
>
> 本仓库提供原创运营摘要与来源导航，不替代 Apple、Google、监管机构或法律来源，也不保证上架通过。

## What this project is

- A bilingual knowledge base: Simplified Chinese and English pages are maintained as pairs.
- A source-backed reference: important conclusions link back to official platform or regulatory sources.
- An operational playbook: policies are connected to release evidence, checklists, deadlines, and appeal workflows.
- A docs-as-code project: changes are reviewed through GitHub and checked by automated validation.

## What this project is not

- Not a copy of another repository, policy site, or third-party codebase.
- Not legal advice or a substitute for jurisdiction-specific counsel.
- Not a guarantee that an app will pass App Review or Google Play review.
- Not a promise that a snapshot remains current after its stated review date.

## Start here

| Your situation / 你的场景 | Recommended entry / 推荐入口 |
| --- | --- |
| New to the hub / 第一次了解项目 | [Bilingual knowledge-base map / 双语知识库导航](docs/navigation/knowledge-base-map.zh-CN.md) |
| Preview the experience / 查看 Demo | [Bilingual Demo home / 双语 Demo 首页](docs/demo/home.zh-CN.md) |
| Preparing a submission / 准备提交 App | [Pre-submission quick check / 提交前快速检查](docs/operations/pre-submission/quick-check.zh-CN.md) |
| Apple requirements / Apple 规则 | [Apple App Store platform map](docs/apple-app-store/README.md) |
| Google Play requirements / Google Play 规则 | [Google Play platform map](docs/google-play/README.md) |
| Shared privacy controls / 共性隐私规则 | [Shared controls](docs/shared/README.md) |
| App rejected or restricted / App 被拒审或限制 | [Rejection and appeals / 拒审与申诉](docs/operations/rejection-and-appeals/README.md) |
| Sources and maintenance / 来源与维护 | [Source and editorial policy / 来源与编辑政策](docs/governance/source-and-editorial-policy.md) |

## Repository map

- [docs/navigation/](docs/navigation/): canonical bilingual maps and reader entry points.
- [docs/apple-app-store/](docs/apple-app-store/): App Review, age ratings, submission, review workflow, developer program, news indexes, and evidence notes.
- [docs/google-play/](docs/google-play/): Developer Policies, Data Safety, permissions, billing, Play Console, publishing, enforcement, announcements, and platform topics.
- [docs/shared/](docs/shared/): cross-platform privacy and data-protection controls.
- [docs/regions/](docs/regions/): jurisdiction maps and regional launch notes.
- [docs/operations/](docs/operations/): pre-submission checks, deadlines, rejection response, and appeals.
- [docs/governance/](docs/governance/): source, editorial, and release-readiness rules.
- [data/sources/](data/sources/): dated snapshot inventories and source registry.
- [scripts/](scripts/): lightweight structural and bilingual metadata validation.
- [mkdocs.yml](mkdocs.yml): documentation-site configuration.

## Coverage at a glance

The current repository contains 101 paired English/Chinese topic pages.

The imported baseline is based on:

- Apple Store Compliance KB snapshot reviewed on 2026-11-10.
- Google Play Knowledge Base snapshot reviewed on 2026-10-24.

The snapshots are evidence inventories, not live-policy guarantees. Before a release decision, recheck the current official source and the page's review date.

Known coverage boundaries include:

- Apple Privacy Manifest, Required Reason API, App Privacy Details, ATT, In-App Purchase, subscriptions, external purchase, and regional terms are not yet complete standalone topic pages.
- Regional requirements are currently organized as a map and launch-note layer; jurisdiction-specific topic coverage is still expanding.
- Some imported pages are editorial indexes, historical records, community evidence, or implementation notes rather than normative platform rules.
- Future-dated Google Play changes are kept separate from current requirements.

## Page and metadata model

A localized topic uses a stable ID and a language-paired filename:

```text
topic.zh-CN.md
topic.en-US.md
```

Localized pages carry metadata for platform, language, authority, status, review date, next review date, regions, and topics. Each localized page must expose an official or clearly identified evidence link. Paired pages must agree on stable ID, platform, authority, and status.

Authority labels distinguish:

- `normative`: current official platform rule or agreement.
- `operational`: official help, submission, console, or workflow guidance.
- `regulatory`: law, regulator, or government source.
- `implementation-note`: practical technical advice derived from sources.
- `community`: practitioner or community evidence used for test discovery.
- `historical`: archived or superseded material.
- `editorial`: maps, indexes, catalogs, and navigation aids.

## Quality gates

Every change should pass:

```bash
python scripts/validate_kb.py
mkdocs build --strict
```

The repository also provides issue forms for [new topics](.github/ISSUE_TEMPLATE/new-topic.yml), [source refreshes](.github/ISSUE_TEMPLATE/source-refresh.yml), and [translation reviews](.github/ISSUE_TEMPLATE/translation-review.yml).

## Documentation site

The site is built with MkDocs Material and checked on pull requests and pushes to `main`. GitHub Pages deployment is currently a manual workflow after the repository's Pages source is enabled.

The first site slice keeps the existing explicit `.zh-CN.md` and `.en-US.md` links. Automatic language routing will be considered after the internal link convention is normalized.

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md) before adding or updating content. For the complete release gate, see [Knowledge Base Release Readiness](docs/governance/release-readiness.md).

## Official starting points

- [Apple App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/)
- [Apple Developer Program](https://developer.apple.com/programs/)
- [Google Play Developer Policy Center](https://play.google.com/about/developer-content-policy/)
- [Google Play User Data policy](https://support.google.com/googleplay/android-developer/answer/10144311)
