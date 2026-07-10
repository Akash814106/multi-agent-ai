from dotenv import load_dotenv
import os
import json
from langchain_groq import ChatGroq
from backend.utils.api_counter import increment

load_dotenv()
groq_api_key3 = os.getenv("GROQ_API_KEY3")

llm = ChatGroq(
    model = "llama-3.3-70b-versatile",
    # model="llama-3.1-8b-instant",
    api_key= groq_api_key3
)

def critic_agent(goal, task, research_result):
    
    prompt = f"""
    You are a Critic Agent.

    Your job is to critically evaluate research content for a given goal and task.

    Goal:
    {goal}

    Task:
    {task}

    Research Content:
    {research_result}

    Evaluation Criteria:

    1. Relevance (40%)
    - Does the content directly address the task?
    - Does it align with the overall goal?

    2. Completeness (40%)
    - Are the important concepts covered?
    - Are any critical details missing?

    3. Clarity (20%)
    - Is the explanation clear, organized, and understandable?
    - Are concepts explained with sufficient depth?

    Rules:
    - Be objective and specific.
    - Evaluate only against the given goal and task.
    - Do not invent missing requirements.
    - Do not suggest extra features unless they are necessary for completing the task.
    - Only identify missing information that is important for the task.
    - Only suggest improvements that would significantly improve quality.
    - Be strict when assigning scores.
    - Do not give high scores merely because the content is technically correct.

    Do not penalize content for missing information unless that information is necessary to complete the given task.

    Scoring Guide:

    9-10:
    - Excellent.
    - Comprehensive coverage.
    - Accurate and well-structured.
    - Minimal or no important information missing.
    - Could be used directly with little or no improvement.

    7-8:
    - Good.
    - Covers most important concepts.
    - Some minor gaps or areas lacking depth.
    - Improvements would be beneficial but are not critical.

    5-6:
    - Average.
    - Covers the basic requirements.
    - Important details are missing.
    - Requires noticeable improvement before being considered complete.

    3-4:
    - Weak.
    - Significant gaps in coverage.
    - Multiple important concepts missing.
    - Explanations lack clarity or depth.

    1-2:
    - Poor.
    - Fails to address the task adequately.
    - Major inaccuracies or missing information.

    Return ONLY valid JSON.

    Format:

    {{
        "score": 7,
        "strengths": [
            "...",
            "..."
        ],
        "weaknesses": [
            "...",
            "..."
        ],
        "missing_information": [
            "...",
            "..."
        ],
        "suggested_improvements": [
            "...",
            "..."
        ]
    }}

    Do not return markdown.
    Do not return explanations outside JSON.
    """
    increment("critic")

    response = llm.invoke(prompt)

    # print("\nRaw Critic Response:\n")
    # print(response.content)

    cleaned_response = response.content.strip()

    cleaned_response = cleaned_response.replace(
        "```json",
        ""
    )

    cleaned_response = cleaned_response.replace(
        "```",
        ""
    )

    try:
        result = json.loads(cleaned_response)

    except Exception as e:

        print("\nJSON ERROR\n")
        print(cleaned_response)
        raise e

    return result