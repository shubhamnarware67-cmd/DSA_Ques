"""
Q338: Find Missing Ranges
===========================
Problem: Given sorted array and range [lower, upper], return missing ranges.

Example:
    nums=[0,1,3,50,75], lower=0, upper=99 -> ["2","4->49","51->74","76->99"]
    nums=[], lower=1, upper=1 -> ["1"]
"""

def find_missing_ranges(nums, lower, upper):
    result = []

    def add_range(lo, hi):
        if lo == hi: result.append(str(lo))
        else: result.append(f"{lo}->{hi}")

    prev = lower - 1
    for num in nums + [upper + 1]:
        if num - prev >= 2:
            add_range(prev + 1, num - 1)
        prev = num
    return result

if __name__ == "__main__":
    print(find_missing_ranges([0,1,3,50,75], 0, 99))
    # ["2","4->49","51->74","76->99"]
    print(find_missing_ranges([], 1, 1))  # ["1"]
    print(find_missing_ranges([-1], -2, -1))  # ["-2"]
