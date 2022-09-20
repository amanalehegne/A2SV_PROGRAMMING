class Solution:
    def ans(self, n, map):
        if n == 0 or n == 1:
            return n
        if map.get(n):
            return map[n]
        else:
            map[n] = self.ans(n - 1, map) + self.ans(n - 2, map)
        return map[n]
    
    def fib(self, n: int) -> int:
        map = {}
        return self.ans(n, map)
        