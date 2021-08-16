from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine import create_engine

engine = create_engine('postgresql+psycopg2://nqueens:nqueens@{}:5432/nqueens'.format('postgres_container'))

class NQueens:

    def __init__(self, size, databaseHelper, useDatabase):
        self.size = size
        self.board = [-1] * self.size
        self.databaseHelper = databaseHelper
        # This has mainly the porpouse of symplifying the testing by
        # avoiding to have to mock the DatabaseHelper class
        self.useDatabase = useDatabase
        self.numberOfSolutions = 0

    def solve(self):
        positions = [-1] * self.size

        if(self.useDatabase):
            solution = self.databaseHelper.checkIfIsSolved(self.size)
            if solution is None:
                # If the problem has not been solved and stored
                # This would happen if we don't want the DB to be droped each time
                self.databaseHelper.storeNProblem(self.size)
                self.place_queen(positions, 0)
                self.databaseHelper.storeNProblemNumberOfSolutions(self.size, self.numberOfSolutions)    
            else:
                # The solution is already in the DB
                self.numberOfSolutions = solution.numberOfSolutions
        else:
            self.place_queen(positions, 0)

        print(self.numberOfSolutions, " solutions were found.")

    def place_queen(self, positions, row):
        if row == self.size:
            if self.useDatabase:
                self.databaseHelper.storeSolution(positions, self.size)
            self.numberOfSolutions += 1
        else:
            for column in range(self.size):
                if self.__is_valid_queen_position(positions, row, column):
                    positions[row] = column
                    self.place_queen(positions, row + 1)

    def __is_valid_queen_position(self, positions, occupied_rows, column):
        for i in range(occupied_rows):
            if positions[i] == column or positions[i] - i == column - occupied_rows or positions[i] + i == column + occupied_rows:
                return False
        return True

