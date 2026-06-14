from workflows.multi_agent_workflow import run_workflow
from utils.api_counter import print_counts
import json

result = run_workflow(
    "Create roadmap for learning Java"
)

# with open("workflow_output.txt", "w", encoding="utf-8") as f:
#     f.write(str(result))

# print("Output saved to workflow_output.txt")

# print_counts()
# print("\n---Result---\n")
# print(result)




with open(
    "workflow_output.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        result,
        f,
        indent=4,
        ensure_ascii=False
    )

print("Output saved to workflow_output.json")

print_counts()