from workflows.multi_agent_workflow import run_workflow
from utils.api_counter import print_counts
import json

result = run_workflow(
    "Design YouTube System"
)

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