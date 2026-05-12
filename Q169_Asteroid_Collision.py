"""
Q169: Asteroid Collision (Stack)
==================================
Problem: Array of asteroids moving right (+) or left (-). Same size = both
explode. Find final state after all collisions.

Example:
    [5,10,-5]   -> [5,10]
    [8,-8]      -> []
    [10,2,-5]   -> [10]
"""

def asteroid_collision(asteroids):
    stack = []
    for a in asteroids:
        alive = True
        while alive and a < 0 and stack and stack[-1] > 0:
            if stack[-1] < -a:
                stack.pop()
            elif stack[-1] == -a:
                stack.pop(); alive = False
            else:
                alive = False
        if alive:
            stack.append(a)
    return stack

if __name__ == "__main__":
    print(asteroid_collision([5,10,-5]))   # [5,10]
    print(asteroid_collision([8,-8]))      # []
    print(asteroid_collision([10,2,-5]))   # [10]
    print(asteroid_collision([-2,-1,1,2])) # [-2,-1,1,2]
