class Solution:
    def countBits(self, n: int) -> List[int]:
        
        def bitCounter(y):
            res = 0
            for i in range(17):
                res += (y & 1)
                y = y >> 1
            
            return res
        
        res = []
        for i in range(n + 1):
            res.append(bitCounter(i))
        
        return res