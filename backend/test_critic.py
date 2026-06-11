from agents.worker_agents.critic_agent import critic_agent

goal = "Design WhatsApp Messaging System"

task = "Design High Level Architecture"

research_result = f"""
Overview:

A WhatsApp-like messaging system requires a scalable architecture to support millions of users. The system should provide real-time messaging and reliable message delivery.

Important Concepts:

- Client Server Architecture
- Load Balancer
- Database
- Authentication

Detailed Explanation:

The system consists of mobile clients communicating with backend servers.

A load balancer distributes traffic across application servers.

Application servers process messages and store them in a database.

Authentication is used to verify users before they can send messages.

The database stores user information and message history.

Key Takeaways:

- Load balancers improve scalability.
- Databases store messages.
- Authentication secures the system.
"""

result = critic_agent(goal,task,research_result)
print("Critic Output : \n")
print(result)