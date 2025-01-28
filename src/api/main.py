from fastapi import FastAPI, Query
from src.models.llama import LlamaModel

app = FastAPI()
llama = LlamaModel()

@app.get("/")
def read_root():
    return {"message": "Agentic RAG is running!"}

@app.get("/query/")
def ask_agent(query: str = Query(..., description="User query")):
    response = llama.generate_response(f"Answer this query: {query}")
    return {"query": query, "response": response}