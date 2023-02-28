class Solution:
    def memo(self, n, dic):
        if n == 0 or n == 1:
            return n
        if dic.get(n):
            return dic[n]
        else:
            dic[n] = self.memo(n - 1, dic) + self.memo(n - 2, dic)
            return dic[n]
        
    def fib(self, n: int) -> int:
        dic = dict()
        return self.memo(n, dic)
        