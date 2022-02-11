from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


file = "auth.sqlite3"
# create an engine
engine = create_engine(f"sqlite:///{file}", echo=False)
# create a configured session class
Session = sessionmaker(bind=engine)

Model = declarative_base()
