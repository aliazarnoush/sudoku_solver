import numpy as np

class SudokuSolver:
    def __init__(self):
        # Initialize the Sudoku board, sets for available numbers, and list of empty cells
        self.board = np.zeros((9, 9), dtype=int)
        self.rows = [set(range(1, 10)) for _ in range(9)]
        self.cols = [set(range(1, 10)) for _ in range(9)]
        self.blocks = [set(range(1, 10)) for _ in range(9)]
        self.empty_cells = []

    def get_block_index(self, row, col):
        # Calculate the block index based on the row and column
        return (row // 3) * 3 + (col // 3)

    def load_sudoku(self, filename):
        # Load the Sudoku puzzle from a file
        with open(filename, 'r') as file:
            lines = file.readlines()
            if len(lines) != 9:
                raise ValueError("Input file must contain exactly 9 lines.")
            for i in range(9):
                line = lines[i].strip().split()
                if len(line) != 9:
                    raise ValueError(f"Line {i + 1} must contain exactly 9 integers.")
                for j in range(9):
                    num = int(line[j])
                    self.board[i][j] = num
                    if num != 0:
                        # If the cell is pre-filled, remove the number from the available sets
                        self.rows[i].remove(num)
                        self.cols[j].remove(num)
                        self.blocks[self.get_block_index(i, j)].remove(num)
                    else:
                        # If the cell is empty, add it to the list of empty cells
                        self.empty_cells.append((i, j))

    def is_valid(self, row, col, num):
        # Check if placing a number is valid by checking the row, column, and block sets
        block_idx = self.get_block_index(row, col)
        return num in self.rows[row] and num in self.cols[col] and num in self.blocks[block_idx]

    def place_number(self, row, col, num):
        # Place a number on the board and update the row, column, and block sets
        self.board[row][col] = num
        self.rows[row].remove(num)
        self.cols[col].remove(num)
        self.blocks[self.get_block_index(row, col)].remove(num)

    def remove_number(self, row, col, num):
        # Remove a number from the board and update the row, column, and block sets
        self.board[row][col] = 0
        self.rows[row].add(num)
        self.cols[col].add(num)
        self.blocks[self.get_block_index(row, col)].add(num)

    def solve(self):
        # Backtracking solver for the Sudoku puzzle
        if not self.empty_cells:
            # If there are no empty cells, the puzzle is solved
            return True

        # Get the next empty cell to fill
        row, col = self.empty_cells.pop()
        block_idx = self.get_block_index(row, col)

        for num in range(1, 10):
            if self.is_valid(row, col, num):
                # If placing the number is valid, place it on the board
                self.place_number(row, col, num)
                if self.solve():
                    # Recursively solve the next cell
                    return True
                # If the solution is not valid, remove the number and backtrack
                self.remove_number(row, col, num)

        # If no number is valid, add the cell back to the list and backtrack
        self.empty_cells.append((row, col))
        return False

    def print_sudoku(self):
        # Print the Sudoku board
        for i in range(9):
            for j in range(9):
                print(self.board[i][j], end=" ")
            print()

# Create a SudokuSolver instance
solver = SudokuSolver()
# Load the Sudoku puzzle from the file
solver.load_sudoku('sudoku.txt')
# Solve the puzzle
if solver.solve():
    # Print the solved puzzle
    solver.print_sudoku()
else:
    print("No solution exists")
