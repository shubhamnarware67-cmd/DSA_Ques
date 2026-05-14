"""
Q174: Simplify Path (Stack)
=============================
Problem: Given absolute Unix path string, simplify it.
'..' = go up one level, '.' = stay, '//' = single slash.

Example:
    "/home/"           -> "/home"
    "/../"             -> "/"
    "/home//foo/"      -> "/home/foo"
    "/a/./b/../../c/"  -> "/c"
"""

def simplify_path(path):
    stack = []
    for part in path.split('/'):
        if part == '..':
            if stack: stack.pop()
        elif part and part != '.':
            stack.append(part)
    return '/' + '/'.join(stack)

if __name__ == "__main__":
    print(simplify_path("/home/"))             # "/home"
    print(simplify_path("/../"))               # "/"
    print(simplify_path("/home//foo/"))        # "/home/foo"
    print(simplify_path("/a/./b/../../c/"))    # "/c"
