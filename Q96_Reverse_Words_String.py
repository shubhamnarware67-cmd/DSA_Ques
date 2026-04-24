"""
Q96: Reverse Words in a String
================================
Problem: Given string s, reverse the order of words.
Words are separated by spaces; result should not have leading/trailing spaces.

Example:
    "the sky is blue"    -> "blue is sky the"
    "  hello world  "    -> "world hello"
    "a good   example"   -> "example good a"
"""

def reverse_words(s):
    return ' '.join(s.split()[::-1])

def reverse_words_manual(s):
    words = []
    word = ""
    for char in s:
        if char != ' ':
            word += char
        elif word:
            words.append(word)
            word = ""
    if word:
        words.append(word)
    return ' '.join(reversed(words))

if __name__ == "__main__":
    print(reverse_words("the sky is blue"))    # "blue is sky the"
    print(reverse_words("  hello world  "))    # "world hello"
    print(reverse_words_manual("a good   example"))  # "example good a"
