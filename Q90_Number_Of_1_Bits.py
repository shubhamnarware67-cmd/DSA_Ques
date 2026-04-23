"""
Q90: Number of 1 Bits (Hamming Weight)
========================================
Problem: Given unsigned integer, return number of '1' bits (Hamming weight).

Example:
    11   (binary: 00000000000000000000000000001011) -> 3
    128  (binary: 00000000000000000000000010000000) -> 1
"""

def hamming_weight(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count

def hamming_weight_trick(n):
    count = 0
    while n:
        n &= n - 1  # Clears lowest set bit
        count += 1
    return count

if __name__ == "__main__":
    print(hamming_weight(11))         # 3
    print(hamming_weight_trick(128))  # 1
    print(hamming_weight(4294967293)) # 31
