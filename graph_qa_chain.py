import os
from graph_cypher_chain import GraphCypherQAChain
from langchain_community.graphs import Neo4jGraph
from langchain.prompts.prompt import PromptTemplate
from state import GraphState
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

qa_template_bio = """
Task: You are required to generate a natural, fluent, and well-structured response in Spanish, using only the information provided from the Cypher query result executed in Neo4j.

Instructions:
Your response must be entirely based on the context provided below and should be written in Spanish.
It is strictly prohibited to introduce any information that is not explicitly present in the context.
Avoid adding any assumptions, elaborations, or additional facts, as this could lead to hallucinations, which we want to prevent.
Ensure that the response is clear, conversational, and flows naturally, while remaining strictly faithful to the provided information.
Do not infer or invent details not found in the original result, but use as much information from the context as you can to respond.

### Additional Instructions:
- Always return the response as a JSON object.
- The JSON object should contain the following properties (if available in the context):
  - `title`: The title found in the context, which could be the name of an author, the title of a work, or any other title such as a critique, magazine, group, or anthology.
  - `text`: The main response to the question, based on the context (this property is **always required**).
  - `multimedia`: A list of multimedia links categorized into:
      - `images`: List of image URLs with their descriptions (if any).
      - `videos`: List of video URLs with their descriptions (if any).
      - `audios`: List of audio URLs with their descriptions (if any).
      - `documents`: List of document URLs with their descriptions (if any).

- If the provided information is insufficient to answer the question, set `text` to "Lo siento, no tengo información acerca de {{tema relacionado}}" in the JSON.

- Only include properties (title, multimedia) if they are present in the context.

### Example JSON output:
{{
  "title": "Teresa Coraspe",
  "text": "This is the response based on the provided context.",
  "multimedia": {{
    "images": [{{"link": "http://example.com/image1.jpg", "description": "Description of image 1"}}],
    "videos": [{{"link": "http://example.com/video1.mp4", "description": "Description of video 1"}}],
    "audios": [{{"link": "http://example.com/audio1.mp3", "description": "Description of audio 1"}}],
    "documents": [{{"link": "http://example.com/doc1.pdf", "description": "Description of document 1"}}]
  }}
}}

Information: {context}
Question: {question}

Helpful Answer (in JSON format):
"""

qa_template_list = """
Task: You are required to generate a natural, fluent, and well-structured response in Spanish, using only the information provided from the Cypher query result executed in Neo4j.

Instructions:
Your response must be entirely based on the context provided below and should be written in Spanish. It is strictly prohibited to introduce any information that is not explicitly present in the context. However, you should use as much specific information as possible for each item in the context. Avoid adding assumptions, elaborations, or additional facts, as this could lead to hallucinations, which we want to prevent.

Ensure the response is clear, conversational, and flows naturally while remaining strictly faithful to the provided information. Do not infer or invent details not found in the original context, but use all available information for each specific item to generate a detailed, context-rich response.

### Additional Instructions:
Always return the response as a JSON object.

The JSON object should contain the following structure:

- `title`: The main title or identifier found in the context. This could vary depending on the nature of the elements being requested. For example, if it's a list of works, the title could be "Obras de (temática o de tal autor)", while for authors, it could be "Autores destacados". The title will reflect the type of elements being described (e.g., authors, critiques, works, etc.).
- `items`: An array where each element represents an individual item (e.g., author, magazine, work, etc.), structured as:
  - `title`: The title or identifier for each item.
  - `text`: A description or summary of the item based on the context.
  - `multimedia`: A list of multimedia links categorized into:
      - `images`: List of image URLs with their descriptions (if any).
      - `videos`: List of video URLs with their descriptions (if any).
      - `audios`: List of audio URLs with their descriptions (if any).
      - `documents`: List of document URLs with their descriptions (if any).

If the provided information is insufficient to answer the question, set the `text` field to "No sé la respuesta" (I don't know the answer) in the JSON.

### Example JSON output:
{{
  "title": "Titulo Relacionado al Listado Ejm (Obras de Ciencia Ficción de Autor X)",
  "items": [
    {{
      "title": "Título de la Obra 1",
      "text": "Descripción o resumen del elemento basado en el contexto",
      "multimedia": {{
        "images": [{{"link": "http://example.com/image1.jpg", "description": "Description of image 1"}}],
        "videos": [{{"link": "http://example.com/video1.mp4", "description": "Description of video 1"}}],
        "audios": [{{"link": "http://example.com/audio1.mp3", "description": "Description of audio 1"}}],
        "documents": [{{"link": "http://example.com/doc1.pdf", "description": "Description of document 1"}}]
      }}
    }},
    {{
      "title": "Título de la Obra 2",
      "text": "Descripción o resumen del segundo elemento",
      "multimedia": {{
        "images": [{{"link": "http://example.com/image1.jpg", "description": "Description of image 1"}}],
        "videos": [{{"link": "http://example.com/video1.mp4", "description": "Description of video 1"}}],
        "audios": [{{"link": "http://example.com/audio1.mp3", "description": "Description of audio 1"}}],
        "documents": [{{"link": "http://example.com/doc1.pdf", "description": "Description of document 1"}}]
      }}
    }}
  ]
}}

### Information:
{context}

### Question:
{question}

Helpful Answer (in JSON format):
"""

qa_template_multimedia = """
You are tasked with generating a JSON response based on multimedia query results. You will receive a context that includes both a question and a query related to multimedia content (such as images, videos, audios, or documents) associated with a variety of entities, including authors, critical works, anthologies, magazines, or groups.

Your job is to:

- Parse the input and generate a structured JSON response.
- Return only the fields that are present in the query result (e.g., if no videos are present, do not include the videos field in the output).
- Ensure the `title` field contains the name or title of the relevant entity (which could be an author, anthology, magazine, group, etc.).
- Include arrays for multimedia links: `images`, `videos`, `audios`, and `documents`—only if they are present in the query result.

### Additional Instructions:
- Return **strictly** the JSON output. It is prohibited to return any additional text, explanations, or comments.
- If a multimedia type is missing from the result (e.g., no images), **exclude** that field from the JSON output.

### Expected Output Structure:
Your response must always return a JSON object with the following structure:

- `title`: The name or title of the relevant entity (could be an author, work, anthology, magazine, or group).
- Optionally include one or more of the following arrays based on the multimedia types present in the query result:
  - `images`: An array of image objects, each containing:
    - `link`: The URL to the image.
    - `description`: A brief description of the image.
  - `videos`: An array of video objects, each containing:
    - `link`: The URL to the video.
    - `description`: A brief description of the video.
  - `audios`: An array of audio objects, each containing:
    - `link`: The URL to the audio.
    - `description`: A brief description of the audio.
  - `documents`: An array of document objects, each containing:
    - `link`: The URL to the document.
    - `description`: A brief description of the document.

### Important Notes:
- Only include fields (e.g., `images`, `videos`, etc.) that contain data in the query result.
- If the query does not return any multimedia of a certain type (e.g., no videos), exclude the corresponding field from the JSON response.
- Return strictly the JSON. No explanations, text, or additional information.

### Example JSON output:
{{
  "title": "Multimedia de (temática puede ser un autor, obra, crítica, etc.)",
  "multimedia": {{
    "images": [{{"link": "http://example.com/image1.jpg", "description": "Description of image 1"}}],
    "videos": [{{"link": "http://example.com/video1.mp4", "description": "Description of video 1"}}],
    "audios": [{{"link": "http://example.com/audio1.mp3", "description": "Description of audio 1"}}],
    "documents": [{{"link": "http://example.com/doc1.pdf", "description": "Description of document 1"}}]
  }}
}}

### Information:
{context}
### Question:
{question}
"""

qa_template_comparison = """
You are tasked with generating a JSON object that compares two or more literary works. The comparison input will consist of multiple objects, each containing multimedia links and descriptive text about the work. Your role is to behave as a literature professor and perform a comparative analysis that focuses on the key aspects of each work, including themes, publication context, narrative, and innovation. Ensure that your analysis is insightful and highlights relevant literary elements.

Input Structure:
You will receive an array called comparacion that includes two or more objects with the following structure:

multimedia: An array of multimedia links associated with the work (e.g., images, videos, etc.).
texto: A description of the work that provides details about its content, including themes, genre, publication details, and any distinctive elements.

Output Structure:
Your response must always be a JSON object with the following structure:

titulo: A title that reflects the comparison between the works (e.g., "comparacion obra1 - obra2").
analisis: A detailed comparative analysis between the works based on the provided text, emphasizing key literary aspects.
multimedia: A combined array of all multimedia links from the works being compared.

Important Notes:
You must strictly return only the JSON object without any additional text or explanation.
The titulo should be based on the nature of the works being compared.
The multimedia array should merge all multimedia links from the works.
The analysis must be insightful, professional, and written from the perspective of a literature professor, comparing aspects such as themes, genre, narrative, and innovation in the works.

Example Input:
{{
  "comparacion": [
    {{
      "multimedia": [
        "https://example.com/machine_cover_new.jpg"
      ],
      "texto": "//DESCRIPCION DE LA OBRA//"
    }},
    {{
      "multimedia": [
        "https://example.com/cover.jpg"
      ],
      "texto": "//DESCRIPCION DE LA OBRA//"
    }}
  ]
}}
Example Output:
{{
  "titulo": "Comparación entre Obra1 Y Obra2",
  "analisis": "//ANALISIS COMPARATIVO//",
  "multimedia": [
    "https://example.com/machine_cover_new.jpg",
    "https://example.com/cover.jpg"
  ]
}}
Information: {context}
Question: {question}
"""

qa_prompt_bio = PromptTemplate(
    input_variables=["context", "question"], template=qa_template_bio
)

qa_prompt_list = PromptTemplate(
    input_variables=["context", "question"], template=qa_template_list
)

qa_prompt_multimedia = PromptTemplate(
    input_variables=["context", "question"], template=qa_template_multimedia
)

qa_prompt_comparison = PromptTemplate(
    input_variables=["context", "question"], template=qa_template_comparison
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