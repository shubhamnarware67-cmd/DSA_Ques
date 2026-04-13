"""
Q45: String Compression
========================
Problem: Given an array of characters, compress it using run-length encoding.
e.g., "aabcccccaaa" -> "a2b1c5a3" or just "a2bc5a3"

Example:
    ['a','a','b','b','c','c','c'] -> ['a','2','b','2','c','3'], returns 6
"""

def compress(chars):
    write = anchor = 0
    for read in range(len(chars)):
        if read + 1 == len(chars) or chars[read+1] != chars[read]:
            chars[write] = chars[anchor]
            write += 1
            count = read - anchor + 1
            if count > 1:
                for c in str(count):
                    chars[write] = c
                    write += 1
            anchor = read + 1
    return write

if __name__ == "__main__":
    chars = ['a','a','b','b','c','c','c']
    length = compress(chars)
    print(chars[:length])  # ['a','2','b','2','c','3']
    print(length)          # 6
