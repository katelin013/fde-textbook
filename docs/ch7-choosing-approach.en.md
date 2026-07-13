# Ch7 Choosing Your Approach: Prompting vs RAG vs Fine-tune

## Chapter Goals

By the end you'll be able to: (1) look at any requirement and quickly judge which approach fits; (2) explain to a client why "we're not using the most expensive option"; (3) nail the interview decision question "when do you fine-tune, when do you use RAG, when do you stick with pure prompting?"

---

## 7.1 What Are the Three Approaches (One-Line Version)

| Approach | In one line | What it changes |
|---|---|---|
| **Prompting** | Write your requirements and examples into the instruction manual | The model's **behavioral instructions** |
| **RAG** | Flip open the reference book during the exam | The **knowledge** available to the model |
| **Fine-tune** | Send the model off for training to change its instincts | The model's **built-in tendencies** (style / format / domain behavior) |

## 7.2 The Golden Decision Order: Cheap to Expensive

**Prompt first → RAG if that's not enough → fine-tune only as a last resort.**

The reason isn't just saving money—it's **iteration speed and maintainability**:

- Change one line in a Prompt, it takes effect a minute later, and you can ship once the regression tests pass
- Updating RAG knowledge = updating the document store, without touching the model
- Every fine-tune adjustment means re-preparing data, training, evaluating, and deploying all over again—iteration measured in "weeks"

> Interview one-liner: "**Fine-tune teaches the model *how* to say things; RAG gives the model *what* to say.** What enterprises want is usually the latter, and they need to be able to cite sources—so my default path is prompt → RAG, and fine-tune is the last resort I only reach for when there's a clear reason."

## 7.3 Breaking Down the Decision Factors One by One

**Is it about knowledge or behavior?**
- Missing **knowledge** (company documents, product data, up-to-date information) → RAG. Fine-tune does a poor job of injecting knowledge, can't cite sources, and goes stale.
- Missing **behavior** (a fixed output format, a domain tone of voice, particular terminology conventions) → try prompt + few-shot first; only if it still doesn't imitate the target well even with examples, *and* the volume is high enough that per-call cost matters → then consider fine-tune.

**Do you need source citations?**
- Yes (almost every enterprise needs this) → RAG is a must. Fine-tune can't tell you "which document this sentence came from."

**How often does the knowledge update?**
- Changes daily → RAG (edit the document and it takes effect). Fine-tune's knowledge is frozen on the day it was trained.

**How many high-quality examples do you have?**
- Fine-tune needs hundreds to thousands of high-quality "input → ideal output" pairs. Without that quantity and quality, what you train is a disaster.

**Do you care about per-call latency and cost (at scale)?**
- One legitimate reason to fine-tune: fine-tune a small model to replace a large one on a specific narrow task—at high volume it saves both money and latency. This is the "distillation" line of thinking.

## 7.4 The Real Cost of Fine-tune (The Client Only Sees the Training Bill—You Have to Explain the Whole Thing)

1. Data preparation: hundreds to thousands of labeled examples (this is actually the most expensive part)
2. Training and tuning: multiple rounds of experiments
3. **Evaluation**: you need your own eval set to prove you didn't break anything (training up ability A while degrading ability B is very common)
4. Deployment and operations: you manage the model versions yourself
5. **Redo it all on every update**: the base model got upgraded? Your fine-tune has to be redone

So here's the standard line for clients: "Fine-tune isn't a one-time purchase, it's raising a training pipeline. Unless there's a clear and ongoing reason, use prompt + RAG first to get 80% of the way there, and save the budget for evals and integration."

## 7.5 Three Real-World Scenarios (For Interview Practice)

**Scenario one: A law firm wants AI to search past case precedents and internal memos.**
→ RAG. Knowledge-heavy, frequently updated, and citations are a must. Fine-tune is completely the wrong remedy.

**Scenario two: A call center wants AI replies that perfectly match the brand's tone of voice, a hundred thousand a day.**
→ Try prompt + few-shot first (usually enough); if the tone is still unstable *and* the volume is high enough that cost matters → fine-tune a small model on high-quality historical replies. The knowledge part (product data) still pairs with RAG—**these two approaches are often a combination, not an either/or**.

**Scenario three: A manufacturer wants AI to understand its in-house abbreviations and jargon ("the QN ticket at station T3").**
→ The first step is, surprisingly, prompt: put the glossary into the System Prompt (or retrieve the glossary via RAG). Only when the vocabulary is too large to fit in the prompt do you talk about anything else. **A lot of "we need fine-tune" requirements are actually solved by a single glossary.**

---

## Common Misconceptions

1. **"Fine-tune is the most advanced, so it gives the best results"**—it's the most expensive, not the most correct. Most enterprise needs are knowledge-heavy, and RAG is the right remedy.
2. **"RAG and fine-tune are an either/or"**—they're often combined: fine-tune handles style, RAG handles knowledge, prompt handles rules.
3. **"Fine-tune can make the model memorize all of our company's documents"**—inefficient, can't cite, goes stale. Use RAG to inject knowledge.
4. **"If the prompt is too long, you should fine-tune"**—first look at Prompt Caching (a fixed prefix is nearly free), then RAG (dynamically inserting only what's needed); fine-tune is the third option.

## Self-Check

1. "When do you fine-tune, when do you use RAG, when do you stick with pure prompting?"—give the complete decision framework as a 3-minute answer.
2. A client insists "we want fine-tune, we hear it's the most powerful"—how do you respond? (You need empathy, options, and tradeoffs.)
3. Answer the three scenarios in 7.5 again without looking at the answers.
4. What are the five real costs of fine-tune?

## Key Points for Reference Answers

    1. The order (cheap → expensive) + the factors (knowledge vs behavior, citation, update frequency, example volume, cost at scale) + the one-liner.
    2. First ask about the nature of the need (do you want knowledge or style?) → show what prompt/RAG can achieve and on what timeline → the full cost of fine-tune → offer a phased plan (ship with RAG first, quantify the gap, then evaluate fine-tune).
    3-4. See 7.4 and 7.5.
