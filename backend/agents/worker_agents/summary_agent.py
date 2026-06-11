from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

llm = ChatGroq(
    model = "llama-3.3-70b-versatile",
    # model="llama-3.1-8b-instant",
    api_key=groq_api_key
)

def summary_agent(revision_output):
    
    prompt = f"""
    You are a Summary Agent.

    Summarize the content into 3-5 concise learning points.

    Content:
    {revision_output}

    Rules:
    - Focus only on the most important information.
    - Avoid unnecessary details.
    - Use clear and concise bullet points.
    - Capture knowledge that would be useful to remember later.
    - Do not repeat similar points.

    Output Format:

    User learned:
    - ...
    - ...
    - ...
    """

    response = llm.invoke(prompt)
    return response.content
