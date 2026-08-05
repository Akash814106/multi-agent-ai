from backend.agents.worker_agents.research_agent import research_agent
from backend.agents.worker_agents.critic_agent import critic_agent
from backend.agents.worker_agents.revision_agent import revision_agent
from backend.agents.worker_agents.summary_agent import summary_agent

MAX_RETRIES = 2
TARGET_SCORE = 8

def process_task(goal,task):
    
    research_result = None
    critic_result = None
    revision_result = None
    summary_result = None

    best_result = None
    best_critic = None
    best_score = 0

    revision_executed = 0
    revision_skipped = 0

    try:

#        print(f"Starting: {task}")

        research_input = f"""
        Goal:
        {goal}
        Task:
        {task}
        """
        research_result = research_agent(research_input)
        critic_result = critic_agent(goal,task,research_result)
        score = critic_result.get("score", 0)

        best_score = score
        best_result = research_result
        best_critic = critic_result

        retry = 0

        while best_score < TARGET_SCORE and retry < MAX_RETRIES:

            revision_result = revision_agent(
                goal,
                task,
                best_result,
                best_critic
            )

            revision_executed+=1

            critic_result = critic_agent(
                goal,
                task,
                revision_result
            )

            score = critic_result.get("score", 0)

            if score > best_score:
                best_score = score
                best_result = revision_result
                best_critic = critic_result

            retry+=1

        if revision_executed == 0:
            revision_skipped =1

        summary_result = summary_agent(best_result)
        # print(f"Finished: {task}")

        return{
            "task":task,
            "research":research_result,
            "critic":best_critic,
            "revision":best_result,
            "summary":summary_result,
            "best_score": best_score,
            "revision_executed": revision_executed,
            "revision_skipped": revision_skipped,
            "status":"SUCCESS"
        }
    
    except Exception as e:

        return {
            "task":task,
            "research":research_result,
            "critic":best_critic,
            "revision":best_result,
            "summary":summary_result,
            "best_score": best_score,
            "revision_executed":revision_executed,
            "revision_skipped":revision_skipped,
            "status":"FAILED",
            "error":f"{type(e).__name__}: {e}"

        }
    