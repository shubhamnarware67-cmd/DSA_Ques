"""
Q190: Fraction to Recurring Decimal
=====================================
Problem: Given numerator and denominator, return string representation
of the fraction. If repeating, put repeating part in parentheses.

Example:
    1, 2   -> "0.5"
    2, 1   -> "2"
    2, 3   -> "0.(6)"
    4, 333 -> "0.(012)"
"""

def fraction_to_decimal(numerator, denominator):
    if numerator == 0: return "0"
    sign = "-" if (numerator < 0) ^ (denominator < 0) else ""
    num, den = abs(numerator), abs(denominator)
    integer_part = num // den
    remainder = num % den
    if remainder == 0:
        return sign + str(integer_part)
    decimal_part = []
    seen = {}
    while remainder != 0:
        if remainder in seen:
            pos = seen[remainder]
            decimal_part.insert(pos, '(')
            decimal_part.append(')')
            break
        seen[remainder] = len(decimal_part)
        remainder *= 10
        decimal_part.append(str(remainder // den))
        remainder %= den
    return sign + str(integer_part) + '.' + ''.join(decimal_part)

if __name__ == "__main__":
    print(fraction_to_decimal(1, 2))    # "0.5"
    print(fraction_to_decimal(2, 1))    # "2"
    print(fraction_to_decimal(2, 3))    # "0.(6)"
    print(fraction_to_decimal(4, 333))  # "0.(012)"
