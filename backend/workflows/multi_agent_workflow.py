import time
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

from utils.workflow_metrics import WorkflowMetrics

from memory.chroma_memory import retrieve_memory,save_memory

from agents.worker_agents.planner_agent import planner_agent
from agents.worker_agents.research_agent import research_agent
from agents.worker_agents.critic_agent import critic_agent
from agents.worker_agents.revision_agent import revision_agent
from agents.worker_agents.summary_agent import summary_agent
from agents.worker_agents.direct_response_agent import direct_response_agent

from agents.control_agents.memory_router_agent import memory_router_agent
from agents.control_agents.memory_save_agent import memory_save_agent
from agents.control_agents.query_router_agent import query_router_agent
from agents.control_agents.query_enhancement_agent import query_enhancement_agent
from utils.task_parser import extract_tasks


def process_task(goal,task):
    revision_executed = 0
    revision_skipped = 0

#    print(f"Starting: {task}")

    research_input = f"""
    Goal:
    {goal}
    Task:
    {task}
    """
    research_result = research_agent(research_input)
    critic_result = critic_agent(goal,task,research_result)
    score = critic_result["score"]
    if score < 8:
        revision_result = revision_agent(goal,task,research_result,critic_result)
        revision_executed += 1
    else :
        revision_result = research_result
        revision_skipped += 1
    summary_result = summary_agent(revision_result)
    # print(f"Finished: {task}")
    
    return{
        "task":task,
        "research":research_result,
        "critic":critic_result,
        "revision":revision_result,
        "summary":summary_result,
        "revision_executed": revision_executed,
        "revision_skipped": revision_skipped
        }
    
def run_workflow(user_query):

    start_time = time.time()

    metrics = WorkflowMetrics()

    all_results = []
    summary_list = []

    router_result = query_router_agent(user_query)
    query_decision = router_result["decision"]

    metrics.query_type = query_decision

    # print("\nQuery router : \n")
    # print(router_result)

    if query_decision == "DIRECT_RESPONSE":
        result = direct_response_agent(user_query)
        save_decision = memory_save_agent(user_query,result)
        if save_decision == "SAVE_MEMORY":
            save_memory(result)
        return result
    
    elif query_decision == "MULTI_AGENT_WORKFLOW":
        print("\n--- Multi-Agent Workflow Selected ---\n")
        enhanced_user_query = query_enhancement_agent(user_query)
    else:
        print(
            f"Invalid router decision: {query_decision}. "
            "Falling back to MULTI_AGENT_WORKFLOW."
        )
        enhanced_user_query = query_enhancement_agent(user_query)
    
    
    #Enhanced query
    # print("\nEnhanced Query :\n")
    # print(enhanced_user_query)
    #Retrieve memory
    memories = retrieve_memory(enhanced_user_query)
    if memories and memories[0]:
        memory_context = "\n".join(memories[0])
    else:
        memory_context=""
    #Combine memory and user query or just use user query
    if not memory_context :
        enhanced_query = enhanced_user_query
    else:
        memory_decision = memory_router_agent(enhanced_user_query,memory_context)
        if memory_decision == "USE_MEMORY":
            enhanced_query = f"""
            Memory : 
            {memory_context}
            Question :
            {enhanced_user_query}
            """
            metrics.memory_used = True
        else:
            enhanced_query = enhanced_user_query
            metrics.memory_used = False
    #Planner agent
    plan = planner_agent(enhanced_query) 

    #Exrtact goal
    goal = ""
    for line in plan.splitlines():
        if line.startswith("Goal:"):
            goal = line.replace("Goal:", "").strip()
            break

    #Extract tasks from plan
    tasks = extract_tasks(plan)

    #Store task length
    metrics.task_count = len(tasks)

    #Send task,goal to research agent and research output to critic agent
    revision_executed = 0
    revision_skipped = 0
    MAX_WORKERS = 3

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = []
        for task in tasks:
            futures.append(
                executor.submit(
                    process_task,
                    goal,
                    task
                )
            )
        for future in futures:
            result = future.result()
            all_results.append(result)
            summary_list.append(result["summary"])
            revision_executed += result["revision_executed"]
            revision_skipped += result["revision_skipped"]

    metrics.revision_executed = revision_executed
    metrics.revision_skipped = revision_skipped

    if len(tasks) > 0:
        metrics.revision_rate = round(
            revision_executed / len(tasks) * 100,
            2
        )

    summary = "\n".join(summary_list)
    final_summary = summary_agent(summary)
    save_decision = memory_save_agent(
        enhanced_user_query,
        final_summary
        )
    
    if save_decision == "SAVE_MEMORY":
        save_memory(final_summary)

    end_time = time.time()

    metrics.execution_time = round(end_time - start_time,2)

    metrics.timestamp = str(
        datetime.now()
    )

    if metrics.task_count > 0:
        metrics.avg_time_per_task = round(
            metrics.execution_time / metrics.task_count,
            2
        )

    return {
        "memory":memory_context,
        "enhanced_user_query":enhanced_user_query,
        "plan":plan,
        "tasks":tasks,
        "results":all_results,
        "final_summary":final_summary,
        "metrics":vars(metrics)
    }      
    