"""
Q246: Suffix Array (O(n log² n))
==================================
Problem: Build suffix array — sorted array of all suffixes of a string.
Used in string processing, pattern matching, LCP computation.

Example:
    s="banana"
    Suffixes sorted: ["a","ana","anana","banana","na","nana"]
    Suffix Array: [5,3,1,0,4,2]
"""

def build_suffix_array(s):
    n = len(s)
    # Build (rank, index) pairs
    suffixes = sorted(range(n), key=lambda i: s[i:])
    return suffixes

def search_pattern(s, sa, pattern):
    """Binary search on suffix array"""
    lo, hi = 0, len(sa)
    while lo < hi:
        mid = (lo+hi)//2
        if s[sa[mid]:sa[mid]+len(pattern)] < pattern: lo = mid+1
        else: hi = mid
    start = lo
    while lo < len(sa) and s[sa[lo]:sa[lo]+len(pattern)] == pattern: lo+=1
    return sa[start:lo]

if __name__ == "__main__":
    s = "banana"
    sa = build_suffix_array(s)
    print("Suffix Array:", sa)  # [5,3,1,0,4,2]
    print("Suffixes:", [s[i:] for i in sa])
    print("Pattern 'ana' at:", sorted(search_pattern(s, sa, "ana")))  # [1,3]
