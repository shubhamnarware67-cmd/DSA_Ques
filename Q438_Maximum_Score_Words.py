"""
Q438: Maximum Score Words Formed by Letters (Bitmask DP)
==========================================================
Problem: Given words, letters (available), and score per letter, find
max score by choosing subset of words (each letter used at most once total).

Example:
    words=["dog","cat","dad","good"], letters=["a","a","c","d","d","d","g","o","o"],
    score=[1,0,9,5,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    -> 23
"""
from collections import Counter

def max_score_words(words, letters, score):
    letter_count = Counter(letters)

    def word_score(word):
        c = Counter(word)
        for ch, cnt in c.items():
            if c[ch] > letter_count.get(ch, 0):
                return None
        return sum(score[ord(ch)-ord('a')] * cnt for ch, cnt in c.items())

    n = len(words)
    best = 0
    for mask in range(1 << n):
        used = Counter()
        total = 0
        valid = True
        for i in range(n):
            if mask & (1 << i):
                used.update(words[i])
        for ch, cnt in used.items():
            if cnt > letter_count.get(ch, 0):
                valid = False; break
            total += score[ord(ch)-ord('a')] * cnt
        if valid:
            best = max(best, total)
    return best

if __name__ == "__main__":
    words = ["dog","cat","dad","good"]
    letters = ["a","a","c","d","d","d","g","o","o"]
    score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    print(max_score_words(words, letters, score))  # 23
