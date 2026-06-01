"""
Q226: Reconstruct Itinerary (Hierholzer's - Eulerian Path)
============================================================
Problem: Given list of airline tickets [from,to], reconstruct itinerary
starting from "JFK". Use all tickets once. Lexicographically smallest order.

Example:
    [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
    -> ["JFK","MUC","LHR","SFO","SJC"]
"""
from collections import defaultdict

def find_itinerary(tickets):
    graph = defaultdict(list)
    for src, dst in sorted(tickets, reverse=True):
        graph[src].append(dst)

    result = []
    def dfs(airport):
        while graph[airport]:
            dfs(graph[airport].pop())
        result.append(airport)

    dfs("JFK")
    return result[::-1]

if __name__ == "__main__":
    t1 = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
    print(find_itinerary(t1))  # ["JFK","MUC","LHR","SFO","SJC"]

    t2 = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
    print(find_itinerary(t2))  # ["JFK","ATL","JFK","SFO","ATL","SFO"]
