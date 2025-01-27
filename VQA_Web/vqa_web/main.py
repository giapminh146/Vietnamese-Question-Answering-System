from fastapi import FastAPI
from pydantic import BaseModel
from vqa_web import model

app = FastAPI()

# Define a request body model
class SentenceRequest(BaseModel):
    question: str
    context: str


# Define a route for processing sentences
@app.post("/vqa/")
def process_sentences(request: SentenceRequest):
    answer = model.get_answer(request.context, request.question)
    return {"Answer": answer}
