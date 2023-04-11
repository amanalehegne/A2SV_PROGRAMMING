class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def check(row, col):
            cols = 0 <= col < len(grid[0])
            rows = 0 <= row < len(grid)
            return cols and rows
    
        seen = set()
        
        def dfs(row, col):
            
            seen.add((row, col))
            grid[row][col] = 0

            for row_, col_ in direction:
                newRow = row + row_
                newCol = col + col_
                validate = check(newRow, newCol)
            
                if validate and grid[newRow][newCol] == "1" and (newRow, newCol) not in seen:
                    dfs(newRow, newCol)
                    
                    
                
        rows = len(grid)
        cols = len(grid[0])
        res = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    dfs(row, col)
                    res += 1
        return res