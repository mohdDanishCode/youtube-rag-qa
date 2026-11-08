def retrieve_documents(vector_store, query: str):

    results = vector_store.similarity_search(
        query=query,
        k=3
    )

    return results