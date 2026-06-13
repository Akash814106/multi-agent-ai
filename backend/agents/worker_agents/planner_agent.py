from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq
from utils.api_counter import increment

load_dotenv()

groq_api_key1 = os.getenv("GROQ_API_KEY1")

llm = ChatGroq(
    model = "llama-3.3-70b-versatile",
    # model="llama-3.1-8b-instant",
    api_key= groq_api_key1
)

def planner_agent(user_query):

    prompt = f"""
    You are a Planner Agent.

    Your responsibility is to convert a user goal into a structured plan.

    User Request:
    {user_query}

    Rules:
    - Focus on the actual topic in the request.
    - Do not explain your reasoning.
    - Generate tasks specific to the user's goal.

    If the request is:
    - A roadmap → create learning steps.
    - A system design question → create design-oriented tasks.
    - A comparison question → create comparison-oriented tasks.
    - A research topic → create research-oriented tasks.

    For system design questions, include tasks such as:
    - Functional Requirements
    - Non Functional Requirements
    - High Level Architecture
    - Database Design
    - API Design
    - Scalability
    - Security and Reliability

    Do NOT create implementation tutorials for individual services unless explicitly requested.

    Output Format:

    Goal:
    <goal>

    Tasks:
    1. <task>
    2. <task>
    3. <task>
    ...
    """

    increment("planner")
    reponse = llm.invoke(prompt)

    return reponse.content