class Solution:
    def tribonacci(self, n: int) -> int:
        def rec(n, dic):
            if n == 0:
                return 0
            if n < 3:
                return 1
            
            if n in dic:
                return dic[n]
            dic[n] = rec(n - 1, dic) + rec(n - 2, dic) + rec(n - 3, dic)
            return dic[n]
        
        return rec(n, dict())