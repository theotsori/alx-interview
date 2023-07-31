# Solving the N-Queens Puzzle with Python

The N-Queens puzzle is a classic problem in computer science and mathematics, where the objective is to place N queens on an NxN chessboard in such a way that no two queens threaten each other. In other words, no two queens can share the same row, column, or diagonal.

![NQueens](https://developers.google.com/static/optimization/images/queens/sol_4x4_b.png)

## Algorithm Overview

We will use a backtracking algorithm to solve the N-Queens puzzle. The backtracking algorithm explores all possible configurations of queens on the chessboard and prunes the search tree whenever a solution is not feasible.

Here are the steps of the backtracking algorithm:

1. Start with an empty chessboard.
2. Place a queen in the first row.
3. Move to the next row and place a queen in a column that does not conflict with the queens already placed.
4. Repeat step 3 for all rows until all queens are placed, or we find a valid solution.
5. if a conflict is encountered while placing queens, backtrack to the previous row and try another position.
6. Continue the process until all solutions are found.

## Python Implementation
```python
def is_safe(board, row, col, N):
  """
  Check if it is safe to place a queen at
  board and on the current row on the left
  side and lower diagnoal on the left side
  and upper diagonal on the left side
  """

  for i in range(col):
    if board[row][i] == 1:
      return False
 
  for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
    if board[i][j] == 1:
      return False
 
  for i, j in zip(range(row, N), range(col, -1, -1)):
    if board[i][j] == 1:
      return False

  return True


def solve_nqueens_util(board, col, N, solutions):
  """
  If all queens are placed, add the solution to the solutions list
  Place the queen in the current position
  Recur to place rest of the queens
  If placing queen in board doesn't lead to a
  solution, backtrack and remove the queen
  """
  if col == N:
    solution = []
    for i in range(N):
      solution.append(''.join(['Q' if board[i][j] == 1 else '.' for j in range(N)]))
    solutions.append(solution)
    return

  for i in range(N):
    if is_safe(board, i, col, N):
      board[i][col] = 1
      solve_nqueens_util(board, col + 1, N, solutions)
      board[i][col] = 0


def solve_nqueens(N):
  """
  Initialize an empty NxN chessboard
  """
  board = [[0 for _ in range(N)] for _ in range(N)]

  solutions = []
  solve_nqueens_util(board, 0, N, solutions)

  return solutions


if __name__ == '__main__':
  N = 8
  solutions = solve_nqueens(N)

  print(f"NUmber of solutions for {N}-Queens: {len(solutions)}")
  for idx, solution in enumerate(solutions):
    print(f"\nSolution {idx + 1}:")
    for row in solution:
      print(row)
```

## Usage

1. Change the value of 'N' to the desired board size in the `__main__` block.
2. Run the script, and it will output the number of solutions found and display each solution on the console.

The script will find and display all possible for the N-Queens puzzle for the given board size 'N'.