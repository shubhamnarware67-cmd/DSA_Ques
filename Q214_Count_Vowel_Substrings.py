"""
Q214: Count Vowel Substrings of a Word (Sliding Window)
========================================================
Problem: Count substrings that contain all 5 vowels (a,e,i,o,u)
and consist only of vowels.

Example:
    "aeiouu"   -> 2  ("aeiou","aeiouu")
    "unicorns" -> 0
    "cuaieuouac" -> 7
"""
from collections import defaultdict

def count_vowel_substrings(word):
    vowels = set('aeiou')
    count = 0
    n = len(word)
    for i in range(n):
        if word[i] not in vowels: continue
        seen = defaultdict(int)
        for j in range(i, n):
            if word[j] not in vowels: break
            seen[word[j]] += 1
            if len(seen) == 5:
                count += 1
    return count

if __name__ == "__main__":
    print(count_vowel_substrings("aeiouu"))     # 2
    print(count_vowel_substrings("unicorns"))   # 0
    print(count_vowel_substrings("cuaieuouac")) # 7
