# YouTube RAG Q&A — AI Knowledge Assistant

An AI-powered YouTube Video Question Answering application built using **Retrieval-Augmented Generation (RAG)**, LangChain, OpenAI, and ChromaDB.

The application extracts transcripts from YouTube videos, converts them into vector embeddings, stores them in a vector database, and allows users to ask natural-language questions about the video content.

Instead of sending the entire transcript to an LLM, the application retrieves only the most relevant context and uses it to generate accurate, context-aware answers.

## Features

- **YouTube Transcript Extraction:** Load video transcripts using LangChain's YouTube Document Loader.
- **Text Chunking:** Split large transcripts into smaller chunks using RecursiveCharacterTextSplitter.
- **Vector Embeddings:** Generate semantic embeddings using OpenAI's `text-embedding-3-small`.
- **Vector Database:** Store and persist embeddings using ChromaDB.
- **Semantic Search:** Retrieve relevant transcript chunks based on user questions.
- **Context-Aware Answers:** Generate answers using retrieved context and OpenAI GPT.
- **Interactive Q&A:** Ask multiple questions about a video through the command line.

## Architecture

```text
            YouTube Video URL
                    |
                    v
             Document Loader
                    |
                    v
            YouTube Transcript
                    |
                    v
               Text Splitter
                    |
                    v
              Text Chunks
                    |
                    v
             Embedding Model
                    |
                    v
                ChromaDB
                    |
                    |
             User Question
                    |
                    v
             Query Embedding
                    |
                    v
            Similarity Search
                    |
                    v
          Relevant Documents
                    |
                    v
          Prompt + Retrieved Context
                    |
                    v
                 OpenAI LLM
                    |
                    v
               Final Answer
```

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| LangChain | LLM application framework |
| OpenAI | Embeddings and answer generation |
| ChromaDB | Vector database |
| YouTube Transcript API | Transcript extraction |
| RecursiveCharacterTextSplitter | Document chunking |
| python-dotenv | Environment variable management |

## Project Structure

```text
youtube-rag-qa/
│
├── src/
│   ├── __init__.py
│   ├── loader.py
│   ├── splitter.py
│   ├── embeddings.py
│   ├── vector_store.py
│   ├── retriever.py
│   └── qa_chain.py
│
├── data/
├── chroma_db/
│
├── main.py
├── .env
├── .env.example
├── .gitignore
└── requirements.txt
```

## Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/youtube-rag-qa.git

cd youtube-rag-qa
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**macOS / Linux**

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the root directory.

```env
OPENAI_API_KEY=your_openai_api_key
```

You need an OpenAI API key with available API credits.

### 5. Run the application

```bash
python main.py
```

## How It Works

### 1. Document Loading

The application extracts the transcript from a YouTube video using `YoutubeLoader`.

### 2. Text Splitting

The transcript is divided into smaller chunks using `RecursiveCharacterTextSplitter`.

Configuration:

- Chunk Size: 500 characters
- Chunk Overlap: 50 characters

### 3. Embedding Generation

Each transcript chunk is converted into a numerical vector using OpenAI's `text-embedding-3-small` model.

### 4. Vector Storage

The generated embeddings, original text, and metadata are stored in ChromaDB for persistent storage.

### 5. Semantic Retrieval

When a user submits a question:

- The question is converted into an embedding.
- ChromaDB performs similarity search.
- The top 3 relevant transcript chunks are retrieved.

### 6. Answer Generation

The retrieved documents and user question are combined using a LangChain PromptTemplate and passed to GPT-4o-mini.

The LLM generates an answer based on the retrieved video context.

## Example Usage

```text
Ask a question (type exit to quit): What is LangChain?

AI Answer:
LangChain is a framework for developing applications
powered by large language models...
```

*Example response; actual answers depend on the selected video.*

## Configuration

| Parameter | Value |
|---|---|
| Embedding Model | text-embedding-3-small |
| LLM | gpt-4o-mini |
| Chunk Size | 500 |
| Chunk Overlap | 50 |
| Retrieved Documents (Top-K) | 3 |
| Vector Database | ChromaDB |

## Future Improvements

- Support multiple YouTube videos.
- Build a Streamlit or FastAPI interface.
- Add source references and timestamps to answers.
- Implement similarity score filtering.
- Add conversational memory.
- Support PDF and other document formats.
- Implement hybrid search (keyword + semantic search).
- Add streaming responses.

## Key Concepts Demonstrated

- Retrieval-Augmented Generation (RAG)
- Document Loaders
- Text Splitting
- Vector Embeddings
- Vector Databases
- Semantic Similarity Search
- Information Retrieval
- Prompt Engineering
- LangChain Expression Language (LCEL)
- LLM Integration

## License

This project is intended for educational and learning purposes.
