from contextlib import asynccontextmanager

from fastapi import FastAPI
import uvicorn


from app.db.session import engine
from app.router.v1 import actor
from app.router.v1 import film

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Context manager to handle the lifespan of the FastAPI application."""
    yield
    await engine.dispose()


app = FastAPI(lifespan=lifespan)
app.include_router(actor.router)
app.include_router(film.router)


if __name__ == '__main__':
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)