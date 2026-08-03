# Feature 22 — Sentiment Analysis of Reviews

> **Priority**: P3 (low) · **Effort**: S (3–4 days with local HF transformers) ·
> **Source**: AI/ML research, marked "weekend polish" feature.
> **One-line**: Weekly digest of Google / TripAdvisor reviews, summarized by
> themes (service, food, ambiance, value) with new-negative-review alerts.

## Goal

The owner / manager gets a Monday-morning Telegram digest of the past week's
reviews, with:
- Overall sentiment trend
- Top positive themes ("salad praised", "great atmosphere")
- Top negative themes ("slow service on weekends", "noisy on Fridays")
- An alert whenever a new 1- or 2-star review lands

## Scope

**In scope (v1 of this feature):**
- Pull reviews weekly from Google Places API (official, paid) or via a
  configured local file (paste reviews manually for testing).
- Local sentiment classifier (HuggingFace `distilbert-base-uncased-finetuned-sst-2-english`).
- Zero-shot topic classification into 4 categories: `food`, `service`, `ambiance`, `value`.
- Weekly Telegram digest (default Monday 9am).
- New-review alert when rating ≤ 2 stars.

**Out of scope:**
- Auto-reply to reviews (Google ToS forbids automated responses).
- Scraping TripAdvisor / Yelp (legally gray; skip).
- Multi-language reviews (English only in v1).

## Description

A weekly background job:
1. Fetch new reviews via Google Places API (or accept a manually-pasted CSV).
2. Run each review through the local sentiment model.
3. Run zero-shot topic classification against `food / service / ambiance / value`.
4. Aggregate per-theme sentiment.
5. Send a Telegram digest to the manager.

An alert fires for any new review with rating ≤ 2.

## Data model

```
Review
  id              PK
  source          TEXT     ('google', 'tripadvisor', 'manual')
  external_id     TEXT     (e.g. Google review ID)
  author_name     TEXT
  rating          INT      (1-5)
  text            TEXT
  language        TEXT     ('en', 'fr', ...)
  fetched_at      DATETIME

ReviewSentiment
  review_id       FK
  sentiment       Enum (positive | neutral | negative)
  confidence      Decimal  (0-1)
  model_version   TEXT     ('distilbert-sst2-v1')

ReviewTopic
  id              PK
  review_id       FK
  topic           Enum (food | service | ambiance | value)
  confidence      Decimal
```

## Implementation

1. **Google Places API** integration — `googlemaps` Python client; poll daily
   for new reviews on the configured `place_id`. Cost: ~$32 per 1000 calls;
   for 50-200 reviews/month, < $10/month.
2. **Local transformer** — `transformers` + `distilbert-base-uncased-finetuned-sst-2-english` (~250 MB).
3. **Zero-shot topic** — `facebook/bart-large-mnli` for the 4 topics.
4. **Weekly job** (`backend/app/services/review_digest.py`): Sunday 23:00 fetch +
   classify + write to DB.
5. **Telegram alerts** — on insert of rating ≤ 2.
6. **Telegram digest** — Monday 9am, formatted summary.

## Telegram interactions

### Weekly digest

```
Bot (Monday 9am): 📊 Weekly review digest (15-21 Jul)

       14 new reviews · avg ★★★★.2

       By topic:
         food      ★★★★.7   "great schnitzel", "fresh salads"
         service   ★★★.5   "friendly waiters", "slow on Sat night"
         ambiance  ★★★★.6   "cozy", "a bit noisy on Fri"
         value     ★★★.9   "fair for the area"

       Trend vs last week: ⬆ +0.3 stars overall
       Top complaint: "slow service when busy"
       Top praise: "tiramisu is the best in the neighborhood"

       [View all reviews] [Set quiet hours]
```

### New negative review alert

```
Bot (real-time): ⚠ New 1-star review on Google:

       "Waited 40 min for a burger. Cold fries. Won't come back."

       Sentiment: negative (0.96)
       Topics: food (0.71), service (0.83)

       [Mark as handled] [Add to follow-up] [Open full review]
```

## Library options

| Library | Stars | Use |
|---|---|---|
| **huggingface/transformers** | 163k | Run local sentiment + zero-shot |
| **explosion/spaCy** | 33.8k | NER + custom rules for restaurant topics |
| **googlemaps/google-maps-services-python** | — | Official Google Places API client |
| **distilbert-base-uncased-finetuned-sst-2-english** | — | Sentiment, ~250 MB |
| **facebook/bart-large-mnli** | — | Zero-shot topic classification |

**Recommended start**: DistilBERT sentiment + spaCy NER (3 days). **Upgrade**: add zero-shot BART (1 more day).

## Cost

- **Local model**: free, ~250 MB disk + 1 GB RAM when running.
- **Google Places API**: ~$32/1000 calls. For a small restaurant with 50-200 reviews/month, ~$5-15/month.
- **Avoid scraping** TripAdvisor / Yelp — ToS risk is real (the AI/ML research flagged this).

## Dependencies

- New: `transformers`, `torch` (CPU-only is fine), `googlemaps` (optional).

## Open questions

- Do we need multi-language support? (Most restaurants in tourist areas do.
  Default: English + French via multilingual DistilBERT.)
- Should the cook see the digest, or only the manager? (Default: manager only.)
- Should we support an "ignore" / "hide" flag for known troll reviews? (Default: yes.)
- How long to retain reviews? (Default: 2 years, then aggregate.)

## Why this matters

The AI/ML research marked this the "weekend polish" feature — easy to ship,
high goodwill value, but not core to restaurant operations. Useful because:
- New-negative-review alerts let the owner respond fast (turn a 1-star into a comeback story).
- Weekly themes give the manager unfiltered guest voice ("we keep hearing about slow service on Saturdays").
- Zero privacy risk (reviews are public).
- Local inference = no API cost.

**Defer** until other AI features ship — sentiment is a nice-to-have, not a must-have.