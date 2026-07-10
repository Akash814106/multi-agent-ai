import time
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

from backend.utils.workflow_metrics import WorkflowMetrics


from backend.memory.chroma_memory import retrieve_memory,save_memory

from backend.agents.worker_agents.planner_agent import planner_agent
from backend.agents.worker_agents.research_agent import research_agent
from backend.agents.worker_agents.critic_agent import critic_agent
from backend.agents.worker_agents.revision_agent import revision_agent
from backend.agents.worker_agents.summary_agent import summary_agent
from backend.agents.worker_agents.direct_response_agent import direct_response_agent

from backend.agents.control_agents.memory_router_agent import memory_router_agent
from backend.agents.control_agents.memory_save_agent import memory_save_agent
from backend.agents.control_agents.query_router_agent import query_router_agent
from backend.agents.control_agents.query_enhancement_agent import query_enhancement_agent
from backend.utils.task_parser import extract_tasks


MAX_RETRIES = 2
TARGET_SCORE = 8

MAX_WORKERS = 3

def process_task(goal,task):
    
    research_result = None
    critic_result = None
    revision_result = None
    summary_result = None

    best_result = None
    best_critic = None
    best_score = 0

    revision_executed = 0
    revision_skipped = 0

    try:

#        print(f"Starting: {task}")

        research_input = f"""
        Goal:
        {goal}
        Task:
        {task}
        """
        research_result = research_agent(research_input)
        critic_result = critic_agent(goal,task,research_result)
        score = critic_result["score"]

        best_score = score
        best_result = research_result
        best_critic = critic_result

        retry = 0

        while best_score < TARGET_SCORE and retry < MAX_RETRIES:

            revision_result = revision_agent(
                goal,
                task,
                best_result,
                best_critic
            )

            revision_executed+=1

            critic_result = critic_agent(
                goal,
                task,
                revision_result
            )

            score = critic_result["score"]

            if score > best_score:
                best_score = score
                best_result = revision_result
                best_critic = critic_result

            retry+=1

        if revision_executed == 0:
            revision_skipped =1

        summary_result = summary_agent(best_result)
        # print(f"Finished: {task}")

        return{
            "task":task,
            "research":research_result,
            "critic":best_critic,
            "revision":best_result,
            "summary":summary_result,
            "best_score": best_score,
            "revision_executed": revision_executed,
            "revision_skipped": revision_skipped,
            "status":"SUCCESS"
        }
    
    except Exception as e:

        return {
            "task":task,
            "research":research_result,
            "critic":best_critic,
            "revision":best_result,
            "summary":summary_result,
            "best_score": best_score,
            "revision_executed":revision_executed,
            "revision_skipped":revision_skipped,
            "status":"FAILED",
            "error":f"{type(e).__name__}: {e}"

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

        save_decision = memory_save_agent(
            user_query,
            result
        )

        if save_decision == "SAVE_MEMORY":
            save_memory(result)

        return {
            "goal": "Direct Response",
            "memory": "",
            "enhanced_user_query": user_query,
            "plan": "",
            "tasks": [],
            "results": [],
            "final_summary": result,
            "metrics": {
                "execution_time": 0,
                "memory_used": False,
                "task_count": 0,
                "revision_executed": 0,
                "revision_skipped": 0,
                "failed_tasks": 0
            }
        }
    
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

    lines = plan.splitlines()

    for i, line in enumerate(lines):

        if line.startswith("Goal:"):

            extracted = line.replace("Goal:", "").strip()

            if extracted:
                goal = extracted

            elif i + 1 < len(lines):
                goal = lines[i + 1].strip()

            break

    #Extract tasks from plan
    tasks = extract_tasks(plan)

    #Store task length
    metrics.task_count = len(tasks)

    #Send task,goal to research agent and research output to critic agent
    revision_executed = 0
    revision_skipped = 0

    failed_tasks = 0

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

            if result["status"] == "SUCCESS":
                summary_list.append(result["summary"])
                revision_executed += result["revision_executed"]
                revision_skipped += result["revision_skipped"]

            else:
                print(f"TASK FAILED : {result['task']}")
                print(f"Reason: {result['error']}")
                failed_tasks+=1

    metrics.revision_executed = revision_executed
    metrics.revision_skipped = revision_skipped
    metrics.failed_tasks = failed_tasks

    if len(tasks) > 0:
        metrics.revision_rate = round(
            revision_executed / len(tasks) * 100,
            2
        )

    if summary_list:
        summary = "\n".join(summary_list)
        final_summary = summary_agent(summary)
    else:
        final_summary = "Workflow failed. No successful task summaries were generated."


    if summary_list:
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
        "goal": goal,
        "memory": memory_context,
        "enhanced_user_query": enhanced_user_query,
        "plan": plan,
        "tasks": tasks,
        "results": all_results,
        "final_summary": final_summary,
        "metrics": vars(metrics),
    
        "workflow_steps": [
            "Query Routed",
            "Query Enhanced",
            "Memory Retrieved",
            "Planning Completed",
            "Research Completed",
            "Critic Completed",
            "Summary Generated"
        ]
    }    
    