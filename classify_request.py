from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from typing import Literal
import os

class RequestType(BaseModel):
    """
    Route a user query to the corresponding classification based on the type of request.
    
    Attributes:
        request_type: The classified type of request.
    """
    
    request_type: Literal["valid_request", "invalid_request"] = Field(
        ...,
        description="The classified request type."
    )

llm = ChatOpenAI(
    model="gpt-4o", 
    temperature=0,
    api_key=os.environ.get("OPENAI_API_KEY"),
)

structured_llm_router = llm.with_structured_output(RequestType)

system_prompt = """
Eres un experto en clasificar solicitudes de usuarios en una de las siguientes dos categorías. Las solicitudes serán proporcionadas en español y pueden tomar la forma de preguntas directas o comandos. Debes entender la solicitud y clasificarla en una de las categorías que se enumeran a continuación. Si la solicitud está relacionada con alguno de los elementos literarios especificados, clasifícala como "valid_request". Si no está relacionada, clasifícala como "invalid_request".

Contexto literario para solicitudes válidas:
Una solicitud válida debe estar relacionada con:

Información de autores: Datos biográficos (nombres, apellidos, fechas de nacimiento/muerte, lugares de nacimiento/muerte: ciudad, municipio, estado, país), género, seudónimos, actividades relevantes (profesión, estudios, cargos públicos), miembros familiares notables como (esposo, esposa, padres, hermanos, hermanas, hijos, hijas, primos, tíos), contexto en el que vivió el autor, imagen del autor (jpg), multimedia (enlace, tipo, restricciones), audio de la voz del autor (mp3), tema principal desarrollado en las obras del autor, género principal cultivado.

Obras: Datos bibliográficos, tipológicos y editoriales: títulos, géneros (novela, cuento, poesía, ensayo, etc.), subgéneros, fechas de publicación, lugar de publicación (ciudad, imprenta, editorial), resumen o descripción (autores, temas, números publicados en antologías/revistas), idioma original, multimedia (enlaces, tipos de archivo, restricciones), PDFs, portadas en JPG, audios en MP3 para descargar y lectura.

Crítica: Interpretaciones, lecturas y evaluaciones de obras y autores. Tipo de crítica (libro, artículo, reseña, tesis), autor, título, fecha de publicación, referencia bibliográfica, resumen o descripción, y enlaces a la crítica.

Grupos literarios, revistas y antologías: Grupos: nombre del grupo, lugar de encuentro (ciudad, municipio), fecha de inicio/finalización, características generales (ideología, tendencia), miembros (nombres, apellidos), publicaciones del grupo (título, año, resumen, autor), actividades del grupo. Revistas: título, fecha del primer y último número, números publicados, lugar de publicación (ciudad, imprenta, editorial), creadores (director, comité editorial), secciones, descripción (temas y géneros dominantes, autores notables), idioma original, multimedia (PDF, JPG). Antologías: autor, título, género, fecha de publicación, lugar de publicación (ciudad, imprenta, editorial), descripción o resumen (autores seleccionados), idioma original, multimedia (PDF, JPG).

Tarea:
Concéntrate solo en el núcleo de la solicitud y clasifícala en una de las categorías: "valid_request" o "invalid_request". Los verbos específicos utilizados en la solicitud no importan; en su lugar, enfócate en si la solicitud está pidiendo información relacionada con la literatura o no, otra cosa la solicitud puede tener información adicional como instrucciones especifica para generar la respuesta como decirle que tome un rol, o que la respuesta sea redactada de cierta forma, esto no debe ser problema. Recuerda, enfócate en el núcleo de la pregunta y lo que esta solicitando.

Ejemplos:
examples = [
    # Solicitudes válidas
    {{
        "question": "¿Cuándo nació el autor John Doe?",
        "category": "valid_request"
    }},
    {{
        "question": "Muéstrame una imagen del autor John Doe.",
        "category": "valid_request"
    }},
    {{
        "question": "Dime cuál es el lugar de publicación de la obra 'Cuentos de la selva'.",
        "category": "valid_request"
    }},
    {{
        "question": "¿Dónde se reunía el grupo de escritores de poesía en Caracas?",
        "category": "valid_request"
    }},
    {{
        "question": "¿Cuál es el tema principal de las obras de John Doe?",
        "category": "valid_request"
    }},
    {{
        "question": "Muéstrame el resumen de la crítica 'Literary Analysis of 'Great Short Stories''.",
        "category": "valid_request"
    }},
    {{
        "question": "¿Cuáles son las obras publicadas en Nueva York?",
        "category": "valid_request"
    }},
    {{
        "question": "Dame la lista de los miembros del grupo 'Generación del 27'.",
        "category": "valid_request"
    }},
    {{
        "question": "Muéstrame las antologías que contienen obras de Jorge Luis Borges.",
        "category": "valid_request"
    }},
    {{
        "question": "¿Cuál es el lugar de fallecimiento de Julio Cortázar?",
        "category": "valid_request"
    }},

    # Solicitudes inválidas
    {{
        "question": "¿Cuál es la mejor receta para hacer pizza?",
        "category": "invalid_request"
    }},
    {{
        "question": "¿Qué clima hacía cuando nació John Doe?",
        "category": "invalid_request"
    }},
    {{
        "question": "¿Cuánto mide Gabriel García Márquez?",
        "category": "invalid_request"
    }},
    {{
        "question": "Muéstrame una receta de empanadas.",
        "category": "invalid_request"
    }},
    {{
        "question": "¿Qué canción estaba de moda cuando publicaron 'Cien Años de Soledad'?",
        "category": "invalid_request"
    }},
    {{
        "question": "Dime qué día es hoy.",
        "category": "invalid_request"
    }},
    {{
        "question": "¿Cuál es el precio de un libro nuevo de 'El Llano en Llamas'?",
        "category": "invalid_request"
    }},
    {{
        "question": "Dame la biografía de un futbolista famoso.",
        "category": "invalid_request"
    }},
    {{
        "question": "¿Qué tipo de coche manejaba Gabriel García Márquez?",
        "category": "invalid_request"
    }},
    {{
        "question": "Muéstrame las canciones populares de los años 90.",
        "category": "invalid_request"
    }}
]
"""

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{question}")
    ]
)

request_classifier = prompt | structured_llm_router