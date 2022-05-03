from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine


engine = create_engine('sqlite:///./my_todo/my_todo.db')

Base = declarative_base()

session = Session(bind=engine, expire_on_commit=False)

