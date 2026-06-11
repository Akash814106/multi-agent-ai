from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq

load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

llm = ChatGroq(
    model = "llama-3.3-70b-versatile",
    # model="llama-3.1-8b-instant",
    api_key= groq_api_key
)

def query_enhancement_agent(user_query):

    prompt = f"""
    You are a Query Enhancement Agent.

    Your job is to rewrite user queries into clearer and more detailed instructions
    for downstream AI agents.

    Rules:
    - Preserve the user's original intent.
    - Do not answer the query.
    - Do not add unrelated topics.
    - Do not change the user's goal.
    - Improve clarity and specificity.
    - Expand vague requests into actionable instructions.
    - If the query is already clear and specific, return it unchanged.
    - Return ONLY the enhanced query text.

    Examples:

    User Query:
    Teach me Java

    Enhanced Query:
    Create a structured learning roadmap for Java, covering fundamentals, object-oriented programming, collections, exception handling, multithreading, and advanced concepts.

    User Query:
    I want to become a backend developer

    Enhanced Query:
    Create a step-by-step roadmap to become a backend developer, including programming fundamentals, backend frameworks, databases, APIs, system design, cloud technologies, and practical projects.

    User Query:
    How do large companies handle millions of users?

    Enhanced Query:
    Explain how large-scale software systems handle millions of users, including scalability, load balancing, caching, databases, distributed systems, and cloud infrastructure.

    User Query:
    What is Java?

    Enhanced Query:
    What is Java?

    User Query:
    Explain Dependency Injection

    Enhanced Query:
    Explain Dependency Injection

    User Query:
    {user_query}

    Enhanced Query:
    """

    response = llm.invoke(prompt)
    return response.content.strip()