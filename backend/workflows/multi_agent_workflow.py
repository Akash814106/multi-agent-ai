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

def run_workflow(user_query):

    all_results = []
    summary_list = []

    router_result = query_router_agent(user_query)
    query_decision = router_result["decision"]

    print("\nQuery router : \n")
    print(router_result)

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
    print("\nEnhanced Query :\n")
    print(enhanced_user_query)

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

        else:
            enhanced_query = enhanced_user_query

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

    #Print task length

    print(f"Task Count: {len(tasks)}")

    #Send task,goal to research agent and research output to critic agent

    for task in tasks:
        
        research_input = f"""
        Goal:
        {goal}

        Task:
        {task}
        """
        research_result = research_agent(research_input)
        critic_result = critic_agent(goal,task,research_result)
        revision_result = revision_agent(goal,task,research_result,critic_result)
        summary_result = summary_agent(revision_result)

        all_results.append(
            {
                "task":task,
                "research":research_result,
                "critic":critic_result,
                "revision":revision_result,
                "summary":summary_result
            }
        )

        summary_list.append(summary_result)
        #save_memory(summary_result)

    summary = "\n".join(summary_list)
    final_summary = summary_agent(summary)

    save_decision = memory_save_agent(
        enhanced_user_query,
        final_summary
        )
    
    if save_decision == "SAVE_MEMORY":
        save_memory(final_summary)

    return {
        "memory":memory_context,
        "enhanced_user_query":enhanced_user_query,
        "plan":plan,
        "tasks":tasks,
        "results":all_results,
        "final_summary":final_summary
    }      


    