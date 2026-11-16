from fastapi import FastAPI

from agentgate.config import settings
from agentgate.logging_config import configure_logging

logger = configure_logging(settings.log_level, settings.log_json)

app = FastAPI(title=settings.app_name)


@app.get("/health")
def health():
    logger.info("health_check")
    return {"status": "ok"}


@app.post("/echo")
def echo(payload: dict):
    logger.info("echo", keys=list(payload))
    return payload
