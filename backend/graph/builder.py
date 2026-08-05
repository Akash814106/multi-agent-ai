from langgraph.graph import StateGraph, END

from backend.graph.state import AgentState

from backend.graph.nodes import (
    query_router_node,
    query_enhancement_node,
    memory_node,
    planner_node,
    parallel_task_node,
    final_summary_node,
    memory_save_node,
    direct_response_node,
)

builder = StateGraph(AgentState)


# Nodes

builder.add_node(
    "query_router",
    query_router_node,
)

builder.add_node(
    "query_enhancement",
    query_enhancement_node,
)

builder.add_node(
    "memory",
    memory_node,
)

builder.add_node(
    "planner",
    planner_node,
)

builder.add_node(
    "parallel_tasks",
    parallel_task_node,
)

builder.add_node(
    "summary",
    final_summary_node,
)

builder.add_node(
    "memory_save",
    memory_save_node,
)

builder.add_node(
    "direct_response",
    direct_response_node,
)


# Entry Point

builder.set_entry_point(
    "query_router"
)


# Conditional Routing

def route_query(state: AgentState):

    if state.get("router_decision") == "DIRECT_RESPONSE":
        return "direct"

    return "workflow"


builder.add_conditional_edges(

    "query_router",

    route_query,

    {

        "direct": "direct_response",

        "workflow": "query_enhancement",

    },

)


# Workflow Path

builder.add_edge(
    "query_enhancement",
    "memory",
)

builder.add_edge(
    "memory",
    "planner",
)

builder.add_edge(
    "planner",
    "parallel_tasks",
)

builder.add_edge(
    "parallel_tasks",
    "summary",
)

builder.add_edge(
    "summary",
    "memory_save",
)

builder.add_edge(
    "memory_save",
    END,
)


# Direct Path

builder.add_edge(
    "direct_response",
    "memory_save",
)

graph = builder.compile()