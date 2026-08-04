from contextlib import asynccontextmanager

from fastapi import FastAPI

from db.session import engine


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    await engine.dispose()


app = FastAPI(lifespan=lifespan)
