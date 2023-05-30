class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def isValidPath(m, n, r, c):
            return (0 <= r < m) and (0 <= c < n)
            
        dir_ = [(1, 0), (0, 1)]
        
        def rec(m, n, r, c, dic):
            if r == m - 1 and c == n - 1:
                return 1
            
            if (r, c) in dic:
                return dic[(r, c)]
            
            total = 0
            for row, col in dir_:
                if isValidPath(m, n, r + row, c + col):
                    val = rec(m, n, r + row, c + col, dic)
                    total += val
            
            dic[(r, c)] = total
            return dic[(r, c)]
        
        return rec(m, n, 0, 0, dict())
                
                    
                