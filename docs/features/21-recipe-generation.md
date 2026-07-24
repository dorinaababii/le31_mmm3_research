# Feature 21 — Recipe Generation from Leftovers

> **Priority**: P2 · **Effort**: S (2–4 days with local LLM) · **Source**: AI/ML
> research, ranked **#3 of 8** for "ship first for a small restaurant".
> **One-line**: Chef types "/recipe chicken, tomatoes, basil" → AI suggests
> a dish that uses exactly those ingredients, with steps, plate cost, and
> suggested menu price.

## Why this matters

The chef has **leftover ingredients** at end of shift — half a chicken, wilted
basil, ripe tomatoes. Throwing them away is waste (5-10% of food cost per
feature 20). Turning them into a "chef's special" tomorrow is pure upside.

The AI/ML subagent flagged this as the **strongest "wow demo per engineering
hour"** — it's the most magical AI feature for the cook, and combines well
with waste prediction (use leftovers → reduce waste → feed into tomorrow's menu).

## Goal

Given a list of available ingredients (with quantities), the system proposes
2-3 plausible dishes, each with:
- Title and short description
- Ingredient list (using the available items, marking missing ones)
- Brief preparation steps
- Estimated plate cost
- Suggested menu price

The chef reviews, edits, and either accepts (adds to tomorrow's menu) or
discards.

## Scope

**In scope (v1 of this feature):**
- Cook runs `/recipe <comma-separated ingredients>` in Telegram.
- System retrieves ~20 of the chef's existing recipes as in-context examples.
- Local LLM (Qwen2.5-3B-Instruct or Llama-3.1-8B via Ollama) generates 3
  recipe candidates.
- Each candidate marked with:
  - "uses ingredients you have" vs "needs additional ingredients"
  - confidence / coverage score
- Cook taps `[✓ Add to tomorrow's menu]` or `[✎ Edit]` or `[✗ Reject]`.

**Out of scope:**
- Image generation of the dish.
- Nutrition / allergen auto-tagging (handled by feature 10).
- Auto-add to POS without chef review.
- Voice input.

## Description

The LLM is given a system prompt:

```
You are a chef's assistant. The chef has these ingredients on hand:
{ingredients}

Here are some of the chef's existing recipes for style reference:
{retrieved_examples}

Suggest 3 dishes the chef could make. For each:
- title (short)
- description (1 sentence)
- ingredients_used (subset of what's on hand + any extras)
- steps (numbered, brief)
- estimated_plate_cost
- suggested_menu_price

Respond as JSON.
```

The output is parsed and presented as inline buttons. On accept, the recipe
is stored and offered as a "chef's special" for tomorrow's menu.

## Implementation

1. **Add `Recipe` table** (already in feature 10 spec) — title, description,
   ingredients, steps, plate_cost, menu_price.
2. **Local LLM**: install Ollama (`ollama pull qwen2.5:3b`) or run llama.cpp
   on the FastAPI host. ~4 GB RAM.
3. **Retrieval**: use `sentence-transformers/all-MiniLM-L6-v2` to embed the
   chef's existing recipes; retrieve top-k by ingredient overlap.
4. **Bot command** `/recipe <ingredients>` in `cook_bot.py`.
5. **Review flow**: inline buttons for accept / edit / reject.

## Telegram interaction

```
Cook: /recipe chicken thigh, tomatoes, basil, mozzarella, pasta
Bot:  Here are 3 dishes using what you have:

      1. 🍝 Caprese Chicken Pasta       (confidence 87%)
         Pan-seared chicken thigh over pasta with tomato-basil-mozza.
         Ingredients used: chicken ✓, tomatoes ✓, basil ✓, mozzarella ✓, pasta ✓
         Plate cost: ~€3.20   Suggested price: €12.50

      2. 🍅 Bruschetta Chicken          (confidence 72%)
         Grilled chicken on tomato-basil toast.
         Ingredients used: chicken ✓, tomatoes ✓, basil ✓, mozzarella ✓
         Missing: bread (€0.40)
         Plate cost: ~€3.60   Suggested price: €11.00

      3. 🥗 Tuscan Chicken Salad       (confidence 65%)
         Cold chicken with tomato-mozza-basil.
         Plate cost: ~€3.40   Suggested price: €10.00

      [✓ Add #1 to tomorrow's menu]
      [✎ Edit #1]   [✎ Edit #2]   [✎ Edit #3]
      [🔄 Regenerate]   [✗ Reject all]
```

Cook taps "✓ Add #1" → Bot: "Done. Added as 'Caprese Chicken Pasta' for tomorrow.
The OCR pipeline will pick it up if you include it in tomorrow's menu photo."

## Library options

| Library | Stars | Use |
|---|---|---|
| **huggingface/transformers** | 163k | Run any local LLM, T5-small/baseline |
| **ollama/ollama** | 130k+ | Easy local model runner; `ollama pull qwen2.5:3b` |
| **ggerganov/llama.cpp** | 80k+ | CPU-efficient inference |
| **UKPLab/sentence-transformers** | 17k | Embeddings for recipe retrieval |
| **Recipe1M+** dataset | — | 1M recipes for fine-tuning (if needed) |

**Recommended start**: Ollama + `qwen2.5:3b` (3-4 days including retrieval setup).
**Recommended upgrade**: fine-tune T5-small on chef's own 50+ recipes (10-15 days).

## Cost & resources

- **Local LLM**: ~4 GB RAM (Qwen2.5-3B with 4-bit quantization) or ~16 GB (Llama-3.1-8B).
- **No API cost** — fully on-prem.
- **Latency**: ~5-15 seconds per `/recipe` call. Acceptable for an end-of-shift cook.
- **Privacy**: 100% local — chef's ingredient lists never leave the device.

## Dependencies

- [10-allergen-tracking.md](10-allergen-tracking.md) — `Ingredient` + `Recipe` tables.
- Optional: Ollama or llama.cpp installed on the host.

## Open questions

- Should we use the chef's existing recipes as in-context examples, or only
  the public Recipe1M+ corpus? (Default: chef's own first.)
- How many examples to retrieve? (Default: 5.)
- Should generated recipes be marked as "AI-suggested, needs chef review"?
  (Yes — always; never auto-add to POS.)
- Should we store failed generations for fine-tuning later? (Yes — `Recipe.rejected_at`
  + a separate `RecipeDraft` table.)

## Why this matters

The AI/ML research ranked this **#3 of 8** to ship first because:
- 2-4 days with a local LLM, no API cost.
- Strong "wow" demo for the chef.
- Compounds with feature 20 (waste prediction) — predicted leftovers → AI recipe → tomorrow's menu.
- Strong differentiator vs Toast/Square/Resy (none of them have this).
- Zero privacy risk (all on-prem).

Per the AI/ML note: *"Strongest 'wow' demo per engineering hour."*

## Caveat

LLM-generated recipes can invent techniques that don't actually work.
**Always require chef review before adding to the menu.** Display confidence
+ ingredient coverage; reject recipes with missing key ingredients unless
the chef overrides.