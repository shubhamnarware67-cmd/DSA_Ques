"""
Q303: Stickers to Spell Word (BFS + Bitmask)
=============================================
Problem: Use stickers (can use each sticker multiple times) to spell target.
Find minimum number of stickers. Return -1 if impossible.

Example:
    stickers=["with","example","science"], target="thehat" -> 3
    stickers=["notice","possible"], target="basicbasic" -> -1
"""
from collections import deque, Counter

def min_stickers(stickers, target):
    n = len(target)
    sticker_counts = [Counter(s) for s in stickers]
    visited = {0}
    queue = deque([(0, 0)])  # (bitmask of covered chars, steps)

    while queue:
        mask, steps = queue.popleft()
        if mask == (1 << n) - 1:
            return steps
        # Find first uncovered character
        first = -1
        for i in range(n):
            if not (mask >> i & 1):
                first = i; break
        for sc in sticker_counts:
            if target[first] not in sc:
                continue
            new_mask = mask
            sc_copy = Counter(sc)
            for i in range(n):
                if not (new_mask >> i & 1) and sc_copy[target[i]] > 0:
                    sc_copy[target[i]] -= 1
                    new_mask |= (1 << i)
            if new_mask not in visited:
                visited.add(new_mask)
                queue.append((new_mask, steps + 1))
    return -1

if __name__ == "__main__":
    print(min_stickers(["with","example","science"], "thehat"))  # 3
    print(min_stickers(["notice","possible"], "basicbasic"))      # -1
