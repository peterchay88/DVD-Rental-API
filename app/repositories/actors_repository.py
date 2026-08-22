from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.deps import get_db
from app.models.actor_table import ActorTable


class ActorsRepository:

    def __init__(self, db: AsyncSession):
        self.db = db
        self.actor_table = ActorTable

    async def get_all_actors(
            self,
            limit: int = None
    ) -> list[ActorTable] | None:
        """
        Retrieve all actors from the database.

        Args:
            limit (int, optional): Maximum number of actors to return.

        Returns:
            list[Actor]: A list of Actor model instances.
        """
        if limit is not None and limit <= 0:
            raise ValueError("Limit must be a positive integer.")

        query = select(self.actor_table)
        if limit is not None:
            query = query.order_by(self.actor_table.actor_id).limit(limit)
        result = await self.db.execute(query)
        actors = result.scalars().all()

        return actors


    async def get_actor_by_id(self, actor_id: int):
        """
        Retrieve an actor by their ID.

        Args:
            actor_id (int): The ID of the actor to retrieve.

        Returns:
            Actor | None: The Actor instance if found, otherwise None.
        """
        query = select(self.actor_table).where(self.actor_table.actor_id == actor_id)
        result = await self.db.execute(query)
        return result.scalar_one_or_none()


def get_actors_repository(db: AsyncSession = Depends(get_db)) -> ActorsRepository:
    """
    Factory function to create and return an instance of ActorsRepository.

    Returns:
        ActorsRepository: An instance of the ActorsRepository class.
    """
    return ActorsRepository(db)
