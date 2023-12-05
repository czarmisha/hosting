from src.db.session import create_session


def get_db():
    return create_session()
