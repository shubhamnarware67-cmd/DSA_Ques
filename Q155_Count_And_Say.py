"""
Q155: Count and Say
====================
Problem: The count-and-say sequence:
1 -> "1"
2 -> "11"  (one 1)
3 -> "21"  (two 1s)
4 -> "1211" (one 2, one 1)
5 -> "111221"

Example:
    n=1 -> "1"
    n=4 -> "1211"
"""

def count_and_say(n):
    result = "1"
    for _ in range(n - 1):
        new_result = ""
        i = 0
        while i < len(result):
            char = result[i]
            count = 1
            while i + count < len(result) and result[i + count] == char:
                count += 1
            new_result += str(count) + char
            i += count
        result = new_result
    return result

if __name__ == "__main__":
    for i in range(1, 7):
        print(f"n={i}: {count_and_say(i)}")
