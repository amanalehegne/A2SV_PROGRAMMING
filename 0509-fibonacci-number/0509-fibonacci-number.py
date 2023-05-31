class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        one, two = 0, 1
        for i in range(n - 1):
            current = two + one
            one = two
            two = current
        
        return two
        