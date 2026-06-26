"""
Q328: Shortest Path to Get All Keys (BFS + Bitmask)
====================================================
Problem: Grid with keys (a-f lowercase), locks (A-F uppercase), obstacles (#).
Find shortest path to collect all keys.

Example:
    ["@.a..","###.#","b.A.B"] -> 8
    ["@..aA","..B#.","....b"] -> 6
"""
from collections import deque

def shortest_path_all_keys(grid):
    rows, cols = len(grid), len(grid[0])
    start_r = start_c = 0
    all_keys = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '@': start_r, start_c = r, c
            elif grid[r][c].islower():
                all_keys |= 1 << (ord(grid[r][c]) - ord('a'))

    queue = deque([(start_r, start_c, 0, 0)])
    visited = {(start_r, start_c, 0)}

    while queue:
        r, c, keys, steps = queue.popleft()
        for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
            nr, nc = r+dr, c+dc
            if nr<0 or nr>=rows or nc<0 or nc>=cols: continue
            cell = grid[nr][nc]
            if cell == '#': continue
            if cell.isupper() and not (keys & (1 << (ord(cell)-ord('A')))): continue
            new_keys = keys
            if cell.islower(): new_keys |= 1 << (ord(cell)-ord('a'))
            if new_keys == all_keys: return steps + 1
            if (nr, nc, new_keys) not in visited:
                visited.add((nr, nc, new_keys))
                queue.append((nr, nc, new_keys, steps+1))
    return -1

if __name__ == "__main__":
    print(shortest_path_all_keys(["@.a..","###.#","b.A.B"]))   # 8
    print(shortest_path_all_keys(["@..aA","..B#.","....b"]))   # 6
