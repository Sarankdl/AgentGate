from fastapi import FastAPI, Request

app = FastAPI(title="AgentGate")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/echo")
async def echo(request: Request):
    return await request.json()
