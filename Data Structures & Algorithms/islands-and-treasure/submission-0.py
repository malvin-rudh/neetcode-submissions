class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        ## Brute Force Idea: Do BFS for each cell trying to find the treasure chest. However, this costs O((nm)^2)
        # What we can think of is actually to do BFS from each of the treasure chest and in the worst case, this would be O(knm)

        DIR =[[-1, 0], [0, 1], [1, 0], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        INF = 2147483647

        
        queue = deque()
        visited = set()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append((r, c))
        
        curr_dist = 0

        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()

                grid[row][col] = min(grid[row][col], curr_dist)

                for dr, dc in DIR:
                    new_row = row + dr
                    new_col = col + dc

                    if new_row >= 0 and new_row < ROWS and new_col >= 0 and new_col < COLS and (new_row, new_col) not in visited and grid[new_row][new_col] == INF:
                        visited.add((new_row, new_col))
                        queue.append((new_row, new_col))


            curr_dist += 1

                

 
            

        
        

        

        