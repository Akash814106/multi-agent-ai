from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

llm = ChatGroq(
    model = "llama-3.3-70b-versatile",
    # model="llama-3.1-8b-instant",
    api_key= groq_api_key
)

def planner_agent(user_query):

  
    prompt = f"""
    You are a Planner Agent.

    Your responsibility is to convert a user goal into an actionable plan.

    User Request:
    {user_query}

    Rules:
    - Focus on the actual topic in the request.
    - Do not explain how planning works.
    - Do not explain your reasoning.
    - Do not analyze the query.
    - Generate tasks specific to the user's goal.
    - Each task should be actionable.

    Output Format:

    Goal:
    <goal>

    Tasks:
    1. <task>
    2. <task>
    3. <task>
    4. <task>
    5. <task>
    """

    reponse = llm.invoke(prompt)

    return reponse.content