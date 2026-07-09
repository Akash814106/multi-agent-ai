def build_search_query(topic):

    goal = ""
    task = ""

    for line in topic.splitlines():

        line = line.strip()

        if line.startswith("Goal:"):
            goal = line.replace("Goal:", "").strip()

        elif line.startswith("Task:"):
            task = line.replace("Task:", "").strip()

    if goal and task:
        return f"{goal} {task}"

    return topic.strip()