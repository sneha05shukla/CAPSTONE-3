from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

from langchain_community.embeddings import FakeEmbeddings

embeddings = FakeEmbeddings(size=384)
db = FAISS.load_local(
    "vectorstore",
    embeddings,
    allow_dangerous_deserialization=True
)

retriever = db.as_retriever(
    search_kwargs={"k": 3}
)

def retrieve_documents(query):
    docs = retriever.invoke(query)
    return docs