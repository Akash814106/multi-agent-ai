from memory.chroma_memory import retrieve_memory,save_memory

from agents.planner_agent import planner_agent
from agents.research_agent import research_agent
from agents.critic_agent import critic_agent
from agents.revision_agent import revision_agent

from utils.task_parser import extract_tasks

def run_workflow(user_query):

    all_results = []

    #Retrieve memory
    memories = retrieve_memory(user_query)

    if memories and memories[0]:
        memory_context = "\n".join(memories[0])
    else:
        memory_context=""

    #Combine memory and user query
    enhanced_query = f"""

    Memory : 
    {memory_context}
    Question :
    {user_query}
    """

    #Planner agent
    plan = planner_agent(enhanced_query)

    #Extract tasks from plan
    tasks = extract_tasks(plan)

    #Send task to research agent and research output to critic agent

    for task in tasks:

        research_result = research_agent(task)
        critic_result = critic_agent(research_result)
        revision_result = revision_agent(task,research_result,critic_result)

        all_results.append(
            {
                "task":task,
                "research":research_result,
                "critic":critic_result,
                "revision":revision_result
            }
        )

        save_memory(revision_result)

    return {
        "memory":memory_context,
        "plan":plan,
        "tasks":tasks,
        "results":all_results
    }      


    