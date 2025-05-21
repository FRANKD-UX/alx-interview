#!/usr/bin/python3
"""
N Queens Puzzle Solution
This script solves the N-Queens problem:
Place N non-attacking queens on an NxN chessboard.
"""
import sys


def is_safe(board, row, col, n):
    """
    Check if a queen can be placed at position (row, col) without attacking
    any other queens already placed on the board.

    Args:
        board: List of lists representing current queen positions
        row: Row position to check
        col: Column position to check
        n: Size of the board

    Returns:
        Boolean: True if safe, False otherwise
    """
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i] == col:
            return False

    # Check upper-left diagonal
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i] == j:
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i] == j:
            return False
        i -= 1
        j += 1

    return True


def solve_nqueens(n):
    """
    Solve the N-Queens puzzle using backtracking.

    Args:
        n: Size of the board (n x n) and number of queens

    Returns:
        List of solutions, where each solution is a list of queen positions
    """
    solutions = []
    board = [-1] * n

    def backtrack(row):
        if row == n:
            # Found a solution, convert to required format
            solution = [[i, board[i]] for i in range(n)]
            solutions.append(solution)
            return

        for col in range(n):
            if is_safe(board, row, col, n):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1  # Backtrack

    backtrack(0)
    return solutions


def main():
    """
    Main function to parse arguments and solve the N-Queens problem.
    """
    # Check argument count
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Parse N
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Check if N is at least 4
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Solve the problem and print solutions
    solutions = solve_nqueens(n)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
