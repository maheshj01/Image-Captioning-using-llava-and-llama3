from fastapi import FastAPI, FastAPI, File, Form, UploadFile, HTTPException
from utils.llm_utils import generate_response, stream_parser, generate_image_desc
from utils.image_utils import get_image_bytes
from fastapi.responses import StreamingResponse
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

@app.post("/api/describe-image")
async def generate_image_description(model: str = Form(...), prompt: str = Form(...), image_file: UploadFile = File(...)):
    if(not image_file):
        raise HTTPException(status_code=400, detail="Image file is required.")
    if (not model) or (not prompt):
        raise HTTPException(status_code=400, detail="Model and prompt are required.")
    # Generate image description using the provided parameters
    stream =  await generate_image_desc(model=model,user_prompt=prompt, image_file =image_file)
    response = stream_parser(stream)
    return {"response": response}


@app.post("/api/generate")
async def generate(request_data: dict):
    model = request_data.get("model")
    prompt = request_data.get("prompt")

    if not model or not prompt:
        raise HTTPException(status_code=400, detail="Model and prompt are required.")

    stream = generate_response(model=model, prompt=prompt)
    response = stream_parser(stream)
    return {"response": ''.join(response)}