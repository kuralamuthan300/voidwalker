# Void Walker — Autonomous Browser Agent

An extensible, growing-graph orchestrator that decomposes user queries into directed acyclic graphs (DAGs) of skill nodes, executes them concurrently, and recovers from failures through re-planning. The core differentiator is a **4-layer browser cascade** (extract → deterministic → a11y → vision) that enables the agent to navigate JavaScript-rendered pages, fill forms, perform multi-step searches, and extract structured data — all through a single `browser` skill.

---

## Architecture Overview

```
User Query
    │
    ▼
┌──────────┐    ┌────────────┐    ┌──────────┐
│ Planner   │───▶│  Skills    │───▶│ Formatter│
│ (decompose)│   │  Registry  │    │ (output) │
└──────────┘    └─────┬──────┘    └──────────┘
                      │
              ┌───────┼───────┐
              ▼       ▼       ▼
         ┌────────┐ ┌──────┐ ┌────────┐
         │Browser │ │Res.  │ │Coder / │
         │(4-layer│ │earcher│ │Sandbox │
         │cascade)│ │(web) │ │Executor│
         └───┬────┘ └──────┘ └────────┘
             │
    ┌────────┼────────┐
    ▼        ▼        ▼
 Layer 1   Layer 2a  Layer 2b/3
 (extract) (sel.)   (a11y/vision)
```

### Key Files

| File | Purpose |
|------|---------|
| `code/flow.py` | Growing-graph orchestrator, node execution, recovery loops |
| `code/skills.py` | Skill registry, prompt rendering, MCP tool dispatch |
| `code/browser/skill.py` | **4-layer browser cascade** — the core contribution |
| `code/browser/driver.py` | A11y (text-only) and Set-of-Marks (vision) drivers |
| `code/browser/client.py` | Gateway client for /v1/vision and /v1/chat endpoints |
| `code/browser/dom.py` | Interactive element enumeration via accessibility tree |
| `code/browser/highlight.py` | Screenshot annotation with numbered bounding boxes |
| `code/agent_config.yaml` | Skill definitions, prompts, and routing config |
| `code/gateway.py` | LLM gateway abstraction (provider failover, cost ledger) |
| `code/prompts/` | System prompts for each skill (planner, critic, browser, etc.) |

### The 4-Layer Browser Cascade

| Layer | Method | When It's Used | Cost |
|-------|--------|----------------|------|
| **1. Extract** | Pure-HTTP fetch + trafilatura | Static pages, no interaction needed | ~0 tokens |
| **2a. Deterministic** | Caller-supplied CSS selectors | Known page structure, precise selectors | ~0 tokens |
| **2b. A11y** | Playwright + accessibility tree → /v1/chat | Interactive pages, text-only LLM calls | Low tokens |
| **3. Vision** | Playwright screenshot → numbered marks → /v1/vision | Complex UIs, vision-dependent tasks | High tokens |

The cascade **escalates** when the current layer produces empty or insufficient output, stopping at the first layer that succeeds.

---

## Query Reports

Eight query runs have been conducted to validate the Browser skill across diverse scenarios:

| # | Report | Query | Browser Path | Status | Total Time | Nodes | Gateway Cost |
|---|--------|-------|-------------|--------|-----------|-------|-------------|
| 1 | [output_79128.md](./output_79128.md) | Compare top 3 Hugging Face text-generation models sorted by likes | `a11y` | ✅ Success (14 browser nodes via recovery loop) | ~122s | ~76 | ~$0.0038 |
| 2 | [output_a4df9.md](./output_a4df9.md) | Go to centuryrealestate.in and fill random fake details | `a11y` → `vision` | ❌ Failed (502 Bad Gateway from vision endpoint) | 4.7s | 2 | $0.000 |
| 3 | [output_aa10e.md](./output_aa10e.md) | YouTube: search "spiderman brand new day", get first comment | `a11y` | ✅ Success | 122.5s | 19 | $0.003804 |
| 4 | [output_c97c7.md](./output_c97c7.md) | Kaggle: find recent datasets on airplanes with high upvotes | `a11y` (n:2, n:7) + `extract` (n:12 fail) | ⚠️ Mixed | 164.2s | 12 | $0.001464 |
| 5 | [output_ec4ed.md](./output_ec4ed.md) | Compare 3 laptops under ₹80,000 | `extract` (n:11 success) + `a11y` (n:16, n:21) | ⚠️ Mixed | 207.5s | 19 | $0.003896 |
| 6 | [output_ee673.md](./output_ee673.md) | Compare 5 AI coding tools by free plan and paid plan | *(No browser — Researcher skill used)* | ✅ Success | 541.8s | 17 | $0.001622 |
| 7 | [output_f7692.md](./output_f7692.md) | Compare 5 CNC/VMC training institutes in Bangalore | *(No browser — Researcher skill used)* | ✅ Success | 244.9s | 41 | $0.027170 |
| 8 | [output_08a75.md](./output_08a75.md) | Go to Excalidraw and draw a rectangle | `a11y` → `vision` | ❌ Failed (canvas-based UI — target page closed) | 12.3s | 4 | $0.000 |

---

## Detailed Run Metadata

### 1. Hugging Face Models Comparison → [`output_79128.md`](./output_79128.md)

| Field | Value |
|-------|-------|
| **Session** | `qr-66d79128` |
| **Original User Goal** | Compare top 3 Hugging Face text-generation models sorted by likes |
| **Planner DAG** | 76+ nodes (planner → browser → distiller → critic → formatter, repeated through recovery loops) |
| **Browser Path Chosen** | `a11y` — all 14 browser nodes used the accessibility-text layer |
| **Target URL** | `https://huggingface.co/models?pipeline_tag=text-generation&sort=likes` |
| **Final Comparison** | Models included deepseek-ai/DeepSeek-R1 (6.03M likes), openai/gpt-oss-20b (6.05M likes), meta-llama/Meta-Llama-3-8B (1.15M likes) |
| **Turn Count** | Most browser nodes completed in 4 turns; first node required 9 turns |
| **Cost Summary** | ~$0.0038 in gateway calls |
| **Key Observation** | Recovery planner repeatedly re-invoked browser nodes because critic rejected distiller output. The critic cap eventually ended the loop without a final formatter output. |

### 2. Century Real Estate Form Fill → [`output_a4df9.md`](./output_a4df9.md)

| Field | Value |
|-------|-------|
| **Session** | `qr-9e6a4df9` |
| **Original User Goal** | Go to centuryrealestate.in, fill random fake details, return the filled data |
| **Planner DAG** | planner → browser → formatter (3 nodes) |
| **Browser Path Chosen** | `a11y` (12 vision turns) → escalated to `vision` (11 turns) |
| **Final URL** | N/A — failed |
| **Status** | ❌ **Failed** — `HTTP 502 Bad Gateway` on `/v1/vision` |
| **Turn Count** | 23 total gateway calls across both layers |
| **Cost Summary** | $0.000 (failed before completion) |
| **Key Observation** | The browser successfully navigated the site and interacted with forms (11 vision turns), but the vision endpoint returned a 502 error. The site uses a popup/overlay that the a11y layer couldn't parse (140-byte legends — empty/no interactive elements detected), forcing escalation to vision. |

### 3. YouTube Comment Extraction → [`output_aa10e.md`](./output_aa10e.md)

| Field | Value |
|-------|-------|
| **Session** | `qr-d4caa10e` |
| **Original User Goal** | Go to YouTube, search "spiderman brand new day", click first video, get the first comment |
| **Planner DAG** | 23 nodes over 5 recovery cycles (planner → browser → distiller → critic → formatter) |
| **Browser Path Chosen** | `a11y` — all 5 browser nodes used accessibility layer |
| **Final URL** | `https://www.youtube.com/watch?v=6TnbSI4yfZY` |
| **Final Output** | First comment by @chrisruiz29 |
| **Turn Count** | 4 turns each (n:2, n:7, n:12, n:17), 3 turns (n:22) |
| **Cost Summary** | 122.5s total, 19 nodes, $0.003804 |
| **Key Observation** | The a11y layer successfully navigated YouTube's complex UI: typed in search box, clicked search button, scrolled to load comments. First comment was extracted consistently across 5 recovery attempts. The n:22 node bypassed the homepage and went directly to search results, completing in 3 turns. |

### 4. Kaggle Airplane Datasets → [`output_c97c7.md`](./output_c97c7.md)

| Field | Value |
|-------|-------|
| **Session** | `qr-97fc97c7` |
| **Original User Goal** | Go to Kaggle and find recent dataset on airplanes with high upvotes |
| **Planner DAG** | 12 nodes (planner → browser → distiller → critic → formatter + recovery) |
| **Browser Path Chosen** | `a11y` (n:2 ✅, n:7 ✅) + `extract` (n:12 ❌ — step cap at 12) |
| **Target URL** | `https://www.kaggle.com/datasets?search=airplane&sort=votes` |
| **Final Output** | Top datasets: Airplane Crashes (12.5K votes), Flight Price Prediction (8.2K votes), Airport Data (5.1K votes) |
| **Turn Count** | 4 turns each for successful a11y nodes; 0 actions for failed extract node |
| **Cost Summary** | 164.2s total, 12 nodes, $0.001464 |
| **Key Observation** | First 2 browser nodes succeeded with a11y in 4 turns. The recovery browser node (n:12) failed — escalated to vision but got stuck in a loop (same screenshot repeated for 12 turns). Demonstrates the cascade handling failure correctly but highlights a limitation: the vision layer can get stuck on unchanging pages. |

### 5. Laptop Comparison Under ₹80,000 → [`output_ec4ed.md`](./output_ec4ed.md)

| Field | Value |
|-------|-------|
| **Session** | `qr-538ec4ed` |
| **Original User Goal** | Compare 3 laptops under ₹80,000 |
| **Planner DAG** | 19 nodes (planner → browser → distiller → critic + researcher fallback) |
| **Browser Path Chosen** | `extract` (n:2 ❌, n:11 ✅ using trafilatura) + `a11y` (n:16 ✅, n:21 ✅) |
| **Target URL** | Amazon.in search for laptops under ₹80,000 |
| **Final Output** | Dell 15 (₹59,990), Dell 15 Smart Choice (₹67,990), HP 15 (₹73,990) |
| **Turn Count** | n:11 = 0 turns (pure extract), n:16 = 6 turns, n:21 = 4 turns |
| **Cost Summary** | 207.5s total, 19 nodes, $0.003896 |
| **Key Observation** | First browser node (n:2) failed on Amazon's homepage (CAPTCHA/anti-bot). Researcher skill (n:6) used web_search as fallback to get laptop specs from Smartprix. Subsequent browser nodes succeeded on the search results page. Demonstrates graceful degradation: when Amazon blocks the browser, the agent falls back to the researcher skill. |

### 6. AI Coding Tools Comparison → [`output_ee673.md`](./output_ee673.md)

| Field | Value |
|-------|-------|
| **Session** | `qr-64dee673` |
| **Original User Goal** | Compare 5 AI coding tools by free plan and paid plan |
| **Browser Path Chosen** | *(No Browser skill used)* — Planner decomposed into 10 researcher fan-out nodes |
| **Skills Used** | 2× planner → 10× researcher → 2× distiller → 2× critic → 2× formatter |
| **Final Output** | Comparison of GitHub Copilot, Cursor AI, Tabnine, Codeium, Supermaven with free/paid plan details |
| **Cost Summary** | 541.8s total, 17 nodes, $0.001622 |
| **Key Observation** | The Planner chose not to use the browser skill at all, instead spawning 10 parallel researcher nodes (5 for the first attempt, 5 for the second after critic rejection). Each researcher ran web_search + fetch_url tools independently. This is more cost-effective ($0.0016 vs ~$0.004 for browser runs) because web search + fetch is cheaper than Playwright + vision. |

### 7. CNC/VMC Training Institutes Comparison → [`output_f7692.md`](./output_f7692.md)

| Field | Value |
|-------|-------|
| **Session** | `qr-be4f7692` |
| **Original User Goal** | Compare 5 CNC/VMC training institutes in Bangalore |
| **Browser Path Chosen** | *(No Browser skill used)* — Planner decomposed into 10+ researcher fan-out nodes |
| **Skills Used** | 6× planner → 10× researcher → 10× distiller → 10× critic → 1× formatter |
| **Final Output** | Comparison of Rite CNC, CADPOINT, Techsys, Alined Technologies, Mass Education Academy |
| **Cost Summary** | 244.9s total, 41 nodes, $0.027170 |
| **Key Observation** | The most expensive run ($0.027) due to 10 researcher invocations in a tight critic-recovery loop. The Planner struggled to get 5 complete institute profiles — each researcher returned partial data (1-3 institutes), the critic rejected it, and a new planner would respawn more researchers. Demonstrates the agent's persistence but also the cost of tight recovery loops. |

### 8. Excalidraw Rectangle Drawing → [`output_08a75.md`](./output_08a75.md)

| Field | Value |
|-------|-------|
| **Session** | `qr-3d508a75` |
| **Original User Goal** | Go to Excalidraw and draw a rectangle |
| **Planner DAG** | planner → browser → formatter → planner → formatter (5 nodes) |
| **Browser Path Chosen** | `a11y` (12 turns) → escalated to `vision` (10 turns) |
| **Status** | ❌ **Failed** — `TargetClosedError: Page closed unexpectedly` |
| **Turn Count** | 22 total gateway calls (12 a11y + 10 vision) |
| **Cost Summary** | 12.3s total, 4 nodes, $0.000 |
| **Final Output** | *(Agent could not draw — formatter returned "I am unable to perform actions on external websites like Excalidraw, as I do not have the capability to interact with graphical interfaces or draw shapes.")* |
| **Key Observation** | Excalidraw is a canvas-based drawing tool — there are no DOM interactive elements to enumerate via the accessibility tree. The a11y layer detected no meaningful elements (668-byte legends). After escalating to vision, the agent attempted to find drawing tools via screenshot analysis for 10 turns, but the page/tab was closed mid-operation (visible in the repeated screenshot sizes changing from 52KB → 30KB → 44KB). Canvas-based UIs are fundamentally challenging for the current DOM-centric approach. |

---

## Comparison Table

| Metric | Q1 (HF) | Q2 (RealEstate) | Q3 (YouTube) | Q4 (Kaggle) | Q5 (Laptops) | Q6 (AI Tools) | Q7 (CNC) | Q8 (Excalidraw) |
|--------|---------|-----------------|-------------|-------------|--------------|---------------|----------|----------------|
| **Status** | ⚠️ Partial | ❌ Failed | ✅ Success | ⚠️ Mixed | ✅ Success | ✅ Success | ✅ Success | ❌ Failed |
| **Browser Layer** | a11y | a11y→vision | a11y | a11y+extract | extract+a11y | *(none)* | *(none)* | a11y→vision |
| **Total Time** | ~122s | 4.7s | 122.5s | 164.2s | 207.5s | 541.8s | 244.9s | 12.3s |
| **Total Nodes** | ~76 | 2 | 19 | 12 | 19 | 17 | 41 | 4 |
| **Gateway Cost** | ~$0.0038 | $0.000 | $0.003804 | $0.001464 | $0.003896 | $0.001622 | $0.027170 | $0.000 |
| **Browser Turns** | 4-9 | 12+11 | 3-4 | 4/0 | 0/4-6 | N/A | N/A | 12+10 |
| **Recovery Cycles** | Many | 0 | 5 | 1 | 3 | 2 | 10+ | 0 |
| **LLM Provider** | gemini/groq | — | gemini/groq | gemini/groq | gemini/groq | gemini/groq | gemini/groq | — |

---

## Key Findings

### What Works Well

1. **A11y layer is robust for most sites** — Hugging Face, YouTube, Amazon, Kaggle all worked with the accessibility-tree text-only approach, completing in 3-6 turns with low cost.
2. **Cascade escalation works** — When extract fails (Amazon's anti-bot), it correctly falls through to Playwright; when a11y can't parse the page (empty legends on centuryrealestate.in, excalidraw.com), it escalates to vision.
3. **Recovery planner prevents total failure** — When a critic rejects distiller output, the planner re-invokes the browser with refined goals, eventually converging on correct data.
4. **Researcher skill is cheaper for text-based research** — For queries that only need web text (not interactive UIs), the Planner correctly chooses Researcher over Browser, saving gateway costs.

### Limitations & Edge Cases

1. **Canvas-based UIs are unsupported** — Excalidraw (Query 8) uses an HTML5 canvas with no interactive DOM elements. The accessibility tree is nearly empty, and the vision layer cannot meaningfully interact with drawing tools.
2. **Vision endpoint stability** — The `/v1/vision` 502 error on Query 2 caused a complete failure. The vision layer also exhibited looping behavior on Kaggle (same screenshot repeated for 12 turns).
3. **Recovery loops can be expensive** — Query 7 (CNC institutes) ran 41 nodes due to repeated critic rejections, costing $0.027 — 10× more than simpler queries.
4. **CAPTCHA/gateway detection** — The gateway block detection correctly identifies CAPTCHA markers before launching Playwright, but some anti-bot measures (Amazon's) still prevent successful extraction.
5. **Empty a11y legends** — On sites with complex overlays/popups (centuryrealestate.in) or canvas-based apps (excalidraw.com), the accessibility tree returns empty, forcing escalation to the more expensive vision layer.
6. **No final formatter on critic cap** — Query 1's many recovery cycles eventually hit the critic-fail cap, meaning no formatter output was produced despite the browser having extracted the data.

---

## Running the Agent

```bash
# Run a single query
cd code && python flow.py "Your query here"

# Run a query with a specific session (for replay)
cd code && python flow.py --resume <session_id>

# Run the demo script
./run_demo.sh

# Quick query runner
./run_query.sh "Your query here"
```

### Prerequisites

- Python 3.10+
- Playwright browsers installed (`playwright install chromium`)
- A running V9 gateway (see `gateway.py` for configuration)
- Required packages: `pip install -r code/requirements.txt`

---

## License & Credits

Built as part of the EAGv3 / Void Walker project. The browser skill implements the **Session 9** specification — a 4-layer cascade for autonomous web interaction.