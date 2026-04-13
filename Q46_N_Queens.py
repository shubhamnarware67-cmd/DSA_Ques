"""
Q46: N-Queens Problem (Backtracking)
=====================================
Problem: Place n queens on an n x n chessboard so that no two queens
attack each other. Return all distinct solutions.

Example:
    n = 4
    Output: 2 solutions
"""

def solve_n_queens(n):
    result = []
    cols = set()
    pos_diag = set()  # (r+c)
    neg_diag = set()  # (r-c)
    board = [['.']*n for _ in range(n)]

    def backtrack(r):
        if r == n:
            result.append([''.join(row) for row in board])
            return
        for c in range(n):
            if c in cols or (r+c) in pos_diag or (r-c) in neg_diag:
                continue
            cols.add(c); pos_diag.add(r+c); neg_diag.add(r-c)
            board[r][c] = 'Q'
            backtrack(r+1)
            cols.remove(c); pos_diag.remove(r+c); neg_diag.remove(r-c)
            board[r][c] = '.'

    backtrack(0)
    return result

if __name__ == "__main__":
    solutions = solve_n_queens(4)
    print(f"Solutions for 4x4: {len(solutions)}")  # 2
    for sol in solutions:
        for row in sol: print(row)
        print()
