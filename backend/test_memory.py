from memory.chroma_memory import save_memory,retrieve_memory

print("\nSaving memories...\n")

save_memory(
    "User is learning Spring Boot"
)

save_memory(
    "User wants to learn Microservices"
)

save_memory(
    "User is interested in Kafka"
)

print("Memories saved.\n")

# result = retrieve_memory(
#     "Spring framework"
# )

result = retrieve_memory(
    "kafka"
)
print("\nRetrieved memory\n")
print(result)