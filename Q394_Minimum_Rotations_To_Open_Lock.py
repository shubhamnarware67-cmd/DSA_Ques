"""
Q394: Open the Lock (BFS + Bidirectional)
==========================================
Problem: 4-wheel lock, each wheel [0-9]. Start at "0000", reach target.
deadends = locked positions. Min turns. Return -1 if impossible.

Example:
    deadends=["0201","0101","0102","1212","2002"], target="0202" -> 6
    deadends=["8888"], target="0009" -> 1
"""
from collections import deque

def open_lock(deadends, target):
    dead = set(deadends)
    if "0000" in dead: return -1
    if target == "0000": return 0

    queue = deque([("0000", 0)])
    visited = {"0000"}

    while queue:
        state, turns = queue.popleft()
        for i in range(4):
            d = int(state[i])
            for delta in (1, -1):
                new_d = (d + delta) % 10
                new_state = state[:i] + str(new_d) + state[i+1:]
                if new_state == target: return turns + 1
                if new_state not in visited and new_state not in dead:
                    visited.add(new_state)
                    queue.append((new_state, turns+1))
    return -1

if __name__ == "__main__":
    print(open_lock(["0201","0101","0102","1212","2002"], "0202"))  # 6
    print(open_lock(["8888"], "0009"))  # 1
    print(open_lock(["8887","8889","8878","8898","8788","8988","7888","9888"], "8888"))  # -1
