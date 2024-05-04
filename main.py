from fastapi import FastAPI, HTTPException
from utils.llm_utils import generate_response, stream_parser
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

# CORS middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow requests from any origin, you can customize it as needed
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],  # Allow the specified methods
    allow_headers=["*"],  # Allow all headers
)

@app.post("/api/generate")
async def generate(request_data: dict):
    model = request_data.get("model")
    prompt = request_data.get("prompt")

    if not model or not prompt:
        raise HTTPException(status_code=400, detail="Model and prompt are required.")

    stream = generate_response(model=model, prompt=prompt)
    response = stream_parser(stream)
    return {"response": ''.join(response)}