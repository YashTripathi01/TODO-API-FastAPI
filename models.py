from sqlalchemy import Column, Integer, String
from .database import Base


class table(Base):
    __tablename__ = 'todo_table'
    id = Column(Integer, primary_key=True)
    task = Column(String(256))
