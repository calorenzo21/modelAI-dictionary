from typing import List, TypedDict

class GraphState(TypedDict):
    """
    Represents the state of our graph.

    Attributes:
        question: question
        prompt: prompt template object
        response: result of the graph query
        type: type of the question 
    """

    question: str
    prompt: object
    response: object
    type: str