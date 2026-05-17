"""
Q182: Shuffle the Array
========================
Problem: Given array [x1,x2,...,xn,y1,y2,...,yn], return [x1,y1,x2,y2,...,xn,yn].

Example:
    [2,5,1,3,4,7], n=3 -> [2,3,5,4,1,7]
    [1,2,3,4,4,3,2,1], n=4 -> [1,4,2,3,3,2,4,1]
"""

def shuffle(nums, n):
    return [val for pair in zip(nums[:n], nums[n:]) for val in pair]

if __name__ == "__main__":
    print(shuffle([2,5,1,3,4,7], 3))           # [2,3,5,4,1,7]
    print(shuffle([1,2,3,4,4,3,2,1], 4))       # [1,4,2,3,3,2,4,1]
