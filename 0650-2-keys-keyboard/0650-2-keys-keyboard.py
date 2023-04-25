class Solution:
    def minSteps(self, n: int) -> int:
        cur = 1
        count = 0
        factor = 0
        
        while cur < n:
            remain = n - cur
            if remain % cur == 0:
                factor = cur
                count += 1
            cur += factor
            count += 1
        
        return count
            
            
            
            
            
            
            
            