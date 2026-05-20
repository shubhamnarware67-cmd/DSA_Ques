"""
Q194: Expression Add Operators (Backtracking)
===============================================
Problem: Given string num and integer target, add +, -, * between digits
to get expressions that equal target. Return all such expressions.

Example:
    num="123", target=6 -> ["1+2+3","1*2*3"]
    num="232", target=8 -> ["2*3+2","2+3*2"]
"""

def add_operators(num, target):
    result = []
    def backtrack(idx, path, val, prev):
        if idx == len(num):
            if val == target:
                result.append(path)
            return
        for i in range(idx, len(num)):
            curr_str = num[idx:i+1]
            if len(curr_str) > 1 and curr_str[0] == '0':
                break
            curr = int(curr_str)
            if idx == 0:
                backtrack(i+1, curr_str, curr, curr)
            else:
                backtrack(i+1, path+'+'+curr_str, val+curr, curr)
                backtrack(i+1, path+'-'+curr_str, val-curr, -curr)
                backtrack(i+1, path+'*'+curr_str, val-prev+prev*curr, prev*curr)
    backtrack(0, "", 0, 0)
    return result

if __name__ == "__main__":
    print(add_operators("123", 6))   # ["1+2+3","1*2*3"]
    print(add_operators("232", 8))   # ["2*3+2","2+3*2"]
    print(add_operators("3456237490", 9191))  # []
