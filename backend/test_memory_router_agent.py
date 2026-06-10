from backend.agents.control_agents.memory_router_agent import memory_router_agent

user_query = "What is the capital of France?"

memory_context =f""" User learned:
- Spring Boot
- Microservices
"""

result = memory_router_agent(user_query,memory_context)
print("\nResult : \n")
print(result)