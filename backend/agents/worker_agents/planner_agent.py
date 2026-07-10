from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq
from backend.utils.api_counter import increment

load_dotenv()

groq_api_key1 = os.getenv("GROQ_API_KEY1")

llm = ChatGroq(
    model = "llama-3.3-70b-versatile",
    # model="llama-3.1-8b-instant",
    api_key= groq_api_key1
)

def planner_agent(user_query):

    prompt = f"""
    You are a Planner Agent.
    
    Your responsibility is to convert a user goal into a structured and actionable plan.
    
    User Request:
    {user_query}
    
    Rules:
    - Focus only on the actual topic in the request.
    - Preserve the user's original intent.
    - Do not answer the request.
    - Do not explain your reasoning.
    - Do not analyze the query.
    - Generate tasks specific to the user's goal.
    - Each task must be actionable and meaningful.
    - Each task should represent a major phase of work.
    - Prefer broader tasks over many small tasks.
    - Combine closely related topics when appropriate.
    - Avoid splitting closely related concepts into separate tasks.
    - Do not create tasks that significantly overlap with each other.
    - Do not generate redundant tasks.
    - Do not generate implementation details unless explicitly requested.
    - Generate between 5 and 8 tasks.
    - Never generate more than 8 tasks.
    
    Task Planning Guidelines:
    
    If the request is a roadmap:
    - Create sequential learning stages.
    - Start with fundamentals.
    - Progress toward advanced topics.
    - End with practical application, projects, or mastery.
    
    If the request is a system design question:
    - Create design-oriented tasks.
    - Focus on architecture and decision-making.
    - Prefer tasks covering:
    
      1. Functional Requirements
      2. Non Functional Requirements
      3. High Level Architecture
      4. Core Components and Services
      5. Database Design
      6. API Design
      7. Scalability
      8. Security and Reliability
    
    - Combine related design topics when necessary to stay within the task limit.
    - Do not create implementation tutorials for individual services unless explicitly requested.
    
    If the request is a comparison question:
    - Create tasks that examine:
      - Definitions
      - Architecture
      - Advantages
      - Disadvantages
      - Tradeoffs
      - Use Cases
      - Decision Criteria
    
    If the request is a research topic:
    - Create tasks that explore:
      - Overview
      - Core Concepts
      - Important Components
      - Benefits
      - Limitations
      - Real World Applications
      - Key Takeaways

    Prioritize breadth over excessive granularity.
    Avoid splitting closely related topics into separate tasks.
    
    Output Format:
    
    Goal:
    <goal>
    
    Tasks:
    1. <task>
    2. <task>
    3. <task>
    4. <task>
    5. <task>
    ...
    """

    increment("planner")
    reponse = llm.invoke(prompt)

    return reponse.content