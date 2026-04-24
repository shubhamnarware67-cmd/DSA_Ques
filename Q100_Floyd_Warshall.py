"""
Q100: Floyd-Warshall Algorithm (All Pairs Shortest Path)
==========================================================
Problem: Find shortest distances between every pair of vertices
in a weighted graph. O(V^3) time.

Example:
    graph = [[0,5,INF,10],[INF,0,3,INF],[INF,INF,0,1],[INF,INF,INF,0]]
    After Floyd-Warshall: all pairs shortest paths computed
"""

INF = float('inf')

def floyd_warshall(graph):
    V = len(graph)
    dist = [row[:] for row in graph]  # Deep copy

    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist

def print_matrix(matrix):
    for row in matrix:
        print([x if x != INF else 'INF' for x in row])

if __name__ == "__main__":
    graph = [
        [0,   5,   INF, 10],
        [INF, 0,   3,   INF],
        [INF, INF, 0,   1],
        [INF, INF, INF, 0]
    ]
    result = floyd_warshall(graph)
    print("All-pairs shortest paths:")
    print_matrix(result)
    # [[0,5,8,9],[INF,0,3,4],[INF,INF,0,1],[INF,INF,INF,0]]
