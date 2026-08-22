from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import async_session_local


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """Yields an asynchronous database session for use in FastAPI endpoints."""
    async with async_session_local() as session:
        yield session
