"""
Q417: Check Move in Tic-Tac-Toe Style Game (Direction Check)
==============================================================
Problem: Given m x n board with pieces, check if moving piece from
(r,c) in direction (dr,dc) is a valid "flip" move (like Othello).

Example:
    board=[['B','_','_'],['_','W','_'],['_','_','B']],
    rMove=1,cMove=1,color='B',direction='Right' -> ...
"""

def check_move(board, rMove, cMove, color, direction):
    dirs = {'Left':(0,-1),'Right':(0,1),'Up':(-1,0),'Down':(1,0),
            'UpLeft':(-1,-1),'UpRight':(-1,1),'DownLeft':(1,-1),'DownRight':(1,1)}
    dr, dc = dirs[direction]
    rows, cols = len(board), len(board[0])
    r, c = rMove + dr, cMove + dc
    opp = 'W' if color == 'B' else 'B'
    count_opp = 0
    while 0 <= r < rows and 0 <= c < cols:
        if board[r][c] == opp:
            count_opp += 1
        elif board[r][c] == color:
            return count_opp > 0
        else:
            return False
        r += dr; c += dc
    return False

if __name__ == "__main__":
    board = [["_","_","_"],["_","B","_"],["_","_","S"]]
    print(check_move(board, 1, 1, "W", "Right"))  # depends on fill — example simplified
