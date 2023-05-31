class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
    
        prev = [0] * n
        current = [0] * n
        current[0] = 1

        for row in range(m):
            for col in range(n):
                rowVal = colVal = 0
                rowVal = prev[col]
                if 0 <= col - 1 < n:
                    colVal = current[col - 1]

                current[col] += rowVal + colVal
            
            if row == m - 1:
                return current[-1]
            prev = current
            current = [0] * n
        
        return -1
                