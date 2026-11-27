# Source and Editorial Policy / 来源与编辑政策

## Evidence levels

| Level | Meaning | How it is used |
| --- | --- | --- |
| Normative | Current Apple/Google rule, agreement, or official policy | May support a compliance conclusion |
| Operational | Official help, console, submission, or workflow guidance | Supports execution steps |
| Regulatory | Official law, regulator, or government source | Supports jurisdiction-specific obligations |
| Implementation note | Practical advice derived from one or more sources | Must be labelled as advice |
| Community evidence | Forum, Reddit, vendor, or practitioner report | Used to discover test cases only |
| Historical | Superseded, archived, or older translation | Used for change history only |

## Source record

Every high-risk conclusion should record:

- source URL
- publisher and page title
- source language
- page or document update date
- knowledge-base review date
- status: current, future-dated, historical, partial, or superseded
- affected platform and region
- reviewer notes and unresolved questions

## Metadata and review cadence

Localized pages use the same stable ID and should agree on platform, authority, and status. The validator also requires review-tracking metadata: `kb_checked_at`, `review_due`, `regions`, and `topics`. Existing pages may use the repository's legacy authority labels such as `regulatory`, `historical`, `implementation-note`, and `community`; new pages should prefer the shorter canonical labels where they fit.

A source URL may be stored in front matter when useful, but the enforceable repository rule is that every localized page exposes at least one Markdown link to an official or clearly identified evidence source. Pages with partial coverage, unavailable sources, or language gaps must say so explicitly.

High-risk topics should be rechecked monthly and immediately after a platform announcement, enforcement change, or known effective-date transition. The owner of a pull request is responsible for recording the review date and unresolved questions.

## Conflicts

When sources differ, keep the obligations separate and describe the conflict. Do not silently merge Apple rules, Google rules, local law, and internal recommendations into one rule. If an operational recommendation is stricter than the platform rule, label it as an internal control recommendation.

## Translation

Chinese and English versions are paired but not assumed identical. If a localized official page lags behind the English version, record the gap and use an editorial translation only when clearly labelled.

## Public-repository safety

Do not publish credentials, customer data, internal app identifiers, private legal advice, unreleased enforcement details, or confidential vendor materials. Public content must be suitable for external readers and must link to the authoritative source.
