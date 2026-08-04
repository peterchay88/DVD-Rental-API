from contextlib import asynccontextmanager

from fastapi import FastAPI

from db.session import engine


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Context manager to handle the lifespan of the FastAPI application."""
    yield
    await engine.dispose()


app = FastAPI(lifespan=lifespan)
