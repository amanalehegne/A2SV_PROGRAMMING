class Solution:
    def mySqrt(self, x: int) -> int:
        """
        1, 2, 3, 4
        
        """
        if x == 1: return 1
        left = 0
        right = x // 2
        while left <= right:
            midPoint = left + (right - left) // 2
            sqrVal = midPoint ** 2
            
            if sqrVal < x:
                left = midPoint + 1
            elif sqrVal > x:
                right = midPoint - 1
            else:
                return midPoint
        
        if right ** 2 <= x: return right
        else: return left
                
        