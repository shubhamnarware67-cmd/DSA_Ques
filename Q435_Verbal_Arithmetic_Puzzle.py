"""
Q435: Verbal Arithmetic Puzzle (Backtracking + Constraints)
=============================================================
Problem: Solve word equation like SEND + MORE = MONEY where each letter
maps to a unique digit (0-9), leading digit can't be 0.

Example:
    words=["SEND","MORE"], result="MONEY" -> True
    words=["SIX","SEVEN","SEVEN"], result="TWENTY" -> True
"""

def is_solvable(words, result):
    all_words = words + [result]
    chars = set(''.join(all_words))
    if len(chars) > 10: return False

    leading = {w[0] for w in all_words if len(w) > 1}
    chars_list = list(chars)
    assignment = {}
    used_digits = [False] * 10

    def backtrack(idx):
        if idx == len(chars_list):
            # Verify equation
            def word_val(w):
                return int(''.join(str(assignment[c]) for c in w))
            return sum(word_val(w) for w in words) == word_val(result)
        c = chars_list[idx]
        for d in range(10):
            if used_digits[d]: continue
            if d == 0 and c in leading: continue
            assignment[c] = d
            used_digits[d] = True
            if backtrack(idx+1): return True
            used_digits[d] = False
            del assignment[c]
        return False

    return backtrack(0)

if __name__ == "__main__":
    print(is_solvable(["SEND","MORE"], "MONEY"))  # True
    print(is_solvable(["SIX","SEVEN","SEVEN"], "TWENTY"))  # True
    print(is_solvable(["LEET","CODE"], "POINT"))  # False
