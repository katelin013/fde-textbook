# Ch1 How an LLM Actually Works

## **Chapter Goals**

By the end of this chapter you'll be able to:<br>
(1) Explain, in plain language, how an LLM works and what its built-in limitations are, to a customer;<br>
(2) Read an API bill and know how to keep costs down;<br>
(3) Clearly explain what the built-in limitations of LLMs are, and the corresponding engineering countermeasures.<br>

---

## **1.1 Start With a Metaphor: A Ridiculously Good Word-Chaining Machine**

At its core, an LLM is a "word-chaining machine": you give it a stretch of text, it predicts "what the next word is most likely to be," writes it out, then predicts the one after that, and keeps chaining along. It has read an enormous amount of text from across the internet, so it chains extremely well—so well that it can write code, reason, and hold a conversation.

This metaphor immediately explains three things:

1. **What it outputs is "the most likely continuation," not "a verified fact"**—which is why hallucinations happen: it states something false with a completely straight face. It isn't lying to you; it's just chaining words.
2. **It has no "database"**—its knowledge is compressed into the model's parameters: fuzzy, non-updatable, and impossible to cite a source for. If you want it to use your company's data, you have to feed that data to it yourself (that's exactly what RAG, in Chapter 3, is about).
3. **Every time, it starts the chain fresh**—the model itself has no memory. "It remembers our conversation" is an illusion: the application re-stuffs the conversation history back into it every single time.

> The version you tell a customer: "AI is like a consultant who has read every document in the world and has an astonishing memory but never checks anything. Our engineering job is to set that consultant up with a database, a verification process, and a permissions system."

## 1.2 Token: The Unit of Measurement in the Model's World

The model doesn't process text one character at a time—it processes it one **token** at a time. A token is a "common string fragment": in English, roughly 4 characters per token; in Chinese, roughly 1–2 tokens per character.

Why do you have to care about tokens? Because three things in the LLM world are all measured in them:

| Thing | Measured in tokens | What it means in practice |
|---|---|---|
| **Cost** | input / output priced separately | output is usually several times more expensive. Rambling output = burning money |
| **Capacity** | the Context Window limit | if it won't fit, you have to trim or summarize |
| **Speed** | generated token by token | asking for short output = faster replies |

## 1.3 Context Window: The Model's Working Memory

The **Context Window** is the upper limit on the total number of tokens the model can "see" in a single pass—including everything you give it (the system prompt, conversation history, documents) plus the reply it's about to generate.

Think of it as a **desk surface**: the desk is big (modern models range from a hundred thousand to a million tokens), but it's still finite. Anything that won't fit on the desk, the model simply cannot see—no matter how important that document is.

Three practical takeaways:

1. **Long conversations "forget"**: once the history exceeds the window, the earliest content gets trimmed away. Fixes: compress with a summary, or store the key points externally and retrieve them back when needed.
2. **"Just dump all the company's documents in" doesn't work**: too much volume, too expensive, and—
3. **Lost in the middle**: even if it all fits, the model pays weaker attention to content in the "middle" of the window, so putting the important stuff at the beginning and the end works best. The more noise you stuff in, the more easily the key information gets diluted. **"Stuff in more" does not equal "answer better"; giving the right small amount beats giving everything**—this is the core philosophy of RAG, covered in detail in Chapter 3.
4. Running /clear at the right moment, once you've wrapped up a stage of a task, often actually makes whatever comes next go more smoothly and finish faster.

## 1.4 Temperature: The Knob That Controls Randomness

When the model predicts the next token, what it actually computes is a probability distribution ("的" 40%, "了" 20%, "呢" 5%…). **Temperature** controls how it picks from that distribution:

- **Low (0–0.3)**: almost always picks the highest-probability option → stable, reproducible output. Used for: classification, extraction, code, enterprise workflows—**95% of an FDE's day-to-day scenarios**.
- **High (0.7 and up)**: allows lower-probability options to be picked → diverse, creative, but unstable. Used for: copywriting ideation, brainstorming.

> Common misconception: temperature 0 does not mean "smarter" or "never wrong"—it only means "the same input gives the same output." A wrong answer will be wrong just as consistently.

## 1.5 Streaming and Latency

The model generates token by token, so it can **stream as it generates** (streaming). The key user-experience metric is **TTFT (time to first token)**—how long the user waits before seeing the first character. An experience with a total generation time of 10 seconds but a TTFT of 0.5 seconds is far better than one that finishes in 5 seconds total but leaves the user staring at a blank screen for all 5.

Latency-optimization checklist for enterprise scenarios: a smaller model → streaming → a leaner prompt → caching → parallelizing the upfront steps (such as retrieval).

## 1.6 The Cost Model and Prompt Caching

API pricing: **input tokens and output tokens are counted separately, and output costs several times more**.

**Prompt Caching**: if the beginning of every request is identical (the same system prompt, the same batch of documents), the provider can cache that "already-read prefix" so it doesn't have to reprocess it next time—cost drops sharply and speed goes up. When you design a prompt, putting "the fixed, unchanging parts up front and the parts that change every time at the back" is precisely how you get to benefit from the cache.

A master list of cost-optimization tactics (expanded further in Chapter 9):

1. Model tiering—use a cheap small model for simple tasks, and only reach for the flagship on hard ones
2. Prompt Caching—a fixed prefix
3. Control output length—if you want JSON, don't let it write prose
4. Batch API—run non-urgent work in batches, usually at half price
5. Cache repeated questions—don't ask the same question twice

## 1.7 The Built-in Limitations, All in One Place

When you're asked "What are the limitations of LLMs," answer with this structure, pairing every limitation with a countermeasure:

| Limitation | Cause | Engineering countermeasure |
|---|---|---|
| **Hallucination** | the probabilistic nature of word-chaining; no verification | RAG + citing sources + evals (AI's evaluation mechanism) + a human-review gate |
| **Stale knowledge** | training has a cutoff date | RAG / tools (search, query a DB) |
| **Can't actually do math** | a language model isn't a calculator | give it a calculation tool (tool use) |
| **Limited window + loses focus in the middle** | an architectural constraint | retrieve curated content instead of force-feeding | 
| **Unstable output** | probabilistic generation | low temperature + Structured Output + validate-and-retry |
| **Can't distinguish instructions from data** | it's all just text | a permission-layer defense (Chapter 8) |

> In one line: "Every limitation of an LLM has a mature engineering countermeasure—so the bottleneck for enterprises adopting AI was never that the model isn't smart enough, but that the surrounding engineering isn't fully built out. This is exactly why FDEs exist."

---

## Common Misconceptions

1. **"The model looks things up online"**—it doesn't, unless you explicitly give it a search tool. On its own, it only has the knowledge from when it was trained. (Editor's note: adding a Skill, such as claude-in-chrome, does let it look things up online—but it won't necessarily do so every time, so if you need it, it's best to say so in the Prompt.)
2. **"It remembers what we talked about last time"**—it doesn't. The application re-feeds the history. This also means: **it knows whatever you feed it, and it doesn't know what you don't feed it**—so the first thing to do when debugging an AI application is always "look at what it actually received." (Editor's note: even within the same Session, memory problems can arise because the Context gets too long and causes confusion.)
3. **"It sounds so confident, it must be right"**—a confident tone is a writing style, not an indicator of trustworthiness. The most dangerous thing about a hallucination is precisely how fluent and confident it is—this is what people mean by an AI that talks nonsense with a completely straight face.
4. **"Just switch to a bigger model and it's solved"**—a bigger model lowers the hallucination rate but doesn't zero it out; a system without RAG and evals is unreliable no matter which model you swap in.

## Self-Check

1. Use a metaphor to explain to a completely non-technical customer "why AI states falsehoods with a straight face," and state your engineering countermeasure.
2. A customer complains that "AI replies too slowly"—list your latency diagnosis and optimization order.
3. What is prompt caching? How should you design a prompt to work with it?
4. Why is "stuffing all your documents into the context" a bad idea? (Cover all three points: cost, window, lost in the middle.)
5. Once you set temperature to 0, is the output guaranteed to be correct? Why?

##  Key Points for the Reference Answers

    1. The word-chaining machine / never-verifying consultant metaphor; countermeasure = RAG + citations + evals.
    2. Measure first (TTFT vs. total time) → streaming → model tiering → leaner prompt → caching → parallelize retrieval.
    3. The processing result of the fixed prefix gets cached; put fixed content up front and changing content at the back.
    4. Expensive (token-based billing), won't fit (window limit), and even if it fits it loses focus (lost in the middle); giving the right small amount beats giving everything.
    5. No guarantee. It only guarantees reproducibility—same input, same output; a wrong answer stays consistently wrong. Correctness is verified through evals.
