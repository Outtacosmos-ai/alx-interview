#!/usr/bin/python3
"""
N Queens solver - Place N non-attacking queens on an NxN chessboard
"""
import sys


def is_safe(board, row, col, n):
    """
    Check if a queen can be placed on board[row][col]
    
    Args:
        board: 2D list representing the board
        row: Current row to check
        col: Current column to check
        n: Size of the board
    
    Returns:
        Boolean indicating if the position is safe
    """
    # Check this row on left side
    for j in range(col):
        if board[row][j] == 1:
            return False
    
    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # Check lower diagonal on left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    return True


def solve_nqueens(n):
    """
    Solve the N Queens problem and return all solutions
    
    Args:
        n: Size of the board and number of queens
    
    Returns:
        List of solutions, where each solution is a list of queen positions
    """
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)
    
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    
    # Initialize the board
    board = [[0 for x in range(n)] for y in range(n)]
    solutions = []
    
    def solve_util(board, col):
        """
        Recursive utility function to solve N Queens problem
        """
        # Base case: If all queens are placed, return True
        if col >= n:
            solution = []
            for i in range(n):
                for j in range(n):
                    if board[i][j] == 1:
                        solution.append([i, j])
            solutions.append(solution)
            return
        
        # Consider this column and try placing this queen in all rows one by one
        for i in range(n):
            if is_safe(board, i, col, n):
                # Place this queen in board[i][col]
                board[i][col] = 1
                
                # Recur to place rest of the queens
                solve_util(board, col + 1)
                
                # If placing queen in board[i][col] doesn't lead to a solution,
                # then remove queen from board[i][col]
                board[i][col] = 0
    
    # Start from first column
    solve_util(board, 0)
    return solutions


def main():
    """Main function to handle command line arguments and print solutions"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    
    solutions = solve_nqueens(n)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
