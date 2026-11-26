---
id: google-play.spam-and-functionality
platform: google-play
language: en-US
authority: normative
status: current
kb_checked_at: 2026-10-22
review_due: 2027-01-22
regions: [global]
topics: [spam, webview, repetitive-content, functionality, user-experience]
snapshot_id: play.spam-and-functionality
snapshot_package: "GooglePlay-KnowledgeBase-2026-10-24-review.zip"
coverage_status: "detailed-summary"
source_url: "https://support.google.com/googleplay/android-developer/answer/9899034?hl=en"
effective_date: "current-policy"
---

# Google Play Spam, Functionality, and User Experience Policies

> **Import note (Google batch 4).** The body is the paraphrased summary from the already separated 2026-10-24 Google Play knowledge-base snapshot (`play.spam-and-functionality`, reviewed 2026-10-22). It is not a verbatim copy of an official page. The English official source is the source of truth. `kb_checked_at` is the review date recorded in the snapshot source file; this import did not re-open the live official pages. Phrases such as “this knowledge base,” “this library,” and “local topic” describe coverage inside that snapshot, not the set of pages imported into this repository. Relative snapshot links to topics, link graphs, ledgers, or CSVs that are not in this repository are kept as text mentions. Relative links that target the Google batch 1–3 topics or these twelve batch 4 topics point at the hub files. The Spam, Functionality, and Help-topic URLs recorded in the snapshot are English. The snapshot does not record a checked Chinese official Spam or Functionality page. The Chinese hub text is the snapshot’s editorial paraphrase, not Google’s published Chinese page text. No future-effective date is recorded. The “1 / 2” numbering locates the current Help article. It does not mean other policies use the same permanent global scheme. The pre-release test list is operational advice for the stability requirement, not an exhaustive test list printed on the policy page. The Play Academy course is training and does not replace the policy text. Spam and Functionality are two separate `normative` Help articles. Check them apart from MUwS, malware, deceptive behavior, and ad fraud.

**Reviewed October 22, 2026.** The Play Center groups Spam and Functionality, Content, and User Experience together, but they have separate Help articles. This topic summarizes both: apps must not fill Google Play with spam or repetitive low-value experiences, and must provide stable functionality and meaningful content.

## Spam

| Risk area | Policy boundary | Pre-release check |
| --- | --- | --- |
| Messages sent on a user's behalf | Apps must not send SMS, email, or other messages without letting the user confirm the content and intended recipients first. A generic Share button does not itself establish confirmation of the exact message and recipients. | Show the complete content and recipients before sending; obtain an explicit user action before transmission. |
| Webview and affiliate spam | A primary purpose of driving affiliate traffic for signup/purchase credit, or wrapping a website in a WebView without permission from its owner/administrator, are common violations. | Ensure the app has independent user functionality; obtain and retain permission for embedded third-party sites. Do not make a referral funnel or website shell the product. |
| Repetitive content | Apps should not merely reproduce the experience of apps already on Play. They should provide unique value through original content or services. Copying without added value, or publishing many highly similar apps with little content, are common problems. | Consider consolidating similar low-content apps into one app with sufficient content; document the real difference in content, service, or experience. |

## Functionality, content, and user experience

Apps should have a basic, stable, responsive degree of mobile functionality and meaningful content. Google's Help page gives examples of limited functionality: static text or PDF-only apps, low-content experiences such as a single-wallpaper app, and apps with no purpose or function. Crashes, force-closes, freezes, failure to install, failure to load, or failure to respond to the user are inconsistent with a functional experience.

### Numbered sections in the current policy (checked October 22, 2026)

The current Help body numbers its sections **1. Limited Functionality and Content** and **2. Broken Functionality**. The first covers examples such as static text/PDF apps, very little content, or no actual function. The second covers failure to install, load, or respond, as well as crashes, force-closes, and freezes. The announcement says standardized numbering is being introduced across some policies over time; treat “1/2” as a locator in this reviewed version, not as proof of a universal policy ID system or an immutable number.

The Help page also says its Policy Summary and Key Considerations are overviews; the full policy takes precedence if they conflict. For review records, retain the policy title, source URL, review date, and section heading instead of relying on a summary or number alone.

**Operational practice:** Before release, test installation, first launch, core user journeys, network errors, and recovery on target devices and system versions. Review content volume, interaction completeness, and failure paths. These are practical ways to implement the stability/functionality requirement, not an exhaustive test list quoted from the policy.

## Relationship to other policies

- Spam and low-value behavior overlap with [Mobile Unwanted Software and deceptive behavior](../mobile-unwanted-software/mobile-unwanted-software.en-US.md), but spam, malware, deceptive behavior, and ad fraud are separate policy categories. Classify the specific behavior before applying a rule.
- If a violation leads to enforcement, use the [enforcement and appeals topic](../enforcement-and-appeals/enforcement-and-appeals.en-US.md) to distinguish rejection, removal, suspension, and warning, then follow the case notice. Repeatedly submitting an unfixed version can escalate the matter.
- The Help pages say their summaries and key considerations are overviews only; the full policy controls if there is a conflict. Play Academy is training and does not replace policy text.

## Page and direct-link audit

The body text in the Spam and Functionality articles was opened. Their image links are policy illustrations, not additional rule text. Access attempts are recorded below; text extraction cannot reliably read the image contents.

| Source page | Direct body-link target | Relationship and access result |
| --- | --- | --- |
| [Spam](https://support.google.com/googleplay/android-developer/answer/9899034?hl=en) | [Messaging-spam illustration](https://lh3.googleusercontent.com/ba4qjNQZ7-IgV4QhGps-OVgNA7cQpgWRb348SxYlgw05cv3tZqFvrNrNlYuzku88Z788%3Dh839), [WebView/affiliate illustration](https://lh3.googleusercontent.com/AZr3T8GiGN_g2AS76qWQ622zQNReHU4GKoKjbhrZGWNazx15FhZTOEomNI9z2o2pEps%3Dh1100), [repetitive-content illustration](https://lh3.googleusercontent.com/6viGjA--lsmMb74UZL8pAO9YY34hHWCDtxkfQAHlK_pbBAmLd9kq8P39lckZh2ayv8LY%3Dw895) | All three targets opened as image URLs. Their contents were not reliably extractable as text, so the summary uses the readable policy text and does not infer further details from the graphics. |
| [Functionality, Content, and User Experience](https://support.google.com/googleplay/android-developer/answer/9898783?hl=en) | [Policy-summary graphic](https://lh3.googleusercontent.com/BPsAL28eke0gFbFJduiZupJyY6uR5X7_JHR_3vev1cApatT5KLrReyskdlNZXRGFsg%3Dw60-h60), [full-policy graphic](https://lh3.googleusercontent.com/hnJIMKQ0lyssVbehdx4OCpjLHPBYy94NeG4dD-xZ40osbCjM8Lt3zS4P5JvA5Xsqig%3Dw30-h34), [limited-functionality illustration](https://play-kmt.teams.x20web.corp.google.com/no_crawl/arhc/images/minimum_funct1.png), [failure-to-load illustration](https://lh3.googleusercontent.com/8Stc92Uebx_6XLNG0-cE6IlFertNFab0nNjhdKrihRS3teDiGk1ePWnAcC5w6W_qIg%3Dh839), [unresponsive-app illustration](https://lh3.googleusercontent.com/VG3exQhozTq3qrIuen3HBMeLGDWBtedEkseEgSlyBMVtuYGJQ-OD3gruKvXogAozuDA%3Dh839), [Key Considerations graphic](https://lh3.googleusercontent.com/IfJhh8qlFSuw1U7A2DSeKi0B3jBYMC5fU0pGMUG40oyCU3urkOu4yGg0D24TkbUvwRk%3Dw40) | All six targets were attempted: four public image URLs returned targets; one internal example redirected to corporate sign-in; one image had a cache miss. These illustrations add no separate policy obligation. |
| Both Help articles | Feedback and support controls | The Qualtrics survey and Help Community returned cache misses. “Contact us” redirected to a Play Console support page that requires account access. These are feedback/support routes, not policy requirements. |
| [Spam, Functionality, and User Experience Help topic](https://support.google.com/googleplay/android-developer/topic/9876964?hl=en) | [Spam](https://support.google.com/googleplay/android-developer/answer/9899034?hl=en), [Functionality](https://support.google.com/googleplay/android-developer/answer/9898783?hl=en), [Play Academy course](https://playacademy.exceedlms.com/student/path/65190-comply-with-google-play-s-spam-and-minimum-functionality-policies) | The Help topic describes the combined aim of preventing spam and ensuring basic functionality; both policies were reviewed separately. The linked course page exposes chapter titles, but lesson content/interactions require login. |
| Play Academy course | [Training video](https://www.youtube.com/watch?v=0PGBqQWgBEA) | Video fetch failed. The course landing page lists Affiliate Spam, Made for Ads, Messaging Spam, Functionality, Repetitive Content, and Webview Spam modules. This is a training outline, not a substitute for unviewed lesson content or policy text. |

Both Help articles also link to Help Community and Contact us page controls; access outcomes are recorded above. Related-content sidebars are navigation, not body links. The Help pages do not provide a dedicated Spam appeal procedure; case outcomes and account status must be checked in the developer's notices and Play Console.

## Pre-release checklist

- [ ] Before sending a message on a user's behalf, show and confirm its contents and recipients.
- [ ] The app is not primarily an affiliate-traffic funnel or an unauthorized WebView of a third-party site.
- [ ] Similar apps have clear incremental user value; consider consolidating low-content duplicates.
- [ ] New users can install, launch, understand, and complete the advertised core function; key failure paths recover gracefully.
- [ ] Store descriptions and screenshots match actual functionality and do not use misleading interaction to imply value.

## Sources

- [Spam](https://support.google.com/googleplay/android-developer/answer/9899034?hl=en)
- [Functionality, Content, and User Experience](https://support.google.com/googleplay/android-developer/answer/9898783?hl=en)
- [Spam, Functionality, and User Experience Help topic](https://support.google.com/googleplay/android-developer/topic/9876964?hl=en)
- [Play Academy course](https://playacademy.exceedlms.com/student/path/65190-comply-with-google-play-s-spam-and-minimum-functionality-policies)

This is a bilingual paraphrased summary, not a full-text mirror. Illustrations, interactive support, and course content may require connectivity or sign-in.
