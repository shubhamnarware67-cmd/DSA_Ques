"""
Q16: Palindrome Check (String & Number)
=======================================
Problem: Check if a string/number is a palindrome.
A palindrome reads the same backward as forward.

Example:
    "racecar" -> True
    "hello"   -> False
    121       -> True
"""

def is_palindrome_string(s):
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]

def is_palindrome_number(x):
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    reversed_half = 0
    while x > reversed_half:
        reversed_half = reversed_half * 10 + x % 10
        x //= 10
    return x == reversed_half or x == reversed_half // 10

if __name__ == "__main__":
    print(is_palindrome_string("racecar"))         # True
    print(is_palindrome_string("A man a plan Panama"))  # True
    print(is_palindrome_string("hello"))           # False
    print(is_palindrome_number(121))               # True
    print(is_palindrome_number(-121))              # False
