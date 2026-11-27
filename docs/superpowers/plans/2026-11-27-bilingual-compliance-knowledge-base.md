# Bilingual Compliance Knowledge Base Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Turn the existing bilingual Markdown repository into a discoverable GitHub knowledge base and prepare a generated documentation site without creating a second content source.

**Architecture:** Keep `docs/` as authored Markdown and `data/sources/` as evidence inventory. Add stable bilingual navigation and a small content Demo first; then build a MkDocs Material site with static search, metadata visibility, language links, and GitHub Pages deployment. GitHub Actions remains the validation and publishing gate.

**Tech Stack:** Markdown with YAML front matter, Python validation script, MkDocs Material, GitHub Actions, GitHub Pages. Automatic locale routing is a follow-up after language-suffixed links are normalized.

**Spec:** `docs/superpowers/specs/2026-11-27-bilingual-compliance-knowledge-base-design.md`

## Global Constraints

- GitHub is the only authored content source; generated site output must not be committed as a parallel source.
- Every `.en-US.md` page must have a matching `.zh-CN.md` page with the same stem.
- Normative pages must expose an official source URL.
- Future-dated requirements must remain explicitly future-dated and must not be written as current requirements.
- English remains the source-language reference when the official source is English.
- Summaries must be original, attributed, bounded by coverage notes, and never presented as legal advice.
- All changes must pass `python scripts/validate_kb.py` before merge.

## Review Focus

- Missing or asymmetric language pairs: the validator must fail with the exact missing path.
- Metadata drift: invalid `authority`, `status`, or missing `source_url` must fail before publishing.
- Relative-link breakage after navigation changes: the site build must fail on broken internal links.
- Future policy dates: pages and the deadlines register must preserve effective-date semantics.
- Site/source divergence: generated output must be built from `docs/` and never edited manually.

---

### Task 1: Strengthen the content contract

**Files:**
- Modify: `scripts/validate_kb.py`
- Modify: `.github/workflows/validate-docs.yml`
- Create: `scripts/fixtures/README.md` only if the validator needs explicit fixture guidance

**Interfaces:**
- Consumes: all Markdown files below `docs/`
- Produces: non-zero exit status and actionable file-level messages for invalid metadata, missing pairs, missing official links, or malformed front matter

- [ ] **Step 1: Add validator checks for enumerated metadata.** Require `authority` in `{normative, operational, implementation, editorial}` and `status` in `{current, future-dated, historical, partial, superseded}`.
- [ ] **Step 2: Add date and source checks.** Require `kb_checked_at` and `source_url` for normative pages; allow editorial pages to document a source registry instead.
- [ ] **Step 3: Add a stale-review warning mode.** Keep current CI non-blocking for stale dates during the first release, but print the page and review date so future policy can promote it to an error.
- [ ] **Step 4: Run `python scripts/validate_kb.py`.** Expected: PASS on current `main`.
- [ ] **Step 5: Commit.** Use `ci: enforce bilingual knowledge-base metadata`.

### Task 2: Build stable repository navigation

**Files:**
- Modify: `README.md`
- Modify: `docs/README.md`
- Modify: `docs/apple-app-store/README.md`
- Modify: `docs/google-play/README.md`
- Modify: `docs/shared/README.md`
- Modify: `docs/regions/README.md`
- Modify: `docs/operations/deadlines/README.md`
- Modify: `docs/operations/rejection-and-appeals/README.md`
- Create: `docs/navigation/knowledge-base-map.en-US.md`
- Create: `docs/navigation/knowledge-base-map.zh-CN.md`

**Interfaces:**
- Consumes: existing topic filenames, source registry, snapshot inventories
- Produces: stable platform/topic/workflow/region entry points with paired language links

- [ ] **Step 1: Create the bilingual knowledge-base map.** Include four top-level paths: Apple App Store, Google Play, Shared, and Operations/Regions.
- [ ] **Step 2: Add “start here” links.** Link pre-submission, privacy baseline, Data Safety baseline, review readiness, rejection/appeals, and deadlines.
- [ ] **Step 3: Add navigation rules.** State that English and Chinese pages are paired and that official sources are the authority.
- [ ] **Step 4: Link the maps from both the root README and `docs/README.md`.**
- [ ] **Step 5: Run the validator and manually inspect every navigation target.**
- [ ] **Step 6: Commit.** Use `docs: add bilingual knowledge-base navigation maps`.

### Task 3: Add the content Demo

**Files:**
- Create: `docs/demo/home.en-US.md`
- Create: `docs/demo/home.zh-CN.md`
- Create: `docs/demo/topic-page.en-US.md`
- Create: `docs/demo/topic-page.zh-CN.md`
- Modify: `docs/README.md`

**Interfaces:**
- Consumes: the shared front-matter contract and representative Apple/Google topics
- Produces: a reviewable Markdown Demo that shows the future docs-site information architecture

- [ ] **Step 1: Create the bilingual Demo home.** Include the title, search promise, four entry paths, quick actions, recently reviewed links, evidence rule, and GitHub source link.
- [ ] **Step 2: Create the bilingual Demo topic page.** Use Google Play Data Safety as the example and show metadata, scope, key requirements, release evidence, common failure modes, related topics, official sources, and coverage boundary.
- [ ] **Step 3: Add a visible language switch and platform/topic links.**
- [ ] **Step 4: Link the Demo from `docs/README.md` as “Preview / Demo”.**
- [ ] **Step 5: Run the validator.** Expected: four Demo pages pass pairing, metadata, and source-link checks.
- [ ] **Step 6: Commit.** Use `docs: add bilingual knowledge-base navigation demo`.

### Task 4: Scaffold the documentation site

**Files:**
- Create: `mkdocs.yml`
- Create: `requirements-docs.txt`
- Create: `.github/workflows/docs-site.yml`
- Modify: `.gitignore` if generated output needs exclusion

**Interfaces:**
- Consumes: `docs/` Markdown pages and front matter
- Produces: a static site artifact with search, bilingual navigation, metadata display, and a GitHub Pages deployment

- [ ] **Step 1: Pin the initial site toolchain.** Use MkDocs Material to build the existing `.zh-CN.md` and `.en-US.md` pages directly; pin compatible major versions in `requirements-docs.txt`.
- [ ] **Step 2: Configure source and theme.** Set `docs_dir: docs`, enable search, navigation tabs, code-copy, metadata display, and a visible GitHub repository link.
- [ ] **Step 3: Preserve the current language-suffixed source links.** Keep explicit `.zh-CN.md` and `.en-US.md` links in the first site slice. Add automatic language routing only in a follow-up after link normalization.
- [ ] **Step 4: Add the build workflow.** On pull requests, run validation and `mkdocs build --strict`; on `main`, publish the built site through GitHub Pages.
- [ ] **Step 5: Run locally in a disposable environment or CI.** Expected: strict build passes and generated output is not added to the repository.
- [ ] **Step 6: Commit.** Use `build: scaffold bilingual documentation site`.

### Task 5: Add contribution and operating templates

**Files:**
- Create: `.github/ISSUE_TEMPLATE/new-topic.yml`
- Create: `.github/ISSUE_TEMPLATE/source-refresh.yml`
- Create: `.github/ISSUE_TEMPLATE/translation-review.yml`
- Modify: `CONTRIBUTING.md`
- Modify: `docs/governance/source-and-editorial-policy.md`

**Interfaces:**
- Consumes: content contract, source registry, and review cadence
- Produces: repeatable issue and pull-request inputs for topic additions, source refreshes, and bilingual review

- [ ] **Step 1: Add issue forms.** Capture platform, topic, source URL, source language, requested languages, authority, status, review date, and coverage boundary.
- [ ] **Step 2: Update contribution guidance.** Describe the page-pair rule, official-source rule, future-date rule, and validation command.
- [ ] **Step 3: Document review cadence.** Set monthly review for high-risk topics and event-driven review for platform announcements.
- [ ] **Step 4: Run the validator and inspect issue form YAML.**
- [ ] **Step 5: Commit.** Use `docs: add knowledge-base contribution workflow`.

### Task 6: Release verification

**Files:**
- Modify: `.github/workflows/validate-docs.yml`
- Modify: `.github/workflows/docs-site.yml` if needed
- Create: `docs/governance/release-readiness.md`

**Interfaces:**
- Consumes: validator output, strict site build, and source registry
- Produces: a documented release gate for knowledge-base updates

- [ ] **Step 1: Add the release-readiness checklist.** Include source freshness, metadata, bilingual parity, internal links, future-date handling, and coverage boundary.
- [ ] **Step 2: Run `python scripts/validate_kb.py`.** Expected: PASS.
- [ ] **Step 3: Run `mkdocs build --strict`.** Expected: PASS with no broken links or navigation warnings.
- [ ] **Step 4: Confirm the latest workflow run is successful on `main`.**
- [ ] **Step 5: Commit.** Use `ci: verify knowledge-base release gates`.

## Suggested execution order

Run Tasks 1–3 first as the GitHub-native Demo milestone. Review the Demo content and navigation before selecting final visual styling. Then run Task 4 as the first MkDocs Material site milestone. Treat automatic locale routing as a follow-up after the repository's language-suffixed links are normalized.

The first milestone is useful on GitHub by itself and can be reviewed without enabling GitHub Pages. The second milestone adds the polished reading experience after the information architecture has been validated by actual users.
