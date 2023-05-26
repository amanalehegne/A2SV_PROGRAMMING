class Solution:
    def climbStairs(self, n: int) -> int:
        def rec(n, dic):
            if n == 1 or n == 0:
                return 1
            if dic.get(n):
                return dic[n]
            
            dic[n] = rec(n - 1, dic) + rec(n - 2, dic)
            return dic[n]
        
        return rec(n, dict())
        