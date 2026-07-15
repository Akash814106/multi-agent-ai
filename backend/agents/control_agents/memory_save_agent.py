from backend.utils.env_loader import *
import os
from langchain_groq import ChatGroq
from backend.utils.api_counter import increment


groq_api_key1 = os.getenv("GROQ_API_KEY1")

llm = ChatGroq(
    model = "llama-3.3-70b-versatile",
    # model="llama-3.1-8b-instant",
    api_key= groq_api_key1
)

def memory_save_agent(user_query,final_summary):

    prompt = f"""
    You are a Memory Save Agent.

    Your job is to decide whether the following information
    is useful for long-term memory.

    Store information only if it is likely to be useful in future conversations.

    Examples of information that SHOULD be stored:
    - Learning goals
    - Topics the user studied or learned
    - Career interests
    - Project progress
    - User preferences
    - Long-term plans
    - Important educational knowledge

    Examples of information that SHOULD NOT be stored:
    - Jokes
    - Greetings
    - Small talk
    - Weather questions
    - One-time factual questions
    - Temporary information
    - Random trivia

    User Query:
    {user_query}

    Summary:
    {final_summary}

    Return ONLY one of the following:

    SAVE_MEMORY

    or

    SKIP_MEMORY

    Do not explain your answer.
    Do not return any other text.
    """

    increment("memory_save")
    response = llm.invoke(prompt)
    return response.content