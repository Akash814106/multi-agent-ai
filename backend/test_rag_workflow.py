from memory.chroma_memory import retrieve_memory
from backend.agents.worker_agents.planner_agent import planner_agent

user_query = "What should i learn next?"

memories = retrieve_memory(user_query)

print("\nRetrieved memories\n")
print(memories)

memory_context = "\n".join(memories[0])

print("\nMemory context\n")
print(memory_context)

enhanced_query = f"""

Memory:{memory_context}

Question :{user_query}
"""

print("\nEnhanced query : \n")
print(enhanced_query)

plan = planner_agent(enhanced_query)

print("\nPlanner Output :\n")
print(plan)