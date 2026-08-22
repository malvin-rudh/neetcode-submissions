class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
            # Idea is you want to always explore the cell where there is a 1 because this indicates a land,
            # then once you get a 1, you would then want to explore all the connecting ones, and then stop and count this as 1 island

            DIR = [[-1, 0], [0, 1], [1, 0], [0, -1]]
            ROWS = len(grid)
            COLS = len(grid[0])
            islands = 0

            def dfs(row, col):

                if grid[row][col] == "1":
                    grid[row][col] = 0
                    for direction in DIR:
                        dr, dc = direction
                        new_row = row + dr
                        new_col = col + dc
                        if new_row >= 0 and new_row < ROWS and new_col >= 0 and new_col < COLS:
                            dfs(new_row, new_col)
                
                return

            
            for r in range(ROWS):
                for c in range(COLS):
                    if grid[r][c] == "1":
                        dfs(r, c)
                        islands += 1
            
            return islands