class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
            Do DFS on every coordinate and see if you can reach both the pacific and atlantic ocean
            
            An alternative smarter approach is to realize that the borders of the atlantic ocean can reach the atlantic ocean and similarly the borders of the pacific ocean can reach the pacific ocean.
            Knowing this, we can run DFS for each of the border cells of both the atlantic and pacific ocean while maintaining a visited set of these 2 separately
            When done, we can take the coordinates that appears in both visited sets
        """
        
        ROWS, COLS = len(heights), len(heights[0])
        visited_atlantic = set()
        visited_pacific = set()

        def dfs(row, col, visit, prev_height):
            if (row, col) not in visit and row >= 0 and col >= 0 and row < ROWS and col < COLS and heights[row][col] >= prev_height:
                visit.add((row, col))
                dfs(row+1, col, visit, heights[row][col])
                dfs(row-1, col, visit, heights[row][col])
                dfs(row, col+1, visit, heights[row][col])
                dfs(row, col-1, visit, heights[row][col])

        
        for i in range(COLS):
            dfs(0, i, visited_pacific, heights[0][i])
            dfs(ROWS-1, i, visited_atlantic, heights[ROWS-1][i])

        for i in range(ROWS):
            dfs(i, 0, visited_pacific, heights[i][0])
            dfs(i, COLS-1, visited_atlantic, heights[i][COLS-1])

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in visited_atlantic and (r, c) in visited_pacific:
                    res.append([r, c])
        return res

        