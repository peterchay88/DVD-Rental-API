import logging
from typing import Annotated

from fastapi import APIRouter, Depends, Response, status, Query

from app.schemas.film_read import FilmRead
from app.repositories.film_repository import FilmRepository, get_fil_repository
from app.schemas.json_data import JsonData
from app.schemas.json_error import JsonError

router = APIRouter()
logger = logging.getLogger(__name__)

film_dependency = Annotated[FilmRepository, Depends(get_fil_repository)]


@router.get("/film", tags=["films"])
async def get_film_by_id(
    film_repo: film_dependency,
    response: Response = None,
    film_id: int = Query(..., description="The ID of the film to retrieve"),
) -> JsonError[str] | JsonData[FilmRead]:
    """
    Endpoint to retrieve a film by its ID.

    Args:
        film_id (int): The ID of the film to retrieve.
        film_repo (FilmRepository): The film repository, injected by FastAPI's dependency system.
        response (Response): Response object that stores the response from the API.
    """
    row = await film_repo.get_film_by_id(film_id)
    if not row:
        response.status_code = status.HTTP_404_NOT_FOUND
        return JsonError(error={"message": "Film not found"})
    
    film = FilmRead.model_validate(row)
    return JsonData(data=[film])


@router.get("/films", tags=["films"])
async def get_films(
    film_repo: film_dependency,
    response: Response = None,
    limit: int = Query(0, description="The number of films to return.")
) -> JsonError[str] | JsonData[FilmRead]:
    """
    Endpoint to retrieve a list of films.
    Args:
        film_repo (FilmRepository): The film repository, injected by FastAPI's dependency system.
        response (Response): Response object that stores the response from the API.
        limit (int, optional): The number of rows to limit

    Returns:
        JsonError[str] | JsonData[FilmRead]: _description_
    """
    rows = await film_repo.get_films(limit)
    
    if not rows:
        response.status_code = status.HTTP_404_NOT_FOUND
        return JsonError(error={"message": "No films returned"})
    
    films = [FilmRead.model_validate(row) for row in rows]
    return JsonData(data=films)