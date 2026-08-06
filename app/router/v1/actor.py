from fastapi import APIRouter, Depends, Response, status
from typing import Annotated

from app.repositories import ActorsRepository, get_actors_repository
from app.schemas.actor_read import ActorRead
from app.schemas.json_data import JsonData

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
    rows = await repo.get_all_actors(limit=limit)
    actor = [ActorRead.model_validate(row) for row in rows]

    return JsonData(data=actor)


@router.get("/actors/{actor_id}", tags=["actors"])
async def get_actor_by_id(
        actor_id: int,
        repo: actor_dependency,
        response: Response
):
    """
    Endpoint to retrieve an actor by their ID.

    Args:
        actor_id (int): The ID of the actor to retrieve.
        repo (ActorsRepository): The actors repository, injected by FastAPI's dependency system.
        response (Response): Response object that stores the response from the API.
    """
    row = await repo.get_actor_by_id(actor_id=actor_id)

    if row is None:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message": "Actor not found"}

    actor = [ActorRead.model_validate(row)]
    return JsonData(data=actor)

