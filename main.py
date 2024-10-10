from typing import Optional
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from graph import app as graph_app

app = FastAPI()

# Agregar middleware de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "https://letrascopio.vercel.app"],  # Permite solicitudes desde localhost:3000
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos HTTP
    allow_headers=["*"],  # Permite todos los headers
)

class QuestionRequest(BaseModel):
    question: str

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/ask") 
async def ask_question(request: QuestionRequest):
    try:
        # Invocar el grafo con la pregunta proporcionada
        graph_qa_result = graph_app.invoke({"question": request.question})

         # Extraer solo los campos query y result
        query = graph_qa_result['response'].get('query')
        result = graph_qa_result['response'].get('result')
        question_type = graph_qa_result['type']

        return {
            "query": query,
            "result": result,
            "type": question_type,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
