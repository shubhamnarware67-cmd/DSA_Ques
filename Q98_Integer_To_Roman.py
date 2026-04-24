"""
Q98: Integer to Roman
======================
Problem: Convert an integer to its Roman numeral representation.

Example:
    3    -> "III"
    58   -> "LVIII"
    1994 -> "MCMXCIV"
"""

def int_to_roman(num):
    vals = [(1000,'M'),(900,'CM'),(500,'D'),(400,'CD'),
            (100,'C'),(90,'XC'),(50,'L'),(40,'XL'),
            (10,'X'),(9,'IX'),(5,'V'),(4,'IV'),(1,'I')]
    result = ""
    for v, symbol in vals:
        while num >= v:
            result += symbol
            num -= v
    return result

if __name__ == "__main__":
    print(int_to_roman(3))     # "III"
    print(int_to_roman(58))    # "LVIII"
    print(int_to_roman(1994))  # "MCMXCIV"
