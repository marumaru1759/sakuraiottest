from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post("/api")
async def api_handler(request: Request):
    return JSONResponse(content={"message": "ok"})
