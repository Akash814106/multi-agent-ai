from concurrent.futures import ThreadPoolExecutor

from backend.graph.state import AgentState

from backend.memory.chroma_memory import (
    retrieve_memory,
    save_memory,
)

from backend.workflows.task_processor import process_task

from backend.agents.control_agents.query_router_agent import (
    query_router_agent,
)

from backend.agents.control_agents.query_enhancement_agent import (
    query_enhancement_agent,
)

from backend.agents.control_agents.memory_router_agent import (
    memory_router_agent,
)

from backend.agents.control_agents.memory_save_agent import (
    memory_save_agent,
)

from backend.agents.worker_agents.planner_agent import (
    planner_agent,
)

from backend.agents.worker_agents.summary_agent import (
    summary_agent,
)

from backend.agents.worker_agents.direct_response_agent import (
    direct_response_agent,
)

from backend.utils.task_parser import extract_tasks

MAX_WORKERS = 3

# def query_router_node(state):
#     print(">>> Entered query_router_node")
#     router_result = query_router_agent(state["user_query"])
#     print(">>> Router:", router_result)
#     return {"router_decision": router_result["decision"]}

def query_router_node(state: AgentState):

    router_result = query_router_agent(
        state["user_query"]
    )

    return {
        "router_decision": router_result["decision"]
    }

def query_enhancement_node(state: AgentState):

    enhanced_user_query = query_enhancement_agent(
        state["user_query"]
    )

    return {
        "enhanced_user_query": enhanced_user_query
    }

def memory_node(state: AgentState):

    memories = retrieve_memory(
        state["enhanced_user_query"],
        state["current_user"],
    )

    if memories and memories[0]:

        memory_context = "\n".join(
            memories[0]
        )

    else:

        memory_context = ""

    enhanced_query = state["enhanced_user_query"]

    memory_decision = "SKIP_MEMORY"

    if memory_context:

        memory_decision = memory_router_agent(

            state["enhanced_user_query"],

            memory_context,

        )

        if memory_decision == "USE_MEMORY":

            enhanced_query = f"""
Memory:
{memory_context}

Question:
{state["enhanced_user_query"]}
"""

    return {

        "memory_context": memory_context,

        "memory_decision": memory_decision,

        "enhanced_query": enhanced_query,

    }

def planner_node(state: AgentState):

    plan = planner_agent(
        state.get(
            "enhanced_query",
            state["enhanced_user_query"]
        )
    )

    goal = ""

    lines = plan.splitlines()

    for i, line in enumerate(lines):

        if line.startswith("Goal:"):

            extracted = line.replace(
                "Goal:",
                ""
            ).strip()

            if extracted:

                goal = extracted

            elif i + 1 < len(lines):

                goal = lines[i + 1].strip()

            break

    tasks = extract_tasks(plan)

    return {

        "goal": goal,

        "plan": plan,

        "tasks": tasks,

    }

def parallel_task_node(state: AgentState):

    all_results = []

    summary_list = []

    revision_executed = 0

    revision_skipped = 0

    failed_tasks = 0

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:

        futures = [

            executor.submit(
                process_task,
                state["goal"],
                task
            )

            for task in state["tasks"]

        ]

        for future in futures:

            result = future.result()

            all_results.append(result)

            if result["status"] == "SUCCESS":

                summary_list.append(
                    result["summary"]
                )

                revision_executed += result[
                    "revision_executed"
                ]

                revision_skipped += result[
                    "revision_skipped"
                ]

            else:

                failed_tasks += 1

    metrics = dict(
        state.get("metrics", {})
    )

    metrics["task_count"] = len(state["tasks"])

    metrics["revision_executed"] = revision_executed

    metrics["revision_skipped"] = revision_skipped

    metrics["failed_tasks"] = failed_tasks

    return {

        "results": all_results,

        "summary_list": summary_list,

        "metrics": metrics,

    }

def final_summary_node(state: AgentState):

    if state["summary_list"]:

        summary = "\n".join(
            state["summary_list"]
        )

        final_summary = summary_agent(
            summary
        )

    else:

        final_summary = (
            "Workflow failed. "
            "No successful task summaries were generated."
        )

    return {

        "final_summary": final_summary

    }

def memory_save_node(state: AgentState):

    if not state.get("final_summary"):

        return {}

    if state["router_decision"] == "DIRECT_RESPONSE":

        query = state["user_query"]

    else:

        query = state.get(
            "enhanced_user_query",
            state["user_query"]
        )

    save_decision = memory_save_agent(

        query,

        state["final_summary"]

    )

    if save_decision == "SAVE_MEMORY":

        save_memory(

            state["final_summary"],

            state["current_user"]

        )

    return {}

def direct_response_node(state: AgentState):

    memories = retrieve_memory(

        state["user_query"],

        state["current_user"],

    )

    memory_context = ""

    enhanced_query = state["user_query"]

    if memories and memories[0]:

        memory_context = "\n".join(

            memories[0]

        )

        enhanced_query = f"""
Memory:
{memory_context}

Question:
{state["user_query"]}
"""

    result = direct_response_agent(
        enhanced_query
    )

    return {

        "memory_context": memory_context,

        "final_summary": result,

    }



