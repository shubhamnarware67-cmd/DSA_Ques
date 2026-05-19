"""
Q191: Find the Celebrity
==========================
Problem: Among n people, find if a celebrity exists: everyone knows the
celebrity, but the celebrity knows no one. Use knows(a,b) API minimally.

Example:
    n=3, relations=[[1,0],[2,0]] -> 0 (person 0 is the celebrity)
"""

def find_celebrity(n, knows_matrix):
    def knows(a, b):
        return knows_matrix[a][b]

    # Find candidate
    candidate = 0
    for i in range(1, n):
        if knows(candidate, i):
            candidate = i
    # Verify candidate
    for i in range(n):
        if i == candidate: continue
        if knows(candidate, i) or not knows(i, candidate):
            return -1
    return candidate

if __name__ == "__main__":
    # Person 0 is celebrity: everyone knows 0, 0 knows no one
    matrix = [[0,0,0],[1,0,1],[1,0,0]]
    print(find_celebrity(3, matrix))  # 0

    # No celebrity
    matrix2 = [[0,1,0],[1,0,0],[0,1,0]]
    print(find_celebrity(3, matrix2))  # -1
