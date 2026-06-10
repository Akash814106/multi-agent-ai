from backend.agents.control_agents.memory_save_agent import memory_save_agent

# user_query = "I want to learn Kafka next"

# final_summary = f"""
# User learned:
# - Kafka is a distributed messaging system
# """

user_query = "Tell me a joke"

final_summary = f"""
User learned:
- A joke about programmers
"""

result = memory_save_agent(user_query,final_summary)
print("\nResult\n")
print(result)