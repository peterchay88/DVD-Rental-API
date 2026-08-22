import logging
from typing import Annotated

from fastapi import APIRouter, Depends, Response, status, Query

from ...schemas.film_read import FilmRead
from ...repositories.film_repository import FilmRepository, get_fil_repository
from ...schemas.json_data import JsonData
from ...schemas.json_error import JsonError

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