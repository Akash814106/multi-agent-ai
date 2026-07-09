from agents.worker_agents.research_agent import research_agent

topic = """
Goal:
Design YouTube System

Task:
Design High Level Architecture
"""

result = research_agent(topic)

print("\nResearch Output:\n")
print(result)