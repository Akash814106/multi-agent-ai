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

    Summarize the following content into
    3-5 key learning points.

    Focus only on the most important concepts.

    Content : {revision_output}

    Return in this format:

    User learned:
    - ...
    - ...
    - ...
    """

    response = llm.invoke(prompt)
    return response.content
