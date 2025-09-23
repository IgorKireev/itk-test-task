from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from src.settings.settings import settings


async_engine = create_async_engine(
    url=settings.database_url_asyncpg,
    echo=False,
    pool_size=5,
    max_overflow=10
)

async_session_factory = async_sessionmaker(async_engine, class_=AsyncSession)

async def get_session() -> AsyncSession:
    async with async_session_factory() as session:
        yield session