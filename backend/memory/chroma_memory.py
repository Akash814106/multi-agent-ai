import chromadb

client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(
    name = "user_memory"
)

def save_memory(memory_text):

    collection.add(
        documents=[memory_text],
        ids=[str(collection.count()+1)]
    )

def retrieve_memory(query):

    results = collection.query(
        query_texts=[query],
        n_results=3
    )

    return results["documents"]
