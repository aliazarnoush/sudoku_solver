# Sudoku Solver

This repository contains a Python implementation of a Sudoku solver. The original code was written in Pascal and has been converted to Python. The solver uses a combination of constraint propagation and backtracking to efficiently solve Sudoku puzzles.

## Usage

To use this solver, you need to create a text file called `sudoku.txt` that contains an unsolved Sudoku puzzle where 0 is used for empty cells. Below is an example of the format:

```text
5 3 0 0 7 0 0 0 0
6 0 0 1 9 5 0 0 0
0 9 8 0 0 0 0 6 0
8 0 0 0 6 0 0 0 3
4 0 0 8 0 3 0 0 1
7 0 0 0 2 0 0 0 6
0 6 0 0 0 0 2 8 0
0 0 0 4 1 9 0 0 5
0 0 0 0 8 0 0 7 9
```

The code will read the puzzle, solve it, and print the solved puzzle. If the puzzle does not have any solutions, it will indicate that no solution exists.

## Methods Used
Constraint Propagation
The solver uses sets to keep track of available numbers for each row, column, and block. This allows the algorithm to quickly check if a number can be placed in a cell.

- Rows, Columns, and Blocks Sets: Each of these sets contains the numbers that can still be placed in the respective row, column, or 3x3 block.
- Initialization: When the puzzle is loaded, the sets are updated to remove the numbers that are already placed in the puzzle.

## Backtracking

The solver employs a backtracking algorithm to try placing numbers in empty cells and revert changes if a conflict is found.

- Recursive Solving: The solve method is called recursively. It tries to place a number in an empty cell, checks if the placement is valid, and then moves on to the next empty cell.
- Heuristic: The solver selects the next empty cell and tries to fill it with a valid number from 1 to 9. If a valid placement is found, it proceeds to the next cell. If no valid number can be placed, it backtracks to the previous cell and tries the next number.

## Methods in the Solver

- `get_block_index`: Calculates the index of the 3x3 block for a given cell.
- `load_sudoku`: Reads the Sudoku puzzle from a file and initializes the board and tracking sets.
- `is_valid`: Checks if placing a number in a given cell is valid according to Sudoku rules.
- `place_number`: Places a number in a cell and updates the tracking sets.
- `remove_number`: Removes a number from a cell and updates the tracking sets.
- `solve`: Implements the backtracking algorithm to solve the puzzle.
- `print_sudoku`: Prints the Sudoku board.

## Example
To run the solver, ensure you have `sudoku.txt` in the same directory as your Python script. Here is how you can run it:

```python
solver = SudokuSolver()
solver.load_sudoku('sudoku.txt')
if solver.solve():
    solver.print_sudoku()
else:
    print("No solution exists")
```
## Conclusion
This Sudoku solver efficiently solves puzzles using a combination of constraint propagation and backtracking. It reads puzzles from a text file, solves them, and prints the solution or indicates if no solution exists. The solver is designed to handle standard 9x9 Sudoku puzzles.
