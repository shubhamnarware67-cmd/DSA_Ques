"""
Q349: Design In-Memory File System
=====================================
Problem: Implement mkdir, addContentToFile, readContentFromFile, ls.

Example:
    ls("/") -> []
    mkdir("/a/b/c")
    addContentToFile("/a/b/c/d", "hello")
    ls("/") -> ["a"]
    readContentFromFile("/a/b/c/d") -> "hello"
"""

class FileSystem:
    def __init__(self):
        self.dirs = {'': {'children': {}, 'content': ''}}

    def _traverse(self, path):
        parts = path.split('/')[1:]  # Skip empty first element
        node = self.dirs['']
        for p in parts:
            if p and p not in node['children']:
                node['children'][p] = {'children': {}, 'content': ''}
            if p: node = node['children'][p]
        return node

    def ls(self, path):
        node = self._traverse(path)
        if node['content']:  # It's a file
            return [path.split('/')[-1]]
        return sorted(node['children'].keys())

    def mkdir(self, path):
        self._traverse(path)

    def addContentToFile(self, path, content):
        node = self._traverse(path)
        node['content'] += content

    def readContentFromFile(self, path):
        return self._traverse(path)['content']

if __name__ == "__main__":
    fs = FileSystem()
    print(fs.ls("/"))                         # []
    fs.mkdir("/a/b/c")
    fs.addContentToFile("/a/b/c/d", "hello")
    print(fs.ls("/"))                         # ["a"]
    print(fs.readContentFromFile("/a/b/c/d")) # "hello"
