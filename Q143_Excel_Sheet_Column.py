"""
Q143: Excel Sheet Column Number
=================================
Problem: Convert Excel column title to its column number.
A=1, B=2, ..., Z=26, AA=27, AB=28, ...

Example:
    "A"  -> 1
    "AB" -> 28
    "ZY" -> 701
"""

def title_to_number(columnTitle):
    result = 0
    for char in columnTitle:
        result = result * 26 + (ord(char) - ord('A') + 1)
    return result

def number_to_title(columnNumber):
    result = ""
    while columnNumber > 0:
        columnNumber -= 1
        result = chr(columnNumber % 26 + ord('A')) + result
        columnNumber //= 26
    return result

if __name__ == "__main__":
    print(title_to_number("A"))   # 1
    print(title_to_number("AB"))  # 28
    print(title_to_number("ZY"))  # 701
    print(number_to_title(28))    # "AB"
    print(number_to_title(701))   # "ZY"
