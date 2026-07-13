# FDE Career-Switch Study Notes

> A note up front: these notes were started by Claude Code — while preparing to switch careers into a Forward Deployed Engineer (FDE) role, I organized this material together with it, and I keep revising it. I'm not an AI expert, so there are bound to be gaps in my understanding; corrections are welcome via [a GitHub Issue](https://github.com/katelin013/fde-textbook/issues).

An engineer who has been writing code for over a decade, wanting to become an FDE — notes organized while learning. Every chapter starts from zero, plain language first, metaphors before jargon.

## What these notes cover

An FDE is an engineer embedded in the customer's environment who delivers AI solutions end to end — from breaking down requirements to shipping and operating them — half engineer, half consultant, fully accountable. These notes cover the ten topics I believe this role needs.

## Table of contents

| Ch | Topic | In one line |
|---|---|---|
| [Ch1](ch1-llm-basics.md) | How LLMs Work | A powerful autocomplete machine: tokens, context, cost, and built-in limits |
| [Ch2](ch2-prompt-engineering.md) | Prompt Engineering | Turning black magic into engineering: a prompt is a spec, not a spell |
| [Ch3](ch3-rag.md) | RAG | Giving the model an open-book exam: the full retrieval-augmented generation pipeline |
| [Ch4](ch4-agents.md) | Agents & Tool Use | From answering questions to completing tasks: controlling the blast radius of mistakes |
| [Ch5](ch5-mcp.md) | MCP | The USB-C of AI: the standard answer to the N×M problem |
| [Ch6](ch6-evals.md) | Evals | How to prove an AI system actually works: the line between demo and production |
| [Ch7](ch7-choosing-approach.md) | Choosing an Approach | Prompting vs RAG vs Fine-tune: the decision order from cheap to expensive |
| [Ch8](ch8-security.md) | Security | Prompt injection and defense in depth: a prompt is not a security boundary |
| [Ch9](ch9-enterprise-deployment.md) | Enterprise Deployment | From demo to production: the engineering that makes an organization dare to use it |
| [Ch10](ch10-infra-basics.md) | Infrastructure Refresher | Linux, networking, K8s: polishing rusty ops knowledge back to whiteboard level |

## How each chapter is structured

1. **Goals** — what you'll be able to do after reading
2. **Main notes** — metaphor-led openings, plain-language explanations, diagrams and code examples
3. **Common misconceptions** — the traps most easily hit in practice and in interviews
4. **Self-check** — with reference answers (expand the collapsible block to check)
5. **Interview links** — which FDE interview topics this chapter maps to

## Suggested reading order

- **First read**: Ch1 → Ch2 → Ch3 → Ch6 (build the "LLM–prompt–RAG–evaluation" backbone first), then Ch4/Ch5 (agents and integration), and finally Ch7/Ch8/Ch9 (decisions, security, enterprise).
- **Before an interview**: go straight to each chapter's "Common misconceptions" and "Self-check".
- **When your ops basics are rusty** (Linux / networking / K8s): flip to Ch10 anytime — it's self-contained.
