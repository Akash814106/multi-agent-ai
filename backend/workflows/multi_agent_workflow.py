import time
from datetime import datetime

from backend.utils.workflow_metrics import WorkflowMetrics

from backend.graph.graph import run_graph

def run_workflow(user_query, current_user):

    start_time = time.time()

    metrics = WorkflowMetrics()

    initial_state = {

        "current_user": current_user,

        "user_query": user_query,

        "enhanced_user_query": "",

        "enhanced_query": "",

        "router_decision": "",

        "memory_decision": "",

        "memory_context": "",

        "goal": "",

        "plan": "",

        "tasks": [],

        "results": [],

        "summary_list": [],

        "final_summary": "",

        "metrics": {},

    }

    state = run_graph(initial_state)
    graph_metrics = state.get("metrics", {})

    metrics.query_type = state.get(
        "router_decision",
        ""
    )

    metrics.memory_used = bool(
        state.get("memory_context")
    )

    metrics.task_count = graph_metrics.get(
        "task_count",
        0,
    )

    metrics.revision_executed = graph_metrics.get(
        "revision_executed",
        0,
    )

    metrics.revision_skipped = graph_metrics.get(
        "revision_skipped",
        0,
    )

    metrics.failed_tasks = graph_metrics.get(
        "failed_tasks",
        0,
    )

    end_time = time.time()

    metrics.execution_time = round(
        end_time - start_time,
        2,
    )

    metrics.timestamp = str(
        datetime.now()
    )

    if metrics.task_count > 0:

        metrics.avg_time_per_task = round(

            metrics.execution_time /

            metrics.task_count,

            2,

        )

        metrics.revision_rate = round(

            metrics.revision_executed /

            metrics.task_count * 100,

            2,

        )

    if state.get("router_decision") == "DIRECT_RESPONSE":

        return {

            "goal": "Direct Response",

            "memory": state.get("memory_context", ""),

            "enhanced_user_query": state.get("user_query"),

            "plan": "",

            "tasks": [],

            "results": [],

            "final_summary": state.get("final_summary"),

            "metrics": vars(metrics),

        }

    return {

        "goal": state.get("goal", ""),

        "memory": state.get("memory_context", ""),

        "enhanced_user_query": state.get("enhanced_user_query", ""),

        "plan": state.get("plan", ""),

        "tasks": state.get("tasks", []),

        "results": state.get("results", []),
        
        "final_summary": state.get("final_summary", ""),

        "metrics": vars(metrics),

        "workflow_steps": [

            "Query Routed",

            "Query Enhanced",

            "Memory Retrieved",

            "Planning Completed",

            "Research Completed",

            "Critic Completed",

            "Summary Generated",

        ],

    }