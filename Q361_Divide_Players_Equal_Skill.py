"""
Q361: Divide Players Into Teams of Equal Skill (Two Pointers)
==============================================================
Problem: Divide even-length array into n/2 pairs with equal sum.
Return sum of products of each pair, or -1 if impossible.

Example:
    [3,2,5,1,3,4] -> 22  (pairs: [1,5],[2,4],[3,3]; products: 5+8+9=22)
    [3,4]          -> 12
    [1,1,2,3]      -> -1
"""

def divide_players(skill):
    skill.sort()
    n = len(skill)
    target = skill[0] + skill[-1]
    result = 0
    for i in range(n // 2):
        if skill[i] + skill[n-1-i] != target:
            return -1
        result += skill[i] * skill[n-1-i]
    return result

if __name__ == "__main__":
    print(divide_players([3,2,5,1,3,4]))  # 22
    print(divide_players([3,4]))           # 12
    print(divide_players([1,1,2,3]))       # -1
