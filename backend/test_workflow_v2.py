from workflows.multi_agent_workflow import run_workflow

result = run_workflow(
    "I know Java and Spring Boot. Create a roadmap to become a Backend Architect and explain each step."
)

print("\n---Result---\n")
print(result)