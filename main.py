from queens import NQueens
import sys
from database_helper import DatabaseHelper

if __name__ == '__main__':
    databaseHelper = DatabaseHelper()

    databaseHelper.init_database()

    if len(sys.argv) == 2:
        n = sys.argv[1]
        if n.isnumeric:
            nqueens = NQueens(int(n), databaseHelper, True)
            nqueens.solve()
