from contextlib import asynccontextmanager

from fastapi import FastAPI
import uvicorn


from app.api.v1.endpoints import actor
from app.db.session import engine


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Context manager to handle the lifespan of the FastAPI application."""
    yield
    await engine.dispose()


app = FastAPI(lifespan=lifespan)
app.include_router(actor.router)


if __name__ == '__main__':
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)