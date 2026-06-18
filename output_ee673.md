# Query Report

**Session:** `qr-64dee673`
**Query:** Compare 5 AI coding tools by free plan and paid plan.
**Generated:** 2026-06-19 01:48:59

---

## 1. Original User Goal

> Compare 5 AI coding tools by free plan and paid plan.


## 2. Planner DAG

**Graph nodes:**

- `n:1` **planner** [complete]  inputs=['USER_QUERY']
- `n:10` **planner** [complete]  inputs=['USER_QUERY']
- `n:11` **researcher** [complete]  inputs=[]
- `n:12` **researcher** [complete]  inputs=[]
- `n:13` **researcher** [complete]  inputs=[]
- `n:14` **researcher** [complete]  inputs=[]
- `n:15` **researcher** [complete]  inputs=[]
- `n:16` **distiller** [complete]  inputs=['n:11', 'n:12', 'n:13', 'n:14', 'n:15']
- `n:17` **formatter** [complete]  inputs=['USER_QUERY', 'n:16']
- `n:18` **critic** [complete]  inputs=['USER_QUERY', 'n:16']
- `n:2` **researcher** [complete]  inputs=[]
- `n:3` **researcher** [complete]  inputs=[]
- `n:4` **researcher** [complete]  inputs=[]
- `n:5` **researcher** [complete]  inputs=[]
- `n:6` **researcher** [complete]  inputs=[]
- `n:7` **distiller** [complete]  inputs=['n:2', 'n:3', 'n:4', 'n:5', 'n:6']
- `n:8` **formatter** [skipped]  inputs=['USER_QUERY', 'n:7']
- `n:9` **critic** [complete]  inputs=['USER_QUERY', 'n:7']

**Edges (data flow):**

  n:1 → n:2
  n:1 → n:3
  n:1 → n:4
  n:1 → n:5
  n:1 → n:6
  n:2 → n:7
  n:3 → n:7
  n:4 → n:7
  n:5 → n:7
  n:6 → n:7
  n:7 → n:9
  n:9 → n:8
  n:10 → n:11
  n:10 → n:12
  n:10 → n:13
  n:10 → n:14
  n:10 → n:15
  n:11 → n:16
  n:12 → n:16
  n:13 → n:16
  n:14 → n:16
  n:15 → n:16
  n:16 → n:18
  n:18 → n:17


## 3. Browser Path Chosen

_(No Browser skill was used in this query.)_


## 4. Browser Actions Taken

_(No Browser skill was used in this query.)_


## 5. Screenshots / Page-State Logs

_(No Browser skill was used in this query.)_


## 6. Extracted Data

**Node n:7 — Distiller**

```json
{
  "GitHub Copilot": {
    "Free": "2,000 completions/month, Haiku 4.5/GPT-5 mini models, Copilot CLI",
    "Paid": "$10/month (Pro plan)"
  },
  "Cursor AI": {
    "Free": "Hobby tier with limited agent requests and tab completions",
    "Paid": "$20/month (Pro), $60/month (Pro+), $200/month (Ultra)"
  },
  "Tabnine": {
    "Free": "Dev Preview with basic completions and foundational AI agents",
    "Paid": "$9/month (Dev Plan), $39/month (Enterprise Plan)"
  },
  "Sourcegraph Cody": {
    "Free": "None (retired July 2025)",
    "Paid": "Enterprise agreement starting at ~$16,000"
  },
  "Supermaven": {
    "Free": "Code suggestions, large codebase compatibility, 7-day data retention",
    "Paid": "$10/month (Pro and Team plans)"
  }
}
```

*Rationale: Pricing and feature details were extracted from the findings of nodes n:2, n:3, n:4, n:5, and n:6.*

---
**Node n:16 — Distiller**

```json
{
  "GitHub Copilot": {
    "Free": "$0, 2,000 completions/mo, Haiku 4.5/GPT-5 mini, Copilot CLI",
    "Paid": "$10/user/mo (Pro)"
  },
  "Cursor AI": {
    "Free": "Hobby plan, limited agent requests and Tab completions",
    "Paid": "Individual ($20/mo), Teams ($40/user/mo), Enterprise (custom)"
  },
  "Tabnine": {
    "Free": "Discontinued",
    "Paid": "Individual, Teams, and Enterprise (custom)"
  },
  "Codeium": {
    "Free": "Free-forever, fast autocomplete, 25 prompt credits/mo",
    "Paid": "$15/mo (Pro), plus Team and Enterprise tiers"
  },
  "Supermaven": {
    "Free": "$0/mo, basic code completion",
    "Paid": "$10/mo (Pro), $10/user/mo (Team)"
  }
}
```

*Rationale: Pricing and feature details were extracted from the findings provided for each respective tool (n:11 through n:15).*

---
**Node n:2 — Researcher**

*Question:* What are the free and paid plan details for GitHub Copilot?

GitHub Copilot offers a tiered pricing structure catering to individuals and businesses. The 'Free' plan is available for individuals to get started at no cost, requiring no credit card. It includes 2,000 completions per month, access to models such as Haiku 4.5 and GPT-5 mini, and access to the Copilot CLI.

The 'Pro' plan is designed for individuals for everyday coding and features agent integration. It is priced at $10 USD per user per month. Additionally, GitHub provides specific plans for students through the GitHub Copilot Student program.

For businesses, GitHub offers specialized plans, such as 'Copilot for Business,' which provide enterprise-grade AI features, security, and management capabilities. These are distinct from individual plans and are intended for teams and organizations.

*Sources:*
  - [GitHub Copilot · Plans & pricing](https://github.com/features/copilot/plans)

---
**Node n:3 — Researcher**

*Question:* What are the free and paid plan details for Cursor AI?

Cursor AI offers a tiered pricing structure that includes a free "Hobby" tier and several paid subscription options for individuals and teams. All plans, regardless of tier, include core features such as full repository awareness, Model Context Protocol (MCP) support, multi-file diff capabilities, and natural language coding assistance.

The free Hobby tier is designed for users to experiment with the IDE. It provides limited access to AI agent requests and tab completions, allowing users to test the workflow before committing to a paid plan. Users who exhaust their free credits can often activate a 7-day free Pro trial to continue their work.

The Pro plan, priced at $20 per month, is the most popular tier for individual developers. It includes virtually unlimited tab completions and significantly higher limits for agent requests compared to the Hobby tier. Additionally, it introduces the ability to use background agents, which can work on coding tasks asynchronously while the developer continues to work in the IDE.

For heavier users or those requiring more capacity, Cursor offers higher-tier plans, including Pro+ ($60/month) and Ultra ($200/month). These plans are designed to accommodate larger volumes of agentic requests and compute usage. Teams and Enterprise plans are also available for organizations requiring collaborative features and administrative controls.

*Sources:*
  - [Cursor Pricing 2026: Free vs Pro vs Ultra — Which Plan?](https://www.braingrid.ai/blog/cursor-pricing)

---
**Node n:4 — Researcher**

*Question:* What are the free and paid plan details for Tabnine?

Tabnine offers a tiered pricing structure designed for different user needs, ranging from individual developers to large enterprises. As of late 2025, the primary tiers include the Dev Preview (Free) plan, the Dev Plan, and the Enterprise Plan.

The Dev Preview (Free) plan is available at no cost and is targeted at individuals and students, providing access to basic code completions and foundational AI agents. The Dev Plan is priced at $9 per user/month and is aimed at professional developers and small teams, offering additional features such as AI chat, full function completion, and natural language-to-code capabilities.

The Enterprise Plan is priced at $39 per user/month and is designed for large organizations and regulated industries. This tier prioritizes features like enterprise-grade security, compliance, and flexible deployment options, which may include SaaS, VPC, on-premises, or fully air-gapped environments.

*Sources:*
  - [A complete guide to Tabnine pricing in 2025 - eesel AI](https://www.eesel.ai/blog/tabnine-pricing)

---
**Node n:5 — Researcher**

*Question:* What are the free and paid plan details for Sourcegraph Cody?

As of July 23, 2025, Sourcegraph Cody no longer offers self-serve plans. Both the free tier and the paid Pro plan were retired on that date, and the Enterprise Starter tier no longer includes access to Cody.

Currently, Cody is available exclusively as part of a Sourcegraph Enterprise agreement. Pricing for Sourcegraph Enterprise begins at approximately $16,000. This model is designed for large engineering organizations rather than individual developers or small teams.

The enterprise offering includes AI-feature credits, which utilize org-wide credit pooling. These credits do not expire monthly and roll over upon contract renewal. The service provides advanced features such as cross-repository code context via the Sourcegraph code graph, Deep Search, and various enterprise-grade security and administrative controls.

*Sources:*
  - [Cody by Sourcegraph: Features, Pricing & Review (June 2026)](https://www.aipedia.wiki/tools/cody/)

---
**Node n:6 — Researcher**

*Question:* What are the free and paid plan details for Supermaven?

Supermaven offers three primary tiers: Free, Pro, and Team. The Free tier provides fast, high-quality code suggestions and compatibility with large codebases at no cost. It includes a 7-day data retention limit.

The Pro plan costs $10 per month and includes all features in the Free tier, plus several enhancements: the ability to adapt to individual coding styles, a 1 million token context window, access to the largest and most intelligent model, and $5 per month in Supermaven Chat credits. A 30-day free trial is available for this plan.

The Team plan is also priced at $10 per month per user. It provides all the benefits of the Pro plan, with the addition of centralized user management and billing for organizational needs.

*Sources:*
  - [Supermaven Pricing](https://supermaven.com/pricing)

---
**Node n:11 — Researcher**

*Question:* What are the free and paid plan details for GitHub Copilot?

GitHub Copilot offers a Free plan and a Pro plan for individuals. The Free plan is priced at $0 and includes 2,000 completions per month, access to models like Haiku 4.5 and GPT-5 mini, and access to the Copilot CLI. It does not require a credit card to sign up, and verified students can access a specific Student plan.

The Pro plan is priced at $10 per user per month. It is designed for everyday coding with agents. GitHub notes that they are gradually enabling new sign-ups for this tier, and users may need to check back if immediate access is unavailable.

*Sources:*
  - [GitHub Copilot · Plans & pricing](https://github.com/features/copilot/plans)

---
**Node n:12 — Researcher**

*Question:* What are the free and paid plan details for Cursor AI?

Cursor AI offers a tiered subscription model starting with a 'Hobby' free plan, which includes limited agent requests and limited Tab completions with no credit card required. Paid plans include Individual (Pro, Pro+, and Ultra tiers), Teams, and Enterprise.

Individual plans (starting at $20/mo) provide extended limits on agents, access to frontier models, support for MCPs, skills, hooks, cloud agents, and usage-based billing for Bugbot. The Teams plan ($40/user/mo) adds centralized administration, team-wide marketplace and privacy settings, usage analytics, and SSO. 

The Enterprise plan is a custom offering that adds features such as pooled usage, invoice/PO billing, advanced access controls (repository/model/MCP), audit logs, and priority support. 

All plans include a set amount of model usage, with on-demand usage billed in arrears if limits are exceeded. Payments for self-serve plans are accepted via major credit and debit cards, while Enterprise customers can contact sales for invoice-based billing and wire transfers.

*Sources:*
  - [Cursor · Pricing](https://cursor.com/pricing)

---
**Node n:13 — Researcher**

*Question:* What are the free and paid plan details for Tabnine?

Recent information indicates that Tabnine has discontinued its free plan as of 2025. The service currently operates on a paid subscription model.

Tabnine offers structured paid plans for individual developers and teams, alongside custom enterprise options. Users are encouraged to contact Tabnine directly for details regarding privately deployed AI software development platforms and custom enterprise pricing.

*Sources:*
  - [Plans & Pricing | Tabnine](https://www.tabnine.com/pricing/)
  - [Tabnine Pricing 2026](https://www.g2.com/products/tabnine/pricing)
  - [Tabnine Pricing & Plans](https://www.saasworthy.com/product/tabnine/pricing)

---
**Node n:14 — Researcher**

*Question:* What are the free and paid plan details for Codeium?

Codeium, now integrated into or rebranded as the Windsurf ecosystem, offers a free-forever tier for individual developers. This free plan includes access to core features such as fast autocomplete and in-editor chat, currently limited to 25 prompt credits per month.

For professional use, Codeium offers a Pro plan priced at $15 per month. This subscription increases the usage capacity to 500 prompt credits per month. Additionally, Codeium provides paid plans tailored for teams and enterprise-level deployments, which offer broader administrative and collaborative features beyond the individual Pro tier.

*Sources:*
  - [Codeium vs Cursor: Which Is Better? Pricing, Speed, Features Compared [2026]](https://uibakery.io/blog/codeium-vs-cursor)

---
**Node n:15 — Researcher**

*Question:* What are the free and paid plan details for Supermaven?

Supermaven offers three primary plan tiers: Free, Pro, and Team. All plans include fast, high-quality code suggestions, support for large codebases, and a 7-day data retention limit.

The Free Tier is available at $0/month and provides basic code completion functionality. It does not include advanced features like style adaptation, the extended context window, or the largest models.

The Pro plan costs $10/month and introduces a 1 million token context window, access to the largest and most intelligent models, and the ability for the AI to adapt to the user's specific coding style. It also includes $5/month in Supermaven Chat credits and offers a 30-day free trial.

The Team plan is priced at $10/month per user and includes all features of the Pro plan. Additionally, it provides centralized user management and billing, making it suitable for companies and organizations.

*Sources:*
  - [Supermaven Pricing](https://supermaven.com/pricing)



## 7. Final Comparison Table

Here is a comparison of five popular AI coding tools based on their free and paid plan structures:

| Tool | Free Plan | Paid Plan |
| :--- | :--- | :--- |
| GitHub Copilot | $0/mo (2,000 completions, limited models) | $10/user/mo (Pro) |
| Cursor AI | Hobby plan (limited agent/tab completions) | $20/mo (Individual), $40/user/mo (Teams) |
| Tabnine | Discontinued | Individual, Teams, and Enterprise (custom) |
| Codeium | Free-forever (fast autocomplete, 25 credits/mo) | $15/mo (Pro), plus Team/Enterprise tiers |
| Supermaven | $0/mo (basic code completion) | $10/mo (Pro), $10/user/mo (Team) |


## 8. Turn Count & Cost Summary

| Node      | Skill              | Status   | Time    | Gateway Ledger (calls / tokens) | Provider      | Turns |
| :-------- | :----------------- | :------- | :------ | :------------------------------- | :------------ | :---- |
| n:1      | planner            | complete |    5.3s | 2 calls                          | gemini       |      |
| n:2      | researcher         | complete |   60.6s | 31 calls                         | gemini       |      |
| n:3      | researcher         | complete |   28.3s | 31 calls                         | gemini       |      |
| n:4      | researcher         | complete |   52.2s | 31 calls                         | gemini       |      |
| n:5      | researcher         | complete |   56.3s | 31 calls                         | gemini       |      |
| n:6      | researcher         | complete |   64.4s | 31 calls                         | gemini       |      |
| n:7      | distiller          | complete |    3.8s | 2 calls                          | gemini       |      |
| n:9      | critic             | complete |    1.3s | 2 calls                          | groq         |      |
| n:10     | planner            | complete |    2.9s | 2 calls                          | gemini       |      |
| n:11     | researcher         | complete |   60.5s | 31 calls                         | gemini       |      |
| n:12     | researcher         | complete |   53.0s | 31 calls                         | gemini       |      |
| n:13     | researcher         | complete |   40.2s | 31 calls                         | gemini       |      |
| n:14     | researcher         | complete |   56.6s | 31 calls                         | gemini       |      |
| n:15     | researcher         | complete |   48.6s | 31 calls                         | gemini       |      |
| n:16     | distiller          | complete |    4.1s | 2 calls                          | gemini       |      |
| n:17     | formatter          | complete |    2.3s | 1 calls                          | gemini       |      |
| n:18     | critic             | complete |    1.3s | 2 calls                          | groq         |      |
| **Total** | **17 nodes** |          | **541.8s** | **$0.001622** |                |       |

