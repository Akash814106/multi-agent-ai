import chromadb

client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(
    name="user_memory"
)


def save_memory(
    memory_text,
    user_email,
):

    collection.add(
        documents=[memory_text],
        metadatas=[
            {
                "user_email": user_email
            }
        ],
        ids=[str(collection.count() + 1)]
    )


def retrieve_memory(
    query,
    user_email,
):

    results = collection.query(
        query_texts=[query],
        n_results=3,
        where={
            "user_email": user_email
        }
    )

    return results["documents"]