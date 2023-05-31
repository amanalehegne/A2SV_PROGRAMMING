class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        def isValidPosition(grid, node):
            return 0 <= node[0] < len(grid) and 0 <= node[1] < len(grid[0])

        
        grid = [[0 for _ in range(n)] for _ in range(m)]
        grid[0][0] = 1    
        
        for row in range(m):
            for col in range(n):
                rowVal = colVal = 0
                if isValidPosition(grid, (row, col - 1)):
                    colVal = grid[row][col - 1]
                if isValidPosition(grid, (row - 1, col)):
                    rowVal = grid[row - 1][col]
    
                grid[row][col] += rowVal + colVal
                
        return grid[-1][-1]