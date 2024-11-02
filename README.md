Sudoku Solver.
Simple programme to efficiently solve any given sudoku board using the backtracking algorithm.

Can't have the same number twice in a row, column, or box.

Back Tracking Algorithm:
# 1) Pick empty square.
# 2) Try numbers 1-9. Find one that works within the parameters of the game.
# 3) Move to the next empty square, repeat step 2.
# Repeat the process until we come to a square with no valid solution.
# Back track to the previous square and continue trying numbers from n + 1 where n is the last number we tried in that square.
# If no valid solution is found in this square after backtracking we back track again.
# This process is repeated until all squares are valid.

Created using python, no other dependencies. 
