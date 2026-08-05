from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.deps import get_db
from app.repositories import ActorsRepository

router = APIRouter()


@router.get("/actors", tags=["actors"])
async def get_actors(
        lmit: int = None,
        db: AsyncSession = Depends(get_db)):
    """
    Endpoint to retrieve a list of actors from the database.

    Args:
        db (AsyncSession): The asynchronous database session, injected by FastAPI's dependency system.
    """
    # result = await db.execute(text("SELECT * FROM public.actor"))
    # actors = result.fetchall()
    # return {"actors": [dict(actor) for actor in actors]}