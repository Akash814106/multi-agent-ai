from backend.utils.env_loader import *
import os
import json
from langchain_groq import ChatGroq
from backend.utils.api_counter import increment


groq_api_key1 = os.getenv("GROQ_API_KEY1")

llm = ChatGroq(
    model = "llama-3.3-70b-versatile",
    # model="llama-3.1-8b-instant",
    api_key= groq_api_key1
)

def direct_response_agent(user_query):

    prompt = f"""
    You are a Direct Response Agent.
    
    Your job is to answer simple questions directly.
    
    The input may contain a Memory section followed by the user's question.
    
    If a Memory section is present:
    
    - Treat it as trusted context.
    - Use it to answer the question whenever relevant.
    - Answer naturally as if you already know the information.
    - Do NOT say things like:
        - "According to the memory..."
        - "Based on the provided memory..."
        - "The stored memory says..."
    - If the memory does not help answer the question, ignore it and answer normally.
    
    Rules:
    
    - Provide a direct answer.
    - Be concise.
    - Prefer 2-4 sentences whenever possible.
    - Give only the most important information.
    - Avoid unnecessary details.
    - Do not provide tutorials, roadmaps, or step-by-step guides.
    - Do not explain topics in depth.
    - Do not add extra sections or headings.
    - If the user asks for detailed learning, planning, comparison, architecture design, or research, that belongs to the multi-agent workflow.
    - Return only the answer.
    
    Input:
    
    {user_query}
    
    Answer:
    """

    increment("direct_response")
    response = llm.invoke(prompt)
    return response.content