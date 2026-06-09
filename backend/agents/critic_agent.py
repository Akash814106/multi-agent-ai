from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq

load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

llm = ChatGroq(
    model = "llama-3.3-70b-versatile",
    api_key= groq_api_key
)

def critic_agent(content):

    prompt = f"""
    You are a Critic Agent.

    Review the following content.

    Identify:
    - Missing information
    - Weak explanations
    - Possible improvements

    Content:
    {content}

    Return:
    - Strengths
    - Weaknesses
    - Suggested Improvements
    """

    response = llm.invoke(prompt)

    return response.content