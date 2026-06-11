from dotenv import load_dotenv
import os
import json
from langchain_groq import ChatGroq

load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

llm = ChatGroq(
    model = "llama-3.3-70b-versatile",
    # model="llama-3.1-8b-instant",
    api_key= groq_api_key
)

def direct_response_agent(user_query):

    prompt = f"""
    You are a Direct Response Agent.

    Your job is to answer simple questions directly.

    Rules:
    - Be concise.
    - Answer in 2-4 sentences whenever possible.
    - Give only the most important information.
    - Do not provide long explanations.
    - Do not provide tutorials or roadmaps.
    - Do not add extra sections unless the user asks.
    - If the user wants detailed learning, that belongs to the multi-agent workflow.

    User Query:
    {user_query}
    """
    response = llm.invoke(prompt)
    return response.content