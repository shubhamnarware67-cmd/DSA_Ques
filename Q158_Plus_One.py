"""
Q158: Plus One
===============
Problem: Given large integer as digit array, increment by one.

Example:
    [1,2,3] -> [1,2,4]
    [9]     -> [1,0]
    [9,9]   -> [1,0,0]
"""

def plus_one(digits):
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    return [1] + digits

if __name__ == "__main__":
    print(plus_one([1,2,3]))  # [1,2,4]
    print(plus_one([9]))      # [1,0]
    print(plus_one([9,9]))    # [1,0,0]
    print(plus_one([1,9,9]))  # [2,0,0]
