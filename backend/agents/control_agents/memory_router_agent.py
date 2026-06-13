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

def memory_router_agent(user_query,memory_context):

    prompt = f"""
    You are a Memory Router Agent.

    Determine whether the retrieved memory
    is relevant to answering the user's question.

    User Query:
    {user_query}

    Retrieved Memory:
    {memory_context}

    Return ONLY one of:

    USE_MEMORY

    or
    
    SKIP_MEMORY

    Do not explain your reasoning.
    Do not return any additional text.
    """

    increment("memory_router")
    response = llm.invoke(prompt)
    return response.content