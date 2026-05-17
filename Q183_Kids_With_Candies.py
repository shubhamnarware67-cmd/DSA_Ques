"""
Q183: Kids With the Greatest Number of Candies
================================================
Problem: Given candies array and extraCandies, return boolean array where
result[i] = True if kid i can have greatest number after getting extraCandies.

Example:
    candies=[2,3,5,1,3], extraCandies=3
    -> [True,True,True,False,True]
"""

def kids_with_candies(candies, extraCandies):
    max_candies = max(candies)
    return [c + extraCandies >= max_candies for c in candies]

if __name__ == "__main__":
    print(kids_with_candies([2,3,5,1,3], 3))   # [True,True,True,False,True]
    print(kids_with_candies([4,2,1,1,2], 1))   # [True,False,False,False,False]
