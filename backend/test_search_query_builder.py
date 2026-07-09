from utils.search_query_builder import build_search_query

topic = """
Goal:
Design YouTube System

Task:
Design High Level Architecture
"""

query = build_search_query(topic)

print("Generated Search Query:\n")
print(query)