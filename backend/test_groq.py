from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

llm = ChatGroq(
    model = "llama-3.3-70b-versatile",
    api_key=groq_api_key
)

response = llm.invoke("Explain what is AI agent in one sentence?")

print("\nAI Response : ")
print(response.content)