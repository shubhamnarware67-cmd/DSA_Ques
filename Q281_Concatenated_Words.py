"""
Q281: Concatenated Words (DP + Trie)
======================================
Problem: Given list of words, find all words that can be formed by
concatenating two or more other words from the list.

Example:
    ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatsratdog"]
    -> ["catsdogcats","dogcatsdog","ratcatsratdog"]
"""

def find_all_concatenated_words(words):
    word_set = set(words)
    memo = {}

    def can_form(word):
        if word in memo: return memo[word]
        for i in range(1, len(word)):
            prefix = word[:i]
            suffix = word[i:]
            if prefix in word_set and (suffix in word_set or can_form(suffix)):
                memo[word] = True
                return True
        memo[word] = False
        return False

    return [w for w in words if can_form(w)]

if __name__ == "__main__":
    words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatsratdog"]
    print(find_all_concatenated_words(words))
    # ["catsdogcats","dogcatsdog","ratcatsratdog"]
