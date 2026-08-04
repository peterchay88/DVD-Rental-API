import os

from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncSession
)


load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_async_engine(
    url=DATABASE_URL,
    pool_size=10,
    max_overflow=20,
    echo=True
)

async_session_local = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)