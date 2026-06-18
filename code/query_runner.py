"""Run one query through the void_walker agent and write a structured
8-section report to output.md.

Usage:
    uv run python query_runner.py "Compare 3 laptops under ₹80,000."
    uv run python query_runner.py "Compare 5 AI coding tools by free plan and paid plan."

The output.md contains:
  1. Original user goal
  2. Planner DAG
  3. Browser path chosen
  4. Browser actions taken
  5. Screenshots or page-state logs
  6. Extracted data
  7. Final comparison table
  8. Turn count and cost summary
"""

from __future__ import annotations

import asyncio
import datetime
import json
import os
import sys
import uuid

import httpx

from flow import Executor
from gateway import GATEWAY_URL
from persistence import SessionStore
from schemas import AgentResult, NodeState


# ── helpers ───────────────────────────────────────────────────────────────────

def _section(title: str, body: str, level: int = 2) -> str:
    prefix = "#" * level
    return f"\n{prefix} {title}\n\n{body}\n"


def _code(text: str, lang: str = "") -> str:
    return f"```{lang}\n{text}\n```\n"


def _find_node(states: list[NodeState], skill: str) -> NodeState | None:
    return next((s for s in states if s.skill == skill), None)


def _find_nodes(states: list[NodeState], skill: str) -> list[NodeState]:
    return [s for s in states if s.skill == skill]


def _browser_output(state: NodeState) -> dict | None:
    """Extract BrowserOutput dict from a node state, if it is a browser node."""
    if state.result and isinstance(state.result.output, dict):
        out = state.result.output
        if "path" in out and "url" in out:
            return out
    return None


# ── cost from gateway ─────────────────────────────────────────────────────────

def _fetch_cost_by_agent(session_id: str) -> dict[str, dict] | None:
    """Query the V9 gateway's cost-by-agent endpoint for this session.
    The gateway returns a list like:
      [{"agent": "planner", "calls": 1, "tokens": "2197 / 239", "dollars": "$0.000000"}, ...]
    Normalises to a dict keyed by agent name for easy lookup.
    Returns None if the gateway is unreachable or returns an error.
    """
    try:
        r = httpx.get(
            f"{GATEWAY_URL}/v1/cost/by_agent",
            params={"session": session_id},
            timeout=5.0,
        )
        r.raise_for_status()
        data = r.json()
        # Normalise: if the gateway returns a list, convert to dict.
        if isinstance(data, list):
            return {item["agent"]: item for item in data if "agent" in item}
        # Already a dict keyed by agent (unlikely but safe to handle).
        if isinstance(data, dict):
            return data
        print(f"[query_runner] unexpected cost response type: {type(data).__name__}",
              file=sys.stderr)
        return None
    except Exception as exc:
        print(f"[query_runner] cost endpoint unavailable: {type(exc).__name__}: {exc}",
              file=sys.stderr)
        return None


def _format_cost_summary(states: list[NodeState], sid: str) -> str:
    """Build a turn count and cost summary table from node states + gateway cost data."""
    total_elapsed = 0.0
    total_cost_dollars = 0.0
    rows: list[str] = []

    # Fetch authoritative cost data from the gateway ledger.
    cost_by_agent = _fetch_cost_by_agent(sid) or {}

    for s in states:
        if not s.result:
            continue
        r = s.result
        skill = s.skill
        status = s.status
        elapsed = r.elapsed_s or 0.0
        total_elapsed += elapsed

        # Use gateway cost data when available (it is the authoritative source
        # per VALIDATION.md); fall back to AgentResult.cost otherwise.
        raw_costs = cost_by_agent.get(skill, {})
        # Normalise: the gateway sometimes wraps a single record in a list.
        if isinstance(raw_costs, list):
            agent_costs = raw_costs[0] if raw_costs else {}
        elif isinstance(raw_costs, dict):
            agent_costs = raw_costs
        else:
            agent_costs = {}
        calls = agent_costs.get("calls", "")
        tokens = agent_costs.get("tokens", "")
        raw_dollars = agent_costs.get("dollars", "")
        # Parse dollar cost: could be string ("$0.012300") or raw float (0.0).
        if isinstance(raw_dollars, (int, float)):
            total_cost_dollars += float(raw_dollars)
        elif isinstance(raw_dollars, str) and raw_dollars.startswith("$"):
            try:
                total_cost_dollars += float(raw_dollars[1:])
            except (ValueError, TypeError):
                pass
        # Construct gateway-ledger column when available.
        if calls or tokens:
            ledger_col = f"{calls} calls {tokens}"
        else:
            ledger_col = f"${r.cost:.4f} (from node)"

        provider = r.provider or "—"
        bo = _browser_output(s)
        turns = str(bo.get("turns", "")) if bo else ""

        rows.append(
            f"| {s.node_id:8s} | {skill:18s} | {status:8s} | "
            f"{elapsed:6.1f}s | {ledger_col:32s} | {provider:12s} | {turns:4s} |"
        )

    header = (
        "| Node      | Skill              | Status   | Time    | Gateway Ledger (calls / tokens) | Provider      | Turns |\n"
        "| :-------- | :----------------- | :------- | :------ | :------------------------------- | :------------ | :---- |"
    )
    footer = (
        f"| **Total** | **{len(states)} nodes** |          | "
        f"**{total_elapsed:.1f}s** | **${total_cost_dollars:.6f}** |                |       |"
    )
    return "\n".join([header] + rows + [footer])


def _format_planner_dag(states: list[NodeState], graph_data: dict | None) -> str:
    """Reconstruct the DAG from graph.json node-link data.
    The graph uses NetworkX's node_link_data format with `source`/`target` keys
    on edges (confirmed from actual graph.json in state/sessions/).
    """
    lines: list[str] = []
    if graph_data and "nodes" in graph_data:
        # Build a lookup by id.
        nodes: dict[str, dict] = {}
        for n in graph_data["nodes"]:
            nodes[n["id"]] = n
        edges: list[tuple[str, str]] = []
        for e in graph_data.get("edges", []):
            edges.append((e["source"], e["target"]))

        lines.append("**Graph nodes:**\n")
        for nid in sorted(nodes):
            attrs = nodes[nid]
            skill = attrs.get("skill", "?")
            status = attrs.get("status", "?")
            inputs = attrs.get("inputs", [])
            lines.append(f"- `{nid}` **{skill}** [{status}]  inputs={inputs}")

        if edges:
            lines.append("\n**Edges (data flow):**\n")
            for src, tgt in edges:
                lines.append(f"  {src} → {tgt}")
    else:
        # Fallback: reconstruct from node states.
        lines.append("**Execution order (from persisted nodes):**\n")
        for s in states:
            deps = s.inputs or []
            dep_str = ", ".join(deps) if deps else "(none)"
            lines.append(f"- `{s.node_id}` **{s.skill}** [{s.status}]  ← {dep_str}")
    return "\n".join(lines)


def _format_browser_actions(bo: dict) -> str:
    """Format browser action steps from BrowserOutput.actions."""
    actions = bo.get("actions", [])
    if not actions:
        return "_(no actions recorded)_\n"
    lines: list[str] = []
    for step in actions:
        turn = step.get("turn", "?")
        raw_actions = step.get("actions", [])
        outcome = step.get("outcome", "")
        acts_str = "; ".join(str(a) for a in raw_actions) if raw_actions else "—"
        lines.append(f"  **Turn {turn}:** `{acts_str}`  → _outcome: {outcome}_")
    return "\n".join(lines) + "\n"


def _format_browser_screenshots(sid: str, code_dir: str) -> str:
    """List screenshot artifacts from the browser session directory.
    Path: state/sessions/<sid>/browser/<timestamp>/<layer>/...
    """
    session_browser_dir = os.path.join(code_dir, "state", "sessions", sid, "browser")
    if not os.path.isdir(session_browser_dir):
        return "_(no browser artifacts found)_\n"

    lines: list[str] = []
    for ts_dir in sorted(os.listdir(session_browser_dir)):
        ts_path = os.path.join(session_browser_dir, ts_dir)
        if not os.path.isdir(ts_path):
            continue
        lines.append(f"\n**Run directory: `{ts_dir}`**\n")
        for layer in sorted(os.listdir(ts_path)):
            layer_path = os.path.join(ts_path, layer)
            if not os.path.isdir(layer_path):
                continue
            lines.append(f"**Layer: `{layer}`**\n")
            for fname in sorted(os.listdir(layer_path)):
                fpath = os.path.join(layer_path, fname)
                if os.path.isfile(fpath):
                    size = os.path.getsize(fpath)
                    if size < 1024:
                        fsize = f"{size:,} bytes"
                    else:
                        fsize = f"{size/1024:.1f} KB"
                    lines.append(f"- `{fname}` ({fsize})\n")
    if not lines:
        return "_(no browser artifacts found)_\n"
    return "".join(lines)


# ── report builder ───────────────────────────────────────────────────────────

def build_report(query: str, sid: str, code_dir: str) -> str | None:
    """Build the 8-section Markdown report from a completed session.
    Returns the report string, or None if the session cannot be read."""
    store = SessionStore(sid)
    states = store.read_all_nodes()
    if not states:
        return None

    graph_data = None
    graph_path = store.graph_path
    if graph_path.exists():
        try:
            graph_data = json.loads(graph_path.read_text())
        except Exception as exc:
            print(f"[query_runner] could not parse graph.json: {exc}", file=sys.stderr)

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    parts: list[str] = [
        "# Query Report",
        "",
        f"**Session:** `{sid}`",
        f"**Query:** {query}",
        f"**Generated:** {timestamp}",
        "",
        "---",
    ]

    # 1. Original user goal
    parts.append(_section("1. Original User Goal", f"> {query}"))

    # 2. Planner DAG
    dag_text = _format_planner_dag(states, graph_data)
    parts.append(_section("2. Planner DAG", dag_text))

    # 3. Browser path chosen
    browser_nodes = [s for s in states if s.skill == "browser"]
    if browser_nodes:
        browser_section: list[str] = []
        for bn in browser_nodes:
            bo = _browser_output(bn)
            if bo:
                path = bo.get("path", "?")
                url = bo.get("url", "")
                goal = bo.get("goal", "")
                success = "✅" if bn.status == "complete" else "❌"
                error = bn.result.error if bn.result and bn.result.error else ""
                browser_section.append(
                    f"**Node {bn.node_id}** {success}\n\n"
                    f"- **URL:** `{url}`\n"
                    f"- **Goal:** {goal}\n"
                    f"- **Path (layer chosen):** `{path}`\n"
                    f"- **Final URL:** `{bo.get('final_url', '')}`\n"
                    f"- **Turns:** {bo.get('turns', 0)}\n"
                    + (f"- **Error:** {error}\n" if error else "")
                )
            else:
                browser_section.append(
                    f"**Node {bn.node_id}**\n\n"
                    f"- **Status:** {bn.status}\n"
                    + (f"- **Error:** {bn.result.error}\n"
                       if bn.result and bn.result.error else "")
                )
        parts.append(_section("3. Browser Path Chosen",
                              "\n---\n".join(browser_section)))

        # 4. Browser actions taken
        actions_section: list[str] = []
        for bn in browser_nodes:
            bo = _browser_output(bn)
            if bo:
                acts = _format_browser_actions(bo)
                actions_section.append(f"**Node {bn.node_id}**\n\n{acts}")
        parts.append(_section("4. Browser Actions Taken",
                              "\n---\n".join(actions_section)))

        # 5. Screenshots or page-state logs
        ss_section: list[str] = []
        for bn in browser_nodes:
            ss = _format_browser_screenshots(sid, code_dir)
            ss_section.append(f"**Node {bn.node_id}**\n\n{ss}")
        parts.append(_section("5. Screenshots / Page-State Logs",
                              "\n---\n".join(ss_section)))
    else:
        parts.append(_section("3. Browser Path Chosen",
                              "_(No Browser skill was used in this query.)_"))
        parts.append(_section("4. Browser Actions Taken",
                              "_(No Browser skill was used in this query.)_"))
        parts.append(_section("5. Screenshots / Page-State Logs",
                              "_(No Browser skill was used in this query.)_"))

    # 6. Extracted data (from Researcher and Distiller nodes)
    extracted: list[str] = []
    for s in _find_nodes(states, "distiller"):
        if s.result and s.result.output:
            fields = s.result.output.get("fields", {})
            rationale = s.result.output.get("rationale", "")
            if fields:
                extracted.append(
                    f"**Node {s.node_id} — Distiller**\n\n"
                    + _code(json.dumps(fields, indent=2, ensure_ascii=False), "json")
                    + f"\n*Rationale: {rationale}*\n"
                )
            else:
                extracted.append(
                    f"**Node {s.node_id} — Distiller**\n\n"
                    f"*Rationale: {rationale}*\n"
                )
    for s in _find_nodes(states, "researcher"):
        if s.result and s.result.output:
            findings = s.result.output.get("findings", "")
            question = s.result.output.get("question", "")
            sources = s.result.output.get("sources", [])
            if findings and findings != "(not found)":
                src_lines = "\n".join(
                    f"  - [{src.get('title', '?')}]({src.get('url', '#')})"
                    for src in sources[:5]
                )
                extracted.append(
                    f"**Node {s.node_id} — Researcher**\n\n"
                    f"*Question:* {question}\n\n"
                    f"{findings}\n\n"
                    f"*Sources:*\n{src_lines}\n"
                )
    if extracted:
        parts.append(_section("6. Extracted Data",
                              "\n---\n".join(extracted)))
    else:
        parts.append(_section("6. Extracted Data",
                              "_(No extractable data found.)_"))

    # 7. Final comparison table (the formatter's final_answer)
    formatter = _find_node(states, "formatter")
    if formatter and formatter.result and formatter.result.output:
        fa = formatter.result.output.get("final_answer", "")
        if fa:
            parts.append(_section("7. Final Comparison Table", fa.strip()))
        else:
            parts.append(_section("7. Final Comparison Table",
                                  "_(Formatter produced no final_answer.)_"))
    else:
        parts.append(_section("7. Final Comparison Table",
                              "_(No formatter output available.)_"))

    # 8. Turn count and cost summary (uses gateway cost endpoint per VALIDATION.md)
    summary = _format_cost_summary(states, sid)
    parts.append(_section("8. Turn Count & Cost Summary", summary))

    return "\n".join(parts) + "\n"


# ── main entry point ──────────────────────────────────────────────────────────

async def run_query(query: str, sid: str) -> str:
    """Run the query through the full agent DAG and return the final answer."""
    return await Executor().run(query, session_id=sid)


def main() -> None:
    query = " ".join(sys.argv[1:]).strip()
    if not query:
        print("Usage: uv run python query_runner.py \"<your query>\"")
        sys.exit(1)

    sid = f"qr-{uuid.uuid4().hex[:8]}"
    code_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(code_dir)

    print(f"[query_runner] session: {sid}")
    print(f"[query_runner] running agent for: {query[:120]}...")
    asyncio.run(run_query(query, sid))

    report = build_report(query, sid, code_dir)
    if report is None:
        print(f"[query_runner] ERROR: could not read session {sid} after run",
              file=sys.stderr)
        sys.exit(1)

    # Unique output file per run using the last 5 chars of the session id.
    out_name = f"output_{sid[-5:]}.md"
    out_path = os.path.join(project_root, out_name)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(report)

    print(f"[query_runner] structured report written to {out_path}")


if __name__ == "__main__":
    main()
