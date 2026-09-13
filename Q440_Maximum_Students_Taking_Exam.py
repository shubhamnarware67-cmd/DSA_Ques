"""
Q440: Maximum Students Taking Exam (Bitmask DP)
==================================================
Problem: Classroom seats with broken seats ('#'). Student cheating possible
if adjacent left/right/diagonal occupied. Maximize seated students.

Example:
    [[".",".","#",".",".","."],
     [".","#",".",".",".","#"],
     [".",".",".",".","#","."]]
    -> 4
"""

def max_students(seats):
    m, n = len(seats), len(seats[0])
    valid_masks = []
    for row in seats:
        mask = 0
        for j, c in enumerate(row):
            if c == '.':
                mask |= 1 << j
        valid_masks.append(mask)

    def no_adjacent(mask):
        return (mask & (mask << 1)) == 0

    from functools import lru_cache

    @lru_cache(None)
    def dp(row, prev_mask):
        if row == m: return 0
        best = dp(row+1, 0)  # Skip this row entirely
        full = valid_masks[row]
        sub = full
        while True:
            if no_adjacent(sub) and (sub & (prev_mask << 1)) == 0 and (sub & (prev_mask >> 1)) == 0:
                count = bin(sub).count('1')
                best = max(best, count + dp(row+1, sub))
            if sub == 0: break
            sub = (sub - 1) & full
        return best

    return dp(0, 0)

if __name__ == "__main__":
    seats = [[".",".","#",".",".","."],
             [".","#",".",".",".","#"],
             [".",".",".",".","#","."]]
    print(max_students(seats))  # 4
