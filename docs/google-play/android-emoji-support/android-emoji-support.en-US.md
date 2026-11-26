---
id: google-play.android-emoji-support
platform: google-play
language: en-US
authority: normative
status: current
kb_checked_at: 2026-10-22
review_due: 2027-01-22
regions: [global]
topics: [emoji, unicode, android, accessibility, compatibility]
snapshot_id: play.android-emoji
snapshot_package: "GooglePlay-KnowledgeBase-2026-10-24-review.zip"
coverage_status: "detailed-summary"
source_url: "https://support.google.com/googleplay/android-developer/answer/11190644?hl=en"
source_url_unicode_index: "https://www.unicode.org/emoji/techindex.html"
source_url_unicode_charts: "https://www.unicode.org/emoji/charts/"
source_url_unicode_standard: "https://www.unicode.org/reports/tr51/"
source_url_android_guide: "https://developer.android.com/develop/ui/views/text-and-emoji/emoji2"
source_url_zh: "https://support.google.com/googleplay/android-developer/answer/11190644?hl=zh-CN"
effective_date: "current Play emoji rule for Android 12+; derived four-month reminder around 2026-12-28 is not an account deadline and is not 2027-01-27"
---

# Google Play Android Emoji support policy

> **Import note (Google batch 8).** The body is the paraphrased summary from the already separated 2026-10-24 Google Play knowledge-base snapshot (`play.android-emoji`, reviewed 2026-10-22). It is not a verbatim copy of an official page. The English official source is the source of truth. `kb_checked_at` is the review date recorded in the snapshot source file; this import did not re-open the live official pages. Phrases such as “this knowledge base,” “this library,” and “local topic” describe coverage inside that snapshot, not the set of pages imported into this repository. Relative snapshot links to topics, link graphs, ledgers, or CSVs that are not in this repository are kept as text mentions. Relative links that target the Google batch 1–7 topics or these thirteen batch 8 topics point at the hub files. Reviewed 2026-10-22. The Chinese file records the policy URL as `hl=zh-CN`. The snapshot does not record a line-by-line check of that Chinese official page or a failed fetch of the route. The Chinese hub text is an editorial paraphrase. Unicode charts and UTS #51 were opened in English. The Play rule requires latest Unicode Emoji support on Android 12+, with a four-month window for custom implementations. UTS #51 dates Unicode Emoji 18.0 to 2026-08-28. A four-month window counted from that date falls around 2026-12-28. That date is a derived reminder, not an account-specific Play deadline and not 2027-01-27. The Emoji2 guide, last updated 2026-10-16, is an implementation note. Its examples stopping at Unicode 16.0 do not lower the Play requirement. Evidence level: Normative for the Play emoji policy; Implementation note for Android Emoji2; Unicode is the standards source for “latest Unicode Emoji.”

**Reviewed October 22, 2026.** Google Play's Android Emoji policy requires all apps running on Android 12 or later to support the latest Unicode Emoji. Apps using the default Android Emoji implementation without customization automatically support the latest version on Android 12+. Apps with custom Emoji implementations, including third-party libraries, must fully support a new Unicode Emoji release within four months.

## Play policy requirements

- **Android 12+:** Every app must support the latest Unicode Emoji. Apps using the platform default implementation generally meet this requirement; apps that replace or wrap Emoji fonts, rendering, or input must check compatibility.
- **Custom implementations:** The policy explicitly includes third-party libraries. Update after each new Unicode Emoji release and complete support within the four-month window. Older announcements, SDK examples, or device OS versions are not permanent exemptions.
- **Derived timing note:** UTS #51 dates Unicode Emoji 18.0 to August 28, 2026. If that date is the “new Unicode Emoji release” date used by the Play policy, the four-month window falls around **December 28, 2026**. This is a reminder inferred from the official date and policy wording, not an account-specific Play deadline.

## Android implementation and testing

Google's [Android Emoji2 guide](https://developer.android.com/develop/ui/views/text-and-emoji/emoji2) explains system Emoji fonts, EmojiCompat, and compatibility implementations. Android 11 (API 30) and earlier cannot receive new Emoji through a system font update; `androidx.emoji2` and AppCompat or Compose compatibility paths can provide updated glyph and sequence support on older systems. Custom text widgets should also be checked for EmojiCompat handling.

Before release, test on target Android versions and Android 11 or earlier with skin-tone modifiers, ZWJ sequences, regional flags, and recently added characters. Check for missing-glyph boxes (“tofu”), split glyphs, incorrect ordering, or input failures. Choose test cases from the current [Unicode Emoji charts](https://www.unicode.org/emoji/charts/) and [UTS #51](https://www.unicode.org/reports/tr51/); technical example lists do not necessarily track the latest Unicode release.

## Direct child links and relationships

| Source | Target | Summary / audit status |
| --- | --- | --- |
| Google Play Android Emoji Policy | [Unicode Emoji technical index](https://www.unicode.org/emoji/techindex.html) | Opened. It groups the Emoji charts, UTS #51, data files, proposals, and FAQs as standards resources. |
| Unicode Emoji technical index | [Unicode Emoji charts](https://www.unicode.org/emoji/charts/) | Opened; currently displays Emoji v18.0 and links to character/sequence, version, presentation, and ordering charts. The page is dynamic; use the corresponding current data files for production tests. |
| Unicode Emoji technical index | [UTS #51: Unicode Emoji](https://www.unicode.org/reports/tr51/) | Opened; v18.0, dated August 28, 2026. It defines Emoji characters and sequences, presentation, modifiers, and interoperability guidance. It is the standards source for interpreting “latest Unicode Emoji.” Its many tables and references are outside Play obligations and were not opened individually. |
| Google Play Android Emoji Policy | [Android: Support modern emoji](https://developer.android.com/develop/ui/views/text-and-emoji/emoji2) | Opened; covers Emoji2, AppCompat, Compose, older Android fallback, custom views, and testing. Last updated October 16, 2026. Its listed test examples stop at Unicode 16.0 while the Unicode standards page is at 18.0; use the latest Unicode charts/data for sample selection. |

## Release checklist

1. Identify whether the app uses custom Emoji fonts, renderers, keyboards, or third-party Emoji libraries on Android 12+.
2. Complete support within four months of every Unicode Emoji release and retain version and test records.
3. Test Unicode sequences on older Android versions, system fonts, input methods, custom views, and UGC surfaces.
4. Refresh regression samples from the current Unicode charts/data. Examples in Android implementation guidance are implementation references, not the policy's version ceiling.

This topic paraphrases the Play policy and implementation guidance; it is not a verbatim mirror of the Unicode standard. The Play rule set is short; the Emoji2 guide supplies implementation paths, not a separate Play-review exemption. The Android Emoji documentation's API descendants have not all been traversed.

## Sources and related knowledge

- [Google Play: Android Emoji Policy](https://support.google.com/googleplay/android-developer/answer/11190644?hl=en)
- [Unicode Emoji technical index](https://www.unicode.org/emoji/techindex.html)
- [Unicode Emoji charts](https://www.unicode.org/emoji/charts/)
- [UTS #51: Unicode Emoji](https://www.unicode.org/reports/tr51/)
- [Android: Support modern emoji](https://developer.android.com/develop/ui/views/text-and-emoji/emoji2)
- [Google Play target API and Android migration](../target-api/target-api-level.en-US.md)
