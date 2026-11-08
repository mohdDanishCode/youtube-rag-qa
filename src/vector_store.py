from langchain_chroma import Chroma
from src.embeddings import create_embeddings


def create_vector_store(chunks):

    embeddings = create_embeddings()

    # Delete existing collection
    Chroma(
        collection_name="youtube_video_transcripts",
        embedding_function=embeddings,
        persist_directory="./chroma_db"
    ).delete_collection()

    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        collection_name="youtube_video_transcripts",
        persist_directory="./chroma_db"
    )

    return vector_store