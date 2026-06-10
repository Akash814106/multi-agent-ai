from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq

load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

llm = ChatGroq(
    model = "llama-3.3-70b-versatile",
    # model="llama-3.1-8b-instant",
    api_key=groq_api_key
)

def revision_agent(task,research_output,critic_feedback):

    prompt = f"""
    You are a Revision Agent.

    Your job is to improve the research content
    using the critic feedback.

    Task:
    {task}

    Original Research:
    {research_output}

    Critic Feedback:
    {critic_feedback}

    Generate a revised and improved version
    of the research content.

    Return only the improved content.
    """

    response = llm.invoke(prompt)
    return response.content