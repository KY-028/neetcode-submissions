class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])

        fresh = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1


        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        if fresh == 0:
            return 0

        time = 0

        while fresh > 0:
            flag = False # to track if no fruits can be rotten further
            
            for i in range(rows):
                for j in range(cols):
                    if grid[i][j] == 2:
                        # corrupt neighbours
                        for d in dirs:
                            r, c = i + d[0], j + d[1]
                            if r < 0 or r == rows or c < 0 or c == cols or grid[r][c] != 1:
                                continue
                            grid[r][c] = 3
                            fresh -= 1
                            flag = True
            if not flag:
                return -1 # no more rotten
            
            for i in range(rows):
                for j in range(cols):
                    if grid[i][j] == 3:
                        grid[i][j] = 2
            time += 1
        return time