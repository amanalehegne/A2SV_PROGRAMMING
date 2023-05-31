class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        def isValidPath(row, col):
            return 0 <= row < m and 0 <= col < n

        
        grid = [[0 for _ in range(n)] for _ in range(m)]
        grid[0][0] = 1    
        
        for row in range(m):
            for col in range(n):
                rowVal = colVal = 0
                if isValidPath(row - 1, col):
                    rowVal = grid[row - 1][col]
                if isValidPath(row, col - 1):
                    colVal = grid[row][col - 1]
    
                grid[row][col] += rowVal + colVal
                
        return grid[-1][-1]