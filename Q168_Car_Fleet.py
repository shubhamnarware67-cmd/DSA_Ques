"""
Q168: Car Fleet (Monotonic Stack)
===================================
Problem: n cars drive to target. car[i] at position[i] with speed[i].
Cars can catch up but can't pass — they form a fleet. Count fleets.

Example:
    target=12, position=[10,8,0,5,3], speed=[2,4,1,1,3] -> 3
"""

def car_fleet(target, position, speed):
    pairs = sorted(zip(position, speed), reverse=True)
    stack = []
    for pos, spd in pairs:
        time = (target - pos) / spd
        if not stack or time > stack[-1]:
            stack.append(time)
    return len(stack)

if __name__ == "__main__":
    print(car_fleet(12, [10,8,0,5,3], [2,4,1,1,3]))  # 3
    print(car_fleet(10, [3], [3]))                     # 1
    print(car_fleet(100, [0,2,4], [4,2,1]))            # 1
