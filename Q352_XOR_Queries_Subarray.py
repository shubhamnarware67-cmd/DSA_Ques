"""
Q352: XOR Queries of a Subarray (Prefix XOR)
=============================================
Problem: For each query [l,r], return XOR of elements from index l to r.

Example:
    arr=[1,3,4,8], queries=[[0,1],[1,2],[0,3],[3,3]]
    -> [2,7,14,8]
"""

def xor_queries(arr, queries):
    prefix = [0] * (len(arr) + 1)
    for i, v in enumerate(arr):
        prefix[i+1] = prefix[i] ^ v
    return [prefix[r+1] ^ prefix[l] for l, r in queries]

if __name__ == "__main__":
    print(xor_queries([1,3,4,8], [[0,1],[1,2],[0,3],[3,3]]))  # [2,7,14,8]
    print(xor_queries([4,8,2,10], [[2,3],[1,3],[0,0],[0,3]]))  # [8,10,4,4]
