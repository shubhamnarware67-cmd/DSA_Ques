"""
Q145: Isomorphic Strings
==========================
Problem: Two strings s and t are isomorphic if characters in s can be
replaced to get t (preserving order, one-to-one mapping).

Example:
    "egg", "add"  -> True  (e->a, g->d)
    "foo", "bar"  -> False (o maps to both a and r)
    "paper", "title" -> True
"""

def is_isomorphic(s, t):
    s_to_t = {}
    t_to_s = {}
    for cs, ct in zip(s, t):
        if cs in s_to_t and s_to_t[cs] != ct: return False
        if ct in t_to_s and t_to_s[ct] != cs: return False
        s_to_t[cs] = ct
        t_to_s[ct] = cs
    return True

if __name__ == "__main__":
    print(is_isomorphic("egg", "add"))    # True
    print(is_isomorphic("foo", "bar"))    # False
    print(is_isomorphic("paper","title")) # True
