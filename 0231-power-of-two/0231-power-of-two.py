class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if not n:
            return n
        return not n & (n - 1)