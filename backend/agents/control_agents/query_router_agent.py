from dotenv import load_dotenv
import os
import json
from langchain_groq import ChatGroq
from utils.api_counter import increment

load_dotenv()
groq_api_key1 = os.getenv("GROQ_API_KEY1")

llm = ChatGroq(
    model = "llama-3.3-70b-versatile",
    # model="llama-3.1-8b-instant",
    api_key= groq_api_key1
)

def query_router_agent(user_query):

   prompt = f"""
    You are a Query Router Agent.

    Decide whether the query should be answered directly
    or sent through a multi-agent workflow.

    Return ONLY valid JSON.

    Possible decisions:

    DIRECT_RESPONSE
    MULTI_AGENT_WORKFLOW

    User Query:
    {user_query}

    Return format:

    {{
        "decision":"DIRECT_RESPONSE",
        "reason":"Simple factual question"
    }}

    Do not return markdown.
    Do not return explanations outside JSON.
    """
   
   increment("query_router")
   response = llm.invoke(prompt)

   print("\nRaw response\n")
   print(response.content)
   
   result = json.loads(response.content)
   return result