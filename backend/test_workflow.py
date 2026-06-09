# from agents.planner_agent import planner_agent
# from agents.research_agent import research_agent

# user_query =  "Learn Spring Boot in 30 days"

# plan = planner_agent(user_query)
# print(plan)

# tasks = [
#     "Spring Core",
#     "Spring Dependency Injection",
#     "Spring REST APIs"
# ]

# for task in tasks:

#     print(f"\nResearching : {task}\n")
#     result = research_agent(task)
#     print(result)
#     print("\n"+"="*50)








from agents.planner_agent import planner_agent
from agents.research_agent import research_agent
from utils.task_parser import extract_tasks

user_query =  "Learn Spring Boot in 30 days"

plan = planner_agent(user_query)
print("------Plan------")
print(plan)

tasks = extract_tasks(plan)
print("------Extracted Tasks------")
print(tasks)


print("------Research------")
for task in tasks:

    print(f"Researching  : {task}\n")
    result = research_agent(task)
    print(result,"\n")

    print("\n"+"="*50)