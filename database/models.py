import uuid

from sqlalchemy import Column, String

from database.connection import Base, engine


class Posts(Base):
    __tablename__ = "posts"

    id = Column(String, primary_key=True, default=f'{uuid.uuid4()}', index=True)
    title = Column(String)
    description = Column(String)


Base.metadata.create_all(engine)
