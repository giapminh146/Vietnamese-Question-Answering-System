from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import vqa_web.model as model

def lifespan(app: FastAPI):
    print("Start ...")
    model.load_model()
    yield
    print("Complete")

app = FastAPI(lifespan=lifespan)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (update this for production)
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

# Define a request body model
class SentenceRequest(BaseModel):
    question: str
    context: str

# Define a route for processing sentences
@app.post("/vqa/")
def process_sentences(request: SentenceRequest):
    answer = model.get_answer(request.context, request.question)
    return {"Answer": answer}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

