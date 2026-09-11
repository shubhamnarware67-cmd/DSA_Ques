"""
Q436: Cracking the Safe (De Bruijn Sequence / Hierholzer)
============================================================
Problem: Find shortest string that contains every possible password
of length n using digits 0..k-1 as a substring.

Example:
    n=1, k=2 -> "10" or "01"
    n=2, k=2 -> "0110" or similar
"""

def crack_safe(n, k):
    seen = set()
    result = []
    start = '0' * n

    def dfs(node):
        for digit in map(str, range(k)):
            nxt = node + digit
            if nxt not in seen:
                seen.add(nxt)
                dfs(nxt[1:])
                result.append(digit)

    dfs(start)
    return ''.join(result) + start

if __name__ == "__main__":
    print(crack_safe(1, 2))  # "10" or "01"
    print(crack_safe(2, 2))  # length 4 + 1 = 5
