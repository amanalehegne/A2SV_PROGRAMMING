class Solution:
    def fib(self, n: int) -> int:
        arr = [1, 1]
        if n == 0 or n == 1: return n

        def rec(n):
            if n - 2 == 0:
                return
            cur = arr[-1] + arr[-2]
            arr.append(cur)
            rec(n - 1)

        rec(n)
        return arr[-1]
        