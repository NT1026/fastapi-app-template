from contextlib import asynccontextmanager

from fastapi import FastAPI
from loguru import logger

from log import init_logging


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    init_logging()
    logger.info("Starting up the FastAPI application...")

    yield

    # Shutdown
    logger.info("Shutting down the FastAPI application...")
