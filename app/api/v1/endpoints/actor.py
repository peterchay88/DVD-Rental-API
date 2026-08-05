from fastapi import APIRouter, Depends
from typing import Annotated

from app.repositories import ActorsRepository, get_actors_repository

router = APIRouter()

actor_dependency = Annotated[ActorsRepository, Depends(get_actors_repository)]


@router.get("/actors", tags=["actors"])
async def get_actors(
        repo: actor_dependency,
        limit: int = None):
    """
    Endpoint to retrieve a list of actors from the database.

    Args:
        repo (ActorsRepository): The actors repository, injected by FastAPI's dependency system.
        limit (int, optional): Maximum number of actors to return.
    """
    actors = await repo.get_all_actors(limit=limit)
    return {"actors": actors}

