# Ch9 Enterprise Deployment: From Demo to Production

## Chapter Goals

By the end of this chapter you'll be able to: (1) clearly articulate exactly what engineering separates a demo from production; (2) give a consultant-grade comparison of "hosted API vs. private deployment"; (3) explain the SSO/RBAC/audit trio; (4) walk confidently into the compliance context of Taiwanese enterprises (finance, manufacturing). This chapter is the dividing line between an FDE and an ordinary AI engineer.

---

## 9.1 The Gulf Between Demo and Production

Friday afternoon, you give the client a demo. The results dazzle, and the CEO signs off on the spot. Then what?

The world of the demo: one user, clean sample data, your laptop, and if something breaks you just try again.
The world of production: three thousand employees, twenty years of dirty data, the client's internal network, and if something breaks it makes the news.

The engineering that lies in between is the FDE's to-do list:

1. **Identity**: How do three thousand people log in? (SSO)
2. **Permissions**: Can the intern see what the sales rep can see? (RBAC + filtering at the retrieval layer)
3. **Audit**: When the regulator comes knocking, can you reconstruct "who asked what and when, and what the AI answered"?
4. **Reliability**: What happens when the API goes down? Retries, degradation, monitoring, alerting.
5. **Quality**: Once it's live, how do you know it's still doing okay? (evals + online signals, Ch6)
6. **Change management**: What process does changing a prompt have to go through? (version control + regression + review)

> Interview soundbite: "A demo proves the model *can* do it; production has to solve whether the *organization dares* to use it — and everything in between is engineering and governance. That's exactly where the FDE adds value."

## 9.2 Hosted API vs. Private Deployment (A Must-Answer Consultant-Grade Question)

The client asks: "Our data is sensitive — shouldn't we host the model ourselves?" Answer with a four-quadrant framing:

| Quadrant | Hosted API (OpenAI/Anthropic, etc.) | Self-hosted open-source model (Llama, etc.) |
|---|---|---|
| **Capability** | Frontier models, continuously upgraded for free | Open source is catching up; narrow tasks can be patched with fine-tuning |
| **Security/Compliance** | Data leaves the corporate network (protected by enterprise terms) | Data never leaves the internal network |
| **Cost** | Pay-as-you-go, zero upfront infrastructure | GPU infrastructure + an operations team; only pays off at high volume |
| **Operations** | None (they run it) | All on you: deployment, scaling, updates, security patches |

**The crucial middle option (the sweet spot for Taiwanese enterprises — always mention it)**: **private endpoints in the cloud** — model services on Azure OpenAI or GCP Vertex AI. You get frontier-model capability + data that stays inside the enterprise's own cloud tenant + compliance with most regulatory requirements, all without carrying your own GPUs. **Most "we need to self-host" requests pivot the moment they hear this option.**

Be honest with the client about the hidden costs of self-hosting: it's not just buying GPUs — it's raising an entire model-operations team (inference optimization, version management, security updates), and even then your model capability lags a generation behind the frontier. "Go live on a private endpoint first to validate the value, and only evaluate self-hosting if there's a genuine reason" is the responsible path.

## 9.3 The Enterprise Integration Trio: SSO, RBAC, Audit

### SSO (Single Sign-On)

Employees log into every system with their company account, backed by the **SAML** or **OIDC** protocol (OIDC is the mainstream for new systems). In plain terms: your AI application doesn't manage passwords itself — it "trusts the pass issued by the company's identity hub (Okta, Azure AD)." What the FDE needs to know: wiring up the OIDC flow and feeding the identity and group information carried in that pass into the application.

### RBAC (Role-Based Access Control)

Once identity is in, the next question is "what is this person allowed to see." What's special about AI systems (important): **permissions have to sink all the way down to the retrieval layer** — when someone in the sales department asks a question, the retrieval scope is limited to sales-department documents only (as Ch3/Ch8 covered: enforce this with metadata filtering, not with the prompt). Mapping from SSO groups to document permission labels is the single easiest place to get enterprise RAG wrong.

### Audit (Audit Trail)

Who, when, what they asked, what the system retrieved, what the AI answered, and whether a human reviewed it — everything leaves a trace. This isn't nice-to-have: in finance it's a hard compliance requirement, and it's the only way to prove your innocence after something goes wrong. (The logs themselves contain sensitive data, so masking and access control must match how you treat personal data.)

## 9.4 Reliability Engineering: SRE Fundamentals for AI Systems

An external LLM API is the "least reliable dependency" in your architecture. Treat it the way you'd treat any fragile external dependency:

- **Retries**: exponential backoff + jitter (this is coding question C2); distinguish retryable (429/timeout) from non-retryable (400).
- **Degradation**: primary model down → backup model / cached answer / a graceful "can't answer right now" failure — **never let an AI outage become a business outage.**
- **Rate limiting and quotas**: protect yourself (cost) and protect the upstream (429).
- **The four golden signals of monitoring**: latency (TTFT/total duration), traffic, error rate, saturation (token quota usage) — plus the AI-specific ones: eval-score trends, hallucination-report rate, and escalation-to-human rate.

## 9.5 Change Management: The Enterprise Cadence

Enterprises have freeze periods, UAT, release windows, and rollback requirements. Your AI system has to play along:

- Version your prompts/models so any change can be rolled back (Ch2).
- A change only passes review if it comes with an eval regression report (Ch6) — "how the score shifted across 500 test cases for this change" is your UAT evidence.
- Canary release: roll a new prompt out to 5% of traffic first.

> "Change anything anytime" is a virtue at a startup and a risk at an enterprise. Repackage "rapid iteration" as "controlled change where every iteration comes with regression evidence," and the enterprise will actually let you move fast.

## 9.6 A Quick Guide to the Taiwan Context

- **Finance**: Regulated by the FSC. Data localization, dedicated rules for outsourced cloud services, and hard audit-trail requirements — your Taishin Bank experience speaks directly to this.
- **Personal Data Protection Act**: Notification and purpose limitation when personal data enters an AI system; log masking.
- **Manufacturing**: The secrets are process parameters and yield data (trade-secret grade), often with requirements for on-prem or "nothing leaves the plant"; deployment in network-isolated environments (AIFT's JD is talking about exactly this).
- The shared mindset: they're not resisting AI, they're afraid of losing control. Your answer is always a governance framework (permissions/audit/human review), never "just trust the model."

---

## Common Misconceptions

1. **"A successful demo means we're about to go live."** — The demo is the starting line; the trio + reliability + change management make up the bulk of the timeline. Factor these in when you quote a schedule, or you'll be burying yourself.
2. **"Sensitive data means we must self-host the model."** — Lead with private endpoints in the cloud; self-hosting is the last resort and must be costed in full.
3. **"Just control permissions with the prompt."** — For the third time: filter at the retrieval layer. This is a red-line question in interviews, and getting it wrong is an instant out.
4. **"Monitoring an AI system just means checking whether the API is alive."** — You also have to monitor quality (eval trends, escalation-to-human rate). A system that's alive but whose answers have degraded is a far more insidious failure.

## Self-Check

1. After the demo, the client asks "how long until the whole company can go live?" — list the demo-to-production engineering checklist (six items).
2. "Our data is really sensitive — shouldn't we host the model ourselves?" — answer at consultant grade with the four quadrants + the middle option.
3. Explain the SSO/RBAC/audit trio in plain terms, and point out what's special about AI systems when it comes to RBAC.
4. Design the reliability of an AI system: the key points of retries, degradation, and monitoring.
5. A financial client's audit department asks "can the AI's decisions be audited?" — your answer (drawing on your Taishin experience).
## Key Points for Reference Answers

    1. See the six items in 9.1.
    2. See 9.2; remember to be honest about the full cost of self-hosting and the "validate on a private endpoint first" path.
    3. See 9.3; the special point = permissions sinking down to the retrieval layer.
    4. See 9.4; the core line: "don't let an AI outage become a business outage."
    5. Full traceability (input/retrieval/output/review) + human-review checkpoint design + segregation of duties modeled on internal controls; "I built an audit system at Taishin — same logic."
