"""
Q445: Tag Validator / Expression Validator (Stack-Based)
=============================================================
Problem: Validate if a string is a valid HTML-like tag structure.

Example:
    "<DIV>This is the first line <![CDATA[<div>]]></DIV>" -> True
    "<DIV>>>  </DIV>" -> True
    "<A>  <B> </A>   </B>" -> False
"""

def is_valid(code):
    stack = []
    i = 0
    n = len(code)
    if not code.startswith('<') or not code.endswith('>'):
        return False

    while i < n:
        if code[i] == '<':
            if i+1 < n and code[i+1] == '/':
                # Closing tag
                j = code.find('>', i)
                if j == -1: return False
                tag_name = code[i+2:j]
                if not tag_name or not stack or stack[-1] != tag_name:
                    return False
                stack.pop()
                i = j + 1
                if not stack and i != n: return False
            elif i+1 < n and code[i+1] == '!':
                # CDATA
                if not stack: return False
                if not code[i:].startswith('<![CDATA['): return False
                j = code.find(']]>', i)
                if j == -1: return False
                i = j + 3
            else:
                # Opening tag
                j = code.find('>', i)
                if j == -1: return False
                tag_name = code[i+1:j]
                if not (1 <= len(tag_name) <= 9) or not tag_name.isupper():
                    return False
                stack.append(tag_name)
                i = j + 1
        else:
            if not stack: return False
            i += 1
    return not stack

if __name__ == "__main__":
    print(is_valid("<DIV>This is the first line <![CDATA[<div>]]></DIV>"))  # True
    print(is_valid("<A>  <B> </A>   </B>"))  # False
