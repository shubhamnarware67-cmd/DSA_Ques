"""
Q360: Minimum Domino Rotations For Equal Row (Greedy)
======================================================
Problem: Array of dominoes. Swap top/bottom. Find min rotations to make
all top or all bottom equal. Return -1 if impossible.

Example:
    tops=[2,1,2,4,2,2], bottoms=[5,2,6,2,3,2] -> 2
    tops=[3,5,1,2,3], bottoms=[3,6,3,3,4]      -> -1
"""

def min_domino_rotations(tops, bottoms):
    def check(val):
        rot_top = rot_bot = 0
        for t, b in zip(tops, bottoms):
            if val not in (t, b): return float('inf')
            if t != val: rot_top += 1
            if b != val: rot_bot += 1
        return min(rot_top, rot_bot)

    for candidate in [tops[0], bottoms[0]]:
        result = check(candidate)
        if result != float('inf'):
            return result
    return -1

if __name__ == "__main__":
    print(min_domino_rotations([2,1,2,4,2,2],[5,2,6,2,3,2]))  # 2
    print(min_domino_rotations([3,5,1,2,3],[3,6,3,3,4]))       # -1
