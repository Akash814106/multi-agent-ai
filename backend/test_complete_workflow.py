from memory.chroma_memory import retrieve_memory

from backend.agents.worker_agents.planner_agent import planner_agent
from backend.agents.worker_agents.research_agent import research_agent
from backend.agents.worker_agents.critic_agent import critic_agent

from utils.task_parser import extract_tasks


user_query = "What should i learn next?"

memories = retrieve_memory(user_query)
memory_context = "\n".join(memories[0])
print("\n Memory context : \n")
print(memory_context)

print("\n"+"="*80)

enhanced_query = f"""
Memory : {memory_context}

Question : {user_query}
"""
print("\nEnhanced Query : \n")
print(enhanced_query)


print("\n"+"="*80)


plan = planner_agent(enhanced_query)
print("\n---Plan---\n")
print(plan)


print("\n"+"="*80)


tasks = extract_tasks(plan)
print("\nExtracted taasks\n")
print(tasks)

print("\n"+"="*80)


for task in tasks:

    research_result = research_agent(task)
    print("\n---Research result---\n")
    print(research_result)

    critic_result = critic_agent(research_result)
    print("\n---Critic result---\n")
    print(critic_result)

    print("\n"+"="*80)