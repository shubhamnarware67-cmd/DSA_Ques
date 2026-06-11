"""
Q280: Freedom Trail (DP)
==========================
Problem: Circular ring with characters. Rotate to align characters to spell
key. Each rotation and button press costs 1 step. Find minimum steps.

Example:
    ring="godding", key="gd" -> 4
    ring="godding", key="godding" -> 13
"""
from functools import lru_cache

def find_rotate_steps(ring, key):
    n, m = len(ring), len(key)
    char_pos = {}
    for i, c in enumerate(ring):
        char_pos.setdefault(c, []).append(i)

    @lru_cache(None)
    def dp(ki, ri):
        if ki == m: return 0
        best = float('inf')
        for pos in char_pos[key[ki]]:
            diff = abs(pos - ri)
            step = min(diff, n - diff)
            best = min(best, step + 1 + dp(ki+1, pos))
        return best

    return dp(0, 0)

if __name__ == "__main__":
    print(find_rotate_steps("godding", "gd"))       # 4
    print(find_rotate_steps("godding", "godding"))  # 13
