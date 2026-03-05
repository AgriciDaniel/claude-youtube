# claude-youtube

> **Status: Beta** -- Actively developed. Core functionality is complete and tested. Breaking changes may occur before v1.0.

A comprehensive [Claude Code](https://claude.com/claude-code) skill for YouTube creators. Covers channel audits, video SEO, retention-engineered scripts, hook writing, thumbnail briefs, content strategy, content calendars, Shorts optimization, analytics interpretation, monetization planning, competitor research, cross-platform repurposing, upload metadata packages, and data-driven video idea generation.

**39 files** | **5,300+ lines of markdown** | **1,300+ lines of Python** | **14 sub-skills** | **9 reference guides** | **9 channel templates** | **6 execution scripts**

---

## What It Does

claude-youtube turns Claude Code into a YouTube growth consultant. Instead of generic advice, every recommendation is grounded in platform-specific benchmarks, algorithm mechanics, and data from your actual channel.

### 14 Commands

| Command | What It Does |
|---------|-------------|
| `/youtube audit` | Full channel health audit across 4 dimensions (SEO, performance, content, monetization) with parallel agents |
| `/youtube seo` | Video SEO package: 3 title variants, full description, tags, chapters, hashtags, VideoObject schema |
| `/youtube script` | Retention-engineered script with hook/intro/content blocks, pattern interrupts every 60-90s, and CTA placement |
| `/youtube hook` | 5 hook variants (shock, problem-agitation, story, curiosity-gap, social proof) with drop-off risk ratings |
| `/youtube thumbnail` | Thumbnail brief with 3 A/B variants, color hex codes, composition specs, and title-thumbnail synergy check |
| `/youtube strategy` | Channel positioning, content pillars (Hub/Hero/Help), niche viability, upload cadence, 30/60/90-day milestones |
| `/youtube calendar` | Monthly content calendar with per-video metadata, Shorts supplement plan, and seasonal CPM timing |
| `/youtube shorts` | Shorts production package: script with visual change markers, SEO metadata, performance prediction, loop setup |
| `/youtube analyze` | Analytics interpretation: funnel diagnosis, retention graph classification, traffic source health, priority actions |
| `/youtube repurpose` | Cross-platform package: Shorts clips, blog outline, LinkedIn post, X thread, email, podcast outline, community post |
| `/youtube monetize` | Revenue strategy across 7 streams, brand deal rate card, external funnel design, 90-day activation plan |
| `/youtube competitor` | Competitor analysis with 4 parallel agents: top videos, keyword gaps, format gaps, audience gaps |
| `/youtube metadata` | Copy-paste-ready upload package: titles, description, tags, chapters, cards, end screens, publish settings |
| `/youtube ideate` | 10 ranked video ideas with keyword analysis, hook angles, thumbnail concepts, and revenue potential |

---

## Architecture

Built on the [Agent Skills](https://github.com/anthropics/claude-code) open standard with a 3-layer architecture:

```
skills/claude-youtube/
  SKILL.md                          # Orchestrator (routing, context-gathering, quality gates)
  sub-skills/                       # 14 sub-skill instruction files
    audit.md, seo.md, script.md, hook.md, thumbnail.md,
    strategy.md, calendar.md, shorts.md, analyze.md,
    repurpose.md, monetize.md, competitor.md, metadata.md, ideate.md
  references/                       # 9 data-grounded reference guides
    algorithm-guide.md              # 3-system architecture, testing cascade, CTR/AVD benchmarks
    seo-playbook.md                 # Title/description/tags/chapters rules, VideoObject schema
    retention-scripting-guide.md    # Hook frameworks, pattern interrupts, CTA placement
    thumbnail-ctr-guide.md          # CTR by niche, face psychology, A/B testing, title formulas
    shorts-playbook.md              # Shorts algorithm, format specs, monetization
    analytics-guide.md              # Metrics hierarchy, funnel ratios, RPM/CPM by niche
    monetization-guide.md           # YPP tiers, 7 revenue streams, brand deal rates
    repurposing-guide.md            # Hub/Hero/Help model, cross-platform workflows
    dataforseo-integration.md       # DataForSEO MCP tool reference for live data
  templates/                        # 9 channel-type templates
    education-channel.md, entertainment-channel.md, tutorial-channel.md,
    vlog-channel.md, review-channel.md, commentary-channel.md,
    niche-authority-channel.md, personal-brand-channel.md, shorts-first-channel.md
  execution/                        # 6 Python scripts for YouTube API integration
    fetch_channel_data.py           # Channel stats + recent videos (~16 quota units)
    fetch_video_analytics.py        # Private analytics via OAuth
    search_competitor_videos.py     # Competitor video search (100 units/search)
    fetch_transcript.py             # Transcript extraction via yt-dlp
    utils/quota_tracker.py          # 10K unit/day quota management
    utils/youtube_auth.py           # API key + OAuth 2.0 handler
```

### How It Works

1. **Orchestrator** (`SKILL.md`) routes your request to the right sub-skill based on trigger phrases
2. **Context-gathering** collects channel niche, size tier, and primary goal before any sub-skill runs
3. **Channel type detection** loads the matching template (education, entertainment, tutorial, etc.) for niche-specific benchmarks
4. **Sub-skills** load only the reference files they need, execute step-by-step, and produce structured output
5. **Quality gates** verify specificity, data grounding, and completeness before delivery

---

## Installation

### Prerequisites

- [Claude Code](https://claude.com/claude-code) CLI installed and configured

### Quick Install

Clone this repo into your Claude Code skills directory:

```bash
git clone https://github.com/AgriciDaniel/claude-youtube.git
cp -r claude-youtube/skills/claude-youtube ~/.claude/skills/claude-youtube
```

Or symlink for development:

```bash
git clone https://github.com/AgriciDaniel/claude-youtube.git ~/claude-youtube
ln -s ~/claude-youtube/skills/claude-youtube ~/.claude/skills/claude-youtube
```

### Optional: YouTube API (for live channel data)

The skill works without API credentials by accepting manual data input. For automated data fetching:

1. Get a YouTube Data API v3 key from [Google Cloud Console](https://console.cloud.google.com/apis/library/youtube.googleapis.com)
2. Set the environment variable:
   ```bash
   export YOUTUBE_API_KEY="your-api-key-here"
   ```
3. For private analytics (own channel), set up OAuth 2.0 credentials

### Optional: DataForSEO MCP (for live keyword/trend data)

When configured, the skill uses live data for keyword research, YouTube SERP analysis, trend intelligence, and competitive research. Without it, the skill falls back to WebSearch.

Add to `~/.claude/settings.json` under `mcpServers`:

```json
{
  "dataforseo": {
    "command": "npx",
    "args": ["-y", "dataforseo-mcp-server"],
    "env": {
      "DATAFORSEO_USERNAME": "your-username",
      "DATAFORSEO_PASSWORD": "your-password",
      "ENABLED_MODULES": "SERP,KEYWORDS_DATA,DATAFORSEO_LABS,ONPAGE"
    }
  }
}
```

Typical workflow costs $0.002-$0.04 per command. See [DataForSEO pricing](https://dataforseo.com/pricing).

### Optional: NanoBanana MCP (for AI thumbnail generation)

When configured, the `/youtube thumbnail` command generates actual thumbnail images using Gemini models instead of just text briefs.

```json
{
  "nanobanana": {
    "command": "uvx",
    "args": ["nanobanana-mcp-server"],
    "env": {
      "GEMINI_API_KEY": "your-gemini-api-key"
    }
  }
}
```

---

## Usage

After installation, use any command in Claude Code:

```
> /youtube audit
> /youtube ideate
> /youtube script "How to Build a PC in 2025"
> /youtube thumbnail
> /youtube seo
```

The skill will ask for any missing context (channel niche, size, goal) before running.

### Multi-command workflows

Commands chain naturally:

```
> Help me plan and script my next video about meal prep for beginners
```

This triggers `ideate` -> `script` -> `metadata` sequentially, passing output between each step.

---

## Reference Data

All benchmarks and statistics in the reference guides are sourced and tagged:

- **CTR benchmarks by niche** -- Focus Digital, December 2025
- **Retention data** -- 10xCreator, Wistia, AIR Media-Tech
- **Algorithm mechanics** -- Retention Rabbit (150M+ minutes analyzed), vidIQ (5.08M channels)
- **Shorts algorithm** -- 35B views study, Tubefilter, Digital i
- **Monetization rates** -- YouTube Creator Academy, industry reports
- **SEO rules** -- 10xCreator (3M+ videos analyzed), Backlinko, HubSpot
- **MrBeast methodology** -- Validated at 100M+ views/video scale

Data points tagged with `[2025]` reflect 2024-2025 platform changes.

---

## Requirements

| Requirement | Required | Notes |
|-------------|----------|-------|
| Claude Code | Yes | Core dependency |
| Python 3.8+ | For execution scripts | Not needed if providing data manually |
| YouTube API key | No | Enables automated channel data fetching |
| DataForSEO MCP | No | Enables live keyword/trend data |
| NanoBanana MCP | No | Enables AI thumbnail generation |

---

## Contributing

This project is in beta. Issues, bug reports, and feature suggestions are welcome via [GitHub Issues](https://github.com/AgriciDaniel/claude-youtube/issues).

---

## License

MIT License. See [LICENSE](LICENSE) for details.
