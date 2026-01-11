from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import spacy
import os

app = FastAPI()

# Esto permite que tu web de Lovable se conecte
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Cargamos el modelo (Render lo instalará según el requirements.txt)
nlp = spacy.load("es_core_news_md")

@app.get("/buscar")
def buscar(query: str):
    doc = nlp(query.lower())
    lemas = [t.lemma_ for t in doc if not t.is_stop]
    return {
        "palabras_clave": lemas,
        "sugerencia": "NVDA" if "chip" in lemas else "AAPL"
    }
