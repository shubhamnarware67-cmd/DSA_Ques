"""
Q382: K Divisible Elements Subarrays (Hashing)
================================================
Problem: Count distinct subarrays with at most k elements divisible by p.

Example:
    nums=[2,3,3,2,2], k=2, p=2 -> 11
    nums=[1,2,3,4], k=4, p=1   -> 10
"""

def count_distinct(nums, k, p):
    n = len(nums)
    seen = set()
    for i in range(n):
        div_count = 0
        sub = []
        for j in range(i, n):
            if nums[j] % p == 0:
                div_count += 1
            if div_count > k:
                break
            sub.append(nums[j])
            seen.add(tuple(sub))
    return len(seen)

if __name__ == "__main__":
    print(count_distinct([2,3,3,2,2], 2, 2))  # 11
    print(count_distinct([1,2,3,4], 4, 1))     # 10
