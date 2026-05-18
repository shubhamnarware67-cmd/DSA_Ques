"""
Q185: Number of Steps to Reduce to Zero
=========================================
Problem: Given integer num, return number of steps to reduce to zero.
If even: divide by 2. If odd: subtract 1.

Example:
    14 -> 6
    8  -> 4
    123 -> 12
"""

def number_of_steps(num):
    steps = 0
    while num > 0:
        if num % 2 == 0:
            num //= 2
        else:
            num -= 1
        steps += 1
    return steps

# Bit manipulation approach
def number_of_steps_bits(num):
    if num == 0: return 0
    binary = bin(num)[2:]
    # Steps = (bits - 1) shifts + number of 1-bits subtractions
    return len(binary) - 1 + binary.count('1')

if __name__ == "__main__":
    print(number_of_steps(14))       # 6
    print(number_of_steps_bits(8))   # 4
    print(number_of_steps(123))      # 12
