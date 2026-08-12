class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        num_islands = 0
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return

            directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            if grid[r][c] == '1':
                grid[r][c] = '#'
                for dir in directions:
                    dfs(r + dir[0], c + dir[1])
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    num_islands += 1
                    dfs(r, c)
        return num_islands