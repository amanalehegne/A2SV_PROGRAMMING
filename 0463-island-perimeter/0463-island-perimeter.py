class Solution:
    def findFirstOne(self, grid):
            rows = len(grid)
            cols = len(grid[0])
        
            for row in range(rows):
                for col in range(cols):
                    if grid[row][col] == 1:
                        return [row, col]
                    
                    
    def check(self, row, col, grid):
        cols = 0 <= col < len(grid[0])
        rows = 0 <= row < len(grid)
        return cols and rows
        
    def dfs(self, row, col, direction, grid, seen):

        seen.add((row, col))
        count = 0

        for row_, col_ in direction:
            newRow = row + row_
            newCol = col + col_
            validate = self.check(newRow, newCol, grid)

            if not validate or grid[newRow][newCol] == 0:
                count += 1
            elif validate and (newRow, newCol) not in seen and grid[newRow][newCol] == 1:
                count += self.dfs(newRow, newCol, direction, grid, seen)

        return count
                    
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        row, col = self.findFirstOne(grid)
        
        direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        seen = set()
        
        return self.dfs(row, col, direction, grid, seen)