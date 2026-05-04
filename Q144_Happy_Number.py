"""
Q144: Happy Number
===================
Problem: Starting with any positive integer, replace the number by the
sum of squares of its digits, and repeat until 1 (happy) or cycle.

Example:
    19 -> 1^2+9^2=82 -> 8^2+2^2=68 -> ... -> 1  (True)
    2  -> cycle (False)
"""

def is_happy(n):
    def get_next(num):
        return sum(int(d)**2 for d in str(num))
    slow = fast = n
    while True:
        slow = get_next(slow)
        fast = get_next(get_next(fast))
        if fast == 1: return True
        if slow == fast: return False

if __name__ == "__main__":
    print(is_happy(19))  # True
    print(is_happy(2))   # False
    print(is_happy(1))   # True
