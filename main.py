from src.loader import load_youtube_transcript
from src.splitter import split_documents
from src.vector_store import create_vector_store
from src.qa_chain import answer_question


video_url = input("\nEnter Youtube Url:")


# Step 1: Load YouTube transcript
documents = load_youtube_transcript(video_url)

print("Transcript Loaded!")

# Step 2: Split transcript
chunks = split_documents(documents)

print("Total Chunks:", len(chunks))

# Step 3: Store chunks in ChromaDB
vector_store = create_vector_store(chunks)

print("Embeddings Stored Successfully!")

# Step 4: Ask questions
while True:

    query = input("\nAsk a question (type exit to quit): ")

    if query.lower() == "exit":
        break

    # Step 5: Generate answer using RAG
    answer = answer_question(vector_store, query)

    print("\nAI Answer:")
    print(answer)
