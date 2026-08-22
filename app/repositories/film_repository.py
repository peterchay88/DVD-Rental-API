from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from ..db.deps import get_db
from ..models.film_table import FilmTable


class FilmRepository:
    
    def __init__(self, db: AsyncSession):
        self.db = db
        self.film_table = FilmTable
        
    async def get_film_by_id(
        self, 
        film_id: int
        ) -> FilmTable | None:
        """
        Retrieve a film by its ID.

        Args:
            film_id (int): The ID of the film to retrieve.

        Returns:
            Film | None: The Film instance if found, otherwise None.
        """
        query = select(self.film_table).where(self.film_table.film_id == film_id)
        result = await self.db.execute(query)
        return result.scalar_one_or_none()