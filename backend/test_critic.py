from agents.worker_agents.critic_agent import critic_agent
goal = "Design WhatsApp Messaging System"

task = "Design High Level Architecture"

research_result = """
WhatsApp uses a client server architecture.
Messages are stored in database.
Users authenticate before messaging.
"""

result = critic_agent(
    goal,
    task,
    research_result
)

print(result)

print(type(result))

print(result["score"])