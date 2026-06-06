"""
Q255: Design File System (Trie-based)
======================================
Problem: Implement a file system that creates paths and assigns values.
createPath(path, value) -> True/False, get(path) -> value or -1.

Example:
    createPath("/leet", 1)       -> True
    createPath("/leet/code", 2)  -> True
    get("/leet/code")            -> 2
    createPath("/leet/code", 3)  -> False (already exists)
"""

class FileSystem:
    def __init__(self):
        self.paths = {'/': -1}

    def createPath(self, path, value):
        if path in self.paths: return False
        parent = path[:path.rfind('/')]
        if parent and parent not in self.paths: return False
        self.paths[path] = value
        return True

    def get(self, path):
        return self.paths.get(path, -1)

if __name__ == "__main__":
    fs = FileSystem()
    print(fs.createPath("/leet", 1))       # True
    print(fs.createPath("/leet/code", 2))  # True
    print(fs.get("/leet/code"))            # 2
    print(fs.createPath("/leet/code", 3))  # False
    print(fs.get("/leet"))                 # 1
