from src.db.session import session_maker


async def get_session():
    async with session_maker() as session:
        yield session
