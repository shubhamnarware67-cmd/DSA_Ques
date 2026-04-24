"""
Q97: Roman to Integer
======================
Problem: Convert a Roman numeral string to an integer.
Roman: I=1, V=5, X=10, L=50, C=100, D=500, M=1000
Subtraction rules: IV=4, IX=9, XL=40, XC=90, CD=400, CM=900

Example:
    "III"    -> 3
    "LVIII"  -> 58
    "MCMXCIV" -> 1994
"""

def roman_to_int(s):
    val = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    result = 0
    for i in range(len(s)):
        if i + 1 < len(s) and val[s[i]] < val[s[i+1]]:
            result -= val[s[i]]
        else:
            result += val[s[i]]
    return result

if __name__ == "__main__":
    print(roman_to_int("III"))      # 3
    print(roman_to_int("LVIII"))    # 58
    print(roman_to_int("MCMXCIV")) # 1994
