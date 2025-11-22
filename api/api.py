from http import HTTPStatus

from fastapi import FastAPI, Request
from loguru import logger

from api.lifespan import lifespan
from api.routers import info_router

app = FastAPI(lifespan=lifespan)

# Routers
app.include_router(info_router, tags=["Info"], prefix="/api/info")


# Logging Middleware
@app.middleware("http")
async def log_requests(request: Request, call_next):
    client_host = request.client.host
    client_port = request.client.port
    response = await call_next(request)
    logger.info(
        f"{client_host}:{client_port} - {request.method} {request.url} - {response.status_code} {HTTPStatus(response.status_code).phrase}"
    )
    return response
