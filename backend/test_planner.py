from backend.agents.worker_agents.planner_agent import planner_agent

query = "How can i learn spring boot in 30 days?"

result = planner_agent(query)

print("\nPlanner output :\n")
print(result)