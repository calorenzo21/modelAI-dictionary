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
- Ensure the `title` field contains the name or title of the relevant entity (which could be an author, anthology, magazine, group, etc.).
- Always include arrays for the multimedia object: `images`, `videos`, `audios`, and `documents`, even if they are empty.

### Additional Instructions:
- Return **strictly** the JSON output. It is prohibited to return any additional text, explanations, or comments.
- If no multimedia is found for a certain type (e.g., no images or videos), return an empty array for that field (e.g., `"images": []`).

### Expected Output Structure:
Your response must always return a JSON object with the following structure:

- `title`: The name or title of the relevant entity (could be an author, work, anthology, magazine, or group).
- Always include the following arrays in the multimedia property:
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
- Even if no data is found for a specific type of multimedia, always include the field with an empty array (e.g., `"images": []`, `"videos": []`).
- Return strictly the JSON. No explanations, text, or additional information.

### Example JSON output:
{{
  "title": "Multimedia de (temática puede ser un autor, obra, crítica, etc.)",
  "multimedia": {{
    "images": [{{"link": "http://example.com/image1.jpg", "description": "Description of image 1"}}],
    "videos": [],
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
You are tasked with generating a JSON object that compares two or more literary elements. The comparison input will consist of multiple objects, each containing multimedia links and descriptive text about the element (which could be a work, author, critique, magazine, anthology, or grouping). Your role is to behave as a literature professor and perform a comparative analysis that focuses on the key aspects of each element, including themes, publication context, narrative, innovation, or any other relevant literary aspect depending on the nature of the elements being compared. Ensure that your analysis is insightful and highlights important literary elements.

Input Structure:
You will receive an array called comparacion that includes two or more objects with the following structure:

multimedia: An array of multimedia links associated with the element (e.g., images, videos, etc.).
texto: A description of the element that provides details about its content, including themes, genre, publication details, and any distinctive elements.

Output Structure:
Your response must always be a JSON object with the following structure:

title: A title that reflects the comparison between the elements (e.g., "Comparación entre [Elemento 1] y [Elemento 2]"). The elements could be works, authors, critiques, magazines, anthologies, or groupings.
text: A detailed comparative analysis between the elements based on the provided text, emphasizing key literary aspects.
items: A combined array of all multimedia links, descriptions, and titles from the elements being compared.

Important Notes:
- You must strictly return only the JSON object without any additional text or explanation.
- The title should be based on the nature of the elements being compared (authors, works, critiques, magazines, anthologies, or groupings).
- The multimedia array should merge all multimedia links from the elements.
- The analysis must be insightful, professional, and written from the perspective of a literature professor, comparing aspects such as themes, genre, narrative, and innovation, adapted to the type of element (whether it's an author, work, critique, magazine, anthology, or grouping).

Example Input:
{{
  "comparacion": [
    {{
      "multimedia": {{
        "imagenes": [
          {{"description": "Descripción de la imagen 1", "link": "https://example.com/imagen1.jpg"}},
          {{"description": "Descripción de la imagen 2", "link": "https://example.com/imagen2.jpg"}}
        ],
        "videos": [
          {{"description": "Descripción del video 1", "link": "https://example.com/video1.mp4"}}
        ],
        "audios": [
          {{"description": "Descripción del audio 1", "link": "https://example.com/audio1.mp3"}}
        ],
        "documentos": [
          {{"description": "Descripción del documento 1", "link": "https://example.com/documento1.pdf"}}
        ]
      }},
      "texto": "//Descripción de la obra A//"
    }},
    {{
      "multimedia": {{
        "imagenes": [
          {{"description": "Descripción de la imagen 3", "link": "https://example.com/imagen3.jpg"}}
        ],
        "videos": [
          {{"description": "Descripción del video 2", "link": "https://example.com/video2.mp4"}}
        ],
        "audios": [
          {{"description": "Descripción del audio 2", "link": "https://example.com/audio2.mp3"}}
        ],
        "documentos": [
          {{"description": "Descripción del documento 2", "link": "https://example.com/documento2.pdf"}}
        ]
      }},
      "texto": "//Descripción de la obra B//"
    }}
  ]
}}

Example Output:
{{
  "title": "Comparación entre Elemento 1 y Elemento 2",
  "text": "//ANALISIS COMPARATIVO//",
  "items": [
    {{
      "title": "Título del Elemento 1",
      "multimedia": {{
        "images": [{{"link": "http://example.com/imagen1.jpg", "description": "Descripción de la imagen 1"}}],
        "videos": [{{"link": "http://example.com/video1.mp4", "description": "Descripción del video 1"}}],
        "audios": [{{"link": "http://example.com/audio1.mp3", "description": "Descripción del audio 1"}}],
        "documents": [{{"link": "http://example.com/documento1.pdf", "description": "Descripción del documento 1"}}]
      }}
    }},
    {{
      "title": "Título del Elemento 2",
      "multimedia": {{
        "images": [{{"link": "http://example.com/imagen3.jpg", "description": "Descripción de la imagen 3"}}],
        "videos": [{{"link": "http://example.com/video2.mp4", "description": "Descripción del video 2"}}],
        "audios": [{{"link": "http://example.com/audio2.mp3", "description": "Descripción del audio 2"}}],
        "documents": [{{"link": "http://example.com/documento2.pdf", "description": "Descripción del documento 2"}}]
      }}
    }}
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