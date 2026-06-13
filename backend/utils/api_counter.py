api_counts = {
    "query_router": 0,
    "query_enhancement": 0,
    "memory_router": 0,
    "memory_save": 0,
    "planner": 0,
    "direct_response": 0,
    "research": 0,
    "critic": 0,
    "revision": 0,
    "summary": 0
}

def increment(agent_name):
    api_counts[agent_name] += 1

def print_counts():
    print("\n===== API COUNTS =====")

    for agent, count in api_counts.items():
        print(f"{agent}: {count}")

    print("======================\n")