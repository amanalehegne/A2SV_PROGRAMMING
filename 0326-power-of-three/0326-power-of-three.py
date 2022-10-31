class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while True:
            if n == 1 or n == 3:
                return True
            if n < 3:
                return False
            n /= 3