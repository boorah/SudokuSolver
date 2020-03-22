import isqrt
import pygame


class SudokuSolver:
    def __init__(self, sudoku, obj):
        self.sudoku = sudoku
        self.count = 0
        self.gui_ob = obj

    def solveBoard(self):
        return self.canSolveBoard(0, 0, self.sudoku)

    def canSolveBoard(self, row, column, board):
        # If the column goes out of bounds, reset it to zero
        if column == len(board[row]):
            column = 0
            row += 1

            # If the new row's index is equal to the board's length then, return true. Since, all rows have been traversed
            if row == len(board):
                return True

        # If the current entry is filled, then move to the next column
        if board[row][column] != 0:
            return self.canSolveBoard(row, column + 1, board)

        # Try and check if a value can be placed
        for i in range(1, len(board) + 1):
            valueToPlace = i

            if self.canPlaceValue(row, column, board, valueToPlace):
                board[row][column] = valueToPlace
                self.gui_ob.update_cell(valueToPlace, self.gui_ob.cells[row][column])
                pygame.time.delay(100)

                self.count += 1
                self.printBoard(board)

                # Keep going on the current path and check to see if the next values can be placed
                if self.canSolveBoard(row, column + 1, board):
                    return True

                board[row][column] = 0

        return False

    def canPlaceValue(self, row, column, board, valueToPlace):
        # Check if valueToPlace conflicts with the other elements in the row
        if valueToPlace in board[row]:
            return False

        # Check if valueToPlace conflicts with other elements in the column
        for i in board:
            if i[column] == valueToPlace:
                return False

        # Check if valueToPlace conflicts with other elements in the subgrid
        squareSize = isqrt.isqrt(len(board))

        startRow = squareSize * (row // squareSize)
        startColumn = squareSize * (column // squareSize)

        for i in range(startRow, startRow + squareSize):
            for j in range(startColumn, startColumn + squareSize):
                if valueToPlace == board[i][j]:
                    return False

        return True

    def printBoard(self, board):
        for i in board:
            print(i)

        print(f"\n{self.count}\n")
