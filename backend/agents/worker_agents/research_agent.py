from backend.utils.env_loader import *
import os
from langchain_groq import ChatGroq
from backend.utils.api_counter import increment

from backend.utils.web_search import search_web
from backend.utils.search_query_builder import build_search_query


groq_api_key2 = os.getenv("GROQ_API_KEY2")

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    # model="llama-3.1-8b-instant",
    api_key= groq_api_key2
)

def research_agent(topic):

    search_query = build_search_query(topic)
    web_context = search_web(search_query)

    prompt = f"""
    You are a Research Agent.

    Your responsibility is to produce an accurate, comprehensive, and well-structured research report for the given topic.

    Topic:
    {topic}

    Relevant Web Search Results:
    {web_context}

    Instructions:

    - Use the web search results as the primary source of information.
    - Combine information from multiple search results into one coherent report.
    - Use your own knowledge only to fill small gaps or improve clarity.
    - Do not fabricate facts or invent information that is not supported.
    - Remove duplicate information from different sources.
    - Focus only on information relevant to the given topic.
    - Provide practical, technical, and real-world information.
    - For system design topics, discuss:
        - Architecture
        - Core Components
        - Data Flow
        - Database Choices
        - APIs (if applicable)
        - Scalability
        - Reliability
        - Security
        - Trade-offs
    - If the topic is not related to system design, ignore the above system design requirements.
    - Organize the response clearly using the format below.

    Return the response in exactly this format:

    Overview:
    <overview>

    Important Concepts:
    <concepts>

    Detailed Explanation:
    <detailed explanation>

    Key Takeaways:
    <takeaways>

    Do not include markdown code blocks.
    Do not explain your reasoning.
    Return only the research report.
    """

    increment("research")
    response = llm.invoke(prompt)
    return response.content