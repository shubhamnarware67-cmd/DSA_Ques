"""
Q321: Frog Jump (DP + HashSet)
================================
Problem: Frog crosses river on stones. From stone k jumped with step s,
next jump can be s-1, s, or s+1. Can frog reach last stone?

Example:
    [0,1,3,5,6,8,12,17] -> True
    [0,1,2,3,4,8,9,11]  -> False
"""

def can_cross(stones):
    stone_set = set(stones)
    memo = {}

    def can_reach(pos, speed):
        if (pos, speed) in memo: return memo[(pos, speed)]
        if pos == stones[-1]: return True
        for s in [speed-1, speed, speed+1]:
            if s > 0 and pos+s in stone_set:
                if can_reach(pos+s, s):
                    memo[(pos, speed)] = True
                    return True
        memo[(pos, speed)] = False
        return False

    return can_reach(0, 0)

if __name__ == "__main__":
    print(can_cross([0,1,3,5,6,8,12,17]))  # True
    print(can_cross([0,1,2,3,4,8,9,11]))   # False
