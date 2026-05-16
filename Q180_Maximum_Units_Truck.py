"""
Q180: Maximum Units on a Truck (Greedy)
=========================================
Problem: Given boxTypes[i]=[numberOfBoxes, numberOfUnitsPerBox] and
truck size, maximize total units loaded.

Example:
    boxTypes=[[1,3],[2,2],[3,1]], truckSize=4 -> 8
    (1 box of 3 + 2 boxes of 2 + 1 box of 1 = 3+4+1=8)
"""

def maximum_units(boxTypes, truckSize):
    boxTypes.sort(key=lambda x: -x[1])  # Sort by units descending
    total_units = 0
    for boxes, units in boxTypes:
        take = min(boxes, truckSize)
        total_units += take * units
        truckSize -= take
        if truckSize == 0:
            break
    return total_units

if __name__ == "__main__":
    print(maximum_units([[1,3],[2,2],[3,1]], 4))   # 8
    print(maximum_units([[5,10],[2,5],[4,7],[3,9]], 10))  # 91
