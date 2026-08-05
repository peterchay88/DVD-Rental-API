import os

from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine


load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL is not set. Define it in your environment or .env file before starting the app.")

engine = create_async_engine(
    url=DATABASE_URL,
    pool_size=10,
    max_overflow=20,
    echo=True,
)

async_session_local = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)