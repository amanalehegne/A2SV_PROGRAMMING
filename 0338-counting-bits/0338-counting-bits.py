class Solution:
    def countBits(self, n: int) -> List[int]:
        def bitCounter(y):
            tmp = 1
            res = 0
            for i in range(17):
                x = (y & tmp)
                if x:
                    res += 1
                tmp = tmp << 1
            
            return res
        
        res = []
        for i in range(n + 1):
            res.append(bitCounter(i))
        
        return res