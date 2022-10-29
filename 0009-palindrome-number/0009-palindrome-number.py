class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        x = str(x)
        l, r = 0, len(x) - 1
        while l < r and x[l] == x[r]:
            r -= 1
            l += 1
        if l >= r:
            return True
        return False