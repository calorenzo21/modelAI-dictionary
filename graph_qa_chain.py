import os
from graph_cypher_chain import GraphCypherQAChain
from langchain_community.graphs import Neo4jGraph
from state import GraphState
from prompts import qa_prompt_bio, qa_prompt_list, qa_prompt_multimedia, qa_prompt_comparison, qa_prompt_summary
from langchain_openai import ChatOpenAI

graph = Neo4jGraph(
    url=os.environ.get('AURA_CONNECTION_URI'),
    username=os.environ.get('AURA_USERNAME'),
    password=os.environ.get('AURA_PASSWORD')
)

llm = ChatOpenAI(
    model="gpt-4o", 
    temperature=0,
    api_key=os.environ.get("OPENAI_API_KEY"),
)

def get_graph_qa_chain_biography(state: GraphState):
    
    """Create a Neo4j Graph Cypher QA Chain"""
    
    prompt = state["prompt"]
    
    graph_qa_chain = GraphCypherQAChain.from_llm(
            cypher_llm = llm,
            qa_llm = llm,
            validate_cypher= True,
            graph=graph,
            verbose=True,
            cypher_prompt = prompt,
            qa_prompt = qa_prompt_bio,
            return_intermediate_steps = True,
            allow_dangerous_requests=True,
        )
    return graph_qa_chain

def get_graph_qa_chain_list(state: GraphState):
    """Create a Neo4j Graph Cypher QA Chain"""
    
    prompt = state["prompt"]
    
    graph_qa_chain = GraphCypherQAChain.from_llm(
            cypher_llm = llm,
            qa_llm = llm,
            validate_cypher= True,
            graph=graph,
            verbose=True,
            cypher_prompt = prompt,
            qa_prompt = qa_prompt_list,
            return_intermediate_steps = True,
            allow_dangerous_requests=True,
        )
    return graph_qa_chain

def get_graph_qa_chain_multimedia(state: GraphState):
    """Create a Neo4j Graph Cypher QA Chain"""
    
    prompt = state["prompt"]
    
    graph_qa_chain = GraphCypherQAChain.from_llm(
            cypher_llm = llm,
            qa_llm = llm,
            validate_cypher= True,
            graph=graph,
            verbose=True,
            cypher_prompt = prompt,
            qa_prompt = qa_prompt_multimedia,
            return_intermediate_steps = True,
            allow_dangerous_requests=True,
        )
    return graph_qa_chain

def get_graph_qa_chain_comparison(state: GraphState):
    """Create a Neo4j Graph Cypher QA Chain"""
    
    prompt = state["prompt"]
    
    graph_qa_chain = GraphCypherQAChain.from_llm(
            cypher_llm = llm,
            qa_llm = llm,
            validate_cypher= True,
            graph=graph,
            verbose=True,
            cypher_prompt = prompt,
            qa_prompt = qa_prompt_comparison,
            return_intermediate_steps = True,
            allow_dangerous_requests=True,
        )
    return graph_qa_chain

def get_graph_qa_chain_similarity(state: GraphState):
    """Create a Neo4j Graph Cypher QA Chain"""
    
    prompt = state["prompt"]
    
    graph_qa_chain = GraphCypherQAChain.from_llm(
            cypher_llm = llm,
            qa_llm = llm,
            validate_cypher= True,
            graph=graph,
            verbose=True,
            cypher_prompt = prompt,
            qa_prompt = qa_prompt_list,
            return_intermediate_steps = True,
            allow_dangerous_requests=True,
        )
    return graph_qa_chain

def get_graph_qa_chain_summary(state: GraphState):
    """Create a Neo4j Graph Cypher QA Chain"""
    
    prompt = state["prompt"]
    
    graph_qa_chain = GraphCypherQAChain.from_llm(
            cypher_llm = llm,
            qa_llm = llm,
            validate_cypher= True,
            graph=graph,
            verbose=True,
            cypher_prompt = prompt,
            qa_prompt = qa_prompt_summary,
            return_intermediate_steps = True,
            allow_dangerous_requests=True,
        )
    return graph_qa_chain