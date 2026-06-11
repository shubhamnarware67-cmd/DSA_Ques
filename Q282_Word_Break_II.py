"""
Q282: Word Break II (Backtracking + Memoization)
=================================================
Problem: Given string and word dictionary, return all possible
sentences by breaking s into dictionary words.

Example:
    s="catsanddog", wordDict=["cat","cats","and","sand","dog"]
    -> ["cats and dog","cat sand dog"]
"""

def word_break_ii(s, wordDict):
    word_set = set(wordDict)
    memo = {}

    def backtrack(start):
        if start in memo: return memo[start]
        if start == len(s): return ['']
        results = []
        for end in range(start+1, len(s)+1):
            word = s[start:end]
            if word in word_set:
                for rest in backtrack(end):
                    results.append(word + (' ' + rest if rest else ''))
        memo[start] = results
        return results

    return backtrack(0)

if __name__ == "__main__":
    print(word_break_ii("catsanddog", ["cat","cats","and","sand","dog"]))
    # ["cats and dog","cat sand dog"]
    print(word_break_ii("pineapplepenapple", ["apple","pen","applepen","pine","pineapple"]))
    # ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
