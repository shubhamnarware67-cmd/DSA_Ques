"""
Q403: Minimum Deletions to Make String Balanced
================================================
Problem: String of 'a' and 'b'. Delete minimum chars so no 'b' comes
before 'a'. (All a's before all b's)

Example:
    "aababbab" -> 2
    "bbaaaaabb" -> 2
"""

def minimum_deletions(s):
    b_count = result = 0
    for c in s:
        if c == 'b':
            b_count += 1
        else:
            result = min(result + 1, b_count)
    return result

if __name__ == "__main__":
    print(minimum_deletions("aababbab"))   # 2
    print(minimum_deletions("bbaaaaabb"))  # 2
    print(minimum_deletions("aaa"))        # 0
