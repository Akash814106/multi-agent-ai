from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq

load_dotenv()
groq_api_key = os.getenv("GROW_API_KEY")

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    # model="llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY")
)

def research_agent(topic):

    prompt = f"""
    You are a Research Agent.

    Your job is to explain and gather information about a topic.

    Topic:
    {topic}

    Return:
    - Overview
    - Important Concepts
    - Key Takeaways
    """

    response = llm.invoke(prompt)
    return response.content