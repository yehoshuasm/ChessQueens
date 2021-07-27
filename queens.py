from solution import Solution
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import Session

engine = create_engine('postgresql://nqueens:nqueens@localhost/NQueens')

class NQueens:

    def __init__(self, size):
        self.size = size
        self.board = [-1] * self.size
        self.solutions = 0

    def solve(self):
        positions = [-1] * self.size
        self.place_queen(positions, 0)
        print(self.solutions, " solutions were found.")

    def place_queen(self, positions, row):
        if row == self.size:
            self.store_position(positions)
            self.solutions += 1
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

    def store_position(self, board):
        solution = ""
        for row in range(self.size):
            for column in range(self.size):
                if(board[row] == column):
                    solution += "Q"
                else:
                    solution += "."
            solution += "\n"
        with Session(engine) as session:
            session.begin()
            try:
                session.add(Solution(position = solution))
            except:
                session.rollback()
            else:
                session.commit()