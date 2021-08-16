from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import Session
from sqlalchemy.sql import select
from sqlalchemy.sql.expression import update
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String


Base = declarative_base()
engine = create_engine('postgresql+psycopg2://nqueens:nqueens@{}:5432/nqueens'.format('postgres_container'))

class NQueenProblem(Base):
    __tablename__ ='n_queen_problems'

    id = Column(Integer(), primary_key=True)
    numberOfSolutions = Column(Integer())

class Solution(Base):
    __tablename__ = 'solutions'

    id = Column(Integer(), primary_key=True)
    n_queen_problem_id = Column(Integer(), ForeignKey('n_queen_problems.id'))
    position = Column(String(), nullable=False, unique=True)



class DatabaseHelper:

    def init_database(self):
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)
    
    def checkIfIsSolved(self, n):
        with Session(engine) as session:
            result = session.query(NQueenProblem).filter(NQueenProblem.id == n).first()

            return result
    
    def storeNProblem(self, size):
        with Session(engine) as session:
            session.begin()
            try:
                session.add(NQueenProblem(id = size, numberOfSolutions = 0))
            except:
                session.rollback()
            else:
                session.commit()

    def storeNProblemNumberOfSolutions(self, size, numberOfSolutions):
        with Session(engine) as session:
            session.begin()
            try:
                session.query(NQueenProblem).filter(NQueenProblem.id == size).update(
                    {
                        NQueenProblem.numberOfSolutions: numberOfSolutions
                    }
                )
            except:
                session.rollback()
            else:
                session.commit()

    def storeSolution(self, board, size):
        solution = ""
        for row in range(size):
            for column in range(size):
                if(board[row] == column):
                    solution += "Q"
                else:
                    solution += "."
            solution += "\n"
        with Session(engine) as session:
            session.begin()
            try:
                session.add(Solution(position = solution, n_queen_problem_id = size))
            except:
                session.rollback()
            else:
                session.commit()