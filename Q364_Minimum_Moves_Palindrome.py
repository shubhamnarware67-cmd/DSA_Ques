"""
Q364: Minimum Number of Moves to Make Palindrome (Greedy)
=========================================================
Problem: Only adjacent swaps allowed. Find min swaps to make string palindrome.

Example:
    "aabb" -> 2
    "letelt" -> 2
"""

def min_moves_to_make_palindrome(s):
    s = list(s)
    moves = 0
    left, right = 0, len(s)-1
    while left < right:
        if s[left] == s[right]:
            left += 1; right -= 1
        else:
            # Find match for s[left] from right side
            k = right
            while k > left and s[k] != s[left]: k -= 1
            if k == left:
                # s[left] has no match — it's the middle element
                s[left], s[left+1] = s[left+1], s[left]
                moves += 1
            else:
                # Bring s[k] to position right
                while k < right:
                    s[k], s[k+1] = s[k+1], s[k]
                    k += 1; moves += 1
                left += 1; right -= 1
    return moves

if __name__ == "__main__":
    print(min_moves_to_make_palindrome("aabb"))    # 2
    print(min_moves_to_make_palindrome("letelt"))  # 2
    print(min_moves_to_make_palindrome("ntiin"))   # 1
