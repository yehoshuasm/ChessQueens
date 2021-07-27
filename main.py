from queens import NQueens
from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative import declarative_base
import sys

Base = declarative_base()
db_engine = create_engine('postgresql://nqueens:nqueens@localhost/NQueens')

if __name__ == '__main__':
    Base.metadata.drop_all(db_engine)
    Base.metadata.create_all(db_engine)

    if len(sys.argv) == 2:
        n = sys.argv[1]
        if n.isnumeric:
            nqueens = NQueens(int(n))
            nqueens.solve()
