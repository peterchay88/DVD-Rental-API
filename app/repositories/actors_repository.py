from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.deps import get_db
from app.models.actors import Actor


class ActorsRepository:

    def __init__(self):
        self.actor = Actor

    def get_actor_by_id(
            self,
            actor_id: int,
            db: AsyncSession = Depends(get_db)
    ):
        """
        Generate a SQL query to retrieve an actor by their ID.

        Args:
            actor_id (int): The ID of the actor to retrieve.

        Returns:
            str: A SQL query string to fetch the actor with the specified ID.
        """
        query = select(self.actor).where(self.actor.id == actor_id)
        db_result = db.scalar(query)

        return db_result


def get_actors_repository() -> ActorsRepository:
    """
    Factory function to create and return an instance of ActorsRepository.

    Returns:
        ActorsRepository: An instance of the ActorsRepository class.
    """
    return ActorsRepository()