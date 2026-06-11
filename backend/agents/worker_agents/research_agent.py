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

    response = llm.invoke(prompt)
    return response.content