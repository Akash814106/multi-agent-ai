from dotenv import load_dotenv
import os
from exa_py import Exa

load_dotenv()

exa = Exa(
    api_key=os.getenv("EXA_API_KEY")
)

def search_web(query):

    try:
        response = exa.search(
            query=query,
            num_results=3
        )

        search_context = ""

        for result in response.results:

            search_context += f"""
Title:
{result.title}

URL:
{result.url}

Content:
{result.text[:1500]}

----------------------------------
"""

        return search_context

    except Exception as e:
        print(f"Web search failed: {e}")
        return ""