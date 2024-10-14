examples = [
    # Preguntas Descriptivas Sobre Autor
    {
        "question": "¿Cuál es el contexto de John Doe?",
        "query": '''CALL db.index.fulltext.queryNodes('fullTextAuthorNames', 'John Doe ') YIELD node AS a OPTIONAL MATCH (a)-[:HAS_MULTIMEDIA]->(m:Multimedia) WITH a, collect({{link: m.link, description: m.description, type: m.type}}) AS multimedia RETURN a.fullName AS titulo, a.text AS contexto, {{imagenes: [item IN multimedia WHERE item.type = 'image' | {{link: item.link, description: item.description}}], videos: [item IN multimedia WHERE item.type = 'video' | {{link: item.link, description: item.description}}], audios: [item IN multimedia WHERE item.type = 'audio' | {{link: item.link, description: item.description}}], documentos: [item IN multimedia WHERE item.type = 'application' | {{link: item.link, description: item.description}}]}} AS multimedia'''
    },
    {
        "question": "¿Cuándo nació el autor John Doe?",
        "query": '''CALL db.index.fulltext.queryNodes('fullTextAuthorNames', 'John Doe') YIELD node AS a OPTIONAL MATCH (a)-[:HAS_MULTIMEDIA]->(m:Multimedia) WITH a, collect({{link: m.link, description: m.description, type: m.type}}) AS multimedia RETURN a.fullName AS titulo, a.text AS contexto, {{imagenes: [item IN multimedia WHERE item.type = 'image' | {{link: item.link, description: item.description}}], videos: [item IN multimedia WHERE item.type = 'video' | {{link: item.link, description: item.description}}], audios: [item IN multimedia WHERE item.type = 'audio' | {{link: item.link, description: item.description}}], documentos: [item IN multimedia WHERE item.type = 'application' | {{link: item.link, description: item.description}}]}} AS multimedia'''
    },
    {
        "question": "¿Cuándo falleció el autor John Doe?",
        "query": '''CALL db.index.fulltext.queryNodes('fullTextAuthorNames', 'John Doe') YIELD node AS a OPTIONAL MATCH (a)-[:HAS_MULTIMEDIA]->(m:Multimedia) WITH a, collect({{link: m.link, description: m.description, type: m.type}}) AS multimedia RETURN a.fullName AS titulo, a.text AS contexto, {{imagenes: [item IN multimedia WHERE item.type = 'image' | {{link: item.link, description: item.description}}], videos: [item IN multimedia WHERE item.type = 'video' | {{link: item.link, description: item.description}}], audios: [item IN multimedia WHERE item.type = 'audio' | {{link: item.link, description: item.description}}], documentos: [item IN multimedia WHERE item.type = 'application' | {{link: item.link, description: item.description}}]}} AS multimedia'''
    },
    {
        "question": "¿Cuál es el género de John Doe?",
        "query": '''CALL db.index.fulltext.queryNodes('fullTextAuthorNames', 'John Doe') YIELD node AS a OPTIONAL MATCH (a)-[:HAS_MULTIMEDIA]->(m:Multimedia) WITH a, collect({{link: m.link, description: m.description, type: m.type}}) AS multimedia RETURN a.fullName AS titulo, a.text AS contexto, {{imagenes: [item IN multimedia WHERE item.type = 'image' | {{link: item.link, description: item.description}}], videos: [item IN multimedia WHERE item.type = 'video' | {{link: item.link, description: item.description}}], audios: [item IN multimedia WHERE item.type = 'audio' | {{link: item.link, description: item.description}}], documentos: [item IN multimedia WHERE item.type = 'application' | {{link: item.link, description: item.description}}]}} AS multimedia'''
    },
    {
        "question": "¿Cuál es el género principal de John Doe?",
        "query": '''CALL db.index.fulltext.queryNodes('fullTextAuthorNames', 'John Doe') YIELD node AS a OPTIONAL MATCH (a)-[:HAS_MULTIMEDIA]->(m:Multimedia) WITH a, collect({{link: m.link, description: m.description, type: m.type}}) AS multimedia RETURN a.fullName AS titulo, a.text AS contexto, {{imagenes: [item IN multimedia WHERE item.type = 'image' | {{link: item.link, description: item.description}}], videos: [item IN multimedia WHERE item.type = 'video' | {{link: item.link, description: item.description}}], audios: [item IN multimedia WHERE item.type = 'audio' | {{link: item.link, description: item.description}}], documentos: [item IN multimedia WHERE item.type = 'application' | {{link: item.link, description: item.description}}]}} AS multimedia'''
    },
    {
        "question": "¿Cuál es el tema principal en las obras de John Doe?",
        "query": '''CALL db.index.fulltext.queryNodes('fullTextAuthorNames', 'John Doe') YIELD node AS a OPTIONAL MATCH (a)-[:HAS_MULTIMEDIA]->(m:Multimedia) WITH a, collect({{link: m.link, description: m.description, type: m.type}}) AS multimedia RETURN a.fullName AS titulo, a.text AS contexto, {{imagenes: [item IN multimedia WHERE item.type = 'image' | {{link: item.link, description: item.description}}], videos: [item IN multimedia WHERE item.type = 'video' | {{link: item.link, description: item.description}}], audios: [item IN multimedia WHERE item.type = 'audio' | {{link: item.link, description: item.description}}], documentos: [item IN multimedia WHERE item.type = 'application' | {{link: item.link, description: item.description}}]}} AS multimedia'''
    },
    {
        "question": "¿Dónde nació John Doe?",
        "query": '''CALL db.index.fulltext.queryNodes('fullTextAuthorNames', 'John Doe') YIELD node AS a OPTIONAL MATCH (a)-[:HAS_MULTIMEDIA]->(m:Multimedia) WITH a, collect({{link: m.link, description: m.description, type: m.type}}) AS multimedia RETURN a.fullName AS titulo, a.text AS contexto, {{imagenes: [item IN multimedia WHERE item.type = 'image' | {{link: item.link, description: item.description}}], videos: [item IN multimedia WHERE item.type = 'video' | {{link: item.link, description: item.description}}], audios: [item IN multimedia WHERE item.type = 'audio' | {{link: item.link, description: item.description}}], documentos: [item IN multimedia WHERE item.type = 'application' | {{link: item.link, description: item.description}}]}} AS multimedia'''
    },
    {
        "question": "¿Dónde falleció John Doe?",
        "query": '''CALL db.index.fulltext.queryNodes('fullTextAuthorNames', 'John Doe') YIELD node AS a OPTIONAL MATCH (a)-[:HAS_MULTIMEDIA]->(m:Multimedia) WITH a, collect({{link: m.link, description: m.description, type: m.type}}) AS multimedia RETURN a.fullName AS titulo, a.text AS contexto, {{imagenes: [item IN multimedia WHERE item.type = 'image' | {{link: item.link, description: item.description}}], videos: [item IN multimedia WHERE item.type = 'video' | {{link: item.link, description: item.description}}], audios: [item IN multimedia WHERE item.type = 'audio' | {{link: item.link, description: item.description}}], documentos: [item IN multimedia WHERE item.type = 'application' | {{link: item.link, description: item.description}}]}} AS multimedia'''
    },
    {
        "question": "¿Cuál es el seudónimo de John Doe?",
        "query": '''CALL db.index.fulltext.queryNodes('fullTextAuthorNames', 'John Doe') YIELD node AS a OPTIONAL MATCH (a)-[:HAS_MULTIMEDIA]->(m:Multimedia) WITH a, collect({{link: m.link, description: m.description, type: m.type}}) AS multimedia RETURN a.fullName AS titulo, a.text AS contexto, {{imagenes: [item IN multimedia WHERE item.type = 'image' | {{link: item.link, description: item.description}}], videos: [item IN multimedia WHERE item.type = 'video' | {{link: item.link, description: item.description}}], audios: [item IN multimedia WHERE item.type = 'audio' | {{link: item.link, description: item.description}}], documentos: [item IN multimedia WHERE item.type = 'application' | {{link: item.link, description: item.description}}]}} AS multimedia'''
    },
    {
        "question": "¿Cuáles son las actividades relevantes de John Doe?",
        "query": '''CALL db.index.fulltext.queryNodes('fullTextAuthorNames', 'John Doe') YIELD node AS a OPTIONAL MATCH (a)-[:HAS_MULTIMEDIA]->(m:Multimedia) WITH a, collect({{link: m.link, description: m.description, type: m.type}}) AS multimedia RETURN a.fullName AS titulo, a.text AS contexto, {{imagenes: [item IN multimedia WHERE item.type = 'image' | {{link: item.link, description: item.description}}], videos: [item IN multimedia WHERE item.type = 'video' | {{link: item.link, description: item.description}}], audios: [item IN multimedia WHERE item.type = 'audio' | {{link: item.link, description: item.description}}], documentos: [item IN multimedia WHERE item.type = 'application' | {{link: item.link, description: item.description}}]}} AS multimedia'''
    },
    #  Preguntas Relación Familiares (Author)
    {
        "question": "¿Qué parientes tiene el autor John Doe?",
        "query": "CALL db.index.fulltext.queryNodes('fullTextAuthorNames', 'John Doe') YIELD node AS a OPTIONAL MATCH (a)-[:HAS_MULTIMEDIA]->(m:Multimedia) WITH a, collect({{link: m.link, description: m.description, type: m.type}}) AS multimedia RETURN a.fullName AS titulo, a.text AS contexto, {{imagenes: [item IN multimedia WHERE item.type = 'image' | {{link: item.link, description: item.description}}], videos: [item IN multimedia WHERE item.type = 'video' | {{link: item.link, description: item.description}}], audios: [item IN multimedia WHERE item.type = 'audio' | {{link: item.link, description: item.description}}], documentos: [item IN multimedia WHERE item.type = 'application' | {{link: item.link, description: item.description}}]}} AS multimedia"
    },
    {
        "question": "¿Quienes son los familiares John Doe?",
        "query": "CALL db.index.fulltext.queryNodes('fullTextAuthorNames', 'John Doe') YIELD node AS a OPTIONAL MATCH (a)-[:HAS_MULTIMEDIA]->(m:Multimedia) WITH a, collect({{link: m.link, description: m.description, type: m.type}}) AS multimedia RETURN a.fullName AS titulo, a.text AS contexto, {{imagenes: [item IN multimedia WHERE item.type = 'image' | {{link: item.link, description: item.description}}], videos: [item IN multimedia WHERE item.type = 'video' | {{link: item.link, description: item.description}}], audios: [item IN multimedia WHERE item.type = 'audio' | {{link: item.link, description: item.description}}], documentos: [item IN multimedia WHERE item.type = 'application' | {{link: item.link, description: item.description}}]}} AS multimedia"
    },
    {
        "question": "¿Quienes son los padres John Doe?",
        "query": "CALL db.index.fulltext.queryNodes('fullTextAuthorNames', 'John Doe') YIELD node AS a OPTIONAL MATCH (a)-[:HAS_MULTIMEDIA]->(m:Multimedia) WITH a, collect({{link: m.link, description: m.description, type: m.type}}) AS multimedia RETURN a.fullName AS titulo, a.text AS contexto, {{imagenes: [item IN multimedia WHERE item.type = 'image' | {{link: item.link, description: item.description}}], videos: [item IN multimedia WHERE item.type = 'video' | {{link: item.link, description: item.description}}], audios: [item IN multimedia WHERE item.type = 'audio' | {{link: item.link, description: item.description}}], documentos: [item IN multimedia WHERE item.type = 'application' | {{link: item.link, description: item.description}}]}} AS multimedia"
    },
    {
        "question": "¿Quienes son los hijos John Doe?",
        "query": "CALL db.index.fulltext.queryNodes('fullTextAuthorNames', 'John Doe') YIELD node AS a OPTIONAL MATCH (a)-[:HAS_MULTIMEDIA]->(m:Multimedia) WITH a, collect({{link: m.link, description: m.description, type: m.type}}) AS multimedia RETURN a.fullName AS titulo, a.text AS contexto, {{imagenes: [item IN multimedia WHERE item.type = 'image' | {{link: item.link, description: item.description}}], videos: [item IN multimedia WHERE item.type = 'video' | {{link: item.link, description: item.description}}], audios: [item IN multimedia WHERE item.type = 'audio' | {{link: item.link, description: item.description}}], documentos: [item IN multimedia WHERE item.type = 'application' | {{link: item.link, description: item.description}}]}} AS multimedia"
    },
    {
        "question": "¿Quienes son los hermanos John Doe?",
        "query": "CALL db.index.fulltext.queryNodes('fullTextAuthorNames', 'John Doe') YIELD node AS a OPTIONAL MATCH (a)-[:HAS_MULTIMEDIA]->(m:Multimedia) WITH a, collect({{link: m.link, description: m.description, type: m.type}}) AS multimedia RETURN a.fullName AS titulo, a.text AS contexto, {{imagenes: [item IN multimedia WHERE item.type = 'image' | {{link: item.link, description: item.description}}], videos: [item IN multimedia WHERE item.type = 'video' | {{link: item.link, description: item.description}}], audios: [item IN multimedia WHERE item.type = 'audio' | {{link: item.link, description: item.description}}], documentos: [item IN multimedia WHERE item.type = 'application' | {{link: item.link, description: item.description}}]}} AS multimedia"
    },
    {
        "question": "¿Quiene es la esposa de John Doe?",
        "query": "CALL db.index.fulltext.queryNodes('fullTextAuthorNames', 'John Doe') YIELD node AS a OPTIONAL MATCH (a)-[:HAS_MULTIMEDIA]->(m:Multimedia) WITH a, collect({{link: m.link, description: m.description, type: m.type}}) AS multimedia RETURN a.fullName AS titulo, a.text AS contexto, {{imagenes: [item IN multimedia WHERE item.type = 'image' | {{link: item.link, description: item.description}}], videos: [item IN multimedia WHERE item.type = 'video' | {{link: item.link, description: item.description}}], audios: [item IN multimedia WHERE item.type = 'audio' | {{link: item.link, description: item.description}}], documentos: [item IN multimedia WHERE item.type = 'application' | {{link: item.link, description: item.description}}]}} AS multimedia"
    },

    # Preguntas Descriptivas Sobre Obras
    {
        "question": "¿Cuál es la descripcion de la obra The Machine's Awakening?",
        "query": '''CALL db.index.fulltext.queryNodes('fullTextWorkTitles', "The Machine's Awakening") YIELD node AS w OPTIONAL MATCH (w)-[:HAS_MULTIMEDIA]->(m:Multimedia) WITH w, collect({{link: m.link, description: m.description, type: m.type}}) AS multimedia RETURN w.title AS titulo, w.text AS contexto, {{imagenes: [item IN multimedia WHERE item.type = 'image' | {{link: item.link, description: item.description}}], videos: [item IN multimedia WHERE item.type = 'video' | {{link: item.link, description: item.description}}], audios: [item IN multimedia WHERE item.type = 'audio' | {{link: item.link, description: item.description}}], documentos: [item IN multimedia WHERE item.type = 'application' | {{link: item.link, description: item.description}}]}} AS multimedia LIMIT 1'''
    },
    {
        "question": "¿Cuál es el género de The Machine's Awakening?",
        "query": '''CALL db.index.fulltext.queryNodes('fullTextWorkTitles', "The Machine's Awakening") YIELD node AS w OPTIONAL MATCH (w)-[:HAS_MULTIMEDIA]->(m:Multimedia) WITH w, collect({{link: m.link, description: m.description, type: m.type}}) AS multimedia RETURN w.title AS titulo, w.text AS contexto, {{imagenes: [item IN multimedia WHERE item.type = 'image' | {{link: item.link, description: item.description}}], videos: [item IN multimedia WHERE item.type = 'video' | {{link: item.link, description: item.description}}], audios: [item IN multimedia WHERE item.type = 'audio' | {{link: item.link, description: item.description}}], documentos: [item IN multimedia WHERE item.type = 'application' | {{link: item.link, description: item.description}}]}} AS multimedia LIMIT 1'''
    },
    {
        "question": "¿Cuál es el idioma original de The Machine's Awakening?",
        "query": '''CALL db.index.fulltext.queryNodes('fullTextWorkTitles', "The Machine's Awakening") YIELD node AS w OPTIONAL MATCH (w)-[:HAS_MULTIMEDIA]->(m:Multimedia) WITH w, collect({{link: m.link, description: m.description, type: m.type}}) AS multimedia RETURN w.title AS titulo, w.text AS contexto, {{imagenes: [item IN multimedia WHERE item.type = 'image' | {{link: item.link, description: item.description}}], videos: [item IN multimedia WHERE item.type = 'video' | {{link: item.link, description: item.description}}], audios: [item IN multimedia WHERE item.type = 'audio' | {{link: item.link, description: item.description}}], documentos: [item IN multimedia WHERE item.type = 'application' | {{link: item.link, description: item.description}}]}} AS multimedia LIMIT 1'''
    },
    {
        "question": "¿Cuál es la fecha de publicación de The Machine's Awakening?",
        "query": '''CALL db.index.fulltext.queryNodes('fullTextWorkTitles', "The Machine's Awakening") YIELD node AS w OPTIONAL MATCH (w)-[:HAS_MULTIMEDIA]->(m:Multimedia) WITH w, collect({{link: m.link, description: m.description, type: m.type}}) AS multimedia RETURN w.title AS titulo, w.text AS contexto, {{imagenes: [item IN multimedia WHERE item.type = 'image' | {{link: item.link, description: item.description}}], videos: [item IN multimedia WHERE item.type = 'video' | {{link: item.link, description: item.description}}], audios: [item IN multimedia WHERE item.type = 'audio' | {{link: item.link, description: item.description}}], documentos: [item IN multimedia WHERE item.type = 'application' | {{link: item.link, description: item.description}}]}} AS multimedia LIMIT 1'''
    },

    # Preguntas Descriptivas sobre Criticas
    {
    "question": "¿Cuál es la autora de la crítica Literary Analysis of 'Great Short Stories'?",
    "query": '''CALL db.index.fulltext.queryNodes('fullTextCriticismTitles', "Literary Analysis of 'Great Short Stories'") YIELD node AS c OPTIONAL MATCH (c)-[:HAS_MULTIMEDIA]->(m:Multimedia) WITH c, collect({{link: m.link, description: m.description, type: m.type}}) AS multimedia RETURN c.text AS contexto, {{imagenes: [item IN multimedia WHERE item.type = 'image' | {{link: item.link, description: item.description}}], videos: [item IN multimedia WHERE item.type = 'video' | {{link: item.link, description: item.description}}], audios: [item IN multimedia WHERE item.type = 'audio' | {{link: item.link, description: item.description}}], documentos: [item IN multimedia WHERE item.type = 'application' | {{link: item.link, description: item.description}}]}} AS multimedia LIMIT 1'''
    },
    {
        "question": "¿Cuál es la referencia bibliográfica de la crítica Literary Analysis of 'Great Short Stories'?",
        "query": '''CALL db.index.fulltext.queryNodes('fullTextCriticismTitles', "Literary Analysis of 'Great Short Stories'") YIELD node AS c OPTIONAL MATCH (c)-[:HAS_MULTIMEDIA]->(m:Multimedia) WITH c, collect({{link: m.link, description: m.description, type: m.type}}) AS multimedia RETURN c.bibliographicReferene AS referenciaBibliografica, {{imagenes: [item IN multimedia WHERE item.type = 'image' | {{link: item.link, description: item.description}}], videos: [item IN multimedia WHERE item.type = 'video' | {{link: item.link, description: item.description}}], audios: [item IN multimedia WHERE item.type = 'audio' | {{link: item.link, description: item.description}}], documentos: [item IN multimedia WHERE item.type = 'application' | {{link: item.link, description: item.description}}]}} AS multimedia LIMIT 1'''
    },
    {
        "question": "¿Cuál es la descripción de la crítica Literary Analysis of 'Great Short Stories'?",
        "query": '''CALL db.index.fulltext.queryNodes('fullTextCriticismTitles', "Literary Analysis of 'Great Short Stories'") YIELD node AS c OPTIONAL MATCH (c)-[:HAS_MULTIMEDIA]->(m:Multimedia) WITH c, collect({{link: m.link, description: m.description, type: m.type}}) AS multimedia RETURN c.text AS contexto, {{imagenes: [item IN multimedia WHERE item.type = 'image' | {{link: item.link, description: item.description}}], videos: [item IN multimedia WHERE item.type = 'video' | {{link: item.link, description: item.description}}], audios: [item IN multimedia WHERE item.type = 'audio' | {{link: item.link, description: item.description}}], documentos: [item IN multimedia WHERE item.type = 'application' | {{link: item.link, description: item.description}}]}} AS multimedia LIMIT 1'''
    },
    {
        "question": "¿Cuál es el enlace de la crítica Literary Analysis of 'Great Short Stories'?",
        "query": '''CALL db.index.fulltext.queryNodes('fullTextCriticismTitles', "Literary Analysis of 'Great Short Stories'") YIELD node AS c OPTIONAL MATCH (c)-[:HAS_MULTIMEDIA]->(m:Multimedia) WITH c, collect({{link: m.link, description: m.description, type: m.type}}) AS multimedia RETURN c.link AS enlace, {{imagenes: [item IN multimedia WHERE item.type = 'image' | {{link: item.link, description: item.description}}], videos: [item IN multimedia WHERE item.type = 'video' | {{link: item.link, description: item.description}}], audios: [item IN multimedia WHERE item.type = 'audio' | {{link: item.link, description: item.description}}], documentos: [item IN multimedia WHERE item.type = 'application' | {{link: item.link, description: item.description}}]}} AS multimedia LIMIT 1'''
    },
    {
        "question": "¿Cuándo fue publicada la crítica Literary Analysis of 'Great Short Stories'?",
        "query": '''CALL db.index.fulltext.queryNodes('fullTextCriticismTitles', "Literary Analysis of 'Great Short Stories'") YIELD node AS c OPTIONAL MATCH (c)-[:HAS_MULTIMEDIA]->(m:Multimedia) WITH c, collect({{link: m.link, description: m.description, type: m.type}}) AS multimedia RETURN c.text AS contexto, {{imagenes: [item IN multimedia WHERE item.type = 'image' | {{link: item.link, description: item.description}}], videos: [item IN multimedia WHERE item.type = 'video' | {{link: item.link, description: item.description}}], audios: [item IN multimedia WHERE item.type = 'audio' | {{link: item.link, description: item.description}}], documentos: [item IN multimedia WHERE item.type = 'application' | {{link: item.link, description: item.description}}]}} AS multimedia LIMIT 1'''
    },
    {
        "question": "¿Cuál es el tipo de la crítica Literary Analysis of 'Great Short Stories'?",
        "query": '''CALL db.index.fulltext.queryNodes('fullTextCriticismTitles', "Literary Analysis of 'Great Short Stories'") YIELD node AS c OPTIONAL MATCH (c)-[:HAS_MULTIMEDIA]->(m:Multimedia) WITH c, collect({{link: m.link, description: m.description, type: m.type}}) AS multimedia RETURN c.text AS contexto, {{imagenes: [item IN multimedia WHERE item.type = 'image' | {{link: item.link, description: item.description}}], videos: [item IN multimedia WHERE item.type = 'video' | {{link: item.link, description: item.description}}], audios: [item IN multimedia WHERE item.type = 'audio' | {{link: item.link, description: item.description}}], documentos: [item IN multimedia WHERE item.type = 'application' | {{link: item.link, description: item.description}}]}} AS multimedia LIMIT 1'''
    },

    # Preguntas Descriptivas sobre Antologías
    {
    "question": "¿Quién es el autor de la antología Great Short Stories of the World?",
    "query": '''CALL db.index.fulltext.queryNodes('fullTextAnthologyTitles', 'Great Short Stories of the World') YIELD node AS a OPTIONAL MATCH (a)-[:HAS_MULTIMEDIA]->(m:Multimedia) WITH a, collect({{link: m.link, description: m.description, type: m.type}}) AS multimedia RETURN a.title AS titulo, a.text AS contexto, {{imagenes: [item IN multimedia WHERE item.type = 'image' | {{link: item.link, description: item.description}}], videos: [item IN multimedia WHERE item.type = 'video' | {{link: item.link, description: item.description}}], audios: [item IN multimedia WHERE item.type = 'audio' | {{link: item.link, description: item.description}}], documentos: [item IN multimedia WHERE item.type = 'application' | {{link: item.link, description: item.description}}]}} AS multimedia'''
    },
    {
        "question": "¿Cuál es la descripción de la antología Great Short Stories of the World?",
        "query": '''CALL db.index.fulltext.queryNodes('fullTextAnthologyTitles', 'Great Short Stories of the World') YIELD node AS a OPTIONAL MATCH (a)-[:HAS_MULTIMEDIA]->(m:Multimedia) WITH a, collect({{link: m.link, description: m.description, type: m.type}}) AS multimedia RETURN a.title AS titulo, a.text AS contexto, {{imagenes: [item IN multimedia WHERE item.type = 'image' | {{link: item.link, description: item.description}}], videos: [item IN multimedia WHERE item.type = 'video' | {{link: item.link, description: item.description}}], audios: [item IN multimedia WHERE item.type = 'audio' | {{link: item.link, description: item.description}}], documentos: [item IN multimedia WHERE item.type = 'application' | {{link: item.link, description: item.description}}]}} AS multimedia'''
    },
    {
        "question": "¿Cuál es el género de la antología Great Short Stories of the World?",
        "query": '''CALL db.index.fulltext.queryNodes('fullTextAnthologyTitles', 'Great Short Stories of the World') YIELD node AS a OPTIONAL MATCH (a)-[:HAS_MULTIMEDIA]->(m:Multimedia) WITH a, collect({{link: m.link, description: m.description, type: m.type}}) AS multimedia RETURN a.title AS titulo, a.text AS contexto, {{imagenes: [item IN multimedia WHERE item.type = 'image' | {{link: item.link, description: item.description}}], videos: [item IN multimedia WHERE item.type = 'video' | {{link: item.link, description: item.description}}], audios: [item IN multimedia WHERE item.type = 'audio' | {{link: item.link, description: item.description}}], documentos: [item IN multimedia WHERE item.type = 'application' | {{link: item.link, description: item.description}}]}} AS multimedia'''
    },
    {
        "question": "¿Cuál es el idioma original de la antología Great Short Stories of the World?",
        "query": '''CALL db.index.fulltext.queryNodes('fullTextAnthologyTitles', 'Great Short Stories of the World') YIELD node AS a OPTIONAL MATCH (a)-[:HAS_MULTIMEDIA]->(m:Multimedia) WITH a, collect({{link: m.link, description: m.description, type: m.type}}) AS multimedia RETURN a.title AS titulo, a.text AS contexto, {{imagenes: [item IN multimedia WHERE item.type = 'image' | {{link: item.link, description: item.description}}], videos: [item IN multimedia WHERE item.type = 'video' | {{link: item.link, description: item.description}}], audios: [item IN multimedia WHERE item.type = 'audio' | {{link: item.link, description: item.description}}], documentos: [item IN multimedia WHERE item.type = 'application' | {{link: item.link, description: item.description}}]}} AS multimedia'''
    },
    {
        "question": "¿Cuándo se publicó la antología Great Short Stories of the World?",
        "query": '''CALL db.index.fulltext.queryNodes('fullTextAnthologyTitles', 'Great Short Stories of the World') YIELD node AS a OPTIONAL MATCH (a)-[:HAS_MULTIMEDIA]->(m:Multimedia) WITH a, collect({{link: m.link, description: m.description, type: m.type}}) AS multimedia RETURN a.title AS titulo, a.text AS contexto, {{imagenes: [item IN multimedia WHERE item.type = 'image' | {{link: item.link, description: item.description}}], videos: [item IN multimedia WHERE item.type = 'video' | {{link: item.link, description: item.description}}], audios: [item IN multimedia WHERE item.type = 'audio' | {{link: item.link, description: item.description}}], documentos: [item IN multimedia WHERE item.type = 'application' | {{link: item.link, description: item.description}}]}} AS multimedia'''
    },
    {
        "question": "¿Cuál es el contenido de la antología Great Short Stories of the World?",
        "query": '''CALL db.index.fulltext.queryNodes('fullTextAnthologyTitles', 'Great Short Stories of the World') YIELD node AS a OPTIONAL MATCH (a)-[:HAS_MULTIMEDIA]->(m:Multimedia) WITH a, collect({{link: m.link, description: m.description, type: m.type}}) AS multimedia RETURN a.title AS titulo, a.text AS contexto, {{imagenes: [item IN multimedia WHERE item.type = 'image' | {{link: item.link, description: item.description}}], videos: [item IN multimedia WHERE item.type = 'video' | {{link: item.link, description: item.description}}], audios: [item IN multimedia WHERE item.type = 'audio' | {{link: item.link, description: item.description}}], documentos: [item IN multimedia WHERE item.type = 'application' | {{link: item.link, description: item.description}}]}} AS multimedia'''
    },

    # Preguntas Descriptivas sobre Revistas
    {
    "question": "¿Cuál es la descripción de la revista The Global Analys?",
    "query": '''CALL db.index.fulltext.queryNodes('fullTextMagazineTitles', 'The Global Analys') YIELD node AS m OPTIONAL MATCH (m)-[:HAS_MULTIMEDIA]->(mult:Multimedia) WITH m, collect({{link: mult.link, description: mult.description, type: mult.type}}) AS multimedia RETURN m.magazineTitle AS titulo, m.text AS contexto, {{imagenes: [item IN multimedia WHERE item.type = 'image' | {{link: item.link, description: item.description}}], videos: [item IN multimedia WHERE item.type = 'video' | {{link: item.link, description: item.description}}], audios: [item IN multimedia WHERE item.type = 'audio' | {{link: item.link, description: item.description}}], documentos: [item IN multimedia WHERE item.type = 'application' | {{link: item.link, description: item.description}}]}} AS multimedia'''
    },
    {
        "question": "¿Cuál es el título de la revista The Global Analys?",
        "query": '''CALL db.index.fulltext.queryNodes('fullTextMagazineTitles', 'The Global Analys') YIELD node AS m OPTIONAL MATCH (m)-[:HAS_MULTIMEDIA]->(mult:Multimedia) WITH m, collect({{link: mult.link, description: mult.description, type: mult.type}}) AS multimedia RETURN m.magazineTitle AS titulo, {{imagenes: [item IN multimedia WHERE item.type = 'image' | {{link: item.link, description: item.description}}], videos: [item IN multimedia WHERE item.type = 'video' | {{link: item.link, description: item.description}}], audios: [item IN multimedia WHERE item.type = 'audio' | {{link: item.link, description: item.description}}], documentos: [item IN multimedia WHERE item.type = 'application' | {{link: item.link, description: item.description}}]}} AS multimedia'''
    },
    {
        "question": "¿Cuál es el idioma original de la revista The Global Analys?",
        "query": '''CALL db.index.fulltext.queryNodes('fullTextMagazineTitles', 'The Global Analys') YIELD node AS m OPTIONAL MATCH (m)-[:HAS_MULTIMEDIA]->(mult:Multimedia) WITH m, collect({{link: mult.link, description: mult.description, type: mult.type}}) AS multimedia RETURN m.magazineTitle AS titulo, m.text AS contexto, {{imagenes: [item IN multimedia WHERE item.type = 'image' | {{link: item.link, description: item.description}}], videos: [item IN multimedia WHERE item.type = 'video' | {{link: item.link, description: item.description}}], audios: [item IN multimedia WHERE item.type = 'audio' | {{link: item.link, description: item.description}}], documentos: [item IN multimedia WHERE item.type = 'application' | {{link: item.link, description: item.description}}]}} AS multimedia'''
    },
    {
        "question": "¿Cuáles son las secciones principales de la revista The Global Analys?",
        "query": '''CALL db.index.fulltext.queryNodes('fullTextMagazineTitles', 'The Global Analys') YIELD node AS m OPTIONAL MATCH (m)-[:HAS_MULTIMEDIA]->(mult:Multimedia) WITH m, collect({{link: mult.link, description: mult.description, type: mult.type}}) AS multimedia RETURN m.magazineTitle AS titulo, m.sections AS secciones, {{imagenes: [item IN multimedia WHERE item.type = 'image' | {{link: item.link, description: item.description}}], videos: [item IN multimedia WHERE item.type = 'video' | {{link: item.link, description: item.description}}], audios: [item IN multimedia WHERE item.type = 'audio' | {{link: item.link, description: item.description}}], documentos: [item IN multimedia WHERE item.type = 'application' | {{link: item.link, description: item.description}}]}} AS multimedia'''
    },
    {
        "question": "¿Cuál es el contenido de la revista The Global Analys?",
        "query": '''CALL db.index.fulltext.queryNodes('fullTextMagazineTitles', 'The Global Analys') YIELD node AS m OPTIONAL MATCH (m)-[:HAS_MULTIMEDIA]->(mult:Multimedia) WITH m, collect({{link: mult.link, description: mult.description, type: mult.type}}) AS multimedia RETURN m.magazineTitle AS titulo, m.text AS contenido, {{imagenes: [item IN multimedia WHERE item.type = 'image' | {{link: item.link, description: item.description}}], videos: [item IN multimedia WHERE item.type = 'video' | {{link: item.link, description: item.description}}], audios: [item IN multimedia WHERE item.type = 'audio' | {{link: item.link, description: item.description}}], documentos: [item IN multimedia WHERE item.type = 'application' | {{link: item.link, description: item.description}}]}} AS multimedia'''
    },

    # Preguntas Descriptivas sobre Agrupaciones:
    {
    "question": "¿Cuál es la fecha de finalización del Writers Collective?",
    "query": '''CALL db.index.fulltext.queryNodes('fullTextGroupingNames', 'Writers Collective') YIELD node AS g OPTIONAL MATCH (g)-[:HAS_MULTIMEDIA]->(mult:Multimedia) WITH g, collect({{link: mult.link, description: mult.description, type: mult.type}}) AS multimedia RETURN g.name AS titulo, g.endDate AS fechaFinalizacion, {{imagenes: [item IN multimedia WHERE item.type = 'image' | {{link: item.link, description: item.description}}], videos: [item IN multimedia WHERE item.type = 'video' | {{link: item.link, description: item.description}}], audios: [item IN multimedia WHERE item.type = 'audio' | {{link: item.link, description: item.description}}], documentos: [item IN multimedia WHERE item.type = 'application' | {{link: item.link, description: item.description}}]}} AS multimedia'''
    },
    {
        "question": "¿Cuáles son las características generales del Writers Collective?",
        "query": '''CALL db.index.fulltext.queryNodes('fullTextGroupingNames', 'Writers Collective') YIELD node AS g OPTIONAL MATCH (g)-[:HAS_MULTIMEDIA]->(mult:Multimedia) WITH g, collect({{link: mult.link, description: mult.description, type: mult.type}}) AS multimedia RETURN g.name AS titulo, g.generalCharacteristics AS caracteristicasGenerales, {{imagenes: [item IN multimedia WHERE item.type = 'image' | {{link: item.link, description: item.description}}], videos: [item IN multimedia WHERE item.type = 'video' | {{link: item.link, description: item.description}}], audios: [item IN multimedia WHERE item.type = 'audio' | {{link: item.link, description: item.description}}], documentos: [item IN multimedia WHERE item.type = 'application' | {{link: item.link, description: item.description}}]}} AS multimedia'''
    },
    {
        "question": "¿Qué actividades realiza el Writers Collective?",
        "query": '''CALL db.index.fulltext.queryNodes('fullTextGroupingNames', 'Writers Collective') YIELD node AS g OPTIONAL MATCH (g)-[:HAS_MULTIMEDIA]->(mult:Multimedia) WITH g, collect({{link: mult.link, description: mult.description, type: mult.type}}) AS multimedia RETURN g.name AS titulo, g.groupActivities AS actividadesDelGrupo, {{imagenes: [item IN multimedia WHERE item.type = 'image' | {{link: item.link, description: item.description}}], videos: [item IN multimedia WHERE item.type = 'video' | {{link: item.link, description: item.description}}], audios: [item IN multimedia WHERE item.type = 'audio' | {{link: item.link, description: item.description}}], documentos: [item IN multimedia WHERE item.type = 'application' | {{link: item.link, description: item.description}}]}} AS multimedia'''
    },
    {
        "question": "¿Cuándo se estableció el Writers Collective?",
        "query": '''CALL db.index.fulltext.queryNodes('fullTextGroupingNames', 'Writers Collective') YIELD node AS g OPTIONAL MATCH (g)-[:HAS_MULTIMEDIA]->(mult:Multimedia) WITH g, collect({{link: mult.link, description: mult.description, type: mult.type}}) AS multimedia RETURN g.name AS titulo, g.startDate AS fechaEstablecimiento, {{imagenes: [item IN multimedia WHERE item.type = 'image' | {{link: item.link, description: item.description}}], videos: [item IN multimedia WHERE item.type = 'video' | {{link: item.link, description: item.description}}], audios: [item IN multimedia WHERE item.type = 'audio' | {{link: item.link, description: item.description}}], documentos: [item IN multimedia WHERE item.type = 'application' | {{link: item.link, description: item.description}}]}} AS multimedia'''
    },
    {
        "question": "¿Cuál es el contenido del Writers Collective?",
        "query": '''CALL db.index.fulltext.queryNodes('fullTextGroupingNames', 'Writers Collective') YIELD node AS g OPTIONAL MATCH (g)-[:HAS_MULTIMEDIA]->(mult:Multimedia) WITH g, collect({{link: mult.link, description: mult.description, type: mult.type}}) AS multimedia RETURN g.name AS titulo, g.text AS contenido, {{imagenes: [item IN multimedia WHERE item.type = 'image' | {{link: item.link, description: item.description}}], videos: [item IN multimedia WHERE item.type = 'video' | {{link: item.link, description: item.description}}], audios: [item IN multimedia WHERE item.type = 'audio' | {{link: item.link, description: item.description}}], documentos: [item IN multimedia WHERE item.type = 'application' | {{link: item.link, description: item.description}}]}} AS multimedia'''
    },

    # Preguntas Relación (Author)-[:HAS_MULTIMEDIA]->(Multimedia)
    {
        "question": "¿Cuál es la multimedia asociada con el autor John Doe?",
        "query": '''CALL db.index.fulltext.queryNodes('fullTextAuthorNames', 'John Doe') YIELD node AS a OPTIONAL MATCH (a)-[:HAS_MULTIMEDIA]->(m:Multimedia) WITH a, collect({{link: m.link, description: m.description, type: m.type}}) AS multimedia RETURN a.fullName AS titulo, {{imagenes: [item IN multimedia WHERE item.type = 'image' | {{link: item.link, description: item.description}}], videos: [item IN multimedia WHERE item.type = 'video' | {{link: item.link, description: item.description}}], audios: [item IN multimedia WHERE item.type = 'audio' | {{link: item.link, description: item.description}}], documentos: [item IN multimedia WHERE item.type = 'application' | {{link: item.link, description: item.description}}]}} AS multimedia'''
    },
    {
        "question": "¿Cuáles son las imágenes asociadas con el autor John Doe?",
        "query": '''CALL db.index.fulltext.queryNodes('fullTextAuthorNames', 'John Doe') YIELD node AS a OPTIONAL MATCH (a)-[:HAS_MULTIMEDIA]->(m:Multimedia) WHERE m.type = 'image' RETURN a.fullName AS titulo, collect({{link: m.link, description: m.description}}) AS imagenes'''
    },
    {
        "question": "¿Cuáles son los videos asociados con el autor John Doe?",
        "query": '''CALL db.index.fulltext.queryNodes('fullTextAuthorNames', 'John Doe') YIELD node AS a OPTIONAL MATCH (a)-[:HAS_MULTIMEDIA]->(m:Multimedia) WHERE m.type = 'video' RETURN a.fullName AS titulo, collect({{link: m.link, description: m.description}}) AS videos'''
    },
    {
        "question": "¿Cuáles son los audios asociados con el autor John Doe?",
        "query": '''CALL db.index.fulltext.queryNodes('fullTextAuthorNames', 'John Doe') YIELD node AS a OPTIONAL MATCH (a)-[:HAS_MULTIMEDIA]->(m:Multimedia) WHERE m.type = 'audio' RETURN a.fullName AS titulo, collect({{link: m.link, description: m.description}}) AS audios'''
    },
    {
        "question": "¿Cuáles son los documentos asociados con el autor John Doe?",
        "query": '''CALL db.index.fulltext.queryNodes('fullTextAuthorNames', 'John Doe') YIELD node AS a OPTIONAL MATCH (a)-[:HAS_MULTIMEDIA]->(m:Multimedia) WHERE m.type = 'application' RETURN a.fullName AS titulo, collect({{link: m.link, description: m.description}}) AS documentos'''
    },

    # Preguntas Relación (Author)-[:CREATED]->(Work)
    {
        "question": "¿Cuáles son los géneros de las obras creadas por John Doe?",
        "query": "CALL db.index.fulltext.queryNodes('fullTextAuthorNames', 'John Doe') YIELD node AS a MATCH (a)-[:CREATED]->(w:Work) RETURN a.fullName AS titulo, collect(w.genre) AS generosObras"
    },
    {
        "question": "¿Qué obras ha creado John Doe?",
        "query": "CALL db.index.fulltext.queryNodes('fullTextAuthorNames', 'John Doe') YIELD node AS a MATCH (a)-[:CREATED]->(w:Work) OPTIONAL MATCH (w)-[:HAS_MULTIMEDIA]->(m:Multimedia) WITH a.fullName AS tituloAutor, w.text AS textoObra, collect({{link: m.link, description: m.description, type: m.type}}) AS multimedia WITH tituloAutor, collect({{texto: textoObra, multimedia: {{imagenes: [item IN multimedia WHERE item.type = 'image' | {{link: item.link, description: item.description}}], videos: [item IN multimedia WHERE item.type = 'video' | {{link: item.link, description: item.description}}], audios: [item IN multimedia WHERE item.type = 'audio' | {{link: item.link, description: item.description}}], documentos: [item IN multimedia WHERE item.type = 'application' | {{link: item.link, description: item.description}}]}}}}) AS obras RETURN {{titulo: tituloAutor, obras: obras}} AS result"
    },
    {
        "question": "¿Qué obras han sido escritas por mujeres?",
        "query": "MATCH (a)-[:CREATED]->(w:Work) WHERE a.gender = 'Femenino' OPTIONAL MATCH (w)-[:HAS_MULTIMEDIA]->(m:Multimedia) WITH a.fullName AS tituloAutor, w.title AS tituloObra, w.text AS textoObra, collect({{link: m.link, description: m.description, type: m.type}}) AS multimedia RETURN {{titulo: tituloObra, autor: tituloAutor, texto: textoObra, multimedia: {{imagenes: [item IN multimedia WHERE item.type = 'image' | {{link: item.link, description: item.description}}], videos: [item IN multimedia WHERE item.type = 'video' | {{link: item.link, description: item.description}}], audios: [item IN multimedia WHERE item.type = 'audio' | {{link: item.link, description: item.description}}], documentos: [item IN multimedia WHERE item.type = 'application' | {{link: item.link, description: item.description}}]}}}} AS result"
    },
    {
        "question": "¿Qué obras han sido escritas por hombres?",
        "query": "MATCH (a)-[:CREATED]->(w:Work) WHERE a.gender = 'Masculino' OPTIONAL MATCH (w)-[:HAS_MULTIMEDIA]->(m:Multimedia) WITH a.fullName AS tituloAutor, w.title AS tituloObra, w.text AS textoObra, collect({{link: m.link, description: m.description, type: m.type}}) AS multimedia RETURN {{titulo: tituloObra, autor: tituloAutor, texto: textoObra, multimedia: {{imagenes: [item IN multimedia WHERE item.type = 'image' | {{link: item.link, description: item.description}}], videos: [item IN multimedia WHERE item.type = 'video' | {{link: item.link, description: item.description}}], audios: [item IN multimedia WHERE item.type = 'audio' | {{link: item.link, description: item.description}}], documentos: [item IN multimedia WHERE item.type = 'application' | {{link: item.link, description: item.description}}]}}}} AS result"
    },


    # Preguntas Relación (Criticism)-[:CRITICIZES_ABOUT]->(Author)
    {
        "question": "¿Cuáles son las críticas asociadas con el autor John Doe?",
        "query": "CALL db.index.fulltext.queryNodes('fullTextAuthorNames', 'John Doe') YIELD node AS a MATCH (c:Criticism)-[:CRITICIZES_ABOUT]->(a) OPTIONAL MATCH (c)-[:HAS_MULTIMEDIA]->(m:Multimedia) WITH a.fullName AS tituloAutor, c.text AS textoCritica, collect({{link: m.link, description: m.description, type: m.type}}) AS multimedia WITH tituloAutor, collect({{texto: textoCritica, multimedia: {{imagenes: [item IN multimedia WHERE item.type = 'image' | {{link: item.link, description: item.description}}], videos: [item IN multimedia WHERE item.type = 'video' | {{link: item.link, description: item.description}}], audios: [item IN multimedia WHERE item.type = 'audio' | {{link: item.link, description: item.description}}], documentos: [item IN multimedia WHERE item.type = 'application' | {{link: item.link, description: item.description}}]}}}}) AS criticas RETURN {{titulo: tituloAutor, criticas: criticas}} AS result"
    },

    {
        "question": "¿Qué obras fueron publicadas en New York?",
        "query": "CALL db.index.fulltext.queryNodes('fullTextCity', 'New York') YIELD node AS pub MATCH (w:Work)-[:PUBLISHED_IN]->(p:Publication) WHERE p = pub OPTIONAL MATCH (w)-[:HAS_MULTIMEDIA]->(m:Multimedia) WITH w.title AS tituloObra, w.text AS textoObra, w.publicationDate AS fechaPublicacion, collect({{link: m.link, description: m.description, type: m.type}}) AS multimedia WITH collect({{titulo: tituloObra, texto: textoObra, fechaPublicacion: fechaPublicacion, multimedia: {{imagenes: [item IN multimedia WHERE item.type = 'image' | {{link: item.link, description: item.description}}], videos: [item IN multimedia WHERE item.type = 'video' | {{link: item.link, description: item.description}}], audios: [item IN multimedia WHERE item.type = 'audio' | {{link: item.link, description: item.description}}], documentos: [item IN multimedia WHERE item.type = 'application' | {{link: item.link, description: item.description}}]}}}}) AS obras RETURN {{obras: obras}} AS result"
    },

    # Preguntas Relación (Author)-[:CRITICIZES_ABOUT]->(Work)-[:PUBLISHED_IN]->(Publication)
    {
        "question": "¿Cuáles son las obras de John Doe publicadas en Nueva York?",
        "query": "CALL db.index.fulltext.queryNodes('fullTextAuthorNames', 'John Doe') YIELD node AS a OPTIONAL MATCH (a)-[:CREATED]->(w:Work)-[:PUBLISHED_IN]->(p:Publication) CALL db.index.fulltext.queryNodes('fullTextCity', 'Nueva York') YIELD node AS pub WHERE pub = p OPTIONAL MATCH (w)-[:HAS_MULTIMEDIA]->(m:Multimedia) WITH a.fullName AS tituloAutor, w.text AS textoObra, collect({{link: m.link, description: m.description, type: m.type}}) AS multimedia WITH tituloAutor, collect({{texto: textoObra, multimedia: {{imagenes: [item IN multimedia WHERE item.type = 'image' | {{link: item.link, description: item.description}}], videos: [item IN multimedia WHERE item.type = 'video' | {{link: item.link, description: item.description}}], audios: [item IN multimedia WHERE item.type = 'audio' | {{link: item.link, description: item.description}}], documentos: [item IN multimedia WHERE item.type = 'application' | {{link: item.link, description: item.description}}]}}}}) AS obras RETURN {{titulo: tituloAutor, obras: obras}} AS result"
    },
    {
        "question": "¿Cuáles son las obras de John Doe impresas por Harper & Sisters?",
        "query": "CALL db.index.fulltext.queryNodes('fullTextAuthorNames', 'John Doe') YIELD node AS a OPTIONAL MATCH (a)-[:CREATED]->(w:Work)-[:PUBLISHED_IN]->(p:Publication) CALL db.index.fulltext.queryNodes('fullTextPrintingHouse', 'Harper & Sisters') YIELD node AS printHouse WHERE printHouse = p OPTIONAL MATCH (w)-[:HAS_MULTIMEDIA]->(m:Multimedia) WHERE m.type = 'image' WITH a.fullName AS tituloAutor, w.text AS textoObra, collect(DISTINCT m.link) AS multimediaLinks WITH tituloAutor, collect({{texto: textoObra, multimedia: multimediaLinks}}) AS obras RETURN {{titulo: tituloAutor, obras: obras}} AS result"
    },
    {
        "question": "¿Cuáles son las obras de John Doe publicadas por Penguin Books?",
        "query": "CALL db.index.fulltext.queryNodes('fullTextAuthorNames', 'John Doe') YIELD node AS a OPTIONAL MATCH (a)-[:CREATED]->(w:Work)-[:PUBLISHED_IN]->(p:Publication) CALL db.index.fulltext.queryNodes('fullTextPublisher', 'Penguin Books') YIELD node AS publisher WHERE publisher = p WITH p, apoc.text.levenshteinSimilarity(toLower(p.publisher), 'Penguin Books') AS similarityScore, a, w WHERE similarityScore > 0.5 OPTIONAL MATCH (w)-[:HAS_MULTIMEDIA]->(m:Multimedia) WITH a.fullName AS tituloAutor, w.text AS textoObra, collect({{link: m.link, description: m.description, type: m.type}}) AS multimedia WITH tituloAutor, collect({{texto: textoObra, multimedia: {{imagenes: [item IN multimedia WHERE item.type = 'image' | {{link: item.link, description: item.description}}], videos: [item IN multimedia WHERE item.type = 'video' | {{link: item.link, description: item.description}}], audios: [item IN multimedia WHERE item.type = 'audio' | {{link: item.link, description: item.description}}], documentos: [item IN multimedia WHERE item.type = 'application' | {{link: item.link, description: item.description}}]}}}}) AS obras RETURN {{titulo: tituloAutor, obras: obras}} AS result"
    },

    # Preguntas Comparaciones entre Obras
    {
        "question": "Hazme una comparación entre las obras The Machine's Awakening y The Future Beyond.",
        "query": '''CALL db.index.fulltext.queryNodes('fullTextWorkTitles', "The Machine's Awakening") YIELD node AS wA OPTIONAL MATCH (wA)-[:HAS_MULTIMEDIA]->(m1:Multimedia) WITH wA.text AS textoObraA, collect({{link: m1.link, description: m1.description, type: m1.type}}) AS multimediaA CALL db.index.fulltext.queryNodes('fullTextWorkTitles', 'The Future Beyond') YIELD node AS wB OPTIONAL MATCH (wB)-[:HAS_MULTIMEDIA]->(m2:Multimedia) WITH textoObraA, multimediaA, wB.text AS textoObraB, collect({{link: m2.link, description: m2.description, type: m2.type}}) AS multimediaB RETURN [{{texto: textoObraA, multimedia: {{imagenes: [item IN multimediaA WHERE item.type = 'image' | {{link: item.link, description: item.description}}], videos: [item IN multimediaA WHERE item.type = 'video' | {{link: item.link, description: item.description}}], audios: [item IN multimediaA WHERE item.type = 'audio' | {{link: item.link, description: item.description}}], documentos: [item IN multimediaA WHERE item.type = 'application' | {{link: item.link, description: item.description}}]}}}}, {{texto: textoObraB, multimedia: {{imagenes: [item IN multimediaB WHERE item.type = 'image' | {{link: item.link, description: item.description}}], videos: [item IN multimediaB WHERE item.type = 'video' | {{link: item.link, description: item.description}}], audios: [item IN multimediaB WHERE item.type = 'audio' | {{link: item.link, description: item.description}}], documentos: [item IN multimediaB WHERE item.type = 'application' | {{link: item.link, description: item.description}}]}}}}] AS comparacion LIMIT 1'''
    },
    
    # Pregunta Comparaciones entre Criticas de Obras
    # {
    #     "question": "Compara las críticas de The Machine's Awakening con las de The Future Beyond.",
    #     "query": ""
    # },

    # Preguntas de Obras Similares
    {
        "question": "Muestrame obras que traten sobre el futuro",
        "query": '''CALL genai.vector.encodeBatch(["futuro"], "OpenAI", {{token: 'sk-N6j1NARm-4DyU-yiO9359Rt6pcsULw5sneQbqTplMwT3BlbkFJeg3hBxCMxoG_F06emsOKe4v4DRuOw-OzwXD7RydZIA'}}) YIELD vector CALL db.index.vector.queryNodes("works_description", 5, vector) YIELD node AS work, score WHERE score > 0.9 OPTIONAL MATCH (work)-[:HAS_MULTIMEDIA]->(m:Multimedia) WITH work.title AS tituloObra, work.text AS textoObra, collect({{link: m.link, description: m.description, type: m.type}}) AS multimedia RETURN {{titulo: tituloObra, texto: textoObra, multimedia: {{imagenes: [item IN multimedia WHERE item.type = 'image' | {{link: item.link, description: item.description}}], videos: [item IN multimedia WHERE item.type = 'video' | {{link: item.link, description: item.description}}], audios: [item IN multimedia WHERE item.type = 'audio' | {{link: item.link, description: item.description}}], documentos: [item IN multimedia WHERE item.type = 'application' | {{link: item.link, description: item.description}}]}}}} AS result'''
    },
    {
        "question": "Muestrame las obras de John Doe que tratan sobre el inteligencia artificial",
        "query": '''CALL genai.vector.encodeBatch(["inteligencia artificial"], "OpenAI", {{token: 'sk-N6j1NARm-4DyU-yiO9359Rt6pcsULw5sneQbqTplMwT3BlbkFJeg3hBxCMxoG_F06emsOKe4v4DRuOw-OzwXD7RydZIA'}}) YIELD vector CALL db.index.vector.queryNodes("works_description", 5, vector) YIELD node AS work, score WHERE score > 0.9 CALL db.index.fulltext.queryNodes('fullTextAuthorNames', 'John Doe') YIELD node AS a MATCH (a)-[:CREATED]->(work) WHERE work = work OPTIONAL MATCH (work)-[:HAS_MULTIMEDIA]->(m:Multimedia) WITH a.fullName AS tituloAutor, work.title AS tituloObra, work.text AS textoObra, collect({{link: m.link, description: m.description, type: m.type}}) AS multimedia RETURN {{titulo: tituloObra, texto: textoObra, multimedia: {{imagenes: [item IN multimedia WHERE item.type = 'image' | {{link: item.link, description: item.description}}], videos: [item IN multimedia WHERE item.type = 'video' | {{link: item.link, description: item.description}}], audios: [item IN multimedia WHERE item.type = 'audio' | {{link: item.link, description: item.description}}], documentos: [item IN multimedia WHERE item.type = 'application' | {{link: item.link, description: item.description}}]}}}} AS result'''
    },
    {
        "question": "Recomiéndame obras sobre el río Orinoco",
        "query": '''CALL genai.vector.encodeBatch([\"río Orinoco\"], \"OpenAI\", {{token: 'sk-N6j1NARm-4DyU-yiO9359Rt6pcsULw5sneQbqTplMwT3BlbkFJeg3hBxCMxoG_F06emsOKe4v4DRuOw-OzwXD7RydZIA'}}) YIELD vector CALL db.index.vector.queryNodes(\"works_description\", 5, vector) YIELD node AS work, score WHERE score > 0.9 OPTIONAL MATCH (work)-[:HAS_MULTIMEDIA]->(m:Multimedia) WITH work.title AS tituloObra, work.text AS textoObra, collect({{link: m.link, description: m.description, type: m.type}}) AS multimedia RETURN {{titulo: tituloObra, texto: textoObra, multimedia: {{imagenes: [item IN multimedia WHERE item.type = 'image' | {{link: item.link, description: item.description}}], videos: [item IN multimedia WHERE item.type = 'video' | {{link: item.link, description: item.description}}], audios: [item IN multimedia WHERE item.type = 'audio' | {{link: item.link, description: item.description}}], documentos: [item IN multimedia WHERE item.type = 'application' | {{link: item.link, description: item.description}}]}}}} AS result'''
    },
    {
        "question": "Que cosas se han escrito sobre el río Orinoco",
        "query": '''CALL genai.vector.encodeBatch([\"río Orinoco\"], \"OpenAI\", {{token: 'sk-N6j1NARm-4DyU-yiO9359Rt6pcsULw5sneQbqTplMwT3BlbkFJeg3hBxCMxoG_F06emsOKe4v4DRuOw-OzwXD7RydZIA'}}) YIELD vector CALL db.index.vector.queryNodes(\"works_description\", 5, vector) YIELD node AS work, score WHERE score > 0.9 OPTIONAL MATCH (work)-[:HAS_MULTIMEDIA]->(m:Multimedia) WITH work.title AS tituloObra, work.text AS textoObra, collect({{link: m.link, description: m.description, type: m.type}}) AS multimedia RETURN {{titulo: tituloObra, texto: textoObra, multimedia: {{imagenes: [item IN multimedia WHERE item.type = 'image' | {{link: item.link, description: item.description}}], videos: [item IN multimedia WHERE item.type = 'video' | {{link: item.link, description: item.description}}], audios: [item IN multimedia WHERE item.type = 'audio' | {{link: item.link, description: item.description}}], documentos: [item IN multimedia WHERE item.type = 'application' | {{link: item.link, description: item.description}}]}}}} AS result'''
    },
    # Preguntas de Tiempo
    {
        "question": "Que obras se han impreso en Upata desde 1940-1990",
        "query": """CALL db.index.fulltext.queryNodes('fullTextCity', 'Upata') YIELD node AS pub MATCH (w:Work)-[:PUBLISHED_IN]->(p:Publication) WHERE p = pub WITH w, CASE WHEN w.publicationDate =~ '.*\\d{{4}}' THEN toInteger(head(apoc.coll.flatten(apoc.text.regexGroups(w.publicationDate, '(\\d{{4}})')))) ELSE null END AS year WHERE year >= 1940 AND year <= 1990 OPTIONAL MATCH (w)-[:HAS_MULTIMEDIA]->(m:Multimedia) WITH w.title AS tituloObra, w.text AS textoObra, w.publicationDate AS fechaPublicacion, year, collect({{link: m.link, description: m.description, type: m.type}}) AS multimedia RETURN {{titulo: tituloObra, texto: textoObra, fechaPublicacion: fechaPublicacion, multimedia: {{imagenes: [item IN multimedia WHERE item.type = 'image' | {{link: item.link, description: item.description}}], videos: [item IN multimedia WHERE item.type = 'video' | {{link: item.link, description: item.description}}], audios: [item IN multimedia WHERE item.type = 'audio' | {{link: item.link, description: item.description}}], documentos: [item IN multimedia WHERE item.type = 'application' | {{link: item.link, description: item.description}}]}}}} AS result ORDER BY year"""
    }   
]


