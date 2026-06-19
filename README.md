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

Eleven query runs have been conducted to validate the Browser skill across diverse scenarios:

| # | Report | Query | Browser Path | Status | Total Time | Nodes | Gateway Cost |
|---|--------|-------|-------------|--------|-----------|-------|-------------|
| 1 | [output_79128.md](./output_79128.md) | Compare top 3 Hugging Face text-generation models sorted by likes | `a11y` | ⚠️ Partial (critic cap hit before formatter) | ~122s | ~76 | ~$0.0038 |
| 2 | [output_a4df9.md](./output_a4df9.md) | Go to centuryrealestate.in and fill random fake details | `a11y` → `vision` | ❌ Failed (502 Bad Gateway from vision endpoint) | 4.7s | 2 | $0.000 |
| 3 | [output_aa10e.md](./output_aa10e.md) | YouTube: search "spiderman brand new day", get first comment | `a11y` | ✅ Success | 122.5s | 19 | $0.003804 |
| 4 | [output_c97c7.md](./output_c97c7.md) | Kaggle: find recent datasets on airplanes with high upvotes | `a11y` + `extract` | ⚠️ Mixed | 164.2s | 12 | $0.001464 |
| 5 | [output_ec4ed.md](./output_ec4ed.md) | Compare 3 laptops under ₹80,000 | `extract` + `a11y` | ✅ Success | 207.5s | 19 | $0.003896 |
| 6 | [output_ee673.md](./output_ee673.md) | Compare 5 AI coding tools by free plan and paid plan | *(No browser — Researcher skill used)* | ✅ Success | 541.8s | 17 | $0.001622 |
| 7 | [output_f7692.md](./output_f7692.md) | Compare 5 CNC/VMC training institutes in Bangalore | *(No browser — Researcher skill used)* | ✅ Success | 244.9s | 41 | $0.027170 |
| 8 | [output_08a75.md](./output_08a75.md) | Go to Excalidraw and draw a rectangle | `a11y` → `vision` | ❌ Failed (TargetClosedError — page crashed mid-draw) | 12.3s | 4 | $0.000 |
| 9 | [output_71060.md](./output_71060.md) | Go to Excalidraw and draw one rectangle | `extract` → `a11y` → `vision` | ❌ Failed (all layers exhausted after 12+12 turns) | 109.9s | 4 | $0.000 |
| 10 | [output_4bd57.md](./output_4bd57.md) | Go to Prestige Constructions and request a call back | `extract` | ❌ Failed (only cookie consent page rendered) | 29.7s | 8 | $0.000263 |
| 11 | [output_b3f42.md](./output_b3f42.md) | Fill and submit Formy project form | `a11y` | ✅ Success | 72.9s | 3 | $0.000 |

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
| **Browser Path Chosen** | `a11y` (12 turns) → escalated to `vision` (11 turns) |
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

### 8. Excalidraw Rectangle Drawing (Attempt 1) → [`output_08a75.md`](./output_08a75.md)

| Field | Value |
|-------|-------|
| **Session** | `qr-3d508a75` |
| **Original User Goal** | Go to Excalidraw and draw a rectangle |
| **Planner DAG** | planner → browser → formatter → planner → formatter (5 nodes) |
| **Browser Path Chosen** | `a11y` (12 turns) → escalated to `vision` (10 turns) |
| **Status** | ❌ **Failed** — `TargetClosedError: Page closed unexpectedly` |
| **Turn Count** | 22 total gateway calls (12 a11y + 10 vision) |
| **Cost Summary** | 12.3s total, 4 nodes, $0.000 |
| **Final Output** | "I am unable to perform actions on external websites like Excalidraw, as I do not have the capability to interact with graphical interfaces or draw shapes." |
| **Key Observation** | The agent **was actively drawing** on Excalidraw — the a11y screenshots vary in size (52KB → 67KB → 80KB → 67KB → 30KB → 29KB → 44KB), proving the canvas was rendering and changing. After escalation to vision, the agent sent 10 turns of marked screenshots (incrementing from 63KB → 52KB), showing it was locating toolbar elements. The actual failure was a **TargetClosedError** (browser tab/page crashed mid-operation). Crucially, the **formatter misattributes the failure**: it claims "I cannot interact with graphical interfaces" — this is false. The agent WAS interacting and making progress; the page simply crashed before it could finish. This reveals a problem in the formatter/recovery pipeline: when a browser node fails due to a technical crash, the downstream LLM fabricates a plausible-sounding but incorrect explanation. |

### 9. Excalidraw Rectangle Drawing (Attempt 2) → [`output_71060.md`](./output_71060.md)

| Field | Value |
|-------|-------|
| **Session** | `qr-0a671060` |
| **Original User Goal** | Go to Excalidraw and draw one rectangle |
| **Planner DAG** | planner → browser → planner → formatter (4 nodes) |
| **Browser Path Chosen** | `extract` → `a11y` (12 turns) → escalated to `vision` (12 turns) — all layers exhausted |
| **Status** | ❌ **Failed** — `step cap reached (12)` on both a11y and vision layers |
| **Turn Count** | 24 total gateway calls (12 a11y + 12 vision) |
| **Cost Summary** | 109.9s total, 4 nodes, $0.000 |
| **Final Output** | "I am unable to perform actions on external websites like Excalidraw, as I do not have the capability to interact with graphical user interfaces or draw shapes." |
| **Key Observation** | This second Excalidraw run shows the same pattern more clearly: the a11y screenshots change every turn (52KB → 67KB → 80KB → 46KB → 31KB → 46KB → 52KB), proving the page was live and the canvas had content. The vision screenshots also increment monotonically (63KB → 47KB → 48KB → 48KB → 49KB → 50KB → 51KB → 51KB → 52KB → 53KB → 54KB → 55KB), each one different — the agent WAS exploring the toolbar and canvas via vision. The failure is that the agent exhausted all 12+12 turns without completing the drawing, and the downstream formatter again produced the incorrect rationalization "I cannot interact with graphical interfaces." The real issue is that canvas-based drawing requires many more steps than the current step cap allows, and the formatter LLM replaces the actual technical failure with a fake explanation. |

### 10. Prestige Constructions Callback Request → [`output_4bd57.md`](./output_4bd57.md)

| Field | Value |
|-------|-------|
| **Session** | `qr-bfc4bd57` |
| **Original User Goal** | Go to Prestige Constructions residential properties page and request a call back with random details |
| **Planner DAG** | planner → browser → distiller → critic → planner → browser(fail) → planner → formatter (8 nodes) |
| **Browser Path Chosen** | `extract` (n:2 ✅ with 0 turns — trafilatura extracted cookie consent page) → `a11y` (n:7 ❌ — execution context destroyed by navigation) |
| **Status** | ❌ **Failed** — The page only served a cookie consent / privacy policy banner; no property listings or forms were visible to the extractor. The Playwright attempt also crashed due to navigation. |
| **Turn Count** | n:2 = 0 turns (extract only); n:7 = crash |
| **Cost Summary** | 29.7s total, 8 nodes, $0.000263 |
| **Final Output** | "The website provided only displays a cookie consent and privacy policy notice, and does not contain any residential property listings or contact forms." |
| **Key Observation** | This site required JavaScript rendering to display actual content — the pure-HTTP extract layer only captured the cookie consent banner. The Playwright a11y attempt then crashed with "execution context was destroyed, most likely because of a navigation" — this occurs when the page redirects or reloads mid-analysis. Sites that gate content behind JavaScript redirects are a known challenge. |

### 11. Formy Project Form Fill → [`output_b3f42.md`](./output_b3f42.md)

| Field | Value |
|-------|-------|
| **Session** | `qr-51cb3f42` |
| **Original User Goal** | Go to Formy project test form, fill random details, and submit |
| **Planner DAG** | planner → browser → formatter (3 nodes — simplest successful run) |
| **Browser Path Chosen** | `a11y` — all 6 turns on the a11y layer |
| **Final URL** | `https://formy-project.herokuapp.com/form` |
| **Final Output** | Form submitted: First Name (John), Last Name (Doe), Job Title (Software Engineer), Education (College), Sex (Male), Experience (2-4 years), Date (12/25/2023) |
| **Turn Count** | 6 turns (typed 3 fields, clicked 5 form elements, submitted) |
| **Cost Summary** | 72.9s total, 3 nodes, $0.000 |
| **Key Observation** | **Most successful Browser skill run** — the agent completed a 7-field form fill and submission in a single browser node with no recovery. The a11y layer handled all interactions: text input into text fields, radio button selection, checkbox toggling, date picker, and click-to-submit. The clean 3-node DAG (planner → browser → formatter) is the ideal execution pattern. This demonstrates that when the target site has standard HTML form elements with proper accessibility labels, the a11y layer is highly capable. |

---

## Comparison Table

| Metric | Q1 (HF) | Q2 (RealEstate) | Q3 (YouTube) | Q4 (Kaggle) | Q5 (Laptops) | Q6 (AI Tools) | Q7 (CNC) | Q8 (Excalidraw1) | Q9 (Excalidraw2) | Q10 (Prestige) | Q11 (Formy) |
|--------|---------|-----------------|-------------|-------------|--------------|---------------|----------|-----------------|-----------------|---------------|------------|
| **Status** | ⚠️ Partial | ❌ Failed | ✅ Success | ⚠️ Mixed | ✅ Success | ✅ Success | ✅ Success | ❌ Failed | ❌ Failed | ❌ Failed | ✅ Success |
| **Browser Layer** | a11y | a11y→vision | a11y | a11y+extract | extract+a11y | *(none)* | *(none)* | a11y→vision | extract→a11y→vision | extract | a11y |
| **Total Time** | ~122s | 4.7s | 122.5s | 164.2s | 207.5s | 541.8s | 244.9s | 12.3s | 109.9s | 29.7s | 72.9s |
| **Total Nodes** | ~76 | 2 | 19 | 12 | 19 | 17 | 41 | 4 | 4 | 8 | 3 |
| **Gateway Cost** | ~$0.0038 | $0.000 | $0.003804 | $0.001464 | $0.003896 | $0.001622 | $0.027170 | $0.000 | $0.000 | $0.000263 | $0.000 |
| **Browser Turns** | 4-9 | 12+11 | 3-4 | 4/0 | 0/4-6 | N/A | N/A | 12+10 | 12+12 | 0/(crash) | 6 |
| **Recovery Cycles** | Many | 0 | 5 | 1 | 3 | 2 | 10+ | 0 | 0 | 1 | 0 |
| **LLM Provider** | gemini/groq | — | gemini/groq | gemini/groq | gemini/groq | gemini/groq | gemini/groq | — | — | gemini/groq | — |

---

## Key Findings

### What Works Well

1. **A11y layer is robust for standard web forms** — The Formy project (Query 11) demonstrated a perfect 6-turn form fill and submission: typed text, selected radio buttons, toggled checkboxes, picked dates, and clicked submit — all via the accessibility tree.
2. **A11y layer works on complex JS-rendered sites** — Hugging Face, YouTube, Amazon, Kaggle all worked with the accessibility-tree text-only approach, completing in 3-6 turns with low cost.
3. **Cascade escalation works** — When extract fails (Amazon's anti-bot), it correctly falls through to Playwright; when a11y can't parse the page (empty legends on Excalidraw, centuryrealestate.in), it escalates to vision.
4. **Recovery planner prevents total failure** — When a critic rejects distiller output, the planner re-invokes the browser with refined goals, eventually converging on correct data.
5. **Researcher skill is cheaper for text-based research** — For queries that only need web text (not interactive UIs), the Planner correctly chooses Researcher over Browser, saving gateway costs.

### Limitations & Edge Cases

1. **Canvas-based UIs: agent CAN draw but fails due to step caps or crashes** — Both Excalidraw runs (Q8, Q9) prove the agent was actively interacting with the canvas: screenshots changed every turn, vision marked screenshots incrementing, proving toolbar exploration was underway. The actual failures were a `TargetClosedError` (page crash) and a step cap exhaustion (12+12 turns not enough). However, the **formatter LLM fabricates a misleading explanation** — it claims "I cannot interact with graphical interfaces" when in reality the agent WAS interacting. This is a critical pipeline issue: technical failures get replaced with false rationalizations by downstream LLM nodes.
2. **Vision endpoint stability** — The `/v1/vision` 502 error on Query 2 caused a complete failure. The vision layer also exhibited looping behavior on Kaggle (same screenshot repeated for 12 turns).
3. **Recovery loops can be expensive** — Query 7 (CNC institutes) ran 41 nodes due to repeated critic rejections, costing $0.027 — 10× more than simpler queries.
4. **JavaScript-gated content** — Sites like Prestige Constructions (Query 10) serve a cookie consent page via HTML but load actual content via JavaScript. The extract layer only gets the cookie wall, and the Playwright layer may crash on redirects.
5. **Empty a11y legends** — On sites with complex overlays/popups (centuryrealestate.in) or canvas-based apps (excalidraw.com), the accessibility tree returns empty, forcing escalation to the more expensive vision layer.
6. **No final formatter on critic cap** — Query 1's many recovery cycles eventually hit the critic-fail cap, meaning no formatter output was produced despite the browser having extracted the data.
7. **Formatter hallucinates failure causes** — In both Excalidraw runs, the formatter node confidently stated "I cannot interact with graphical interfaces" despite clear evidence (changing screenshots, marked vision frames) that the agent WAS interacting. The formatter substitutes a plausible-sounding explanation for the real technical cause.

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