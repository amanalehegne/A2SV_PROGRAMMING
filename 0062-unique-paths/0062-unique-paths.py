class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        def isValidPosition(node):
            return 0 <= node[0] < m and 0 <= node[1] < n

        def dp(state, memo):
            row, col = state
            
            if row == 0 and col == 0:
                return 1
            
            if state in memo:
                return memo[state]
            
            rowVal = colVal = 0
            if isValidPosition((row - 1, col)):
                rowVal += dp((row - 1, col), memo)
            if isValidPosition((row, col - 1)):
                colVal += dp((row, col - 1), memo)
            
            memo[state] = rowVal + colVal
            return memo[state]
        
        return dp((m - 1, n - 1), dict())