"""
Q304: Cat and Mouse (Game Theory + BFS)
=========================================
Problem: Cat at node 2, Mouse at node 1, Hole at 0. They alternate moves.
Mouse wins if reaches 0. Cat wins if catches mouse. Return result:
1 = mouse wins, 2 = cat wins, 0 = draw.

Example:
    graph=[[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]] -> 0
"""
from collections import deque

def cat_mouse_game(graph):
    MOUSE_WIN, CAT_WIN, DRAW = 1, 2, 0
    n = len(graph)
    # State: (mouse_pos, cat_pos, turn) -> result
    # turn: 1=mouse, 2=cat
    degree = {}
    color = {}
    for m in range(n):
        for c in range(n):
            degree[(m,c,1)] = len(graph[m])
            degree[(m,c,2)] = len(graph[c])

    queue = deque()
    # Known results
    for i in range(1, n):
        for t in [1, 2]:
            color[(0,i,t)] = MOUSE_WIN
            queue.append((0,i,t))
            color[(i,i,t)] = CAT_WIN
            queue.append((i,i,t))

    while queue:
        m, c, t = queue.popleft()
        res = color[(m,c,t)]
        # Parent states
        if t == 1:  # Mouse moved, prev turn was cat's
            for pc in graph[c]:
                if (m,pc,2) in color: continue
                if res == CAT_WIN:
                    color[(m,pc,2)] = CAT_WIN
                    queue.append((m,pc,2))
                else:
                    degree[(m,pc,2)] -= 1
                    if degree[(m,pc,2)] == 0:
                        color[(m,pc,2)] = MOUSE_WIN
                        queue.append((m,pc,2))
        else:  # Cat moved, prev turn was mouse's
            for pm in graph[m]:
                if (pm,c,1) in color: continue
                if res == MOUSE_WIN:
                    color[(pm,c,1)] = MOUSE_WIN
                    queue.append((pm,c,1))
                else:
                    degree[(pm,c,1)] -= 1
                    if degree[(pm,c,1)] == 0:
                        color[(pm,c,1)] = CAT_WIN
                        queue.append((pm,c,1))

    return color.get((1,2,1), DRAW)

if __name__ == "__main__":
    print(cat_mouse_game([[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]]))  # 0
    print(cat_mouse_game([[1,3],[0],[3],[0,2]]))  # 1
