class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        ROWS, COLS = len(board), len(board[0])
        visit = set()

        def dfs(r, c):
            if (r, c) in visit or r < 0 or r >= ROWS or c < 0 or c >= COLS or board[r][c] == 'X':
                return 
            visit.add((r, c))
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        for r in range(ROWS):
            dfs(r, 0)
            dfs(r, COLS-1)
        for c in range(COLS):
            dfs(0, c)
            dfs(ROWS-1, c)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O' and (r, c) not in visit:
                    board[r][c] = 'X'
        