from backend.agents.worker_agents.planner_agent import planner_agent
from backend.agents.worker_agents.research_agent import research_agent
from backend.agents.worker_agents.critic_agent import critic_agent

from utils.task_parser import extract_tasks

user_query = "Learn Spring Boot in 30 days"

print("------Plan------")
plan  = planner_agent(user_query)
print(plan)


tasks = extract_tasks(plan)
print("------Tasks-----")
print(tasks)

print("------Research------")

for task in tasks:

    print(f"Researching : {task}")
    result = research_agent(task)
    print(result,"\n")
    

    print("------Critic Agent------")
    critic_result = critic_agent(result)
    print(critic_result)

    print("\n"+"="*80)


