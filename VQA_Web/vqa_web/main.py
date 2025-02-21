from fastapi import FastAPI
from fastapi import Request
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
async def vqa(request: Request):
    data = await request.json()
    context = data.get("context", "")
    question = data.get("question", "")
    selected_model = data.get("model", "")  # Get the selected model from request
    
    # Pass the selected model to get_answer
    result = model.get_answer(context, question, selected_model)
    
    return {
        "Answer": result["answer"],
        "Model": result["model"]
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

