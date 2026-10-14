from fastapi import FastAPI
from pydantic import BaseModel

from src.graph.workflow import graph

app = FastAPI()

class QueryRequest(BaseModel):
    session_id: str
    query: str

@app.get("/")
def home():
    return {"message": "RAG API Running"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/query")
def query(data: QueryRequest):

    result = graph.invoke(
        {
            "query": data.query
        }
    )

    return result
class FeedbackRequest(BaseModel):
    query: str
    feedback: str

@app.post("/feedback")
def feedback(data: FeedbackRequest):

    return {
        "message": "Feedback Received",
        "query": data.query,
        "feedback": data.feedback
    }