"""
Q356: Count Number of Homogeneous Substrings
=============================================
Problem: A string is homogeneous if all characters are the same.
Count total homogeneous substrings (mod 10^9+7).

Example:
    "abbcccaa" -> 13
    "xy"       -> 2
    "zzzzz"    -> 15
"""

def count_homogeneous(s):
    MOD = 10**9 + 7
    result = 0
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            result += count * (count + 1) // 2
            count = 1
    result += count * (count + 1) // 2
    return result % MOD

if __name__ == "__main__":
    print(count_homogeneous("abbcccaa"))  # 13
    print(count_homogeneous("xy"))        # 2
    print(count_homogeneous("zzzzz"))     # 15
