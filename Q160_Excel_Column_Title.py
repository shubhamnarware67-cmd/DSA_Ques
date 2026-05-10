"""
Q160: Multiply Strings
=======================
Problem: Given two non-negative integers as strings, return their product
as a string. Must not convert directly to integer.

Example:
    "2" * "3"   -> "6"
    "123" * "456" -> "56088"
"""

def multiply(num1, num2):
    m, n = len(num1), len(num2)
    pos = [0] * (m + n)
    for i in range(m-1, -1, -1):
        for j in range(n-1, -1, -1):
            mul = (ord(num1[i])-48) * (ord(num2[j])-48)
            p1, p2 = i+j, i+j+1
            total = mul + pos[p2]
            pos[p2] = total % 10
            pos[p1] += total // 10
    result = ''.join(map(str, pos)).lstrip('0')
    return result or '0'

if __name__ == "__main__":
    print(multiply("2", "3"))      # "6"
    print(multiply("123", "456"))  # "56088"
    print(multiply("0", "456"))    # "0"
