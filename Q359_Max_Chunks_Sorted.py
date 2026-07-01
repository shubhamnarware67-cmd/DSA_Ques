"""
Q359: Max Chunks To Make Sorted (I & II)
==========================================
Problem I: Array is permutation of [0..n-1]. Max chunks to sort independently.
Problem II: General array. Max chunks to sort independently.

Example I:  [4,3,2,1,0] -> 1,  [1,0,2,3,4] -> 4
Example II: [5,4,3,2,1] -> 1,  [2,1,3,4,4] -> 4
"""

def max_chunks_to_sorted_i(arr):
    chunks = 0
    max_val = 0
    for i, v in enumerate(arr):
        max_val = max(max_val, v)
        if max_val == i:  # Everything so far fits in [0..i]
            chunks += 1
    return chunks

def max_chunks_to_sorted_ii(arr):
    # Use monotonic stack
    stack = []
    for v in arr:
        max_val = v
        while stack and stack[-1] > v:
            max_val = max(max_val, stack.pop())
        stack.append(max_val)
    return len(stack)

if __name__ == "__main__":
    print(max_chunks_to_sorted_i([4,3,2,1,0]))  # 1
    print(max_chunks_to_sorted_i([1,0,2,3,4]))  # 4
    print(max_chunks_to_sorted_ii([5,4,3,2,1])) # 1
    print(max_chunks_to_sorted_ii([2,1,3,4,4])) # 4
