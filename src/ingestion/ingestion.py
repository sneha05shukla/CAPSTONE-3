from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# Load document
loader = TextLoader("data/customer_support.txt")
documents = loader.load()

# Split documents
splitter = RecursiveCharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=50
)

docs = splitter.split_documents(documents)

print(f"Total Chunks Created: {len(docs)}")

# Create embeddings
from langchain_community.embeddings import FakeEmbeddings

embeddings = FakeEmbeddings(size=384)
# Create vector store
vector_db = FAISS.from_documents(
    docs,
    embeddings
)

# Save vector store
vector_db.save_local("vectorstore")

print("Vector Store Created Successfully")