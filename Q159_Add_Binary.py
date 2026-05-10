"""
Q159: Add Binary
=================
Problem: Given two binary strings a and b, return their sum as a binary string.

Example:
    a="11", b="1"   -> "100"
    a="1010", b="1011" -> "10101"
"""

def add_binary(a, b):
    result = []
    carry = 0
    i, j = len(a)-1, len(b)-1
    while i >= 0 or j >= 0 or carry:
        bit_a = int(a[i]) if i >= 0 else 0
        bit_b = int(b[j]) if j >= 0 else 0
        total = bit_a + bit_b + carry
        carry, bit = divmod(total, 2)
        result.append(str(bit))
        i -= 1; j -= 1
    return ''.join(reversed(result))

if __name__ == "__main__":
    print(add_binary("11", "1"))        # "100"
    print(add_binary("1010", "1011"))   # "10101"
