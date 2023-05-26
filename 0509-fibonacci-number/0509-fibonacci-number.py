class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n < 3:
            return 1
        prev = 1
        nxt = 1
        n -= 2
        while n:
            val = prev + nxt
            prev = nxt
            nxt = val
            n -= 1
        
        return val