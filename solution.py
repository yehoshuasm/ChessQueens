from sqlalchemy.schema import Column
from sqlalchemy.sql.sqltypes import Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Solution(Base):
    __tablename__ = 'solutions'

    id = Column(Integer(), primary_key=True)
    position = Column(String(), nullable=False, unique=True)