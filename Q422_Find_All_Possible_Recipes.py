"""
Q422: Find All Possible Recipes from Given Supplies (Topological Sort)
=========================================================================
Problem: Recipes need ingredients (could be other recipes). Given supplies,
return all recipes you can make.

Example:
    recipes=["bread"], ingredients=[["yeast","flour"]], supplies=["yeast","flour","corn"]
    -> ["bread"]
"""
from collections import defaultdict, deque

def find_all_recipes(recipes, ingredients, supplies):
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    recipe_set = set(recipes)

    for recipe, ings in zip(recipes, ingredients):
        for ing in ings:
            graph[ing].append(recipe)
            in_degree[recipe] += 1

    queue = deque(supplies)
    result = []
    made = set()

    while queue:
        item = queue.popleft()
        for recipe in graph[item]:
            in_degree[recipe] -= 1
            if in_degree[recipe] == 0:
                made.add(recipe)
                result.append(recipe)
                queue.append(recipe)

    return result

if __name__ == "__main__":
    print(find_all_recipes(["bread"], [["yeast","flour"]], ["yeast","flour","corn"]))
    # ["bread"]
    print(find_all_recipes(["bread","sandwich"],
                           [["yeast","flour"],["bread","meat"]],
                           ["yeast","flour","meat"]))
    # ["bread","sandwich"]
