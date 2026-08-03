"""
Q420: Smallest Missing Genetic Value in Each Subtree (DSU + Tracking)
========================================================================
Problem: Tree with genetic values nums[i]. For each node, find smallest
missing positive integer in its subtree's genetic values.

Example:
    parents=[-1,0,0,2], nums=[1,2,3,4] -> [5,1,1,1]
    parents=[-1,0,1,0,3,3], nums=[5,4,6,2,1,3] -> [1,1,1,1,1,1]
"""

def smallest_missing_value_subtree(parents, nums):
    n = len(parents)
    result = [1] * n
    children = [[] for _ in range(n)]
    for i in range(1, n):
        children[parents[i]].append(i)

    # Find node with value 1
    node_with_1 = -1
    for i in range(n):
        if nums[i] == 1:
            node_with_1 = i
            break
    if node_with_1 == -1:
        return result  # All are 1 (default)

    visited = set()
    seen_values = set()
    missing = 1
    node = node_with_1
    prev = -1
    while node != -1:
        # DFS to collect all values in subtree of node (excluding prev branch)
        stack = [node]
        while stack:
            curr = stack.pop()
            if curr in visited: continue
            visited.add(curr)
            seen_values.add(nums[curr])
            for child in children[curr]:
                if child != prev:
                    stack.append(child)
        while missing in seen_values:
            missing += 1
        result[node] = missing
        prev = node
        node = parents[node]
    return result

if __name__ == "__main__":
    print(smallest_missing_value_subtree([-1,0,0,2], [1,2,3,4]))  # [5,1,1,1]
    print(smallest_missing_value_subtree([-1,0,1,0,3,3], [5,4,6,2,1,3]))  # [1,1,1,1,1,1]
