from src.retrieval.retriever import retrieve_documents
def rag_tool(query):

    docs = retrieve_documents(query)

    context = "\n".join(
        [doc.page_content for doc in docs]
    )

    return context