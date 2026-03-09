# Claude YouTube — YouTube Creator Skill

## Project Overview

This repository contains **Claude YouTube**, a Claude Code skill for YouTube creators.
It covers channel audits, video SEO, retention-engineered scripts, hook writing, thumbnail
briefs, content strategy, Shorts optimization, analytics, monetization, competitor research,
and cross-platform repurposing. 14 sub-skills, 9 reference guides, 9 channel templates,
and 6 execution scripts.

## Architecture

```
claude-youtube/
  CLAUDE.md                          # Project instructions (this file)
  skills/claude-youtube/             # Main skill (single skill, not orchestrator)
    SKILL.md                         # Entry point, routing, core rules
    sub-skills/                      # 14 sub-skill instruction files (.md)
      audit.md, seo.md, script.md, hook.md, thumbnail.md,
      strategy.md, calendar.md, shorts.md, analyze.md,
      repurpose.md, monetize.md, competitor.md, metadata.md, ideate.md
    references/                      # 9 on-demand knowledge guides
    templates/                       # 9 channel type templates
    execution/                       # 6 Python scripts
      fetch_channel_data.py         # YouTube Data API v3 channel stats
      fetch_transcript.py           # Video transcript extraction
      fetch_video_analytics.py      # Analytics data retrieval
      search_competitor_videos.py   # Competitor video search
      utils/                        # Shared Python utilities
```

## Commands

| Command | Purpose |
|---------|---------|
| `/youtube audit` | Full channel health audit (4 dimensions) |
| `/youtube seo` | Video SEO package (titles, description, tags, schema) |
| `/youtube script` | Retention-engineered script with pattern interrupts |
| `/youtube hook` | 5 hook variants with drop-off risk ratings |
| `/youtube thumbnail` | Thumbnail brief with 3 A/B variants |
| `/youtube strategy` | Channel positioning and 30/60/90-day milestones |
| `/youtube calendar` | Monthly content calendar with Shorts plan |
| `/youtube shorts` | Shorts production package |
| `/youtube analyze` | Analytics interpretation and priority actions |
| `/youtube repurpose` | Cross-platform content package |
| `/youtube monetize` | Revenue strategy across 7 streams |
| `/youtube competitor` | Competitor analysis with parallel agents |
| `/youtube metadata` | Copy-paste-ready upload package |
| `/youtube ideate` | 10 ranked video ideas with keyword analysis |

## Development Rules

- Keep SKILL.md under 500 lines
- Sub-skills are instruction files in `sub-skills/`, not separate SKILL.md directories
- Reference files should be focused and under 200 lines
- Python scripts in `execution/` must have docstrings and CLI interface
- Follow kebab-case naming for directories
