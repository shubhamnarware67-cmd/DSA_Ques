"""
Q153: Ransom Note
==================
Problem: Given ransomNote and magazine strings, return True if you
can construct ransomNote using letters from magazine (each letter used once).

Example:
    ransomNote="a",  magazine="b"   -> False
    ransomNote="aa", magazine="ab"  -> False
    ransomNote="aa", magazine="aab" -> True
"""
from collections import Counter

def can_construct(ransomNote, magazine):
    mag_count = Counter(magazine)
    for ch in ransomNote:
        if mag_count[ch] <= 0:
            return False
        mag_count[ch] -= 1
    return True

if __name__ == "__main__":
    print(can_construct("a", "b"))    # False
    print(can_construct("aa", "ab"))  # False
    print(can_construct("aa", "aab")) # True
