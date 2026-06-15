"""
Q302: Zuma Game (Interval DP / Memoization)
=============================================
Problem: Zuma board with colored balls. Insert balls to remove groups
of >= 3 same colored balls. Find minimum balls to insert to clear board.

Example:
    board="WRRBBW", hand="RB" -> -1
    board="WWRRBBWW", hand="WRBRW" -> 2
    board="G", hand="GGGGG" -> 2
"""
from functools import lru_cache

def find_min_step(board, hand):
    hand_count = [0] * 26
    for c in hand:
        hand_count[ord(c)-ord('A')] += 1

    @lru_cache(None)
    def dp(board, hand_tuple):
        hand = list(hand_tuple)
        if not board: return 0
        res = float('inf')
        i = 0
        while i < len(board):
            j = i
            while j < len(board) and board[j] == board[i]: j += 1
            color = ord(board[i]) - ord('A')
            need = max(0, 3 - (j - i))
            if hand[color] >= need:
                hand[color] -= need
                sub = dp(board[:i] + board[j:], tuple(hand))
                if sub != float('inf'):
                    res = min(res, need + sub)
                hand[color] += need
            i = j
        return res

    result = dp(board, tuple(hand_count))
    return result if result != float('inf') else -1

if __name__ == "__main__":
    print(find_min_step("WRRBBW", "RB"))         # -1
    print(find_min_step("WWRRBBWW", "WRBRW"))    # 2
    print(find_min_step("G", "GGGGG"))            # 2
