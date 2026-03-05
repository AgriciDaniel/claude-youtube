# YouTube Analytics Guide

## Table of Contents

1. [Metrics Hierarchy](#metrics-hierarchy)
2. [Vanity Metrics to Ignore](#vanity-metrics-to-ignore)
3. [Impressions Funnel](#impressions-funnel)
4. [Traffic Source Health](#traffic-source-health)
5. [RPM vs CPM](#rpm-vs-cpm)
6. [CPM Ranges by Niche](#cpm-ranges-by-niche)
7. [RPM Ranges by Niche](#rpm-ranges-by-niche)
8. [Geographic & Seasonal Factors](#geographic--seasonal-factors)
9. [Channel Health Indicators](#channel-health-indicators)
10. [YouTube Analytics API](#youtube-analytics-api)
11. [YouTube Reporting API](#youtube-reporting-api)
12. [Key Constraints & Gotchas](#key-constraints--gotchas)

---

## Metrics Hierarchy

| Priority | Metric | Impact |
|----------|--------|--------|
| 1 | Watch time | Most influential overall signal |
| 2 | CTR | ~**80%** of initial distribution decisions |
| 3 | AVD (Average View Duration) | **50%+ = 3x more likely** to be recommended |
| 4 | Traffic sources | Distribution health indicator |
| 5 | Subscribers gained per video | Long-term channel value signal |

## Vanity Metrics to Ignore

- **Subscriber count in isolation** -- PewDiePie: 110M subs, ~2.2M typical views
- **Total views without retention context**
- **Likes in isolation**

## Impressions Funnel

| Phase | CTR Range | Meaning |
|-------|-----------|---------|
| Launch (warm audience) | **12%+** | Normal for initial push |
| Expansion | Natural drop | Impressions scaling to cold audience |
| Sustained healthy | **4-8%** | Stable performance |

### Diagnostic Matrix

| Impressions | CTR | Diagnosis |
|-------------|-----|-----------|
| High | Low | Thumbnail/title problem |
| High | High + Low AVD | Clickbait signal |
| Low | High | Limited reach, content too niche |

## Traffic Source Health

| Pattern | Interpretation |
|---------|---------------|
| Balanced Suggested + Search | Healthy channel |
| Suggested growing faster than Search | Strong retention signals |
| External dominant | Over-reliant on off-platform promotion |
| Search dominant + low Suggested | Good SEO but content not engaging enough |

## RPM vs CPM

| Metric | Definition |
|--------|-----------|
| **CPM** | Advertiser pays per 1K **ad impressions** (before YouTube cut) |
| **RPM** | Creator earns per 1K **total views** (after YouTube 45% cut, all revenue sources) |

- RPM is **always lower** than CPM
- Videos **>8 min** with mid-roll ads = RPM roughly **doubles**

## CPM Ranges by Niche

`[2025]` Advertiser cost per 1K ad impressions:

| Niche | CPM Range |
|-------|-----------|
| Finance / Investing | $12-$16 |
| Tech / SaaS | $8-$14 |
| Business / Education | $5-$12 |
| Health | $4-$8 |
| Gaming | $1-$4 |

## RPM Ranges by Niche

`[2025]` Creator earnings per 1K total views (US audience):

### Tier 1 (High Value)

| Niche | RPM |
|-------|-----|
| Personal Finance | $20-$40+ |
| Legal / Real Estate | $20-$35 |
| Business / Entrepreneurship | $15-$30 |
| Tech / Software | $15-$25 |
| Digital Marketing | $12-$25 |

### Tier 2 (Mid Value)

| Niche | RPM |
|-------|-----|
| Health / Fitness | $8-$15 |
| Education | $8-$15 |
| DIY | $8-$14 |
| Food / Cooking | $6-$12 |
| Travel | $6-$12 |

### Tier 3 (Lower Value)

| Niche | RPM |
|-------|-----|
| Beauty | $5-$8 |
| Gaming | $2-$5 (median US $3.50) |
| Entertainment | $2-$5 |
| Lifestyle | $3-$6 |
| Music | $1-$3 |

## Geographic & Seasonal Factors

- **US viewers 5-8x more valuable** than SE Asian viewers
- Finance RPM: USA $15-$25 vs India $0.50-$1.50
- **Q4 (Oct-Dec)**: CPMs **30-60% higher**
- **January**: cheapest CPMs of the year

## Channel Health Indicators

### Healthy Channel

| Metric | Target |
|--------|--------|
| CTR | 4-8% |
| Retention | Above 40% (ahead of **83% of channels**) |
| Sub growth | Steady increase |
| Traffic sources | Balanced mix |
| Viewer ratio | Good new:returning balance |

### Struggling Channel

| Signal | Threshold |
|--------|-----------|
| CTR | Below 3% |
| View duration | Dropped **40%+** |
| Source reliance | **80%+** from single source |
| Schedule | Inconsistent uploads |

- JI Digital 20-point audit: channels scoring **76+** grow subs **3.2x faster** than those below 50

## YouTube Analytics API

### Queryable Metrics

- `views`, `engagedViews`, `estimatedMinutesWatched`, `averageViewDuration`
- `estimatedRevenue`, `estimatedAdRevenue`, `grossRevenue`, `CPM`
- `likes`, `dislikes`, `comments`, `shares`
- `subscribersGained`, `subscribersLost`
- `cardClickRate`, `playlistViews`, `playlistStarts`

**`engagedViews`** `[2025]`: Official metric since April 2025. For long-form, equals `views`. For Shorts, captures the pre-March 2025 view counting (minimum watch time required). Use `engagedViews` for accurate Shorts performance comparison across the view counting change.

### Available Dimensions

- **Time**: `day`, `month`
- **Geography**: `country`, `province`, `city`
- **Demographics**: `ageGroup`, `gender`
- **Device**: `deviceType`, `operatingSystem`
- **Source**: `insightTrafficSourceType`
- **Content**: `video`, `playlist`, `liveOrOnDemand`, `subscribedStatus`

### Limits

- Max **200 results** per query
- Groups up to **500 videos**

## YouTube Reporting API

- Bulk CSV exports
- **24-hour** granularity
- **60-day** data availability window
- `channel_reach_basic_a1` report: thumbnail impressions and CTR

---

## Key Constraints & Gotchas

- CTR naturally drops as impressions expand -- a declining CTR is not always bad
- AVD at 50%+ is the threshold for 3x recommendation likelihood
- RPM is always lower than CPM; never confuse the two in calculations
- Videos under 8 min cannot have mid-roll ads, roughly halving RPM potential
- US viewers are 5-8x more valuable than SE Asian -- audience geography dominates revenue
- Q4 CPM spikes 30-60%; plan high-value content for Oct-Dec
- Analytics API caps at 200 results per query; paginate for large datasets
- Reporting API data only available for 60 days; export regularly
- Subscriber count is a vanity metric without per-video view context
- 80%+ traffic from a single source indicates dangerous channel fragility
