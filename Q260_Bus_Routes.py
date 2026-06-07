"""
Q260: Bus Routes (BFS on Stops)
=================================
Problem: Each route is a bus loop. Find min number of buses to travel
from source to target stop.

Example:
    routes=[[1,2,7],[3,6,7]], source=1, target=6 -> 2
    routes=[[7,12],[4,5,15],[6],[15,19],[9,12,13]], source=15, target=12 -> -1
"""
from collections import defaultdict, deque

def num_buses_to_destination(routes, source, target):
    if source == target: return 0
    stop_to_routes = defaultdict(set)
    for i, route in enumerate(routes):
        for stop in route:
            stop_to_routes[stop].add(i)

    visited_stops = {source}
    visited_routes = set()
    queue = deque([(source, 0)])

    while queue:
        stop, buses = queue.popleft()
        for route_id in stop_to_routes[stop]:
            if route_id in visited_routes: continue
            visited_routes.add(route_id)
            for next_stop in routes[route_id]:
                if next_stop == target: return buses + 1
                if next_stop not in visited_stops:
                    visited_stops.add(next_stop)
                    queue.append((next_stop, buses + 1))
    return -1

if __name__ == "__main__":
    print(num_buses_to_destination([[1,2,7],[3,6,7]], 1, 6))  # 2
    print(num_buses_to_destination([[7,12],[4,5,15],[6],[15,19],[9,12,13]], 15, 12))  # -1
