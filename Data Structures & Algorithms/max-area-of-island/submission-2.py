class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        
        def dfs(r, c):
            if r < 0 or r == rows or c < 0 or c == cols or (r, c) in visited or grid[r][c] == 0:
                return 0
            
            visited.add((r, c))
            dirs = [[0, -1], [0, 1], [1, 0], [-1, 0]]
            area = 1
            for d in dirs:
                area += dfs(r + d[0], c + d[1])
            return area
        
        area = 0
        for i in range(rows):
            for j in range(cols):
                area = max(area, dfs(i, j))

        return area