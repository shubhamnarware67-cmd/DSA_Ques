"""
Q79: Gas Station (Greedy)
===========================
Problem: There are n gas stations. gas[i] is fuel at station i, cost[i]
is fuel to travel to next. Find starting station index to complete circuit,
or -1 if impossible.

Example:
    gas=[1,2,3,4,5], cost=[3,4,5,1,2] -> 3
"""

def can_complete_circuit(gas, cost):
    total = tank = start = 0
    for i in range(len(gas)):
        diff = gas[i] - cost[i]
        total += diff
        tank += diff
        if tank < 0:
            start = i + 1
            tank = 0
    return start if total >= 0 else -1

if __name__ == "__main__":
    print(can_complete_circuit([1,2,3,4,5],[3,4,5,1,2]))  # 3
    print(can_complete_circuit([2,3,4],[3,4,3]))           # -1
