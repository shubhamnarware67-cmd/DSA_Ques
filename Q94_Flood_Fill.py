"""
Q94: Flood Fill (DFS/BFS)
===========================
Problem: Given image (2D array), starting pixel (sr,sc), and color,
flood fill the image starting from that pixel.

Example:
    image=[[1,1,1],[1,1,0],[1,0,1]], sr=1, sc=1, color=2
    Output: [[2,2,2],[2,2,0],[2,0,1]]
"""

def flood_fill(image, sr, sc, color):
    orig_color = image[sr][sc]
    if orig_color == color:
        return image

    def dfs(r, c):
        if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]):
            return
        if image[r][c] != orig_color:
            return
        image[r][c] = color
        dfs(r+1,c); dfs(r-1,c); dfs(r,c+1); dfs(r,c-1)

    dfs(sr, sc)
    return image

if __name__ == "__main__":
    img = [[1,1,1],[1,1,0],[1,0,1]]
    result = flood_fill(img, 1, 1, 2)
    for row in result: print(row)
    # [2,2,2], [2,2,0], [2,0,1]
