from typing import List, TypedDict


class GraphState(TypedDict):
    """
    Represents the state of our graph.

    Attributes:
        question: question
        generation: LLM generation
        web_search: whether to add search
        documents: list of documents
    """

    question: str #to check whether everything is related to it. So the state is always maintained
    generation: str #what the LLM generates
    web_search: bool #whether to search web or not
    documents: List[str] #store documents in the list