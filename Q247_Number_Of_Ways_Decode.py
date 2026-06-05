"""
Q247: Number of Ways to Decode (Star variant with '*')
=======================================================
Problem: '*' can represent digits 1-9. Count decoding ways modulo 10^9+7.

Example:
    "*"   -> 9   ('*' = 1..9)
    "1*"  -> 18  ('11'-'19' = 9 ways, plus '1','*' separately)
    "2*"  -> 15  ('21'-'26' = 6 ways + '2','*'=9 ways)
"""

def num_decodings_star(s):
    MOD = 10**9 + 7
    n = len(s)
    dp = [0] * (n+1)
    dp[0] = 1
    dp[1] = 9 if s[0]=='*' else (0 if s[0]=='0' else 1)
    for i in range(2, n+1):
        c, p = s[i-1], s[i-2]
        if c == '*': dp[i] = 9 * dp[i-1]
        elif c != '0': dp[i] = dp[i-1]
        if p == '*' and c == '*': dp[i] = (dp[i] + 15*dp[i-2]) % MOD
        elif p == '*': dp[i] = (dp[i] + (2 if c<='6' else 1)*dp[i-2]) % MOD
        elif c == '*': dp[i] = (dp[i] + (9 if p=='1' else 6 if p=='2' else 0)*dp[i-2]) % MOD
        elif p == '1' or (p == '2' and c <= '6'): dp[i] = (dp[i]+dp[i-2]) % MOD
    return dp[n]

if __name__ == "__main__":
    print(num_decodings_star("*"))   # 9
    print(num_decodings_star("1*"))  # 18
    print(num_decodings_star("2*"))  # 15
