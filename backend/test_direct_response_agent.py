from agents.worker_agents.direct_response_agent import direct_response_agent

user_query="Explain Dependency Injection."

result = direct_response_agent(user_query)

print("\nResult : \n")
print(result)