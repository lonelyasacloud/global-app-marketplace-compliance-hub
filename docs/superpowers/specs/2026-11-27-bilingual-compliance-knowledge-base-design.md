# Bilingual Compliance Knowledge Base Design

## Intent

Turn `global-app-marketplace-compliance-hub` into a maintainable bilingual knowledge base for product, engineering, legal, and operations teams shipping mobile apps globally.

The repository remains the single source of truth. GitHub is the collaboration and review layer; a generated documentation site is the reading and search layer. The first site slice builds the repository's existing language-suffixed Markdown directly; automatic locale routing is deferred until link normalization is complete.

## Goals

- Make Apple App Store and Google Play requirements discoverable by platform, topic, region, and workflow.
- Keep Simplified Chinese and English pages paired, linked, and validated.
- Distinguish official/normative requirements from operational guidance, implementation notes, and editorial indexes.
- Show review dates, effective dates, authority level, source URLs, coverage boundaries, and future-dated changes.
- Provide a practical path from policy discovery to pre-submission action.
- Enable predictable updates through pull requests and automated validation.

## Non-goals

- Do not copy the source project `mjmirza/app-store-compliance` or reproduce its text.
- Do not treat summaries as legal advice or as a substitute for checking current official policies.
- Do not introduce a database or CMS as a second source of truth in the first release.
- Do not promise that a checklist guarantees platform approval.

## Product shape

### Public reading experience

The future docs site should have:

1. A bilingual landing page with search and four entry paths:
   - Apple App Store
   - Google Play
   - Regional requirements
   - Operational workflows

2. A global header with:
   - language switcher: 简体中文 / English
   - platform filter
   - topic search
   - link back to GitHub source

3. Topic pages with a consistent evidence panel:
   - platform
   - language
   - authority
   - status
   - knowledge-base review date
   - effective date, when known
   - official source links
   - coverage boundary
   - related checklist or workflow

4. Workflow pages:
   - pre-submission quick check
   - privacy/data safety preparation
   - rejection and appeal handling
   - deadline and future-change tracking

### Repository information architecture

- `docs/apple-app-store/`: Apple topics and platform map
- `docs/google-play/`: Google Play topics and platform map
- `docs/shared/`: cross-platform privacy, data protection, and common concepts
- `docs/regions/`: jurisdiction-specific requirements
- `docs/operations/`: checklists, deadlines, appeals, and release workflows
- `docs/governance/`: editorial and source policy
- `data/sources/`: source registry and dated snapshot inventories
- `scripts/`: structural, metadata, link, and bilingual-pair validation

## Content model

Every localized topic page uses front matter with at least:

- `id`
- `platform`
- `language`
- `authority`
- `status`
- `kb_checked_at`
- `review_due`
- `regions`
- `topics`
- `source_url`

The English page is the source-language reference when the official source is English. The Chinese page is a faithful translation or localized summary and must preserve uncertainty, dates, scope, and coverage boundaries.

Allowed authority values:

- `normative`: official policy or contractual requirement
- `operational`: platform workflow or release operation
- `implementation`: technical guidance that supports compliance
- `editorial`: map, index, catalog, or navigation aid

Allowed status values:

- `current`
- `future-dated`
- `historical`
- `partial`
- `superseded`

## Demo information architecture

### Landing page

```text
Global App Marketplace Compliance Hub
全球应用市场合规知识库

Search policies, topics, regions, and release tasks
搜索政策、主题、地区和发布任务

[Apple App Store] [Google Play] [Regional] [Operations]

Quick actions:
[Pre-submission check] [Privacy baseline] [Data Safety]
[Review & appeals] [Deadlines]

Recently reviewed:
- Apple: Review readiness
- Google Play: Data Safety baseline
- Shared: Privacy baseline

Evidence rule:
Official source first · Review date visible · Future changes separated
```

### Topic page

```text
Google Play · Data Safety
Google Play · 数据安全

Authority: Normative
Status: Current
Reviewed: 2026-10-24
Languages: 简体中文 | English

What this covers
Key requirements
Release evidence to prepare
Common failure modes
Related topics
Official sources
Coverage boundary
```

### Search/filter behavior

The first release only needs static-site search and metadata filters:

- platform: Apple / Google Play / Shared
- language: zh-CN / en-US
- authority: normative / operational / implementation / editorial
- status: current / future-dated / historical
- topic and region tags

## Delivery phases

### Phase 0 — Foundation and content contract

- Freeze front-matter vocabulary and page naming rules.
- Add bilingual-pair, source-link, metadata, and stale-review checks.
- Add a source registry convention and snapshot inventory.
- Define contribution and review expectations.

Exit criteria: every localized page is paired, has required metadata, and exposes at least one official source URL.

### Phase 1 — Navigation and Demo

- Add a top-level knowledge-base map.
- Add platform maps for Apple and Google Play.
- Add shared, regional, and operations landing pages.
- Add a static Demo home page and one representative topic page per platform.
- Add “related topics” and “next action” links to core pages.

Exit criteria: a new reader can reach a platform topic or release checklist in three clicks from the repository README or docs home.

### Phase 2 — Documentation site

- Use the existing Markdown tree as the source.
- Generate a static site with bilingual navigation, search, metadata display, and platform/topic filters.
- Keep the current explicit `.zh-CN.md` / `.en-US.md` links in the first site slice; enable automatic locale routing only after links are normalized to language-neutral targets.
- Publish from `main` through GitHub Actions.
- Keep generated output separate from authored content.

Exit criteria: site build succeeds in CI, every page has a stable URL, search finds both language variants, and links resolve.

### Phase 3 — Operating model

- Add monthly or policy-event review cadence.
- Track future-dated policies in the deadlines register.
- Add issue templates for new topic, source refresh, translation review, and broken link.
- Add coverage reports for missing regions and high-risk topics.

Exit criteria: a contributor can update a policy, record evidence, request translation review, and see automated validation results without undocumented steps.

## Quality gates

- No localized page without its language pair.
- No normative page without an official source URL.
- No future date represented as an already-effective requirement.
- No page that hides a failed source fetch or partial coverage.
- No copied third-party content; summaries must be original and attributed to official sources.
- Links, front matter, and page pairs pass the repository validator on every pull request.

## Recommended next implementation slice

Implement Phase 1 first. It has the highest user value with the lowest operational risk and does not require choosing a docs-site framework prematurely. After the navigation and Demo pages feel right, keep the first MkDocs Material build green with explicit bilingual links. Then normalize language-suffixed internal links and evaluate automatic locale routing before adding a language plugin.
