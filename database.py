
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql+psycopg2://postgres:mysecretpassword@db:5432/postgres")

LocalSession = sessionmaker(bind=engine,autocommit=False, autoflush=False)
Base=declarative_base()