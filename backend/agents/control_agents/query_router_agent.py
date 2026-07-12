from dotenv import load_dotenv
import os
import json
from langchain_groq import ChatGroq
from backend.utils.api_counter import increment

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

    Your job is to classify every user query into ONE of two categories.

    Return ONLY valid JSON.

    Possible decisions:

    DIRECT_RESPONSE
    MULTI_AGENT_WORKFLOW


    Choose DIRECT_RESPONSE when:

    - Greetings
    - Casual conversation
    - Simple factual questions
    - Questions that can be answered from the user's stored memory
    - Questions about the user's own preferences
    - Questions about previous conversations
    - Questions asking what the AI remembers
    - Questions requiring only one concise answer
    - Follow-up questions that do not require research

    Examples:

    User:
    Hi

    Decision:
    DIRECT_RESPONSE

    User:
    What is Python?

    Decision:
    DIRECT_RESPONSE

    User:
    What is my favorite language?

    Decision:
    DIRECT_RESPONSE

    User:
    Where do I live?

    Decision:
    DIRECT_RESPONSE

    User:
    What did I tell you yesterday?

    Decision:
    DIRECT_RESPONSE

    User:
    Do you remember my project?

    Decision:
    DIRECT_RESPONSE


    Choose MULTI_AGENT_WORKFLOW when:

    - The user requests research
    - Multiple topics must be investigated
    - Comparison is required
    - Planning is required
    - Step-by-step learning is required
    - Architecture design
    - Coding project planning
    - Long explanations
    - Web research
    - Multiple tasks are needed before answering

    Examples:

    User:
    Explain how JWT authentication works.

    Decision:
    MULTI_AGENT_WORKFLOW

    User:
    Compare MongoDB and PostgreSQL.

    Decision:
    MULTI_AGENT_WORKFLOW

    User:
    Design a scalable chat application.

    Decision:
    MULTI_AGENT_WORKFLOW


    User Query:

    {user_query}


    Return ONLY JSON.

    Format:

    {{
        "decision":"DIRECT_RESPONSE",
        "reason":"..."
    }}

    Do not return markdown.
    Do not explain your answer.
    """
   
    increment("query_router")
    response = llm.invoke(prompt)

#    print("\nRaw response\n")
#    print(response.content)
   
    result = json.loads(response.content)
    return result