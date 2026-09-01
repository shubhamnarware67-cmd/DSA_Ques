"""
Q433: Stamping the Sequence (Greedy Reverse Simulation)
=========================================================
Problem: Stamp s onto target (?????) replacing substring matches.
Find order of stamps to build target. Reverse: replace target chars
matching stamp with '?'.

Example:
    stamp="abc", target="ababc" -> [0,2]
    stamp="abca", target="aabcaca" -> [3,0,1]
"""

def moves_to_stamp(stamp, target):
    n, m = len(stamp), len(target)
    target = list(target)
    result = []
    stamped = [False] * m
    total_stamped = 0

    def can_stamp(pos):
        changed = False
        for i in range(n):
            if target[pos+i] == '?': continue
            if target[pos+i] != stamp[i]: return -1
            changed = True
        return changed

    def do_stamp(pos):
        cnt = 0
        for i in range(n):
            if target[pos+i] != '?':
                target[pos+i] = '?'
                cnt += 1
        return cnt

    while total_stamped < m:
        stamped_this_round = False
        for i in range(m - n + 1):
            if stamped[i]: continue
            res = can_stamp(i)
            if res == -1: continue
            cnt = do_stamp(i)
            if cnt > 0:
                total_stamped += cnt
                result.append(i)
                stamped[i] = True
                stamped_this_round = True
        if not stamped_this_round:
            return []
    return result[::-1]

if __name__ == "__main__":
    print(moves_to_stamp("abc", "ababc"))      # [0,2] or similar
    print(moves_to_stamp("abca", "aabcaca"))   # [3,0,1] or similar
