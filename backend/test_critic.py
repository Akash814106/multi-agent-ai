from agents.critic_agent import critic_agent

sample_content = """
Spring Dependency Injection is a design pattern
used to reduce coupling between components.
"""

result = critic_agent(sample_content)
print("Critic Output : \n")
print(result)