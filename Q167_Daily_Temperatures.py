"""
Q167: Daily Temperatures (Monotonic Stack)
============================================
Problem: Given temperatures array, return array where answer[i] is
number of days you have to wait for a warmer temperature. 0 if no future.

Example:
    [73,74,75,71,69,72,76,73] -> [1,1,4,2,1,1,0,0]
"""

def daily_temperatures(temperatures):
    result = [0] * len(temperatures)
    stack = []  # Stores indices
    for i, temp in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < temp:
            idx = stack.pop()
            result[idx] = i - idx
        stack.append(i)
    return result

if __name__ == "__main__":
    print(daily_temperatures([73,74,75,71,69,72,76,73]))  # [1,1,4,2,1,1,0,0]
    print(daily_temperatures([30,40,50,60]))               # [1,1,1,0]
