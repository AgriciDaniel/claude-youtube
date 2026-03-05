# DataForSEO Integration Reference

Live YouTube data via the DataForSEO MCP server. When available, youtube skills use
these tools for real keyword metrics, YouTube SERP analysis, video intelligence,
trend data, and competitive research. Falls back to WebSearch + execution scripts
when DataForSEO is unavailable.

## Table of Contents

- [Detection & Fallback](#detection--fallback)
- [Default Parameters](#default-parameters)
- [API Credit Efficiency](#api-credit-efficiency)
- [YouTube-Specific Tools](#youtube-specific-tools)
- [Keyword Research Tools](#keyword-research-tools)
- [Trends & Seasonality](#trends--seasonality)
- [Competitor & Domain Analysis](#competitor--domain-analysis)
- [AI Visibility (GEO)](#ai-visibility-geo)
- [Sub-Skill → DataForSEO Module Mapping](#sub-skill--dataforseo-module-mapping)
- [Estimated Cost Per Workflow](#estimated-cost-per-workflow)
- [YouTube SERP Research Workflow](#youtube-serp-research-workflow)
- [Key Constraints & Gotchas](#key-constraints--gotchas)

---

## Detection & Fallback

Before using DataForSEO tools, check availability by calling any tool (e.g.,
`serp_youtube_organic_live_advanced`). If the call fails or the tool is not
found, fall back to WebSearch and execution scripts for that step.

**Pattern:**
1. Attempt DataForSEO tool call
2. If successful → use live data
3. If unavailable → fall back to WebSearch + execution scripts
4. Never block a workflow because DataForSEO is unavailable

## Default Parameters

All DataForSEO tools accept these defaults unless the user specifies otherwise:
- `location_code`: 2840 (United States)
- `language_code`: "en"
- `device`: "desktop" (SERP tools)
- `limit`: 50 (list endpoints)
- `depth`: 100 (SERP depth)

## API Credit Efficiency

DataForSEO charges per API call. Follow these rules:
- **Batch keywords** into single calls (volume/difficulty/intent tools accept arrays)
- **Don't re-fetch** data already retrieved in the same session
- **Use `dataforseo_labs_google_keyword_overview`** for single-keyword lookups
- **Default to limit=50** for list endpoints unless more results are needed
- **Warn the user** before running expensive operations (large keyword lists, full crawls)

---

## YouTube-Specific Tools

### YouTube SERP (Search Results)

| Tool | Purpose | Key Parameters | ~Cost |
|------|---------|---------------|-------|
| `serp_youtube_organic_live_advanced` | YouTube search results for a keyword | `keyword`, `location_code`, `language_code`, `device`, `depth` | ~0.002 |

**Response fields per result:**
- `youtube_video`: title, url, video_id, thumbnail_url, channel_id, channel_name, channel_url, channel_logo, description, views_count, publication_date, duration_time, duration_time_seconds, is_live, is_shorts, badges
- `youtube_channel`: channel_id, name, url, logo, video_count, is_verified, description
- `youtube_playlist`: title, url, playlist_id, videos_count, preview_videos

**Use cases:**
- Keyword competition analysis (how many videos rank, their view counts)
- Content gap discovery (what topics have low competition)
- Competitor video identification for any keyword
- Shorts vs long-form ratio analysis in search results

### YouTube Video Intelligence

| Tool | Purpose | Key Parameters | ~Cost |
|------|---------|---------------|-------|
| `serp_youtube_video_info_live_advanced` | Full video metadata and metrics | `video_id` | ~0.002 |
| `serp_youtube_video_comments_live_advanced` | Video comments with engagement | `video_id` | ~0.002 |
| `serp_youtube_video_subtitles_live_advanced` | Video subtitles/transcript | `video_id` | ~0.002 |

**Video info response fields:**
- Core: video_id, title, url, thumbnail_url, description, duration_time, duration_time_seconds, publication_date
- Engagement: views_count, likes_count, comments_count
- Channel: channel_id, channel_name, channel_url, channel_subscribers_count
- Classification: keywords (tags), category, is_live, is_embeddable
- Technical: subtitles (languages available), streaming_quality (resolutions)

**Comments response:** Comment text, author, likes, reply count, timestamp
**Subtitles response:** Full transcript text with language and auto-generation flags

---

## Keyword Research Tools

| Tool | Purpose | Parameters | ~Cost |
|------|---------|------------|-------|
| `kw_data_google_ads_search_volume` | Monthly search volume, CPC, competition, monthly trends | `keywords` (array), `location_code`, `language_code` | ~0.001 |
| `dataforseo_labs_google_keyword_ideas` | Generate keyword ideas from seed | `keywords` (array), `location_code`, `language_code`, `limit` | ~0.001 |
| `dataforseo_labs_google_keyword_suggestions` | Autocomplete-style suggestions | `keywords` (array), `location_code`, `language_code`, `limit` | ~0.001 |
| `dataforseo_labs_google_related_keywords` | Semantically related keywords | `keywords` (array), `location_code`, `language_code`, `limit` | ~0.001 |
| `dataforseo_labs_bulk_keyword_difficulty` | Difficulty scores (0-100) | `keywords` (array), `location_code`, `language_code` | ~0.001 |
| `dataforseo_labs_search_intent` | Intent classification (informational, commercial, transactional, navigational) | `keywords` (array), `location_code`, `language_code` | ~0.0005 |
| `dataforseo_labs_google_keyword_overview` | Quick overview: volume + difficulty + intent | `keywords` (array), `location_code`, `language_code` | ~0.001 |

**YouTube context:** Google search volume strongly correlates with YouTube search volume.
Keywords with high Google volume + informational intent are prime YouTube targets.
Commercial/transactional keywords convert better for monetisation but have lower view potential.

## Trends & Seasonality

| Tool | Purpose | Parameters | ~Cost |
|------|---------|------------|-------|
| `kw_data_google_trends_explore` | Google Trends time series data | `keywords` (array, max 5), `location_code`, `date_from`, `date_to`, `type` | ~0.001 |
| `content_analysis_phrase_trends` | Phrase popularity over time | `keyword`, `date_from`, `date_to` | ~0.002 |

**Critical for YouTube:** Use `kw_data_google_trends_explore` to:
- Identify rising topics before they peak (ideal upload timing)
- Compare topic seasonality for calendar planning
- Validate ideation topics against real trend data
- Detect declining topics to avoid (wasted production effort)

## Competitor & Domain Analysis

| Tool | Purpose | Parameters | ~Cost |
|------|---------|------------|-------|
| `dataforseo_labs_google_competitors_domain` | Competing domains by keyword overlap | `target` (domain), `location_code`, `language_code` | ~0.002 |
| `dataforseo_labs_google_ranked_keywords` | Keywords a domain ranks for with positions | `target` (domain), `location_code`, `language_code`, `limit` | ~0.002 |
| `dataforseo_labs_google_domain_intersection` | Shared keywords across 2-20 domains | `targets` (array), `location_code`, `language_code` | ~0.002 |
| `dataforseo_labs_bulk_traffic_estimation` | Estimated organic traffic for domains | `targets` (array), `location_code`, `language_code` | ~0.001 |
| `content_analysis_search` | Find content by topic with quality scores | `keyword` or `url` | ~0.002 |

**YouTube context:** Use these to analyze competitor channel websites and blog presence.
Cross-reference with `serp_youtube_organic_live_advanced` to build a complete picture
of competitor keyword coverage across both Google and YouTube.

## AI Visibility (GEO)

| Tool | Purpose | Parameters | ~Cost |
|------|---------|------------|-------|
| `ai_optimization_chat_gpt_scraper` | ChatGPT web search results: cited sources | `query`, `location_code`, `language_code` | ~0.01 |
| `ai_opt_llm_ment_search` | LLM mentions of a keyword/brand | `keyword`, `location_code`, `language_code` | ~0.01 |
| `ai_opt_llm_ment_top_domains` | Top domains cited by LLMs | `keyword`, `location_code`, `language_code` | ~0.01 |

**YouTube context:** YouTube videos appear in AI citations. Use these to check
if a creator's videos are being cited by AI platforms and identify gaps.

---

## Sub-Skill → DataForSEO Module Mapping

| Sub-Skill | DataForSEO Modules | What It Gets |
|-----------|-------------------|--------------|
| ideate | KEYWORDS_DATA, SERP (YouTube), ONPAGE | Keyword ideas, YouTube SERP competition, trends, search volume for idea validation |
| seo | KEYWORDS_DATA, DATAFORSEO_LABS, SERP (YouTube) | Volume, difficulty, intent for title/tag optimisation, YouTube SERP for competition check |
| competitor | SERP (YouTube), DATAFORSEO_LABS | YouTube SERP for keyword gaps, competitor domain analysis, ranked keywords |
| strategy | KEYWORDS_DATA, DATAFORSEO_LABS, SERP (YouTube), ONPAGE | Trends, volume, competition depth, niche viability, content gaps |
| calendar | KEYWORDS_DATA, ONPAGE | Google Trends for seasonal planning, volume for prioritisation |
| analyze | SERP (YouTube), DATAFORSEO_LABS | YouTube SERP position tracking, keyword overview for diagnosed videos |
| audit | SERP (YouTube), DATAFORSEO_LABS, KEYWORDS_DATA | Channel keyword coverage, YouTube SERP positions, competitor benchmarking |
| shorts | SERP (YouTube), KEYWORDS_DATA | Shorts-specific keyword trends, YouTube SERP Shorts ratio |
| hook | SERP (YouTube) | Top-performing video titles/hooks for the keyword from YouTube SERP |
| thumbnail | SERP (YouTube) | Competitor thumbnail analysis via YouTube SERP results |
| metadata | KEYWORDS_DATA, DATAFORSEO_LABS | Real volume/difficulty for tag optimisation, intent for description framing |

## Estimated Cost Per Workflow

| Workflow | Typical API Calls | Est. Cost |
|----------|------------------|-----------|
| `/youtube ideate <niche>` | 5-8 (trends + volume + ideas + YouTube SERP) | ~$0.01 |
| `/youtube seo <video>` | 3-5 (volume + difficulty + intent + YouTube SERP) | ~$0.008 |
| `/youtube competitor <channels>` | 6-10 (YouTube SERP × keywords + domain analysis) | ~$0.02 |
| `/youtube strategy <niche>` | 8-12 (trends + volume + YouTube SERP + competition) | ~$0.03 |
| `/youtube calendar` | 3-5 (trends + volume for scheduling) | ~$0.008 |
| `/youtube audit <channel>` | 8-15 (YouTube SERP + volume + video info × videos) | ~$0.04 |
| `/youtube analyze <video>` | 2-4 (video info + YouTube SERP + keyword overview) | ~$0.008 |
| `/youtube metadata <video>` | 2-3 (volume + difficulty for tags) | ~$0.004 |

## YouTube SERP Research Workflow

Standard research pattern for any YouTube sub-skill:

```
1. Identify target keywords (from user input or ideation)
2. Run `serp_youtube_organic_live_advanced` for each keyword
3. Extract from results:
   - Top video view counts → benchmark for niche
   - Channel distribution → concentration vs fragmentation
   - Shorts vs long-form ratio → format opportunity
   - Publication dates → content freshness in niche
   - Title patterns → what's working
4. Cross-reference with `kw_data_google_ads_search_volume`
   - High Google volume + low YouTube competition = opportunity
5. Validate with `kw_data_google_trends_explore`
   - Rising trend = act now, declining = avoid
```

---

## Key Constraints & Gotchas

- **Google volume ≠ YouTube volume** -- DataForSEO provides Google Ads search volume, not YouTube-specific volume. Google volume is a strong proxy but not identical; some keywords are disproportionately searched on YouTube (gaming, tutorials) vs Google
- **Batch keywords to save credits** -- volume, difficulty, and intent tools all accept arrays. Sending 20 keywords in one call costs the same as sending 1. Never loop single-keyword calls
- **Never re-fetch in the same session** -- if you already retrieved keyword data or YouTube SERP results for a keyword earlier in the conversation, reuse that data instead of making another API call
- **YouTube SERP results may lag** -- DataForSEO caches YouTube SERP data; results may be hours or days old. For trending topic analysis, supplement with `kw_data_google_trends_explore` for real-time signals
- **Video info requires video_id, not URL** -- extract the video ID from URLs before calling `serp_youtube_video_info_live_advanced`. Format: 11-character alphanumeric string (e.g., `dQw4w9WgXcQ`)
- **Comments tool returns limited depth** -- `serp_youtube_video_comments_live_advanced` returns top-level comments sorted by relevance, not all comments. Sufficient for audience gap analysis but not exhaustive
- **Subtitles may be auto-generated** -- check the auto-generation flag in `serp_youtube_video_subtitles_live_advanced` responses. Auto-generated transcripts contain errors that affect content analysis accuracy
- **CPC as RPM proxy is approximate** -- higher Google Ads CPC generally correlates with higher YouTube RPM for a topic, but the relationship is not linear. Use as a directional signal, not a precise estimate
- **Trends data compares relative interest, not absolute volume** -- `kw_data_google_trends_explore` returns index values (0-100), not search counts. Always pair with volume data for a complete picture
- **Cost awareness** -- typical YouTube workflow costs $0.002-$0.04. Warn the user before operations exceeding ~$0.05 (large keyword lists, multiple YouTube SERP queries)
