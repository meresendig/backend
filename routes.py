from fastapi import APIRouter
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from gpt_client import ChatGPTClient

router = APIRouter()
gpt = ChatGPTClient("auth.json")

class GPTRequest(BaseModel):
    prompt: str

@router.post("/gpt")
async def ask_gpt(req: GPTRequest):
    try:
        result = await gpt.send_prompt(req.prompt)
        return {"answer": result}
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
