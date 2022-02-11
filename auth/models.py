from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.orm import relationship
from .base.models import Model, engine


class User(Model):
    """creates a table users"""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    first_name = Column(String)
    last_name = Column(String)
    password = Column(String)


Model.metadata.create_all(engine)
