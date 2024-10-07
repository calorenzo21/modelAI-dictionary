from dotenv import load_dotenv
from langgraph.graph import StateGraph, END, START
from state import GraphState
from nodes import prompt_template, unrecognized_node, router_request, biography_qa, list_qa, router_question, multimedia_qa, similiraty_qa, comparison_qa
import os
load_dotenv(".env", override=True)
    
print(os.getenv("GEMINI_API_KEY"))
print(os.getenv("OPENAI_API_KEY"))

# Inicializar el grafo
workflow = StateGraph(GraphState)

# Agregar nodos al grafo
workflow.add_node("prompt_template", prompt_template)
workflow.add_node("unrecognized_node", unrecognized_node)
workflow.add_node("biography_qa", biography_qa)
workflow.add_node("list_qa", list_qa)
workflow.add_node("multimedia_qa", multimedia_qa)
workflow.add_node("similiraty_qa", similiraty_qa)
workflow.add_node("comparison_qa", comparison_qa)

# Transiciones entre los nodos
workflow.add_conditional_edges(START, router_request, { 
    "prompt_template": "prompt_template", 
    "unrecognized_node": "unrecognized_node" 
})
workflow.add_conditional_edges("prompt_template", router_question, { 
    "biography_qa": "biography_qa", 
    "list_qa": "list_qa",
    "multimedia_qa": "multimedia_qa",
    "similiraty_qa": "similiraty_qa",
    "comparison_qa": "comparison_qa"
})
workflow.add_edge("unrecognized_node", END)
workflow.add_edge("biography_qa", END)
workflow.add_edge("list_qa", END)
workflow.add_edge("multimedia_qa", END)
workflow.add_edge("similiraty_qa", END)
workflow.add_edge("comparison_qa", END)

app = workflow.compile()