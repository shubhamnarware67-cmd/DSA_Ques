"""
Q93: Sudoku Solver (Backtracking)
===================================
Problem: Solve a 9x9 Sudoku puzzle by filling in the empty cells ('.').
Each row, column, and 3x3 box must contain digits 1-9 exactly once.
"""

def solve_sudoku(board):
    def is_valid(r, c, num):
        box_r, box_c = 3*(r//3), 3*(c//3)
        for i in range(9):
            if board[r][i] == num: return False
            if board[i][c] == num: return False
            if board[box_r + i//3][box_c + i%3] == num: return False
        return True

    def solve():
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    for num in '123456789':
                        if is_valid(r, c, num):
                            board[r][c] = num
                            if solve(): return True
                            board[r][c] = '.'
                    return False
        return True

    solve()

if __name__ == "__main__":
    board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    solve_sudoku(board)
    for row in board: print(row)
