"""
Q173: Decode String (Stack)
=============================
Problem: Decode an encoded string. k[encoded_string] means the encoded_string
is repeated k times.

Example:
    "3[a]2[bc]"     -> "aaabcbc"
    "3[a2[c]]"      -> "accaccacc"
    "2[abc]3[cd]ef" -> "abcabccdcdcdef"
"""

def decode_string(s):
    stack = []
    current_str = ""
    current_num = 0
    for ch in s:
        if ch.isdigit():
            current_num = current_num * 10 + int(ch)
        elif ch == '[':
            stack.append((current_str, current_num))
            current_str = ""; current_num = 0
        elif ch == ']':
            prev_str, num = stack.pop()
            current_str = prev_str + num * current_str
        else:
            current_str += ch
    return current_str

if __name__ == "__main__":
    print(decode_string("3[a]2[bc]"))      # "aaabcbc"
    print(decode_string("3[a2[c]]"))       # "accaccacc"
    print(decode_string("2[abc]3[cd]ef"))  # "abcabccdcdcdef"
