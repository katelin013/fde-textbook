# Ch2 Prompt Engineering: Turning Black Magic into Engineering

## Chapter Goals

By the end of this chapter you'll be able to:<br>(1) write stable prompts systematically instead of tuning them by gut feel;<br>(2) set up an engineering workflow for managing prompts (version control, testing, rollback);<br>(3) clearly explain how to tell whether a prompt is any good once you've written it.

---

## 2.1 The Core Mindset: A Prompt Is a Spec, Not an Incantation

Imagine you're outsourcing your work to **an extremely capable engineer who takes everything completely literally and shows up for their first day on the job every single time**. The work instructions you write for them are the prompt.

This analogy dictates every principle that follows:

- The AI doesn't know your company's jargon—**terms that need defining must be defined**
- The AI doesn't do "you know what I mean, right?"—**vague requirements get you vague results**
- The AI forgets what you taught it last time, every time—**the rules have to be in the instructions on every pass**
- Showing the AI an example beats giving it adjectives—**"do it like this" beats "make it more professional"**

Skill at writing prompts is, at its core, **skill at writing specs**.

## 2.2 The Standard Anatomy of a Prompt

A production-grade prompt usually contains these parts (roughly in this order too, with the stable pieces pinned to the front to work with prompt caching):

```
[System Prompt]
1. Role and task: "You are a classifier for insurance claim documents"
2. Rules and boundaries: "Output exactly one of the following five categories; when there isn't enough information, output UNKNOWN—do not guess"
3. Output format: an explicit JSON schema
4. Examples (few-shot): 2–5 pairs of input → correct output

[User Message]
5. The actual content to process this time
```

A few key details:

- **Rules phrased as "what to do" beat "what not to do."** "Output JSON only" is more stable than "don't output extra text."
- **Give it an exit.** Tell it explicitly what to do when there isn't enough information (output UNKNOWN / say "the document doesn't mention this"). Without an exit, it'll make something up—hallucination is often just the prompt failing to offer an "I don't know" option.
- **Few-shot is the cheapest performance boost there is.** Unstable formatting, drifting classifications—add examples before you do anything else. The examples should cover edge cases (one normal case, one ambiguous case, one that should return UNKNOWN).

## 2.3 Chain of Thought: Think First, Answer Second

Asking the model to **"reason step by step first, then give the final answer" (CoT)** noticeably improves accuracy on complex tasks. The principle is easy to grasp through a word-chain analogy: demanding the answer directly is asking it to "land on the right conclusion in a single step"; letting it reason first is like letting it lay out the intermediate steps on the table, so the rest of the chain has something to build on.

The cost: more output tokens (money) and latency. So: **skip CoT on simple tasks (format conversion, clear-cut classification); use it only when judgment or multi-step derivation is needed.** Modern reasoning models bake this in at the model layer—when you use them, you no longer have to ask for it manually in the prompt.

## 2.4 Structured Output: Never Trust the Model to Behave

The iron law of enterprise integration: **if a model's output is going into a system, it has to be in a verifiable, structured format.** The standard three-part approach:

```python
def extract(document: str, retries: int = 2) -> Claim:
    for attempt in range(retries + 1):
        raw = llm(SYSTEM_PROMPT, document)      # 1. prompt asks for JSON (give it the schema and examples)
        try:
            return Claim.model_validate_json(raw)  # 2. validate against the schema in code (pydantic)
        except ValidationError as e:
            document = f"{document}\n\nLast output had a format error: {e}, please fix it"  # 3. retry carrying the error
    raise ExtractFailed(document)               # retries exhausted → send to a human queue, never let dirty data flow downstream
```

All three layers are essential: **require the format → validate → retry and fall back on failure.** Most APIs also offer native structured output / JSON mode—use it when you can—but validation in code still can't be skipped; this is the trust boundary.

## 2.5 Engineering-Grade Prompt Management: Prompt is Code

The prompt directly determines system behavior—so it *is* code, and you should manage it the way you manage code:

| What you do with code | The prompt equivalent |
|---|---|
| Version control | Prompts go into git, not scattered across code strings or someone's notepad |
| Testing | Run the eval set as a regression on every change (Chapter 6) |
| Code review | Prompt changes go through the PR process |
| Deployment and rollback | Prompts have version numbers; a production issue can roll back to an old version in one click |
| A/B testing | Split traffic between old and new prompts and compare production metrics |

Once you've written a prompt, how do you know if it's good? "Run a regression against the eval set—don't eyeball two examples." Changing a single word can make one class of inputs better and another worse, and the naked eye simply can't see it; only a full test set can.

## 2.6 A Practical Debugging Workflow (the order to debug in when a prompt is unstable)

1. **First, look at what the model actually received.** Got its history truncated? A variable that never got substituted in? Eight times out of ten a "prompt problem" is really an assembly problem.
2. **Shrink the repro.** Find the smallest input that fails.
3. **Check whether it's missing an exit.** Is it making things up because you never let it say "I don't know"?
4. **Add an example.** Add one few-shot example targeting the failure mode.
5. **Split the steps.** A single prompt doing five things does all five mediocrely; break it into a pipeline so each step is simple.
6. **Run the regression on every change.** Don't go by "feels better now."

---

## Common Misconceptions

1. **"Prompt engineering is just clever wording tricks."** Prompt engineering in production is spec writing + format validation + regression testing + version management. The wordsmithing is maybe ten percent of it.
2. **"Tune it once and you're done."** Models get upgraded, and input distributions drift. A prompt with no regression tests is a time bomb.
3. **"The more rules the safer."** Rules that conflict with each other, or that bury the important points in the middle (lost in the middle), actually make things less stable. Rules should be few and clear; push complex logic into code or a multi-step pipeline.
4. **"If the model outputs the wrong format, the model is bad."** Shipping without validation and retries—that's the engineer's fault.

## Self-Check

1. A client's classification prompt has unstable accuracy. What's your debugging order? (at least five steps)
2. What is few-shot? How should you pick the examples?
3. Write out the structured-output three-part approach, and explain why you still validate in code even when there's a native JSON mode.
4. "Once a prompt is written, how do you know if it's good?"—give a complete, well-organized answer.
5. Why does a prompt need to "give an exit"? What does that have to do with hallucination?

## Key Points for the Answers

    1. Look at the actual input → minimal repro → check the exit → add examples → split the steps → regression test.
    2. Few-shot = putting a few "input → correct output" pairs directly in the prompt to demonstrate to the model. Don't make all your examples easy ones—gather all three kinds: one normal case, one ambiguous edge case, and one refusal case that should return UNKNOWN.
    3. Require the format → validate against the schema → retry carrying the error → fall back to a human; validation is the trust boundary, because the model's output can always go off-format.
    4. Regression against an eval set, not the naked eye; a change can help one thing and hurt another, and only the test set reveals it.
    5. Without an "I don't know" option, the model is forced to keep the chain going and make something up; an exit is one of the cheapest anti-hallucination measures there is.
