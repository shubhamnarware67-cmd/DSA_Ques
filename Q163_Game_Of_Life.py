"""
Q163: Game of Life (Conway's)
===============================
Problem: Apply Game of Life rules simultaneously to all cells.
Rules: live(1) cell with <2 or >3 live neighbors dies.
       live cell with 2-3 neighbors survives.
       dead(0) cell with exactly 3 live neighbors becomes alive.

Example:
    [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
    -> [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
"""

def game_of_life(board):
    rows, cols = len(board), len(board[0])
    dirs = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

    def count_live(r, c):
        return sum(1 for dr,dc in dirs
                   if 0<=r+dr<rows and 0<=c+dc<cols and abs(board[r+dr][c+dc])==1)

    for r in range(rows):
        for c in range(cols):
            live = count_live(r, c)
            if board[r][c] == 1 and live not in [2,3]: board[r][c] = -1
            elif board[r][c] == 0 and live == 3:       board[r][c] = 2

    for r in range(rows):
        for c in range(cols):
            if board[r][c] == -1: board[r][c] = 0
            elif board[r][c] == 2: board[r][c] = 1

if __name__ == "__main__":
    board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
    game_of_life(board)
    for row in board: print(row)
