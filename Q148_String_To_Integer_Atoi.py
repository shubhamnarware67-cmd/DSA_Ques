"""
Q148: String to Integer (atoi)
================================
Problem: Implement atoi which converts a string to a 32-bit signed integer.
Handle: leading whitespace, optional +/- sign, digits, non-digit stop.

Example:
    "42"           -> 42
    "   -42"       -> -42
    "4193 with words" -> 4193
    "words and 987"   -> 0
"""

def my_atoi(s):
    s = s.lstrip()
    if not s: return 0
    sign = 1
    i = 0
    if s[0] in '+-':
        sign = -1 if s[0] == '-' else 1
        i = 1
    result = 0
    while i < len(s) and s[i].isdigit():
        result = result * 10 + int(s[i])
        i += 1
    result *= sign
    INT_MAX, INT_MIN = 2**31 - 1, -(2**31)
    return max(INT_MIN, min(INT_MAX, result))

if __name__ == "__main__":
    print(my_atoi("42"))              # 42
    print(my_atoi("   -42"))          # -42
    print(my_atoi("4193 with words")) # 4193
    print(my_atoi("words and 987"))   # 0
