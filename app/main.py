from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from .generator import generate_content

app =FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class GenerateRequest(BaseModel):
    prompt: str
    content_type: str = "blog"

@app.post("/generate")
def generate(request: GenerateRequest):
    output = generate_content(request.prompt, request.content_type)
    return {"result": output}