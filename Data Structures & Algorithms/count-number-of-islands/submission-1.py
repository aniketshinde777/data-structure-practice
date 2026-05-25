class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(row, col):            
            if (row < 0 or
                row >= ROWS or
                col <0 or
                col >= COLS):
                return

            if grid[row][col] == "0":
                return

            if grid[row][col] == "1":
                grid[row][col] = "0"
                dfs(row + 1, col)
                dfs(row - 1, col)
                dfs(row, col + 1)
                dfs(row, col - 1)

        total_no_islands = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1":
                    total_no_islands += 1
                    dfs(i, j)

        return total_no_islands