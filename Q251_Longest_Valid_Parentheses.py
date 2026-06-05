"""
Q251: Longest Valid Parentheses (Stack/DP)
==========================================
Problem: Given string of '(' and ')', find length of longest valid
(well-formed) parentheses substring.

Example:
    "(()"    -> 2
    ")()())" -> 4
    ""       -> 0
"""

def longest_valid_parentheses(s):
    stack = [-1]
    max_len = 0
    for i, ch in enumerate(s):
        if ch == '(':
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                max_len = max(max_len, i - stack[-1])
    return max_len

def longest_valid_dp(s):
    n = len(s)
    dp = [0] * n
    for i in range(1, n):
        if s[i] == ')':
            if s[i-1] == '(':
                dp[i] = (dp[i-2] if i >= 2 else 0) + 2
            elif dp[i-1] > 0:
                j = i - dp[i-1] - 1
                if j >= 0 and s[j] == '(':
                    dp[i] = dp[i-1] + 2 + (dp[j-1] if j >= 1 else 0)
    return max(dp) if dp else 0

if __name__ == "__main__":
    print(longest_valid_parentheses("(()"))    # 2
    print(longest_valid_parentheses(")()())")) # 4
    print(longest_valid_dp("()(()"))           # 4
