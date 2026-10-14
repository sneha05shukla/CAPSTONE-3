import os
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import FakeEmbeddings

embeddings = FakeEmbeddings(size=384)

db = None

if os.path.exists("vectorstore/index.faiss"):
    db = FAISS.load_local(
        "vectorstore",
        embeddings,
        allow_dangerous_deserialization=True
    )


def retrieve_documents(query):

    if db is None:
        return ["Vector store not available"]

    retriever = db.as_retriever(search_kwargs={"k": 3})

    docs = retriever.invoke(query)

    return [doc.page_content for doc in docs]