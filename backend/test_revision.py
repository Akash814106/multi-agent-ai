from backend.agents.worker_agents.revision_agent import revision_agent


task = "Explain Spring Boot Dependency Injection"

research_output = """
Dependency Injection allows objects
to receive dependencies from outside.
"""

critic_feedback = """
Add examples.
Explain advantages.
Mention Spring IoC container.
"""

result =  revision_agent(
    task,
    research_output,
    critic_feedback
)

print("\n---Result---\n")
print(result)