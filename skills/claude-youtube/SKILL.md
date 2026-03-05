---
name: claude-youtube
description: >
  The ultimate YouTube creator skill. Covers channel audits, video SEO,
  retention-engineered scripts, hook writing, thumbnail briefs, content
  strategy, content calendars, Shorts optimisation, analytics interpretation,
  monetisation planning, competitor research, cross-platform repurposing,
  upload metadata packages, and data-driven video idea generation.
  Triggers on: "youtube", "channel", "video", "views", "subscribers",
  "watch time", "shorts", "thumbnail", "CTR", "retention", "monetize",
  "script", "hook", "upload", "youtube audit", "video ideas",
  "content calendar", "competitor analysis", "repurpose video",
  "youtube seo", "youtube strategy", "youtube analytics".
tools:
  - Read
  - Write
  - Bash
  - WebSearch
  - Edit
  - Grep
  - Glob
  - Agent
---

# Claude YouTube — YouTube Creator Skill

> Orchestrator for 14 sub-skills covering every aspect of YouTube channel growth,
> optimisation, and monetisation. You route, delegate, and quality-check — sub-skills
> and execution scripts do the work.

## Command Router

| Command | Sub-Skill | Trigger Phrases |
|---------|-----------|----------------|
| `/youtube audit` | `sub-skills/audit.md` | "audit my channel", "channel health", "what's wrong with my channel", "my channel isn't growing" |
| `/youtube seo` | `sub-skills/seo.md` | "video SEO", "rank higher", "keyword research", "improve search ranking" |
| `/youtube script` | `sub-skills/script.md` | "write a script", "script for my video", "help me script" |
| `/youtube hook` | `sub-skills/hook.md` | "write a hook", "improve my intro", "first 30 seconds", "opening" |
| `/youtube thumbnail` | `sub-skills/thumbnail.md` | "thumbnail brief", "improve CTR", "design thumbnail" |
| `/youtube strategy` | `sub-skills/strategy.md` | "channel strategy", "content plan", "positioning", "niche" |
| `/youtube calendar` | `sub-skills/calendar.md` | "content calendar", "upload schedule", "what should I post this month" |
| `/youtube shorts` | `sub-skills/shorts.md` | "Shorts", "short video", "vertical video", "Shorts strategy" |
| `/youtube analyze` | `sub-skills/analyze.md` | "analyze metrics", "why are views dropping", "interpret analytics" |
| `/youtube repurpose` | `sub-skills/repurpose.md` | "repurpose video", "turn into Shorts", "cross-platform", "extract clips" |
| `/youtube monetize` | `sub-skills/monetize.md` | "monetize", "make money", "revenue", "brand deals", "memberships" |
| `/youtube competitor` | `sub-skills/competitor.md` | "competitor analysis", "spy on channel", "what is [channel] doing" |
| `/youtube metadata` | `sub-skills/metadata.md` | "upload metadata", "title and description", "pre-publish checklist" |
| `/youtube ideate` | `sub-skills/ideate.md` | "video ideas", "what should I make next", "brainstorm", "content ideas" |

If the user's request doesn't clearly match one command, ask a clarifying question.
If the request spans multiple sub-skills (e.g., "help me plan and script my next video"),
run the relevant sub-skills sequentially, passing output from each as input to the next.

## Context-Gathering Protocol

Before invoking ANY sub-skill, you MUST collect these three inputs. If any are missing, ask:

1. **Channel niche/topic** — What is the channel about? Be specific (not "tech" — "budget Android phone reviews").
2. **Channel size tier:**
   - New: < 1K subscribers
   - Growing: 1K–10K subscribers
   - Established: 10K–100K subscribers
   - Authority: 100K+ subscribers
3. **Primary goal:** Growth / Monetisation / Brand Authority / Audience Engagement

For `audit`, `analyze`, and `competitor` sub-skills, also collect the channel URL or handle.

## Channel Type Detection

Based on niche and content description, classify into one of 9 types and load the
matching template from `templates/`:

| Type | Template | Signals |
|------|----------|---------|
| Education | `templates/education-channel.md` | How-to, explainers, courses |
| Entertainment | `templates/entertainment-channel.md` | Comedy, challenges, reactions |
| Tutorial | `templates/tutorial-channel.md` | Step-by-step, walkthroughs, demos |
| Vlog | `templates/vlog-channel.md` | Day-in-life, personal updates |
| Review | `templates/review-channel.md` | Product reviews, comparisons, unboxing |
| Commentary | `templates/commentary-channel.md` | News commentary, opinion, essays |
| Niche Authority | `templates/niche-authority-channel.md` | Deep-dive single topic, expert positioning |
| Personal Brand | `templates/personal-brand-channel.md` | Creator-as-brand, multi-format |
| Shorts-First | `templates/shorts-first-channel.md` | Primarily vertical content |

## Parallel Agent Rules

**`audit` sub-skill** — spawn 4 parallel agents:
- Agent A: Technical SEO audit (loads `references/seo-playbook.md`)
- Agent B: Performance audit (loads `references/analytics-guide.md`)
- Agent C: Content strategy audit (loads `references/algorithm-guide.md`)
- Agent D: Monetisation audit (loads `references/monetization-guide.md`)

**`competitor` sub-skill** — spawn 4 parallel agents:
- Agent A: Top video analysis
- Agent B: Keyword gap analysis
- Agent C: Format gap analysis
- Agent D: Audience gap analysis (comment mining)

All other sub-skills run inline (single-threaded). If Agent tool is unavailable,
fall back to sequential inline execution.

## Reference Files

Load on-demand when a sub-skill requests them. Never pre-load all at once.
Do not reload a reference file already in context for this session.

| File | Content |
|------|---------|
| `references/algorithm-guide.md` | 3-system architecture, testing cascade, CTR/AVD benchmarks, 2024-2025 changes |
| `references/seo-playbook.md` | Title/description/tags/chapters/hashtags rules, VideoObject schema |
| `references/retention-scripting-guide.md` | Hook frameworks, pattern interrupts, CTA placement, retention graphs |
| `references/thumbnail-ctr-guide.md` | CTR by niche, face psychology, A/B testing, title formulas |
| `references/shorts-playbook.md` | Shorts algorithm, format specs, monetisation, repurposing |
| `references/analytics-guide.md` | Metrics hierarchy, funnel ratios, RPM/CPM by niche |
| `references/monetization-guide.md` | YPP tiers, 7 revenue streams, brand deal rates |
| `references/repurposing-guide.md` | Hub/Hero/Help model, cross-platform workflows, platform specs |
| `references/dataforseo-integration.md` | DataForSEO MCP tool reference, YouTube SERP, keyword research, trends |

## DataForSEO MCP Integration (Optional)

When the DataForSEO MCP server is available (configured in `~/.claude/settings.json`),
youtube skills use live data for keyword research, YouTube SERP analysis, trend
intelligence, video metadata, and competitive research. Falls back to WebSearch +
execution scripts when unavailable.

**Reference:** Load `references/dataforseo-integration.md` for full tool reference,
parameters, and efficiency guidelines.

**Detection:** Attempt any DataForSEO tool call (e.g., `serp_youtube_organic_live_advanced`).
If it fails, fall back to WebSearch + execution scripts. Never block a workflow
because DataForSEO is unavailable.

**Default parameters:** location_code=2840 (US), language_code="en"

### Key YouTube DataForSEO Tools

| Tool | Purpose |
|------|---------|
| `serp_youtube_organic_live_advanced` | YouTube search results for a keyword — videos, channels, playlists with view counts |
| `serp_youtube_video_info_live_advanced` | Deep video analysis — views, likes, comments, tags, category, subtitles |
| `serp_youtube_video_comments_live_advanced` | Video comments with engagement data |
| `serp_youtube_video_subtitles_live_advanced` | Video transcript/subtitles extraction |
| `kw_data_google_ads_search_volume` | Search volume, CPC, competition for keyword arrays |
| `dataforseo_labs_google_keyword_ideas` | Keyword ideas from seed keywords |
| `dataforseo_labs_google_keyword_suggestions` | Autocomplete-style keyword suggestions |
| `dataforseo_labs_bulk_keyword_difficulty` | Keyword difficulty scores (0-100) |
| `dataforseo_labs_search_intent` | Intent classification (informational/commercial/transactional) |
| `kw_data_google_trends_explore` | Google Trends time series (supports YouTube-specific filtering) |

### Sub-Skill → DataForSEO Module Mapping

| Sub-Skill | DataForSEO Tools Used |
|-----------|----------------------|
| ideate | YouTube SERP + keyword ideas + trends + volume |
| seo | Volume + difficulty + intent + YouTube SERP competition |
| competitor | YouTube SERP × keywords + video info + comments |
| strategy | Trends + volume + YouTube SERP + keyword ideas |
| calendar | Google Trends for seasonal planning + volume for prioritisation |
| analyze | YouTube SERP position tracking + video info |
| audit | YouTube SERP + volume + video info + keyword difficulty |
| shorts | YouTube SERP (Shorts filter) + trends |
| hook | YouTube SERP top video titles for keyword |
| thumbnail | YouTube SERP competitor thumbnails |
| metadata | Volume + difficulty for tag optimisation |

### API Credit Awareness

DataForSEO charges per API call. Typical workflow costs $0.002-$0.04.
Rules:
- Batch keywords into single calls (volume, difficulty, intent tools accept arrays)
- Don't re-fetch data already retrieved in the same session
- Use `dataforseo_labs_google_keyword_overview` for single-keyword lookups
- Warn the user before running expensive operations

## NanoBanana MCP — Thumbnail Generation (Optional)

When the NanoBanana MCP server is configured, the `thumbnail` sub-skill can generate
actual thumbnail images using Gemini models instead of just producing text briefs.

**Tool:** `generate_image`

**Recommended thumbnail settings:**
- `aspect_ratio`: `"16:9"` (YouTube standard)
- `resolution`: `"4k"` (1280×720 minimum for YouTube)
- `model_tier`: `"nb2"` (fast, high-quality production assets)

**Detection:** Attempt `generate_image` tool call. If unavailable, deliver text-based
thumbnail briefs only — they are detailed enough for any designer to execute.

**Workflow:** Primary thumbnail + 3 A/B variants = 4 `generate_image` calls per brief.
See `sub-skills/thumbnail.md` for prompt engineering guidelines.

## Execution Scripts

Scripts require YouTube API credentials. Before calling any script:
1. Check if `YOUTUBE_API_KEY` environment variable exists
2. If missing, provide the user with setup instructions instead of failing silently
3. For Analytics API scripts, check OAuth token exists

If credentials are absent, fall back to asking the user to provide data manually
(e.g., paste YouTube Studio screenshots or describe their metrics).

| Script | Purpose | Quota Cost |
|--------|---------|-----------|
| `execution/fetch_channel_data.py` | Channel stats + last N videos via Data API v3 | ~16 units |
| `execution/fetch_video_analytics.py` | Private analytics (own channel, OAuth) | ~5 units |
| `execution/search_competitor_videos.py` | Search competitor videos (expensive) | 100 units/search |
| `execution/fetch_transcript.py` | Video transcript extraction | 1-2 units |
| `execution/utils/quota_tracker.py` | Tracks 10K unit/day quota | 0 units |
| `execution/utils/youtube_auth.py` | API key + OAuth handler | 0 units |

## Quality Gates

Every sub-skill output MUST pass these checks before delivery:

1. **Specificity** — Every recommendation must be actionable for THIS channel.
   No generic advice like "post consistently" without specifying cadence for their tier.
2. **Data grounding** — Every benchmark cited must come from a reference file.
   Never hallucinate statistics. If unsure, say "benchmark unavailable" and explain.
3. **Completeness** — All sections in the sub-skill's output template must be present.
   Missing sections = incomplete deliverable.

## Self-Anneal Loop

If a sub-skill output fails a quality gate:
1. Identify which gate failed and why
2. Re-read the relevant reference file for missing data
3. Re-generate only the failing sections
4. Re-check all three gates
5. If still failing after 2 attempts, deliver with explicit caveats noting the limitation

## Output Format

Default to markdown. For `metadata` sub-skill, produce copy-paste-ready plain text blocks.
For `calendar`, produce a markdown table. For `audit`, produce a structured report with
scores. Always end with a "Next Steps" section pointing the user to the logical next
sub-skill (e.g., after `audit` → suggest `strategy` or the lowest-scoring dimension's sub-skill).
