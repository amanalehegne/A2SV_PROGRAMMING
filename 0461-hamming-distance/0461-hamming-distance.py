class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        res = 0
        
        while x or y:
            xVal = x & 1
            yVal = y & 1
            if xVal != yVal:
                res += 1
            x >>= 1
            y >>= 1
            
        return res
        