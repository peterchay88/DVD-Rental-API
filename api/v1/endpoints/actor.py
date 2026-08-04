from fastapi import (
    APIRouter,
    Depends
)
from sqlalchemy.ext.asyncio import AsyncSession

from db.deps import get_db


router = APIRouter()

@router.get("/actors")
async def get_actors(db: AsyncSession = Depends(get_db)):
    """
    Endpoint to retrieve a list of actors from the database.

    Args:
        db (AsyncSession): The asynchronous database session, injected by FastAPI's dependency system.
    """
    result = await db.execute("SELECT * FROM actors")
    actors = result.fetchall()
    return {"actors": [dict(actor) for actor in actors]}