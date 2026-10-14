from src.retrieval.retriever import retrieve_documents

def retrieval_agent(state):

    docs = retrieve_documents(
        state["query"]
    )

    context = "\n".join(
        [doc.page_content for doc in docs]
    )

    state["context"] = context

    return state