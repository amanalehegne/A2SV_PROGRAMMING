# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 0
        right = n - 1
        while left <= right:
            midPoint = left + (right - left) // 2
            if not isBadVersion(midPoint):
                left = midPoint + 1
            else:
                right = midPoint - 1
        
        return left
            
            
        