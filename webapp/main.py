from transformers import pipeline
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import HTMLResponse

generator = pipeline('text-generation', model='gpt2')

app = FastAPI()

class Text(BaseModel):
    text: str

@app.get("/")
def read_root():
    return HTMLResponse(content="<h1>self-documenting API to interact with a GPT2 model and generate text</h1>")

@app.post("/generate")
def generate_text(text: Text):
    results = generator(text.text, max_length=100, num_return_sequences=1)
    return results[0]