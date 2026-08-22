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
    
    async def get_films(
        self,
        limit: int
    ) -> FilmTable | None:
        """
        Gets a a list of films

        Args:
            limit (int): The number of films to return
        """
        if limit < 0:
                    raise ValueError("Limit must be a positive integer.")
                
        if limit == 0:
            query = select(self.film_table).order_by("film_id")
        else:
            query = (
                select(self.film_table)
                    .limit(limit)
                    .order_by("film_id"))
        
        result = await self.db.execute(query)
        return result.scalars().all()
    

def get_fil_repository(db: AsyncSession = Depends(get_db)) -> FilmRepository:
    """
    Factory function to create and return an instance of FilmRepository.

    Returns:
        FilmRepository: An instance of the FilmRepository class.
    """
    return FilmRepository(db)