"""
Q91: Letter Combinations of Phone Number (Backtracking)
========================================================
Problem: Given a string of digits 2-9, return all possible letter
combinations (like phone keypad).

Example:
    "23" -> ["ad","ae","af","bd","be","bf","cd","ce","cf"]
"""

def letter_combinations(digits):
    if not digits: return []
    phone = {'2':'abc','3':'def','4':'ghi','5':'jkl',
             '6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
    result = []
    def backtrack(index, current):
        if index == len(digits):
            result.append(current)
            return
        for char in phone[digits[index]]:
            backtrack(index + 1, current + char)
    backtrack(0, "")
    return result

if __name__ == "__main__":
    print(letter_combinations("23"))  # ["ad","ae","af","bd","be","bf","cd","ce","cf"]
    print(letter_combinations(""))    # []
