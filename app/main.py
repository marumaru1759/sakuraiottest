from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()

class Location(BaseModel):
    latitude: float
    longitude: float
    timestamp: str

@app.post("/api")
async def api_handler(request: Request):
    body = await request.json()
    #print("Recieved JSON Data:", body)
    #return JSONResponse(content={"message": "ok"})
    return {"received": body}