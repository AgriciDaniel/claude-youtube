# YouTube SEO Playbook

## Table of Contents

- [Title Optimization](#title-optimization)
- [Description Structure](#description-structure)
- [Tags](#tags)
- [Chapters & Timestamps](#chapters--timestamps)
- [Hashtags](#hashtags)
- [Captions & Transcription](#captions--transcription)
- [Cards & End Screens](#cards--end-screens)
- [VideoObject Schema Markup](#videoobject-schema-markup)
- [YouTube Search vs Google Search](#youtube-search-vs-google-search)
- [Keyword Research Tools](#keyword-research-tools)
- [Key Constraints & Gotchas](#key-constraints--gotchas)

---

## Title Optimization

| Property | Value |
|----------|-------|
| Hard character limit | 100 characters |
| Desktop truncation | ~60-70 characters |
| Mobile truncation | ~40-50 characters |
| Front-load keyword | First 40-50 characters |

### Performance Data

- **70-100 character titles** outperform shorter titles by **10-14%** (10xCreator, 3M+ videos analyzed)
- **Numbers in titles** = +20-30% CTR
- **Brackets** add useful context (e.g., `[2025 Update]`, `[Step-by-Step]`)

### Clickbait Penalty `[2025]`

- Official rollout: late 2024, India first, then global
- **Gemini AI** compares actual video content against title/thumbnail metadata
- Misleading titles are actively suppressed

---

## Description Structure

| Property | Value |
|----------|-------|
| Max length | 5,000 characters |
| Visible before "Show more" | First 150-200 characters |
| Primary keyword placement | First 25 words |

### Recommended Structure

| Section | Content |
|---------|---------|
| Lines 1-3 | Primary keyword + hook (visible in preview) |
| Next block | Timestamps/chapters |
| Body | 200-350 words, keyword appears 2-4x |
| Links | Relevant resources, social |
| CTA | Subscribe, comment prompt |
| Closing | 3 hashtags |

- `[2025]` **29.5%** of Google AI Overviews cite YouTube (BrightEdge, mid-2025)

---

## Tags

- **Status**: Vestigial -- minimal ranking impact
- **Limit**: 500 characters, spend max 30 seconds
- `[2025]` Gemini analyzes actual video content now, not tags

### Only Use Tags For

- Common misspellings of your topic
- Disambiguation (when your topic has multiple meanings)
- Brand-new channels with no content history

---

## Chapters & Timestamps

| Requirement | Value |
|-------------|-------|
| Must start at | 0:00 |
| Minimum chapters | 3 |
| Minimum chapter length | 10 seconds each |

### Impact

- Enables **Google Key Moments** in search results
- **25%+** of Google search results include video snippets
- **4% higher AVD** (Backlinko)
- **Retention up to 50% higher** with timestamps (HubSpot)
- Use keyword-rich chapter labels

---

## Hashtags

| Context | Optimal Count | Max Before Ignored |
|---------|--------------|-------------------|
| Regular videos | 3-5 | 15 (exceeding = ALL ignored) |
| Shorts | 1-5 | 60 total characters |

- First 3 hashtags appear **above the video title**
- Exceeding 15 hashtags causes YouTube to ignore ALL of them

---

## Captions & Transcription

- **12% longer watch time** with captions enabled
- **80%** of caption users are not deaf (accessibility + comprehension)
- Manual SRT uploads rank better for indexing than auto-captions
- **Say target keywords naturally** on camera -- YouTube transcribes audio as SEO signals

---

## Cards & End Screens

- Cards and end screens **do not directly affect ranking**
- End screen CTR benchmarks:
  - **2%+** = healthy
  - **4%+** = strong
- Optimal placement: last **15-20 seconds** of video
- End screens can **double post-viewing engagement**

---

## VideoObject Schema Markup

### Required Properties

| Property | Description |
|----------|-------------|
| `name` | Video title |
| `thumbnailUrl` | Thumbnail image URL |
| `uploadDate` | ISO 8601 date |

### Performance

- `[2025]` **30% higher CTR** with VideoObject schema (Backlinko 2025)
- Use **JSON-LD** format
- Add **Clip** and **SeekToAction** markup for chapter-level rich results
- Since late 2023: video must be **main content** of the page for rich snippets (not sidebar embeds)

---

## YouTube Search vs Google Search

| Factor | YouTube Search | Google Search |
|--------|---------------|---------------|
| Primary ranking signal | Retention & satisfaction | Information delivery |
| Content priority | Watch time, engagement | Relevance, authority |

### Video-Trigger Keywords (Appear in Google Video Results)

- "how to", "tutorial", "review", "vs", "explained"

### Discovery Tool

- Use **Google Trends** with **YouTube Search filter** for keyword demand validation

---

## Keyword Research Tools

| Tool | Best For | Price |
|------|----------|-------|
| **vidIQ** | Research quality, keyword scoring | $17.50/mo |
| **TubeBuddy** | A/B testing integration | $2.25/mo |
| **YouTube Studio Research** | Own channel analytics | Free |
| **Google Trends (YouTube filter)** | Trend validation | Free |

- Neither vidIQ nor TubeBuddy has a public API
- `[2025]` Jan 2026 Search Filter Update for long-tail keywords (unconfirmed -- mentioned in community reports, not officially documented)

---

## Key Constraints & Gotchas

- **Mobile truncates titles at ~40-50 chars** -- if the keyword or hook isn't in that range, mobile viewers miss it
- **Exceeding 15 hashtags causes ALL hashtags to be ignored** -- not just the extras
- **Tags are effectively dead** -- spending more than 30 seconds on them is wasted effort. Gemini reads video content directly `[2025]`
- **Description keyword stuffing hurts** -- 2-4x keyword density in 200-350 words is the ceiling
- **First 150-200 chars of description** are all viewers see before clicking "Show more" -- treat them as ad copy
- **VideoObject schema only works** when the video is the main page content (since late 2023)
- **Clickbait penalty is AI-enforced** `[2025]` -- Gemini compares metadata to actual content. No manual review needed to trigger suppression
- **Auto-captions are inferior** to manual SRT for SEO indexing
- **Chapters require 0:00 start** -- omitting it disables the entire chapter system
- **Google AI Overviews increasingly cite YouTube** (29.5%, BrightEdge mid-2025) -- optimize descriptions for Google, not just YouTube search
