from fastapi import APIRouter, Request
from pydantic import BaseModel
from gpt_client import ChatGPTClient

router = APIRouter()
gpt = ChatGPTClient("auth.json")

class GPTRequest(BaseModel):
    prompt: str

@router.post("/gpt")
async def ask_gpt(req: GPTRequest):
    result = await gpt.send_prompt(req.prompt)
    return {"answer": result}
