# YouTube Algorithm Reference Guide

## Table of Contents

- [Three-System Architecture](#three-system-architecture)
- [Signal Hierarchy & Satisfaction Metrics](#signal-hierarchy--satisfaction-metrics)
- [CTR Benchmarks](#ctr-benchmarks)
- [Average View Duration (AVD)](#average-view-duration-avd)
- [Context-Adaptive Weighting](#context-adaptive-weighting)
- [Engagement Signals](#engagement-signals)
- [Upload Cadence & Growth](#upload-cadence--growth)
- [New Channel Promotion](#new-channel-promotion)
- [Algorithm Timeline 2024-2025](#algorithm-timeline-2024-2025)
- [Key Constraints & Gotchas](#key-constraints--gotchas)

---

## Three-System Architecture

YouTube operates three distinct recommendation systems, each with its own signal hierarchy:

| System | Primary Surface | Core Signals |
|--------|----------------|--------------|
| **Browse** | Home feed, Subscriptions | Personalization, satisfaction, freshness |
| **Search** | Search results | Query relevance, metadata, engagement |
| **Shorts** | Shorts feed | Completion rate, loops, freshness |

- Each system ranks and serves content independently
- A video can perform well in one system and poorly in another
- `[2025]` Beaupre (January 2025): YouTube is a "per-viewer prediction engine", satisfaction-weighted

---

## Signal Hierarchy & Satisfaction Metrics

### 4-Layer Testing Cascade

Videos are tested through progressively wider audiences:

1. **Core audience** -- Subscribers and frequent viewers
2. **Expanded** -- Similar interest profiles
3. **Broader** -- Wider demographic/topic match
4. **High authority** -- Trending/viral distribution

- Advancement to next layer depends on performance relative to predictions at each stage

### Satisfaction Signals (Ranked)

| Signal | Weight Notes |
|--------|-------------|
| **Shares** | Strongest per-action signal |
| **Repeat viewing** | Indicates high satisfaction |
| **Session continuation** | Viewer stays on platform |
| **Saves** | Bookmarking intent |
| **Surveys** | Direct satisfaction measurement |
| **Likes** | Standard positive signal |
| **Comments** | Weighted for time investment |

- **Quality Click Ratio**: Clicks that convert to satisfied viewing (not just any click)

---

## CTR Benchmarks

### CTR by Traffic Source `[2025]`

Source: Focus Digital (single-agency report), December 2025

| Traffic Source | Average CTR |
|---------------|-------------|
| Search | 12.5% |
| Suggested | 9.5% |
| Browse | 3.5% |
| External | 2.8% |

### CTR Performance Tiers

| CTR Range | Assessment |
|-----------|------------|
| Below 3% | Fix needed |
| 4-6% | Average |
| 7-10% | Good |
| 10%+ | Exceptional |

---

## Average View Duration (AVD)

Source: Retention Rabbit, 150M+ minutes analyzed

- **Average AVD**: 23.7%
- **Only 16.8%** of videos surpass 50% AVD
- **Below 40% AVD** = deprioritized by the algorithm

---

## Context-Adaptive Weighting

Watch time is weighted differently depending on device and content type:

| Context | Watch Time Weight |
|---------|------------------|
| TV / CTV | Higher |
| Mobile | Lower (relative to TV) |
| Podcasts | Higher |
| Music | Lower (relative to podcasts) |

---

## Engagement Signals

- **50+ comments replied** within 2 hours = **15-20% higher reach**
- Comment replies in the first 2 hours are critical for the testing cascade

---

## Upload Cadence & Growth

Source: vidIQ, 5.08M channels analyzed

| Cadence | Growth Impact |
|---------|---------------|
| 12+/month | 8x faster view growth, 3x subscriber growth |
| Consistency > frequency | Regular schedule beats sporadic bursts |

- **Max 3 notifications per 24 hours** -- uploads beyond this won't trigger subscriber notifications

---

## New Channel Promotion

- Channels **under 500 subscribers** receive active algorithmic promotion
- **Hype feature**: 3 votes per week per user, weighted more heavily for smaller channels
- Beta results: **5M hypes across 50K channels**

---

## Algorithm Timeline 2024-2025

| Date | Change |
|------|--------|
| Mid-2024 | Thumbnail A/B testing rollout |
| Oct 2024 | `[2025]` Shorts extended to 3 minutes |
| Jan 2025 | `[2025]` LLMs integrated into recommendations, satisfaction-weighted |
| Mar 2025 | `[2025]` Shorts view counting change (any playback = view, loops = additional views). Engaged Views metric introduced |
| Aug 2025 | `[2025]` Undocumented ~30% viewership drops reported; desktop-to-mobile shift observed |
| Oct 2025 | `[2025]` Pichai confirms Shorts earn more per watch hour than in-stream ads in US |
| Late 2025 | `[2025]` Home feed long-form reduced up to 80% (per MrBeast retention director). Shorts consuming feed real estate |
| Sep 2025 | `[2025]` Shorts freshness prioritization; Shorts older than ~28-30 days deprioritized |

---

## Core Mindset: Algorithm = Audience

Source: MrBeast methodology (validated at 100M+ views/video scale)

Whenever you hear "algorithm," replace it with "audience." The algorithm is simply
a measurement of human behavior. If people click and watch your content, YouTube
will promote it. There is no secret hack -- only understanding what your specific
audience wants and delivering it better than anyone else.

**Practical implication:** Stop optimizing for "the algorithm" and start studying
human psychology. Why do people click? Why do they leave? Why do they share?
Every decision (thumbnail, title, script, pacing) should answer these questions.

---

## Key Constraints & Gotchas

- **Browse CTR is naturally low** (3.5%) -- do not compare it against Search CTR (12.5%); they are different systems
- **AVD below 40% triggers deprioritization** -- retention is non-negotiable
- **Notification cap of 3/24h** means uploading more than 3 times daily wastes notification slots
- **Consistency beats frequency** -- irregular 12/month is worse than regular 4/month
- **Shorts older than ~28-30 days lose freshness boost** `[2025]` -- plan for front-loaded Shorts performance
- **Long-form Home feed visibility dropped up to 80%** `[2025]` -- diversify traffic sources beyond Browse
- **August 2025 viewership drops** were undocumented -- monitor analytics for unexplained dips
- **Quality Click Ratio** matters more than raw CTR -- clickbait that doesn't convert hurts ranking
- **TV/CTV watch time is weighted higher** -- optimize for lean-back viewing if targeting living room audiences
- **Comment replies are time-sensitive** -- the 2-hour window is critical for the 15-20% reach boost
