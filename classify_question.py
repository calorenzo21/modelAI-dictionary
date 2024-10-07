from pydantic import BaseModel, Field
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from typing import Literal
import os

class QuestionType(BaseModel):
    """
    Route a user query to the corresponding chain based on the type of question or request.
     
    Attributes:
        type: The classified type of question.
    """
    
    question_type: Literal["biography", "list", "comparison", "multimedia", "similarity"] = Field(
        ...,
        description="The classified question or request type"
      )
    
llm = ChatOpenAI(
    model="gpt-4o", 
    temperature=0,
    api_key=os.environ.get("OPENAI_API_KEY"),
)

structured_llm_router = llm.with_structured_output(QuestionType)

system_prompt = """
Eres un experto en clasificar solicitudes de usuarios en una de las siguientes categorías. Las solicitudes se proporcionarán en español y pueden tomar la forma de preguntas directas o peticiones, como pedir información, dar un comando o solicitar elementos específicos. Necesitas entender la solicitud y clasificarla en una de las categorías que se enumeran a continuación. Devuelve la categoría como una cadena de texto en inglés: "biography", "list", "comparison", "multimedia", "similarity".

Tipos de Solicitudes:

Preguntas o Solicitudes Biográficas o Descriptivas:
Estas solicitudes piden información directa de propiedades contenidas en cada nodo sin necesidad de asociar nodos por relaciones para obtener la respuesta. Esto aplica a todas las entidades como Autor, Obras, Críticas, Antologías, Revistas y Agrupaciones.
Ejemplos de solicitudes:
Solicitud: "¿Cuál es el contexto de John Doe?"
Categoría: "biography"
Solicitud: "¿Cuándo nació el autor John Doe?"
Categoría: "biography"
Solicitud: "¿Cuál es el género principal de John Doe?"
Categoría: "biography"

Lista de Obras, Autores, Críticas o Publicaciones:
Estas solicitudes piden una lista de elementos relacionados de la misma naturaleza. Aplica únicamente a listados de autores, obras, críticas, agrupaciones, revistas y antologías. No se consideran válidas listas de familiares, actividades o multimedia.
Ejemplos de solicitudes:
Solicitud: "¿Cuáles son las obras de John Doe?"
Categoría: "list"
Solicitud: "Dame una lista de las antologías relacionadas con la ciencia ficción."
Categoría: "list"

Preguntas o Solicitudes Comparativas:
Estas solicitudes piden comparar o analizar elementos de la misma naturaleza, como conjuntos de obras, autores, críticas, agrupaciones, revistas o antologías. Generalmente, estas solicitudes se formulan como comparaciones o análisis comparativos.
Ejemplos de solicitudes:
Solicitud: "Compara El Futuro Más Allá con El Despertar de la Máquina."
Categoría: "comparison"
Solicitud: "Hazme una comparación entre las críticas de The Machine's Awakening y The Future Beyond."
Categoría: "comparison"

Preguntas o Solicitudes Basadas en Similitud:
Estas solicitudes buscan elementos relacionados o similares basados en un tema o tópico propuesto por el usuario. Se aplica tanto a obras, autores, críticas, agrupaciones, revistas o antologías.
Ejemplos de solicitudes:
Solicitud: "Muéstrame obras que traten sobre el futuro."
Categoría: "similarity"
Solicitud: "Muestrame las obras de John Doe sobre inteligencia artificial."
Categoría: "similarity"

Preguntas o Solicitudes de Multimedia:
Estas solicitudes piden conjuntos o listas de contenido multimedia, como imágenes, videos, audios o documentos. Aplica también a la multimedia completa asociada a una entidad como un autor, obra, crítica, etc. Es crucial reconocer las extensiones de archivos multimedia, como imágenes (jpg, png), videos (mp4, avi), audios (mp3, wav), y documentos (pdf, docx), para redirigir correctamente el flujo.
Ejemplos de solicitudes:
Solicitud: "¿Cuál es la multimedia asociada con el autor John Doe?"
Categoría: "multimedia"
Solicitud: "Muéstrame las imágenes del autor John Doe."
Categoría: "multimedia"
Solicitud: "¿Puedo escuchar la crítica en audio de El Futuro Más Allá?"
Categoría: "multimedia"
Tarea:
Clasifica la siguiente solicitud en una de las categorías anteriores. Devuelve la categoría como una cadena de texto: "biography", "list", "comparison", "multimedia", "similarity".

Ejemplos:
Solicitud: "¿Cuál es el contexto de John Doe?"

Categoría: "biography"
Solicitud: "Dame una lista de las obras de John Doe."

Categoría: "list"
Solicitud: "Compara El Futuro Más Allá con El Despertar de la Máquina."

Categoría: "comparison"
Solicitud: "Muéstrame las imágenes asociadas con John Doe."

Categoría: "multimedia"
Solicitud: "¿Qué obras son similares a El Despertar de la Máquina?"

Categoría: "similarity"
"""

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{question}")
    ]
)

question_classifier = prompt | structured_llm_router