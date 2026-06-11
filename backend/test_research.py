from agents.worker_agents.research_agent import research_agent

topic = f"""
Goal:
Design WhatsApp Messaging System

Task:
Design High Level Architecture
"""

result = research_agent(topic)

print("\nResearch output :\n")
print(result)