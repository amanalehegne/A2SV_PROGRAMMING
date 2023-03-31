class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        prev = None
        while n:
            val = min(1, n & 1)
            if prev is not None and val == prev:
                return False
            prev = val
            n >>= 1
        
        return True
            
        