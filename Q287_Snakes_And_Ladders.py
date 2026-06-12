"""
Q287: Snakes and Ladders (BFS)
================================
Problem: n x n board, numbered 1 to n^2. -1 means no snake/ladder.
Find minimum dice rolls to reach n^2.

Example:
    board=[[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],
           [-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
    -> 4
"""
from collections import deque

def snakes_and_ladders(board):
    n = len(board)
    def label_to_pos(s):
        q, r = divmod(s-1, n)
        row = n-1-q
        col = r if q%2==0 else n-1-r
        return row, col

    visited = {1}
    queue = deque([(1, 0)])
    while queue:
        s, moves = queue.popleft()
        for dice in range(1, 7):
            ns = s + dice
            if ns > n*n: break
            r, c = label_to_pos(ns)
            if board[r][c] != -1: ns = board[r][c]
            if ns == n*n: return moves+1
            if ns not in visited:
                visited.add(ns)
                queue.append((ns, moves+1))
    return -1

if __name__ == "__main__":
    board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],
             [-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
    print(snakes_and_ladders(board))  # 4
