"""
Q66: Course Schedule (Cycle Detection in Directed Graph)
=========================================================
Problem: There are numCourses labeled 0 to n-1. prerequisites[i]=[a,b]
means you must take b before a. Return True if you can finish all courses.

Example:
    numCourses=2, prerequisites=[[1,0]]       -> True
    numCourses=2, prerequisites=[[1,0],[0,1]] -> False (cycle)
"""
from collections import deque

def can_finish(numCourses, prerequisites):
    graph = [[] for _ in range(numCourses)]
    in_degree = [0] * numCourses
    for a, b in prerequisites:
        graph[b].append(a)
        in_degree[a] += 1
    queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
    taken = 0
    while queue:
        course = queue.popleft()
        taken += 1
        for nxt in graph[course]:
            in_degree[nxt] -= 1
            if in_degree[nxt] == 0:
                queue.append(nxt)
    return taken == numCourses

if __name__ == "__main__":
    print(can_finish(2, [[1,0]]))          # True
    print(can_finish(2, [[1,0],[0,1]]))    # False
    print(can_finish(4, [[1,0],[2,1],[3,2]])) # True
