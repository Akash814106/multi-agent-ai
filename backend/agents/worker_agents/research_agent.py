from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq
from utils.api_counter import increment

load_dotenv()
groq_api_key2 = os.getenv("GROQ_API_KEY2")

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    # model="llama-3.1-8b-instant",
    api_key= groq_api_key2
)

def research_agent(topic):

    prompt = f"""
    You are a Research Agent.

    Your job is to provide detailed information about the given topic.

    Topic:
    {topic}

    Rules:
    - Focus only on the given topic.
    - Provide practical and concrete information.
    - Avoid generic textbook definitions.
    - Include real-world considerations when relevant.
    - For system design topics, discuss architecture, components, tradeoffs, scalability, reliability, and security.

    Return:

    Overview:
    <overview>

    Important Concepts:
    <concepts>

    Detailed Explanation:
    <detailed explanation>

    Key Takeaways:
    <takeaways>
    """

    increment("research")
    response = llm.invoke(prompt)
    return response.content