from typing import Any, Dict

from graph.state import GraphState
from ingestion import retriever

##get the current graph state. extract the questions
##retrieve relevant docs. Semmantic search capabilities of vector store

def retrieve(state: GraphState) -> Dict[str, Any]:
    print("---RETRIEVE---")
    question = state["question"]

    documents = retriever.invoke(question)
    return {"documents": documents, "question": question}