"""
Q76: Word Break (DP)
=====================
Problem: Given a string s and a dictionary wordDict, return True if s
can be segmented into space-separated dictionary words.

Example:
    s="leetcode", wordDict=["leet","code"] -> True
    s="applepenapple", wordDict=["apple","pen"] -> True
    s="catsandog", wordDict=["cats","dog","sand","and","cat"] -> False
"""

def word_break(s, wordDict):
    word_set = set(wordDict)
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True
    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break
    return dp[n]

if __name__ == "__main__":
    print(word_break("leetcode", ["leet","code"]))         # True
    print(word_break("applepenapple", ["apple","pen"]))    # True
    print(word_break("catsandog", ["cats","dog","sand","and","cat"]))  # False
