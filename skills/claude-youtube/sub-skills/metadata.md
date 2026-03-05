# Metadata Sub-Skill

This sub-skill generates a complete, copy-paste-ready upload metadata package for a YouTube video — title variants, full description, tags, hashtags, chapters, thumbnail brief, card/end screen placement, publish settings, and a pre-publish SEO checklist. It serves as the final pre-publish gate, ensuring every SEO and discoverability element is optimised before the video goes live.

## Inputs Required

- **Video title** (string): working title (will be optimised)
- **Description** (string): draft description or bullet points of what the video covers
- **Content summary** (string): brief overview of the video's content and key points
- **Niche** (string): content category for keyword and audience targeting
- **Target keyword** (string): primary keyword the video should rank for
- **Video duration** (optional): total length for card/end screen timing calculations
- **Chapter timestamps** (optional): existing chapter markers to refine

## Reference Files to Load

- `references/seo-playbook.md`

## DataForSEO Research (When Available)

Validate metadata choices with live data:

1. **Tag optimization**: Run `kw_data_google_ads_search_volume` with all candidate tags to prioritise by real search volume.
2. **Keyword difficulty**: Use `dataforseo_labs_bulk_keyword_difficulty` to avoid tags where competition is too high for the channel's authority level.
3. **Title validation**: Run `serp_youtube_organic_live_advanced` with the primary keyword to check if the chosen title pattern aligns with what's currently ranking.

**Fallback:** If DataForSEO is unavailable, rely on keyword heuristics from the SEO playbook reference.

**Efficiency:** Typical metadata workflow costs ~$0.004 (2-3 API calls).

## Parallel Agents

Not required. Execute sequentially.

## Step-by-Step Execution

1. Load the SEO playbook reference file. Internalise title formulas, description structure, tag strategy, and all metadata best practices.
2. Analyse the target keyword. Assess its placement potential in titles and descriptions. Identify 2-3 secondary keywords and long-tail variations.
3. Generate 3 title variants: one search-optimised (keyword-forward, clear intent match), one browse-optimised (curiosity-driven, emotional trigger), and one hybrid (keyword present but wrapped in compelling framing). All titles must be under 100 characters with the primary keyword in the first 40 characters.
4. Write the full description (max 5000 characters). Structure it with the primary keyword in the first 25 words, a compelling first 2 lines (visible before "Show More"), timestamps/chapters, relevant links, and a channel description boilerplate. Include hashtags at the bottom of the description (not in the title).
5. Generate 10-15 tags in priority order. Start with the exact target keyword, then variations, then broader topic tags. Total tag string must be under 500 characters.
6. Select 3-5 hashtags. Lead with the most specific, end with the broadest.
7. Format chapters starting at 0:00 with a minimum of 3 chapters. If timestamps were provided, refine them. If not, create placeholder chapters based on the content summary.
8. Write a one-line thumbnail brief covering: subject/focal point, emotion/expression, text overlay (max 3-4 words), and dominant colour scheme.
9. Plan cards and end screens. Place cards at approximately 20% and 70% of video length. Recommend which video to link (related content or series next). Design end screen for the final 20 seconds with video suggestion and subscribe element.
10. Recommend publish settings: optimal day/time for the niche, audience setting (made for kids or not), category, and language.
11. Compile the pre-publish SEO checklist.

## Output Template

````markdown
## Upload Metadata Package: "[Working Title]"

**Target keyword**: [Primary keyword]
**Secondary keywords**: [Keyword 2], [Keyword 3]

---

### TITLE OPTIONS (3 variants)

| Type | Title | Chars |
|------|-------|-------|
| Search-optimised | [Keyword-forward, clear intent] | [N] |
| Browse-optimised | [Curiosity-driven, emotional] | [N] |
| Hybrid (recommended) | [Keyword + compelling frame] | [N] |

**Recommendation**: Use [type] because [reasoning].

---

### FINAL DESCRIPTION (copy-paste ready)

```
[First 2 lines — visible before "Show More". Primary keyword in first 25 words. Compelling hook.]

[Paragraph 2 — expanded context, secondary keywords naturally included]

TIMESTAMPS:
0:00 Introduction
[MM:SS Chapter title]
[MM:SS Chapter title]
[MM:SS Chapter title]

RESOURCES MENTIONED:
- [Resource 1]: [link placeholder]
- [Resource 2]: [link placeholder]

CONNECT:
[Social link placeholders]

ABOUT THIS CHANNEL:
[1-2 sentence channel description boilerplate]

#hashtag1 #hashtag2 #hashtag3 [#hashtag4] [#hashtag5]
```

**Character count**: [N] / 5000

---

### TAGS (copy-paste, comma-separated)

```
[exact target keyword], [variation 1], [variation 2], [long-tail 1], [long-tail 2], [related topic 1], [related topic 2], [broader term 1], [broader term 2], [broader term 3], [channel name]
```

**Character count**: [N] / 500

---

### HASHTAGS

```
#[specific1] #[specific2] #[mid-range] #[broader] #[broadest]
```

---

### CHAPTERS

```
0:00 Introduction
[MM:SS] [Chapter title — descriptive, keyword-aware]
[MM:SS] [Chapter title]
[MM:SS] [Chapter title]
[MM:SS] [Chapter title]
```

**Chapter count**: [N] (minimum 3 required)

---

### THUMBNAIL BRIEF

> **Subject**: [Who/what is the focal point]
> **Emotion**: [Expression or mood]
> **Text overlay**: [3-4 words max]
> **Dominant colours**: [2-3 colours, high contrast]
> **Composition**: [Left/right/center weighted, rule of thirds note]

---

### CARDS & END SCREENS

**Card 1** (at [MM:SS] — ~20% mark):
- Link to: "[Related video title]"
- CTA text: "[Teaser text]"
- Trigger: Place after [content moment that creates curiosity about related topic]

**Card 2** (at [MM:SS] — ~70% mark):
- Link to: "[Related video or playlist title]"
- CTA text: "[Teaser text]"
- Trigger: Place after [relevant content moment]

**End screen** (final 20 seconds, starts at [MM:SS]):
- Element 1: Best for viewer (video suggestion)
- Element 2: Subscribe button
- Verbal CTA: "[Exact words to say during end screen]"

---

### PUBLISH SETTINGS

| Setting | Value | Rationale |
|---------|-------|-----------|
| Publish day | [Day] | [Why — niche audience behaviour] |
| Publish time | [HH:MM timezone] | [Why — peak audience activity] |
| Audience | [Not made for kids / Made for kids] | |
| Category | [Category] | |
| Language | [Language] | |
| Visibility | [Public / Unlisted / Scheduled] | |
| Premiere | [Yes / No] | [Rationale] |

---

### PRE-PUBLISH SEO CHECKLIST

- [ ] Primary keyword in title (first 40 characters)
- [ ] Primary keyword in first 25 words of description
- [ ] Description under 5000 characters
- [ ] Timestamps start at 0:00 with minimum 3 chapters
- [ ] Tags under 500 characters total
- [ ] Custom thumbnail uploaded (not auto-generated)
- [ ] Hashtags in description body (not in title)
- [ ] Cards placed at ~20% and ~70% of video length
- [ ] End screen covers final 20 seconds
- [ ] End screen has video suggestion + subscribe element
- [ ] Subtitles/captions uploaded or auto-generated reviewed
- [ ] Audience setting correct (kids/not kids)
- [ ] Video category selected
- [ ] Verbal CTA matches end screen timing
````

## Quality Criteria

- All 3 title variants are genuinely distinct in strategy, not minor word swaps
- Primary keyword appears in the first 40 characters of every title variant
- Description places the primary keyword within the first 25 words naturally
- Description first 2 lines are compelling standalone (they appear before "Show More")
- Tags are in priority order: exact keyword first, then variations, then broad terms
- Tag total is under 500 characters — verified with a character count
- Description total is under 5000 characters — verified with a character count
- Chapters start at 0:00 and include at least 3 entries
- Hashtags are in description, never in the title
- Card placements reference specific content moments, not arbitrary timestamps
- End screen timing accounts for the actual video duration
- Thumbnail brief is specific enough for a designer to execute without questions
- Pre-publish checklist covers all items — none are omitted
- The entire package is copy-paste ready with no placeholder brackets remaining in the copy-paste sections (except link placeholders clearly marked)
