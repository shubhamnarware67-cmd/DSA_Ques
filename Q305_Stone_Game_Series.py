"""
Q305: Stone Game (Various Variants)
=====================================
Problem I: Two players take from ends. Alex first. Does Alex always win?
Problem II: M changes. Maximize stones for player.
Problem III: Take 1,2, or 3 piles. Maximize score.

Example I:  [5,3,4,5] -> True
Example II: piles=[2,7,9,4,4], M=1 -> 10
Example III: [1,2,3,7] -> False (second player wins)
"""

def stone_game_i(piles):
    # Math: first player always wins with even array
    return True

def stone_game_ii(piles):
    n = len(piles)
    suffix = [0] * (n+1)
    for i in range(n-1, -1, -1):
        suffix[i] = suffix[i+1] + piles[i]
    from functools import lru_cache
    @lru_cache(None)
    def dp(i, M):
        if i + 2*M >= n: return suffix[i]
        best = 0
        for x in range(1, 2*M+1):
            best = max(best, suffix[i] - dp(i+x, max(M, x)))
        return best
    return dp(0, 1)

def stone_game_iii(stoneValue):
    n = len(stoneValue)
    dp = [float('-inf')] * (n+1)
    dp[n] = 0
    for i in range(n-1, -1, -1):
        total = 0
        for k in range(1, 4):
            if i+k <= n:
                total += stoneValue[i+k-1]
                dp[i] = max(dp[i], total - dp[i+k])
    return "First" if dp[0] > 0 else "Second" if dp[0] < 0 else "Tie"

if __name__ == "__main__":
    print(stone_game_i([5,3,4,5]))           # True
    print(stone_game_ii([2,7,9,4,4]))        # 10
    print(stone_game_iii([1,2,3,7]))         # "Second"
    print(stone_game_iii([1,2,3,-9]))        # "First"
