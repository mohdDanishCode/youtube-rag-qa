
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

from src.retriever import retrieve_documents


def answer_question(vector_store, query: str):

    # Step 1: Retrieve relevant documents
    retrieved_docs = retrieve_documents(vector_store, query)

    # Step 2: Combine retrieved documents
    context = "\n\n".join(
        doc.page_content for doc in retrieved_docs
    )

    # Step 3: Create prompt template
    prompt = ChatPromptTemplate.from_template(
        """
        You are a helpful AI assistant.

        Answer the user's question using ONLY the
        information provided in the context.

        If the answer is not available in the context,
        say: "The answer is not available in this video."

        Context:
        {context}

        Question:
        {question}

        Answer:
        """
    )

    # Step 4: Initialize LLM
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0
    )

    # Step 5: Create LCEL chain
    chain = prompt | llm

    # Step 6: Generate answer
    response = chain.invoke({
        "context": context,
        "question": query
    })

    return response.content
