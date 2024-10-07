import os
from state import GraphState
from promp_template import create_few_shot_prompt
from graph_qa_chain import get_graph_qa_chain_biography, get_graph_qa_chain_list, get_graph_qa_chain_multimedia, get_graph_qa_chain_comparison, get_graph_qa_chain_similarity
from classify_question import question_classifier
from classify_request import request_classifier

def router_request(state: GraphState):
    '''Returns the next step in the control flow based on the type of request'''
    
    question = state["question"]
    request_type = request_classifier.invoke({"question": question}).request_type
    
    if request_type == "valid_request":
        print("---ROUTE REQUEST TO VALID REQUEST HANDLER---")
        return "prompt_template"
    elif request_type == "invalid_request":
        print("---ROUTE REQUEST TO INVALID REQUEST HANDLER---")
        return "unrecognized_node"

def unrecognized_node(state: GraphState):
    print("---UNRECOGNIZED NODE---")

def prompt_template(state: GraphState):
    '''Returns a dictionary of at least one of the GraphState'''
    '''Create a dynamic prompt template for graph qa with context chain'''

    prompt = create_few_shot_prompt()

    return {"prompt" : prompt, "question": state['question']}

def router_question(state: GraphState):
    '''Returns a dictionary of at least one of the GraphState'''
    '''Route the question to the corresponding chain based on the type of question'''

    question = state["question"]
    type = question_classifier.invoke({"question": question}).question_type
    
    if type == "biography":
        print("---ROUTE QUESTION TO BIOGRAPHY---")
        return "biography_qa"
    elif type == "list":
        print("---ROUTE QUESTION TO LIST---")
        return "list_qa"
    elif type == "comparison":
        print("---ROUTE QUESTION TO COMPARISON---")
        return "comparison_qa"
    elif type == "multimedia":
        print("---ROUTE QUESTION TO MULTIMEDIA---")
        return "multimedia_qa"
    elif type == "similarity":
        print("---ROUTE QUESTION TO SIMILARITY---")
        return "similiraty_qa"



def biography_qa(state: GraphState):
    
    ''' Returns a dictionary of at least one of the GraphState '''
    ''' Invoke a Graph QA Chain to answer a biography question '''
    
    print("---BIORAPHY QA---")
    question = state["question"]
    
    graph_qa_chain = get_graph_qa_chain_biography(state)
    
    result = graph_qa_chain.invoke(
        { 
            "query": question,
        },
    )

    return {"response": result, "question":question, "type":"biography"}

def list_qa(state: GraphState):
    
    ''' Returns a dictionary of at least one of the GraphState '''
    ''' Invoke a Graph QA Chain to answer a list question'''
    
    print("---LIST QA---")
    question = state["question"]
    
    graph_qa_chain = get_graph_qa_chain_list(state)
    
    result = graph_qa_chain.invoke(
        { 
            "query": question,
        },
    )

    return {"response": result, "question":question, "type": "list"}

def multimedia_qa(state: GraphState):
    
    ''' Returns a dictionary of at least one of the GraphState '''
    ''' Invoke a Graph QA Chain to answer a multimedia question'''
    
    print("---MULTIMEDIA QA---")
    question = state["question"]
    
    graph_qa_chain = get_graph_qa_chain_multimedia(state)
    
    result = graph_qa_chain.invoke(
        { 
            "query": question,
        },
    )

    return {"response": result, "question":question, "type": "multimedia"}

def similiraty_qa(state: GraphState):
    
    ''' Returns a dictionary of at least one of the GraphState '''
    ''' Invoke a Graph QA Chain to answer a similarity question'''
    
    print("---SIMILARITY QA---")
    question = state["question"]
    
    graph_qa_chain = get_graph_qa_chain_similarity(state)
    
    result = graph_qa_chain.invoke(
        { 
            "query": question,
            "openAIapiKey" : os.getenv("OPENAI_API_KEY")
        },
    )

    return {"response": result, "question":question, "type": "similarity"}

def comparison_qa(state: GraphState):
    
    ''' Returns a dictionary of at least one of the GraphState '''
    ''' Invoke a Graph QA Chain to answer a comparison question'''
    
    print("---SIMILARITY QA---")
    question = state["question"]
    
    graph_qa_chain = get_graph_qa_chain_comparison(state)
    
    result = graph_qa_chain.invoke(
        { 
            "query": question,
        },
    )

    return {"response": result, "question":question, "type": "comparison"}

