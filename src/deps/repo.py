from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from .session import get_session


def get_repo(repo):
    async def dep(session: AsyncSession = Depends(get_session)):
        yield repo(session)

    return dep
