import json

with open("api_counts.json", "r") as f:
    counts = json.load(f)

print("\nAPI COUNTS\n")

for agent, count in counts.items():
    print(f"{agent}: {count}")