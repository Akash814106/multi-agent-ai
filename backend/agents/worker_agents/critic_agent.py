from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq
from utils.api_counter import increment

load_dotenv()
groq_api_key3 = os.getenv("GROQ_API_KEY3")

llm = ChatGroq(
    model = "llama-3.3-70b-versatile",
    # model="llama-3.1-8b-instant",
    api_key= groq_api_key3
)

def critic_agent(goal, task, research_result):

    prompt = f"""
    You are a Critic Agent.

    Your job is to critically review the research content in the context of the overall goal and task.

    Goal:
    {goal}

    Task:
    {task}

    Research Content:
    {research_result}

    Rules:
    - Be objective and specific.
    - Evaluate whether the content satisfies the task.
    - Evaluate whether the content supports the overall goal.
    - Identify missing information.
    - Identify inaccurate, vague, or incomplete explanations.
    - Identify areas lacking depth.
    - Suggest concrete improvements.
    - Do not rewrite the content.

    Return:

    Strengths:
    - ...

    Weaknesses:
    - ...

    Missing Information:
    - ...

    Suggested Improvements:
    - ...
    """

    increment("critic")
    response = llm.invoke(prompt)

    return response.content