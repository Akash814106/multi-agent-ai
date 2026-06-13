from workflows.multi_agent_workflow import run_workflow
from utils.api_counter import print_counts


result = run_workflow(
    "Create roadmap for learning Java"
)

with open("workflow_output.txt", "w", encoding="utf-8") as f:
    f.write(str(result))

print("Output saved to workflow_output.txt")

print_counts()
# print("\n---Result---\n")
# print(result)