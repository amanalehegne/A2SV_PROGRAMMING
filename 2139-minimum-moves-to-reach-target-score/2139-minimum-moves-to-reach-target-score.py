class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        res = 0
        while target > 1 and maxDoubles > 0:
            res += (target%2 + 1)
            target //= 2
            maxDoubles -= 1
        
        return res + target - 1