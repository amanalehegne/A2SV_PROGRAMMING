class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        def findFirstOne(rows, cols):
            for row in range(rows):
                for col in range(cols):
                    if grid[row][col] == 1:
                        return [row, col]
        
        row, col = findFirstOne(rows, cols)
        
        direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def check(row, col):
            cols = 0 <= col < len(grid[0])
            rows = 0 <= row < len(grid)
            return cols and rows
    
        seen = set()
        
        def dfs(row, col):
            
            seen.add((row, col))
            count = 0

            for row_, col_ in direction:
                newRow = row + row_
                newCol = col + col_
                validate = check(newRow, newCol)
                
                if not validate or grid[newRow][newCol] == 0:
                    count += 1
                elif validate and (newRow, newCol) not in seen and grid[newRow][newCol] == 1:
                    count += dfs(newRow, newCol)
            
            return count
        
        return dfs(row, col)