"""
Q452: Course Schedule IV (Floyd-Warshall / BFS)
=================================================
Problem: Given prerequisites and queries [u,v], determine if u is a
prerequisite of v (directly or indirectly).

Example:
    n=2, prereq=[[1,0]], queries=[[0,1],[1,0]] -> [False,True]
    n=3, prereq=[[1,2],[1,0],[2,0]], queries=[[1,0],[1,2]] -> [True,True]
"""

def check_if_prerequisite(numCourses, prerequisites, queries):
    reachable = [[False]*numCourses for _ in range(numCourses)]
    for u, v in prerequisites:
        reachable[u][v] = True
    for k in range(numCourses):
        for i in range(numCourses):
            for j in range(numCourses):
                if reachable[i][k] and reachable[k][j]:
                    reachable[i][j] = True
    return [reachable[u][v] for u, v in queries]

if __name__ == "__main__":
    print(check_if_prerequisite(2, [[1,0]], [[0,1],[1,0]]))  # [False, True]
    print(check_if_prerequisite(3, [[1,2],[1,0],[2,0]], [[1,0],[1,2]]))  # [True, True]
