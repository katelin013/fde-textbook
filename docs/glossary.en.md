# Glossary Quick Reference

A one-stop list of the AI terms every FDE needs — full English name, Chinese, and a one-line explanation. Grouped by topic and mapped to each chapter, so you can skim it quickly before an interview.

## LLM Basics (Ch1)

| Term | Chinese | One-line explanation |
|---|---|---|
| **LLM** (Large Language Model) | 大型語言模型 | A model trained on massive amounts of text that works by "predicting the next word"; it can write code, hold conversations, and reason, but at heart it's playing word-chain, not fact-checking. |
| **Token** | 詞元 | The smallest unit a model uses to process text; cost, capacity, and speed are all measured in it. |
| **Context Window** | 上下文視窗 | The maximum total number of tokens a model can "see" in a single pass; anything that doesn't fit, the model can't see. |
| **Temperature** | 溫度 | A parameter that controls how random the output is; low = stable and reproducible, high = varied and creative. |
| **Hallucination** | 幻覺 | When a model states something wrong with total confidence; it stems from the model playing word-chain rather than verifying facts. |
| **Streaming** | 串流輸出 | Returning output as it's being generated, so users see the first word sooner. |
| **TTFT** (Time To First Token) | 首字延遲 | The wait from when a user hits send to when they see the first word; a key metric for user experience. |
| **Inference** | 推論 | The process of the model "running once and producing output"; the counterpart to training. |
| **Prompt Caching** | 提示快取 | Caching the opening (prefix) that stays the same every time, to save cost and speed things up. |

## Prompt Engineering (Ch2)

| Term | Chinese | One-line explanation |
|---|---|---|
| **Prompt** | 提示詞 | The instructions and content you feed the model, which determine how it answers. |
| **System Prompt** | 系統提示 | The top-level instruction that sets the model's role and rules, usually placed at the very front of the conversation. |
| **Zero-shot / Few-shot** | 零樣本 / 少樣本 | Giving no examples / giving a few examples for the model to follow. |
| **Chain-of-Thought** (CoT) | 思維鏈 | Having the model "think step by step" before answering, to improve reasoning accuracy. |
| **Structured Output** | 結構化輸出 | Requiring the model to output a fixed format (such as JSON) so your program can easily take it from there. |

## RAG (Ch3)

| Term | Chinese | One-line explanation |
|---|---|---|
| **RAG** (Retrieval-Augmented Generation) | 檢索增強生成 | First pull relevant content from your database, then feed it to the model to answer, so it can draw on private knowledge. |
| **Embedding** | 嵌入向量 | Turning text into a string of numbers (a vector), so that semantically similar content ends up with similar values. |
| **Vector Database** | 向量資料庫 | A database built to store embeddings and support "find the most semantically similar" queries. |
| **Chunking** | 切塊 / 分段 | Splitting long documents into small pieces before embedding and retrieval. |
| **Semantic Search** | 語意搜尋 | Finding content by "meaning" rather than by keyword matching. |
| **Reranking** | 重排序 | Finely re-sorting the initial retrieval results to push the most relevant ones to the front. |

## Agent (Ch4)

| Term | Chinese | One-line explanation |
|---|---|---|
| **Agent** | 代理 / 智能體 | An AI system that can plan its own steps, call tools, and loop through execution to reach a goal. |
| **Tool Use / Function Calling** | 工具呼叫 / 函式呼叫 | Letting the model call external functions (look up data, do math, hit an API) to gain abilities it doesn't have on its own. |
| **ReAct** (Reason + Act) | 推理並行動 | The classic agent pattern of a "think → act → observe" loop. |
| **Orchestration** | 編排 | The overall flow control that coordinates multiple steps / tools / models. |

## MCP (Ch5)

| Term | Chinese | One-line explanation |
|---|---|---|
| **MCP** (Model Context Protocol) | 模型情境協定 | An open protocol that lets AI applications connect to external tools and data sources through a single unified standard. |
| **MCP Server / Client** | MCP 伺服端 / 用戶端 | The Server provides tools and data; the Client (the AI application) connects to and uses them. |

## Technology Selection (Ch7)

| Term | Chinese | One-line explanation |
|---|---|---|
| **Fine-tuning** | 微調 | Retraining a model on extra data to change its behavior or style. |
| **Prompt vs RAG vs Fine-tune** | 三種調校手段 | The selection order from cheap to expensive: try Prompt first, then RAG, and only then Fine-tune. |

## Evals (Ch6)

| Term | Chinese | One-line explanation |
|---|---|---|
| **Evals** (Evaluations) | 評估 | A mechanism that uses a test set to quantify the quality of AI output; it's the AI version of automated testing. |
| **Ground Truth** | 標準答案 / 基準真值 | The correct answer you compare model output against to judge right from wrong. |
| **LLM-as-a-Judge** | 以 LLM 當評審 | Using another LLM to automatically score how good or bad a model's output is. |
| **Regression** | 回歸（測試） | Using a test set after a change to confirm that "what used to work hasn't gotten worse." |

## Security (Ch8)

| Term | Chinese | One-line explanation |
|---|---|---|
| **Prompt Injection** | 提示注入 | An attacker hides malicious instructions inside the input data to trick the model into executing them. |
| **Jailbreak** | 越獄 | Using clever wording to bypass a model's safety limits and get it to do something it should refuse. |
| **Guardrails** | 護欄 | Checks and filters added before and after the model to block improper input / output. |

## Enterprise Deployment and Infrastructure (Ch9 / Ch10)

| Term | Chinese | One-line explanation |
|---|---|---|
| **Latency** | 延遲 | The time it takes from request to response; it directly affects user experience. |
| **Throughput** | 吞吐量 | The volume of requests that can be handled per unit of time; it affects scale and cost. |
| **Batch API** | 批次 API | Submitting non-urgent work in batches for non-real-time processing, usually at half price. |
| **SLA** (Service Level Agreement) | 服務等級協議 | The provider's committed metrics for things like availability and latency. |
| **FDE** (Forward Deployed Engineer) | 前進部署工程師 | The engineering role that goes on-site with the customer and actually integrates and lands the AI product. |

---

## AI CLI Tools: A Cross-Tool Comparison

The three major AI coding CLIs: **Claude Code** (Anthropic), **Gemini CLI** (Google), and **Codex CLI** (OpenAI). The same feature often has a different name or filename across the three tools; the table below maps them, with a one-line note on purpose.

| Concept (purpose) | Claude Code | Gemini CLI | Codex CLI |
|---|---|---|---|
| **Project instructions / memory file**<br>Tells the AI the project's rules, conventions, and architecture; read on every conversation | `CLAUDE.md` | `GEMINI.md` | `AGENTS.md` |
| **Config file**<br>Settings for permissions, default model, environment variables, and so on | `.claude/settings.json` | `.gemini/settings.json` | `~/.codex/config.toml` |
| **Custom slash commands**<br>Save frequently used prompts as a `/command` for one-click reuse | Slash commands<br>`.claude/commands/*.md` | Custom commands<br>`.gemini/commands/*.toml` | Custom prompts<br>`~/.codex/prompts/*.md` |
| **Skills**<br>Workflows bundled with instructional files that the AI applies automatically based on context | Agent Skills (`SKILL.md`, auto-triggered) | Provided via Extensions | Skills (`~/.codex/skills/…/SKILL.md`) |
| **Subagents**<br>Spin up a clone to run subtasks in an independent context | Subagents (`.claude/agents/*.md`) | Not natively available yet | Not natively available yet (can pair with the Agents SDK) |
| **Plugins / Extensions**<br>Bundle skills, commands, and MCP into an installable, version-controlled unit | Plugins (bundle skills / agents / commands / hooks / MCP) | Extensions (`gemini-extension.json`) | No official plugin system |
| **Marketplace**<br>A source that lets plugins be searched, installed, and updated | Yes (`/plugin marketplace add …`) | Yes (`gemini extensions install …`) | No official marketplace |
| **MCP server**<br>Connect the AI to external tools and data sources via a unified protocol | Supported | Supported | Supported |

### Where Should the Rules Be Defined?

To set project rules for these three CLIs (conventions, architecture, style, prohibitions), write them into each tool's **project instructions file** — placed at the project root and automatically loaded on every conversation:

- **Claude Code** → `CLAUDE.md`
- **Gemini CLI** → `GEMINI.md`
- **Codex CLI** → `AGENTS.md`

All three also support placing the file in your home directory (e.g. `~/.claude/CLAUDE.md`) to serve as cross-project **global rules**. Among them, **`AGENTS.md` is gradually becoming the cross-tool open standard**: Codex CLI reads it natively, and Gemini CLI can also be configured in `settings.json` (`context.fileName`) to read `AGENTS.md` instead — so if you want to "write one set of rules to feed multiple tools," `AGENTS.md` is the preferred choice.

(Files like `.cursor/rules` and `.windsurfrules` are how **editor-type** tools such as Cursor and Windsurf handle "rules," and have nothing to do with the three CLIs above.)

---

## The Evolution of AI Engineering Paradigms: From Prompt to Loop

The "core skill" of collaborating with AI has been climbing up levels of abstraction over the past few years — the bottleneck has moved from "the words you say" → "the context you provide" → "the spec you write" → "the loop you design." The four stages are **cumulative**, not replacements for one another: you still use prompt engineering inside loop engineering.

| Evolution stage | Era | Core question | One-line explanation |
|---|---|---|---|
| **Prompt Engineering**<br>提示工程 | ~2022–2024 | "How should I phrase things to get the best single output?" | Polishing a single instruction: few-shot, CoT, role-play, XML tags. Chasing "one input → one best output." |
| **Context Engineering**<br>情境工程 | 2025 | "What should I put inside the context window?" | Kicked off by Karpathy: a single prompt isn't enough; you need to dynamically assemble the entire context — retrieved documents, conversation history, tool definitions, RAG results. |
| **Spec-Driven Development**<br>規格驅動開發 (SDD, also called Spec Engineering) | 2025 | "What spec should I write so the agent can build to it?" | Instead of dictating instructions sentence by sentence, you first write a clear spec and hand it off to the agent to implement (GitHub Spec Kit and AWS Kiro are representative tools). |
| **Loop Engineering**<br>循環工程 (also called Harness Engineering) | 2026 | "What system should I design so the agent finds work, finishes it, verifies it, and remembers it — without me sitting in the loop?" | Emerged in June 2026. The focus shifts from "writing prompts" to "designing the loop that drives the agent": the generation side reruns cheaply, and the real bottleneck is the verifier. |

> **The key point for FDEs**: If an interview asks "will prompt engineering become obsolete," the right framing is — it hasn't been made obsolete, it's been **absorbed** into a higher-level skill. Being able to lay out this evolutionary line (prompt → context → spec → loop) and explain "why the bottleneck keeps moving up" shows that you're keeping pace and thinking clearly.

*Note: `spec engineer` and `sdd engineer` are actually the same thing (SDD = Spec-Driven Development), and the table above has merged them; `context engineering` is a crucial link that your original list missed, and it has been added back in.*
