from typing import Generator

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import Session

async def get_getsession() -> Generator:
    session: AsyncSession = Session()

    try:
        yield session
    finally:
        await session.close()
