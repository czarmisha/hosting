from sqlalchemy import MetaData


from db.session import engine

MetaData().create_all(engine)