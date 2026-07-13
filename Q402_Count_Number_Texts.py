"""
Q402: Count Number of Texts (DP)
==================================
Problem: Phone keypad. Keys 2-9 map to letters. Messages are pressed
in groups. Count possible text messages from digit string.
2,3,4,5,6,8 have 3 letters; 7,9 have 4 letters.

Example:
    "22233" -> 8
    "222222222222222222222222222222222222" -> 82876089
"""

def count_texts(pressedKeys):
    MOD = 10**9 + 7
    n = len(pressedKeys)
    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        c = pressedKeys[i-1]
        max_rep = 4 if c in '79' else 3
        for k in range(1, max_rep + 1):
            if i >= k and pressedKeys[i-k:i] == c * k:
                dp[i] = (dp[i] + dp[i-k]) % MOD
            else:
                break
    return dp[n]

if __name__ == "__main__":
    print(count_texts("22233"))   # 8
    print(count_texts("222222222222222222222222222222222222"))  # 82876089
