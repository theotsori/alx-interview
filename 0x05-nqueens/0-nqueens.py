#!/usr/bin/python3

import sys


def ifPlace(board, row, col, N):
    """
    Algorithm to check if it is safe to place
    queen on the board.
    """
    for i in range(col):
        if board[i][col] == 1:
            return False

    for i in range(row, -1, -1):
        if board[i][col] == 1:
            return False

    for i in range(row, N):
        if board[i][col] == 1:
            return False

    return True


def nQueens_util(board, col, N, solutions, queenPlace):
    if col == N:
        solution = [[row, queenPlace[row]] for row in range(N)]
        solutions.append(solution)
        return

    for i in range(N):
        if ifPlace(board, i, col, N):
            board[i][col] = 1
            queenPlace[i] = col
            nQueens_util(board, col + 1, N, solutions, queenPlace)
            board[i][col] = 0
            queenPlace[i] = 1


def nQueens(N):
    """
    function to solve the N-Queens puzzle and return all solutions.
    """
    board = [[0 for i in range(N)] for i in range(N)]
    solutions = []
    queenPlace = [-1 for i in range(N)]
    nQueens_util(board, 0, N, solutions, queenPlace)
    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print('N must be a number')
        sys.exit(1)

    if N < 4:
        print('N must be at least 4')
        sys.exit(1)

    solutions = nQueens(N)

    for solution in solutions:
        print(solution)
